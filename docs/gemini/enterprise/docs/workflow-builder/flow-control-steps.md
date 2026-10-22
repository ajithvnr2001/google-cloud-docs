---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps/
title: Use flow control steps \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:37.874145+00:00
---

# Use flow control steps  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Use flow control steps Stay organized with collections  Save and categorize content based on your preferences. 

You can add flow control steps to your agent workflow to direct execution based on conditions, filter data, or loop over lists of items.

Flow control steps let you build complex workflows with branching logic, scoped data processing, and iterative operations.

## Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## Flow control step types

Workflow Builder provides three flow control step types:

  * **Condition** : Branch your workflow into different paths based on criteria you define. Use conditions to route execution to different steps depending on data values or step outputs.
  * **Filter** : Filter a list of data to process only items that match your criteria. Use filters to narrow results from a search or previous step before passing data to downstream steps.
  * **Loop** : Iterate over a list of items and run one or more steps for each item. Use loops to process multiple records, such as each email in a search result or each ticket in a project.



## Add a condition step

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing agent or create a new agent.
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, click **Flow control** to expand the section.
  5. Click **Condition**.
  6. The condition step is added to your workflow and its configuration panel opens on the right.
  7. Configure the condition criteria that determines which branch the workflow follows.
  8. Add steps to each branch of the condition.



## Add a filter step

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing agent or create a new agent.
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, click **Flow control** to expand the section.
  5. Click **Filter**.
  6. The filter step is added to your workflow and its configuration panel opens on the right.
  7. Configure the filter criteria to specify which items should pass through to downstream steps.



## Add a loop step

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing agent or create a new agent.
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, click **Flow control** to expand the section.
  5. Click **Loop**.
  6. The loop step is added to your workflow and its configuration panel opens on the right.
  7. Configure the list of items to iterate over.
  8. Add one or more steps inside the loop that run for each item in the list.



## What's next

  * Learn how to [configure Agent node connectors and actions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions).
  * Learn how to [search with filters](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/search-with-filters).
  * Learn how to [use human-in-the-loop steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-hitl-steps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
