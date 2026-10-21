---
url: https://docs.cloud.google.com/monitoring/audit-logging/
title: Monitoring audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:00.677971+00:00
---

# Monitoring audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Monitoring audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Cloud Monitoring. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Monitoring audit logs use the service name `monitoring.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="monitoring.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Monitoring generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.monitoring.dashboard.v1.DashboardsService.GetDashboard`  
`google.monitoring.dashboard.v1.DashboardsService.ListDashboards`  
`google.monitoring.v3.AlertPolicyService.GetAlertPolicy`  
`google.monitoring.v3.AlertPolicyService.ListAlertPolicies`  
`google.monitoring.v3.GroupService.GetGroup`  
`google.monitoring.v3.GroupService.ListGroupMembers`  
`google.monitoring.v3.GroupService.ListGroups`  
`google.monitoring.v3.MetricService.GetMetricDescriptor`  
`google.monitoring.v3.MetricService.ListMetricDescriptors`  
`google.monitoring.v3.NotificationChannelService.GetNotificationChannel`  
`google.monitoring.v3.NotificationChannelService.GetNotificationChannelVerificationCode`  
`google.monitoring.v3.NotificationChannelService.ListNotificationChannels`  
`google.monitoring.v3.ServiceMonitoringService.GetService`  
`google.monitoring.v3.ServiceMonitoringService.GetServiceLevelObjective`  
`google.monitoring.v3.ServiceMonitoringService.ListServiceLevelObjectives`  
`google.monitoring.v3.ServiceMonitoringService.ListServices`  
`google.monitoring.v3.SnoozeService.GetSnooze`  
`google.monitoring.v3.SnoozeService.ListSnoozes`  
`google.monitoring.v3.UptimeCheckService.GetUptimeCheckConfig`  
`google.monitoring.v3.UptimeCheckService.ListUptimeCheckConfigs`  
`ADMIN_WRITE` | `google.monitoring.dashboard.v1.DashboardsService.CreateDashboard`  
`google.monitoring.dashboard.v1.DashboardsService.DeleteDashboard`  
`google.monitoring.dashboard.v1.DashboardsService.UpdateDashboard`  
`google.monitoring.metricsscope.v1.MetricsScopes.CreateMonitoredProject` (LRO)  
`google.monitoring.metricsscope.v1.MetricsScopes.DeleteMonitoredProject` (LRO)  
`google.monitoring.v3.AlertPolicyService.CreateAlertPolicy`  
`google.monitoring.v3.AlertPolicyService.DeleteAlertPolicy`  
`google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy`  
`google.monitoring.v3.GroupService.CreateGroup`  
`google.monitoring.v3.GroupService.DeleteGroup`  
`google.monitoring.v3.GroupService.UpdateGroup`  
`google.monitoring.v3.MetricService.CreateMetricDescriptor`  
`google.monitoring.v3.MetricService.DeleteMetricDescriptor`  
`google.monitoring.v3.NotificationChannelService.CreateNotificationChannel`  
`google.monitoring.v3.NotificationChannelService.DeleteNotificationChannel`  
`google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel`  
`google.monitoring.v3.NotificationChannelService.VerifyNotificationChannel`  
`google.monitoring.v3.ServiceMonitoringService.CreateService`  
`google.monitoring.v3.ServiceMonitoringService.CreateServiceLevelObjective`  
`google.monitoring.v3.ServiceMonitoringService.DeleteService`  
`google.monitoring.v3.ServiceMonitoringService.DeleteServiceLevelObjective`  
`google.monitoring.v3.ServiceMonitoringService.UpdateService`  
`google.monitoring.v3.ServiceMonitoringService.UpdateServiceLevelObjective`  
`google.monitoring.v3.SnoozeService.CreateSnooze`  
`google.monitoring.v3.SnoozeService.UpdateSnooze`  
`google.monitoring.v3.UptimeCheckService.CreateUptimeCheckConfig`  
`google.monitoring.v3.UptimeCheckService.DeleteUptimeCheckConfig`  
`google.monitoring.v3.UptimeCheckService.UpdateUptimeCheckConfig`  
`DATA_READ` | `google.monitoring.prometheus.v1.PrometheusUpstream.LabelValues`  
`google.monitoring.prometheus.v1.PrometheusUpstream.ListMetricMetadata`  
`google.monitoring.prometheus.v1.PrometheusUpstream.QueryExemplars`  
`google.monitoring.prometheus.v1.PrometheusUpstream.QueryInstant`  
`google.monitoring.prometheus.v1.PrometheusUpstream.QueryLabels`  
`google.monitoring.prometheus.v1.PrometheusUpstream.QueryRange`  
`google.monitoring.prometheus.v1.PrometheusUpstream.QuerySeries`  
`google.monitoring.v3.MetricService.ListTimeSeries`  
`google.monitoring.v3.QueryService.QueryTimeSeries`  
`DATA_WRITE` | `google.monitoring.v3.AgentTranslationService.CreateCollectdTimeSeries`  
`google.monitoring.v3.MetricService.CreateServiceTimeSeries`  
`google.monitoring.v3.MetricService.CreateTimeSeries`  
`google.monitoring.v3.NotificationChannelService.SendNotificationChannelVerificationCode`  
`OTHER` | `google.monitoring.metricsscope.v1.MetricsScopes.GetMetricsScope`: To enable this log, enable `ADMIN_READ` under the service `cloudresourcemanager.googleapis.com`.  
`google.monitoring.metricsscope.v1.MetricsScopes.ListMetricsScopesByMonitoredProject`: To enable this log, enable `ADMIN_READ` under the service `cloudresourcemanager.googleapis.com`.  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Monitoring.

