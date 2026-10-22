---
url: https://docs.cloud.google.com/logging/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:41.194971+00:00
---

# Access control with IAM  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you understand how Cloud Logging uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles and permissions to control access to Logging resources. Your IAM roles determine whether you can perform actions like create log sinks or log buckets, read log data stored in a log bucket, or access pages like the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). If you issue a [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest) or [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) command, then your IAM roles determine whether you have the permission to run the command.

## Overview

Your IAM roles determine what actions you can perform within Logging. A [role](https://docs.cloud.google.com/iam/docs/overview#roles) is a collection of [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions). When you grant a role to a principal, you grant them all the permissions that the role contains. You can grant multiple roles to the same principal.

IAM roles are granted on a resource, such as a Google Cloud project, folder, bucket, or organization. For example, you might grant a principal the Logs Viewer role (`roles/logging.viewer`) on a particular Google Cloud project.

The Predefined roles and Logging roles sections of this page provide comprehensive information about Logging roles and permissions. Other sections of this page provide information about roles or permissions for specific use cases.

The remainder of this section summarizes how you can grant a principal access to log buckets or grant them access to only some of the log entries in a log bucket. It also describes how you can restrict access to some `LogEntry` fields.

**Note:** [Log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage) aren't used for access control. A log scope is used to define what resources to search for log data. Your IAM roles on those resources determine whether you have the permissions required to view the log data.

### Grant access to log buckets

The Logs Viewer role (`roles/logging.viewer`) lets a principal access all log data stored in the `_Required` and `_Default` log buckets, except for data access logs. If a principal needs access to data access logs, then grant the Private Logs Viewer role (`roles/logging.privateLogViewer`).

For custom log buckets, you can grant access to the `_AllLogs` view or to a custom log view. Logging automatically creates the `_AllLogs` view, which includes all log entries in the log bucket. To grant access to a log view, you add an IAM binding to the IAM policy attached to the log view or to the project. To learn more, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).

Logging also supports tags on log buckets, which can help you understand your costs. You can also use tags to prevent a user from deleting a log bucket. To learn more, see [Use tags to manage access to log buckets](https://docs.cloud.google.com/logging/docs/manage-log-buckets-with-tags).

### Grant access to some log entries in a log bucket

To grant a principal access to only some of the log entries stored in a log bucket, create a log view and then grant the principal access to the log view. For example, you might create a log view on the `_Default` log bucket that only includes log entries whose resource type is a Compute Engine instance. To learn more about creating log views and the different strategies that you can use to grant access to the view, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

### Restrict access to specific `LogEntry` fields

To restrict access to specific fields in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) data structure, configure field-level access controls on the log bucket that stores your data. For example, for your `_Default` log bucket, you can place a restriction on the `jsonPayload` of the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) data structure, and then grant your administrators access to that field. To learn more, see [Configure field-level access controls](https://docs.cloud.google.com/logging/docs/field-level-acl).

You can't restrict fields on a log bucket that has been upgraded to use Observability Analytics. Similarly, if a log bucket contains a restricted field, then you can't upgrade it to use Observability Analytics.

## Predefined roles

IAM provides predefined roles to grant granular access to specific Google Cloud resources and prevent unwanted access to other resources. Google Cloud creates and maintains these roles and automatically updates their permissions as necessary, such as when Logging adds new features.

The following table lists the predefined roles for Logging. For each role, the table displays the role title, description, contained permissions, and the lowest-level resource type where the roles can be granted. You can grant the predefined roles at the Google Cloud project level or, in most cases, any type higher in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). To restrict the Logs View Accessor role to a log view on a bucket, use [resource attributes for IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes).

