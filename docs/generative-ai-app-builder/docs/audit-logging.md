---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/audit-logging/
title: Agent Search audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:07.207741+00:00
---

# Agent Search audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/audit-logging/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Agent Search audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Agent Search. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Agent Search audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="discoveryengine.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Agent Search generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `a2a.v1.A2AService.GetAgentCard`  
`google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig`  
`google.cloud.discoveryengine.v1.AssistantService.GetAssistant`  
`google.cloud.discoveryengine.v1.AssistantService.ListAssistants`  
`google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig`  
`google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs`  
`google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector`  
`google.cloud.discoveryengine.v1.DataStoreService.GetDataStore`  
`google.cloud.discoveryengine.v1.DataStoreService.ListDataStores`  
`google.cloud.discoveryengine.v1.EngineService.GetEngine`  
`google.cloud.discoveryengine.v1.EngineService.GetIamPolicy`  
`google.cloud.discoveryengine.v1.EngineService.ListEngines`  
`google.cloud.discoveryengine.v1.LicenseConfigService.GetLicenseConfig`  
`google.cloud.discoveryengine.v1.SchemaService.GetSchema`  
`google.cloud.discoveryengine.v1.SchemaService.ListSchemas`  
`google.cloud.discoveryengine.v1.ServingConfigService.GetServingConfig`  
`google.cloud.discoveryengine.v1.ServingConfigService.ListServingConfigs`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomainVerificationStatus`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSiteSearchEngine`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTargetSite`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTargetSites`  
`google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig`  
`google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig`  
`google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant`  
`google.cloud.discoveryengine.v1alpha.AssistantService.ListAssistants`  
`google.cloud.discoveryengine.v1alpha.AuthorizationService.GetAuthorization`  
`google.cloud.discoveryengine.v1alpha.AuthorizationService.ListAuthorizations`  
`google.cloud.discoveryengine.v1alpha.BranchService.GetBranch`  
`google.cloud.discoveryengine.v1alpha.BranchService.ListBranches`  
`google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCannedQuery`  
`google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCannedQueries`  
`google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmekConfig`  
`google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmekConfigs`  
`google.cloud.discoveryengine.v1alpha.CollectionService.GetCollection`  
`google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy`  
`google.cloud.discoveryengine.v1alpha.CollectionService.ListCollections`  
`google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorSecret`  
`google.cloud.discoveryengine.v1alpha.DataConnectorService.GetDataConnector`  
`google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnectorRuns`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletionConfig`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProcessingConfig`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStores`  
`google.cloud.discoveryengine.v1alpha.EngineService.GetEngine`  
`google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy`  
`google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspaceSettings`  
`google.cloud.discoveryengine.v1alpha.EngineService.ListEngines`  
`google.cloud.discoveryengine.v1alpha.EstimateBillingService.EstimateDataSize` (LRO)  
`google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetBillingAccountLicenseConfig`  
`google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetLicenseConfig`  
`google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsentChange`  
`google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema`  
`google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas`  
`google.cloud.discoveryengine.v1alpha.ServingConfigService.GetServingConfig`  
`google.cloud.discoveryengine.v1alpha.ServingConfigService.ListServingConfigs`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchDomainVerificationStatus`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetSiteSearchEngine`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetTargetSite`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUriPatternDocumentData`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.ListTargetSites`  
`google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUserLicenses`  
`google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidgetConfig`  
`google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig`  
`google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant`  
`google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants`  
`google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig`  
`google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs`  
`google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore`  
`google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores`  
`google.cloud.discoveryengine.v1beta.EngineService.GetEngine`  
`google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy`  
`google.cloud.discoveryengine.v1beta.EngineService.ListEngines`  
`google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig`  
`google.cloud.discoveryengine.v1beta.SchemaService.GetSchema`  
`google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas`  
`google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConfig`  
`google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingConfigs`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchDomainVerificationStatus`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSiteSearchEngine`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetTargetSite`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetSites`  
`google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewedNotebooks`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig`  
`google.cloud.discoveryengine.v1.AssistantService.CreateAssistant`  
`google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant`  
`google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant`  
`google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig` (LRO)  
`google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig` (LRO)  
`google.cloud.discoveryengine.v1.CollectionService.DeleteCollection` (LRO)  
`google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector` (LRO)  
`google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector`  
`google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore` (LRO)  
`google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore` (LRO)  
`google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore`  
`google.cloud.discoveryengine.v1.EngineService.CreateEngine` (LRO)  
`google.cloud.discoveryengine.v1.EngineService.DeleteEngine` (LRO)  
`google.cloud.discoveryengine.v1.EngineService.SetIamPolicy`  
`google.cloud.discoveryengine.v1.EngineService.UpdateEngine`  
`google.cloud.discoveryengine.v1.IdentityMappingStoreService.CreateIdentityMappingStore`  
`google.cloud.discoveryengine.v1.IdentityMappingStoreService.DeleteIdentityMappingStore` (LRO)  
`google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicenseConfig`  
`google.cloud.discoveryengine.v1.LicenseConfigService.DistributeLicenseConfig`  
`google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicenseConfig`  
`google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicenseConfig`  
`google.cloud.discoveryengine.v1.ProjectService.ProvisionProject` (LRO)  
`google.cloud.discoveryengine.v1.SchemaService.CreateSchema` (LRO)  
`google.cloud.discoveryengine.v1.SchemaService.DeleteSchema` (LRO)  
`google.cloud.discoveryengine.v1.SchemaService.UpdateSchema` (LRO)  
`google.cloud.discoveryengine.v1.ServingConfigService.CreateServingConfig`  
`google.cloud.discoveryengine.v1.ServingConfigService.DeleteServingConfig`  
`google.cloud.discoveryengine.v1.ServingConfigService.UpdateServingConfig`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerifyTargetSites` (LRO)  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateSitemap`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateTargetSite` (LRO)  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteSitemap`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteTargetSite` (LRO)  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.DisableAdvancedSiteSearch` (LRO)  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.EnableAdvancedSiteSearch` (LRO)  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris` (LRO)  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.UpdateTargetSite` (LRO)  
`google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicenses` (LRO)  
`google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore`  
`google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig`  
`google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAclConfig`  
`google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent`  
`google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent` (LRO)  
`google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlphaEvolveExperimentAndPrograms`  
`google.cloud.discoveryengine.v1alpha.AssistantService.CreateAssistant`  
`google.cloud.discoveryengine.v1alpha.AssistantService.DeleteAssistant`  
`google.cloud.discoveryengine.v1alpha.AssistantService.UpdateAssistant`  
`google.cloud.discoveryengine.v1alpha.AuthorizationService.CreateAuthorization`  
`google.cloud.discoveryengine.v1alpha.AuthorizationService.DeleteAuthorization`  
`google.cloud.discoveryengine.v1alpha.AuthorizationService.UpdateAuthorization`  
`google.cloud.discoveryengine.v1alpha.CannedQueryService.CreateCannedQuery`  
`google.cloud.discoveryengine.v1alpha.CannedQueryService.DeleteCannedQuery`  
`google.cloud.discoveryengine.v1alpha.CannedQueryService.UpdateCannedQuery`  
`google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmekConfig` (LRO)  
`google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmekConfig` (LRO)  
`google.cloud.discoveryengine.v1alpha.CollectionService.DeleteCollection` (LRO)  
`google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy`  
`google.cloud.discoveryengine.v1alpha.CollectionService.UpdateCollection` (LRO)  
`google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpDataConnector` (LRO)  
`google.cloud.discoveryengine.v1alpha.DataConnectorService.UpdateDataConnector`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatientFilter` (LRO)  
`google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStore` (LRO)  
`google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStore` (LRO)  
`google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatientFilters`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatientFilter`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.ReplacePatientFilter` (LRO)  
`google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateCompletionConfig`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStore`  
`google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentProcessingConfig`  
`google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine` (LRO)  
`google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine` (LRO)  
`google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy`  
`google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine`  
`google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.CreateIdentityMappingStore`  
`google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.DeleteIdentityMappingStore` (LRO)  
`google.cloud.discoveryengine.v1alpha.LicenseConfigService.CreateLicenseConfig`  
`google.cloud.discoveryengine.v1alpha.LicenseConfigService.DistributeLicenseConfig`  
`google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicenseConfig`  
`google.cloud.discoveryengine.v1alpha.LicenseConfigService.UpdateLicenseConfig`  
`google.cloud.discoveryengine.v1alpha.ProjectService.ProvisionProject` (LRO)  
`google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject`  
`google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema` (LRO)  
`google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema` (LRO)  
`google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema` (LRO)  
`google.cloud.discoveryengine.v1alpha.ServingConfigService.CreateServingConfig`  
`google.cloud.discoveryengine.v1alpha.ServingConfigService.DeleteServingConfig`  
`google.cloud.discoveryengine.v1alpha.ServingConfigService.UpdateServingConfig`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchVerifyTargetSites` (LRO)  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateSitemap`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateTargetSite` (LRO)  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteSitemap`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteTargetSite` (LRO)  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DisableAdvancedSiteSearch` (LRO)  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.EnableAdvancedSiteSearch` (LRO)  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.RecrawlUris` (LRO)  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUriPatternDocumentData` (LRO)  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.UpdateTargetSite` (LRO)  
`google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdateUserLicenses` (LRO)  
`google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUserStore`  
`google.cloud.discoveryengine.v1alpha.WidgetConfigService.UpdateWidgetConfig`  
`google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAclConfig`  
`google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant`  
`google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant`  
`google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant`  
`google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmekConfig` (LRO)  
`google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmekConfig` (LRO)  
`google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore` (LRO)  
`google.cloud.discoveryengine.v1beta.DataStoreService.DeleteDataStore` (LRO)  
`google.cloud.discoveryengine.v1beta.DataStoreService.UpdateDataStore`  
`google.cloud.discoveryengine.v1beta.EngineService.CreateEngine` (LRO)  
`google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine` (LRO)  
`google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy`  
`google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine`  
`google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.CreateIdentityMappingStore`  
`google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.DeleteIdentityMappingStore` (LRO)  
`google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig`  
`google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig`  
`google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig`  
`google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig`  
`google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject` (LRO)  
`google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema` (LRO)  
`google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema` (LRO)  
`google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema` (LRO)  
`google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingConfig`  
`google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingConfig`  
`google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingConfig`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchVerifyTargetSites` (LRO)  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateSitemap`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateTargetSite` (LRO)  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteSitemap`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteTargetSite` (LRO)  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DisableAdvancedSiteSearch` (LRO)  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.EnableAdvancedSiteSearch` (LRO)  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.RecrawlUris` (LRO)  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.UpdateTargetSite`  
`google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdateUserLicenses` (LRO)  
`google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore`  
`google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook`  
`DATA_READ` | `google.cloud.discoveryengine.v1.CompletionService.AdvancedCompleteQuery`  
`google.cloud.discoveryengine.v1.CompletionService.CompleteQuery`  
`google.cloud.discoveryengine.v1.ControlService.GetControl`  
`google.cloud.discoveryengine.v1.ControlService.ListControls`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversation`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.ListConversations`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.ListSessions`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswerQuery`  
`google.cloud.discoveryengine.v1.DocumentService.BatchGetDocumentsMetadata`  
`google.cloud.discoveryengine.v1.DocumentService.GetDocument`  
`google.cloud.discoveryengine.v1.DocumentService.ListDocuments`  
`google.cloud.discoveryengine.v1.GroundedGenerationService.CheckGrounding`  
`google.cloud.discoveryengine.v1.IdentityMappingStoreService.ListIdentityMappings`  
`google.cloud.discoveryengine.v1.RankService.Rank`  
`google.cloud.discoveryengine.v1.RecommendationService.Recommend`  
`google.cloud.discoveryengine.v1.SearchService.Search`  
`google.cloud.discoveryengine.v1.SearchTuningService.ListCustomModels`  
`google.cloud.discoveryengine.v1.SessionService.GetSession`  
`google.cloud.discoveryengine.v1.SessionService.ListSessions`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchSitemaps`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveExperiment`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveProgram`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolveExperiments`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolvePrograms`  
`google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics` (LRO)  
`google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalyticsConfig`  
`google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk`  
`google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks`  
`google.cloud.discoveryengine.v1alpha.CompletionService.AdvancedCompleteQuery`  
`google.cloud.discoveryengine.v1alpha.CompletionService.CompleteExternalIdentities`  
`google.cloud.discoveryengine.v1alpha.CompletionService.CompleteQuery`  
`google.cloud.discoveryengine.v1alpha.ControlService.GetControl`  
`google.cloud.discoveryengine.v1alpha.ControlService.ListControls`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.AnswerQuery`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetAnswer`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetConversation`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetSession`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListConversations`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListSessions`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.StreamAnswerQuery`  
`google.cloud.discoveryengine.v1alpha.DataConnectorService.CheckRefreshToken`  
`google.cloud.discoveryengine.v1alpha.DocumentService.BatchGetDocumentsMetadata`  
`google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument`  
`google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessedDocument`  
`google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments`  
`google.cloud.discoveryengine.v1alpha.EvaluationService.GetEvaluation`  
`google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults`  
`google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations`  
`google.cloud.discoveryengine.v1alpha.GroundedGenerationService.CheckGrounding`  
`google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ListIdentityMappings`  
`google.cloud.discoveryengine.v1alpha.RankService.Rank`  
`google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend`  
`google.cloud.discoveryengine.v1alpha.RequirementService.CheckRequirement`  
`google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSampleQuery`  
`google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSampleQueries`  
`google.cloud.discoveryengine.v1alpha.SampleQuerySetService.GetSampleQuerySet`  
`google.cloud.discoveryengine.v1alpha.SampleQuerySetService.ListSampleQuerySets`  
`google.cloud.discoveryengine.v1alpha.SearchService.Search`  
`google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomModels`  
`google.cloud.discoveryengine.v1alpha.SessionService.GetSession`  
`google.cloud.discoveryengine.v1alpha.SessionService.ListFiles`  
`google.cloud.discoveryengine.v1alpha.SessionService.ListSessions`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchSitemaps`  
`google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQuery`  
`google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery`  
`google.cloud.discoveryengine.v1beta.ControlService.GetControl`  
`google.cloud.discoveryengine.v1beta.ControlService.ListControls`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.AnswerQuery`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetAnswer`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetConversation`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetSession`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListConversations`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListSessions`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.StreamAnswerQuery`  
`google.cloud.discoveryengine.v1beta.DocumentService.BatchGetDocumentsMetadata`  
`google.cloud.discoveryengine.v1beta.DocumentService.GetDocument`  
`google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments`  
`google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation`  
`google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationResults`  
`google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluations`  
`google.cloud.discoveryengine.v1beta.GroundedGenerationService.CheckGrounding`  
`google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ListIdentityMappings`  
`google.cloud.discoveryengine.v1beta.RankService.Rank`  
`google.cloud.discoveryengine.v1beta.RecommendationService.Recommend`  
`google.cloud.discoveryengine.v1beta.SampleQueryService.GetSampleQuery`  
`google.cloud.discoveryengine.v1beta.SampleQueryService.ListSampleQueries`  
`google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuerySet`  
`google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets`  
`google.cloud.discoveryengine.v1beta.SearchService.Search`  
`google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustomModels`  
`google.cloud.discoveryengine.v1beta.SessionService.GetSession`  
`google.cloud.discoveryengine.v1beta.SessionService.ListSessions`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchSitemaps`  
`google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook`  
`google.cloud.notebooklm.v1alpha.SourceService.GetSource`  
`DATA_WRITE` | `google.cloud.discoveryengine.v1.AssistantService.StreamAssist`  
`google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestions` (LRO)  
`google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntries` (LRO)  
`google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestions` (LRO)  
`google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntries` (LRO)  
`google.cloud.discoveryengine.v1.ControlService.CreateControl`  
`google.cloud.discoveryengine.v1.ControlService.DeleteControl`  
`google.cloud.discoveryengine.v1.ControlService.UpdateControl`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseConversation`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConversation`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSession`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConversation`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSession`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConversation`  
`google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSession`  
`google.cloud.discoveryengine.v1.DocumentService.CreateDocument`  
`google.cloud.discoveryengine.v1.DocumentService.DeleteDocument`  
`google.cloud.discoveryengine.v1.DocumentService.ImportDocuments` (LRO)  
`google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments` (LRO)  
`google.cloud.discoveryengine.v1.DocumentService.UpdateDocument`  
`google.cloud.discoveryengine.v1.IdentityMappingStoreService.ImportIdentityMappings` (LRO)  
`google.cloud.discoveryengine.v1.IdentityMappingStoreService.PurgeIdentityMappings` (LRO)  
`google.cloud.discoveryengine.v1.SearchTuningService.TrainCustomModel`  
`google.cloud.discoveryengine.v1.SessionService.CreateSession`  
`google.cloud.discoveryengine.v1.SessionService.DeleteSession`  
`google.cloud.discoveryengine.v1.SessionService.UpdateSession`  
`google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreateTargetSites` (LRO)  
`google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents` (LRO)  
`google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents` (LRO)  
`google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent`  
`google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.AcquirePrograms`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveExperiment`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveProgram`  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ResumeExperiment` (LRO)  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.StartExperiment` (LRO)  
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.SubmitProgramsEvaluations`  
`google.cloud.discoveryengine.v1alpha.AnalyticsService.UpdateAnalyticsConfig`  
`google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist`  
`google.cloud.discoveryengine.v1alpha.CompletionService.ImportCompletionSuggestions`  
`google.cloud.discoveryengine.v1alpha.CompletionService.ImportSuggestionDenyListEntries` (LRO)  
`google.cloud.discoveryengine.v1alpha.CompletionService.PurgeCompletionSuggestions` (LRO)  
`google.cloud.discoveryengine.v1alpha.CompletionService.PurgeSuggestionDenyListEntries` (LRO)  
`google.cloud.discoveryengine.v1alpha.CompletionService.RemoveSuggestion`  
`google.cloud.discoveryengine.v1alpha.ControlService.CreateControl`  
`google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl`  
`google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ConverseConversation`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateConversation`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateSession`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteConversation`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteSession`  
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService.UpdateConversation`  
`google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAccessToken`  
`google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument`  
`google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument`  
`google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments` (LRO)  
`google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments` (LRO)  
`google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument`  
`google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine`  
`google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine`  
`google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine` (LRO)  
`google.cloud.discoveryengine.v1alpha.EvaluationService.CreateEvaluation` (LRO)  
`google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ImportIdentityMappings` (LRO)  
`google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.PurgeIdentityMappings`  
`google.cloud.discoveryengine.v1alpha.SampleQueryService.CreateSampleQuery`  
`google.cloud.discoveryengine.v1alpha.SampleQueryService.DeleteSampleQuery`  
`google.cloud.discoveryengine.v1alpha.SampleQueryService.ImportSampleQueries` (LRO)  
`google.cloud.discoveryengine.v1alpha.SampleQueryService.UpdateSampleQuery`  
`google.cloud.discoveryengine.v1alpha.SampleQuerySetService.CreateSampleQuerySet`  
`google.cloud.discoveryengine.v1alpha.SampleQuerySetService.DeleteSampleQuerySet`  
`google.cloud.discoveryengine.v1alpha.SampleQuerySetService.UpdateSampleQuerySet`  
`google.cloud.discoveryengine.v1alpha.SearchTuningService.TrainCustomModel` (LRO)  
`google.cloud.discoveryengine.v1alpha.SessionService.CreateSession`  
`google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession`  
`google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession`  
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchCreateTargetSites` (LRO)  
`google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents` (LRO)  
`google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUserEvents` (LRO)  
`google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent`  
`google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist`  
`google.cloud.discoveryengine.v1beta.CompletionService.ImportCompletionSuggestions`  
`google.cloud.discoveryengine.v1beta.CompletionService.ImportSuggestionDenyListEntries` (LRO)  
`google.cloud.discoveryengine.v1beta.CompletionService.PurgeCompletionSuggestions` (LRO)  
`google.cloud.discoveryengine.v1beta.CompletionService.PurgeSuggestionDenyListEntries` (LRO)  
`google.cloud.discoveryengine.v1beta.CompletionService.RemoveSuggestion`  
`google.cloud.discoveryengine.v1beta.ControlService.CreateControl`  
`google.cloud.discoveryengine.v1beta.ControlService.DeleteControl`  
`google.cloud.discoveryengine.v1beta.ControlService.UpdateControl`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateConversation`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateSession`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteConversation`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteSession`  
`google.cloud.discoveryengine.v1beta.ConversationalSearchService.UpdateConversation`  
`google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument`  
`google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument`  
`google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments` (LRO)  
`google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments` (LRO)  
`google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument`  
`google.cloud.discoveryengine.v1beta.EngineService.PauseEngine`  
`google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine`  
`google.cloud.discoveryengine.v1beta.EngineService.TuneEngine`  
`google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluation` (LRO)  
`google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ImportIdentityMappings`  
`google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.PurgeIdentityMappings`  
`google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSampleQuery`  
`google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSampleQuery`  
`google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSampleQueries` (LRO)  
`google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSampleQuery`  
`google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQuerySet`  
`google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQuerySet`  
`google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet`  
`google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustomModel`  
`google.cloud.discoveryengine.v1beta.SessionService.CreateSession`  
`google.cloud.discoveryengine.v1beta.SessionService.DeleteSession`  
`google.cloud.discoveryengine.v1beta.SessionService.UpdateSession`  
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchCreateTargetSites` (LRO)  
`google.cloud.discoveryengine.v1beta.UserEventService.ImportUserEvents` (LRO)  
`google.cloud.discoveryengine.v1beta.UserEventService.PurgeUserEvents`  
`google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent`  
`google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudioOverview`  
`google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudioOverview`  
`google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook`  
`google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources`  
`google.longrunning.Operations.CancelOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Agent Search.

### `a2a.v1.A2AService`

The following audit logs are associated with methods belonging to `a2a.v1.A2AService`.

#### `GetAgentCard`

  * **Method** : `a2a.v1.A2AService.GetAgentCard`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="a2a.v1.A2AService.GetAgentCard" `  




