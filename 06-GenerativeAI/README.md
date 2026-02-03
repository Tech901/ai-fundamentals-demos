# Generative AI Workloads on Azure - Demo Ideas

Based on Chapter 8: *Features of Generative AI Workloads on Azure* from the provided study guide, here is a list of demo ideas tailored for your lecture. These demos are designed to practically illustrate the core concepts of the AI-900 exam, specifically focusing on Azure OpenAI Studio and Responsible AI.

---

## 1. The "Persona" Demo (Prompt Engineering & System Messages)

**Concept:** This demonstrates how System Messages guide the behavior and tone of the model, a key component of the "Metaprompt" layer in responsible AI. It also illustrates the Chat Playground interface.

- **The Setup:** Open Azure OpenAI Studio and navigate to the Chat playground.
- **The Action:**
  1. Leave the "System message" blank (or default) and ask: "What is a generative AI model?" Note the standard, factual response.
  2. Change the "System message" to the example provided in the text: "Shakespearean Writing Assistant".
  3. Ask the same question again.
  4. Show the output (e.g., "A generative AI, thou asketh, is a wondrous creation...").
- **Talking Point:** Explain that the model is not just "looking up" answers; it is generating new content based on the constraints (persona) you provided. This illustrates how developers can customize the "personality" of an AI agent for specific business needs (e.g., a formal legal assistant vs. a casual travel buddy).

---

## 2. The "Grounding" Demo (Retrieval-Augmented Generation / RAG)

**Concept:** This illustrates the "Bring your own data" feature, which is critical for enterprise use cases where the model must answer based on proprietary data rather than general internet knowledge. The study guide refers to this as *grounding*.

- **The Setup:** In Azure OpenAI Studio, locate the "Bring your own data" tile.
- **The Action:**
  1. Upload a specific, unique document (e.g., a fictional HR policy that says "Employees get free pizza on Tuesdays").
  2. Ask the model: "What is the policy on free food?"
  3. Show how the model cites the uploaded document in its answer.
- **Talking Point:** Explain that this technique prevents hallucinations (making things up) by restricting the model to trusted sources. It is essential for internal business chatbots.

---

## 3. The "Visual Creativity" Demo (DALL-E Image Generation)

**Concept:** This demonstrates the capabilities of DALL-E for generating original images from text descriptions, a key feature of Azure's Generative AI workload.

- **The Setup:** Navigate to the Images playground (DALL-E) in Azure OpenAI Studio.
- **The Action:**
  1. Enter the prompt suggested in the study guide: "Design an inviting book cover for a cozy mystery novel set in a small town".
  2. Generate the image.
  3. Refine the prompt (e.g., "Make it in the style of a watercolor painting") to show how iteration changes the output.
- **Talking Point:** Discuss how this is used for marketing, storyboarding, and rapid prototyping. Emphasize that the AI is generating pixels from scratch, not searching for an existing image on Google.

---

## 4. The "Safety First" Demo (Content Filtering)

**Concept:** This covers the Responsible AI section of the exam, specifically the Safety System Layer and Content Safety filters.

- **The Setup:** In Azure OpenAI Studio, navigate to the Content Filters configuration tab.
- **The Action:**
  1. Show the audience the configurable categories: Hate, Self-Harm, Sexual, and Violence.
  2. Demonstrate the severity thresholds (Safe, Low, Medium, High).
  3. *Optional:* Instead of generating harmful content (which is risky in a demo), simply lower the threshold to "Low" for a category and explain that even mild infractions would now be blocked by the Azure platform before the user ever sees them.
- **Talking Point:** Explain that Microsoft Azure provides these "guardrails" at the platform level so developers don't have to build their own toxicity filters from scratch. This helps mitigate risks identified during the "Assess" phase of the Responsible AI framework.

---

## 5. The "Tokenizer" Demo (How LLMs Read)

**Concept:** This illustrates Tokenization, the process of breaking text into numeric tokens, which is the foundational step for Transformer models.

