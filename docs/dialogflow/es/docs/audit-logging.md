---
url: https://docs.cloud.google.com/dialogflow/es/docs/audit-logging/
title: Dialogflow audit logging \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:46.330055+00:00
---

# Dialogflow audit logging  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Dialogflow audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Dialogflow. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Dialogflow audit logs use the service name `dialogflow.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="dialogflow.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Dialogflow generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.dialogflow.cx.v3.Agents.ExportAgent`  
`google.cloud.dialogflow.cx.v3.Agents.GetAgent`  
`google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult`  
`google.cloud.dialogflow.cx.v3.Agents.GetGenerativeSettings`  
`google.cloud.dialogflow.cx.v3.Agents.ListAgents`  
`google.cloud.dialogflow.cx.v3.SecuritySettingsService.GetSecuritySettings`  
`google.cloud.dialogflow.cx.v3.SecuritySettingsService.ListSecuritySettings`  
`google.cloud.dialogflow.cx.v3beta1.Agents.ExportAgent`  
`google.cloud.dialogflow.cx.v3beta1.Agents.GetAgent`  
`google.cloud.dialogflow.cx.v3beta1.Agents.GetAgentValidationResult`  
`google.cloud.dialogflow.cx.v3beta1.Agents.GetGenerativeSettings`  
`google.cloud.dialogflow.cx.v3beta1.Agents.ListAgents`  
`google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.GetSecuritySettings`  
`google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.ListSecuritySettings`  
`google.cloud.dialogflow.v2.Agents.ExportAgent`  
`google.cloud.dialogflow.v2.Agents.GetAgent`  
`google.cloud.dialogflow.v2.Agents.GetValidationResult`  
`google.cloud.dialogflow.v2.Agents.SearchAgents`  
`google.cloud.dialogflow.v2.ConversationProfiles.GetConversationProfile`  
`google.cloud.dialogflow.v2.ConversationProfiles.ListConversationProfiles`  
`google.cloud.dialogflow.v2.Fulfillments.GetFulfillment`  
`google.cloud.dialogflow.v2.KnowledgeBases.GetKnowledgeBase`  
`google.cloud.dialogflow.v2.KnowledgeBases.ListKnowledgeBases`  
`google.cloud.dialogflow.v2beta1.Agents.ExportAgent`  
`google.cloud.dialogflow.v2beta1.Agents.GetAgent`  
`google.cloud.dialogflow.v2beta1.Agents.GetValidationResult`  
`google.cloud.dialogflow.v2beta1.Agents.SearchAgents`  
`google.cloud.dialogflow.v2beta1.ConversationProfiles.GetConversationProfile`  
`google.cloud.dialogflow.v2beta1.ConversationProfiles.ListConversationProfiles`  
`google.cloud.dialogflow.v2beta1.EncryptionSpecService.GetEncryptionSpec`  
`google.cloud.dialogflow.v2beta1.Fulfillments.GetFulfillment`  
`google.cloud.dialogflow.v2beta1.KnowledgeBases.GetKnowledgeBase`  
`google.cloud.dialogflow.v2beta1.KnowledgeBases.ListKnowledgeBases`  
`google.cloud.location.Locations.GetLocation`  
`google.cloud.location.Locations.ListLocations`  
`ADMIN_WRITE` | `google.cloud.dialogflow.cx.v3.Agents.CreateAgent`  
`google.cloud.dialogflow.cx.v3.Agents.DeleteAgent`  
`google.cloud.dialogflow.cx.v3.Agents.RestoreAgent`  
`google.cloud.dialogflow.cx.v3.Agents.UpdateAgent`  
`google.cloud.dialogflow.cx.v3.Agents.UpdateGenerativeSettings`  
`google.cloud.dialogflow.cx.v3.Agents.ValidateAgent`  
`google.cloud.dialogflow.cx.v3.SecuritySettingsService.CreateSecuritySettings`  
`google.cloud.dialogflow.cx.v3.SecuritySettingsService.DeleteSecuritySettings`  
`google.cloud.dialogflow.cx.v3.SecuritySettingsService.UpdateSecuritySettings`  
`google.cloud.dialogflow.cx.v3beta1.Agents.CreateAgent`  
`google.cloud.dialogflow.cx.v3beta1.Agents.DeleteAgent`  
`google.cloud.dialogflow.cx.v3beta1.Agents.RestoreAgent`  
`google.cloud.dialogflow.cx.v3beta1.Agents.UpdateAgent`  
`google.cloud.dialogflow.cx.v3beta1.Agents.UpdateGenerativeSettings`  
`google.cloud.dialogflow.cx.v3beta1.Agents.ValidateAgent`  
`google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.CreateSecuritySettings`  
`google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.DeleteSecuritySettings`  
`google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.UpdateSecuritySettings`  
`google.cloud.dialogflow.v2.Agents.DeleteAgent`  
`google.cloud.dialogflow.v2.Agents.ImportAgent`  
`google.cloud.dialogflow.v2.Agents.RestoreAgent`  
`google.cloud.dialogflow.v2.Agents.SetAgent`  
`google.cloud.dialogflow.v2.Agents.TrainAgent`  
`google.cloud.dialogflow.v2.ConversationProfiles.ClearSuggestionFeatureConfig`  
`google.cloud.dialogflow.v2.ConversationProfiles.CreateConversationProfile`  
`google.cloud.dialogflow.v2.ConversationProfiles.DeleteConversationProfile`  
`google.cloud.dialogflow.v2.ConversationProfiles.UpdateConversationProfile`  
`google.cloud.dialogflow.v2.Fulfillments.UpdateFulfillment`  
`google.cloud.dialogflow.v2.KnowledgeBases.CreateKnowledgeBase`  
`google.cloud.dialogflow.v2.KnowledgeBases.DeleteKnowledgeBase`  
`google.cloud.dialogflow.v2.KnowledgeBases.UpdateKnowledgeBase`  
`google.cloud.dialogflow.v2beta1.Agents.DeleteAgent`  
`google.cloud.dialogflow.v2beta1.Agents.ImportAgent`  
`google.cloud.dialogflow.v2beta1.Agents.RestoreAgent`  
`google.cloud.dialogflow.v2beta1.Agents.SetAgent`  
`google.cloud.dialogflow.v2beta1.Agents.TrainAgent`  
`google.cloud.dialogflow.v2beta1.ConversationProfiles.ClearSuggestionFeatureConfig`  
`google.cloud.dialogflow.v2beta1.ConversationProfiles.CreateConversationProfile`  
`google.cloud.dialogflow.v2beta1.ConversationProfiles.DeleteConversationProfile`  
`google.cloud.dialogflow.v2beta1.ConversationProfiles.SetSuggestionFeatureConfig`  
`google.cloud.dialogflow.v2beta1.ConversationProfiles.UpdateConversationProfile`  
`google.cloud.dialogflow.v2beta1.EncryptionSpecService.InitializeEncryptionSpec`  
`google.cloud.dialogflow.v2beta1.Fulfillments.UpdateFulfillment`  
`google.cloud.dialogflow.v2beta1.KnowledgeBases.CreateKnowledgeBase`  
`google.cloud.dialogflow.v2beta1.KnowledgeBases.DeleteKnowledgeBase`  
`google.cloud.dialogflow.v2beta1.KnowledgeBases.UpdateKnowledgeBase`  
`DATA_READ` | `google.cloud.dialogflow.cx.v3.Changelogs.GetChangelog`  
`google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogs`  
`google.cloud.dialogflow.cx.v3.Deployments.ListDeployments`  
`google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes`  
`google.cloud.dialogflow.cx.v3.EntityTypes.GetEntityType`  
`google.cloud.dialogflow.cx.v3.EntityTypes.ListEntityTypes`  
`google.cloud.dialogflow.cx.v3.Environments.GetEnvironment`  
`google.cloud.dialogflow.cx.v3.Environments.ListEnvironments`  
`google.cloud.dialogflow.cx.v3.Environments.LookupEnvironmentHistory`  
`google.cloud.dialogflow.cx.v3.Experiments.GetExperiment`  
`google.cloud.dialogflow.cx.v3.Experiments.ListExperiments`  
`google.cloud.dialogflow.cx.v3.Flows.ExportFlow`  
`google.cloud.dialogflow.cx.v3.Flows.GetFlow`  
`google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult`  
`google.cloud.dialogflow.cx.v3.Flows.ListFlows`  
`google.cloud.dialogflow.cx.v3.Generators.GetGenerator`  
`google.cloud.dialogflow.cx.v3.Generators.ListGenerators`  
`google.cloud.dialogflow.cx.v3.Intents.ExportIntents`  
`google.cloud.dialogflow.cx.v3.Intents.GetIntent`  
`google.cloud.dialogflow.cx.v3.Intents.ListIntents`  
`google.cloud.dialogflow.cx.v3.Pages.GetPage`  
`google.cloud.dialogflow.cx.v3.Pages.ListPages`  
`google.cloud.dialogflow.cx.v3.SessionEntityTypes.GetSessionEntityType`  
`google.cloud.dialogflow.cx.v3.SessionEntityTypes.ListSessionEntityTypes`  
`google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage`  
`google.cloud.dialogflow.cx.v3.TestCases.GetTestCase`  
`google.cloud.dialogflow.cx.v3.TestCases.ListTestCaseResults`  
`google.cloud.dialogflow.cx.v3.TestCases.ListTestCases`  
`google.cloud.dialogflow.cx.v3.TransitionRouteGroups.GetTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3.TransitionRouteGroups.ListTransitionRouteGroups`  
`google.cloud.dialogflow.cx.v3.Versions.CompareVersions`  
`google.cloud.dialogflow.cx.v3.Versions.GetVersion`  
`google.cloud.dialogflow.cx.v3.Versions.ListVersions`  
`google.cloud.dialogflow.cx.v3.Webhooks.GetWebhook`  
`google.cloud.dialogflow.cx.v3.Webhooks.ListWebhooks`  
`google.cloud.dialogflow.cx.v3beta1.Changelogs.ListChangelogs`  
`google.cloud.dialogflow.cx.v3beta1.ConversationHistory.GetConversation`  
`google.cloud.dialogflow.cx.v3beta1.ConversationHistory.ListConversations`  
`google.cloud.dialogflow.cx.v3beta1.EntityTypes.GetEntityType`  
`google.cloud.dialogflow.cx.v3beta1.EntityTypes.ListEntityTypes`  
`google.cloud.dialogflow.cx.v3beta1.Environments.GetEnvironment`  
`google.cloud.dialogflow.cx.v3beta1.Environments.ListEnvironments`  
`google.cloud.dialogflow.cx.v3beta1.Environments.LookupEnvironmentHistory`  
`google.cloud.dialogflow.cx.v3beta1.Examples.GetExample`  
`google.cloud.dialogflow.cx.v3beta1.Examples.ListExamples`  
`google.cloud.dialogflow.cx.v3beta1.Flows.ExportFlow`  
`google.cloud.dialogflow.cx.v3beta1.Flows.GetFlow`  
`google.cloud.dialogflow.cx.v3beta1.Flows.GetFlowValidationResult`  
`google.cloud.dialogflow.cx.v3beta1.Flows.ListFlows`  
`google.cloud.dialogflow.cx.v3beta1.Generators.GetGenerator`  
`google.cloud.dialogflow.cx.v3beta1.Generators.ListGenerators`  
`google.cloud.dialogflow.cx.v3beta1.Intents.GetIntent`  
`google.cloud.dialogflow.cx.v3beta1.Intents.ListIntents`  
`google.cloud.dialogflow.cx.v3beta1.Pages.GetPage`  
`google.cloud.dialogflow.cx.v3beta1.Pages.ListPages`  
`google.cloud.dialogflow.cx.v3beta1.Playbooks.GetPlaybook`  
`google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybookVersions`  
`google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybooks`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.CalculateCoverage`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.ExportTestCases`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.GetTestCase`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCaseResults`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCases`  
`google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.GetTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.ListTransitionRouteGroups`  
`google.cloud.dialogflow.cx.v3beta1.Versions.CompareVersions`  
`google.cloud.dialogflow.cx.v3beta1.Versions.GetVersion`  
`google.cloud.dialogflow.cx.v3beta1.Versions.ListVersions`  
`google.cloud.dialogflow.cx.v3beta1.Webhooks.GetWebhook`  
`google.cloud.dialogflow.cx.v3beta1.Webhooks.ListWebhooks`  
`google.cloud.dialogflow.v2.AnswerRecords.ListAnswerRecords`  
`google.cloud.dialogflow.v2.Contexts.GetContext`  
`google.cloud.dialogflow.v2.Contexts.ListContexts`  
`google.cloud.dialogflow.v2.ConversationModels.GetConversationModelEvaluation`  
`google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations`  
`google.cloud.dialogflow.v2.Conversations.CompleteConversation`  
`google.cloud.dialogflow.v2.Conversations.GenerateStatelessSuggestion`  
`google.cloud.dialogflow.v2.Conversations.GetConversation`  
`google.cloud.dialogflow.v2.Conversations.ListConversations`  
`google.cloud.dialogflow.v2.Conversations.ListMessages`  
`google.cloud.dialogflow.v2.Documents.ExportDocument`  
`google.cloud.dialogflow.v2.Documents.GetDocument`  
`google.cloud.dialogflow.v2.Documents.ListDocuments`  
`google.cloud.dialogflow.v2.EntityTypes.GetEntityType`  
`google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes`  
`google.cloud.dialogflow.v2.Environments.GetEnvironment`  
`google.cloud.dialogflow.v2.Environments.GetEnvironmentHistory`  
`google.cloud.dialogflow.v2.Environments.ListEnvironments`  
`google.cloud.dialogflow.v2.Generators.GetGenerator`  
`google.cloud.dialogflow.v2.Generators.ListGenerators`  
`google.cloud.dialogflow.v2.Intents.GetIntent`  
`google.cloud.dialogflow.v2.Intents.ListIntents`  
`google.cloud.dialogflow.v2.Participants.GetParticipant`  
`google.cloud.dialogflow.v2.Participants.ListParticipants`  
`google.cloud.dialogflow.v2.Participants.SuggestArticles`  
`google.cloud.dialogflow.v2.Participants.SuggestFaqAnswers`  
`google.cloud.dialogflow.v2.Participants.SuggestKnowledgeAssist`  
`google.cloud.dialogflow.v2.Participants.SuggestSmartReplies`  
`google.cloud.dialogflow.v2.SessionEntityTypes.GetSessionEntityType`  
`google.cloud.dialogflow.v2.SessionEntityTypes.ListSessionEntityTypes`  
`google.cloud.dialogflow.v2.Versions.GetVersion`  
`google.cloud.dialogflow.v2.Versions.ListVersions`  
`google.cloud.dialogflow.v2beta1.AnswerRecords.GetAnswerRecord`  
`google.cloud.dialogflow.v2beta1.AnswerRecords.ListAnswerRecords`  
`google.cloud.dialogflow.v2beta1.Contexts.GetContext`  
`google.cloud.dialogflow.v2beta1.Contexts.ListContexts`  
`google.cloud.dialogflow.v2beta1.Conversations.BatchCreateMessages`  
`google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation`  
`google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion`  
`google.cloud.dialogflow.v2beta1.Conversations.GetConversation`  
`google.cloud.dialogflow.v2beta1.Conversations.ListConversations`  
`google.cloud.dialogflow.v2beta1.Conversations.ListMessages`  
`google.cloud.dialogflow.v2beta1.Documents.GetDocument`  
`google.cloud.dialogflow.v2beta1.Documents.ListDocuments`  
`google.cloud.dialogflow.v2beta1.EntityTypes.GetEntityType`  
`google.cloud.dialogflow.v2beta1.EntityTypes.ListEntityTypes`  
`google.cloud.dialogflow.v2beta1.Environments.GetEnvironment`  
`google.cloud.dialogflow.v2beta1.Environments.GetEnvironmentHistory`  
`google.cloud.dialogflow.v2beta1.Environments.ListEnvironments`  
`google.cloud.dialogflow.v2beta1.Generators.GetGenerator`  
`google.cloud.dialogflow.v2beta1.Generators.ListGenerators`  
`google.cloud.dialogflow.v2beta1.Intents.GetIntent`  
`google.cloud.dialogflow.v2beta1.Intents.ListIntents`  
`google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion`  
`google.cloud.dialogflow.v2beta1.Participants.GetParticipant`  
`google.cloud.dialogflow.v2beta1.Participants.ListParticipants`  
`google.cloud.dialogflow.v2beta1.Participants.ListSuggestions`  
`google.cloud.dialogflow.v2beta1.Participants.SuggestArticles`  
`google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers`  
`google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist`  
`google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies`  
`google.cloud.dialogflow.v2beta1.SessionEntityTypes.GetSessionEntityType`  
`google.cloud.dialogflow.v2beta1.SessionEntityTypes.ListSessionEntityTypes`  
`google.cloud.dialogflow.v2beta1.Versions.GetVersion`  
`google.cloud.dialogflow.v2beta1.Versions.ListVersions`  
`google.longrunning.Operations.GetOperation`  
`DATA_WRITE` | `google.cloud.dialogflow.cx.v3.EntityTypes.CreateEntityType`  
`google.cloud.dialogflow.cx.v3.EntityTypes.DeleteEntityType`  
`google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes`  
`google.cloud.dialogflow.cx.v3.EntityTypes.UpdateEntityType`  
`google.cloud.dialogflow.cx.v3.Environments.CreateEnvironment`  
`google.cloud.dialogflow.cx.v3.Environments.DeleteEnvironment`  
`google.cloud.dialogflow.cx.v3.Environments.DeployFlow`  
`google.cloud.dialogflow.cx.v3.Environments.UpdateEnvironment`  
`google.cloud.dialogflow.cx.v3.Experiments.CreateExperiment`  
`google.cloud.dialogflow.cx.v3.Flows.CreateFlow`  
`google.cloud.dialogflow.cx.v3.Flows.DeleteFlow`  
`google.cloud.dialogflow.cx.v3.Flows.ImportFlow`  
`google.cloud.dialogflow.cx.v3.Flows.TrainFlow`  
`google.cloud.dialogflow.cx.v3.Flows.UpdateFlow`  
`google.cloud.dialogflow.cx.v3.Flows.ValidateFlow`  
`google.cloud.dialogflow.cx.v3.Generators.CreateGenerator`  
`google.cloud.dialogflow.cx.v3.Intents.CreateIntent`  
`google.cloud.dialogflow.cx.v3.Intents.DeleteIntent`  
`google.cloud.dialogflow.cx.v3.Intents.ImportIntents`  
`google.cloud.dialogflow.cx.v3.Intents.UpdateIntent`  
`google.cloud.dialogflow.cx.v3.Pages.CreatePage`  
`google.cloud.dialogflow.cx.v3.Pages.DeletePage`  
`google.cloud.dialogflow.cx.v3.Pages.UpdatePage`  
`google.cloud.dialogflow.cx.v3.SessionEntityTypes.CreateSessionEntityType`  
`google.cloud.dialogflow.cx.v3.SessionEntityTypes.UpdateSessionEntityType`  
`google.cloud.dialogflow.cx.v3.Sessions.DetectIntent`  
`google.cloud.dialogflow.cx.v3.Sessions.FulfillIntent`  
`google.cloud.dialogflow.cx.v3.Sessions.MatchIntent`  
`google.cloud.dialogflow.cx.v3.Sessions.ServerStreamingDetectIntent`  
`google.cloud.dialogflow.cx.v3.Sessions.StreamingDetectIntent`  
`google.cloud.dialogflow.cx.v3.Sessions.SubmitAnswerFeedback`  
`google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases`  
`google.cloud.dialogflow.cx.v3.TestCases.CreateTestCase`  
`google.cloud.dialogflow.cx.v3.TestCases.RunTestCase`  
`google.cloud.dialogflow.cx.v3.TestCases.UpdateTestCase`  
`google.cloud.dialogflow.cx.v3.TransitionRouteGroups.CreateTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3.TransitionRouteGroups.DeleteTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3.TransitionRouteGroups.UpdateTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3.Versions.CreateVersion`  
`google.cloud.dialogflow.cx.v3.Versions.DeleteVersion`  
`google.cloud.dialogflow.cx.v3.Versions.LoadVersion`  
`google.cloud.dialogflow.cx.v3.Versions.UpdateVersion`  
`google.cloud.dialogflow.cx.v3.Webhooks.CreateWebhook`  
`google.cloud.dialogflow.cx.v3.Webhooks.DeleteWebhook`  
`google.cloud.dialogflow.cx.v3.Webhooks.UpdateWebhook`  
`google.cloud.dialogflow.cx.v3beta1.EntityTypes.CreateEntityType`  
`google.cloud.dialogflow.cx.v3beta1.EntityTypes.DeleteEntityType`  
`google.cloud.dialogflow.cx.v3beta1.EntityTypes.UpdateEntityType`  
`google.cloud.dialogflow.cx.v3beta1.Environments.CreateEnvironment`  
`google.cloud.dialogflow.cx.v3beta1.Environments.DeployFlow`  
`google.cloud.dialogflow.cx.v3beta1.Environments.UpdateEnvironment`  
`google.cloud.dialogflow.cx.v3beta1.Examples.CreateExample`  
`google.cloud.dialogflow.cx.v3beta1.Examples.UpdateExample`  
`google.cloud.dialogflow.cx.v3beta1.Flows.CreateFlow`  
`google.cloud.dialogflow.cx.v3beta1.Flows.DeleteFlow`  
`google.cloud.dialogflow.cx.v3beta1.Flows.ImportFlow`  
`google.cloud.dialogflow.cx.v3beta1.Flows.TrainFlow`  
`google.cloud.dialogflow.cx.v3beta1.Flows.UpdateFlow`  
`google.cloud.dialogflow.cx.v3beta1.Flows.ValidateFlow`  
`google.cloud.dialogflow.cx.v3beta1.Generators.CreateGenerator`  
`google.cloud.dialogflow.cx.v3beta1.Generators.UpdateGenerator`  
`google.cloud.dialogflow.cx.v3beta1.Intents.CreateIntent`  
`google.cloud.dialogflow.cx.v3beta1.Intents.DeleteIntent`  
`google.cloud.dialogflow.cx.v3beta1.Intents.UpdateIntent`  
`google.cloud.dialogflow.cx.v3beta1.Pages.CreatePage`  
`google.cloud.dialogflow.cx.v3beta1.Pages.DeletePage`  
`google.cloud.dialogflow.cx.v3beta1.Pages.UpdatePage`  
`google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybook`  
`google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybookVersion`  
`google.cloud.dialogflow.cx.v3beta1.Playbooks.DeletePlaybookVersion`  
`google.cloud.dialogflow.cx.v3beta1.Playbooks.UpdatePlaybook`  
`google.cloud.dialogflow.cx.v3beta1.Sessions.DetectIntent`  
`google.cloud.dialogflow.cx.v3beta1.Sessions.MatchIntent`  
`google.cloud.dialogflow.cx.v3beta1.Sessions.ServerStreamingDetectIntent`  
`google.cloud.dialogflow.cx.v3beta1.Sessions.StreamingDetectIntent`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.BatchDeleteTestCases`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.BatchRunTestCases`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.ImportTestCases`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.RunTestCase`  
`google.cloud.dialogflow.cx.v3beta1.TestCases.UpdateTestCase`  
`google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.CreateTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.DeleteTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.UpdateTransitionRouteGroup`  
`google.cloud.dialogflow.cx.v3beta1.Versions.CreateVersion`  
`google.cloud.dialogflow.cx.v3beta1.Versions.DeleteVersion`  
`google.cloud.dialogflow.cx.v3beta1.Webhooks.CreateWebhook`  
`google.cloud.dialogflow.cx.v3beta1.Webhooks.DeleteWebhook`  
`google.cloud.dialogflow.cx.v3beta1.Webhooks.UpdateWebhook`  
`google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord`  
`google.cloud.dialogflow.v2.Contexts.CreateContext`  
`google.cloud.dialogflow.v2.Contexts.DeleteAllContexts`  
`google.cloud.dialogflow.v2.Contexts.DeleteContext`  
`google.cloud.dialogflow.v2.Contexts.UpdateContext`  
`google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluation`  
`google.cloud.dialogflow.v2.Conversations.CreateConversation`  
`google.cloud.dialogflow.v2.Documents.CreateDocument`  
`google.cloud.dialogflow.v2.Documents.DeleteDocument`  
`google.cloud.dialogflow.v2.Documents.ImportDocuments`  
`google.cloud.dialogflow.v2.Documents.ReloadDocument`  
`google.cloud.dialogflow.v2.Documents.UpdateDocument`  
`google.cloud.dialogflow.v2.EntityTypes.BatchCreateEntities`  
`google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntities`  
`google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntityTypes`  
`google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntities`  
`google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes`  
`google.cloud.dialogflow.v2.EntityTypes.CreateEntityType`  
`google.cloud.dialogflow.v2.EntityTypes.DeleteEntityType`  
`google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType`  
`google.cloud.dialogflow.v2.Environments.CreateEnvironment`  
`google.cloud.dialogflow.v2.Environments.DeleteEnvironment`  
`google.cloud.dialogflow.v2.Environments.UpdateEnvironment`  
`google.cloud.dialogflow.v2.Generators.CreateGenerator`  
`google.cloud.dialogflow.v2.Generators.DeleteGenerator`  
`google.cloud.dialogflow.v2.Generators.UpdateGenerator`  
`google.cloud.dialogflow.v2.Intents.BatchDeleteIntents`  
`google.cloud.dialogflow.v2.Intents.BatchUpdateIntents`  
`google.cloud.dialogflow.v2.Intents.CreateIntent`  
`google.cloud.dialogflow.v2.Intents.DeleteIntent`  
`google.cloud.dialogflow.v2.Intents.UpdateIntent`  
`google.cloud.dialogflow.v2.Participants.AnalyzeContent`  
`google.cloud.dialogflow.v2.Participants.CreateParticipant`  
`google.cloud.dialogflow.v2.Participants.StreamingAnalyzeContent`  
`google.cloud.dialogflow.v2.Participants.UpdateParticipant`  
`google.cloud.dialogflow.v2.SessionEntityTypes.CreateSessionEntityType`  
`google.cloud.dialogflow.v2.SessionEntityTypes.DeleteSessionEntityType`  
`google.cloud.dialogflow.v2.SessionEntityTypes.UpdateSessionEntityType`  
`google.cloud.dialogflow.v2.Sessions.DetectIntent`  
`google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent`  
`google.cloud.dialogflow.v2.Versions.CreateVersion`  
`google.cloud.dialogflow.v2.Versions.DeleteVersion`  
`google.cloud.dialogflow.v2.Versions.UpdateVersion`  
`google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord`  
`google.cloud.dialogflow.v2beta1.Contexts.CreateContext`  
`google.cloud.dialogflow.v2beta1.Contexts.DeleteAllContexts`  
`google.cloud.dialogflow.v2beta1.Contexts.DeleteContext`  
`google.cloud.dialogflow.v2beta1.Contexts.UpdateContext`  
`google.cloud.dialogflow.v2beta1.Conversations.CreateConversation`  
`google.cloud.dialogflow.v2beta1.Documents.CreateDocument`  
`google.cloud.dialogflow.v2beta1.Documents.DeleteDocument`  
`google.cloud.dialogflow.v2beta1.Documents.ImportDocuments`  
`google.cloud.dialogflow.v2beta1.Documents.ReloadDocument`  
`google.cloud.dialogflow.v2beta1.Documents.UpdateDocument`  
`google.cloud.dialogflow.v2beta1.EntityTypes.BatchCreateEntities`  
`google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntities`  
`google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntityTypes`  
`google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntities`  
`google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntityTypes`  
`google.cloud.dialogflow.v2beta1.EntityTypes.CreateEntityType`  
`google.cloud.dialogflow.v2beta1.EntityTypes.DeleteEntityType`  
`google.cloud.dialogflow.v2beta1.EntityTypes.UpdateEntityType`  
`google.cloud.dialogflow.v2beta1.Environments.CreateEnvironment`  
`google.cloud.dialogflow.v2beta1.Environments.DeleteEnvironment`  
`google.cloud.dialogflow.v2beta1.Environments.UpdateEnvironment`  
`google.cloud.dialogflow.v2beta1.Generators.CreateGenerator`  
`google.cloud.dialogflow.v2beta1.Generators.DeleteGenerator`  
`google.cloud.dialogflow.v2beta1.Generators.UpdateGenerator`  
`google.cloud.dialogflow.v2beta1.Intents.BatchDeleteIntents`  
`google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents`  
`google.cloud.dialogflow.v2beta1.Intents.CreateIntent`  
`google.cloud.dialogflow.v2beta1.Intents.DeleteIntent`  
`google.cloud.dialogflow.v2beta1.Intents.UpdateIntent`  
`google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent`  
`google.cloud.dialogflow.v2beta1.Participants.CreateParticipant`  
`google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent`  
`google.cloud.dialogflow.v2beta1.Participants.UpdateParticipant`  
`google.cloud.dialogflow.v2beta1.SessionEntityTypes.CreateSessionEntityType`  
`google.cloud.dialogflow.v2beta1.SessionEntityTypes.DeleteSessionEntityType`  
`google.cloud.dialogflow.v2beta1.SessionEntityTypes.UpdateSessionEntityType`  
`google.cloud.dialogflow.v2beta1.Sessions.DetectIntent`  
`google.cloud.dialogflow.v2beta1.Sessions.StreamingDetectIntent`  
`google.cloud.dialogflow.v2beta1.Versions.CreateVersion`  
`google.cloud.dialogflow.v2beta1.Versions.DeleteVersion`  
`google.cloud.dialogflow.v2beta1.Versions.UpdateVersion`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Dialogflow.

### `google.cloud.dialogflow.cx.v3.Agents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Agents`.

#### `CreateAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.CreateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.CreateAgent" `  




