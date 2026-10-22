---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/handle-large-alerts/
title: Manage large alerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:28.236143+00:00
---

# Manage large alerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/handle-large-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage large alerts

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Most security alerts ingested through connectors or webhooks don't impact system performance. However, alerts that exceed 26.7 MB (28 million characters) or exceed specific event and relation count thresholds trigger automatic mitigation processes, known as trimming, to prevent processing delays. 

This page describes the different trimming mechanisms, their limitations, and best practices to prevent alerts from being trimmed. 

### Pre-ingestion alert trimming (Size-based)

When the size of an alert exceeds 26.7 MB (28 million characters), the platform triggers a phased trimming process before the alert is queued for ingestion. The platform executes each phase sequentially, initiating the next phase only if the previous phase fails to reduce the alert size below 26.7 MB: 

  1. **Trim largest data field:** The system identifies the largest field within the raw data for every event. If the field's value exceeds 35 characters, the value is replaced with the literal string: `"Trimmed due to alert size violation."`
  2. **Trim field count:** The total number of data fields in each event is limited to a maximum of 100 fields, giving preference to shorter fields. Any fields exceeding this limit are removed. 
  3. **Trim event count:** The total number of events in the alert is limited to a maximum of 50 events, giving preference to shorter events based on raw data size. Any events exceeding this limit are removed. 



#### Visibility and notifications

  * **System notification:** When an alert is trimmed, a system notification is issued with the following message:  
`Alert <alert name> with ID <alert id> was trimmed due to maximum alert size violation. Please check connectors configuration`
  * **Case view:** There is no direct visual indication on the case itself, but the alert fields contain an attribute set to `isTrimmed: true`. 



### Ingestion pipeline trimming (Event-count limits)

If an alert contains more than 500 events, excess events are dropped during ingestion. 

  * **Alert property:** The alert is tagged with the property `IsCaseEventsOverFlowFlag: true`. 
  * **Mock case notification:** Every 60 minutes, a mock case with the suffix `***OVERFLOW***` is created to notify administrators. 



### Entity and relation trimming

To maintain performance, the system limits the number of entities and relations within an alert to a maximum of 500. 

The trimming is executed as follows:

  1. **Duplicate relation trimming:** If relations exceed 500, duplicate relations (where the same two entities are connected in multiple events, even with different identifiers) are removed first. 
  2. **One-to-many entity and relation trimming:**
     * The system identifies "important entities" that are associated with 15 or more "related entities" of the same type. 
     * For these related entities, the system: 
       * Retains only the most frequent entity type.
       * Excludes entities with more than one relation.
       * Excludes entities that are also classified as important entities.
     * The system deletes related entities and their associated relations until the total count is below 500, while maintaining the proportion of each entity type consistent with the original set. 



#### High-limit exemption

If an alert initially contains more than 10,000 entities or relations, **no trimming is performed**. This exemption prevents corrupting alerts with severe source connector or ontology mapping issues. 

### Best practices to avoid trimming

To prevent your alerts from being trimmed, apply the following optimizations:

  * **Filter unnecessary fields:** Configure your connectors or webhook sources to only send essential fields and exclude large diagnostic payloads. 
  * **Limit event volume:** Set up ingestion filters to group alerts logically or restrict the maximum number of events pulled per polling cycle. 
  * **Optimize ontology mapping:** Make sure ontology mappings are precise and don't generate unnecessary entity relationships that could push the alert over the 500 or 10,000 entity limits. 
  * **Avoid large field values:** Make sure fields don't capture massive, unstructured data blobs (such as raw log dumps or base64 files) that exceed the 35-character single-field threshold. 



For information about default service limits, see [Service limits](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/service-limits). 

To request adjustments to limit parameter values, contact [Google Support](https://console.cloud.google.com/).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
