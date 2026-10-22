---
url: https://docs.cloud.google.com/chronicle/docs/reports/dashboard-data-sources-prefixes/
title: Dashboard data sources and field prefixes \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:14.004502+00:00
---

# Dashboard data sources and field prefixes  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/dashboard-data-sources-prefixes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dashboard data sources and field prefixes

Supported in:

Google SecOps 

This guide is for security analysts and dashboard authors who want to query different data sources when creating custom charts and filters in Google Security Operations dashboards. It explains how to identify the required YARA-L field prefix for each supported data source, respect query time intervals, and write valid chart queries. By following this guidance, you prevent query compilation errors and empty chart results. Accurate dashboard configurations provide reliable visibility into security telemetry, detection efficacy, and SOAR operations.

## Key terminology

  * **YARA-L field prefix** : A qualifier prepended to a field name (such as `case.`, `detection.`, or `ingestion.`) that specifies which underlying Google Security Operations data source the query targets.
  * **Unified Data Model (UDM)** : The standard Google Security Operations schema that structures and normalizes raw security event telemetry. Queries against UDM event data don't use a field prefix.
  * **Data table (`%`)**: A user-defined tabular dataset in Google Security Operations that you reference in YARA-L queries by prepending a percent sign (`%`) to the table name.



## Common use cases

The following use cases illustrate how dashboard authors apply YARA-L field prefixes across Google Security Operations data sources.

### Build operational SOAR and detection charts

  * **Objective** : Create custom dashboard charts that track open SOAR cases, playbook execution metrics, or rule detections over time by using the `case`, `playbook`, and `detection` prefixes.
  * **Value** : Centralizes incident response and detection performance metrics alongside SIEM event telemetry in a unified operational dashboard.



### Configure dashboard filters across data sources

  * **Objective** : Define dashboard-level filters that target specific data sources by specifying their required field prefixes.
  * **Value** : Lets analysts dynamically filter multiple charts across a dashboard without editing individual YARA-L chart queries.



## Before you begin

Before creating or modifying dashboard charts and filters, confirm the following requirements:

  * **Permissions** : To add or edit charts and filters in a dashboard, you must have the `chronicle.nativeDashboards.update` IAM permission. For more information about dashboard permissions and access control, see [Manage charts in dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts) and [Control access to dashboards](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-dashboards).
  * **Data RBAC considerations** : Your access to underlying chart data depends on the Data Role-Based Access Control (Data RBAC) policies configured for your user role. For details, see [Impact of data RBAC](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards#impact-of-data-rbac).



## Select and apply YARA-L field prefixes in dashboard queries

When you build a chart query or configure a dashboard filter, you must select the prefix that corresponds to your target data source and apply it to every field in the query.

### Identify the required prefix for your data source

Before writing your query, identify the required YARA-L prefix and supported query time interval for your data source. If you don't use the required prefix, your query returns an error or fails to return the expected data.

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

### Apply prefix syntax rules to your query

Apply the appropriate prefix format when writing a YARA-L query in the chart query editor or configuring a dashboard filter:

  1. For **Events** (in YARA-L chart queries and basic dashboard filters), enter the Unified Data Model (UDM) field name directly without a prefix (for example, `metadata.event_type = "USER_LOGIN"`).
  2. For **Prefixed data sources** (such as Cases and alerts, Detections, or Ingestion metrics, in YARA-L chart queries and basic dashboard filters), prepend the data source prefix followed by a dot to each field name (for example, `case.priority = "PRIORITY_HIGH"` for Cases and alerts, or `detection.detection.rule_name` for Detections).
  3. For **Data tables** (in YARA-L chart queries and dynamic queries in advanced filters), prepend a percent sign (`%`) followed by the data table name and a dot before the column name (for example, `%allowlist.ip`). Basic dashboard filters (`Field to filter`) aren't supported for data tables.

**Caution:** If you omit the required prefix for a non-event data source or mix incompatible prefixes without a supported join, the query editor rejects the syntax or returns empty results. Verify that every data source field referenced in your query uses the prefix listed for that data source.

## Examples and reference information

Use the following query examples and schema references to construct YARA-L queries for your dashboard charts.

### Events query without a prefix

The following query searches UDM event data without a prefix:
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "BLOCK"
    
    match:
      principal.user.userid
    
    outcome:
      $failed_logins = count(metadata.id)
    

### Cases and alerts query with a prefix

The following query searches Cases and alerts by using the `case` prefix:
    
    
    case.incident = true
    case.priority = "PRIORITY_HIGH"
    
    match:
      case.status
    
    outcome:
      $open_cases = count(case.name)
    

### Data tables query with a percent sign (%) prefix

The following query filters UDM login events by joining them with a custom data table (`%example_table`) using the `%` prefix:
    
    
    metadata.event_type = "USER_LOGIN"
    security_result.action = "ALLOW"
    principal.user.userid = %example_table.uid
    
    match:
      principal.user.userid
    
    outcome:
      $login_count = count(metadata.id)
    

### Additional query templates and schemas

For complete query templates, field dictionaries, and additional examples for every supported data source, see the [YARA-L 2.0 dashboard query library](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard).

## Troubleshooting

This section outlines platform limits and provides self-service fixes for common dashboard query issues.

### Latency and limits

When building dashboard charts, keep the following service limits and data retention boundaries in mind:

  * **Row limits** : By default, chart queries return a maximum of 1,000 rows. For custom dashboard queries, you can increase this limit up to 10,000 rows by adding the `limit` section to your YARA-L query. Curated dashboard queries don't support custom row limits.
  * **Query time intervals** : Each data source enforces a maximum query time interval: 90 days for **Events** , 365 days for all other prefixed data sources (except **Rules**), and no time limit for **Rules** (which filters by the rule creation timestamp `rules.create_time`). **Data tables** don't have a standalone time limit; when queried with another data source, that data source's time interval applies.
  * **SOAR historical data** : Dashboards support querying SOAR case data generated on or after May 10, 2025.



### Error remediation

Use the following table to resolve common issues when querying dashboard data sources:

**Issue** | **Description** | **Fix**  
---|---|---  
Unrecognized field or compilation error | The query references a field from a non-event data source (such as `priority` or `rule_name`) without its required prefix. | Prepend the required data source prefix and a dot to the field name (for example, `case.priority` or `detection.detection.rule_name`).  
Empty chart results for active rules | A chart querying the `rules` schema returns no results when the time range is set to a recent window (such as the last 365 days). | Because the `rules` schema maps the chart time window to `rules.create_time`, set the chart time range to the maximum available limit (such as 10+ years) to include active rules created earlier.  
Missing SOAR case data for older dates | Queries that use the `case`, `case_history`, or `playbook` prefixes return no records prior to May 2025. | Restrict your dashboard query time range to dates on or after May 10, 2025.  
  
### Validation and testing

To verify that your query uses the right prefix and returns data before saving a chart, open the [**Edit Dashboard**](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#edit-dashboards) page to [add or edit a chart](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts#add-a-chart), enter your YARA-L query in the chart query editor, select a time range within the data source's supported interval, and click **Run Search**. Confirm that the tabular preview populates with the expected columns before you click **Add to Dashboard**.

## What's next

  * [Manage charts in dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts)
  * [Configure dashboard filters](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters)
  * [YARA-L 2.0 dashboard query library](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
