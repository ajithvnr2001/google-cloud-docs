---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-operations-anomalies-alerts/
title: Create anomaly alerts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:31.991482+00:00
---

# Create anomaly alerts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-operations-anomalies-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create anomaly alerts Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

When operations anomalies detects an anomaly, it displays the event in the [ operations anomalies dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/investigate-anomalies). However, it doesn't automatically raise an alert for the anomaly.

If you want to be notified about operations anomalies, you can create an anomaly alert and notification.

When creating anomaly alerts, you don't need to define the exact conditions for each anomaly yourself. Operations anomalies determines the right anomaly conditions using statistical methods, and updates them based on recent traffic data.

## Before you begin

To use anomaly alerts, first make sure your project and your user account meet the requirements in [Prerequisites for using operations anomalies](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/operations-anomalies-overview#prerequisites-for-using-operations-anomalies). 

### Create anomaly alerts

In the Google Cloud console, go to the **Monitoring > Alerting > Policies** page.

[Go to Policy Configuration Mode](https://console.cloud.google.com/monitoring/alerting/policies/create)

See the [Alerting overview](https://cloud.google.com/monitoring/alerts) instructions for using Alerting policy dashboard.

For Apigee operations anomalies alerting:

  * Select **Apigee anomaly event count** as the metric.
  * In the **Configure alert trigger** window, set the **Threshold** to **0.5**. (Any number between 0 and 1 will work for the threshold.) With this value, a single anomaly exceeds the threshold and triggers the alert. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
