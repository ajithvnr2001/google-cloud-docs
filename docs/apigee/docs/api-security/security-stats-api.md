---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-stats-api/
title: Security stats API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:08.569787+00:00
---

# Security stats API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-stats-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Security stats API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The security stats API lets you view abuse and bot-related statistics over the past 14 days. There are two type of security stats:

  * Tabular stats, which don't have a time dimension. Tabular stats are often computed using an aggregation function, for example, `sum for message_count` or `bot_traffic`.
  * Time series stats, which do have a time dimension.

**Note:** Bot detection has a processing delay of around 15 to 20 minutes on average.

## Parameters in example API calls

The following sections give examples of API calls that use the security stats API. The API calls contain the following parameters:

  * ORG: Your organization.
  * ENV: Your environment.
  * METRIC_i: A metric for the statistic. See Metrics and aggregation functions.
  * AGGREGATION_i: An aggregation function for the metric. See the table below.
  * DIMENSION_i: A  dimension for grouping the values of the statistic.
  * PAGE_SIZE: Maximum number of subcomponents returned in a single page.
  * `time_range`: The time range for the statistics in the form 
        
        "time_range": {
            "start_time": START_TIME,
            "end_time": END_TIME
        }

where:

    * START_TIME is the start time for the time range.
    * END_TIME is the end time for the time range.

START_TIME and END_TIME are of the form `"YYYY-MM-DDT00:00:00Z"`.

The length of the time range can be at most 14 days, and both the start date and end date must be within the past 365 days.




## Example: Query tabular security stats for an environment

A request that queries tabular stats has the following format:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityStats:queryTabularStats" \
           -H 'Content-type: application/json' -H "Authorization: Bearer $TOKEN" -X POST -d \
           '{ "metrics": [{"metric": "METRIC_1", "aggregation": "AGGREGATION_1",
                          {"metric": "METRIC_2", "aggregation": "AGGREGATION_2"}],
              "dimensions": ["DIMENSION_1",  "DIMENSION_2"],
              "page_size": PAGE_SIZE,
              "time_range": {
                  "start_time": START_TIME,
                  "end_time": END_TIME
              }
            }'

See Parameters in example API calls.

See Limitations on security stats for the maximum numbers of metrics, aggregation functions, and dimensions that can be included in a request.

Here is an example of a request that queries tabular stats:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityStats:queryTabularStats" \
           -H 'Content-type: application/json' -H "Authorization: Bearer $TOKEN" -X POST -d \
           '{ "metrics": [{"metric": "bot", "aggregation": "count_distinct"},
                          {"metric": "bot_traffic", "aggregation": "sum"},
                          {"metric": "bot_first_detected", "aggregation": "min"},
                          {"metric": "bot_last_detected", "aggregation": "max"}],
              "dimensions": ["apiproxy",  "bot_reason", "ax_resolved_client_ip",  "ax_geo_city",  "ax_geo_country",  "client_id",  "proxy_basepath", "proxy_pathsuffix"],
              "page_size": 1,
              "time_range": {
                "start_time": START_TIME,
                "end_time": END_TIME
              }
            }'

See the [ `queryTabularStats`](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTabularStats) reference page for descriptions of the request and response.

## Example: Query time series security stats for an environment

Time series APIs return time series stats for the chosen metrics, grouped by the chosen dimension.

The following call invokes time series stats for bot traffic grouped by API proxy. Since there are four proxies, this yields four sequences of time series points. The order of the points of each row match the corresponding index in the columns field.

Here is a sample request:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityStats:queryTimeSeriesStats" \
           -H 'Content-type: application/json' -H "Authorization: Bearer $TOKEN" -X POST -d \
           '{ "metrics": [{"metric": "METRIC_1", "aggregation": "AGGREGATION_1", "order": "ORDER"}],
              "dimensions": ["DIMENSION_1"], "window_size": "WINDOW_SIZE",
              "page_size": PAGE_SIZE,
              "time_range": {
                "start_time": START_TIME,
                "end_time": END_TIME
              }
            }'

See Parameters in example API calls.

See the [ `queryTabularStats`](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTimeSeriesStats) reference page for descriptions of the request and response.

## Example: Query incident details for abuse detection

The following example queries the details of an incident for Advanced API Security's [Abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection). The call returns details for bot count for the developer_app for a given incident.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityStats:queryTabularStats" \
           -H "Content-Type: application/json" -H "Authorization: Bearer $(gcloud auth print-access-token)" -X POST -d  \
           '{"metrics": [{"metric": "bot_traffic", "aggregation": "sum"}],
             "dimensions": ["incident_id", "developer_app"],
              "filter": "incident_id eq '\''d897d1af-51ac-4b5d-a29e-d1059d922a05'\''",
              "page_size": 100,
              "time_range": {
                "start_time": START_TIME,
                "end_time": END_TIME
              }
            }'

