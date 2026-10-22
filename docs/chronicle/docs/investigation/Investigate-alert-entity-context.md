---
url: https://docs.cloud.google.com/chronicle/docs/investigation/Investigate-alert-entity-context/
title: Investigate alerts and entity context \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:20.412967+00:00
---

# Investigate alerts and entity context  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/Investigate-alert-entity-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Investigate alerts and entity context

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide is for investigators who want to identify correlated activities and evaluate risk profiles from alerts. You can use this guide to understand how to pivot from an alert to an entity's timeline. Successful investigation can reduce the time-to-triage for complex incidents and help you focus on high-impact threats first.

## Common use cases

This section lists some common use cases.

### Triage and case prioritization

**Objective** : Determine which alerts require immediate escalation by evaluating the risk profile of the involved entities. This approach moves beyond chronological processing by identifying alerts that pose the greatest organizational threat.

**Workflow** :

  1. Open the **Alerts** dashboard and view an alert.

  2. Copy the asset ID or username and pivot to **Risk Analytics**.

  3. If the entity already has a high entity risk score, prioritize this case over alerts involving low risk entities.




**Outcome** : Limited SOC resources can focus on high impact threats first.

### Analyse scope of impact of an alert

**Objective** : Understand the full scope of an incident by tracking the alert's correlated activity. By tracking the correlated activity across the environment, you can map out the relationship between compromised systems and accounts to visualize how a threat has migrated.

**Workflow** :

  1. Open the **Alerts** dashboard and view a high risk alert.

  2. Go the graph tab to view entity context graph (ECG) relationships.

  3. For each related entity, pivot to the **Detections timeline** in **Risk Analytics**.

  4. Look for overlapping detection patterns to map how the threat may have spread.




**Outcome:** A comprehensive map of the incident that identifies affected systems and accounts.

### Lateral movement investigation

**Objective** : Proactively identify malicious behavior by comparing UDM events against a baseline of _normal_ behavioral history. You can identify subtle anomalies in internal communications and access patterns that suggest an attacker is moving through the network.

**Workflow** :

  1. Select an entity and review its **behavioral history** (usual login times or file access).

  2. Search UDM events for deviations, such as an asset suddenly communicating with a new internal IP address or a user accessing a sensitive application for the first time.

  3. Evaluate if these anomalies have caused a recent spike in the entity risk score, even if a formal alert has not yet been triggered.

  4. By linking the UDM events to the entity's history, you can distinguish between a legitimate business change and potential lateral movement.




**Outcome:** Early detection of threats that bypass signature-based alerting.

## Before you begin

Make sure you have the following in place:

  * **Permissions** : You must have access to the Alerts dashboard, Risk Analytics dashboard, and UDM Search capabilities.

  * **Environment check** : Enable ECG and Risk Analytics to ensure that they are ingesting data to populate timelines.




## Investigate detections and entity context

Complete the following steps to manually link an alert to a risk profile and analyze the historical activity of the involved assets.

### Identify the entity from an alert

Identify the specific asset or user involved in the alert to establish a starting point for your investigation.

  1. Go to the **Alerts** page.

  2. In the **Detections** table, click the alert name to open the alert page.

**Note:** If the **Inputs** table only displays a file hash, you won't see a direct asset ID. You must run a UDM search using that hash to identify the specific asset associated with it.
  3. Locate the **Inputs** table.

     * If the table contains **Entities** , do the following:

       1. Click the entity name to open the **Entity context** tab.

       2. Identify the related entities (for example, a specific hash, IP address, or asset name).

       3. Copy the **Asset ID** or **Username**.

     * If the table contains **Detections** or **Events** , do the following:

       1. For detections, click the **Detection** row to view the underlying events.

       2. Click the event row to open the **Event viewer** tab.

       3. In the **Entities** tab, identify the related entities (for example, a specific hash, IP address, or asset name).

**Note:** If only a hash is visible, run a UDM search to identify the specific asset associated with that hash.
       1. Copy the **Asset ID** or **Username** identified in the alert.



### Pivot to risk analytics

Use the identifier found in the alert to access the entity's broader risk profile within the analytics dashboard.

  1. Go to the **Risk Analytics** dashboard.

  2. Go to the **Entities** tab and paste the copied identifier into the search bar.

  3. From the results, click the entity name to view the **Detections Timeline** of the asset. The **Detections Timeline** gives the historical context of the asset or user.




### Analyze detections timeline

  1. Examine the list of detections (for example, `19 detections`) that contributed to the current risk score.

  2. Review the timeline to see how UDM events and ECG relationships have evolved over time to determine the severity of the incident.




**Note:** If you ignore the timeline and only look at the single alert, you might miss overlapping detection patterns that indicate a larger, coordinated threat.

## Troubleshooting

This section outlines performance expectations and provides self-service fixes for common investigation issues.

### Latency and limits

Be aware that the correlation of new events into your timeline takes approximately 10–15 minutes due to sync latency. Avoid re-running searches or filing a support ticket during this window.

### Common investigation issues

Use the following table to solve common investigation gaps.

Issue  | Description  | Fix  | Missing asset ID  | Your alert only shows a file hash or IP address without a linked asset.  | Run a UDM search for that hash or IP to identify the associated `principal.asset_id`.   
---|---|---  
Empty timeline  | The entity exists in Risk Analytics but no detections are listed.  | Ensure that the entity has triggered detections. If it has, verify whether your ECG ingestion pipeline is active.   
  
### Validation and testing

After your investigation, you can optionally use the UDM Search to verify that specific events found in the timeline exist as raw logs, which confirms the accuracy of the correlation.

### What's next

[Investigate an alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert)

[Investigate a GCTI alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-uppercase-alert)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
