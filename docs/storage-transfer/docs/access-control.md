---
url: https://docs.cloud.google.com/storage-transfer/docs/access-control/
title: Permissions and roles \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:45.243876+00:00
---

# Permissions and roles  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Permissions and roles Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service uses [Identity and Access Management (IAM)](https://cloud.google.com/iam/) permissions and roles to control who can access Storage Transfer Service resources. The main types of resources available in Storage Transfer Service are jobs, operations, and agent pools. In the [IAM policy hierarchy](https://docs.cloud.google.com/iam/docs/overview#policy_hierarchy), jobs are child resources of projects, and operations are child resources of jobs.

To grant access to a resource, you assign one or more [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions) or [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to a user, group, or a [service account](https://docs.cloud.google.com/iam/docs/overview#service_account).

## Permissions

You can grant the following Storage Transfer Service permissions:

### Transfer project permission

Permission | Description  
---|---  
`storagetransfer.projects.getServiceAccount` | Can read the GoogleServiceAccount used by the Storage Transfer Service to access Cloud Storage buckets.  
  
### Transfer job permissions

The following table describes permissions for Storage Transfer Service jobs:

Permission | Description  
---|---  
`storagetransfer.jobs.create` | Can create new transfer jobs.  
`storagetransfer.jobs.delete` | Can delete existing transfer jobs.  
  
Transfer jobs are deleted by calling the **patch** function. However, users must have this permission when deleting transfer jobs to avoid permission errors.   
`storagetransfer.jobs.get` | Can retrieve specific jobs.  
`storagetransfer.jobs.list` | Can list all transfer jobs.  
`storagetransfer.jobs.run` | Can run all transfer jobs.  
`storagetransfer.jobs.update` | Can update transfer job configurations without deleting them.  
  
### Transfer operations permissions

The following table describes permissions for Storage Transfer Service operations:

Permission | Description  
---|---  
`storagetransfer.operations.assign` | Used by transfer agents to assign operations.  
`storagetransfer.operations.cancel` | Can cancel transfer operations.  
`storagetransfer.operations.get` | Can get details of transfer operations.  
`storagetransfer.operations.list` | Can list all transfer job operations.  
`storagetransfer.operations.pause` | Can pause transfer operations.  
`storagetransfer.operations.report` | Used by transfer agents to report operation status.  
`storagetransfer.operations.resume` | Can resume paused transfer operations.  
  
### Transfer agent pool permissions

The following table describes permissions for file system transfer agent pools:

Permission | Description  
---|---  
`storagetransfer.agentpools.create` | Can create agent pools.  
`storagetransfer.agentpools.update` | Can update agent pools.  
`storagetransfer.agentpools.delete` | Can delete agent pools.  
`storagetransfer.agentpools.get` | Can get information on specific agent pools.  
`storagetransfer.agentpools.list` | Can list information for all agent pools in the project.  
`storagetransfer.agentpools.report` | Used by transfer agents to report status.  
  
## Predefined roles

This section describes the predefined roles for Storage Transfer Service. Roles are the preferred way of setting IAM permissions.

### Role comparison

You can assign the following project role or Storage Transfer Service predefined roles:

Capability | Editor (`roles/editor`) | Storage Transfer (`roles/storagetransfer.`)   
---|---|---  
Admin (`admin`) | User (`user`) | Viewer (`viewer`)  
List/get jobs |  |  |  |   
Create jobs |  |  |  |   
Run jobs |  |  |  |   
Update jobs |  |  |  |   
Delete jobs |  |  |  |   
List/get transfer operations |  |  |  |   
Pause/resume transfer operations |  |  |  |   
Read Google service account details that are used by Storage Transfer Service to access Cloud Storage buckets. |  |  |  |   
List agent pools |  |  |  |   
Create agent pools |  |  |  |   
Update agent pools |  |  |  |   
Delete agent pools |  |  |  |   
Get agent pools |  |  |  |   
Read or set project bandwidth |  |  |  |   
  
### Role details

The following table describes in detail the predefined roles for Storage Transfer Service:

Role | Description | Included Permissions  
---|---|---  
**Storage Transfer Admin  
(`roles/storagetransfer.admin`)** |  Provides all Storage Transfer Service permissions, including deleting jobs.  **Rationale:** This is the highest-level role with the broadest responsibilities, the superuser who supports their colleagues as they perform transfers. This is most suitable for people that will administer transfers, such as IT admins.  | 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `storagetransfer.*`

  
**Storage Transfer User  
(`roles/storagetransfer.user`)** |  Provides permissions for the user to create, get, update, and list transfer jobs within the project. However, they can't delete their own jobs.  **Rationale:** This role allows the separation of creating and maintaining jobs from deleting jobs. This role is best suited for users who are required to execute transfers as part of their job function, such as an employee. This role doesn't allow transfer to be deleted, so that auditors or security personnel can view a fully preserved record of past transfers.  | 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `storagetransfer.agentpools.create`
  * `storagetransfer.agentpools.get`
  * `storagetransfer.agentpools.list`
  * `storagetransfer.agentpools.report`
  * `storagetransfer.agentpools.update`
  * `storagetransfer.jobs.create`
  * `storagetransfer.jobs.get`
  * `storagetransfer.jobs.list`
  * `storagetransfer.jobs.run`
  * `storagetransfer.jobs.update`
  * `storagetransfer.operations.*`
  * `storagetransfer.projects.getServiceAccount`

  
**Storage Transfer Viewer  
(`roles/storagetransfer.viewer`)** |  Provides permissions to list and get jobs and transfer operations within the project. The user can't schedule, update, or delete jobs.  **Rationale:** The viewer role is intended for read-only access to view transfer jobs and operations. This role allows separating the report and auditing tasks from creating and maintaining jobs. This role is most suitable for users or internal teams that audit transfer usage, such as security, compliance, or business unit leaders.  | 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `storagetransfer.agentpools.get`
  * `storagetransfer.agentpools.list`
  * `storagetransfer.jobs.get`
  * `storagetransfer.jobs.list`
  * `storagetransfer.operations.get`
  * `storagetransfer.operations.list`
  * `storagetransfer.projects.getServiceAccount`

  
**Storage Transfer Agent (`roles/storagetransfer.transferAgent`) ** |  Gives transfer agents the Storage Transfer Service permissions required to complete a transfer. As of May 1, 2024, `pubsub` permissions are no longer required. Grant this role to the user or service account being used by agents.  | 

  * `logging.logEntries.create`
  * `monitoring.timeSeries.create`
  * `pubsub.subscriptions.consume`
  * `pubsub.subscriptions.create`
  * `pubsub.subscriptions.delete`
  * `pubsub.subscriptions.get`
  * `pubsub.topics.attachSubscription`
  * `pubsub.topics.create`
  * `pubsub.topics.get`
  * `pubsub.topics.list`
  * `pubsub.topics.publish`
  * `storagetransfer.agentpools.report`
  * `storagetransfer.operations.assign`
  * `storagetransfer.operations.get`
  * `storagetransfer.operations.report`

  
**Storage Transfer Service Agent (`roles/storagetransfer.serviceAgent`) ** |  Gives the [ Storage Transfer Service service agent](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions#service_account) the permissions required to create and modify Pub/Sub topics to communicate from Google Cloud to transfer agents. Grant this role to the [ Storage Transfer Service service agent](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions#service_account).  | 

  * `pubsub.subscriptions.consume`
  * `pubsub.subscriptions.create`
  * `pubsub.subscriptions.delete`
  * `pubsub.subscriptions.get`
  * `pubsub.subscriptions.update`
  * `pubsub.topics.attachSubscription`
  * `pubsub.topics.create`
  * `pubsub.topics.delete`
  * `pubsub.topics.get`
  * `pubsub.topics.publish`
  * `pubsub.topics.update`

  
  
## Custom roles

You can create and apply [custom IAM roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) to meet your organization's access requirements.

When creating custom roles, we recommend using a combination of predefined roles to ensure that the correct permissions are included together.

The Google Cloud console will not work properly if the custom role is missing required permissions. For example, some parts of the Google Cloud console assume a role has read access to display an item before editing it, so a role with only write permissions may encounter Google Cloud console screens that don't work.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
