import pathlib, os
file = pathlib.Path(r"C:\Users\DSAXPS_13_9360\Documents\coding languages\CODE files\ANSII escape sequence documentation.md")
os.system('clear')
for line in file.open():
    print(line)