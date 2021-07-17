import colors
#using printc function. You can also set c_end to false and the color will not end
#will print hi but light blue
colors.printc('hello', 'lightblue')
#example of setting c_end to false
#if the color name ends with h it wil set the background
colors.printc('', 'redh', end='')
colors.printc('test', 'yellow')
#you can also print like this:
print(colors.lightblue+'hello world!'+colors.end)
print(colors.redh+'colors is awesome!')
print(colors.end)
#using format to print in color
print(f'{colors.yellow}awesome{colors.end}')
print('{}test{}'.format(colors.green, colors.end))
#color will return a string colored the color you specified
color=colors.color('hi', 'lightblue')
print(color)