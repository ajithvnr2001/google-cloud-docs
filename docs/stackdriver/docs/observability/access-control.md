---
url: https://docs.cloud.google.com/stackdriver/docs/observability/access-control/
title: Control access with IAM \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:23.693701+00:00
---

# Control access with IAM  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Control access with IAM Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Google Cloud project, you are the only user on the project. By default, no other users have access to your project or its resources. Identity and Access Management (IAM) manages access to Google Cloud resources, like clusters. Permissions are assigned to IAM _principals_.

IAM lets you grant [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to [principals](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity). A role is a collection of permissions, and when granted to a principal, controls access to one or more Google Cloud [resources](https://docs.cloud.google.com/iam/docs/overview#resource). You can use the following types of roles:

  * [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) provide coarse permissions limited to Owner, Editor, and Viewer.
  * [Pre-defined roles](https://docs.cloud.google.com/iam/docs/roles-permissions), provide finer-grained access than basic roles and address many common use cases.
  * [Custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) allow you to create unique combinations of permissions.



A principal can be any of the following:

  * User account
  * Service account
  * Google Workspace Google Group
  * Google Workspace domain
  * Cloud Identity domain



### IAM policy types

IAM supports the following policy types:

  * **Allow policies** : grant roles to principals. For details, see [Allow policy](https://docs.cloud.google.com/iam/docs/overview#cloud-iam-policy).
  * **Deny policies** : prevent principals from using specific IAM permissions regardless of the roles that those principals are granted. For details, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).



Use deny policies to restrict specific principals from performing specific actions in your project, folder, or organization even if an IAM allow policy grants those principals a role that contains the relevant permissions.

## Predefined roles

IAM provides predefined roles to grant granular access to specific Google Cloud resources and to prevent unwanted access to other resources. Google Cloud creates and maintains these roles and automatically updates their permissions as necessary, such as when Google Cloud Observability adds new features.

Predefined roles for Google Cloud Observability contain permissions for features that span multiple product areas. For this reason, you might see some permissions, like `observability.scopes.get`, included in predefined roles for those product areas. For example, the Logs Viewer role (`roles/logging.viewer`) includes the `observability.scopes.get` permission in addition to many logging-specific permissions.

The following table lists the predefined roles for Google Cloud Observability. For each role, the table displays the role title, description, contained permissions, and the lowest-level resource type where the roles can be granted. You can grant the predefined roles at the Google Cloud project level or, in most cases, any type higher in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

To get a list of all individual permissions contained in a role, see [Getting the role metadata](https://docs.cloud.google.com/iam/docs/creating-custom-roles#getting_the_role_metadata).

### Observability roles

Role | Permissions  
---|---  
  
#### Observability Admin 

(`roles/observability.admin`) Full access to Observability resources.  |  `observability.*`

  * `observability.analyticsViews.create`
  * `observability.analyticsViews.delete`
  * `observability.analyticsViews.get`
  * `observability.analyticsViews.list`
  * `observability.analyticsViews.update`
  * `observability.buckets.create`
  * `observability.buckets.delete`
  * `observability.buckets.get`
  * `observability.buckets.list`
  * `observability.buckets.undelete`
  * `observability.buckets.update`
  * `observability.datasets.create`
  * `observability.datasets.delete`
  * `observability.datasets.get`
  * `observability.datasets.list`
  * `observability.datasets.undelete`
  * `observability.datasets.update`
  * `observability.links.create`
  * `observability.links.delete`
  * `observability.links.get`
  * `observability.links.list`
  * `observability.links.update`
  * `observability.locations.get`
  * `observability.locations.list`
  * `observability.operations.cancel`
  * `observability.operations.delete`
  * `observability.operations.get`
  * `observability.operations.list`
  * `observability.scopes.get`
  * `observability.scopes.update`
  * `observability.settings.get`
  * `observability.settings.update`
  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`
  * `observability.views.access`
  * `observability.views.create`
  * `observability.views.delete`
  * `observability.views.get`
  * `observability.views.list`
  * `observability.views.update`

  
  
#### Observability Editor 

(`roles/observability.editor`) Edit access to Observability resources.  |  `observability.analyticsViews.*`

  * `observability.analyticsViews.create`
  * `observability.analyticsViews.delete`
  * `observability.analyticsViews.get`
  * `observability.analyticsViews.list`
  * `observability.analyticsViews.update`

`observability.buckets.create` `observability.buckets.get` `observability.buckets.list` `observability.buckets.update` `observability.datasets.create` `observability.datasets.get` `observability.datasets.list` `observability.datasets.update` `observability.links.*`

  * `observability.links.create`
  * `observability.links.delete`
  * `observability.links.get`
  * `observability.links.list`
  * `observability.links.update`

`observability.locations.*`

  * `observability.locations.get`
  * `observability.locations.list`

`observability.operations.*`

  * `observability.operations.cancel`
  * `observability.operations.delete`
  * `observability.operations.get`
  * `observability.operations.list`

`observability.scopes.*`

  * `observability.scopes.get`
  * `observability.scopes.update`

`observability.settings.*`

  * `observability.settings.get`
  * `observability.settings.update`

`observability.traceScopes.*`

  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`

`observability.views.create` `observability.views.delete` `observability.views.get` `observability.views.list` `observability.views.update`  
  
#### Observability Viewer 

(`roles/observability.viewer`) Read only access to Observability resources.  |  `observability.analyticsViews.get` `observability.analyticsViews.list` `observability.buckets.get` `observability.buckets.list` `observability.datasets.get` `observability.datasets.list` `observability.links.get` `observability.links.list` `observability.locations.*`

  * `observability.locations.get`
  * `observability.locations.list`

`observability.operations.get` `observability.operations.list` `observability.scopes.get` `observability.settings.get` `observability.traceScopes.get` `observability.traceScopes.list` `observability.views.get` `observability.views.list`  
  
#### Observability Analytics User 

(`roles/observability.analyticsUser`) Grants permissions to use Cloud Observability Analytics.  |  `logging.queries.getShared` `logging.queries.listShared` `logging.queries.usePrivate` `observability.analyticsViews.*`

  * `observability.analyticsViews.create`
  * `observability.analyticsViews.delete`
  * `observability.analyticsViews.get`
  * `observability.analyticsViews.list`
  * `observability.analyticsViews.update`

`observability.buckets.get` `observability.buckets.list` `observability.datasets.get` `observability.datasets.list` `observability.links.get` `observability.links.list` `observability.locations.*`

  * `observability.locations.get`
  * `observability.locations.list`

`observability.operations.get` `observability.operations.list` `observability.scopes.get` `observability.settings.get` `observability.traceScopes.get` `observability.traceScopes.list` `observability.views.get` `observability.views.list`  
  
#### Observability Scopes Editor 

(`roles/observability.scopesEditor`) Grants permission to view and edit Observability, Logging, Trace, and Monitoring scopes  |  `logging.logScopes.*`

  * `logging.logScopes.create`
  * `logging.logScopes.delete`
  * `logging.logScopes.get`
  * `logging.logScopes.list`
  * `logging.logScopes.update`

`monitoring.metricsScopes.link` `observability.scopes.*`

  * `observability.scopes.get`
  * `observability.scopes.update`

`observability.traceScopes.*`

  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`

  
  
#### Observability View Accessor 

(`roles/observability.viewAccessor`) Read only access to data defined by an Observability View.  |  `observability.views.access`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Observability Service Agent 

(`roles/observability.serviceAgent`) Grants Observability service account the ability to list, create and link datasets in the consumer project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.datasets.link`  
  
### Telemetry API roles

Role | Permissions  
---|---  
  
#### Telemetry Admin 

(`roles/telemetry.admin`) Admin role for telemetry  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `telemetry.*`

  * `telemetry.consumers.getIamPolicy`
  * `telemetry.consumers.setIamPolicy`
  * `telemetry.consumers.writeLogs`
  * `telemetry.consumers.writeMetrics`
  * `telemetry.consumers.writeTraces`
  * `telemetry.traces.write`

  
  
#### Telemetry Editor 

(`roles/telemetry.editor`) Editor role for telemetry  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `telemetry.traces.write`  
  
#### Consumer Admin Beta

(`roles/telemetry.consumerAdmin`) Grants permission management access to consumer resources.  |  `telemetry.consumers.getIamPolicy` `telemetry.consumers.setIamPolicy`  
  
#### Cloud Telemetry Logs Writer 

(`roles/telemetry.logsWriter`) Access to write logs.  |  `logging.logEntries.create`  
  
#### Cloud Telemetry Metrics Writer 

(`roles/telemetry.metricsWriter`) Access to write metrics.  |  `monitoring.timeSeries.create`  
  
#### Integrated Service Telemetry Logs Writer Beta

(`roles/telemetry.serviceLogsWriter`) Allows an onboarded service to write log data to a destination.  |  `telemetry.consumers.writeLogs`  
  
#### Integrated Service Telemetry Metrics Writer Beta

(`roles/telemetry.serviceMetricsWriter`) Allows an onboarded service to write metrics data to a destination.  |  `telemetry.consumers.writeMetrics`  
  
#### Integrated Service Telemetry Writer Beta

(`roles/telemetry.serviceTelemetryWriter`) Allows an onboarded service to write all telemetry data to a destination.  |  `telemetry.consumers.writeLogs` `telemetry.consumers.writeMetrics` `telemetry.consumers.writeTraces`  
  
#### Integrated Service Telemetry Traces Writer Beta

(`roles/telemetry.serviceTracesWriter`) Allows an onboarded service to write trace data to a destination.  |  `telemetry.consumers.writeTraces`  
  
#### Cloud Telemetry Traces Writer 

(`roles/telemetry.tracesWriter`) Access to write trace spans.  |  `telemetry.traces.write`  
  
#### Cloud Telemetry Writer 

(`roles/telemetry.writer`) Full access to write all telemetry data.  |  `logging.logEntries.create` `monitoring.timeSeries.create` `telemetry.traces.write`  
  
## What's next

  * [Logging: Control access with IAM](https://docs.cloud.google.com/logging/docs/access-control)
  * [Monitoring: Control access with IAM](https://docs.cloud.google.com/monitoring/access-control)
  * [Trace: Control access with IAM](https://docs.cloud.google.com/trace/docs/iam)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
