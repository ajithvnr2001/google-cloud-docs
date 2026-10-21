---
url: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/viewing-service-logs/
title: View your service's Logs \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:34.155172+00:00
---

# View your service's Logs  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/viewing-service-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  View your service's Logs Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Node.js web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service).

This guides shows you how to view App Engine logs by using the Logs Explorer and the Google Cloud console. By viewing your service's logs, you can easily monitor the performance of your web services.

## Before you begin

This guide is part of an introductory series that walks you through how to build an App Engine app. To start from the beginning of the series, see [Building a Node.js App on App Engine](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app).

Before continuing with this guide, review the steps for how to [update your web service](https://docs.cloud.google.com/appengine/docs/standard/nodejs/building-app/updating-web-service).

## View logs by using the Logs Explorer

To view your service's logs, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer?resource=gae_app)

  2. In the **Resource** list, select **GAE application** , and then click **Apply**.

  3. In the **Search all fields** field, enter the name of the log that you want to search.




You can use the filters at the top of the page to view different log streams such as standard error, HTTP requests, or App Engine internal activity.

You can search for items containing specific content, and you can also restrict the logs to a specific App Engine service or version.

## What's next

  * To build further with Node.js and App Engine, see [Tutorials](https://docs.cloud.google.com/docs/tutorials).

  * Learn more about [using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * Learn more about [monitoring and alerting latency](https://docs.cloud.google.com/appengine/docs/standard/monitoring-and-alerting-latency).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