### `google.monitoring.dashboard.v1.DashboardsService`

The following audit logs are associated with methods belonging to `google.monitoring.dashboard.v1.DashboardsService`.

#### `CreateDashboard`

  * **Method** : `google.monitoring.dashboard.v1.DashboardsService.CreateDashboard`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.dashboards.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.dashboard.v1.DashboardsService.CreateDashboard" `  




#### `DeleteDashboard`

  * **Method** : `google.monitoring.dashboard.v1.DashboardsService.DeleteDashboard`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.dashboards.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.dashboard.v1.DashboardsService.DeleteDashboard" `  




#### `GetDashboard`

  * **Method** : `google.monitoring.dashboard.v1.DashboardsService.GetDashboard`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.dashboards.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.dashboard.v1.DashboardsService.GetDashboard" `  




#### `ListDashboards`

  * **Method** : `google.monitoring.dashboard.v1.DashboardsService.ListDashboards`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.dashboards.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.dashboard.v1.DashboardsService.ListDashboards" `  




#### `UpdateDashboard`

  * **Method** : `google.monitoring.dashboard.v1.DashboardsService.UpdateDashboard`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.dashboards.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.dashboard.v1.DashboardsService.UpdateDashboard" `  




### `google.monitoring.metricsscope.v1.MetricsScopes`

The following audit logs are associated with methods belonging to `google.monitoring.metricsscope.v1.MetricsScopes`.

#### `CreateMonitoredProject`

  * **Method** : `google.monitoring.metricsscope.v1.MetricsScopes.CreateMonitoredProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.metricsScopes.link - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.metricsscope.v1.MetricsScopes.CreateMonitoredProject" `  




#### `DeleteMonitoredProject`

  * **Method** : `google.monitoring.metricsscope.v1.MetricsScopes.DeleteMonitoredProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.metricsScopes.link - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.metricsscope.v1.MetricsScopes.DeleteMonitoredProject" `  




#### `GetMetricsScope`

  * **Method** : `google.monitoring.metricsscope.v1.MetricsScopes.GetMetricsScope`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.metricsscope.v1.MetricsScopes.GetMetricsScope" `  




#### `ListMetricsScopesByMonitoredProject`

  * **Method** : `google.monitoring.metricsscope.v1.MetricsScopes.ListMetricsScopesByMonitoredProject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `resourcemanager.projects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.metricsscope.v1.MetricsScopes.ListMetricsScopesByMonitoredProject" `  




### `google.monitoring.prometheus.v1.PrometheusUpstream`

The following audit logs are associated with methods belonging to `google.monitoring.prometheus.v1.PrometheusUpstream`.

#### `LabelValues`

  * **Method** : `google.monitoring.prometheus.v1.PrometheusUpstream.LabelValues`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.prometheus.v1.PrometheusUpstream.LabelValues" `  




#### `ListMetricMetadata`

  * **Method** : `google.monitoring.prometheus.v1.PrometheusUpstream.ListMetricMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.prometheus.v1.PrometheusUpstream.ListMetricMetadata" `  




#### `QueryExemplars`

  * **Method** : `google.monitoring.prometheus.v1.PrometheusUpstream.QueryExemplars`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.prometheus.v1.PrometheusUpstream.QueryExemplars" `  




#### `QueryInstant`

  * **Method** : `google.monitoring.prometheus.v1.PrometheusUpstream.QueryInstant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.prometheus.v1.PrometheusUpstream.QueryInstant" `  




#### `QueryLabels`

  * **Method** : `google.monitoring.prometheus.v1.PrometheusUpstream.QueryLabels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.prometheus.v1.PrometheusUpstream.QueryLabels" `  




