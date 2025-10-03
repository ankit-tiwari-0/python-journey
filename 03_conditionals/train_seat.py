seat_type =  input("ENter seat type (sleeper/AC/General)").lower()




match seat_type:
    case "sleeper":
        print("Sleeper -  No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reserve")
    case "luxury":
        print("Luxury - Premium seats eith meals")   
    case _:
        print("INvalid seat bhag Gareeb")     