#### `DeleteAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.DeleteAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.DeleteAgent" `  




#### `ExportAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.ExportAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.ExportAgent" `  




#### `GetAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.GetAgent" `  




#### `GetAgentValidationResult`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult" `  




#### `GetGenerativeSettings`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.GetGenerativeSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.GetGenerativeSettings" `  




#### `ListAgents`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.ListAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.ListAgents" `  




#### `RestoreAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.RestoreAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.RestoreAgent" `  




#### `UpdateAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.UpdateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.UpdateAgent" `  




#### `UpdateGenerativeSettings`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.UpdateGenerativeSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.UpdateGenerativeSettings" `  




#### `ValidateAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Agents.ValidateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.validate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Agents.ValidateAgent" `  




### `google.cloud.dialogflow.cx.v3.Changelogs`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Changelogs`.

#### `GetChangelog`

  * **Method** : `google.cloud.dialogflow.cx.v3.Changelogs.GetChangelog`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.changelogs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Changelogs.GetChangelog" `  




#### `ListChangelogs`

  * **Method** : `google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.changelogs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogs" `  




### `google.cloud.dialogflow.cx.v3.Deployments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Deployments`.

#### `ListDeployments`

  * **Method** : `google.cloud.dialogflow.cx.v3.Deployments.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.deployments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Deployments.ListDeployments" `  




