import glob
import os
from services.config import logger
from typing import Dict, List


def scan_files(folder_path: str, pattern: str) -> List[str]:
    matches = glob.glob(os.path.join(folder_path, pattern))
    return [p for p in matches if os.path.isfile(p)]


def purge_files(files: List[str], dry_run: bool) -> Dict[str, int]:
    deleted = failed = 0
    for file_path in files:
        name = os.path.basename(file_path)
        if dry_run:
            logger.info(f"[SYSTEM] DRY RUN – SKIP CLEANER : {name}")
            continue
        try:
            os.remove(file_path)
            logger.info(f"[SYSTEM] CLEANER SUCCESS ON : {name}")
            deleted += 1
        except Exception:
            logger.error(f"[SYSTEM] CLEANER FAILED ON : {name}", exc_info=True)
            failed += 1
    return {"deleted": deleted, "failed": failed}


def log_summary(result: Dict[str, int], dry_run: bool) -> None:
    mode = "DRY RUN" if dry_run else "ACTUAL RUN"
    logger.info(f"[SYSTEM] MODE : {mode}")
    logger.info(f"[SYSTEM] DELETED : {result['deleted']}")
    logger.info(f"[SYSTEM] FAILED : {result['failed']}")


def clean_path(
    target_folder: str,
    filename_pattern: str = "*",
    dry_run: bool = False,
) -> Dict[str, int]:
    if not os.path.isdir(target_folder):
        logger.error(f"[SYSTEM] PATH FOLDER NOT EXIST: {target_folder}")
        return {"deleted": 0, "failed": 0}

    files = scan_files(target_folder, filename_pattern)

    if not files:
        logger.warning(f"[SYSTEM] NO FILES IN FOLDER: {target_folder}")
        return {"deleted": 0, "failed": 0}

    logger.info(f"[SYSTEM] FOUND {len(files)} FILE(S) IN: {target_folder}")
    result = purge_files(files, dry_run=dry_run)
    log_summary(result, dry_run=dry_run)
    return result
