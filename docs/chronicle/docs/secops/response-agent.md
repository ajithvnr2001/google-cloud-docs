---
url: https://docs.cloud.google.com/chronicle/docs/secops/response-agent/
title: Contain threats with the SecOps Response Agent \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:04:59.714626+00:00
---

# Contain threats with the SecOps Response Agent  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/response-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Contain threats with the SecOps Response Agent

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

**Important:** You need to opt-in to the Response Agent in the Google Security Operations platform before you can start using the agent. For more information, see Configure the Response Agent.

This guide explains how you can leverage the AI-powered Response Agent within Google SecOps to respond to and remediate security alerts. Use the Response Agent to:

  * Automatically generate immediate, context-aware response recommendations based on investigation verdicts.
  * Execute verified response actions directly from the agentic investigation interface.
  * Bridge the gap between threat detection and threat resolution with tiered automation controls.



When you use the Response Agent, you can reduce manual response overhead and eliminate delays between threat identification and containment. Successful use of the Response Agent leads to predictable, safety-checked threat neutralization across critical organizational assets.

## Key terminology

  * **Response Agent:** The AI-powered assistant that suggests or executes response actions to neutralize a detected threat.
  * **Containment:** Short-term, immediate actions taken to stop the spread of a threat (for example, isolating a host or blocking an IP address).
  * **Remediation:** Long-term actions aimed at removing a threat completely and patching vulnerabilities (powered in conjunction with external tools like Wiz).
  * **Manual approval:** A human-in-the-loop tier where the agent presents intended actions as recommendations for your approval.
  * **Autonomous execution:** A tier where the agent executes actions automatically based on predefined risk thresholds (Low Risk, Medium Risk, High Risk).



## Quota usage during Private Preview

  * **Response Agent:** During the Private Preview phase, generating response plans with the Response Agent does not consume your AI quota.
  * **Using integrations:** When you execute response and containment actions through installed integrations within the Response Agent, standard integration usage applies.



## Before you begin

Make sure you have or do the following:

  * **Permissions:** Configuring agent settings and managing exclusions requires administrator permissions, managed in **SIEM Settings > Gemini Investigations**. Reviewing alerts and executing plans is performed by security analysts. Specific Identity and Access Management (IAM) roles may be required to modify these settings.
  * **Execution pathways:** Verify that your preferred execution pathway is configured:

    * **Triage Agent (TIN) path:** Requires **Auto-Investigate Alerts in Gemini** to be enabled under **SIEM Settings > Gemini Investigations > Triage Agent**. Response plans are generated automatically for alerts evaluated as true positives.
    * **Playbooks path:** Does not require TIN. You can drag the **Response Agent** step into a playbook to run dynamically alongside deterministic steps when an alert triggers. 
**Note:** When using the Playbooks path, it is recommended to ensure that relevant enrichment steps (such as GTI or Active Directory lookups) have completed before the Response Agent runs, ensuring it has sufficient context to build a valid plan.
  * **Environment check:** Ensure your response and endpoint tools (such as EDRs, firewalls, or Identity Providers) are installed and active as integrations in your Google SecOps environment under **Available Tools**.




## How the Response Agent works

The Response Agent operates as the active response component of the Agentic SOC ecosystem. It processes enriched context and alert verdicts to synthesize safety-checked response plans. The following sections explain the underlying autonomy logic, triggering stages, and response workflow.

### Tiered autonomy and risk logic

To ensure safety, the agent evaluates response actions against an **Autonomous Execution Level** setting (Manual Approval, Low Risk, Medium Risk, High Risk). 

#### Risk assessment mechanism

Risk levels are calculated by evaluating the operational impact, reversibility, and scope of the proposed action itself (for example, resetting a password versus wiping a device).

#### Global execution modes

You can configure the agent to run in the following global modes based on your risk tolerance:

  * **Manual approval:** Actions require explicit approval before execution. This is the default setting.
  * **Autonomous execution:** Actions at or below the selected risk threshold run automatically. You can set the threshold to **Low Risk** , **Medium Risk** , or **High Risk**. For example, if **Medium Risk** is selected, the agent will execute all low and medium-risk actions automatically without asking for approval. High-risk actions will default to requiring manual approval.



#### Per-tool overrides

Additionally, you can configure granular overrides under **Available Tools** , either at the **integration level** or the **action level** :

  * **Autonomous:** Always runs automatically regardless of the global risk setting.
  * **Default:** Inherits execution behavior from the global Autonomous Execution Level.
  * **Manual Approval:** Always requires human approval regardless of the global risk setting.



### Stage 1: Building the response plan

  1. **Synthesize context:** The agent reviews the case verdict, enriched entities, and environmental context to form a list of concrete recommended actions tailored to the specific scenario.
  2. **AI Script & Code Generation:** If **AI Script & Code Generation** is enabled (disabled by default) and a recommended response action does not exist in your current integrations, Gemini can dynamically write custom code to execute missing actions.



### Stage 2: Viewing and executing the plan

  1. **Access cases:** Go to **Cases** and select a case tagged with **Gemini**.
  2. **Review the plan:** Review the response plan at either the case level or the alert level: 
     * **Case-level aggregation:** On the **Overview** tab, review the **Case Summary** widget for aggregated recommendations.
     * **Alert-level details:** Click the **Alerts & Detections** tab. Select an alert, click **View investigation and response plan** , and then click **View response plan** to open the response drawer.
  3. **Review actions:** Inspect the recommended actions, target entity parameters, and execution risk levels.
  4. **Modify plan:** Select or clear individual actions, edit target parameters, or append manual response steps (such as blocking an IP address) as direct feedback for incomplete plans.
  5. **Execute:** Click **Execute actions** to run the selected plan.
  6. **Audit trail:** Executed actions display individual success or failure statuses directly within the workflow.



### Stage 3: Wiz integration (cloud responses)

While the SecOps Response Agent focuses primarily on immediate containment actions within your environment, the integration with Wiz provides a strategic, long-term defense. It helps you fully remediate identified cloud vulnerabilities and secure your posture to prevent future attacks.

The Response Agent pulls critical risk data directly from Wiz to assist in resolving cloud infrastructure risks:

  * **Related risks:** Displays critical related Wiz risk issues attached to cloud entities involved in the case.
  * **Next steps:** For detailed actions and response steps, click **View Issue in Wiz** to link directly to the Wiz platform and safely complete the remediation within the Wiz environment.



## Configure the Response Agent

  1. **Access Settings:** Go to **SIEM Settings > Gemini Investigations > Context & Response**.
  2. **Enable or disable:** In the **Context & Response** section, toggle **Response Agent** to **Enabled** or **Disabled**.
  3. **Set Autonomous Execution Level:** Select the maximum risk level allowed to run automatically (**Manual Approval** , **Low Risk** , **Medium Risk** , or **High Risk**).
  4. **Configure AI Script & Code Generation:** Optional: Toggle **AI Script & Code Generation** to **Enabled** (disabled by default) to allow Gemini to write dynamic code for unhandled actions.
  5. **Manage tool overrides (Exclusions):** Optional: Under **Available Tools** , select specific integrations or actions to override their execution mode (**Autonomous** , **Default** , or **Manual Approval**). This is how you manage exclusions (by turning off or restricting specific integrations or actions).

**Note:** The integration instance configuration is shared with the **3P Context Agent (CONA)**. For more information on configuring instances, see [Investigate alerts with the 3P Context Agent](https://docs.cloud.google.com/chronicle/docs/investigation/context-agent-investigation).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
