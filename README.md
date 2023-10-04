# phase-3-code-challenge-3 SQLAlchemy Code Challenge Restaurants

For this assignment, we'll be working with a Yelp-style domain.

We have three models: `Restaurant`, `Customer`, and `Review`.

For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many `Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.

`Restaurant` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- SQLAlchemy Migrations
- SQLAlchemy Relationships
- Class and Instance Methods
- SQLAlchemy Querying
## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`. You'll need to create your own sample instances so that you can try out your code on your own. Make sure your relationships and methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it, run `python tools/debug.py` from the command line. This will start a `ipdb` session with your classes defined. You can test out the methods that you write here. You can add code to the `tools/debug.py` file to define variables and create sample instances of your objects.

Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.

## Sample Schema:
`restaurants` Table:
| Column | Type    |
| --------- | -------  |
| name    | String   |
| price     | Intege  |
 

`customers` Table:
|Column     | Type   |
| ------------ | ------  |
| first_name | String |
| last_name  | String |


## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.


### Object Relationship Methods

#### Review

- `Review customer()`
  - should return the `Customer` instance for this review
- `Review restaurant()`
 - should return the `Restaurant` instance for this review

#### Restaurant

- `Restaurant reviews()`
  - returns a list of all reviews for the restaurant
- `Restaurant customers()`
  
  - returns a collection of all the customers who reviewed the `Restaurant`
#### Customer

- `Customer reviews()`
  - should return a collection of all the reviews that the `Customer` has left
- `Customer restaurants()`
  - should return a collection of all the restaurants that the `Customer` has reviewed


### Aggregate and Relationship Methods
# Customer
- `Customer full_name()`
  - returns the full name of the customer, with the first name and the last name concatenated Western style.
- `Customer favorite_restaurant()`
  - returns the restaurant instance that has the highest star rating from this customer
- `Customer add_review(restaurant, rating)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and a rating creates a new review for the restaurant with the given `restaurant_id`
- `Customer delete_reviews(restaurant)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and removes **all** their reviews for this restaurant
# Review
- `Review full_review()`
  - should return a string formatted as follows:
        - Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
# Restaurant
- `Restaurant fanciest(), this method should be a class method`
  - returns _one_ restaurant instance for the restaurant that has the highest price
- `Restaurant all_reviews()`
  - should return a list of strings with all the reviews for this restaurant formatted as follows:
-------------------------------------------------------------------------------------------------------------------------
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
]