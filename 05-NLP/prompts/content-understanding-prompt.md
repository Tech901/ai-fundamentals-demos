# Content Understanding Demo

The goal of this work is to highlight some of the capabilities present in Azure AI Content Understanding service
in Foundry Tools.

## Resources

Use the following environment variables to connect to MS Foundry resources and APIs:

- `FOUNDRY_CONTENT_UNDERSTANDING_ENDPOINT` -- the API endpoint for the Azure AI Content Understanding
- `FOUNDRY_API_KEY`  -- the API key
- `FOUNDRY_REGION` -- region in which foundry resoruces are provisioned

### Documentation

- [Choosing the right AI tool: Overview of services](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/choosing-right-ai-tool#overview-of-services)
- [Azure AI Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/)
- [What is a Content Understanding Analyzer](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/analyzer-reference)
- [Azure Content Understanding REST API](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/quickstart/use-rest-api?tabs=portal%2Cdocument)
    - [REST API Reference](https://learn.microsoft.com/en-us/rest/api/contentunderstanding/operation-groups?view=rest-contentunderstanding-2025-11-01)
- [Prebuilt analyzers in Azure Content Understanding in Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/prebuilt-analyzers)
- [Content Understanding classification/segmentation](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/classifier)

## Expected outputs.

The goal is to generate a jupyter notebook that illustrates usage of the following capabilities in the Azure
Content Understanding service in Foundry tools.

Create a juptyer notebook named `06-ContentUnderstanding.ipynb`, and within that notebook, we want to include a
section that highlights each capability listed below:

### Capability: List the content analyzers

- Use the [Content Analyzers - List](https://learn.microsoft.com/en-us/rest/api/contentunderstanding/content-analyzers/list?view=rest-contentunderstanding-2025-11-01&tabs=HTTP) endpoint
- Just print the output as human-friendly JSON so we can understand what analyzers exist.

### Capability: Content Extraction

- Sample Data: This link contains a PDF ebook with some highlights: https://www.dropbox.com/scl/fi/405z56tds3tewycemxp23/Azure-AI-Fundamentals-AI-900-Study-Guide-1.pdf?rlkey=i0t4xnrrt392lba4s4fqlt1j7&st=yomn8xte&dl=0
- Use the endpoint: [Content Analyzers - Analyze](https://learn.microsoft.com/en-us/rest/api/contentunderstanding/content-analyzers/analyze?view=rest-contentunderstanding-2025-11-01&tabs=HTTP)
- Use the `prebuilt-layout` analyzer to:
    - Extract the annotations (e.g. highlights) from the provided PDF
    - peform any necessary setup to call the API
    - make an API call
    - print the RAW results from the API,
    - print a human-friendly result constructed from the API's results.

### Capability: Classification and segmentation

- Sample Data: This example has multiple inputs Repeat for each of the following images:
    - An image of produce: https://images.unsplash.com/photo-1635341083777-5f93a755e916?q=80&w=500
    - An image of elephants: https://images.unsplash.com/photo-1505148230895-d9a785a555fa?q=80&w=500
- Use the endpoint: [Content Analyzers - Analyze Binary](https://learn.microsoft.com/en-us/rest/api/contentunderstanding/content-analyzers/analyze-binary?view=rest-contentunderstanding-2025-11-01&tabs=HTTP)
- Use the `prebuilt-image` analyzer to:
    - classify and segment items in the sample image.
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