### `google.cloud.dialogflow.cx.v3.EntityTypes`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.EntityTypes`.

#### `CreateEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3.EntityTypes.CreateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.EntityTypes.CreateEntityType" `  




#### `DeleteEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3.EntityTypes.DeleteEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.EntityTypes.DeleteEntityType" `  




#### `ExportEntityTypes`

  * **Method** : `google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes" `  




#### `GetEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3.EntityTypes.GetEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.EntityTypes.GetEntityType" `  




#### `ImportEntityTypes`

  * **Method** : `google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes" `  




#### `ListEntityTypes`

  * **Method** : `google.cloud.dialogflow.cx.v3.EntityTypes.ListEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.EntityTypes.ListEntityTypes" `  




#### `UpdateEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3.EntityTypes.UpdateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.EntityTypes.UpdateEntityType" `  




### `google.cloud.dialogflow.cx.v3.Environments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Environments`.

#### `CreateEnvironment`

  * **Method** : `google.cloud.dialogflow.cx.v3.Environments.CreateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Environments.CreateEnvironment" `  




#### `DeleteEnvironment`

  * **Method** : `google.cloud.dialogflow.cx.v3.Environments.DeleteEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Environments.DeleteEnvironment" `  




#### `DeployFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Environments.DeployFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Environments.DeployFlow" `  




