---
url: https://docs.cloud.google.com/application-integration/docs/integration-designer-layout/
title: Explore the Integration editor layout \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:34.012535+00:00
---

# Explore the Integration editor layout  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/integration-designer-layout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Explore the Integration editor layout

The _Integration editor_ is a drag-and-drop interface that lets you design and develop your entire integration flow with little or no code. You can create, modify, and run all your integrations in the _Integration editor_. Overall, you can think of the _Integration editor_ as a unified workspace for managing your integration. 

Application Integration provides out-of-the-box [triggers](https://docs.cloud.google.com/application-integration/docs/trigger-overview) and [tasks](https://docs.cloud.google.com/application-integration/docs/task-overview) to further assist you in rapid development of your integration. Every task or trigger element is connected using an [edge](https://docs.cloud.google.com/application-integration/docs/edge-overview) along with its respective [fork and join](https://docs.cloud.google.com/application-integration/docs/forks-joins). Edges also indicate the flow of control from one task/trigger to another. For information on specifying conditions for edges and tasks, see [Edge conditions](https://docs.cloud.google.com/application-integration/docs/edge-overview#edge_condition). 

## Open integration editor

To open your integration in the _Integration editor_ , do the following: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select an existing integration or create a new integration by clicking **Create integration**.

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** dialog.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Click **Create**. The newly created integration opens in the _integration editor_.




## Explore integration editor layout

The following figure shows a sample layout of the _Integration editor_.

![Integrations designer layout](https://docs.cloud.google.com/static/application-integration/images/integrations_editor_layout.png)![Integrations editor layout](https://docs.cloud.google.com/static/application-integration/images/integrations_editor_layout.png)

The following table describes the different sections that comprise the integration editor:

Section  | Description   
---|---  
Toolbar Show layout ![Integrations designer toolbar](https://docs.cloud.google.com/static/application-integration/images/toolbar.png) |  The designer toolbar displays the following information about your integration: 

  * Name of the integration.
  * Last edit timestamp.
  * Current [version](https://docs.cloud.google.com/application-integration/docs/integration-versions) of the integration.
  * [Local logging](https://docs.cloud.google.com/application-integration/docs/local-logging) status. 

To view a summary of the whole integration in one place, click  info . To perform actions such as [deleting](https://docs.cloud.google.com/application-integration/docs/delete-integrations) an integration, [cloning](https://docs.cloud.google.com/application-integration/docs/clone-integrations) an integration, or [downloading and uploading](https://docs.cloud.google.com/application-integration/docs/upload-download-integrations) an integration, and [ viewing the OpenAPI Specification](https://docs.cloud.google.com/application-integration/docs/view-openapi-spec) of an integration, click the  more_vert  (Actions menu) in the toolbar.   
Navigation bar  Show layout ![Integrations designer nav bar](https://docs.cloud.google.com/static/application-integration/images/navigationbar.png) | The designer navigation bar lets you perform the following actions: 

  * Add [triggers](https://docs.cloud.google.com/application-integration/docs/triggers) and [tasks](https://docs.cloud.google.com/application-integration/docs/tasks) to your integration.
  * Undo and redo.
  * Clean up and auto-orient the integration flow in the designer canvas.
  * Canvas  zoom_in  zoom-in and  zoom_out  zoom-out.
  * Create integration flow with Gemini pen_spark
  * vertical_align_top  [Publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) and  play_circle  [test](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) integration.
  * Open [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs) to view the available connections in the region.
  * View integration [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs).
  * View [monitoring dashboard](https://docs.cloud.google.com/application-integration/docs/monitoring-dashboard). 

  
Variables pane Show layout ![Integrations designer var](https://docs.cloud.google.com/static/application-integration/images/varpane.png) |  The **Variables** panes lists all the integration variables and task variables available in the integration. It also displays a count of the total variable references within the integration.  To perform actions such as deleting or duplicating a variable, click  more_vert  (Actions menu) next to the respective variable.  For more information about variable, see [Variables](https://docs.cloud.google.com/application-integration/docs/variables).  
Designer canvas Show layout ![Integrations designer canvas](https://docs.cloud.google.com/static/application-integration/images/canvas.png) | The designer canvas is the backdrop on which you can design and develop your integration flow.   
Configuration pane  Show layout ![Integrations designer config](https://docs.cloud.google.com/static/application-integration/images/configpane.png) |  The configuration pane displays the configuration settings for each of the triggers and tasks that are added in your designer canvas. For information about how to configure a trigger or task, see [Triggers and tasks](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).   
  
## What's next

  * Start a [quickstart](https://docs.cloud.google.com/application-integration/docs/quickstarts).
  * Learn about the [canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view).
  * Get a deeper understanding of the fundamental Application Integration [concepts](https://docs.cloud.google.com/application-integration/docs/concepts).
  * Learn how to add and configure the available [triggers and tasks](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
