---
url: https://docs.cloud.google.com/chronicle/docs/detection/archive-a-rule/
title: Archive rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:04:13.784899+00:00
---

# Archive rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/archive-a-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Archive rules

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Archiving a rule enables you to hide the security data related to that rule (and all of its versions) without actually deleting the rule. Much of the functionality available for active rules (for example, enabling a rule) is not available for archived rules.

Note the following:

  * Rules Dashboard does not display archived rules.
  * Test Rule can be used on archived rules.



## Viewing rules

Complete the following steps to navigate to the **View Rules** page:

  1. In the navigation bar, click **Detection > Rules & Detections**.
  2. Select the **Rules Editor** tab to view the rules page.
  3. Click the filter icon at the top-right corner of the left navigation tab. The menu provides the following options: **Show All** , **Active Rules** , and **Archived Rules**.



## Viewing rule detections

On the **Rules Editor** tab, select **View Rule Detections** from the drop-down list available on the top-right corner. The **Rule Detections** page appears.

## Archiving a rule

To archive a rule, complete the following steps:

  1. Select a rule in the left navigation and click the option icon in the top- right corner of the Google Security Operations user interface. Select **Archive Rule** from the menu.

Note the following:

     * Archiving is allowed even if the Alerting toggle is ON, it is automatically disabled.
     * Archiving is NOT allowed unless the Live toggle is disabled.
     * Archiving is NOT allowed unless there are NO Retrohunts in progress.
  2. The following window is displayed with a message confirmation.

![Confirm Archive message](https://docs.cloud.google.com/chronicle/images/confirm-archive-1.png)**Confirm Archive message**

![Confirm Archive message continued](https://docs.cloud.google.com/chronicle/images/confirm-archive-2.png)**Confirm Archive message continued**




## Unarchiving a rule

To unarchive a rule, complete the following steps:

  1. Click the option icon for a specific rule in the left navigation pane. A menu appears with the following options: **View Detections** , **Duplicate** , and **Unarchive**.

  2. Select **Unarchive**.

  3. Select a rule in the left navigation pane and click the option icon in the top right corner of the Google SecOps user interface. A menu appears with the following options: **View Detections** , **Duplicate** , and **Unarchive**.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
