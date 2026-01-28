# Foundry AI NLP Demos

The goal of this work is to highlight some of the capabilities present in Azure Language in Foundry Tools.

Review the [ideas.md](./ideas.md) document for basic ideas and scenarios for each of the mentioned language capabilities.

## Resources

Use the following environment variables to connect to MS Foundry resources and APIs:

- `FOUNDRY_ENDPOINT` -- the API endpoint
- `FOUNDRY_API_KEY`  -- the API key
- `FOUNDRY_REGION` -- region in which foundry resoruces are provisioned

### Documentation

- [Azure Language in Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
- [SDK and REST developer Guides](https://learn.microsoft.com/en-us/azure/ai-services/language-service/concepts/developer-guide?tabs=language-studio)
- Capabilities to showcase:
    - [Sentiment Analysis](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/overview)
    - [Named Entity Recognition](https://learn.microsoft.com/en-us/azure/ai-services/language-service/named-entity-recognition/overview)
    - [Custom Question Answering](https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/overview)
    - [Key Phrase Extraction](https://learn.microsoft.com/en-us/azure/ai-services/language-service/key-phrase-extraction/overview)
    - [PII Redaction](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/overview?tabs=text-pii)
- [Azure AI Language API Reference](https://learn.microsoft.com/en-us/rest/api/language/)

## Expected outputs.

The goal is to generate a jupyter notebook that illustrates usage of the aforementioned capabilities in the Azure
Language in Foundry tools. For each capability listed below, generate the following:

1. A juptyer notebook named after the capability; e.g. `01-AzureLanguage-NamedEntityRecognition.ipynb`.
2. A dedicated directory for sample texts, e.g. `01-NamedEntityRecognition-data/`
3. One fabricated sample data set (as unstructured text) for each capability.

### Capability: Sentiment Analysis

- Sample Data: Fabricate a sample data file that contains customer reviews for a Restaurant named "The Bowl"
- Use the [Analyze Text](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2024-11-01&tabs=HTTP) to illlustrate performing sentitment analysis on the sample data.
- The resulting jupyter notebook should:
    - load the sample data
    - peform any necessary setup to call the API
    - make an API call
    - print the RAW results from the API,
    - print a human-friendly result constructed from the API's results.

### Capability: Named Entity Recognition

- Sample Data: Fabricate a sample data file that contains a business contract between fictitious companies -- e.g. Aperture Labratories agrees to provide ML services to the Umbrella Corporation.
- Use the [Analyze Text](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2024-11-01&tabs=HTTP) to performing named entity recognition on the sample business contract.
- The resulting jupyter notebook should:
    - load the sample data
    - peform any necessary setup to call the API
    - make an API call
    - print the RAW results from the API,
    - print a human-friendly result constructed from the API's results.

### Capability: Custom Question Answering

- Sample Data: For this example, we want to use real-world data fetched from the the following locations:
    - Tech901 Courses: https://www.tech901.org/courses
    - Tech901 Calendar: https://www.tech901.org/calendar
    - Tech901 Class prices: https://www.tech901.org/class-prices
    - Fetch the above pages and save as a data set suitable for sending to the Azure Language Question Answering service.
- Use the [Question Answering - Get Answers From Text](https://learn.microsoft.com/en-us/rest/api/language/question-answering/question-answering/get-answers-from-text?view=rest-language-question-answering-2023-04-01&tabs=HTTP) endpoint to answer a user-provided question from the supplied text records.
- The resulting jupyter notebook should:
    - load the sample data
    - peform any necessary setup to call the API
    - make an API call
    - print the RAW results from the API,
    - print a human-friendly result constructed from the API's results.

### Capability: Key Phrase Extraction

- Sample Data: Fabricate an 500-word (max) essay on the benefits of exercise and nutrition.
- Use the [Analyze Text](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2024-11-01&tabs=HTTP) to performing Key Phrase Extraction on the sample data
- The resulting jupyter notebook should:
    - load the sample data
    - peform any necessary setup to call the API
    - make an API call
    - print the RAW results from the API,
    - print a human-friendly result constructed from the API's results.

### Capability: PII Redaction

- Sample Data: Fabricate content representing a Medical report for Joe T. Public. The report should contain Joe's full home address, phone number, an internal patient identifier (aka account number) as well as his SSN. The medical report should also contain sensitive information about his medical condition: Cotard’s syndrome and congenital analgesia.
- Use the [Analyze Text](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2024-11-01&tabs=HTTP) to performing PII entity recognition on the sample data
- The resulting jupyter notebook should:
    - load the sample data
    - peform any necessary setup to call the API
    - make an API call
    - print the RAW results from the API,
    - print a human-friendly result constructed from the API's results.

## Additional Technical Guidance

- This project is managed by `uv`; See the `pyproject.toml` and `uv.lock` files for dependency details.
- Use `uv add` to add any new python packages.
- Ensure python code adheres to PEP8 standards.
- Run `ruff check` and `ruff format` on all python code.
- Use the `rich` library where appropriate to make data output more human-friendly
