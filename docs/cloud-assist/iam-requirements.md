---
url: https://docs.cloud.google.com/cloud-assist/iam-requirements/
title: IAM requirements for using Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:00.106028+00:00
---

# IAM requirements for using Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/iam-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  IAM requirements for using Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses the Identity and Access Management roles that users need in order to successfully use Gemini Cloud Assist. For information about setting up Gemini Cloud Assist, see [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

## Overview

In order to support questions and requests about your Google Cloud resources, Gemini Cloud Assist needs the appropriate IAM permissions for those resources. Gemini Cloud Assist has the same permissions that the user querying Gemini Cloud Assist has, so in many cases, the necessary IAM permissions are already granted.

## IAM roles for using Gemini Cloud Assist

The following IAM roles are recommended for general usage of Gemini Cloud Assist:

IAM role | Notes  
---|---  
[**Gemini Cloud Assist User**](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) |  This role gives users permission to use Gemini Cloud Assist, which includes invoking agents, chatting, creating agent artifacts, and sharing artifacts owned by the user.   
[**Cloud Asset Viewer**](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) |  This role allows the user's agent to discover the topology of assets relevant to the user's question, because [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) manages Google Cloud assets and metadata associated with those assets. Assets include your Google Cloud resources, policies, and configurations.  
  
### Available IAM roles for Gemini Cloud Assist

In most cases, the recommended IAM role for using Gemini Cloud Assist is **Gemini Cloud Assist User**. In some cases, you might want to switch this role for a different Gemini Cloud Assist role. The following table lists different Gemini Cloud Assist roles that you can use:

IAM role | Function  
---|---  
[**Gemini Cloud Assist Viewer**](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.viewer) |  This role gives users permission to view agent artifacts, such as investigations or reports, and view agent configurations. This role grants more limited access when compared to the **Gemini Cloud Assist User** role; for example, the **Gemini Cloud Assist Viewer** role doesn't grant permission to invoke or chat with the agent.   
[**Gemini Cloud Assist User**](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) |  This role gives users permission to use Gemini Cloud Assist, which includes invoking agents, chatting, creating agent artifacts, and sharing artifacts owned by the user.   
[**Gemini Cloud Assist Editor**](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.editor) |  This role gives users editor permissions for Gemini Cloud Assist. In addition to permissions contained within the **Gemini Cloud Assist User** role, the editor role contains permissions to delete chat topics, delete agent artifacts, and update specific agent configurations.   
[**Gemini Cloud Assist Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) |  This role gives users administrative permissions for Gemini Cloud Assist. In addition to permissions contained within the **Gemini Cloud Assist Editor** role, the administrator role contains permissions that let you configure different policies of Gemini Cloud Assist, such as enabling proactive agents and data sharing, grant permissions on agents, and share artifacts project-wide.   
  
### Specific IAM permissions

The following are specific IAM permissions that are important for the functioning of Gemini Cloud Assist. Use this information when [creating custom IAM roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

IAM permission | Function  
---|---  
[`geminicloudassist.agents.invoke`](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.agents.invoke) |  Sending and receiving messages to Gemini Cloud Assist agents.   
[`cloudaicompanion.topics.create`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topics.create) |  Initiating a chat with Gemini Cloud Assist.   
[`cloudaicompanion.geminiGcpEnablementSettings.update`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.geminiGcpEnablementSettings.update) |  Configuring the administrator settings for Gemini Cloud Assist.   
[`mcp.tools.call`](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.tools.call) |  Sending and receiving messages to Gemini Cloud Assist agents through MCP.   
  
#### Permissions required for chat

The Gemini Cloud Assist [chat panel](https://docs.cloud.google.com/cloud-assist/chat-panel) uses a backend resource called a _topic_. When you start a chat, Gemini Cloud Assist creates a topic resource and grants you the `roles/cloudaicompanion.topicAdmin` role for that topic, which includes the `cloudaicompanion.topics.update` permission. This behavior means a chat is viewable and updatable by only the user who created the topic.

If your organization has a [custom constraint](https://docs.cloud.google.com/organization-policy/overview#custom-constraints) that prevents Gemini Cloud Assist from granting `roles/cloudaicompanion.topicAdmin` to users, your attempt to start a chat session fails. To fix the issue, ask your administrator to update the organization's custom constraints to [allow specific roles to be granted](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints#example_constraints).

## IAM role recommendations for different use cases

In addition to the access granted from IAM roles for using Gemini Cloud Assist, tasks performed through Gemini Cloud Assist require access to the Google Cloud resources that are relevant to that task. For example:

  * If you are using agents to understand the health of GKE applications, then IAM permissions for GKE and its associated resources are most critical.

  * If you are using agents to deploy data processing jobs, then IAM permissions for Dataflow, Managed Service for Apache Spark, or BigQuery might be most critical.




Necessary IAM permissions depend on the specific domain that your tasks are in. In turn, appropriate IAM roles that contain these permissions vary by use case. The following job-function IAM roles provide a good starting point if you are not sure what roles users or agent identities should have.

Task | Relevant Roles  
---|---  
Troubleshooting and ensuring the reliability and scalability of Google Cloud infrastructure broadly across multiple domains, both proactively and interactively  | 
* `roles/iam.siteReliabilityEngineer`
* `roles/iam.supportUser`  
Deploying, updating, and exploring Google Cloud infrastructure broadly across multiple domains  | 
* `roles/iam.infrastructureAdmin`
* `roles/iam.devOps`
* `roles/logging.viewer`
* `roles/monitoring.viewer`
* `roles/cloudtrace.user`
* `roles/apptopology.viewer`  
Exploring, understanding, and troubleshooting your network infrastructure  | 
* `roles/iam.networkAdmin`
* `roles/logging.viewer`
* `roles/monitoring.viewer`
* `roles/cloudtrace.user`
* `roles/apptopology.viewer`  
Interacting with and analyzing data through data processing, transformation, and analysis pipelines  | 
* `roles/iam.dataScientist`
* `roles/logging.viewer`
* `roles/monitoring.viewer`  
Deploying, updating, and troubleshooting databases  | 
* `roles/iam.databaseAdmin`
* `roles/logging.viewer`
* `roles/monitoring.viewer`  
Understanding and analyzing your application's costs in detail  | 
* `roles/cloudhub.operator`
* `roles/monitoring.viewer`
* `roles/logging.viewer`  
Browsing and viewing Google Cloud resources, folder hierarchy, logs, security configuration, and key resource metadata.  | 
* `roles/iam.securityAuditor`  
Using Gemini Cloud Assist with [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) to understand your Cloud Storage usage.  | 
* `roles/bigquery.jobUser`
* `roles/bigquery.dataViewer`
* `roles/storageinsights.viewer`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
