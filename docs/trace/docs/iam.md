---
url: https://docs.cloud.google.com/trace/docs/iam/
title: Control access with IAM \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:09.469358+00:00
---

# Control access with IAM  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Control access with IAM Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles to grant granular permissions for viewing, writing, or managing Cloud Trace resources and preventing unauthorized access to trace data.

  * For information about granting IAM roles to a user or service account, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * For information about predefined roles, see [IAM: Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).
  * For help choosing the most appropriate predefined roles, see [Choose predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).



## Best practice

To facilitate troubleshooting, grant the [Cloud Trace User role (`roles/cloudtrace.user`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) to all people, groups, and domains that need to view trace data in a project. This role gives principals the permissions they need to view trace data.

## Permissions and predefined roles

IAM roles include permissions and can be assigned to users, groups, and service accounts.

### Cloud Trace roles

The following table lists the predefined roles for Cloud Trace, and it lists the permissions for those roles:

Role | Permissions  
---|---  
  
#### Cloud Trace Admin 

(`roles/cloudtrace.admin`) Provides full access to the Trace console and read-write access to traces.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudtrace.*`

  * `cloudtrace.insights.get`
  * `cloudtrace.insights.list`
  * `cloudtrace.stats.get`
  * `cloudtrace.tasks.create`
  * `cloudtrace.tasks.delete`
  * `cloudtrace.tasks.get`
  * `cloudtrace.tasks.list`
  * `cloudtrace.traceScopes.create`
  * `cloudtrace.traceScopes.delete`
  * `cloudtrace.traceScopes.get`
  * `cloudtrace.traceScopes.list`
  * `cloudtrace.traceScopes.update`
  * `cloudtrace.traces.get`
  * `cloudtrace.traces.list`
  * `cloudtrace.traces.patch`

`observability.scopes.get` `observability.traceScopes.*`

  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `telemetry.traces.write`  
  
#### Cloud Trace User 

(`roles/cloudtrace.user`) Provides full access to the Trace console and read access to traces.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudtrace.insights.*`

  * `cloudtrace.insights.get`
  * `cloudtrace.insights.list`

`cloudtrace.stats.get` `cloudtrace.tasks.*`

  * `cloudtrace.tasks.create`
  * `cloudtrace.tasks.delete`
  * `cloudtrace.tasks.get`
  * `cloudtrace.tasks.list`

`cloudtrace.traceScopes.*`

  * `cloudtrace.traceScopes.create`
  * `cloudtrace.traceScopes.delete`
  * `cloudtrace.traceScopes.get`
  * `cloudtrace.traceScopes.list`
  * `cloudtrace.traceScopes.update`

`cloudtrace.traces.get` `cloudtrace.traces.list` `observability.scopes.get` `observability.traceScopes.*`

  * `observability.traceScopes.create`
  * `observability.traceScopes.delete`
  * `observability.traceScopes.get`
  * `observability.traceScopes.list`
  * `observability.traceScopes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Trace Agent 

(`roles/cloudtrace.agent`) For service accounts. Provides ability to write traces by sending the data to Stackdriver Trace.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudtrace.traces.patch` `telemetry.traces.write`  
  
### Telemetry API roles

The following table lists the predefined roles for the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview), and it lists the permissions for those roles:

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
  
## Create custom roles

To create a custom role that includes Cloud Trace permissions, do the following:

  * To create a role that contains only permissions to use the Cloud Trace API, select the specific permissions required by your API calls.
  * To create a role that contains permissions to use the Cloud Trace API and the Google Cloud console, choose permission groups from one of the predefined Cloud Trace roles.
  * To grant the ability to write trace data, copy the permissions from the Cloud Trace Agent role (`roles/cloudtrace.agent`).



For more information about custom roles, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Permissions for API methods

For information about the permissions required to execute an API call, see the Cloud Trace API reference documentation:

  * [REST v1 documentation](https://docs.cloud.google.com/trace/docs/reference/v1/rest)
  * [REST v2 documentation](https://docs.cloud.google.com/trace/docs/reference/v2/rest)
  * [RPC documentation](https://docs.cloud.google.com/trace/docs/reference/v2/rpc)



## Roles for cross-project tracing

Your applications might store trace data in multiple Google Cloud projects. However, you can view this data in a single project when you do the following:

  * In the project where you want to view trace data, you configure a trace scope. To configure this scope, you must have the [Observability Scopes Editor role (`roles/observability.scopesEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor).

  * In the project where you want to view trace data and in all projects that store trace data, you have the [Cloud Trace User role (`roles/cloudtrace.user`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user).




For more information, see [View traces across projects](https://docs.cloud.google.com/trace/docs/cross-project-traces).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
