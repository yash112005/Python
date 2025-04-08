import time

def typing_speed_test():
    text_to_type = input("enter text to type: ")
    print("Type the following text as quickly and accurately as possible:")
    print(f"\n{text_to_type}\n")
    
    input("Press Enter when you're ready to start!")
    start_time = time.time()
    
    typed_text = input("\nStart typing:\n")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_per_minute = len(typed_text.split()) / (time_taken / 60)
    
    accuracy = sum(1 for a, b in zip(typed_text, text_to_type) if a == b) / len(text_to_type) * 100
    
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute (WPM): {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

typing_speed_test()

