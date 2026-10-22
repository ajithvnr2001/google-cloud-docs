---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version/
title: Versions \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:29.757061+00:00
---

# Versions  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Versions Stay organized with collections  Save and categorize content based on your preferences. 

Versions allow you to save the state of your agent application by creating immutable snapshots in time. You can use versions to memorialize completed work, save progress before making major changes, or roll back to a previous state if needed. The **Versions** pane also provides a detailed change history, listing every modification made to the agent.

## The Versions pane

To open the Versions pane, click the **Versions** button on the right side of the builder page.

The pane displays a record of all changes that have occurred on the agent application, including:

  * A timestamp of the change.
  * The type of action (create, update, delete).
  * The name of the resource that was modified.
  * The email of the user that made the modifications.



Clicking on an individual change shows the details of that change and a diff of the state before and after the modification.

After you create a version, any changes recorded between that version and the previously created version appear grouped underneath it in the Versions pane.

## Create a version

To create a new version:

  1. Open the agent builder.
  2. Click the **Versions** button on the right side of the builder page.
  3. Click **\+ Create version** in the Versions pane.
  4. Enter a name and an optional description for the version.
  5. Click **Create**.



A new version will only be created if there are changes to the agent application configuration.

## View a version

To see the resources that were saved in a specific version:

  1. Open the agent builder.
  2. Click the **Versions** button on the right side of the builder page.
  3. Find the version you want to view.
  4. Click the overflow menu on the right side of the row.
  5. Click **View**.



## Delete a version

To delete a version:

  1. Open the agent builder.
  2. Click the **Versions** button on the right side of the builder page.
  3. Find the version you want to delete.
  4. Click the overflow menu on the right side of the row.
  5. Click **Delete**.
  6. Confirm you want to delete the version.



## Restore a version

To restore or revert to a previous version:

  1. Open the agent builder.
  2. Click the **Versions** button on the right side of the builder page.
  3. Find the version you want to restore.
  4. Click the overflow menu on the right side of the row.
  5. Click **Restore**.
  6. Confirm the restore action.



If there are changes to the current application configuration since the last version was saved, restoring to a previous version first creates an automatic system version (authored by `system@google.com`) to save any unsaved work. This lets you "revert a revert" in case a mistake is made. If there are no changes to the current application configuration, the restore will be a no-op.

## Versions and deployments

You can associate versions with deployments to serve traffic to specific, immutable snapshots of your agent. When a version is attached to a deployment, it displays a **Live** badge in the Versions pane.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