#### `QueryRange`

  * **Method** : `google.monitoring.prometheus.v1.PrometheusUpstream.QueryRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.prometheus.v1.PrometheusUpstream.QueryRange" `  




#### `QuerySeries`

  * **Method** : `google.monitoring.prometheus.v1.PrometheusUpstream.QuerySeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.prometheus.v1.PrometheusUpstream.QuerySeries" `  




### `google.monitoring.v3.AgentTranslationService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.AgentTranslationService`.

#### `CreateCollectdTimeSeries`

  * **Method** : `google.monitoring.v3.AgentTranslationService.CreateCollectdTimeSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.AgentTranslationService.CreateCollectdTimeSeries" `  




### `google.monitoring.v3.AlertPolicyService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.AlertPolicyService`.

#### `CreateAlertPolicy`

  * **Method** : `google.monitoring.v3.AlertPolicyService.CreateAlertPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.alertPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.AlertPolicyService.CreateAlertPolicy" `  




#### `DeleteAlertPolicy`

  * **Method** : `google.monitoring.v3.AlertPolicyService.DeleteAlertPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.alertPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.AlertPolicyService.DeleteAlertPolicy" `  




#### `GetAlertPolicy`

  * **Method** : `google.monitoring.v3.AlertPolicyService.GetAlertPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.alertPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.AlertPolicyService.GetAlertPolicy" `  




#### `ListAlertPolicies`

  * **Method** : `google.monitoring.v3.AlertPolicyService.ListAlertPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.alertPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.AlertPolicyService.ListAlertPolicies" `  




#### `UpdateAlertPolicy`

  * **Method** : `google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.alertPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy" `  




### `google.monitoring.v3.GroupService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.GroupService`.

#### `CreateGroup`

  * **Method** : `google.monitoring.v3.GroupService.CreateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.groups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.GroupService.CreateGroup" `  




#### `DeleteGroup`

  * **Method** : `google.monitoring.v3.GroupService.DeleteGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.groups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.GroupService.DeleteGroup" `  




#### `GetGroup`

  * **Method** : `google.monitoring.v3.GroupService.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.GroupService.GetGroup" `  




#### `ListGroupMembers`

  * **Method** : `google.monitoring.v3.GroupService.ListGroupMembers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.GroupService.ListGroupMembers" `  




#### `ListGroups`

  * **Method** : `google.monitoring.v3.GroupService.ListGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.groups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.GroupService.ListGroups" `  




#### `UpdateGroup`

  * **Method** : `google.monitoring.v3.GroupService.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.GroupService.UpdateGroup" `  




### `google.monitoring.v3.MetricService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.MetricService`.

#### `CreateMetricDescriptor`

  * **Method** : `google.monitoring.v3.MetricService.CreateMetricDescriptor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.metricDescriptors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.MetricService.CreateMetricDescriptor" `  




#### `CreateServiceTimeSeries`

  * **Method** : `google.monitoring.v3.MetricService.CreateServiceTimeSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.MetricService.CreateServiceTimeSeries" `  




#### `CreateTimeSeries`

  * **Method** : `google.monitoring.v3.MetricService.CreateTimeSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.MetricService.CreateTimeSeries" `  




#### `DeleteMetricDescriptor`

  * **Method** : `google.monitoring.v3.MetricService.DeleteMetricDescriptor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.metricDescriptors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.MetricService.DeleteMetricDescriptor" `  




#### `GetMetricDescriptor`

  * **Method** : `google.monitoring.v3.MetricService.GetMetricDescriptor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.metricDescriptors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.MetricService.GetMetricDescriptor" `  




#### `ListMetricDescriptors`

  * **Method** : `google.monitoring.v3.MetricService.ListMetricDescriptors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.metricDescriptors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.MetricService.ListMetricDescriptors" `  




#### `ListTimeSeries`

  * **Method** : `google.monitoring.v3.MetricService.ListTimeSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.MetricService.ListTimeSeries" `  




### `google.monitoring.v3.NotificationChannelService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.NotificationChannelService`.

#### `CreateNotificationChannel`

  * **Method** : `google.monitoring.v3.NotificationChannelService.CreateNotificationChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.notificationChannels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.CreateNotificationChannel" `  




#### `DeleteNotificationChannel`

  * **Method** : `google.monitoring.v3.NotificationChannelService.DeleteNotificationChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.notificationChannels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.DeleteNotificationChannel" `  




#### `GetNotificationChannel`

  * **Method** : `google.monitoring.v3.NotificationChannelService.GetNotificationChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.notificationChannels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.GetNotificationChannel" `  




#### `GetNotificationChannelVerificationCode`

  * **Method** : `google.monitoring.v3.NotificationChannelService.GetNotificationChannelVerificationCode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.notificationChannels.getVerificationCode - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.GetNotificationChannelVerificationCode" `  




