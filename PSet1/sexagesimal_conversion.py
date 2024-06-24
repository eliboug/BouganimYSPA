def conversion():  
    response1 = input("Would you like to convert to decimal or sexagesimal angles? ")
    # convertion to decimal
    if response1 == "decimal":
        # take inputs
        degrees = float(input("How many degrees in this angle? "))
        arcminutes = float(input("How many arcminutes in this angle? "))
        arcseconds = float(input("How many arcseconds in this angle? "))
        # convert to degrees
        decimal_arcminutes = arcminutes / 60
        decimal_arcseconds = arcseconds / 3600
        degrees += (decimal_arcminutes + decimal_arcseconds)
        # display output
        print("Your angle in decimal measure is " + str(degrees) + " degree(s).")
    # conversion to sexagesimal
    elif response1 == "sexagesimal":
        degrees = float(input("Enter the angle measurement in degrees: "))
        sexagesimal_degrees = int(degrees)
        sexagesimal_arcminutes = (degrees % 1) * 60
        sexagesimal_arcseconds = (sexagesimal_arcminutes % 1) * 60
        
        sexagesimal_arcminutes = int(sexagesimal_arcminutes)
        sexagesimal_arcseconds = int(sexagesimal_arcseconds)
        # TODO: account for sig figs
        print(f"{sexagesimal_degrees}° {sexagesimal_arcminutes:02d}' {sexagesimal_arcseconds:4d}\"")
    # handle unexpected responses
    else: 
        print("Please enter either 'decimal' or 'sexagesimal'.")
        conversion()

# main
conversion()

