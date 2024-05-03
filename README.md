# Copyist

This Python script allows you to synchronize two paths using the `rsync` command, skipping `node_modules` directories and symlinks. It provides options for performing a dry run to simulate the synchronization operation.

## Prerequisites

- Python 3.x
- `rsync` command-line utility

## Usage

1. Clone or download this repository to your local machine.
2. Set up your source and destination paths:
    - Define environment variables `SOURCE_PATH` and `DESTINATION_PATH` with the paths to your source and destination paths respectively.
3. Run the script using Python 3:

    ```bash
    python3 app.py [--dry-run]
    ```

    - `--dry-run`: Perform a dry run (simulation) of the synchronization operation.

    If you need to execute the script with elevated privileges (e.g., `sudo`) to access certain folders or files in the source path, ensure that the environment variables are passed to the script using the `-E` or `--preserve-env` option:

    ```bash
    sudo -E python3 app.py --dry-run
    ```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
