---
url: https://docs.cloud.google.com/architecture/agentic-ai-classify-multimodal-data/
title: Agentic AI use case: Classify multimodal data \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:31.695615+00:00
---

# Agentic AI use case: Classify multimodal data  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agentic-ai-classify-multimodal-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Agentic AI use case: Classify multimodal data Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-03-03 UTC

This document provides a high-level architecture for a multi-agent AI system deployed on Cloud Run that analyzes disparate multimodal data and produces a high-confidence classification. This approach cross-validates fragmented media by matching live data against historical ground truth to produce grounded, verifiable insights.

The intended audience for this document includes architects, developers, and administrators who build and manage AI infrastructure and applications in the cloud. This document assumes that you have a foundational understanding of AI agents and models. The document doesn't provide specific guidance for designing and coding AI agents.

The Deployment section of this document lists code samples that you can use to learn how to build and deploy multi-agent AI systems.

## Architecture

The following diagram shows the architecture of the multi-agent AI system that uses a [parallel agent design pattern](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#parallel-pattern) to coordinate independent analysis on multimodal data to produce a single classification.

![Architecture of a multi-agent AI system that classifies multimodal data.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-classify-multimodal-data.svg)

![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-classify-multimodal-data.svg)

The architecture shows the following data flow:

  1. The web application sends a request to the root agent to analyze a set of multimodal data for classification. The root agent is a [coordinator agent](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#coordinator-pattern) that receives requests and is deployed on a [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service.
  2. The root agent handles the request in the following way: 
     1. The root agent initiates a [`before_agent_callback`](https://google.github.io/adk-docs/callbacks/types-of-callbacks/#before-agent-callback) to gather environment configurations, validate user input, and save resource paths in a shared [session state](https://google.github.io/adk-docs/sessions/state/). All of the subagents can access the shared session state, which eliminates redundant calls to fetch state data and decreases overall latency.
     2. The root agent uses Gemini on Gemini Enterprise Agent Platform to interpret the user's request and distribute tasks to specialized subagents that run in parallel.
  3. Each subagent is specialized in a particular domain and conducts the following tasks independently: 
     1. The image and video analyst subagents interact with [custom Model Context Protocol (MCP) servers](https://docs.cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server) to perform the following actions: 
        1. Fetch raw unstructured data stored in a Cloud Storage bucket.
        2. Send a request to Gemini to interpret the input data, classify the data, and calculate a confidence level.
        3. Gemini sends the suggested classification and confidence level back to the custom MCP server.
        4. The custom MCP server forwards the response back to the subagent.
     2. The structured data analyst subagent orchestrates analysis by completing the following tasks: 
        1. Interacts with the [BigQuery MCP server](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp) to fetch structured, contextual data (such as historical records, event logs, or sensor readings) stored in a [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs).
        2. The structured data analyst sends a request to Gemini to interpret the input data, classify the data, and calculate a confidence level.
        3. Gemini sends the suggested classification and confidence level back to the subagent.
  4. Each subagent sends the suggested classification and confidence level back to the root agent.
  5. The root agent uses Gemini to summarize the outputs from the specialized subagents to produce a single, high-confidence classification. 
     * If a majority of the classifications from the specialized subagents match, then the root agent sends the matched classification to the web application.
     * If the subagents don't provide a matching classification, then the root agent selects the classification with the highest confidence level and sends it to the web application.



## Products used

This reference architecture uses the following Google Cloud products and tools:

  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Gemini](https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 
  * [ BigQuery](https://cloud.google.com/bigquery): An enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview): Google-managed remote services that implement the [Model Context Protocol (MCP)](https://cloud.google.com/discover/what-is-model-context-protocol) to provide AI applications access to Google and Google Cloud products and services. 
  * [ Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro): An open-source standard for connecting AI applications to external systems.
  * [Agent Development Kit (ADK)](https://google.github.io/adk-docs/): A set of tools and libraries to develop, test, and deploy AI agents.



For information about how to select alternative components for your agentic AI system including framework, agent runtime, tools, memory, and design patterns, see [Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components).

## Use case

This architecture is designed for use cases that synthesize diverse multimodal data for classification and detection tasks. For enhanced accuracy and scalability, the architecture uses a multi-agent AI system instead of a monolithic single-agent approach. This design pattern provides focused instructions, avoids conflicting directives, enables smaller tool sets for faster decisions, and supports independent updates, which leads to more robust and sophisticated outcomes.

The following are examples of use cases for the architecture that's described in this document:

  * **Medical diagnosis** : Provide comprehensive diagnostic assessments by deploying specialized agents to independently analyze medical images, patient symptoms, and lab results. The AI system summarizes these findings based on a determined confidence threshold to provide grounded, verifiable insights for clinicians.
  * **Fraud detection** : Detect and flag potential fraud by deploying agents to independently analyze user behavior patterns and transaction data like scanned receipts and merchant invoices. By cross-referencing visual evidence from documents against digital network activity, the system identifies discrepancies and flags any transactions where a single agent identifies a suspicious indicator.
  * **Document processing** : Automate the classification and extraction of information from documents by deploying specialized agents for [Optical Character Recognition (OCR)](https://cloud.google.com/use-cases/ocr), document classification and data extraction. To support high-confidence processing, the AI system requires all agents to agree on the output.
  * **Quality Control** : Classify product quality or detect anomalies by deploying specialized agents for visual inspection, sensor data analysis, and specification checking. The system determines a pass or fail based on a determined confidence threshold among the agents.



## Design considerations

To implement this architecture for production, consider the following recommendations:

  * **Agent security** : To limit an agent's ability to take dangerous actions, create an [agent identity](https://docs.cloud.google.com/mcp/authenticate-mcp#agent-identity) and then secure access to your MCP servers by using [Identity and Access Management (IAM) attributes](https://docs.cloud.google.com/mcp/control-mcp-use-iam). By applying the [principle of least privilege](https://docs.cloud.google.com/secret-manager/docs/access-control#principle-of-least-privilege), you can help ensure that your agentic AI system performs expected behavior and prevents unintended read-write access to your production resources.
  * **Ingress security:** To control access to the application, [disable the default run.app URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url) of the frontend Cloud Run service and [set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless). In addition to load-balancing incoming traffic to the application, the load balancer handles SSL certificate management. For added protection, use [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#serverless) to provide request filtering, DDoS protection, and rate limiting for the service.
  * **Container image security:** To ensure that only authorized container images are deployed to Cloud Run, use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/run/overview). To identify and mitigate security risks in the container images, automatically run vulnerability scans by using [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs). For more information, see [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).
  * **Cost-effective prompting** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. For more information, see the [best practices for prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#best-practices).
  * **Storage costs:** To control storage costs, you can choose the [Standard storage class](https://docs.cloud.google.com/storage/docs/storage-classes) and enable [object lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) and [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass). These features help you optimize costs by automatically moving or deleting data between storage classes based on your access patterns or rules that you set.
  * **Storage security** : Cloud Storage supports two methods for controlling user access to your buckets and objects: IAM and access control lists (ACLs). In most cases, we recommend using IAM, which lets you grant permissions at the bucket and project levels. For more information, see [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).
  * **Resource allocation:** Depending on your performance requirements, configure the [memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) and [CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu) to be allocated to the Cloud Run service. For more performance optimization guidance, see [General Cloud Run development tips](https://docs.cloud.google.com/run/docs/tips/general#optimize_performance).



For information about design factors and best practices, and for recommendations about building and deploying a multi-agent AI system, see [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system#design_considerations).

## Deployment

To deploy a sample implementation of this architecture, try the [Way Back Home Level 1 codelab](https://codelabs.developers.google.com/way-back-home-level-1/instructions#0).

## What's next

  * Learn how to [host AI agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Learn how to [build and deploy a remote MCP server on Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server).
  * Learn how to [choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)
  * (Video) Watch the [Agent Factory Podcast about building custom tools for agents](https://www.youtube.com/embed/NiLb5DK4_rU).
  * Explore learning resources to build and deploy enterprise-grade agents with [Gemini Enterprise Agent Ready (GEAR)](https://developers.google.com/program/gear).
  * Explore more [agentic AI architecture guides](https://docs.cloud.google.com/architecture/agentic-ai-overview).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer

Other contributors: 

  * [Amina Mansour](https://www.linkedin.com/in/aminamansour/) | Tech Lead, Global Developer Relations & Strategic Content
  * [Andrey Shakirov](https://www.linkedin.com/in/andrey-shakirov-000b4a5/) | Solutions Architect, Google Cloud
  * [Ayo Adedeji](https://www.linkedin.com/in/ayoadedeji/) | Developer Relations Engineer
  * [Christina Lin](https://www.linkedin.com/in/weimeilin/) | Developer Relations Engineer Manager
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Ryan Pei](https://www.linkedin.com/in/ryanpei/) | Product Manager, Google Cloud



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-03 UTC."],[],[]] 
