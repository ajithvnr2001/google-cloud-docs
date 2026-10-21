---
url: https://docs.cloud.google.com/chronicle/docs/yara-l/detection-event-sampling/
title: Detection event sampling \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:51:19.693091+00:00
---

# Detection event sampling  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/yara-l/detection-event-sampling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Detection event sampling

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Detections from multi-event rules contain event samples, which provide context about the events that triggered the alert. There is a limit of up to 10 event samples for each event variable defined in the rule. For example, if a rule defines 2 event variables, each detection can have up to 20 event samples. The limit applies to each event variable separately. If one event variable has 2 applicable events in this detection, and the other event variable has 10 applicable events, the resulting detection contains 12 event samples (2 + 10).

Any event samples over the limit are omitted from the detection.

If you want more information about the events that caused your detection, you can use aggregations in the [outcome section](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax) to output additional information in your detection.

If you are viewing detections in the UI, you can download all events samples for a detection. For more information, see [Download events](https://docs.cloud.google.com/chronicle/docs/detection/downloading-events).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
