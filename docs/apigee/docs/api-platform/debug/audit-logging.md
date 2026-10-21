---
url: https://docs.cloud.google.com/apigee/docs/api-platform/debug/audit-logging/
title: Apigee audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:45:40.290995+00:00
---

# Apigee audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/debug/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Apigee. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Apigee audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="apigee.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Apigee generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.apigee.v1.AnalyticsCustomReport.GetCustomReport`  
`google.cloud.apigee.v1.AnalyticsCustomReport.ListCustomReports`  
`google.cloud.apigee.v1.AnalyticsDatastore.GetDatastore`  
`google.cloud.apigee.v1.AnalyticsDatastore.ListDatastores`  
`google.cloud.apigee.v1.AnalyticsSchema.GetSchema`  
`google.cloud.apigee.v1.ApiCategories.GetApiCategory`  
`google.cloud.apigee.v1.ApiCategories.ListApiCategories`  
`google.cloud.apigee.v1.ApiDocs.GetApiDoc`  
`google.cloud.apigee.v1.ApiDocs.GetApiDocDocumentation`  
`google.cloud.apigee.v1.ApiDocs.ListApiDocs`  
`google.cloud.apigee.v1.ApiDocs.ListPublishableProducts`  
`google.cloud.apigee.v1.ApiProducts.GetApiProduct`  
`google.cloud.apigee.v1.ApiProducts.GetApiProductAttribute`  
`google.cloud.apigee.v1.ApiProducts.ListApiProductAttributes`  
`google.cloud.apigee.v1.ApiProducts.ListApiProducts`  
`google.cloud.apigee.v1.ApiProxyService.GetApiProxy`  
`google.cloud.apigee.v1.ApiProxyService.GetApiProxyRevision`  
`google.cloud.apigee.v1.ApiProxyService.ListApiProxies`  
`google.cloud.apigee.v1.ApiProxyService.ListApiProxyRevisions`  
`google.cloud.apigee.v1.ApimServiceExtensionService.GetApimServiceExtension`  
`google.cloud.apigee.v1.ApimServiceExtensionService.ListApimServiceExtensions`  
`google.cloud.apigee.v1.AppGroupAppKeys.GetAppGroupAppKey`  
`google.cloud.apigee.v1.AppGroupApps.GetAppGroupApp`  
`google.cloud.apigee.v1.AppGroupApps.ListAppGroupApps`  
`google.cloud.apigee.v1.AppGroupSubscriptions.GetAppGroupSubscription`  
`google.cloud.apigee.v1.AppGroupSubscriptions.ListAppGroupSubscriptions`  
`google.cloud.apigee.v1.AppGroups.GetAppGroup`  
`google.cloud.apigee.v1.AppGroups.GetAppGroupBalance`  
`google.cloud.apigee.v1.AppGroups.GetAppGroupMonetizationConfig`  
`google.cloud.apigee.v1.AppGroups.ListAppGroups`  
`google.cloud.apigee.v1.Apps.GetApp`  
`google.cloud.apigee.v1.Apps.ListApps`  
`google.cloud.apigee.v1.ArchiveDeploymentService.GenerateDownloadUrl`  
`google.cloud.apigee.v1.ArchiveDeploymentService.GetArchiveDeployment`  
`google.cloud.apigee.v1.ArchiveDeploymentService.ListArchiveDeployments`  
`google.cloud.apigee.v1.AsyncQueryService.GetAsyncQuery`  
`google.cloud.apigee.v1.AsyncQueryService.GetAsyncQueryResult`  
`google.cloud.apigee.v1.AsyncQueryService.GetAsyncQueryResultView`  
`google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQuery`  
`google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQueryResult`  
`google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQueryResultView`  
`google.cloud.apigee.v1.AsyncQueryService.ListAsyncQueries`  
`google.cloud.apigee.v1.AsyncQueryService.ListHostAsyncQueries`  
`google.cloud.apigee.v1.CacheService.ListCaches`  
`google.cloud.apigee.v1.CollectionService.GetOrganizationDataLocation`  
`google.cloud.apigee.v1.Consumer.GetConsumerAudience`  
`google.cloud.apigee.v1.Consumer.GetConsumerTeam`  
`google.cloud.apigee.v1.Consumer.GetConsumerUser`  
`google.cloud.apigee.v1.Consumer.ListConsumerAudiences`  
`google.cloud.apigee.v1.Consumer.ListConsumerTeams`  
`google.cloud.apigee.v1.Consumer.ListConsumerUsers`  
`google.cloud.apigee.v1.Customcss.GetCustomCss`  
`google.cloud.apigee.v1.Customcss.GetEditorSchema`  
`google.cloud.apigee.v1.DataCollectorService.GetDataCollector`  
`google.cloud.apigee.v1.DataCollectorService.ListDataCollectors`  
`google.cloud.apigee.v1.DataExport.GetExport`  
`google.cloud.apigee.v1.DataExport.ListExports`  
`google.cloud.apigee.v1.DeploymentService.GetApiDeployment`  
`google.cloud.apigee.v1.DeploymentService.GetEnvironmentDeployment`  
`google.cloud.apigee.v1.DeploymentService.GetFlowHook`  
`google.cloud.apigee.v1.DeploymentService.GetIamPolicy`  
`google.cloud.apigee.v1.DeploymentService.GetSharedFlowDeployment`  
`google.cloud.apigee.v1.DeploymentService.ListApiDeployments`  
`google.cloud.apigee.v1.DeploymentService.ListApiDeploymentsInEnvironment`  
`google.cloud.apigee.v1.DeploymentService.ListApiRevisionDeployments`  
`google.cloud.apigee.v1.DeploymentService.ListEnvironmentDeployments`  
`google.cloud.apigee.v1.DeploymentService.ListFlowHooks`  
`google.cloud.apigee.v1.DeploymentService.ListOrganizationDeployments`  
`google.cloud.apigee.v1.DeploymentService.ListSharedFlowDeployments`  
`google.cloud.apigee.v1.DeploymentService.ListSharedFlowDeploymentsInEnvironment`  
`google.cloud.apigee.v1.DeploymentService.ListSharedFlowRevisionDeployments`  
`google.cloud.apigee.v1.DeveloperAppKeys.GetDeveloperAppKey`  
`google.cloud.apigee.v1.DeveloperApps.GetDeveloperApp`  
`google.cloud.apigee.v1.DeveloperApps.GetDeveloperAppAttribute`  
`google.cloud.apigee.v1.DeveloperApps.ListDeveloperAppAttributes`  
`google.cloud.apigee.v1.DeveloperApps.ListDeveloperApps`  
`google.cloud.apigee.v1.DeveloperSubscriptions.GetDeveloperSubscription`  
`google.cloud.apigee.v1.DeveloperSubscriptions.ListDeveloperSubscriptions`  
`google.cloud.apigee.v1.Developers.GetDeveloper`  
`google.cloud.apigee.v1.Developers.GetDeveloperAttribute`  
`google.cloud.apigee.v1.Developers.GetDeveloperBalance`  
`google.cloud.apigee.v1.Developers.GetDeveloperMonetizationConfig`  
`google.cloud.apigee.v1.Developers.ListDeveloperAttributes`  
`google.cloud.apigee.v1.Developers.ListDevelopers`  
`google.cloud.apigee.v1.DnsZoneService.GetDnsZone`  
`google.cloud.apigee.v1.DnsZoneService.ListDnsZones`  
`google.cloud.apigee.v1.EndpointAttachmentService.GetEndpointAttachment`  
`google.cloud.apigee.v1.EndpointAttachmentService.ListEndpointAttachments`  
`google.cloud.apigee.v1.EnvironmentAddons.GetAddonsConfig`  
`google.cloud.apigee.v1.EnvironmentGroupAttachmentService.GetEnvironmentGroupAttachment`  
`google.cloud.apigee.v1.EnvironmentGroupAttachmentService.ListEnvironmentGroupAttachments`  
`google.cloud.apigee.v1.EnvironmentGroupService.GetEnvironmentGroup`  
`google.cloud.apigee.v1.EnvironmentGroupService.ListEnvironmentGroups`  
`google.cloud.apigee.v1.EnvironmentService.GetApiSecurityRuntimeConfig`  
`google.cloud.apigee.v1.EnvironmentService.GetDeployedConfig`  
`google.cloud.apigee.v1.EnvironmentService.GetEnvironment`  
`google.cloud.apigee.v1.EnvironmentService.GetIamPolicy`  
`google.cloud.apigee.v1.EnvironmentService.ListEnvironments`  
`google.cloud.apigee.v1.InstanceAttachmentService.GetInstanceAttachment`  
`google.cloud.apigee.v1.InstanceAttachmentService.ListInstanceAttachments`  
`google.cloud.apigee.v1.InstanceService.GetInstance`  
`google.cloud.apigee.v1.InstanceService.ListInstances`  
`google.cloud.apigee.v1.KeyValueMapService.GetKeyValueEntry`  
`google.cloud.apigee.v1.KeyValueMapService.GetKeyValueMap`  
`google.cloud.apigee.v1.KeyValueMapService.ListApiProxyKeyValueMaps`  
`google.cloud.apigee.v1.KeyValueMapService.ListEnvironmentKeyValueMaps`  
`google.cloud.apigee.v1.KeyValueMapService.ListKeyValueEntries`  
`google.cloud.apigee.v1.KeyValueMapService.ListOrganizationKeyValueMaps`  
`google.cloud.apigee.v1.KeystoreService.GetKeystore`  
`google.cloud.apigee.v1.KeystoreService.ListKeystores`  
`google.cloud.apigee.v1.MenuItems.ListMenuItems`  
`google.cloud.apigee.v1.MenuTypes.ListMenuTypes`  
`google.cloud.apigee.v1.MenuTypes.ListMenuTypesByPage`  
`google.cloud.apigee.v1.NatAddressService.GetNatAddress`  
`google.cloud.apigee.v1.NatAddressService.ListNatAddresses`  
`google.cloud.apigee.v1.OrganizationService.GetControlPlaneAccess`  
`google.cloud.apigee.v1.OrganizationService.GetOrganization`  
`google.cloud.apigee.v1.OrganizationService.GetProjectMapping`  
`google.cloud.apigee.v1.OrganizationService.GetSyncAuthorization`  
`google.cloud.apigee.v1.Pages.GetPage`  
`google.cloud.apigee.v1.Pages.ListPages`  
`google.cloud.apigee.v1.RatePlans.GetRatePlan`  
`google.cloud.apigee.v1.RatePlans.ListRatePlans`  
`google.cloud.apigee.v1.ReferenceService.GetReference`  
`google.cloud.apigee.v1.ReferenceService.ListReferences`  
`google.cloud.apigee.v1.ResourceEntitlements.GetDefaultResourceEntitlements`  
`google.cloud.apigee.v1.ResourceEntitlements.GetResourceEntitlement`  
`google.cloud.apigee.v1.ResourceFileService.GetEnvironmentResource`  
`google.cloud.apigee.v1.ResourceFileService.ListEnvironmentResources`  
`google.cloud.apigee.v1.Resources.GetConsumerResourceTypes`  
`google.cloud.apigee.v1.Resources.QueryApiDocs`  
`google.cloud.apigee.v1.Resources.QueryPages`  
`google.cloud.apigee.v1.RuntimeService.GetCanaryEvaluation`  
`google.cloud.apigee.v1.RuntimeService.GetDeployedIngressConfig`  
`google.cloud.apigee.v1.RuntimeService.GetEnvGroupDeployedIngressConfig`  
`google.cloud.apigee.v1.RuntimeService.GetMcpServerConfig`  
`google.cloud.apigee.v1.RuntimeService.GetRuntimeConfig`  
`google.cloud.apigee.v1.SecurityActionService.GetSecurityAction`  
`google.cloud.apigee.v1.SecurityActionService.GetSecurityActionsConfig`  
`google.cloud.apigee.v1.SecurityActionService.ListSecurityActions`  
`google.cloud.apigee.v1.SecurityFeedbackService.GetSecurityFeedback`  
`google.cloud.apigee.v1.SecurityFeedbackService.ListSecurityFeedback`  
`google.cloud.apigee.v1.SecurityIncidentService.GetSecurityIncident`  
`google.cloud.apigee.v1.SecurityIncidentService.ListSecurityIncidents`  
`google.cloud.apigee.v1.SecurityProfileService.ComputeEnvironmentScores`  
`google.cloud.apigee.v1.SecurityProfileService.GetSecurityProfile`  
`google.cloud.apigee.v1.SecurityProfileService.ListSecurityProfileRevisions`  
`google.cloud.apigee.v1.SecurityProfileService.ListSecurityProfiles`  
`google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReport`  
`google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReportResult`  
`google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReportResultView`  
`google.cloud.apigee.v1.SecurityReportService.GetSecurityReport`  
`google.cloud.apigee.v1.SecurityReportService.GetSecurityReportResult`  
`google.cloud.apigee.v1.SecurityReportService.GetSecurityReportResultView`  
`google.cloud.apigee.v1.SecurityReportService.ListHostSecurityReports`  
`google.cloud.apigee.v1.SecurityReportService.ListSecurityReports`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.BatchComputeSecurityAssessmentResults`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.GetSecurityMonitoringCondition`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.GetSecurityProfileV2`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.ListSecurityMonitoringConditions`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.ListSecurityProfilesV2`  
`google.cloud.apigee.v1.SecuritySettingsService.GetSecuritySettings`  
`google.cloud.apigee.v1.SecurityStatsService.QueryTabularStats`  
`google.cloud.apigee.v1.SecurityStatsService.QueryTimeSeriesStats`  
`google.cloud.apigee.v1.SharedFlowService.GetSharedFlow`  
`google.cloud.apigee.v1.SharedFlowService.GetSharedFlowRevision`  
`google.cloud.apigee.v1.SharedFlowService.ListSharedFlowRevisions`  
`google.cloud.apigee.v1.SharedFlowService.ListSharedFlows`  
`google.cloud.apigee.v1.SiteDomain.GetCustomDomainConfig`  
`google.cloud.apigee.v1.SiteEmail.GetEmailTemplate`  
`google.cloud.apigee.v1.SiteFile.ListFiles`  
`google.cloud.apigee.v1.SiteOperation.GetContentSecurityPolicy`  
`google.cloud.apigee.v1.SiteOperation.GetDefaultAnonAllowed`  
`google.cloud.apigee.v1.SiteOperation.GetDraftToken`  
`google.cloud.apigee.v1.SiteOperation.GetOrgType`  
`google.cloud.apigee.v1.Sites.GetAllInOrgOrSingleWithDomain`  
`google.cloud.apigee.v1.Sites.GetKeystores`  
`google.cloud.apigee.v1.Sites.GetPublishedApis`  
`google.cloud.apigee.v1.Sites.GetSite`  
`google.cloud.apigee.v1.Sites.GetSmtp`  
`google.cloud.apigee.v1.Sites.ListProxySpecs`  
`google.cloud.apigee.v1.Sites.Render`  
`google.cloud.apigee.v1.SpaceService.GetIamPolicy`  
`google.cloud.apigee.v1.SpaceService.GetSpace`  
`google.cloud.apigee.v1.SpaceService.ListSpaces`  
`google.cloud.apigee.v1.System.GetAnnouncement`  
`google.cloud.apigee.v1.System.GetConfig`  
`google.cloud.apigee.v1.System.GetServerStatus`  
`google.cloud.apigee.v1.System.GetSystemState`  
`google.cloud.apigee.v1.TargetServerService.GetTargetServer`  
`google.cloud.apigee.v1.TargetServerService.ListTargetServers`  
`google.cloud.apigee.v1.TraceConfigOverrideService.GetTraceConfigOverride`  
`google.cloud.apigee.v1.TraceConfigOverrideService.ListTraceConfigOverrides`  
`google.cloud.apigee.v1.TraceConfigService.GetTraceConfig`  
`google.cloud.apigee.v1.Zones.GetAudiencesEnabled`  
`google.cloud.apigee.v1.Zones.GetIdentityProvider`  
`google.cloud.apigee.v1.Zones.GetZone`  
`google.cloud.apigee.v1.Zones.GetZoneAudiencesEnabledForZone`  
`google.cloud.apigee.v1.Zones.ListAudiencesEnabledForZonesInOrg`  
`google.cloud.apigee.v1.Zones.ListIdentityProviders`  
`google.cloud.apigee.v1.Zones.ListZones`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.apigee.v1.AnalyticsCustomReport.CreateCustomReport`  
`google.cloud.apigee.v1.AnalyticsCustomReport.DeleteCustomReport`  
`google.cloud.apigee.v1.AnalyticsCustomReport.UpdateCustomReport`  
`google.cloud.apigee.v1.AnalyticsDatastore.CreateDatastore`  
`google.cloud.apigee.v1.AnalyticsDatastore.DeleteDatastore`  
`google.cloud.apigee.v1.AnalyticsDatastore.TestDatastore`  
`google.cloud.apigee.v1.AnalyticsDatastore.UpdateDatastore`  
`google.cloud.apigee.v1.ApiCategories.CreateApiCategory`  
`google.cloud.apigee.v1.ApiCategories.DeleteApiCategory`  
`google.cloud.apigee.v1.ApiCategories.UpdateApiCategory`  
`google.cloud.apigee.v1.ApiDocs.CreateApiDoc`  
`google.cloud.apigee.v1.ApiDocs.DeleteApiDoc`  
`google.cloud.apigee.v1.ApiDocs.DeleteSnapshot`  
`google.cloud.apigee.v1.ApiDocs.PostSnapshot`  
`google.cloud.apigee.v1.ApiDocs.TagApiDocs`  
`google.cloud.apigee.v1.ApiDocs.UpdateApiDoc`  
`google.cloud.apigee.v1.ApiDocs.UpdateApiDocDocumentation`  
`google.cloud.apigee.v1.ApiProducts.CreateApiProduct`  
`google.cloud.apigee.v1.ApiProducts.DeleteApiProduct`  
`google.cloud.apigee.v1.ApiProducts.DeleteApiProductAttribute`  
`google.cloud.apigee.v1.ApiProducts.MoveApiProduct`  
`google.cloud.apigee.v1.ApiProducts.UpdateApiProduct`  
`google.cloud.apigee.v1.ApiProducts.UpdateApiProductAttribute`  
`google.cloud.apigee.v1.ApiProducts.UpdateApiProductAttributes`  
`google.cloud.apigee.v1.ApiProxyService.CreateApiProxyRevision`  
`google.cloud.apigee.v1.ApiProxyService.DeleteApiProxy`  
`google.cloud.apigee.v1.ApiProxyService.DeleteApiProxyRevision`  
`google.cloud.apigee.v1.ApiProxyService.MoveApiProxy`  
`google.cloud.apigee.v1.ApiProxyService.UpdateApiProxy`  
`google.cloud.apigee.v1.ApiProxyService.UpdateApiProxyRevision`  
`google.cloud.apigee.v1.ApimServiceExtensionService.CreateApimServiceExtension` (LRO)  
`google.cloud.apigee.v1.ApimServiceExtensionService.DeleteApimServiceExtension` (LRO)  
`google.cloud.apigee.v1.ApimServiceExtensionService.UpdateApimServiceExtension` (LRO)  
`google.cloud.apigee.v1.AppGroupAppKeys.CreateAppGroupAppKey`  
`google.cloud.apigee.v1.AppGroupAppKeys.DeleteApiProductAssociation`  
`google.cloud.apigee.v1.AppGroupAppKeys.DeleteAppGroupAppKey`  
`google.cloud.apigee.v1.AppGroupAppKeys.UpdateAppGroupAppKey`  
`google.cloud.apigee.v1.AppGroupAppKeys.UpdateAppGroupAppKeyApiProduct`  
`google.cloud.apigee.v1.AppGroupApps.CreateAppGroupApp`  
`google.cloud.apigee.v1.AppGroupApps.DeleteAppGroupApp`  
`google.cloud.apigee.v1.AppGroupApps.UpdateAppGroupApp`  
`google.cloud.apigee.v1.AppGroupSubscriptions.CreateAppGroupSubscription`  
`google.cloud.apigee.v1.AppGroupSubscriptions.ExpireAppGroupSubscription`  
`google.cloud.apigee.v1.AppGroups.AdjustAppGroupBalance`  
`google.cloud.apigee.v1.AppGroups.CreateAppGroup`  
`google.cloud.apigee.v1.AppGroups.CreditAppGroupBalance`  
`google.cloud.apigee.v1.AppGroups.DeleteAppGroup`  
`google.cloud.apigee.v1.AppGroups.UpdateAppGroup`  
`google.cloud.apigee.v1.AppGroups.UpdateAppGroupMonetizationConfig`  
`google.cloud.apigee.v1.ArchiveDeploymentService.CreateArchiveDeployment`  
`google.cloud.apigee.v1.ArchiveDeploymentService.DeleteArchiveDeployment`  
`google.cloud.apigee.v1.ArchiveDeploymentService.GenerateUploadUrl`  
`google.cloud.apigee.v1.ArchiveDeploymentService.UpdateArchiveDeployment`  
`google.cloud.apigee.v1.AsyncQueryService.CreateAsyncQuery`  
`google.cloud.apigee.v1.AsyncQueryService.CreateHostAsyncQuery`  
`google.cloud.apigee.v1.CacheService.DeleteCache`  
`google.cloud.apigee.v1.Consumer.CreateConsumerAudience`  
`google.cloud.apigee.v1.Consumer.CreateConsumerAudienceMemberships`  
`google.cloud.apigee.v1.Consumer.DeleteConsumerAudience`  
`google.cloud.apigee.v1.Consumer.DeleteConsumerUser`  
`google.cloud.apigee.v1.Consumer.UpdateConsumerAudience`  
`google.cloud.apigee.v1.Consumer.UpdateConsumerUser`  
`google.cloud.apigee.v1.Customcss.PublishCustomCss`  
`google.cloud.apigee.v1.Customcss.UpdateCustomCss`  
`google.cloud.apigee.v1.DataCollectorService.CreateDataCollector`  
`google.cloud.apigee.v1.DataCollectorService.DeleteDataCollector`  
`google.cloud.apigee.v1.DataCollectorService.UpdateDataCollector`  
`google.cloud.apigee.v1.DataExport.CreateExport`  
`google.cloud.apigee.v1.DataMaskService.UpdateEnvironmentDebugMask`  
`google.cloud.apigee.v1.DeploymentService.AttachSharedFlowToFlowHook`  
`google.cloud.apigee.v1.DeploymentService.DeployApiProxy`  
`google.cloud.apigee.v1.DeploymentService.DeploySharedFlow`  
`google.cloud.apigee.v1.DeploymentService.DetachSharedFlowFromFlowHook`  
`google.cloud.apigee.v1.DeploymentService.GenerateDeployChangeReport`  
`google.cloud.apigee.v1.DeploymentService.GenerateUndeployChangeReport`  
`google.cloud.apigee.v1.DeploymentService.SetIamPolicy`  
`google.cloud.apigee.v1.DeploymentService.UndeployApiProxy`  
`google.cloud.apigee.v1.DeploymentService.UndeploySharedFlow`  
`google.cloud.apigee.v1.DeveloperAppKeys.CreateDeveloperAppKey`  
`google.cloud.apigee.v1.DeveloperAppKeys.DeleteApiProduct`  
`google.cloud.apigee.v1.DeveloperAppKeys.DeleteDeveloperAppKey`  
`google.cloud.apigee.v1.DeveloperAppKeys.ReplaceDeveloperAppKey`  
`google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKey`  
`google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKeyApiProduct`  
`google.cloud.apigee.v1.DeveloperApps.CreateDeveloperApp`  
`google.cloud.apigee.v1.DeveloperApps.DeleteDeveloperApp`  
`google.cloud.apigee.v1.DeveloperApps.DeleteDeveloperAppAttribute`  
`google.cloud.apigee.v1.DeveloperApps.GenerateKeyPairOrUpdateDeveloperAppStatus`  
`google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperApp`  
`google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperAppAttribute`  
`google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperAppAttributes`  
`google.cloud.apigee.v1.DeveloperSubscriptions.CreateDeveloperSubscription`  
`google.cloud.apigee.v1.DeveloperSubscriptions.ExpireDeveloperSubscription`  
`google.cloud.apigee.v1.Developers.AdjustDeveloperBalance`  
`google.cloud.apigee.v1.Developers.CreateDeveloper`  
`google.cloud.apigee.v1.Developers.CreditDeveloperBalance`  
`google.cloud.apigee.v1.Developers.DeleteDeveloper`  
`google.cloud.apigee.v1.Developers.DeleteDeveloperAttribute`  
`google.cloud.apigee.v1.Developers.SetDeveloperStatus`  
`google.cloud.apigee.v1.Developers.UpdateDeveloper`  
`google.cloud.apigee.v1.Developers.UpdateDeveloperAttribute`  
`google.cloud.apigee.v1.Developers.UpdateDeveloperAttributes`  
`google.cloud.apigee.v1.Developers.UpdateDeveloperMonetizationConfig`  
`google.cloud.apigee.v1.DnsZoneService.CreateDnsZone` (LRO)  
`google.cloud.apigee.v1.DnsZoneService.DeleteDnsZone` (LRO)  
`google.cloud.apigee.v1.EndpointAttachmentService.CreateEndpointAttachment` (LRO)  
`google.cloud.apigee.v1.EndpointAttachmentService.DeleteEndpointAttachment` (LRO)  
`google.cloud.apigee.v1.EnvironmentAddons.SetAddonEnablement` (LRO)  
`google.cloud.apigee.v1.EnvironmentGroupAttachmentService.CreateEnvironmentGroupAttachment` (LRO)  
`google.cloud.apigee.v1.EnvironmentGroupAttachmentService.DeleteEnvironmentGroupAttachment` (LRO)  
`google.cloud.apigee.v1.EnvironmentGroupService.CreateEnvironmentGroup` (LRO)  
`google.cloud.apigee.v1.EnvironmentGroupService.DeleteEnvironmentGroup` (LRO)  
`google.cloud.apigee.v1.EnvironmentGroupService.UpdateEnvironmentGroup` (LRO)  
`google.cloud.apigee.v1.EnvironmentService.CreateEnvironment` (LRO)  
`google.cloud.apigee.v1.EnvironmentService.DeleteEnvironment` (LRO)  
`google.cloud.apigee.v1.EnvironmentService.ModifyEnvironment` (LRO)  
`google.cloud.apigee.v1.EnvironmentService.SetIamPolicy`  
`google.cloud.apigee.v1.EnvironmentService.Subscribe`  
`google.cloud.apigee.v1.EnvironmentService.Unsubscribe`  
`google.cloud.apigee.v1.EnvironmentService.UpdateEnvironment`  
`google.cloud.apigee.v1.InstanceAttachmentService.CreateInstanceAttachment` (LRO)  
`google.cloud.apigee.v1.InstanceAttachmentService.DeleteInstanceAttachment` (LRO)  
`google.cloud.apigee.v1.InstanceService.CreateInstance` (LRO)  
`google.cloud.apigee.v1.InstanceService.DeleteInstance` (LRO)  
`google.cloud.apigee.v1.InstanceService.UpdateInstance` (LRO)  
`google.cloud.apigee.v1.KeyValueMapService.CreateApiProxyKeyValueMap`  
`google.cloud.apigee.v1.KeyValueMapService.CreateEnvironmentKeyValueMap`  
`google.cloud.apigee.v1.KeyValueMapService.CreateKeyValueEntry`  
`google.cloud.apigee.v1.KeyValueMapService.CreateOrganizationKeyValueMap`  
`google.cloud.apigee.v1.KeyValueMapService.DeleteApiProxyKeyValueMap`  
`google.cloud.apigee.v1.KeyValueMapService.DeleteEnvironmentKeyValueMap`  
`google.cloud.apigee.v1.KeyValueMapService.DeleteKeyValueEntry`  
`google.cloud.apigee.v1.KeyValueMapService.DeleteOrganizationKeyValueMap`  
`google.cloud.apigee.v1.KeyValueMapService.UpdateKeyValueEntry`  
`google.cloud.apigee.v1.KeyValueMapService.UpdateKeyValueMap`  
`google.cloud.apigee.v1.KeystoreService.CreateKeystore`  
`google.cloud.apigee.v1.KeystoreService.DeleteKeystore`  
`google.cloud.apigee.v1.MenuItems.CreateMenuItem`  
`google.cloud.apigee.v1.MenuItems.DeleteMenuItem`  
`google.cloud.apigee.v1.MenuItems.PublishMenuItem`  
`google.cloud.apigee.v1.MenuItems.ToggleNested`  
`google.cloud.apigee.v1.MenuItems.UpdateMenuItem`  
`google.cloud.apigee.v1.MenuItems.UpdatePriorities`  
`google.cloud.apigee.v1.NatAddressService.ActivateNatAddress` (LRO)  
`google.cloud.apigee.v1.NatAddressService.CreateNatAddress` (LRO)  
`google.cloud.apigee.v1.NatAddressService.DeleteNatAddress` (LRO)  
`google.cloud.apigee.v1.OrganizationService.CreateOrganization` (LRO)  
`google.cloud.apigee.v1.OrganizationService.DeleteOrganization` (LRO)  
`google.cloud.apigee.v1.OrganizationService.SetAddons` (LRO)  
`google.cloud.apigee.v1.OrganizationService.SetSyncAuthorization`  
`google.cloud.apigee.v1.OrganizationService.UpdateControlPlaneAccess` (LRO)  
`google.cloud.apigee.v1.OrganizationService.UpdateOrganization`  
`google.cloud.apigee.v1.Pages.CreatePage`  
`google.cloud.apigee.v1.Pages.DeletePage`  
`google.cloud.apigee.v1.Pages.PublishPage`  
`google.cloud.apigee.v1.Pages.SetPageContent`  
`google.cloud.apigee.v1.Pages.UnpublishPage`  
`google.cloud.apigee.v1.Pages.UpdatePage`  
`google.cloud.apigee.v1.ProjectService.ProvisionOrganization` (LRO)  
`google.cloud.apigee.v1.RatePlans.CreateRatePlan`  
`google.cloud.apigee.v1.RatePlans.DeleteRatePlan`  
`google.cloud.apigee.v1.RatePlans.UpdateRatePlan`  
`google.cloud.apigee.v1.ReferenceService.CreateReference`  
`google.cloud.apigee.v1.ReferenceService.DeleteReference`  
`google.cloud.apigee.v1.ReferenceService.UpdateReference`  
`google.cloud.apigee.v1.ResourceEntitlements.UpdateDefaultResourceEntitlement`  
`google.cloud.apigee.v1.ResourceEntitlements.UpdateResourceEntitlement`  
`google.cloud.apigee.v1.ResourceFileService.CreateEnvironmentResource`  
`google.cloud.apigee.v1.ResourceFileService.DeleteEnvironmentResource`  
`google.cloud.apigee.v1.ResourceFileService.UpdateEnvironmentResource`  
`google.cloud.apigee.v1.RuntimeService.CreateCanaryEvaluation` (LRO)  
`google.cloud.apigee.v1.RuntimeService.ReportInstanceStatus`  
`google.cloud.apigee.v1.SecurityActionService.CreateSecurityAction`  
`google.cloud.apigee.v1.SecurityActionService.DeleteSecurityAction`  
`google.cloud.apigee.v1.SecurityActionService.DisableSecurityAction`  
`google.cloud.apigee.v1.SecurityActionService.EnableSecurityAction`  
`google.cloud.apigee.v1.SecurityActionService.UpdateSecurityAction`  
`google.cloud.apigee.v1.SecurityActionService.UpdateSecurityActionsConfig`  
`google.cloud.apigee.v1.SecurityFeedbackService.CreateSecurityFeedback`  
`google.cloud.apigee.v1.SecurityFeedbackService.DeleteSecurityFeedback`  
`google.cloud.apigee.v1.SecurityFeedbackService.UpdateSecurityFeedback`  
`google.cloud.apigee.v1.SecurityIncidentService.BatchUpdateSecurityIncidents`  
`google.cloud.apigee.v1.SecurityIncidentService.UpdateSecurityIncident`  
`google.cloud.apigee.v1.SecurityProfileService.CreateSecurityProfile`  
`google.cloud.apigee.v1.SecurityProfileService.CreateSecurityProfileEnvironmentAssociation`  
`google.cloud.apigee.v1.SecurityProfileService.DeleteSecurityProfile`  
`google.cloud.apigee.v1.SecurityProfileService.DeleteSecurityProfileEnvironmentAssociation`  
`google.cloud.apigee.v1.SecurityProfileService.UpdateSecurityProfile`  
`google.cloud.apigee.v1.SecurityReportService.CreateHostSecurityReport`  
`google.cloud.apigee.v1.SecurityReportService.CreateSecurityReport`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.CreateSecurityMonitoringCondition`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.CreateSecurityProfileV2`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.DeleteSecurityMonitoringCondition`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.DeleteSecurityProfileV2`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.UpdateSecurityMonitoringCondition`  
`google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.UpdateSecurityProfileV2`  
`google.cloud.apigee.v1.SecuritySettingsService.UpdateSecuritySettings`  
`google.cloud.apigee.v1.SharedFlowService.CreateSharedFlowRevision`  
`google.cloud.apigee.v1.SharedFlowService.DeleteSharedFlow`  
`google.cloud.apigee.v1.SharedFlowService.DeleteSharedFlowRevision`  
`google.cloud.apigee.v1.SharedFlowService.MoveSharedFlow`  
`google.cloud.apigee.v1.SharedFlowService.UpdateSharedFlowRevision`  
`google.cloud.apigee.v1.SiteDomain.DisableCustomDomain`  
`google.cloud.apigee.v1.SiteDomain.EnableCustomDomain`  
`google.cloud.apigee.v1.SiteEmail.UpdateEmailTemplate`  
`google.cloud.apigee.v1.SiteFile.DeleteFile`  
`google.cloud.apigee.v1.SiteFile.UploadFile`  
`google.cloud.apigee.v1.SiteOperation.RegenerateSecretKey`  
`google.cloud.apigee.v1.SiteOperation.ResetSmtp`  
`google.cloud.apigee.v1.SiteOperation.SendTestEmail`  
`google.cloud.apigee.v1.SiteOperation.SetApprovedEmails`  
`google.cloud.apigee.v1.SiteOperation.SetDefaultAnonAllowed`  
`google.cloud.apigee.v1.SiteOperation.TrashSite`  
`google.cloud.apigee.v1.SiteOperation.UpdateAnalyticsScript`  
`google.cloud.apigee.v1.SiteOperation.UpdateContentSecurityPolicy`  
`google.cloud.apigee.v1.SiteOperation.VerifyDraftToken`  
`google.cloud.apigee.v1.Sites.CloneSite`  
`google.cloud.apigee.v1.Sites.CreateSite`  
`google.cloud.apigee.v1.Sites.UpdateSite`  
`google.cloud.apigee.v1.Sites.UpdateSmtp`  
`google.cloud.apigee.v1.SpaceService.CreateSpace`  
`google.cloud.apigee.v1.SpaceService.DeleteSpace`  
`google.cloud.apigee.v1.SpaceService.SetIamPolicy`  
`google.cloud.apigee.v1.SpaceService.UpdateSpace`  
`google.cloud.apigee.v1.TargetServerService.CreateTargetServer`  
`google.cloud.apigee.v1.TargetServerService.DeleteTargetServer`  
`google.cloud.apigee.v1.TargetServerService.UpdateTargetServer`  
`google.cloud.apigee.v1.TraceConfigOverrideService.CreateTraceConfigOverride`  
`google.cloud.apigee.v1.TraceConfigOverrideService.DeleteTraceConfigOverride`  
`google.cloud.apigee.v1.TraceConfigOverrideService.UpdateTraceConfigOverride`  
`google.cloud.apigee.v1.TraceConfigService.UpdateTraceConfig`  
`google.cloud.apigee.v1.Zones.AssociateSiteZone`  
`google.cloud.apigee.v1.Zones.CreateIdentityProvider`  
`google.cloud.apigee.v1.Zones.EnableZoneAudience`  
`google.cloud.apigee.v1.Zones.UpdateIdentityProvider`  
`google.cloud.apigee.v1.Zones.UpdateIdentityProviderCertificate`  
`google.cloud.apigee.v1.Zones.UpdateIdentityProviderConfig`  
`google.cloud.apigee.v1.Zones.UpdateZone`  
`google.cloud.apigee.v1.Zones.VerifyCertificate`  
`DATA_READ` | `google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetHostStats`  
`google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetOptimizedHostStats`  
`google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetOptimizedStats`  
`google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetStats`  
`google.cloud.apigee.v1.CollectionService.GetDataLocation`  
`google.cloud.apigee.v1.DataMaskService.GetEnvironmentDebugMask`  
`google.cloud.apigee.v1.DebugSessionService.GetDebugSession`  
`google.cloud.apigee.v1.DebugSessionService.GetDebugSessionTransaction`  
`google.cloud.apigee.v1.DebugSessionService.ListApiDebugSessions`  
`google.cloud.apigee.v1.DebugSessionService.ListDebugSessionTransactions`  
`google.cloud.apigee.v1.DebugSessionService.ListDebugSessions`  
`google.cloud.apigee.v1.KeystoreService.GenerateCsr`  
`google.cloud.apigee.v1.KeystoreService.GetAlias`  
`google.cloud.apigee.v1.KeystoreService.ListAliases`  
`DATA_WRITE` | `google.cloud.apigee.v1.DebugSessionService.CreateDebugSession`  
`google.cloud.apigee.v1.DebugSessionService.DeleteDebugSessionData`  
`google.cloud.apigee.v1.KeystoreService.CreateAlias`  
`google.cloud.apigee.v1.KeystoreService.DeleteAlias`  
`google.cloud.apigee.v1.KeystoreService.GetCertificateFromAlias`  
`google.cloud.apigee.v1.KeystoreService.UpdateAlias`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Apigee.

### `google.cloud.apigee.v1.AnalyticsCustomReport`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AnalyticsCustomReport`.

