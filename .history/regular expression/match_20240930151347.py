import RE

match = re.search(r'portal', s)


if match:
    print("Start Index : ", match.start())
    print("End Index : ", match.end())
else:
    print("No match found")