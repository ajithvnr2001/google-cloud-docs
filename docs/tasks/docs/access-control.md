---
url: https://docs.cloud.google.com/tasks/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:34.712287+00:00
---

# Access control with IAM  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Tasks uses Identity and Access Management (IAM) for access control. For an introduction to IAM and its features, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview). To learn how to grant and revoke access, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You can configure access control at the project level and at the queue level. For example, you might grant a user permission to create and add tasks to a queue, but not delete the queue. Or you might grant access to all Cloud Tasks resources within a project to a group of users. For more information, see [Secure queue configuration](https://docs.cloud.google.com/tasks/docs/secure-queue-configuration).

Every Cloud Tasks method requires the caller to have the necessary permissions. This page describes the permissions and roles that Cloud Tasks supports. Permissions are also checked when [`queue.yaml`](https://docs.cloud.google.com/tasks/docs/queue-yaml) (or the legacy `queue.xml` file) is updated; or when you use the Google Cloud console.

**Note:** To access and manage tasks using the Google Cloud console, you must also have the `appengine.applications.get` permission. All of the [App Engine predefined roles](https://docs.cloud.google.com/appengine/docs/standard/python3/roles) include this permission.

## Enable the Cloud Tasks API

To view and assign IAM roles for Cloud Tasks, you must enable the Cloud Tasks API for your project. You won't be able to see the Cloud Tasks roles in the Google Cloud console until you enable the API.

###  Console 

Enable the Cloud Tasks API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudtasks.googleapis.com&redirect=https%3A//console.cloud.google.com)

###  gcloud 

Enable the Cloud Tasks API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable cloudtasks.googleapis.com

## Predefined roles

The following table lists the Cloud Tasks predefined IAM roles and their corresponding permissions.

The predefined roles address most typical use cases. If your use case isn't covered by the predefined roles, you can [create an IAM custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

Role | Permissions  
---|---  
  
#### Cloud Tasks Admin 

(`roles/cloudtasks.admin`) Full access to queues and tasks.  |  `cloudtasks.*`

  * `cloudtasks.cmekConfig.get`
  * `cloudtasks.cmekConfig.update`
  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`
  * `cloudtasks.operations.get`
  * `cloudtasks.queues.create`
  * `cloudtasks.queues.delete`
  * `cloudtasks.queues.get`
  * `cloudtasks.queues.getIamPolicy`
  * `cloudtasks.queues.list`
  * `cloudtasks.queues.pause`
  * `cloudtasks.queues.purge`
  * `cloudtasks.queues.resume`
  * `cloudtasks.queues.setIamPolicy`
  * `cloudtasks.queues.update`
  * `cloudtasks.tasks.create`
  * `cloudtasks.tasks.delete`
  * `cloudtasks.tasks.fullView`
  * `cloudtasks.tasks.get`
  * `cloudtasks.tasks.list`
  * `cloudtasks.tasks.run`

`monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Editor 

(`roles/cloudtasks.editor`) Editor role for cloudtasks  |  `cloudtasks.cmekConfig.get` `cloudtasks.locations.*`

  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`

`cloudtasks.operations.get` `cloudtasks.queues.create` `cloudtasks.queues.delete` `cloudtasks.queues.get` `cloudtasks.queues.list` `cloudtasks.queues.pause` `cloudtasks.queues.purge` `cloudtasks.queues.resume` `cloudtasks.queues.update` `cloudtasks.tasks.*`

  * `cloudtasks.tasks.create`
  * `cloudtasks.tasks.delete`
  * `cloudtasks.tasks.fullView`
  * `cloudtasks.tasks.get`
  * `cloudtasks.tasks.list`
  * `cloudtasks.tasks.run`

`monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Viewer 

(`roles/cloudtasks.viewer`) Get and list access to tasks, queues, and locations.  |  `cloudtasks.cmekConfig.get` `cloudtasks.locations.*`

  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`

`cloudtasks.operations.get` `cloudtasks.queues.get` `cloudtasks.queues.list` `cloudtasks.tasks.fullView` `cloudtasks.tasks.get` `cloudtasks.tasks.list` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Enqueuer Beta

(`roles/cloudtasks.enqueuer`) Access to create tasks.  |  `cloudtasks.operations.get` `cloudtasks.tasks.create` `cloudtasks.tasks.fullView` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Queue Admin 

(`roles/cloudtasks.queueAdmin`) Admin access to queues.  |  `cloudtasks.locations.*`

  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`

`cloudtasks.queues.*`

  * `cloudtasks.queues.create`
  * `cloudtasks.queues.delete`
  * `cloudtasks.queues.get`
  * `cloudtasks.queues.getIamPolicy`
  * `cloudtasks.queues.list`
  * `cloudtasks.queues.pause`
  * `cloudtasks.queues.purge`
  * `cloudtasks.queues.resume`
  * `cloudtasks.queues.setIamPolicy`
  * `cloudtasks.queues.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Task Deleter 

(`roles/cloudtasks.taskDeleter`) Access to delete tasks.  |  `cloudtasks.tasks.delete` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Task Runner Beta

(`roles/cloudtasks.taskRunner`) Access to run tasks.  |  `cloudtasks.tasks.fullView` `cloudtasks.tasks.run` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Tasks Service Agent 

(`roles/cloudtasks.serviceAgent`) Grants Cloud Tasks Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.logEntries.create`  
  
## What's next

  * [Authenticate to Cloud Tasks](https://docs.cloud.google.com/tasks/docs/authentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
