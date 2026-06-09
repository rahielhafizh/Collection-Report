import os
import glob
from services.config import logger


def remove_report_lor():
    target_folder = r"D:\EL\SOURCE_MOBCOLL_LOR\WHATSAPP\SUBMISSION"
    if not os.path.exists(target_folder):
        logger.error(f"FOLDER PATH DOES NOT EXIST: {target_folder}")
        return

    search_pattern = os.path.join(target_folder, "*")
    all_items = glob.glob(search_pattern)
    matching_files = [item for item in all_items if os.path.isfile(item)]
    file_count = len(matching_files)

    if file_count > 0:
        logger.info(f"FOUND {file_count} FILES IN TARGET FOLDER")
        deleted_count = 0
        failed_count = 0

        for file_path in matching_files:
            try:
                os.remove(file_path)
                logger.info(f"SUCCESS DELETE {os.path.basename(file_path)}")
                deleted_count += 1
            except Exception as e:
                logger.error(f"FAILED DELETE {os.path.basename(file_path)} | {str(e)}")
                failed_count += 1

        logger.info(f"{deleted_count} FILES DELETED, {failed_count} FILES FAILED")
    else:
        logger.warning("NO FILES FOUND IN TARGET FOLDER")


if __name__ == "__main__":
    remove_report_lor()
