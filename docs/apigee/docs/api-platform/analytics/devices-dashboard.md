---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/devices-dashboard/
title: Devices dashboard \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:20.047627+00:00
---

# Devices dashboard  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/devices-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Devices dashboard Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Dashboard availability:** This dashboard is not available if your Apigee organization was provisioned with compliance-related Apigee features, such as [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), [CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts), and [workforce identity federation](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/workforce-identity-federation-apigee#accessing-features-only-available-in-the-classic-apigee-ui).

## What does this dashboard tell me?

The Devices dashboard tells you about the devices and servers that are being used to access your APIs. It lets you spot trends in how users are accessing your APIs. For instance, you might notice that traffic from one type of device is increasing, while another is going down, and then decide if the change requires any action or not.

**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The Devices dashboard

**Required roles:** To access the **Devices** dashboard, you must have the following IAM predefined roles: 

  * `roles/apigee.analyticsViewer`
  * `roles/apigee.analyticsEditor`
  * `roles/apigee.addonsconfig.get`



For more information, see [How to specify a predefined role](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#expandable-1). 

To access the Devices dashboard:

In the Google Cloud console, go to the **Apigee > Analytics > End user analysis > Devices** page.

[Go to Devices](https://console.cloud.google.com//apigee/analytics/enduser/devices)

The dashboard opens as shown:

![The Devices dashboard includes charts for metrics such as top device category and
    traffic by agent family.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/devices.png)

## Using the dashboard

The dashboard has a set of dropdown menus that you can use to filter the information shown in it. The filter dropdown menus are dynamic. For example, if you select an environment from the Environments dropdown, then any proxies, and hostnames associated with that environment are automatically selected in the other dropdown menus, charts, and tables. For more information, see [About filter properties](https://docs.cloud.google.com/looker/docs/studio/about-filter-properties) in the Data Studio documentation.

Use the date selector to pick a start and end date to measure. The date selector only lets you select dates in day increments. You can't select a time range increment that is smaller than a day.

The graphs are interactive. Hover over a graph to see more details. Use the action menu in a graph for options like sorting and exporting data.

**Note:** Seeing a dimension entity named _**(not set)**_? For more information, see [ What does an analytics entity named (not set) mean?](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/why-am-i-seeing-analytics-entity-named-not-set)

## What does this dashboard measure?

In addition to the following metrics, the dashboard shows the top agents, agent types, device types, and OS families.

Metric | Description  
---|---  
Traffic by user agent family | Measures how much traffic is coming from a specific application, like Google Chrome, Safari, Firefox, cURL, IE, and other agents.  
Traffic by user agent type | Tells you if traffic is coming from a browser, a robot, a library, or other agents.  
Traffic by device category  | Tells you if traffic is coming from a PC, a mobile device, and other categories.  
  
  
## What else do I need to know about this dashboard?

You can view data for all API proxies in your organization, or you can use the **Proxies** drop-down to select individual APIs to analyze. When traffic origination cannot be determined, it is recorded as "Others".

This dashboard uses standard controls, like the date and data aggregation selectors, hovering over graphs for more context, exporting data to CSV, and so on. To learn more, see [Using the analytics dashboards](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-analytics-dashboards).

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
