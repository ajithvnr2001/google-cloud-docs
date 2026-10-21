---
url: https://docs.cloud.google.com/apigee/docs/apihub/attach-manage-tags/
title: Attach and manage tags \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:24:17.110470+00:00
---

# Attach and manage tags  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/attach-manage-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Attach and manage tags Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to attach and manage tags for API hub resources. API hub currently only supports tags using the gcloud CLI.

## What are tags?

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are metadata key-value pairs that are attached to Google Cloud resources. Tags are used for several purposes: 

  * To conditionally allow or deny policies based on whether a resource has a specific tag.
  * To group and organise your resources.
  * To filter your resources.



Tagging resources involves creating tags, managing access, and attaching key-value pairs. Each key can have only one value per resource. For example, a resource tagged with `environment: development` cannot also be tagged with `environment: production` or `environment: test`. The maximum number of tags allowed per resource is **50**. 

**Note:** Tags are different from [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#what-are-labels), which are another way to organize and filter your resources. Tags and labels work independently of each other, and you can use both on the same resource. 

## Supported resources

You can attach tags to the following API hub resources after resource creation: 

  * [APIs](https://docs.cloud.google.com/apigee/docs/apihub/apis-intro)
  * [API deployments](https://docs.cloud.google.com/apigee/docs/apihub/deployments-intro)
**Note:** By default, tags are inherited by child resources. For example, tags attached to an API are inherited by all API versions, operations, and specifications. 


## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. To manage tags for API hub resources, user accounts and service accounts should be granted the **Tag User** (`roles/resourcemanager.tagUser`) role. For more information, see [Tags roles and permissions](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#required-permissions).
  9. Create and define tags. For more information, see [Create and manage tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).



## Attach tags to a resource

To attach tags to a resource, you must create a [TagBinding resource](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings) that links the tag value to the Google Cloud resource. See [Attaching tags to a resource](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#gcloud_8) for detailed instructions. 

### gcloud

The following example shows how to attach a tag to an API:
    
    
    gcloud resource-manager tags bindings create \
    --tag-value=tagValues/TAG_VALUE \
    --parent=//apihub.googleapis.com/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID \
    --location=HUB_LOCATION
          

Replace the following: 

  * `TAG_VALUE`: the numeric ID of the Tag value
  * `HUB_PROJECT`: the project ID of the API hub project.
  * `HUB_LOCATION`: the location of the API hub project.
  * `API_ID`: the ID of the API.



**Example:**
    
    
    gcloud resource-manager tags bindings create \
    --tag-value=tagValues/123456789012 \
    --parent=//apihub.googleapis.com/projects/my-project/locations/us-central1/apis/my-api \
    --location=us-central1
    

## IAM conditions and tags

You can use tags and [IAM conditions](https://docs.cloud.google.com/apigee/docs/apihub/add-iam-conditions) to conditionally grant role bindings to users. If an IAM policy with conditional role bindings is applied, changing or deleting the tag attached to a resource can remove user access to that resource. 

For more information, see [Tags and conditional access](https://docs.cloud.google.com/iam/docs/tags-access-control).

## Detach tags from a resource

To detach tags from a resource, you must delete the tag binding resource that links the tag value to the Google Cloud resource. See [Detaching tags from a resource](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#detaching) for detailed instructions. 

### gcloud

The following example shows how to detach a tag from an API deployment:
    
    
    gcloud resource-manager tags bindings delete \
    --tag-value=tagValues/TAG_VALUE \
    --parent=//apihub.googleapis.com/projects/HUB_PROJECT/locations/HUB_LOCATION/deployments?deployment_id=DEPLOYMENT_ID \
    --location=HUB_LOCATION
          

Replace the following:

  * `TAG_VALUE`: the numeric ID of the Tag value
  * `HUB_PROJECT`: the project ID of the API hub project.
  * `HUB_LOCATION`: the location of the API hub project.
  * `DEPLOYMENT_ID`: the ID of the deployment.



**Example:**
    
    
    gcloud resource-manager tags bindings delete \
    --tag-value=tagValues/123456789012 \
    --parent=//apihub.googleapis.com/projects/my-project/locations/us-central1/deployments?deployment_id=my-deployment \
    --location=us-central1
    

## List tags for a resource

To get a list of tag bindings directly attached to a resource, use the `gcloud resource-manager tags bindings list` command. You can add the `--effective` flag, to additonally return a list of tags inherited by this resource. See [Listing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#listing_tags) for detailed instructions. 

### gcloud

The following example shows how to list tags for an API:
    
    
    gcloud resource-manager tags bindings list \
    --parent=//apihub.googleapis.com/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID \
    --location=HUB_LOCATION
          

Replace the following:

  * `HUB_PROJECT`: the project ID of the API hub project.
  * `HUB_LOCATION`: the location of the API hub project.
  * `API_ID`: the ID of the API.



**Example:**
    
    
    gcloud resource-manager tags bindings list \
    --parent=//apihub.googleapis.com/projects/my-project/locations/us-central1/apis/my-api \
    --location=us-central1 
    

## What's next

  * Learn how to use tags with policies that support them to conditionally enforce those policies. See [Policies and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#policies).
  * Learn how to add [IAM conditions](https://docs.cloud.google.com/apigee/docs/apihub/add-iam-conditions) in API hub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
