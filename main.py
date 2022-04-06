from enabler import enabler_self_test
from generate_html import generate_html
from generate_md import generate_md

if __name__ == '__main__':
    enabler_self_test()
    generate_md()
    generate_html()
