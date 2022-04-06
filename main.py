from enabler import file_path_from_enabler_name, enabler_self_test
from generate_html import generate_html
from generate_md import generate_md

if __name__ == '__main__':
    print(file_path_from_enabler_name("Connect First"))
    enabler_self_test()
    generate_md()
    generate_html()
