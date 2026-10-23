---
url: https://docs.cloud.google.com/transcoder/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:57.477538+00:00
---

# Access control with IAM  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

The Transcoder API uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) for access control.

You can configure access control for the Transcoder API at the project level. For example, you can grant access for developers to list and get all jobs within a project.

For a detailed description of IAM and its features, see the [IAM documentation](https://docs.cloud.google.com/iam/docs). In particular, see the section on [managing IAM policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Every Transcoder API method requires the caller to have the necessary permissions. For more information, see Permissions and Roles.

## Permissions

This section summarizes the Transcoder API permissions that IAM supports.

### Required permissions

The following tables list the IAM permissions that are associated with the Transcoder API.

**Note:** Method names are shortened in the table so that each method's full name begins with `projects.locations`.Job method | Required permissions  
---|---  
`jobs.create` | `transcoder.jobs.create` on the parent Google Cloud project.  
`jobs.delete` | `transcoder.jobs.delete` on the parent Google Cloud project.  
`jobs.get` | `transcoder.jobs.get` on the parent Google Cloud project.  
`jobs.list` | `transcoder.jobs.list` on the parent Google Cloud project.  
Job template method | Required permissions  
---|---  
`jobTemplates.create` | `transcoder.jobTemplates.create` on the parent Google Cloud project.  
`jobTemplates.delete` | `transcoder.jobTemplates.delete` on the parent Google Cloud project.  
`jobTemplates.get` | `transcoder.jobTemplates.get` on the parent Google Cloud project.  
`jobTemplates.list` | `transcoder.jobTemplates.list` on the parent Google Cloud project.  
  
## Roles

The following table lists the Transcoder API IAM roles, including the permissions associated with each role:

IAM role | Permissions  
---|---  
  
#### Transcoder Viewer 

(`roles/transcoder.viewer`) Viewer of all transcoder resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `transcoder.jobTemplates.get` `transcoder.jobTemplates.list` `transcoder.jobTemplates.listEffectiveTags` `transcoder.jobTemplates.listTagBindings` `transcoder.jobs.get` `transcoder.jobs.list` `transcoder.jobs.listEffectiveTags` `transcoder.jobs.listTagBindings`  
  
#### Transcoder Admin 

(`roles/transcoder.admin`) Full access to all transcoder resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `transcoder.*`

  * `transcoder.jobTemplates.create`
  * `transcoder.jobTemplates.createTagBinding`
  * `transcoder.jobTemplates.delete`
  * `transcoder.jobTemplates.deleteTagBinding`
  * `transcoder.jobTemplates.get`
  * `transcoder.jobTemplates.list`
  * `transcoder.jobTemplates.listEffectiveTags`
  * `transcoder.jobTemplates.listTagBindings`
  * `transcoder.jobs.create`
  * `transcoder.jobs.createTagBinding`
  * `transcoder.jobs.delete`
  * `transcoder.jobs.deleteTagBinding`
  * `transcoder.jobs.get`
  * `transcoder.jobs.list`
  * `transcoder.jobs.listEffectiveTags`
  * `transcoder.jobs.listTagBindings`

  
  
The roles `roles/owner` and `roles/editor` grant the permissions associated with the `roles/transcoder.admin` role. The role `roles/viewer` grants permissions associated with the `roles/transcoder.viewer` role.

The roles `roles/owner`, `roles/editor`, and `roles/viewer` include permissions for other Google Cloud services as well. For more information about roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Access to Cloud Storage and Pub/Sub

By default, the Transcoder API has access to all of your project's Cloud Storage buckets and Pub/Sub topics. When you create your first job, the Transcoder API creates a service account using the following naming convention:

`service-PROJECT_NUMBER@gcp-sa-transcoder.iam.gserviceaccount.com`

PROJECT_NUMBER is the project number of your project with the Transcoder API enabled. This service account is granted the Transcoder Service Agent role and has permissions to do the following:

  * Download and upload files to your project's Cloud Storage buckets
  * Publish status updates to your project's Pub/Sub topics



**Note:** It can take up to 7 minutes for the API service account to deploy. If you try to create a job and [receive a permissions error](https://docs.cloud.google.com/iam/docs/access-change-propagation), try again after waiting 7 minutes.

### Limiting access

To limit this access, remove the Transcoder Service Agent role from the service account and replace it with more fine-grained access. Follow these steps:

  1. Go to the [IAM](https://console.cloud.google.com/iam-admin/iam) page (**Permissions** tab) in the Google Cloud console.
  2. Find the service account with the Transcoder Service Agent role and select the edit button.
  3. Delete the Transcoder Service Agent role from the service account.
  4. Grant access to the service account for each individual Cloud Storage bucket: 
     1. Go to the [Cloud Storage Browser](https://console.cloud.google.com/storage/browser) page.
     2. Click a bucket.
     3. Select the **Permissions** tab.
     4. Click **Add**.
     5. In the **New principals** box, type the name of the service account.
     6. Under **Role** , select **Storage Object Admin**.
     7. Click **Save**. The Transcoder API now has access to the bucket.
  5. (Optional) Grant access to the service account for any configured Pub/Sub topic: 
     1. Go to the [Pub/Sub topics](https://console.cloud.google.com/cloudpubsub/topic/list) page.
     2. Click a topic.
     3. Select the **Permissions** tab.
     4. Click **Add principal**.
     5. In the **New principals** box, type the name of the service account.
     6. Under **Role** , select **Pub/Sub Publisher**.
     7. Click **Save**. The Transcoder API now has access to the topic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