### `google.cloud.discoveryengine.v1.AclConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.AclConfigService`.

#### `GetAclConfig`

  * **Method** : `google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.aclConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig" `  




#### `UpdateAclConfig`

  * **Method** : `google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.aclConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig" `  




### `google.cloud.discoveryengine.v1.AssistantService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.AssistantService`.

#### `CreateAssistant`

  * **Method** : `google.cloud.discoveryengine.v1.AssistantService.CreateAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.CreateAssistant" `  




#### `DeleteAssistant`

  * **Method** : `google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant" `  




#### `GetAssistant`

  * **Method** : `google.cloud.discoveryengine.v1.AssistantService.GetAssistant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.GetAssistant" `  




#### `ListAssistants`

  * **Method** : `google.cloud.discoveryengine.v1.AssistantService.ListAssistants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.ListAssistants" `  




#### `StreamAssist`

  * **Method** : `google.cloud.discoveryengine.v1.AssistantService.StreamAssist`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.assist - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.StreamAssist" `  




#### `UpdateAssistant`

  * **Method** : `google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant" `  




### `google.cloud.discoveryengine.v1.CmekConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.CmekConfigService`.

#### `DeleteCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig" `  




#### `GetCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig" `  




#### `ListCmekConfigs`

  * **Method** : `google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs" `  




