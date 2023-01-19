# Product Details API

Product Details API is an API that provides product information and question answering capabilities for the Store Assistant application. It uses the BERT-large-uncased-whole-word-masking-finetuned-SQUAD model to answer customer questions about products. The data is stored in SQLite database.
## Technical details

    The API is built using FastAPI, a modern, fast, web framework for building APIs with Python.
    The API uses the BERT-large-uncased-whole-word-masking-finetuned-SQUAD model, which is a pre-trained transformer-based model that has been fine-tuned on the SQuAD dataset for question answering tasks.
    The API uses SQLite database to store product information
    The API uses Hugging Face's transformers library to fine-tune the model and generate answers.

## API Endpoints

    /items/{item_id}: Returns details of a specific product
    /items/{item_id}/{question}: Accepts question and product_id as parameters and returns answer
    /item: Accepts product information to append it to the database

## Installation and usage

    Clone the repository:

git clone https://github.com/PrathamSoneja/arAssistant.git

    Install the required packages:

pip install -r requirements.txt

    Run the application:

uvicorn main:main --reload

    Use the API endpoints to fetch product information and answer question

## Limitations

    The model is only as good as the data it was trained on, so it may not be able to answer all questions accurately.
    The model is only able to answer questions in English.

## Future work

    Adding support for multiple languages.

## Contributions

    Pull requests and suggestions for improvement are welcome.

## Licensing

    This project is licensed under the Mozilla Public License 2.0. See LICENSE for more information.

## Note

    The API is hosted on https://540zfa.deta.dev/ and the documentation can be found at https://540zfa.deta.dev/docs
    The API is intended to be used with the Store Assistant application.
    If you want to use the API in production, you may need to consider the cost and usage limits of the hosting service.
