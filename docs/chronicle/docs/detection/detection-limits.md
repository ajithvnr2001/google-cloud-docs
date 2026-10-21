---
url: https://docs.cloud.google.com/chronicle/docs/detection/detection-limits/
title: Detection limits reference \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:46:37.259445+00:00
---

# Detection limits reference  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/detection-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Detection limits reference

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google Security Operations has the following limitations with regards to rule detections:

  * Each rule version has a limit of 10,000 detections per day. This limit resets at midnight UTC.

For example, a rule version might generate 9,900 detections by 3 PM UTC on January 1. If all these detections are recorded for January 1, it generates only 100 more detections that day. On January 2, the rule version can generate 10,000 new detections.

  * If the rule version is updated, the limit is reset and the rule can again generate 10,000 detections in that same day.

For example, if a rule version produces 9,900 detections by 3 PM UTC on January 1, and all of these detections have a detection time on January 1, it generates only 100 more detections for that day. If rule version is updated at 4 PM on January 1, the rule version can generate 10,000 detections with a detection time on January 1 until the end of day. On January 2, the rule version can generate another 10,000 new detections.

  * The **Rules Dashboard** can display up to 50 MB of detection data. If the total size of the detections exceeds this limit, the interface shows a message indicating that the data is incomplete. This means the system generated more detections than the interface can display, but the detections still exist and are not lost.

  * Running a retrohunt after updating the reference list doesn't reset the existing detections limits or generate new ones. If the existing detection limit has already been reached, no new detections are generated.

  * [Retrohunts](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-historical-data) limitations:

    * Run a maximum of 3 concurrent retrohunt jobs for each Google SecOps instance or tenant.
    * The combined text size of all rules must not exceed 1 MB.
    * If you run multiple retrohunts in parallel, the system allocates resources from the same Google SecOps instance. This can lead to slower performance or delays in job completion.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