#### `UpdateCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig" `  




### `google.cloud.discoveryengine.v1.CollectionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.CollectionService`.

#### `DeleteCollection`

  * **Method** : `google.cloud.discoveryengine.v1.CollectionService.DeleteCollection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.collections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CollectionService.DeleteCollection" `  




### `google.cloud.discoveryengine.v1.CompletionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.CompletionService`.

#### `AdvancedCompleteQuery`

  * **Method** : `google.cloud.discoveryengine.v1.CompletionService.AdvancedCompleteQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionConfigs.completeQuery - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.AdvancedCompleteQuery" `  




#### `CompleteQuery`

  * **Method** : `google.cloud.discoveryengine.v1.CompletionService.CompleteQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.completeQuery - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.CompleteQuery" `  




#### `ImportCompletionSuggestions`

  * **Method** : `google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionSuggestions.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestions" `  




#### `ImportSuggestionDenyListEntries`

  * **Method** : `google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntries" `  




#### `PurgeCompletionSuggestions`

  * **Method** : `google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionSuggestions.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestions" `  




#### `PurgeSuggestionDenyListEntries`

  * **Method** : `google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntries" `  




### `google.cloud.discoveryengine.v1.ControlService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ControlService`.

#### `CreateControl`

  * **Method** : `google.cloud.discoveryengine.v1.ControlService.CreateControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.CreateControl" `  




#### `DeleteControl`

  * **Method** : `google.cloud.discoveryengine.v1.ControlService.DeleteControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.DeleteControl" `  




#### `GetControl`

  * **Method** : `google.cloud.discoveryengine.v1.ControlService.GetControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.GetControl" `  




#### `ListControls`

  * **Method** : `google.cloud.discoveryengine.v1.ControlService.ListControls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.ListControls" `  




#### `UpdateControl`

  * **Method** : `google.cloud.discoveryengine.v1.ControlService.UpdateControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.UpdateControl" `  




### `google.cloud.discoveryengine.v1.ConversationalSearchService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ConversationalSearchService`.

#### `AnswerQuery`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.answer - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery" `  




#### `ConverseConversation`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.converse - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseConversation" `  




#### `CreateConversation`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConversation" `  




#### `CreateSession`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSession" `  




#### `DeleteConversation`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConversation" `  




#### `DeleteSession`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSession" `  




#### `GetAnswer`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.answers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer" `  




#### `GetConversation`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversation" `  




#### `GetSession`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession" `  




#### `ListConversations`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.ListConversations" `  




#### `ListSessions`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.ListSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.ListSessions" `  




#### `StreamAnswerQuery`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswerQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.answer - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswerQuery" `  




#### `UpdateConversation`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConversation" `  




#### `UpdateSession`

  * **Method** : `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSession" `  




### `google.cloud.discoveryengine.v1.DataConnectorService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.DataConnectorService`.

#### `GetDataConnector`

  * **Method** : `google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector" `  




#### `SetUpDataConnector`

  * **Method** : `google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.locations.setUpDataConnector - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector" `  




#### `UpdateDataConnector`

  * **Method** : `google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataConnectors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector" `  




### `google.cloud.discoveryengine.v1.DataStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.DataStoreService`.

#### `CreateDataStore`

  * **Method** : `google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore" `  




#### `DeleteDataStore`

  * **Method** : `google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore" `  




#### `GetDataStore`

  * **Method** : `google.cloud.discoveryengine.v1.DataStoreService.GetDataStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.GetDataStore" `  




#### `ListDataStores`

  * **Method** : `google.cloud.discoveryengine.v1.DataStoreService.ListDataStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.ListDataStores" `  




#### `UpdateDataStore`

  * **Method** : `google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore" `  




### `google.cloud.discoveryengine.v1.DocumentService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.DocumentService`.

#### `BatchGetDocumentsMetadata`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.BatchGetDocumentsMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.BatchGetDocumentsMetadata" `  




