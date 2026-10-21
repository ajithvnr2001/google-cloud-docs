---
url: https://docs.cloud.google.com/pubsub/docs/tags/
title: Create and manage tags \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:59.074853+00:00
---

# Create and manage tags  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create and manage tags Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Google Cloud tags and how to use them with Pub/Sub. Tags can be applied to Pub/Sub topics, subscriptions, and snapshots. Support for applying tags to Pub/Sub schemas is planned.

## About tags

A tag is a key-value pair that can attach to a resource within Google Cloud. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a resource has a specific tag. For more information about tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

Tags are attached to resources by creating a tag binding resource that links the value to the Google Cloud resource.

## Required permissions

To get the permissions that you need to manage tags, ask your administrator to grant you the following IAM roles: 

  * [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the resources the tags are attached to
  * View and manage tags at the organization level: [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`) on the organization 
  * Create, update, and delete tag definitions: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on the resource you're creating, updating, or deleting tags for 
  * Attach and remove tags from resources: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and the resources that you are attaching or removing the tag value to 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To attach tags to Pub/Sub topics, subscriptions, or snapshots, you need the [Pub/Sub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) role (`roles/pubsub.editor`). 

## Create tag keys and values

Before you can attach a tag, you need to create a tag and configure its value. To create tag keys and tag values, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [Adding a tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

## Add tags during resource creation

You can add tags at the time of creating topics, subscriptions, or snapshots. Adding tags lets you instantly provide essential metadata for your topics, subscriptions, or snapshots and also helps with better organization, cost tracking, and automated policy application.

### Console

  1. Go to the **Pub/Sub** page in the Google Cloud console.

[Go to Pub/Sub](https://console.cloud.google.com/projectselector/cloudpubsub)

  2. Select the option to create a new topic, subscription, or snapshot.
  3. Click label_important**Manage tags**.
  4. If your organization doesn't appear in the **Manage tags** panel, click **Select scope for tags**. Choose to add tags defined either at your organization or project level, and then enter the ID for the same. 
  5. Click **Add tag**.
  6. Select the key for the tag you want to attach from the list. You can filter the list by typing keywords.
  7. Select the value for the tag you want to attach from the list. You can filter the list by typing keywords.
  8. Click **Save**. The **Tags** section is updated with the tags information.
  9. Create your topic, subscription, or snapshot. The new topic, subscription, or snapshot is created with the provided tags.



### gcloud

To add tags during topic, subscription, or snapshot creation, run the following command:
    
    
           gcloud pubsub topics create TOPIC_ID --tags=TAG_KEY=TAG_VALUE
         

Replace the following:

  * TOPIC_ID: the ID of the topic
  * TAG_KEY: the permanent ID or namespaced name of the tag key that is attached-for example, tagKeys/567890123456
  * TAG_VALUE: the permanent ID or namespaced name of the tag value that is attached—for example, tagValues/567890123456



Specify multiple tags by separating the tags with a comma, for example, `TAGKEY1=TAGVALUE1,TAGKEY2=TAGVALUE2`

### API

Send a `POST` request to the following URL:
    
    
          https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics/TOPIC_ID

Provide the following JSON in the request body:
    
    
          
    {
      "name": "projects/PROJECT_ID/topics/TOPIC_ID",
      "tags": {
        "TAGKEY_NAME": "TAGVALUE_NAME"
      }
    }
    

Replace the following:

  * PROJECT_ID: the ID of the project
  * TOPIC_ID: the ID of the topic
  * TAGKEY_NAME: the permanent ID or namespaced name of the tag key that is attached-for example, tagKeys/567890123456
  * TAGVALUE_NAME: the permanent ID or namespaced name of the tag value that is attached—for example, tagValues/567890123456



## Enforce mandatory tags

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enforce mandatory tags on resources to ensure that specific tags are present when resources are created, such as a Cost Center tag, to maintain compliance with organizational policies. You can do this using organization policies and custom constraints. Enforcement occurs at resource creation, preventing the provisioning of resources without the required tags. For more information, see [Enforcement of mandatory tags using organization policies](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#enforce_tags).

### Set up a custom constraint to enforce tags

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Select the project picker at the top of the page.

  3. From the project picker, select the organization where you want to enforce the custom constraint.

  4. [Set up a custom constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#set_up_custom_constraint) with the following parameters:

     * **Enforcement method** : `Govern tags`
     * **Resource type** : the fully qualified name of the Google Cloud REST resource that you want to enforce mandatory tags on, for example, `file.googleapis.com/Instance`
     * **Condition** : a Common Expression Language (CEL) condition specifying the tag keys that you want to enforce on the resource, for example `resource.hasDirectTagKey("1234567890/owner")` to enforce a tag binding for the tag key `1234567890/owner`. The `resource.hasDirectTagKey` CEL function only matches tags directly applied to a resource and doesn't consider tags inherited from ancestors in the resource hierarchy.
     * **Action** : `Allow` or `Deny`. 
       * Allow: If the specified condition is met, the action to create or update the resource is permitted.
       * Deny: If the specified condition is met, the action to create or update the resource is blocked.
  5. Click **Create constraint**.




###  gcloud 

Create a YAML file for the custom constraint:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - RESOURCE_NAME
    methodTypes:
    - GOVERN_TAGS
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `1234567890`.

  * `CONSTRAINT_NAME`: the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers, for example, `custom.enforceMandatoryTags`.

  * `RESOURCE_NAME`: the fully qualified name of the Google Cloud REST resource that you want to enforce mandatory tags on, for example, `file.googleapis.com/Instance`.

  * `CONDITION`: a Common Expression Language (CEL) condition specifying the tag keys that you want to enforce on the resource, for example `resource.hasDirectTagKey("1234567890/owner")` to enforce a tag binding for the tag key `1234567890/owner`.

  * `ACTION`: the action to take if the `condition` is met. This can be either `ALLOW` or `DENY`.

The deny action means that if the specified condition is met, the operation to create or update the resource is blocked.

The allow action means that if the specified condition is met, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2000 characters.




[Set up the custom constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#set_up_custom_constraint) to make it available for organization policies in your organization.

After you've defined the custom constraint, you can [test and analyze the organization policy changes](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#test_and_analyze) and [enforce the constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#enforcing_custom_constraints).

## Add tags to existing resources

To add a tag to existing topics, subscriptions, or snapshots, follow these steps:

### Console

  1. Go to the **Pub/Sub** page in the Google Cloud console.

[Go to Pub/Sub](https://console.cloud.google.com/projectselector/cloudpubsub)

  2. Select the page for the resource to which you want to attach a tag. For example, to attach a tag to a topic, go to the **Topics** page. 
  3. Click label_important**Tags**.
  4. If your organization doesn't appear in the **Tags** panel, click **Select scope**. Select your organization and click **Open**.
  5. Click **Add tag**.
  6. Select the key for the tag you want to attach from the list. You can filter the list by typing keywords.
  7. Select the value for the tag you want to attach from the list. You can filter the list by typing keywords.
  8. Click **Save**.
  9. In the **Confirm** dialog, click **Confirm** to attach the tag.

A notification confirms that your tags updated.




### gcloud

To attach a tag to a topic, subscription, or snapshot, you must create a tag binding resource by using the `gcloud resource-manager tags bindings create` command:
    
    
          gcloud resource-manager tags bindings create \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that you attach to a resource—for example, `tagValues/567890123456`.
  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//pubsub.googleapis.com/`). For example, to attach a tag to `/projects/PROJECT_ID/topics/TOPIC_ID`, the full ID is `//pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID`. 



## List tags attached to resources

You can view a list of tag bindings directly attached to or inherited by the topic, subscription, or snapshot.

### Console

  1. Go to the **Pub/Sub** page in the Google Cloud console.

[Go to Pub/Sub](https://console.cloud.google.com/projectselector/cloudpubsub)

  2. Select the page for the resource to which you want to view tags. For example, to view tags for topic, go to the **Topics** page.

Tags are displayed in the **Tags** section of the topic page in the console.




### gcloud

To get a list of tag bindings attached to a resource, use the `gcloud resource-manager tags bindings list` command:
    
    
          gcloud resource-manager tags bindings list \
              --parent=RESOURCE_ID
          

Replace the following:

  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//pubsub.googleapis.com/`). For example, to attach a tag to `/projects/PROJECT_ID/topics/TOPIC_ID`, the full ID is `//pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID`. 



You should get a response similar to the following:
    
    
    name: tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F7890123456/tagValues/567890123456
              tagValue: tagValues/567890123456
              resource: //pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID
          

## Detach tags from resources

You can detach tags that have been directly attached to a topic, subscription, or snapshot. Inherited tags can be overridden by attaching a tag with the same key and a different value, but they can't be detached.

### Console

  1. Go to the **Pub/Sub** page in the Google Cloud console.

[Go to Pub/Sub](https://console.cloud.google.com/projectselector/cloudpubsub)

  2. Select the page for the resource to which you want to remove a tag. For example, to remove a tag from a topic, go to the **Topics** page. 
  3. Click label_important**Tags**.
  4. In the **Tags** panel, next to the tag you want to detach, click delete**Delete item**.
  5. Click **Save**.
  6. In the **Confirm** dialog, click **Confirm** to detach the tag.



A notification confirms that your tags updated.

### gcloud

To delete a tag binding, use the `gcloud resource-manager tags bindings delete` command:
    
    
          gcloud resource-manager tags bindings delete \
              --tag-value=TAGVALUE_NAME \
              --parent=RESOURCE_ID
          

Replace the following:

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that is attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//pubsub.googleapis.com/`). For example, to attach a tag to `/projects/PROJECT_ID/topics/TOPIC_ID`, the full ID is `//pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID`. 



## Delete tag keys and values

When removing a tag key or value definition, ensure that the tag is detached from the topic, subscription, or snapshot. You must delete existing tag attachments, called tag bindings, before deleting the tag definition itself. To delete tag keys and tag values, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

## Identity and Access Management conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your hierarchy. Changing or deleting the tag attached to a resource can remove user access to that resource if an IAM policy with conditional role bindings has been applied. For more information, see [Identity and Access Management conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * See the other [services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * See [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control) to learn how to use tags with IAM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
