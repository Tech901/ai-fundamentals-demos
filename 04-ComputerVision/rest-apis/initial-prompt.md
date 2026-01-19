# Create sample python scripts to use Azure Computer vision

Formerly part of the "Cognitive Services"  products, these APIs are now part of Microsoft Foundry.

## API endpoints

- [Analyze - Image](https://learn.microsoft.com/en-us/rest/api/computervision/analyze/image?view=rest-computervision-v4.0%20(2024-02-01)&tabs=HTTP)
    - Note: The docs have a [Try It](https://learn.microsoft.com/en-us/rest/api/computervision/analyze/image?view=rest-computervision-v4.0%20(2024-02-01)&tabs=HTTP#code-try-0) section.
- [Vectorize - Image](https://learn.microsoft.com/en-us/rest/api/computervision/vectorize/image?view=rest-computervision-v4.0%20(2024-02-01)&tabs=HTTP)

## Additional Resources

- [Microsoft Foundry: What is Image Analysis](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0)
- [Computer Vision REST API reference](https://learn.microsoft.com/en-us/rest/api/computer-vision/?view=rest-computervision-v4.0%20(2024-02-01))
- [What is Azure vision in Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview)

## Environment Variables

The following environment variables should be used for this application.

- AZURE_SUBSCRIPTION -- The subscription of the azure account.
- AZURE_RESOURCE_GROUP -- the resource group in which the CV service is provisioned.
- AZURE_CV_ENDPOINT -- the API endpoint
- AZURE_CV_KEY1 -- an API key for computer vision
- AZURE_CV_KEY2 -- a second API key for computer vision
- AZURE_CV_REGION -- the region for the computer vision service.


## desired output

We want a Jupyter notebook that showcases how to use the Analyze Image API endpoints. Each cell in the notebook should either perform some setup code or should illustrate how to call the API from python. This includes:


1. Cells illustrating how to call the Analyze Image api with:
    - `features=tags`
    - `features=caption`
    - `features=denseCaptions`
    - `features=objects`
    - `features=read`
    - `features=people`
    - All examples should use `language=en`.
    - The input `url` for the body should use a user-defined variable that defaults to: https://placecats.com/300/200
2. Cells illustrating how to call the Vectorize Image API. The `model-version` request parameter should use the value: "2023-04-15"