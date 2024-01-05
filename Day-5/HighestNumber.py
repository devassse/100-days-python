#Find the Highest Number - without using max()

# highest_score = 0
# scores = [43, 10, 87, 67, 55]
# for score in scores:
#     if score > highest_score:
#         highest_score = score

# print(f"The Highest Score is {highest_score}")


# n = 10
# for number in range(1, n+1):
#     print(number)


#Add EVEN number from 1 to 100
n = 100
evens = 0
for number in range(1, n + 1):
    if number % 2 == 0:
        evens += number

print(f"The SUM of EVEN numbers is {evens}")

#Add EVEN number from 1 to 100
n = 100
evens = 0
for number in range(2, n + 1, 2):
    evens += number

print(f"The SUM of EVEN numbers is {evens}")