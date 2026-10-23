---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/configure-event-trigger/
title: Set up event triggers \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:55.934982+00:00
---

# Set up event triggers  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/configure-event-trigger/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Set up event triggers Stay organized with collections  Save and categorize content based on your preferences. 

You can configure your workflow to run automatically when data changes in a connector.

Event triggers use polling to detect changes such as new emails, updated calendar events, or new files in a connected data store. When a change is detected, the configured workflow runs.

**Note:** There might be a delay of 5-10 minutes for an event to be received and trigger a workflow. The specific ordering of events is not guaranteed. 

## Before you begin

Before using this feature, complete the following steps:

  * Ensure that you have a web app with the necessary data sources connected. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).
  * Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * Ensure that the connector you want to use as a trigger source is connected as a data store in your Gemini Enterprise app. For more information, see [Connect a third-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).



## Supported connectors

The following connectors support event triggers:

  * Confluence
  * Gmail
  * Google Calendar
  * Google Drive
  * Jira Cloud
  * OneDrive
  * Outlook
  * ServiceNow
  * SharePoint
  * Teams

**Note:** Some connectors require you to click **Connect** before you can select events. Connectors that are already connected to your Gemini Enterprise app display a chevron icon and can be selected immediately.

## Configure an event trigger

### App

  1. Open your Gemini Enterprise web app in a browser.
  2. In the navigation menu, click **Agents**.
  3. Click **Create agent**.
  4. Click **Start manually**.
  5. On the **What should trigger your agent?** page, click **App event**.
  6. In the details panel, under **App event - Choose an app to start with** , browse or search for the connector you want to use. Click the connector name to select it.
  7. Select the event that triggers your workflow. Events are organized by category.
  8. After selecting an event, the trigger is added to the top of your workflow in the flow builder.
  9. Click **Add step** to add workflow steps that run when the trigger fires.



## Test an agent with event triggers

Before turning on your workflow, you can test its functionality by previewing trigger events and running simulations with sample event data.

### Preview event trigger results

### App

  1. In the workflow canvas, click the event trigger node at the top of your workflow.
  2. In the right-side configuration panel, click **Preview results**.
  3. Gemini Enterprise fetches recent events from the connector. Each item displays the event title and timestamp. Google Calendar preview results are based on recently updated events and might not reflect recent events.
  4. You can click a preview result to see the details of the event.



### Test your agent workflow

### App

  1. Switch to the **Test** tab in the workflow canvas.
  2. In the trigger input section, select a sample event from the list of previewed events using the **Select input** selector.
  3. Click **Start manually** to run the workflow simulation using the sample event data.
  4. When the run finishes, expand the simulation summary to inspect the outputs and verify that each step processed the trigger payload correctly.



## Manage event triggers

You can manage event triggers by editing their configuration, turning workflows on or off, or deleting triggers.

NOTE: Events can take up to 10 minutes to appear.

  * **Edit an event trigger:** Open the agent in edit mode, click the trigger node on the canvas, and update its settings or filter criteria in the configuration panel.
  * **Turn on an event trigger:** To activate the trigger and begin polling for events, turn on the workflows. For more information, see [Turn a workflow on or off](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/publish-workflows).
  * **Turn off an event trigger:** To pause or deactivate event polling, turn off the workflow.



## Known issues and limitations

These are known issues and limitations when working with event triggers.

  * **Connector unlinking:** When an administrator unlinks a connector from the engine or app, the event trigger is paused automatically. However, no notification is sent to the user, and users cannot view paused agents in their gallery.
  * **Failed session retries:** If an agent execution fails due to errors fetching data from an associated connector in an event trigger, a session is created with a failed status. Manual retries on failed sessions are not currently supported.
  * **Filters:** Always add filters to your event triggers to ensure timely agent execution on most important events.
  * **Gmail triggers:**
    * Agent initiation might be slower for users with a high volume of emails.
    * Gmail supports two triggers: **When an email is sent** and **When an email is received**. If you want to trigger an agent by sending yourself an email, use **When an email is sent**. If you use **When an email is received** , that will not trigger the agent.



For a full list of system constraints, see [Workflow Builder quotas and limits](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits).

## What's next

  * Learn how to [configure Agent node connectors and actions](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions).
  * Learn how to [search with filters](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/search-with-filters).
  * Learn how to [view agent execution logs](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs).
  * Learn how to [turn a workflow on or off](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/publish-workflows).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
