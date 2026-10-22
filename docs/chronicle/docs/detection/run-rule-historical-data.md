---
url: https://docs.cloud.google.com/chronicle/docs/detection/run-rule-historical-data/
title: Run a rule against historical data \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:40.317827+00:00
---

# Run a rule against historical data  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/run-rule-historical-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run a rule against historical data

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains the functionality of real-time rule execution and the retrohunt feature within the Google Security Operations platform. While new rules begin monitoring incoming events immediately, a retrohunt lets you apply the same detection logic to existing historical data to identify previously undiscovered threats. These historical searches are scheduled based on available system resources, and as such, completion times may vary.

**Note:** Running a retrohunt on a rule with alerting enabled creates a SOAR alert for every detection found. This volume can flood your system with overflow cases and temporarily block case creation for other alerts. To safely search historical data, we recommend running the retrohunt with the rule's alerting status disabled. Detections found this way don't trigger SOAR alerts. If you need alerts for the historical detections, create a new rule version with alerting enabled and run the retrohunt again.

To start a retrohunt, complete the following steps:

  1. Navigate to the Rules Dashboard.

  2. Click the Rules option icon for a rule and select **Yara-L Retrohunt**.

![Retrohunt](https://docs.cloud.google.com/chronicle/images/retrohunt.png)**YARA-L Retrohunt option**

  3. In the **YARA-L Retrohunt** window, select the start and end times for your search. The default is one week. The window provides the available date and time range. For multi-event rules, the retrohunt search range must be greater than or equal to the match window size.

  4. Click **RUN**.

![Retrohunt dialog Window](https://docs.cloud.google.com/chronicle/images/retrohunt-window.png)

**Yara-L Retrohunt dialog window**

  5. You can view the progress of the retrohunt run from the rule detections view for the rule. If you cancel a retrohunt in progress, you can still view any detections it was able to make while running.

  6. If you have completed multiple retrohunts, you can view the results of past retrohunt runs by clicking the date range link as shown in the following figure. The results of each run are displayed in the Timeline and Detections graph in Rule Detections view.

![Retrohunt Running](https://docs.cloud.google.com/chronicle/images/retrohunt-run.png)

**Yara-L retrohunt runs**

  7. If you use a reference list in a rule, run a retrohunt, and then remove items from that list, then you need to revise that rule to a new version to see the new results. Google SecOps doesn't delete detections from reference lists, so refreshing the rule won't update the results.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
