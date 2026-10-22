---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions/
title: Manage workflow versions \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:37.469539+00:00
---

# Manage workflow versions  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Manage workflow versions Stay organized with collections  Save and categorize content based on your preferences. 

You can save, compare, delete, and restore versions of your workflow in Workflow Builder.

Versioning lets you track changes across workflow iterations, preserve working configurations, and restore previous versions if needed.

## Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## Save a version

To save a version of your workflow:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow in the flow builder.
  3. Click the drop-down arrow next to the **Turn on** or **Update** button.
  4. Click **Save version**.
  5. In the **Save version** dialog, do one of the following: 
     * Click **Save version only** to save the version without turning it on.
     * Click **Turn on** (or **Update**) to save and make it live.



**Note:** Turning on the workflow or updating it creates a new version of your workflow with your most recent changes and makes it live. Saving a version without making it live preserves your changes but does not update the live workflow.

## View version history

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow in the flow builder.
  3. Click the drop-down arrow next to the **Turn on** or **Update** button.
  4. Click **View version history**.
  5. Browse the list of saved versions. Each version shows the version name and timestamp.
  6. Click a version to view its details or restore it.



## Restore a version

To restore a version of your workflow:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow in the flow builder.
  3. Click the drop-down arrow next to the **Turn on** or **Update** button.
  4. Click **View version history**.
  5. Browse the list of saved versions. Each version shows the version name and timestamp.
  6. Click a version to view its details or restore it.
  7. Click **Restore this version**. The **Restore version?** dialog opens.
  8. Click **Restore**.



The restored version details overwrite the current working draft. This includes the workflow's graph but _not_ the workflow name or description.

## Delete a version

To delete a version of your workflow:

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. Navigate to an existing workflow in the flow builder.
  3. Click the drop-down arrow next to the **Turn on** or **Update** button.
  4. Click **View version history**.
  5. Browse the list of saved versions. Each version shows the version name and timestamp.
  6. Click the **More actions** icon and then click **Delete**. The **Delete version** dialog opens. 
     1. Select the checkbox confirming your request to delete the version.
     2. Click **Delete**.



After the version is deleted, it can't be restored and the data associated with the version is not retained.

**Note:** Deleting a version removes the associated workflow graph for that version's runs. Use caution when deleting versions.

## What's next

  * Learn how to [edit a workflow with natural language](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows).
  * Learn how to [view workflow runs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs).
  * Learn how to [create a workflow with natural language](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-natural-language).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
