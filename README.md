# code_challange_Restaurants
#### This project is a Python implementation of a Yelp-style domain for a code challenge.
#### By **stanley wanjau**

## Description
 this is project that includes three main models: `Customer`, `Restaurant`, and `Review`. The relationships between these models represent a simplified version of a restaurant review system.
## How to Use
### Requirements
* A computer Which can run python
* Access to the internet
### Installation process
1. clone this respository using 
```bash 
git clone https://github.com/stanleywanjau/code_challange_Restaurants
```
or by downloading a ZIP file of the code 
2. The repository, if downloaded as a .zip file will need to be extracted to your preferred location.
3. Navigate to the project folder on your bash terminal.

4. Make sure you have the required dependencies installed using the provided Pipfile. You can install them by running:
```bash 
pipenv install

pipenv shell
```
  
## Technologies Used
* python 

## Class Structure
#### Customer
* `Customer __init__(given_name, family_name)`: Initializes a new customer with given and family names.
* `Customer full_name()`: Returns the full name of the customer.
* `Customer num_reviews()`: Returns the total number of reviews authored by the customer.
* `Customer find_by_name(name)`: Returns the first customer whose full name matches the specified name.
* `Customer find_all_by_given_name(name)`: Returns a list of customers with the given name.
* `Customer restaurants()`: Returns a unique list of restaurants reviewed by the customer.
* `Customer add_review(restaurant, rating, review_name)`: Adds a new review for the customer
  
#### Restaurant
* `Restaurant __init__(name)`: Initializes a new restaurant with a name.
* `Restaurant name()`: Returns the name of the restaurant.
* `Restaurant reviews()`: Returns a list of all reviews for the restaurant.
* `Restaurant customers()`: Returns a unique list of customers who have reviewed the restaurant.
* `Restaurant average_star_rating()`: Returns the average star rating based on its reviews.
#### Review
* `Review __init__(customer, restaurant, name, rating)`: Initializes a new review with a customer, restaurant, name, and rating.
* `Review rating()`: Returns the rating for a restaurant.
* `Review customer()`: Returns the customer object for that review.
* `Review restaurant()`: Returns the restaurant object for that given review.
* `Review all()` Returns all reviews.

## Support and Contact Details
Incase of any query, need for collaboration or issues with this code, feel free to reach me at
stanley.muiruri@student.moringaschool.com

## License 
MIT License

Copyright &copy; 2023 Stanley Wanjau

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