#### `GetEnvironment`

  * **Method** : `google.cloud.dialogflow.cx.v3.Environments.GetEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Environments.GetEnvironment" `  




#### `ListEnvironments`

  * **Method** : `google.cloud.dialogflow.cx.v3.Environments.ListEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Environments.ListEnvironments" `  




#### `LookupEnvironmentHistory`

  * **Method** : `google.cloud.dialogflow.cx.v3.Environments.LookupEnvironmentHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.lookupHistory - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Environments.LookupEnvironmentHistory" `  




#### `UpdateEnvironment`

  * **Method** : `google.cloud.dialogflow.cx.v3.Environments.UpdateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Environments.UpdateEnvironment" `  




### `google.cloud.dialogflow.cx.v3.Experiments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Experiments`.

#### `CreateExperiment`

  * **Method** : `google.cloud.dialogflow.cx.v3.Experiments.CreateExperiment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.experiments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Experiments.CreateExperiment" `  




#### `GetExperiment`

  * **Method** : `google.cloud.dialogflow.cx.v3.Experiments.GetExperiment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.experiments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Experiments.GetExperiment" `  




#### `ListExperiments`

  * **Method** : `google.cloud.dialogflow.cx.v3.Experiments.ListExperiments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.experiments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Experiments.ListExperiments" `  




### `google.cloud.dialogflow.cx.v3.Flows`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Flows`.

#### `CreateFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.CreateFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.CreateFlow" `  




#### `DeleteFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.DeleteFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.DeleteFlow" `  




#### `ExportFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.ExportFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.ExportFlow" `  




#### `GetFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.GetFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.GetFlow" `  




#### `GetFlowValidationResult`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult" `  




#### `ImportFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.ImportFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.ImportFlow" `  




#### `ListFlows`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.ListFlows`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.ListFlows" `  




#### `TrainFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.TrainFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.train - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.TrainFlow" `  




#### `UpdateFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.UpdateFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.UpdateFlow" `  




#### `ValidateFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3.Flows.ValidateFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.validate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Flows.ValidateFlow" `  




### `google.cloud.dialogflow.cx.v3.Generators`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Generators`.

#### `CreateGenerator`

  * **Method** : `google.cloud.dialogflow.cx.v3.Generators.CreateGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Generators.CreateGenerator" `  




#### `GetGenerator`

  * **Method** : `google.cloud.dialogflow.cx.v3.Generators.GetGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Generators.GetGenerator" `  




#### `ListGenerators`

  * **Method** : `google.cloud.dialogflow.cx.v3.Generators.ListGenerators`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Generators.ListGenerators" `  




### `google.cloud.dialogflow.cx.v3.Intents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Intents`.

#### `CreateIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Intents.CreateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Intents.CreateIntent" `  




#### `DeleteIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Intents.DeleteIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Intents.DeleteIntent" `  




#### `ExportIntents`

  * **Method** : `google.cloud.dialogflow.cx.v3.Intents.ExportIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Intents.ExportIntents" `  




#### `GetIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Intents.GetIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Intents.GetIntent" `  




#### `ImportIntents`

  * **Method** : `google.cloud.dialogflow.cx.v3.Intents.ImportIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Intents.ImportIntents" `  




#### `ListIntents`

  * **Method** : `google.cloud.dialogflow.cx.v3.Intents.ListIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Intents.ListIntents" `  




#### `UpdateIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Intents.UpdateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Intents.UpdateIntent" `  




### `google.cloud.dialogflow.cx.v3.Pages`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Pages`.

#### `CreatePage`

  * **Method** : `google.cloud.dialogflow.cx.v3.Pages.CreatePage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Pages.CreatePage" `  




#### `DeletePage`

  * **Method** : `google.cloud.dialogflow.cx.v3.Pages.DeletePage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Pages.DeletePage" `  




#### `GetPage`

  * **Method** : `google.cloud.dialogflow.cx.v3.Pages.GetPage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Pages.GetPage" `  




#### `ListPages`

  * **Method** : `google.cloud.dialogflow.cx.v3.Pages.ListPages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Pages.ListPages" `  




#### `UpdatePage`

  * **Method** : `google.cloud.dialogflow.cx.v3.Pages.UpdatePage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Pages.UpdatePage" `  




### `google.cloud.dialogflow.cx.v3.SecuritySettingsService`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.SecuritySettingsService`.

#### `CreateSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3.SecuritySettingsService.CreateSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.securitySettings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SecuritySettingsService.CreateSecuritySettings" `  




#### `DeleteSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3.SecuritySettingsService.DeleteSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.securitySettings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SecuritySettingsService.DeleteSecuritySettings" `  




#### `GetSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3.SecuritySettingsService.GetSecuritySettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.securitySettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SecuritySettingsService.GetSecuritySettings" `  




#### `ListSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3.SecuritySettingsService.ListSecuritySettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.securitySettings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SecuritySettingsService.ListSecuritySettings" `  




#### `UpdateSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3.SecuritySettingsService.UpdateSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.securitySettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SecuritySettingsService.UpdateSecuritySettings" `  




### `google.cloud.dialogflow.cx.v3.SessionEntityTypes`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.SessionEntityTypes`.

#### `CreateSessionEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3.SessionEntityTypes.CreateSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SessionEntityTypes.CreateSessionEntityType" `  




#### `GetSessionEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3.SessionEntityTypes.GetSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SessionEntityTypes.GetSessionEntityType" `  




#### `ListSessionEntityTypes`

  * **Method** : `google.cloud.dialogflow.cx.v3.SessionEntityTypes.ListSessionEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SessionEntityTypes.ListSessionEntityTypes" `  




#### `UpdateSessionEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3.SessionEntityTypes.UpdateSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.SessionEntityTypes.UpdateSessionEntityType" `  




### `google.cloud.dialogflow.cx.v3.Sessions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Sessions`.

#### `DetectIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Sessions.DetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Sessions.DetectIntent" `  




#### `FulfillIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Sessions.FulfillIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Sessions.FulfillIntent" `  




#### `MatchIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Sessions.MatchIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Sessions.MatchIntent" `  




#### `ServerStreamingDetectIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Sessions.ServerStreamingDetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Sessions.ServerStreamingDetectIntent" `  




#### `StreamingDetectIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3.Sessions.StreamingDetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.streamingDetectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Sessions.StreamingDetectIntent" `  




#### `SubmitAnswerFeedback`

  * **Method** : `google.cloud.dialogflow.cx.v3.Sessions.SubmitAnswerFeedback`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Sessions.SubmitAnswerFeedback" `  




### `google.cloud.dialogflow.cx.v3.TestCases`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.TestCases`.

#### `BatchRunTestCases`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases" `  




#### `CalculateCoverage`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.calculateCoverage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage" `  




#### `CreateTestCase`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.CreateTestCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.CreateTestCase" `  




#### `GetTestCase`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.GetTestCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.GetTestCase" `  




#### `ListTestCaseResults`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.ListTestCaseResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.ListTestCaseResults" `  




#### `ListTestCases`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.ListTestCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.ListTestCases" `  




#### `RunTestCase`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.RunTestCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.RunTestCase" `  




#### `UpdateTestCase`

  * **Method** : `google.cloud.dialogflow.cx.v3.TestCases.UpdateTestCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TestCases.UpdateTestCase" `  




### `google.cloud.dialogflow.cx.v3.TransitionRouteGroups`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.TransitionRouteGroups`.

#### `CreateTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3.TransitionRouteGroups.CreateTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TransitionRouteGroups.CreateTransitionRouteGroup" `  




#### `DeleteTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3.TransitionRouteGroups.DeleteTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TransitionRouteGroups.DeleteTransitionRouteGroup" `  




#### `GetTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3.TransitionRouteGroups.GetTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TransitionRouteGroups.GetTransitionRouteGroup" `  




#### `ListTransitionRouteGroups`

  * **Method** : `google.cloud.dialogflow.cx.v3.TransitionRouteGroups.ListTransitionRouteGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TransitionRouteGroups.ListTransitionRouteGroups" `  




#### `UpdateTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3.TransitionRouteGroups.UpdateTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.TransitionRouteGroups.UpdateTransitionRouteGroup" `  




### `google.cloud.dialogflow.cx.v3.Versions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Versions`.

#### `CompareVersions`

  * **Method** : `google.cloud.dialogflow.cx.v3.Versions.CompareVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Versions.CompareVersions" `  




#### `CreateVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3.Versions.CreateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Versions.CreateVersion" `  




