current_weather = input("What's the weather like today? (sunny/rainy/cold): ")
clothing_recommendation = ""

if current_weather == "sunny":
    clothing_recommendation = "Wear a t-shirt and sunglasses."
elif current_weather == "rainy":
    clothing_recommendation = "Don't forget your umbrella and a raincoat."
elif current_weather == "cold":
    clothing_recommendation = "Make sure to wear a warm coat and a scarf."

else:
    clothing_recommendation = "Sorry, I don't have recommendations for this weather."

print(clothing_recommendation)