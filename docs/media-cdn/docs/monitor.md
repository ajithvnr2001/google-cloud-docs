---
url: https://docs.cloud.google.com/media-cdn/docs/monitor/
title: Monitor the Media CDN service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:18:21.463815+00:00
---

# Monitor the Media CDN service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Monitor the Media CDN service Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor a Media CDN service. The Media CDN Monitoring dashboard displays information that can help you monitor the performance of your Media CDN service.

For detailed information about Media CDN metrics in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), including [CMCD](https://cdn.cta.tech/cta/media/media/resources/standards/pdfs/cta-5004-final.pdf) metrics, see the [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-edgecache) page.

## Open the Monitoring dashboard

To open the Monitoring dashboard, do the following:

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the service name.

  3. On the **Details** page, click the **Monitoring** tab.

  4. From the **Continent filter** list, select one or more `proxy_continent` values, which represent the continents of users who send requests to the service based on their GeoIP.

  5. Optional: To change the selected time period, select one of the other predefined periods on the time selector. Alternatively, click **Custom** and define a start time and an end time.




## Summary cards

Summary cards show the aggregated values for some metrics and provide an overview of the Media CDN service. The following table briefly describes the summary cards.

Summary card | Description  
---|---  
Total requests | The total number of requests to the `EdgeCacheService` resource  
Cache egress | The cache egress count in bytes  
Cache fill | The cache fill count in bytes  
Error rate | The rate at which errors are logged  
  
## Tables

The tables show traffic volume data grouped by parameters, including client countries, proxy regions, and cache results. The data shown includes response counts and cache egress as both values and ratios.

The following table describes the parameters by which the data is grouped in these tables.

Table| Description  
---|---  
Audience | The traffic volume data grouped by `client_country`, which is the country of the user who sends the request based on their GeoIP  
Proxy regions | The traffic volume data grouped by `proxy_region` values, which represent the country of the cache node egressing the content  
Cache results summary | The traffic volume data grouped by `cache_result` status labels such as `HIT` and `MISS`  
  
You can work with the tables on the **Monitoring** page in the following ways:

  * To sort a table by a column, click the column header.

  * To filter the results, do the following:

    1. To see a list of properties, click the area next to **Filter**.

    2. In the list, select a property. The property name, followed by a colon, appears next to the **Filter table** label.

    3. To see a list of values that match the property, insert a space next to the colon, and then select a value from the list.

    4. Optional: To specify combined filters, enter the `OR` operator between the property-value pairs.

  * To browse through a table that spans multiple pages, use the page navigator at the lower-right corner of each table.




## Metrics charts

The metrics charts show information about important metrics that help you gain insights into any issues that you might have with your Media CDN service.

The following table describes the charts that appear on the Media CDN Monitoring dashboard. The metric type strings follow the prefix `edgecache.googleapis.com/edge_cache_route_rule/`.

Chart | Metric | Description  
---|---|---  
Edge Cache egress bandwidth | `response_bytes_count` | The count of response bytes  
Edge Cache request hit rate | `request_count` | The number of cache hits as a fraction of the total number of requests  
Cache egress vs. cache fill bandwidth | `response_bytes_count`, `origin_response_bytes_count` | The total response bytes egressed from the cache against the count of response bytes ingressed from the origin  
Requests by response code | `request_count` | The count of requests by `response_code_class`  
Origin requests by response code | `origin_request_count` | The count of requests to the origin by `response_code_class`  
Top 5 error response codes | `request_count` | The count of requests by the top five `response_code` values  
Total latencies | `total_latencies_by_proxy` | The distribution of latencies calculated from when requests were received by a proxy until the client acknowledged the proxy on the last response byte  
Origin time to first byte | `origin_http_ttfb` | The distribution of latencies calculated from when the request was sent by the proxy until the response headers were received from the origin  
HTTP time to last byte | `http_ttlb_by_client` | The distribution of latencies calculated from when the request was received by the proxy until the last byte of the response was sent with client location information  
  
The toolbar on each chart card provides the following set of standard options:

  * To hide or display the legend, click legend_toggle.

  * To view metric values for a specific moment in the selected period, move the cursor over the chart.

  * To view a chart in full-screen mode, click fullscreen. To exit full-screen mode, click **Esc**.

  * To zoom a chart, click the chart and drag horizontally along the x-axis. To revert the zoom operation, click youtube_searched_for. Zoom operations apply at the same time to all charts on a dashboard.

  * To view additional options, click more_vert.

The charts offer these options:

    * **Download PNG**
    * **Download CSV**
    * **Add to custom dashboard**. After selecting this option, provide a name for the dashboard or select an existing custom dashboard. View and edit the dashboard by using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/dashboards).
    * **View in Metrics Explorer**. View the metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
