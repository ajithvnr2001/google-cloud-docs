---
url: https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta
title: Package google.cloud.databasecenter.v1beta \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:29.766964+00:00
---

# Package google.cloud.databasecenter.v1beta  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Package google.cloud.databasecenter.v1beta Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[DatabaseCenter](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseCenter)` (interface)
  * `[AdditionalDetail](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AdditionalDetail)` (message)
  * `[AggregateFleetRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateFleetRequest)` (message)
  * `[AggregateFleetResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateFleetResponse)` (message)
  * `[AggregateFleetRow](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateFleetRow)` (message)
  * `[AggregateIssueStatsRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateIssueStatsRequest)` (message)
  * `[AggregateIssueStatsResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateIssueStatsResponse)` (message)
  * `[AutomatedBackupPolicyInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AutomatedBackupPolicyInfo)` (message)
  * `[BackupDRConfig](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.BackupDRConfig)` (message)
  * `[BackupRunInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.BackupRunInfo)` (message)
  * `[BackupRunInfo.State](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.BackupRunInfo.State)` (enum)
  * `[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResource)` (message)
  * `[DatabaseResourceGroup](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResourceGroup)` (message)
  * `[DatabaseResourceIssue](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResourceIssue)` (message)
  * `[DeletionProtectionInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DeletionProtectionInfo)` (message)
  * `[DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DeltaDetails)` (message)
  * `[Dimension](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Dimension)` (message)
  * `[Edition](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Edition)` (enum)
  * `[Engine](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Engine)` (enum)
  * `[InefficientQueryInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.InefficientQueryInfo)` (message)
  * `[IssueCount](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueCount)` (message)
  * `[IssueGroupStats](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueGroupStats)` (message)
  * `[IssueSeverity](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueSeverity)` (enum)
  * `[IssueStats](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueStats)` (message)
  * `[Label](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Label)` (message)
  * `[MachineConfig](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MachineConfig)` (message)
  * `[MaintenanceInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MaintenanceInfo)` (message)
  * `[MaintenanceRecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MaintenanceRecommendationInfo)` (message)
  * `[ManagementType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ManagementType)` (enum)
  * `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` (message)
  * `[Metrics](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Metrics)` (message)
  * `[OperationErrorType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.OperationErrorType)` (enum)
  * `[OutdatedMinorVersionInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.OutdatedMinorVersionInfo)` (message)
  * `[Phase](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Phase)` (enum)
  * `[Product](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Product)` (message)
  * `[ProductType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ProductType)` (enum)
  * `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryDatabaseResourceGroupsRequest)` (message)
  * `[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryDatabaseResourceGroupsResponse)` (message)
  * `[QueryIssuesRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryIssuesRequest)` (message)
  * `[QueryIssuesResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryIssuesResponse)` (message)
  * `[QueryProductsRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryProductsRequest)` (message)
  * `[QueryProductsResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryProductsResponse)` (message)
  * `[RecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.RecommendationInfo)` (message)
  * `[RegulatoryStandard](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.RegulatoryStandard)` (message)
  * `[ResourceCategory](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceCategory)` (enum)
  * `[ResourceDetails](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceDetails)` (message)
  * `[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceMaintenanceDenySchedule)` (message)
  * `[ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceMaintenanceSchedule)` (message)
  * `[ResourceSuspensionInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceSuspensionInfo)` (message)
  * `[RetentionSettingsInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.RetentionSettingsInfo)` (message)
  * `[SCCInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SCCInfo)` (message)
  * `[Signal](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Signal)` (message)
  * `[SignalFilter](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalFilter)` (message)
  * `[SignalGroup](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalGroup)` (message)
  * `[SignalProductsFilters](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalProductsFilters)` (message)
  * `[SignalSource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalSource)` (enum)
  * `[SignalStatus](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalStatus)` (enum)
  * `[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType)` (enum)
  * `[SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalTypeGroup)` (message)
  * `[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResource)` (message)
  * `[SubResourceType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResourceType)` (enum)
  * `[SuspensionReason](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SuspensionReason)` (enum)
  * `[Tag](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Tag)` (message)
  * `[TypedValue](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.TypedValue)` (message)



## DatabaseCenter

DatabaseCenter contains methods to query fleet view for database resources.

AggregateFleet  
---  
` rpc AggregateFleet(`[AggregateFleetRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateFleetRequest)`) returns (`[AggregateFleetResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateFleetResponse)`) ` AggregateFleet provides statistics about the fleet grouped by various fields.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.fleetStats.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
AggregateIssueStats  
---  
` rpc AggregateIssueStats(`[AggregateIssueStatsRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateIssueStatsRequest)`) returns (`[AggregateIssueStatsResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateIssueStatsResponse)`) ` AggregateIssueStats provides database resource issues statistics.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.fleetHealthStats.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
QueryDatabaseResourceGroups  
---  
` rpc QueryDatabaseResourceGroups(`[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryDatabaseResourceGroupsRequest)`) returns (`[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryDatabaseResourceGroupsResponse)`) ` QueryDatabaseResourceGroups returns paginated results of database groups.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.databaseGroups.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
QueryIssues  
---  
` rpc QueryIssues(`[QueryIssuesRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryIssuesRequest)`) returns (`[QueryIssuesResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryIssuesResponse)`) ` QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.fleetHealthStats.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
QueryProducts  
---  
` rpc QueryProducts(`[QueryProductsRequest](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryProductsRequest)`) returns (`[QueryProductsResponse](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.QueryProductsResponse)`) ` QueryProducts provides a list of all possible products which can be used to filter database resources.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.products.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## AdditionalDetail

Details related to signal.

