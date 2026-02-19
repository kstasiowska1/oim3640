# for i in range(5):
#     print(i)

# i = 0
# while i < 5: # as long as its true, keep running the loop
#     print(i)
#     i += 1 # should make this not true at some point

# This continues asking the user for input until they type "quit"
# response = ""
# while response != "quit":
#     response = input("Enter command: ")
#     print(f"You said: {response}")

# # break - exit the loop imeediately
words = ["hello", "target", "python"]
# for word in words:
#     if word == "target":
#         print("Found it!")
#         break

# continue - skip to the next iteration
for num in range(10):
    if num % 2 == 0: # if true, number will not be printed but it will iterate to the next number
        continue
    print(num) # will only print off numbers b/c they have remainders

