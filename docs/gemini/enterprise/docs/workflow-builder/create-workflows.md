---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows/
title: Create a workflow \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:59.691187+00:00
---

# Create a workflow  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Create a workflow Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the workflow canvas to create a workflow using either natural prompts or the visual editor.

## Before you begin

Before using this feature, complete the following steps:

  * Ensure that you have a web app with the necessary data sources connected. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store), and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).
  * Ensure that you have enabled the Workflow Builder feature toggle for your web app. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).



## Create a workflow using natural prompts

### App

To create a workflow using natural language prompts, you describe the task you want the agent to perform, and Workflow Builder generates a workflow scaffold for you. For more information, see [Create a workflow using natural language](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-natural-language).

## Create a workflow using the visual editor

### App

To create a workflow using the visual editor, do the following:

  1. Open your Gemini Enterprise web app in a browser.
  2. In the web app navigation menu, click **\+ New agent > Workflow**.
  3. Click **Build manually** to open the visual editor.
  4. A default manual trigger is added to the canvas. Click **Input fields** to enter a required or optional input field that the user can provide when running the workflow.  
  
To change the trigger to another trigger type, click the manual trigger in the canvas and then select another trigger type in the configuration pane.  
  
![Visual editor showing the canvas with a default schedule trigger.](https://docs.cloud.google.com/static/gemini/enterprise/docs/workflow-builder/images/editor-tab-manual-trigger.png)
  5. Click **\+ Add step** to add additional steps to the workflow. For the list of supported steps and their configurations, see [Steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows#steps).
  6. To preview and test your workflow, switch to the **Test** tab and start a test run.
  7. To turn on your workflow and make it live, click **Turn on**.

The workflow is live and starts to execute according to the configured schedule or events, or manually by the user.




## What's next

  * Learn how to [run test simulations for your workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/simulate-workflows).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