#### `DeleteVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3.Versions.DeleteVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Versions.DeleteVersion" `  




#### `GetVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3.Versions.GetVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Versions.GetVersion" `  




#### `ListVersions`

  * **Method** : `google.cloud.dialogflow.cx.v3.Versions.ListVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Versions.ListVersions" `  




#### `LoadVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3.Versions.LoadVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.load - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Versions.LoadVersion" `  




#### `UpdateVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3.Versions.UpdateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Versions.UpdateVersion" `  




### `google.cloud.dialogflow.cx.v3.Webhooks`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3.Webhooks`.

#### `CreateWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3.Webhooks.CreateWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Webhooks.CreateWebhook" `  




#### `DeleteWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3.Webhooks.DeleteWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Webhooks.DeleteWebhook" `  




#### `GetWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3.Webhooks.GetWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Webhooks.GetWebhook" `  




#### `ListWebhooks`

  * **Method** : `google.cloud.dialogflow.cx.v3.Webhooks.ListWebhooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Webhooks.ListWebhooks" `  




#### `UpdateWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3.Webhooks.UpdateWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3.Webhooks.UpdateWebhook" `  




### `google.cloud.dialogflow.cx.v3beta1.Agents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Agents`.

#### `CreateAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.CreateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.CreateAgent" `  




#### `DeleteAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.DeleteAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.DeleteAgent" `  




#### `ExportAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.ExportAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.ExportAgent" `  




#### `GetAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.GetAgent" `  




#### `GetAgentValidationResult`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.GetAgentValidationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.GetAgentValidationResult" `  




#### `GetGenerativeSettings`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.GetGenerativeSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.GetGenerativeSettings" `  




#### `ListAgents`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.ListAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.ListAgents" `  




#### `RestoreAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.RestoreAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.RestoreAgent" `  




#### `UpdateAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.UpdateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.UpdateAgent" `  




#### `UpdateGenerativeSettings`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.UpdateGenerativeSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.UpdateGenerativeSettings" `  




#### `ValidateAgent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Agents.ValidateAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.validate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Agents.ValidateAgent" `  




### `google.cloud.dialogflow.cx.v3beta1.Changelogs`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Changelogs`.

#### `ListChangelogs`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Changelogs.ListChangelogs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.changelogs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Changelogs.ListChangelogs" `  




### `google.cloud.dialogflow.cx.v3beta1.ConversationHistory`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.ConversationHistory`.

#### `GetConversation`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.ConversationHistory.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.ConversationHistory.GetConversation" `  




#### `ListConversations`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.ConversationHistory.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.ConversationHistory.ListConversations" `  




### `google.cloud.dialogflow.cx.v3beta1.EntityTypes`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.EntityTypes`.

#### `CreateEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.EntityTypes.CreateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.EntityTypes.CreateEntityType" `  




#### `DeleteEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.EntityTypes.DeleteEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.EntityTypes.DeleteEntityType" `  




#### `GetEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.EntityTypes.GetEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.EntityTypes.GetEntityType" `  




#### `ListEntityTypes`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.EntityTypes.ListEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.EntityTypes.ListEntityTypes" `  




#### `UpdateEntityType`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.EntityTypes.UpdateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.EntityTypes.UpdateEntityType" `  




### `google.cloud.dialogflow.cx.v3beta1.Environments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Environments`.

#### `CreateEnvironment`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Environments.CreateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Environments.CreateEnvironment" `  




#### `DeployFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Environments.DeployFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Environments.DeployFlow" `  




#### `GetEnvironment`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Environments.GetEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Environments.GetEnvironment" `  




#### `ListEnvironments`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Environments.ListEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Environments.ListEnvironments" `  




#### `LookupEnvironmentHistory`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Environments.LookupEnvironmentHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.lookupHistory - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Environments.LookupEnvironmentHistory" `  




#### `UpdateEnvironment`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Environments.UpdateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Environments.UpdateEnvironment" `  




### `google.cloud.dialogflow.cx.v3beta1.Examples`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Examples`.

#### `CreateExample`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Examples.CreateExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.examples.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Examples.CreateExample" `  




#### `GetExample`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Examples.GetExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.examples.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Examples.GetExample" `  




#### `ListExamples`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Examples.ListExamples`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.examples.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Examples.ListExamples" `  




#### `UpdateExample`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Examples.UpdateExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.examples.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Examples.UpdateExample" `  




### `google.cloud.dialogflow.cx.v3beta1.Flows`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Flows`.

#### `CreateFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.CreateFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.CreateFlow" `  




#### `DeleteFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.DeleteFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.DeleteFlow" `  




#### `ExportFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.ExportFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.ExportFlow" `  




#### `GetFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.GetFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.GetFlow" `  




#### `GetFlowValidationResult`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.GetFlowValidationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.GetFlowValidationResult" `  




#### `ImportFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.ImportFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.ImportFlow" `  




#### `ListFlows`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.ListFlows`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.ListFlows" `  




#### `TrainFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.TrainFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.train - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.TrainFlow" `  




#### `UpdateFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.UpdateFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.UpdateFlow" `  




#### `ValidateFlow`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Flows.ValidateFlow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.flows.validate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Flows.ValidateFlow" `  




### `google.cloud.dialogflow.cx.v3beta1.Generators`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Generators`.

#### `CreateGenerator`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Generators.CreateGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Generators.CreateGenerator" `  




#### `GetGenerator`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Generators.GetGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Generators.GetGenerator" `  




#### `ListGenerators`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Generators.ListGenerators`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Generators.ListGenerators" `  




#### `UpdateGenerator`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Generators.UpdateGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Generators.UpdateGenerator" `  




### `google.cloud.dialogflow.cx.v3beta1.Intents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Intents`.

#### `CreateIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Intents.CreateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Intents.CreateIntent" `  




#### `DeleteIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Intents.DeleteIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Intents.DeleteIntent" `  




#### `GetIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Intents.GetIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Intents.GetIntent" `  




#### `ListIntents`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Intents.ListIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Intents.ListIntents" `  




#### `UpdateIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Intents.UpdateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Intents.UpdateIntent" `  




### `google.cloud.dialogflow.cx.v3beta1.Pages`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Pages`.

#### `CreatePage`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Pages.CreatePage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Pages.CreatePage" `  




#### `DeletePage`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Pages.DeletePage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Pages.DeletePage" `  




#### `GetPage`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Pages.GetPage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Pages.GetPage" `  




#### `ListPages`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Pages.ListPages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Pages.ListPages" `  




#### `UpdatePage`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Pages.UpdatePage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.pages.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Pages.UpdatePage" `  




### `google.cloud.dialogflow.cx.v3beta1.Playbooks`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Playbooks`.

#### `CreatePlaybook`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.playbooks.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybook" `  




#### `CreatePlaybookVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybookVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.playbooks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybookVersion" `  




#### `DeletePlaybookVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Playbooks.DeletePlaybookVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.playbooks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Playbooks.DeletePlaybookVersion" `  




#### `GetPlaybook`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Playbooks.GetPlaybook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.playbooks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Playbooks.GetPlaybook" `  




#### `ListPlaybookVersions`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybookVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.playbooks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybookVersions" `  




#### `ListPlaybooks`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.playbooks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybooks" `  




#### `UpdatePlaybook`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Playbooks.UpdatePlaybook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.playbooks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Playbooks.UpdatePlaybook" `  




### `google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService`.

#### `CreateSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.CreateSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.securitySettings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.CreateSecuritySettings" `  




#### `DeleteSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.DeleteSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.securitySettings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.DeleteSecuritySettings" `  




#### `GetSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.GetSecuritySettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.securitySettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.GetSecuritySettings" `  




#### `ListSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.ListSecuritySettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.securitySettings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.ListSecuritySettings" `  




#### `UpdateSecuritySettings`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.UpdateSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.securitySettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.SecuritySettingsService.UpdateSecuritySettings" `  




### `google.cloud.dialogflow.cx.v3beta1.Sessions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Sessions`.

#### `DetectIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Sessions.DetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Sessions.DetectIntent" `  




#### `MatchIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Sessions.MatchIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Sessions.MatchIntent" `  




#### `ServerStreamingDetectIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Sessions.ServerStreamingDetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Sessions.ServerStreamingDetectIntent" `  




#### `StreamingDetectIntent`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Sessions.StreamingDetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.streamingDetectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Sessions.StreamingDetectIntent" `  




### `google.cloud.dialogflow.cx.v3beta1.TestCases`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.TestCases`.

#### `BatchDeleteTestCases`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.BatchDeleteTestCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.BatchDeleteTestCases" `  




#### `BatchRunTestCases`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.BatchRunTestCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.BatchRunTestCases" `  




#### `CalculateCoverage`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.CalculateCoverage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.calculateCoverage - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.CalculateCoverage" `  




#### `ExportTestCases`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.ExportTestCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.export - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.ExportTestCases" `  




#### `GetTestCase`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.GetTestCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.GetTestCase" `  




#### `ImportTestCases`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.ImportTestCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.ImportTestCases" `  




#### `ListTestCaseResults`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCaseResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCaseResults" `  




#### `ListTestCases`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.ListTestCases" `  




#### `RunTestCase`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.RunTestCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.RunTestCase" `  




#### `UpdateTestCase`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TestCases.UpdateTestCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.testcases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TestCases.UpdateTestCase" `  




### `google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups`.

#### `CreateTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.CreateTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.CreateTransitionRouteGroup" `  




#### `DeleteTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.DeleteTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.DeleteTransitionRouteGroup" `  




#### `GetTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.GetTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.GetTransitionRouteGroup" `  




#### `ListTransitionRouteGroups`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.ListTransitionRouteGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.ListTransitionRouteGroups" `  




#### `UpdateTransitionRouteGroup`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.UpdateTransitionRouteGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.transitionRouteGroups.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.TransitionRouteGroups.UpdateTransitionRouteGroup" `  




### `google.cloud.dialogflow.cx.v3beta1.Versions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Versions`.

#### `CompareVersions`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Versions.CompareVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Versions.CompareVersions" `  




#### `CreateVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Versions.CreateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Versions.CreateVersion" `  




#### `DeleteVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Versions.DeleteVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Versions.DeleteVersion" `  




#### `GetVersion`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Versions.GetVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Versions.GetVersion" `  




