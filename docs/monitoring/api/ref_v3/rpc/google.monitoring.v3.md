---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3
title: Package google.monitoring.v3 \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:24.063555+00:00
---

# Package google.monitoring.v3  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Package google.monitoring.v3 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AlertPolicyService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService)` (interface)
  * `[AlertService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertService)` (interface)
  * `[GroupService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupService)` (interface)
  * `[MetricService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MetricService)` (interface)
  * `[NotificationChannelService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService)` (interface)
  * `[QueryService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryService)` (interface)
  * `[ServiceMonitoringService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceMonitoringService)` (interface)
  * `[SnoozeService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SnoozeService)` (interface)
  * `[UptimeCheckService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckService)` (interface)
  * `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation)` (message)
  * `[Aggregation.Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation.Aligner)` (enum)
  * `[Aggregation.Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation.Reducer)` (enum)
  * `[Alert](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert)` (message)
  * `[Alert.LogMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert.LogMetadata)` (message)
  * `[Alert.PolicySnapshot](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert.PolicySnapshot)` (message)
  * `[Alert.State](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert.State)` (enum)
  * `[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)` (message)
  * `[AlertPolicy.AlertStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy)` (message)
  * `[AlertPolicy.AlertStrategy.NotificationChannelStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationChannelStrategy)` (message)
  * `[AlertPolicy.AlertStrategy.NotificationPrompt](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationPrompt)` (enum)
  * `[AlertPolicy.AlertStrategy.NotificationRateLimit](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationRateLimit)` (message)
  * `[AlertPolicy.Condition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition)` (message)
  * `[AlertPolicy.Condition.EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.EvaluationMissingData)` (enum)
  * `[AlertPolicy.Condition.LogMatch](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.LogMatch)` (message)
  * `[AlertPolicy.Condition.MetricAbsence](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MetricAbsence)` (message)
  * `[AlertPolicy.Condition.MetricThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MetricThreshold)` (message)
  * `[AlertPolicy.Condition.MetricThreshold.ForecastOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.ForecastOptions)` (message)
  * `[AlertPolicy.Condition.MonitoringQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MonitoringQueryLanguageCondition)` (message)
  * `[AlertPolicy.Condition.PrometheusQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.PrometheusQueryLanguageCondition)` (message)
  * `[AlertPolicy.Condition.SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition)` (message)
  * `[AlertPolicy.Condition.SqlCondition.BooleanTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTest)` (message)
  * `[AlertPolicy.Condition.SqlCondition.Daily](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Daily)` (message)
  * `[AlertPolicy.Condition.SqlCondition.Hourly](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Hourly)` (message)
  * `[AlertPolicy.Condition.SqlCondition.Minutes](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Minutes)` (message)
  * `[AlertPolicy.Condition.SqlCondition.RowCountTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTest)` (message)
  * `[AlertPolicy.Condition.Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.Trigger)` (message)
  * `[AlertPolicy.ConditionCombinerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.ConditionCombinerType)` (enum)
  * `[AlertPolicy.Documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Documentation)` (message)
  * `[AlertPolicy.Documentation.Link](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Documentation.Link)` (message)
  * `[AlertPolicy.Severity](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Severity)` (enum)
  * `[BasicSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.BasicSli)` (message)
  * `[BasicSli.AvailabilityCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.BasicSli.AvailabilityCriteria)` (message)
  * `[BasicSli.LatencyCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.BasicSli.LatencyCriteria)` (message)
  * `[ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ComparisonType)` (enum)
  * `[CreateAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateAlertPolicyRequest)` (message)
  * `[CreateGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateGroupRequest)` (message)
  * `[CreateMetricDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateMetricDescriptorRequest)` (message)
  * `[CreateNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateNotificationChannelRequest)` (message)
  * `[CreateServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateServiceLevelObjectiveRequest)` (message)
  * `[CreateServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateServiceRequest)` (message)
  * `[CreateSnoozeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateSnoozeRequest)` (message)
  * `[CreateTimeSeriesError](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateTimeSeriesError)` (message)
  * `[CreateTimeSeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateTimeSeriesRequest)` (message)
  * `[CreateTimeSeriesSummary](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateTimeSeriesSummary)` (message)
  * `[CreateTimeSeriesSummary.Error](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateTimeSeriesSummary.Error)` (message)
  * `[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateUptimeCheckConfigRequest)` (message)
  * `[DeleteAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteAlertPolicyRequest)` (message)
  * `[DeleteGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteGroupRequest)` (message)
  * `[DeleteMetricDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteMetricDescriptorRequest)` (message)
  * `[DeleteNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteNotificationChannelRequest)` (message)
  * `[DeleteServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteServiceLevelObjectiveRequest)` (message)
  * `[DeleteServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteServiceRequest)` (message)
  * `[DeleteUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteUptimeCheckConfigRequest)` (message)
  * `[DistributionCut](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DistributionCut)` (message)
  * `[DroppedLabels](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DroppedLabels)` (message)
  * `[GetAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetAlertPolicyRequest)` (message)
  * `[GetAlertRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetAlertRequest)` (message)
  * `[GetGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetGroupRequest)` (message)
  * `[GetMetricDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetMetricDescriptorRequest)` (message)
  * `[GetMonitoredResourceDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetMonitoredResourceDescriptorRequest)` (message)
  * `[GetNotificationChannelDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelDescriptorRequest)` (message)
  * `[GetNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelRequest)` (message)
  * `[GetNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelVerificationCodeRequest)` (message)
  * `[GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelVerificationCodeResponse)` (message)
  * `[GetServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetServiceLevelObjectiveRequest)` (message)
  * `[GetServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetServiceRequest)` (message)
  * `[GetSnoozeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetSnoozeRequest)` (message)
  * `[GetUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetUptimeCheckConfigRequest)` (message)
  * `[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Group)` (message)
  * `[GroupResourceType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupResourceType)` (enum)
  * `[InternalChecker](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.InternalChecker)` (message) **(deprecated)**
  * `[InternalChecker.State](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.InternalChecker.State)` (enum)
  * `[LabelValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.LabelValue)` (message)
  * `[ListAlertPoliciesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertPoliciesRequest)` (message)
  * `[ListAlertPoliciesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertPoliciesResponse)` (message)
  * `[ListAlertsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertsRequest)` (message)
  * `[ListAlertsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertsResponse)` (message)
  * `[ListGroupMembersRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupMembersRequest)` (message)
  * `[ListGroupMembersResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupMembersResponse)` (message)
  * `[ListGroupsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupsRequest)` (message)
  * `[ListGroupsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupsResponse)` (message)
  * `[ListMetricDescriptorsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMetricDescriptorsRequest)` (message)
  * `[ListMetricDescriptorsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMetricDescriptorsResponse)` (message)
  * `[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMonitoredResourceDescriptorsRequest)` (message)
  * `[ListMonitoredResourceDescriptorsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMonitoredResourceDescriptorsResponse)` (message)
  * `[ListNotificationChannelDescriptorsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelDescriptorsRequest)` (message)
  * `[ListNotificationChannelDescriptorsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelDescriptorsResponse)` (message)
  * `[ListNotificationChannelsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelsRequest)` (message)
  * `[ListNotificationChannelsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelsResponse)` (message)
  * `[ListServiceLevelObjectivesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServiceLevelObjectivesRequest)` (message)
  * `[ListServiceLevelObjectivesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServiceLevelObjectivesResponse)` (message)
  * `[ListServicesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServicesRequest)` (message)
  * `[ListServicesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServicesResponse)` (message)
  * `[ListSnoozesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListSnoozesRequest)` (message)
  * `[ListSnoozesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListSnoozesResponse)` (message)
  * `[ListTimeSeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListTimeSeriesRequest)` (message)
  * `[ListTimeSeriesRequest.TimeSeriesView](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListTimeSeriesRequest.TimeSeriesView)` (enum)
  * `[ListTimeSeriesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListTimeSeriesResponse)` (message)
  * `[ListUptimeCheckConfigsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckConfigsRequest)` (message)
  * `[ListUptimeCheckConfigsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckConfigsResponse)` (message)
  * `[ListUptimeCheckIpsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckIpsRequest)` (message)
  * `[ListUptimeCheckIpsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckIpsResponse)` (message)
  * `[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MutationRecord)` (message)
  * `[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)` (message)
  * `[NotificationChannel.VerificationStatus](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel.VerificationStatus)` (enum)
  * `[NotificationChannelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelDescriptor)` (message)
  * `[Point](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Point)` (message)
  * `[QueryError](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryError)` (message)
  * `[QueryErrorList](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryErrorList)` (message)
  * `[QueryTimeSeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryTimeSeriesRequest)` (message) **(deprecated)**
  * `[QueryTimeSeriesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryTimeSeriesResponse)` (message) **(deprecated)**
  * `[Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Range)` (message)
  * `[RequestBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.RequestBasedSli)` (message)
  * `[SendNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SendNotificationChannelVerificationCodeRequest)` (message)
  * `[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service)` (message)
  * `[Service.AppEngine](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.AppEngine)` (message)
  * `[Service.BasicService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.BasicService)` (message)
  * `[Service.CloudRun](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.CloudRun)` (message)
  * `[Service.ClusterIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.ClusterIstio)` (message)
  * `[Service.Custom](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.Custom)` (message)
  * `[Service.GkeNamespace](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.GkeNamespace)` (message)
  * `[Service.GkeService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.GkeService)` (message)
  * `[Service.GkeWorkload](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.GkeWorkload)` (message)
  * `[Service.IstioCanonicalService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.IstioCanonicalService)` (message)
  * `[Service.MeshIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.MeshIstio)` (message)
  * `[Service.Telemetry](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.Telemetry)` (message)
  * `[ServiceLevelIndicator](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelIndicator)` (message)
  * `[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective)` (message)
  * `[ServiceLevelObjective.View](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective.View)` (enum)
  * `[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze)` (message)
  * `[Snooze.Criteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze.Criteria)` (message)
  * `[SpanContext](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SpanContext)` (message)
  * `[SyntheticMonitorTarget](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SyntheticMonitorTarget)` (message)
  * `[SyntheticMonitorTarget.CloudFunctionV2Target](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SyntheticMonitorTarget.CloudFunctionV2Target)` (message)
  * `[TextLocator](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TextLocator)` (message)
  * `[TextLocator.Position](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TextLocator.Position)` (message)
  * `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` (message)
  * `[TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)` (message)
  * `[TimeSeriesData](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesData)` (message)
  * `[TimeSeriesData.PointData](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesData.PointData)` (message)
  * `[TimeSeriesDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesDescriptor)` (message)
  * `[TimeSeriesDescriptor.ValueDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesDescriptor.ValueDescriptor)` (message)
  * `[TimeSeriesRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesRatio)` (message)
  * `[TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TypedValue)` (message)
  * `[UpdateAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateAlertPolicyRequest)` (message)
  * `[UpdateGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateGroupRequest)` (message)
  * `[UpdateNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateNotificationChannelRequest)` (message)
  * `[UpdateServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateServiceLevelObjectiveRequest)` (message)
  * `[UpdateServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateServiceRequest)` (message)
  * `[UpdateSnoozeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateSnoozeRequest)` (message)
  * `[UpdateUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateUptimeCheckConfigRequest)` (message)
  * `[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig)` (message)
  * `[UptimeCheckConfig.CheckerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.CheckerType)` (enum)
  * `[UptimeCheckConfig.ContentMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher)` (message)
  * `[UptimeCheckConfig.ContentMatcher.ContentMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher.ContentMatcherOption)` (enum)
  * `[UptimeCheckConfig.ContentMatcher.JsonPathMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher.JsonPathMatcher)` (message)
  * `[UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption)` (enum)
  * `[UptimeCheckConfig.HttpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck)` (message)
  * `[UptimeCheckConfig.HttpCheck.BasicAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication)` (message)
  * `[UptimeCheckConfig.HttpCheck.ContentType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ContentType)` (enum)
  * `[UptimeCheckConfig.HttpCheck.RequestMethod](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.RequestMethod)` (enum)
  * `[UptimeCheckConfig.HttpCheck.ResponseStatusCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ResponseStatusCode)` (message)
  * `[UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass)` (enum)
  * `[UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication)` (message)
  * `[UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType)` (enum)
  * `[UptimeCheckConfig.PingConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.PingConfig)` (message)
  * `[UptimeCheckConfig.ResourceGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ResourceGroup)` (message)
  * `[UptimeCheckConfig.TcpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.TcpCheck)` (message)
  * `[UptimeCheckIp](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckIp)` (message)
  * `[UptimeCheckRegion](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckRegion)` (enum)
  * `[VerifyNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.VerifyNotificationChannelRequest)` (message)
  * `[WindowsBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.WindowsBasedSli)` (message)
  * `[WindowsBasedSli.MetricRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.WindowsBasedSli.MetricRange)` (message)
  * `[WindowsBasedSli.PerformanceThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.WindowsBasedSli.PerformanceThreshold)` (message)



## AlertPolicyService

