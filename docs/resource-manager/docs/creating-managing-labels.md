---
url: https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels/
title: Create and update labels for projects \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:21.297345+00:00
---

# Create and update labels for projects  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Create and update labels for projects Stay organized with collections  Save and categorize content based on your preferences. 

This document provides details on how to create and update labels for projects using gcloud CLI, the Cloud Resource Manager API, and the Google Cloud console.

**Note:** Resource Manager labels apply to **projects only** (folders and organizations don't support labels). Labels attached to a project don't automatically propagate to child resources within the project. To apply or update labels on specific service resources (such as Compute Engine instances or Cloud Storage buckets), see the resource's documentation or [Services that support labels](https://docs.cloud.google.com/resource-manager/docs/labels-supported-services).**Note:** Pub/Sub supports labels for topic and subscription throughput billing, but egress billing SKUs don't support labels.

## Create labels for projects

### Console

To add labels to a single project:

  1. Open the **Labels** page in the Google Cloud console.

[Open the Labels page](https://console.cloud.google.com/projectselector/iam-admin/labels)

  2. Select your project from the **Select a project** drop-down.

  3. To add a new label entry, click **\+ Add label** and enter a label key and value for each label you want to add.

  4. When you're finished adding labels, click **Save**.




To add labels for more than one project at the same time:

  1. Open the **Manage resources** page in the Google Cloud console.

[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. On the **Manage resources** page, select the projects for which you want to add labels.

  3. In the info panel, in the **Labels** tab, click **\+ Add label** and enter a label key and value for each label you want to add.

  4. When you're finished adding labels, click **Save**.




After you add labels, you can filter projects by typing a label key or value in the filter box above the projects list. The filter box will suggest keys and values so you can preview results.

### gcloud

To create a **new** project with labels using gcloud CLI, use the `gcloud projects create` command with the `--labels` flag:
    
    
    gcloud projects create PROJECT_ID \
        --labels=KEY1=VALUE1,KEY2=VALUE2
    

To add labels to an **existing** project, use the `gcloud projects update` command with the `--update-labels` flag:
    
    
    gcloud projects update PROJECT_ID \
        --update-labels=KEY1=VALUE1,KEY2=VALUE2
    

Where:

  * `PROJECT_ID` is the ID of the project you want to create or update.
  * `KEY1=VALUE1` is a key-value pair for the label you want to add.



### REST

To create a **new** project with a label, include the `labels` field when you make a `POST` request to the `projects.create` method:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "projectId": "PROJECT_ID",
        "displayName": "PROJECT_NAME",
        "labels": {
          "environment": "development"
        }
      }' \
      "https://cloudresourcemanager.googleapis.com/v3/projects"
    

To add labels to an **existing** project, use the `projects.patch` method:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "labels": {
          "environment": "development"
        }
      }' \
      "https://cloudresourcemanager.googleapis.com/v3/projects/PROJECT_ID?updateMask=labels"
    

## Update labels for projects

### Console

To update labels for a single project:

  1. Open the **Labels** page in the Google Cloud console.

[Open the Labels page](https://console.cloud.google.com/projectselector/iam-admin/labels)

  2. Select your project from the **Select a project** drop-down.

  3. Update the labels for your project:

     1. To edit a label, click the value that you want to edit, then make your desired changes.
     2. To delete a label, hold the pointer over the key or value, then click delete .
  4. When you're finished updating labels, click **Save**.




To update labels for more than one project at the same time:

  1. Open the **Manage resources** page in the Google Cloud console.

[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. On the **Manage resources** page, select the projects for which you want to update labels.

  3. In the info panel, click the **Labels** tab and update labels for the selected projects:

     1. To edit a label, click the value that you want to edit, then make your desired changes.
     2. To delete a label, hold the pointer over the key or value, then click delete .
  4. When you're finished updating labels, click **Save**.




### gcloud

To update labels for a project using gcloud CLI, use the `gcloud projects update` command with the `--update-labels`, `--remove-labels`, or `--clear-labels` flag.

To add or update labels:
    
    
    gcloud projects update PROJECT_ID \
        --update-labels=KEY1=VALUE1,KEY2=VALUE2
    

To remove specific labels:
    
    
    gcloud projects update PROJECT_ID \
        --remove-labels=KEY1,KEY2
    

To remove all labels from a project:
    
    
    gcloud projects update PROJECT_ID \
        --clear-labels
    

### REST

To update a project's labels using the API, send a `PATCH` request to the `projects.patch` method:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "labels": {
          "color": "red"
        }
      }' \
      "https://cloudresourcemanager.googleapis.com/v3/projects/PROJECT_ID?updateMask=labels"
    

Where `PROJECT_ID` is the ID of the project you want to update.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
