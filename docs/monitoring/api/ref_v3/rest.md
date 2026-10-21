---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/
title: Cloud Monitoring API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:10.928630+00:00
---

# Cloud Monitoring API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Cloud Monitoring API Stay organized with collections  Save and categorize content based on your preferences. 

Manages your Cloud Monitoring data and configurations.

  * REST Resource: v3.folders.timeSeries
  * REST Resource: v3.organizations.timeSeries
  * REST Resource: v3.projects.alertPolicies
  * REST Resource: v3.projects.alerts
  * REST Resource: v3.projects.groups
  * REST Resource: v3.projects.groups.members
  * REST Resource: v3.projects.metricDescriptors
  * REST Resource: v3.projects.monitoredResourceDescriptors
  * REST Resource: v3.projects.notificationChannelDescriptors
  * REST Resource: v3.projects.notificationChannels
  * REST Resource: v3.projects.snoozes
  * REST Resource: v3.projects.timeSeries
  * REST Resource: v3.projects.uptimeCheckConfigs
  * REST Resource: v3.services
  * REST Resource: v3.services.serviceLevelObjectives
  * REST Resource: v3.uptimeCheckIps
  * REST Resource: v1.locations.global.metricsScopes
  * REST Resource: v1.locations.global.metricsScopes.projects
  * REST Resource: v1.operations
  * REST Resource: v1.projects.dashboards
  * REST Resource: v1.projects.location.prometheus.api.v1
  * REST Resource: v1.projects.location.prometheus.api.v1.label
  * REST Resource: v1.projects.location.prometheus.api.v1.metadata



## Service: monitoring.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://monitoring.googleapis.com/$discovery/rest?version=v3>
  * <https://monitoring.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://monitoring.googleapis.com`



## REST Resource: [v3.folders.timeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/folders.timeSeries)

Methods  
---  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/folders.timeSeries/list)` |  `GET /v3/{name}/timeSeries`   
Lists time series that match a filter.  
  
## REST Resource: [v3.organizations.timeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/organizations.timeSeries)

Methods  
---  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/organizations.timeSeries/list)` |  `GET /v3/{name}/timeSeries`   
Lists time series that match a filter.  
  
## REST Resource: [v3.projects.alertPolicies](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create)` |  `POST /v3/{name}/alertPolicies`   
Creates a new alerting policy.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/delete)` |  `DELETE /v3/{name}`   
Deletes an alerting policy.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/get)` |  `GET /v3/{name}`   
Gets a single alerting policy.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list)` |  `GET /v3/{name}/alertPolicies`   
Lists the existing alerting policies for the workspace.  
`[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch)` |  `PATCH /v3/{alertPolicy.name}`   
Updates an alerting policy.  
  
## REST Resource: [v3.projects.alerts](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts)

Methods  
---  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/get)` |  `GET /v3/{name}`   
Gets a single alert.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/list)` |  `GET /v3/{parent}/alerts`   
Lists the existing alerts for the metrics scope of the project.  
  
## REST Resource: [v3.projects.groups](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/create)` |  `POST /v3/{name}/groups`   
Creates a new group.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/delete)` |  `DELETE /v3/{name}`   
Deletes an existing group.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/get)` |  `GET /v3/{name}`   
Gets a single group.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/list)` |  `GET /v3/{name}/groups`   
Lists the existing groups.  
`[update](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/update)` |  `PUT /v3/{group.name}`   
Updates an existing group.  
  
## REST Resource: [v3.projects.groups.members](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups.members)

Methods  
---  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups.members/list)` |  `GET /v3/{name}/members`   
Lists the monitored resources that are members of a group.  
  
