---
url: https://docs.cloud.google.com/error-reporting/docs/iam/
title: Control access with IAM \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:45.345435+00:00
---

# Control access with IAM  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Control access with IAM Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles to control access to Error Reporting data, ensuring team members have the permissions they need to view, triage, and manage application errors while enforcing least privilege.

IAM roles and permissions determine which Error Reporting resources you can access through the Google Cloud console and the [Error Reporting API](https://docs.cloud.google.com/error-reporting/reference/rest). You grant these roles at the Google Cloud project, folder, or organization level to provide principals with appropriate access across your resource hierarchy.

## Predefined roles

IAM provides predefined roles to give granular access to specific Google Cloud resources. Google Cloud creates and maintains these roles and automatically updates their permissions as necessary, such as when Error Reporting adds new features. For information about roles and permissions, see the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions).

The following table lists the Error Reporting roles, the roles' titles, their descriptions, contained permissions, and the lowest-level resource type where the roles can be set. A particular role can be granted on this resource type or, in most cases, any resource type above it in the [Google Cloud hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

Role | Permissions  
---|---  
  
#### Error Reporting Admin Beta

(`roles/errorreporting.admin`) Provides full access to Error Reporting data.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudnotifications.activities.list` `errorreporting.*`

  * `errorreporting.applications.list`
  * `errorreporting.errorEvents.create`
  * `errorreporting.errorEvents.delete`
  * `errorreporting.errorEvents.list`
  * `errorreporting.groupMetadata.get`
  * `errorreporting.groupMetadata.update`
  * `errorreporting.groups.list`

`logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get`  
  
#### Error Reporting User Beta

(`roles/errorreporting.user`) Provides the permissions to read and write Error Reporting data, except for sending new error events.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudnotifications.activities.list` `errorreporting.applications.list` `errorreporting.errorEvents.delete` `errorreporting.errorEvents.list` `errorreporting.groupMetadata.*`

  * `errorreporting.groupMetadata.get`
  * `errorreporting.groupMetadata.update`

`errorreporting.groups.list` `logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get`  
  
#### Error Reporting Viewer Beta

(`roles/errorreporting.viewer`) Provides read-only access to Error Reporting data.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudnotifications.activities.list` `errorreporting.applications.list` `errorreporting.errorEvents.list` `errorreporting.groupMetadata.get` `errorreporting.groups.list` `logging.notificationRules.get` `logging.notificationRules.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get`  
  
#### Error Reporting Writer Beta

(`roles/errorreporting.writer`) Provides the permissions to send error events to Error Reporting.  Lowest-level resources where you can grant this role:

  * Service Account 

|  `errorreporting.errorEvents.create`  
  
## API permissions

Error Reporting API methods require specific IAM permissions. The following table lists and describes the permissions needed by the API methods.

Method | Required permission(s) | Description  
---|---|---  
`[deleteEvents](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects/deleteEvents)` | `errorreporting.errorEvents.delete` | Delete error events.  
`[events.list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/list)` | `errorreporting.errorEvents.list` | List error events.  
`[events.report](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report)` | `errorreporting.errorEvents.create` | Create or update error events.  
`[groupStats.list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list)` | `errorreporting.groups.list` | List `ErrorGroupStats`.  
`[groups.get](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups/get)` | `errorreporting.groupMetadata.get` | Retrieve error group information.  
`[groups.update](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups/update)` | 
* `errorreporting.groupMetadata.update`
* `errorreporting.applications.list`
| 
* Update and mute error group information.   
Change error resolution status. 
* List services and versions for a project.  
  
## Further considerations

When deciding which permissions and roles apply to a principal's use cases, consider the following summary of Error Reporting activities and required permissions:

Activities | Required permissions  
---|---  
Have read-only access to the Error Reporting Google Cloud console page. | `errorreporting.applications.list`  
`errorreporting.groupMetadata.get`  
`errorreporting.groups.list`  
See group details in the Google Cloud console. | Permissions for read-only access plus:  
`errorreporting.errorEvents.list`  
Change metadata and resolution status in the Google Cloud console, including muting errors. | Permissions for read-only access plus:  
`errorreporting.groupMetadata.update`  
Delete errors in the Google Cloud console. | Permissions for read-only access plus:  
`errorreporting.errorEvents.delete`  
Create errors (no Google Cloud console permissions needed). | `errorreporting.errorEvents.create`  
Subscribe to notifications. | Permissions for read-only access plus:  
`cloudnotifications.activities.list`  
  
## Grant and manage roles

You can grant and manage IAM roles using the Google Cloud console, the IAM API methods, or the Google Cloud CLI. For instructions on granting and managing roles, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You can grant multiple roles to the same user. To get a list of the permissions contained in a role, see [Getting the role metadata](https://docs.cloud.google.com/iam/docs/creating-custom-roles#getting_the_role_metadata).

If you're trying to access a Google Cloud resource and lack the necessary permissions, contact the user who is listed as the **Owner** for the resource.

### Custom roles

To create a custom role with Error Reporting permissions, choose permissions from API permissions, then follow the instructions to [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

## Role change latency

Error Reporting caches IAM permissions for five minutes, so it can take up to five minutes for a role change to become effective.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
