import sys
txt = sys.argv[1:][0]

if len(sys.argv) > 2:
    print2k = sys.argv[2].lower() == 'true'
else:
    print2k = True

msg = ""
for l in txt:
    if l == " ": # catch and double spaces
        msg += "  "
    elif l.isalpha(): # catch only letters
        msg += ":regional_indicator_" + l.lower() + ": "
    else: # leave it alone
        msg += l

print("Original message:\n{}".format(txt))

if (len(msg) > 2000) and print2k: # cut to 2k and drop last letter (probably incomplete)
    print("Message too long for Discord! Cutting it down to size...")
    print("Formatted message:\n{}".format(msg[0:2000].rsplit(' ',1)[0]))
else:
    print("Formatted message:\n{}".format(msg))
