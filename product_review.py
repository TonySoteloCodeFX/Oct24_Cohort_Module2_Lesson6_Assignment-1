reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


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
            print(new_review)
            print("-" * 50)


def sentiment_tally():
    good_words = 0
    bad_words = 0
    for review in reviews:
        for word in positive_words + negative_words:
            if word in review.lower() and word in positive_words:
                good_words += 1
            elif word in review.lower() and word in negative_words:
                bad_words += 1
    print(f"Positive Word Count: {good_words}")
    print(f"Negative Word Count: {bad_words}")
    print("-" * 50)

sentiment_tally()

print("Review Summary:")
print("-" * 50)
for review in reviews:
    summary_count = 29
    while review[summary_count] != " ":
        summary_count += 1
    if review[summary_count] == " ":
        print(review[:summary_count] + "...")
        print("-" * 50)