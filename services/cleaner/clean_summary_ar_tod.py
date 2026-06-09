from services.config import load_config
from services.cleaner.submission_folder_cleaner import clean_path

CONFIG = load_config()


if __name__ == "__main__":
    clean_path(
        target_folder=CONFIG["SUBMISSION_AR_TOD"],
        filename_pattern="*",
        dry_run=False,
    )
