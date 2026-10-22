---
url: https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started/
title: Detect threats with unified rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:04.158195+00:00
---

# Detect threats with unified rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Detect threats with unified rules

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide is for detection engineers who want to detect threats for their organization. It explains how to leverage the **Unified Rules** interface to accelerate your threat detection capabilities.

## Common use cases

Common use cases for this workflow include the following:

### Accelerated rule deployment

**Objective:** Quickly identify and enable curated detections for specific adversary tactics (for example, `Initial Access`).

**Value:** Reduces the mean-time-to-detect (MTTD) for common attack vectors without requiring manual rule development.

### Centralized rule lifecycle management

**Objective:** Monitor rule execution, status, and deployment history from a single console.

**Value:** Improves operational oversight and ensures that active detections are performing as expected.

## Key terminology

  * **Curated detections:** Prebuilt detection sets managed by Google Cloud security experts.

  * **Unified Rules interface:** A consolidated management console for both custom YARA-L rules and curated content.

  * **Rule deployment:** The state of a rule (live or archived) and its associated alerting configuration.

  * **Retro hunt:** A process that runs a rule against historical data to find past instances of a threat.




## Before you begin

If your team uses custom IAM roles, make sure you have the following permissions for working with the **Unified Rules** dashboard and editor.

If your organization uses Data Role-Based Access Control (Data RBAC), you must also have access to the scopes associated with the rules you want to manage. For more information, see [Data RBAC overview](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

### Unified Rules dashboard permissions

Permission  | Required IAM permission   
---|---  
`View` | 

  * `chronicle.rules.list`
  * `chronicle.retrohunts.list`
  * `chronicle.ruleDeployments.list`
  * `chronicle.legacies.legacySearchCustomerStats`
  * `chronicle.legacies.legacyGetRuleCounts`
  * `chronicle.legacies.legacyGetRulesTrends`
  * `chronicle.legacies.legacyGetCuratedRulesTrends`
  * `chronicle.sharedPreferenceSets.get`
  * `chronicle.sharedPreferenceSets.list`
  * `chronicle.rules.get`
  * `chronicle.rules.listRevisions`
  * `chronicle.legacies.legacyTestRuleStreaming`
  * `chronicle.legacies.legacyFetchAlertsView`

  
`Edit` | 

  * `chronicle.retrohunts.create`
  * `chronicle.ruleDeployments.update`
  * `chronicle.rules.modifyRules`
  * `chronicle.rules.create`
  * `chronicle.rules.update`
  * `chronicle.rules.verifyRuleText`

  
  
#### Saved views - list and create saved rule views

This section lists the permissions required to create saved views. Saved views let you create and save a custom set of rule filters, column sets, and sorting orders for quick access on your **Unified Rules** dashboard.

Permission  | Required IAM permission   
---|---  
`Manage` | 

  * `chronicle.sharedPreferenceSets.get`
  * `chronicle.sharedPreferenceSets.list`
  * `chronicle.sharedPreferenceSets.create`
  * `chronicle.sharedPreferenceSets.update`
  * `chronicle.sharedPreferenceSets.delete`

  
  
### Rules editor permissions

Component  | IAM permission (if you use IAM)  | Analyst permission (if you use legacy RBAC)   
---|---|---  
**Rules editor** page  | `chronicle.ruleDeployments.list` `chronicle.rules.list` | `detectRulesView`  
Related reference list section  | `chronicle.referenceLists.get` `chronicle.referenceLists.list` | `referenceListView`  
Related data table section  | `chronicle.dataTables.get` `chronicle.dataTables.list` | N/A   
**Create new rule** button  | `chronicle.rules.verifyRuleText` `chronicle.rules.create` | `detectRulesCreate`  
**Test rule** button  | `chronicle.legacies.legacyRunTestRule` | `detectRulesRun`  
**Rule scope** menu  | `chronicle.rules.update` | `detectRulesEdit`  
**Save rule** button  | `chronicle.rules.update` | `detectRulesEdit`  
**Save as new rule** button  | `chronicle.rules.create` | `detectRulesCreate`  
**Rule retro hunt** button  | `chronicle.retrohunts.create` | `detectRulesRun`  
**Rule live** toggle  | `chronicle.ruleDeployments.update` | `detectRulesEdit`  
**Rule alert** toggle  | `chronicle.ruleDeployments.update` | `detectRulesEdit`  
**Rule run frequency** toggle  | `chronicle.ruleDeployments.update` | `detectRulesEdit`  
**Rule archive and unarchive** toggle  | `chronicle.ruleDeployments.update` | `detectRulesEdit`  
View curated rule in editor  | `chronicle.featuredContentRules.list` | N/A   
  
## Manage your unified interface preferences

You can switch between the unified experience and the legacy view for both the **Unified Rules** dashboard and the rules editor. Once you make a selection, your instance saves your preference and loads that specific version by default.

  * **Unified Rules dashboard:** To opt in to the **Unified Rules** dashboard, navigate to the **Rules** dashboard and click **Try our new Unified Rules page**. To opt out, click **Go back to the legacy Rules dashboard**.

  * **Rules editor:** To opt in to the new rules editor, navigate to the rules editor page and click **New rule editor page**. To opt out, click **Legacy rules editor page**.




## Curated saved views

The **Unified Rules** dashboard includes default saved views that let you quickly filter and organize rules. The following table describes these default curated saved views:

Saved view | Description | Filter criteria  
---|---|---  
**Unhealthy rules** | Displays rules that are having execution issues or are in a non-default execution state. | Non-archived rules with `execution_state` not equal to `default`.  
**Live and alerting Google rules** | Displays curated rules authored by Google that are live and configured to generate alerts. | Rules with `rule_owner` set to `GOOGLE`, `archived` set to `false`, `alerting_enabled` set to `true`, and `live_mode_enabled` set to `true`.  
**Rules that use ECG** | Displays rules that leverage Entity Context Graph (ECG) data. | Non-archived rules that use `graph.entity`.  
**Persistence & privilege escalation rules** | Displays rules related to persistence and privilege escalation tactics. | Non-archived rules tagged with `TA0003` (Persistence) or `TA0004` (Privilege Escalation).  
**Mandiant recommended rules** | Displays high-confidence, expert-vetted rules curated by Mandiant. For more information, see [Mandiant recommended rules](https://docs.cloud.google.com/chronicle/docs/detection/mandiant-recommended). | Non-archived rules tagged with `google.mandiant.recommended`.  
  
## Accelerate threat detection with curated rules

You can use the **Unified Rules** interface to identify detections for specific MITRE ATT&CK tactics. To find rules with alerting enabled and are related to initial access, do the following:

  1. Navigate to the **Unified Rules** dashboard.

  2. Use the search bar to filter for specific threats.

For example, to find curated rules related to initial access (MITRE ATT&CK tactic `TA0001`), use the following search query:

`alerting_enabled = true AND tags:"TA0001"`

For complex filtering, see the advanced syntax on the [Search](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/search-rules-list) rules page.

  3. Optional: Select a rule from your search results to view the rule details.

  4. Click more_vert **Menu** adjacent to the rule that you want to deploy.

  5. Click the **Live rule** and **Alerting** toggles to begin actively detecting threats.




You can track the rule's execution, status, and alert history from your dashboard.

## Use saved views

The **Unified Rules** dashboard supports saved views. Saved views let you create and save a custom set of rule filters, column sets, and sorting orders for quick access on your **Unified Rules** dashboard.

**Important:** Data role-based access control (Data RBAC) governs rule visibility. While saved view configurations are globally accessible to all authenticated users, the underlying rule data is only rendered if the user possesses the appropriate scope access. For information about data RBAC, see [Data RBAC overview](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

### Create a custom view

  1. Navigate to the **Unified Rules** dashboard.

  2. Click the **Saved views** menu and select **Save as a new view**.

  3. Type the view name and click **Save**.

  4. Configure your target filters, columns, and sorting order in the **Unified Rules** dashboard.




### Apply a saved view

To update the dashboard with a saved configuration, do the following:

  1. Navigate to the **Unified Rules** dashboard.

  2. Click the **Saved views** menu and select the required saved view from the list.

  3. Click **Save**.




### Manage saved views

To modify, rename, hide, or delete a saved view, do the following:

  1. Click the **Saved views** menu and select **Manage views**.

  2. Click **Save**.


**Note:** If the active dashboard state diverges from the applied view (for example, through adjusted filters or sorting parameters), an asterisk (*) appears next to the view name in the **Saved views** menu. To commit these changes and overwrite the existing configuration, click **Save**.

## Troubleshooting

This section provides information to resolve common issues and understand the limitations of the **Unified Rules** interface.

### Latency and limits

  * **Rule execution:** There may be a short propagation delay (typically a few minutes) between saving a rule and seeing its first execution metrics in the dashboard.

  * **Retro hunt limits:** Curated detections cannot be run as retro hunts. Additionally, retro hunts are subject to lookback window limits based on your data retention tier.




### Error remediation

Error code  | Issue description  | Fix  | 403 Forbidden  | Missing permissions to view curated content.  | Ensure `chronicle.featuredContentRules.list` is added to your IAM role.   
---|---|---  
Deployment failed  | Rule syntax error or conflict.  | Use the **Test rule** button in the Rules editor to validate YARA-L syntax.   
`user does not have access to scope <scope_name>` | The user doesn't have the Data RBAC permissions needed for the scope assigned to the rule.  | Ensure you have access to the required scope. For more information, see [Configure Data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users).   
`The rule has been modified by someone else` | Another user has saved a new version of the rule since you opened it.  | Copy your changes, refresh the page to load the latest version, and then re-apply and save your changes.   
`rules editing not enabled` | Rule editing is disabled for your Google SecOps instance.  | Contact your administrator to enable rule editing.   
  
## What's next

  * [Manage Unified Rules](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/manage-unified-rules)

  * [Search the Unified Rules list](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/search-rules-list)




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