#### `CreateCustomReport`

  * **Method** : `google.cloud.apigee.v1.AnalyticsCustomReport.CreateCustomReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.reports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsCustomReport.CreateCustomReport" `  




#### `DeleteCustomReport`

  * **Method** : `google.cloud.apigee.v1.AnalyticsCustomReport.DeleteCustomReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.reports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsCustomReport.DeleteCustomReport" `  




#### `GetCustomReport`

  * **Method** : `google.cloud.apigee.v1.AnalyticsCustomReport.GetCustomReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.reports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsCustomReport.GetCustomReport" `  




#### `ListCustomReports`

  * **Method** : `google.cloud.apigee.v1.AnalyticsCustomReport.ListCustomReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.reports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsCustomReport.ListCustomReports" `  




#### `UpdateCustomReport`

  * **Method** : `google.cloud.apigee.v1.AnalyticsCustomReport.UpdateCustomReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.reports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsCustomReport.UpdateCustomReport" `  




### `google.cloud.apigee.v1.AnalyticsDatastore`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AnalyticsDatastore`.

#### `CreateDatastore`

  * **Method** : `google.cloud.apigee.v1.AnalyticsDatastore.CreateDatastore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.datastores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsDatastore.CreateDatastore" `  




#### `DeleteDatastore`

  * **Method** : `google.cloud.apigee.v1.AnalyticsDatastore.DeleteDatastore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.datastores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsDatastore.DeleteDatastore" `  




