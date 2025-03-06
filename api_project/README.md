This project is a simple API built with Django REST Framework (DRF) to manage books.

## How to set it up

1.  *Clone the repository:*
    bash
    git clone [your_repository_url]
    cd Alx_DjangoLearnLab/api_project
    

2.  *Create a virtual environment (recommended):*
    bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    

3.  *Install dependencies:*
    bash
    pip install -r requirements.txt
    
    (Make sure you have a requirements.txt file listing your dependencies)

4.  *Run migrations:*
    bash
    python manage.py migrate
    

5.  *Start the development server:*
    bash
    python manage.py runserver
    

## Authentication part

This API uses token-based authentication.

### How to obtain a Token

1.  Send a POST request to http://127.0.0.1:8000/api-token-auth/ with the following JSON body:

    json
    {
        "username": "your_username",
        "password": "your_password"
    }
    

2.  The response will contain your authentication token in the token field.

### Using the Token

1.  Include the token in the Authorization header of your requests, using the format:

    
    Authorization: Token your_token_here
    

    (Replace your_token_here with your actual token)

2.  For example, in curl:

    bash
    curl -H "Authorization: Token your_token_here" [http://127.0.0.1:8000/books_all/](http://127.0.0.1:8000/books_all/)
    

3.  In Postman, set the "Authorization" type to "Token" and paste your token in the "Token" field.

## Permissions

* **BookViewSet:**
    * Access is restricted to authenticated users.
    * This is enforced by the permissions.IsAuthenticated permission class.

## API Endpoints

* **/books_all/:**
    * GET: List all books.
    * POST: Create a new book.
* **/books_all/{id}/:**
    * GET: Retrieve a book by ID.
    * PUT/PATCH: Update a book.
    * DELETE: Delete a book.
* **/api-token-auth/:**
    * POST: Obtain an authentication token.

## Example Request (Create a Book)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Token your_token_here" -d '{
    "title": "Example Book",
    "author": "John Doe"
}' [http://127.0.0.1:8000/books_all/](http://127.0.0.1:8000/books_all/)