Fields  
---  
`signal_source` |  `[SignalSource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalSource)` Where the signal is coming from.  
`signal_type` |  `[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType)` Type of the signal.  
`signal_event_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Event time when signal was recorded by source service.  
Union field `detail`. Details related to signal. `detail` can be only one of the following:  
`short_backup_retention_info` |  `[RetentionSettingsInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.RetentionSettingsInfo)` Short backup retention information applies to signals with type SIGNAL_TYPE_SHORT_BACKUP_RETENTION.  
`backup_run_info` |  `[BackupRunInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.BackupRunInfo)` Backup run information applies to signals with types SIGNAL_TYPE_LAST_BACKUP_FAILED and SIGNAL_TYPE_LAST_BACKUP_OLD.  
`scc_info` |  `[SCCInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SCCInfo)` SCC information applies to SCC signals.  
`recommendation_info` |  `[RecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.RecommendationInfo)` Recommendation information applies to recommendations.  
`automated_backup_policy_info` |  `[AutomatedBackupPolicyInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AutomatedBackupPolicyInfo)` Automated backup policy information applies to signals with type SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY.  
`deletion_protection_info` |  `[DeletionProtectionInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DeletionProtectionInfo)` Deletion protection information applies to signals with type `[SIGNAL_TYPE_NO_DELETION_PROTECTION](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType.ENUM_VALUES.google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_NO_DELETION_PROTECTION)`  
`resource_suspension_info` |  `[ResourceSuspensionInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceSuspensionInfo)` Resource suspension information applies to signals with type `[SIGNAL_TYPE_RESOURCE_SUSPENDED](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType.ENUM_VALUES.google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_RESOURCE_SUSPENDED)`.  
`inefficient_query_info` |  `[InefficientQueryInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.InefficientQueryInfo)` Inefficient query information applies to signals with type `[SIGNAL_TYPE_INEFFICIENT_QUERY](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType.ENUM_VALUES.google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_INEFFICIENT_QUERY)`.  
`outdated_minor_version_info` |  `[OutdatedMinorVersionInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.OutdatedMinorVersionInfo)` Outdated minor version information applies to signals with type SIGNAL_TYPE_OUTDATED_MINOR_VERSION.  
`maintenance_recommendation_info` |  `[MaintenanceRecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MaintenanceRecommendationInfo)` Maintenance recommendation information applies to signals with type SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES.  
  
## AggregateFleetRequest

The request message to aggregate fleet which are grouped by a field.

Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. The expression to filter resources.Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info, 'resource_name', etc.The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`  
`group_by` |  `string` Optional. A field that statistics are grouped by. Valid values are any combination of the following: * container * product.type * product.engine * product.version * location * sub_resource_type * management_type * tag.key * tag.value * tag.source * tag.inherited * label.key * label.value * label.source * has_maintenance_schedule * has_deny_maintenance_schedules Comma separated list.  
`order_by` |  `string` Optional. Valid values to order by are: * resource_groups_count * resources_count * and all fields supported by `group_by` The default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It supports ordering using multiple fields. For example: `order_by = "resource_groups_count"` sorts response in ascending order `order_by = "resource_groups_count DESC"` sorts response in descending order `order_by = "product.type, product.version DESC, location"` orders by type in ascending order, version in descending order and location in ascending order  
`page_size` |  `int32` Optional. If unspecified, at most 50 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `AggregateFleet` call. Provide this to retrieve the subsequent page. All other parameters should match the parameters in the call that provided the page token except for page_size which can be different.  
`baseline_date` |  `[Date](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.type#google.type.Date)` Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.  
  
## AggregateFleetResponse

The response message to aggregate a fleet by some group by fields.

Fields  
---  
`rows[]` |  `[AggregateFleetRow](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AggregateFleetRow)` Represents a row grouped by the fields in the input.  
`resource_groups_total_count` |  `int32` Count of all resource groups in the fleet. This includes counts from all pages.  
`resource_total_count` |  `int32` Count of all resources in the fleet. This includes counts from all pages.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
## AggregateFleetRow

Individual row grouped by a particular dimension.

Fields  
---  
`dimension[]` |  `[Dimension](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Dimension)` Group by dimension.  
`resource_groups_count` |  `int32` Number of resource groups that have a particular dimension.  
`resources_count` |  `int32` Number of resources that have a particular dimension.  
`delta_details` |  `[DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DeltaDetails)` Optional. Delta counts and details of resources which were added to/deleted from fleet.  
  
## AggregateIssueStatsRequest

AggregateIssueStatsRequest represents the input to the AggregateIssueStats method.

Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. The expression to filter resources.Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info,'resource_name', etc.The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"`  
`signal_type_groups[]` |  `[SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalTypeGroup)` Optional. Lists of signal types that are issues.  
`baseline_date` |  `[Date](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.type#google.type.Date)` Optional. The baseline date w.r.t. which the delta counts are calculated. If not set, delta counts are not included in the response and the response indicates the current state of the fleet.  
  
## AggregateIssueStatsResponse

The response message containing one of more group of relevant health issues for database resources.

Fields  
---  
`issue_group_stats[]` |  `[IssueGroupStats](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueGroupStats)` List of issue group stats where each group contains stats for resources having a particular combination of relevant issues.  
`total_resources_count` |  `int32` Total count of the resources filtered in based on the user given filter.  
`total_resource_groups_count` |  `int32` Total count of the resource filtered in based on the user given filter.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
## AutomatedBackupPolicyInfo

Automated backup policy signal info

Fields  
---  
`sub_resource` |  `[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResource)` Optional. Sub resource details associated with the signal.  
`is_enabled` |  `bool` Is automated policy enabled.  
  
## BackupDRConfig

BackupDRConfig to capture the backup and disaster recovery details of database resource.

Fields  
---  
`backupdr_managed` |  `bool` Indicates if the resource is managed by BackupDR.  
  
## BackupRunInfo

Metadata about latest backup run state for a database resource.

Fields  
---  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the backup operation started.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the backup operation completed.  
`state` |  `[State](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.BackupRunInfo.State)` Output only. The state of this run.  
`error_message` |  `string` Additional information about the error encountered.  
`operation_error_type` |  `[OperationErrorType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.OperationErrorType)` Optional. OperationErrorType to expose specific error when backup operation of database resource failed, that is state is FAILED.  
`sub_resource` |  `[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResource)` Optional. Sub resource details associated with the backup run.  
  
## State

The status of a backup run.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`SUCCEEDED` | The backup succeeded.  
`FAILED` | The backup was unsuccessful.  
  
## DatabaseResource

DatabaseResource represents every individually configured database unit representing compute and/or storage.

