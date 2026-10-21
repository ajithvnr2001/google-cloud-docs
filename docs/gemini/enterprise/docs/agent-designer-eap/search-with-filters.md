---
url: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/search-with-filters/
title: Search with filters \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:17:29.316383+00:00
---

# Search with filters  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/search-with-filters/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)



Send feedback 

#  Search with filters Stay organized with collections  Save and categorize content based on your preferences. 

You can add filters to search steps in your workflow to scope results from connectors.

Filters let you target specific data, such as emails matching certain criteria or files in a particular folder. You can describe filters in natural language or edit them manually.

## Before you begin

Before using this feature, complete the following steps:

  * Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * Ensure that the connector you want to search is connected as a data store in your Gemini Enterprise app. For more information, see [Connect a third-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).



## Add a search step with filters

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow or create a workflow.
  3. In the flow builder, click **Add step**.
  4. In the **Add step** panel, go to the **Apps** section.
  5. Click the connector name (for example, **Gmail**) and then click a search action (for example, **Find message(s)**).

The search step is added to your workflow, and its configuration panel opens.

  6. In the **Filter messages** field, describe the filter you want to apply in natural language. For example: "Emails from the last 24 hours with attachments" or "Messages with the label 'urgent'."

  7. Click **+** or the microphone button to submit your filter description.




## Edit filters manually

### App

  1. In the search step configuration panel, click **Edit manually** for the **Filter messages** field.
  2. Configure the filter criteria using the manual filter fields.

**Note:** If you describe a filter that includes an unsupported operation, Gemini Enterprise informs you which operations are not supported.

## What's next

  * Learn how to [configure Agent node connectors and actions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions).
  * Learn how to [use flow control steps](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps).
  * Learn how to [view workflow runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
