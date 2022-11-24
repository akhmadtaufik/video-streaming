from video_streaming import User, NewUser

user_1 = User("Shandy", 12, "Basic Plan")

# check attribute in Class
user_1.username, user_1.duration_plan, user_1.current_plan

# Test Case 1
print("Test Case 1")
print("-----------")
user_1.check_benefit()
print("\n")

# Test Case 2
print("Test Case 2")
print("-----------")
user_1.check_plan("Shandy")
print("\n")

# Test Case 3
print("Test Case 3")
print("-----------")
user_1.upgrade_plan("Shandy", "Basic Plan", "Standard Plan")
print("\n")

# Test Case 4
# Testing with another Object
user_2 = User("Cahya", 24, "Standard Plan")

print("Test Case 4")
print("-----------")
user_2.check_benefit()
print("\n")
user_2.check_plan("Cahya")
print("\n")
user_2.upgrade_plan("Cahya", "Standard Plan", "Premium Plan")
print("\n")

# Test Case 5
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"],
}
# Create NewUser
faizal = NewUser("faizal_icikiwir")
print("Test Case 5")
print("-----------")
faizal.convert_data_to_list(data)
faizal.pick_plan("Standard Plan", "ana-2f9g")
print("\n")