#### `GetDatastore`

  * **Method** : `google.cloud.apigee.v1.AnalyticsDatastore.GetDatastore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.datastores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsDatastore.GetDatastore" `  




#### `ListDatastores`

  * **Method** : `google.cloud.apigee.v1.AnalyticsDatastore.ListDatastores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.datastores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsDatastore.ListDatastores" `  




#### `TestDatastore`

  * **Method** : `google.cloud.apigee.v1.AnalyticsDatastore.TestDatastore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.datastores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsDatastore.TestDatastore" `  




#### `UpdateDatastore`

  * **Method** : `google.cloud.apigee.v1.AnalyticsDatastore.UpdateDatastore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.datastores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsDatastore.UpdateDatastore" `  




### `google.cloud.apigee.v1.AnalyticsInteractiveQuery`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AnalyticsInteractiveQuery`.

#### `GetHostStats`

  * **Method** : `google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetHostStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hoststats.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetHostStats" `  




#### `GetOptimizedHostStats`

  * **Method** : `google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetOptimizedHostStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hoststats.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetOptimizedHostStats" `  




#### `GetOptimizedStats`

  * **Method** : `google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetOptimizedStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.getStats - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetOptimizedStats" `  




#### `GetStats`

  * **Method** : `google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.getStats - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsInteractiveQuery.GetStats" `  




### `google.cloud.apigee.v1.AnalyticsSchema`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AnalyticsSchema`.

#### `GetSchema`

  * **Method** : `google.cloud.apigee.v1.AnalyticsSchema.GetSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AnalyticsSchema.GetSchema" `  




### `google.cloud.apigee.v1.ApiCategories`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ApiCategories`.

#### `CreateApiCategory`

  * **Method** : `google.cloud.apigee.v1.ApiCategories.CreateApiCategory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiCategories.CreateApiCategory" `  




#### `DeleteApiCategory`

  * **Method** : `google.cloud.apigee.v1.ApiCategories.DeleteApiCategory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiCategories.DeleteApiCategory" `  




#### `GetApiCategory`

  * **Method** : `google.cloud.apigee.v1.ApiCategories.GetApiCategory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiCategories.GetApiCategory" `  




#### `ListApiCategories`

  * **Method** : `google.cloud.apigee.v1.ApiCategories.ListApiCategories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiCategories.ListApiCategories" `  




#### `UpdateApiCategory`

  * **Method** : `google.cloud.apigee.v1.ApiCategories.UpdateApiCategory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiCategories.UpdateApiCategory" `  




### `google.cloud.apigee.v1.ApiDocs`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ApiDocs`.

#### `CreateApiDoc`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.CreateApiDoc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.CreateApiDoc" `  




#### `DeleteApiDoc`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.DeleteApiDoc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.DeleteApiDoc" `  




#### `DeleteSnapshot`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.DeleteSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.DeleteSnapshot" `  




#### `GetApiDoc`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.GetApiDoc`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.GetApiDoc" `  




#### `GetApiDocDocumentation`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.GetApiDocDocumentation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.GetApiDocDocumentation" `  




#### `ListApiDocs`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.ListApiDocs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.ListApiDocs" `  




#### `ListPublishableProducts`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.ListPublishableProducts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.ListPublishableProducts" `  




#### `PostSnapshot`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.PostSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.PostSnapshot" `  




#### `TagApiDocs`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.TagApiDocs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.TagApiDocs" `  




#### `UpdateApiDoc`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.UpdateApiDoc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.UpdateApiDoc" `  




#### `UpdateApiDocDocumentation`

  * **Method** : `google.cloud.apigee.v1.ApiDocs.UpdateApiDocDocumentation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiDocs.UpdateApiDocDocumentation" `  




### `google.cloud.apigee.v1.ApiProducts`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ApiProducts`.

#### `CreateApiProduct`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.CreateApiProduct`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apiproducts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.CreateApiProduct" `  




#### `DeleteApiProduct`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.DeleteApiProduct`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apiproducts.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.DeleteApiProduct" `  




#### `DeleteApiProductAttribute`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.DeleteApiProductAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apiproductattributes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.DeleteApiProductAttribute" `  




#### `GetApiProduct`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.GetApiProduct`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apiproducts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.GetApiProduct" `  