See Parameters in example API calls.

This returns a response like the following:
    
    
    {
      "values": [
        [
          "d897d1af-51ac-4b5d-a29e-d1059d922a05",
          "Developer2_App1",
          18353
        ],
        [
          "d897d1af-51ac-4b5d-a29e-d1059d922a05",
          "Developer1_App1",
          18082
        ]
      ],
      "columns": [
        "incident_id",
        "developer_app",
        "bot_traffic"
      ]
    }

See the [ `queryTabularStats`](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityStats/queryTabularStats) reference page for descriptions of the request and response.

## Metrics and aggregation functions

The following table describes the metrics and aggregation functions available in the security stats API:

`Metric` | Description | `Aggregation function`  
---|---|---  
`bot` | The number of distinct IP addresses for detected bots over one-minute intervals.  | `count_distinct`  
`bot_first_detected` | Date and time the bot was first detected. Only available through the API. | `min`  
`bot_last_detected` | Date and time the bot was last detected. Only available through the API. | `max`  
`bot_traffic` | The number of messages from IP addresses of detected bots over one-minute intervals.  | `sum`  
`message_count` | Total number of API calls processed by Apigee in one-minute intervals. **Note:** `message_count` cannot be used with other metrics in the same report. | `sum`  
`response_size` | Size of the response. | `average`, `max`, `min`, `sum`  
  
## Dimensions

Dimensions let you group metric values together based on related subsets of the data. The following table describes the dimensions that are specific to Advanced API Security reports:

Dimension | Description  
---|---  
`bot_reason` | Can be any combination of the security [detection rules](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules). `bot_reason` consists of the subset of the detection rules that the bot's traffic pattern matched.  
`incident_id` (preview) | The UUID for a security incident, which is returned by a call to the Incidents API. See [ Example: Get details or a specific incident](https://docs.cloud.google.com/apigee/docs/api-security/incidents-api#example:-get-details-for-a-specific-incident).   
`security_action` | The security action. Possibly values are `ALLOW`, `DENY`, or `FLAG`.   
`security_action_name` | The name of the security action.  
`security_action_headers` | Headers that you can use to query for a flag security action.  
  
**Note:** `bot_reason` and `incident_id` only work with the following metrics:

  * `bot`
  * `bot_traffic`
  * `response_size`



In addition to the dimensions described above, Advanced API Security also supports the following [dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions):

  * `access_token`
  * `api_product`
  * `apiproxy`
  * `app_group_app`
  * `app_group_name`
  * `ax_edge_execution_fault_code`
  * `ax_geo_city`
  * `ax_geo_continent`
  * `ax_geo_country`
  * `ax_geo_region`
  * `ax_isp`
  * `ax_resolved_client_ip`
  * `ax_ua_agent_version`
  * `client_id`
  * `developer`
  * `developer_app`
  * `developer_email`
  * `environment`
  * `is_filtered_out`
  * `proxy_basepath`
  * `proxy_pathsuffix`
  * `request_uri`
  * `response_status_code`
  * `target_url`
  * `useragent`



## Limitations on security stats

The security stats API (both tabular and time series) has the following limits:

  * Maximum page size: 14400
  * Maximum of 10 time series dimensions
  * Maximum of 15 tabular stats dimensions
  * Maximum of 5 metric aggregations.
  * Maximum of 5 time series metric aggregations
  * Time range: Length can be at most 14 days, and both the start date and end date must be within the past 365 days.
  * The dimensions `incident_id` and `bot_reason` cannot be used with the metrics `message_count` or `response_size`.
  * The dimensions `is_filtered_out` is only supported by tabular stats, and apply to old data as well.



## Comparing the security stats API and the security reports API

Both the security stats API and the security reports API return abuse and bot-related security statistics, but they have the following differences:

  * The security stats API is designed to view statistics for recent API traffic. Data for the security stats API goes back only 14 days, but you can view the stats immediately when you send a request.

Security stats are also displayed in the [Abuse metrics view](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#abuse-metrics-view) in the Apigee UI.

  * The [security reports API](https://docs.cloud.google.com/apigee/docs/api-security/security-reports-api) is designed to view statistics for long-running operations. To use the security scores API, you submit a job and view the results only when the job is completed. Data for the security scores API goes back one year.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
