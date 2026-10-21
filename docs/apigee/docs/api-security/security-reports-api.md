---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-reports-api/
title: Manage security reports using the API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:13:30.024170+00:00
---

# Manage security reports using the API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-reports-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage security reports using the API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to create and view [security reports](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs) using the security reports API.

For an overview of security reports, including limitations, see [ Security reports overview](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs). For the API reference documentation for security reports, see the [ Security reports API reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityReports).

**Note:** Data flowing into the Apigee Analytics pipeline has a delay of up to 15 to 20 minutes on average. As a result, a security report in which the end time is less than 20 minutes in the past might return incorrect results.

## Parameters in example API calls

The following sections give examples of API calls that use the security reports API. The API calls contain the following parameters:

  * ORG is your organization.
  * ENV is the environment in which you want the report to be calculated.
  * ENVGROUP is an environment group containing the environment.
  * REPORT_ID is the report ID returned by a call to create a security report.
  * `$TOKEN` is the environment variable for an [OAuth access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). 
  * `timeRange` is the time range for the report.



## Create a security report

To create a security report, enter a command like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityReports" \
           -X POST -d @./Query.json \
           -H 'Content-type: application/json' -i \
           -H "Authorization: Bearer $TOKEN"

where Query.json is a _query template_ that defines the query. An example of a query template is shown below.
    
    
    {
      "dimensions": [
        "ax_resolved_client_ip",
      ],
      "metrics": [
        {
          "aggregation_function": "count_distinct",
          "name": "bot"
        },
        {
          "aggregation_function": "sum",
          "name": "bot_traffic"
        },
      ],
      "groupByTimeUnit": "minute",
      "timeRange": "last7days"
    }

The query has the following parameters:

  * Metrics: 
    * `bot`. This counts the number of distinct IP addresses that have been identified as sources of bots.

Aggregation function: `count_distinct`

    * `bot_traffic`. The total number of requests from IP addresses that are the sources of bots.

Aggregation function: `sum`

