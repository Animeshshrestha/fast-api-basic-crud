# Project Setup

This is basic CRUD FastAPI project. It uses alembic for handling migration of databases, postgres as Databases. At first, clone the repo into your workspace. Then after that in the folder directory where alembic.ini is located created .env file. Refer to .env.example  for sample env file.

After that run **alembic upgrade head** to apply the migration to your database.

Use following command to run fast api server:

> uvicorn app.main:app --reload

Note: Make sure you are running above command in the same directory where **alembic.ini** file is located.

For swagger docs visit: localhost:8000/docs

There are two different endpoints but does the same task. Try to research the similarities and disimilarities in the endpoint views. Look into file named post_v1 and post_v2 inside of router folder . Router folder is inside of app folder. Thanks