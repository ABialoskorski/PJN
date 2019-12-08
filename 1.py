import re

file2 = '<a href="/2813270"   data-reviewshref="" class="go-to-product js_conv js_clickHash js_seoUrl" data-source-tag=""> Makita GA5030</a>'
data = file2
znalezione = re.findall(r'<a href="/[0-9]+"   data-reviewshref="" class="go-to-product js_conv js_clickHash js_seoUrl" data-source-tag=""> [A-Za-z0-9-( )]+</a>',
    str(data))

print(znalezione)
