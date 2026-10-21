---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-new-case-close-root-cause-admin/
title: Configure the close case dialog \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:52.007726+00:00
---

# Configure the close case dialog  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/add-new-case-close-root-cause-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure the close case dialog

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to customize the **Close Case** dialog in Google Security Operations (Google SecOps). By default, the dialog includes the **Reason** , **Root Cause** , and **Comment** fields. Administrators can extend this dialog by adding custom parameters and root causes to improve the consistency and quality of case documentation.

Learn more about [how to resolve and close cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases).

## Add a custom field

To customize the **Close Case** dialog with additional parameters, complete the following steps:

  1. Go to **SOAR Settings > Case Data > Close Case**.
  2. Click add **Add Custom Parameters**.
  3. Complete the common fields:
     * **Name:** Enter a name for the new parameter.
     * **Type:** Select a field type to add from the **Type** menu:
**Note:** For the **Radio Button** , **Single Choice List** , and **Multi Choice List** types, press **Enter** after each item in the content field to add it as a separate entry. 
       * **Free Text** : Enter a name for the field to let the analyst enter custom details for that case. For example, name the field **Customer phone number** , and the analyst can enter the relevant contact details.
       * **Radio Button** : Select one of two options. For example, to specify whether a case was resolved or needs escalation, in the **Radio Button Content** field, use **Mitigated** or **Escalated** to indicate the case resolution status.
       * **Single choice list** : A list where the analyst selects one option. For example, to categorize the type of threat identified in a case, use options like **Malware** , **Phishing** , or **Insider Threat** to classify the threat type.
       * **Multi choice List** : Select multiple options. For example, to log incident actions, include options such as **Containment Measures Implemented** , **System Patches Applied** , **User Education Provided** , **Alerts Updated** , or **Access Revoked**.
     * **Default Value:** Optionally set a default for the **Close Case** dialog. Leave the **Default Value** field blank if no option is pre-selected. To remove a default value you've set, click **Reset**.
     * **Description:** Enter a description that appears as a tooltip when you hold the pointer over the info next to the parameter in the **Close Case** dialog.



## Add a new root cause

To add a new root cause to the **Root Cause** menu, follow these steps:

  1. Go to **SOAR Settings > Case Data > Close Case**.
  2. Click add**Add Root Cause**. The **Add Case Close Root Cause** dialog appears.
  3. In the **Reason** list, select a reason, and enter relevant information in the **Root Cause** field.
  4. Click **Add** to save the root cause.



**Note:** The text you enter in the **Root Cause** field may appear differently when displayed in the Case Wall records. If you use PascalCase, Google SecOps automatically reformats the strings to space-separated lowercase words. For example: `BruteForceAttack` will appear as `brute force attack` in the Case Wall.

##  Case disposition and rule tuning

Disposition lets you identify "noisy" rules that produce high volumes of non-actionable alerts. When closing cases, you can categorize them as **Malicious** or **Non-Malicious** which corresponds to **True Positive** or **False Positive**.

To capture other closure types, or to keep the names **True and False Positive** , Google recommends creating a custom field (**Single Choice List**) labeled **Disposition** in the **Close Case** dialog. This approach ensures that the **Root Cause** field remains available to describe the technical origin of the case.

### Recommended disposition values:

  * True Positive: A legitimate security threat that required mitigation.

  * Benign Positive: A correct detection of authorized activity (for example, a sanctioned pentest). These values are primary candidates for tuning or exclusion lists.

  * False Positive: An incorrect detection caused by logic errors or "noisy" software behavior.

  * Undetermined: Insufficient data to reach a conclusion.




Analysts can use these dispositions in SOC dashboards to visualize the False Positive Rate per Rule ID, allowing engineers to prioritize which rules require immediate logic refinement. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