#### `ListVersions`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Versions.ListVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Versions.ListVersions" `  




### `google.cloud.dialogflow.cx.v3beta1.Webhooks`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.cx.v3beta1.Webhooks`.

#### `CreateWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Webhooks.CreateWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Webhooks.CreateWebhook" `  




#### `DeleteWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Webhooks.DeleteWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Webhooks.DeleteWebhook" `  




#### `GetWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Webhooks.GetWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Webhooks.GetWebhook" `  




#### `ListWebhooks`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Webhooks.ListWebhooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Webhooks.ListWebhooks" `  




#### `UpdateWebhook`

  * **Method** : `google.cloud.dialogflow.cx.v3beta1.Webhooks.UpdateWebhook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.webhooks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.cx.v3beta1.Webhooks.UpdateWebhook" `  




### `google.cloud.dialogflow.v2.Agents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Agents`.

#### `DeleteAgent`

  * **Method** : `google.cloud.dialogflow.v2.Agents.DeleteAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.DeleteAgent" `  




#### `ExportAgent`

  * **Method** : `google.cloud.dialogflow.v2.Agents.ExportAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.ExportAgent" `  




#### `GetAgent`

  * **Method** : `google.cloud.dialogflow.v2.Agents.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.GetAgent" `  




#### `GetValidationResult`

  * **Method** : `google.cloud.dialogflow.v2.Agents.GetValidationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.GetValidationResult" `  




#### `ImportAgent`

  * **Method** : `google.cloud.dialogflow.v2.Agents.ImportAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.ImportAgent" `  




#### `RestoreAgent`

  * **Method** : `google.cloud.dialogflow.v2.Agents.RestoreAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.RestoreAgent" `  




#### `SearchAgents`

  * **Method** : `google.cloud.dialogflow.v2.Agents.SearchAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.SearchAgents" `  




#### `SetAgent`

  * **Method** : `google.cloud.dialogflow.v2.Agents.SetAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.SetAgent" `  




#### `TrainAgent`

  * **Method** : `google.cloud.dialogflow.v2.Agents.TrainAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.train - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Agents.TrainAgent" `  




### `google.cloud.dialogflow.v2.AnswerRecords`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.AnswerRecords`.

#### `ListAnswerRecords`

  * **Method** : `google.cloud.dialogflow.v2.AnswerRecords.ListAnswerRecords`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.answerrecords.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.AnswerRecords.ListAnswerRecords" `  




#### `UpdateAnswerRecord`

  * **Method** : `google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.answerrecords.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord" `  




### `google.cloud.dialogflow.v2.Contexts`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Contexts`.

#### `CreateContext`

  * **Method** : `google.cloud.dialogflow.v2.Contexts.CreateContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Contexts.CreateContext" `  




#### `DeleteAllContexts`

  * **Method** : `google.cloud.dialogflow.v2.Contexts.DeleteAllContexts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Contexts.DeleteAllContexts" `  




#### `DeleteContext`

  * **Method** : `google.cloud.dialogflow.v2.Contexts.DeleteContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Contexts.DeleteContext" `  




#### `GetContext`

  * **Method** : `google.cloud.dialogflow.v2.Contexts.GetContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Contexts.GetContext" `  




#### `ListContexts`

  * **Method** : `google.cloud.dialogflow.v2.Contexts.ListContexts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Contexts.ListContexts" `  




#### `UpdateContext`

  * **Method** : `google.cloud.dialogflow.v2.Contexts.UpdateContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Contexts.UpdateContext" `  




### `google.cloud.dialogflow.v2.ConversationModels`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.ConversationModels`.

#### `CreateConversationModelEvaluation`

  * **Method** : `google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.modelEvaluations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluation" `  




#### `GetConversationModelEvaluation`

  * **Method** : `google.cloud.dialogflow.v2.ConversationModels.GetConversationModelEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.modelEvaluations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationModels.GetConversationModelEvaluation" `  




#### `ListConversationModelEvaluations`

  * **Method** : `google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.modelEvaluations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluations" `  




### `google.cloud.dialogflow.v2.ConversationProfiles`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.ConversationProfiles`.

#### `ClearSuggestionFeatureConfig`

  * **Method** : `google.cloud.dialogflow.v2.ConversationProfiles.ClearSuggestionFeatureConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationProfiles.ClearSuggestionFeatureConfig" `  




#### `CreateConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2.ConversationProfiles.CreateConversationProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationProfiles.CreateConversationProfile" `  




#### `DeleteConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2.ConversationProfiles.DeleteConversationProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationProfiles.DeleteConversationProfile" `  




#### `GetConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2.ConversationProfiles.GetConversationProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationProfiles.GetConversationProfile" `  




#### `ListConversationProfiles`

  * **Method** : `google.cloud.dialogflow.v2.ConversationProfiles.ListConversationProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationProfiles.ListConversationProfiles" `  




#### `UpdateConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2.ConversationProfiles.UpdateConversationProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.ConversationProfiles.UpdateConversationProfile" `  




### `google.cloud.dialogflow.v2.Conversations`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Conversations`.

#### `CompleteConversation`

  * **Method** : `google.cloud.dialogflow.v2.Conversations.CompleteConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.complete - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Conversations.CompleteConversation" `  




#### `CreateConversation`

  * **Method** : `google.cloud.dialogflow.v2.Conversations.CreateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Conversations.CreateConversation" `  




#### `GenerateStatelessSuggestion`

  * **Method** : `google.cloud.dialogflow.v2.Conversations.GenerateStatelessSuggestion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.suggest - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Conversations.GenerateStatelessSuggestion" `  




#### `GetConversation`

  * **Method** : `google.cloud.dialogflow.v2.Conversations.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Conversations.GetConversation" `  




#### `ListConversations`

  * **Method** : `google.cloud.dialogflow.v2.Conversations.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Conversations.ListConversations" `  




#### `ListMessages`

  * **Method** : `google.cloud.dialogflow.v2.Conversations.ListMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.messages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Conversations.ListMessages" `  




### `google.cloud.dialogflow.v2.Documents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Documents`.

#### `CreateDocument`

  * **Method** : `google.cloud.dialogflow.v2.Documents.CreateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.CreateDocument" `  




#### `DeleteDocument`

  * **Method** : `google.cloud.dialogflow.v2.Documents.DeleteDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.DeleteDocument" `  




#### `ExportDocument`

  * **Method** : `google.cloud.dialogflow.v2.Documents.ExportDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.ExportDocument" `  




#### `GetDocument`

  * **Method** : `google.cloud.dialogflow.v2.Documents.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.GetDocument" `  




#### `ImportDocuments`

  * **Method** : `google.cloud.dialogflow.v2.Documents.ImportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.ImportDocuments" `  




#### `ListDocuments`

  * **Method** : `google.cloud.dialogflow.v2.Documents.ListDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.ListDocuments" `  




#### `ReloadDocument`

  * **Method** : `google.cloud.dialogflow.v2.Documents.ReloadDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.ReloadDocument" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.dialogflow.v2.Documents.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Documents.UpdateDocument" `  




### `google.cloud.dialogflow.v2.EntityTypes`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.EntityTypes`.

#### `BatchCreateEntities`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.BatchCreateEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.createEntity - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.BatchCreateEntities" `  




#### `BatchDeleteEntities`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.deleteEntity - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntities" `  




#### `BatchDeleteEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntityTypes" `  




#### `BatchUpdateEntities`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.updateEntity - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntities" `  




#### `BatchUpdateEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes" `  




#### `CreateEntityType`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.CreateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.CreateEntityType" `  




#### `DeleteEntityType`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.DeleteEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.DeleteEntityType" `  




#### `GetEntityType`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.GetEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.GetEntityType" `  




#### `ListEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes" `  




#### `UpdateEntityType`

  * **Method** : `google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType" `  




### `google.cloud.dialogflow.v2.Environments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Environments`.

#### `CreateEnvironment`

  * **Method** : `google.cloud.dialogflow.v2.Environments.CreateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Environments.CreateEnvironment" `  




#### `DeleteEnvironment`

  * **Method** : `google.cloud.dialogflow.v2.Environments.DeleteEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Environments.DeleteEnvironment" `  




#### `GetEnvironment`

  * **Method** : `google.cloud.dialogflow.v2.Environments.GetEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Environments.GetEnvironment" `  




#### `GetEnvironmentHistory`

  * **Method** : `google.cloud.dialogflow.v2.Environments.GetEnvironmentHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.getHistory - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Environments.GetEnvironmentHistory" `  




#### `ListEnvironments`

  * **Method** : `google.cloud.dialogflow.v2.Environments.ListEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Environments.ListEnvironments" `  




#### `UpdateEnvironment`

  * **Method** : `google.cloud.dialogflow.v2.Environments.UpdateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Environments.UpdateEnvironment" `  




### `google.cloud.dialogflow.v2.Fulfillments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Fulfillments`.

#### `GetFulfillment`

  * **Method** : `google.cloud.dialogflow.v2.Fulfillments.GetFulfillment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.fulfillments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Fulfillments.GetFulfillment" `  




#### `UpdateFulfillment`

  * **Method** : `google.cloud.dialogflow.v2.Fulfillments.UpdateFulfillment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.fulfillments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Fulfillments.UpdateFulfillment" `  




### `google.cloud.dialogflow.v2.Generators`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Generators`.

#### `CreateGenerator`

  * **Method** : `google.cloud.dialogflow.v2.Generators.CreateGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Generators.CreateGenerator" `  




#### `DeleteGenerator`

  * **Method** : `google.cloud.dialogflow.v2.Generators.DeleteGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Generators.DeleteGenerator" `  




#### `GetGenerator`

  * **Method** : `google.cloud.dialogflow.v2.Generators.GetGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Generators.GetGenerator" `  




#### `ListGenerators`

  * **Method** : `google.cloud.dialogflow.v2.Generators.ListGenerators`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Generators.ListGenerators" `  




#### `UpdateGenerator`

  * **Method** : `google.cloud.dialogflow.v2.Generators.UpdateGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Generators.UpdateGenerator" `  




### `google.cloud.dialogflow.v2.Intents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Intents`.

#### `BatchDeleteIntents`

  * **Method** : `google.cloud.dialogflow.v2.Intents.BatchDeleteIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Intents.BatchDeleteIntents" `  




