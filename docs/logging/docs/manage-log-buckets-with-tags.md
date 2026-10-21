---
url: https://docs.cloud.google.com/logging/docs/manage-log-buckets-with-tags/
title: Use tags to manage access to log buckets \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:40.311724+00:00
---

# Use tags to manage access to log buckets  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/manage-log-buckets-with-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Use tags to manage access to log buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use Tags to manage your Cloud Logging log buckets. Tags, which are created at the organization- or project-level, let you annotate your resources. You can also [conditionally grant Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/conditions-overview) or [conditionally deny IAM permissions](https://docs.cloud.google.com/iam/docs/deny-overview) based on whether a resource has a specific tag. For information about tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

For example, if you use [BigQuery to analyze your Cloud Billing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags), then you might attach the `project:production` tag to log buckets that store log data from production resources, and you might attach the `project:development` tag to log buckets that store log data from development resources. Then, you can [query Cloud Billing data with tags](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-with-tags) and see a breakdown of your costs between development and production.

Tags can be explicitly attached to log buckets, or inherited from their parent organization, folders, and projects.

## Before you begin

**Note:** If you plan to use custom roles instead of predefined roles, then review the section of this document titled Custom roles and role grants with IAM conditions.

To get started with managing your log buckets by using tags, do the following:

  1. Ensure that you've created a tag and configured its values. You use [Resource Manager](https://docs.cloud.google.com/resource-manager/docs) to manage tag definitions. For information about how to create and manage tags, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing). 
  2. To get the permissions that you need to manage your log buckets by using tags, ask your administrator to grant you the following IAM roles on your project or organization: 

     * [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)
     * [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage your log buckets by using tags. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage your log buckets by using tags:

     * Add or remove tags to log buckets: 
       * `resourcemanager.tagValues.{get,list}`
       * `resourcemanager.tagKeys.{get,list}`
       * `resourcemanager.projects.get`
       * `logging.buckets.createTagbinding`
       * `logging.buckets.deleteTagBinding`
     * View tags that are attached to log buckets: 
       * `resourcemanager.tagValues.{get,list}`
       * `resourcemanager.tagKeys.{get,list}`
       * `logging.buckets.listTagBindings`
       * `logging.buckets.listEffectiveTags`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. To get the permission that you need to manage log buckets, ask your administrator to grant you the [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `logging.buckets.list` permission, which is required to manage log buckets. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Attach tags to a log bucket

To attach a tag to a log bucket, do the following:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate the log bucket to attach a tag to.

  3. On the log bucket, click **More** _more_vert_ , and then click **Edit tags**.

  4. In the dialog, in the **Direct tags** section, locate the tag by selecting the resource in which the tag was created. For example, to use a tag that was created at the project-level, choose **Select current project** as the scope.

You can also manually search for the project, organization, or tag ID by selecting the **Manual Entry** option.

  5. Select the appropriate key-value pair, then click **Save**.

  6. A dialog confirming your changes appears. Click **Confirm** to finalize your changes.




###  gcloud 

To attach a tag to a log bucket, create a tag binding by running the [`gcloud resource-manager tags bindings create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create) command:
    
    
    gcloud resource-manager tags bindings create \
    --tag-value=TAG_VALUE_ID \
    --parent=BUCKET_NAME \
    --location=LOCATION

In the previous command, make the following replacements:

  * TAG_VALUE_ID: The permanent ID or the namespaced name of the tag value. For example, `tagValues/4567890123`. For more information about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).

  * BUCKET_NAME: The name of the log bucket. For example, `//logging.googleapis.com/projects/BUCKET_PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID`.

  * LOCATION: The location of the log bucket.




###  API 

To attach a tag to a log bucket, use the [`tagBindings.create`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/create) method.

###  Terraform 

To attach a tag to a log bucket by using Terraform, do one of the following:

  * For log buckets in the `global` location, create a tag binding resource by using [`google_tags_tag_binding`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_binding)
  * For regional log buckets, create a tag binding resource by using [`google_tags_location_tag_binding`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_tags_location_tag_binding).



Then, run `terraform apply` to apply your changes.

## View tags attached to a log bucket

To view the tags attached to a log bucket, do the following:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate the log bucket whose tags you want to view.

In the **Tags** column, a tag associated with the log bucket is listed. To view all tags associated with the log bucket, click the _arrow_drop_down_ **More** button to expand the list of tags.




###  gcloud 

Run the [`gcloud resource-manager tags bindings list`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/list) command:
    
    
    gcloud resource-manager tags bindings list \
    --parent=BUCKET_NAME \
    --location=LOCATION

In the previous command, make the following replacements:

  * BUCKET_NAME: The name of the log bucket. For example, `//logging.googleapis.com/projects/BUCKET_PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID`.

  * LOCATION: The location of the log bucket.




Optional: To view tags inherited by the log bucket, add the `--effective` flag, Adding this flag returns a response similar to the following:
    
    
    namespacedTagKey: 961309089256/environment
    namespacedTagValue: 961309089256/environment/production
    tagKey: tagKeys/417628178507
    tagValue: tagValues/247197504380
    inherited: true
    

If all tags are explicitly attached to the log bucket and no tags are inherited, then the `inherited` field is false and is omitted.

###  API 

To get a list of tag bindings for a bucket, use the [`tagBindings.list`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/list) method.

###  Terraform 

You can use Terraform to attach a tag to a log bucket. However, you can't use Terraform to list the tags.

## Remove tags on a log bucket

To remove the tags attached to a log bucket, you must delete the tag binding attached to the log bucket. To delete a tag, you must remove the tags from all attached resources.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate the log bucket whose tag you want to remove.

  3. On the log bucket, click **More** _more_vert_ , and then click **Edit tags**.

  4. In the dialog, hold the pointer over the tag to remove, and click delete **Delete item**. Click **Save** to save your changes.

  5. A dialog confirming your changes appears. Click **Confirm** to finalize your changes.




###  gcloud 

Run the [`gcloud resource-manager tags bindings delete`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete) command:
    
    
    gcloud resource-manager tags bindings delete \
    --tag-value=TAG_VALUE_ID \
    --parent=BUCKET_NAME \
    --location=LOCATION

In the previous command, make the following replacements:

  * TAG_VALUE_ID: The permanent ID or the namespaced name of the tag value. For example, `tagValues/4567890123`. For more information about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).

  * BUCKET_NAME: The name of the log bucket. For example, `//logging.googleapis.com/projects/BUCKET_PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID`.

  * LOCATION: The location of the log bucket.




###  API 

To remove a tag on a log bucket, use the [`tagBindings.delete`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/delete) method.

###  Terraform 

To remove a tag on a log bucket by using Terraform, delete the tag binding resource in your configuration, then run `terraform apply` to apply your changes.

## Limitations

  * You can't use IAM role grants to control which log buckets a principal sees when they list the log buckets in a Google Cloud project. A principal will see either a complete list or an empty list. However, you can use IAM role grants with IAM conditions to restrict the actions that a principal can take on a log bucket. For example, you can restrict whether a principal can delete a specific log bucket.

  * If you use Cloud Billing data exports with BigQuery, then tags might take up to an hour to be used in the export. If a tag has been added or removed within an hour, or if the log bucket has existed for less than an hour, then it might not appear in the export.




## Custom roles and role grants with IAM conditions

If you plan to use custom IAM roles and if you plan to attach IAM conditions to the role grants, then you might need to create multiple custom roles. Some IAM permissions are invalidated when an IAM condition is attached to a role grant.

For Cloud Logging, the following IAM permissions are invalidated when a role grant contains an IAM condition:

  * `logging.buckets.list`
  * `logging.buckets.create`



Therefore, you might need to create one role with the `list` and `create` permissions and another role that contains other bucket-specific permissions. For example, you might create a role that contains the `logging.buckets.delete` and `logging.buckets.update` permissions.

When you grant the role that contains the `list` and `create` permissions, don't attach an IAM condition to the role grant. When you grant the role that contains the `delete` and `update` permissions, then you can add an IAM condition that restricts the grant to resources with a specific tag.

## What's next

  * Learn how to set an [organization policy with Tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).

  * For information about use tags in Cloud Billing data exports, see the [Cloud Billing data exports documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
