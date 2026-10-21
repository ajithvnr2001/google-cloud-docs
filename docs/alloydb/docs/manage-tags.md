---
url: https://docs.cloud.google.com/alloydb/docs/manage-tags/
title: Attach and manage tags on AlloyDB resources \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:08.714682+00:00
---

# Attach and manage tags on AlloyDB resources  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/manage-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Attach and manage tags on AlloyDB resources Stay organized with collections  Save and categorize content based on your preferences. 

Resource Manager tags let you organize your AlloyDB for PostgreSQL clusters and backups, conditionally control Identity and Access Management (IAM) access, and track usage in Cloud Billing exports. You can attach, detach, and list tags on AlloyDB resources by using the Google Cloud CLI. Tags attached to a cluster resource are automatically inherited by child resources, such as instances, and can't be overridden on those child resources.

**Note:** Unlike tags, labels on AlloyDB clusters can be attached and managed only by using the AlloyDB API, not the Google Cloud console or the Google Cloud CLI. For more information about how tags work, see [Organize resources using tags](https://docs.cloud.google.com/alloydb/docs/tags) and [Tag inheritance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).

## Before you begin

To get the permissions that you need to view and set tags on AlloyDB resources, ask your administrator to grant you the following IAM roles on your project: 

  * Cloud AlloyDB Admin (`roles/alloydb.admin`): assign to set and view tags 
  * Cloud AlloyDB Viewer (`roles/alloydb.viewer`): assign to view tags 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Work with tags

After you've [created and defined](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) a tag using Resource Manager, you can start using tags with AlloyDB cluster and backup resources. For more information about the Google Cloud CLI commands to use tag bindings, see [gcloud resource-manager tags bindings](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings).

For all of the commands on this page, replace the following:

  * `PARENT_PATH`: The complete path to the backup or cluster resource—for example, `//alloydb.googleapis.com/projects/my-project/locations/us-central1/backups/my-backup`.
  * `TAG_VALUE`: The tag value that you want to attach to your resource—for example, the tag value set as `815471563813/environment/development` includes the following components:

    * `815471563813` is the organization ID or your project ID.

    * `environment` is the tag key.

    * `development` is the tag value.

  * `LOCATION`: The region where your cluster or backup is placed—for example, `us-central1`.




### Attach tags to AlloyDB resources
    
    
    gcloud resource-manager tags bindings create \
    --parent=PARENT_PATH \
    --tag-value=TAG_VALUE \
    --location=LOCATION
    

### Detach tags from AlloyDB resources
    
    
    gcloud resource-manager tags bindings delete \
    --parent=PARENT_PATH \
    --tag-value=TAG_VALUE \
    --location=LOCATION
    

### List tags on AlloyDB resources
    
    
    gcloud resource-manager tags bindings list \
    --parent=PARENT_PATH \
    --location=LOCATION
    

## What's next

  * [Learn more about attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching).
  * [Export Cloud Billing data to BigQuery with resource-level tags](https://docs.cloud.google.com/alloydb/docs/tags#billing-bq-export)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
