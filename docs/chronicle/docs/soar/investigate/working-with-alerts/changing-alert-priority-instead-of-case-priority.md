---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/changing-alert-priority-instead-of-case-priority/
title: Change alert priority \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:02:40.219471+00:00
---

# Change alert priority  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/changing-alert-priority-instead-of-case-priority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change alert priority

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies both to SOAR standalone customers and Google SecOps unified customers using the legacy cases experience. 

This document outlines the best practice for managing priority within security cases. As such, we highly recommend setting and changing priority at the alert level instead of directly changing the case priority. This practice leverages the system's priority inheritance model to prevent severe issues from being misclassified.

## Risk of direct case priority changes

If you change the case priority directly, each incoming alert and its attached playbook logic can override the established case severity. For example, if a _Critical_ alert is grouped with a subsequent _Low_ alert, the case priority may drop to _Low_ , causing important issues to go undetected.

## Alert-level priority benefits

When you change the alert priority, the case automatically inherits the highest priority of all grouped alerts. This inheritance makes sure that a subsequent alert with a lower priority doesn't override a critical severity previously assigned by another alert.

## Change the priority of an alert

There are two ways you can change the priority of the alert:

  * **Action-based** : Use the **Change Alert Priority** action, configured either within a playbook or run as a manual action.
  * **Direct modification** : Change the priority through the alert interface:
    1. Locate the target alert (via the **Alert Options** menu on the **Alerts** tab in the legacy experience, or within the alert details side drawer in the enhanced experience) and select **Change Priority**.
[ ![changealertpriority](https://docs.cloud.google.com/static/chronicle/images/soar/changealertpriority.png)](https://docs.cloud.google.com/static/chronicle/images/soar/changealertpriority.png)
    2. In the **Change Alert Priority** dialog, select the required priority and click **Save**.  


**Note:** You can still change the case priority if required, but we don't recommend this as a best practice because of the inheritance risks.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
