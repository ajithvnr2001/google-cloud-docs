---
url: https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard/
title: API insights dashboards \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:15:39.981485+00:00
---

# API insights dashboards  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API insights dashboards Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes the dashboards available in API insights and provides an overview of the metrics available in each dashboard. 

The following dashboards are available in API insights: 

  * Gateway performance
  * API performance
  * API error analysis
  * Latency analysis
  * Target performance
  * AI performance
  * Tool performance



## Before you begin

Assign the required IAM roles and permissions to your principal account. See [IAM roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview#iam-roles) for more details.

## Gateway performance

The **Gateway performance** dashboard helps you monitor the health of your entire API ecosystem, allowing you to prioritize efforts by identifying active gateways and managing inactive or underperforming ones. You can filter the dashboard by **Gateway type** and **Gateway name**. 

To view this dashboard, go to the **API hub > API insights** page in the Google Cloud console and select the **Gateway performance** tab. 

The following metrics are available in this dashboard: 

  * **Top gateways by number of active APIs** : displays the top gateways ranked by the number of active APIs in the selected time period. 

![Top gateways by number of active APIs screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gwp1.png)![Top gateways by number of active APIs screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gwp1.png)

  * **Top gateways by total traffic** : displays the top gateways ranked by the total traffic in the selected time period. 

![Top gateways by total traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gwp2.png)![Top gateways by total traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gwp2.png)

  * **Top gateways by errors (# and %)** : displays the top gateways ranked by the number of errors and percentage of errors in the selected time period. 

![Top gateways by errors \(# and %\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gwp3.png)![Top gateways by errors \(# and %\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gwp3.png)

  * **Number of APIs per gateway** : displays a time-series graph of the number of APIs present for each gateway in the selected time period. 

![Number of APIs per gateway screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gw4.png)![Number of APIs per gateway screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gw4.png)

  * **Traffic per gateway** : displays a time-series graph of the traffic volume for each gateway in the selected time period. 

![Traffic per gateway screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gw5.png)![Traffic per gateway screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/gw5.png)




## API performance

The **API performance** dashboard provides insights into the traffic and performance of your APIs, with filters for **Gateway type** , **Gateway name** , **API name** , **Deployment name** , **API style** , and **MCP tool name**. You can click on the names of the APIs to view detailed information about that API. 

To view this dashboard, go to the **API hub > API insights** page in the Google Cloud console and select the **API performance** tab.

The following metrics are available in this dashboard: 

  * **Summary scorecards** : the following metric scorecards are displayed to provide a quick overview of the API traffic and performance data: 
    * **Total traffic** : the overall volume of API traffic in the selected time period.
    * **Successful traffic** : the total count of successful API calls in the selected time period.
    * **Traffic errors** : the total count of errors encountered in the selected time period.
    * **Avg response time** : the average time taken for a request to be processed by the gateway in the selected time period.
    * **Avg TPS** : the average number of transactions processed per second in the selected time period.
![Summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api1.png)![Summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api1.png)
  * **Transactions per second (TPS) per API** : displays a time-series graph of the number of transactions processed per second for individual APIs in the selected time period. One request and its response count as one transaction. 

![Transactions per second \(TPS\) per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api2.png)![Transactions per second \(TPS\) per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api2.png)

  * **Success rate (%) per API** : displays a time-series graph of the success rate percentage for APIs in the selected time period. 

![Success rate per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api3.png)![Success rate per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api3.png)

  * **Error rate (%) per API** : displays a time-series graph of the error rate percentage for APIs in the selected time period. 

![Error rate per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api4.png)![Error rate per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api4.png)

  * **Average response time (ms) per API** : displays a time-series graph of the average latency (total response time) in milliseconds for APIs in the selected time period. 

![Average response time \(ms\) per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api5.png)![Average response time \(ms\) per API screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api5.png)

  * **Top APIs by total traffic** : displays the top APIs ranked by the total traffic in the selected time period. 

![Top APIs by total traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api6.png)![Top APIs by total traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api6.png)

  * **Request payload size (bytes) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of request payload sizes of APIs in the selected time period. 

![Request payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api7.png)![Request payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api7.png)

  * **Response payload size (bytes) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of response payload sizes of APIs in the selected time period. 

![Response payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api8.png)![Response payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/api8.png)




## API error analysis

The **API error analysis** dashboard provides insights into the number of errors and the error type of your APIs, with filters for **Gateway type** , **Gateway name** , **API name** , **Deployment name** , **API style** , and **MCP tool name**. API errors are based on HTTP error code categories. 

To view this dashboard, go to the **API hub > API insights** page in the Google Cloud console and select the **API error analysis** tab.

The following metrics are available in this dashboard: 

  * **Number of errors** : displays a time-series graph of the total number of errors for APIs in the selected time period. 

![Number of errors screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/err1.png)![Number of errors screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/err1.png)

  * **Top APIs by number of errors** : displays the top APIs ranked by the number of errors in the selected time period. 

![Top APIs in terms of errors screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/err2.png)![Top APIs in terms of errors screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/err2.png)

  * **Number of errors based on HTTP error codes** : displays the number of API calls for each HTTP error code category. 

![API errors based on HTTP error codes categories screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/err3.png)![API errors based on HTTP error codes categories screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/err3.png)




## Latency analysis

The **Latency analysis** dashboard provides insights into the latency of your APIs across multiple percentiles, with filters for **Gateway type** , **Gateway name** , **API name** , **Deployment name** , **API style** , and **MCP tool name**. You can analyze latency by 50th, 95th, and 99th percentiles for all metrics. 

To view this dashboard, go to the **API hub > API insights** page in the Google Cloud console and select the **Latency analysis** tab.

The following metrics are available in this dashboard: 

  * **Response time (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the overall response time in milliseconds for APIs in the selected time period. 

![Response time \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/la1.png)![Response time \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/la1.png)

  * **Request processing latency (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the latency specifically during the request processing phase in milliseconds for APIs in the selected time period. 

![Request processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/la2.png)![Request processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/la2.png)

  * **Response processing latency (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the latency specifically during the response processing phase in milliseconds for APIs in the selected time period. 

![Response processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/la3.png)![Response processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/la3.png)




## Target performance

The **Target performance** dashboard provides insights into the traffic and performance of your targets, with filters for **Gateway type** , **Gateway name** , **API name** , **Target IP** , **Deployment name** , **API style** , and **MCP tool name**. 

To view this dashboard, go to the **API hub > API insights** page in the Google Cloud console and select the **Target performance** tab.

The following metrics are available in this dashboard: 

  * **Summary scorecards** : the following metric scorecards are displayed to provide a quick overview of the target traffic and performance data: 
    * **Successful target traffic** : the overall successful traffic to targets in the selected time period.
    * **Target traffic errors** : the overall traffic errors to targets in the selected time period.
![Summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp1.png)![Summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp1.png)
  * **Traffic by target** : displays a time-series graph of the traffic volume for each target in the selected time period. 

![Traffic by target screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp2.png)![Traffic by target screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp2.png)

  * **Target traffic composition (error vs. success)** : displays a time-series graph of the successful traffic versus error traffic to targets in the selected time period. 

![Target traffic composition \(error vs. success\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp3.png)![Target traffic composition \(error vs. success\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp3.png)

  * **Response time (ms) composition (avg. total vs. avg. target)** : displays a time-series graph of the average total response time versus the average target response time in the selected time period. ![Response time \(ms\) composition \(avg. total vs. avg. target\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp4.png)![Response time \(ms\) composition \(avg. total vs. avg. target\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp4.png)
  * **Target response time (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the target response time in milliseconds for targets in the selected time period. 

![Target response time \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp5.png)![Target response time \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp5.png)

  * **Error composition (total vs. target)** : displays a time-series graph of the total error count versus the target error count in the selected time period. 

![Error composition \(total vs. target\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp6.png)![Error composition \(total vs. target\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp6.png)

  * **Total target errors by response codes** : displays the total target errors categorized by HTTP response codes. 

![Total target error count grouped by response code categories screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp7.png)![Total target error count grouped by response code categories screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp7.png)

  * **Top target IPs by target traffic errors** : displays the top target IPs based on the number of target traffic errors. 

![Top target IPs by target traffic errors screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp8.png)![Top target IPs by target traffic errors screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tp8.png)




## AI performance

The **AI performance** dashboard provides insights into the token usage and performance of the large language models (LLMs) called through your gateways, with filters for **Gateway name** , **Gateway type** , **Model** , and **Provider**. 

To view this dashboard, go to the **API hub > API insights** page in the Google Cloud console and select the **AI performance** tab.

**Note:** To populate the **AI performance** dashboard, attach the following three policies to your LLM-fronting API proxy. As traffic passes through the proxy, these policies record the token and model details that the dashboard displays. Attach all three so that every chart and filter has data: 

  * [VerifyAPIKey](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) identifies the calling app, which powers the **Tokens usage by app** table. Without it, total token usage still appears but the by-app breakdown is empty. 
  * [PromptTokenLimit](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy) records the prompt (input) token count, which powers the **Prompt tokens by model** chart and the prompt-token portion of the summary scorecards. 
  * [LLMTokenQuota](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) records the model name and the response (output) token count, which power the **Response tokens by model** , **Model latency** , and **Model error rate** charts and the **Model** and **Provider** filters. 

For configuration guidance, including using these token policies for analytics only, see [Get started with LLM token policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-ai-token-policies). 

The following metrics are available in this dashboard: 

  * **Summary scorecards** : the following metric scorecards are displayed to provide a quick overview of the token usage and model performance data: 
    * **Total tokens** : the combined number of prompt and response tokens across all model calls in the selected time period.
    * **Prompt token share** : the percentage of total tokens consumed by prompts in the selected time period.
    * **Response token share** : the percentage of total tokens consumed by responses in the selected time period.
    * **Avg. model latency** : the average time taken by the model to respond in the selected time period.

![AI performance summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip1.png)![AI performance summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip1.png)

  * **Prompt tokens by model** : displays a time-series graph of the number of prompt tokens consumed by each model in the selected time period. 

![Prompt tokens by model screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip2.png)![Prompt tokens by model screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip2.png)

  * **Response tokens by model** : displays a time-series graph of the number of response tokens produced by each model in the selected time period. 

![Response tokens by model screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip3.png)![Response tokens by model screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip3.png)

  * **Tokens usage by app** : displays a table of the prompt tokens and response tokens attributed to each application in the selected time period, sorted by response tokens in descending order. 

![Tokens usage by app screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip4.png)![Tokens usage by app screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip4.png)

  * **Model latency (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the model response time in milliseconds in the selected time period. These percentiles pool data across all models rather than calculating percentiles for each model. To view the latency of a single model, apply the **Model** filter. 

![Model latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip5.png)![Model latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip5.png)

  * **Model error rate (%) by model** : displays a time-series graph of the error rate percentage for each model in the selected time period. 

![Model error rate \(%\) by model screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip6.png)![Model error rate \(%\) by model screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/aip6.png)




## Tool performance

The **Tool performance** dashboard provides insights into the traffic and performance of your Model Context Protocol (MCP) tools, with filters for **Gateway name** , **Gateway type** , **MCP server name** , **Deployment name** , and **MCP tool name**. 

To view this dashboard, go to the **API hub > API insights** page in the Google Cloud console and select the **Tool performance** tab.

The following metrics are available in this dashboard: 

  * **Summary scorecards** : the following metric scorecards are displayed to provide a quick overview of the MCP tool traffic and performance data: 
    * **Total traffic** : the overall volume of MCP tool calls in the selected time period.
    * **Avg. response time** : the average time taken for an MCP tool call to be processed by the gateway in the selected time period.
    * **Avg. TPS** : the average number of MCP tool transactions processed per second in the selected time period.

![Tool performance summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp1.png)![Tool performance summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp1.png)

  * **Transactions per second (TPS) per tool** : displays a time-series graph of the number of transactions processed per second for individual MCP tools in the selected time period. One request and its response count as one transaction. 

![Transactions per second \(TPS\) per tool screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp2.png)![Transactions per second \(TPS\) per tool screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp2.png)

  * **Top tools by total traffic** : displays the top MCP tools ranked by the total traffic in the selected time period. 

![Top tools by total traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp3.png)![Top tools by total traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp3.png)

  * **Request payload size (bytes) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of request payload sizes of MCP tool calls in the selected time period. 

![Request payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp4.png)![Request payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp4.png)

  * **Response payload size (bytes) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of response payload sizes of MCP tool calls in the selected time period. 

![Response payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp5.png)![Response payload size \(bytes\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp5.png)

  * **Response time (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the overall response time in milliseconds for MCP tool calls in the selected time period. 

![Response time \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp6.png)![Response time \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp6.png)

  * **Request processing latency (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the latency specifically during the request processing phase in milliseconds for MCP tool calls in the selected time period. 

![Request processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp7.png)![Request processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp7.png)

  * **Response processing latency (ms) (p50, p90, p99)** : displays percentiles (p50, p90, p99) of the latency specifically during the response processing phase in milliseconds for MCP tool calls in the selected time period. 

![Response processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp8.png)![Response processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/tlp8.png)


**Note:** The percentile charts on this dashboard pool data across all MCP tools rather than calculating percentiles for each tool. To view the percentiles for a single tool, apply the **MCP tool name** filter. 

## Limitations

  * Time-series charts and tables are limited to displaying the top **50** resources. 



## Considerations

  * **Time-series charting discrepancy with API analytics**

When comparing time-series charts between API insights and [API analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview), you may notice a time shift in how data points are plotted. While the overall shape of the graph for a given metric is identical, the timestamps on the x-axis will be different. 

This discrepancy is due to a fundamental difference in how the two systems anchor data points in time: 

    * API insights plots a metric value at the end time of its collection interval. For example, a data point for traffic aggregated from 8:00 AM to 9:00 AM will be displayed at the 9:00 AM timestamp. 
    * API analytics plots the same value at the start time of the interval, meaning it would be displayed at the 8:00 AM timestamp. 

The duration of this time shift is determined by the data aggregation interval (granularity), which varies based on the time range you select in the UI. 

  * API insights presents empty API data values as `Not set`. 
  * If the data volume is too large for a selected time range, or if you have a high number of resources (such as APIs, deployments, plugin instances, or target IPs), the UI might not be able to display the data. Consider selecting smaller time ranges for better results and keeping your resources below 1000. 



## What's next

  * Learn more about [API insights overview](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview). 
  * Learn about the available insights for each API resource. See [View API resource insights](https://docs.cloud.google.com/apigee/docs/apihub/view-api-resource-insights). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
