try:
    bananas=int(input("How many bananas would you like? "))
    
    if bananas>=5:
        print(f"You sure like bananas! Here, have {bananas} bananas!")
    elif bananas==4:
        print(f"Ah you can make a pudding. Here, have {bananas} bananas!")
    elif bananas==3:
        print(f"Have them with nutella and pancakes? Here, have {bananas} bananas!")
    elif bananas==2:
        print(f"Fancy a couple for breakfast? Here, have {bananas} bananas!")
    elif bananas==1:
        print(f"Just a quick snack? Here, have {bananas} banana!")
    elif bananas==0:
        print("Would you like some apples, then?")
except ValueError:
    print("What do you mean? Please enter a number of bananas.")
