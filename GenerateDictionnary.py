from colour import Color


with open("XKCDColors.txt") as f:
	colours = f.readlines()

file = open("XKCD_colour_definition.py","w")
file.write("XKCD_RGB_TO_COLOR_NAMES = {")

for colour in colours[1:-1]:
	print(colour.strip())
	values = colour.split("\t")
	colour_name = values[0].replace(" ", "_")
	colour_name = colour_name.replace("'", "")
	colour_HEX = values[1].strip()
	c = Color(colour_HEX)
	file.write("(" + str(c.red) +", "+ str(c.green) + ", " + str(c.blue) + "): ['XKCD_" + colour_name + "'],\n")
print(colours[-1].strip())
values = colours[-1].split("\t")
colour_name = values[0].replace(" ", "_")
colour_HEX = values[1].strip()
c = Color(colour_HEX)
file.write("(" + str(c.red) +", "+ str(c.green) + ", " + str(c.blue) + "): ['XKCD_" + colour_name + "']\n")
file.write("}")
file.close() 

 


