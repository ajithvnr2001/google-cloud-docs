---
url: https://docs.cloud.google.com/storage/docs/projects/
title: Projects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:07.982585+00:00
---

# Projects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Projects Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud projects let you organize resources, manage access, and track billing. All of your Google Cloud resources belong to a project, including Cloud Storage resources like buckets and objects.

A project consists of a set of users, a set of APIs, and the billing, authentication, and monitoring settings for those APIs. So, for example, all of your Cloud Storage buckets and objects, along with user permissions for accessing them, reside in a project.

You can have one project, or you can create multiple projects and use them to organize your Google Cloud resources, including your Cloud Storage data, into logical groups.

For background information, see the [overview of projects in Google Cloud](https://docs.cloud.google.com/docs/overview#projects).

## When to specify a project

Most of the time, you don't need to specify a project when performing actions in Cloud Storage. However, you should include either the project ID or the project number in the following cases:

### Console

  * When using Cloud Storage with the Google Cloud console, you're automatically associated with a project. You can change projects by using the drop-down menu at the top of the Google Cloud console window.

  * When first accessing a bucket that has enabled [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays), you're prompted to select a project to bill requests to. You can subsequently change the billing project by using the **Change project** button located above the list of objects in the bucket.




### Command line

The following commands use the [`project` property](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) set in your Google Cloud CLI configuration, unless you use the [global `--project` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--project) in the command to specify a different project:

  * [`storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create)
  * [`storage ls`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) (when listing buckets) and [`storage buckets list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list)
  * [`storage service-agent`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/service-agent)
  * [`storage hmac create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hmac/create) and [`storage hmac list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hmac/list)



Use the [global `--billing-project` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project), along with a project identifier, to indicate the project to charge for bucket access. This is required when accessing a bucket that has enabled [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) and is optional otherwise.

### Client libraries

The [Cloud Storage Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries) require a project to be specified under the same circumstances as the JSON API.

### JSON API

The following methods require you to specify a project:

  * [List buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list)
  * [Insert bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert)
  * [Get project service agent](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount/get)
  * All methods associated with the [HMAC key resource](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys)



The project is sent as a parameter in the request URL, as in the following example:
    
    
    GET https://storage.googleapis.com/storage/v1/b?project=PROJECT_IDENTIFIER

  * To indicate a project to charge for bucket access, use the 'userProject' query parameter, along with a project identifier, as in the following example:
        
        GET https://storage.googleapis.com/storage/v1/b?userProject=PROJECT_IDENTIFIER

This query parameter is required when accessing a bucket that has enabled [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) and is optional otherwise.




### XML API

The following requests require you to specify a project, unless you have [set a default project](https://docs.cloud.google.com/storage/docs/aws-simple-migration#defaultproj) for interoperable access:

  * [List buckets](https://docs.cloud.google.com/storage/docs/xml-api/get-service)
  * [Create a bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create)



The project associated with these XML API requests is specified in the [`x-goog-project-id`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogprojectid) HTTP header, as in the following example:
    
    
    x-goog-project-id: PROJECT_ID

The header is optional for other XML API requests.

  * To indicate a project to charge for bucket access, use the 'x-goog-user-project' header, along with a project ID, as in the following example:
        
        x-goog-user-project: PROJECT_ID

This header is required when accessing a bucket that has enabled [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) and is optional otherwise.




## Projects and permissions

For each project, you use [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) to grant the ability to manage and work on your project. When you grant an IAM _role_ to a _principal_ , such as a user account, that principal obtains certain _permissions_ that allow them to perform actions. When you grant a role at the project level, the access provided by the role applies to every bucket and object within the project. Alternatively, when you grant a role for an individual bucket, the access provided by the role is limited to just that bucket and the objects the bucket contains.

For a list of available roles that apply to Cloud Storage, as well as a discussion about how a special set of roles, called _basic roles_ , apply to Cloud Storage, see [Cloud Storage IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

For instructions for viewing, granting, and revoking a principal's roles at the bucket and project level, see [Using IAM with projects](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Service accounts

[Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) allow applications to authenticate and access Google Cloud resources and services. For example, you can create a service account that your Compute Engine instances use to access objects stored in Cloud Storage buckets. Service accounts are created within a project and have a unique email address that identifies them.

The following are examples of actions related to Cloud Storage that are often taken by service accounts that [you create and manage](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts):

  * Performing [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) transfers.
  * [Moving data to and from Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/import-export).
  * Creating [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).



### Service agents

A [service agent](https://docs.cloud.google.com/iam/docs/service-agents) is a special type of service account that acts on behalf of a Google Cloud service. Cloud Storage uses a service agent for the following features:

  * [Pub/Sub Notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications).
  * [Customer-Managed Encryption Keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).



The Cloud Storage service agent is not initially available when you make a project. Instead, it is automatically activated the first time it's accessed, either by one of the features listed previously or when you [request the service agent's name](https://docs.cloud.google.com/storage/docs/getting-service-agent). The service agent must be activated prior to [assigning permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to it.

The following is an example email address for the Cloud Storage service agent associated with [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) `123456789876`:
    
    
    service-123456789876@gs-project-accounts.iam.gserviceaccount.com

## Project deletions

When you delete (shut down) a project, your Cloud Storage buckets and the objects in them are also deleted unless they are protected by soft delete. To help protect your data in case a project is accidentally or maliciously deleted, we recommend that you [enable soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) on your buckets:

  * If you delete your project, any bucket that has soft delete enabled is retained for the soft delete retention duration or the [Google Cloud project recovery window](https://docs.cloud.google.com/storage/docs/introduction#quickstarts), whichever time period is shorter. After this time period, the bucket is permanently deleted.

  * If you restore a deleted project, buckets are restored to the state that they were in when the project was deleted. For example, buckets that were live when the project was deleted are restored as live buckets.

  * Buckets that aren't protected by soft delete might be deleted immediately when a project is deleted, and might not be restorable.




We also recommend the following strategies to help protect your data from project deletions:

  * Limit access to project-level deletion by [placing a lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) on your projects.

  * Back up business-critical data to buckets in a different project.




For more information about options to help protect and recover your data, see [Data protection, backup, and recovery options](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects).

## What's next

  * Complete one of the [Cloud Storage quickstarts](https://docs.cloud.google.com/storage/docs/introduction#quickstarts).
  * Learn how to [create a new project and manage existing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * Find out how to [use the Google Cloud console to manage your data](https://docs.cloud.google.com/storage/docs/cloud-console).
  * [Manage your project's service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
