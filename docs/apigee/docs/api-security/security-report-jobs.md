---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs/
title: Security reports overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:58:05.418215+00:00
---

# Security reports overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Security reports overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Security reports are reports that identify security threats to your APIs. To generate reports, Apigee scans API traffic data over a specified time interval and searches for unusual traffic patterns that could be caused by malicious agents. The resulting report shows suspicious activity. You can use this information to block attacks against your APIs.

You can create security reports either in [Apigee in Cloud console](https://docs.cloud.google.com/apigee/docs/api-security/security-reports-ui) or using the [security reports API](https://docs.cloud.google.com/apigee/docs/api-security/security-reports-api). If you use the UI, the data for reports is restricted to the environment you choose. However, using the API, you can also create reports for environment groups.

See [ Required roles for security reports](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#required-roles-for-security-reports) for the roles needed to perform security reports tasks.

To use this feature, you must enable the add-on. If you are a Subscription customer, you can enable the add-on for your organization. See [ Manage Advanced API Security for Subscription organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-subscription-organizations) for more details. If you are a Pay-as-you-go customer, you can enable the add-on in your eligible environments. For more information, see [ Manage the Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-security-add-on).

**Note:** If you add an environment after enabling Advanced API Security, you will need to re-enable it, by running the command shown in [Enable Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#enable-creating-organization) again, to view security reports for the new environment.

## Bot detection

One of the most serious threats to API security comes from [bots](https://en.wikipedia.org/wiki/Internet_bot): automated scripts that send malicious requests to APIs. Advanced API Security searches for specific API traffic patterns, called [_detection rules_](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules), which are based on analysis of real API data, to detect bots.

## Security reports data delay

Data flowing into the Apigee Analytics pipeline has a delay of up to 15 to 20 minutes on average. As a result, a security report in which the end time is less than 20 minutes in the past might return incorrect results.

## Metrics and aggregation functions in security reports

You can use the following metrics and aggregation functions, which compute statistics from a metric, for a report.

Metric | Description | `Aggregation function`  
---|---|---  
`bot` | The number of distinct IP addresses for detected bots over one-minute intervals.  | `count_distinct`  
`bot_traffic` | The number of messages from IP addresses of detected bots over one-minute intervals.  | `sum`  
`message_count` | Total number of API calls processed by Apigee in one-minute intervals. **Note:** `message_count` cannot be used with other metrics in the same report. | `sum`  
`response_size` | Size of the response payload returned in bytes. | `sum`, `avg`, `min`, `max`  
`bot_first_detected` | Date and time the bot was first detected. Only available through the API. | `min`  
`bot_last_detected` | Date and time the bot was last detected. Only available through the API. | `max`  
  
## Dimensions in security reports

Dimensions let you group metric values together based on related subsets of the data. The following table describes the dimensions that are specific to Advanced API Security:

Dimension | Description  
---|---  
`bot_reason` | Can be any combination of the security [detection rules](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules). `bot_reason` consists of the subset of the detection rules that the bot's traffic pattern matched. `bot_reason` only works with the following metrics:

  * `bot`
  * `bot_traffic`
  * `response_size`

  
`incident_id` (preview) | The UUID for a security incident, which is returned by a call to the Incidents API. See [ Example: Get details for a specific incident](https://docs.cloud.google.com/apigee/docs/api-security/incidents-api#example:-get-details-for-a-specific-incident). `incident_id` only works with the following metrics:

  * `bot`
  * `bot_traffic`
  * `response_size`

  
`security_action` | The security action. Possibly values are `ALLOW`, `DENY`, or `FLAG`.   
`security_action_name` | The name of the security action.  
`security_action_headers` | Headers that you can use to query for a flag security action.  
  
In addition to these Advanced API Security-specific dimensions, Advanced API Security also supports additional dimensions, which are described in [dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions).

## Reference security reports

This table lists examples of security of reports that you can create using different metrics and dimensions:

Report | Metrics | Dimensions  
---|---|---  
All Bot Traffic & Bot Count Report for per environment | **bot** , **bot_traffic** | **environment**  
Bot Traffic & Bot Count Report for different bot reasons | **bot** , **bot_traffic** | **bot_reason**  
Bot Traffic & Bot Count Report for different Countries | **bot** , **bot_traffic** | **ax_geo_country**  
Bot Traffic & Bot Count Report for different ISPs | **bot** , **bot_traffic** | **ax_isp**  
Bot Detection Report (Detailed List View) | **bot_traffic** | **Resolved Client IP** , **ax_isp** , **bot_reason** , **request_uri** , **client_id**  
Bot traffic per Access Token | **bot_traffic** | **access_token**  
Bot traffic per API proxy | **bot_traffic** | **apiproxy**  
Bot traffic per Agent Family | **bot_traffic** | **ax_ua_agent_family**  
Bot traffic per User Agent | **bot_traffic** | **useragent**  
Bot traffic per Agent Type | **bot_traffic** | **ax_ua_agent_type**  
Bot traffic per Device Category | **bot_traffic** | **ax_ua_device_category**  
Bot traffic per OS family | **bot_traffic** | **ax_ua_os_family**  
Bot traffic per Client ID | **bot_traffic** | **client_id**  
Bot traffic per Proxy Basepath | **bot_traffic** | **proxy_basepath**  
Bot traffic per Proxy Path Suffix | **bot_traffic** | **proxy_pathsuffix**  
Bot traffic per Request URI | **bot_traffic** | **request_uri**  
Bot traffic per Request Verb | **bot_traffic** | **request_verb**  
Bot traffic per Response Status Code | **bot_traffic** | **response_status_code**  
  
## Limitations on security reports

Security reports have the following limitations:

  * Data flowing into the Apigee Analytics pipeline has a delay of up to 15 to 20 minutes on average. As a result, creating a report in which the **End Time** is less than 20 mins in the past might return incorrect results.
  * Maximum time range for bot reports is 1 year.
  * The maximum number of metrics you can use in a report is 25, and the maximum number of dimensions you can use is 25.
  * As with the [asynchronous custom reports API](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/asynch-reports-api), there is a limit of 31 MB of data for a report. If you encounter a size limit on a report, you can either: 
    * Reduce the time range of the report.
    * Split the data into smaller subsets by filtering on a set of values, and then create multiple reports, one for each subset.
  * The **Resolved Client IP** dimension can't be listed in the same report with either the **ax_geo_city** or **ax_geo_country** dimension, due to privacy concerns.
  * Security report jobs that filter on the `incident_id` must include the `incident_id` as a dimension.
  * The following metrics are only available via the [security reports API](https://docs.cloud.google.com/apigee/docs/api-security/security-reports-api), but not in the UI: **bot_first_detected (min)** and **bot_last_detected (max)**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
