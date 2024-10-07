reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for word in keywords:
        if word in review.lower():
            target = review.lower().find(word)
            target_len = len(word)
            first_half = review[:target]
            replace_word = word.upper()
            second_half = review[target + target_len:]
            new_review = first_half + replace_word + second_half
            
            print("-" * 50)
            # print(review)
            # print(f"Word: {word.upper()}\nIndex: {target}\nLength: {target_len}")
            # print(f"1st Half: {first_half}")
            # print(f"Word: {replace_word}")
            # print(f"2nd Half: {second_half}")
            print(new_review)
            print("-" * 50)
            

