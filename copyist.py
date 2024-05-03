import os
import subprocess
import argparse

def rsync_workspace(source_dir, destination_dir, dry_run=False):
    # Exclude symlinks
    exclude_symlinks = [f for f in os.listdir(source_dir) if os.path.islink(os.path.join(source_dir, f))]
    exclude_symlinks = [f'--exclude={os.path.join(source_dir, f)}' for f in exclude_symlinks]

    # Command to sync files using rsync, skipping node_modules directories and symlinks
    rsync_cmd = [
        "rsync",
        "-a",
        "--exclude=node_modules",
        *exclude_symlinks,
        "--update", # Skip files that are newer on the receiving side
        source_dir + "/",  # Include trailing slash to sync the contents of the directory, not the directory itself
        destination_dir
    ]

    # Run rsync command
    try:
        if dry_run:
            rsync_cmd.insert(1, "--dry-run")
        subprocess.run(rsync_cmd, check=True)
        if dry_run:
            print("Dry run completed successfully!")
        else:
            print("Workspace synced successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error syncing workspace: {e}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Sync workspace with rsync")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run (simulation)")
    args = parser.parse_args()

    # Get source and destination directories from environment variables
    source_directory = os.getenv("SOURCE_WORKSPACE")
    destination_directory = os.getenv("DESTINATION_WORKSPACE")

    # Check if environment variables are set
    if source_directory is None or destination_directory is None:
        print("Please set SOURCE_WORKSPACE and DESTINATION_WORKSPACE environment variables.")
        exit(1)

    # Perform rsync
    rsync_workspace(source_directory, destination_directory, args.dry_run)