- **The Setup:** Use the [OpenAI Tokenizer tool](https://platform.openai.com/tokenizer) (or a visualization of it) mentioned in Chapter 8.
- **The Action:**
  1. Paste the sentence from the study guide: "Artificial intelligence like machine learning and natural language processing...".
  2. Show how the tool breaks words into chunks (e.g., "Artificial" might be one token, but complex words or spaces might be split).
  3. Click to reveal the Token IDs (the vector numbers like `[186671, 22990...]`).
- **Talking Point:** Explain that the model doesn't "read" English; it processes these numbers to predict the next likely number in the sequence. This demystifies the "magic" of the Transformer architecture.

---

## 6. The "Microsoft Copilot" Demo (Web-Based Assistant)

**Concept:** If you cannot access the Azure portal, this demonstrates Copilots as a SaaS implementation of Generative AI.

- **The Setup:** Open the Microsoft Edge browser sidebar, the Copilot app in Windows, or go to the [Copilot website](https://copilot.microsoft.com).
- **The Action:**
  1. Use the "Compose" tab to write a short email or blog post.
  2. Toggle the "Tone" settings (Professional vs. Casual vs. Funny).
  3. Show how the output changes instantly.
- **Talking Point:** This illustrates how Generative AI is embedded into daily workflows to boost productivity, a key distinction between raw models (like in Azure OpenAI Studio) and finished applications (Copilots).

---

## 7. The "GitHub Copilot" Demo

### VSCode

**Concept:** Usage of agentic software development in VS Code.

- **The Setup:** Open VS Code with the GitHub Copilot extension installed. Ensure you are signed in to your GitHub account with an active Copilot subscription.
- **The Action:**
  1. Open a new file and start typing a function signature (e.g., `function calculateTax(income, rate) {`).
  2. Wait for Copilot to suggest code completion in gray text, then press Tab to accept.
  3. Open Copilot Chat (Ctrl+Shift+I) and ask it to explain or refactor the code.
  4. Use Agent Mode to request a multi-file change (e.g., "Create a REST API endpoint for user registration").
- **Talking Point:** Explain how GitHub Copilot acts as an AI pair programmer, understanding context from your codebase to provide relevant suggestions. This demonstrates the shift from chat-based AI to agentic AI that can take autonomous actions within your development environment.

### copilot-cli

**Concept:** Usage of agentic software development in WSL using a CLI.

- **The Setup:** Install GitHub Copilot CLI in your WSL environment using `gh extension install github/gh-copilot`. Authenticate with `gh auth login`.
- **The Action:**
  1. Run `ghcs` (GitHub Copilot in the Shell) and ask: "How do I find all files larger than 100MB in this directory?"
  2. Show how Copilot suggests the correct shell command and explains what it does.
  3. Run `ghce` (GitHub Copilot Explain) on a complex command to demonstrate code explanation.
  4. Use the interactive agent mode to perform a multi-step task like "Create a Python virtual environment and install Flask".
- **Talking Point:** This demonstrates how Generative AI extends beyond traditional IDEs into command-line workflows. Developers can leverage natural language to generate shell commands, reducing the cognitive load of remembering complex syntax across different tools.

---

## 8. Easy "local AI" with Jan

**Concept:** Usage of a _local_ (or remote) LLM provider through a locally running UI.

- **The Setup:** Install [Jan.ai](https://www.jan.ai/), and deploy a model such as `gpt-4.1-mini` in Azure OpenAI service. Configure Jan to connect to your Azure OpenAI endpoint using the API key and endpoint URL.
- **The Action:**
  1. Download and run a local model (e.g., Llama 3 or Mistral) directly within Jan to demonstrate offline AI capabilities.
  2. Switch to your Azure OpenAI connection and ask the same question to compare response quality.
  3. Show how Jan provides a unified interface for both local and cloud-based models.
  4. Demonstrate a privacy-sensitive use case where data never leaves your machine using the local model.
- **Talking Point:** Explain the trade-offs between local and cloud AI: local models offer privacy and offline access but require hardware resources, while cloud models like Azure OpenAI provide more powerful capabilities with enterprise-grade security. This illustrates how organizations can choose deployment options based on their specific requirements for privacy, performance, and cost.

