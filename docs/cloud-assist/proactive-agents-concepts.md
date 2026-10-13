---
url: https://docs.cloud.google.com/cloud-assist/proactive-agents-concepts/
title: Agent identity concepts \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:52.803882+00:00
---

# Agent identity concepts  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/proactive-agents-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Agent identity concepts Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Proactive cost optimization and proactive alert investigations are in private preview, and are only available to users that have a [Premium Support contract](https://cloud.google.com/support/premium).   
  
Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

Gemini Cloud Assist operates using two distinct identity modes to manage permissions and auditing. The mode used depends on how an action is triggered: interactively by a user or proactively by the system.

## Identity modes summary

The following table summarizes the triggers and the permission source for each mode:

Identity mode | Trigger | Permission source  
---|---|---  
End-user identity | Chat and interactive requests | Your personal IAM permissions  
Agent identity | Autonomous background tasks | A dedicated service account  
  
### End-user identity

When you interact with Gemini Cloud Assist through the [chat panel](https://docs.cloud.google.com/cloud-assist/chat-panel), the service uses your end-user identity.

In this mode, Gemini Cloud Assist inherits your existing permissions to access resources and perform actions. The assistant cannot see or modify any resource that you don't have permission to access yourself. All state-changing actions, known as resource mutations, require your explicit consent. Actions taken by Gemini Cloud Assist are recorded in Cloud Audit Logs under your identity, as if you took the action. This includes categorizing the action under its relevant Cloud Audit Logs [log type](https://docs.cloud.google.com/logging/docs/audit#types) and omitting an action from the logs if the action belongs to a log type that isn't [enabled](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) in Cloud Audit Logs.

### Agent identity

When Gemini Cloud Assist performs autonomous background tasks—such as [investigating alerts](https://docs.cloud.google.com/cloud-assist/investigations) or [analyzing cost anomalies](https://docs.cloud.google.com/cloud-assist/proactive-cost-optimization)—it uses a dedicated agent identity. Proactive investigation of alerts does not support log-based alerts.

The agent identity is a system-provisioned IAM principal unique to your project. This allows Gemini Cloud Assist to function without an active user session while maintaining a strict security boundary.

#### Governance and controls

Administrators manage the agent identity through the following mechanisms:

  * **Configurable permissions** : Unlike user identities, an administrator must explicitly [grant IAM roles](https://docs.cloud.google.com/cloud-assist/proactive-agents-setup#configure_permissions) to the agent identity.
  * **Scoped access** : By default, the agent is restricted to read-only telemetry and logs. It cannot access sensitive data in databases or storage buckets unless specifically authorized.
  * **Audit logging** : All autonomous actions are fully audit-logged. Proactive results are tagged as **System** generated in the Google Cloud console to distinguish them from user-initiated actions. Similar to user-initiated actions, autonomous actions are omitted from the logs when the relevant [log type](https://docs.cloud.google.com/logging/docs/audit#types) isn't [enabled](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) in Cloud Audit Logs.



## What's next

  * [Set up Proactive Mode](https://docs.cloud.google.com/cloud-assist/proactive-agents-setup) and provision an agent identity.
  * Review [IAM requirements](https://docs.cloud.google.com/cloud-assist/iam-requirements) for users and agents.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