#### `GetApiProductAttribute`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.GetApiProductAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apiproductattributes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.GetApiProductAttribute" `  




#### `ListApiProductAttributes`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.ListApiProductAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apiproductattributes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.ListApiProductAttributes" `  




#### `ListApiProducts`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.ListApiProducts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apiproducts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.ListApiProducts" `  




#### `MoveApiProduct`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.MoveApiProduct`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apiproducts.create - ADMIN_WRITE`
    * `apigee.apiproducts.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.MoveApiProduct" `  




#### `UpdateApiProduct`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.UpdateApiProduct`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apiproducts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.UpdateApiProduct" `  




#### `UpdateApiProductAttribute`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.UpdateApiProductAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apiproductattributes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.UpdateApiProductAttribute" `  




#### `UpdateApiProductAttributes`

  * **Method** : `google.cloud.apigee.v1.ApiProducts.UpdateApiProductAttributes`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apiproductattributes.createOrUpdateAll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProducts.UpdateApiProductAttributes" `  




### `google.cloud.apigee.v1.ApiProxyService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ApiProxyService`.

#### `CreateApiProxyRevision`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.CreateApiProxyRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.proxies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.CreateApiProxyRevision" `  




#### `DeleteApiProxy`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.DeleteApiProxy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.proxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.DeleteApiProxy" `  




#### `DeleteApiProxyRevision`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.DeleteApiProxyRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.proxyrevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.DeleteApiProxyRevision" `  




#### `GetApiProxy`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.GetApiProxy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.proxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.GetApiProxy" `  




#### `GetApiProxyRevision`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.GetApiProxyRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.proxyrevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.GetApiProxyRevision" `  




#### `ListApiProxies`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.ListApiProxies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.proxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.ListApiProxies" `  




#### `ListApiProxyRevisions`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.ListApiProxyRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.proxyrevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.ListApiProxyRevisions" `  




#### `MoveApiProxy`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.MoveApiProxy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.proxies.create - ADMIN_WRITE`
    * `apigee.proxies.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.MoveApiProxy" `  




#### `UpdateApiProxy`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.UpdateApiProxy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.proxies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.UpdateApiProxy" `  




#### `UpdateApiProxyRevision`

  * **Method** : `google.cloud.apigee.v1.ApiProxyService.UpdateApiProxyRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.proxyrevisions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApiProxyService.UpdateApiProxyRevision" `  




### `google.cloud.apigee.v1.ApimServiceExtensionService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ApimServiceExtensionService`.

#### `CreateApimServiceExtension`

  * **Method** : `google.cloud.apigee.v1.ApimServiceExtensionService.CreateApimServiceExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apimServiceExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApimServiceExtensionService.CreateApimServiceExtension" `  




#### `DeleteApimServiceExtension`

  * **Method** : `google.cloud.apigee.v1.ApimServiceExtensionService.DeleteApimServiceExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apimServiceExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApimServiceExtensionService.DeleteApimServiceExtension" `  




#### `GetApimServiceExtension`

  * **Method** : `google.cloud.apigee.v1.ApimServiceExtensionService.GetApimServiceExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apimServiceExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApimServiceExtensionService.GetApimServiceExtension" `  




#### `ListApimServiceExtensions`

  * **Method** : `google.cloud.apigee.v1.ApimServiceExtensionService.ListApimServiceExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apimServiceExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApimServiceExtensionService.ListApimServiceExtensions" `  




#### `UpdateApimServiceExtension`

  * **Method** : `google.cloud.apigee.v1.ApimServiceExtensionService.UpdateApimServiceExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.apimServiceExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ApimServiceExtensionService.UpdateApimServiceExtension" `  




### `google.cloud.apigee.v1.AppGroupAppKeys`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AppGroupAppKeys`.

#### `CreateAppGroupAppKey`

  * **Method** : `google.cloud.apigee.v1.AppGroupAppKeys.CreateAppGroupAppKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupAppKeys.CreateAppGroupAppKey" `  




#### `DeleteApiProductAssociation`

  * **Method** : `google.cloud.apigee.v1.AppGroupAppKeys.DeleteApiProductAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupAppKeys.DeleteApiProductAssociation" `  




#### `DeleteAppGroupAppKey`

  * **Method** : `google.cloud.apigee.v1.AppGroupAppKeys.DeleteAppGroupAppKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupAppKeys.DeleteAppGroupAppKey" `  




#### `GetAppGroupAppKey`

  * **Method** : `google.cloud.apigee.v1.AppGroupAppKeys.GetAppGroupAppKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appkeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupAppKeys.GetAppGroupAppKey" `  




#### `UpdateAppGroupAppKey`

  * **Method** : `google.cloud.apigee.v1.AppGroupAppKeys.UpdateAppGroupAppKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupAppKeys.UpdateAppGroupAppKey" `  




#### `UpdateAppGroupAppKeyApiProduct`

  * **Method** : `google.cloud.apigee.v1.AppGroupAppKeys.UpdateAppGroupAppKeyApiProduct`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupAppKeys.UpdateAppGroupAppKeyApiProduct" `  




### `google.cloud.apigee.v1.AppGroupApps`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AppGroupApps`.

#### `CreateAppGroupApp`

  * **Method** : `google.cloud.apigee.v1.AppGroupApps.CreateAppGroupApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupapps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupApps.CreateAppGroupApp" `  




#### `DeleteAppGroupApp`

  * **Method** : `google.cloud.apigee.v1.AppGroupApps.DeleteAppGroupApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupapps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupApps.DeleteAppGroupApp" `  




#### `GetAppGroupApp`

  * **Method** : `google.cloud.apigee.v1.AppGroupApps.GetAppGroupApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroupapps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupApps.GetAppGroupApp" `  




#### `ListAppGroupApps`

  * **Method** : `google.cloud.apigee.v1.AppGroupApps.ListAppGroupApps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroupapps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupApps.ListAppGroupApps" `  




#### `UpdateAppGroupApp`

  * **Method** : `google.cloud.apigee.v1.AppGroupApps.UpdateAppGroupApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupapps.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupApps.UpdateAppGroupApp" `  




### `google.cloud.apigee.v1.AppGroupSubscriptions`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AppGroupSubscriptions`.

#### `CreateAppGroupSubscription`

  * **Method** : `google.cloud.apigee.v1.AppGroupSubscriptions.CreateAppGroupSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupsubscriptions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupSubscriptions.CreateAppGroupSubscription" `  




#### `ExpireAppGroupSubscription`

  * **Method** : `google.cloud.apigee.v1.AppGroupSubscriptions.ExpireAppGroupSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupsubscriptions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupSubscriptions.ExpireAppGroupSubscription" `  




#### `GetAppGroupSubscription`

  * **Method** : `google.cloud.apigee.v1.AppGroupSubscriptions.GetAppGroupSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroupsubscriptions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupSubscriptions.GetAppGroupSubscription" `  




#### `ListAppGroupSubscriptions`

  * **Method** : `google.cloud.apigee.v1.AppGroupSubscriptions.ListAppGroupSubscriptions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroupsubscriptions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroupSubscriptions.ListAppGroupSubscriptions" `  




### `google.cloud.apigee.v1.AppGroups`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AppGroups`.

#### `AdjustAppGroupBalance`

  * **Method** : `google.cloud.apigee.v1.AppGroups.AdjustAppGroupBalance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupbalances.adjust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.AdjustAppGroupBalance" `  




#### `CreateAppGroup`

  * **Method** : `google.cloud.apigee.v1.AppGroups.CreateAppGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.CreateAppGroup" `  




#### `CreditAppGroupBalance`

  * **Method** : `google.cloud.apigee.v1.AppGroups.CreditAppGroupBalance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupbalances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.CreditAppGroupBalance" `  




#### `DeleteAppGroup`

  * **Method** : `google.cloud.apigee.v1.AppGroups.DeleteAppGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.DeleteAppGroup" `  




#### `GetAppGroup`

  * **Method** : `google.cloud.apigee.v1.AppGroups.GetAppGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.GetAppGroup" `  




#### `GetAppGroupBalance`

  * **Method** : `google.cloud.apigee.v1.AppGroups.GetAppGroupBalance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroupbalances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.GetAppGroupBalance" `  




#### `GetAppGroupMonetizationConfig`

  * **Method** : `google.cloud.apigee.v1.AppGroups.GetAppGroupMonetizationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroupmonetizationconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.GetAppGroupMonetizationConfig" `  




#### `ListAppGroups`

  * **Method** : `google.cloud.apigee.v1.AppGroups.ListAppGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appgroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.ListAppGroups" `  




#### `UpdateAppGroup`

  * **Method** : `google.cloud.apigee.v1.AppGroups.UpdateAppGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.UpdateAppGroup" `  




#### `UpdateAppGroupMonetizationConfig`

  * **Method** : `google.cloud.apigee.v1.AppGroups.UpdateAppGroupMonetizationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appgroupmonetizationconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AppGroups.UpdateAppGroupMonetizationConfig" `  




### `google.cloud.apigee.v1.Apps`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Apps`.

#### `GetApp`

  * **Method** : `google.cloud.apigee.v1.Apps.GetApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Apps.GetApp" `  




#### `ListApps`

  * **Method** : `google.cloud.apigee.v1.Apps.ListApps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.apps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Apps.ListApps" `  




### `google.cloud.apigee.v1.ArchiveDeploymentService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ArchiveDeploymentService`.

#### `CreateArchiveDeployment`

  * **Method** : `google.cloud.apigee.v1.ArchiveDeploymentService.CreateArchiveDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.archivedeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ArchiveDeploymentService.CreateArchiveDeployment" `  




#### `DeleteArchiveDeployment`

  * **Method** : `google.cloud.apigee.v1.ArchiveDeploymentService.DeleteArchiveDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.archivedeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ArchiveDeploymentService.DeleteArchiveDeployment" `  




#### `GenerateDownloadUrl`

  * **Method** : `google.cloud.apigee.v1.ArchiveDeploymentService.GenerateDownloadUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.archivedeployments.download - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ArchiveDeploymentService.GenerateDownloadUrl" `  




#### `GenerateUploadUrl`

  * **Method** : `google.cloud.apigee.v1.ArchiveDeploymentService.GenerateUploadUrl`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.archivedeployments.upload - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ArchiveDeploymentService.GenerateUploadUrl" `  




#### `GetArchiveDeployment`

  * **Method** : `google.cloud.apigee.v1.ArchiveDeploymentService.GetArchiveDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.archivedeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ArchiveDeploymentService.GetArchiveDeployment" `  




#### `ListArchiveDeployments`

  * **Method** : `google.cloud.apigee.v1.ArchiveDeploymentService.ListArchiveDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.archivedeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ArchiveDeploymentService.ListArchiveDeployments" `  




#### `UpdateArchiveDeployment`

  * **Method** : `google.cloud.apigee.v1.ArchiveDeploymentService.UpdateArchiveDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.archivedeployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ArchiveDeploymentService.UpdateArchiveDeployment" `  




### `google.cloud.apigee.v1.AsyncQueryService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.AsyncQueryService`.

#### `CreateAsyncQuery`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.CreateAsyncQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.queries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.CreateAsyncQuery" `  




#### `CreateHostAsyncQuery`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.CreateHostAsyncQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.hostqueries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.CreateHostAsyncQuery" `  




#### `GetAsyncQuery`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.GetAsyncQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.queries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.GetAsyncQuery" `  




#### `GetAsyncQueryResult`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.GetAsyncQueryResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.queries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.GetAsyncQueryResult" `  




#### `GetAsyncQueryResultView`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.GetAsyncQueryResultView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.queries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.GetAsyncQueryResultView" `  




#### `GetHostAsyncQuery`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostqueries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQuery" `  




#### `GetHostAsyncQueryResult`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQueryResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostqueries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQueryResult" `  




#### `GetHostAsyncQueryResultView`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQueryResultView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostqueries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.GetHostAsyncQueryResultView" `  




#### `ListAsyncQueries`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.ListAsyncQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.queries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.ListAsyncQueries" `  




#### `ListHostAsyncQueries`

  * **Method** : `google.cloud.apigee.v1.AsyncQueryService.ListHostAsyncQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostqueries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.AsyncQueryService.ListHostAsyncQueries" `  




### `google.cloud.apigee.v1.CacheService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.CacheService`.

#### `DeleteCache`

  * **Method** : `google.cloud.apigee.v1.CacheService.DeleteCache`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.caches.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.CacheService.DeleteCache" `  




#### `ListCaches`

  * **Method** : `google.cloud.apigee.v1.CacheService.ListCaches`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.caches.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.CacheService.ListCaches" `  




### `google.cloud.apigee.v1.CollectionService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.CollectionService`.

#### `GetDataLocation`

  * **Method** : `google.cloud.apigee.v1.CollectionService.GetDataLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.getDataLocation - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.CollectionService.GetDataLocation" `  




#### `GetOrganizationDataLocation`

  * **Method** : `google.cloud.apigee.v1.CollectionService.GetOrganizationDataLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.datalocation.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.CollectionService.GetOrganizationDataLocation" `  




### `google.cloud.apigee.v1.Consumer`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Consumer`.

#### `CreateConsumerAudience`

  * **Method** : `google.cloud.apigee.v1.Consumer.CreateConsumerAudience`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.CreateConsumerAudience" `  




#### `CreateConsumerAudienceMemberships`

  * **Method** : `google.cloud.apigee.v1.Consumer.CreateConsumerAudienceMemberships`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.CreateConsumerAudienceMemberships" `  




#### `DeleteConsumerAudience`

  * **Method** : `google.cloud.apigee.v1.Consumer.DeleteConsumerAudience`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.DeleteConsumerAudience" `  




#### `DeleteConsumerUser`

  * **Method** : `google.cloud.apigee.v1.Consumer.DeleteConsumerUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.DeleteConsumerUser" `  




#### `GetConsumerAudience`

  * **Method** : `google.cloud.apigee.v1.Consumer.GetConsumerAudience`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.GetConsumerAudience" `  




#### `GetConsumerTeam`

  * **Method** : `google.cloud.apigee.v1.Consumer.GetConsumerTeam`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.GetConsumerTeam" `  




#### `GetConsumerUser`

  * **Method** : `google.cloud.apigee.v1.Consumer.GetConsumerUser`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.GetConsumerUser" `  




#### `ListConsumerAudiences`

  * **Method** : `google.cloud.apigee.v1.Consumer.ListConsumerAudiences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.ListConsumerAudiences" `  




#### `ListConsumerTeams`

  * **Method** : `google.cloud.apigee.v1.Consumer.ListConsumerTeams`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.ListConsumerTeams" `  




