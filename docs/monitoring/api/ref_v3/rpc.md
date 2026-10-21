---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/
title: Cloud Monitoring API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:20.823190+00:00
---

# Cloud Monitoring API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Cloud Monitoring API Stay organized with collections  Save and categorize content based on your preferences. 

Manages your Cloud Monitoring data and configurations.

## Service: monitoring.googleapis.com

The Service name `monitoring.googleapis.com` is needed to create RPC client stubs.

## `[google.longrunning.Operations](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[GetOperation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
  
## `[google.monitoring.dashboard.v1.DashboardsService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardsService)`

Methods  
---  
``[CreateDashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardsService.CreateDashboard)`` |  Creates a new custom dashboard.  
``[DeleteDashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardsService.DeleteDashboard)`` |  Deletes an existing custom dashboard.  
``[GetDashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardsService.GetDashboard)`` |  Fetches a specific dashboard.  
``[ListDashboards](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardsService.ListDashboards)`` |  Lists the existing dashboards.  
``[UpdateDashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardsService.UpdateDashboard)`` |  Replaces an existing custom dashboard with a new definition.  
  
## `[google.monitoring.metricsscope.v1.MetricsScopes](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScopes)`

Methods  
---  
``[CreateMonitoredProject](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScopes.CreateMonitoredProject)`` |  Adds a `MonitoredProject` with the given project ID to the specified `Metrics Scope`.  
``[DeleteMonitoredProject](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScopes.DeleteMonitoredProject)`` |  Deletes a `MonitoredProject` from the specified `Metrics Scope`.  
``[GetMetricsScope](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScopes.GetMetricsScope)`` |  Returns a specific `Metrics Scope`, including the list of projects monitored by the specified `Metrics Scope`.  
``[ListMetricsScopesByMonitoredProject](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.metricsscope.v1#google.monitoring.metricsscope.v1.MetricsScopes.ListMetricsScopesByMonitoredProject)`` |  Returns a list of every `Metrics Scope` that a specific `MonitoredProject` has been added to.  
  
## `[google.monitoring.prometheus.v1.PrometheusUpstream](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream)`

Methods  
---  
``[LabelValues](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream.LabelValues)`` |  Lists possible values for a given label name.  
``[ListMetricMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream.ListMetricMetadata)`` |  Lists metadata for metrics.  
``[QueryExemplars](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream.QueryExemplars)`` |  Lists exemplars relevant to a given PromQL query,  
``[QueryInstant](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream.QueryInstant)`` |  Evaluate a PromQL query at a single point in time.  
``[QueryLabels](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream.QueryLabels)`` |  Lists labels for metrics.  
``[QueryRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream.QueryRange)`` |  Evaluate a PromQL query with [start, end] time range.  
``[QuerySeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream.QuerySeries)`` |  Lists metadata for metrics.  
  
## `[google.monitoring.v3.AlertPolicyService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService)`

Methods  
---  
``[CreateAlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.CreateAlertPolicy)`` |  Creates a new alerting policy.  
``[DeleteAlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.DeleteAlertPolicy)`` |  Deletes an alerting policy.  
``[GetAlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.GetAlertPolicy)`` |  Gets a single alerting policy.  
``[ListAlertPolicies](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.ListAlertPolicies)`` |  Lists the existing alerting policies for the workspace.  
``[UpdateAlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy)`` |  Updates an alerting policy.  
  
## `[google.monitoring.v3.AlertService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertService)`

Methods  
---  
``[GetAlert](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertService.GetAlert)`` |  Gets a single alert.  
``[ListAlerts](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertService.ListAlerts)`` |  Lists the existing alerts for the metrics scope of the project.  
  
## `[google.monitoring.v3.GroupService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService)`

Methods  
---  
``[CreateGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService.CreateGroup)`` |  Creates a new group.  
``[DeleteGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService.DeleteGroup)`` |  Deletes an existing group.  
``[GetGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService.GetGroup)`` |  Gets a single group.  
``[ListGroupMembers](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService.ListGroupMembers)`` |  Lists the monitored resources that are members of a group.  
``[ListGroups](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService.ListGroups)`` |  Lists the existing groups.  
``[UpdateGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService.UpdateGroup)`` |  Updates an existing group.  
  
## `[google.monitoring.v3.MetricService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService)`

Methods  
---  
``[CreateMetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.CreateMetricDescriptor)`` |  Creates a new metric descriptor.  
``[CreateTimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.CreateTimeSeries)`` |  Creates or adds data to one or more time series.  
``[DeleteMetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.DeleteMetricDescriptor)`` |  Deletes a metric descriptor.  
``[GetMetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.GetMetricDescriptor)`` |  Gets a single metric descriptor.  
``[GetMonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.GetMonitoredResourceDescriptor)`` |  Gets a single monitored resource descriptor.  
``[ListMetricDescriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.ListMetricDescriptors)`` |  Lists metric descriptors that match a filter.  
``[ListMonitoredResourceDescriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.ListMonitoredResourceDescriptors)`` |  Lists monitored resource descriptors that match a filter.  
``[ListTimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService.ListTimeSeries)`` |  Lists time series that match a filter.  
  
## `[google.monitoring.v3.NotificationChannelService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService)`

Methods  
---  
``[CreateNotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.CreateNotificationChannel)`` |  Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.  
``[DeleteNotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.DeleteNotificationChannel)`` |  Deletes a notification channel.  
``[GetNotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.GetNotificationChannel)`` |  Gets a single notification channel.  
``[GetNotificationChannelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.GetNotificationChannelDescriptor)`` |  Gets a single channel descriptor.  
``[GetNotificationChannelVerificationCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.GetNotificationChannelVerificationCode)`` |  Requests a verification code for an already verified channel that can then be used in a call to VerifyNotificationChannel() on a different channel with an equivalent identity in the same or in a different project.  
``[ListNotificationChannelDescriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.ListNotificationChannelDescriptors)`` |  Lists the descriptors for supported channel types.  
``[ListNotificationChannels](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.ListNotificationChannels)`` |  Lists the notification channels that have been created for the project.  
``[SendNotificationChannelVerificationCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.SendNotificationChannelVerificationCode)`` |  Causes a verification code to be delivered to the channel.  
``[UpdateNotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel)`` |  Updates a notification channel.  
``[VerifyNotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.VerifyNotificationChannel)`` |  Verifies a `NotificationChannel` by proving receipt of the code delivered to the channel as a result of calling `SendNotificationChannelVerificationCode`.  
  
## `[google.monitoring.v3.QueryService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryService)`

Methods  
---  
``[QueryTimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryService.QueryTimeSeries)`   
**(deprecated)**` |  Queries time series by using Monitoring Query Language (MQL).  
  
## `[google.monitoring.v3.ServiceMonitoringService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService)`

Methods  
---  
``[CreateService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.CreateService)`` |  Create a `Service`.  
``[CreateServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.CreateServiceLevelObjective)`` |  Create a `ServiceLevelObjective` for the given `Service`.  
``[DeleteService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.DeleteService)`` |  Soft delete this `Service`.  
``[DeleteServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.DeleteServiceLevelObjective)`` |  Delete the given `ServiceLevelObjective`.  
``[GetService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.GetService)`` |  Get the named `Service`.  
``[GetServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.GetServiceLevelObjective)`` |  Get a `ServiceLevelObjective` by name.  
``[ListServiceLevelObjectives](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.ListServiceLevelObjectives)`` |  List the `ServiceLevelObjective`s for the given `Service`.  
``[ListServices](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.ListServices)`` |  List `Service`s for this Metrics Scope.  
``[UpdateService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.UpdateService)`` |  Update this `Service`.  
``[UpdateServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService.UpdateServiceLevelObjective)`` |  Update the given `ServiceLevelObjective`.  
  
## `[google.monitoring.v3.SnoozeService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SnoozeService)`

Methods  
---  
``[CreateSnooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SnoozeService.CreateSnooze)`` |  Creates a `Snooze` that will prevent alerts, which match the provided criteria, from being opened.  
``[GetSnooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SnoozeService.GetSnooze)`` |  Retrieves a `Snooze` by `name`.  
``[ListSnoozes](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SnoozeService.ListSnoozes)`` |  Lists the `Snooze`s associated with a project.  
``[UpdateSnooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SnoozeService.UpdateSnooze)`` |  Updates a `Snooze`, identified by its `name`, with the parameters in the given `Snooze` object.  
  
## `[google.monitoring.v3.UptimeCheckService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService)`

Methods  
---  
``[CreateUptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService.CreateUptimeCheckConfig)`` |  Creates a new Uptime check configuration.  
``[DeleteUptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService.DeleteUptimeCheckConfig)`` |  Deletes an Uptime check configuration.  
``[GetUptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService.GetUptimeCheckConfig)`` |  Gets a single Uptime check configuration.  
``[ListUptimeCheckConfigs](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService.ListUptimeCheckConfigs)`` |  Lists the existing valid Uptime check configurations for the project (leaving out any invalid configurations).  
``[ListUptimeCheckIps](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService.ListUptimeCheckIps)`` |  Returns the list of IP addresses that checkers run from.  
``[UpdateUptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService.UpdateUptimeCheckConfig)`` |  Updates an Uptime check configuration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
