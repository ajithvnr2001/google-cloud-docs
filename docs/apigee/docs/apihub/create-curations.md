---
url: https://docs.cloud.google.com/apigee/docs/apihub/create-curations/
title: Create curations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:43.548593+00:00
---

# Create curations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/create-curations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create curations Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to set up custom curations in API hub. Custom curations enable you to override the default curation logic of your [plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-instance) to implement a tailored data transformation and enrichment process based on your organization's needs. 

## Before you begin

Ensure the following before setting up a custom curation:

  * Provision Application Integration in your Google Cloud project. See [Set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration) for more information. **Note:** You must provision Application Integration in the same Google Cloud project and region as your API hub instance.



## Create a custom curation

To create a new custom curation logic, do the following:

  1. Create an integration for the custom curation in Application Integration.
  2. Set up a custom curation in API hub.



### Create an integration for the custom curation in Application Integration

To create a custom curation logic in Application Integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. The **Integrations** page appears. 
  3. Click add_box **Create integration** and provide the following details in the **Create Integration** page: 
     1. **Integration name:** Enter a name for your integration.
     2. **Description:** Optionally, enter a description for your integration.
     3. **Region:** Select the region for your integration. This must be the same region as your API hub instance.
     4. Click **Create** to open the integration in the integration editor.
  4. Configure [integration variables](https://docs.cloud.google.com/application-integration/docs/variables#integration_var) using the [`ApiData`](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations/collectApiData#ApiData) definition. These variables will be used as input and output task variables for the custom curation logic.
  5. Add an [API trigger](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger) and use the available [tasks](https://docs.cloud.google.com/application-integration/docs/tasks) to build your custom curation logic.
  6. Once complete, click **Publish** to publish the integration.



For more information about Application Integration, see the [Application Integration](https://docs.cloud.google.com/application-integration/docs/overview) documentation. 

### Set up a custom curation

Once you have created and published your integration in Application Integration, you can set up the custom curation in API hub. To set up a custom curation, do the following: 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Curations** tab to view the list of curations.
  4. Click **Setup a new curation**.
  5. In the **Set up curation** pane, provide the following details: 
     1. Optional: Click **Specify ID** to provide a unique ID for the curation. API hub generates a unique ID if you don't provide one. **Note:** The ID must be between 4 to 500 characters in length and can only contain the following characters: `/[A-Z][a-z][0-9]-/.`
     2. **Display name** : Enter a name for the curation.
     3. **Description** : Enter a description for the curation.
     4. If you have an existing integration created for your curation logic in Application Integration, do the following under **Associate an existing integration** section: 
        1. **Integration** : Choose the integration that you want to associate for the curation. **Note:** Only published integrations can be associated for curations. 
        2. **Trigger ID** : Choose the API trigger ID that you want to associate for the curation.
     5. If you don't have an existing integration created for your curation logic in Application Integration, follow the instructions in Create an integration for the custom curation to create an integration and then continue from Step 5d. 
  6. Click **Create curation** to initiate the creation of the custom curation. 

On successful creation, the curation is listed under **Manage curations** as shown in the following image:

![Image showing the custom curation.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/custom-curation.png)![Image showing the custom curation.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/custom-curation.png)




## What's next

  * Learn how to [view and manage curations](https://docs.cloud.google.com/apigee/docs/apihub/manage-curations).
  * Learn how to [edit the configuration of a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
