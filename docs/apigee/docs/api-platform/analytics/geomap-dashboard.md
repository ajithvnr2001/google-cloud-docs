---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/geomap-dashboard/
title: Geomap dashboard \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:01.393241+00:00
---

# Geomap dashboard  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/geomap-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Geomap dashboard Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This product includes GeoLite Data created by MaxMind, available from [https://www.maxmind.com](https://www.maxmind.com/).**Dashboard availability:** This dashboard is not available if your Apigee organization was provisioned with compliance-related Apigee features, such as [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), [CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts), and [workforce identity federation](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/workforce-identity-federation-apigee#accessing-features-only-available-in-the-classic-apigee-ui).

## What does this dashboard tell me?

The Geomap dashboard tracks traffic patterns, error patterns, and quality of service across geographical locations. You can view information about all your APIs, or zoom in on specific ones. This dashboard helps you assess:

  * **API growth trends** \- Use the **Sum of traffic metric** to see where your traffic is coming from. By using different time periods you can see which countries generate the most traffic at which times. You can also record traffic rates over different time periods to see trends in growth. 
  * **Error trends** \- Use the **Sum of error count** metric to see where API errors are coming from. By using different time periods you can see which countries generate the most errors at which times. You can also record error rates over different time periods to see trends in growth.
  * **Quality of service** \- Use the **Average of total response time** and **Average of target response time** metrics to see how your backend services are performing by country.



**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The Geomap Dashboard

**Required roles:** To access the **Geomap** dashboard, you must have the following IAM predefined roles: 

  * `roles/apigee.analyticsViewer`
  * `roles/apigee.analyticsEditor`
  * `roles/apigee.addonsconfig.get`



For more information, see [How to specify a predefined role](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#expandable-1). 

To access the Geomap dashboard:

In the Google Cloud console, go to the **Apigee > Analytics > End user analysis > Geomap** page.

[Go to Geomap](https://console.cloud.google.com//apigee/analytics/enduser/geomap)

The dashboard opens as shown:

![The dashboard displays a world map and bar graph that represent the sum of traffic
    for all proxies in all countries.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/geomap-dashboard2.png)

## What does this dashboard measure?

By default, the dashboard displays the **Sum of traffic** metric. The following table describes each of the metrics tracked by the Geomap dashboard:

Metric | Description  
---|---  
Sum of traffic | Also known as throughput. The number of API requests and resulting responses seen by the organization.  
Sum of error count | The total number of all API requests that are unsuccessful, that is, the request does not deliver a response as desired by the end user.  
Average of total response time | The time an API takes to respond to an incoming request.  
Average of target response time | The average time it takes the target endpoint to respond to an incoming request for the selected period.  
  
## Using the dashboard

The dashboard has a set of dropdown menus that you can use to filter the information shown in it. The filter dropdown menus are dynamic. For example, if you select an environment from the Environments dropdown, then any proxies, hostnames, countries, and regions associated with that environment are automatically selected in the other dropdown menus, charts, and tables. For more information, see [About filter properties](https://docs.cloud.google.com/looker/docs/studio/about-filter-properties) in the Data Studio documentation.

Use the date selector to pick a start and end date to measure. The date selector only lets you select dates in day increments. You can't select a time range increment that is smaller than a day.

The map is interactive. Click a country to see traffic for that country. You can right-click a data table for actions like sorting and exporting data.

**Note:** Seeing a dimension entity named _**(not set)**_? For more information, see [ What does an analytics entity named (not set) mean?](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/why-am-i-seeing-analytics-entity-named-not-set)

## What else do I need to know about this dashboard?

By default, the dashboard displays metrics for all API proxies. Alternatively, select an API proxy to measure from the **Proxies** dropdown menu. 

Select an entry under the **Countries** and **Geographical regions** lists to drill down on specific countries, states, and cities (depending on the specific geography of the country you are interested in). For example, you can look at United States data, then select a geographical region, and then view a list of cities from which traffic is generated. You can click a city name in the table to see traffic for that city.

This dashboard uses standard controls, like the date selector, hovering over maps for more context, exporting data to CSV, and so on. To learn more, see [Using the analytics dashboards](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-analytics-dashboards).

## Make a copy in Data Studio

You can edit, save, and share a copy of the dashboard in [Data Studio](https://docs.cloud.google.com/looker/docs/studio/new-studio-docs). To get started:

  1. Click **Make a copy in Data Studio**.
  2. From the dropdown menu, select the report you wish to copy.
  3. In Data Studio, click **Save and share**.
  4. Click **Acknowledge and save**.



You can now edit the copy saved in your user account. For details on using Data Studio to edit and create reports, see the [Data Studio documentation](https://docs.cloud.google.com/looker/docs/studio/about-reports).

**Note:** Any changes you make in Data Studio are not reflected back in the Apigee dashboard.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
