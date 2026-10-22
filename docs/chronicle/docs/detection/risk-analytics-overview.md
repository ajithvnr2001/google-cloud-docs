---
url: https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-overview/
title: Risk Analytics overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:41.751614+00:00
---

# Risk Analytics overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Risk Analytics overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Risk Analytics is used to identify unusual behavior and understand the potential risk that entities pose to your enterprise. On systems that use data RBAC, only users with global scope can access risk analytics. The Risk Analytics dashboard consists of a Behavioral Analytics section, which lists entities according to Google Security Operations Entities risk scores and a Watchlist section, which lists entities according to internal enterprise risk calculations.

Risk scores are used throughout Google SecOps. The definition and function of these scores vary depending on which feature you are using.

Risk Analytics is available with Enterprise and Enterprise Plus licenses, or as an add-on to a Google SecOps SIEM standalone license.

## Entities, risk, and findings in Risk Analytics

This section defines the concepts of entities, risk, and findings as they are presented on the [Risk Analytics dashboard](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard).

  * **Entities** : Contextual representation of an asset or user in your environment. All the events associated with entities provide context about how risky the entity is. For more information, see [Logical objects: Event and Entity](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview#logical_objects_event_and_entity).

  * **Risk calculation window** : Lets you change the timeframe for the dashboard, enabling you to look at data through different periods of time. For example, you can uncover brute force login attempts by using the shorter time window or examine long-term malicious activity by setting the longer time window.

  * **Normalized** : Normalized scores are set between 1-1000 to distinguish the entities without scores from the entities that do have detections within the risk window.

  * **Normalized trend** : Change in the normalized entity risk score since the previous window.

  * **Base** : Base scores are calculated by adding the risk scores across findings (alerts and detections) for an entity during the risk window with weighting applied. 

Weighting defines how alert and detection risk scores contribute to entity risk score calculations. Weighting can take a value from 0-1.  
If the weighting value is 1, weighting won't have an impact. All other values are percentages (for example, .5 equals 50%). The default weighting value is .2 and can be changed in Settings. For more information, see [Entity risk score weighting](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#score-weighting).

  * **Base change** : Change in the base entity risk score since the previous window.

  * **First/last seen in window** : Timestamp corresponding to when the entity was first or last seen in a finding (alert or detection) for the time period specified in the risk window.




## Findings in Risk Analytics

The following terms are used on the Findings page (click an entity in the entities table to open it in the Findings page).

  * **Findings** : Number of findings (alerts and detections) that include this entity for the time period in the risk window.

  * **Severity** : Severity is set by the source when a finding is created.

  * **Priority** : Priority is set by the source when a finding is created.

  * **Risk Score** : Risk scores are set by the source when a finding is created. If the risk scores are not set, the default risk score for alerts and detections is used. The default risk score for alerts is 40. The default risk score for detections is 15.


**Note:** When the risk score for alerts is 0, the Findings page displays a risk score of 0, and the normalized risk score for the related entity is 1. When the risk score for detections is 0, the entity is not displayed in the [Entities table](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#entity_count_risk_score_and_entities_table)

## Risk score calculation

The risk score calculation for each entity is based on the risk score of findings and is modified based on a set of parameters you can specify and a set of parameters controlled by Google SecOps. The parameters you can control are accessible by going to the navigation bar and clicking **Settings > Entity risk scores**:

  * **Closed alert coefficient** : If the security analysts marks an alert as closed, it is multiplied with this floating point modifier. The range is 0-1. The default value is 1.

  * **Default detection risk score** : Specify the risk score for detections in the rules engine. The range is 0-1000. The default value is 15.




The following parameters are specified by Google SecOps:

  * **Risk score modification with TTL** : Base entity risk score is modified by a multiplying factor for the time range.

  * **Risk score modification without TTL** : Detection risk score is modified with a multiplying factor.




The following are the formulas used for calculating the risk score and normalized risk score:

  * **Risk score calculation** : (Base entity risk score) = (Maximum risk score for the finding) + (Weighting * (Sum of the remaining risk scores for the findings))

  * **Normalized risk score** : Base entity risk scores are normalized across all entities. The base entity risk score uses min-max normalization and ranges from 1-1000. Entities with zero risk are not included.




### Entity precedence for assigning risk score

When assigning the risk score, Google SecOps uses a subset of top-level noun types `principal`, `src`, `target`, and `about`—and assigns a risk score according to the _alias_ fields of the [`user`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#user) and [`asset`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#asset) event subtypes. Risk scoring doesn't support `RESOURCE` or `GROUP` entity types.

Google SecOps assigns the risk score to the most reliable alias (indicator) available for an entity within a given risk calculation window. Higher-ranking alias fields take precedence when assigning the risk score, with `1` being the highest ranking. If the highest-ranking alias isn't available in the risk window, Google SecOps assigns the score to the next highest-ranking available alias.

For [`user`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#user) alias fields, Google SecOps uses the following ranking when assigning the risk score:

  1. `windows_sid`
  2. `email_addresses`
  3. `userid`
  4. `employee_id`
  5. `product_object_id`



For [`asset`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#asset) alias fields, Google SecOps uses the following ranking when assigning the risk score:

  1. `hostname`
  2. `mac`
  3. `asset_id`
  4. `ip`
  5. `product_object_id`



### Example risk score calculation

The following describes the full sequence for how a risk detection score is calculated for an entity:

  1. **Input** : Detections generated by rules are grouped based on their underlying indicators.
  2. **(Optional) Closed alert coefficient** : If the detection risk score is for a closed alert, the score is multiplied by the closed alert coefficient.
  3. **(Optional) Default Risk Score modification** If it isn't explicitly set in a rule, the default detection risk score is applied. Default alerting or non-alerting detection risk scores can be changed in the entity risk scores settings.
  4. **(Optional) Composite detections modification** : By default, Google SecOps assigns the risk score to all entities in the sampled events. It also assigns the score to all entities captured in the `match` and `outcome` sections of the rule. To assign the risk score to specific entities instead, specify the [`$risk_entity_to_score` outcome variable](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax#risk_entity_to_score) in the rule.
  5. **Risk score calculation** : The weighting factor is multiplied to the sum of all detections (except for the maximum detection risk score) and then added to the maximum detection risk score. This value represents the raw entity risk score.
  6. **Modification weight** : The raw entity risk score is multiplied with the modification weight. This modification is a one-time operation, unless a TTL is set. This value is the base entity risk score.
  7. **Watchlist weight** : If an entity is part of a watchlist, the watchlist weight is added to the detection risk score.
  8. **Normalized risk score** : The base entity risk score is normalized across all entities using min-max normalization.



## Risk score settings

The **Entity risk scores** page lets you define how risk scores are calculated for entities, alerts, and detections. You can apply weighting to entity risk score calculations and set default alert and detection risk scores. Changes only apply to new alerts and detections and can take up to 30 minutes to take effect.

  * **Entity risk score weighting** : Weighting defines how alert and detection risk scores are factored in entity risk score calculations. Weighting is a value from 0 to 1. The formula for the base entity risk score is defined as follows:

Base entity risk score = (Maximum risk score for the finding) + (Weighting * (Sum of the remaining risk scores for the findings))

  * **Default risk scores for Alerts** : Specify the default alert risk score in the **Settings** page. The default is 40. You can modify individual alert risk scores in the rules themselves. These override any defaults configured in the **Settings** page.

  * **Default risk scores for Detections** : Specify the default detection risk score in the **Settings** page. The default is 15. You can modify individual detection risk scores in the rules themselves. These override any defaults configured in the **Settings** page.




## Near real-time risk analytics for Enterprise customers

This rapid recalculation lets you use risk-based alerting (RBA) to meet enterprise alerting service-level objectives (SLOs) by by minimizing the delay in identifying and responding to likely compromised assets.

## MRI resolution for risk scoring in UEBA

For User and Entity Behavior Analytics (UEBA), the Most Reliable Indicator (MRI) resolution logic identifies the most authoritative identifier for a supported entity (user or asset) when multiple indicators are present. This process is necessary for indexing and risk scoring. Risk scoring doesn't support `RESOURCE` or `GROUP` entity types. This ensures that risk is attributed to the most stable identity available for a user across different data sources. MRI resolution uses the following processes to identify the more reliable indicator:

  * **Type-based priority** : Each indicator category has an internal priority map where higher values indicate greater reliability. For example, WINDOWS_SID (priority 4) is inherently more reliable than Employee ID (priority 1).
  * **Tie breaking** : If two indicators have the same priority, the system compares their display names and namespaces to decide which indicator is more reliable.



### Reliability hierarchy within entity types

The following hierarchy lists the available indicators from most reliable (priority 4) to least reliable (priority 0) within each entity type.

  1. **User Indicators**
     1. Windows SID: priority 4
     2. Email: priority 3
     3. Username: priority 2
     4. Employee ID: priority 1
     5. Product object ID: priority 0
  2. **Asset Indicators**
     1. Hostname: Top-level hostnames prioritized if configured) (priority 4)
     2. MAC address: priority 3
     3. Product-specific ID or Asset ID: priority 2
     4. Asset IP address: priority 1
     5. Product object ID: priority 0



### MRI scope resolution

The scope of MRI resolution is restricted to the following entity types:

  * ASSET_IP_ADDRESS
  * MAC, HOSTNAME
  * PRODUCT_SPECIFIC_ID
  * EMAIL
  * USERNAME
  * WINDOWS_SID
  * EMPLOYEE_ID
  * PRODUCT_OBJECT_ID.



We don't use MRI resolution with process and file indicators.

### risk_entity_to_score outcome variable

By default, Google SecOps assigns the risk score to all entities in the sampled events. It also assigns the score to all entities captured in the `match` and `outcome` sections of a rule. To assign the risk score to specific entities instead, specify the `risk_entity_to_score` outcome variable in the rule.

The `risk_entity_to_score` outcome variable specifies the entity to score, not the field to display the score under. To prevent risk fragmentation, Google SecOps consolidates risk under the MRI available for the selected entity within a given risk calculation window. If you specify a non-MRI identifier in `risk_entity_to_score`, Google SecOps doesn't assign the score to that identifier directly. Instead, it updates the MRI available for that entity in the risk window.

For more information, see [risk_entity_to_score outcome variable](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax#risk_entity_to_score).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