#### `CreateDocument`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.CreateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.CreateDocument" `  




#### `DeleteDocument`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.DeleteDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.DeleteDocument" `  




#### `GetDocument`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.GetDocument" `  




#### `ImportDocuments`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.ImportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.ImportDocuments" `  




#### `ListDocuments`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.ListDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.ListDocuments" `  




#### `PurgeDocuments`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.discoveryengine.v1.DocumentService.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.UpdateDocument" `  




### `google.cloud.discoveryengine.v1.EngineService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.EngineService`.

#### `CreateEngine`

  * **Method** : `google.cloud.discoveryengine.v1.EngineService.CreateEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.CreateEngine" `  




#### `DeleteEngine`

  * **Method** : `google.cloud.discoveryengine.v1.EngineService.DeleteEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.DeleteEngine" `  




#### `GetEngine`

  * **Method** : `google.cloud.discoveryengine.v1.EngineService.GetEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.GetEngine" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1.EngineService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.GetIamPolicy" `  




#### `ListEngines`

  * **Method** : `google.cloud.discoveryengine.v1.EngineService.ListEngines`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.ListEngines" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1.EngineService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.SetIamPolicy" `  




#### `UpdateEngine`

  * **Method** : `google.cloud.discoveryengine.v1.EngineService.UpdateEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.UpdateEngine" `  




### `google.cloud.discoveryengine.v1.GroundedGenerationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.GroundedGenerationService`.

#### `CheckGrounding`

  * **Method** : `google.cloud.discoveryengine.v1.GroundedGenerationService.CheckGrounding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.groundingConfigs.check - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.GroundedGenerationService.CheckGrounding" `  




### `google.cloud.discoveryengine.v1.IdentityMappingStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.IdentityMappingStoreService`.

#### `CreateIdentityMappingStore`

  * **Method** : `google.cloud.discoveryengine.v1.IdentityMappingStoreService.CreateIdentityMappingStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.CreateIdentityMappingStore" `  




#### `DeleteIdentityMappingStore`

  * **Method** : `google.cloud.discoveryengine.v1.IdentityMappingStoreService.DeleteIdentityMappingStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.DeleteIdentityMappingStore" `  




#### `ImportIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1.IdentityMappingStoreService.ImportIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.importIdentityMappings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.ImportIdentityMappings" `  




#### `ListIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1.IdentityMappingStoreService.ListIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.listIdentityMappings - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.ListIdentityMappings" `  




#### `PurgeIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1.IdentityMappingStoreService.PurgeIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.purgeIdentityMappings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.PurgeIdentityMappings" `  




### `google.cloud.discoveryengine.v1.LicenseConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.LicenseConfigService`.

#### `CreateLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicenseConfig" `  




#### `DistributeLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1.LicenseConfigService.DistributeLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.billingAccountLicenseConfigs.distribute - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.DistributeLicenseConfig" `  




#### `GetLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1.LicenseConfigService.GetLicenseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.GetLicenseConfig" `  




#### `RetractLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicenseConfig" `  




#### `UpdateLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicenseConfig" `  




### `google.cloud.discoveryengine.v1.ProjectService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ProjectService`.

#### `ProvisionProject`

  * **Method** : `google.cloud.discoveryengine.v1.ProjectService.ProvisionProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.projects.provision - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ProjectService.ProvisionProject" `  




### `google.cloud.discoveryengine.v1.RankService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.RankService`.

#### `Rank`

  * **Method** : `google.cloud.discoveryengine.v1.RankService.Rank`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.rankingConfigs.rank - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.RankService.Rank" `  




### `google.cloud.discoveryengine.v1.RecommendationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.RecommendationService`.

#### `Recommend`

  * **Method** : `google.cloud.discoveryengine.v1.RecommendationService.Recommend`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.recommend - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.RecommendationService.Recommend" `  




### `google.cloud.discoveryengine.v1.SchemaService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SchemaService`.

#### `CreateSchema`

  * **Method** : `google.cloud.discoveryengine.v1.SchemaService.CreateSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.CreateSchema" `  




#### `DeleteSchema`

  * **Method** : `google.cloud.discoveryengine.v1.SchemaService.DeleteSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.DeleteSchema" `  




#### `GetSchema`

  * **Method** : `google.cloud.discoveryengine.v1.SchemaService.GetSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.schemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.GetSchema" `  




#### `ListSchemas`

  * **Method** : `google.cloud.discoveryengine.v1.SchemaService.ListSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.schemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.ListSchemas" `  




#### `UpdateSchema`

  * **Method** : `google.cloud.discoveryengine.v1.SchemaService.UpdateSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.UpdateSchema" `  




### `google.cloud.discoveryengine.v1.SearchService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SearchService`.

#### `Search`

  * **Method** : `google.cloud.discoveryengine.v1.SearchService.Search`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.search - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SearchService.Search" `  




### `google.cloud.discoveryengine.v1.SearchTuningService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SearchTuningService`.

#### `ListCustomModels`

  * **Method** : `google.cloud.discoveryengine.v1.SearchTuningService.ListCustomModels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.listCustomModels - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SearchTuningService.ListCustomModels" `  




#### `TrainCustomModel`

  * **Method** : `google.cloud.discoveryengine.v1.SearchTuningService.TrainCustomModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.trainCustomModel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SearchTuningService.TrainCustomModel" `  




### `google.cloud.discoveryengine.v1.ServingConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ServingConfigService`.

#### `CreateServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1.ServingConfigService.CreateServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.CreateServingConfig" `  




#### `DeleteServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1.ServingConfigService.DeleteServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.DeleteServingConfig" `  




#### `GetServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1.ServingConfigService.GetServingConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.GetServingConfig" `  




#### `ListServingConfigs`

  * **Method** : `google.cloud.discoveryengine.v1.ServingConfigService.ListServingConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.ListServingConfigs" `  




#### `UpdateServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1.ServingConfigService.UpdateServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.UpdateServingConfig" `  




### `google.cloud.discoveryengine.v1.SessionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SessionService`.

#### `CreateSession`

  * **Method** : `google.cloud.discoveryengine.v1.SessionService.CreateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.CreateSession" `  




#### `DeleteSession`

  * **Method** : `google.cloud.discoveryengine.v1.SessionService.DeleteSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.DeleteSession" `  




#### `GetSession`

  * **Method** : `google.cloud.discoveryengine.v1.SessionService.GetSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.GetSession" `  




#### `ListSessions`

  * **Method** : `google.cloud.discoveryengine.v1.SessionService.ListSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.ListSessions" `  




#### `UpdateSession`

  * **Method** : `google.cloud.discoveryengine.v1.SessionService.UpdateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.UpdateSession" `  




### `google.cloud.discoveryengine.v1.SiteSearchEngineService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SiteSearchEngineService`.

#### `BatchCreateTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreateTargetSites`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.batchCreate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreateTargetSites" `  




#### `BatchVerifyTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerifyTargetSites`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.batchVerifyTargetSites - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerifyTargetSites" `  




#### `CreateSitemap`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateSitemap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateSitemap" `  




#### `CreateTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateTargetSite" `  




#### `DeleteSitemap`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteSitemap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteSitemap" `  




#### `DeleteTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteTargetSite" `  




#### `DisableAdvancedSiteSearch`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.DisableAdvancedSiteSearch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.DisableAdvancedSiteSearch" `  




#### `EnableAdvancedSiteSearch`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.EnableAdvancedSiteSearch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.EnableAdvancedSiteSearch" `  




#### `FetchDomainVerificationStatus`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomainVerificationStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomainVerificationStatus" `  




#### `FetchSitemaps`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchSitemaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.fetch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchSitemaps" `  




#### `GetSiteSearchEngine`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSiteSearchEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSiteSearchEngine" `  




#### `GetTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTargetSite`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTargetSite" `  




#### `ListTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTargetSites`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTargetSites" `  




#### `RecrawlUris`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris" `  




#### `UpdateTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1.SiteSearchEngineService.UpdateTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.UpdateTargetSite" `  




### `google.cloud.discoveryengine.v1.UserEventService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.UserEventService`.

#### `ImportUserEvents`

  * **Method** : `google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents" `  




#### `PurgeUserEvents`

  * **Method** : `google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents" `  




#### `WriteUserEvent`

  * **Method** : `google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent" `  




### `google.cloud.discoveryengine.v1.UserLicenseService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.UserLicenseService`.

#### `BatchUpdateUserLicenses`

  * **Method** : `google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicenses`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicenses" `  




### `google.cloud.discoveryengine.v1.UserStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.UserStoreService`.

#### `UpdateUserStore`

  * **Method** : `google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.userStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore" `  




### `google.cloud.discoveryengine.v1.WidgetConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.WidgetConfigService`.

#### `GetWidgetConfig`

  * **Method** : `google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.widgetConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig" `  




#### `UpdateWidgetConfig`

  * **Method** : `google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.widgetConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig" `  




### `google.cloud.discoveryengine.v1alpha.AclConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AclConfigService`.

#### `GetAclConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.aclConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig" `  




#### `UpdateAclConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAclConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.aclConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAclConfig" `  




### `google.cloud.discoveryengine.v1alpha.AgentService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AgentService`.

#### `CreateAgent`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.agents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent" `  




