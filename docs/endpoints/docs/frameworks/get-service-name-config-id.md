---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/get-service-name-config-id/
title: Getting the service name and configuration ID \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:31.762762+00:00
---

# Getting the service name and configuration ID  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/get-service-name-config-id/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Getting the service name and configuration ID Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get the name of your service and its configuration ID.

### Google Cloud console

  1. In the Google Cloud console, go to the **Endpoints** > **Services** page for your project. 

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, select an API from the list.
  3. Click the **Deployment history** tab.

The service name is displayed between the API name and the tabs, near the top-left side of the page. In the **Service configuration deployments** list, the configuration ID is displayed along with the date and the email address of the principal who deployed the configuration. The **Service configuration deployments** list displays the latest 100 configuration deployments. The most recent configuration is displayed at the top of the list.




### `gcloud`

  1. Enter the following to display the project IDs for your Google Cloud projects: 
         
         gcloud projects list

  2. Using the applicable project ID from the previous step, set the default project to the one that your API is in: 
         
         gcloud config set project YOUR_PROJECT_ID

  3. Get a list of services in your project: 
         
         gcloud endpoints services list

  4. Using the applicable service name from the previous step, get a list of configuration IDs for the service: 
         
         gcloud endpoints configs list --service=YOUR_SERVICE_NAME




For more information on the preceding commands, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
