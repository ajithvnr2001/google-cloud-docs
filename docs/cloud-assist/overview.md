---
url: https://docs.cloud.google.com/cloud-assist/overview/
title: Gemini Cloud Assist overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:56.214200+00:00
---

# Gemini Cloud Assist overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Gemini Cloud Assist overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/service-terms), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).

Gemini Cloud Assist serves as your AI-powered collaborator, helping you move from reactive troubleshooting to proactive, autonomous cloud operations. By integrating deeply into the cloud platform, Gemini Cloud Assist simplifies the end-to-end application lifecycle, offering intelligent, agentic guidance for designing, deploying, troubleshooting, and optimizing your workloads.

Gemini Cloud Assist is a multi-agent ecosystem capable of dynamic reasoning, executing iterative tool calls, and maintaining long-term memory across complex tasks. It not only understands your cloud infrastructure but also your application code, organizational policies, and real-time operational state.

This document shows the types of generative AI assistance that are available to all Google Cloud users and available to [Gemini Code Assist Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/overview) users. Learn about [Gemini Cloud Assist pricing](https://cloud.google.com/products/gemini/pricing).

The Gemini large language models (LLMs) that are used by Gemini Code Assist are trained on datasets of publicly available code, Google Cloud-specific material, and other relevant technical information in addition to the datasets used to train the Gemini [foundation models](https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf). Models are trained so that Gemini Code Assist responses are as useful to Gemini Code Assist users as possible.

Additionally, Gemini Cloud Assist uses the following details as context when generating responses and assistance:

  * Your Google Cloud project ID and organization ID.
  * **Page context awareness** : The current Google Cloud product page you are viewing in the Google Cloud console, including the page URL and all visible text on the screen. This helps ensure responses are highly contextualized and helps eliminate hallucinations.
  * **Memory** : Gemini Cloud Assist leverages memory to store session histories, prioritize key details, and maintain context across complex tasks and multiple turns.



Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## AI assistance with Gemini Cloud Assist

The following sections describe the types of generative AI assistance that Gemini Cloud Assist offers.

### Design and build

The following table shows the types of generative AI assistance for building and designing applications:

Feature | Available to all Google Cloud users | Code Assist Enterprise  
---|---|---  
[**Natural language design**](https://docs.cloud.google.com/cloud-assist/design-application). Design, configure, provision, and manage complex cloud architectures using natural language interaction within the Application Design Center. |  |   
[**Infrastructure as code (IaC)**](https://docs.cloud.google.com/cloud-assist/design-application). Iteratively generate or refine Google Cloud CLI commands, `kubectl` manifests, and Terraform code for infrastructure and organizational policies through interactive conversations in App Design Center and Gemini Cloud Assist chat, and simulate the generated policies directly within chat. |  |   
[**Identity and Access Management (IAM)**](https://docs.cloud.google.com/iam/docs/role-picker-gemini). Simplify IAM tasks by selecting roles, understanding policies, or generating them using natural language or guided flows. |  |   
[**Google Cloud console chat**](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/try-gemini#chat). Get answers to general questions, best practices, and basic how-to information for Firebase products and services in chat, using project context. |  |   
  
### Support and troubleshoot

The following table shows the types of generative AI assistance for diagnosing and resolving issues:

Feature | Available to all Google Cloud users | Code Assist Enterprise  
---|---|---  
[**Investigations**](https://docs.cloud.google.com/cloud-assist/investigations). Diagnose complex issues by creating and managing AI-driven investigations based on logs, errors, or natural language prompts. Acting as a user-guided site reliability engineer (SRE), Gemini Cloud Assist can ingest logs, metrics, and configurations to explore multiple hypotheses in parallel and trace root causes across multi-tier topologies. |  |   
**Proactive alert investigations**. Configure Cloud Alerting policies to automatically trigger Gemini Cloud Assist. When an alert is triggered, Gemini Cloud Assist analyzes the issue in the background, clusters related alerts, and generates a preliminary root-cause analysis with recommended next steps. |  |   
[**Support handoff**](https://docs.cloud.google.com/cloud-assist/investigations). Escalate investigations or complex issues by connecting directly with Google Cloud support and providing investigation results as context in the support case. |  | If enrolled in a [support package](https://docs.cloud.google.com/support)  
**AI-powered support**. As the primary entry point for support, Gemini Cloud Assist streamlines the support experience by summarizing environment states and error logs for rich context. Gemini Cloud Assist integrates AI investigation tools to help you resolve issues before escalating to a human agent. When automated capabilities or quotas are reached, the agent seamlessly passes the issue to human support engineers. Fields are automatically filled with information from the chat conversation. |  | If enrolled in a [support package](https://docs.cloud.google.com/support)  
**Database and analytics troubleshooting**. AI-powered troubleshooting workflows to empower developers and simplify the resolution of complex performance issues across multiple data services, including [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/observe-troubleshoot-with-ai), [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/observe-troubleshoot-with-ai), AlloyDB for PostgreSQL, BigQuery, Managed Service for Apache Spark, and Spanner. Gemini Cloud Assist helps users identify slow SQL queries, manage slot reservations and capacity, troubleshoot performance bottlenecks, and configure data environments. |  |   
**Application code troubleshooting**. Investigations go beyond infrastructure. For services like Cloud Run, Gemini Cloud Assist can trace root causes from infrastructure signals directly down to application code, identifying issues across both code and infrastructure.  |  |   
[**Artifact Analysis**](https://docs.cloud.google.com/artifact-analysis/docs/explore-vulnerabilities-with-gemini-assistance). Ask questions about vulnerabilities identified by Artifact Analysis.  |  |   
[**Artifact Registry**](https://docs.cloud.google.com/artifact-registry/docs/docker/learn-about-your-container-images-with-gemini-assistance). List your Artifact Registry repositories and container images stored in Docker-format repositories.  |  |   
**Security worker**. A proactive agent that helps non-security professionals triage and remediate security findings from Security Command Center by translating complex security risks into clear, actionable steps to resolve external resource exposure, help secure service accounts, and improve overall compliance.  |  |   
[**Developer Connect insights**](https://docs.cloud.google.com/developer-connect/docs/insights) ([Preview](https://cloud.google.com/products#product-launch-stages)). Learn more about your software development lifecycle and diagnose problems with your applications.  |  |   
[**Google Cloud Observability**](https://docs.cloud.google.com/stackdriver/docs). Monitor system health and troubleshoot issues by exploring metrics, logs, alerts, and errors using natural language within Google Cloud Observability. |  |   
[**Firebase troubleshooting assistance**](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/try-gemini). Troubleshoot specific Firebase product issues using AI-driven expertise and guidance tailored to project context. |  |   
  
### Optimize

The following table shows the types of generative AI assistance for optimizing cost and usage:

Feature | Available to all Google Cloud users | Code Assist Enterprise  
---|---|---  
**Cost optimization for applications, SKUs, products, resources, and workloads**. Ask natural language questions in the chat panel to get precise answers about your cloud spend. This feature extends [Cloud Hub Optimization](https://docs.cloud.google.com/hub/docs/optimize) and [Cost Explorer](https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs). |  |   
[**Cost optimization in FinOps Hub**](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview). Optimize cloud spend by analyzing costs, trends, waste, and utilization with tailored FinOps views. Also includes AI-drafted summaries for collaboration. |  |   
**Proactive cost anomaly analysis**. Detected cost anomalies can proactively trigger an analysis to explain the root cause of a cost change. This analysis runs once a day when an anomaly is detected in a project. The agent analyzes the cost spike, analyzes products, SKUs, and resources to identify the infrastructure changes that caused the cost spike along with the user / service account responsible for those changes. When applicable, the agent proposes potential strategies to fix such cost spikes. Gemini Cloud Assist can make mistakes, so double-check any proposed strategies before implementing them. |  |   
[**Database optimization**](https://docs.cloud.google.com/database-center/docs/learn-database-products-using-gemini#use-gemini-cloud-assist). AI-driven insights to optimize database costs and potentially achieve savings by configuring instances based on usage patterns. |  |   
[**Flow analyzer**](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/write-queries-gemini). Analyze network flows and configurations using natural language queries within the Network Intelligence Center. |  |   
[**Storage Insights**](https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist). Understand and manage storage services by querying usage, configuration, and insights using natural language. |  |   
  
### Core platform capabilities

The following table shows the core platform capabilities of Gemini Cloud Assist:

Feature | Available to all Google Cloud users | Code Assist Enterprise  
---|---|---  
**Agentic reasoning**. Gemini Cloud Assist employs dynamic reasoning loops, iteratively invoking tools (such as Cloud APIs and Kubernetes APIs) to gather data, evaluate state, and determine the next best action. |  |   
**User-guided multiturn agent**. Provides multi-turn, user-guided chat interactions. You can ask for clarification, guide the agent's focus, receive clarifying questions, and dynamically change the scope of your request without losing context. |  |   
**Agent identity**. When operating proactively in the background, Gemini Cloud Assist utilizes a dedicated Service Account (Agent Identity) rather than your personal credentials. This enforces the principle of least privilege and ensures all autonomous actions are fully audit-logged. |  |   
**MCP support**. Extend Gemini Cloud Assist anywhere using the Model Context Protocol (MCP). You can invoke agents directly from third-party client agents, local integrated development environments (IDEs) like Gemini CLI, or Claude Code. |  |   
**Custom instructions**. Administrators and users can provide persistent, custom system instructions. This lets you define specific agent personas (for example, a strict SRE), enforce response formats, or provide supplemental business context like naming conventions. |  |   
  
## Where to interact with Gemini Cloud Assist

The following table describes where to interact with Gemini Cloud Assist.

Where to interact with Gemini Cloud Assist | Available to all Google Cloud users | Code Assist Enterprise  
---|---|---  
[**Cloud Assist panel**](https://docs.cloud.google.com/cloud-assist/chat-panel). The **Cloud Assist** panel lets you get conversational assistance in the Google Cloud console and the Cloud Mobile App. |  |   
**Google Cloud console quick prompts**. Various buttons and interactive elements are available in the Google Cloud console and Cloud Mobile App.  |  |   
[**Cloud Hub**](https://docs.cloud.google.com/hub/docs/overview). A hub available in the Google Cloud console that empowers DevOps teams to optimize resource and application costs and utilization. |  |   
[**Database Center**](https://docs.cloud.google.com/database-center/docs/learn-database-products-using-gemini#use-gemini-cloud-assist). Simplifies development with efficient queries and optimized schemas. It enhances security by identifying vulnerabilities, automates migrations, and provides centralized management for database fleets, boosting performance and reducing costs. |  |   
[**Application Design Center**](https://docs.cloud.google.com/cloud-assist/design-application). Design optimal cloud applications that can be managed throughout their lifecycle with Gemini in the App Design Center. Describe your technical and business requirements to Gemini in the App Design Center, and it collaboratively produces solutions for consideration, refinement, and deployment.  |  |   
[**Investigations**](https://docs.cloud.google.com/cloud-assist/investigations). The Gemini Cloud Assist investigations feature is an AI-enabled tool for analyzing, troubleshooting, and diagnosing technical issues, available within the Google Cloud console, Cloud Mobile App app, command-line interface, and IDEs. For example, you can run an investigation if you receive an error message or are unable to accomplish a task because of unexpected behavior in the Google Cloud console.  |  |   
**Third-party integrations**. Integrate Gemini Cloud Assist with third-party developer productivity tools such as Slack, WhatsApp, and ServiceNow.  |  |   
  
## Set up Gemini Cloud Assist

For detailed setup steps, see [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

## What's next

  * See the latest enhancements and fixes in [release notes](https://docs.cloud.google.com/cloud-assist/release-notes).
  * Learn about [Gemini Cloud Assist pricing](https://cloud.google.com/products/gemini/pricing).
  * Learn how to [use the **Cloud Assist** panel in the Google Cloud console](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
