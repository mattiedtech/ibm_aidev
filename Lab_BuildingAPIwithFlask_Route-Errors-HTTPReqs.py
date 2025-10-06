# Import the Flask class from the flask module
from flask import Flask, make_response, request

# Create an instance of the Flask class, passing the name of the current module
app = Flask(__name__)

# DATA
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


# Define a route for the root URL
@app.route('/')
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world!"

# No content error with tuple
@app.route('/no_content')
def no_content():
    status = 204
    return({"error":"No content found."}, 204)

# Use make_response() method for 200
@app.route('/exp')
def index_explicit():
    res = make_response({"Response:":"<b> Peep this reponse!</b>"})
    res.status_code = 200
    return res

# Get data in JSON
@app.route('/data')
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return JSON response with length
            return {"message:":f"Data of length {len(data)} found."}
        else:
            # If 'data' empty reurn Json with response 500 error
            return {"message:": "Data is empty"}, 500
    except NameError:
        # Handle case where 'data' is not defined with 404 Not Found
        return {"message:": "Data not found."}, 404

# Name Search
@app.route('/name_search')
def name_search():
    # Get the argument 'q' from the query params of the request
    query = request.args.get('q')
    # Check if 'q' is missing
    if query is None:
        return {"message:": "Query parameter 'q' is missing."}, 400
    # Check if 'q' is present but invalid (empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message:": "Invalid input parameter."}, 422
    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person w/ 200 OK
            return person, 200
        # if no match found, return JSON response with a message indicating 404 error
    return {"message:": "person not found."}, 400

# Create GET/count endpoint
@app.route('/count')
def count():
    try:
        # Attempt to return a JSON with count of items in data
        return {"data count": len(data)}, 200
    except NameError:
        # If 'data' isn't defined, 500 Internal Server Error
        return {"message:": "data not defined"}, 500

# GET / person / id/ endpoint
@app.route('/person/<var_name>')
def find_by_uuid(var_name):
    # Iterate through data to search for UUID
    for person in data:
        if person['id'] == str(var_name):
            return person
    return {"message": "Person not found"}, 404

# DELETE ENDPOINT
@app.route("/person/<var_name>", methods=['DELETE'])
def delete_by_uuid(var_name):
    for person in data:
        if person["id"] == str(var_name):
            # Remove the person from the data list
            data.remove(person)
            # Return a JSON response with a message and HTTP status code 200 (OK)
            return {"message": "Person with ID deleted"}, 200
    # If no person with the given ID is found, return a JSON response with a message and HTTP status code 404 (Not Found)
    return {"message": "Person not found"}, 404

@app.route('/person', methods=['POST'])
def create_person():
    # Get the JSON data from the incoming request
    new_person = request.get_json()
    # Check is JSON is empty/none
    if not new_person:
        return {"message": "Invalid input, no data provided"}, 422
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"New person created: ID is {new_person['id']}"}, 200

#ERROR HANDLERS
@app.route("/test500")
def test500():
    """"Catch any unhandled Exception anywher in the app and rout it to this handler"""
    raise Exception("Forced exception for testing")

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "Sorry! API not found"}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500
