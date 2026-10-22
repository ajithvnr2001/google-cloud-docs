---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/traffic-composition-dashboard/
title: Traffic composition \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:56.118172+00:00
---

# Traffic composition  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/traffic-composition-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Traffic composition Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Dashboard availability:** This dashboard is not available if your Apigee organization was provisioned with compliance-related Apigee features, such as [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), [CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts), and [workforce identity federation](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/workforce-identity-federation-apigee#accessing-features-only-available-in-the-classic-apigee-ui).

## What does this dashboard tell me?

The Traffic Composition dashboard measures the relative contribution of your top APIs, apps, developers, and products to your overall API program.

Use the report to detect business problems such as lower traffic trends or diminishing contribution from key apps and developers. Based on this data, you can decide what corrective action to take. You can also get early notification of new entities that contribute to API traffic, and take actions to respond — for example, you can determine which new developers are highly contributing and include them in nurturing programs.

**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The Traffic Composition dashboard

**Required roles:** To access the **Traffic Composition** dashboard, you must have the following IAM predefined roles: 

  * `roles/apigee.analyticsViewer`
  * `roles/apigee.analyticsEditor`
  * `roles/apigee.addonsconfig.get`



For more information, see [How to specify a predefined role](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#expandable-1). 

To access the Traffic Composition dashboard:

In the Google Cloud console, go to the **Apigee > Analytics > Developer analysis > Traffic composition** page.

[Go to Traffic composition](https://console.cloud.google.com//apigee/analytics/developer-analysis/traffic-composition)

The dashboard opens as shown below:

![A dashboard containing a chart about developer engagement points to where you find
      the analyze button.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/traffic-comp-main2.png)

## Using the dashboard

The dashboard has a set of dropdown menus that you can use to filter the information shown in the dashboard. The filter dropdown menus are dynamic. For example, if you select a developer from the Developers dropdown, then any proxies, apps, and API products associated with that developer are automatically selected in the other dropdown menus, charts, and tables. For more information, see [About filter properties](https://docs.cloud.google.com/looker/docs/studio/about-filter-properties) in the Data Studio documentation.

Use the date selector to pick a start and end date to measure. The date selector only lets you select dates in day increments. You can't select a time range increment that is smaller than a day.

**Note:** Seeing a dimension entity named _**(not set)**_? For more information, see [ What does an analytics entity named (not set) mean?](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/why-am-i-seeing-analytics-entity-named-not-set)

## What does this dashboard measure?

This dashboard has two measurement modes, which you select with the **Overview** and **Dimension** tabs:

Mode | Description  
---|---  
Overview | Gives you a quick glance at traffic patterns for proxies, developer apps, products, and developers. For example, use this view to see which proxy, app, product, or developer is generating the most traffic.  
Dimension | Let's you drill in to see a more detailed view of proxy, developer app, product, and developer traffic.  
**Note:** Seeing a dimension entity named _**(not set)**_? For more information, see [What does an analytics entity named (not set) mean?](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/why-am-i-seeing-analytics-entity-named-not-set).

### What the Overview mode tells you

Click **Overview** to display this mode. This mode presents a set of straight-forward graphs showing traffic patterns proxies, developer apps, developers, and products.

The following figure shows part of the traffic composition overview page:

Mode | Description  
---|---  
Top 10 proxies by traffic | Shows the top 10 proxies measured by API traffic.  
Top 10 developers by traffic | Shows the top 10 developers measured by API traffic.  
Top 10 products by traffic | Shows the top 10 products measured by API traffic.  
Top 10 apps by traffic | Shows the top 10 developer apps measured by API traffic.  
  
### What the Dimension mode tells you

Click **Dimension** to display this mode. This mode lets you drill in to see traffic pattern details for **specific** proxies, developer apps, developers, and products.

Details shown in the dimension mode include:

Metric | Description  
---|---  
Traffic over time by proxy | Lets you see the relative traffic contribution of each proxy.  
Traffic over time by developer | Lets you see the relative traffic contribution of each developer.  
Traffic over time by product | Lets you see the relative traffic contribution of each API product.  
Traffic over time by apps | Lets you see the relative traffic contribution of each developer app.  
  
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
