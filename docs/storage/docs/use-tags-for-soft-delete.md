---
url: https://docs.cloud.google.com/storage/docs/use-tags-for-soft-delete/
title: Use tags to set a default soft delete retention duration for new buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:22.639347+00:00
---

# Use tags to set a default soft delete retention duration for new buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/use-tags-for-soft-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use tags to set a default soft delete retention duration for new buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use tags to set a default soft delete retention duration.

## Overview

When using [tags](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags), you can set a default [soft delete retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) that gets applied to new buckets you create with soft delete enabled. Tags let you set key-value pairs that specify the amount of days you want Cloud Storage to retain soft-deleted data, giving you greater control over how long your data is retained. You can also use tags to disable soft delete by default.

## Considerations

  * For a tag to take effect, you must create the tag as a child of the organization you want to set a default retention duration for, after which it can be attached to a project, [Resource Manager folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or organization.

  * When you use tags to customize a default soft delete retention duration on a resource, existing buckets in the resource don't automatically inherit the new soft delete retention duration. To change the soft delete retention duration on an existing bucket, you must [edit the bucket's soft delete policy](https://docs.cloud.google.com/storage/docs/use-soft-delete#manage-policy).

  * Settings that are implemented using tags are editable, meaning you can edit the soft delete retention duration that the tag sets during or after bucket creation.

  * If you set a [`storage.softDeletePolicySeconds` organization policy constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#soft-delete-retention) which restricts the soft delete retention duration on newly created buckets to only a set of values allowed by your organization and also want to use tags to set a default soft delete retention duration, you can only set the default retention duration to a value allowed by your organization policy constraint. All other values result in an error.

  * If you delete a tag binding that was previously set on a child resource of your organization, the child resource inherits the organization's default soft delete retention duration. If you delete the organization's tag binding, your resource inherits the soft delete system default retention duration of seven days. To learn more about how tag values are inherited, see [Tag inheritance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).

  * Creating or deleting a tag binding usually takes less than one day to take effect.




## Required roles

The following permissions are required to perform the actions described in this page.

  * To create a default soft delete retention duration tag and tag values, you need the Tag Administrator role (`roles/resourcemanager.tagAdmin`).

  * To attach or remove a default soft delete retention duration tag from a resource, you need the Tag User role (`roles/resourcemanager.tagUser`), or another role with equivalent permissions, on both the tag value and the resources that you are attaching the tag value to.




To see the permissions that are required to perform the actions described in this page, expand the **Required permissions** section:

#### Required permissions

  * Permissions required to create a default soft delete retention duration tag and tag values:
    * `resourcemanager.tagKeys.create`
    * `resourcemanager.tagValues.create`


  * Permissions required for attaching or removing a default soft delete retention duration tag from a resource: 
    * Permissions required for the resource you're attaching the tag value: 
      * Resource-specific `createTagBinding` permission, such as `storage.buckets.createTagBinding` for Cloud Storage buckets.
      * Resource-specific `deleteTagBinding` permission, such as `storage.buckets.deleteTagBinding` for Cloud Storage buckets.
Alternatively, to attach the tag value on a project level, give the `resourcemanager.hierarchyNodes.createTagBinding` and `resourcemanager.hierarchyNodes.deleteTagBinding` permissions on the project. 
    * Permissions required for the tag value:
      * `resourcemanager.tagValueBindings.create`
      * `resourcemanager.tagValueBindings.delete`



You can get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Create a default soft delete retention duration tag and tag values

To create the default soft delete retention duration tag and tag values, complete the following instructions:

### Console

  1. In the Google Cloud console, go to the Tags page. 

[Go to Tags](https://console.cloud.google.com/iam-admin/tags)

  2. Select the parent organization you want to create a tag key for.

  3. Click add **Create**.

  4. In the **Tag key** field, enter `storage.defaultSoftDeletePolicy`.

**Note:** Only the `storage.defaultSoftDeletePolicy` tag name updates the default soft delete retention duration.
  5. In the **Tag key description** field, enter a description of your tag key.

  6. Click add **Add value**.

  7. In the **Tag value** field, enter the length of time you want to set as the default soft delete retention duration. Format the retention duration as a number value between 7 days and 90 days, such as `30d`. Or, to disable soft delete on your resource by default, enter `0d`.

  8. In the **Tag value description** field, enter a description of your tag value.

  9. Click **Create tag key**.




The newly created tag appears in the **Tag keys** list.

### Command line

  1. Create a tag using the [`gcloud resource-manager tags key create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create) command. Note that only the `storage.defaultSoftDeletePolicy` tag name updates the default soft delete policy.
         
         gcloud resource-manager tags keys create storage.defaultSoftDeletePolicy \
         --parent=organizations/ORGANIZATION_ID \
         --description="Configures the default softDeletePolicy for new Storage buckets."
         

Replace the following:

     * `ORGANIZATION_ID`: the numeric ID of the organization you want to set a default soft delete retention duration for. For example, `12345678901`.
  2. Add a tag value using the [`gcloud resource-manager tags values create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create) command and replace the following:
         
         gcloud resource-manager tags values create RETENTION_DURATION \
          --parent=ORGANIZATION_ID/storage.defaultSoftDeletePolicy \
          --description="Sets the default soft delete retention duration for new Storage buckets to $duration."
         

     * `RETENTION_DURATION`: the length of time you want to set as the new default soft delete retention duration. Format the retention duration as a number value between 7 days and 90 days, such as `30d`. Or, to disable soft delete on your resource by default, enter `0d`.

     * `ORGANIZATION_ID`: the numeric ID of the organization you want to set the default soft delete retention duration for. For example, `12345678901`.




**Note:** Creating a tag and tag values alone doesn't set a default soft delete retention duration. For the tag you created to take effect, you must attach the tag to a resource, see Attach a default soft delete retention duration tag to a resource.

## Attach a default soft delete retention duration tag to a resource

After you've created a default soft delete retention duration tag and set its tag values, you must attach the tag to a resource using a tag binding resource in order for the new default soft delete retention duration to take effect. To attach a tag to a resource, complete the following instructions:

### Console

  1. In the Google Cloud console, open the **Manage resources** page. 

[Open Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Click the organization, folder, or project you want to attach a tag to.

  3. Click label_important**Tags**.

  4. In the **Tags** panel, click **Select scope**.

  5. Select the parent organization, then click **Open**.

  6. In the **Tags** panel, select **Add tag**.

  7. In the **Key** field, select the default soft delete retention duration tag. You can filter the list by typing keywords.

  8. In the **Value** field, select the length of time you want to set as the default soft delete retention duration from the list. You can filter the list by typing keywords.

  9. Click **Save**.

  10. In the **Confirm** dialog, click **Confirm** to attach the tag.




A notification appears confirming that your tags are updated. The new tags appear under the **Tags** column on the **Manage resources** page.

### Command line

Attach the default soft delete retention duration tag to a resource using the [`gcloud resource-manager tags bindings create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create).
    
    
     gcloud resource-manager tags bindings create \
      --tag-value=ORGANIZATION_ID/storage.defaultSoftDeletePolicy/RETENTION_DURATION \
      --parent=RESOURCE_ID
    

Replace the following:

  * `ORGANIZATION_ID`: the numeric ID of the organization under which the tag was created. For example, `12345678901`.

  * `RETENTION_DURATION`: the length of time you want to set the new default soft delete retention duration to. Format the retention duration as a number value between 7 days and 90 days, such as `30d`. Or, to disable soft delete on your resource by default, enter `0d`.

  * `RESOURCE_ID`: the full name of the folder, project, or organization you want to create the tag binding for. For example, to attach a tag to `projects/7890123456`, enter `//cloudresourcemanager.googleapis.com/projects/7890123456`.




## Remove a default soft delete retention duration tag from a resource

You can remove a default soft delete retention duration tag from a resource by deleting the tag binding resource. To delete a tag binding resource, complete the following instructions:

### Console

  1. In the Google Cloud console, open the **Manage resources** page. 

[Open Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Click the organization, folder, or project from which you want to detach a tag.

  3. Click label_important**Tags**.

  4. In the **Tags** panel, next to the tag you want to detach, click delete**Delete item**.

  5. Click **Save**.

  6. In the **Confirm** dialog, click **Confirm** to detach the tag.




A notification appears confirming that your tags are updated. The updated list of tags appears under the **Tags** column on the **Manage resources** page.

### Command line

Delete a tag binding using the [`gcloud resource-manager tag bindings delete`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete) command:
    
    
     gcloud resource-manager tags bindings delete \
      --tag-value=ORGANIZATION_ID/storage.defaultSoftDeletePolicy/RETENTION_DURATION \
      --parent=RESOURCE_ID
    

Replace the following:

  * `ORGANIZATION_ID`: the numeric ID you used to set your default soft delete retention duration. For example, `12345678901`.

  * `RETENTION_DURATION`: the length of time you entered as the default soft delete retention duration for your resource. For example, if you set a default soft delete retention duration of 10 days, enter `10d`.

  * `RESOURCE_ID`: the full name of the folder, project, or organization you want to delete the tag binding for.




## What's next

  * Learn how to [use soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects).

  * Learn more about [Resource Manager tag creation and management](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