#### `BatchUpdateIntents`

  * **Method** : `google.cloud.dialogflow.v2.Intents.BatchUpdateIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Intents.BatchUpdateIntents" `  




#### `CreateIntent`

  * **Method** : `google.cloud.dialogflow.v2.Intents.CreateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Intents.CreateIntent" `  




#### `DeleteIntent`

  * **Method** : `google.cloud.dialogflow.v2.Intents.DeleteIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Intents.DeleteIntent" `  




#### `GetIntent`

  * **Method** : `google.cloud.dialogflow.v2.Intents.GetIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Intents.GetIntent" `  




#### `ListIntents`

  * **Method** : `google.cloud.dialogflow.v2.Intents.ListIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Intents.ListIntents" `  




#### `UpdateIntent`

  * **Method** : `google.cloud.dialogflow.v2.Intents.UpdateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Intents.UpdateIntent" `  




### `google.cloud.dialogflow.v2.KnowledgeBases`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.KnowledgeBases`.

#### `CreateKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2.KnowledgeBases.CreateKnowledgeBase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.KnowledgeBases.CreateKnowledgeBase" `  




#### `DeleteKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2.KnowledgeBases.DeleteKnowledgeBase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.KnowledgeBases.DeleteKnowledgeBase" `  




#### `GetKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2.KnowledgeBases.GetKnowledgeBase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.KnowledgeBases.GetKnowledgeBase" `  




#### `ListKnowledgeBases`

  * **Method** : `google.cloud.dialogflow.v2.KnowledgeBases.ListKnowledgeBases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.KnowledgeBases.ListKnowledgeBases" `  




#### `UpdateKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2.KnowledgeBases.UpdateKnowledgeBase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.KnowledgeBases.UpdateKnowledgeBase" `  




### `google.cloud.dialogflow.v2.Participants`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Participants`.

#### `AnalyzeContent`

  * **Method** : `google.cloud.dialogflow.v2.Participants.AnalyzeContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.analyzeContent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.AnalyzeContent" `  




#### `CreateParticipant`

  * **Method** : `google.cloud.dialogflow.v2.Participants.CreateParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.CreateParticipant" `  




#### `GetParticipant`

  * **Method** : `google.cloud.dialogflow.v2.Participants.GetParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.GetParticipant" `  




#### `ListParticipants`

  * **Method** : `google.cloud.dialogflow.v2.Participants.ListParticipants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.ListParticipants" `  




#### `StreamingAnalyzeContent`

  * **Method** : `google.cloud.dialogflow.v2.Participants.StreamingAnalyzeContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.analyzeContent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.StreamingAnalyzeContent" `  




#### `SuggestArticles`

  * **Method** : `google.cloud.dialogflow.v2.Participants.SuggestArticles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.SuggestArticles" `  




#### `SuggestFaqAnswers`

  * **Method** : `google.cloud.dialogflow.v2.Participants.SuggestFaqAnswers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.SuggestFaqAnswers" `  




#### `SuggestKnowledgeAssist`

  * **Method** : `google.cloud.dialogflow.v2.Participants.SuggestKnowledgeAssist`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.SuggestKnowledgeAssist" `  




#### `SuggestSmartReplies`

  * **Method** : `google.cloud.dialogflow.v2.Participants.SuggestSmartReplies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.SuggestSmartReplies" `  




#### `UpdateParticipant`

  * **Method** : `google.cloud.dialogflow.v2.Participants.UpdateParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Participants.UpdateParticipant" `  




### `google.cloud.dialogflow.v2.SessionEntityTypes`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.SessionEntityTypes`.

#### `CreateSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2.SessionEntityTypes.CreateSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.SessionEntityTypes.CreateSessionEntityType" `  




#### `DeleteSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2.SessionEntityTypes.DeleteSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.SessionEntityTypes.DeleteSessionEntityType" `  




#### `GetSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2.SessionEntityTypes.GetSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.SessionEntityTypes.GetSessionEntityType" `  




#### `ListSessionEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2.SessionEntityTypes.ListSessionEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.SessionEntityTypes.ListSessionEntityTypes" `  




#### `UpdateSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2.SessionEntityTypes.UpdateSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.SessionEntityTypes.UpdateSessionEntityType" `  




### `google.cloud.dialogflow.v2.Sessions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Sessions`.

#### `DetectIntent`

  * **Method** : `google.cloud.dialogflow.v2.Sessions.DetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Sessions.DetectIntent" `  




#### `StreamingDetectIntent`

  * **Method** : `google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.streamingDetectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent" `  




### `google.cloud.dialogflow.v2.Versions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2.Versions`.

#### `CreateVersion`

  * **Method** : `google.cloud.dialogflow.v2.Versions.CreateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Versions.CreateVersion" `  




#### `DeleteVersion`

  * **Method** : `google.cloud.dialogflow.v2.Versions.DeleteVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Versions.DeleteVersion" `  




#### `GetVersion`

  * **Method** : `google.cloud.dialogflow.v2.Versions.GetVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Versions.GetVersion" `  




#### `ListVersions`

  * **Method** : `google.cloud.dialogflow.v2.Versions.ListVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Versions.ListVersions" `  




#### `UpdateVersion`

  * **Method** : `google.cloud.dialogflow.v2.Versions.UpdateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2.Versions.UpdateVersion" `  




### `google.cloud.dialogflow.v2beta1.Agents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Agents`.

#### `DeleteAgent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.DeleteAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.DeleteAgent" `  




#### `ExportAgent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.ExportAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.ExportAgent" `  




#### `GetAgent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.GetAgent" `  




#### `GetValidationResult`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.GetValidationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.GetValidationResult" `  




#### `ImportAgent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.ImportAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.ImportAgent" `  




#### `RestoreAgent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.RestoreAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.RestoreAgent" `  




#### `SearchAgents`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.SearchAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.SearchAgents" `  




#### `SetAgent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.SetAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.SetAgent" `  




#### `TrainAgent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Agents.TrainAgent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.agents.train - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Agents.TrainAgent" `  




### `google.cloud.dialogflow.v2beta1.AnswerRecords`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.AnswerRecords`.

#### `GetAnswerRecord`

  * **Method** : `google.cloud.dialogflow.v2beta1.AnswerRecords.GetAnswerRecord`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.answerrecords.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.AnswerRecords.GetAnswerRecord" `  




#### `ListAnswerRecords`

  * **Method** : `google.cloud.dialogflow.v2beta1.AnswerRecords.ListAnswerRecords`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.answerrecords.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.AnswerRecords.ListAnswerRecords" `  




#### `UpdateAnswerRecord`

  * **Method** : `google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.answerrecords.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord" `  




### `google.cloud.dialogflow.v2beta1.Contexts`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Contexts`.

#### `CreateContext`

  * **Method** : `google.cloud.dialogflow.v2beta1.Contexts.CreateContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Contexts.CreateContext" `  




#### `DeleteAllContexts`

  * **Method** : `google.cloud.dialogflow.v2beta1.Contexts.DeleteAllContexts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Contexts.DeleteAllContexts" `  




#### `DeleteContext`

  * **Method** : `google.cloud.dialogflow.v2beta1.Contexts.DeleteContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Contexts.DeleteContext" `  




#### `GetContext`

  * **Method** : `google.cloud.dialogflow.v2beta1.Contexts.GetContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Contexts.GetContext" `  




#### `ListContexts`

  * **Method** : `google.cloud.dialogflow.v2beta1.Contexts.ListContexts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Contexts.ListContexts" `  




#### `UpdateContext`

  * **Method** : `google.cloud.dialogflow.v2beta1.Contexts.UpdateContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.contexts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Contexts.UpdateContext" `  




### `google.cloud.dialogflow.v2beta1.ConversationProfiles`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.ConversationProfiles`.

#### `ClearSuggestionFeatureConfig`

  * **Method** : `google.cloud.dialogflow.v2beta1.ConversationProfiles.ClearSuggestionFeatureConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.ConversationProfiles.ClearSuggestionFeatureConfig" `  




#### `CreateConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2beta1.ConversationProfiles.CreateConversationProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.ConversationProfiles.CreateConversationProfile" `  




#### `DeleteConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2beta1.ConversationProfiles.DeleteConversationProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.ConversationProfiles.DeleteConversationProfile" `  




#### `GetConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2beta1.ConversationProfiles.GetConversationProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.ConversationProfiles.GetConversationProfile" `  




#### `ListConversationProfiles`

  * **Method** : `google.cloud.dialogflow.v2beta1.ConversationProfiles.ListConversationProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.ConversationProfiles.ListConversationProfiles" `  




#### `SetSuggestionFeatureConfig`

  * **Method** : `google.cloud.dialogflow.v2beta1.ConversationProfiles.SetSuggestionFeatureConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.ConversationProfiles.SetSuggestionFeatureConfig" `  




#### `UpdateConversationProfile`

  * **Method** : `google.cloud.dialogflow.v2beta1.ConversationProfiles.UpdateConversationProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.conversationProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.ConversationProfiles.UpdateConversationProfile" `  




### `google.cloud.dialogflow.v2beta1.Conversations`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Conversations`.

#### `BatchCreateMessages`

  * **Method** : `google.cloud.dialogflow.v2beta1.Conversations.BatchCreateMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.messages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Conversations.BatchCreateMessages" `  




#### `CompleteConversation`

  * **Method** : `google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.complete - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation" `  




#### `CreateConversation`

  * **Method** : `google.cloud.dialogflow.v2beta1.Conversations.CreateConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Conversations.CreateConversation" `  




#### `GenerateStatelessSuggestion`

  * **Method** : `google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.suggest - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion" `  




#### `GetConversation`

  * **Method** : `google.cloud.dialogflow.v2beta1.Conversations.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Conversations.GetConversation" `  




#### `ListConversations`

  * **Method** : `google.cloud.dialogflow.v2beta1.Conversations.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Conversations.ListConversations" `  




#### `ListMessages`

  * **Method** : `google.cloud.dialogflow.v2beta1.Conversations.ListMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.messages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Conversations.ListMessages" `  




### `google.cloud.dialogflow.v2beta1.Documents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Documents`.

#### `CreateDocument`

  * **Method** : `google.cloud.dialogflow.v2beta1.Documents.CreateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Documents.CreateDocument" `  




#### `DeleteDocument`

  * **Method** : `google.cloud.dialogflow.v2beta1.Documents.DeleteDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Documents.DeleteDocument" `  




