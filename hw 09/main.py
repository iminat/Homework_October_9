import re
result = re.match(r'AV', 'AV Analytics Vidhya AV')
result = result.group(0)

print(result)
