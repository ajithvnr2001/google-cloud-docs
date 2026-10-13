---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent/
title: Create an agent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:21.553627+00:00
---

# Create an agent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Create an agent Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Agent Platform supports deploying agents built with various frameworks. To get started, you must first develop an agent that can be deployed on the platform.

You can also use Google-built prebuilt agents, such as [CodeMender](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender) for autonomous code security and [Gemini Deep Research Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/use-deep-research) for multi-step research synthesis, or start from prebuilt samples in [Agent Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden).

The Agents API enables developers to build and deploy agents from configuration. These agents run within a secured Linux-based sandbox, leveraging the Antigravity harness and providing access to tools and skills. For more information on managed agents, see [Managed Agents API on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents).

The easiest way to develop an agent is to use one of the framework-specific templates that we provide. These templates handle common aspects of agent development, such as serializing objects and separating initialization code from execution code. We provide templates for the following frameworks:

Framework | Description  
---|---  
[Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-adk-agent) | Designed based on Google's internal best practices for developers building AI applications or teams needing to rapidly prototype and deploy robust agent-based solutions.  
[Agent2Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-a2a-agent) (preview) | The [Agent2Agent (A2A) protocol](https://a2a-protocol.org/) is an open standard designed to enable seamless communication and collaboration between AI agents.  
[LangChain](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-langchain-agent) | Easier to implement for basic use cases because of its predefined configurations and abstractions.  
[LangGraph](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-langgraph-agent) | Graph-based approach to defining workflows, with advanced human-in-the-loop and rewind/replay capabilities.  
[AG2 (formerly AutoGen)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-an-ag2-agent) | AG2 provides multi-agent conversation framework as a high-level abstraction for building LLM workflows.  
[LlamaIndex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-llamaindex-agent) (preview) | LlamaIndex's query pipeline offers a high-level interface for creating Retrieval-Augmented Generation (RAG) workflows.  
  
If your use case doesn't align with one of the framework-specific templates, you can [develop your own custom agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-custom-agent).

## Agent2Agent (A2A) protocol

If you are building a multi-agent system, we highly recommend reviewing the [A2A Protocol](https://a2a-protocol.org/). A2A Protocol is an open standard that enables seamless communication and collaboration between AI agents, regardless of their underlying frameworks. It was [donated by Google Cloud to the Linux Foundation in June 2025](https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/). To use the A2A SDKs, or try out the samples, check out the [GitHub repository](https://github.com/a2aproject/A2A).

## Building for the platform

When creating an agent to run on the Agent Platform, keep in mind that your agent is executed in a managed environment. To ensure compatibility, follow these patterns:

  * **Object serialization** : The platform serializes your agent object to deploy it. Ensure that your agent state and tools are serializable (for example, avoid keeping open file handles or network sockets in the agent state).
  * **Lifecycle separation** : Separate your agent's initialization logic (loading models, setting up tools) from its execution logic (handling queries). The provided templates handle this automatically.



## What's next

Guide 

###  [ Create a custom agent ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime/create-a-custom-agent)

Create a custom agent using Agent Platform Runtime. 

Overview 

###  [ Managed Agents API on Agent Platform overview ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents)

Learn about Managed Agents API on Agent Platform, a config-driven, REST-first environment for building autonomous agents. 

Guide 

###  [ Deploy agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent)

Learn the five ways to deploy an agent on Agent Platform Runtime based on your development needs. 

Guide 

###  [ Evaluate your agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-agents)

Create and deploy a basic agent and use the Gen AI evaluation service to evaluate the agent 

Resource 

###  [ Get support ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-support)

Find resources and support for Google Agent Platform. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
