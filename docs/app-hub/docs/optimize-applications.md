---
url: https://docs.cloud.google.com/app-hub/docs/optimize-applications/
title: Optimize an application with design recommendations \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:15.537317+00:00
---

# Optimize an application with design recommendations  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/optimize-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Optimize an application with design recommendations Stay organized with collections  Save and categorize content based on your preferences. 

Continuously improving your App Hub applications is key to meeting operational and business goals. Application insights and assistance services, such as [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview) and [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview), help you identify optimization opportunities. For example, you might receive recommendations to resize underutilized virtual machines or configure Cloud CDN to reduce latency and cost.

This guide shows you how to analyze an existing application and then use [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) to implement architectural changes.

## Before you begin

This document assumes you have [set up a folder-level application management boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) for your applications. Application Design Center, Cloud Hub, and Gemini Cloud Assist require this boundary type.

You must complete the following steps before using application insights and assistance services:

  * **For administrators** :

    1. Enable required APIs for all Google Cloud resources you intend to use.
    2. [Set up Application Design Center](https://docs.cloud.google.com/application-design-center/docs/setup). Only required if you intend to create new application components from [templates](https://docs.cloud.google.com/app-hub/docs/key-concepts#template).
    3. [Set up Cloud Hub](https://docs.cloud.google.com/hub/docs/setup-cloud-hub). Only required if you intend to use Cloud Hub to identify optimization opportunities.
    4. [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini). Only required if you intend to use Gemini Cloud Assist to identify optimization opportunities.
    5. [Grant access to users](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles). Assign appropriate IAM roles based on user's responsibilities in the application lifecycle.
  * **For developers and operators** :

    1. Confirm that applications exist within your [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary).
    2. [Make sure you have the necessary IAM roles](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles) for the tasks you want to perform.
    3. Open your [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) in the Google Cloud console.



## Analyze the application for optimization opportunities

Use [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview) and [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) to get a consolidated view of your application's operational data and receive recommendations:

  1. In the Google Cloud console, use the project picker to select your management project.
  2. Navigate to the **Home** page from Cloud Hub:

[Go to Home](https://console.cloud.google.com/cloud-hub/home)

  3. Select your application to view its integrated dashboard.

  4. Review incidents, alerts, performance metrics, and cost trends. For more information, see [Application views and project views](https://docs.cloud.google.com/hub/docs/app-project-views).

  5. Optionally, [use the Gemini Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel) to ask for optimization recommendations using natural language prompts, for example:

     * `Give me recommendations to optimize my application.`
     * `Show me the most expensive resources with the lowest utilization for this application.`

Gemini Cloud Assist provides recommendations, such as resizing underutilized machine types or enabling a Cloud CDN.




## Evolve the application architecture

After identifying an optimization, use [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) to model and deploy the improved architecture:

  * **If the application was deployed from a template:** [Open the template and modify its architecture](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#revise_and_reshare_your_template) based on the recommendations. You can then [deploy the new version](https://docs.cloud.google.com/app-hub/docs/create-applications-from-templates) as an update to the existing application instance.
  * **If the application wasn't deployed from a template:** [Create a new template](https://docs.cloud.google.com/app-hub/docs/create-reusable-template) in Application Design Center that reflects the optimized architecture.



[Deploy the optimized application architecture](https://docs.cloud.google.com/application-design-center/docs/deploy-from-console). This process might involve updating an existing deployment or creating a new one, depending on the nature of the changes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
