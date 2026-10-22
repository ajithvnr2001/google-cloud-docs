---
url: https://docs.cloud.google.com/architecture/agentic-ai-interactive-learning/
title: Agentic AI use case: Administer interactive learning \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:45.557743+00:00
---

# Agentic AI use case: Administer interactive learning  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agentic-ai-interactive-learning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Agentic AI use case: Administer interactive learning Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-14 UTC

This document describes a high-level architecture for an application that generates and administers an interactive learning quiz with an agentic AI workflow. The agent assesses a user's knowledge on a specific topic and it uses a persistent session state and long-term memory to create a personalized experience. The agent maintains a history of the user's answers, which lets it dynamically adjust the difficulty and content of subsequent questions.

The intended audience for this document includes architects, developers, and administrators who build and manage agentic AI applications. This architecture is adaptable for creating interactive and stateful educational applications across various industries. The document assumes a foundational understanding of AI agent systems. For information about how agents differ from non-agentic systems, see [What is the difference between AI agents, AI assistants, and bots?](https://cloud.google.com/discover/what-are-ai-agents#what-is-the-difference-between-ai-agents-ai-assistants-and-bots)

The deployment section of this document provides a link to a code sample to help you experiment with deploying an agentic AI application that administers an interactive learning quiz.

## Architecture

The following diagram shows a high-level architecture for an interactive learning agent.

![Architecture for an interactive learning agent.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-interactive-learning.png)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-interactive-learning.png)

The architecture shows the following data flow:

  1. A user performs an action, such as starting a quiz or submitting an answer, within the quiz application that is hosted on Cloud Run.
  2. The application forwards the user's input to the AI agent.
  3. The AI agent uses the Gemini model on Gemini Enterprise Agent Platform to interpret the user's input. Based on the user's request, the agent calls the appropriate tools to perform the requested quiz action.

For example, the agent selects a tool to start a quiz session, evaluate an answer, or generate the next question.

  4. The agent sends the response to the quiz application.

  5. The quiz application forwards the response to the user.




To maintain the quiz's state and personalize the experience, the agent performs the following background tasks:

  * The agent appends the latest quiz progress and score to the history of the saved session that's stored in [Gemini Enterprise Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions).
  * The agent transforms quiz data into memories and stores them in Memory Bank for long-term recall. The agent uses the historical data that's stored in memory to generate context-aware responses in future sessions.



## Products used

This example architecture uses the following Google Cloud and open-source products and tools:

  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [Agent Development Kit (ADK)](https://adk.dev/): A set of tools and libraries to develop, test, and deploy AI agents.
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Gemini Enterprise Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions): A persistent storage service that saves and retrieves the history of interactions between a user and agents. 
  * [ Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank): A persistent storage service that generates, refines, manages, and retrieves long-term memories based on a user's conversations with an agent. 



## Security considerations

To help address the unique security risks of AI agents, Google recommends an [approach](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that combines deterministic security controls with dynamic, reasoning-based defenses:

  * **Human oversight** : Incorporate a human-in-the-loop flow in business-critical systems so human supervisors can review outputs and approve, override, or pause agent actions.
  * **[Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)** : Assign each agent a workload-bound identity to enforce least-privilege access control and centrally manage credentials for external tools.
  * **[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)** : Enforce ingress and egress traffic governance, default-deny access policies, and inline prompt and tool inspection with [Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).
  * **[Agent Registry](https://docs.cloud.google.com/agent-registry/overview)** : Verify that agents only connect to approved subagents and MCP tools.



The guidance in this section isn't exhaustive. For more information about design factors and best practices, and for recommendations about building and deploying a multi-agent AI system, see [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system#design_considerations).

## Deployment

To deploy a sample implementation of this architecture that provides coding-related quizzes, use the [Python tutor code sample](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/python-tutor) that's available in GitHub.

## What's next

  * (Notebook) [Get started with Agent Platform Sessions and Memory Bank for ADK agents in Cloud Run](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/cloud_run/agents_with_memory/get_started_with_memory_for_adk_in_cloud_run.ipynb).
  * (Blog) Learn more about [state and memory with ADK](https://cloud.google.com/blog/topics/developers-practitioners/remember-this-agent-state-and-memory-with-adk).
  * (Codelab) [Build a production AI code review assistant with ADK](https://codelabs.developers.google.com/adk-code-reviewer-assistant/instructions).
  * (Video) Watch [AI agent long-term memory with memory bank](https://www.youtube.com/embed/KZPo15M2DbM?si=no2v-gNqqSKBughI).
  * Learn how to [host AI agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer

Other contributors: 

  * [Amina Mansour](https://www.linkedin.com/in/aminamansour/) | Tech Lead, Global Developer Relations & Strategic Content
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Megan O'Keefe](https://www.linkedin.com/in/askmeegs) | Developer Advocate
  * [Rachael Deacon-Smith](https://www.linkedin.com/in/rachael-ds/) | Developer Advocate
  * [Shir Meir Lador](https://www.linkedin.com/in/shirmeirlador) | Developer Relations Engineering Manager



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