## REST Resource: [v3.projects.metricDescriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create)` |  `POST /v3/{name}/metricDescriptors`   
Creates a new metric descriptor.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete)` |  `DELETE /v3/{name}`   
Deletes a metric descriptor.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/get)` |  `GET /v3/{name}`   
Gets a single metric descriptor.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list)` |  `GET /v3/{name}/metricDescriptors`   
Lists metric descriptors that match a filter.  
  
## REST Resource: [v3.projects.monitoredResourceDescriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors)

Methods  
---  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/get)` |  `GET /v3/{name}`   
Gets a single monitored resource descriptor.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list)` |  `GET /v3/{name}/monitoredResourceDescriptors`   
Lists monitored resource descriptors that match a filter.  
  
## REST Resource: [v3.projects.notificationChannelDescriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors)

Methods  
---  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/get)` |  `GET /v3/{name}`   
Gets a single channel descriptor.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list)` |  `GET /v3/{name}/notificationChannelDescriptors`   
Lists the descriptors for supported channel types.  
  
## REST Resource: [v3.projects.notificationChannels](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/create)` |  `POST /v3/{name}/notificationChannels`   
Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/delete)` |  `DELETE /v3/{name}`   
Deletes a notification channel.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/get)` |  `GET /v3/{name}`   
Gets a single notification channel.  
`[getVerificationCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/getVerificationCode)` |  `POST /v3/{name}:getVerificationCode`   
Requests a verification code for an already verified channel that can then be used in a call to VerifyNotificationChannel() on a different channel with an equivalent identity in the same or in a different project.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list)` |  `GET /v3/{name}/notificationChannels`   
Lists the notification channels that have been created for the project.  
`[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/patch)` |  `PATCH /v3/{notificationChannel.name}`   
Updates a notification channel.  
`[sendVerificationCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/sendVerificationCode)` |  `POST /v3/{name}:sendVerificationCode`   
Causes a verification code to be delivered to the channel.  
`[verify](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/verify)` |  `POST /v3/{name}:verify`   
Verifies a `NotificationChannel` by proving receipt of the code delivered to the channel as a result of calling `SendNotificationChannelVerificationCode`.  
  
## REST Resource: [v3.projects.snoozes](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes/create)` |  `POST /v3/{parent}/snoozes`   
Creates a `Snooze` that will prevent alerts, which match the provided criteria, from being opened.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes/get)` |  `GET /v3/{name}`   
Retrieves a `Snooze` by `name`.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes/list)` |  `GET /v3/{parent}/snoozes`   
Lists the `Snooze`s associated with a project.  
`[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes/patch)` |  `PATCH /v3/{snooze.name}`   
Updates a `Snooze`, identified by its `name`, with the parameters in the given `Snooze` object.  
  
## REST Resource: [v3.projects.timeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create)` |  `POST /v3/{name}/timeSeries`   
Creates or adds data to one or more time series.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list)` |  `GET /v3/{name}/timeSeries`   
Lists time series that match a filter.  
`[query](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query)   
**(deprecated)**` |  `POST /v3/{name}/timeSeries:query`   
Queries time series by using Monitoring Query Language (MQL).  
  
## REST Resource: [v3.projects.uptimeCheckConfigs](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create)` |  `POST /v3/{parent}/uptimeCheckConfigs`   
Creates a new Uptime check configuration.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/delete)` |  `DELETE /v3/{name}`   
Deletes an Uptime check configuration.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/get)` |  `GET /v3/{name}`   
Gets a single Uptime check configuration.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list)` |  `GET /v3/{parent}/uptimeCheckConfigs`   
Lists the existing valid Uptime check configurations for the project (leaving out any invalid configurations).  
`[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/patch)` |  `PATCH /v3/{uptimeCheckConfig.name}`   
Updates an Uptime check configuration.  
  
## REST Resource: [v3.services](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/create)` |  `POST /v3/{parent}/services`   
Create a `Service`.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/delete)` |  `DELETE /v3/{name}`   
Soft delete this `Service`.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/get)` |  `GET /v3/{name}`   
Get the named `Service`.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/list)` |  `GET /v3/{parent}/services`   
List `Service`s for this Metrics Scope.  
`[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/patch)` |  `PATCH /v3/{service.name}`   
Update this `Service`.  
  
## REST Resource: [v3.services.serviceLevelObjectives](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/create)` |  `POST /v3/{parent}/serviceLevelObjectives`   
Create a `ServiceLevelObjective` for the given `Service`.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/delete)` |  `DELETE /v3/{name}`   
Delete the given `ServiceLevelObjective`.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/get)` |  `GET /v3/{name}`   
Get a `ServiceLevelObjective` by name.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/list)` |  `GET /v3/{parent}/serviceLevelObjectives`   
List the `ServiceLevelObjective`s for the given `Service`.  
`[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/patch)` |  `PATCH /v3/{serviceLevelObjective.name}`   
Update the given `ServiceLevelObjective`.  
  
## REST Resource: [v3.uptimeCheckIps](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/uptimeCheckIps)

Methods  
---  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/uptimeCheckIps/list)` |  `GET /v3/uptimeCheckIps`   
Returns the list of IP addresses that checkers run from.  
  
