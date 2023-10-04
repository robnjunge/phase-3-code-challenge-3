class Customer:
   
    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"




class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating
    
    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews


    def __str__(self):
        return f"Review by {self._customer.full_name()} for {self._restaurant.name()}: Rating {self._rating}"


class Restaurant:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


customer = Customer("Morgan", "Jason")
restaurant = Restaurant("The Kenyan Fried Chicken")


# Create a review instance
review = Review(customer, restaurant, 9.5)



# Retrieve the customer and restaurant objects for the review
review_customer = review.customer()
review_restaurant = review.restaurant()

# Access customer information

# print(customer1.full_name())

# print(customer2.full_name())


# Access the customer's full name and the restaurant's name
print(review_customer.full_name())  
print(review_restaurant.name())  
# Access the review's rating
print(review.rating()) 

# Print the review with customer and restaurant information
print(review) 

#__str__(self): This special method defines the string representation
# of the review object. It returns a formatted string containing the customer's full name,
# the restaurant's name, and the rating.
# Get all reviews
all_reviews = Review.all()