#### `DeleteAgent`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.agents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent" `  




#### `ImportAgentFile`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.agentFiles.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile" `  




#### `UpdateAgent`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.agents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent" `  




### `google.cloud.discoveryengine.v1alpha.AlphaEvolveService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AlphaEvolveService`.

#### `AcquirePrograms`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.AcquirePrograms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.acquirePrograms - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.AcquirePrograms" `  




#### `CreateAlphaEvolveExperiment`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveExperiment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveExperiment" `  




#### `CreateAlphaEvolveProgram`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveProgram`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolvePrograms.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveProgram" `  




#### `DeleteAlphaEvolveExperimentAndPrograms`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlphaEvolveExperimentAndPrograms`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlphaEvolveExperimentAndPrograms" `  




#### `GetAlphaEvolveExperiment`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveExperiment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveExperiment" `  




#### `GetAlphaEvolveProgram`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveProgram`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolvePrograms.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveProgram" `  




#### `ListAlphaEvolveExperiments`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolveExperiments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolveExperiments" `  




#### `ListAlphaEvolvePrograms`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolvePrograms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolvePrograms.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolvePrograms" `  




#### `ResumeExperiment`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ResumeExperiment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.resume - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ResumeExperiment" `  




#### `StartExperiment`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.StartExperiment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.start - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.StartExperiment" `  




#### `SubmitProgramsEvaluations`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.SubmitProgramsEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.alphaEvolveExperiments.submitProgramsEvaluations - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.SubmitProgramsEvaluations" `  




### `google.cloud.discoveryengine.v1alpha.AnalyticsService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AnalyticsService`.

#### `ExportMetrics`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.analytics.exportMetrics - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics" `  




#### `GetAnalyticsConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalyticsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.analyticsConfigs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalyticsConfig" `  




#### `UpdateAnalyticsConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AnalyticsService.UpdateAnalyticsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.analyticsConfigs.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AnalyticsService.UpdateAnalyticsConfig" `  




### `google.cloud.discoveryengine.v1alpha.AssistantService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AssistantService`.

#### `CreateAssistant`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AssistantService.CreateAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.CreateAssistant" `  




#### `DeleteAssistant`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AssistantService.DeleteAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.DeleteAssistant" `  




#### `GetAssistant`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant" `  




#### `ListAssistants`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AssistantService.ListAssistants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.ListAssistants" `  




#### `StreamAssist`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.assist - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist" `  




#### `UpdateAssistant`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AssistantService.UpdateAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.UpdateAssistant" `  




### `google.cloud.discoveryengine.v1alpha.AuthorizationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AuthorizationService`.

#### `CreateAuthorization`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AuthorizationService.CreateAuthorization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.authorizations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.CreateAuthorization" `  




#### `DeleteAuthorization`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AuthorizationService.DeleteAuthorization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.authorizations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.DeleteAuthorization" `  




#### `GetAuthorization`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AuthorizationService.GetAuthorization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.authorizations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.GetAuthorization" `  




#### `ListAuthorizations`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AuthorizationService.ListAuthorizations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.authorizations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.ListAuthorizations" `  




#### `UpdateAuthorization`

  * **Method** : `google.cloud.discoveryengine.v1alpha.AuthorizationService.UpdateAuthorization`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.authorizations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.UpdateAuthorization" `  




### `google.cloud.discoveryengine.v1alpha.BranchService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.BranchService`.

#### `GetBranch`

  * **Method** : `google.cloud.discoveryengine.v1alpha.BranchService.GetBranch`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.branches.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.BranchService.GetBranch" `  




#### `ListBranches`

  * **Method** : `google.cloud.discoveryengine.v1alpha.BranchService.ListBranches`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.branches.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.BranchService.ListBranches" `  




### `google.cloud.discoveryengine.v1alpha.CannedQueryService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CannedQueryService`.

#### `CreateCannedQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CannedQueryService.CreateCannedQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cannedQueries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.CreateCannedQuery" `  




#### `DeleteCannedQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CannedQueryService.DeleteCannedQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cannedQueries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.DeleteCannedQuery" `  




#### `GetCannedQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCannedQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cannedQueries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCannedQuery" `  




#### `ListCannedQueries`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCannedQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cannedQueries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCannedQueries" `  




#### `UpdateCannedQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CannedQueryService.UpdateCannedQuery`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cannedQueries.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.UpdateCannedQuery" `  




### `google.cloud.discoveryengine.v1alpha.ChunkService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ChunkService`.

#### `GetChunk`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.chunks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk" `  




#### `ListChunks`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.chunks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks" `  




### `google.cloud.discoveryengine.v1alpha.CmekConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CmekConfigService`.

#### `DeleteCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmekConfig" `  




#### `GetCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmekConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmekConfig" `  




#### `ListCmekConfigs`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmekConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmekConfigs" `  




#### `UpdateCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmekConfig" `  




### `google.cloud.discoveryengine.v1alpha.CollectionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CollectionService`.

#### `DeleteCollection`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CollectionService.DeleteCollection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.collections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.DeleteCollection" `  




#### `GetCollection`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CollectionService.GetCollection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.collections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.GetCollection" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.collections.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy" `  




#### `ListCollections`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CollectionService.ListCollections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.collections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.ListCollections" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.collections.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy" `  




#### `UpdateCollection`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CollectionService.UpdateCollection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.collections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.UpdateCollection" `  




### `google.cloud.discoveryengine.v1alpha.CompletionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CompletionService`.

#### `AdvancedCompleteQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.AdvancedCompleteQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionConfigs.completeQuery - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.AdvancedCompleteQuery" `  




#### `CompleteExternalIdentities`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.CompleteExternalIdentities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.locations.completeExternalIdentities - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.CompleteExternalIdentities" `  




#### `CompleteQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.CompleteQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.completeQuery - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.CompleteQuery" `  




#### `ImportCompletionSuggestions`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.ImportCompletionSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionSuggestions.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.ImportCompletionSuggestions" `  




#### `ImportSuggestionDenyListEntries`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.ImportSuggestionDenyListEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.ImportSuggestionDenyListEntries" `  




#### `PurgeCompletionSuggestions`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.PurgeCompletionSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionSuggestions.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.PurgeCompletionSuggestions" `  




#### `PurgeSuggestionDenyListEntries`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.PurgeSuggestionDenyListEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.PurgeSuggestionDenyListEntries" `  




#### `RemoveSuggestion`

  * **Method** : `google.cloud.discoveryengine.v1alpha.CompletionService.RemoveSuggestion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionConfigs.removeSuggestion - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.RemoveSuggestion" `  




### `google.cloud.discoveryengine.v1alpha.ControlService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ControlService`.

#### `CreateControl`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ControlService.CreateControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.CreateControl" `  




#### `DeleteControl`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl" `  




#### `GetControl`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ControlService.GetControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.GetControl" `  




#### `ListControls`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ControlService.ListControls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.ListControls" `  




#### `UpdateControl`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl" `  




### `google.cloud.discoveryengine.v1alpha.ConversationalSearchService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ConversationalSearchService`.

#### `AnswerQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.AnswerQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.answer - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.AnswerQuery" `  




#### `ConverseConversation`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ConverseConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.converse - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ConverseConversation" `  




#### `CreateConversation`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateConversation" `  




#### `CreateSession`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateSession" `  




#### `DeleteConversation`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteConversation" `  




#### `DeleteSession`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteSession" `  




#### `GetAnswer`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetAnswer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.answers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetAnswer" `  




#### `GetConversation`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetConversation" `  




#### `GetSession`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetSession" `  




#### `ListConversations`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListConversations" `  




#### `ListSessions`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListSessions" `  




#### `StreamAnswerQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.StreamAnswerQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.answer - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.StreamAnswerQuery" `  




#### `UpdateConversation`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.UpdateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.UpdateConversation" `  




### `google.cloud.discoveryengine.v1alpha.DataConnectorService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.DataConnectorService`.

#### `AcquireAccessToken`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAccessToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataConnectors.acquireAccessToken - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAccessToken" `  




#### `CheckRefreshToken`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataConnectorService.CheckRefreshToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataConnectors.checkRefreshToken - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.CheckRefreshToken" `  




#### `GetConnectorSecret`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorSecret`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorSecret" `  




#### `GetDataConnector`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataConnectorService.GetDataConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.GetDataConnector" `  




#### `ListConnectorRuns`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnectorRuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.connectorRuns.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnectorRuns" `  




#### `SetUpDataConnector`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpDataConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.locations.setUpDataConnector - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpDataConnector" `  




#### `UpdateDataConnector`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataConnectorService.UpdateDataConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataConnectors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.UpdateDataConnector" `  




### `google.cloud.discoveryengine.v1alpha.DataStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.DataStoreService`.

#### `AddPatientFilter`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatientFilter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.addPatientFilters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatientFilter" `  




#### `CreateDataStore`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStore" `  




#### `DeleteDataStore`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStore" `  




#### `DeletePatientFilters`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatientFilters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.deletePatientFilters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatientFilters" `  




#### `GetCompletionConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletionConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletionConfig" `  




#### `GetDataStore`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore" `  




#### `GetDocumentProcessingConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProcessingConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documentProcessingConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProcessingConfig" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy" `  




