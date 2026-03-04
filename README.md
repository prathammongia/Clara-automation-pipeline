# Clara Answers – Automation Pipeline Assignment

## Overview

This project implements a **zero-cost automation pipeline** that converts customer call transcripts into structured operational rules and generates a preliminary **Retell AI agent configuration**.

The system simulates Clara’s real-world onboarding workflow:

Demo call → preliminary AI agent → onboarding update → revised agent configuration.

The pipeline processes both **demo calls and onboarding calls**, generates versioned outputs, and produces a clear changelog describing updates between versions.

All tools used in this project are **free and locally runnable**, satisfying the assignment constraint of zero paid services.

---

# Architecture

The system contains two main automation pipelines.

## Pipeline A – Demo Call → Preliminary Agent (v1)

Input
Demo call transcript

Process
Transcript → Data extraction → Structured account memo → Agent configuration generation

Output
Account memo JSON
Retell agent configuration (v1)

---

## Pipeline B – Onboarding Call → Agent Update (v2)

Input
Onboarding transcript or form

Process
Extract updates → Apply patch to existing memo → Generate updated agent

Output
Updated account memo (v2)
Updated agent configuration (v2)
Changelog describing changes

---

# System Architecture Diagram

Transcript
↓
Extraction Script
↓
Account Memo JSON
↓
Agent Prompt Generator
↓
Store Outputs (v1)
↓
Onboarding Update
↓
Patch Existing Memo
↓
Generate Agent v2
↓
Store Outputs + Changelog

---

# Project Structure

```
clara-agent-automation
│
├── workflows
│
├── scripts
│   extract_data.py
│   generate_agent.py
│   update_agent.py
│   run_pipeline.py
│
├── dataset
│   ├── demo_calls
│   └── onboarding_calls
│
├── outputs
│   └── accounts
│       └── <account_id>
│           ├── v1
│           └── v2
│
├── changelog
│
└── README.md
```

---

# Data Schema

Each account produces a structured **Account Memo JSON**.

Example:

```
{
  "account_id": "acct_1",
  "company_name": "Metro Fire Protection",
  "business_hours": {
    "start": "8am",
    "end": "5pm"
  },
  "services_supported": [
    "sprinkler services",
    "fire alarm services"
  ],
  "emergency_definition": [
    "sprinkler leak",
    "fire alarm triggered"
  ],
  "questions_or_unknowns": []
}
```

---

# Agent Configuration

The pipeline generates a **Retell agent specification** including:

• agent name
• voice style
• system prompt
• routing rules
• transfer protocol
• fallback protocol

Example structure:

```
{
  "agent_name": "acct_1_agent",
  "voice_style": "professional",
  "version": "v1",
  "system_prompt": "...generated prompt...",
  "variables": {...}
}
```

---

# Setup Instructions

## 1. Clone the Repository

```
git clone <repository_url>
cd clara-agent-automation
```

---

## 2. Create Python Environment

```
python -m venv venv
```

Activate:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

## 3. Add Dataset Files

Place demo transcripts inside:

```
dataset/demo_calls
```

Place onboarding transcripts inside:

```
dataset/onboarding_calls
```

---

## 4. Run the Pipeline

Navigate to scripts directory:

```
cd scripts
```

Run:

```
python run_pipeline.py
```

The pipeline will automatically process transcripts and generate outputs.

---

# Output Structure

Outputs are stored as:

```
outputs/accounts/<account_id>/v1
outputs/accounts/<account_id>/v2
```

Example:

```
outputs/accounts/acct_1/v1/memo.json
outputs/accounts/acct_1/v1/agent.json

outputs/accounts/acct_1/v2/memo.json
outputs/accounts/acct_1/v2/agent.json
```

---

# Changelog

Each onboarding update generates a changelog file describing the modifications.

Example:

```
changelog/acct_1.txt

business_hours updated
emergency_definition updated
```

---

# Automation Characteristics

The pipeline was designed with the following goals:

• Repeatable execution
• Idempotent processing
• Versioned outputs
• Clear separation of demo assumptions vs onboarding confirmation
• No hallucinated data

Missing information is stored in:

```
questions_or_unknowns
```

---

# Known Limitations

• Extraction is currently keyword-based.
• Business hours detection may not capture complex formats.
• No automatic speech-to-text pipeline included.

---

# Future Improvements

• Integrate Whisper for local audio transcription
• Use NLP models for more accurate extraction
• Add dashboard for agent configuration review
• Implement diff viewer for memo comparison

---

# Notes

All processing is performed locally and does not require any paid APIs or services.

This project demonstrates a reproducible automation pipeline capable of transforming real-world conversation data into deployable AI agent configurations.
