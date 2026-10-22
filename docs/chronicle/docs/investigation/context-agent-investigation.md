---
url: https://docs.cloud.google.com/chronicle/docs/investigation/context-agent-investigation/
title: Investigate alerts with the 3P Context Agent \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:13.619385+00:00
---

# Investigate alerts with the 3P Context Agent  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/context-agent-investigation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Investigate alerts with the 3P Context Agent

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

**Important:** You need to opt-in to the 3P (third-party) Context Agent in the Google Security Operations platform before you can start using the agent. For more information, see Configure the 3P Context Agent.

This guide is for security analysts who want to efficiently investigate security alerts. It explains how to leverage the AI-powered Google SecOps 3P Context Agent within Google SecOps to:

  * Automatically enrich alerts and entities with crucial external contextual data derived from your organizational environment.
  * Augment the Triage and Investigation agent's (TIN) verdict by adding additional contextual investigation data.



When you use the 3P Context Agent, you can reduce manual data gathering and accelerate the triage process. It saves you time from having to develop and maintain custom enrichment workflows. Successful use of the 3P Context Agent leads to faster Mean Time To Respond (MTTR) and more informed decisions during investigations, providing significant business value by improving security posture and operational efficiency.

## Key terminology

  * **3P Context Agent:** The AI-powered assistant that automatically enriches alerts with contextual data from third-party tools deployed in your environment.
  * **Triage and Investigation agent (TIN):** The agent that performs initial alert analysis and creates resultant verdicts. The 3P Context Agent acts as a sub-agent to the TIN.
  * **Enrichment:** The process of adding additional context to the alert. When using the 3P Context Agent, enrichment can be added manually or automatically by using a wide variety of integrations, whether commercial or custom. These can include security tools, ticketing systems, and other data sources.



## Quota usage during Private Preview

  * **3P Context Agent:** During the Private Preview phase, using the 3P Context Agent to enrich data from third-party tools won't consume your AI quota.
  * **TIN:** When triggering the 3P Context Agent, the TIN agent may consume an average of 5% additional AI quota.
  * **Using integrations:** When you use integrations within the 3P Context Agent for enrichment purposes, you may incur additional fees from these integrations, similar to when you run them manually or using a playbook.



## Before you begin

Make sure you have or do the following:

  * **Permissions:** Access to configure the 3P Context Agent is managed using SIEM settings. Go to **SIEM Settings > Gemini Investigations > 3P Context Agent**. Specific Identity and Access Management (IAM) roles may be required to modify these settings.
  * **Environment check:** Make sure the relevant third-party integrations, such as EDR, IAM, and Threat Intelligence tools, are installed and active in your Google SecOps environment. The 3P Context Agent can only utilize integrations that are already deployed and configured.



## How the 3P Context Agent works

### Guardrails and restrictions

The 3P Context Agent operates with strict guardrails. It is restricted to only accessing **read-only enrichment actions** from commercial integrations. It cannot perform any actions that modify data or states within those third-party systems.

### Stage 1: Triggering the 3P Context Agent

The 3P Context Agent is primarily triggered as a sub-agent when the TIN runs. This occurs automatically if you opted-in, using the **Gemini Investigations** settings.

### Stage 2: Tools and data sources

  1. **Dynamic tool selection:** The 3P Context Agent intelligently chooses the most appropriate tools from your installed third-party integrations based on the alert type and entities involved.
  2. **Google SecOps first-party tools:** The following first-party tools are executed directly by the TIN, not by the 3P Context Agent: 
     * GoogleChronicle
     * Google Threat Intelligence (GTI)
     * Mandiant
     * Mandiant Threat Intelligence
     * VirusTotal
     * VirusTotal V3



### Stage 3: Viewing the outcome

  1. **Alert entities:** Go to the alert details page. Entities associated with the alert will be enriched with findings from the 3P Context Agent. This data is also available for use in playbooks.
  2. **Augment verdicts:** The outcomes generated by the 3P Context Agent are also used to augment the TIN verdict and confidence level.
  3. **Gemini Investigations timeline:** Review the timeline for the investigation. Each tool execution by the 3P Context Agent is logged here, including a summary of findings and an option to view the raw results.
  4. All enrichment tools that were executed by the 3P Context Agent will be visible and audited in the Case Wall, including their results.



## Configure the 3P Context Agent

  1. **Access Settings:** Go to **SIEM settings > Gemini Investigations > 3P Context Agent**.
  2. **Enable or disable:** Enable or disable the 3P Context Agent by changing the toggle.
  3. **Manage tools:**
     * By default, all newly installed integrations are automatically included. You can select which, if any, tools you want to exclude.
     * From your installed integrations, review the list of available read-only enrichment tools.
     * Deactivate entire integrations or specific actions within an integration to control which data the 3P Context Agent can access.
  4. **Manage instances (integration configuration):**
     * By default, the 3P Context Agent will first select a configured instance from the executed environment. If there are no existing configured instances in the environment, the 3P Context Agent then automatically uses available shared instances if they exist.
     * For each environment, you can disable automatic selection and manually select instances either from the environment or from shared instances. This is useful when you have multiple instances configured for the environment and you want the 3P Context Agent to use a specific one.
     * You can disable 3P Context Agent access for specific environments entirely to prevent the agent from using the tool in those environments.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