## REST Resource: [v1.locations.global.metricsScopes](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes)

Methods  
---  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes/get)` |  `GET /v1/{name}`   
Returns a specific `Metrics Scope`, including the list of projects monitored by the specified `Metrics Scope`.  
`[listMetricsScopesByMonitoredProject](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes/listMetricsScopesByMonitoredProject)` |  `GET /v1/locations/global/metricsScopes:listMetricsScopesByMonitoredProject`   
Returns a list of every `Metrics Scope` that a specific `MonitoredProject` has been added to.  
  
## REST Resource: [v1.locations.global.metricsScopes.projects](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects/create)` |  `POST /v1/{parent}/projects`   
Adds a `MonitoredProject` with the given project ID to the specified `Metrics Scope`.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects/delete)` |  `DELETE /v1/{name}`   
Deletes a `MonitoredProject` from the specified `Metrics Scope`.  
  
## REST Resource: [v1.operations](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations)

Methods  
---  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations/get)` |  `GET /v1/{name}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.dashboards](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards)

Methods  
---  
`[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create)` |  `POST /v1/{parent}/dashboards`   
Creates a new custom dashboard.  
`[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/delete)` |  `DELETE /v1/{name}`   
Deletes an existing custom dashboard.  
`[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/get)` |  `GET /v1/{name}`   
Fetches a specific dashboard.  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/list)` |  `GET /v1/{parent}/dashboards`   
Lists the existing dashboards.  
`[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/patch)` |  `PATCH /v1/{dashboard.name}`   
Replaces an existing custom dashboard with a new definition.  
  
## REST Resource: [v1.projects.location.prometheus.api.v1](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1)

Methods  
---  
`[labels](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/labels)` |  `GET /v1/{name}/location/{location}/prometheus/api/v1/labels`   
Lists labels for metrics.  
`[query](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query)` |  `GET /v1/{name}/location/{location}/prometheus/api/v1/query`   
Evaluate a PromQL query at a single point in time.  
`[query_exemplars](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query_exemplars)` |  `GET /v1/{name}/location/{location}/prometheus/api/v1/query_exemplars`   
Lists exemplars relevant to a given PromQL query,  
`[query_range](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query_range)` |  `GET /v1/{name}/location/{location}/prometheus/api/v1/query_range`   
Evaluate a PromQL query with [start, end] time range.  
`[series](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/series)` |  `GET /v1/{name}/location/{location}/prometheus/api/v1/series`   
Lists metadata for metrics.  
  
## REST Resource: [v1.projects.location.prometheus.api.v1.label](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1.label)

Methods  
---  
`[values](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1.label/values)` |  `GET /v1/{name}/location/{location}/prometheus/api/v1/label/{label}/values`   
Lists possible values for a given label name.  
  
## REST Resource: [v1.projects.location.prometheus.api.v1.metadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1.metadata)

Methods  
---  
`[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1.metadata/list)` |  `GET /v1/{name}/location/{location}/prometheus/api/v1/metadata`   
Lists metadata for metrics.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
