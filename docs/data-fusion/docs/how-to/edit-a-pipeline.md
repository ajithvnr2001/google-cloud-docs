---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/
title: Edit pipelines \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:34:32.208413+00:00
---

# Edit pipelines  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/edit-a-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Edit pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to edit deployed batch pipelines in Cloud Data Fusion.

Editing a pipeline lets you do the following:

  * Incrementally add features to a deployed pipeline without creating duplicates. For example, you can add, remove, or modify plugins, then redeploy the pipeline. Editing a pipeline creates a new version of the same pipeline, which prevents a proliferation of pipelines, allowing for better organization. Duplicating a pipeline creates a new pipeline with a different name.
  * Maintain a history of the edited versions.
  * View and restore old versions of a pipeline.
  * Edit any part of the pipeline, such as the pipeline structure, configuration, metadata, preferences, and comments.
  * Export an edited JSON file for a deployed pipeline.



When you edit the pipeline, Cloud Data Fusion creates a new draft, which becomes the _latest version_. The name of the pipeline remains the same. You develop the pipeline iteratively, without creating duplicate pipelines with unique names. The latest version retains the triggers, pipeline configurations, runtime arguments, metadata, comments, and schedules from the previous version. The latest version is the active version of the pipeline: it can be run or scheduled to run.

## Before you begin

  * Cloud Data Fusion supports editing deployed batch pipelines in version 6.9.1 and later. To upgrade to the latest version, see [Upgrade your Cloud Data Fusion environment](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).
  * Cloud Data Fusion doesn't support editing deployed real-time pipelines or replication jobs.



## Edit the pipeline

To edit a deployed batch pipeline in Cloud Data Fusion, follow these steps:

  1. Go to your instance: 
     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **List > Deployed**.
  3. Go to the pipeline that you want to edit and click more_vert **More > Edit**.

A new draft of the pipeline appears on the **Studio** page.

  4. Edit your pipeline. For example, add a new analytics node, or edit the properties of a source.

  5. Optional: To finish editing the pipeline later, click **Save**.

  6. After you finish editing the pipeline, click **Deploy**.

  7. In the **Enter change summary** dialog, enter a description of the changes you made to the pipeline and click **Deploy**. The deployed pipeline opens on the **Pipeline** page.


**Note:** You can also edit the pipeline from the **Pipeline** page by clicking **Actions > Edit**.

## View or restore a previous version of the pipeline

To view or deploy a previous version of a batch pipeline, follow these steps:

  1. Open your instance in the Cloud Data Fusion interface.
  2. Click **List > Deployed**.
  3. Select a pipeline. The pipeline appears on the **Pipeline** page.
  4. Click history **History**.

A version history list appears.

  5. Optional: To view a previous version of a pipeline, click **View**.

  6. Optional: To restore an older version of the pipeline to the latest version, click **Restore**.

Cloud Data Fusion creates a new version of the pipeline and opens it on the **Pipeline** page. It's now the latest version.




## Export an edited version of a deployed pipeline

You can export the edited version of a deployed pipeline as a JSON file to share with other developers, add it to version control, or move it from a development environment to a test or production environment. For example, after you edit a pipeline during development and debugging phases, you export the JSON file, and then import and deploy it in a production environment.

**Note:** Cloud Data Fusion exports pipelines in the `Draft` state.

### Export the latest version

To export the latest version of the pipeline, follow these steps:

  1. Open your instance in the Cloud Data Fusion interface.
  2. Click **List > Deployed**.
  3. Select the pipeline that you want to export and click more_vert **More > Export**.

A JSON file with the pipeline configurations from the latest version is saved locally.




### Export a previous version

To export previous versions of the pipeline, follow these steps:

  1. Open your instance in the Cloud Data Fusion interface.
  2. Click **List > Deployed**.
  3. Select the pipeline. The latest version opens on the **Pipelines** page.
  4. Click history **History**.
  5. Select the pipeline version that you want to export and click **View > Actions > Export**.



## Import an edited version of a deployed pipeline

All pipelines are exported in the `Draft` state. Edited versions of a deployed pipeline are also imported in the `Draft` state. For more information, see [Import a pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines#import).

## Delete an edited version of a pipeline

When you delete the latest version of a deployed pipeline, all versions of the deployed pipeline are deleted. Draft versions aren't deleted.

Instead, the draft pipeline version has the **Orphaned** status. To resolve this status, deploy the draft pipeline. Cloud Data Fusion creates a new pipeline, which is the latest version.

## Statuses for edited pipelines

When you edit pipelines, the following statuses might appear on the **Pipeline Drafts** page.

Status | Description  
---|---  
**In-Progress** | You have saved edits to the pipeline.  
**Orphaned** | The latest version of the pipeline was deleted and associated drafts no longer belong to an existing pipeline. You might see this status if someone deletes the pipeline with the following endpoint: `DELETE/v3/namespaces/NAMESPACE_ID/apps/APP_ID `.   
**Obsolete** | A newer version has been deployed while edits have been in progress. You might see this status if another developer deploys the pipeline before you finish editing. This is the same as **Draft Out of Date** that appears on the Pipeline page.  
  
When you edit pipelines, the following statuses might appear on the **Studio** page.

Status | Description  
---|---  
Editing in progress | You're editing a draft pipeline.  
Orphaned draft | Someone deployed a newer version while you were editing the pipeline.   
  
## What's next

  * Learn how to [export and import pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
