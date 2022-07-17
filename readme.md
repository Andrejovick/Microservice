Requests with python

Documentation:
https://requests.readthedocs.io/en/latest/

Windows install:
```CMD
install requests
```

External API:
https://jsonplaceholder.typicode.com/

The available nested routes are:

    /posts/1/comments
    /albums/1/photos
    /users/1/albums
    /users/1/todos
    /users/1/posts


You can use your own local JSON server:

Install JSON Server 

```bash
npm install -g json-server
```

Start JSON Server

```bash
json-server --watch db.json
```

Create a `db.json` file with some data

Example:
```json
{
  "post": [
    { "id": 1, "title": "json-server", "body": "typicode", "userId": 1 }
  ],
}
