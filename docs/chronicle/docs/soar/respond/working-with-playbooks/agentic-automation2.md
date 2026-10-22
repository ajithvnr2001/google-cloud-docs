---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/agentic-automation2/
title: Embed AI agents in playbooks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:15.624812+00:00
---

# Embed AI agents in playbooks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/agentic-automation2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Embed AI agents in playbooks

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.**Note:** Agentic Automation is only available for Google Security Operations instances that have been migrated to [Google Cloud infrastructure](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

_Agentic Automation_ in Google Security Operations lets you build dynamic, adaptive automation by embedding AI Agents directly into your workflows. This lets you integrate AI-driven capabilities into your existing playbooks by combining AI agents with deterministic automation steps, ensuring you stay in charge of critical actions.

Deterministic automation relies on hard-coded logic where every step and outcome is fixed and predefined. While this offers control, it can struggle to handle new use cases, manage scenarios where parts of the automation fail, or adapt when faced with missing information. Agentic Automation shifts the focus toward workflows built on AI agents that can reason through these unplanned variables.

## Case Overview and Visibility

When an agent triages an alert, the findings appear in the **Gemini Investigations** side drawer and in the AI agent step results.

The playbook monitors the agent's progress using three distinct states. This is an asynchronous process; the playbook pauses without occupying the execution queue while waiting for the agent to complete.

  * **Not Run:** The agent has not been triggered yet.

  * **Running:** An investigation is in progress or the playbook is polling for results.

  * **Completed:** The agent has finished its analysis and the results are ready for downstream steps.




To use Agentic Automation, you must opt in the relevant AI agents for your tenant. You can manage this in the settings of the **Gemini investigation** side menu within the **Case Overview**.

**Note:** Permissions for AI agents in playbooks are managed by Google. You do not need to configure specific IAM roles for these agents to operate within your playbooks.**Note:** Agentic Automation supports up to 5 automatic investigations per hour and is subject to underlying Gemini resource availability and Vertex AI capacity constraints. These limits are intended to ensure system stability; performance may fluctuate based on resource demand outside the direct control of Google SecOps.

## Triage and Investigation agent (TIN) integration

Agentic Automation supports the [Triage and Investigation Agent (TIN)](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent), which performs autonomous analysis of security alerts by gathering evidence and performing first-party enrichment. The agent provides a True Positive or False Positive verdict, a confidence score, and additional outputs that can be used to drive subsequent steps in the playbook workflow.

### Supported alert types

TIN's investigative capabilities depend on the alert source and how the agent is triggered:

  * Manual investigations: You can manually trigger a TIN investigation on any alert, provided it does not originate from a SOAR Connector.
  * Automatic investigations: By default, TIN supports automatic investigations for alerts originating from specific SIEM detection engine log types. For the list of these sources, see [Default Supported Log Types](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent#tinsupportedlogtypes).
  * Unsupported alerts: If an unsupported alert type triggers an automatic agent step, you can configure the playbook to either stop execution or skip the step and continue the workflow.



## Add an AI Agent to a playbook

  1. Go to **Response > Playbooks**.
  2. Open an existing playbook or create a new one.
  3. Open the **Step Selection** panel and locate the **AI Agents** category.
  4. Drag an agent from the list onto the canvas.
  5. Click the step to open the configuration panel.



### Configure the Agent step

Within the configuration panel, define how the playbook interacts with the AI Agent:

  * **Action type:** Set to **Automatic** to let the agent run without manual intervention, or **Manual** if an analyst must run the **AI Agent** step from within a case.
  * **Retry on failure:** Toggle whether the step should attempt to rerun if the agent encounters a transient error. This applies to the failure of the agent execution itself, rather than a failure of a specific tool.
  * **Error Handling (If step fails):** Use these settings to define the workflow if the agent cannot process the input (for example, due to an unsupported data format): 
    * **Stop the playbook:** Cease all actions if the agent cannot provide a result.
    * **Skip to the next step:** Continue the playbook execution, bypassing the **AI Agent** step.



## Use Agent results in logic branching

TIN generates structured results that you can use in the [Expression Builder](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder). This lets you navigate the automation flow based on the agent's verdict and confidence level rather than relying on predefined static inputs.

### Example Logic

  1. Drag a **Flow block (Conditional)** onto the canvas after the AI Agent step.
  2. Click the condition to open the **Placeholder** menu.
  3. Locate and select the **AI Agent** step results.
  4. Open the **Expression Builder** for the JSON result and select the value you want to evaluate (for example, `verdict` or `confidence_level`).
  5. Define your branches based on the AI's insights: 
     * **True Positive:** Connect to remediation steps (for example, "Isolate Host" or "Block User").
     * **False Positive (High Confidence):** Connect to a **Close Alert** action to automatically reduce analyst noise.
     * **False Positive (Low/Medium Confidence):** Connect to an analyst assignment or manual review step for secondary verification.



## Manage agent quotas

To maintain consistent playbook performance and system stability, ensure your workflows stay within the service limits for Agentic Automation.

**Note:** Running AI agents consumes service quotas. For the most up-to-date information on investigation limits, see [Triage and Investigation Agent (TIN)](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
