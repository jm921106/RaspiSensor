import config

rst = config.byteorder
print rst, 'endian'

rst = config.api_version
print 'Api Version', rst

rst = config.float_info
print(rst)

print('==================path====================')

rst = config.path
for st in rst:
    print st
rst = config.builtin_module_names
for lst in rst:
    print lst
