---
url: https://docs.cloud.google.com/recommender/docs/insights/using-insights/
title: Insights \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:52.688850+00:00
---

# Insights  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/insights/using-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Insights

Recommender uses machine learning to provide detailed and high quality _insights_. Insights are findings that you can use to proactively focus on important patterns in resource usage. You can use insights independently from recommendations. Some insights link to [recommendations](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations) and provide evidence for the associated recommendations.

This page describes key concepts for interpreting and using insights.

## Insight types

Each insight has a specific _insight type_. Insight types are specific to a single Google Cloud product and resource type. A single product can have multiple insight types, where each provides a different type of insight for a different resource.

Each insight type has a unique insight type ID that identifies the service internally. You use the insight type ID when interacting with insights using the Recommender [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/recommender), or the [REST](https://docs.cloud.google.com/recommender/docs/reference/rest) or [RPC](https://docs.cloud.google.com/recommender/docs/reference/rpc) APIs.

For more information, see [Insight types](https://docs.cloud.google.com/recommender/docs/insights/insight-types).

## Insights

An _insight_ is a machine-generated finding that may be linked to one or more recommendations. An insight has the following core attributes:

  * Name
  * Description
  * Insight Subtype
  * Content
  * Category
  * Target Resources
  * State Info
  * Etag
  * Severity
  * Last Refresh Time
  * Observation Period
  * Recommendation reference



### Name

The insight name is stored in the `name` field of the Insight entity. It has the following format:
    
    
    projects/TARGET_PROJECT_ID/locations/LOCATION/insightTypes/INSIGHT_TYPE_ID/insights/INSIGHT_ID
    

where:

  * TARGET_PROJECT_ID is the ID of the project where the insight was generated.
  * LOCATION is the Google Cloud [location](https://cloud.google.com/about/locations) where resources associated with the insight are located (for example, `global` or `us-central1-a`)
  * INSIGHT_TYPE_ID is the fully-qualified insight type ID (for example, `google.compute.firewall.Insight`)
  * INSIGHT_ID is a unique ID for the insight



### Description

This is human-readable summary of the insight. It is only available in English.

### Insight Subtype

Each insight type may support multiple subtypes. The content schema is stable for a given subtype.

### Content

Structured fields that include insight details. Content schema is determined by insight type and subtype. For example, `"grantedPermissionsCount": "1000"`

### Category

Similar to [impacts](https://docs.cloud.google.com/recommender/docs/key-concepts#impact) for recommendations, there are categories for insights:

  * `COST`
  * `SECURITY`
  * `PERFORMANCE`



### Target Resources

Fully qualified resource names of the Google Cloud resources the insight is targeting.

### State Info

#### State

Insights go through multiple state transitions after they are proposed:

  * `ACTIVE`, which means that the insight has been generated, but no actions have been taken in response. Content for active insights is updated when the underlying data changes. Active insights can be marked `DISMISSED` OR `ACCEPTED`.
  * `ACCEPTED`, which means that some action has been taken based on the insight. Insights become accepted when an associated recommendation has been marked `CLAIMED`, `SUCCEEDED`, or `FAILED`. Insights can also be accepted directly. Content for accepted insights is immutable. Accepted insights are retained for 90 days from the time of the state change.
  * `DISMISSED`, which means that the insight has been dismissed without taking any action based on it. Content for dismissed insights is updated when the underlying data changes.



#### State Metadata

When directly marking an insight ACCEPTED, you can include additional metadata about the operation with state metadata. The metadata is specified as `key:value` pairs. Updates to the state metadata field overwrite any existing state metadata.

### Etag

An _etag_ is a unique fingerprint that identifies the current state of an insight. Each time the insight changes, a new etag value is assigned.  
In order to change insight state, you must provide the etag of the existing insight. This makes sure that any operations are performed only if the insight has not changed since you last retrieved it.

### Severity

A [_severity_](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/billingAccounts.locations.insightTypes.insights#severity) for an insight indicates the likelihood of one of the following [impacts](https://docs.cloud.google.com/recommender/docs/key-concepts#impact):

  * An outage (for a performance impact)
  * A compromise (for a security impact)
  * An overspend (for a cost impact)
  * A mismanagement (for a manageability impact)



This field comes with values `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW` with `LOW` set as the default severity. Each [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types) can have its own severity strategy defined.

### Last Refresh Time

The last refresh time indicates the freshness of the data used to generate the insight.

### Observation Period

Observation period is the time period leading up to the insight. The source data used to generate the insight ends at`last_refresh_time` and begins at `last_refresh_time` minus `observation_period`.

### Recommendation reference

Reference to an associated [recommendation](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations). References link insights with their associated recommendations. This field is empty when there are no recommendations derived from the insight.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
