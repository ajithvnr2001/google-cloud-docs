---
url: https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini/
title: Build integrations with Gemini Code Assist \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:20.637907+00:00
---

# Build integrations with Gemini Code Assist  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build integrations with Gemini Code Assist

Gemini Code Assist is an AI-powered collaborator in Google Cloud that provides help to users of all skill levels where they need it. In Application Integration, Gemini Code Assist can assist you to do the following: 

  * Create integrations
  * Configure connector tasks in an integration
  * Configure Call REST API tasks in an integration
  * Add edge conditions and append additional tasks to an integration
  * Configure JavaScript tasks ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Generate integration description



For detailed information about Gemini for Google Cloud, see [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).

## Before you begin

  1. In the Google Cloud console, go to the **Application Integration** page.  


[Go to Application Integration](https://console.cloud.google.com/integrations)

The following image shows the Application Integration page:

![Enable Gemini in Application Integration](https://docs.cloud.google.com/static/application-integration/images/gemini-explore.png)![Enable Gemini in Application Integration](https://docs.cloud.google.com/static/application-integration/images/gemini-explore.png)

     1. In the **Get AI to build your integrations** section, click **Explore**.
     2. In the **Gemini in Application Integration** pane that appears, click **Enable Service** to enable the Gemini for Google Cloud API. 

For information about activating Gemini Code Assist in a Google Cloud project, see [Set up Gemini Code Assist for a project](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini).

  2. Set up Application Integration in your Google Cloud project. For more information, see [Set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration).
  3. If you plan to create an integration using [connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors), ensure to configure the desired connections in your Google Cloud project. 
  4. If you plan to create an integration using [Apigee API Hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) APIs that are in a host project, ensure that you have [provisioned the API Hub in your project](https://docs.cloud.google.com/apigee/docs/apihub/provision) and that the Application Integration service account has the required role to access the APIs in the other project.

**Note:** Gemini provides connector- and API Hub-based recommendations or suggestions for your integrations using the configured connections in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs) and APIs in [Apigee API Hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub). If you don't have any connections or APIs configured in your project, then Gemini might not provide connector- and API-based recommendations or suggestions.

## Required roles

  * To get the permissions that you need to use Gemini, ask your administrator to grant you the [Gemini for Google Cloud User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * If you plan to create an integration with [Apigee API Hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub), ensure that you have the Cloud API hub Viewer role (`roles/apigeeregistry.viewer`) on the project that contains the APIs.
  * If you plan to create an integration with [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs), ensure that you have the Connectors Viewer role (`roles/connectors.viewer`) on the project.



## Supported tasks and triggers

Gemini can assist you to add the following tasks and triggers: **Triggers** | **Tasks**  
---|---  
  
  * [API trigger](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger)
  * [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger)
  * [Salesforce trigger](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger)
  * [Jira Cloud](https://docs.cloud.google.com/application-integration/docs/configure-jira-cloud-trigger)
  * [ServiceNow](https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger)
  * [Zendesk](https://docs.cloud.google.com/application-integration/docs/configure-zendesk-trigger)
  * [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger)

| 

  * [Data mapper task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task)
  * [Approval task](https://docs.cloud.google.com/application-integration/docs/configure-approval-task)
  * [Suspend task](https://docs.cloud.google.com/application-integration/docs/configure-suspend-task)
  * [Javascript task](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task)
  * [Cloud Run functions](https://docs.cloud.google.com/application-integration/docs/configure-cloud-function-task)
  * [Timer task](https://docs.cloud.google.com/application-integration/docs/configure-timer-task)
  * [Return task](https://docs.cloud.google.com/application-integration/docs/configure-return-task)
  * [Send email task](https://docs.cloud.google.com/application-integration/docs/configure-send-email-task)
  * [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task)
  * [Call REST endpoint task](https://docs.cloud.google.com/application-integration/docs/configure-call-rest-endpoint-task)
  * [Doc AI - Process task](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-documentai-process-task)

Gemini also assists you to create the following control flow tasks but can't generate sub-integrations:

  * [For Each Loop task](https://docs.cloud.google.com/application-integration/docs/configure-for-each-loop-task)
  * [For Each Parallel task](https://docs.cloud.google.com/application-integration/docs/configure-for-each-parallel-task)
  * [While Loop task](https://docs.cloud.google.com/application-integration/docs/configure-while-loop-task)
  * [Call Integration task](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task)

  
  
## Create an integration

Gemini assists you to create and build integrations using your natural language statements (or _prompts_) as input. This allows you to create and build simple to complex integrations quickly and with minimal manual configurations. 

Provide Gemini a brief prompt or description of the integration flow that you intent to build and Gemini will suggest one or more integration flows to help you get started. 

To build an integration using Gemini, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click spark **Help me create**. The **Create Integration with Gemini** pane appears. 

Alternatively, on the **Create Integration** page, [create a new integration](https://docs.cloud.google.com/application-integration/docs/create-integrations) and then on the _integration editor_ , click pen_spark **Create integration flows with Gemini** to use Gemini.

![image showing Gemini icon in the navigation bar](https://docs.cloud.google.com/static/application-integration/images/gemini-prompt.png)![image showing Gemini icon in the navigation bar](https://docs.cloud.google.com/static/application-integration/images/gemini-prompt.png)

     1. If you want to select a prompt template, select one from the **Sample prompt templates**. Otherwise, enter a prompt for Gemini to generate integrations. To learn how to write better prompts, see [Write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts). 

For example, suppose you added the following prompt: _Create an integration which fetches a jira issue and then creates the zendesk ticket._

     2. Click **Generate**. **Note:** Gemini suggests one or more integration flows that qualifies your prompt: 
        * If you have enabled API Hub and Integration Connectors and met all prerequisites, then recommendations will contain Call REST Endpoint and Connectors tasks.
        * If you have a data mapping requirement in your integration, then Gemini can also suggest a data mapping task. When you confirm the prompt, the data mapping task is replaced by a JavaScript task.

The following diagram shows the **Create an integration with Gemini** pane with the suggestions provided by Gemini:

![Gemini create integration suggestions](https://docs.cloud.google.com/static/application-integration/images/gemini-integration-suggestions.png)![Gemini create integration suggestions](https://docs.cloud.google.com/static/application-integration/images/gemini-integration-suggestions.png)

Use the navigate_before **Previous** and navigate_next **Next** buttons to view the suggestions provided.

     3. If you want to modify the suggested integration name, you can update the **Integration name** field. **Note:** Integration name must be unique in the Google Cloud project.
     4. Select a region for the integration. If your project has a single provisioned region, then the **Region** field is set to that region. **Note:** The **Region** list shows the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     5. If you want to edit the prompt, click **Edit Prompt**.
     6. To accept an integration flow suggestion, click **Confirm**. Application Integration shows the progress of the steps for creating the integration. Integrations created using Gemini replaces any existing integration elements and variables. 

![Gemini create integration loader](https://docs.cloud.google.com/static/application-integration/images/gemini-create-integration-loader.png)![Gemini create integration loader](https://docs.cloud.google.com/static/application-integration/images/gemini-create-integration-loader.png)




## Contextual recommendations

You can use Gemini to provide contextual recommendations for your existing integrations. Gemini can assist you to provide contextually appropriate connector configuration recommendations based on the logical flow of your existing integration. If a connection in your integration has more than 1000 entities, then that connector isn't included in the recommendations by Gemini. For more limitations, see Limitations.

### Configure connector tasks

Gemini can assist you to provide contextually appropriate connector configuration recommendations based on the logical flow of your existing integration. If a connection in your integration has more than 1000 entities, then that connector isn't included in the recommendations by Gemini. For more limitations, see Limitations.

You can configure connector configuration with the Gemini recommended replacements, or you can interact with Gemini (using prompts) and ask for the desired configuration suggestions.

To configure a connector task in your integration using Gemini, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration to open it in the _integration editor_. 
  4. In the navigation bar, click the **New canvas view (Preview)** toggle to the on position. Then, use the canvas to create your integration workflow.
  5. For a connector task, click more_horiz **More actions** and then click **Configure task**. 

A pop-up menu, similar to the following image, appears displaying a set of Gemini recommendations. **Note:** Gemini can recommend connectors task for Call REST endpoint tasks and vice-versa.

![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-connectors-task.png)![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-connectors-task.png)

  6. Gemini automatically recommends one or more replacements or alternatives relevant to the logical flow of your integration. You can use the prompt input to interact with Gemini and fine-tune or re-generated the suggested recommendations if desired. 
  7. Select any one of the recommended replacements or modifications to accept. Gemini configures the selected connector task. 



### Configure Call REST API tasks

If you have API Hub enabled in your project, then Gemini in Application Integration can assist you in providing contextually appropriate [Call REST Endpoint task](https://docs.cloud.google.com/application-integration/docs/configure-call-rest-endpoint-task) and task configuration recommendations based on the logical flow of your existing integration. You can leverage these recommendations to directly replace your existing tasks or modify them without the need of going through any manual configuration process.

You can either directly replace an existing task or a task configuration with the Gemini recommended replacements, or you can interact with Gemini (using prompts) and ask for the desired task suggestions.

After you have met all prerequisites, to replace or modify an existing task in your integration using Gemini, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration to open it in the _integration editor_. 
  4. In the navigation bar, click the **New canvas view (Preview)** toggle to the on position. Then, use the canvas to create your integration workflow.
  5. In the _integration editor_ canvas, select the task that you want to replace or modify.
  6. Click more_horiz **More actions** and then click **Configure task**. 

A pop-up menu, similar to the following image, appears displaying a set of Gemini recommendations. **Note:** Gemini can recommend connectors task for Call REST endpoint tasks and vice-versa.

![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-call-rest-api.png)![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-call-rest-api.png)

  7. Gemini automatically recommends one or more replacements or alternatives relevant to the logical flow of your integration. You can use the prompt input to interact with Gemini and fine-tune or re-generated the suggested recommendations if desired. 
  8. Simply select any one of the recommended replacements or modifications to accept. 

Gemini directly replaces your selected task or modifies it without any additional configurations.




### Add edge conditions and append additional tasks

You can use Gemini to append new tasks and to add [edge conditions](https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions#edge_condition) to your existing integration flow.

To add an edge condition or to append new tasks to your integration using Gemini, perform the following steps:

  1. In the Google Cloud, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration to open it in the _integration editor_. 
  4. In the navigation bar, click the **New canvas view (Preview)** toggle to the on position. Then, use the canvas to create your integration workflow.
  5. In the _integration editor_ , select the [edge](https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions) for which you want to add the edge condition or from which you want to append a new task.
  6. Click more_horiz **More actions** and then click **Create branch**. 

A pop-up menu, similar to the following image, appears prompting you to provide an input.

![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-edge-condition.png)![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-edge-condition.png)

  7. Enter your prompt specifying the edge condition that you want to add or the additional task that you want to append. 

Here is a sample prompt that you can use: 
         
         If order qty>100, send an email

To learn how to write better prompts, see [Write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts). 
  8. Click  pen_spark **Create**.

Gemini automatically inserts the qualified edge conditions and configures the additional tasks from the selected edge in your existing integration.

  9. Click **Confirm** to accept the sugessted insertions and additions. 

If you din't like the suggested inserts or additions, click **Cancel** . 




## Configure JavaScript tasks

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use Gemini to configure [JavaScript tasks](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task) in your integration. Gemini can assist you in providing contextually appropriate JavaScript task configuration recommendations based on the logical flow of your existing integration. You can leverage these recommendations to directly replace your existing tasks or modify them without the need of going through any manual configuration process.

### Add a JavaScript task

The JavaScript task lets you write custom JavaScript code snippets for your integration. To add the code snippets using Gemini, follow these steps:

  1. In the Google Cloud, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. [Create an integration](https://docs.cloud.google.com/application-integration/docs/create-integration) or select an existing integration to open it in the _integration editor_. 
  4. Click and place the **JavaScript** element in the integration editor.
  5. Click the **JavaScript** element on the canvas to view the **JavaScript** task configuration pane.
  6. Click spark **Script with Gemini**. The **Script with Gemini** pane opens. Then, do the following: 
     1. If you want to select a prompt template, select one from the **Sample prompt templates**. Otherwise, enter a prompt for Gemini to generate the JavaScript code. To learn how to write better prompts, see [Write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts). 

Suppose that you want to process a customer order. Your intgeration contains the `customer` and `item` variables. To create an order, you can enter a prompt similar to the following:
            
            Create order using customer and items.
            

![add prompt to generate script using Gemini](https://docs.cloud.google.com/static/application-integration/images/gemini-javascript-add-example.png)![add prompt to generate script using Gemini](https://docs.cloud.google.com/static/application-integration/images/gemini-javascript-add-example.png)

     2. Click **Generate**. 

Gemini suggests one or more code snippets that qualifies your prompt. Use the chevron_left **Previous** and chevron_right **Next** buttons to view the suggestions provided.

     3. To add the suggested code snippet to the **JavaScript** task, click **Confirm**. The code snippet appears in the **JavaScript editor** field.



### Edit a JavaScript task

The JavaScript task lets you write custom JavaScript code snippets for your integration. To add the code snippets using Gemini, follow these steps:

  1. In the Google Cloud, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an integration that contains the **JavaScript** task.. 
  4. Click and place the **JavaScript** element in the integration editor.
  5. Click the **JavaScript** element on the canvas to view the **JavaScript** task configuration pane.
  6. Click **Open Script Editor**. The **JavaScript Task Editor** page appears.
  7. Click spark **Use Gemini to edit and understand the script** > **Edit script**. The **Edit script with Gemini** pane appears. Then, do the following: 
     1. If you want to select a prompt template, select one from the **Sample prompt templates**. Otherwise, enter a prompt for Gemini to generate JavaScript code. To learn how to write better prompts, see [Write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts). 

Suppose that you want to log in the order when the cost of the order is greater than 100. Then, you can enter a prompt similar to the following:
            
            Log in the order when the cost is greater than 100.
                  

![edit prompt to generate script using Gemini](https://docs.cloud.google.com/static/application-integration/images/gemini-javascript-edit-example.png)![edit prompt to generate script using Gemini](https://docs.cloud.google.com/static/application-integration/images/gemini-javascript-edit-example.png)

     2. Click **Generate**. 

Gemini suggests one or more code snipptes that qualifies your prompt. Use the navigate_before **Previous** and navigate_next **Next** buttons to view the suggestions provided.

     3. To add the suggested updates to the code snippet into the **JavaScript** task, click **Confirm**. The updated code snippet appears in the **JavaScript editor** field.



### Understand the JavaScript task

Gemini can help you understand the code snippet in the **JavaScript** task. To do so, follow these steps:

  1. In the integration, click the **JavaScript** element on the canvas to view the **JavaScript** task configuration pane.
  2. In the task configuration pane, click **Open script editor**. The **Script editor** pane appears. Then, do the following: 
     1. Click spark > info_spark **Help me understand**. 

If you want to understand a part of the code, you can select the part of the snippet that you want to understand and click spark > info_spark **Help me understand**. 

The **Gemini** pane appears: 

![help understand script using Gemini](https://docs.cloud.google.com/static/application-integration/images/gemini-javascript-help-understand.png)![help understand script using Gemini](https://docs.cloud.google.com/static/application-integration/images/gemini-javascript-help-understand.png)

     2. In the **Gemini** pane, enter a prompt for Gemini to understand the code snippet. To learn how to write better prompts, see [Write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).



## Generate integration description

The integration description feature available in Gemini in Application Integration provides a description summary of the integration that you've created in your _integration editor_. The integration description summary is generated in plain language and can help you in understanding the overall integration use case, underlying orchestration, and business context which might be difficult to assess due to the structure or complexity of an integration.

To generate an integration description summary of your integration using Gemini, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration to open it in the _integration editor_. 
  4. In the _integration editor_ toolbar, and click info (**Integration summary**). The integration details page appears. 
  5. In the integration details page, click **Help me with description**. 

Gemini parses through the integration in your _integration editor_ and generates a detailed summary description similar to the following image.

![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-description2.png)![image showing Gemini pop-up menu](https://docs.cloud.google.com/static/application-integration/images/gemini-description2.png)

  6. Click **Done** to accept the generated integration description. 

Verify and validate the integration (including the variables) before running it.




## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/gemini/docs/quotas).

## Limitations

Gemini in Application Integration is subject to the following limitations:

  * If the connection in your integration has more than 1000 entities, then that connector isn't included in the recommendations by Gemini.
  * Application Integration supports data residency. Integrations that are built using Gemini support data residency. We don't store any data such as prompts and Gemini responses. Only data in use and transit for generation using Gemini doesn't support data residency.



## Provide feedback

You can get support or provide contextual feedback while using Gemini for building integration. This information helps us improve Gemini.

## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Learn about [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
