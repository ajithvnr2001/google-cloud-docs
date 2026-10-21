---
url: https://docs.cloud.google.com/application-integration/docs/canvas-view/
title: Use the canvas view \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:34.288071+00:00
---

# Use the canvas view  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/canvas-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the canvas view

The canvas view provides an intuitive and user-friendly interface for managing your integration workflows.

## Benefits

The canvas view offers the following benefits:

  * **Improved responsiveness of the canvas interaction:** With the canvas view, you can smoothly move tasks and triggers, making it easier to create complex workflows.
  * **Clearer view of your integration:** The updated visual design provides a clearer view of your integration.
  * **Minimap view:** With the minimap view, you can see the viewport relative to the graph.
  * **Easier to build integrations:** The canvas view provides an intuitive method to add a new child task with a connecting edge or create a new edge to an existing task in your integration. 

![Canvas view add task](https://docs.cloud.google.com/static/application-integration/images/canvas-view-add-task.png)![Canvas view add task](https://docs.cloud.google.com/static/application-integration/images/canvas-view-add-task.png)

  * **Improved discoverability:** In the task configuration pane, you can configure the _Execution strategy for this task_ and the _Execution policy for next tasks_. For more information about these policies, see [Forks and joins](https://docs.cloud.google.com/application-integration/docs/forks-joins).



## Use the canvas view

To use the canvas view, follow these steps:

  1. Open the integration editor.
  2. In the navigation bar, the canvas view will automatically be active. Use the canvas to create your integration workflow. 
  3. To add a task or an edge, click the add_circle **Add new task or edge to the existing task**. 

![Canvas view add task](https://docs.cloud.google.com/static/application-integration/images/canvas-view-add-task-edge.png)![Canvas view add task](https://docs.cloud.google.com/static/application-integration/images/canvas-view-add-task-edge.png)

  4. If you have multiple triggers in an integration, you can use the _Minimap view_ to see the viewport relative to the graph. 

![Canvas view minimap](https://docs.cloud.google.com/static/application-integration/images/canvas-view-minimap.png)![Canvas view minimap](https://docs.cloud.google.com/static/application-integration/images/canvas-view-minimap.png)

  5. To configure an [edge](https://docs.cloud.google.com/application-integration/docs/edge-and-edge-conditions), click the settings **Configure edge**. If you have [enabled Gemini](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini), then a pop-up menu, similar to the following image appears prompting you to provide an input. 

![Canvas view configure edge](https://docs.cloud.google.com/static/application-integration/images/canvas-view-configure-edge.png)![Canvas view configure edge](https://docs.cloud.google.com/static/application-integration/images/canvas-view-configure-edge.png)

  6. To add a [fork](https://docs.cloud.google.com/application-integration/docs/forks-joins), click the task and then in the **Task configuration** pane, expand the **Execution policy for next tasks**. 

![Canvas view add fork](https://docs.cloud.google.com/static/application-integration/images/canvas-view-add-fork.png)![Canvas view add fork](https://docs.cloud.google.com/static/application-integration/images/canvas-view-add-fork.png)

  7. Optionally, to use hotkeys, click a task or a trigger in the canvas view. Then, use hotkeys to update the integration workflow.



## Hotkeys

The following hotkeys are available in the canvas view:

Key  | Function   
---|---  
Ctrl + C  | Copy   
Ctrl + V  | Paste   
Ctrl + Z | Undo  
Shift + Ctrl + Z | Redo  
Delete | Delete selected element  
  
## What's next

  * Learn about the [Integration editor layout](https://docs.cloud.google.com/application-integration/docs/integration-designer-layout). 
  * Learn about [Application Integration concepts](https://docs.cloud.google.com/application-integration/docs/concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
