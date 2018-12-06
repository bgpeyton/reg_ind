import sys
txt = sys.argv[1:][0]
msg = ""
for l in txt:
    if l == " ":
        msg += "  "
    else:
        msg += ":regional_indicator_" + l.lower() + ": "
print("Original message:\n{}".format(txt))
print("Formatted message:\n{}".format(msg))
