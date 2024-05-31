## How to Run the pdf_form_parser.py File

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:ish-codes-ai/pdf_form_parser.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pdf_form_parser
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Modify the `config.py` file according to your needs. You can find it in the project directory.

5. Run the `pdf_form_parser.py` file:

    ```bash
    python3 pdf_form_parser.py
    ```

## Modifications

If you need to make modifications to the `config.py` file, you can follow these guidelines:

- `Model name`: Default is set to `gpt-3.5-turbo-0125`
- `Max tokens`: Set to how short or large you want the summary. Max can be 4096

In the `.env` file, put your own `OPENAI API KEY`.

Make sure to test your modifications thoroughly before running the script.