Fields  
---  
`child_resources[]` |  `[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResource)` List of children associated with a database group.  
`full_resource_name` |  `string` The full resource name, based on CAIS resource name format <https://cloud.google.com/asset-inventory/docs/resource-name-format>Example:`//cloudsql.googleapis.com/projects/project-number/instances/mysql-1` `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` `//spanner.googleapis.com/projects/project-number/instances/spanner-instance-1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1/instances/i1`  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
`product` |  `[Product](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Product)` The product this resource represents.  
`location` |  `string` The location of the resources. It supports returning only regional locations in Google Cloud. These are of the form: "us-central1", "us-east1", etc. See <https://cloud.google.com/about/locations> for a list of such regions.  
`labels[]` |  `[Label](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Label)` Labels applied on the resource. The requirements for labels assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/labels-overview#requirements>  
`tags[]` |  `[Tag](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Tag)` Tags applied on the resource. The requirements for tags assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/tags/tags-overview>  
`resource_type` |  `string` The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance  
`sub_resource_type` |  `[SubResourceType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResourceType)` Subtype of the resource specified at creation time.  
`machine_config` |  `[MachineConfig](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MachineConfig)` Machine configuration like CPU, memory, etc for the resource.  
`signal_groups[]` |  `[SignalGroup](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalGroup)` The list of signal groups and count of issues related to the resource. Only those signals which have been requested would be included.  
`metrics` |  `[Metrics](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Metrics)` Observable metrics for the resource e.g. CPU utilization, memory utilization, etc.  
`resource_category` |  `[ResourceCategory](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceCategory)` The category of the resource.  
`resource_name` |  `string` The name of the resource(The last part of the full resource name). Example: For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/mysql-1`, resource name - `mysql-1` For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` , resource name - `postgres-1` Note: In some cases, there might be more than one resource with the same resource name.  
`backupdr_config` |  `[BackupDRConfig](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.BackupDRConfig)` Optional. Backup and disaster recovery details for the resource.  
`edition` |  `[Edition](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Edition)` The edition of the resource.  
`maintenance_info` |  `[MaintenanceInfo](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MaintenanceInfo)` Optional. The maintenance information of the resource.  
  
## DatabaseResourceGroup

DatabaseResourceGroup represents all resources that serve a common data set. It is considered notionally as a single entity, powered by any number of units of compute and storage.

Fields  
---  
`root_resources[]` |  `[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResource)` A database resource that serves as a root of the group of database resources. It is repeated just in case we have the concept of multiple roots in the future, however, it will only be populated with a single value for now.  
`signal_groups[]` |  `[IssueCount](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueCount)` The filtered signal groups and the count of issues associated with the resources that have been filtered in.  
  
## DatabaseResourceIssue

DatabaseResource and Issue associated with it.

Fields  
---  
`signal` |  `[Signal](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Signal)` Signal associated with the issue.  
`resource` |  `[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResource)` Resource associated with the issue.  
  
## DeletionProtectionInfo

Deletion protection signal info for a database resource.

Fields  
---  
`sub_resource` |  `[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResource)` Optional. Sub resource details associated with the signal.  
`deletion_protection_enabled` |  `bool` Is deletion protection enabled.  
  
## DeltaDetails

Captures the details of items that have increased or decreased in some bucket when compared to some point in history. It is currently used to capture the delta of resources that have been added or removed in the fleet as well as to capture the resources that have a change in Issue/Signal status.

Fields  
---  
`increased_resources[]` |  `[ResourceDetails](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceDetails)` Details of resources that have increased.  
`decreased_resources[]` |  `[ResourceDetails](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceDetails)` Details of resources that have decreased.  
  
## Dimension

Dimension used to aggregate the fleet.

Fields  
---  
Union field `dimension`. Followings are the dimensions to be used to aggregate the fleet. `dimension` can be only one of the following:  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
`product_type` |  `[ProductType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ProductType)` Type to identify a product  
`product_engine` |  `[Engine](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Engine)` Engine refers to underlying database binary running in an instance.  
`product_version` |  `string` Version of the underlying database engine  
`location` |  `string` The location of the resources. It supports returning only regional locations in Google Cloud.  
`resource_type` |  `string` The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance  
`sub_resource_type` |  `[SubResourceType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResourceType)` Subtype of the resource specified at creation time.  
`resource_category` |  `[ResourceCategory](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceCategory)` The category of the resource.  
`management_type` |  `[ManagementType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ManagementType)` The management type of the resource.  
`edition` |  `[Edition](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Edition)` The edition of the resource.  
`tag_key` |  `string` Tag key of the resource.  
`tag_value` |  `string` Tag value of the resource.  
`tag_source` |  `string` Tag source of the resource.  
`tag_inherited` |  `bool` Tag inheritance value of the resource.  
`label_key` |  `string` Label key of the resource.  
`label_value` |  `string` Label value of the resource.  
`label_source` |  `string` Label source of the resource.  
`has_maintenance_schedule` |  `bool` Whether the resource has a maintenance schedule.  
`has_deny_maintenance_schedules` |  `bool` Whether the resource has deny maintenance schedules.  
  
## Edition

Represents the edition of a database resource.

Enums  
---  
`EDITION_UNSPECIFIED` | Default, to make it consistent with instance edition enum.  
`EDITION_ENTERPRISE` | Represents the enterprise edition.  
`EDITION_ENTERPRISE_PLUS` | Represents the enterprise plus edition.  
`EDITION_STANDARD` | Represents the standard edition.  
  
## Engine

Engine refers to underlying database binary running in an instance.

Enums  
---  
`ENGINE_UNSPECIFIED` | UNSPECIFIED means engine type is not known or available.  
`ENGINE_MYSQL` | MySQL binary running as an engine in the database instance.  
`ENGINE_POSTGRES` | Postgres binary running as engine in database instance.  
`ENGINE_SQL_SERVER` | SQLServer binary running as engine in database instance.  
`ENGINE_NATIVE` | Native database binary running as engine in instance.  
`ENGINE_MEMORYSTORE_FOR_REDIS` | Memorystore with Redis dialect.  
`ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER` | Memorystore with Redis cluster dialect.  
`ENGINE_FIRESTORE_WITH_NATIVE_MODE` | Firestore with native mode.  
`ENGINE_FIRESTORE_WITH_DATASTORE_MODE` | Firestore with datastore mode.  
`ENGINE_EXADATA_ORACLE` | Oracle Exadata engine.  
`ENGINE_ADB_SERVERLESS_ORACLE` | Oracle Autonomous DB Serverless engine.  
`ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE` | Firestore with MongoDB compatibility.  
`ENGINE_OTHER` | Other refers to rest of other database engine. This is to be when engine is known, but it is not present in this enum.  
  
## InefficientQueryInfo

Metadata about inefficient query signal info for a database resource.

Fields  
---  
`database` |  `string` Name of the database where index is required. For example, "db1", which is the name of the database present in the instance.  
`table` |  `string` Name of the table where index is required  
`sql_index_statement` |  `string` SQL statement of the index. Based on the ddl type, this will be either CREATE INDEX or DROP INDEX.  
`storage_cost_bytes` |  `int64` Cost of additional disk usage in bytes  
`impacted_queries_count` |  `int64` Count of queries to be impacted if index is applied  
  
## IssueCount

Count of issues for a group of signals.