To get a list of all individual permissions contained in a role, see [Getting the role metadata](https://docs.cloud.google.com/iam/docs/creating-custom-roles#getting_the_role_metadata).

Role | Permissions  
---|---  
  
#### Logging Admin 

(`roles/logging.admin`) Provides all permissions necessary to use all features of Cloud Logging.  Lowest-level resources where you can grant this role:

  * View 

|  `logging.buckets.copyLogEntries` `logging.buckets.create` `logging.buckets.createTagBinding` `logging.buckets.delete` `logging.buckets.deleteTagBinding` `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.buckets.undelete` `logging.buckets.update` `logging.exclusions.*`

  * `logging.exclusions.create`
  * `logging.exclusions.delete`
  * `logging.exclusions.get`
  * `logging.exclusions.list`
  * `logging.exclusions.update`

`logging.fields.access` `logging.links.*`

  * `logging.links.create`
  * `logging.links.delete`
  * `logging.links.get`
  * `logging.links.list`

`logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.*`

  * `logging.logEntries.create`
  * `logging.logEntries.download`
  * `logging.logEntries.list`
  * `logging.logEntries.route`

`logging.logMetrics.*`

  * `logging.logMetrics.create`
  * `logging.logMetrics.delete`
  * `logging.logMetrics.get`
  * `logging.logMetrics.list`
  * `logging.logMetrics.update`

`logging.logScopes.*`

  * `logging.logScopes.create`
  * `logging.logScopes.delete`
  * `logging.logScopes.get`
  * `logging.logScopes.list`
  * `logging.logScopes.update`

`logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.*`

  * `logging.logs.delete`
  * `logging.logs.list`

`logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`logging.operations.*`

  * `logging.operations.cancel`
  * `logging.operations.get`
  * `logging.operations.list`

`logging.privateLogEntries.list` `logging.queries.*`

  * `logging.queries.deleteShared`
  * `logging.queries.getShared`
  * `logging.queries.listShared`
  * `logging.queries.share`
  * `logging.queries.updateShared`
  * `logging.queries.usePrivate`

`logging.settings.*`

  * `logging.settings.get`
  * `logging.settings.update`

`logging.sinks.*`

  * `logging.sinks.create`
  * `logging.sinks.delete`
  * `logging.sinks.get`
  * `logging.sinks.list`
  * `logging.sinks.update`

`logging.sqlAlerts.*`

  * `logging.sqlAlerts.create`
  * `logging.sqlAlerts.update`

`logging.usage.get` `logging.views.*`

  * `logging.views.access`
  * `logging.views.create`
  * `logging.views.delete`
  * `logging.views.get`
  * `logging.views.getIamPolicy`
  * `logging.views.list`
  * `logging.views.listLogs`
  * `logging.views.listResourceKeys`
  * `logging.views.listResourceValues`
  * `logging.views.setIamPolicy`
  * `logging.views.update`

`observability.scopes.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Logs Bucket Writer 

(`roles/logging.bucketWriter`) Ability to write logs to a log bucket.  Lowest-level resources where you can grant this role:

  * Project 

|  `logging.buckets.write`  
  
#### Logs Writer 

(`roles/logging.logWriter`) Provides the permissions to write log entries.  Lowest-level resources where you can grant this role:

  * Project 

|  `logging.logEntries.create` `logging.logEntries.route`  
  
#### Private Logs Viewer 

(`roles/logging.privateLogViewer`) Provides permissions of the Logs Viewer role and in addition, provides read-only access to log entries in private logs.  Lowest-level resources where you can grant this role:

  * View 

|  `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.exclusions.get` `logging.exclusions.list` `logging.links.get` `logging.links.list` `logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.list` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.get` `logging.notificationRules.list` `logging.operations.get` `logging.operations.list` `logging.privateLogEntries.list` `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `logging.settings.get` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `logging.views.access` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `observability.scopes.get` `resourcemanager.projects.get`  
  
#### Logs Viewer 

(`roles/logging.viewer`) Provides access to view logs.  Lowest-level resources where you can grant this role:

  * View 

|  `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.exclusions.get` `logging.exclusions.list` `logging.links.get` `logging.links.list` `logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logEntries.list` `logging.logMetrics.get` `logging.logMetrics.list` `logging.logScopes.get` `logging.logScopes.list` `logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.get` `logging.notificationRules.list` `logging.operations.get` `logging.operations.list` `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `logging.settings.get` `logging.sinks.get` `logging.sinks.list` `logging.usage.get` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `observability.scopes.get` `resourcemanager.projects.get`  
  
#### Logs Configuration Writer 

(`roles/logging.configWriter`) Provides permissions to read and write the configurations of logs-based metrics and sinks for exporting logs.  Lowest-level resources where you can grant this role:

  * View 

|  `logging.buckets.create` `logging.buckets.createTagBinding` `logging.buckets.delete` `logging.buckets.deleteTagBinding` `logging.buckets.get` `logging.buckets.list` `logging.buckets.listEffectiveTags` `logging.buckets.listTagBindings` `logging.buckets.undelete` `logging.buckets.update` `logging.exclusions.*`

  * `logging.exclusions.create`
  * `logging.exclusions.delete`
  * `logging.exclusions.get`
  * `logging.exclusions.list`
  * `logging.exclusions.update`

`logging.links.*`

  * `logging.links.create`
  * `logging.links.delete`
  * `logging.links.get`
  * `logging.links.list`

`logging.locations.*`

  * `logging.locations.get`
  * `logging.locations.list`

`logging.logMetrics.*`

  * `logging.logMetrics.create`
  * `logging.logMetrics.delete`
  * `logging.logMetrics.get`
  * `logging.logMetrics.list`
  * `logging.logMetrics.update`

`logging.logScopes.*`

  * `logging.logScopes.create`
  * `logging.logScopes.delete`
  * `logging.logScopes.get`
  * `logging.logScopes.list`
  * `logging.logScopes.update`

`logging.logServiceIndexes.list` `logging.logServices.list` `logging.logs.list` `logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`logging.operations.*`

  * `logging.operations.cancel`
  * `logging.operations.get`
  * `logging.operations.list`

`logging.settings.*`

  * `logging.settings.get`
  * `logging.settings.update`

`logging.sinks.*`

  * `logging.sinks.create`
  * `logging.sinks.delete`
  * `logging.sinks.get`
  * `logging.sinks.list`
  * `logging.sinks.update`

`logging.sqlAlerts.*`

  * `logging.sqlAlerts.create`
  * `logging.sqlAlerts.update`

`logging.views.create` `logging.views.delete` `logging.views.get` `logging.views.getIamPolicy` `logging.views.list` `logging.views.update` `observability.scopes.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Log Field Accessor 

(`roles/logging.fieldAccessor`) Ability to read restricted fields in a log bucket.  Lowest-level resources where you can grant this role:

  * Project 

|  `logging.fields.access`  
  
#### Log Link Accessor 

(`roles/logging.linkViewer`) Ability to see links for a bucket.  |  `logging.links.get` `logging.links.list`  
  
#### SQL Alert Writer Beta

(`roles/logging.sqlAlertWriter`) Ability to write SQL Alerts.  |  `logging.sqlAlerts.*`

  * `logging.sqlAlerts.create`
  * `logging.sqlAlerts.update`

  
  
#### Logs View Accessor 

(`roles/logging.viewAccessor`) Ability to read logs in a view.  Lowest-level resources where you can grant this role:

  * View 

|  `logging.logEntries.download` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Logging Service Agent 

(`roles/logging.serviceAgent`) Grants a Cloud Logging Service Account the ability to create and link datasets.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.datasets.link`  
  
The following sections provide additional information to help you decide which roles apply to your principals' use cases.

### Logging roles

  * To let a user perform all actions in Logging, grant the Logging Admin (`roles/logging.admin`) role.

  * To let a user create and modify logging configurations, grant the Logs Configuration Writer (`roles/logging.configWriter`) role. This role lets you create or modify any of the following:

    * [Log sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks)
    * [Log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries)
    * [Log views](https://docs.cloud.google.com/logging/docs/logs-views)
    * [Linked data sets](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset)
    * [Log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage)
    * [Analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views)

This role isn't sufficient to create [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) or [log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts). For information about the roles required for these tasks, see Permissions for log-based metrics and Permissions for log-based alerting policies.

  * To let a user read logs in the `_Required` and `_Default` buckets or to use the **Logs Explorer** and **Observability Analytics** pages, grant one of the following roles:

    * For access to all logs in the `_Required` bucket, and access to the `_Default` view on the `_Default` bucket, grant the Logs Viewer (`roles/logging.viewer`) role.
    * For access to all logs in the `_Required` and `_Default` buckets, including data access logs, grant the Private Logs Viewer (`roles/logging.privateLogViewer`) role.
  * To let a user read logs in all log views that are in a project, grant them the IAM role of `roles/logging.viewAccessor` on the project.

  * To let a user only read logs in a specific log view, you have two options:

    * Create an IAM policy for the log view, and then add an IAM binding to that policy which grants the principal access to the log view.

    * Grant the principal the IAM role of `roles/logging.viewAccessor` on the project that contains the log view, but attach an [IAM condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to restrict the grant to the specific log view.

For information about creating log views and granting access, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).



  * To give a user access to restricted [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields, if any, in a given log bucket, grant the Logs Field Accessor (`roles/logging.fieldAccessor`) role. For more information, see [Configure field-level access](https://docs.cloud.google.com/logging/docs/field-level-acl).


  * To let a user write logs by using the Logging API, grant the Logs Writer (`roles/logging.logWriter`) role. This role doesn't grant viewing permissions.

  * To let the service account of a sink route logs to a bucket in a different Google Cloud project, grant the service account the Logs Bucket Writer (`roles/logging.bucketWriter`) role. For instructions about granting permissions to a service account, see [Set destination permissions](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-auth).




### Project-level roles

**Caution:** The following [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) include thousands of permissions across all Google Cloud services. Use these roles carefully, or consider using their corresponding Logging predefined roles.

  * To give view access to most Google Cloud services, grant the Viewer (`roles/viewer`) role.

This role includes all permissions granted by the Logs Viewer (`roles/logging.viewer`) role.

  * To give editor access to most Google Cloud services, grant the Editor (`roles/editor`) role.

This role includes all permissions granted by the Logs Viewer (`roles/logging.viewer`) role, and the permissions to write log entries, delete logs, and create log-based metrics. However, this role doesn't let users create sinks, read Data Access audit logs that are in the `_Default` bucket, or read logs that are in user-defined log buckets.

  * To give full access to most Google Cloud services, grant the Owner (`roles/owner`) role.




## Granting roles

To learn how to grant a role to a principal, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You can grant multiple roles to the same user. To get a list of the permissions contained in a role, see [Getting the role metadata](https://docs.cloud.google.com/iam/docs/creating-custom-roles#getting_the_role_metadata).

If you're trying to access a Google Cloud resource and lack the necessary permissions, then contact the principal who is listed as the **Owner** for the resource.

## Custom roles

To create a custom role with Logging permissions, do the following:

  * For a role granting permissions for the Logging API, choose permissions from API permissions, then follow the instructions to [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

  * For a role granting permissions to use the Logs Explorer, choose from permission groups in Console permissions, then follow the instructions to [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

  * For a role granting permissions to use `gcloud logging`, see the Command-line permissions section on this page, then follow the instructions to [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).




For more information about custom roles, see [Understanding IAM custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

## Cloud Logging permissions

The following table is a partial list of the permissions needed for specific features of Cloud Logging. This table can help you identify the permissions that you need to use pages like the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

In the table, `a.b.{x,y}` means `a.b.x` and `a.b.y`.

Console activity  | Required permissions  
---|---  
Minimal read-only access | `logging.logEntries.list  
logging.logs.list  
logging.logServiceIndexes.list  
logging.logServices.list  
resourcemanager.projects.get`  
View Data Access audit logs | `logging.privateLogEntries.list`  
View log-based metrics | `logging.logMetrics.{list, get}`  
View sinks | `logging.sinks.{list, get}`  
View logs usage | `logging.usage.get`  
Download logs | `logging.logEntries.{list, download}` Only one of these permissions is necessary to download logs. Roles containing the permissions to download logs must be granted at a project-level. You can't download logs if a role containing these permissions is granted in the IAM policy file of a log view.  
List and view log scopes | `logging.logScopes.{get, list}`  
View the default log scope | `observability.scopes.get`  
Exclude logs | `logging.exclusions.{list, create, get, update, delete}` When creating a custom role that includes permissions to manage exclusion filters, add the `logging.sinks.*` permissions to the role instead of adding the `logging.exclusions.*` permissions.  
Create and use sinks | `logging.sinks.{list, create, get, update, delete}` When creating a sink, you must also grant the service account an IAM role that lets it write log entries to the destination. For more information, see [ Set destination permissions](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-auth). After your log entries have been routed to a supported destination, access to the log entries is controlled entirely by IAM permissions and roles on the destination.  
Create log-based alerts | See Roles required to create and use log-based alerting policies.   
Create log-based metrics | `logging.logMetrics.{list, create, get, update, delete}` For information about other IAM roles that you need to create and use log-based metrics, see Roles required to create and use log-based metrics.  
Save and use private queries | `logging.queries.usePrivate`  
`logging.queries.{listShared,getShared}`  
Save and use shared queries | `logging.queries.{share, getShared, updateShared, deleteShared, listShared}`  
Create and manage log scopes | `logging.logScopes.{create, delete, get, list, update}`  
Set and manage the default log scope | `observability.scopes.{get, update}`  
Create and manage analytics views | `observability.analyticsViews.{create, delete, get, list, update}`  
Create [linked BigQuery datasets](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset) | `logging.links.{create, delete, get, list}` You might need additional IAM roles to query the linked BigQuery dataset. For example, these permissions don't grant you access to the BigQuery interface. For more information, see [BigQuery: Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control).  
  
## Permissions for the command-line

[`gcloud logging`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) commands are controlled by IAM permissions.

To use any of the `gcloud logging` commands, principals must have the `serviceusage.services.use` permission.

A principal must also have the IAM role that corresponds to the log's resource, and to the use case. For details, see [command-line interface permissions](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging).

## Roles required to create and use log-based metrics

Following is a summary of the common roles and permissions that a principal needs to access log-based metrics:

  * The Logs Configuration Writer (`roles/logging.configWriter`) role lets principals list, create, get, update, and delete log-based metrics.

  * The Logs Viewer (`roles/logging.viewer`) role contains permissions to view existing metrics. Specifically, a principal needs the `logging.logMetrics.get` and `logging.logMetrics.list` permissions to view existing metrics.

  * The [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) (`roles/monitoring.viewer`) role contains the permissions to read [TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) data. Specifically, a principal needs the `monitoring.timeSeries.list` permission to read time series data.

  * The Logging Admin (`roles/logging.admin`), [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`), and [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`) roles contain the permissions to create log-based metrics. Specifically, a principal needs the `logging.logMetrics.create` permission to create log-based metrics.


**Note:** To secure private logs data, such as Data Access audit logs and Access Transparency audit logs, from unauthorized access, ensure that principals are granted the minimal permissions they need to do their jobs. For example, principals that have the [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`) role can create log-based metrics with labels that can extract sensitive information.

## Roles required to create and use log-based alerting policies

This section describes the roles that you need to create log-based alerting policies, [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options), and [notification rules](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#notification-rules). Notification channels specify how Cloud Monitoring notifies you. A notification rule describes how to match incoming log entries to the alerting policy.

### Required roles

To get the permissions that you need to create log-based alerting policies, to create notification channels, and to create the associated Logging [notification rules](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#notification-rules), ask your administrator to grant you the following IAM roles on your project: 

  * [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`)
  * [Monitoring NotificationChannel Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelEditor) (`roles/monitoring.notificationChannelEditor`)
  * [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create log-based alerting policies, to create notification channels, and to create the associated Logging [notification rules](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#notification-rules). To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create log-based alerting policies, to create notification channels, and to create the associated Logging [notification rules](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#notification-rules):

  * `monitoring.alertPolicies.create`
  * `monitoring.notificationChannels.create`
  * `logging.notificationRules.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Additional required roles for Google Cloud CLI users

To get the permission that you need to create an alerting policy by using the Google Cloud CLI, ask your administrator to grant you the [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `serviceusage.services.use` permission, which is required to create an alerting policy by using the Google Cloud CLI. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Permissions for SQL-based alerting policies

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

SQL-based alerting policies evaluate the results of a SQL query run against data from groups of log entries. For information about the roles required to create and manage SQL-based alerting policies, see the [Before you begin](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting#before-you-begin) section in [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting).

## Logging access scopes

[Access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) are the legacy method of specifying permissions for the service accounts on your Compute Engine VM instances.

The following access scopes apply to the Logging API:

Access scope | Permissions granted  
---|---  
https://www.googleapis.com/auth/logging.read | `roles/logging.viewer`  
https://www.googleapis.com/auth/logging.write | `roles/logging.logWriter`  
https://www.googleapis.com/auth/logging.admin | Full access to the Logging API.  
https://www.googleapis.com/auth/cloud-platform | Full access to the Logging API and to all other enabled Google Cloud APIs.  
  
For information on using this legacy method to set your service accounts' levels of access, see [Access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