See [Metrics and aggregation functions](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#metrics-and-aggregation-functions).

  * Dimension: `ax_resolved_client_ip`. This groups the counts of bots in the report by the IP address of their source. See [Dimensions](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#dimensions) for information of supported dimensions.
  * Filter: `environment`. 
  * groupByTimeUnit: `minute`
  * timeRange: `last7days`. See Time range.



Note that this API call returns the same report as the [ bot IP addresses report](https://docs.cloud.google.com/apigee/docs/api-security/security-reports-ui#example:-bot-ip-addresses-report) example created using the Apigee UI.

### Time range

The time range for the report. You can set the `timeRange` field in either of the following ways:

  * Specify how long in the past the report should extend. Options are: 
        
        "timeRange": "{last60minutes/last24hours/last7days}"

  * Specify a start and end time for the report in the following format: 
        
        "timeRange": {
                "start": "YYYY-MM-DDT00:00:00Z",
                "end": "YYYY-MM-DDT00:00:00Z"
                }

Both `start` and `end` must be in the past, and can be at most 1 year before the present when you create the report.




#### Sample response

The above query returns a response like the following:
    
    
    {
      "self": "/organizations/ORG/environments/ENV/securityReports/3964675e-9934-4398-bff5-39dd93a67201",
      "state": "enqueued",
      "created": "2021-08-06T22:28:28Z"
    }

The response contains the following: 

  * The report ID, which you can use to get the report once it is completed. In the example above, the report ID is `3964675e-9934-4398-bff5-39dd93a67201`.
  * `"state"`: The state of the report job, which can be one of the following: 
    * `enqueued`: The report job has just been created but is not running yet.
    * `running`: The report job is running.
    * `completed`: The report job is completed. At this stage, you can view the report.
    * `expired`: The report job has expired, and you can no longer view the report.



### Get the report status

To get the status of a report, send a request like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityReports/REPORT_ID" \
           -X GET  -H 'Content-type: application/json' -i \
           -H "Authorization: Bearer $TOKEN"

where REPORT_ID is the report ID. See Parameters in example API calls.

The response contains a summary of the report parameters, as well as the current status of the report. In this example, the status is `"completed"`, so you can view the report's results.
    
    
    {
      "self": "/organizations/sense-staging-test/environments/local/securityReports/bd2f4fe0-a906-44c2-8dcb-2c618e4b565d",
      "state": "completed",
      "created": "2022-06-27T13:00:25-07:00",
      "updated": "2022-06-27T13:01:08-07:00",
      "result": {
        "self": "/organizations/sense-staging-test/environments/local/securityReports/bd2f4fe0-a906-44c2-8dcb-2c618e4b565d/result",
        "expires": "2022-07-04T13:01:08-07:00"
      },
      "resultRows": "848",
      "resultFileSize": "5.10 KB",
      "executionTime": "43 seconds",
      "queryParams": {
        "metrics": [
          "name:bot,func:count_distinct,alias:count_distinct_bot,op:,val:",
          "name:bot_traffic,func:sum,alias:sum_bot_traffic,op:,val:"
        ],
        "dimensions": [
          "ax_resolved_client_ip"
        ],
        "startTimestamp": "2022-06-20T20:00:25.098237292Z",
        "endTimestamp": "2022-06-27T20:00:25.098237292Z",
        "mimeType": "json",
        "timeUnit": "minute"
      },
      "displayName": "Sample Query Bot"
    }

### Get the report

To download the security report, send a request like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityReports/REPORT_ID/result" \
           -X GET -O -J \
           -H "Authorization: Bearer $TOKEN"

where REPORT_ID is the report ID. See Parameters in example API calls.

This returns a file containing the report, whose name is of the form `OfflineQueryResult-{ID}.zip`. To view the report:

  1. Unzip `OfflineQueryResult-{ID}.zip`.
  2. Enter `gzip -d QueryResults-{ID}*.json.gz`.
  3. Enter `cat QueryResults-{ID}*.json`
. 


## Bot traffic example

The following example creates a report on `bot_traffic`:
    
    
    {
      "dimensions": [
        "bot_reason"
      ],
       "metrics": [
        {
          "aggregation_function": "sum",
          "name": "bot_traffic"
        }
      ],
      "groupByTimeUnit": "minute",
      "timeRange": "last7days"
    }

The query has the following parameters:

  * Metric: `bot_traffic`. This is the total number of requests from IP addresses that have been identified as bot sources, in one-minute intervals.

See [Metrics and aggregation functions](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#metrics-and-aggregation-functions).

  * Dimension: `bot_reason`. `bot_reason` can be any combination of the [detection rules](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules) for bots. When a bot is detected, `bot_reason` consists of the subset of the detection rules that the bot's traffic pattern matched.

See [Dimensions](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#dimensions).

  * Filter: `environment`. 
  * groupByTimeUnit: `minute`
  * timeRange: `last7days`



Note that this API call returns the same report as the [ bot IP addresses report](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#example:-bot-traffic-by-bot-reason-report) example created using the Apigee UI.

### Bot detection data delay

Bot detection has a processing delay of around 15 to 20 minutes on average.

## Create a security report for an environment group

Using the security reports API, you can create a report for data in an environment group (as opposed to just an environment). To do so, enter a command like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/hostSecurityReports" \
           -X POST -d @./Query.json \
           -H 'Content-type: application/json' -i \
           -H "Authorization: Bearer $TOKEN"

and make sure the query template, `Query.json`, contains the following line:
    
    
    "envgroup_hostname": "ENVGROUP"

where ENVGROUP is the name of an environment group that contains the environment. You can find the name of the environment group in the Apigee UI by going to **Admin > Environments > Groups**.

**Notes:**

  * Environment group level Report APIs only support the metric `message_count` with the aggregation function `sum`.
  * Environment group level Report APIs do not support the dimensions `bot_reason` or `incident_id`, but do support all other [dimensions](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs#dimensions) for security reports.



## Get the report status

To get the status of a report, enter a command like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/securityReports/REPORT_ID" \
           -X GET  -H 'Content-type: application/json' -i \
           -H 'Content-type: application/json' -i \
           -H "Authorization: Bearer $TOKEN"

This returns a summary of the report request, and the current state of the report. Here's a sample response:
    
    
    {
      "self": "/organizations/ngsaas-runtime-staging/environments/test/securityReports/3964675e-9934-4398-bff5-39dd93a67201",
      "state": "completed",
      "created": "2021-08-06T15:28:28-07:00",
      "updated": "2021-08-06T15:28:40-07:00",
      "result": {
        "self": "/organizations/ngsaas-runtime-staging/environments/test/securityReports/3964675e-9934-4398-bff5-39dd93a67201/result",
        "expires": "2021-08-13T15:28:40-07:00"
      },
      "resultRows": "60",
      "resultFileSize": "0.31 KB",
      "executionTime": "11 seconds",
      "queryParams": {
        "metrics": [
          "name:message_count,func:sum,alias:sum_message_count,op:,val:"
        ],
        "dimensions": [
          "apiproxy"
        ],
        "startTimestamp": "2021-08-06T21:28:28.570770570Z",
        "endTimestamp": "2021-08-06T22:28:28.570770570Z",
        "mimeType": "json",
        "timeUnit": "minute"
      }
    }

Since the state is `"completed"`, you can now view the report, as described next.

## View a security report

To view a security report, enter a command like the following:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG/hostSecurityReports/REPORT_ID/result" \
           -X GET -O -J \
           -H 'Content-type: application/json' -i \
           -H "Authorization: Bearer $TOKEN"

This returns a file containing the report, whose name is of the form `OfflineQueryResult-{ID}.zip`. To view the report:

  1. Unzip `OfflineQueryResult-{ID}.zip`.
  2. Enter `gzip -d QueryResults-{ID}*.json.gz`.
  3. Enter `cat QueryResults-{ID}*.json`
. 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
