
# 🔐 Skyflow Privacy Agent + LLM Workflow with LlamaIndex

This project showcases a full **agentic workflow implementation** using [LlamaIndex](https://www.llamaindex.ai/), designed to protect sensitive user data using Skyflow, and generate intelligent responses using OpenAI's GPT-4.

It consists of **two modular agents**:
- A **PrivacyPreservingAgent** that deidentifies input using Skyflow’s Detect API.
- An **LLMAgent** that processes the deidentified data using OpenAI's LLM.

These are chained together in a workflow that first deidentifies any sensitive data, then forwards the clean output to an LLM for response generation.

---

## 🧠 Workflow Overview

```
User Input (with sensitive info)
     │
     ▼
PrivacyPreservingAgent (Skyflow Detect)
     │ processed_text
     ▼
LLMAgent (OpenAI GPT-4)
     │
     ▼
 Final Response
```

---

## 📁 Project Structure

```
multi_agent_workflow/
├── agents/
│   ├── privacy_agent.py        # Handles Skyflow deidentification
│   └── llm_agent.py            # Handles OpenAI prompt generation
├── workflows/
│   └── multi_agent_workflow.py # Chains the agents
├── main.py                     # Entry point
├── .env                        # API secrets
├── requirements.txt            # Project dependencies
└── README.md                   # You are here!
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi_agent_workflow.git
cd multi_agent_workflow
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root folder and add the following:

```
OPENAI_API_KEY=your_openai_api_key
SKYFLOW_ACCOUNT_ID=your_skyflow_account_id
BEARER_TOKEN=your_skyflow_bearer_token
VAULT_ID=your_vault_id
URL=https://your_skyflow_url
```

### 5. Run the Workflow

```bash
python main.py
```

You will see the deidentified version of your input and a response from the LLM.

---

## 💡 Why Use This?

- ✅ Keeps sensitive data secure via tokenization
- ✅ LLM only receives privacy-safe text
- ✅ Modular agents allow for plug-and-play customization
- ✅ Uses LlamaIndex’s latest `AgentWorkflow` for multi-agent orchestration

---

## 📦 Future Roadmap

- [x] Implement Skyflow PrivacyPreservingAgent
- [x] Integrate LLM Agent using OpenAI GPT-4
- [x] Chain them via `AgentWorkflow`
- [ ] ✅ Publish `SkyflowPrivacyAgent` as an official tool on [LlamaIndex GitHub](https://github.com/jerryjliu/llama_index)
  
---

## ✍️ Want to Contribute?

We’d love to contribute this to the official LlamaIndex repo. If you'd like to help:

1. Fork the [llama_index](https://github.com/jerryjliu/llama_index) repo
2. Add `SkyflowPrivacyAgent` to `llama_index/tools`
3. Include documentation + example usage
4. Submit a PR titled: `feat(agent): Add SkyflowPrivacyAgent for privacy-preserving LLM workflows`
