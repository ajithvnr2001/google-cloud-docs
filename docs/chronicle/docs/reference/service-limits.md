---
url: https://docs.cloud.google.com/chronicle/docs/reference/service-limits/
title: Service limits \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:29.534252+00:00
---

# Service limits  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/service-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service limits

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc) [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Caution:** The Backstory API and Ingestion API described in this document are [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To access Google SecOps security data and services programmatically, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This page provides details on the limits that apply to Google Security Operations. You can request API limit increases by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).

## Backstory API quotas

The Backstory API quotas are enforced at the server level using an interceptor. Each service which integrates with the Backstory API must specify the appropriate quota server key to enable quota enforcement.

The following table lists the enforced quotas. The abbreviations are:

  * QPS - Queries Per Second
  * QPM - Queries Per Minute
  * QPH - Queries Per Hour
  * QPD - Queries Per Day

Group | API | Query Quota  
---|---|---  
Search | ListCuratedRuleDetections | 10 QPM  
Search | ListEvents | 1 QPS  
Search | ListIocs | 1 QPS  
Search | ListIocDetails | 1 QPS  
Search | ListAssets | 5 QPS  
Search | SearchRawLogs | 1 QPM  
Partner | CreateCustomer | 10 QPD  
Tools | RetrieveSampleLogs | 10 QPM  
Tools | ValidateCBNParser | 1 QPS  
Tools | ListCbnParsers | 1 QPS  
Tools | SubmitCbnParser | 1 QPM  
Tools | GetCbnParser | 1 QPS  
Tools | ListCbnParserHistory | 1 QPS  
Tools | ListCbnErrors | 1 QPS  
Rules | GetRule | 1 QPS  
Rules | GetDetection | 1 QPS  
Rules | GetRetrohunt | 1 QPS  
Rules | ListRules | 1 QPS  
Rules | ListRuleVersions | 1 QPS  
Rules | ListDetections | 10 QPM  
Rules | ListRetrohunts | 1 QPS  
Rules | CreateRule | 1 QPS  
Rules | CreateRuleVersion | 1 QPS  
Rules | DeleteRule | 1 QPS  
Rules | EnableLiveRule | 1 QPS  
Rules | DisableLiveRule | 1 QPS  
Rules | EnableAlerting | 1 QPS  
Rules | DisableAlerting | 1 QPS  
Rules | RunRetrohunt | 1 QPS  
Rules | CancelRetrohunt | 1 QPS  
Rules | WaitRetrohunt | 1 QPS  
Rules | StreamTestRule | 3 QPM  
Rules | ArchiveRule | 1 QPS  
Rules | UnarchiveRule | 1 QPS  
Health | GetError | 1 QPS  
Health | ListErrors | 1 QPS  
ReferenceList | CreateReferenceList | 1 QPS  
ReferenceList | GetReferenceList | 1 QPS  
ReferenceList | ListReferenceLists | 1 QPS  
  
See additional API documentation:

  * [Detection Engine API](https://docs.cloud.google.com/chronicle/docs/reference/detection-engine-api)
  * [BigQuery Access API](https://docs.cloud.google.com/chronicle/docs/reference/bigquery-access-api)
  * [Search API](https://docs.cloud.google.com/chronicle/docs/reference/search-api)
  * [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api)
  * [Forwarder Management API](https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-api)



## Chronicle API and Google Cloud project quotas

You can view quotas for the Chronicle API and your Google Cloud project using the Google Cloud console. See [View quotas in the Google Cloud console](https://docs.cloud.google.com/docs/quotas/view-manage#viewing_your_quota_console) for more information.

## Dashboard data sources supported

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

## Dashboard search limit

For search, the quota is per user per hour, but for dashboards it is per Google SecOps instance. For more information about dashboards, see [Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards).

## Data ingestion burst limits

Data ingestion burst limits restrict the amount of data a customer can send to Google SecOps. They help to ensure that customer data ingestion operates smoothly.

For detailed information, see [Understand quotas and burst limits](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits).

## Data table limits

  * Maximum number of data tables for a Google SecOps account: 1,000.

  * Data tables support only CSV data. Data tables support tab-separated values only when [adding a new data table](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables#new-data-table) and importing a tab-separated values (TSV) file.

  * Data table fields don't support comma (`,`) characters.

  * The [limits](https://docs.cloud.google.com/chronicle/docs/yara-l/reference-list-syntax) on the number of `in` statements when referencing a reference list in a query also apply to `in` statements in a data table.

  * Maximum number of `in` statements in a query for `String` and `Number` data type columns: 10.

  * Maximum number of `in` statements with regular expression operators: 5.

  * Maximum number of `in` statements with CIDR operators: 5.

  * Maximum number of `= (JOIN)` statements: 10.

  * Maximum columns per data table: 1,000.

  * Maximum rows per data table: 10 million.

  * Maximum display limit in web page for data table rows in text and table editor view: 10,000 rows.

  * Maximum data volume in a data table: 10 GB.

  * Placeholders aren't allowed in the setup section.

  * Unmapped columns of a data table with data type set to `string` can only be joined with string fields of UDM event or UDM entity.

  * Use only unmapped columns in a data table with a data type set to `cidr` or `regex` for CIDR or regular expression.

  * Data table lookups: Regular expression wildcards aren't supported and search terms are limited to 100 characters.




### Joins

  * Fetching all event samples for detections isn't supported when using data table joins with events.

  * Unlike entities and UDM, data tables don't support placeholders. This means you can't:

    * Apply one set of filters to a data table and join it with a UDM entity.

    * Apply a different set of filters to the same data table while joining it with another UDM placeholder.

For example, a data table named `dt` with 3 columns: `my_hostname`, `org`, and `my_email` and with the following rule:
    
    events:
    $e1.principal.hostname =  %dt.my_hostname
    %dt.org ="hr"
    
    $e2.principal.email =  %dt.my_email
    %dt.org !="hr"
    




All filters on a data table are applied first, and then the filtered rows from the data table are joined with UDM. In this case, the contradictory filters (`%dt.org ="hr" and %dt.org !="hr"`) on the `dt` table result in an empty data table, which is then joined with both `e1` and `e2`.

### Use data tables with rules

The following limitations apply to data tables when used with rules.

#### Output to data tables

  * `any` and `all` modifiers aren't supported for repeated field columns in data tables.

  * Array indexing isn't supported for repeated fields columns in data tables.

  * You can only export outcome variables to a data table. You can't export event path or data table columns directly.

  * Column lists must include the primary key columns for data tables.

  * You can have a maximum of 20 outcomes.

  * If a data table doesn't exist, a new table is created with the default `string` data type for all columns, following the order specified.

  * Only one rule can write to a data table at a time. If a rule tries to write to a data table that another rule is already writing to, the rule compilation fails.

  * There's no guarantee that a producer rule can add rows to a data table before a consumer rule for that data table starts.

  * A single rule has a limit on the number of outcomes rows. A maximum 10,000-row limit applies over the result and persisted data and to data tables.

  * If a row with the same primary key already exists in the data table, it's non-primary key columns are replaced with the new values.




#### Entity enrichment from data tables

  * You can apply only one enrichment operation (either `override`, `append`, or `exclude`) to a single entity graph variable.

  * Each enrichment operation can use only one data table.

  * You can define a maximum of two enrichment operations of any type in the `setup` section of a YARA-L rule. 




In the following example, an `override` operation is applied to the entity graph variable `$g1` and an `append` operation is applied to the entity graph variable `$g2`.
    
    
        setup:
        graph_override($g1.graph.entity.user.userid = %table1.myids)
        graph_append [$g2, %table1]
    

In the preceding example, the same data table (`table1`) is used to enhance different entity graphs. You can also use different data tables to enhance the different entity graphs, as follows:
    
    
        setup:
        graph_override($g1.graph.entity.user.userid = %table1.myids)
        graph_append [$g2, %table2]
    

### Use data tables with Search

The following apply to data tables when used with Search.

  * Data tables support customer-managed encryption keys (CMEK) users.

  * A single query execution can output a maximum of 1 million rows to a data table or 1 GB, whichever limit comes first.

  * Search output to a data table skips event rows if they exceed 5 MB.

  * Entity enrichment is not supported with Search.

  * Writes are limited to 6 per minute per customer.

  * Statistics queries aren't supported with data table joins.

  * Data table and data table joins are only supported with UDM events, and not with entities.

Supported: `%datatable1.column1 = %datatable2.column1` Not supported: `graph.entity.hostname = %sample.test`

  * You can't include a `match` variable in statistics query in the `export` section of a statistics query.

For example, the following is not supported:
        
        match:
              principal.hostname
          export:
              %sample.write_row(
              row: principal.hostname
            )
        




## Ingestion rate

When the data ingestion rate for a tenant reaches a certain threshold, Google Security Operations dynamically adjusts the ingestion rate to ensure availability for new data feeds. The ingestion volume and tenant's usage history determines the threshold. For information on volume of data which can be ingested into Google SecOps by a single customer, see [Burst limits](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits).

**Note:** HTTPS push feeds, including webhook, Cloud Storage, Pub/Sub, and Amazon Kinesis Firehose, are subject to the following limits:

  * Rate limit of 15,000 queries per second (QPS).

  * The maximum size for a single log line which is 1 MB. This limit also applies to earlier versions of the Google SecOps ingestion API. In contrast, the current [Chronicle API ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) support an individual log size of up to 4 MB.




## Reference list limits

A reference list is a generic list of values which can be used to analyze your data. For more information, see [Reference lists](https://docs.cloud.google.com/chronicle/docs/reference/reference-lists).

### String lists

String lists have the following limits:

  * Maximum list size: 6MB
  * Maximum length of any single list content line: 5000 characters



### Regular expression lists

Regular expression lists have the following size limits:

  * Maximum list size: 0.1MB
  * Maximum number of lines: 100
  * Maximum length of each content line: 5000 characters



### CIDR lists

CIDR lists have the following size limits:

  * Maximum list size: 0.1MB
  * Maximum number of lines: 150
  * Maximum length of each content line: 5000 characters



## Rule limits

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



### Rule quotas

Google SecOps enforces capacity limits on detection rules to ensure consistent system performance and query speed.

The custom rule quotas for each Google SecOps package are:

  * **Standard** : 1,000 total rules (including up to 75 multi-event rules)
  * **Enterprise** : 2,000 total rules (including up to 200 multi-event rules)
  * **Enterprise Plus** : 3,500 total rules (including up to 400 multi-event rules)



For details about rule quotas, see [Understand rule quotas](https://docs.cloud.google.com/chronicle/docs/detection/rule-quotas).

## Result limits for data sources

The following table lists the maximum number of results returned for each data source:

Search type or Data source | Maximum number of events or rows in search results  
---|---  
UDM | 1,000,000  
ECG | 1,000,000  
Data table | 1,000,000  
UDM to UDM join | 1,000,000  
UDM to ECG join | 1,000,000  
UDM to Data table join | 1,000,000  
Cases and case history | 1,000,000  
Stats | 100,000  
Detections | 100,000  
**Note:** The limits are the same whether you're using the platform or the API. See [Asynchronous Search APIs](https://docs.cloud.google.com/chronicle/docs/investigation/search-lro-api) for information about the API limits.

## Alert, case, and entity limits

Type | Default amount | Maximum amount  
---|---|---  
Alerts per day | According to license | According to license  
Alerts per case | 20 alerts | 90 alerts  
Alert size | 28 million characters (26.7 MB) per alert. | 28 million characters (26.7 MB) per alert. Alerts that exceed this limit may be trimmed. For more information, see [ Handle large alerts.](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/handle-large-alerts)  
Event field size | N/A | 25 thousand characters  
Events in alert | 500 events | 500 events (Events that exceed this amount are removed from the alert.)  
Entities in alert or case | 500 entities in the same case or alert. | 500 entities in the same case or alert  
Relations in alert or case | 500 relations in the same case or alert  | 500 relations in the same case or alert. The same case or alert can contain both 500 entities and 500 relations.  
Timeframe for grouping alerts | 2 hours  | 24 hours (maximum).  
Timeframe for overflow case grouping | 2 hours  | 24 hours (maximum). For more information, see [ Define alert overflow](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/define-alert-overflow-admin).   
Alert grouping into overflow case | 50  | 100  
  
## Playbook limits

Type | Default amount | Maximum amount  
---|---|---  
Playbook import size | N/A | 10 MB  
Playbooks per day | Based on the amount of alerts according to your license. Each alert includes one playbook automatically attached. | Based on the amount of alerts according to your license  
Playbooks per alert | 10 in total - 1 automatically and 9 can be manually added | 10 in total  
Parallel actions | 5 actions per step | 5 actions per step. For more information, see [ Using parallel actions.](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-parallel-actions)  
Playbook sync actions run time | 10 minutes | 20 minutes  
Playbook async actions runtime | 

  * 10 minutes for script timeout
  * 1 hour for async polling interval
  * 1 day for async action timeout

| 

  * 20 minutes for script timeout
  * 24 hours for async polling interval
  * 1 day for async action timeout

  
Playbook JSON result | 28 million characters (26.7 MB) | 28 million characters (26.7 MB)  
  
## Case and user management limits

Type | Default amount | Maximum amount  
---|---|---  
Case - entity properties | 100 properties per entity | 100 properties per entity  
File size uploaded on case wall | 50 MB | 50 MB  
Roles in platform | 20 roles | 20 roles  
Case stages | 20 stages | 20 stages  
  
## Automation feature system limits

Type | Default amount | Maximum amount  
---|---|---  
Data retention | 12 months | 60 months  
API rate | 4000 requests per minute | N/A  
Size of libraries added to IDE integration | N/A | 500 MB  
Manual Python execution: Run connector once, Run manual action, and IDE - Play item | 5-minute timeout | 5-minute timeout  
  
## Gemini Case summary limits

The Gemini Case summary feature supports case summary generation at a rate of 2 cases per minute, with a maximum of 100 cases per hour and is subject to Vertex capacity constraints. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
