from random import choice


def get_recipe_bot_response(user_response):

  bot_response_blt = ["One toasted piece of bread, spread on mayo, add crispy bacon, slice of tomato, and fresh lettuce, and if you feel adventurous onion. Lastly add second piece of toast!! Yummmmm!" ]
  bot_response_burger = ["Top bun toasted, spread all your favorite condiments, add lettuce, tomato, onion, on top of a hot charbroiled burger patty, sometimes it's good to add bacon, or an egg, or even BOTH! Don't forget cheese. Place all ingredients on top of bottom toasted bun! Eat and Enjoy!!"]
  bot_response_hotdog = ["Toast the hotdog bun, add grilled kosher dog, add condiments, onion and relish....YES,I LIKE RELISH..Ok? This dog is best eaten at a ballpark or backyard BBQ"]

  if user_response ==  "blt":
    return choice(bot_response_blt)
  elif user_response == "burger" :
    return choice(bot_response_burger)
  elif user_response == "hotdog" :
    return choice(bot_response_hotdog)
  else:
    return "I can't cook that shit. I'm a damn robot, not a chef!"




print(" Let's Make Lunch")
print(" Select one menu item 'blt','burger', or 'hotdog' and I will give you my favorite recipe. ")

user_response = ""

while True:
  user_response = input(" What are we making?: ")
  
  
  if user_response == 'Finished Making Lunch':
    break

  
  bot_response = get_recipe_bot_response(user_response)
  print(bot_response)

