---
url: https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards2/
title: Dashboards overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:36.132499+00:00
---

# Dashboards overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dashboards overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document provides a technical guide for using the Google Security Operations Dashboards engine to construct data visualizations across disparate telemetry streams.

The Dashboards framework is built on a modular architecture where individual widgets (charts) interface with specific data sources using the YARA-L 2.0 syntax. By using the YARA-L schema properties and aggregation functions, you can build visualizations for real-time monitoring, threat analysis, and operational auditing.

For a deeper dive into the underlying dashboard infrastructure, see the [Dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview).

## Before you begin

Confirm that your Google SecOps instance meets the following configuration requirements:

  * [Configure a Google Cloud project](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) or migrate your Google SecOps instance to an [existing cloud project](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).

  * Configure a [Google Cloud Identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication) or [third-party identify provider (IdP)](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

  * [Configure feature access control using Identity and Access Management](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).




### IAM permissions required

The following permissions are required to access dashboards:

IAM permission | Purpose  
---|---  
`chronicle.nativeDashboards.list` | [ View the list of all dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#view-dashboards).  
`chronicle.nativeDashboards.get` | [ View a dashboard](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#view-a-dashboard), [ apply a dashboard filter](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters#apply-filter), and [ apply the global filter](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters#apply-global-time-filter).  
`chronicle.nativeDashboards.create` | [ Create a new dashboard.](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#new-dashboards)  
`chronicle.nativeDashboards.duplicate` | [ Make a copy of an existing dashboard.](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#copy-dashboards)  
`chronicle.nativeDashboards.update` | [ Add and edit charts](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts), [add a filter](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters#add-filter), [ change dashboard access](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#change-dashboard-access), and [ manage the global time filter](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters#manage-global-time-filter).  
`chronicle.nativeDashboards.delete` | [ Delete a dashboard](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#delete-dashboards).  
  
## Understand dashboards

Dashboards provide insights into security events, detections, and related data. This section outlines the supported data sources and explains how role-based access control (RBAC) affects visibility and data access within the dashboards.

### Predefined dashboards catalog

Google Security Operations provides out-of-the-box curated dashboards designed for visibility across various security use cases. While you cannot edit or delete curated dashboards, you can make a copy and customize it for your organization's specific requirements.

To explore all available predefined dashboards, review their chart descriptions, and view the underlying search queries for individual widgets, see the [Out-of-the-box dashboards catalog](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards#out-of-the-box-dashboards-catalog). For operational overviews of common predefined dashboards, see [Common curated dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards-overview).

**Note:** When using the [`collection`](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Collection) object to configure dashboards, the following fields are not supported:

  * `investigation`
  * `response_platform_info`
  * `case_name`
  * `feedback_summary`
  * `feedback_history`
  * `soar_alert`
  * `soar_alert_metadata`



### Data sources supported

Dashboards include the following data sources, each with its own query time limit and YARA-L prefix:

Data source | Query time interval | YARA-L prefix | Schema | Dashboard examples  
---|---|---|---|---  
Case history | 365 days | `case_history` | [Fields (SOAR)](https://docs.cloud.google.com/chronicle/docs/reference/soar-data-dashboard#case-history) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#dashboard-query-examples-case-history) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-case-history)  
Cases and alerts | 365 days | `case` | [Fields (SOAR)](https://docs.cloud.google.com/chronicle/docs/reference/soar-data-dashboard#cases-and-alerts) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#cases-and-alerts) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-cases)  
Data tables | No standalone time limit (governed by the joined data source) | `%` | User-defined | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-data-tables)  
Detections | 365 days | `detection` | [Fields](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#detections-fields) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#detections) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#dashboard-query-examples-detections)  
Entity Graph | 365 days | `graph` | [Fields](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#entity-graph-fields) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#entity-graph) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-entity-graph)  
Events | 90 days | `no prefix` | [Fields (UDM)](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#udm-event) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-events)  
Ingestion metrics | 365 days | `ingestion` | [Fields](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#ingestion-metrics) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-ingestion-metrics)  
IoCs | 365 days | `ioc` | [Fields](https://docs.cloud.google.com/chronicle/docs/reference/yaral-functions-native-dashboards#ioc_fields) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#iocs) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-iocs)  
Playbooks | 365 days | `playbook` | [Fields (SOAR)](https://docs.cloud.google.com/chronicle/docs/reference/soar-data-dashboard#playbook) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#playbooks) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-playbooks)  
Rule sets | 365 days | `ruleset` | [Fields](https://docs.cloud.google.com/chronicle/docs/reference/yaral-functions-native-dashboards#rule_sets_fields) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#dashboard-query-examples-rulesets) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-rulesets)  
Rules | No time limit | `rules` | [Fields](https://docs.cloud.google.com/chronicle/docs/reference/yaral-functions-native-dashboards#rule_fields) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#rules) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-rules)  
Triage and Investigation Agent | 365 days | `gemini_investigation`, `gemini_investigation_feedback` | [Fields](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#triage-investigation-agent-fields) | [Template](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#triage-investigation-agent) | [Examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#query-examples-triage-investigation-agent)  
**Note:** By default, chart queries return a limit of 1,000 rows. You can customize this limit up to 10,000 using the `limit` section in YARA-L queries. This customization applies only to custom dashboard queries, not to curated queries.**Note:** Dashboards support querying SOAR case data generated on or after May 10, 2025.

### Impact of data RBAC

Data role-based access control (RBAC) is a security model that uses individual user roles to restrict user access to data within an organization. Data RBAC lets administrators define scopes and assign them to users, ensuring access is limited to only the data necessary for their job functions. All queries in dashboards follow data RBAC rules. For more information about access controls and scopes, see [Access controls and scopes in data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#access-control-with-scopes-labels). For more information about data RBAC for dashboards, see [Configure data RBAC for dashboards](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-dashboards)

### Events, entity graph, and IOC matches

The data returned from these sources is restricted to the user's assigned access scopes, ensuring that they only see results from authorized data. If a user has multiple scopes, queries include data from all assigned scopes. Data outside the user's accessible scopes doesn't appear in dashboard search results.

### Rules

Users can only see rules that are associated with their assigned scopes.

### Detection and rulesets with detections

Detections are generated when incoming security data matches the criteria defined in a rule. Users can only see detections that originate from rules associated with their assigned scopes. The rulesets with detections are only visible to [global users](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles).

### SOAR data sources

Dashboards with SOAR data, such as Cases, Case history, Playbooks and Alerts, are only visible to global users.

Cases and case history dashboards don't support SOAR Access mechanisms (like environments and SOC roles). A user with permissions to access dashboards can view cases across all environments and SOC roles.

### Ingestion metrics

Ingestion components are services or pipelines that bring logs into the platform from source log feeds. Each component collects a specific set of log fields within its own ingestion metrics schema.

Administrators can use RBAC for ingestion metrics to restrict visibility of system health data, such as ingestion volume, errors, and throughput, based on a user's business scope.

The Data Ingestion and Health dashboard uses Data Access scopes. When a scoped user loads the dashboard, the system automatically filters metrics to show only data that matches their assigned labels.

You can filter using the following labels:

  * **Namespace** : The primary method for segregation (for example, `Eu-Prod`, `Alpha-Corp`).
  * **Log Type** : Role-based segregation (for example, `GCP_VPC_FLOW`, `CROWDSTRIKE_EDR`).
  * **Ingestion Source** : Granular source tracking (for example, specific forwarder ID).



#### Unexpected log types in ingestion metrics

Some dashboards may display entries for log types such as `UNSPECIFIED_LOG_TYPE` or internal identifiers, including `LT_X` (where X is a number). These `LT_X` identifiers are used within the Google SecOps system to uniquely identify custom log types created by a customer.

These entries can appear even if the full data ingestion or parsing for these specific log types has not been successfully completed. This happens because certain system metrics are recorded regardless of the final ingestion status.

To focus on successfully ingested and parsed data, you can use the filtering capabilities within the dashboard interface to exclude or specifically filter out `UNSPECIFIED_LOG_TYPE` and other unexpected internal log type identifiers from your views. 

#### Discrepancies between raw log volume and dashboard log volume

The total `ingestion.log_volume` shown in a dashboard chart (for example, a query filtering on `ingestion.component = "Ingestion API"` for the last 365 days) can differ from your cumulative raw log volume for the following reasons:

  * **Time scope and lookback limits** : The Google SecOps interface doesn't display an all-time cumulative ingestion counter from when your instance was provisioned. You can't calculate an all-time total beyond the 365-day query limit in Google SecOps dashboards, even on the curated **Ingestion - Throughput (All-Time)** chart. For Bring Your Own Project (BYOP) instances, you can query up to 24 months in Cloud Monitoring.
  * **Data source and pipeline** : Raw log volume reflects the byte size of raw log batches in storage. Dashboards query the `ingestion_metrics` table, which collects telemetry asynchronously at approximately 5-minute intervals. Because the metrics pipeline can experience collection latency or transient metric drops, treat dashboard `ingestion.log_volume` totals as approximate indicators rather than exact byte counts. For a breakdown of where to calculate ingestion volume and how values differ across tools, see [Where to calculate ingestion volume and how values differ](https://docs.cloud.google.com/chronicle/docs/ingestion/understand-ingestion-metrics#where-to-calculate-ingestion-volume).



#### Limitations

  * **Custom label** : Assigning a user scope that contains a custom label—such as a label created using UDM regular expression or data tables—automatically disables RBAC for ingestion metrics for that user. As a result, the user won't see any data in their dashboards. For ingestion monitoring scopes, you must use only standard labels such as Log Type, Namespace, and Ingestion Source.

  * **Ingestion source Limitation** : Filtering by ingestion source applies only to the Log Count metric. Charts displaying bandwidth (bytes) or error rates metrics might show no data if filtered strictly by ingestion source. Google recommends filtering by Namespace for broader health monitoring.




## Advanced features and monitoring

To fine-tune detections and improve visibility, you can use advanced configurations, such as YARA-L 2.0 rules and ingestion metrics. This section explores these feature insights, helping you optimize detection efficiency and monitor data processing.

### YARA-L 2.0 properties

YARA-L 2.0 has the following unique properties when used in dashboards:

  * Additional data sources, such as entity graph, ingestion metrics, rule sets, and detections are available in dashboards. Some of these data sources are not yet available in YARA-L rules and Unified Data Model (UDM) search.

  * See [YARA-L 2.0 functions for Google Security Operations dashboards](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#yara-l-functions-native-dashboards) and aggregate functions that include statistical measures.

  * The query in YARA-L 2.0 must contain a `match` or an `outcome` section, or both.

  * The `events` section of a YARA-L rule is implied and does not need to be declared in queries.

  * The `condition` section of a YARA-L rule is not available for dashboards.

  * Dashboards don't support rules from the Risk Analytics for UEBA category.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
