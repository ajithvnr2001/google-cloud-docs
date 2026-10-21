---
url: https://docs.cloud.google.com/chronicle/docs/detection/rule-effectiveness/
title: Monitor rule performance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:15:53.090092+00:00
---

# Monitor rule performance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/rule-effectiveness/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor rule performance

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide is for security engineers who create, deploy, and monitor rules in Google Security Operations. It explains how to monitor rules to ensure they are working as intended and aren't consuming resources excessively using the data available in your Google SecOps instance. This data helps you debug delayed detections, understand the impact of late-arriving enrichment data on rules, and identify which rules have the highest mean time to detect (MTTD).

This guide provides documentation on the following tasks:

  * How to evaluate a rule during its initial release, receive alerts, and check the **Rules Dashboard** to monitor its health.

  * How to identify the cause of any detection delays (for example, whether it was due to late ingestion or inefficient logic) and either adjusting Mean Time to Detect (MTTD) reporting or tuning the rule with additional **Rule exclusions**.




## Before you begin

To view and modify rules as described in this document, you need to be a Chronicle API Editor. For more information, see [Google Security Operations roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle).

Prior to analyzing the effectiveness of rules in Google SecOps, you should develop a good understanding of the YARA-L language, YARA-L queries, how to create and manage rules, and how to create dashboards:

  * [YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started)
  * [Creating YARA-L queries](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started#build-first-search)
  * [Creating and managing rules](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started#build-rule)
  * [Creating dashboards based on YARA-L queries and rules](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started#create-widget)



## Key terminology

  * **Rules** : Identify threats automatically as log data is ingested into your Google SecOps account.
  * **Quotas** : Limits on your data ingestion volume, the number and complexity of queries you can run against your data, and the number and complexity of the rules you have active in your Google SecOps account.
  * **Alerts and detections** : Security issues identified by Google SecOps and your own security infrastructure that require your attention.
  * **Ingestion** : Process of importing your security data to Google SecOps and converting it to UDM.
  * **Rule replays** : Automatic reruns of rules against existing data in the event that relevant context data arrives or is processed later than the initial event data.
  * **Retrohunt** : Apply new rules to existing data to identify previously undiscovered threats.



## How to analyze rules

The following sections describe how to analyze the performance of your rules.

### Test and evaluate rules after deployment

When you first deploy a rule to production, monitor it in the `Rule Observability` dashboard for 24 to 48 hours:

  1. Navigate to **Dashboards**

  2. Search for `Rule Observability`.

  3. Search for the new rule in the **Rule** column. The **Rule Observability** dashboard includes statistics like the detection count, ingestion latency, and the time from ingestion to detection.




To ensure the rule logic isn't introducing artificial delays before it begins to generate high-priority alerts, you can use the [schema reference for detections](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#detections-fields). The schema defines the structured format used to monitor security alerts. It's optimized for tracking detection frequency, risk distribution, and rule performance. You can get a better sense of how to use the schema by taking a close look at the [Query examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#dashboard-query-examples-detections).

### Identify reason for rule result delay

Complete the following steps to determine whether rule results are delayed and, if so, why:

  1. Navigate to **Detections > Alerts & IOCs**.
  2. On the **Alerts** tab, find the **Detection Type** column.
  3. Search for alerts with a yellow light bulb icon.
  4. Hover over the icon to see if the detection was triggered by any of the following: 
     * **Rule reprocessing** : Generated due to a rule replay
     * **Retrohunt** : Triggered manually by a user.
     * **Delayed event data** : Generated due to a rule replay specifically because of late arriving data.



For a more detailed description of detections created due to rule reprocessing, see [rule replays](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays#replay-triggers).

### Filter alerts based on detection time

  1. Navigate to **Detections > Alerts & IOCs**.

  2. On the **Alerts** tab, use the filter element for the **Detection time** column to sort detections based on their arrival time.

  3. Click the refresh icon autorenew at the top of the table and click **Refresh Now**. You can see the latest alerts arriving in your Google SecOps account and the rule associated with each alert (check the **Rule name** column).




### Examine metadata

For additional insight into how your rules are performing, you can inspect the raw detection JSON using [`latencyMetrics`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Collection#latencymetrics) to find the difference between the `oldestEventTime` and the`oldestIngestionTime`.

#### Detection timing values

The following table lists the enumerated values associated with [`DetectionTimingDetails`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Collection#detectiontimingdetails):

  
**Value** |   
**Description** |   
**MTTD impact**  
---|---|---  
` UNSPECIFIED ` |   
Detection created within the standard scheduling window. |   
Ground truth for MTTD.  
` REPROCESSING ` |   
Generated due to a rule replay (for example, late-arriving data). |   
Represents operational risk; should be accounted for in reports.  
` RETROHUNT ` |   
Generated through a historical retrohunt run. |   
Typically filtered out of standard MTTD reporting.  
  
#### Example: `latencyMetrics` metadata

The following [`latencyMetrics`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Collection#latencymetrics) example shows the time difference between when an event occurred (`oldestEventTime` versus `newestEventTime`) and when the event was ingested (`oldestIngestionTime` versus `newestIngestionTime`). The latency between the event and the ingestion into the Google SecOps account is about 53 minutes.
    
    
    "detectionTimingDetails": ["DETECTION_TIMING_DETAILS_REPROCESSING"],
    "latencyMetrics": {
      "oldestIngestionTime": "2025-12-09T16:54:14Z",
      "newestIngestionTime": "2025-12-09T16:54:14Z",
      "oldestEventTime": "2025-12-09T16:01:06Z",
      "newestEventTime": "2025-12-09T16:01:06Z"
    }
      
  
---  
  
## Troubleshooting

The following table lists some of the issues you might have with your rules and how to resolve them:

  
Issue |   
Resolution  
---|---  
  
Lightbulb icon appears, but the enumeration is `UNSPECIFIED.` |   
This is normal behavior when the delta between event time and ingestion time exceeds 30 minutes. Use the **Data Health Hub** metrics to investigate the source of the ingestion delay.  
  
Detection appears late relative to the time of the event. |   
Check the `detectionTimingDetails`. If the enumeration value is `REPROCESSING`, the delay is likely due to late-arriving enrichment data rather than rule execution latency. If `UNSPECIFIED`, investigate the efficiency of the rule logic.  
  
Excess compute. |   
The rule is likely scanning too much data or has inefficient logic. Navigate to **Rule Exclusions** or use **Filter Offloading** to tune the rule to narrow its data search.  
  
## Known limitations

  * **Threshold rigidity:** The visual cue for late data is fixed at a 30-minute threshold and doesn't account for user-defined latency windows.
  * **Data health:** Rule observability informs rule health, but data health monitoring (closer to ingestion) is more effective for catching general late-arriving data issues.
  * **Quota enforcement:** While the dashboard shows resource usage, it doesn't provide real-time notifications when rules are nearing a quota limit.



## What's next

For information on rule replays and rule detection delays, see the following:

  * [Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays)

  * [Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays)

  * [UDM search compared with rule results](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-vs-rules-results)




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
