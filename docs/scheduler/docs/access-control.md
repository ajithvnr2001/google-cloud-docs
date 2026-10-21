---
url: https://docs.cloud.google.com/scheduler/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:01.083614+00:00
---

# Access control with IAM  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) lets you manage access to Cloud Scheduler resources by granting specific permissions to service accounts and principals. You can assign predefined or custom roles to control who can view, configure, and run scheduled jobs.

## Overview

Cloud Scheduler uses IAM for access control.

For an introduction to IAM and its features, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview). To learn how to grant and revoke access, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

For lists of the permissions and roles that Cloud Scheduler supports, see the following sections.

## Enable the Cloud Scheduler API

To view and assign IAM roles for Cloud Scheduler, you must enable the Cloud Scheduler API for your project. You won't be able to see the Cloud Scheduler roles in the Google Cloud console until you enable the API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudscheduler.googleapis.com&redirect=https%3A//console.cloud.google.com)

## Predefined roles

The following table lists the Cloud Scheduler predefined IAM roles with a corresponding list of all the permissions each role includes.

The predefined roles address most typical use cases. If your use case isn't covered by the predefined roles, you can [create an IAM custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

### Cloud Scheduler roles

Role | Permissions  
---|---  
  
#### Cloud Scheduler Admin 

(`roles/cloudscheduler.admin`) Full access to jobs and executions.  Note that a Cloud Scheduler Admin (or any custom role with the permission cloudscheduler.jobs.create) can create jobs that publish to any Pub/Sub topics within the project.  |  `appengine.applications.get` `cloudscheduler.*`

  * `cloudscheduler.jobs.create`
  * `cloudscheduler.jobs.delete`
  * `cloudscheduler.jobs.enable`
  * `cloudscheduler.jobs.fullView`
  * `cloudscheduler.jobs.get`
  * `cloudscheduler.jobs.list`
  * `cloudscheduler.jobs.pause`
  * `cloudscheduler.jobs.run`
  * `cloudscheduler.jobs.update`
  * `cloudscheduler.locations.get`
  * `cloudscheduler.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Cloud Scheduler Viewer 

(`roles/cloudscheduler.viewer`) Get and list access to jobs, executions, and locations.  |  `appengine.applications.get` `cloudscheduler.jobs.fullView` `cloudscheduler.jobs.get` `cloudscheduler.jobs.list` `cloudscheduler.locations.*`

  * `cloudscheduler.locations.get`
  * `cloudscheduler.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Cloud Scheduler Job Runner 

(`roles/cloudscheduler.jobRunner`) Access to run jobs.  |  `appengine.applications.get` `cloudscheduler.jobs.fullView` `cloudscheduler.jobs.run` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Scheduler Service Agent 

(`roles/cloudscheduler.serviceAgent`) Grants Cloud Scheduler Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.logEntries.create` `logging.logEntries.route` `pubsub.topics.publish`  
  
## Project-level IAM management

At the project level, you can grant, change, and revoke IAM roles using the Google Cloud console, the IAM API, or the Google Cloud CLI. For instructions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
