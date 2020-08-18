Takes text and converts it to `:regional_indicator_X:` form, for use as emojis in Discord text chat. 

To run:
`python reg_ind.py "TEXT HERE"`

Only letters are transformed, all other characters are left alone (spaces are doubled). Caps ignored. Messages will be reduced to 2000 characters (to fit into Discord text box). Pass optional third argument `false` to ignore this limitation:
`python reg_ind.py "TEXT HERE" false`