Fields  
---  
`display_name` |  `string` Title of a signal group corresponding to the request.  
`issue_count` |  `int32` The count of the number of issues associated with those resources that are explicitly filtered in by the filters present in the request. A signal is an issue when its SignalStatus field is set to SIGNAL_STATUS_ISSUE.  
  
## IssueGroupStats

IssueGroupStats refers to stats for a particulare combination of relevant health issues of database resources.

Fields  
---  
`display_name` |  `string` Database resource level health card name. This will corresponds to one of the requested input group names.  
`resource_groups_count` |  `int32` Total count of the groups of resources returned by the filter that also have one or more resources for which any of the specified issues are applicable.  
`resources_count` |  `int32` Total count of resources returned by the filter for which any of the specified issues are applicable.  
`healthy_resource_groups_count` |  `int32` The number of resource groups from the total groups as defined above that are healthy with respect to all of the specified issues.  
`healthy_resources_count` |  `int32` The number of resources from the total defined above in field total_resources_count that are healthy with respect to all of the specified issues.  
`issue_stats[]` |  `[IssueStats](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueStats)` List of issues stats containing count of resources having particular issue category.  
  
## IssueSeverity

IssueSeverity represents the severity of an issue.

Enums  
---  
`ISSUE_SEVERITY_UNSPECIFIED` | Unspecified.  
`ISSUE_SEVERITY_LOW` | Low severity.  
`ISSUE_SEVERITY_MEDIUM` | Medium severity.  
`ISSUE_SEVERITY_HIGH` | High severity.  
`ISSUE_SEVERITY_CRITICAL` | Critical severity.  
`ISSUE_SEVERITY_IRRELEVANT` | Irrelevant severity. This means the issue should not be surfaced at all.  
  
## IssueStats

IssueStats holds stats for a particular signal category.

Fields  
---  
`signal_type` |  `[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType)` Type of signal which is an issue.  
`resource_count` |  `int32` Number of resources having issues of a given type.  
`delta_details` |  `[DeltaDetails](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DeltaDetails)` Optional. Delta counts and details of resources for which issue was raised or fixed.  
`issue_severity` |  `[IssueSeverity](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueSeverity)` Severity of the issue.  
  
## Label

Label is a key value pair applied to a resource.

Fields  
---  
`key` |  `string` The key part of the label.  
`value` |  `string` The value part of the label.  
`source` |  `string` The source of the Label. Source is empty if the label is directly attached to the resource and not inherited.  
  
## MachineConfig

MachineConfig describes the configuration of a machine specific to a Database Resource.

Fields  
---  
`memory_size_bytes` |  `int64` Memory size in bytes.  
`shard_count` |  `int32` Optional. The number of Shards (if applicable).  
`vcpu_count` |  `double` Optional. The number of vCPUs (if applicable).  
  
## MaintenanceInfo

MaintenanceInfo to capture the maintenance details of database resource.

Fields  
---  
`maintenance_schedule` |  `[ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceMaintenanceSchedule)` Optional. Maintenance window for the database resource.  
`deny_maintenance_schedules[]` |  `[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceMaintenanceDenySchedule)` Optional. List of Deny maintenance period for the database resource.  
`maintenance_version` |  `string` Output only. Current Maintenance version of the database resource. Example: "MYSQL_8_0_41.R20250531.01_15"  
  
## MaintenanceRecommendationInfo

Info associated with maintenance recommendation.

Fields  
---  
`resource_maintenance_schedules[]` |  `[ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ResourceMaintenanceSchedule)` Optional. List of recommended maintenance schedules for the database resource.  
  
## ManagementType

The management type of the resource.

Enums  
---  
`MANAGEMENT_TYPE_UNSPECIFIED` | Unspecified.  
`MANAGEMENT_TYPE_GCP_MANAGED` | Google-managed resource.  
`MANAGEMENT_TYPE_SELF_MANAGED` | Self-managed resource.  
  
## MetricData

MetricData represents the metric data for a database resource.

