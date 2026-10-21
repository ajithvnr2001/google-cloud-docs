---
url: https://docs.cloud.google.com/chronicle/docs/detection/risk-based-alerting/
title: Enable risk-based alerting \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:01:16.479925+00:00
---

# Enable risk-based alerting  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/risk-based-alerting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable risk-based alerting 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

With the `ENTITY_RISK_CHANGE` Unified Data Model (UDM) event type, you can write YARA-L detection rules that trigger independently of ingested events. This capability lets you focus specifically on changes in an entity's risk score, significantly decreasing the time required for Google Security Operations to detect and alert on shifting entity risk levels. This document explains how to monitor risk scores using this UDM event type in your rules.

In Search, you can display events tagged with `ENTITY_RISK_CHANGE` using the following YARA-L syntax. Be aware that raw log search doesn't support entity search.
    
    
    metadata.event_type = "ENTITY_RISK_CHANGE"
    

**Note:** Event ingestion doesn't count against your [ingestion rate limit](https://docs.cloud.google.com/chronicle/docs/reference/service-limits#ingestion_rate) and doesn't have any effect on billing.

## Examples: ENTITY_RISK_CHANGE rules

This section shows two single-event rule examples for efficient risk tracking, which helps you avoid the complexity and lower limits of multi-event rules. For information on your Rules quota, see [Display Rules quota](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-live-data#display_rules_quota).

### Detect when an entity's risk score exceeds 100

The following example rule uses the `ENTITY_RISK_CHANGE` event type to detect when an entity's risk score exceeds 100:
    
    
    rule entity_only_risk_change {
      meta:
        author = "test@google.com"
        description = "Alert on entities crossing a threshold"
      events:
        // Check only Entity Risk Change events
        $e1.metadata.event_type = "ENTITY_RISK_CHANGE"
    
        // Check for a Risk Score change with 100 as the threshold 
        $e1.extensions.entity_risk.risk_score >= 100
    
      outcome:
        // Reset risk score to prevent feedback
        $risk_score = 0
    
      condition:
        $e1
    }
    

### Filter entities with risk scores over 0

The following example rule uses the `ENTITY_RISK_CHANGE` event type to track when the risk scores of entities exceed 0:
    
    
    rule entity_only_risk {
      meta:
         author = "test@google.com"
         description = "Track changing risk per hostname"
      events:
         // Filter for Risk Change events with risk scores greater than 0
         $e1.metadata.event_type = "ENTITY_RISK_CHANGE"
         $e1.extensions.entity_risk.risk_score > 0
    
         // Deduplication
         $e1.extensions.entity_risk.risk_window_has_new_detections = true
    
         // Aggregation data
         $hostname = $e1.about.hostname
         $risk_score = $e1.extensions.entity_risk.risk_score
      match:
         $hostname over 5m
      outcome:
         $calculated_risk_score = sum($risk_score)
         $single_risk_score = max($risk_score)
      condition:
         $e1
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