#### `ListNotificationChannels`

  * **Method** : `google.monitoring.v3.NotificationChannelService.ListNotificationChannels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.notificationChannels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.ListNotificationChannels" `  




#### `SendNotificationChannelVerificationCode`

  * **Method** : `google.monitoring.v3.NotificationChannelService.SendNotificationChannelVerificationCode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.notificationChannels.sendVerificationCode - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.SendNotificationChannelVerificationCode" `  




#### `UpdateNotificationChannel`

  * **Method** : `google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.notificationChannels.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel" `  




#### `VerifyNotificationChannel`

  * **Method** : `google.monitoring.v3.NotificationChannelService.VerifyNotificationChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.notificationChannels.verify - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.NotificationChannelService.VerifyNotificationChannel" `  




### `google.monitoring.v3.QueryService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.QueryService`.

#### `QueryTimeSeries`

  * **Method** : `google.monitoring.v3.QueryService.QueryTimeSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.timeSeries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.QueryService.QueryTimeSeries" `  




### `google.monitoring.v3.ServiceMonitoringService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.ServiceMonitoringService`.

#### `CreateService`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.CreateService" `  




#### `CreateServiceLevelObjective`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.CreateServiceLevelObjective`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.slos.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.CreateServiceLevelObjective" `  




#### `DeleteService`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.DeleteService" `  




#### `DeleteServiceLevelObjective`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.DeleteServiceLevelObjective`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.slos.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.DeleteServiceLevelObjective" `  




#### `GetService`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.GetService" `  




#### `GetServiceLevelObjective`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.GetServiceLevelObjective`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.slos.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.GetServiceLevelObjective" `  




#### `ListServiceLevelObjectives`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.ListServiceLevelObjectives`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.slos.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.ListServiceLevelObjectives" `  




#### `ListServices`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.ListServices" `  




#### `UpdateService`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.UpdateService" `  




#### `UpdateServiceLevelObjective`

  * **Method** : `google.monitoring.v3.ServiceMonitoringService.UpdateServiceLevelObjective`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.slos.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.ServiceMonitoringService.UpdateServiceLevelObjective" `  




### `google.monitoring.v3.SnoozeService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.SnoozeService`.

#### `CreateSnooze`

  * **Method** : `google.monitoring.v3.SnoozeService.CreateSnooze`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.snoozes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.SnoozeService.CreateSnooze" `  




#### `GetSnooze`

  * **Method** : `google.monitoring.v3.SnoozeService.GetSnooze`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.snoozes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.SnoozeService.GetSnooze" `  




#### `ListSnoozes`

  * **Method** : `google.monitoring.v3.SnoozeService.ListSnoozes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.snoozes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.SnoozeService.ListSnoozes" `  




#### `UpdateSnooze`

  * **Method** : `google.monitoring.v3.SnoozeService.UpdateSnooze`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.snoozes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.SnoozeService.UpdateSnooze" `  




### `google.monitoring.v3.UptimeCheckService`

The following audit logs are associated with methods belonging to `google.monitoring.v3.UptimeCheckService`.

#### `CreateUptimeCheckConfig`

  * **Method** : `google.monitoring.v3.UptimeCheckService.CreateUptimeCheckConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.uptimeCheckConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.UptimeCheckService.CreateUptimeCheckConfig" `  




#### `DeleteUptimeCheckConfig`

  * **Method** : `google.monitoring.v3.UptimeCheckService.DeleteUptimeCheckConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.uptimeCheckConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.UptimeCheckService.DeleteUptimeCheckConfig" `  




#### `GetUptimeCheckConfig`

  * **Method** : `google.monitoring.v3.UptimeCheckService.GetUptimeCheckConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.uptimeCheckConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.UptimeCheckService.GetUptimeCheckConfig" `  




#### `ListUptimeCheckConfigs`

  * **Method** : `google.monitoring.v3.UptimeCheckService.ListUptimeCheckConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `monitoring.uptimeCheckConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.UptimeCheckService.ListUptimeCheckConfigs" `  




#### `UpdateUptimeCheckConfig`

  * **Method** : `google.monitoring.v3.UptimeCheckService.UpdateUptimeCheckConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `monitoring.uptimeCheckConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.monitoring.v3.UptimeCheckService.UpdateUptimeCheckConfig" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.monitoring.v3.NotificationChannelService.GetNotificationChannelDescriptor`
  * `google.monitoring.v3.NotificationChannelService.ListNotificationChannelDescriptors`
  * `google.monitoring.v3.UptimeCheckService.ListUptimeCheckIps`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