#### `GetDocument`

  * **Method** : `google.cloud.dialogflow.v2beta1.Documents.GetDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Documents.GetDocument" `  




#### `ImportDocuments`

  * **Method** : `google.cloud.dialogflow.v2beta1.Documents.ImportDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Documents.ImportDocuments" `  




#### `ListDocuments`

  * **Method** : `google.cloud.dialogflow.v2beta1.Documents.ListDocuments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Documents.ListDocuments" `  




#### `ReloadDocument`

  * **Method** : `google.cloud.dialogflow.v2beta1.Documents.ReloadDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Documents.ReloadDocument" `  




#### `UpdateDocument`

  * **Method** : `google.cloud.dialogflow.v2beta1.Documents.UpdateDocument`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.documents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Documents.UpdateDocument" `  




### `google.cloud.dialogflow.v2beta1.EncryptionSpecService`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.EncryptionSpecService`.

#### `GetEncryptionSpec`

  * **Method** : `google.cloud.dialogflow.v2beta1.EncryptionSpecService.GetEncryptionSpec`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.encryptionspec.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EncryptionSpecService.GetEncryptionSpec" `  




#### `InitializeEncryptionSpec`

  * **Method** : `google.cloud.dialogflow.v2beta1.EncryptionSpecService.InitializeEncryptionSpec`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.encryptionspec.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EncryptionSpecService.InitializeEncryptionSpec" `  




### `google.cloud.dialogflow.v2beta1.EntityTypes`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.EntityTypes`.

#### `BatchCreateEntities`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.BatchCreateEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.createEntity - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.BatchCreateEntities" `  




#### `BatchDeleteEntities`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.deleteEntity - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntities" `  




#### `BatchDeleteEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntityTypes" `  




#### `BatchUpdateEntities`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.updateEntity - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntities" `  




#### `BatchUpdateEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntityTypes" `  




#### `CreateEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.CreateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.CreateEntityType" `  




#### `DeleteEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.DeleteEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.DeleteEntityType" `  




#### `GetEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.GetEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.GetEntityType" `  




#### `ListEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.ListEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.ListEntityTypes" `  




#### `UpdateEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.EntityTypes.UpdateEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.entityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.EntityTypes.UpdateEntityType" `  




### `google.cloud.dialogflow.v2beta1.Environments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Environments`.

#### `CreateEnvironment`

  * **Method** : `google.cloud.dialogflow.v2beta1.Environments.CreateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Environments.CreateEnvironment" `  




#### `DeleteEnvironment`

  * **Method** : `google.cloud.dialogflow.v2beta1.Environments.DeleteEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Environments.DeleteEnvironment" `  




#### `GetEnvironment`

  * **Method** : `google.cloud.dialogflow.v2beta1.Environments.GetEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Environments.GetEnvironment" `  




#### `GetEnvironmentHistory`

  * **Method** : `google.cloud.dialogflow.v2beta1.Environments.GetEnvironmentHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.getHistory - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Environments.GetEnvironmentHistory" `  




#### `ListEnvironments`

  * **Method** : `google.cloud.dialogflow.v2beta1.Environments.ListEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Environments.ListEnvironments" `  




#### `UpdateEnvironment`

  * **Method** : `google.cloud.dialogflow.v2beta1.Environments.UpdateEnvironment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.environments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Environments.UpdateEnvironment" `  




### `google.cloud.dialogflow.v2beta1.Fulfillments`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Fulfillments`.

#### `GetFulfillment`

  * **Method** : `google.cloud.dialogflow.v2beta1.Fulfillments.GetFulfillment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.fulfillments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Fulfillments.GetFulfillment" `  




#### `UpdateFulfillment`

  * **Method** : `google.cloud.dialogflow.v2beta1.Fulfillments.UpdateFulfillment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.fulfillments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Fulfillments.UpdateFulfillment" `  




### `google.cloud.dialogflow.v2beta1.Generators`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Generators`.

#### `CreateGenerator`

  * **Method** : `google.cloud.dialogflow.v2beta1.Generators.CreateGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Generators.CreateGenerator" `  




#### `DeleteGenerator`

  * **Method** : `google.cloud.dialogflow.v2beta1.Generators.DeleteGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Generators.DeleteGenerator" `  




#### `GetGenerator`

  * **Method** : `google.cloud.dialogflow.v2beta1.Generators.GetGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Generators.GetGenerator" `  




#### `ListGenerators`

  * **Method** : `google.cloud.dialogflow.v2beta1.Generators.ListGenerators`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Generators.ListGenerators" `  




#### `UpdateGenerator`

  * **Method** : `google.cloud.dialogflow.v2beta1.Generators.UpdateGenerator`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.generators.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Generators.UpdateGenerator" `  




### `google.cloud.dialogflow.v2beta1.Intents`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Intents`.

#### `BatchDeleteIntents`

  * **Method** : `google.cloud.dialogflow.v2beta1.Intents.BatchDeleteIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Intents.BatchDeleteIntents" `  




#### `BatchUpdateIntents`

  * **Method** : `google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents" `  




#### `CreateIntent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Intents.CreateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Intents.CreateIntent" `  




#### `DeleteIntent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Intents.DeleteIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Intents.DeleteIntent" `  




#### `GetIntent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Intents.GetIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Intents.GetIntent" `  




#### `ListIntents`

  * **Method** : `google.cloud.dialogflow.v2beta1.Intents.ListIntents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Intents.ListIntents" `  




#### `UpdateIntent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Intents.UpdateIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.intents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Intents.UpdateIntent" `  




### `google.cloud.dialogflow.v2beta1.KnowledgeBases`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.KnowledgeBases`.

#### `CreateKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2beta1.KnowledgeBases.CreateKnowledgeBase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.KnowledgeBases.CreateKnowledgeBase" `  




#### `DeleteKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2beta1.KnowledgeBases.DeleteKnowledgeBase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.KnowledgeBases.DeleteKnowledgeBase" `  




#### `GetKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2beta1.KnowledgeBases.GetKnowledgeBase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.KnowledgeBases.GetKnowledgeBase" `  




#### `ListKnowledgeBases`

  * **Method** : `google.cloud.dialogflow.v2beta1.KnowledgeBases.ListKnowledgeBases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.KnowledgeBases.ListKnowledgeBases" `  




#### `UpdateKnowledgeBase`

  * **Method** : `google.cloud.dialogflow.v2beta1.KnowledgeBases.UpdateKnowledgeBase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dialogflow.knowledgeBases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.KnowledgeBases.UpdateKnowledgeBase" `  




### `google.cloud.dialogflow.v2beta1.Participants`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Participants`.

#### `AnalyzeContent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.analyzeContent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent" `  




#### `CompileSuggestion`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion" `  




#### `CreateParticipant`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.CreateParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.CreateParticipant" `  




#### `GetParticipant`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.GetParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.GetParticipant" `  




#### `ListParticipants`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.ListParticipants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.ListParticipants" `  




#### `ListSuggestions`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.ListSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.ListSuggestions" `  




#### `StreamingAnalyzeContent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.analyzeContent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent" `  




#### `SuggestArticles`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.SuggestArticles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.SuggestArticles" `  




#### `SuggestFaqAnswers`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers" `  




#### `SuggestKnowledgeAssist`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist" `  




#### `SuggestSmartReplies`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.suggestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies" `  




#### `UpdateParticipant`

  * **Method** : `google.cloud.dialogflow.v2beta1.Participants.UpdateParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.participants.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Participants.UpdateParticipant" `  




### `google.cloud.dialogflow.v2beta1.SessionEntityTypes`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.SessionEntityTypes`.

#### `CreateSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.SessionEntityTypes.CreateSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.SessionEntityTypes.CreateSessionEntityType" `  




#### `DeleteSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.SessionEntityTypes.DeleteSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.SessionEntityTypes.DeleteSessionEntityType" `  




#### `GetSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.SessionEntityTypes.GetSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.SessionEntityTypes.GetSessionEntityType" `  




#### `ListSessionEntityTypes`

  * **Method** : `google.cloud.dialogflow.v2beta1.SessionEntityTypes.ListSessionEntityTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.SessionEntityTypes.ListSessionEntityTypes" `  




#### `UpdateSessionEntityType`

  * **Method** : `google.cloud.dialogflow.v2beta1.SessionEntityTypes.UpdateSessionEntityType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessionEntityTypes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.SessionEntityTypes.UpdateSessionEntityType" `  




### `google.cloud.dialogflow.v2beta1.Sessions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Sessions`.

#### `DetectIntent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Sessions.DetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.detectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Sessions.DetectIntent" `  




#### `StreamingDetectIntent`

  * **Method** : `google.cloud.dialogflow.v2beta1.Sessions.StreamingDetectIntent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.sessions.streamingDetectIntent - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Sessions.StreamingDetectIntent" `  




### `google.cloud.dialogflow.v2beta1.Versions`

The following audit logs are associated with methods belonging to `google.cloud.dialogflow.v2beta1.Versions`.

#### `CreateVersion`

  * **Method** : `google.cloud.dialogflow.v2beta1.Versions.CreateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Versions.CreateVersion" `  




#### `DeleteVersion`

  * **Method** : `google.cloud.dialogflow.v2beta1.Versions.DeleteVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Versions.DeleteVersion" `  




#### `GetVersion`

  * **Method** : `google.cloud.dialogflow.v2beta1.Versions.GetVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Versions.GetVersion" `  




#### `ListVersions`

  * **Method** : `google.cloud.dialogflow.v2beta1.Versions.ListVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Versions.ListVersions" `  




#### `UpdateVersion`

  * **Method** : `google.cloud.dialogflow.v2beta1.Versions.UpdateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.versions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dialogflow.v2beta1.Versions.UpdateVersion" `  




### `google.cloud.location.Locations`

The following audit logs are associated with methods belonging to `google.cloud.location.Locations`.

#### `GetLocation`

  * **Method** : `google.cloud.location.Locations.GetLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.GetLocation" `  




#### `ListLocations`

  * **Method** : `google.cloud.location.Locations.ListLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.agents.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.ListLocations" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dialogflow.operations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




[ Previous arrow_back  Speech data logging  ](https://docs.cloud.google.com/dialogflow/es/docs/data-logging)

[ Next Agent validation  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-validation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
