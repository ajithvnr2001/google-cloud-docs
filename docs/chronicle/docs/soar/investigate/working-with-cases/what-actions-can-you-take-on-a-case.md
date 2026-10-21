---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case/
title: Manage cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:43:13.477550+00:00
---

# Manage cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage cases

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the various actions you can perform on a case, including updating its status or priority, managing associated alerts, generating reports, and taking individual or bulk actions to streamline case handling.

## Mark a case as important

When you want to highlight a case, you can mark it as important. You can also remove the **Important** tag from the same menu.

To mark a case as important, follow these steps:

  * Click  format_list_bulleted  **Case Actions** , select a case to tag, and select **Mark as important** ; a yellow  arrow_drop_up  appears with the case.



## Mark a case as an Incident

If a case you're assigned is urgent and requires immediate action, mark it as an **Incident**. This automatically:

  * Sets the case priority to **Critical**
  * Changes the case stage to **Incident**
  * Assigns the case to the SOC Manager
  * Sends a notification to all analysts



To mark a case as an incident, follow these steps:

  1. On the **Cases** page, go to the relevant case.
  2. Click  format_list_bulleted  **Case Actions** and select **Incident**. 
  3. In the **Confirmation** dialog, click **Yes**. The page refreshes and the new incident appears in the case list with the incident icon and a red critical sidebar. The case is automatically assigned to a user with the SOC Manager role. 



## Change the case stage

If you're assigned a case, you can update its stage, based on your team's workflow. 

To change a case stage, follow these steps:

  1. Select a case from the queue. 
  2. Click  format_list_bulleted  **Case Actions** and select **Stage**. 
  3. Select one of the following stages: 
     * **Triage** : Initial phase when the case is created. This is the default. 
     * **Assessment** : The case is escalated to the next tier for evaluation. 
     * **Investigation** : The case is assigned an active investigation of alerts and entities. 
     * **Improvement** : The case is flagged for refining SOC detection rules or follow-up review. 
     * **Research** : The case is assigned a deeper investigation into external access or threat behavior to your organization. 
     * **Incident** : The final case stage for critical events. Once you select **Incident** , you can't change it. 
  4. Click **Save**.



### Change the case priority

To change the case priority, follow these steps:

  1. Select a case from the queue. 
  2. Click  format_list_bulleted  **Case Actions** and select **Priority**. 
  3. Choose one of the following levels, each has a corresponding case color indicator: 
     * **Informative** (gray)
     * **Low** (blue)
     * **Medium** (yellow)
     * **High** (orange)
     * **Critical** (red)
  4. Click **OK**. The case priority is changed.
  5. Optional: Click the color swatch to change the case bar color. 



### Download a case report

You can download a case report in DOC, XLSX, or CSV format. Reports include the following details: 

  * Case details 
  * Alerts, entities, and insights 
  * User and system activities 
  * Playbook actions and case activity 
  * All entries included in the case wall 



To download a report, follow these steps:

  1. Select a case from the queue. 
  2. Click  format_list_bulleted  **Case Actions** and select **Report**. 
  3. In the **Select Report Type** dialog, select the file type and then click **Select**.
  4. Open the downloaded file to view the report. 



## Manage alerts within a case

To manage specific alerts within a case, do the following:

  1. On the **Alert Options** menu (found on the **Alerts** tab in the legacy experience, or within the alert details drawer/canvas in the enhanced experience), click  more_vert **Alert Options**.
  2. Select one of the available options:
     * **Explore Alert** : For more information about the **Alerts Results** page, click [Investigate an alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert). 
     * **Ingest alert as test case******: Click**Ingest alert as test case** to add a new test case to the system. The system marks it as a **Test Case** for identification. Ingested alerts are excluded from dashboards and reports and are not grouped with other alerts.
     * **Change Priority:** We recommend changing the alert priority rather than the case's. Changing the alert priority doesn't affect the case's priority. For more information, see [Change alert priority instead of case priority.](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/changing-alert-priority-instead-of-case-priority)
     * **Move Alert** : If you're assigned a case with multiple alerts, you can either **Move the Alert to new case** or **Move Alert to existing case**. If you select **Move Alert to existing case** , choose the destination case from the menu and click **Move**. 
     * **Manage Alert Detection Rule** : Available only for Google Security Operations users.
       * If the rule is a predefined Google SecOps rule, the system redirects you to the **Rules Detection** page. For more information, see [Filter data in the Rule Detections view](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-rule-detections).
       * If the rule is a customer rule, the system redirects you to the **Rules Editor** page. For more information, see [Manage rules using the Rules Editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules).
       * **Close Alert:** Closes the alert within the case. Select a value from the **Reason** , **Root Cause** , or **Usefulness** field.
         * The **Usefulness** field appears only for Google SecOps users and helps rule analysts get more precise feedback on alert rules from customer input.
         * Closed alerts in a case appear unavailable and display a **Closed** tag. You can only close an alert if other alerts are present in the case and it's assigned to you.
       * **Add Entity:** Manually add an existing or new entity to an alert.



## Run a manual action in a case

Manual actions and playbook actions become available after you install the corresponding integration from the Content Hub.

