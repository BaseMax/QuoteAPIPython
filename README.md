# Quote API Python

## Random Quote Generator API

In this project, we will build a RESTful API that generates random quotes. The quotes will be stored in a database and the API will expose endpoints for CRUD operations (Create, Read, Update, Delete).

Here are some additional features we can add:

- Filter quotes by author name or keyword in the text
- Allow users to rate quotes and retrieve a list of top-rated quotes
- Add user authentication and authorization to restrict access to quote creation, deletion, and updating

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Requirements

1. Retrieve a random quote

```http
GET /quotes/random
```

Returns a single random quote:

```json
{
    "id": 1,
    "text": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "author": "Nelson Mandela"
}
```

2.Search in Quotes:

```http
GET /quotes?q=someone
```

Response:

```json
[
    {
        "id": 5,
        "text": "Dignity will only happen when you realize that having someone in your life doesn’t validate your worth.",
        "author": "Shannon L. Alder"
    }
]
```

3. Retrieve a list of all quotes

```http
GET /quotes
```

Returns a list of all quotes in the system:

```json
[
    {
        "id": 1,
        "text": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "author": "Nelson Mandela"
    },
    {
        "id": 2,
        "text": "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
        "author": "Oprah Winfrey"
    }
]
```

4. Add a new quote

```http
POST /quotes
```

Adds a new quote to the system. The request body should include a JSON object with the following properties:
- `text` (string, required): the text of the quote
- `author` (string, required): the author of the quote

```json
{
    "text": "The best way to predict the future is to invent it.",
    "author": "Alan Kay"
}
```

5. Update an existing quote

```http
PUT /quotes/{quote_id}
```

Updates an existing quote with the given quote_id. The request body should include a JSON object with the following properties:
- `text` (string): the new text of the quote
- `author` (string): the new author of the quote

```json
{
    "text": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs"
}
```

6. Delete a quote

```http
DELETE /quotes/{quote_id}
```

Deletes the quote with the given `quote_id`.

Copyright 2023, Max Base
