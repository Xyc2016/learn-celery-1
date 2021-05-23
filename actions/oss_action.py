import oss2
from oss_utils.bucket import learn_oss_bucket


class OssAction:
    def __init__(self) -> None:
        self._bucket = learn_oss_bucket

    def get_page_files(self, page_no: int, page_size: int) -> list:
        pass
