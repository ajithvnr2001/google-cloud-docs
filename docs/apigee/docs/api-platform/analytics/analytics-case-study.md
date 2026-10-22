---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-case-study/
title: Troubleshooting with analytics \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:05.129571+00:00
---

# Troubleshooting with analytics  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-case-study/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Troubleshooting with analytics Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Data visualization is an important **troubleshooting** tool. Apigee is always collecting and analyzing data for your APIs, and visualization is the most powerful way to unlock, compare, contrast, and assess that data. 

So, let's say you've been hearing from customers (perhaps via support calls, social media sites, or user forums) that one of your APIs is slow. Visualization can help. Where do you begin?

## Consider and test for possible causes

Possible causes might include:

  * If the slowness being seen by just one app or is it from multiple apps? If one app, then it might be a problem with the app. 
  * If it being seen by multiple users across multiple apps and users seem to be in the same geo location, then it could be a network issue
  * If you're not seeing either of these issue, it could be an issue with Apigee. If you recently added or updated a policy. It could be configured incorrectly.
  * If the total response time is being reported as high, but the average endpoint response time has not changed then it might be an Apigee issue. If the average endpoint response time is also high then it could be an issue in the network between Apigee and the target server, or an internal application server.



## Visualize which API is slow

To discover which API is underperforming, one approach is to compare the average response times of all your APIs to see if one of them is out of line. 

  1. Select API Proxies from the APIs menu. 
  2. In the Performance section of the API Proxies page, select Average Response Time from the Performance menu.
  3. Select a range of dates to evaluate. 
  4. Select which APIs you wish to evaluate. 



In the plot, look for sudden spikes or gradual increases in response time. 

## Visualize with a custom report

If you suspect which API is causing a problem, you can create a custom report that includes charts and plots comparing specific metrics that you select. For example, you can visualize the maximum latency time by app and resource. 

To visualize with a custom report:

  1. In the Google Cloud console, go to the **Apigee > Analytics > Custom Reports** page.

[Go to Custom Reports](https://console.cloud.google.com/apigee/analytics/custom-reports)

  2. Click the **Reports** tab.
  3. Click **Create > Custom Report**. 
  4. Fill out the Custom Report basics. 
  5. To add a metric, select **Total Response Time** metric and **Max** as the aggregate function in the **New Metric** field, and click **Done**.
  6. To add dimensions, click add **Add a dimension** , and select **Proxy**.
  7. To add another dimension, click add **Add a dimension** , and select **Request Path**.
  8. Click **Create**.



## Analyze the resulting report

The new latency report will show you the response times by API and then by each resource within an API. By combining this information with what you know about your network architecture, you can quickly find issues that may be related to your infrastructure.

## Drill down

You can drill down on the worst performing API (the one with the highest latency). 

## Act

Now that you know which resource is performing badly, you can examine your network to see if there's a service issue, or you can add a 3rd dimension like Developer App to see which apps are impacted by this slow resource, or developer to figure out which developers are impacted by the slow resource. 

As you can see, Apigee Analytics includes multiple ways to approach a specific problem, and visualization plays an important role in any troubleshooting process. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
