---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-tags-in-cases-admin/
title: Manage case and alert tags \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:55.035192+00:00
---

# Manage case and alert tags  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-tags-in-cases-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage case and alert tags

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to manage tags in Google Security Operations cases.

Tags help classify and organize cases for easier filtering and analysis. They can be assigned automatically based on predefined rules or added manually from the case and alert views. 

While you can remove tags from individual cases, the tags themselves remain available in the system's autocomplete list unless an administrator removes them from the table in the **Case Data > Tags** settings.

You may also want to import tags—for example, when migrating from a staging to a production environment or for backup purposes. For more information, see Import tags.

## Manage tags in cases and alerts

Tags help you track and categorize your cases. You can quickly identify cases by searching for them by their tags. 

You can manage tags from the following places:

  * **Case or Alert** : Manually add and remove tags from a specific case or an individual alert.
  * **Main menu** : Click **Settings > Case Data > Tags**. For more information, see Create an automatic tagging rule. 
  * **Playbooks** : Trigger a playbook on a tag name using the tag trigger. You can also add a case tag to a playbook block: select a playbook block, click **Open Step Selection** , and in the **Triggers** tab, select **Tag Name**. 

**Note:** To add or manage case tags, the SLA module must be enabled in your environment, in addition to standard case management permissions. 

### Add a tag to a case

To add a tag to a case, follow these steps:

  1. Go to the **Cases** page and select a case you want to tag.
  2. Click  sell  **Manage Tags**.
  3. In the **Manage Tags** dialog, enter the name of the tag and press **Enter** , or select a tag from the list and click **Add**.



### Add a tag to an alert

To add a tag to an alert, follow these steps:

  1. Go to the **Cases** page and select a case.
  2. Select the alert you want to tag.
  3. Click  more_vert  **Alert Options** and then select **Manage tags**.
  4. In the **Manage Tags** dialog, enter the name of the tag and press **Enter** , or select a tag from the list and click **Add**.

**Note:** The ability to create new tags (tags that don't already exist in the system) versus attaching existing tags depends on your specific user permissions. 

### Alert tag behavior during case changes

Manually assigned alert-level tags remain attached to the specific alert during case management actions:

  * **Moving alerts** : If you move an alert to a different case, any tags manually assigned to that alert move with it.
  * **Merging cases** : When cases are merged, individual alerts within the consolidated case retain their manually assigned alert-level tags.

**Note:** Alert-level tags are supported only in built-in dashboards. They are not supported in legacy reports. 

## Configure tag settings

### Import tags

To import a tag, follow these steps:

  1. Go to **SOAR Settings > Case Data > Tags**. 
  2. Click  vertical_align_bottom  **Download template**. The CSV file shows the required tag import structure.
  3. Enter the tag information.
  4. Click  login  **Import**. The imported tags should appear in the platform.

**Note:** The relationship between **Assigned Tag** and **Search Name** is many-to-many. That is, more than one Assigned Tag can be associated with one Search Name, and more than one Search Name can be associated with one Assigned Tag. For example, Google SecOps assigns the same tag "DLP" to alerts that the SIEM tags as "Data Exfiltration" or "Symantec DLP – Financial Information – Network". 

### Remove a tag from autocomplete

To prevent a tag from appearing in autocomplete suggestions, you must remove it from the Tag table in the Case Data settings.

  1. Go to **SOAR Settings > Case Data > Tags**.
  2. Locate the tag in the table and click delete **Delete**.

**Note:** Deleting a tag from the Tag table removes it from autocomplete suggestions, but does not remove the tag from cases or alerts where it has already been applied. 

## Create an automatic tagging rule

To create a rule that automatically assigns tags to incoming alerts based on specific conditions, follow these steps:

  1. Go to **SOAR Settings > Case Data > Tags**. 
  2. Click  add  **Add Tag**.
  3. In the **Tag name** field, enter a name for the tag.
  4. Select a match source from **Entities** , **Product** , **Rule Generator** and **Vendor**.
  5. From the menu, choose a qualifier that defines how to match the value:
     * **contains**
     * **exact**
     * **starts with**
     * **ends with**
  6. Select the specific entity or product source. Enter the appropriate **Property** and **Value** , if applicable. Alternatively, select the **Product** , **Rule Generator** , or **Vendor**.
  7. Select the priority for the tag.  
Note: Google SecOps merges priority with other alerts and entities and events so that the priority here is not an absolute.
  8. Optional: Select **Can be a case name** if required. When selected, the tag is assigned as the title of the case if it meets the conditions. 
  9. Click **Save**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