Fields  
---  
`value` |  `[TypedValue](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.TypedValue)` The value associated with the metric.  
`observation_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the metric was observed in the metric source service.  
  
## Metrics

Metrics represents the metrics for a database resource.

Fields  
---  
`p99_cpu_utilization` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` P99 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`p95_cpu_utilization` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` P95 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`current_storage_used_bytes` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` Current storage used by the resource in bytes.  
`peak_storage_utilization` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` Peak storage utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`peak_memory_utilization` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` Peak memory utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`peak_number_connections` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` Peak number of connections observed for the resource. The value is a positive integer.  
`node_count` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` Number of nodes in instance for spanner or bigtable.  
`processing_unit_count` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` Number of processing units in spanner.  
`current_memory_used_bytes` |  `[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.MetricData)` Current memory used by the resource in bytes.  
  
## OperationErrorType

OperationErrorType is used to expose specific error type which can happen in database resource while performing an operation. For example, an error can happen while database resource being backed up.

Enums  
---  
`OPERATION_ERROR_TYPE_UNSPECIFIED` | UNSPECIFIED means operation error type is not known or available.  
`KMS_KEY_ERROR` | Key destroyed, expired, not found, unreachable or permission denied.  
`DATABASE_ERROR` | Database is not accessible.  
`STOCKOUT_ERROR` | The zone or region does not have sufficient resources to handle the request at the moment.  
`CANCELLATION_ERROR` | User initiated cancellation.  
`SQLSERVER_ERROR` | SQL server specific error.  
`INTERNAL_ERROR` | Any other internal error.  
  
## OutdatedMinorVersionInfo

Info associated with outdated minor version.

Fields  
---  
`recommended_minor_version` |  `string` Recommended minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
## Phase

Phase/Week of the maintenance window. This is to capture order of maintenance. For example, for Cloud SQL resources - <https://cloud.google.com/sql/docs/mysql/maintenance>. This enum can be extended to support DB Center specific phases for recommendation plan generation.

Enums  
---  
`PHASE_UNSPECIFIED` | Phase is unspecified.  
`PHASE_WEEK1` | Week 1.  
`PHASE_WEEK2` | Week 2.  
`PHASE_WEEK5` | Week 5.  
`PHASE_ANY` | Any phase.  
  
## Product

Product specification for databasecenter resources.

Fields  
---  
`type` |  `[ProductType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.ProductType)` Optional. Type of specific database product. It could be CloudSQL, AlloyDB etc..  
`engine` |  `[Engine](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Engine)` Optional. The specific engine that the underlying database is running.  
`version` |  `string` Optional. Version of the underlying database engine. Example values: For MySQL, it could be "8.0", "5.7" etc. For Postgres, it could be "14", "15" etc.  
`minor_version` |  `string` Optional. Minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
## ProductType

ProductType is used to identify a database service offering either in a cloud provider or on-premise. This enum needs to be updated whenever we introduce a new ProductType.

Enums  
---  
`PRODUCT_TYPE_UNSPECIFIED` | PRODUCT_TYPE_UNSPECIFIED means product type is not known or that the user didn't provide this field in the request.  
`PRODUCT_TYPE_CLOUD_SQL` | Cloud SQL product area in Google Cloud  
`PRODUCT_TYPE_ALLOYDB` | AlloyDB product area in Google Cloud  
`PRODUCT_TYPE_SPANNER` | Spanner product area in Google Cloud  
`PRODUCT_TYPE_BIGTABLE` | Bigtable product area in Google Cloud  
`PRODUCT_TYPE_MEMORYSTORE` | Memorystore product area in Google Cloud  
`PRODUCT_TYPE_FIRESTORE` | Firestore product area in Google Cloud  
`PRODUCT_TYPE_COMPUTE_ENGINE` | Compute Engine self managed databases  
`PRODUCT_TYPE_ORACLE_ON_GCP` | Oracle product area in Google Cloud  
`PRODUCT_TYPE_BIGQUERY` | BigQuery product area in Google Cloud  
`PRODUCT_TYPE_OTHER` | Other refers to rest of other product type. This is to be when product type is known, but it is not present in this enum.  
  
## QueryDatabaseResourceGroupsRequest

QueryDatabaseResourceGroupsRequest is the request to get a list of database groups.

Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `scope`.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. The expression to filter resources.The following fields are filterable: * full_resource_name * resource_type * container * product.type * product.engine * product.version * location * labels * resource_category * machine_config.cpu_count * machine_config.memory_size_bytes * machine_config.shard_count * resource_name * tags * backupdr_config.backupdr_managed * editionThe expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations.Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"` Example: `full_resource_name=~"test"` Example: `full_resource_name=~"test.*master"`  
`signal_type_groups[]` |  `[SignalTypeGroup](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalTypeGroup)` Optional. Groups of signal types that are requested.  
`signal_filters[]` |  `[SignalFilter](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalFilter)` Optional. Filters based on signals. The list will be ORed together and then ANDed with the `filters` field above.  
`order_by` |  `string` Optional. A field that specifies the sort order of the results.The following fields are sortable: * full_resource_name * product.type * product.engine * product.version * container * issue_count * machine_config.vcpu_count * machine_config.memory_size_bytes * machine_config.shard_count * resource_name * issue_severity * signal_type * location * resource_type * instance_type * edition * metrics.p99_cpu_utilization * metrics.p95_cpu_utilization * metrics.current_storage_used_bytes * metrics.node_count * metrics.processing_unit_count * metrics.current_memory_used_bytes * metrics.peak_storage_utilization * metrics.peak_number_connections * metrics.peak_memory_utilizationThe default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It only supports a single field at a time.For example: `order_by = "full_resource_name"` sorts response in ascending order `order_by = "full_resource_name DESC"` sorts response in descending order `order_by = "issue_count DESC"` sorts response in descending order of count of all issues associated with a resource.More explicitly, `order_by = "full_resource_name, product"` is not supported.  
`page_size` |  `int32` Optional. If unspecified, at most 50 resource groups will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `QueryDatabaseResourceGroupsRequest` call. Provide this to retrieve the subsequent page. All parameters except page_token should match the parameters in the call that provided the page page token.  
  
## QueryDatabaseResourceGroupsResponse

QueryDatabaseResourceGroupsResponse represents the response message containing a list of resource groups.

Fields  
---  
`resource_groups[]` |  `[DatabaseResourceGroup](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResourceGroup)` List of database resource groups that pass the filter.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
## QueryIssuesRequest

QueryIssuesRequest is the request to get a list of issues.

Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The list is limited to the one attached to resources within the `scope` that a user has access to.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. Supported fields are: 'product', `location`, `issue_severity`, 'tags', 'labels',  
`signal_products_filters[]` |  `[SignalProductsFilters](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalProductsFilters)` Optional. Filters based on signal and product. The filter list will be ORed across pairs and ANDed within a signal and products pair.  
`order_by` |  `string` Optional. Following fields are sortable: SignalType Product Location IssueSeverityThe default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It only supports a single field at a time.  
`page_size` |  `int32` Optional. If unspecified, at most 50 issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `QueryIssues` call. Provide this to retrieve the subsequent page. All parameters except page size should match the parameters used in the call that provided the page token.  
  
## QueryIssuesResponse

QueryIssuesResponse is the response containing a list of issues.

Fields  
---  
`resource_issues[]` |  `[DatabaseResourceIssue](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.DatabaseResourceIssue)` List of issues and resource details.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
## QueryProductsRequest

