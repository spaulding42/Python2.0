class User:
    def __init__(self, FirstName, LastName, Email, Age):
        self.first_name = FirstName
        self.last_name = LastName
        self.email = Email
        self.age = Age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First Name: " , self.first_name)
        print("Last Name: ", self.last_name)
        print("Email Address: ", self.email)
        print("Age: ", self.age)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points - amount >= 0:
            self.gold_card_points -= amount
        else:
            print("Not enough points")

user1 = User("Devin", "Spaulding", "spaulding42@gmail.com", 37)
# print(user1.last_name)
user1.display_info()
user1.spend_points(50)
print("spent")
user1.spend_points(190)