#### `ListDataStores`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStores" `  




#### `RemovePatientFilter`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatientFilter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.deletePatientFilters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatientFilter" `  




#### `ReplacePatientFilter`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.ReplacePatientFilter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.updatePatientFilters - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.ReplacePatientFilter" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy" `  




#### `UpdateCompletionConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateCompletionConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.completionConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateCompletionConfig" `  




#### `UpdateDataStore`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStore" `  




#### `UpdateDocumentProcessingConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentProcessingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.documentProcessingConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentProcessingConfig" `  




### `google.cloud.discoveryengine.v1alpha.DocumentService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.DocumentService`.

#### `BatchGetDocumentsMetadata`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.BatchGetDocumentsMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.BatchGetDocumentsMetadata" `  




#### `CreateDocument`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument" `  




#### `DeleteDocument`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument" `  




#### `GetDocument`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument" `  




#### `GetProcessedDocument`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessedDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessedDocument" `  




#### `ImportDocuments`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments" `  




#### `ListDocuments`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments" `  




#### `PurgeDocuments`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument" `  




### `google.cloud.discoveryengine.v1alpha.EngineService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.EngineService`.

#### `CreateEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine" `  




#### `DeleteEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine" `  




#### `GetEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.GetEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.GetEngine" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy" `  




#### `GetWorkspaceSettings`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspaceSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspaceSettings" `  




#### `ListEngines`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.ListEngines`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.ListEngines" `  




#### `PauseEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.pause - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine" `  




#### `ResumeEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.resume - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy" `  




#### `TuneEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.tune - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine" `  




#### `UpdateEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine" `  




### `google.cloud.discoveryengine.v1alpha.EstimateBillingService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.EstimateBillingService`.

#### `EstimateDataSize`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EstimateBillingService.EstimateDataSize`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.locations.estimateDataSize - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EstimateBillingService.EstimateDataSize" `  




### `google.cloud.discoveryengine.v1alpha.EvaluationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.EvaluationService`.

#### `CreateEvaluation`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EvaluationService.CreateEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.CreateEvaluation" `  




#### `GetEvaluation`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EvaluationService.GetEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.GetEvaluation" `  




#### `ListEvaluationResults`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults" `  




#### `ListEvaluations`

  * **Method** : `google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations" `  




### `google.cloud.discoveryengine.v1alpha.GroundedGenerationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.GroundedGenerationService`.

#### `CheckGrounding`

  * **Method** : `google.cloud.discoveryengine.v1alpha.GroundedGenerationService.CheckGrounding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.groundingConfigs.check - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.GroundedGenerationService.CheckGrounding" `  




### `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService`.

#### `CreateIdentityMappingStore`

  * **Method** : `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.CreateIdentityMappingStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.CreateIdentityMappingStore" `  




#### `DeleteIdentityMappingStore`

  * **Method** : `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.DeleteIdentityMappingStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.DeleteIdentityMappingStore" `  




#### `ImportIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ImportIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.importIdentityMappings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ImportIdentityMappings" `  




#### `ListIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ListIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.listIdentityMappings - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ListIdentityMappings" `  




#### `PurgeIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.PurgeIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.purgeIdentityMappings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.PurgeIdentityMappings" `  




### `google.cloud.discoveryengine.v1alpha.LicenseConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.LicenseConfigService`.

#### `CreateLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.LicenseConfigService.CreateLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.CreateLicenseConfig" `  




#### `DistributeLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.LicenseConfigService.DistributeLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.billingAccountLicenseConfigs.distribute - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.DistributeLicenseConfig" `  




#### `GetBillingAccountLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetBillingAccountLicenseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.billingAccountLicenseConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetBillingAccountLicenseConfig" `  




#### `GetLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetLicenseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetLicenseConfig" `  




#### `RetractLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicenseConfig" `  




#### `UpdateLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.LicenseConfigService.UpdateLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.UpdateLicenseConfig" `  




### `google.cloud.discoveryengine.v1alpha.ProjectService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ProjectService`.

#### `ProvisionProject`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ProjectService.ProvisionProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.projects.provision - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectService.ProvisionProject" `  




#### `ReportConsentChange`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsentChange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.projects.reportConsentChange - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsentChange" `  




#### `UpdateProject`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.projects.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject" `  




### `google.cloud.discoveryengine.v1alpha.RankService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.RankService`.

#### `Rank`

  * **Method** : `google.cloud.discoveryengine.v1alpha.RankService.Rank`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.rankingConfigs.rank - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.RankService.Rank" `  




### `google.cloud.discoveryengine.v1alpha.RecommendationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.RecommendationService`.

#### `Recommend`

  * **Method** : `google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.recommend - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend" `  




### `google.cloud.discoveryengine.v1alpha.RequirementService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.RequirementService`.

#### `CheckRequirement`

  * **Method** : `google.cloud.discoveryengine.v1alpha.RequirementService.CheckRequirement`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.requirements.checkRequirement - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.RequirementService.CheckRequirement" `  




### `google.cloud.discoveryengine.v1alpha.SampleQueryService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SampleQueryService`.

#### `CreateSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQueryService.CreateSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.CreateSampleQuery" `  




#### `DeleteSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQueryService.DeleteSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.DeleteSampleQuery" `  




#### `GetSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSampleQuery" `  




#### `ImportSampleQueries`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQueryService.ImportSampleQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.ImportSampleQueries" `  




#### `ListSampleQueries`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSampleQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSampleQueries" `  




#### `UpdateSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQueryService.UpdateSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.UpdateSampleQuery" `  




### `google.cloud.discoveryengine.v1alpha.SampleQuerySetService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SampleQuerySetService`.

#### `CreateSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.CreateSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.CreateSampleQuerySet" `  




#### `DeleteSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.DeleteSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.DeleteSampleQuerySet" `  




#### `GetSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.GetSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.GetSampleQuerySet" `  




#### `ListSampleQuerySets`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.ListSampleQuerySets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.ListSampleQuerySets" `  




#### `UpdateSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.UpdateSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.UpdateSampleQuerySet" `  




### `google.cloud.discoveryengine.v1alpha.SchemaService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SchemaService`.

#### `CreateSchema`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema" `  




#### `DeleteSchema`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema" `  




#### `GetSchema`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.schemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema" `  




#### `ListSchemas`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.schemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas" `  




#### `UpdateSchema`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema" `  




### `google.cloud.discoveryengine.v1alpha.SearchService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SearchService`.

#### `Search`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SearchService.Search`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.search - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchService.Search" `  




### `google.cloud.discoveryengine.v1alpha.SearchTuningService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SearchTuningService`.

#### `ListCustomModels`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomModels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.listCustomModels - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomModels" `  




#### `TrainCustomModel`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SearchTuningService.TrainCustomModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.trainCustomModel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchTuningService.TrainCustomModel" `  




### `google.cloud.discoveryengine.v1alpha.ServingConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ServingConfigService`.

#### `CreateServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ServingConfigService.CreateServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.CreateServingConfig" `  




#### `DeleteServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ServingConfigService.DeleteServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.DeleteServingConfig" `  




#### `GetServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ServingConfigService.GetServingConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.GetServingConfig" `  




#### `ListServingConfigs`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ServingConfigService.ListServingConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.ListServingConfigs" `  




#### `UpdateServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.ServingConfigService.UpdateServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.UpdateServingConfig" `  




### `google.cloud.discoveryengine.v1alpha.SessionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SessionService`.

#### `CreateSession`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SessionService.CreateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.CreateSession" `  




#### `DeleteSession`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession" `  




#### `GetSession`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SessionService.GetSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.GetSession" `  




#### `ListFiles`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SessionService.ListFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.listSessionFileMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.ListFiles" `  




#### `ListSessions`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SessionService.ListSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.ListSessions" `  




#### `UpdateSession`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession" `  




### `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService`.

#### `BatchCreateTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchCreateTargetSites`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.batchCreate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchCreateTargetSites" `  




#### `BatchVerifyTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchVerifyTargetSites`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.batchVerifyTargetSites - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchVerifyTargetSites" `  




#### `CreateSitemap`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateSitemap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateSitemap" `  




#### `CreateTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateTargetSite" `  




#### `DeleteSitemap`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteSitemap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteSitemap" `  




#### `DeleteTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteTargetSite" `  




#### `DisableAdvancedSiteSearch`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DisableAdvancedSiteSearch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DisableAdvancedSiteSearch" `  




#### `EnableAdvancedSiteSearch`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.EnableAdvancedSiteSearch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.EnableAdvancedSiteSearch" `  




#### `FetchDomainVerificationStatus`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchDomainVerificationStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchDomainVerificationStatus" `  




#### `FetchSitemaps`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchSitemaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.fetch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchSitemaps" `  




#### `GetSiteSearchEngine`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetSiteSearchEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetSiteSearchEngine" `  




#### `GetTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetTargetSite`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetTargetSite" `  




#### `GetUriPatternDocumentData`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUriPatternDocumentData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.getUriPatternDocumentData - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUriPatternDocumentData" `  




#### `ListTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.ListTargetSites`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.ListTargetSites" `  




