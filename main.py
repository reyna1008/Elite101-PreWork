assist1 = 0
assist2 = 0

print ("Well seems like there's a new customer on the line, trust me, you will not regret clicking on this tab...So let's begin!");
user_name = input("Before anything, what's your name? ");
user_age = input("Well " +user_name+", how old are you exactly? ");
user_age = int(user_age)
if user_age >= 18:
  assist1 = int(input("An adult here I see...but anyways how can I assist you? (pick a number)\n 1.What's your open hours?\n 2. What's the best thing on our market?\n 3.What days are you closed?\n 4. Is everything legal for sale?\n 5. I just want to leave\n"))
else:
  assist2 = int(input("Wow you're young...but anyways how can I assist you? (pick a number)\n 1.What's your open hours?\n 2. What's the best thing on our market?\n 3.What days are you closed?\n 4. Is everything legal for sale?\n 5. I just want to leave\n"))

#I will add the rest of the answers later for now it's just to exit
if assist1 or assist2 == 5:
  print("oh...well that's a shame, but I'll be here if you need me!");