#### `ListConsumerUsers`

  * **Method** : `google.cloud.apigee.v1.Consumer.ListConsumerUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.ListConsumerUsers" `  




#### `UpdateConsumerAudience`

  * **Method** : `google.cloud.apigee.v1.Consumer.UpdateConsumerAudience`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.UpdateConsumerAudience" `  




#### `UpdateConsumerUser`

  * **Method** : `google.cloud.apigee.v1.Consumer.UpdateConsumerUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Consumer.UpdateConsumerUser" `  




### `google.cloud.apigee.v1.Customcss`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Customcss`.

#### `GetCustomCss`

  * **Method** : `google.cloud.apigee.v1.Customcss.GetCustomCss`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Customcss.GetCustomCss" `  




#### `GetEditorSchema`

  * **Method** : `google.cloud.apigee.v1.Customcss.GetEditorSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Customcss.GetEditorSchema" `  




#### `PublishCustomCss`

  * **Method** : `google.cloud.apigee.v1.Customcss.PublishCustomCss`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Customcss.PublishCustomCss" `  




#### `UpdateCustomCss`

  * **Method** : `google.cloud.apigee.v1.Customcss.UpdateCustomCss`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Customcss.UpdateCustomCss" `  




### `google.cloud.apigee.v1.DataCollectorService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DataCollectorService`.

#### `CreateDataCollector`

  * **Method** : `google.cloud.apigee.v1.DataCollectorService.CreateDataCollector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.datacollectors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataCollectorService.CreateDataCollector" `  




#### `DeleteDataCollector`

  * **Method** : `google.cloud.apigee.v1.DataCollectorService.DeleteDataCollector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.datacollectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataCollectorService.DeleteDataCollector" `  




#### `GetDataCollector`

  * **Method** : `google.cloud.apigee.v1.DataCollectorService.GetDataCollector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.datacollectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataCollectorService.GetDataCollector" `  




#### `ListDataCollectors`

  * **Method** : `google.cloud.apigee.v1.DataCollectorService.ListDataCollectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.datacollectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataCollectorService.ListDataCollectors" `  




#### `UpdateDataCollector`

  * **Method** : `google.cloud.apigee.v1.DataCollectorService.UpdateDataCollector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.datacollectors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataCollectorService.UpdateDataCollector" `  




### `google.cloud.apigee.v1.DataExport`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DataExport`.

#### `CreateExport`

  * **Method** : `google.cloud.apigee.v1.DataExport.CreateExport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.exports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataExport.CreateExport" `  




#### `GetExport`

  * **Method** : `google.cloud.apigee.v1.DataExport.GetExport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.exports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataExport.GetExport" `  




#### `ListExports`

  * **Method** : `google.cloud.apigee.v1.DataExport.ListExports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.exports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataExport.ListExports" `  




### `google.cloud.apigee.v1.DataMaskService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DataMaskService`.

#### `GetEnvironmentDebugMask`

  * **Method** : `google.cloud.apigee.v1.DataMaskService.GetEnvironmentDebugMask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.maskconfigs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataMaskService.GetEnvironmentDebugMask" `  




#### `UpdateEnvironmentDebugMask`

  * **Method** : `google.cloud.apigee.v1.DataMaskService.UpdateEnvironmentDebugMask`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.maskconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DataMaskService.UpdateEnvironmentDebugMask" `  




### `google.cloud.apigee.v1.DebugSessionService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DebugSessionService`.

#### `CreateDebugSession`

  * **Method** : `google.cloud.apigee.v1.DebugSessionService.CreateDebugSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.tracesessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DebugSessionService.CreateDebugSession" `  




#### `DeleteDebugSessionData`

  * **Method** : `google.cloud.apigee.v1.DebugSessionService.DeleteDebugSessionData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.tracesessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DebugSessionService.DeleteDebugSessionData" `  




#### `GetDebugSession`

  * **Method** : `google.cloud.apigee.v1.DebugSessionService.GetDebugSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.tracesessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DebugSessionService.GetDebugSession" `  




#### `GetDebugSessionTransaction`

  * **Method** : `google.cloud.apigee.v1.DebugSessionService.GetDebugSessionTransaction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.tracesessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DebugSessionService.GetDebugSessionTransaction" `  




#### `ListApiDebugSessions`

  * **Method** : `google.cloud.apigee.v1.DebugSessionService.ListApiDebugSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.tracesessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DebugSessionService.ListApiDebugSessions" `  




#### `ListDebugSessionTransactions`

  * **Method** : `google.cloud.apigee.v1.DebugSessionService.ListDebugSessionTransactions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.tracesessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DebugSessionService.ListDebugSessionTransactions" `  




#### `ListDebugSessions`

  * **Method** : `google.cloud.apigee.v1.DebugSessionService.ListDebugSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.tracesessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DebugSessionService.ListDebugSessions" `  




### `google.cloud.apigee.v1.DeploymentService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DeploymentService`.

#### `AttachSharedFlowToFlowHook`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.AttachSharedFlowToFlowHook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.flowhooks.attachSharedFlow - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.AttachSharedFlowToFlowHook" `  




#### `DeployApiProxy`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.DeployApiProxy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.deployments.create - ADMIN_WRITE`
    * `apigee.proxyrevisions.deploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.DeployApiProxy" `  




#### `DeploySharedFlow`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.DeploySharedFlow`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.deployments.create - ADMIN_WRITE`
    * `apigee.sharedflowrevisions.deploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.DeploySharedFlow" `  




#### `DetachSharedFlowFromFlowHook`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.DetachSharedFlowFromFlowHook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.flowhooks.detachSharedFlow - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.DetachSharedFlowFromFlowHook" `  




#### `GenerateDeployChangeReport`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.GenerateDeployChangeReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.deployments.create - ADMIN_WRITE`
    * `apigee.proxyrevisions.deploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.GenerateDeployChangeReport" `  




#### `GenerateUndeployChangeReport`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.GenerateUndeployChangeReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.deployments.delete - ADMIN_WRITE`
    * `apigee.proxyrevisions.undeploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.GenerateUndeployChangeReport" `  




#### `GetApiDeployment`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.GetApiDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.GetApiDeployment" `  




#### `GetEnvironmentDeployment`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.GetEnvironmentDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.GetEnvironmentDeployment" `  




#### `GetFlowHook`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.GetFlowHook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.flowhooks.getSharedFlow - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.GetFlowHook" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.GetIamPolicy" `  




#### `GetSharedFlowDeployment`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.GetSharedFlowDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.GetSharedFlowDeployment" `  




#### `ListApiDeployments`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListApiDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListApiDeployments" `  




#### `ListApiDeploymentsInEnvironment`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListApiDeploymentsInEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListApiDeploymentsInEnvironment" `  




#### `ListApiRevisionDeployments`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListApiRevisionDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListApiRevisionDeployments" `  




#### `ListEnvironmentDeployments`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListEnvironmentDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListEnvironmentDeployments" `  




#### `ListFlowHooks`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListFlowHooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.flowhooks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListFlowHooks" `  




#### `ListOrganizationDeployments`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListOrganizationDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListOrganizationDeployments" `  




#### `ListSharedFlowDeployments`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListSharedFlowDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListSharedFlowDeployments" `  




#### `ListSharedFlowDeploymentsInEnvironment`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListSharedFlowDeploymentsInEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListSharedFlowDeploymentsInEnvironment" `  




#### `ListSharedFlowRevisionDeployments`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.ListSharedFlowRevisionDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.ListSharedFlowRevisionDeployments" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.deployments.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.SetIamPolicy" `  




#### `UndeployApiProxy`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.UndeployApiProxy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.deployments.delete - ADMIN_WRITE`
    * `apigee.proxyrevisions.undeploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.UndeployApiProxy" `  




#### `UndeploySharedFlow`

  * **Method** : `google.cloud.apigee.v1.DeploymentService.UndeploySharedFlow`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.deployments.delete - ADMIN_WRITE`
    * `apigee.sharedflowrevisions.undeploy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeploymentService.UndeploySharedFlow" `  




### `google.cloud.apigee.v1.DeveloperAppKeys`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DeveloperAppKeys`.

#### `CreateDeveloperAppKey`

  * **Method** : `google.cloud.apigee.v1.DeveloperAppKeys.CreateDeveloperAppKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperAppKeys.CreateDeveloperAppKey" `  




#### `DeleteApiProduct`

  * **Method** : `google.cloud.apigee.v1.DeveloperAppKeys.DeleteApiProduct`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperAppKeys.DeleteApiProduct" `  




#### `DeleteDeveloperAppKey`

  * **Method** : `google.cloud.apigee.v1.DeveloperAppKeys.DeleteDeveloperAppKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperAppKeys.DeleteDeveloperAppKey" `  




#### `GetDeveloperAppKey`

  * **Method** : `google.cloud.apigee.v1.DeveloperAppKeys.GetDeveloperAppKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.appkeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperAppKeys.GetDeveloperAppKey" `  




#### `ReplaceDeveloperAppKey`

  * **Method** : `google.cloud.apigee.v1.DeveloperAppKeys.ReplaceDeveloperAppKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperAppKeys.ReplaceDeveloperAppKey" `  




#### `UpdateDeveloperAppKey`

  * **Method** : `google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKey" `  




#### `UpdateDeveloperAppKeyApiProduct`

  * **Method** : `google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKeyApiProduct`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.appkeys.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKeyApiProduct" `  




### `google.cloud.apigee.v1.DeveloperApps`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DeveloperApps`.

#### `CreateDeveloperApp`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.CreateDeveloperApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerapps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.CreateDeveloperApp" `  




#### `DeleteDeveloperApp`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.DeleteDeveloperApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerapps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.DeleteDeveloperApp" `  




#### `DeleteDeveloperAppAttribute`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.DeleteDeveloperAppAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerappattributes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.DeleteDeveloperAppAttribute" `  




#### `GenerateKeyPairOrUpdateDeveloperAppStatus`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.GenerateKeyPairOrUpdateDeveloperAppStatus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerapps.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.GenerateKeyPairOrUpdateDeveloperAppStatus" `  




#### `GetDeveloperApp`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.GetDeveloperApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developerapps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.GetDeveloperApp" `  




#### `GetDeveloperAppAttribute`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.GetDeveloperAppAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developerappattributes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.GetDeveloperAppAttribute" `  




#### `ListDeveloperAppAttributes`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.ListDeveloperAppAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developerappattributes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.ListDeveloperAppAttributes" `  




#### `ListDeveloperApps`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.ListDeveloperApps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developerapps.get - ADMIN_READ`
    * `apigee.developerapps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.ListDeveloperApps" `  




#### `UpdateDeveloperApp`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerapps.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperApp" `  




#### `UpdateDeveloperAppAttribute`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperAppAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerappattributes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperAppAttribute" `  




#### `UpdateDeveloperAppAttributes`

  * **Method** : `google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperAppAttributes`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerappattributes.createOrUpdateAll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperApps.UpdateDeveloperAppAttributes" `  




### `google.cloud.apigee.v1.DeveloperSubscriptions`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DeveloperSubscriptions`.

#### `CreateDeveloperSubscription`

  * **Method** : `google.cloud.apigee.v1.DeveloperSubscriptions.CreateDeveloperSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developersubscriptions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperSubscriptions.CreateDeveloperSubscription" `  




#### `ExpireDeveloperSubscription`

  * **Method** : `google.cloud.apigee.v1.DeveloperSubscriptions.ExpireDeveloperSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developersubscriptions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperSubscriptions.ExpireDeveloperSubscription" `  




#### `GetDeveloperSubscription`

  * **Method** : `google.cloud.apigee.v1.DeveloperSubscriptions.GetDeveloperSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developersubscriptions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperSubscriptions.GetDeveloperSubscription" `  




#### `ListDeveloperSubscriptions`

  * **Method** : `google.cloud.apigee.v1.DeveloperSubscriptions.ListDeveloperSubscriptions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developersubscriptions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DeveloperSubscriptions.ListDeveloperSubscriptions" `  




### `google.cloud.apigee.v1.Developers`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Developers`.

#### `AdjustDeveloperBalance`

  * **Method** : `google.cloud.apigee.v1.Developers.AdjustDeveloperBalance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerbalances.adjust - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.AdjustDeveloperBalance" `  




#### `CreateDeveloper`

  * **Method** : `google.cloud.apigee.v1.Developers.CreateDeveloper`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.CreateDeveloper" `  




#### `CreditDeveloperBalance`

  * **Method** : `google.cloud.apigee.v1.Developers.CreditDeveloperBalance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerbalances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.CreditDeveloperBalance" `  




#### `DeleteDeveloper`

  * **Method** : `google.cloud.apigee.v1.Developers.DeleteDeveloper`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.DeleteDeveloper" `  




#### `DeleteDeveloperAttribute`

  * **Method** : `google.cloud.apigee.v1.Developers.DeleteDeveloperAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerattributes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.DeleteDeveloperAttribute" `  




#### `GetDeveloper`

  * **Method** : `google.cloud.apigee.v1.Developers.GetDeveloper`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.GetDeveloper" `  




#### `GetDeveloperAttribute`

  * **Method** : `google.cloud.apigee.v1.Developers.GetDeveloperAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developerattributes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.GetDeveloperAttribute" `  




#### `GetDeveloperBalance`

  * **Method** : `google.cloud.apigee.v1.Developers.GetDeveloperBalance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developerbalances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.GetDeveloperBalance" `  




#### `GetDeveloperMonetizationConfig`

  * **Method** : `google.cloud.apigee.v1.Developers.GetDeveloperMonetizationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developermonetizationconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.GetDeveloperMonetizationConfig" `  




#### `ListDeveloperAttributes`

  * **Method** : `google.cloud.apigee.v1.Developers.ListDeveloperAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developerattributes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.ListDeveloperAttributes" `  




#### `ListDevelopers`

  * **Method** : `google.cloud.apigee.v1.Developers.ListDevelopers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.developers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.ListDevelopers" `  




#### `SetDeveloperStatus`

  * **Method** : `google.cloud.apigee.v1.Developers.SetDeveloperStatus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.SetDeveloperStatus" `  




#### `UpdateDeveloper`

  * **Method** : `google.cloud.apigee.v1.Developers.UpdateDeveloper`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.UpdateDeveloper" `  




#### `UpdateDeveloperAttribute`

  * **Method** : `google.cloud.apigee.v1.Developers.UpdateDeveloperAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerattributes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.UpdateDeveloperAttribute" `  




#### `UpdateDeveloperAttributes`

  * **Method** : `google.cloud.apigee.v1.Developers.UpdateDeveloperAttributes`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developerattributes.createOrUpdateAll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.UpdateDeveloperAttributes" `  




