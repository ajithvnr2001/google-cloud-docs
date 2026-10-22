---
url: https://docs.cloud.google.com/docs/security/compliance/config-fedramp20x-gemini-gov/
title: Configure Gemini for Government for FedRAMP 20x Class B (Low) \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:52.371556+00:00
---

# Configure Gemini for Government for FedRAMP 20x Class B (Low)  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/config-fedramp20x-gemini-gov/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Configure Gemini for Government for FedRAMP 20x Class B (Low) Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-06-11 UTC

This page describes how government agencies can deploy [Gemini for Government](https://cloud.google.com/blog/topics/public-sector/introducing-gemini-for-government-supporting-the-us-governments-transformation-with-ai) under [FedRAMP 20x](https://www.fedramp.gov/20x/) Class B (Low) criteria. The FedRAMP 20x Class B (Low) authorization covers publicly releasable information with minimal sensitivity. If your agency requires processing data at a FedRAMP Moderate or High level, see [Deployment guidance for Gemini for Government](https://docs.cloud.google.com/docs/security/compliance/deploy-gemini-gov).

To request access to detailed [Gemini for Government FedRAMP 20x Low](https://www.fedramp.gov/marketplace/products/FR2604952026/) documentation, email [fedramp@google.com](mailto:fedramp@google.com) and state your interest in obtaining the package materials.

## FedRAMP 20x Low certified services

The following services are listed as certified within the Gemini for Government FedRAMP 20x Low boundary:

  * Gemini Enterprise
  * Generative AI on Gemini Enterprise Agent Platform (formerly Generative AI on Vertex AI)
  * BigQuery
  * Cloud Storage
  * Looker (Google Cloud core)
  * Conversational Agents
  * Gemini Code Assist
  * NotebookLM Enterprise
  * Agent Search on Gemini Enterprise Agent Platform (formerly Agent Search)



This certification level is intended for unclassified information with minimal sensitivity.

## FedRAMP 20x Low certified services and features

The following table lists the services and features that you can use within Gemini for Government for FedRAMP 20x Class B (Low).

Models | [Generally available Gemini models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models#generally_available_models)  
---|---  
Agents and galleries | 

  * [Prompt gallery](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/prompt-gallery)
  * [Idea Generation agent](https://docs.cloud.google.com/gemini/enterprise/docs/idea-generation)
  * [Deep Research agent](https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant)
  * No-code agent creation using [Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer)
  * [Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery)

  
Analytics and dependent features | 

  * [View analytics data](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics)
  * [Data agent context for Looker data sources](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/data-agent-authored-context-looker)
  * [Data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/data-agent-authored-context-bq)
  * [Data agents that you create](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview#build-and-interact-with-a-data-agent) using the Conversational Analytics API
  * [Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview)
  * [Gemini in Looker](https://docs.cloud.google.com/gemini/docs/looker/overview)

  
Data connectors and stores | 

  * FedRAMP Authorized data stores such as [Cloud Storage](https://docs.cloud.google.com/gemini/enterprise/docs/connect-cloud-storage) and [BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connect-bigquery)
  * Google Workspace data sources such as Google Drive, Gmail, or Google Calendar
  * Google Cloud data stores such as Cloud SQL and Firestore
  * [Google Calendar and Gmail actions](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-actions-google)
  * Third-party data sources such as Salesforce or Microsoft
  * People data sources such as [Google Workspace](https://docs.cloud.google.com/gemini/enterprise/docs/connect-people), [Microsoft Entra](https://docs.cloud.google.com/gemini/enterprise/docs/connect-entra-id), or [custom sources](https://docs.cloud.google.com/gemini/enterprise/docs/connect-people-custom)

  
Grounding | 

  * [Web Grounding for Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/web-grounding-enterprise)
  * [Grounding with Google Maps Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps)
  * [Grounding with Google Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search)
  * Grounding using Google Drive uploads
  * Grounding using Microsoft OneDrive uploads

  
Generative features | 

  * [Generate images using Imagen](https://ai.google.dev/gemini-api/docs/imagen)
  * [Generate video with Veo](https://ai.google.dev/gemini-api/docs/video)

  
User, session, and UI features | 

  * [Autocomplete](https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete)
  * [Serving controls](https://docs.cloud.google.com/gemini/enterprise/docs/configure-serving-controls)
  * [Uploading documents](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#upload_and_chat_about_files) from local machines
  * Ability for end users to [select models](https://docs.cloud.google.com/gemini/enterprise/docs/answer-generation-models)
  * [User events for Gemini Enterprise apps](https://docs.cloud.google.com/gemini/enterprise/docs/user-events)
  * [Personalization and memory in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization)
  * [Prompt chips](https://docs.cloud.google.com/gemini/enterprise/docs/configure-prompt-chips)

  
Other features | 

  * [Private Knowledge Graph in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search)
  * [NotebookLM Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview)
  * [Implicit context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)
  * [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview)
  * [Model Armor](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor)
  * [Image generation using Nano Banana](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#generate_an_image)

  
  
## Configure your environment

Complete the following tasks within the Google Cloud organization of your agency.

  1. Create a [Google Cloud project](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin) to host your Gemini Enterprise data stores and applications.
  2. Configure your APIs and solutions in [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs). Your subscription settings automatically enable Gemini for Government. Gemini for Government includes the Gemini Enterprise Standard Edition and prevents unexpected costs by stopping requests after a quota is reached, rather than billing for overages. You can manage these settings within the subscriptions console.
  3. Configure security features for Gemini for Government as described in the [Gemini Enterprise security overview](https://docs.cloud.google.com/gemini/enterprise/docs/security-overview). To help ensure compliance with FedRAMP 20x, configure the following based on your agency's policies:

     * [Identity and Access Management (IAM)](https://docs.cloud.google.com/gemini/enterprise/docs/access-control)
     * [Gemini Enterprise data security](https://docs.cloud.google.com/gemini/enterprise/docs/security-overview#data-security), particularly VPC Service Controls and customer managed encryption keys (CMEK)
     * [Gemini Enterprise compliance](https://docs.cloud.google.com/gemini/enterprise/docs/security-overview#compliance), particularly access transparency and audit logging
  4. Optionally, review and apply additional security best practices for Google Cloud:

     * [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper)
     * [General best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices)
     * [FedRAMP implementation guidance on Google Cloud](https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide)



## Manage your compliance for FedRAMP 20x

To maintain your FedRAMP 20x Class B (Low) compliance posture for Gemini for Government, you can use [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview). Compliance Manager includes a [FedRAMP Low 20x framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#fedramp-low-20x) that you can deploy in your environment and use for auditing.

  1. In the console, select the United States regional toggle, and adjust the view to **Global**. Locate the relevant domain address and select **Configure** to proceed.
  2. Activate [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier) to enable Compliance Manager.
  3. In Compliance Manager, deploy the FedRAMP 20x framework. For instructions, see [Deploy a framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#deploy-framework). Deploying the framework lets you [monitor for compliance](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-monitor-framework).
  4. Audit the FedRAMP 20x framework to compile compliance evidence. For instructions, see [Audit your environment with Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit). An audit can take several hours to run.

**Note** : The artifacts produced during an audit are provided to support your own audit preparation and process. They aren't guaranteed to satisfy all auditor or regulatory requirements. It is your responsibility to collaborate with your auditors to ensure compliance.

  5. Review the detailed audit assessments against each resource and rule. Optionally, download the evidence to support your FedRAMP package submission.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