#### `RecrawlUris`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.RecrawlUris`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.RecrawlUris" `  




#### `SetUriPatternDocumentData`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUriPatternDocumentData`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.setUriPatternDocumentData - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUriPatternDocumentData" `  




#### `UpdateTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.UpdateTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.UpdateTargetSite" `  




### `google.cloud.discoveryengine.v1alpha.UserEventService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.UserEventService`.

#### `ImportUserEvents`

  * **Method** : `google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents" `  




#### `PurgeUserEvents`

  * **Method** : `google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUserEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUserEvents" `  




#### `WriteUserEvent`

  * **Method** : `google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent" `  




### `google.cloud.discoveryengine.v1alpha.UserLicenseService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.UserLicenseService`.

#### `BatchUpdateUserLicenses`

  * **Method** : `google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdateUserLicenses`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdateUserLicenses" `  




#### `ExportUserLicenses`

  * **Method** : `google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUserLicenses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userStores.listUserLicenses - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUserLicenses" `  




### `google.cloud.discoveryengine.v1alpha.UserStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.UserStoreService`.

#### `UpdateUserStore`

  * **Method** : `google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUserStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.userStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUserStore" `  




### `google.cloud.discoveryengine.v1alpha.WidgetConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.WidgetConfigService`.

#### `GetWidgetConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidgetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.widgetConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidgetConfig" `  




#### `UpdateWidgetConfig`

  * **Method** : `google.cloud.discoveryengine.v1alpha.WidgetConfigService.UpdateWidgetConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.widgetConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1alpha.WidgetConfigService.UpdateWidgetConfig" `  




### `google.cloud.discoveryengine.v1beta.AclConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.AclConfigService`.

#### `GetAclConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.aclConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig" `  




#### `UpdateAclConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAclConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.aclConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAclConfig" `  




### `google.cloud.discoveryengine.v1beta.AssistantService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.AssistantService`.

#### `CreateAssistant`

  * **Method** : `google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant" `  




#### `DeleteAssistant`

  * **Method** : `google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant" `  




#### `GetAssistant`

  * **Method** : `google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant" `  




#### `ListAssistants`

  * **Method** : `google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants" `  




#### `StreamAssist`

  * **Method** : `google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.assistants.assist - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist" `  




#### `UpdateAssistant`

  * **Method** : `google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.assistants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant" `  




### `google.cloud.discoveryengine.v1beta.CmekConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.CmekConfigService`.

#### `DeleteCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmekConfig" `  




#### `GetCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig" `  




#### `ListCmekConfigs`

  * **Method** : `google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs" `  




#### `UpdateCmekConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.cmekConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmekConfig" `  




### `google.cloud.discoveryengine.v1beta.CompletionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.CompletionService`.

#### `AdvancedCompleteQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionConfigs.completeQuery - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQuery" `  




#### `CompleteQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.completeQuery - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery" `  




#### `ImportCompletionSuggestions`

  * **Method** : `google.cloud.discoveryengine.v1beta.CompletionService.ImportCompletionSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionSuggestions.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.ImportCompletionSuggestions" `  




#### `ImportSuggestionDenyListEntries`

  * **Method** : `google.cloud.discoveryengine.v1beta.CompletionService.ImportSuggestionDenyListEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.ImportSuggestionDenyListEntries" `  




#### `PurgeCompletionSuggestions`

  * **Method** : `google.cloud.discoveryengine.v1beta.CompletionService.PurgeCompletionSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionSuggestions.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.PurgeCompletionSuggestions" `  




#### `PurgeSuggestionDenyListEntries`

  * **Method** : `google.cloud.discoveryengine.v1beta.CompletionService.PurgeSuggestionDenyListEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.PurgeSuggestionDenyListEntries" `  




#### `RemoveSuggestion`

  * **Method** : `google.cloud.discoveryengine.v1beta.CompletionService.RemoveSuggestion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.completionConfigs.removeSuggestion - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.RemoveSuggestion" `  




### `google.cloud.discoveryengine.v1beta.ControlService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ControlService`.

#### `CreateControl`

  * **Method** : `google.cloud.discoveryengine.v1beta.ControlService.CreateControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.CreateControl" `  




#### `DeleteControl`

  * **Method** : `google.cloud.discoveryengine.v1beta.ControlService.DeleteControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.DeleteControl" `  




#### `GetControl`

  * **Method** : `google.cloud.discoveryengine.v1beta.ControlService.GetControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.GetControl" `  




#### `ListControls`

  * **Method** : `google.cloud.discoveryengine.v1beta.ControlService.ListControls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.ListControls" `  




#### `UpdateControl`

  * **Method** : `google.cloud.discoveryengine.v1beta.ControlService.UpdateControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.controls.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.UpdateControl" `  




### `google.cloud.discoveryengine.v1beta.ConversationalSearchService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ConversationalSearchService`.

#### `AnswerQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.AnswerQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.answer - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.AnswerQuery" `  




#### `ConverseConversation`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.converse - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation" `  




#### `CreateConversation`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateConversation" `  




#### `CreateSession`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateSession" `  




#### `DeleteConversation`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteConversation" `  




#### `DeleteSession`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteSession" `  




#### `GetAnswer`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetAnswer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.answers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetAnswer" `  




#### `GetConversation`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetConversation" `  




#### `GetSession`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetSession" `  




#### `ListConversations`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListConversations" `  




#### `ListSessions`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListSessions" `  




#### `StreamAnswerQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.StreamAnswerQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.answer - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.StreamAnswerQuery" `  




#### `UpdateConversation`

  * **Method** : `google.cloud.discoveryengine.v1beta.ConversationalSearchService.UpdateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.conversations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.UpdateConversation" `  




### `google.cloud.discoveryengine.v1beta.DataStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.DataStoreService`.

#### `CreateDataStore`

  * **Method** : `google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore" `  




#### `DeleteDataStore`

  * **Method** : `google.cloud.discoveryengine.v1beta.DataStoreService.DeleteDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.DeleteDataStore" `  




#### `GetDataStore`

  * **Method** : `google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore" `  




#### `ListDataStores`

  * **Method** : `google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores" `  




#### `UpdateDataStore`

  * **Method** : `google.cloud.discoveryengine.v1beta.DataStoreService.UpdateDataStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.dataStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.UpdateDataStore" `  




### `google.cloud.discoveryengine.v1beta.DocumentService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.DocumentService`.

#### `BatchGetDocumentsMetadata`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.BatchGetDocumentsMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.BatchGetDocumentsMetadata" `  




#### `CreateDocument`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument" `  




#### `DeleteDocument`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument" `  




#### `GetDocument`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.GetDocument" `  




#### `ImportDocuments`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments" `  




#### `ListDocuments`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments" `  




#### `PurgeDocuments`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument" `  




### `google.cloud.discoveryengine.v1beta.EngineService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.EngineService`.

#### `CreateEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.CreateEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.CreateEngine" `  




#### `DeleteEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine" `  




#### `GetEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.GetEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.GetEngine" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy" `  




#### `ListEngines`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.ListEngines`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.ListEngines" `  




#### `PauseEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.PauseEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.pause - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.PauseEngine" `  




#### `ResumeEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.resume - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy" `  




#### `TuneEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.TuneEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.engines.tune - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.TuneEngine" `  




#### `UpdateEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.engines.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine" `  




### `google.cloud.discoveryengine.v1beta.EvaluationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.EvaluationService`.

#### `CreateEvaluation`

  * **Method** : `google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluation" `  




#### `GetEvaluation`

  * **Method** : `google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation" `  




#### `ListEvaluationResults`

  * **Method** : `google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationResults" `  




#### `ListEvaluations`

  * **Method** : `google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.evaluations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluations" `  




### `google.cloud.discoveryengine.v1beta.GroundedGenerationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.GroundedGenerationService`.

#### `CheckGrounding`

  * **Method** : `google.cloud.discoveryengine.v1beta.GroundedGenerationService.CheckGrounding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.groundingConfigs.check - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.GroundedGenerationService.CheckGrounding" `  




### `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService`.

#### `CreateIdentityMappingStore`

  * **Method** : `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.CreateIdentityMappingStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.CreateIdentityMappingStore" `  




#### `DeleteIdentityMappingStore`

  * **Method** : `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.DeleteIdentityMappingStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.DeleteIdentityMappingStore" `  




#### `ImportIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ImportIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.importIdentityMappings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ImportIdentityMappings" `  




#### `ListIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ListIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.listIdentityMappings - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ListIdentityMappings" `  




#### `PurgeIdentityMappings`

  * **Method** : `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.PurgeIdentityMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.identityMappingStores.purgeIdentityMappings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.PurgeIdentityMappings" `  




### `google.cloud.discoveryengine.v1beta.LicenseConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.LicenseConfigService`.

#### `CreateLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig" `  




#### `DistributeLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.billingAccountLicenseConfigs.distribute - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig" `  




#### `GetLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig" `  




#### `RetractLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig" `  




#### `UpdateLicenseConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.licenseConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig" `  




### `google.cloud.discoveryengine.v1beta.ProjectService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ProjectService`.

#### `ProvisionProject`

  * **Method** : `google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.projects.provision - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject" `  




