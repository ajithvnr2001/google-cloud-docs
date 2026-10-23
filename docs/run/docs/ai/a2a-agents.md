---
url: https://docs.cloud.google.com/run/docs/ai/a2a-agents/
title: Overview of A2A agents on Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:34.072527+00:00
---

# Overview of A2A agents on Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/ai/a2a-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Overview of A2A agents on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Agent2Agent (A2A)**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run lets you deploy and scale Agent2Agent (A2A) agents as Cloud Run services. This architecture helps you run autonomous multi-agent workflows that collaborate and exchange tasks across distributed environments.

For an introduction to foundational protocol concepts, see [Key Concepts in A2A](https://a2a-protocol.org/latest/topics/key-concepts/).

## Relationship of AI Agents and the A2A Protocol

**AI Agents** are software programs that can perceive their environment, make decisions, and take autonomous actions to achieve specific goals. These agents are becoming increasingly sophisticated, often leveraging Large Language Models (LLMs) for complex tasks like reasoning, planning, and natural language interactions.

As more specialized AI agents are developed, the need for them to communicate and collaborate becomes essential. The **Agent2Agent (A2A) Protocol** is an open standard designed to enable seamless and secure communication and interoperability between AI agents, even if they are built using different frameworks, by different vendors, or are running on separate servers. A2A allows agents to work together as peers without exposing their internal state or logic.

The following diagram illustrates the architecture of an A2A Agent system, showing an A2A Client (user or agent) interacting with the A2A Agent:

![An agent interacting with other agents, hosted on
    Cloud Run. ](https://docs.cloud.google.com/static/run/docs/images/host-a2a-agents.svg)**Figure 1.** Components of an A2A agents hosted on Cloud Run.

The A2A Agent's core is a serving and orchestration layer, such as Cloud Run. This layer manages interactions with AI models like Gemini and Vertex AI, memory storages like AlloyDB and A2A TaskStore, and external tools through APIs. Clients interact with the agent by sending requests, such as "Get Agent Card" or "send message," and receive task updates.

For information about A2A request lifecycle, see the [A2A Request Lifecycle](https://a2a-protocol.org/latest/topics/what-is-a2a/#a2a-request-lifecycle) section.

## What's next

  * To learn the practical steps for deploying your own A2A agents, see [Build and deploy an A2A agent on Cloud Run](https://docs.cloud.google.com/run/docs/deploy-a2a-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