#### `UpdateDeveloperMonetizationConfig`

  * **Method** : `google.cloud.apigee.v1.Developers.UpdateDeveloperMonetizationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.developermonetizationconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Developers.UpdateDeveloperMonetizationConfig" `  




### `google.cloud.apigee.v1.DnsZoneService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.DnsZoneService`.

#### `CreateDnsZone`

  * **Method** : `google.cloud.apigee.v1.DnsZoneService.CreateDnsZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.dnsZones.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DnsZoneService.CreateDnsZone" `  




#### `DeleteDnsZone`

  * **Method** : `google.cloud.apigee.v1.DnsZoneService.DeleteDnsZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.dnsZones.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DnsZoneService.DeleteDnsZone" `  




#### `GetDnsZone`

  * **Method** : `google.cloud.apigee.v1.DnsZoneService.GetDnsZone`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.dnsZones.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DnsZoneService.GetDnsZone" `  




#### `ListDnsZones`

  * **Method** : `google.cloud.apigee.v1.DnsZoneService.ListDnsZones`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.dnsZones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.DnsZoneService.ListDnsZones" `  




### `google.cloud.apigee.v1.EndpointAttachmentService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.EndpointAttachmentService`.

#### `CreateEndpointAttachment`

  * **Method** : `google.cloud.apigee.v1.EndpointAttachmentService.CreateEndpointAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.endpointattachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EndpointAttachmentService.CreateEndpointAttachment" `  




#### `DeleteEndpointAttachment`

  * **Method** : `google.cloud.apigee.v1.EndpointAttachmentService.DeleteEndpointAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.endpointattachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EndpointAttachmentService.DeleteEndpointAttachment" `  




#### `GetEndpointAttachment`

  * **Method** : `google.cloud.apigee.v1.EndpointAttachmentService.GetEndpointAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.endpointattachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EndpointAttachmentService.GetEndpointAttachment" `  




#### `ListEndpointAttachments`

  * **Method** : `google.cloud.apigee.v1.EndpointAttachmentService.ListEndpointAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.endpointattachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EndpointAttachmentService.ListEndpointAttachments" `  




### `google.cloud.apigee.v1.EnvironmentAddons`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.EnvironmentAddons`.

#### `GetAddonsConfig`

  * **Method** : `google.cloud.apigee.v1.EnvironmentAddons.GetAddonsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.addonsconfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentAddons.GetAddonsConfig" `  




#### `SetAddonEnablement`

  * **Method** : `google.cloud.apigee.v1.EnvironmentAddons.SetAddonEnablement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.addonsconfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentAddons.SetAddonEnablement" `  




### `google.cloud.apigee.v1.EnvironmentGroupAttachmentService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.EnvironmentGroupAttachmentService`.

#### `CreateEnvironmentGroupAttachment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupAttachmentService.CreateEnvironmentGroupAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.envgroupattachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupAttachmentService.CreateEnvironmentGroupAttachment" `  




#### `DeleteEnvironmentGroupAttachment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupAttachmentService.DeleteEnvironmentGroupAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.envgroupattachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupAttachmentService.DeleteEnvironmentGroupAttachment" `  




#### `GetEnvironmentGroupAttachment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupAttachmentService.GetEnvironmentGroupAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.envgroupattachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupAttachmentService.GetEnvironmentGroupAttachment" `  




#### `ListEnvironmentGroupAttachments`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupAttachmentService.ListEnvironmentGroupAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.envgroupattachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupAttachmentService.ListEnvironmentGroupAttachments" `  




### `google.cloud.apigee.v1.EnvironmentGroupService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.EnvironmentGroupService`.

#### `CreateEnvironmentGroup`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupService.CreateEnvironmentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.envgroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupService.CreateEnvironmentGroup" `  




#### `DeleteEnvironmentGroup`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupService.DeleteEnvironmentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.envgroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupService.DeleteEnvironmentGroup" `  




#### `GetEnvironmentGroup`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupService.GetEnvironmentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.envgroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupService.GetEnvironmentGroup" `  




#### `ListEnvironmentGroups`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupService.ListEnvironmentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.envgroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupService.ListEnvironmentGroups" `  




#### `UpdateEnvironmentGroup`

  * **Method** : `google.cloud.apigee.v1.EnvironmentGroupService.UpdateEnvironmentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.envgroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentGroupService.UpdateEnvironmentGroup" `  




### `google.cloud.apigee.v1.EnvironmentService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.EnvironmentService`.

#### `CreateEnvironment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.CreateEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.environments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.CreateEnvironment" `  




#### `DeleteEnvironment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.DeleteEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.environments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.DeleteEnvironment" `  




#### `GetApiSecurityRuntimeConfig`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.GetApiSecurityRuntimeConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.GetApiSecurityRuntimeConfig" `  




#### `GetDeployedConfig`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.GetDeployedConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.GetDeployedConfig" `  




#### `GetEnvironment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.GetEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.GetEnvironment" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.GetIamPolicy" `  




#### `ListEnvironments`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.ListEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.environments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.ListEnvironments" `  




#### `ModifyEnvironment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.ModifyEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.ModifyEnvironment" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.environments.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.SetIamPolicy" `  




#### `Subscribe`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.Subscribe`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.environments.manageRuntime - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.Subscribe" `  




#### `Unsubscribe`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.Unsubscribe`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.environments.manageRuntime - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.Unsubscribe" `  




#### `UpdateEnvironment`

  * **Method** : `google.cloud.apigee.v1.EnvironmentService.UpdateEnvironment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.environments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.EnvironmentService.UpdateEnvironment" `  




### `google.cloud.apigee.v1.InstanceAttachmentService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.InstanceAttachmentService`.

#### `CreateInstanceAttachment`

  * **Method** : `google.cloud.apigee.v1.InstanceAttachmentService.CreateInstanceAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.instanceattachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceAttachmentService.CreateInstanceAttachment" `  




#### `DeleteInstanceAttachment`

  * **Method** : `google.cloud.apigee.v1.InstanceAttachmentService.DeleteInstanceAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.instanceattachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceAttachmentService.DeleteInstanceAttachment" `  




#### `GetInstanceAttachment`

  * **Method** : `google.cloud.apigee.v1.InstanceAttachmentService.GetInstanceAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.instanceattachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceAttachmentService.GetInstanceAttachment" `  




#### `ListInstanceAttachments`

  * **Method** : `google.cloud.apigee.v1.InstanceAttachmentService.ListInstanceAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.instanceattachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceAttachmentService.ListInstanceAttachments" `  




### `google.cloud.apigee.v1.InstanceService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.InstanceService`.

#### `CreateInstance`

  * **Method** : `google.cloud.apigee.v1.InstanceService.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceService.CreateInstance" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.apigee.v1.InstanceService.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceService.DeleteInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.apigee.v1.InstanceService.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceService.GetInstance" `  




#### `ListInstances`

  * **Method** : `google.cloud.apigee.v1.InstanceService.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceService.ListInstances" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.apigee.v1.InstanceService.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.InstanceService.UpdateInstance" `  




### `google.cloud.apigee.v1.KeyValueMapService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.KeyValueMapService`.

#### `CreateApiProxyKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.CreateApiProxyKeyValueMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.CreateApiProxyKeyValueMap" `  




#### `CreateEnvironmentKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.CreateEnvironmentKeyValueMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.CreateEnvironmentKeyValueMap" `  




#### `CreateKeyValueEntry`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.CreateKeyValueEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemapentries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.CreateKeyValueEntry" `  




#### `CreateOrganizationKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.CreateOrganizationKeyValueMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.CreateOrganizationKeyValueMap" `  




#### `DeleteApiProxyKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.DeleteApiProxyKeyValueMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.DeleteApiProxyKeyValueMap" `  




#### `DeleteEnvironmentKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.DeleteEnvironmentKeyValueMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.DeleteEnvironmentKeyValueMap" `  




#### `DeleteKeyValueEntry`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.DeleteKeyValueEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemapentries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.DeleteKeyValueEntry" `  




#### `DeleteOrganizationKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.DeleteOrganizationKeyValueMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.DeleteOrganizationKeyValueMap" `  




#### `GetKeyValueEntry`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.GetKeyValueEntry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keyvaluemapentries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.GetKeyValueEntry" `  




#### `GetKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.GetKeyValueMap`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.GetKeyValueMap" `  




#### `ListApiProxyKeyValueMaps`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.ListApiProxyKeyValueMaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.ListApiProxyKeyValueMaps" `  




#### `ListEnvironmentKeyValueMaps`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.ListEnvironmentKeyValueMaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.ListEnvironmentKeyValueMaps" `  




#### `ListKeyValueEntries`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.ListKeyValueEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keyvaluemapentries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.ListKeyValueEntries" `  




#### `ListOrganizationKeyValueMaps`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.ListOrganizationKeyValueMaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.ListOrganizationKeyValueMaps" `  




#### `UpdateKeyValueEntry`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.UpdateKeyValueEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemapentries.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.UpdateKeyValueEntry" `  




#### `UpdateKeyValueMap`

  * **Method** : `google.cloud.apigee.v1.KeyValueMapService.UpdateKeyValueMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keyvaluemaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeyValueMapService.UpdateKeyValueMap" `  




### `google.cloud.apigee.v1.KeystoreService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.KeystoreService`.

#### `CreateAlias`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.CreateAlias`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystorealiases.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.CreateAlias" `  




#### `CreateKeystore`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.CreateKeystore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keystores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.CreateKeystore" `  




#### `DeleteAlias`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.DeleteAlias`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystorealiases.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.DeleteAlias" `  




#### `DeleteKeystore`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.DeleteKeystore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.keystores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.DeleteKeystore" `  




#### `GenerateCsr`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.GenerateCsr`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystorealiases.generateCSR - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.GenerateCsr" `  




#### `GetAlias`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.GetAlias`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystorealiases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.GetAlias" `  




#### `GetCertificateFromAlias`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.GetCertificateFromAlias`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystorealiases.exportCertificate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.GetCertificateFromAlias" `  




#### `GetKeystore`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.GetKeystore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.GetKeystore" `  




#### `ListAliases`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.ListAliases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystorealiases.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.ListAliases" `  




#### `ListKeystores`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.ListKeystores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.ListKeystores" `  




#### `UpdateAlias`

  * **Method** : `google.cloud.apigee.v1.KeystoreService.UpdateAlias`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.keystorealiases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.KeystoreService.UpdateAlias" `  




### `google.cloud.apigee.v1.MenuItems`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.MenuItems`.

#### `CreateMenuItem`

  * **Method** : `google.cloud.apigee.v1.MenuItems.CreateMenuItem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuItems.CreateMenuItem" `  




#### `DeleteMenuItem`

  * **Method** : `google.cloud.apigee.v1.MenuItems.DeleteMenuItem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuItems.DeleteMenuItem" `  




#### `ListMenuItems`

  * **Method** : `google.cloud.apigee.v1.MenuItems.ListMenuItems`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuItems.ListMenuItems" `  




#### `PublishMenuItem`

  * **Method** : `google.cloud.apigee.v1.MenuItems.PublishMenuItem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuItems.PublishMenuItem" `  




#### `ToggleNested`

  * **Method** : `google.cloud.apigee.v1.MenuItems.ToggleNested`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuItems.ToggleNested" `  




#### `UpdateMenuItem`

  * **Method** : `google.cloud.apigee.v1.MenuItems.UpdateMenuItem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuItems.UpdateMenuItem" `  




#### `UpdatePriorities`

  * **Method** : `google.cloud.apigee.v1.MenuItems.UpdatePriorities`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuItems.UpdatePriorities" `  




### `google.cloud.apigee.v1.MenuTypes`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.MenuTypes`.

#### `ListMenuTypes`

  * **Method** : `google.cloud.apigee.v1.MenuTypes.ListMenuTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuTypes.ListMenuTypes" `  




#### `ListMenuTypesByPage`

  * **Method** : `google.cloud.apigee.v1.MenuTypes.ListMenuTypesByPage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.MenuTypes.ListMenuTypesByPage" `  




### `google.cloud.apigee.v1.NatAddressService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.NatAddressService`.

#### `ActivateNatAddress`

  * **Method** : `google.cloud.apigee.v1.NatAddressService.ActivateNatAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.nataddresses.activate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.NatAddressService.ActivateNatAddress" `  




#### `CreateNatAddress`

  * **Method** : `google.cloud.apigee.v1.NatAddressService.CreateNatAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.nataddresses.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.NatAddressService.CreateNatAddress" `  




#### `DeleteNatAddress`

  * **Method** : `google.cloud.apigee.v1.NatAddressService.DeleteNatAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.nataddresses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.NatAddressService.DeleteNatAddress" `  




#### `GetNatAddress`

  * **Method** : `google.cloud.apigee.v1.NatAddressService.GetNatAddress`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.nataddresses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.NatAddressService.GetNatAddress" `  




#### `ListNatAddresses`

  * **Method** : `google.cloud.apigee.v1.NatAddressService.ListNatAddresses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.nataddresses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.NatAddressService.ListNatAddresses" `  




### `google.cloud.apigee.v1.OrganizationService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.OrganizationService`.

#### `CreateOrganization`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.CreateOrganization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.organizations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.CreateOrganization" `  




#### `DeleteOrganization`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.DeleteOrganization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.organizations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.DeleteOrganization" `  




#### `GetControlPlaneAccess`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.GetControlPlaneAccess`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.organizations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.GetControlPlaneAccess" `  




#### `GetOrganization`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.GetOrganization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.organizations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.GetOrganization" `  




#### `GetProjectMapping`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.GetProjectMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.organizations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.GetProjectMapping" `  




#### `GetSyncAuthorization`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.GetSyncAuthorization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.organizations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.GetSyncAuthorization" `  




#### `SetAddons`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.SetAddons`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.organizations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.SetAddons" `  




#### `SetSyncAuthorization`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.SetSyncAuthorization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.organizations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.SetSyncAuthorization" `  




#### `UpdateControlPlaneAccess`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.UpdateControlPlaneAccess`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.organizations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.UpdateControlPlaneAccess" `  




#### `UpdateOrganization`

  * **Method** : `google.cloud.apigee.v1.OrganizationService.UpdateOrganization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.organizations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.OrganizationService.UpdateOrganization" `  




### `google.cloud.apigee.v1.Pages`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Pages`.

#### `CreatePage`

  * **Method** : `google.cloud.apigee.v1.Pages.CreatePage`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.CreatePage" `  




#### `DeletePage`

  * **Method** : `google.cloud.apigee.v1.Pages.DeletePage`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.DeletePage" `  