QueryProductsRequest is the request to get a list of products.

Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization.The allowed values are:

  * projects/{PROJECT_ID}/locations/{LOCATION} (e.g.,"projects/foo-bar/locations/us-central1")
  * projects/{PROJECT_NUMBER}/locations/{LOCATION} (e.g.,"projects/12345678/locations/us-central1")
  * folders/{FOLDER_NUMBER}/locations/{LOCATION} (e.g.,"folders/1234567/locations/us-central1")
  * organizations/{ORGANIZATION_NUMBER}/locations/{LOCATION} (e.g.,"organizations/123456/locations/us-central1")
  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`page_size` |  `int32` Optional. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListLocations` call. Provide this to retrieve the subsequent page. All other parameters except page size should match the call that provided the page page token.  
  
## QueryProductsResponse

QueryProductsResponse represents the response containing a list of products.

Fields  
---  
`products[]` |  `[Product](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Product)` List of database products returned.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
## RecommendationInfo

Info associated with recommendation.

Fields  
---  
`recommender` |  `string` Name of recommendation. Examples: organizations/1234/locations/us-central1/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations/9876  
`recommender_id` |  `string` ID of recommender. Examples: "google.cloudsql.instance.PerformanceRecommender"  
`recommender_subtype` |  `string` Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender.Examples: For recommender = "google.cloudsql.instance.PerformanceRecommender", recommender_subtype can be "MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE"/"POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION_BEST_PRACTICE"  
  
## RegulatoryStandard

Compliances associated with signals.

Fields  
---  
`standard` |  `string` Name of industry compliance standards, such as such as CIS, PCI, and OWASP.  
`version` |  `string` Version of the standard or benchmark, for example, 1.1.  
  
## ResourceCategory

The enum value corresponds to 'type' suffix in the resource_type field.

Enums  
---  
`RESOURCE_CATEGORY_UNSPECIFIED` | Unspecified.  
`INSTANCE` | A resource that is an Instance.  
`CLUSTER` | A resource that is a Cluster.  
`DATABASE` | A resource that is a Database.  
  
## ResourceDetails

Capture the resource details for resources that are included in the delta counts.

Fields  
---  
`full_resource_name` |  `string` Full resource name of the resource.  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
`product` |  `[Product](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Product)` Product type of the resource.  
`location` |  `string` Location of the resource.  
  
## ResourceMaintenanceDenySchedule

Deny maintenance period for the database resource. It specifies the time range during which the maintenance cannot start. This is configured by the customer.

Fields  
---  
`start_date` |  `[Date](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.type#google.type.Date)` Optional. The start date of the deny maintenance period.  
`end_date` |  `[Date](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.type#google.type.Date)` Optional. Deny period end date.  
`time` |  `[TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.type#google.type.TimeOfDay)` Optional. Time in UTC when the deny period starts on start_date and ends on end_date.  
  
## ResourceMaintenanceSchedule

Maintenance window for the database resource. It specifies preferred time and day of the week and phase in some cases, when the maintenance can start.

Fields  
---  
`start_time` |  `[TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.type#google.type.TimeOfDay)` Optional. Preferred time to start the maintenance operation on the specified day.  
`day` |  `[DayOfWeek](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.type#google.type.DayOfWeek)` Optional. Preferred day of the week for maintenance, e.g. MONDAY, TUESDAY, etc.  
`phase` |  `[Phase](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Phase)` Optional. Phase of the maintenance window. This is to capture order of maintenance. For example, for Cloud SQL resources, this can be used to capture if the maintenance window is in Week1, Week2, Week5, etc. Non production resources are usually part of early phase. For more details, refer to Cloud SQL resources - <https://cloud.google.com/sql/docs/mysql/maintenance>  
  
## ResourceSuspensionInfo

Resource suspension info for a database resource.

Fields  
---  
`resource_suspended` |  `bool` Is resource suspended.  
`suspension_reason` |  `[SuspensionReason](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SuspensionReason)` Suspension reason for the resource.  
  
## RetentionSettingsInfo

Metadata about backup retention settings for a database resource.

Fields  
---  
`sub_resource` |  `[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SubResource)` Optional. Sub resource details associated with the backup configuration.  
Union field `retention`. Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is 'COUNT', we will retain this many backups. `retention` can be only one of the following:  
`quantity_based_retention` |  `[Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32-value)` Number of backups that will be retained.  
`duration_based_retention` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Duration based retention period i.e. 172800 seconds (2 days)  
`timestamp_based_retention_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp based retention period i.e. till 2024-05-01T00:00:00Z  
  
## SCCInfo

Info associated with SCC signals.

Fields  
---  
`signal` |  `string` Name of the signal.  
`category` |  `string` Name by which SCC calls this signal.  
`regulatory_standards[]` |  `[RegulatoryStandard](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.RegulatoryStandard)` Compliances that are associated with the signal.  
`external_uri` |  `string` External URI which points to a SCC page associated with the signal.  
  
## Signal

Represents a signal.

Fields  
---  
`signal_type` |  `[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType)` Type of the signal.  
`signal_status` |  `[SignalStatus](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalStatus)` Status of the signal.  
`additional_details[]` |  `[AdditionalDetail](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.AdditionalDetail)` Additional information related to the signal. In the case of composite signals, this field encapsulates details associated with granular signals, having a signal status of "ISSUE"; signals with a status of "OK" are not included. For granular signals, it encompasses information relevant to the signal, regardless of the signal status.  
`issue_severity` |  `[IssueSeverity](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.IssueSeverity)` Severity of the issue.  
`issue_create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp when the issue was created (when signal status is ISSUE).  
  
## SignalFilter

A filter for Signals.

If signal_type is left unset, all signals should be returned. For example, the following filter returns all issues. signal_filter: { signal_status: SIGNAL_STATUS_ISSUE; }

Another example, the following filter returns issues of the given type: signal_filter: { type: SIGNAL_TYPE_NO_PROMOTABLE_REPLICA signal_status: ISSUE }

If signal_status is left unset or set to SIGNAL_STATE_UNSPECIFIED, an error should be returned.

Fields  
---  
`signal_type` |  `[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType)` Optional. Represents the type of the Signal for which the filter is for.  
`signal_status` |  `[SignalStatus](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalStatus)` Optional. Represents the status of the Signal for which the filter is for.  
  
## SignalGroup

A group of signals and their counts.

Fields  
---  
`display_name` |  `string` Title of a signal group corresponding to the request.  
`issue_count` |  `int32` When applied to a DatabaseResource represents count of issues associated with the resource. A signal is an issue when its SignalStatus field is set to SIGNAL_STATUS_ISSUE.  
`signals[]` |  `[Signal](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Signal)` List of signals present in the group and associated with the resource.Only applies to a DatabaseResource.  
  
## SignalProductsFilters

SignalProductsFilters represents a signal and list of supported products.

Fields  
---  
`signal_type` |  `[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType)` Optional. The type of signal.  
`products[]` |  `[Product](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Product)` Optional. Product type of the resource. The version of the product will be ignored in filtering.  
  
## SignalSource

Represents the source system from where a signal comes from. More enum values are expected to be added as needed.

Enums  
---  
`SIGNAL_SOURCE_UNSPECIFIED` | Unspecified.  
`SIGNAL_SOURCE_RESOURCE_METADATA` | Signal comes from resource metadata.  
`SIGNAL_SOURCE_SECURITY_FINDINGS` | Signal comes from SCC findings.  
`SIGNAL_SOURCE_RECOMMENDER` | Signal comes from recommender hub.  
`SIGNAL_SOURCE_MODERN_OBSERVABILITY` | Signal comes from modern observability platform.  
  
## SignalStatus

Represents the state of a signal. More enum values are expected to be added as needed.

Enums  
---  
`SIGNAL_STATUS_UNSPECIFIED` | Unspecified.  
`SIGNAL_STATUS_NOT_APPLICABLE` | Signal is not applicable to the resource.  
`SIGNAL_STATUS_OK` | Signal is not an issue.  
`SIGNAL_STATUS_ISSUE` | Signal is an issue.  
`SIGNAL_STATUS_NOT_ENABLED` | Signal is not enabled for the resource.  
  
## SignalType

Represents the type of a signal. More values are expected to be added as needed.

Enums  
---  
`SIGNAL_TYPE_UNSPECIFIED` | Unspecified.  
`SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED` | Represents if a resource is protected by automatic failover. Checks for resources that are configured to have redundancy within a region that enables automatic failover.  
`SIGNAL_TYPE_GROUP_MULTIREGIONAL` | Represents if a group is replicating across regions. Checks for resources that are configured to have redundancy, and ongoing replication, across regions.  
`SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY` | Represents if a resource has an automated backup policy.  
`SIGNAL_TYPE_SHORT_BACKUP_RETENTION` | Represents if a resources has a short backup retention period.  
`SIGNAL_TYPE_LAST_BACKUP_FAILED` | Represents if the last backup of a resource failed.  
`SIGNAL_TYPE_LAST_BACKUP_OLD` | Represents if the last backup of a resource is older than some threshold value.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0` | Represents if a resource violates CIS Google Cloud Platform Foundation 2.0.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.3.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.2.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.1.  
`SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0` | Represents if a resource violates CIS Google Cloud Platform Foundation 1.0.  
`SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0` | Represents if a resource violates CIS Controls 8.0.  
`SIGNAL_TYPE_VIOLATES_NIST_800_53` | Represents if a resource violates NIST 800-53.  
`SIGNAL_TYPE_VIOLATES_NIST_800_53_R5` | Represents if a resource violates NIST 800-53 R5.  
`SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0` | Represents if a resource violates NIST Cybersecurity Framework 1.0.  
`SIGNAL_TYPE_VIOLATES_ISO_27001` | Represents if a resource violates ISO-27001.  
`SIGNAL_TYPE_VIOLATES_ISO_27001_V2022` | Represents if a resource violates ISO 27001 2022.  
`SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1` | Represents if a resource violates PCI-DSS v3.2.1.  
`SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0` | Represents if a resource violates PCI-DSS v4.0.  
`SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4` | Represents if a resource violates Cloud Controls Matrix v4.0.  
`SIGNAL_TYPE_VIOLATES_HIPAA` | Represents if a resource violates HIPAA.  
`SIGNAL_TYPE_VIOLATES_SOC2_V2017` | Represents if a resource violates SOC2 v2017.  
`SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING` | Represents if log_checkpoints database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED` | Represents if the log_duration database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_VERBOSE_ERROR_LOGGING` | Represents if the log_error_verbosity database flag for a Cloud SQL for PostgreSQL instance is not set to default or stricter (default or terse).  
`SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED` | Represents if the log_lock_waits database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_LOGGING_MOST_ERRORS` | Represents if the log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance is not set appropriately.  
`SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS` | Represents if the log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance does not have an appropriate severity level.  
`SIGNAL_TYPE_MINIMAL_ERROR_LOGGING` | Represents if the log_min_messages database flag for a Cloud SQL for PostgreSQL instance is not set to warning or another recommended value.  
`SIGNAL_TYPE_QUERY_STATS_LOGGED` | Represents if the databaseFlags property of instance metadata for the log_executor_status field is set to on.  
`SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME` | Represents if the log_hostname database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS` | Represents if the log_parser_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS` | Represents if the log_planner_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS` | Represents if the log_statement database flag for a Cloud SQL for PostgreSQL instance is not set to DDL (all data definition statements).  
`SIGNAL_TYPE_LOGGING_QUERY_STATS` | Represents if the log_statement_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.  
`SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES` | Represents if the log_temp_files database flag for a Cloud SQL for PostgreSQL instance is not set to "0". (NOTE: 0 = ON)  
`SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED` | Represents if the user connections database flag for a Cloud SQL for SQL Server instance is configured.  
`SIGNAL_TYPE_USER_OPTIONS_CONFIGURED` | Represents if the user options database flag for Cloud SQL SQL Server instance is configured or not.  
`SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS` | Represents if a resource is exposed to public access.  
`SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS` | Represents if a resources requires all incoming connections to use SSL or not.  
`SIGNAL_TYPE_NO_ROOT_PASSWORD` | Represents if a Cloud SQL database has a password configured for the root account or not.  
`SIGNAL_TYPE_WEAK_ROOT_PASSWORD` | Represents if a Cloud SQL database has a weak password configured for the root account.  
`SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED` | Represents if a SQL database instance is not encrypted with customer-managed encryption keys (CMEK).  
`SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED` | Represents if The contained database authentication database flag for a Cloud SQL for SQL Server instance is not set to off.  
`SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS` | Represents if he external scripts enabled database flag for a Cloud SQL for SQL Server instance is not set to off.  
`SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS` | Represents if the local_infile database flag for a Cloud SQL for MySQL instance is not set to off.  
`SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED` | Represents if the log_connections database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED` | Represents if the log_disconnections database flag for a Cloud SQL for PostgreSQL instance is not set to on.  
`SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO` | Represents if the log_min_duration_statement database flag for a Cloud SQL for PostgreSQL instance is not set to -1.  
`SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS` | Represents if the remote access database flag for a Cloud SQL for SQL Server instance is not set to off.  
`SIGNAL_TYPE_DATABASE_NAMES_EXPOSED` | Represents if the skip_show_database database flag for a Cloud SQL for MySQL instance is not set to on.  
`SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED` | Represents if the 3625 (trace flag) database flag for a Cloud SQL for SQL Server instance is not set to on.  
`SIGNAL_TYPE_PUBLIC_IP_ENABLED` | Represents if public IP is enabled.  
`SIGNAL_TYPE_IDLE` | Represents idle instance helps to reduce costs.  
`SIGNAL_TYPE_OVERPROVISIONED` | Represents instances that are unnecessarily large for given workload.  
`SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES` | Represents high number of concurrently opened tables.  
`SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES` | Represents high table count close to SLA limit.  
`SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION` | Represents high number of unvacuumed transactions  
`SIGNAL_TYPE_UNDERPROVISIONED` | Represents need for more CPU and/or memory  
`SIGNAL_TYPE_OUT_OF_DISK` | Represents out of disk.  
`SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY` | Represents server certificate is near expiry.  
`SIGNAL_TYPE_DATABASE_AUDITING_DISABLED` | Represents database auditing is disabled.  
`SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS` | Represents not restricted to authorized networks.  
`SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP` | Represents violate org policy restrict public ip.  
`SIGNAL_TYPE_QUOTA_LIMIT` | Cluster nearing quota limit  
`SIGNAL_TYPE_NO_PASSWORD_POLICY` | No password policy set on resources  
`SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT` | Performance impact of connections settings  
`SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT` | Performance impact of temporary tables settings  
`SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT` | Performance impact of transaction logs settings  
`SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES` | Performance impact of high joins without indexes  
`SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES` | Detects events where a database superuser (postgres for PostgreSQL servers or root for MySQL users) writes to non-system tables.  
`SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS` | Detects events where a database user or role has been granted all privileges to a database, or to all tables, procedures, or functions in a schema.  
`SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET` | Detects if database instance data exported to a Cloud Storage bucket outside of the organization.  
`SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET` | Detects if database instance data exported to a Cloud Storage bucket that is owned by the organization and is publicly accessible.  
`SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM` | Detects if a database instance is using a weak password hash algorithm.  
`SIGNAL_TYPE_NO_USER_PASSWORD_POLICY` | Detects if a database instance has no user password policy set.  
`SIGNAL_TYPE_HOT_NODE` | Detects if a database instance/cluster has a hot node.  
`SIGNAL_TYPE_NO_DELETION_PROTECTION` | Deletion Protection Disabled for the resource  
`SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY` | Detects if a database instance has no point in time recovery enabled.  
`SIGNAL_TYPE_RESOURCE_SUSPENDED` | Detects if a database instance/cluster has suspended resources.  
`SIGNAL_TYPE_EXPENSIVE_COMMANDS` | Detects that expensive commands are being run on a database instance impacting overall performance.  
`SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED` | Indicates that the instance does not have a maintenance policy configured.  
`SIGNAL_TYPE_INEFFICIENT_QUERY` | Indicates that the instance has inefficient queries detected.  
`SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD` | Indicates that the instance has read intensive workload.  
`SIGNAL_TYPE_MEMORY_LIMIT` | Indicates that the instance is nearing memory limit.  
`SIGNAL_TYPE_MAX_SERVER_MEMORY` | Indicates that the instance's max server memory is configured higher than the recommended value.  
`SIGNAL_TYPE_LARGE_ROWS` | Indicates that the database has large rows beyond the recommended limit.  
`SIGNAL_TYPE_HIGH_WRITE_PRESSURE` | Heavy write pressure on the database rows.  
`SIGNAL_TYPE_HIGH_READ_PRESSURE` | Heavy read pressure on the database rows.  
`SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED` | Encryption org policy not satisfied.  
`SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED` | Location org policy not satisfied.  
`SIGNAL_TYPE_OUTDATED_MINOR_VERSION` | Outdated DB minor version.  
`SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED` | Schema not optimized.  
`SIGNAL_TYPE_REPLICATION_LAG` | Replication delay.  
`SIGNAL_TYPE_OUTDATED_CLIENT` | Outdated client.  
`SIGNAL_TYPE_DATABOOST_DISABLED` | Databoost is disabled.  
`SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES` | Recommended maintenance policy.  
`SIGNAL_TYPE_EXTENDED_SUPPORT` | Resource version is in extended support.  
`SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE` | Represents a database version nearing end of life.  
  
## SignalTypeGroup

A group of signal types that specifies what the user is interested in.

Used by QueryDatabaseResourceGroups API.

Example:

signal_type_group { name = "AVAILABILITY" types = [SIGNAL_TYPE_NO_PROMOTABLE_REPLICA] }

Fields  
---  
`display_name` |  `string` Required. The display name of a signal group.  
`signal_types[]` |  `[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.SignalType)` Optional. List of signal types present in the group.  
  
## SubResource

Sub resource details For Spanner/Bigtable instance certain data protection settings are at sub resource level like database/table. This message is used to capture such sub resource details.

Fields  
---  
`resource_type` |  `string` Optional. Resource type associated with the sub resource where backup settings are configured. E.g. "spanner.googleapis.com/Database" for Spanner where backup retention is configured on database within an instance OPTIONAL  
`full_resource_name` |  `string` Optional. Resource name associated with the sub resource where backup settings are configured. E.g."//spanner.googleapis.com/projects/project1/instances/inst1/databases/db1" for Spanner where backup retention is configured on database within an instance OPTIONAL  
`product` |  `[Product](https://docs.cloud.google.com/database-center/docs/reference/rpc/google.cloud.databasecenter.v1beta#google.cloud.databasecenter.v1beta.Product)` Optional. Product information associated with the sub resource where backup retention settings are configured. e.g.
    
    
    product: {
     type   : PRODUCT_TYPE_SPANNER
     engine : ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT
    }
    

for Spanner where backup is configured on database within an instance OPTIONAL  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
  
## SubResourceType

SubResourceType refers to the sub-type of database resource.

Enums  
---  
`SUB_RESOURCE_TYPE_UNSPECIFIED` | Unspecified.  
`SUB_RESOURCE_TYPE_PRIMARY` | A resource acting as a primary.  
`SUB_RESOURCE_TYPE_SECONDARY` | A resource acting as a secondary.  
`SUB_RESOURCE_TYPE_READ_REPLICA` | A resource acting as a read-replica.  
`SUB_RESOURCE_TYPE_EXTERNAL_PRIMARY` | A resource acting as an external primary.  
`SUB_RESOURCE_TYPE_READ_POOL` | A resource acting as a read pool.  
`SUB_RESOURCE_TYPE_RESERVATION` | Represents a reservation resource.  
`SUB_RESOURCE_TYPE_DATASET` | Represents a dataset resource.  
`SUB_RESOURCE_TYPE_OTHER` | For the rest of the categories.  
  
## SuspensionReason

The reason for suspension of the database resource.

Enums  
---  
`SUSPENSION_REASON_UNSPECIFIED` | Suspension reason is unspecified.  
`WIPEOUT_HIDE_EVENT` | Wipeout hide event.  
`WIPEOUT_PURGE_EVENT` | Wipeout purge event.  
`BILLING_DISABLED` | Billing disabled for project  
`ABUSER_DETECTED` | Abuse detected for resource  
`ENCRYPTION_KEY_INACCESSIBLE` | Encryption key inaccessible.  
`REPLICATED_CLUSTER_ENCRYPTION_KEY_INACCESSIBLE` | Replicated cluster encryption key inaccessible.  
  
## Tag

Tag is a key value pair attached to a resource.

Fields  
---  
`key` |  `string`  
`value` |  `string` The value part of the tag.  
`source` |  `string` The source of the tag. According to <https://cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels>, tags can be created only at the project or organization level. Tags can be inherited from different project as well not just the current project where the database resource is present. Format: "projects/{PROJECT_ID}", "projects/{PROJECT_NUMBER}", "organizations/{ORGANIZATION_ID}"  
`inherited` |  `bool` Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource.  
  
## TypedValue

TypedValue represents the value of the metric based on data type.

Fields  
---  
Union field `value`. The data type of metric value would be chosen based on the metric type. `value` can be only one of the following:  
`double_value` |  `double` The value of the metric as double.  
`int64_value` |  `int64` The value of the metric as int.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
