from pages.base_page import BasePage
import os
import test_find 
import json

class WriteFile(BasePage):
    def write_info_file(info_list):
        info = json.dumps(info_list)
        info_file = open(f"{test_find.value}.json", "w")
        info_file.write(info)
        info_file.close()   
        
    def should_be_json_file():
        assert os.path.exists(f'{test_find.value}.json'), 'File not found'

    def should_be_json_file_not_empty():
        assert os.stat(f'{test_find.value}.json').st_size > 0, 'File empty'