#### `GetPage`

  * **Method** : `google.cloud.apigee.v1.Pages.GetPage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.GetPage" `  




#### `ListPages`

  * **Method** : `google.cloud.apigee.v1.Pages.ListPages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.ListPages" `  




#### `PublishPage`

  * **Method** : `google.cloud.apigee.v1.Pages.PublishPage`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.PublishPage" `  




#### `SetPageContent`

  * **Method** : `google.cloud.apigee.v1.Pages.SetPageContent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.SetPageContent" `  




#### `UnpublishPage`

  * **Method** : `google.cloud.apigee.v1.Pages.UnpublishPage`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.UnpublishPage" `  




#### `UpdatePage`

  * **Method** : `google.cloud.apigee.v1.Pages.UpdatePage`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Pages.UpdatePage" `  




### `google.cloud.apigee.v1.ProjectService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ProjectService`.

#### `ProvisionOrganization`

  * **Method** : `google.cloud.apigee.v1.ProjectService.ProvisionOrganization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.projects.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ProjectService.ProvisionOrganization" `  




### `google.cloud.apigee.v1.RatePlans`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.RatePlans`.

#### `CreateRatePlan`

  * **Method** : `google.cloud.apigee.v1.RatePlans.CreateRatePlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.rateplans.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RatePlans.CreateRatePlan" `  




#### `DeleteRatePlan`

  * **Method** : `google.cloud.apigee.v1.RatePlans.DeleteRatePlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.rateplans.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RatePlans.DeleteRatePlan" `  




#### `GetRatePlan`

  * **Method** : `google.cloud.apigee.v1.RatePlans.GetRatePlan`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.rateplans.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RatePlans.GetRatePlan" `  




#### `ListRatePlans`

  * **Method** : `google.cloud.apigee.v1.RatePlans.ListRatePlans`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.rateplans.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RatePlans.ListRatePlans" `  




#### `UpdateRatePlan`

  * **Method** : `google.cloud.apigee.v1.RatePlans.UpdateRatePlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.rateplans.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RatePlans.UpdateRatePlan" `  




### `google.cloud.apigee.v1.ReferenceService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ReferenceService`.

#### `CreateReference`

  * **Method** : `google.cloud.apigee.v1.ReferenceService.CreateReference`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.references.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ReferenceService.CreateReference" `  




#### `DeleteReference`

  * **Method** : `google.cloud.apigee.v1.ReferenceService.DeleteReference`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.references.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ReferenceService.DeleteReference" `  




#### `GetReference`

  * **Method** : `google.cloud.apigee.v1.ReferenceService.GetReference`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.references.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ReferenceService.GetReference" `  




#### `ListReferences`

  * **Method** : `google.cloud.apigee.v1.ReferenceService.ListReferences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.references.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ReferenceService.ListReferences" `  




#### `UpdateReference`

  * **Method** : `google.cloud.apigee.v1.ReferenceService.UpdateReference`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.references.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ReferenceService.UpdateReference" `  




### `google.cloud.apigee.v1.ResourceEntitlements`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ResourceEntitlements`.

#### `GetDefaultResourceEntitlements`

  * **Method** : `google.cloud.apigee.v1.ResourceEntitlements.GetDefaultResourceEntitlements`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceEntitlements.GetDefaultResourceEntitlements" `  




#### `GetResourceEntitlement`

  * **Method** : `google.cloud.apigee.v1.ResourceEntitlements.GetResourceEntitlement`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceEntitlements.GetResourceEntitlement" `  




#### `UpdateDefaultResourceEntitlement`

  * **Method** : `google.cloud.apigee.v1.ResourceEntitlements.UpdateDefaultResourceEntitlement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceEntitlements.UpdateDefaultResourceEntitlement" `  




#### `UpdateResourceEntitlement`

  * **Method** : `google.cloud.apigee.v1.ResourceEntitlements.UpdateResourceEntitlement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceEntitlements.UpdateResourceEntitlement" `  




### `google.cloud.apigee.v1.ResourceFileService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.ResourceFileService`.

#### `CreateEnvironmentResource`

  * **Method** : `google.cloud.apigee.v1.ResourceFileService.CreateEnvironmentResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.resourcefiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceFileService.CreateEnvironmentResource" `  




#### `DeleteEnvironmentResource`

  * **Method** : `google.cloud.apigee.v1.ResourceFileService.DeleteEnvironmentResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.resourcefiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceFileService.DeleteEnvironmentResource" `  




#### `GetEnvironmentResource`

  * **Method** : `google.cloud.apigee.v1.ResourceFileService.GetEnvironmentResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.resourcefiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceFileService.GetEnvironmentResource" `  




#### `ListEnvironmentResources`

  * **Method** : `google.cloud.apigee.v1.ResourceFileService.ListEnvironmentResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.resourcefiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceFileService.ListEnvironmentResources" `  




#### `UpdateEnvironmentResource`

  * **Method** : `google.cloud.apigee.v1.ResourceFileService.UpdateEnvironmentResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.resourcefiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.ResourceFileService.UpdateEnvironmentResource" `  




### `google.cloud.apigee.v1.Resources`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Resources`.

#### `GetConsumerResourceTypes`

  * **Method** : `google.cloud.apigee.v1.Resources.GetConsumerResourceTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Resources.GetConsumerResourceTypes" `  




#### `QueryApiDocs`

  * **Method** : `google.cloud.apigee.v1.Resources.QueryApiDocs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Resources.QueryApiDocs" `  




#### `QueryPages`

  * **Method** : `google.cloud.apigee.v1.Resources.QueryPages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Resources.QueryPages" `  




### `google.cloud.apigee.v1.RuntimeService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.RuntimeService`.

#### `CreateCanaryEvaluation`

  * **Method** : `google.cloud.apigee.v1.RuntimeService.CreateCanaryEvaluation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.canaryevaluations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RuntimeService.CreateCanaryEvaluation" `  




#### `GetCanaryEvaluation`

  * **Method** : `google.cloud.apigee.v1.RuntimeService.GetCanaryEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.canaryevaluations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RuntimeService.GetCanaryEvaluation" `  




#### `GetDeployedIngressConfig`

  * **Method** : `google.cloud.apigee.v1.RuntimeService.GetDeployedIngressConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.ingressconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RuntimeService.GetDeployedIngressConfig" `  




#### `GetEnvGroupDeployedIngressConfig`

  * **Method** : `google.cloud.apigee.v1.RuntimeService.GetEnvGroupDeployedIngressConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.ingressconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RuntimeService.GetEnvGroupDeployedIngressConfig" `  




#### `GetMcpServerConfig`

  * **Method** : `google.cloud.apigee.v1.RuntimeService.GetMcpServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.runtimeconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RuntimeService.GetMcpServerConfig" `  




#### `GetRuntimeConfig`

  * **Method** : `google.cloud.apigee.v1.RuntimeService.GetRuntimeConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.runtimeconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RuntimeService.GetRuntimeConfig" `  




#### `ReportInstanceStatus`

  * **Method** : `google.cloud.apigee.v1.RuntimeService.ReportInstanceStatus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.instances.reportStatus - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.RuntimeService.ReportInstanceStatus" `  




### `google.cloud.apigee.v1.SecurityActionService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecurityActionService`.

#### `CreateSecurityAction`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.CreateSecurityAction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityActions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.CreateSecurityAction" `  




#### `DeleteSecurityAction`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.DeleteSecurityAction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityActions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.DeleteSecurityAction" `  




#### `DisableSecurityAction`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.DisableSecurityAction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityActions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.DisableSecurityAction" `  




#### `EnableSecurityAction`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.EnableSecurityAction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityActions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.EnableSecurityAction" `  




#### `GetSecurityAction`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.GetSecurityAction`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityActions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.GetSecurityAction" `  




#### `GetSecurityActionsConfig`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.GetSecurityActionsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityActionsConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.GetSecurityActionsConfig" `  




#### `ListSecurityActions`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.ListSecurityActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityActions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.ListSecurityActions" `  




#### `UpdateSecurityAction`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.UpdateSecurityAction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityActions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.UpdateSecurityAction" `  




#### `UpdateSecurityActionsConfig`

  * **Method** : `google.cloud.apigee.v1.SecurityActionService.UpdateSecurityActionsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityActionsConfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityActionService.UpdateSecurityActionsConfig" `  




### `google.cloud.apigee.v1.SecurityFeedbackService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecurityFeedbackService`.

#### `CreateSecurityFeedback`

  * **Method** : `google.cloud.apigee.v1.SecurityFeedbackService.CreateSecurityFeedback`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityFeedback.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityFeedbackService.CreateSecurityFeedback" `  




#### `DeleteSecurityFeedback`

  * **Method** : `google.cloud.apigee.v1.SecurityFeedbackService.DeleteSecurityFeedback`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityFeedback.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityFeedbackService.DeleteSecurityFeedback" `  




#### `GetSecurityFeedback`

  * **Method** : `google.cloud.apigee.v1.SecurityFeedbackService.GetSecurityFeedback`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityFeedback.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityFeedbackService.GetSecurityFeedback" `  




#### `ListSecurityFeedback`

  * **Method** : `google.cloud.apigee.v1.SecurityFeedbackService.ListSecurityFeedback`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityFeedback.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityFeedbackService.ListSecurityFeedback" `  




#### `UpdateSecurityFeedback`

  * **Method** : `google.cloud.apigee.v1.SecurityFeedbackService.UpdateSecurityFeedback`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityFeedback.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityFeedbackService.UpdateSecurityFeedback" `  




### `google.cloud.apigee.v1.SecurityIncidentService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecurityIncidentService`.

#### `BatchUpdateSecurityIncidents`

  * **Method** : `google.cloud.apigee.v1.SecurityIncidentService.BatchUpdateSecurityIncidents`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityIncidents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityIncidentService.BatchUpdateSecurityIncidents" `  




#### `GetSecurityIncident`

  * **Method** : `google.cloud.apigee.v1.SecurityIncidentService.GetSecurityIncident`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityIncidents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityIncidentService.GetSecurityIncident" `  




#### `ListSecurityIncidents`

  * **Method** : `google.cloud.apigee.v1.SecurityIncidentService.ListSecurityIncidents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityIncidents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityIncidentService.ListSecurityIncidents" `  




#### `UpdateSecurityIncident`

  * **Method** : `google.cloud.apigee.v1.SecurityIncidentService.UpdateSecurityIncident`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityIncidents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityIncidentService.UpdateSecurityIncident" `  




### `google.cloud.apigee.v1.SecurityProfileService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecurityProfileService`.

#### `ComputeEnvironmentScores`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.ComputeEnvironmentScores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityProfileEnvironments.computeScore - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.ComputeEnvironmentScores" `  




#### `CreateSecurityProfile`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.CreateSecurityProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.CreateSecurityProfile" `  




#### `CreateSecurityProfileEnvironmentAssociation`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.CreateSecurityProfileEnvironmentAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfileEnvironments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.CreateSecurityProfileEnvironmentAssociation" `  




#### `DeleteSecurityProfile`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.DeleteSecurityProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.DeleteSecurityProfile" `  




#### `DeleteSecurityProfileEnvironmentAssociation`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.DeleteSecurityProfileEnvironmentAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfileEnvironments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.DeleteSecurityProfileEnvironmentAssociation" `  




#### `GetSecurityProfile`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.GetSecurityProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.GetSecurityProfile" `  




#### `ListSecurityProfileRevisions`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.ListSecurityProfileRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.ListSecurityProfileRevisions" `  




#### `ListSecurityProfiles`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.ListSecurityProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.ListSecurityProfiles" `  




#### `UpdateSecurityProfile`

  * **Method** : `google.cloud.apigee.v1.SecurityProfileService.UpdateSecurityProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityProfileService.UpdateSecurityProfile" `  




### `google.cloud.apigee.v1.SecurityReportService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecurityReportService`.

#### `CreateHostSecurityReport`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.CreateHostSecurityReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.hostsecurityreports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.CreateHostSecurityReport" `  




#### `CreateSecurityReport`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.CreateSecurityReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityreports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.CreateSecurityReport" `  




#### `GetHostSecurityReport`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostsecurityreports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReport" `  




#### `GetHostSecurityReportResult`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReportResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostsecurityreports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReportResult" `  




#### `GetHostSecurityReportResultView`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReportResultView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostsecurityreports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.GetHostSecurityReportResultView" `  




#### `GetSecurityReport`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.GetSecurityReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityreports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.GetSecurityReport" `  




#### `GetSecurityReportResult`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.GetSecurityReportResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityreports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.GetSecurityReportResult" `  




#### `GetSecurityReportResultView`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.GetSecurityReportResultView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityreports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.GetSecurityReportResultView" `  




#### `ListHostSecurityReports`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.ListHostSecurityReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.hostsecurityreports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.ListHostSecurityReports" `  




#### `ListSecurityReports`

  * **Method** : `google.cloud.apigee.v1.SecurityReportService.ListSecurityReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityreports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityReportService.ListSecurityReports" `  




### `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service`.

#### `BatchComputeSecurityAssessmentResults`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.BatchComputeSecurityAssessmentResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityAssessmentResults.compute - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.BatchComputeSecurityAssessmentResults" `  




#### `CreateSecurityMonitoringCondition`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.CreateSecurityMonitoringCondition`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityMonitoringConditions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.CreateSecurityMonitoringCondition" `  




#### `CreateSecurityProfileV2`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.CreateSecurityProfileV2`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfilesV2.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.CreateSecurityProfileV2" `  




#### `DeleteSecurityMonitoringCondition`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.DeleteSecurityMonitoringCondition`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityMonitoringConditions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.DeleteSecurityMonitoringCondition" `  




#### `DeleteSecurityProfileV2`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.DeleteSecurityProfileV2`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfilesV2.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.DeleteSecurityProfileV2" `  




#### `GetSecurityMonitoringCondition`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.GetSecurityMonitoringCondition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityMonitoringConditions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.GetSecurityMonitoringCondition" `  




#### `GetSecurityProfileV2`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.GetSecurityProfileV2`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityProfilesV2.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.GetSecurityProfileV2" `  




#### `ListSecurityMonitoringConditions`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.ListSecurityMonitoringConditions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityMonitoringConditions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.ListSecurityMonitoringConditions" `  




#### `ListSecurityProfilesV2`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.ListSecurityProfilesV2`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityProfilesV2.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.ListSecurityProfilesV2" `  




