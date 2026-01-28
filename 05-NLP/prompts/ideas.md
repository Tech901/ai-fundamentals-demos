# Ideas for NLP Demos

## 1. Brand Reputation and Customer Feedback Analysis

**Real-World Scenario:** Marketing teams often need to track brand reputation
over time by monitoring social media comments or product reviews. For instance,
a company might analyze reviews for a new phone to determine if customers feel
positively about the camera but negatively about the battery life. This allows
businesses to pinpoint specific areas for product improvement without manually
reading thousands of reviews.

- **Applicable Product:** Azure AI Language
  - **Specific Features:** Sentiment Analysis and Key Phrase Extraction
- **Demo Idea:** Use the Language Studio to input a mixed-review paragraph
  (e.g., "The food was delicious, but the service was slow"). Show students how
  the service returns an overall sentiment score (Positive/Negative/Neutral)
  and extracts key phrases like "food" and "service" with confidence scores.

## 2. Automating Data Extraction from Legal and Financial Documents

**Real-World Scenario:** In legal or financial sectors, professionals often
need to sift through massive amounts of unstructured text to find specific
people, organizations, or dates. For example, a system can automatically tag
names, locations, and contract dates in legal documents, or identify financial
figures in reports, reducing the need for tedious manual review.

- **Applicable Product:** Azure AI Language (specifically Named Entity
  Recognition) or Azure AI Foundry
  - **Specific Features:** Named Entity Recognition (NER) and Personally
    Identifiable Information (PII) Detection
- **Demo Idea:** Input a sample contract or a medical report into Azure AI
  Foundry (formerly Azure AI Studio). Demonstrate how the NER feature
  highlights entities like "John Doe" (Person), "October 10, 2024" (Date), or
  sensitive data like Social Security numbers for redaction.

## 3. Breaking Language Barriers in Global Communications

**Real-World Scenario:** Global organizations and social media platforms must
bridge linguistic gaps to connect people. This includes translating government
documents for accessibility or providing instant "click-to-translate" buttons
on social media posts. This allows for real-time, cross-language conversations
and content consumption.

- **Applicable Product:** Azure AI Translator
  - **Specific Features:** Text Translation and Document Translation
- **Demo Idea:** Use Azure AI Translator to perform a synchronous translation
  of a JSON file or a text string from English to languages like French or
  Italian. Show how the service detects the input language automatically and
  provides a confidence score alongside the translation.

## 4. 24/7 Intelligent Customer Support Bots

**Real-World Scenario:** Companies need to keep up with customer demands for
fast responses outside of business hours. Conversational AI, or "bots," can
troubleshoot issues, answer FAQs, and guide users using natural language. A
well-informed bot connects to a company's knowledge base (like an FAQ page or
user manual) to provide accurate answers without human intervention.

- **Applicable Product:** Azure AI Language (Question Answering)
  - **Specific Features:** Conversational Language Understanding (CLU) and
    Question Answering
- **Demo Idea:** In Language Studio, create a "Custom Question Answering"
  project. Import a URL from a public FAQ page (e.g., a Microsoft support page)
  as the knowledge base. Test the bot via the chat interface by asking natural
  language questions like "Is there SDK support?" to show how it retrieves the
  correct answer from the ingested source material.
