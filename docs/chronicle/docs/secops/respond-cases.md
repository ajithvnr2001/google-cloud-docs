---
url: https://docs.cloud.google.com/chronicle/docs/secops/respond-cases/
title: Respond to alerts and cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:58.281648+00:00
---

# Respond to alerts and cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/respond-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Respond to alerts and cases 

Supported in:

Google SecOps 

This guide helps security analysts efficiently identify and prioritize cases and security alerts that demand immediate attention. It explains how to use Google Security Operations features, including personalized views, automation, AI-powered triage, and playbooks. By following this method, analysts can reduce noise, accelerate response times, and focus analyst efforts on the true positives that pose the greatest risk. Successful completion ensures timely mitigation of critical threats.

## Common use case

  * **Objective** : Efficiently identify high-risk alerts and cases amidst a large volume of security data using automation and AI.
  * **Value** : Ensures a rapid response to critical threats, minimizing potential impact.



## Before you begin

  * **Permissions** : Ensure you have the necessary permissions within Google SecOps to access **Cases** , **Your Workdesk** , and to execute **Playbooks**. Specific IAM roles may be required such as:

    * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin)
    * [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor)
    * [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer)
    * [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer)



## Determine which cases and alerts require immediate attention

This section describes the sequential steps to determine urgency.

### Monitor personalized queues and apply strict filters

The following approach ensures that you see both items needing your specific attention and the overall pool of high-risk incidents, providing immediate visibility into the most impactful events.

  1. On the Google SecOps platform, select **Your Workdesk** > **My Cases**. This view displays cases directly assigned to you or your analyst role.
  2. Open the main **Cases** page, and then click **Cases Filter**.
  3. Filter for findings with **Critical** and **High** priority levels. Make sure to save these filters so you can return to them easily. 



### Leverage AI and automation for triage

For any alert, use [agentic automation](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/agentic-automation), which combines deterministic, predefined playbooks with dynamic AI agents, such as the **Gemini Triage and Investigation Agent**. This agent automates initial deep analysis, often condensing 15-20 minutes of manual work into a much shorter timeframe. 

**Key features** :

  * **Automation sequencing** : [Configure playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-edit-playbook-with-gemini) so that a remediation playbook (for example, host isolation or account suspension) automatically initiates based on the output of the Gemini Triage and Investigation Agent and can immediately act o important cases.
  * **Adaptive responses** : Use AI-generated outputs (such as risk scores, or verdicts such as `True Positive`) as conditions within playbooks to trigger different automated response paths. For example, auto-isolate a host if the verdict is `Malicious`, but only flag for review if `Suspicious`. You can use the verdict or risk score to raise the priority or escalate the case. For example. escalate to a higher tier, or send a message to the assignee.
  * **Process-tree reconstruction** : The triage agent can generate a visual timeline of system activity, helping analysts instantly understand the attack chain, parent-child process relationships, and lateral movement.



### Use playbooks for rapid triage and consistent action

On the **Cases** page, use prebuilt and custom **Playbooks**. Playbooks codify standard operating procedures (SOPs) into automated workflows, minimizing manual effort and ensuring consistency.

**Key playbook capabilities** :

  * **Automated enrichment** : Many playbooks automatically enrich alerts with threat intelligence from sources like VirusTotal, CrowdStrike, and internal threat feeds, providing immediate context on indicators of compromise (IoCs) such as hashes, IP addresses, and domains.
  * **Guided decision points** : Playbooks can pause and present analysts with yes-no questions, multiple-choice questions, or conditional prompts—for example, `"Is this activity expected for this user role?"... if "No", then "Escalate to Tier 3", if "Yes", then "Mark as False Positive", or "Continue monitoring"`.
  * **Controlled manual intervention** : For sensitive actions, playbooks can include manual approval steps. This lets analysts review proposed actions (for example, isolate host, detonate file in sandbox, or block IP address) before execution.
  * **Automated case-management** : Playbooks can automate case routing to specialized teams based on findings and auto-close alerts confirmed as benign or informational, keeping the active queue focused on actionable threats.



**How analysts use playbooks for this journey** :

  * **Standardized response** : Ensures all alerts of a specific type (for example, phishing, or ransomware) are handled according to established organizational SOPs.
  * **Noise reduction** : Automatically filters out or resolves low-fidelity alerts based on predefined logic.
  * **Reduced toil** : Automates time-consuming tasks like data gathering, log correlation, and entity enrichment.
  * **Agentic automation in action** : Combines the analytical speed of AI agents with the reliability of deterministic playbooks.
  * **Agentic Step** : playbooks can leverage Vertex AI integration to build a curated workstream powered by Gemini to help with the investigation.



**Benefit** : Streamlines the triage process, enforces consistent responses, reduces repetitive tasks, and lets analysts handle more complex threats effectively.

## Examples of immediate-attention scenarios

This section contains examples of scenarios that require immediate attention.

### Automated remediation kick-off

You see a **Critical** priority alert on the **Cases** page for `Suspicious PowerShell Execution`.

The linked playbook shows that the Gemini Triage Agent ran, returned a `True Positive` verdict with high confidence, and consequently, the playbook automatically triggered an **Isolate Host** action, which is now pending approval or completed.

This requires immediate review of the agent's findings and the isolation state.

### AI-assisted manual decision

You filter the **Cases** queue for **Priority: Critical**.

When you open a case, you find a playbook has paused at a yes-no question, asking whether to escalate the case or close it.

You review the Gemini Triage and Investigation Agent's summary, which states **Highly Likely True Positive** with a detailed rationale citing specific malicious indicators.

You confidently select **Escalate to Tier 2**.

## Troubleshooting

### Latency, service quota, and limits

  * **Triage-agent quota** : The Gemini Triage and Investigation Agent is subject to a quota, typically around 10 investigations per hour per tenant (for example, 5 manual triggers, 5 automatic triggers). Alerts exceeding this limit require manual triage.



### Error remediation

**Error code** | **Issue description** | **Fix**  
---|---|---  
N/A  | Expected urgent items are missing from the My Cases or Cases queue.  | Make sure that rule `Alerting` is toggled ON for relevant detections. Verify that cases are correctly assigned to your user or role, and check that no restrictive filters are inadvertently applied to the queue.   
N/A  | `Gemini` summary is missing.  | Check the `Gemini Investigations` status in the case wall. If the quota was reached, you will see a message indicating the agent couldn't be triggered.   
  
### Validation and testing

To validate that the process is working, confirm that:

  * High and Critical alerts appear as expected based on filters.
  * Playbooks are triggered on new alerts.
  * Gemini Triage and Investigation Agent summaries are present where expected.
  * Cases are escalated or closed based on playbook logic and analyst decisions.

Symptom  | Resolution   
---|---  
Expected urgent items are missing from the My Cases or Cases queue.  | Make sure that rule `Alerting` is toggled ON for relevant detections. Verify that cases are correctly assigned to your user or role, and check that no restrictive filters are inadvertently applied to the queue.   
`Gemini` summary is missing.  | Check the `Gemini Investigations` status in the case wall. If the quota was reached, you will see a message indicating the agent couldn't be triggered.   
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