#### `UpdateSecurityMonitoringCondition`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.UpdateSecurityMonitoringCondition`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityMonitoringConditions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.UpdateSecurityMonitoringCondition" `  




#### `UpdateSecurityProfileV2`

  * **Method** : `google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.UpdateSecurityProfileV2`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securityProfilesV2.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityRiskAssessmentV2Service.UpdateSecurityProfileV2" `  




### `google.cloud.apigee.v1.SecuritySettingsService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecuritySettingsService`.

#### `GetSecuritySettings`

  * **Method** : `google.cloud.apigee.v1.SecuritySettingsService.GetSecuritySettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securitySettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecuritySettingsService.GetSecuritySettings" `  




#### `UpdateSecuritySettings`

  * **Method** : `google.cloud.apigee.v1.SecuritySettingsService.UpdateSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.securitySettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecuritySettingsService.UpdateSecuritySettings" `  




### `google.cloud.apigee.v1.SecurityStatsService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SecurityStatsService`.

#### `QueryTabularStats`

  * **Method** : `google.cloud.apigee.v1.SecurityStatsService.QueryTabularStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityStats.queryTabularStats - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityStatsService.QueryTabularStats" `  




#### `QueryTimeSeriesStats`

  * **Method** : `google.cloud.apigee.v1.SecurityStatsService.QueryTimeSeriesStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.securityStats.queryTimeSeriesStats - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SecurityStatsService.QueryTimeSeriesStats" `  




### `google.cloud.apigee.v1.SharedFlowService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SharedFlowService`.

#### `CreateSharedFlowRevision`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.CreateSharedFlowRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.sharedflows.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.CreateSharedFlowRevision" `  




#### `DeleteSharedFlow`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.DeleteSharedFlow`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.sharedflows.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.DeleteSharedFlow" `  




#### `DeleteSharedFlowRevision`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.DeleteSharedFlowRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.sharedflowrevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.DeleteSharedFlowRevision" `  




#### `GetSharedFlow`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.GetSharedFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.sharedflows.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.GetSharedFlow" `  




#### `GetSharedFlowRevision`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.GetSharedFlowRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.sharedflowrevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.GetSharedFlowRevision" `  




#### `ListSharedFlowRevisions`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.ListSharedFlowRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.sharedflowrevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.ListSharedFlowRevisions" `  




#### `ListSharedFlows`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.ListSharedFlows`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.sharedflows.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.ListSharedFlows" `  




#### `MoveSharedFlow`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.MoveSharedFlow`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.sharedflows.create - ADMIN_WRITE`
    * `apigee.sharedflows.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.MoveSharedFlow" `  




#### `UpdateSharedFlowRevision`

  * **Method** : `google.cloud.apigee.v1.SharedFlowService.UpdateSharedFlowRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.sharedflowrevisions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SharedFlowService.UpdateSharedFlowRevision" `  




### `google.cloud.apigee.v1.SiteDomain`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SiteDomain`.

#### `DisableCustomDomain`

  * **Method** : `google.cloud.apigee.v1.SiteDomain.DisableCustomDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteDomain.DisableCustomDomain" `  




#### `EnableCustomDomain`

  * **Method** : `google.cloud.apigee.v1.SiteDomain.EnableCustomDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteDomain.EnableCustomDomain" `  




#### `GetCustomDomainConfig`

  * **Method** : `google.cloud.apigee.v1.SiteDomain.GetCustomDomainConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteDomain.GetCustomDomainConfig" `  




### `google.cloud.apigee.v1.SiteEmail`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SiteEmail`.

#### `GetEmailTemplate`

  * **Method** : `google.cloud.apigee.v1.SiteEmail.GetEmailTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteEmail.GetEmailTemplate" `  




#### `UpdateEmailTemplate`

  * **Method** : `google.cloud.apigee.v1.SiteEmail.UpdateEmailTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteEmail.UpdateEmailTemplate" `  




### `google.cloud.apigee.v1.SiteFile`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SiteFile`.

#### `DeleteFile`

  * **Method** : `google.cloud.apigee.v1.SiteFile.DeleteFile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteFile.DeleteFile" `  




#### `ListFiles`

  * **Method** : `google.cloud.apigee.v1.SiteFile.ListFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteFile.ListFiles" `  




#### `UploadFile`

  * **Method** : `google.cloud.apigee.v1.SiteFile.UploadFile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteFile.UploadFile" `  




### `google.cloud.apigee.v1.SiteOperation`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SiteOperation`.

#### `GetContentSecurityPolicy`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.GetContentSecurityPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.GetContentSecurityPolicy" `  




#### `GetDefaultAnonAllowed`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.GetDefaultAnonAllowed`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.GetDefaultAnonAllowed" `  




#### `GetDraftToken`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.GetDraftToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.GetDraftToken" `  




#### `GetOrgType`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.GetOrgType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.GetOrgType" `  




#### `RegenerateSecretKey`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.RegenerateSecretKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.RegenerateSecretKey" `  




#### `ResetSmtp`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.ResetSmtp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.ResetSmtp" `  




#### `SendTestEmail`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.SendTestEmail`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.SendTestEmail" `  




#### `SetApprovedEmails`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.SetApprovedEmails`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.SetApprovedEmails" `  




#### `SetDefaultAnonAllowed`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.SetDefaultAnonAllowed`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.SetDefaultAnonAllowed" `  




#### `TrashSite`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.TrashSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.TrashSite" `  




#### `UpdateAnalyticsScript`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.UpdateAnalyticsScript`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.UpdateAnalyticsScript" `  




#### `UpdateContentSecurityPolicy`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.UpdateContentSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.UpdateContentSecurityPolicy" `  




#### `VerifyDraftToken`

  * **Method** : `google.cloud.apigee.v1.SiteOperation.VerifyDraftToken`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SiteOperation.VerifyDraftToken" `  




### `google.cloud.apigee.v1.Sites`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Sites`.

#### `CloneSite`

  * **Method** : `google.cloud.apigee.v1.Sites.CloneSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.CloneSite" `  




#### `CreateSite`

  * **Method** : `google.cloud.apigee.v1.Sites.CreateSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.CreateSite" `  




#### `GetAllInOrgOrSingleWithDomain`

  * **Method** : `google.cloud.apigee.v1.Sites.GetAllInOrgOrSingleWithDomain`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.GetAllInOrgOrSingleWithDomain" `  




#### `GetKeystores`

  * **Method** : `google.cloud.apigee.v1.Sites.GetKeystores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.GetKeystores" `  




#### `GetPublishedApis`

  * **Method** : `google.cloud.apigee.v1.Sites.GetPublishedApis`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.GetPublishedApis" `  




#### `GetSite`

  * **Method** : `google.cloud.apigee.v1.Sites.GetSite`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.GetSite" `  




#### `GetSmtp`

  * **Method** : `google.cloud.apigee.v1.Sites.GetSmtp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.GetSmtp" `  




#### `ListProxySpecs`

  * **Method** : `google.cloud.apigee.v1.Sites.ListProxySpecs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.ListProxySpecs" `  




#### `Render`

  * **Method** : `google.cloud.apigee.v1.Sites.Render`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.Render" `  




#### `UpdateSite`

  * **Method** : `google.cloud.apigee.v1.Sites.UpdateSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.UpdateSite" `  




#### `UpdateSmtp`

  * **Method** : `google.cloud.apigee.v1.Sites.UpdateSmtp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Sites.UpdateSmtp" `  




### `google.cloud.apigee.v1.SpaceService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.SpaceService`.

#### `CreateSpace`

  * **Method** : `google.cloud.apigee.v1.SpaceService.CreateSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.spaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SpaceService.CreateSpace" `  




#### `DeleteSpace`

  * **Method** : `google.cloud.apigee.v1.SpaceService.DeleteSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.spaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SpaceService.DeleteSpace" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.apigee.v1.SpaceService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.spaces.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SpaceService.GetIamPolicy" `  




#### `GetSpace`

  * **Method** : `google.cloud.apigee.v1.SpaceService.GetSpace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.spaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SpaceService.GetSpace" `  




#### `ListSpaces`

  * **Method** : `google.cloud.apigee.v1.SpaceService.ListSpaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.spaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SpaceService.ListSpaces" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.apigee.v1.SpaceService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.spaces.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SpaceService.SetIamPolicy" `  




#### `UpdateSpace`

  * **Method** : `google.cloud.apigee.v1.SpaceService.UpdateSpace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.spaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.SpaceService.UpdateSpace" `  




### `google.cloud.apigee.v1.System`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.System`.

#### `GetAnnouncement`

  * **Method** : `google.cloud.apigee.v1.System.GetAnnouncement`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.System.GetAnnouncement" `  




#### `GetConfig`

  * **Method** : `google.cloud.apigee.v1.System.GetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.System.GetConfig" `  




#### `GetServerStatus`

  * **Method** : `google.cloud.apigee.v1.System.GetServerStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.System.GetServerStatus" `  




#### `GetSystemState`

  * **Method** : `google.cloud.apigee.v1.System.GetSystemState`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.System.GetSystemState" `  




### `google.cloud.apigee.v1.TargetServerService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.TargetServerService`.

#### `CreateTargetServer`

  * **Method** : `google.cloud.apigee.v1.TargetServerService.CreateTargetServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.targetservers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TargetServerService.CreateTargetServer" `  




#### `DeleteTargetServer`

  * **Method** : `google.cloud.apigee.v1.TargetServerService.DeleteTargetServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.targetservers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TargetServerService.DeleteTargetServer" `  




#### `GetTargetServer`

  * **Method** : `google.cloud.apigee.v1.TargetServerService.GetTargetServer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.targetservers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TargetServerService.GetTargetServer" `  




#### `ListTargetServers`

  * **Method** : `google.cloud.apigee.v1.TargetServerService.ListTargetServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.targetservers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TargetServerService.ListTargetServers" `  




#### `UpdateTargetServer`

  * **Method** : `google.cloud.apigee.v1.TargetServerService.UpdateTargetServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.targetservers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TargetServerService.UpdateTargetServer" `  




### `google.cloud.apigee.v1.TraceConfigOverrideService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.TraceConfigOverrideService`.

#### `CreateTraceConfigOverride`

  * **Method** : `google.cloud.apigee.v1.TraceConfigOverrideService.CreateTraceConfigOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.traceconfigoverrides.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TraceConfigOverrideService.CreateTraceConfigOverride" `  




#### `DeleteTraceConfigOverride`

  * **Method** : `google.cloud.apigee.v1.TraceConfigOverrideService.DeleteTraceConfigOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.traceconfigoverrides.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TraceConfigOverrideService.DeleteTraceConfigOverride" `  




#### `GetTraceConfigOverride`

  * **Method** : `google.cloud.apigee.v1.TraceConfigOverrideService.GetTraceConfigOverride`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.traceconfigoverrides.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TraceConfigOverrideService.GetTraceConfigOverride" `  




#### `ListTraceConfigOverrides`

  * **Method** : `google.cloud.apigee.v1.TraceConfigOverrideService.ListTraceConfigOverrides`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.traceconfigoverrides.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TraceConfigOverrideService.ListTraceConfigOverrides" `  




#### `UpdateTraceConfigOverride`

  * **Method** : `google.cloud.apigee.v1.TraceConfigOverrideService.UpdateTraceConfigOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.traceconfigoverrides.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TraceConfigOverrideService.UpdateTraceConfigOverride" `  




### `google.cloud.apigee.v1.TraceConfigService`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.TraceConfigService`.

#### `GetTraceConfig`

  * **Method** : `google.cloud.apigee.v1.TraceConfigService.GetTraceConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.traceconfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TraceConfigService.GetTraceConfig" `  




#### `UpdateTraceConfig`

  * **Method** : `google.cloud.apigee.v1.TraceConfigService.UpdateTraceConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.traceconfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.TraceConfigService.UpdateTraceConfig" `  




### `google.cloud.apigee.v1.Zones`

The following audit logs are associated with methods belonging to `google.cloud.apigee.v1.Zones`.

#### `AssociateSiteZone`

  * **Method** : `google.cloud.apigee.v1.Zones.AssociateSiteZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.AssociateSiteZone" `  




#### `CreateIdentityProvider`

  * **Method** : `google.cloud.apigee.v1.Zones.CreateIdentityProvider`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.CreateIdentityProvider" `  




#### `EnableZoneAudience`

  * **Method** : `google.cloud.apigee.v1.Zones.EnableZoneAudience`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.EnableZoneAudience" `  




#### `GetAudiencesEnabled`

  * **Method** : `google.cloud.apigee.v1.Zones.GetAudiencesEnabled`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.GetAudiencesEnabled" `  




#### `GetIdentityProvider`

  * **Method** : `google.cloud.apigee.v1.Zones.GetIdentityProvider`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.GetIdentityProvider" `  




#### `GetZone`

  * **Method** : `google.cloud.apigee.v1.Zones.GetZone`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.GetZone" `  




#### `GetZoneAudiencesEnabledForZone`

  * **Method** : `google.cloud.apigee.v1.Zones.GetZoneAudiencesEnabledForZone`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.GetZoneAudiencesEnabledForZone" `  




#### `ListAudiencesEnabledForZonesInOrg`

  * **Method** : `google.cloud.apigee.v1.Zones.ListAudiencesEnabledForZonesInOrg`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.ListAudiencesEnabledForZonesInOrg" `  




#### `ListIdentityProviders`

  * **Method** : `google.cloud.apigee.v1.Zones.ListIdentityProviders`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.ListIdentityProviders" `  




#### `ListZones`

  * **Method** : `google.cloud.apigee.v1.Zones.ListZones`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.portals.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.ListZones" `  




#### `UpdateIdentityProvider`

  * **Method** : `google.cloud.apigee.v1.Zones.UpdateIdentityProvider`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.UpdateIdentityProvider" `  




#### `UpdateIdentityProviderCertificate`

  * **Method** : `google.cloud.apigee.v1.Zones.UpdateIdentityProviderCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.UpdateIdentityProviderCertificate" `  




#### `UpdateIdentityProviderConfig`

  * **Method** : `google.cloud.apigee.v1.Zones.UpdateIdentityProviderConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.UpdateIdentityProviderConfig" `  




#### `UpdateZone`

  * **Method** : `google.cloud.apigee.v1.Zones.UpdateZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.UpdateZone" `  




#### `VerifyCertificate`

  * **Method** : `google.cloud.apigee.v1.Zones.VerifyCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apigee.portals.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apigee.v1.Zones.VerifyCertificate" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apigee.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.apigee.v1.EnvironmentService.TestIamPermissions`
  * `google.cloud.apigee.v1.SpaceService.TestIamPermissions`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
