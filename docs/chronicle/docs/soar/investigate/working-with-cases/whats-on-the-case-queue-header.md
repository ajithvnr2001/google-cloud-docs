---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-queue-header/
title: Manage cases from the case queue \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:28.130913+00:00
---

# Manage cases from the case queue  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-queue-header/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage cases from the case queue

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies both to SOAR standalone customers and Google SecOps unified customers using the legacy cases experience. 

The case queue header provides quick access to key actions and display options for managing and reviewing cases. Use the controls in the header to customize your view, apply filters, and take bulk or individual actions on selected cases.

## Navigate the case queue header

This section describes the available options on the case queue header.

### Sort cases

You can sort cases in the queue based on various criteria to help with organization and prioritization. Available options include the following:

  * **By ID** : High to Low / Low to High
  * **By Time Created** : Newest to Oldest / Oldest to Newest
  * **By Modified** : Newest to Oldest / Oldest to Newest
  * **By Playbook Status** : Success to Failure / Failure to Success
  * **By Priority** : High to Low / Low to High
  * **By SLA** : Longest to Shortest / Shortest to Longest



## Switch between side-by-side view and list view

Analysts can choose to see cases in either the **side-by-side** view (default when you open the **Cases** page) or the **List** view.

  * To switch between the **side-by-side** view and **list** view, click ![sbslistviewicon](https://docs.cloud.google.com/static/chronicle/images/soar/sbslistviewicon.png)**Cases view selection**.



The **List** view displays all open cases in a single space, which helps with triage, sorting, filtering, customization, and updating case information. 

You can also do the following with the **List** view:

  * **Manage columns** : Click  view_column  **Manage columns** to hide or display specific columns. 
  * **Clickable Case ID** : Click a case ID to open a specific case.



Both views support the following actions:

  * **Apply Filters** : Narrow your case search. Filters applied in one view also apply in the other. For more information about filters, see [Apply and save filters](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters). 
  * **Create a manual case/simulate cases** : Click  add **Add** to [Create a manual case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case) or [Simulate cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/simulate-cases). 
  * **Merge cases** : For details about how to merge cases, see [Merge Cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-queue-header#merge-cases). 
  * **Close cases** : For details about how to close a case, see [How to close cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases). 



### Switch to Compact view

You can switch to a **Compact** view to display essential information like playbooks, their status, alert count, and assigned roles. This view is useful for a quick glance at cases in the queue.

To switch to **Compact** view, click  sync_alt  **Switch to Compact view**.

### Merge cases

You can merge cases directly from the case queue (from both the **side-by-side** view and the **List** view). This lets you review and consolidate the case information and determine which cases should be merged.

### Merge cases from the side-by-side view

To merge cases from the **Side-by-side** view, follow these steps:

  1. Click ![multipleselecticon](https://docs.cloud.google.com/static/chronicle/images/soar/multipleselecticon.png)**Multiple Selection**.
  2. Select the required cases in the case queue.
  3. Click menu **Menu**.
  4. Click **Merge Cases**.
  5. In the **Merge Cases** dialog, select the parent case that contains the merged cases.
  6. Click **Merge**.



### Merge cases from the List view

To merge cases from the **List view** , follow these steps: 

  1. Click ![mergecasesicon](https://docs.cloud.google.com/static/chronicle/images/soar/mergecasesicon.png)**Merge cases**.
  2. In the **Merge Cases** dialog, select the parent case that contains the merged cases.
  3. Click **Merge**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
