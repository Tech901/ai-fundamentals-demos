# Azure Language NLP Demos

This project contains a comprehensive set of Jupyter notebooks demonstrating the capabilities of **Azure Language in Foundry Tools**. Each notebook showcases a different natural language processing (NLP) capability using real-world sample data and the Azure Language REST APIs.

## 📋 Project Overview

The goal of this project is to provide hands-on examples of how to use Azure Language services for common NLP tasks. The notebooks include both API integration examples and human-friendly result formatting using the `rich` library.

## 🎯 Capabilities Demonstrated

This project covers **5 key Azure Language capabilities**:

### 1. **Sentiment Analysis** (`01-AzureLanguage-SentimentAnalysis.ipynb`)
Analyze the sentiment of text documents to determine if they express positive, negative, neutral, or mixed opinions.

- **Sample Data**: Customer reviews for "The Bowl" restaurant
- **API Used**: [Analyze Text - Sentiment Analysis](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text)
- **Use Cases**: Customer feedback analysis, brand reputation monitoring, product reviews

### 2. **Named Entity Recognition** (`02-AzureLanguage-NamedEntityRecognition.ipynb`)
Extract and classify named entities (people, organizations, locations, dates, etc.) from text.

- **Sample Data**: Business contract between Aperture Laboratories and Umbrella Corporation
- **API Used**: [Analyze Text - Entity Recognition](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text)
- **Use Cases**: Document parsing, contract analysis, information extraction

### 3. **Custom Question Answering** (`03-AzureLanguage-QuestionAnswering.ipynb`)
Answer natural language questions by searching through provided text records.

- **Sample Data**: Tech901 course information, schedules, and pricing
- **API Used**: [Question Answering - Get Answers From Text](https://learn.microsoft.com/en-us/rest/api/language/question-answering/question-answering/get-answers-from-text)
- **Use Cases**: FAQ chatbots, knowledge base search, customer support automation

### 4. **Key Phrase Extraction** (`04-AzureLanguage-KeyPhraseExtraction.ipynb`)
Automatically identify and extract the most important key phrases and concepts from text.

- **Sample Data**: Essay on the benefits of exercise and nutrition
- **API Used**: [Analyze Text - Key Phrase Extraction](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text)
- **Use Cases**: Content summarization, topic modeling, content tagging

### 5. **PII Redaction** (`05-AzureLanguage-PIIRedaction.ipynb`)
Detect and redact Personally Identifiable Information (PII) from documents for data privacy compliance.

- **Sample Data**: Medical report containing sensitive patient information
- **API Used**: [Analyze Text - PII Entity Recognition](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text)
- **Use Cases**: HIPAA compliance, data protection, privacy enforcement

## 📁 Project Structure

```
05-NLP/
├── README.md                                      # This file
├── pyproject.toml                                 # Project dependencies
├── ideas.md                                       # Conceptual scenarios
├── initial-prompt.md                              # Project requirements
│
├── 01-AzureLanguage-SentimentAnalysis.ipynb
├── 01-SentimentAnalysis-data/
│   └── restaurant_reviews.txt
│
├── 02-AzureLanguage-NamedEntityRecognition.ipynb
├── 02-NamedEntityRecognition-data/
│   └── business_contract.txt
│
├── 03-AzureLanguage-QuestionAnswering.ipynb
├── 03-QuestionAnswering-data/
│   ├── tech901_courses.txt
│   ├── tech901_calendar.txt
│   └── tech901_prices.txt
│
├── 04-AzureLanguage-KeyPhraseExtraction.ipynb
├── 04-KeyPhraseExtraction-data/
│   └── exercise_nutrition_essay.txt
│
└── 05-AzureLanguage-PIIRedaction.ipynb
    └── 05-PIIRedaction-data/
        └── medical_report.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- An Azure Language resource with endpoint and API key
- Jupyter Notebook environment

### Environment Setup

Set the following environment variables before running the notebooks:

```bash
export FOUNDRY_ENDPOINT="https://<your-resource>.api.cognitiveservices.azure.com"
export FOUNDRY_API_KEY="<your-api-key>"
export FOUNDRY_REGION="<your-region>"  # e.g., "eastus"
```

### Installation

This project uses `uv` for dependency management:

```bash
# Install dependencies
uv sync

# Start Jupyter
jupyter notebook
```

### Running the Notebooks

1. Open Jupyter and navigate to any notebook (e.g., `01-AzureLanguage-SentimentAnalysis.ipynb`)
2. Run the cells in order:
   - Cell 1: Import required libraries
   - Cell 2: Load sample data
   - Cell 3: Configure API
   - Cell 4: Make API call
   - Cell 5: Display raw JSON results
   - Cell 6: Display formatted results

Each notebook is self-contained and can be run independently.

## 📦 Dependencies

- **requests**: HTTP library for API calls
- **rich**: Terminal formatting and beautiful output
- **jupyter**: Interactive notebook environment
- **pandas**: Data manipulation (optional, for some demos)

See `pyproject.toml` for complete dependency list.

## 📚 API Reference

All notebooks use Azure Language REST APIs. For detailed documentation:

- [Azure Language Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
- [Analyze Text API Reference](https://learn.microsoft.com/en-us/rest/api/language/analyze-text/analyze-text/analyze-text)
- [Question Answering API Reference](https://learn.microsoft.com/en-us/rest/api/language/question-answering/question-answering/get-answers-from-text)

## 🎨 Output Formatting

All notebooks use the `rich` library to format output beautifully:

- **Tables**: Display structured data with colors and alignment
- **Panels**: Highlight important information and summaries
- **Syntax Highlighting**: Make JSON and code more readable

## 📝 Code Quality

All Python code in the notebooks adheres to:

- **PEP 8** style guidelines
- **Ruff** linting standards
- **Import sorting** (isort)

Run quality checks with:

```bash
uv run ruff check *.ipynb
uv run ruff format *.ipynb
```

## 💡 Learning Outcomes

After working through these notebooks, you will understand:

- How to authenticate with Azure Language services
- How to structure requests for different NLP tasks
- How to parse and interpret API responses
- How to build user-friendly output from API results
- Real-world applications of NLP in business

## 🔗 Related Resources

- [Tech901 Website](https://www.tech901.org/)
- [Azure AI Services](https://learn.microsoft.com/en-us/azure/ai-services/)
- [Ideas and Scenarios](./ideas.md)
- [Initial Project Requirements](./initial-prompt.md)

## ✨ Features

- ✅ 5 different NLP capabilities
- ✅ Sample datasets for each capability
- ✅ Complete API integration examples
- ✅ Rich, formatted output
- ✅ Error handling and validation
- ✅ Environment-based configuration
- ✅ PEP 8 compliant code
- ✅ Comprehensive documentation

## 📄 License

This project is part of the Tech901 AI Fundamentals Demos series.

---

**Last Updated**: January 24, 2026