To run a manual action in a case, follow these steps:

  1. In the selected case, click ![manualactionicon](https://docs.cloud.google.com/static/chronicle/images/soar/manualactionicon.png)**Manual Action**.
  2. In the **Manual Action** dialog, select the required action. For example, select **VirusTotalV3 > Enrich URL**. Enter the required information. 
  3. Select the alerts and entities the action should apply to.
  4. Click **Execute** to display the action details on the case wall.



## Simulate cases in Google SecOps

You can simulate a case populated with system-generated default alerts. Simulated cases are useful in staging environments or for demonstrations.

You can also create custom cases or import existing cases in JSON format using files with the `.CASE` suffix. 

To simulate a case, follow these steps:

  1. In the **Case queue** header, click add **Add a Case** , then select **Simulate Cases**.  

  2. In the **Simulate Cases** dialog, select a case from the list. 
  3. Click **Create**. 



### Create a new case

To create a new, simulated case, follow these steps:

  1. In the **Simulate Cases** dialog, click add **Add or import case** , then click **Add New Case**. 
  2. In the **Add New Case** dialog, enter the **Source/SIEM Name** , **Rule Name** (Rule Generator), **Alert Product** , **Alert Name** , **Event Name**
  3. Optionally, you can also provide: 
     * **Additional Alert Fields**
     * **Additional Event Fields**
  4. Click **Save**. The case appears in the **Simulate Cases** list. 
  5. Select the newly created case and click **Create**. 
  6. Select the target environment and click **Simulate**. The new case appears in the queue. 



### Import a case to a JSON file

To import a case to a JSON file, follow these steps:

  1. In the **Simulate Cases** dialog, click add **Add or import case** , then click **Import Case**. 
  2. Select the required case and click **Open**. The case is imported in JSON format. 



## Perform batch actions on multiple cases

You can perform batch actions on multiple cases from the case queue or the **Search** page.

Available batch actions include the following: 

  * **Export to CSV** : Downloads a list of selected cases and their metadata in CSV format for offline review or reporting.
  * [**Close case**](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases): You can close cases using various interface options, including the case details page, the case queue (side-by-side and list views), and the Search page. You can close a case once it's resolved.
  * **Reopen case** : Reopens previously closed cases to resume investigation or follow-up actions.
  * **Change priority** : Updates the priority level (Low, Medium, High, or Critical) of selected cases to reflect urgency or severity.
  * **Assign case** : Assigns a case to a specific user or group for further investigation.
  * [**Add tag**](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-tags-in-cases-admin): Applies one or more tags to selected cases to support filtering, categorization, or automation rules.
  * [**Merge cases**](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-queue-header#fourthanchor): Combines multiple related cases into a single case to reduce duplication and centralize investigation.
  * **Change stage** : Updates the stage of selected cases to reflect their progress or status.



To perform a batch action, follow these steps:

  1. Go to **Investigation** and click **SOAR Search** (or navigate to the case queue on the **Cases** page).
  2. Select the timeframe for the relevant cases.
  3. Select the cases using the required filter.
  4. Select the checkboxes to apply the relevant filters > **Apply**.
  5. In the **Results** list, select the checkboxes for the cases you want to modify.
  6. Select an action from the **Search Results** menu.



## Quick actions

The **Quick Actions** widget lets you define reusable actions that you can execute directly from cases and alerts. You can add this widget to the case view, alert view, and custom alert views in playbooks across both the legacy and enhanced experiences.

Defining parameters for Quick Actions is optional. If provided, you can review and modify them before execution. If left blank, parameters must be filled in at runtime.

If an integration is removed after a Quick Action is configured, the corresponding **Quick Action** button is hidden, and the widget is flagged in the configuration view to indicate a missing integration.

For setup instructions, see the following:

  * [Define default case view](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-default-view-for-cases-admin)
  * [Define default alert view](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/define-default-alert-view-admin)
  * [Define customized alert views from Playbook Designer](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/define-customized-alert-views-from-playbook-designer)



## Use case: Configure Quick Action for malicious file investigation

This use case shows how to create a Quick Action that helps investigate potentially malicious files within a case.

### Add the Quick Actions widget

  1. Go to **SOAR Settings > Case Data > Views**.
  2. Select **Default Case View**.
  3. Select the **General** tab.
  4. Drag the **Quick Actions** widget into the **Default Case View**.



### Configure the widget

  1. Click settings **Configuration**.
  2. In the **Quick Actions** side drawer, enter `File Investigation` for the widget title.
  3. For the widget description, enter `Quickly scan file hashes.`
  4. Optional: choose a widget width.
  5. Click **Advanced Settings**.
  6. In the **Conditions** section, define the criteria for displaying the widget. To show the widget only when a case is tagged with `malicious-file`, use the condition **`Case.Tags` contains `malicious-file`**. **Note:** The Quick Actions widget is displayed by default. However, if conditions are defined in the **Conditions** section, the widget will only appear when those conditions are met. This lets you control the visibility of the widget and ensure it's only displayed for relevant cases or alerts. 



### Add a Scan Hash button

  1. In **Text** , you can provide instructions or context directly within the widget. For this use case, add the following text: `Use the 'Scan Hash' button to check suspicious files.`
  2. In **Buttons** , click **\+ Add New Button** to create a new Quick Action. You can add up to six buttons, each corresponding to a different Quick Action.
  3. In the **Add Button** dialog that appears, configure the Quick Action (**Scan Hash**): 
     * **Name** : Scan Hash
     * **Button Color** : Choose a color.
     * **Action** : Select **Scan Hash** from the VirusTotal section in the **Action** list. **Note:** Only installed and configured integrations will be available in the list. 
     * Optional: choose the relevant **Instance** for VirusTotal.
     * Optional: in **Parameters** , define the **Hash** parameter:  
**Hash:** `[Case.FileHash]`
  4. In the **Add Button** dialog, click **Close**.
  5. In the **Quick Actions** side drawer, click **Save**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
