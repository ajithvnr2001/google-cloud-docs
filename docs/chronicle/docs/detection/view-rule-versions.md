---
url: https://docs.cloud.google.com/chronicle/docs/detection/view-rule-versions/
title: View rule versions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:49.279453+00:00
---

# View rule versions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/view-rule-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View rule versions

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

You can create multiple versions of a rule. This lets you to experiment with your rule logic for a more nuanced examination of your event data.

**Note:** Any detections made with a version of a rule remain with it. If you switch to a different version of a rule, the detections you view are associated with that version and that version only.**Note:** Rules can create detections on existing data. During reprocessing of enriched events, a rule can create a detection on an event that was modified (enrichment reoccurred) or on an event that matches the logic of a new rule version.

To view the versions of a rule, navigate to the Rules Editor:

  1. Select a rule.
  2. Click the rule menu icon and select **View Versions** as shown below.

![View Rule Versions](https://docs.cloud.google.com/chronicle/images/rule-view-versions.png)**View Versions menu option**

  3. Rule versions view is displayed.

From this view, you can select any of the previous versions of the rule. Rule versions are labeled with the time it was created.

  4. This view provides you with a number of options:

     * **SAVE AS NEW** —Saves the currently displayed version of the rule as a new and separate rule.
     * **VIEW DETECTIONS** —Display the detections stored with this version of the rule. Note: These detections might not be current depending on the age of the rule version.
     * **RUN TEST** —Test the current version of the rule in real time, enabling you to determine the effectiveness of this version of the rule.
**Note:** Detections found through the test are not saved.
  5. When you have finished examining the versions of the selected rule, click **EXIT** to return to the Rules Editor.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
