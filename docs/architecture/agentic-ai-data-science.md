---
url: https://docs.cloud.google.com/architecture/agentic-ai-data-science/
title: Agentic AI use case: Automate data science workflows \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:43.898214+00:00
---

# Agentic AI use case: Automate data science workflows  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agentic-ai-data-science/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Agentic AI use case: Automate data science workflows Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-14 UTC

This document describes a high-level architecture for an application that runs a data science workflow to automate complex data analytics and machine learning tasks.

This architecture uses datasets that are hosted in BigQuery or AlloyDB for PostgreSQL. The architecture is a multi-agent system that lets users run actions in natural language commands and it eliminates the need to write complex SQL or Python code.

The intended audience for this document includes architects, developers, and administrators who build and manage agentic AI applications. This architecture lets business and data teams analyze metrics across a wide range of industries, such as retail, finance, and manufacturing. The document assumes a foundational understanding of agentic AI systems. For information about how agents differ from non-agentic systems, see [What is the difference between AI agents, AI assistants, and bots?](https://cloud.google.com/discover/what-are-ai-agents#what-is-the-difference-between-ai-agents-ai-assistants-and-bots)

## Architecture

The following diagram shows the architecture for a data science workflow agent.

![Architecture for a data science workflow agent.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-data-science.png)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-data-science.png)

This architecture includes the following components:

Frontend
     Users interact with the multi-agent system through a frontend, such as a chat interface, that runs as a serverless [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service. 
AI model and model runtimes
     For inference serving, the agents in this example architecture use the latest [Gemini model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models) on [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start). 
Agents
    

This architecture uses the following agents:

  * **Root agent** : A [coordinator agent](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#coordinator-pattern) that receives requests from the frontend service. The root agent interprets the user's request and it attempts to resolve a request itself. If the task requires specialized tools, the root agent delegates the request to the appropriate specialized agent.
  * **Specialized agent** : The root agent invokes the following specialized agents by using the [agent as a tool](https://adk.dev/tools-custom/function-tools/#agent-tool) feature: 
    * **Analytics agent** : A specialized agent for data analysis and visualization. The analytics agent uses the AI model to generate and run Python code to process datasets, create charts, and perform statistical analysis.
    * **AlloyDB for PostgreSQL agent** : A specialized agent for interacting with data in AlloyDB for PostgreSQL. The agent uses the AI model to interpret the user's request and to generate SQL in the PostgreSQL dialect. The agent securely [connects to the database using MCP Toolbox for Databases](https://docs.cloud.google.com/alloydb/docs/connect-ide-using-mcp-toolbox#configure-your-mcp-client) and then it runs the query to retrieve the requested data.
    * **BigQuery agent** : A specialized agent for interacting with data in BigQuery. The agent uses the AI model to interpret the user's request and generate [GoogleSQL](https://docs.cloud.google.com/bigquery/docs/introduction-sql) queries. The agent connects to BigQuery using [Agent Development Kit (ADK)'s built-in BigQuery tool](https://adk.dev/integrations/bigquery/) and then it runs the query to retrieve the requested data.
  * **BigQuery ML agent** : A subagent of the root agent that is dedicated to machine learning workflows. The agent interacts with [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) to manage the end-to-end ML lifecycle. The agent can create and train models, run evaluations, and generate predictions based on user requests.


Agents runtime
     The AI agents in this architecture are deployed as [serverless Cloud Run services ](https://docs.cloud.google.com/run/docs/ai-agents). 
ADK
     [ADK](https://adk.dev/) provides tools and a framework to develop, test, and deploy agents. ADK abstracts the complexity of agent creation and lets AI developers focus on the agent's logic and capabilities. 

## Products used

This example architecture uses the following Google Cloud and open-source products and tools:

  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [Agent Development Kit (ADK)](https://adk.dev/): A set of tools and libraries to develop, test, and deploy AI agents.
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Gemini](https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 
  * [ BigQuery](https://cloud.google.com/bigquery): An enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence. 
  * [ AlloyDB for PostgreSQL](https://cloud.google.com/alloydb): A fully managed, PostgreSQL-compatible database service that's designed for your most demanding workloads, including hybrid transactional and analytical processing. 
  * [ MCP Toolbox for Databases](https://mcp-toolbox.dev/documentation/introduction/): An open-source [ Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) server that lets AI agents securely connect to databases by managing database complexities like connection pooling, authentication, and observability.



## Security considerations

To help address the unique security risks of AI agents, Google recommends an [approach](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that combines deterministic security controls with dynamic, reasoning-based defenses:

  * **Human oversight** : Incorporate a human-in-the-loop flow in business-critical systems so human supervisors can review outputs and approve, override, or pause agent actions.
  * **[Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)** : Assign each agent a workload-bound identity to enforce least-privilege access control and centrally manage credentials for external tools.
  * **[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)** : Enforce ingress and egress traffic governance, default-deny access policies, and inline prompt and tool inspection with [Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).
  * **[Agent Registry](https://docs.cloud.google.com/agent-registry/overview)** : Verify that agents only connect to approved subagents and MCP tools.



The guidance in this section isn't exhaustive. For more information about design factors and best practices, and for recommendations about building and deploying a multi-agent AI system, see [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system#design_considerations).

## What's next

  * (Video) Watch [Agent Factory Podcast about AI agents for data engineering and data science](https://www.youtube.com/embed/ATgIU47V1yI?si=vbsBQltnUzInQUXG).
  * (Notebook) [Use the data science agent in Colab Enterprise](https://docs.cloud.google.com/colab/docs/use-data-science-agent).
  * Learn about how to [host AI agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
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
