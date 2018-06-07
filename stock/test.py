from urllib.parse import urlencode
from urllib.parse import quote
import re
company='拉客的搜索'
if re.match('[\u4e00-\u9fa5]', company) and len(company) <= 3:
    print(123)


