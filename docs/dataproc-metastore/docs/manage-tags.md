---
url: https://docs.cloud.google.com/dataproc-metastore/docs/manage-tags/
title: Attach and manage tags on Dataproc Metastore resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:39.971490+00:00
---

# Attach and manage tags on Dataproc Metastore resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/manage-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Attach and manage tags on Dataproc Metastore resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to attach, detach, and list tags on Dataproc Metastore resources. For an overview of tags on Dataproc Metastore, see [Organize Dataproc Metastore resources using tags](https://docs.cloud.google.com/dataproc-metastore/docs/tags).

## Before you begin

To get the permissions that you need to view and set tags on Dataproc Metastore resources, ask your administrator to grant you the following IAM roles on your project: 

  * Dataproc Metastore Editor (`roles/metastore.editor`): assign to set and view tags 
  * Dataproc Metastore Viewer (`roles/metastore.viewer`): assign to view tags 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Work with tags

After you've [created and defined](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) a tag using Resource Manager, you can start using tags with Dataproc Metastore service and federation resources. For more information about the Google Cloud CLI commands to use tag bindings, see [gcloud resource-manager tags bindings](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings).

For all of the commands on this page, replace the following:

  * `PARENT_PATH`: The complete path to the service or federation resource—for example, `//metastore.googleapis.com/projects/my-project/locations/us-central1/services/my-service`.
  * `TAG_VALUE`: The tag value that you want to attach to your resource—for example, the tag value set as `815471563813/environment/development` includes the following components:

    * `815471563813` is the organization ID or your project ID.

    * `environment` is the tag key.

    * `development` is the tag value.

  * `LOCATION`: The region where your service or federation is located—for example, `us-central1`.




### Attach tags to Dataproc Metastore resources
    
    
    gcloud resource-manager tags bindings create \
    --parent=PARENT_PATH \
    --tag-value=TAG_VALUE \
    --location=LOCATION
    

### Detach tags from Dataproc Metastore resources
    
    
    gcloud resource-manager tags bindings delete \
    --parent=PARENT_PATH \
    --tag-value=TAG_VALUE \
    --location=LOCATION
    

### List tags on Dataproc Metastore resources
    
    
    gcloud resource-manager tags bindings list \
    --parent=PARENT_PATH \
    --location=LOCATION
    

## What's next

  * [Learn more about attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
