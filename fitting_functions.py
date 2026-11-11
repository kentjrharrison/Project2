def linear(m,x,b):
    y=m*x+b
    return y
def slope_units(x_units,y_units):
    x_units=x_units.rstrip("s")
    y_units=y_units.rstrip("s")
    return y_units+'/'+x_units
def print_equation(m,b,y_units,x_units):
    print('The equation of the line is:y=',m,slope_units(x_units,y_units),'+',b,y_units.rstrip('s'))

    