The AlertPolicyService API is used to manage (list, create, delete, edit) alert policies in Cloud Monitoring. An alerting policy is a description of the conditions under which some aspect of your system is considered to be "unhealthy" and the ways to notify people or services about this state. In addition to using this API, alert policies can also be managed through [Cloud Monitoring](https://cloud.google.com/monitoring/docs/), which can be reached by clicking the "Monitoring" tab in [Cloud console](https://console.cloud.google.com/).

CreateAlertPolicy  
---  
` rpc CreateAlertPolicy(`[CreateAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateAlertPolicyRequest)`) returns (`[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)`) ` Creates a new alerting policy.Design your application to single-thread API calls that modify the state of alerting policies in a single project. This includes calls to CreateAlertPolicy, DeleteAlertPolicy and UpdateAlertPolicy.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteAlertPolicy  
---  
` rpc DeleteAlertPolicy(`[DeleteAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteAlertPolicyRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an alerting policy.Design your application to single-thread API calls that modify the state of alerting policies in a single project. This includes calls to CreateAlertPolicy, DeleteAlertPolicy and UpdateAlertPolicy.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetAlertPolicy  
---  
` rpc GetAlertPolicy(`[GetAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetAlertPolicyRequest)`) returns (`[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)`) ` Gets a single alerting policy.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListAlertPolicies  
---  
` rpc ListAlertPolicies(`[ListAlertPoliciesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertPoliciesRequest)`) returns (`[ListAlertPoliciesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertPoliciesResponse)`) ` Lists the existing alerting policies for the workspace.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateAlertPolicy  
---  
` rpc UpdateAlertPolicy(`[UpdateAlertPolicyRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateAlertPolicyRequest)`) returns (`[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)`) ` Updates an alerting policy. You can either replace the entire policy with a new one or replace only certain fields in the current alerting policy by specifying the fields to be updated via `updateMask`. Returns the updated alerting policy.Design your application to single-thread API calls that modify the state of alerting policies in a single project. This includes calls to CreateAlertPolicy, DeleteAlertPolicy and UpdateAlertPolicy.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## AlertService

The AlertService API is used to retrieve alerts from Cloud Monitoring. Alerts are a read-only resource.

GetAlert  
---  
` rpc GetAlert(`[GetAlertRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetAlertRequest)`) returns (`[Alert](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert)`) ` Gets a single alert.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListAlerts  
---  
` rpc ListAlerts(`[ListAlertsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertsRequest)`) returns (`[ListAlertsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListAlertsResponse)`) ` Lists the existing alerts for the metrics scope of the project.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## GroupService

The Group API lets you inspect and manage your groups.

A group is a named filter that is used to identify a collection of monitored resources. Groups are typically used to mirror the physical and/or logical topology of the environment. Because group membership is computed dynamically, monitored resources that are started in the future are automatically placed in matching groups. By using a group to name monitored resources in, for example, an alert policy, the target of that alert policy is updated automatically as monitored resources are added and removed from the infrastructure.

CreateGroup  
---  
` rpc CreateGroup(`[CreateGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateGroupRequest)`) returns (`[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Group)`) ` Creates a new group.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteGroup  
---  
` rpc DeleteGroup(`[DeleteGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteGroupRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an existing group.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetGroup  
---  
` rpc GetGroup(`[GetGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetGroupRequest)`) returns (`[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Group)`) ` Gets a single group.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListGroupMembers  
---  
` rpc ListGroupMembers(`[ListGroupMembersRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupMembersRequest)`) returns (`[ListGroupMembersResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupMembersResponse)`) ` Lists the monitored resources that are members of a group.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListGroups  
---  
` rpc ListGroups(`[ListGroupsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupsRequest)`) returns (`[ListGroupsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListGroupsResponse)`) ` Lists the existing groups.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateGroup  
---  
` rpc UpdateGroup(`[UpdateGroupRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateGroupRequest)`) returns (`[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Group)`) ` Updates an existing group. You can change any group attributes except `name`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## MetricService

Manages metric descriptors, monitored resource descriptors, and time series data.

CreateMetricDescriptor  
---  
` rpc CreateMetricDescriptor(`[CreateMetricDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateMetricDescriptorRequest)`) returns (`[MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)`) ` Creates a new metric descriptor. The creation is executed asynchronously. User-created metric descriptors define [custom metrics](https://cloud.google.com/monitoring/custom-metrics). The metric descriptor is updated if it already exists, except that metric labels are never removed.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateTimeSeries  
---  
` rpc CreateTimeSeries(`[CreateTimeSeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateTimeSeriesRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Creates or adds data to one or more time series. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. This method does not support [resource locations constraint of an organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations#setting_the_organization_policy).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteMetricDescriptor  
---  
` rpc DeleteMetricDescriptor(`[DeleteMetricDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteMetricDescriptorRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a metric descriptor. Only user-created [custom metrics](https://cloud.google.com/monitoring/custom-metrics) can be deleted.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetMetricDescriptor  
---  
` rpc GetMetricDescriptor(`[GetMetricDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetMetricDescriptorRequest)`) returns (`[MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)`) ` Gets a single metric descriptor.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetMonitoredResourceDescriptor  
---  
` rpc GetMonitoredResourceDescriptor(`[GetMonitoredResourceDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetMonitoredResourceDescriptorRequest)`) returns (`[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceDescriptor)`) ` Gets a single monitored resource descriptor.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListMetricDescriptors  
---  
` rpc ListMetricDescriptors(`[ListMetricDescriptorsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMetricDescriptorsRequest)`) returns (`[ListMetricDescriptorsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMetricDescriptorsResponse)`) ` Lists metric descriptors that match a filter.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListMonitoredResourceDescriptors  
---  
` rpc ListMonitoredResourceDescriptors(`[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMonitoredResourceDescriptorsRequest)`) returns (`[ListMonitoredResourceDescriptorsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListMonitoredResourceDescriptorsResponse)`) ` Lists monitored resource descriptors that match a filter.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListTimeSeries  
---  
` rpc ListTimeSeries(`[ListTimeSeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListTimeSeriesRequest)`) returns (`[ListTimeSeriesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListTimeSeriesResponse)`) ` Lists time series that match a filter.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## NotificationChannelService

The Notification Channel API provides access to configuration that controls how messages related to incidents are sent.

CreateNotificationChannel  
---  
` rpc CreateNotificationChannel(`[CreateNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateNotificationChannelRequest)`) returns (`[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)`) ` Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteNotificationChannel  
---  
` rpc DeleteNotificationChannel(`[DeleteNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteNotificationChannelRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a notification channel.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetNotificationChannel  
---  
` rpc GetNotificationChannel(`[GetNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelRequest)`) returns (`[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)`) ` Gets a single notification channel. The channel includes the relevant configuration details with which the channel was created. However, the response may truncate or omit passwords, API keys, or other private key matter and thus the response may not be 100% identical to the information that was supplied in the call to the create method.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetNotificationChannelDescriptor  
---  
` rpc GetNotificationChannelDescriptor(`[GetNotificationChannelDescriptorRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelDescriptorRequest)`) returns (`[NotificationChannelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelDescriptor)`) ` Gets a single channel descriptor. The descriptor indicates which fields are expected / permitted for a notification channel of the given type.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetNotificationChannelVerificationCode  
---  
` rpc GetNotificationChannelVerificationCode(`[GetNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelVerificationCodeRequest)`) returns (`[GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetNotificationChannelVerificationCodeResponse)`) ` Requests a verification code for an already verified channel that can then be used in a call to VerifyNotificationChannel() on a different channel with an equivalent identity in the same or in a different project. This makes it possible to copy a channel between projects without requiring manual reverification of the channel. If the channel is not in the verified state, this method will fail (in other words, this may only be used if the SendNotificationChannelVerificationCode and VerifyNotificationChannel paths have already been used to put the given channel into the verified state).There is no guarantee that the verification codes returned by this method will be of a similar structure or form as the ones that are delivered to the channel via SendNotificationChannelVerificationCode; while VerifyNotificationChannel() will recognize both the codes delivered via SendNotificationChannelVerificationCode() and returned from GetNotificationChannelVerificationCode(), it is typically the case that the verification codes delivered via SendNotificationChannelVerificationCode() will be shorter and also have a shorter expiration (e.g. codes such as "G-123456") whereas GetVerificationCode() will typically return a much longer, websafe base 64 encoded string that has a longer expiration time.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListNotificationChannelDescriptors  
---  
` rpc ListNotificationChannelDescriptors(`[ListNotificationChannelDescriptorsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelDescriptorsRequest)`) returns (`[ListNotificationChannelDescriptorsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelDescriptorsResponse)`) ` Lists the descriptors for supported channel types. The use of descriptors makes it possible for new channel types to be dynamically added.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListNotificationChannels  
---  
` rpc ListNotificationChannels(`[ListNotificationChannelsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelsRequest)`) returns (`[ListNotificationChannelsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListNotificationChannelsResponse)`) ` Lists the notification channels that have been created for the project. To list the types of notification channels that are supported, use the `ListNotificationChannelDescriptors` method.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SendNotificationChannelVerificationCode  
---  
` rpc SendNotificationChannelVerificationCode(`[SendNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SendNotificationChannelVerificationCodeRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Causes a verification code to be delivered to the channel. The code can then be supplied in `VerifyNotificationChannel` to verify the channel.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateNotificationChannel  
---  
` rpc UpdateNotificationChannel(`[UpdateNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateNotificationChannelRequest)`) returns (`[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)`) ` Updates a notification channel. Fields not specified in the field mask remain unchanged.Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
VerifyNotificationChannel  
---  
` rpc VerifyNotificationChannel(`[VerifyNotificationChannelRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.VerifyNotificationChannelRequest)`) returns (`[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)`) ` Verifies a `NotificationChannel` by proving receipt of the code delivered to the channel as a result of calling `SendNotificationChannelVerificationCode`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## QueryService

The QueryService API is used to manage time series data in Cloud Monitoring. Time series data is a collection of data points that describes the time-varying values of a metric.

QueryTimeSeries  
---  
This item is deprecated!` rpc QueryTimeSeries(`[QueryTimeSeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryTimeSeriesRequest)`) returns (`[QueryTimeSeriesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryTimeSeriesResponse)`) ` Queries time series by using Monitoring Query Language (MQL). We recommend using PromQL instead of MQL. For more information about the status of MQL, see the [MQL deprecation notice](https://cloud.google.com/stackdriver/docs/deprecations/mql).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## ServiceMonitoringService

The Cloud Monitoring Service-Oriented Monitoring API has endpoints for managing and querying aspects of a Metrics Scope's services. These include the `Service`'s monitored resources, its Service-Level Objectives, and a taxonomy of categorized Health Metrics.

CreateService  
---  
` rpc CreateService(`[CreateServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateServiceRequest)`) returns (`[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service)`) ` Create a `Service`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateServiceLevelObjective  
---  
` rpc CreateServiceLevelObjective(`[CreateServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateServiceLevelObjectiveRequest)`) returns (`[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective)`) ` Create a `ServiceLevelObjective` for the given `Service`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteService  
---  
` rpc DeleteService(`[DeleteServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteServiceRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Soft delete this `Service`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteServiceLevelObjective  
---  
` rpc DeleteServiceLevelObjective(`[DeleteServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteServiceLevelObjectiveRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete the given `ServiceLevelObjective`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetService  
---  
` rpc GetService(`[GetServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetServiceRequest)`) returns (`[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service)`) ` Get the named `Service`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetServiceLevelObjective  
---  
` rpc GetServiceLevelObjective(`[GetServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetServiceLevelObjectiveRequest)`) returns (`[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective)`) ` Get a `ServiceLevelObjective` by name.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListServiceLevelObjectives  
---  
` rpc ListServiceLevelObjectives(`[ListServiceLevelObjectivesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServiceLevelObjectivesRequest)`) returns (`[ListServiceLevelObjectivesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServiceLevelObjectivesResponse)`) ` List the `ServiceLevelObjective`s for the given `Service`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListServices  
---  
` rpc ListServices(`[ListServicesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServicesRequest)`) returns (`[ListServicesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListServicesResponse)`) ` List `Service`s for this Metrics Scope.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateService  
---  
` rpc UpdateService(`[UpdateServiceRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateServiceRequest)`) returns (`[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service)`) ` Update this `Service`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateServiceLevelObjective  
---  
` rpc UpdateServiceLevelObjective(`[UpdateServiceLevelObjectiveRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateServiceLevelObjectiveRequest)`) returns (`[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective)`) ` Update the given `ServiceLevelObjective`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## SnoozeService

The SnoozeService API is used to temporarily prevent an alert policy from generating alerts. A Snooze is a description of the criteria under which one or more alert policies should not fire alerts for the specified duration.

CreateSnooze  
---  
` rpc CreateSnooze(`[CreateSnoozeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateSnoozeRequest)`) returns (`[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze)`) ` Creates a `Snooze` that will prevent alerts, which match the provided criteria, from being opened. The `Snooze` applies for a specific time interval.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetSnooze  
---  
` rpc GetSnooze(`[GetSnoozeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetSnoozeRequest)`) returns (`[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze)`) ` Retrieves a `Snooze` by `name`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListSnoozes  
---  
` rpc ListSnoozes(`[ListSnoozesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListSnoozesRequest)`) returns (`[ListSnoozesResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListSnoozesResponse)`) ` Lists the `Snooze`s associated with a project. Can optionally pass in `filter`, which specifies predicates to match `Snooze`s.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateSnooze  
---  
` rpc UpdateSnooze(`[UpdateSnoozeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateSnoozeRequest)`) returns (`[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze)`) ` Updates a `Snooze`, identified by its `name`, with the parameters in the given `Snooze` object.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## UptimeCheckService

The UptimeCheckService API is used to manage (list, create, delete, edit) Uptime check configurations in the Cloud Monitoring product. An Uptime check is a piece of configuration that determines which resources and services to monitor for availability. These configurations can also be configured interactively by navigating to the [Cloud console](https://console.cloud.google.com), selecting the appropriate project, clicking on "Monitoring" on the left-hand side to navigate to Cloud Monitoring, and then clicking on "Uptime".

CreateUptimeCheckConfig  
---  
` rpc CreateUptimeCheckConfig(`[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateUptimeCheckConfigRequest)`) returns (`[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig)`) ` Creates a new Uptime check configuration.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteUptimeCheckConfig  
---  
` rpc DeleteUptimeCheckConfig(`[DeleteUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DeleteUptimeCheckConfigRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an Uptime check configuration. Note that this method will fail if the Uptime check configuration is referenced by an alert policy or other dependent configs that would be rendered invalid by the deletion.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetUptimeCheckConfig  
---  
` rpc GetUptimeCheckConfig(`[GetUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GetUptimeCheckConfigRequest)`) returns (`[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig)`) ` Gets a single Uptime check configuration.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListUptimeCheckConfigs  
---  
` rpc ListUptimeCheckConfigs(`[ListUptimeCheckConfigsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckConfigsRequest)`) returns (`[ListUptimeCheckConfigsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckConfigsResponse)`) ` Lists the existing valid Uptime check configurations for the project (leaving out any invalid configurations).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListUptimeCheckIps  
---  
` rpc ListUptimeCheckIps(`[ListUptimeCheckIpsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckIpsRequest)`) returns (`[ListUptimeCheckIpsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListUptimeCheckIpsResponse)`) ` Returns the list of IP addresses that checkers run from.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateUptimeCheckConfig  
---  
` rpc UpdateUptimeCheckConfig(`[UpdateUptimeCheckConfigRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UpdateUptimeCheckConfigRequest)`) returns (`[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig)`) ` Updates an Uptime check configuration. You can either replace the entire configuration with a new one or replace only certain fields in the current configuration by specifying the fields to be updated via `updateMask`. Returns the updated configuration.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Aggregation

Describes how to combine multiple time series to provide a different view of the data. Aggregation of time series is done in two steps. First, each time series in the set is _aligned_ to the same time interval boundaries, then the set of time series is optionally _reduced_ in number.

Alignment consists of applying the `per_series_aligner` operation to each time series after its data has been divided into regular `alignment_period` time intervals. This process takes _all_ of the data points in an alignment period, applies a mathematical transformation such as averaging, minimum, maximum, delta, etc., and converts them into a single data point per period.

Reduction is when the aligned and transformed time series can optionally be combined, reducing the number of time series through similar mathematical transformations. Reduction involves applying a `cross_series_reducer` to all the time series, optionally sorting the time series into subsets with `group_by_fields`, and applying the reducer to each subset.

The raw time series data can contain a huge amount of information from multiple sources. Alignment and reduction transforms this mass of data into a more manageable and representative collection of data, for example "the 95% latency across the average of all tasks in a cluster". This representative data can be more easily graphed and comprehended, and the individual time series data is still available for later drilldown. For more details, see [Filtering and aggregation](https://cloud.google.com/monitoring/api/v3/aggregation).

Fields  
---  
`alignment_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The `alignment_period` specifies a time interval, in seconds, that is used to divide the data in all the `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)` into consistent blocks of time. This will be done before the per-series aligner can be applied to the data.The value must be at least 60 seconds. If a per-series aligner other than `ALIGN_NONE` is specified, this field is required or an error is returned. If no per-series aligner is specified, or the aligner `ALIGN_NONE` is specified, then this field is ignored.The maximum value of the `alignment_period` is 104 weeks (2 years) for charts, and 90,000 seconds (25 hours) for alerting policies.  
`per_series_aligner` |  `[Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation.Aligner)` An `Aligner` describes how to bring the data points in a single time series into temporal alignment. Except for `ALIGN_NONE`, all alignments cause all the data points in an `alignment_period` to be mathematically grouped together, resulting in a single data point for each `alignment_period` with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the `metric_kind` and `value_type` of the original time series. Alignment can change the `metric_kind` or the `value_type` of the time series.Time series data must be aligned in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified and not equal to `ALIGN_NONE` and `alignment_period` must be specified; otherwise, an error is returned.  
`cross_series_reducer` |  `[Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation.Reducer)` The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the `metric_kind` and the `value_type` of the original time series. Reduction can yield a time series with a different `metric_kind` or `value_type` than the input time series.Time series data must first be aligned (see `per_series_aligner`) in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified, and must not be `ALIGN_NONE`. An `alignment_period` must also be specified; otherwise, an error is returned.  
`group_by_fields[]` |  `string` The set of fields to preserve when `cross_series_reducer` is specified. The `group_by_fields` determine how the time series are partitioned into subsets prior to applying the aggregation operation. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The `cross_series_reducer` is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains `resource.type`. Fields not specified in `group_by_fields` are aggregated away. If `group_by_fields` is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If `cross_series_reducer` is not defined, this field is ignored.  
  
## Aligner

The `Aligner` specifies the operation that will be applied to the data points in each alignment period in a time series. Except for `ALIGN_NONE`, which specifies that no operation be applied, each alignment operation replaces the set of data values in each alignment period with a single value: the result of applying the operation to the data values. An aligned time series has a single data value at the end of each `alignment_period`.

An alignment operation can change the data type of the values, too. For example, if you apply a counting operation to boolean values, the data `value_type` in the original time series is `BOOLEAN`, but the `value_type` in the aligned result is `INT64`.

Enums  
---  
`ALIGN_NONE` | No alignment. Raw data is returned. Not valid if cross-series reduction is requested. The `value_type` of the result is the same as the `value_type` of the input.  
`ALIGN_DELTA` | Align and convert to `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.DELTA)`. The output is `delta = y1 - y0`.This alignment is valid for `[CUMULATIVE](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.CUMULATIVE)` and `DELTA` metrics. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_RATE` | Align and convert to a rate. The result is computed as `rate = (y1 - y0)/(t1 - t0)`, or "delta over time". Think of this aligner as providing the slope of the line that passes through the value at the start and at the end of the `alignment_period`.This aligner is valid for `CUMULATIVE` and `DELTA` metrics with numeric values. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The output is a `GAUGE` metric with `value_type` `DOUBLE`.If, by "rate", you mean "percentage change", see the `ALIGN_PERCENT_CHANGE` aligner instead.  
`ALIGN_INTERPOLATE` | Align by interpolating between adjacent points around the alignment period boundary. This aligner is valid for `GAUGE` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_NEXT_OLDER` | Align by moving the most recent data point before the end of the alignment period to the boundary at the end of the alignment period. This aligner is valid for `GAUGE` metrics. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MIN` | Align the time series by returning the minimum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MAX` | Align the time series by returning the maximum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MEAN` | Align the time series by returning the mean value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is `DOUBLE`.  
`ALIGN_COUNT` | Align the time series by returning the number of values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric or Boolean values. The `value_type` of the aligned result is `INT64`.  
`ALIGN_SUM` | Align the time series by returning the sum of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric and distribution values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_STDDEV` | Align the time series by returning the standard deviation of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the output is `DOUBLE`.  
`ALIGN_COUNT_TRUE` | Align the time series by returning the number of `True` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `value_type` of the output is `INT64`.  
`ALIGN_COUNT_FALSE` | Align the time series by returning the number of `False` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `value_type` of the output is `INT64`.  
`ALIGN_FRACTION_TRUE` | Align the time series by returning the ratio of the number of `True` values to the total number of values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The output value is in the range [0.0, 1.0] and has `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_99` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 99th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_95` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 95th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_50` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 50th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_05` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 5th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENT_CHANGE` | Align and convert to a percentage change. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. This alignment returns `((current - previous)/previous) * 100`, where the value of `previous` is determined based on the `alignment_period`.If the values of `current` and `previous` are both 0, then the returned value is 0. If only `previous` is 0, the returned value is infinity.A 10-minute moving mean is computed at each point of the alignment period prior to the above calculation to smooth the metric and prevent false positives from very short-lived spikes. The moving mean is only applicable for data whose values are `>= 0`. Any values `< 0` are treated as a missing datapoint, and are ignored. While `DELTA` metrics are accepted by this alignment, special care should be taken that the values for the metric will always be positive. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
  
## Reducer

A Reducer operation describes how to aggregate data points from multiple time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.

Enums  
---  
`REDUCE_NONE` | No cross-time series reduction. The output of the `Aligner` is returned.  
`REDUCE_MEAN` | Reduce by computing the mean value across time series for each alignment period. This reducer is valid for `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.DELTA)` and `[GAUGE](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.GAUGE)` metrics with numeric or distribution values. The `value_type` of the output is `[DOUBLE](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.ValueType.ENUM_VALUES.google.api.MetricDescriptor.ValueType.DOUBLE)`.  
`REDUCE_MIN` | Reduce by computing the minimum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_MAX` | Reduce by computing the maximum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_SUM` | Reduce by computing the sum across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric and distribution values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_STDDEV` | Reduce by computing the standard deviation across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric or distribution values. The `value_type` of the output is `DOUBLE`.  
`REDUCE_COUNT` | Reduce by computing the number of data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of numeric, Boolean, distribution, and string `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_COUNT_TRUE` | Reduce by computing the number of `True`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_COUNT_FALSE` | Reduce by computing the number of `False`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_FRACTION_TRUE` | Reduce by computing the ratio of the number of `True`-valued data points to the total number of data points for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The output value is in the range [0.0, 1.0] and has `value_type` `DOUBLE`.  
`REDUCE_PERCENTILE_99` | Reduce by computing the [99th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_95` | Reduce by computing the [95th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_50` | Reduce by computing the [50th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_05` | Reduce by computing the [5th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
  
## Alert

An alert is the representation of a violation of an alert policy. It is a read-only resource that cannot be modified by the accompanied API.

Fields  
---  
`name` |  `string` Identifier. The name of the alert.The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alerts/[ALERT_ID]
    

The `[ALERT_ID]` is a system-assigned unique identifier for the alert.  
`state` |  `[State](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert.State)` Output only. The current state of the alert.  
`open_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time when the alert was opened.  
`close_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time when the alert was closed.  
`resource` |  `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` The monitored resource type and any monitored resource labels preserved from the incident's generating condition.  
`metadata` |  `[MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceMetadata)` The metadata of the monitored resource.  
`metric` |  `[Metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Metric)` The metric type and any metric labels preserved from the incident's generating condition.  
`log` |  `[LogMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert.LogMetadata)` The log information associated with the alert. This field is only populated for log-based alerts.  
`policy` |  `[PolicySnapshot](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert.PolicySnapshot)` The snapshot of the alert policy that generated this alert.  
  
## LogMetadata

Information about the log for log-based alerts.

Fields  
---  
`extracted_labels` |  `map<string, string>` The labels extracted from the log.  
  
## PolicySnapshot

The state of the policy at the time the alert was generated.

Fields  
---  
`name` |  `string` The name of the alert policy resource. In the form of "projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]".  
`display_name` |  `string` The display name of the alert policy.  
`severity` |  `[Severity](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Severity)` The severity of the alert policy.  
`user_labels` |  `map<string, string>` The user labels for the alert policy.  
  
## State

The enumeration of possible states for an alert.

Enums  
---  
`STATE_UNSPECIFIED` | The alert state is unspecified.  
`OPEN` | The alert is open.  
`CLOSED` | The alert is closed.  
  
## AlertPolicy

A description of the conditions under which some aspect of your system is considered to be "unhealthy" and the ways to notify people or services about this state. For an overview of alerting policies, see [Introduction to Alerting](https://cloud.google.com/monitoring/alerts/).

Fields  
---  
`name` |  `string` Identifier. Required if the policy exists. The resource name for this policy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
    

`[ALERT_POLICY_ID]` is assigned by Cloud Monitoring when the policy is created. When calling the `[alertPolicies.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.CreateAlertPolicy)` method, do not include the `name` field in the alerting policy passed as part of the request.  
`display_name` |  `string` A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters.The convention for the display_name of a PrometheusQueryLanguageCondition is "{rule group name}/{alert name}", where the {rule group name} and {alert name} should be taken from the corresponding Prometheus configuration file. This convention is not enforced. In any case the display_name is not a unique key of the AlertPolicy.  
`documentation` |  `[Documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Documentation)` Documentation that is included with notifications and incidents related to this policy. Best practice is for the documentation to include information to help responders understand, mitigate, escalate, and correct the underlying problems detected by the alerting policy. Notification channels that have limited capacity might not show this documentation.  
`user_labels` |  `map<string, string>` User-supplied key/value data to be used for organizing and identifying the `AlertPolicy` objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.Note that Prometheus {alert name} is a [valid Prometheus label names](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels), whereas Prometheus {rule group} is an unrestricted UTF-8 string. This means that they cannot be stored as-is in user labels, because they may contain characters that are not allowed in user-label values.  
`conditions[]` |  `[Condition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition)` A list of conditions for the policy. The conditions are combined by AND or OR according to the `combiner` field. If the combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions. If `condition_time_series_query_language` is present, it must be the only `condition`. If `condition_monitoring_query_language` is present, it must be the only `condition`.  
`combiner` |  `[ConditionCombinerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.ConditionCombinerType)` How to combine the results of multiple conditions to determine if an incident should be opened. If `condition_time_series_query_language` is present, this must be `COMBINE_UNSPECIFIED`.  
`enabled` |  `[BoolValue](https://protobuf.dev/reference/protobuf/google.protobuf/#bool-value)` Whether or not the policy is enabled. On write, the default interpretation if unset is that the policy is enabled. On read, clients should not make any assumption about the state if it has not been populated. The field should always be populated on List and Get operations, unless a field projection has been specified that strips it out.  
`validity` |  `[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.rpc#google.rpc.Status)` Read-only description of how the alerting policy is invalid. This field is only set when the alerting policy is invalid. An invalid alerting policy will not generate incidents.  
`notification_channels[]` |  `string` Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the `name` field in each of the `[`NotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)` objects that are returned from the `[`ListNotificationChannels`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.ListNotificationChannels)` method. The format of the entries in this field is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
      
  
`creation_record` |  `[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MutationRecord)` A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be ignored.  
`mutation_record` |  `[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MutationRecord)` A read-only record of the most recent change to the alerting policy. If provided in a call to create or update, this field will be ignored.  
`alert_strategy` |  `[AlertStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy)` Control over how this alerting policy's notification channels are notified.  
`severity` |  `[Severity](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Severity)` Optional. The severity of an alerting policy indicates how important incidents generated by that policy are. The severity level will be displayed on the Incident detail page and in notifications.  
  
## AlertStrategy

Control over how the notification channels in `notification_channels` are notified when this alert fires.

Fields  
---  
`notification_rate_limit` |  `[NotificationRateLimit](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationRateLimit)` Required for log-based alerting policies, i.e. policies with a `LogMatch` condition.This limit is not implemented for alerting policies that do not have a LogMatch condition.  
`notification_prompts[]` |  `[NotificationPrompt](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationPrompt)` For log-based alert policies, the notification prompts is always [OPENED]. For non log-based alert policies, the notification prompts can be [OPENED] or [OPENED, CLOSED].  
`auto_close` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` If an alerting policy that was active has no data for this long, any open incidents will close  
`notification_channel_strategy[]` |  `[NotificationChannelStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationChannelStrategy)` Control how notifications will be sent out, on a per-channel basis.  
  
## NotificationChannelStrategy

Control over how the notification channels in `notification_channels` are notified when this alert fires, on a per-channel basis.

Fields  
---  
`notification_channel_names[]` |  `string` The full REST resource name for the notification channels that these settings apply to. Each of these correspond to the name field in one of the NotificationChannel objects referenced in the notification_channels field of this AlertPolicy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
      
  
`renotify_interval` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The frequency at which to send reminder notifications for open incidents. The value must be between 30 minutes and 24 hours.  
  
## NotificationPrompt

Control when notifications will be sent out.

Enums  
---  
`NOTIFICATION_PROMPT_UNSPECIFIED` | No strategy specified. Treated as error.  
`OPENED` | Notify when an incident is opened.  
`CLOSED` | Notify when an incident is closed.  
  
## NotificationRateLimit

Control over the rate of notifications sent to this alerting policy's notification channels.

Fields  
---  
`period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Not more than one notification per `period`.  
  
## Condition

A condition is a true/false test that determines when an alerting policy should open an incident. If a condition evaluates to true, it signifies that something is wrong.

Fields  
---  
`name` |  `string` Required if the condition exists. The unique resource name for this condition. Its format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
    

`[CONDITION_ID]` is assigned by Cloud Monitoring when the condition is created as part of a new or updated alerting policy.When calling the `[alertPolicies.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.CreateAlertPolicy)` method, do not include the `name` field in the conditions of the requested alerting policy. Cloud Monitoring creates the condition identifiers and includes them in the new policy.When calling the `[alertPolicies.update](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy)` method to update a policy, including a condition `name` causes the existing condition to be updated. Conditions without names are added to the updated policy. Existing conditions are deleted if they are not updated.Best practice is to preserve `[CONDITION_ID]` if you make only small changes, such as those to condition thresholds, durations, or trigger values. Otherwise, treat the change as a new condition and let the existing condition be deleted.  
`display_name` |  `string` A short name or phrase used to identify the condition in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple conditions in the same policy.  
Union field `condition`. Only one of the following condition types will be specified. `condition` can be only one of the following:  
`condition_threshold` |  `[MetricThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MetricThreshold)` A condition that compares a time series against a threshold.  
`condition_absent` |  `[MetricAbsence](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MetricAbsence)` A condition that checks that a time series continues to receive new data points.  
`condition_matched_log` |  `[LogMatch](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.LogMatch)` A condition that checks for log messages matching given constraints. If set, no other conditions can be present.  
`condition_monitoring_query_language` |  `[MonitoringQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MonitoringQueryLanguageCondition)` A condition that uses the Monitoring Query Language to define alerts.  
`condition_prometheus_query_language` |  `[PrometheusQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.PrometheusQueryLanguageCondition)` A condition that uses the Prometheus query language to define alerts.  
`condition_sql` |  `[SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition)` A condition that periodically evaluates a SQL query result.  
  
## EvaluationMissingData

A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. This control doesn't affect metric-absence policies.

Enums  
---  
`EVALUATION_MISSING_DATA_UNSPECIFIED` | An unspecified evaluation missing data option. Equivalent to EVALUATION_MISSING_DATA_NO_OP.  
`EVALUATION_MISSING_DATA_INACTIVE` | If there is no data to evaluate the condition, then evaluate the condition as false.  
`EVALUATION_MISSING_DATA_ACTIVE` | If there is no data to evaluate the condition, then evaluate the condition as true.  
`EVALUATION_MISSING_DATA_NO_OP` | Do not evaluate the condition to any value if there is no data.  
  
## LogMatch

A condition type that checks whether a log message in the [scoping project](https://cloud.google.com/monitoring/api/v3#project_name) satisfies the given filter. Logs from other projects in the metrics scope are not evaluated.

Fields  
---  
`filter` |  `string` Required. A logs-based filter. See [Advanced Logs Queries](https://cloud.google.com/logging/docs/view/advanced-queries) for how this filter should be constructed.  
`label_extractors` |  `map<string, string>` Optional. A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match `filter`. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition.Please see [the documentation on logs-based metric `valueExtractor`s](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric.FIELDS.value_extractor) for syntax and examples.  
  
## MetricAbsence

A condition type that checks that monitored resources are reporting data. The configuration defines a metric and a set of monitored resources. The predicate is considered in violation when a time series for the specified metric of a monitored resource does not include any data in the specified `duration`.

Fields  
---  
`filter` |  `string` Required. A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) (that call is useful to verify the time series that will be retrieved / processed). The filter must specify the metric type and the resource type. Optionally, it can specify resource labels and metric labels. This field must not exceed 2048 Unicode characters in length.  
`aggregations[]` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.This field is similar to the one in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). It is advisable to use the `ListTimeSeries` method when debugging this field.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Required. The amount of time that a time series must fail to report new data to be considered failing. The minimum value of this field is 120 seconds. Larger values that are a multiple of a minute--for example, 240 or 300 seconds--are supported. If an invalid value is given, an error will be returned.  
`trigger` |  `[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.Trigger)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`.  
  
## MetricThreshold

A condition type that compares a collection of time series against a threshold.

Fields  
---  
`filter` |  `string` Required. A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) (that call is useful to verify the time series that will be retrieved / processed). The filter must specify the metric type and the resource type. Optionally, it can specify resource labels and metric labels. This field must not exceed 2048 Unicode characters in length.  
`aggregations[]` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.This field is similar to the one in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). It is advisable to use the `ListTimeSeries` method when debugging this field.  
`denominator_filter` |  `string` A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a `denominator_filter` is specified, the time series specified by the `filter` field will be used as the numerator.The filter must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.  
`denominator_aggregations[]` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation)` Specifies the alignment of data points in individual time series selected by `denominatorFilter` as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources).When computing ratios, the `aggregations` and `denominator_aggregations` fields must use the same alignment period and produce time series that have the same periodicity and labels.  
`forecast_options` |  `[ForecastOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.ForecastOptions)` When this field is present, the `MetricThreshold` condition forecasts whether the time series is predicted to violate the threshold within the `forecast_horizon`. When this field is not set, the `MetricThreshold` tests the current value of the timeseries against the threshold.  
`comparison` |  `[ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ComparisonType)` The comparison to apply between the time series (indicated by `filter` and `aggregation`) and the threshold (indicated by `threshold_value`). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side.Only `COMPARISON_LT` and `COMPARISON_GT` are supported currently.  
`threshold_value` |  `double` A value against which to compare the time series.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Required. The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the `aggregations` field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly.  
`trigger` |  `[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.Trigger)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`, or by the ratio, if `denominator_filter` and `denominator_aggregations` are specified.  
`evaluation_missing_data` |  `[EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.EvaluationMissingData)` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. To use this control, the value of the `duration` field must be greater than or equal to 60 seconds.  
  
## ForecastOptions

Options used when forecasting the time series and testing the predicted value against the threshold.

Fields  
---  
`forecast_horizon` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Required. The length of time into the future to forecast whether a time series will violate the threshold. If the predicted value is found to violate the threshold, and the violation is observed in all forecasts made for the configured `duration`, then the time series is considered to be failing. The forecast horizon can range from 1 hour to 60 hours.  
  
## MonitoringQueryLanguageCondition

A condition type that allows alerting policies to be defined using [Monitoring Query Language](https://cloud.google.com/monitoring/mql).

Fields  
---  
`query` |  `string` [Monitoring Query Language](https://cloud.google.com/monitoring/mql) query that outputs a boolean stream.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the `aggregations` field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. The default value is zero.  
`trigger` |  `[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.Trigger)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`, or by the ratio, if `denominator_filter` and `denominator_aggregations` are specified.  
`evaluation_missing_data` |  `[EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.EvaluationMissingData)` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving.  
  
## PrometheusQueryLanguageCondition

A condition type that allows alerting policies to be defined using [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/).

The PrometheusQueryLanguageCondition message contains information from a Prometheus alerting rule and its associated rule group.

A Prometheus alerting rule is described [here](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/). The semantics of a Prometheus alerting rule is described [here](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule).

A Prometheus rule group is described [here](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/). The semantics of a Prometheus rule group is described [here](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule_group).

Because Cloud Alerting has no representation of a Prometheus rule group resource, we must embed the information of the parent rule group inside each of the conditions that refer to it. We must also update the contents of all Prometheus alerts in case the information of their rule group changes.

The PrometheusQueryLanguageCondition protocol buffer combines the information of the corresponding rule group and alerting rule. The structure of the PrometheusQueryLanguageCondition protocol buffer does NOT mimic the structure of the Prometheus rule group and alerting rule YAML declarations. The PrometheusQueryLanguageCondition protocol buffer may change in the future to support future rule group and/or alerting rule features. There are no new such features at the present time (2023-06-26).

Fields  
---  
`query` |  `string` Required. The PromQL expression to evaluate. Every evaluation cycle this expression is evaluated at the current time, and all resultant time series become pending/firing alerts. This field must not be empty.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Alerts are considered firing once their PromQL expression was evaluated to be "true" for this long. Alerts whose PromQL expression was not evaluated to be "true" for long enough are considered pending. Must be a non-negative duration or missing. This field is optional. Its default value is zero.  
`evaluation_interval` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. How often this rule should be evaluated. Must be a positive multiple of 30 seconds or missing. This field is optional. Its default value is 30 seconds. If this PrometheusQueryLanguageCondition was generated from a Prometheus alerting rule, then this value should be taken from the enclosing rule group.  
`labels` |  `map<string, string>` Optional. Labels to add to or overwrite in the PromQL query result. Label names [must be valid](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels). Label values can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars). The only available variable names are the names of the labels in the PromQL result, including "__name__" and "value". "labels" may be empty.  
`rule_group` |  `string` Optional. The rule group name of this alert in the corresponding Prometheus configuration file.Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future.This field is optional. If this field is not empty, then it must contain a valid UTF-8 string. This field may not exceed 2048 Unicode characters in length.  
`alert_rule` |  `string` Optional. The alerting rule name of this alert in the corresponding Prometheus configuration file.Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future.This field is optional. If this field is not empty, then it must be a [valid Prometheus label name](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels). This field may not exceed 2048 Unicode characters in length.  
`disable_metric_validation` |  `bool` Optional. Whether to disable metric existence validation for this condition.This allows alerting policies to be defined on metrics that do not yet exist, improving advanced customer workflows such as configuring alerting policies using Terraform.Users with the `monitoring.alertPolicyViewer` role are able to see the name of the non-existent metric in the alerting policy condition.  
  
## SqlCondition

A condition that allows alerting policies to be defined using GoogleSQL. SQL conditions examine a sliding window of logs using GoogleSQL. Alert policies with SQL conditions may incur additional billing.

Fields  
---  
`query` |  `string` Required. The Log Analytics SQL query to run, as a string. The query must conform to the required shape. Specifically, the query must not try to filter the input by time. A filter will automatically be applied to filter the input so that the query receives all rows received since the last time the query was run.For example, the following query extracts all log entries containing an HTTP request:
    
    
    SELECT
      timestamp, log_name, severity, http_request, resource, labels
    FROM
      my-project.global._Default._AllLogs
    WHERE
      http_request IS NOT NULL
      
  
Union field `schedule`. The schedule indicates how often the query should be run. `schedule` can be only one of the following:  
`minutes` |  `[Minutes](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Minutes)` Schedule the query to execute every so many minutes.  
`hourly` |  `[Hourly](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Hourly)` Schedule the query to execute every so many hours.  
`daily` |  `[Daily](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.Daily)` Schedule the query to execute every so many days.  
Union field `evaluate`. The test to be run against the SQL result set. `evaluate` can be only one of the following:  
`row_count_test` |  `[RowCountTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTest)` Test the row count against a threshold.  
`boolean_test` |  `[BooleanTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTest)` Test the boolean value in the indicated column.  
  
## BooleanTest

A test that uses an alerting result in a boolean column produced by the SQL query.

Fields  
---  
`column` |  `string` Required. The name of the column containing the boolean value. If the value in a row is NULL, that row is ignored.  
  
## Daily

Used to schedule the query to run every so many days.

Fields  
---  
`periodicity` |  `int32` Required. The number of days between runs. Must be greater than or equal to 1 day and less than or equal to 31 days.  
`execution_time` |  `[TimeOfDay](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type#google.type.TimeOfDay)` Optional. The time of day (in UTC) at which the query should run. If left unspecified, the server picks an arbitrary time of day and runs the query at the same time each day.  
  
## Hourly

Used to schedule the query to run every so many hours.

Fields  
---  
`periodicity` |  `int32` Required. The number of hours between runs. Must be greater than or equal to 1 hour and less than or equal to 48 hours.  
`minute_offset` |  `int32` Optional. The number of minutes after the hour (in UTC) to run the query. Must be greater than or equal to 0 minutes and less than or equal to 59 minutes. If left unspecified, then an arbitrary offset is used.  
  
## Minutes

Used to schedule the query to run every so many minutes.

Fields  
---  
`periodicity` |  `int32` Required. Number of minutes between runs. The interval must be greater than or equal to 5 minutes and less than or equal to 1440 minutes.  
  
## RowCountTest

A test that checks if the number of rows in the result set violates some threshold.

Fields  
---  
`comparison` |  `[ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ComparisonType)` Required. The comparison to apply between the number of rows returned by the query and the threshold.  
`threshold` |  `int64` Required. The value against which to compare the row count.  
  
## Trigger

Specifies how many time series must fail a predicate to trigger a condition. If not specified, then a `{count: 1}` trigger is used.

Fields  
---  
Union field `type`. A type of trigger. `type` can be only one of the following:  
`count` |  `int32` The absolute number of time series that must fail the predicate for the condition to be triggered.  
`percent` |  `double` The percentage of time series that must fail the predicate for the condition to be triggered.  
  
## ConditionCombinerType

Operators for combining conditions.

Enums  
---  
`COMBINE_UNSPECIFIED` | An unspecified combiner.  
`AND` | Combine conditions using the logical `AND` operator. An incident is created only if all the conditions are met simultaneously. This combiner is satisfied if all conditions are met, even if they are met on completely different resources.  
`OR` | Combine conditions using the logical `OR` operator. An incident is created if any of the listed conditions is met.  
`AND_WITH_MATCHING_RESOURCE` | Combine conditions using logical `AND` operator, but unlike the regular `AND` option, an incident is created only if all conditions are met simultaneously on at least one resource.  
  
## Documentation

Documentation that is included in the notifications and incidents pertaining to this policy.

Fields  
---  
`content` |  `string` The body of the documentation, interpreted according to `mime_type`. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller. This text can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars).  
`mime_type` |  `string` The format of the `content` field. Presently, only the value `"text/markdown"` is supported. See [Markdown](https://en.wikipedia.org/wiki/Markdown) for more information.  
`subject` |  `string` Optional. The subject line of the notification. The subject line may not exceed 10,240 bytes. In notifications generated by this policy, the contents of the subject line after variable expansion will be truncated to 255 bytes or shorter at the latest UTF-8 character boundary. The 255-byte limit is recommended by [this thread](https://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit). It is both the limit imposed by some third-party ticketing products and it is common to define textual fields in databases as VARCHAR(255).The contents of the subject line can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars). If this field is missing or empty, a default subject line will be generated.  
`links[]` |  `[Link](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy.Documentation.Link)` Optional. Links to content such as playbooks, repositories, and other resources. This field can contain up to 3 entries.  
  
## Link

Links to content such as playbooks, repositories, and other resources.

Fields  
---  
`display_name` |  `string` A short display name for the link. The display name must not be empty or exceed 63 characters. Example: "playbook".  
`url` |  `string` The url of a webpage. A url can be templatized by using variables in the path or the query parameters. The total length of a URL should not exceed 2083 characters before and after variable expansion. Example: "https://my_domain.com/playbook?name=${resource.name}"  
  
## Severity

An enumeration of possible severity level for an alerting policy.

Enums  
---  
`SEVERITY_UNSPECIFIED` | No severity is specified. This is the default value.  
`CRITICAL` | This is the highest severity level. Use this if the problem could cause significant damage or downtime.  
`ERROR` | This is the medium severity level. Use this if the problem could cause minor damage or downtime.  
`WARNING` | This is the lowest severity level. Use this if the problem is not causing any damage or downtime, but could potentially lead to a problem in the future.  
  
## BasicSli

An SLI measuring performance on a well-known service type. Performance will be computed on the basis of pre-defined metrics. The type of the `service_resource` determines the metrics to use and the `service_resource.labels` and `metric_labels` are used to construct a monitoring filter to filter that metric down to just the data relevant to this service.

Fields  
---  
`method[]` |  `string` OPTIONAL: The set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service's methods. For service types that don't support breaking down by method, setting this field will result in an error.  
`location[]` |  `string` OPTIONAL: The set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don't support breaking down by location, setting this field will result in an error.  
`version[]` |  `string` OPTIONAL: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don't support breaking down by version, setting this field will result in an error.  
Union field `sli_criteria`. This SLI can be evaluated on the basis of availability or latency. `sli_criteria` can be only one of the following:  
`availability` |  `[AvailabilityCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.BasicSli.AvailabilityCriteria)` Good service is defined to be the count of requests made to this service that return successfully.  
`latency` |  `[LatencyCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.BasicSli.LatencyCriteria)` Good service is defined to be the count of requests made to this service that are fast enough with respect to `latency.threshold`.  
  
## AvailabilityCriteria

This type has no fields.

Future parameters for the availability SLI.

## LatencyCriteria

Parameters for a latency threshold SLI.

Fields  
---  
`threshold` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Good service is defined to be the count of requests made to this service that return in no more than `threshold`.  
  
## ComparisonType

Specifies an ordering relationship on two arguments, called `left` and `right`.

Enums  
---  
`COMPARISON_UNSPECIFIED` | No ordering relationship is specified.  
`COMPARISON_GT` | True if the left argument is greater than the right argument.  
`COMPARISON_GE` | True if the left argument is greater than or equal to the right argument.  
`COMPARISON_LT` | True if the left argument is less than the right argument.  
`COMPARISON_LE` | True if the left argument is less than or equal to the right argument.  
`COMPARISON_EQ` | True if the left argument is equal to the right argument.  
`COMPARISON_NE` | True if the left argument is not equal to the right argument.  
  
## CreateAlertPolicyRequest

The protocol for the `CreateAlertPolicy` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) in which to create the alerting policy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Note that this field names the parent container in which the alerting policy will be written, not the name of the created policy. |name| must be a host project of a Metrics Scope, otherwise INVALID_ARGUMENT error will return. The alerting policy that is returned will have a name that contains a normalized representation of this name as a prefix but adds a suffix of the form `/alertPolicies/[ALERT_POLICY_ID]`, identifying the policy in the container. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.alertPolicies.create`

  
`alert_policy` |  `[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)` Required. The requested alerting policy. You should omit the `name` field in this policy. The name will be returned in the new policy, including a new `[ALERT_POLICY_ID]` value.  
  
## CreateGroupRequest

The `CreateGroup` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) in which to create the group. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`group` |  `[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Group)` Required. A group definition. It is an error to define the `name` field because the system assigns the name.  
`validate_only` |  `bool` If true, validate this request but do not create the group.  
  
## CreateMetricDescriptorRequest

The `CreateMetricDescriptor` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is: 4 projects/[PROJECT_ID_OR_NUMBER]  
`metric_descriptor` |  `[MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)` Required. The new [custom metric](https://cloud.google.com/monitoring/custom-metrics) descriptor.  
  
## CreateNotificationChannelRequest

The `CreateNotificationChannel` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

This names the container into which the channel will be written, this does not name the newly created channel. The resulting channel's name will have a normalized version of this field as a prefix, but will add `/notificationChannels/[CHANNEL_ID]` to identify the channel. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.create`

  
`notification_channel` |  `[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)` Required. The definition of the `NotificationChannel` to create.  
  
## CreateServiceLevelObjectiveRequest

The `CreateServiceLevelObjective` request.

Fields  
---  
`parent` |  `string` Required. Resource name of the parent `Service`. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
      
  
`service_level_objective_id` |  `string` Optional. The ServiceLevelObjective id to use for this ServiceLevelObjective. If omitted, an id will be generated instead. Must match the pattern `^[a-zA-Z0-9-_:.]+$`  
`service_level_objective` |  `[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective)` Required. The `ServiceLevelObjective` to create. The provided `name` will be respected if no `ServiceLevelObjective` exists with this name.  
  
## CreateServiceRequest

The `CreateService` request.

Fields  
---  
`parent` |  `string` Required. Resource [name](https://cloud.google.com/monitoring/api/v3#project_name) of the parent Metrics Scope. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`service_id` |  `string` Optional. The Service id to use for this Service. If omitted, an id will be generated instead. Must match the pattern `[a-z0-9\-]+`  
`service` |  `[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service)` Required. The `Service` to create.  
  
## CreateSnoozeRequest

The message definition for creating a `Snooze`. Users must provide the body of the `Snooze` to be created but must omit the `Snooze` field, `name`.

Fields  
---  
`parent` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) in which a `Snooze` should be created. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`snooze` |  `[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze)` Required. The `Snooze` to create. Omit the `name` field, as it will be filled in by the API.  
  
## CreateTimeSeriesError

DEPRECATED. Used to hold per-time-series error status.

Fields  
---  
`time_series  
**(deprecated)**` |  `[TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)` This item is deprecated!DEPRECATED. Time series ID that resulted in the `status` error.  
`status  
**(deprecated)**` |  `[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.rpc#google.rpc.Status)` This item is deprecated!DEPRECATED. The status of the requested write operation for `time_series`.  
  
## CreateTimeSeriesRequest

The `CreateTimeSeries` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`time_series[]` |  `[TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)` Required. The new data to be added to a list of time series. Adds at most one data point to each of several time series. The new data point must be more recent than any other point in its time series. Each `TimeSeries` value must fully specify a unique time series by supplying all label values for the metric and the monitored resource.The maximum number of `TimeSeries` objects per `Create` request is 200.  
  
## CreateTimeSeriesSummary

Summary of the result of a failed request to write data to a time series.

Fields  
---  
`total_point_count` |  `int32` The number of points in the request.  
`success_point_count` |  `int32` The number of points that were successfully written.  
`errors[]` |  `[Error](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.CreateTimeSeriesSummary.Error)` The number of points that failed to be written. Order is not guaranteed.  
  
## Error

Detailed information about an error category.

Fields  
---  
`status` |  `[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.rpc#google.rpc.Status)` The status of the requested write operation.  
`point_count` |  `int32` The number of points that couldn't be written because of `status`.  
  
## CreateUptimeCheckConfigRequest

The protocol for the `CreateUptimeCheckConfig` request.

Fields  
---  
`parent` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) in which to create the Uptime check. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `monitoring.uptimeCheckConfigs.create`

  
`uptime_check_config` |  `[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig)` Required. The new Uptime check configuration.  
  
## DeleteAlertPolicyRequest

The protocol for the `DeleteAlertPolicy` request.

Fields  
---  
`name` |  `string` Required. The alerting policy to delete. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
    

For more information, see `[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.alertPolicies.delete`

  
  
## DeleteGroupRequest

The `DeleteGroup` request. The default behavior is to be able to delete a single group without any descendants.

Fields  
---  
`name` |  `string` Required. The group to delete. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
      
  
`recursive` |  `bool` If this field is true, then the request means to delete a group with all its descendants. Otherwise, the request means to delete a group only when it has no descendants. The default value is false.  
  
## DeleteMetricDescriptorRequest

The `DeleteMetricDescriptor` request.

Fields  
---  
`name` |  `string` Required. The metric descriptor on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/metricDescriptors/[METRIC_ID]
    

An example of `[METRIC_ID]` is: `"custom.googleapis.com/my_test_metric"`.  
  
## DeleteNotificationChannelRequest

The `DeleteNotificationChannel` request.

Fields  
---  
`name` |  `string` Required. The channel for which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.delete`

  
`force` |  `bool` If true, the notification channel will be deleted regardless of its use in alert policies (the policies will be updated to remove the channel). If false, this operation will fail if the notification channel is referenced by existing alerting policies.  
  
## DeleteServiceLevelObjectiveRequest

The `DeleteServiceLevelObjective` request.

Fields  
---  
`name` |  `string` Required. Resource name of the `ServiceLevelObjective` to delete. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]
      
  
## DeleteServiceRequest

The `DeleteService` request.

Fields  
---  
`name` |  `string` Required. Resource name of the `Service` to delete. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
      
  
## DeleteUptimeCheckConfigRequest

The protocol for the `DeleteUptimeCheckConfig` request.

Fields  
---  
`name` |  `string` Required. The Uptime check configuration to delete. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.uptimeCheckConfigs.delete`

  
  
## DistributionCut

A `DistributionCut` defines a `TimeSeries` and thresholds used for measuring good service and total service. The `TimeSeries` must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. The computed `good_service` will be the estimated count of values in the `Distribution` that fall within the specified `min` and `max`.

Fields  
---  
`distribution_filter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` aggregating values. Must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
`range` |  `[Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Range)` Range of values considered "good." For a one-sided range, set one bound to an infinite value.  
  
## DroppedLabels

A set of (label, value) pairs that were removed from a Distribution time series during aggregation and then added as an attachment to a Distribution.Exemplar.

The full label set for the exemplars is constructed by using the dropped pairs in combination with the label values that remain on the aggregated Distribution time series. The constructed full label set can be used to identify the specific entity, such as the instance or job, which might be contributing to a long-tail. However, with dropped labels, the storage requirements are reduced because only the aggregated distribution values for a large group of time series are stored.

Note that there are no guarantees on ordering of the labels from exemplar-to-exemplar and from distribution-to-distribution in the same stream, and there may be duplicates. It is up to clients to resolve any ambiguities.

Fields  
---  
`label` |  `map<string, string>` Map from label to its value, for all labels dropped in any aggregation.  
  
## GetAlertPolicyRequest

The protocol for the `GetAlertPolicy` request.

Fields  
---  
`name` |  `string` Required. The alerting policy to retrieve. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.alertPolicies.get`

  
  
## GetAlertRequest

The `GetAlert` request.

Fields  
---  
`name` |  `string` Required. The name of the alert.The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alerts/[ALERT_ID]
    

The `[ALERT_ID]` is a system-assigned unique identifier for the alert.  
  
## GetGroupRequest

The `GetGroup` request.

Fields  
---  
`name` |  `string` Required. The group to retrieve. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
      
  
## GetMetricDescriptorRequest

The `GetMetricDescriptor` request.

Fields  
---  
`name` |  `string` Required. The metric descriptor on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/metricDescriptors/[METRIC_ID]
    

An example value of `[METRIC_ID]` is `"compute.googleapis.com/instance/disk/read_bytes_count"`.  
  
## GetMonitoredResourceDescriptorRequest

The `GetMonitoredResourceDescriptor` request.

Fields  
---  
`name` |  `string` Required. The monitored resource descriptor to get. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/monitoredResourceDescriptors/[RESOURCE_TYPE]
    

The `[RESOURCE_TYPE]` is a predefined type, such as `cloudsql_database`.  
  
## GetNotificationChannelDescriptorRequest

The `GetNotificationChannelDescriptor` response.

Fields  
---  
`name` |  `string` Required. The channel type for which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[CHANNEL_TYPE]
      
  
## GetNotificationChannelRequest

The `GetNotificationChannel` request.

Fields  
---  
`name` |  `string` Required. The channel for which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.get`

  
  
## GetNotificationChannelVerificationCodeRequest

The `GetNotificationChannelVerificationCode` request.

Fields  
---  
`name` |  `string` Required. The notification channel for which a verification code is to be generated and retrieved. This must name a channel that is already verified; if the specified channel is not verified, the request will fail. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.getVerificationCode`

  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The desired expiration time. If specified, the API will guarantee that the returned code will not be valid after the specified timestamp; however, the API cannot guarantee that the returned code will be valid for at least as long as the requested time (the API puts an upper bound on the amount of time for which a code may be valid). If omitted, a default expiration will be used, which may be less than the max permissible expiration (so specifying an expiration may extend the code's lifetime over omitting an expiration, even though the API does impose an upper limit on the maximum expiration that is permitted).  
  
## GetNotificationChannelVerificationCodeResponse

The `GetNotificationChannelVerificationCode` request.

Fields  
---  
`code` |  `string` The verification code, which may be used to verify other channels that have an equivalent identity (i.e. other channels of the same type with the same fingerprint such as other email channels with the same email address or other sms channels with the same number).  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The expiration time associated with the code that was returned. If an expiration was provided in the request, this is the minimum of the requested expiration in the request and the max permitted expiration.  
  
## GetServiceLevelObjectiveRequest

The `GetServiceLevelObjective` request.

Fields  
---  
`name` |  `string` Required. Resource name of the `ServiceLevelObjective` to get. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]
      
  
`view` |  `[View](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective.View)` View of the `ServiceLevelObjective` to return. If `DEFAULT`, return the `ServiceLevelObjective` as originally defined. If `EXPLICIT` and the `ServiceLevelObjective` is defined in terms of a `BasicSli`, replace the `BasicSli` with a `RequestBasedSli` spelling out how the SLI is computed.  
  
## GetServiceRequest

The `GetService` request.

Fields  
---  
`name` |  `string` Required. Resource name of the `Service`. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
      
  
## GetSnoozeRequest

The message definition for retrieving a `Snooze`. Users must specify the field, `name`, which identifies the `Snooze`.

Fields  
---  
`name` |  `string` Required. The ID of the `Snooze` to retrieve. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/snoozes/[SNOOZE_ID]
      
  
## GetUptimeCheckConfigRequest

The protocol for the `GetUptimeCheckConfig` request.

Fields  
---  
`name` |  `string` Required. The Uptime check configuration to retrieve. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.uptimeCheckConfigs.get`

  
  
## Group

The description of a dynamic collection of monitored resources. Each group has a filter that is matched against monitored resources and their associated metadata. If a group's filter matches an available monitored resource, then that resource is a member of that group. Groups can contain any number of monitored resources, and each monitored resource can be a member of any number of groups.

Groups can be nested in parent-child hierarchies. The `parentName` field identifies an optional parent for each group. If a group has a parent, then the only monitored resources available to be matched by the group's filter are the resources contained in the parent group. In other words, a group contains the monitored resources that match its filter and the filters of all the group's ancestors. A group without a parent can contain any monitored resource.

For example, consider an infrastructure running a set of instances with two user-defined tags: `"environment"` and `"role"`. A parent group has a filter, `environment="production"`. A child of that parent group has a filter, `role="transcoder"`. The parent group contains all instances in the production environment, regardless of their roles. The child group contains instances that have the transcoder role _and_ are in the production environment.

The monitored resources contained in a group can change at any moment, depending on what resources exist and what filters are associated with the group and its ancestors.

Fields  
---  
`name` |  `string` Output only. The name of this group. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

When creating a group, this field is ignored and a new name is created consisting of the project specified in the call to `CreateGroup` and a unique `[GROUP_ID]` that is generated automatically.  
`display_name` |  `string` A user-assigned name for this group, used only for display purposes.  
`parent_name` |  `string` The name of the group's parent, if it has one. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

For groups with no parent, `parent_name` is the empty string, `""`.  
`filter` |  `string` The filter used to determine which monitored resources belong to this group.  
`is_cluster` |  `bool` If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups that are clusters.  
  
## GroupResourceType

The supported resource types that can be used as values of `group_resource.resource_type`. `INSTANCE` includes `gce_instance` and `aws_ec2_instance` resource types. The resource types `gae_app` and `uptime_url` are not valid here because group checks on App Engine modules and URLs are not allowed.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Default value (not valid).  
`INSTANCE` | A group of instances from Google Cloud Platform (GCP) or Amazon Web Services (AWS).  
`AWS_ELB_LOAD_BALANCER` | A group of Amazon ELB load balancers.  
  
## InternalChecker

This item is deprecated!

An internal checker allows Uptime checks to run on private/internal GCP resources.

Fields  
---  
`name` |  `string` A unique resource name for this InternalChecker. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/internalCheckers/[INTERNAL_CHECKER_ID]
    

`[PROJECT_ID_OR_NUMBER]` is the Cloud Monitoring Metrics Scope project for the Uptime check config associated with the internal checker.  
`display_name` |  `string` The checker's human-readable name. The display name should be unique within a Cloud Monitoring Metrics Scope in order to make it easier to identify; however, uniqueness is not enforced.  
`network` |  `string` The [GCP VPC network](https://cloud.google.com/vpc/docs/vpc) where the internal resource lives (ex: "default").  
`gcp_zone` |  `string` The GCP zone the Uptime check should egress from. Only respected for internal Uptime checks, where internal_network is specified.  
`peer_project_id` |  `string` The GCP project ID where the internal checker lives. Not necessary the same as the Metrics Scope project.  
`state` |  `[State](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.InternalChecker.State)` The current operational state of the internal checker.  
  
## State

Operational states for an internal checker.

Enums  
---  
`UNSPECIFIED` | An internal checker should never be in the unspecified state.  
`CREATING` | The checker is being created, provisioned, and configured. A checker in this state can be returned by `ListInternalCheckers` or `GetInternalChecker`, as well as by examining the [long running Operation](https://cloud.google.com/apis/design/design_patterns#long_running_operations) that created it.  
`RUNNING` | The checker is running and available for use. A checker in this state can be returned by `ListInternalCheckers` or `GetInternalChecker` as well as by examining the [long running Operation](https://cloud.google.com/apis/design/design_patterns#long_running_operations) that created it. If a checker is being torn down, it is neither visible nor usable, so there is no "deleting" or "down" state.  
  
## LabelValue

A label value.

Fields  
---  
Union field `value`. The label value can be a bool, int64, or string. `value` can be only one of the following:  
`bool_value` |  `bool` A bool label value.  
`int64_value` |  `int64` An int64 label value.  
`string_value` |  `string` A string label value.  
  
## ListAlertPoliciesRequest

The protocol for the `ListAlertPolicies` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose alert policies are to be listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Note that this field names the parent container in which the alerting policies to be listed are stored. To retrieve a single alerting policy by name, use the `[GetAlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicyService.GetAlertPolicy)` operation, instead. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.alertPolicies.list`

  
`filter` |  `string` Optional. If provided, this field specifies the criteria that must be met by alert policies to be included in the response.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`order_by` |  `string` Optional. A comma-separated list of fields by which to sort the result. Supports the same set of field references as the `filter` field. Entries can be prefixed with a minus sign to sort by the field in descending order.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`page_size` |  `int32` Optional. The maximum number of results to return in a single response.  
`page_token` |  `string` Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return more results from the previous method call.  
  
## ListAlertPoliciesResponse

The protocol for the `ListAlertPolicies` response.

Fields  
---  
`alert_policies[]` |  `[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)` The returned alert policies.  
`next_page_token` |  `string` If there might be more results than were returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
`total_size` |  `int32` The total number of alert policies in all pages. This number is only an estimate, and may change in subsequent pages. <https://aip.dev/158>  
  
## ListAlertsRequest

The `ListAlerts` request.

Fields  
---  
`parent` |  `string` Required. The name of the project to list alerts for.  
`filter` |  `string` Optional. An alert is returned if there is a match on any fields belonging to the alert or its subfields.  
`order_by` |  `string` Optional. A comma-separated list of fields in `Alert` to use for sorting. The default sort direction is ascending. To specify descending order for a field, add a `desc` modifier. The following fields are supported:

  * `open_time`
  * `close_time`

For example, `close_time desc, open_time` will return the alerts closed most recently, with ties broken in the order of older alerts listed first.If the field is not set, the results are sorted by `open_time desc`.  
`page_size` |  `int32` Optional. The maximum number of results to return in a single response. If not set to a positive number, at most 50 alerts will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. If non-empty, `page_token` must contain a value returned as the `next_page_token` in a previous response to request the next set of results.  
  
## ListAlertsResponse

The `ListAlerts` response.

Fields  
---  
`alerts[]` |  `[Alert](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Alert)` The list of alerts.  
`next_page_token` |  `string` If not empty, indicates that there may be more results that match the request. Use the value in the `page_token` field in a subsequent request to fetch the next set of results. The token is encrypted and only guaranteed to return correct results for 72 hours after it is created. If empty, all results have been returned.  
`total_size` |  `int32` The estimated total number of matching results for this query.  
  
## ListGroupMembersRequest

The `ListGroupMembers` request.

Fields  
---  
`name` |  `string` Required. The group whose members are listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
      
  
`page_size` |  `int32` A positive number that is the maximum number of results to return.  
`page_token` |  `string` If this field is not empty then it must contain the `next_page_token` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
`filter` |  `string` An optional [list filter](https://cloud.google.com/monitoring/api/learn_more#filtering) describing the members to be returned. The filter may reference the type, labels, and metadata of monitored resources that comprise the group. For example, to return only resources representing Compute Engine VM instances, use this filter:
    
    
    `resource.type = "gce_instance"`
      
  
`interval` |  `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` An optional time interval for which results should be returned. Only members that were part of the group during the specified interval are included in the response. If no interval is provided then the group membership over the last minute is returned.  
  
## ListGroupMembersResponse

The `ListGroupMembers` response.

Fields  
---  
`members[]` |  `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` A set of monitored resources in the group.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
`total_size` |  `int32` The total number of elements matching this request.  
  
## ListGroupsRequest

The `ListGroup` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose groups are to be listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`page_size` |  `int32` A positive number that is the maximum number of results to return.  
`page_token` |  `string` If this field is not empty then it must contain the `next_page_token` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
Union field `filter`. An optional filter consisting of a single group name. The filters limit the groups returned based on their parent-child relationship with the specified group. If no filter is specified, all groups are returned. `filter` can be only one of the following:  
`children_of_group` |  `string` A group name. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

Returns groups whose `parent_name` field contains the group name. If no groups have this parent, the results are empty.  
`ancestors_of_group` |  `string` A group name. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

Returns groups that are ancestors of the specified group. The groups are returned in order, starting with the immediate parent and ending with the most distant ancestor. If the specified group has no immediate parent, the results are empty.  
`descendants_of_group` |  `string` A group name. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

Returns the descendants of the specified group. This is a superset of the results returned by the `children_of_group` filter, and includes children-of-children, and so forth.  
  
## ListGroupsResponse

The `ListGroups` response.

Fields  
---  
`group[]` |  `[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Group)` The groups that match the specified filters.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
  
## ListMetricDescriptorsRequest

The `ListMetricDescriptors` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`filter` |  `string` Optional. If this field is empty, all custom and system-defined metric descriptors are returned. Otherwise, the [filter](https://cloud.google.com/monitoring/api/v3/filters) specifies which metric descriptors are to be returned. For example, the following filter matches all [custom metrics](https://cloud.google.com/monitoring/custom-metrics):
    
    
    metric.type = starts_with("custom.googleapis.com/")
      
  
`page_size` |  `int32` Optional. A positive number that is the maximum number of results to return. The default and maximum value is 10,000. If a page_size <= 0 or > 10,000 is submitted, will instead return a maximum of 10,000 results.  
`page_token` |  `string` Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
`active_only` |  `bool` Optional. If true, only metrics and monitored resource types that have recent data (within roughly 25 hours) will be included in the response. - If a metric descriptor enumerates monitored resource types, only the monitored resource types for which the metric type has recent data will be included in the returned metric descriptor, and if none of them have recent data, the metric descriptor will not be returned. - If a metric descriptor does not enumerate the compatible monitored resource types, it will be returned only if the metric type has recent data for some monitored resource type. The returned descriptor will not enumerate any monitored resource types.  
  
## ListMetricDescriptorsResponse

The `ListMetricDescriptors` response.

Fields  
---  
`metric_descriptors[]` |  `[MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)` The metric descriptors that are available to the project and that match the value of `filter`, if present.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
  
## ListMonitoredResourceDescriptorsRequest

The `ListMonitoredResourceDescriptors` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`filter` |  `string` An optional [filter](https://cloud.google.com/monitoring/api/v3/filters) describing the descriptors to be returned. The filter can reference the descriptor's type and labels. For example, the following filter returns only Google Compute Engine descriptors that have an `id` label:
    
    
    resource.type = starts_with("gce_") AND resource.label:id
      
  
`page_size` |  `int32` A positive number that is the maximum number of results to return.  
`page_token` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
## ListMonitoredResourceDescriptorsResponse

The `ListMonitoredResourceDescriptors` response.

Fields  
---  
`resource_descriptors[]` |  `[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceDescriptor)` The monitored resource descriptors that are available to this project and that match `filter`, if present.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
  
## ListNotificationChannelDescriptorsRequest

The `ListNotificationChannelDescriptors` request.

Fields  
---  
`name` |  `string` Required. The REST resource name of the parent from which to retrieve the notification channel descriptors. The expected syntax is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Note that this [names](https://cloud.google.com/monitoring/api/v3#project_name) the parent container in which to look for the descriptors; to retrieve a single descriptor by name, use the `[GetNotificationChannelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.GetNotificationChannelDescriptor)` operation, instead. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannelDescriptors.list`

  
`page_size` |  `int32` The maximum number of results to return in a single response. If not set to a positive number, a reasonable value will be chosen by the service.  
`page_token` |  `string` If non-empty, `page_token` must contain a value returned as the `next_page_token` in a previous response to request the next set of results.  
  
## ListNotificationChannelDescriptorsResponse

The `ListNotificationChannelDescriptors` response.

Fields  
---  
`channel_descriptors[]` |  `[NotificationChannelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelDescriptor)` The monitored resource descriptors supported for the specified project, optionally filtered.  
`next_page_token` |  `string` If not empty, indicates that there may be more results that match the request. Use the value in the `page_token` field in a subsequent request to fetch the next set of results. If empty, all results have been returned.  
  
## ListNotificationChannelsRequest

The `ListNotificationChannels` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

This names the container in which to look for the notification channels; it does not name a specific channel. To query a specific channel by REST resource name, use the `[`GetNotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.GetNotificationChannel)` operation. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.list`

  
`filter` |  `string` Optional. If provided, this field specifies the criteria that must be met by notification channels to be included in the response.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`order_by` |  `string` Optional. A comma-separated list of fields by which to sort the result. Supports the same set of fields as in `filter`. Entries can be prefixed with a minus sign to sort in descending rather than ascending order.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`page_size` |  `int32` Optional. The maximum number of results to return in a single response. If not set to a positive number, a reasonable value will be chosen by the service.  
`page_token` |  `string` Optional. If non-empty, `page_token` must contain a value returned as the `next_page_token` in a previous response to request the next set of results.  
  
## ListNotificationChannelsResponse

The `ListNotificationChannels` response.

Fields  
---  
`notification_channels[]` |  `[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)` The notification channels defined for the specified project.  
`next_page_token` |  `string` If not empty, indicates that there may be more results that match the request. Use the value in the `page_token` field in a subsequent request to fetch the next set of results. If empty, all results have been returned.  
`total_size` |  `int32` The total number of notification channels in all pages. This number is only an estimate, and may change in subsequent pages. <https://aip.dev/158>  
  
## ListServiceLevelObjectivesRequest

The `ListServiceLevelObjectives` request.

Fields  
---  
`parent` |  `string` Required. Resource name of the parent containing the listed SLOs, either a project or a Monitoring Metrics Scope. The formats are:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
    workspaces/[HOST_PROJECT_ID_OR_NUMBER]/services/-
      
  
`filter` |  `string` A filter specifying what `ServiceLevelObjective`s to return.  
`page_size` |  `int32` A non-negative number that is the maximum number of results to return. When 0, use default page size.  
`page_token` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
`view` |  `[View](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective.View)` View of the `ServiceLevelObjective`s to return. If `DEFAULT`, return each `ServiceLevelObjective` as originally defined. If `EXPLICIT` and the `ServiceLevelObjective` is defined in terms of a `BasicSli`, replace the `BasicSli` with a `RequestBasedSli` spelling out how the SLI is computed.  
  
## ListServiceLevelObjectivesResponse

The `ListServiceLevelObjectives` response.

Fields  
---  
`service_level_objectives[]` |  `[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective)` The `ServiceLevelObjective`s matching the specified filter.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
  
## ListServicesRequest

The `ListServices` request.

Fields  
---  
`parent` |  `string` Required. Resource name of the parent containing the listed services, either a [project](https://cloud.google.com/monitoring/api/v3#project_name) or a Monitoring Metrics Scope. The formats are:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    workspaces/[HOST_PROJECT_ID_OR_NUMBER]
      
  
`filter` |  `string` A filter specifying what `Service`s to return. The filter supports filtering on a particular service-identifier type or one of its attributes.To filter on a particular service-identifier type, the `identifier_case` refers to which option in the `identifier` field is populated. For example, the filter `identifier_case = "CUSTOM"` would match all services with a value for the `custom` field. Valid options include "CUSTOM", "APP_ENGINE", "MESH_ISTIO", and the other options listed at <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service>To filter on an attribute of a service-identifier type, apply the filter name by using the snake case of the service-identifier type and the attribute of that service-identifier type, and join the two with a period. For example, to filter by the `meshUid` field of the `MeshIstio` service-identifier type, you must filter on `mesh_istio.mesh_uid = "123"` to match all services with mesh UID "123". Service-identifier types and their attributes are described at <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Service>  
`page_size` |  `int32` A non-negative number that is the maximum number of results to return. When 0, use default page size.  
`page_token` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
## ListServicesResponse

The `ListServices` response.

Fields  
---  
`services[]` |  `[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service)` The `Service`s matching the specified filter.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
  
## ListSnoozesRequest

The message definition for listing `Snooze`s associated with the given `parent`, satisfying the optional `filter`.

Fields  
---  
`parent` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose `Snooze`s should be listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`filter` |  `string` Optional. Optional filter to restrict results to the given criteria. The following fields are supported.

  * `interval.start_time`
  * `interval.end_time`

For example:
    
    
    interval.start_time > "2022-03-11T00:00:00-08:00" AND
        interval.end_time < "2022-03-12T00:00:00-08:00"
      
  
`page_size` |  `int32` Optional. The maximum number of results to return for a single query. The server may further constrain the maximum number of results returned in a single page. The value should be in the range [1, 1000]. If the value given is outside this range, the server will decide the number of results to be returned.  
`page_token` |  `string` Optional. The `next_page_token` from a previous call to `ListSnoozesRequest` to get the next page of results.  
  
## ListSnoozesResponse

The results of a successful `ListSnoozes` call, containing the matching `Snooze`s.

Fields  
---  
`snoozes[]` |  `[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze)` `Snooze`s matching this list call.  
`next_page_token` |  `string` Page token for repeated calls to `ListSnoozes`, to fetch additional pages of results. If this is empty or missing, there are no more pages.  
  
## ListTimeSeriesRequest

The `ListTimeSeries` request.

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name), organization or folder on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    organizations/[ORGANIZATION_ID]
    folders/[FOLDER_ID]
      
  
`filter` |  `string` Required. A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that specifies which time series should be returned. The filter must specify a single metric type, and can additionally specify metric labels and other information. For example:
    
    
    metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
        metric.labels.instance_name = "my-instance-name"
      
  
`interval` |  `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` Required. The time interval for which results should be returned. Only time series that contain data points in the specified interval are included in the response.  
`aggregation` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series across specified labels.By default (if no `aggregation` is explicitly specified), the raw time series data is returned.  
`secondary_aggregation` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Aggregation)` Apply a second aggregation after `aggregation` is applied. May only be specified if `aggregation` is specified.  
`order_by` |  `string` Unsupported: must be left blank. The points in each time series are currently returned in reverse time order (most recent to oldest).  
`view` |  `[TimeSeriesView](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ListTimeSeriesRequest.TimeSeriesView)` Required. Specifies which information is returned about the time series.  
`page_size` |  `int32` A positive number that is the maximum number of results to return. If `page_size` is empty or more than 100,000 results, the effective `page_size` is 100,000 results. If `view` is set to `FULL`, this is the maximum number of `Points` returned. If `view` is set to `HEADERS`, this is the maximum number of `TimeSeries` returned.  
`page_token` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
## TimeSeriesView

Controls which fields are returned by `ListTimeSeries*`.

Enums  
---  
`FULL` | Returns the identity of the metric(s), the time series, and the time series data.  
`HEADERS` | Returns the identity of the metric and the time series resource, but not the time series data.  
  
## ListTimeSeriesResponse

The `ListTimeSeries` response.

Fields  
---  
`time_series[]` |  `[TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)` One or more time series that match the filter included in the request.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
`execution_errors[]` |  `[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.rpc#google.rpc.Status)` Query execution errors that may have caused the time series data returned to be incomplete.  
`unit` |  `string` The unit in which all `time_series` point values are reported. `unit` follows the UCUM format for units as seen in <https://unitsofmeasure.org/ucum.html>. If different `time_series` have different units (for example, because they come from different metric types, or a unit is absent), then `unit` will be "{not_a_unit}".  
`unreachable[]` |  `string` Cloud regions that were unreachable which may have caused incomplete data to be returned.  
  
## ListUptimeCheckConfigsRequest

The protocol for the `ListUptimeCheckConfigs` request.

Fields  
---  
`parent` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose Uptime check configurations are listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `monitoring.uptimeCheckConfigs.list`

  
`filter` |  `string` If provided, this field specifies the criteria that must be met by uptime checks to be included in the response.For more details, see [Filtering syntax](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering#filter_syntax).  
`page_size` |  `int32` The maximum number of results to return in a single response. The server may further constrain the maximum number of results returned in a single page. If the page_size is <=0, the server will decide the number of results to be returned.  
`page_token` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return more results from the previous method call.  
  
## ListUptimeCheckConfigsResponse

The protocol for the `ListUptimeCheckConfigs` response.

Fields  
---  
`uptime_check_configs[]` |  `[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig)` The returned Uptime check configurations.  
`next_page_token` |  `string` This field represents the pagination token to retrieve the next page of results. If the value is empty, it means no further results for the request. To retrieve the next page of results, the value of the next_page_token is passed to the subsequent List method call (in the request message's page_token field).  
`total_size` |  `int32` The total number of Uptime check configurations for the project, irrespective of any pagination.  
  
## ListUptimeCheckIpsRequest

The protocol for the `ListUptimeCheckIps` request.

Fields  
---  
`page_size` |  `int32` The maximum number of results to return in a single response. The server may further constrain the maximum number of results returned in a single page. If the page_size is <=0, the server will decide the number of results to be returned. NOTE: this field is not yet implemented  
`page_token` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return more results from the previous method call. NOTE: this field is not yet implemented  
  
## ListUptimeCheckIpsResponse

The protocol for the `ListUptimeCheckIps` response.

Fields  
---  
`uptime_check_ips[]` |  `[UptimeCheckIp](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckIp)` The returned list of IP addresses (including region and location) that the checkers run from.  
`next_page_token` |  `string` This field represents the pagination token to retrieve the next page of results. If the value is empty, it means no further results for the request. To retrieve the next page of results, the value of the next_page_token is passed to the subsequent List method call (in the request message's page_token field). NOTE: this field is not yet implemented  
  
## MutationRecord

Describes a change made to a configuration.

Fields  
---  
`mutate_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` When the change occurred.  
`mutated_by` |  `string` The email address of the user making the change.  
  
## NotificationChannel

A `NotificationChannel` is a medium through which an alert is delivered when a policy violation is detected. Examples of channels include email, SMS, and third-party messaging applications. Fields containing sensitive information like authentication tokens or contact info are only partially populated on retrieval.

Fields  
---  
`type` |  `string` The type of the notification channel. This field matches the value of the `[NotificationChannelDescriptor.type](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelDescriptor.FIELDS.string.google.monitoring.v3.NotificationChannelDescriptor.type)` field.  
`name` |  `string` Identifier. The full REST resource name for this channel. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
    

The `[CHANNEL_ID]` is automatically assigned by the server on creation.  
`display_name` |  `string` An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.  
`description` |  `string` An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.  
`labels` |  `map<string, string>` Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the `[NotificationChannelDescriptor.labels](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelDescriptor.FIELDS.repeated.google.api.LabelDescriptor.google.monitoring.v3.NotificationChannelDescriptor.labels)` of the `NotificationChannelDescriptor` corresponding to the `type` field.  
`user_labels` |  `map<string, string>` User-supplied key/value data that does not need to conform to the corresponding `NotificationChannelDescriptor`'s schema, unlike the `labels` field. This field is intended to be used for organizing and identifying the `NotificationChannel` objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.  
`verification_status` |  `[VerificationStatus](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel.VerificationStatus)` Indicates whether this channel has been verified or not. On a `[`ListNotificationChannels`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.ListNotificationChannels)` or `[`GetNotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.GetNotificationChannel)` operation, this field is expected to be populated.If the value is `UNVERIFIED`, then it indicates that the channel is non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel works.If the channel is neither `VERIFIED` nor `UNVERIFIED`, it implies that the channel is of a type that does not require verification or that this specific channel has been exempted from verification because it was created prior to verification being required for channels of this type.This field cannot be modified using a standard `[`UpdateNotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel)` operation. To change the value of this field, you must call `[`VerifyNotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.VerifyNotificationChannel)`.  
`enabled` |  `[BoolValue](https://protobuf.dev/reference/protobuf/google.protobuf/#bool-value)` Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.  
`creation_record` |  `[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MutationRecord)` Record of the creation of this channel.  
`mutation_records[]` |  `[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.MutationRecord)` Records of the modification of this channel.  
  
## VerificationStatus

Indicates whether the channel has been verified or not. It is illegal to specify this field in a `[`CreateNotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.CreateNotificationChannel)` or an `[`UpdateNotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel)` operation.

Enums  
---  
`VERIFICATION_STATUS_UNSPECIFIED` | Sentinel value used to indicate that the state is unknown, omitted, or is not applicable (as in the case of channels that neither support nor require verification in order to function).  
`UNVERIFIED` | The channel has yet to be verified and requires verification to function. Note that this state also applies to the case where the verification process has been initiated by sending a verification code but where the verification code has not been submitted to complete the process.  
`VERIFIED` | It has been proven that notifications can be received on this notification channel and that someone on the project has access to messages that are delivered to that channel.  
  
## NotificationChannelDescriptor

A description of a notification channel. The descriptor includes the properties of the channel and the set of labels or fields that must be specified to configure channels of a given type.

Fields  
---  
`name` |  `string` The full REST resource name for this descriptor. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[TYPE]
    

In the above, `[TYPE]` is the value of the `type` field.  
`type` |  `string` The type of notification channel, such as "email" and "sms". To view the full list of channels, see [Channel descriptors](https://cloud.google.com/monitoring/alerts/using-channels-api#ncd). Notification channel types are globally unique.  
`display_name` |  `string` A human-readable name for the notification channel type. This form of the name is suitable for a user interface.  
`description` |  `string` A human-readable description of the notification channel type. The description may include a description of the properties of the channel and pointers to external documentation.  
`labels[]` |  `[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LabelDescriptor)` The set of labels that must be defined to identify a particular channel of the corresponding type. Each label includes a description for how that field should be populated.  
`launch_stage` |  `[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LaunchStage)` The product launch stage for channels of this type.  
  
## Point

A single data point in a time series.

Fields  
---  
`interval` |  `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` The time interval to which the data point applies. For `GAUGE` metrics, the start time is optional, but if it is supplied, it must equal the end time. For `DELTA` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying contiguous and non-overlapping intervals. For `CUMULATIVE` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
`value` |  `[TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TypedValue)` The value of the data point.  
  
## QueryError

An error associated with a query in the time series query language format.

Fields  
---  
`locator` |  `[TextLocator](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TextLocator)` The location of the time series query language text that this error applies to.  
`message` |  `string` The error message.  
  
## QueryErrorList

This is an error detail intended to be used with INVALID_ARGUMENT errors.

Fields  
---  
`errors[]` |  `[QueryError](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.QueryError)` Errors in parsing the time series query language text. The number of errors in the response may be limited.  
`error_summary` |  `string` A summary of all the errors.  
  
## QueryTimeSeriesRequest

This item is deprecated!

The `QueryTimeSeries` request. For information about the status of Monitoring Query Language (MQL), see the [MQL deprecation notice](https://cloud.google.com/stackdriver/docs/deprecations/mql).

Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`query` |  `string` Required. The query in the [Monitoring Query Language](https://cloud.google.com/monitoring/mql/reference) format. The default time zone is in UTC.  
`page_size` |  `int32` A positive number that is the maximum number of time_series_data to return.  
`page_token` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
## QueryTimeSeriesResponse

This item is deprecated!

The `QueryTimeSeries` response. For information about the status of Monitoring Query Language (MQL), see the [MQL deprecation notice](https://cloud.google.com/stackdriver/docs/deprecations/mql).

Fields  
---  
`time_series_descriptor` |  `[TimeSeriesDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesDescriptor)` The descriptor for the time series data.  
`time_series_data[]` |  `[TimeSeriesData](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesData)` The time series data.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.rpc#google.rpc.Status)` Query execution errors that may have caused the time series data returned to be incomplete. The available data will be available in the response.  
  
## Range

Range of numerical values within `min` and `max`.

Fields  
---  
`min` |  `double` Range minimum.  
`max` |  `double` Range maximum.  
  
## RequestBasedSli

Service Level Indicators for which atomic units of service are counted directly.

Fields  
---  
Union field `method`. The means to compute a ratio of `good_service` to `total_service`. `method` can be only one of the following:  
`good_total_ratio` |  `[TimeSeriesRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesRatio)` `good_total_ratio` is used when the ratio of `good_service` to `total_service` is computed from two `TimeSeries`.  
`distribution_cut` |  `[DistributionCut](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.DistributionCut)` `distribution_cut` is used when `good_service` is a count of values aggregated in a `Distribution` that fall into a good range. The `total_service` is the total count of all values aggregated in the `Distribution`.  
  
## SendNotificationChannelVerificationCodeRequest

The `SendNotificationChannelVerificationCode` request.

Fields  
---  
`name` |  `string` Required. The notification channel to which to send a verification code. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.sendVerificationCode`

  
  
## Service

A `Service` is a discrete, autonomous, and network-accessible unit, designed to solve an individual concern ([Wikipedia](https://en.wikipedia.org/wiki/Service-orientation)). In Cloud Monitoring, a `Service` acts as the root resource under which operational aspects of the service are accessible.

Fields  
---  
`name` |  `string` Identifier. Resource name for this Service. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
      
  
`display_name` |  `string` Name used for UI elements listing this Service.  
`basic_service` |  `[BasicService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.BasicService)` Message that contains the service type and service labels of this service if it is a basic service. Documentation and examples [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).  
`telemetry` |  `[Telemetry](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.Telemetry)` Configuration for how to query telemetry on a Service.  
`user_labels` |  `map<string, string>` Labels which have been used to annotate the service. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value.  
Union field `identifier`. REQUIRED. Service-identifying atoms specifying the underlying service. `identifier` can be only one of the following:  
`custom` |  `[Custom](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.Custom)` Custom service type.  
`app_engine` |  `[AppEngine](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.AppEngine)` Type used for App Engine services.  
`cluster_istio` |  `[ClusterIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.ClusterIstio)` Type used for Istio services that live in a Kubernetes cluster.  
`mesh_istio` |  `[MeshIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.MeshIstio)` Type used for Istio services scoped to an Istio mesh.  
`istio_canonical_service` |  `[IstioCanonicalService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.IstioCanonicalService)` Type used for canonical services scoped to an Istio mesh. Metrics for Istio are [documented here](https://istio.io/latest/docs/reference/config/metrics/)  
`cloud_run` |  `[CloudRun](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.CloudRun)` Type used for Cloud Run services.  
`gke_namespace` |  `[GkeNamespace](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.GkeNamespace)` Type used for GKE Namespaces.  
`gke_workload` |  `[GkeWorkload](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.GkeWorkload)` Type used for GKE Workloads.  
`gke_service` |  `[GkeService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service.GkeService)` Type used for GKE Services (the Kubernetes concept of a service).  
  
## AppEngine

App Engine service. Learn more at <https://cloud.google.com/appengine>.

Fields  
---  
`module_id` |  `string` The ID of the App Engine module underlying this service. Corresponds to the `module_id` resource label in the [`gae_app` monitored resource](https://cloud.google.com/monitoring/api/resources#tag_gae_app).  
  
## BasicService

A well-known service type, defined by its service type and service labels. Documentation and examples [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).

Fields  
---  
`service_type` |  `string` The type of service that this basic service defines, e.g. APP_ENGINE service type. Documentation and valid values [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).  
`service_labels` |  `map<string, string>` Labels that specify the resource that emits the monitoring data which is used for SLO reporting of this `Service`. Documentation and valid values for given service types [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).  
  
## CloudRun

Cloud Run service. Learn more at <https://cloud.google.com/run>.

Fields  
---  
`service_name` |  `string` The name of the Cloud Run service. Corresponds to the `service_name` resource label in the [`cloud_run_revision` monitored resource](https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision).  
`location` |  `string` The location the service is run. Corresponds to the `location` resource label in the [`cloud_run_revision` monitored resource](https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision).  
  
## ClusterIstio

Istio service scoped to a single Kubernetes cluster. Learn more at <https://istio.io>. Clusters running OSS Istio will have their services ingested as this type.

Fields  
---  
`location` |  `string` The location of the Kubernetes cluster in which this Istio service is defined. Corresponds to the `location` resource label in `k8s_cluster` resources.  
`cluster_name` |  `string` The name of the Kubernetes cluster in which this Istio service is defined. Corresponds to the `cluster_name` resource label in `k8s_cluster` resources.  
`service_namespace` |  `string` The namespace of the Istio service underlying this service. Corresponds to the `destination_service_namespace` metric label in Istio metrics.  
`service_name` |  `string` The name of the Istio service underlying this service. Corresponds to the `destination_service_name` metric label in Istio metrics.  
  
## Custom

This type has no fields.

Use a custom service to designate a service that you want to monitor when none of the other service types (like App Engine, Cloud Run, or a GKE type) matches your intended service.

## GkeNamespace

GKE Namespace. The field names correspond to the resource metadata labels on monitored resources that fall under a namespace (for example, `k8s_container` or `k8s_pod`).

Fields  
---  
`project_id` |  `string` Output only. The project this resource lives in. For legacy services migrated from the `Custom` type, this may be a distinct project from the one parenting the service itself.  
`location` |  `string` The location of the parent cluster. This may be a zone or region.  
`cluster_name` |  `string` The name of the parent cluster.  
`namespace_name` |  `string` The name of this namespace.  
  
## GkeService

GKE Service. The "service" here represents a [Kubernetes service object](https://kubernetes.io/docs/concepts/services-networking/service). The field names correspond to the resource labels on [`k8s_service` monitored resources](https://cloud.google.com/monitoring/api/resources#tag_k8s_service).

Fields  
---  
`project_id` |  `string` Output only. The project this resource lives in. For legacy services migrated from the `Custom` type, this may be a distinct project from the one parenting the service itself.  
`location` |  `string` The location of the parent cluster. This may be a zone or region.  
`cluster_name` |  `string` The name of the parent cluster.  
`namespace_name` |  `string` The name of the parent namespace.  
`service_name` |  `string` The name of this service.  
  
## GkeWorkload

A GKE Workload (Deployment, StatefulSet, etc). The field names correspond to the metadata labels on monitored resources that fall under a workload (for example, `k8s_container` or `k8s_pod`).

Fields  
---  
`project_id` |  `string` Output only. The project this resource lives in. For legacy services migrated from the `Custom` type, this may be a distinct project from the one parenting the service itself.  
`location` |  `string` The location of the parent cluster. This may be a zone or region.  
`cluster_name` |  `string` The name of the parent cluster.  
`namespace_name` |  `string` The name of the parent namespace.  
`top_level_controller_type` |  `string` The type of this workload (for example, "Deployment" or "DaemonSet")  
`top_level_controller_name` |  `string` The name of this workload.  
  
## IstioCanonicalService

Canonical service scoped to an Istio mesh. Anthos clusters running ASM >= 1.6.8 will have their services ingested as this type.

Fields  
---  
`mesh_uid` |  `string` Identifier for the Istio mesh in which this canonical service is defined. Corresponds to the `mesh_uid` metric label in [Istio metrics](https://cloud.google.com/monitoring/api/metrics_istio).  
`canonical_service_namespace` |  `string` The namespace of the canonical service underlying this service. Corresponds to the `destination_canonical_service_namespace` metric label in [Istio metrics](https://cloud.google.com/monitoring/api/metrics_istio).  
`canonical_service` |  `string` The name of the canonical service underlying this service. Corresponds to the `destination_canonical_service_name` metric label in label in [Istio metrics](https://cloud.google.com/monitoring/api/metrics_istio).  
  
## MeshIstio

Istio service scoped to an Istio mesh. Anthos clusters running ASM < 1.6.8 will have their services ingested as this type.

Fields  
---  
`mesh_uid` |  `string` Identifier for the mesh in which this Istio service is defined. Corresponds to the `mesh_uid` metric label in Istio metrics.  
`service_namespace` |  `string` The namespace of the Istio service underlying this service. Corresponds to the `destination_service_namespace` metric label in Istio metrics.  
`service_name` |  `string` The name of the Istio service underlying this service. Corresponds to the `destination_service_name` metric label in Istio metrics.  
  
## Telemetry

Configuration for how to query telemetry on a Service.

Fields  
---  
`resource_name` |  `string` The full name of the resource that defines this service. Formatted as described in <https://cloud.google.com/apis/design/resource_names>.  
  
## ServiceLevelIndicator

A Service-Level Indicator (SLI) describes the "performance" of a service. For some services, the SLI is well-defined. In such cases, the SLI can be described easily by referencing the well-known SLI and providing the needed parameters. Alternatively, a "custom" SLI can be defined with a query to the underlying metric store. An SLI is defined to be `good_service / total_service` over any queried time interval. The value of performance always falls into the range `0 <= performance <= 1`. A custom SLI describes how to compute this ratio, whether this is by dividing values from a pair of time series, cutting a `Distribution` into good and bad counts, or counting time windows in which the service complies with a criterion. For separation of concerns, a single Service-Level Indicator measures performance for only one aspect of service quality, such as fraction of successful queries or fast-enough queries.

Fields  
---  
Union field `type`. Service level indicators can be grouped by whether the "unit" of service being measured is based on counts of good requests or on counts of good time windows `type` can be only one of the following:  
`basic_sli` |  `[BasicSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.BasicSli)` Basic SLI on a well-known service type.  
`request_based` |  `[RequestBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.RequestBasedSli)` Request-based SLIs  
`windows_based` |  `[WindowsBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.WindowsBasedSli)` Windows-based SLIs  
  
## ServiceLevelObjective

A Service-Level Objective (SLO) describes a level of desired good service. It consists of a service-level indicator (SLI), a performance goal, and a period over which the objective is to be evaluated against that goal. The SLO can use SLIs defined in a number of different manners. Typical SLOs might include "99% of requests in each rolling week have latency below 200 milliseconds" or "99.5% of requests in each calendar month return successfully."

Fields  
---  
`name` |  `string` Identifier. Resource name for this `ServiceLevelObjective`. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]
      
  
`display_name` |  `string` Name used for UI elements listing this SLO.  
`service_level_indicator` |  `[ServiceLevelIndicator](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelIndicator)` The definition of good service, used to measure and calculate the quality of the `Service`'s performance with respect to a single aspect of service quality.  
`goal` |  `double` The fraction of service that must be good in order for this objective to be met. `0 < goal <= 0.9999`.  
`user_labels` |  `map<string, string>` Labels which have been used to annotate the service-level objective. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value.  
Union field `period`. The time period over which the objective will be evaluated. `period` can be only one of the following:  
`rolling_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` A rolling time period, semantically "in the past `<rolling_period>`". Must be an integer multiple of 1 day no larger than 30 days.  
`calendar_period` |  `[CalendarPeriod](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type#google.type.CalendarPeriod)` A calendar period, semantically "since the start of the current `<calendar_period>`". At this time, only `DAY`, `WEEK`, `FORTNIGHT`, and `MONTH` are supported.  
  
## View

`ServiceLevelObjective.View` determines what form of `ServiceLevelObjective` is returned from `GetServiceLevelObjective`, `ListServiceLevelObjectives`, and `ListServiceLevelObjectiveVersions` RPCs.

Enums  
---  
`VIEW_UNSPECIFIED` | Same as FULL.  
`FULL` | Return the embedded `ServiceLevelIndicator` in the form in which it was defined. If it was defined using a `BasicSli`, return that `BasicSli`.  
`EXPLICIT` | For `ServiceLevelIndicator`s using `BasicSli` articulation, instead return the `ServiceLevelIndicator` with its mode of computation fully spelled out as a `RequestBasedSli`. For `ServiceLevelIndicator`s using `RequestBasedSli` or `WindowsBasedSli`, return the `ServiceLevelIndicator` as it was provided.  
  
## Snooze

A `Snooze` will prevent any alerts from being opened, and close any that are already open. The `Snooze` will work on alerts that match the criteria defined in the `Snooze`. The `Snooze` will be active from `interval.start_time` through `interval.end_time`.

Fields  
---  
`name` |  `string` Required. Identifier. The name of the `Snooze`. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/snoozes/[SNOOZE_ID]
    

The ID of the `Snooze` will be generated by the system.  
`criteria` |  `[Criteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze.Criteria)` Required. This defines the criteria for applying the `Snooze`. See `Criteria` for more information.  
`interval` |  `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` Required. The `Snooze` will be active from `interval.start_time` through `interval.end_time`. `interval.start_time` cannot be in the past. There is a 15 second clock skew to account for the time it takes for a request to reach the API from the UI.  
`display_name` |  `string` Required. A display name for the `Snooze`. This can be, at most, 512 unicode characters.  
  
## Criteria

Criteria specific to the `AlertPolicy`s that this `Snooze` applies to. The `Snooze` will suppress alerts that come from one of the `AlertPolicy`s whose names are supplied.

Fields  
---  
`policies[]` |  `string` The specific `AlertPolicy` names for the alert that should be snoozed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[POLICY_ID]
    

There is a limit of 16 policies per snooze. This limit is checked during snooze creation. Exactly 1 alert policy is required if `filter` is specified at the same time.  
`filter` |  `string` Optional. When you define a snooze, you can also define a filter for that snooze. The filter is a string containing one or more key-value pairs. The string uses the standard <https://google.aip.dev/160> filter syntax. If you define a filter for a snooze, then the snooze can only apply to one alert policy. When the snooze is active, incidents won't be created when the incident would have key-value pairs (labels) that match those specified by the filter in the snooze.Snooze filters support resource, metric, and metadata labels. If multiple labels are used, then they must be connected with an AND operator. For example, the following filter applies the snooze to incidents that have a resource label with an instance ID of `1234567890`, a metric label with an instance name of `test_group`, a metadata user label with a key of `foo` and a value of `bar`, and a metadata system label with a key of `region` and a value of `us-central1`:
    
    
    "filter": "resource.labels.instance_id=\"1234567890\" AND
    metric.labels.instance_name=\"test_group\" AND
    metadata.user_labels.foo=\"bar\" AND
    metadata.system_labels.region=\"us-central1\""
      
  
## SpanContext

The context of a span. This is attached to an `[Exemplar](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.Exemplar)` in `[Distribution](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution)` values during aggregation.

It contains the name of a span with format:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

Fields  
---  
`span_name` |  `string` The resource name of the span. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

`[TRACE_ID]` is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array.`[SPAN_ID]` is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array.  
  
## SyntheticMonitorTarget

Describes a Synthetic Monitor to be invoked by Uptime.

Fields  
---  
Union field `target`. Specifies a Synthetic Monitor's execution stack. `target` can be only one of the following:  
`cloud_function_v2` |  `[CloudFunctionV2Target](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SyntheticMonitorTarget.CloudFunctionV2Target)` Target a Synthetic Monitor GCFv2 instance.  
  
## CloudFunctionV2Target

A Synthetic Monitor deployed to a Cloud Functions V2 instance.

Fields  
---  
`name` |  `string` Required. Fully qualified GCFv2 resource name i.e. `projects/{project}/locations/{location}/functions/{function}` Required.  
`cloud_run_revision` |  `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` Output only. The `cloud_run_revision` Monitored Resource associated with the GCFv2. The Synthetic Monitor execution results (metrics, logs, and spans) are reported against this Monitored Resource. This field is output only.  
  
## TextLocator

A locator for text. Indicates a particular part of the text of a request or of an object referenced in the request.

For example, suppose the request field `text` contains:

text: "The quick brown fox jumps over the lazy dog."

Then the locator:

source: "text" start_position { line: 1 column: 17 } end_position { line: 1 column: 19 }

refers to the part of the text: "fox".

Fields  
---  
`source` |  `string` The source of the text. The source may be a field in the request, in which case its format is the format of the google.rpc.BadRequest.FieldViolation.field field in <https://cloud.google.com/apis/design/errors#error_details>. It may also be be a source other than the request field (e.g. a macro definition referenced in the text of the query), in which case this is the name of the source (e.g. the macro name).  
`start_position` |  `[Position](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TextLocator.Position)` The position of the first byte within the text.  
`end_position` |  `[Position](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TextLocator.Position)` The position of the last byte within the text.  
`nested_locator` |  `[TextLocator](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TextLocator)` If `source`, `start_position`, and `end_position` describe a call on some object (e.g. a macro in the time series query language text) and a location is to be designated in that object's text, `nested_locator` identifies the location within that object.  
`nesting_reason` |  `string` When `nested_locator` is set, this field gives the reason for the nesting. Usually, the reason is a macro invocation. In that case, the macro name (including the leading '@') signals the location of the macro call in the text and a macro argument name (including the leading '$') signals the location of the macro argument inside the macro body that got substituted away.  
  
## Position

The position of a byte within the text.

Fields  
---  
`line` |  `int32` The line, starting with 1, where the byte is positioned.  
`column` |  `int32` The column within the line, starting with 1, where the byte is positioned. This is a byte index even though the text is UTF-8.  
  
## TimeInterval

Describes a time interval:

  * Reads: A half-open time interval. It includes the end time but excludes the start time: `(startTime, endTime]`. The start time must be specified, must be earlier than the end time, and should be no older than the data retention period for the metric.
  * Writes: A closed time interval. It extends from the start time to the end time, and includes both: `[startTime, endTime]`. Valid time intervals depend on the [`MetricKind`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind) of the metric value. The end time must not be earlier than the start time, and the end time must not be more than 25 hours in the past or more than five minutes in the future. 
    * For `GAUGE` metrics, the `startTime` value is technically optional; if no value is specified, the start time defaults to the value of the end time, and the interval represents a single point in time. If both start and end times are specified, they must be identical. Such an interval is valid only for `GAUGE` metrics, which are point-in-time measurements. The end time of a new interval must be at least a millisecond after the end time of the previous interval.
    * For `DELTA` metrics, the start time and end time must specify a non-zero interval, with subsequent points specifying contiguous and non-overlapping intervals. For `DELTA` metrics, the start time of the next interval must be at least a millisecond after the end time of the previous interval.
    * For `CUMULATIVE` metrics, the start time and end time must specify a non-zero interval, with subsequent points specifying the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points. The new start time must be at least a millisecond after the end time of the previous interval.
    * The start time of a new interval must be at least a millisecond after the end time of the previous interval because intervals are closed. If the start time of a new interval is the same as the end time of the previous interval, then data written at the new start time could overwrite data written at the previous end time.

Fields  
---  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. The end of the time interval.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. The beginning of the time interval. The default value for the start time is the end time. The start time must not be later than the end time.  
  
## TimeSeries

A collection of data points that describes the time-varying values of a metric. A time series is identified by a combination of a fully-specified monitored resource and a fully-specified metric. This type is used for both listing and creating time series.

Fields  
---  
`metric` |  `[Metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Metric)` The associated metric. A fully-specified metric used to identify the time series.  
`resource` |  `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` The associated monitored resource. Custom metrics can use only certain monitored resource types in their time series data. For more information, see [Monitored resources for custom metrics](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#custom-metric-resources).  
`metadata` |  `[MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceMetadata)` Output only. The associated monitored resource metadata. When reading a time series, this field will include metadata labels that are explicitly named in the reduction. When creating a time series, this field is ignored.  
`metric_kind` |  `[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind)` The metric kind of the time series. When listing time series, this metric kind might be different from the metric kind of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`.  
`value_type` |  `[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.ValueType)` The value type of the time series. When listing time series, this value type might be different from the value type of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the type of the data in the `points` field.  
`points[]` |  `[Point](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Point)` The data points of this time series. When listing time series, points are returned in reverse time order.When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values. This field can only be changed through CreateTimeSeries when it is empty.  
`description` |  `string` Input only. A detailed description of the time series that will be associated with the `[google.api.MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)` for the metric. Once set, this field cannot be changed through CreateTimeSeries.  
  
## TimeSeriesData

Represents the values of a time series associated with a TimeSeriesDescriptor.

Fields  
---  
`label_values[]` |  `[LabelValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.LabelValue)` The values of the labels in the time series identifier, given in the same order as the `label_descriptors` field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of `label_descriptors`.  
`point_data[]` |  `[PointData](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesData.PointData)` The points in the time series.  
  
## PointData

A point's value columns and time interval. Each point has one or more point values corresponding to the entries in `point_descriptors` field in the TimeSeriesDescriptor associated with this object.

Fields  
---  
`values[]` |  `[TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TypedValue)` The values that make up the point.  
`time_interval` |  `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` The time interval associated with the point.  
  
## TimeSeriesDescriptor

A descriptor for the labels and points in a time series.

Fields  
---  
`label_descriptors[]` |  `[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LabelDescriptor)` Descriptors for the labels.  
`point_descriptors[]` |  `[ValueDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeriesDescriptor.ValueDescriptor)` Descriptors for the point data value columns.  
  
## ValueDescriptor

A descriptor for the value columns in a data point.

Fields  
---  
`key` |  `string` The value key.  
`value_type` |  `[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.ValueType)` The value type.  
`metric_kind` |  `[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind)` The value stream kind.  
`unit` |  `string` The unit in which `time_series` point values are reported. `unit` follows the UCUM format for units as seen in <https://unitsofmeasure.org/ucum.html>. `unit` is only valid if `value_type` is INTEGER, DOUBLE, DISTRIBUTION.  
  
## TimeSeriesRatio

A `TimeSeriesRatio` specifies two `TimeSeries` to use for computing the `good_service / total_service` ratio. The specified `TimeSeries` must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. The `TimeSeriesRatio` must specify exactly two of good, bad, and total, and the relationship `good_service + bad_service = total_service` will be assumed.

Fields  
---  
`good_service_filter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` quantifying good service provided. Must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
`bad_service_filter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` quantifying bad service, either demanded service that was not provided or demanded service that was of inadequate quality. Must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
`total_service_filter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` quantifying total demanded service. Must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
  
## TypedValue

A single strongly-typed value.

Fields  
---  
Union field `value`. The typed value field. `value` can be only one of the following:  
`bool_value` |  `bool` A Boolean value: `true` or `false`.  
`int64_value` |  `int64` A 64-bit integer. Its range is approximately ±9.2x1018.  
`double_value` |  `double` A 64-bit double-precision floating-point number. Its magnitude is approximately ±10±300 and it has 16 significant digits of precision.  
`string_value` |  `string` A variable-length string value.  
`distribution_value` |  `[Distribution](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution)` A distribution value.  
  
## UpdateAlertPolicyRequest

The protocol for the `UpdateAlertPolicy` request.

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. A list of alerting policy field names. If this field is not empty, each listed field in the existing alerting policy is set to the value of the corresponding field in the supplied policy (`alert_policy`), or to the field's default value if the field is not in the supplied alerting policy. Fields not listed retain their previous value.Examples of valid field masks include `display_name`, `documentation`, `documentation.content`, `documentation.mime_type`, `user_labels`, `user_label.nameofkey`, `enabled`, `conditions`, `combiner`, etc.If this field is empty, then the supplied alerting policy replaces the existing policy. It is the same as deleting the existing policy and adding the supplied policy, except for the following:

  * The new policy will have the same `[ALERT_POLICY_ID]` as the former policy. This gives you continuity with the former policy in your notifications and incidents.
  * Conditions in the new policy will keep their former `[CONDITION_ID]` if the supplied condition includes the `name` field with that `[CONDITION_ID]`. If the supplied condition omits the `name` field, then a new `[CONDITION_ID]` is created.

  
`alert_policy` |  `[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.AlertPolicy)` Required. The updated alerting policy or the updated values for the fields listed in `update_mask`. If `update_mask` is not empty, any fields in this policy that are not in `update_mask` are ignored. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `alertPolicy`:

  * `monitoring.alertPolicies.update`

  
  
## UpdateGroupRequest

The `UpdateGroup` request.

Fields  
---  
`group` |  `[Group](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Group)` Required. The new definition of the group. All fields of the existing group, excepting `name`, are replaced with the corresponding fields of this group.  
`validate_only` |  `bool` If true, validate this request but do not update the existing group.  
  
## UpdateNotificationChannelRequest

The `UpdateNotificationChannel` request.

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The fields to update.  
`notification_channel` |  `[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.NotificationChannel)` Required. A description of the changes to be applied to the specified notification channel. The description must provide a definition for fields to be updated; the names of these fields should also be included in the `update_mask`.  
  
## UpdateServiceLevelObjectiveRequest

The `UpdateServiceLevelObjective` request.

Fields  
---  
`service_level_objective` |  `[ServiceLevelObjective](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.ServiceLevelObjective)` Required. The `ServiceLevelObjective` to draw updates from. The given `name` specifies the resource to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` A set of field paths defining which fields to use for the update.  
  
## UpdateServiceRequest

The `UpdateService` request.

Fields  
---  
`service` |  `[Service](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Service)` Required. The `Service` to draw updates from. The given `name` specifies the resource to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` A set of field paths defining which fields to use for the update.  
  
## UpdateSnoozeRequest

The message definition for updating a `Snooze`. The field, `snooze.name` identifies the `Snooze` to be updated. The remainder of `snooze` gives the content the `Snooze` in question will be assigned.

What fields can be updated depends on the start time and end time of the `Snooze`.

  * end time is in the past: These `Snooze`s are considered read-only and cannot be updated.
  * start time is in the past and end time is in the future: `display_name` and `interval.end_time` can be updated.
  * start time is in the future: `display_name`, `interval.start_time` and `interval.end_time` can be updated.

Fields  
---  
`snooze` |  `[Snooze](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Snooze)` Required. The `Snooze` to update. Must have the name field present.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The fields to update.For each field listed in `update_mask`:

  * If the `Snooze` object supplied in the `UpdateSnoozeRequest` has a value for that field, the value of the field in the existing `Snooze` will be set to the value of the field in the supplied `Snooze`.
  * If the field does not have a value in the supplied `Snooze`, the field in the existing `Snooze` is set to its default value.

Fields not listed retain their existing value.The following are the field names that are accepted in `update_mask`:

  * `display_name`
  * `interval.start_time`
  * `interval.end_time`

That said, the start time and end time of the `Snooze` determines which fields can legally be updated. Before attempting an update, users should consult the documentation for `UpdateSnoozeRequest`, which talks about which fields can be updated.  
  
## UpdateUptimeCheckConfigRequest

The protocol for the `UpdateUptimeCheckConfig` request.

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. If present, only the listed fields in the current Uptime check configuration are updated with values from the new configuration. If this field is empty, then the current configuration is completely replaced with the new configuration.  
`uptime_check_config` |  `[UptimeCheckConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig)` Required. If an `updateMask` has been specified, this field gives the values for the set of fields mentioned in the `updateMask`. If an `updateMask` has not been given, this Uptime check configuration replaces the current configuration. If a field is mentioned in `updateMask` but the corresponding field is omitted in this partial Uptime check configuration, it has the effect of deleting/clearing the field from the configuration on the server.The following fields can be updated: `display_name`, `http_check`, `tcp_check`, `timeout`, `content_matchers`, and `selected_regions`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `uptimeCheckConfig`:

  * `monitoring.uptimeCheckConfigs.update`

  
  
## UptimeCheckConfig

This message configures which resources and services to monitor for availability.

Fields  
---  
`name` |  `string` Identifier. A unique resource name for this Uptime check configuration. The format is:
    
    
     projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID]
    

`[PROJECT_ID_OR_NUMBER]` is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response.  
`display_name` |  `string` A human-friendly name for the Uptime check configuration. The display name should be unique within a Cloud Monitoring Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required.  
`period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` How often, in seconds, the Uptime check is performed. Currently, the only supported values are `60s` (1 minute), `300s` (5 minutes), `600s` (10 minutes), and `900s` (15 minutes). Optional, defaults to `60s`.  
`timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required.  
`content_matchers[]` |  `[ContentMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher)` The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the `content_matchers` list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check.  
`checker_type` |  `[CheckerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.CheckerType)` The type of checkers to use to execute the Uptime check.  
`disabled` |  `bool` Whether the check is disabled or not.  
`selected_regions[]` |  `[UptimeCheckRegion](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckRegion)` The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions.  
`log_check_failures` |  `bool` To specify whether to log the results of failed probes to Cloud Logging.  
`is_internal  
**(deprecated)**` |  `bool` This item is deprecated!If this is `true`, then checks are made only from the 'internal_checkers'. If it is `false`, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is `true`, or to provide 'internal_checkers' when is_internal is `false`.  
`internal_checkers[]  
**(deprecated)**` |  `[InternalChecker](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.InternalChecker)` This item is deprecated!The internal checkers that this check will egress from. If `is_internal` is `true` and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this `UptimeCheckConfig`.  
`user_labels` |  `map<string, string>` User-supplied key/value data to be used for organizing and identifying the `UptimeCheckConfig` objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.  
Union field `resource`. The resource the check is checking. Required. `resource` can be only one of the following:  
`monitored_resource` |  `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` The [monitored resource](https://cloud.google.com/monitoring/api/resources) associated with the configuration. The following monitored resource types are valid for this field: `uptime_url`, `gce_instance`, `gae_app`, `aws_ec2_instance`, `aws_elb_load_balancer` `k8s_service` `servicedirectory_service` `cloud_run_revision`  
`resource_group` |  `[ResourceGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ResourceGroup)` The group resource associated with the configuration.  
`synthetic_monitor` |  `[SyntheticMonitorTarget](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.SyntheticMonitorTarget)` Specifies a Synthetic Monitor to invoke.  
Union field `check_request_type`. The type of Uptime check request. `check_request_type` can be only one of the following:  
`http_check` |  `[HttpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck)` Contains information needed to make an HTTP or HTTPS check.  
`tcp_check` |  `[TcpCheck](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.TcpCheck)` Contains information needed to make a TCP check.  
  
## CheckerType

What kind of checkers are available to be used by the check.

Enums  
---  
`CHECKER_TYPE_UNSPECIFIED` | The default checker type. Currently converted to `STATIC_IP_CHECKERS` on creation, the default conversion behavior may change in the future.  
`STATIC_IP_CHECKERS` | `STATIC_IP_CHECKERS` are used for uptime checks that perform egress across the public internet. `STATIC_IP_CHECKERS` use the static IP addresses returned by `ListUptimeCheckIps`.  
`VPC_CHECKERS` | `VPC_CHECKERS` are used for uptime checks that perform egress using Service Directory and private network access. When using `VPC_CHECKERS`, the monitored resource type must be `servicedirectory_service`.  
  
## ContentMatcher

Optional. Used to perform content matching. This allows matching based on substrings and regular expressions, together with their negations. Only the first 4 MB of an HTTP or HTTPS check's response (and the first 1 MB of a TCP check's response) are examined for purposes of content matching.

Fields  
---  
`content` |  `string` String, regex or JSON content to match. Maximum 1024 bytes. An empty `content` string indicates no content matching is to be performed.  
`matcher` |  `[ContentMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher.ContentMatcherOption)` The type of content matcher that will be applied to the server output, compared to the `content` string when the check is run.  
Union field `additional_matcher_info`. Certain `ContentMatcherOption` types require additional information. `MATCHES_JSON_PATH` or `NOT_MATCHES_JSON_PATH` require a `JsonPathMatcher`; not used for other options. `additional_matcher_info` can be only one of the following:  
`json_path_matcher` |  `[JsonPathMatcher](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher.JsonPathMatcher)` Matcher information for `MATCHES_JSON_PATH` and `NOT_MATCHES_JSON_PATH`  
  
## ContentMatcherOption

Options to perform content matching.

Enums  
---  
`CONTENT_MATCHER_OPTION_UNSPECIFIED` | No content matcher type specified (maintained for backward compatibility, but deprecated for future use). Treated as `CONTAINS_STRING`.  
`CONTAINS_STRING` | Selects substring matching. The match succeeds if the output contains the `content` string. This is the default value for checks without a `matcher` option, or where the value of `matcher` is `CONTENT_MATCHER_OPTION_UNSPECIFIED`.  
`NOT_CONTAINS_STRING` | Selects negation of substring matching. The match succeeds if the output does _NOT_ contain the `content` string.  
`MATCHES_REGEX` | Selects regular-expression matching. The match succeeds if the output matches the regular expression specified in the `content` string. Regex matching is only supported for HTTP/HTTPS checks.  
`NOT_MATCHES_REGEX` | Selects negation of regular-expression matching. The match succeeds if the output does _NOT_ match the regular expression specified in the `content` string. Regex matching is only supported for HTTP/HTTPS checks.  
`MATCHES_JSON_PATH` | Selects JSONPath matching. See `JsonPathMatcher` for details on when the match succeeds. JSONPath matching is only supported for HTTP/HTTPS checks.  
`NOT_MATCHES_JSON_PATH` | Selects JSONPath matching. See `JsonPathMatcher` for details on when the match succeeds. Succeeds when output does _NOT_ match as specified. JSONPath is only supported for HTTP/HTTPS checks.  
  
## JsonPathMatcher

Information needed to perform a JSONPath content match. Used for `ContentMatcherOption::MATCHES_JSON_PATH` and `ContentMatcherOption::NOT_MATCHES_JSON_PATH`.

Fields  
---  
`json_path` |  `string` JSONPath within the response output pointing to the expected `ContentMatcher::content` to match against.  
`json_matcher` |  `[JsonPathMatcherOption](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.ContentMatcher.JsonPathMatcher.JsonPathMatcherOption)` The type of JSONPath match that will be applied to the JSON output (`ContentMatcher.content`)  
  
## JsonPathMatcherOption

Options to perform JSONPath content matching.

Enums  
---  
`JSON_PATH_MATCHER_OPTION_UNSPECIFIED` | No JSONPath matcher type specified (not valid).  
`EXACT_MATCH` | Selects 'exact string' matching. The match succeeds if the content at the `json_path` within the output is exactly the same as the `content` string.  
`REGEX_MATCH` | Selects regular-expression matching. The match succeeds if the content at the `json_path` within the output matches the regular expression specified in the `content` string.  
  
## HttpCheck

Information involved in an HTTP/HTTPS Uptime check request.

Fields  
---  
`request_method` |  `[RequestMethod](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.RequestMethod)` The HTTP request method to use for the check. If set to `METHOD_UNSPECIFIED` then `request_method` defaults to `GET`.  
`use_ssl` |  `bool` If `true`, use HTTPS instead of HTTP to run the check.  
`path` |  `string` Optional (defaults to "/"). The path to the page against which to run the check. Will be combined with the `host` (specified within the `monitored_resource`) and `port` to construct the full URL. If the provided path does not begin with "/", a "/" will be prepended automatically.  
`port` |  `int32` Optional (defaults to 80 when `use_ssl` is `false`, and 443 when `use_ssl` is `true`). The TCP port on the HTTP server against which to run the check. Will be combined with host (specified within the `monitored_resource`) and `path` to construct the full URL.  
`auth_info` |  `[BasicAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication)` The authentication information. Optional when creating an HTTP check; defaults to empty. Do not set both `auth_method` and `auth_info`.  
`mask_headers` |  `bool` Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if `mask_headers` is set to `true` then the headers will be obscured with `******.`  
`headers` |  `map<string, string>` The list of headers to send as part of the Uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at <https://www.w3.org/Protocols/rfc2616/rfc2616.txt> (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.  
`content_type` |  `[ContentType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ContentType)` The content type header to use for the check. The following configurations result in errors: 1. Content type is specified in both the `headers` field and the `content_type` field. 2. Request method is `GET` and `content_type` is not `TYPE_UNSPECIFIED` 3\. Request method is `POST` and `content_type` is `TYPE_UNSPECIFIED`. 4. Request method is `POST` and a "Content-Type" header is provided via `headers` field. The `content_type` field should be used instead.  
`custom_content_type` |  `string` A user provided content type header to use for the check. The invalid configurations outlined in the `content_type` field apply to `custom_content_type`, as well as the following: 1. `content_type` is `URL_ENCODED` and `custom_content_type` is set. 2. `content_type` is `USER_PROVIDED` and `custom_content_type` is not set.  
`validate_ssl` |  `bool` Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where `monitored_resource` is set to `uptime_url`. If `use_ssl` is `false`, setting `validate_ssl` to `true` has no effect.  
`body` |  `bytes` The request body associated with the HTTP POST request. If `content_type` is `URL_ENCODED`, the body passed in must be URL-encoded. Users can provide a `Content-Length` header via the `headers` field or the API will do so. If the `request_method` is `GET` and `body` is not empty, the API will return an error. The maximum byte size is 1 megabyte.Note: If client libraries aren't used (which performs the conversion automatically) base64 encode your `body` data since the field is of `bytes` type.  
`accepted_response_status_codes[]` |  `[ResponseStatusCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ResponseStatusCode)` If present, the check will only pass if the HTTP response status code is in this set of status codes. If empty, the HTTP status code will only pass if the HTTP status code is 200-299.  
`ping_config` |  `[PingConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.PingConfig)` Contains information needed to add pings to an HTTP check.  
Union field `auth_method`. This field is optional and should be set only by users interested in an authenticated uptime check. Do not set both `auth_method` and `auth_info`. `auth_method` can be only one of the following:  
`service_agent_authentication` |  `[ServiceAgentAuthentication](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication)` If specified, Uptime will generate and attach an OIDC JWT token for the Monitoring service agent service account as an `Authorization` header in the HTTP request when probing.  
  
## BasicAuthentication

The authentication parameters to provide to the specified resource or URL that requires a username and password. Currently, only [Basic HTTP authentication](https://tools.ietf.org/html/rfc7617) is supported in Uptime checks.

Fields  
---  
`username` |  `string` The username to use when authenticating with the HTTP server.  
`password` |  `string` The password to use when authenticating with the HTTP server.  
  
## ContentType

Header options corresponding to the content type of a HTTP request body.

Enums  
---  
`TYPE_UNSPECIFIED` | No content type specified.  
`URL_ENCODED` | `body` is in URL-encoded form. Equivalent to setting the `Content-Type` to `application/x-www-form-urlencoded` in the HTTP request.  
`USER_PROVIDED` | `body` is in `custom_content_type` form. Equivalent to setting the `Content-Type` to the contents of `custom_content_type` in the HTTP request.  
  
## RequestMethod

The HTTP request method options.

Enums  
---  
`METHOD_UNSPECIFIED` | No request method specified.  
`GET` | GET request.  
`POST` | POST request.  
  
## ResponseStatusCode

A status to accept. Either a status code class like "2xx", or an integer status code like "200".

Fields  
---  
Union field `status_code`. Either a specific value or a class of status codes. `status_code` can be only one of the following:  
`status_value` |  `int32` A status code to accept.  
`status_class` |  `[StatusClass](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ResponseStatusCode.StatusClass)` A class of status codes to accept.  
  
## StatusClass

An HTTP status code class.

Enums  
---  
`STATUS_CLASS_UNSPECIFIED` | Default value that matches no status codes.  
`STATUS_CLASS_1XX` | The class of status codes between 100 and 199.  
`STATUS_CLASS_2XX` | The class of status codes between 200 and 299.  
`STATUS_CLASS_3XX` | The class of status codes between 300 and 399.  
`STATUS_CLASS_4XX` | The class of status codes between 400 and 499.  
`STATUS_CLASS_5XX` | The class of status codes between 500 and 599.  
`STATUS_CLASS_ANY` | The class of all status codes.  
  
## ServiceAgentAuthentication

Contains information needed for generating either an [OpenID Connect token](https://developers.google.com/identity/protocols/OpenIDConnect) or [OAuth token](https://developers.google.com/identity/protocols/oauth2). The token will be generated for the Monitoring service agent service account.

Fields  
---  
`type` |  `[ServiceAgentAuthenticationType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.HttpCheck.ServiceAgentAuthentication.ServiceAgentAuthenticationType)` Type of authentication.  
  
## ServiceAgentAuthenticationType

Type of authentication.

Enums  
---  
`SERVICE_AGENT_AUTHENTICATION_TYPE_UNSPECIFIED` | Default value, will result in OIDC Authentication.  
`OIDC_TOKEN` | OIDC Authentication  
  
## PingConfig

Information involved in sending ICMP pings alongside public HTTP/TCP checks. For HTTP, the pings are performed for each part of the redirect chain.

Fields  
---  
`pings_count` |  `int32` Number of ICMP pings. A maximum of 3 ICMP pings is currently supported.  
  
## ResourceGroup

The resource submessage for group checks. It can be used instead of a monitored resource, when multiple resources are being monitored.

Fields  
---  
`group_id` |  `string` The group of resources being monitored. Should be only the `[GROUP_ID]`, and not the full-path `projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]`.  
`resource_type` |  `[GroupResourceType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.GroupResourceType)` The resource type of the group members.  
  
## TcpCheck

Information required for a TCP Uptime check request.

Fields  
---  
`port` |  `int32` The TCP port on the server against which to run the check. Will be combined with host (specified within the `monitored_resource`) to construct the full URL. Required.  
`ping_config` |  `[PingConfig](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckConfig.PingConfig)` Contains information needed to add pings to a TCP check.  
  
## UptimeCheckIp

Contains the region, location, and list of IP addresses where checkers in the location run from.

Fields  
---  
`region` |  `[UptimeCheckRegion](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.UptimeCheckRegion)` A broad region category in which the IP address is located.  
`location` |  `string` A more specific location within the region that typically encodes a particular city/town/metro (and its containing state/province or country) within the broader umbrella region category.  
`ip_address` |  `string` The IP address from which the Uptime check originates. This is a fully specified IP address (not an IP address range). Most IP addresses, as of this publication, are in IPv4 format; however, one should not rely on the IP addresses being in IPv4 format indefinitely, and should support interpreting this field in either IPv4 or IPv6 format.  
  
## UptimeCheckRegion

The regions from which an Uptime check can be run.

Enums  
---  
`REGION_UNSPECIFIED` | Default value if no region is specified. Will result in Uptime checks running from all regions.  
`USA` | Allows checks to run from locations within the United States of America.  
`EUROPE` | Allows checks to run from locations within the continent of Europe.  
`SOUTH_AMERICA` | Allows checks to run from locations within the continent of South America.  
`ASIA_PACIFIC` | Allows checks to run from locations within the Asia Pacific area (ex: Singapore).  
`USA_OREGON` | Allows checks to run from locations within the western United States of America  
`USA_IOWA` | Allows checks to run from locations within the central United States of America  
`USA_VIRGINIA` | Allows checks to run from locations within the eastern United States of America  
  
## VerifyNotificationChannelRequest

The `VerifyNotificationChannel` request.

Fields  
---  
`name` |  `string` Required. The notification channel to verify. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.verify`

  
`code` |  `string` Required. The verification code that was delivered to the channel as a result of invoking the `SendNotificationChannelVerificationCode` API method or that was retrieved from a verified channel via `GetNotificationChannelVerificationCode`. For example, one might have "G-123456" or "TKNZGhhd2EyN3I1MnRnMjRv" (in general, one is only guaranteed that the code is valid UTF-8; one should not make any assumptions regarding the structure or format of the code).  
  
## WindowsBasedSli

A `WindowsBasedSli` defines `good_service` as the count of time windows for which the provided service was of good quality. Criteria for determining if service was good are embedded in the `window_criterion`.

Fields  
---  
`window_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Duration over which window quality is evaluated. Must be an integer fraction of a day and at least `60s`.  
Union field `window_criterion`. The criterion to use for evaluating window goodness. `window_criterion` can be only one of the following:  
`good_bad_metric_filter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` with `ValueType = BOOL`. The window is good if any `true` values appear in the window.  
`good_total_ratio_threshold` |  `[PerformanceThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.WindowsBasedSli.PerformanceThreshold)` A window is good if its `performance` is high enough.  
`metric_mean_in_range` |  `[MetricRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.WindowsBasedSli.MetricRange)` A window is good if the metric's value is in a good range, averaged across returned streams.  
`metric_sum_in_range` |  `[MetricRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.WindowsBasedSli.MetricRange)` A window is good if the metric's value is in a good range, summed across returned streams.  
  
## MetricRange

A `MetricRange` is used when each window is good when the value x of a single `TimeSeries` satisfies `range.min <= x <= range.max`. The provided `TimeSeries` must have `ValueType = INT64` or `ValueType = DOUBLE` and `MetricKind = GAUGE`.

Fields  
---  
`time_series` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying the `TimeSeries` to use for evaluating window quality.  
`range` |  `[Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.Range)` Range of values considered "good." For a one-sided range, set one bound to an infinite value.  
  
## PerformanceThreshold

A `PerformanceThreshold` is used when each window is good when that window has a sufficiently high `performance`.

Fields  
---  
`threshold` |  `double` If window `performance >= threshold`, the window is counted as good.  
Union field `type`. The means, either a request-based SLI or a basic SLI, by which to compute performance over a window. `type` can be only one of the following:  
`performance` |  `[RequestBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.RequestBasedSli)` `RequestBasedSli` to evaluate to judge window quality.  
`basic_sli_performance` |  `[BasicSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.BasicSli)` `BasicSli` to evaluate to judge window quality.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 