### `google.cloud.discoveryengine.v1beta.RankService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.RankService`.

#### `Rank`

  * **Method** : `google.cloud.discoveryengine.v1beta.RankService.Rank`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.rankingConfigs.rank - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.RankService.Rank" `  




### `google.cloud.discoveryengine.v1beta.RecommendationService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.RecommendationService`.

#### `Recommend`

  * **Method** : `google.cloud.discoveryengine.v1beta.RecommendationService.Recommend`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.recommend - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.RecommendationService.Recommend" `  




### `google.cloud.discoveryengine.v1beta.SampleQueryService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SampleQueryService`.

#### `CreateSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSampleQuery" `  




#### `DeleteSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSampleQuery" `  




#### `GetSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQueryService.GetSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.GetSampleQuery" `  




#### `ImportSampleQueries`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSampleQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSampleQueries" `  




#### `ListSampleQueries`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQueryService.ListSampleQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.ListSampleQueries" `  




#### `UpdateSampleQuery`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSampleQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQueries.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSampleQuery" `  




### `google.cloud.discoveryengine.v1beta.SampleQuerySetService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SampleQuerySetService`.

#### `CreateSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQuerySet" `  




#### `DeleteSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQuerySet" `  




#### `GetSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuerySet" `  




#### `ListSampleQuerySets`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets" `  




#### `UpdateSampleQuerySet`

  * **Method** : `google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sampleQuerySets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet" `  




### `google.cloud.discoveryengine.v1beta.SchemaService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SchemaService`.

#### `CreateSchema`

  * **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema" `  




#### `DeleteSchema`

  * **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema" `  




#### `GetSchema`

  * **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.GetSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.schemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.GetSchema" `  




#### `ListSchemas`

  * **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.schemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas" `  




#### `UpdateSchema`

  * **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.schemas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema" `  




### `google.cloud.discoveryengine.v1beta.SearchService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SearchService`.

#### `Search`

  * **Method** : `google.cloud.discoveryengine.v1beta.SearchService.Search`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.search - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchService.Search" `  




### `google.cloud.discoveryengine.v1beta.SearchTuningService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SearchTuningService`.

#### `ListCustomModels`

  * **Method** : `google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustomModels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.listCustomModels - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustomModels" `  




#### `TrainCustomModel`

  * **Method** : `google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustomModel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.dataStores.trainCustomModel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustomModel" `  




### `google.cloud.discoveryengine.v1beta.ServingConfigService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ServingConfigService`.

#### `CreateServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingConfig" `  




#### `DeleteServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingConfig" `  




#### `GetServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConfig" `  




#### `ListServingConfigs`

  * **Method** : `google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingConfigs" `  




#### `UpdateServingConfig`

  * **Method** : `google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.servingConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingConfig" `  




### `google.cloud.discoveryengine.v1beta.SessionService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SessionService`.

#### `CreateSession`

  * **Method** : `google.cloud.discoveryengine.v1beta.SessionService.CreateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.CreateSession" `  




#### `DeleteSession`

  * **Method** : `google.cloud.discoveryengine.v1beta.SessionService.DeleteSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.DeleteSession" `  




#### `GetSession`

  * **Method** : `google.cloud.discoveryengine.v1beta.SessionService.GetSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.GetSession" `  




#### `ListSessions`

  * **Method** : `google.cloud.discoveryengine.v1beta.SessionService.ListSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.ListSessions" `  




#### `UpdateSession`

  * **Method** : `google.cloud.discoveryengine.v1beta.SessionService.UpdateSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sessions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.UpdateSession" `  




### `google.cloud.discoveryengine.v1beta.SiteSearchEngineService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SiteSearchEngineService`.

#### `BatchCreateTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchCreateTargetSites`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.batchCreate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchCreateTargetSites" `  




#### `BatchVerifyTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchVerifyTargetSites`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.batchVerifyTargetSites - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchVerifyTargetSites" `  




#### `CreateSitemap`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateSitemap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateSitemap" `  




#### `CreateTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateTargetSite" `  




#### `DeleteSitemap`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteSitemap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteSitemap" `  




#### `DeleteTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteTargetSite" `  




#### `DisableAdvancedSiteSearch`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DisableAdvancedSiteSearch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DisableAdvancedSiteSearch" `  




#### `EnableAdvancedSiteSearch`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.EnableAdvancedSiteSearch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.EnableAdvancedSiteSearch" `  




#### `FetchDomainVerificationStatus`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchDomainVerificationStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchDomainVerificationStatus" `  




#### `FetchSitemaps`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchSitemaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sitemaps.fetch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchSitemaps" `  




#### `GetSiteSearchEngine`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSiteSearchEngine`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSiteSearchEngine" `  




#### `GetTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetTargetSite`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetTargetSite" `  




#### `ListTargetSites`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetSites`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.targetSites.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetSites" `  




#### `RecrawlUris`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.RecrawlUris`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.RecrawlUris" `  




#### `UpdateTargetSite`

  * **Method** : `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.UpdateTargetSite`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.targetSites.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.UpdateTargetSite" `  




### `google.cloud.discoveryengine.v1beta.UserEventService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.UserEventService`.

#### `ImportUserEvents`

  * **Method** : `google.cloud.discoveryengine.v1beta.UserEventService.ImportUserEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventService.ImportUserEvents" `  




#### `PurgeUserEvents`

  * **Method** : `google.cloud.discoveryengine.v1beta.UserEventService.PurgeUserEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventService.PurgeUserEvents" `  




#### `WriteUserEvent`

  * **Method** : `google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.userEvents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent" `  




### `google.cloud.discoveryengine.v1beta.UserLicenseService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.UserLicenseService`.

#### `BatchUpdateUserLicenses`

  * **Method** : `google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdateUserLicenses`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdateUserLicenses" `  




### `google.cloud.discoveryengine.v1beta.UserStoreService`

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.UserStoreService`.

#### `UpdateUserStore`

  * **Method** : `google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.userStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore" `  




### `google.cloud.notebooklm.v1alpha.AudioOverviewService`

The following audit logs are associated with methods belonging to `google.cloud.notebooklm.v1alpha.AudioOverviewService`.

#### `CreateAudioOverview`

  * **Method** : `google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudioOverview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.audioOverviews.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudioOverview" `  




#### `DeleteAudioOverview`

  * **Method** : `google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudioOverview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.audioOverviews.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudioOverview" `  




### `google.cloud.notebooklm.v1alpha.NotebookService`

The following audit logs are associated with methods belonging to `google.cloud.notebooklm.v1alpha.NotebookService`.

#### `CreateNotebook`

  * **Method** : `google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.notebooks.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook" `  




#### `GetNotebook`

  * **Method** : `google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.notebooks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook" `  




#### `ListRecentlyViewedNotebooks`

  * **Method** : `google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewedNotebooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.notebooks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewedNotebooks" `  




#### `ShareNotebook`

  * **Method** : `google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `discoveryengine.notebooks.getIamPolicy - ADMIN_WRITE`
    * `discoveryengine.notebooks.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook" `  




### `google.cloud.notebooklm.v1alpha.SourceService`

The following audit logs are associated with methods belonging to `google.cloud.notebooklm.v1alpha.SourceService`.

#### `BatchCreateSources`

  * **Method** : `google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sources.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources" `  




#### `GetSource`

  * **Method** : `google.cloud.notebooklm.v1alpha.SourceService.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.sources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.notebooklm.v1alpha.SourceService.GetSource" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.operations.cancel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `discoveryengine.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `a2a.v1.A2AService.CancelTask`
  * `a2a.v1.A2AService.CreateTaskPushNotificationConfig`
  * `a2a.v1.A2AService.DeleteTaskPushNotificationConfig`
  * `a2a.v1.A2AService.GetTask`
  * `a2a.v1.A2AService.GetTaskPushNotificationConfig`
  * `a2a.v1.A2AService.ListTaskPushNotificationConfig`
  * `a2a.v1.A2AService.TaskSubscription`
  * `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpDeleteRequest`
  * `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpGetRequest`
  * `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpPostRequest`
  * `google.cloud.discoveryengine.v1.SearchService.SearchLite`
  * `google.cloud.discoveryengine.v1.UserEventService.CollectUserEvent`
  * `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpDeleteRequest`
  * `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpGetRequest`
  * `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpPostRequest`
  * `google.cloud.discoveryengine.v1alpha.DataConnectorService.StartConnectorRun`
  * `google.cloud.discoveryengine.v1alpha.SearchService.SearchLite`
  * `google.cloud.discoveryengine.v1alpha.UserEventService.CollectUserEvent`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.LookupWidgetConfig`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAcquireAccessToken`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAcquireAndStoreRefreshToken`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAdvancedCompleteQuery`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAnswerQuery`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetCompleteQuery`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetConverseConversation`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetCreateSession`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetDeleteSession`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetDisconnectConnector`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetExecuteAction`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetGetSession`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetHomepageFetchDocuments`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetListSessions`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetSearch`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetStreamAnswerQuery`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetUpdateSession`
  * `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetWriteUserEvent`
  * `google.cloud.discoveryengine.v1beta.SearchService.SearchLite`
  * `google.cloud.discoveryengine.v1beta.UserEventService.CollectUserEvent`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
