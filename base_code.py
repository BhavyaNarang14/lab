print("""
For add press '+'
For sub press '-'
For mul press 'x'
For div press '/'
""")


i = input("enter your choice:")
switch(i) { 
        case 1: 
            return "zero";
        break;
        case 2: 
            return "one";
        break;
        case 3: 
            return "two";
        break;
        case 4: 
            return "nothing";
        break;
        default:
            print("no case")
    }; 
