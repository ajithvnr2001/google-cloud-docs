---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/audit-logging/
title: Customer Experience Insights audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:28.163913+00:00
---

# Customer Experience Insights audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Customer Experience Insights audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Customer Experience Insights. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Customer Experience Insights audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="contactcenterinsights.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Customer Experience Insights generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.iam.v1.IAMPolicy.GetIamPolicy`  
`ADMIN_WRITE` | `google.iam.v1.IAMPolicy.SetIamPolicy`  
`DATA_READ` | `google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateIssueModelStats`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateStats`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportInsightsData` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerateConversationSignedAudio`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerativeInsights` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysis`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysisRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessment`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessmentRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAutoLabelingRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetChart`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetConversation`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetCorrelationConfig`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDashboard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDataset`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetEncryptionSpec`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetFeedbackLabel`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssue`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssueModel`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetPhraseMatcher`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestion`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestionTag`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetSettings`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAllFeedbackLabels`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalyses`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalysisRules`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessmentRules`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessments`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViewSets`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViews`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAutoLabelingRules`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListCharts`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListConversations`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDashboards`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDatasets`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDiagnostics`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListFeedbackLabels`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssueModels`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssues`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListNotes`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListPhraseMatchers`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestionTags`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestions`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecardRevisions`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecards`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListViews`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryMetrics` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryPerformanceOverview` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.SampleConversations` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestAutoLabelingRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestCorrelationConfig`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CalculateStats`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportInsightsData` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysis`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysisRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessment`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessmentRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetConversation`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetDataset`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetEncryptionSpec`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetFeedbackLabel`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssue`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssueModel`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetPhraseMatcher`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestion`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestionTag`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecard`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetSettings`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAllFeedbackLabels`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalyses`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalysisRules`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessmentRules`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessments`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViewSets`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViews`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListConversations`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListDatasets`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListFeedbackLabels`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssueModels`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssues`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListNotes`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListPhraseMatchers`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestionTags`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestions`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecardRevisions`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecards`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListViews`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.QueryMetrics` (LRO)  
`DATA_WRITE` | `google.cloud.contactcenterinsights.v1.ContactCenterInsights.AppealAssessment`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkAnalyzeConversations` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteConversations` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteFeedbackLabels` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDownloadFeedbackLabels` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkUploadFeedbackLabels` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysis` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysisRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessment`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessmentRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAutoLabelingRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateChart`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateConversation`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDashboard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDataset`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateFeedbackLabel`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssue` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateNote`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreatePhraseMatcher`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestion`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestionTag`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysis`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysisRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessment`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessmentRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAutoLabelingRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteChart`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteConversation`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDashboard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDataset` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteFeedbackLabel`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssue`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteNote`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeletePhraseMatcher`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestion`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestionTag` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.DiagnoseConversations` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.FinalizeAssessment`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.ImportIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.IngestConversations` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.InitializeEncryptionSpec` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.PublishAssessment`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.TuneQaScorecardRevision` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAnalysisRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAssessmentRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAutoLabelingRule`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateChart`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateConversation`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateCorrelationConfig`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDashboard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDataset`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateFeedbackLabel`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssue`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssueModel`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateNote`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdatePhraseMatcher`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestion`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestionTag` (LRO)  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaScorecard`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateSettings`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateView`  
`google.cloud.contactcenterinsights.v1.ContactCenterInsights.UploadConversation` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.AppealAssessment`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkAnalyzeConversations` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteConversations` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteFeedbackLabels` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDownloadFeedbackLabels` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkUploadFeedbackLabels` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysis` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysisRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessment`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessmentRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateConversation`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateDataset`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateFeedbackLabel`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssue`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateNote`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreatePhraseMatcher`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestion`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestionTag`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecard`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysis`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysisRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessment`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessmentRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteConversation`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteDataset` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteFeedbackLabel`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssue`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteNote`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeletePhraseMatcher`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestion`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestionTag` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecard`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DiagnoseConversations`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.FinalizeAssessment`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ImportIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.IngestConversations` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.InitializeEncryptionSpec` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.PublishAssessment`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.TuneQaScorecardRevision` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployIssueModel` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployQaScorecardRevision`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAnalysisRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAssessmentRule`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedViewSet`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateConversation`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateFeedbackLabel`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssue`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssueModel`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateNote`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdatePhraseMatcher`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestion`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestionTag` (LRO)  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaScorecard`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateSettings`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateView`  
`google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UploadConversation` (LRO)  
`google.longrunning.Operations.CancelOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Customer Experience Insights.

### `google.cloud.contactcenterinsights.v1.ContactCenterInsights`

The following audit logs are associated with methods belonging to `google.cloud.contactcenterinsights.v1.ContactCenterInsights`.

#### `AppealAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.AppealAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.AppealAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.appeal - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.AppealAssessment" `  




#### `BulkAnalyzeConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkAnalyzeConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkAnalyzeConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkAnalyzeConversations" `  




#### `BulkDeleteConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteConversations" `  




#### `BulkDeleteFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDeleteFeedbackLabels" `  




#### `BulkDownloadFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDownloadFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDownloadFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.download - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkDownloadFeedbackLabels" `  




#### `BulkUploadFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkUploadFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkUploadFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.upload - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.BulkUploadFeedbackLabels" `  




#### `CalculateIssueModelStats`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateIssueModelStats](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateIssueModelStats)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateIssueModelStats" `  




#### `CalculateStats`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateStats](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateStats)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CalculateStats" `  




#### `CreateAnalysis`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysis](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysis)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysis" `  




#### `CreateAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAnalysisRule" `  




#### `CreateAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessment" `  




#### `CreateAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAssessmentRule" `  




#### `CreateAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedView" `  




#### `CreateAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAuthorizedViewSet" `  




#### `CreateAutoLabelingRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAutoLabelingRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAutoLabelingRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.autoLabelingRules.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateAutoLabelingRule" `  




#### `CreateChart`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateChart](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateChart)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.charts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateChart" `  




#### `CreateConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateConversation" `  




#### `CreateDashboard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDashboard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDashboard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.dashboards.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDashboard" `  




#### `CreateDataset`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDataset](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDataset)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateDataset" `  




#### `CreateFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateFeedbackLabel" `  




#### `CreateIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssue" `  




#### `CreateIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateIssueModel" `  




#### `CreateNote`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateNote](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateNote)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateNote" `  




#### `CreatePhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreatePhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreatePhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreatePhraseMatcher" `  




#### `CreateQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestion" `  




#### `CreateQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaQuestionTag" `  




#### `CreateQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecard" `  




#### `CreateQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateQaScorecardRevision" `  




#### `CreateView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.CreateView" `  




#### `DeleteAnalysis`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysis](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysis)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysis" `  




#### `DeleteAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAnalysisRule" `  




#### `DeleteAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessment" `  




#### `DeleteAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAssessmentRule" `  




#### `DeleteAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedView" `  




#### `DeleteAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAuthorizedViewSet" `  




#### `DeleteAutoLabelingRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAutoLabelingRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAutoLabelingRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.autoLabelingRules.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteAutoLabelingRule" `  




#### `DeleteChart`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteChart](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteChart)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.charts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteChart" `  




#### `DeleteConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteConversation" `  




#### `DeleteDashboard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDashboard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDashboard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.dashboards.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDashboard" `  




#### `DeleteDataset`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDataset](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDataset)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteDataset" `  




#### `DeleteFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteFeedbackLabel" `  




#### `DeleteIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssue" `  




#### `DeleteIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteIssueModel" `  




#### `DeleteNote`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteNote](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteNote)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteNote" `  




#### `DeletePhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeletePhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeletePhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeletePhraseMatcher" `  




#### `DeleteQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestion" `  




#### `DeleteQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaQuestionTag" `  




#### `DeleteQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecard" `  




#### `DeleteQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteQaScorecardRevision" `  




#### `DeleteView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeleteView" `  




#### `DeployIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.deploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployIssueModel" `  




#### `DeployQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.deploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DeployQaScorecardRevision" `  




#### `DiagnoseConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.DiagnoseConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.DiagnoseConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.DiagnoseConversations" `  




#### `ExportInsightsData`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportInsightsData](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportInsightsData)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportInsightsData" `  




#### `ExportIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.export - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ExportIssueModel" `  




#### `FinalizeAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.FinalizeAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.FinalizeAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.finalize - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.FinalizeAssessment" `  




#### `GenerateConversationSignedAudio`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerateConversationSignedAudio](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerateConversationSignedAudio)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.generateSignedAudio - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerateConversationSignedAudio" `  




#### `GenerativeInsights`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerativeInsights](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerativeInsights)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GenerativeInsights" `  




#### `GetAnalysis`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysis](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysis)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysis" `  




#### `GetAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAnalysisRule" `  




#### `GetAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessment" `  




#### `GetAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAssessmentRule" `  




#### `GetAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedView" `  




#### `GetAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAuthorizedViewSet" `  




#### `GetAutoLabelingRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAutoLabelingRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAutoLabelingRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.autoLabelingRules.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetAutoLabelingRule" `  




#### `GetChart`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetChart](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetChart)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.charts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetChart" `  




#### `GetConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetConversation" `  




#### `GetCorrelationConfig`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetCorrelationConfig](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetCorrelationConfig)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.correlationConfigs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetCorrelationConfig" `  




#### `GetDashboard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDashboard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDashboard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.dashboards.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDashboard" `  




#### `GetDataset`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDataset](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDataset)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetDataset" `  




#### `GetEncryptionSpec`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetEncryptionSpec](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetEncryptionSpec)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.encryptionSpecs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetEncryptionSpec" `  




#### `GetFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetFeedbackLabel" `  




#### `GetIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssue" `  




#### `GetIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetIssueModel" `  




#### `GetPhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetPhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetPhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetPhraseMatcher" `  




#### `GetQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestion" `  




#### `GetQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaQuestionTag" `  




#### `GetQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecard" `  




#### `GetQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetQaScorecardRevision" `  




#### `GetSettings`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetSettings](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.settings.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetSettings" `  




#### `GetView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.GetView" `  




#### `ImportIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ImportIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ImportIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.create - DATA_WRITE`
    * `contactcenterinsights.issueModels.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ImportIssueModel" `  




#### `IngestConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.IngestConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.IngestConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.IngestConversations" `  




#### `InitializeEncryptionSpec`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.InitializeEncryptionSpec](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.InitializeEncryptionSpec)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.encryptionSpecs.initialize - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.InitializeEncryptionSpec" `  




#### `ListAllFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAllFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAllFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAllFeedbackLabels" `  




#### `ListAnalyses`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalyses](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalyses)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalyses" `  




#### `ListAnalysisRules`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalysisRules](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalysisRules)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAnalysisRules" `  




#### `ListAssessmentRules`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessmentRules](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessmentRules)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessmentRules" `  




#### `ListAssessments`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessments](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessments)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAssessments" `  




#### `ListAuthorizedViewSets`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViewSets](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViewSets)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViewSets" `  




#### `ListAuthorizedViews`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViews](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViews)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAuthorizedViews" `  




#### `ListAutoLabelingRules`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAutoLabelingRules](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAutoLabelingRules)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.autoLabelingRules.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListAutoLabelingRules" `  




#### `ListCharts`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListCharts](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListCharts)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.charts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListCharts" `  




#### `ListConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListConversations" `  




#### `ListDashboards`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDashboards](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDashboards)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.dashboards.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDashboards" `  




#### `ListDatasets`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDatasets](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDatasets)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDatasets" `  




#### `ListDiagnostics`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDiagnostics](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDiagnostics)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListDiagnostics" `  




#### `ListFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListFeedbackLabels" `  




#### `ListIssueModels`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssueModels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssueModels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssueModels" `  




#### `ListIssues`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssues](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssues)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListIssues" `  




#### `ListNotes`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListNotes](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListNotes)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListNotes" `  




#### `ListPhraseMatchers`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListPhraseMatchers](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListPhraseMatchers)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListPhraseMatchers" `  




#### `ListQaQuestionTags`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestionTags](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestionTags)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestionTags" `  




#### `ListQaQuestions`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestions](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestions)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaQuestions" `  




#### `ListQaScorecardRevisions`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecardRevisions](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecardRevisions)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecardRevisions" `  




#### `ListQaScorecards`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecards](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecards)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListQaScorecards" `  




#### `ListViews`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListViews](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListViews)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.ListViews" `  




#### `PublishAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.PublishAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.PublishAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.publish - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.PublishAssessment" `  




#### `QueryMetrics`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryMetrics](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryMetrics)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryMetrics" `  




#### `QueryPerformanceOverview`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryPerformanceOverview](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryPerformanceOverview)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedConversations.list - DATA_READ`
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.QueryPerformanceOverview" `  




#### `SampleConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.SampleConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.SampleConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
    * `contactcenterinsights.datasetConversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.SampleConversations" `  




#### `TestAutoLabelingRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestAutoLabelingRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestAutoLabelingRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.autoLabelingRules.test - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestAutoLabelingRule" `  




#### `TestCorrelationConfig`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestCorrelationConfig](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestCorrelationConfig)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.correlationConfigs.test - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.TestCorrelationConfig" `  




#### `TuneQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.TuneQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.TuneQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.tune - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.TuneQaScorecardRevision" `  




#### `UndeployIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.undeploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployIssueModel" `  




#### `UndeployQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.undeploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UndeployQaScorecardRevision" `  




#### `UpdateAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAnalysisRule" `  




#### `UpdateAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAssessmentRule" `  




#### `UpdateAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedView" `  




#### `UpdateAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAuthorizedViewSet" `  




#### `UpdateAutoLabelingRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAutoLabelingRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAutoLabelingRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.autoLabelingRules.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateAutoLabelingRule" `  




#### `UpdateChart`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateChart](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateChart)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.charts.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateChart" `  




#### `UpdateConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateConversation" `  




#### `UpdateCorrelationConfig`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateCorrelationConfig](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateCorrelationConfig)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.correlationConfigs.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateCorrelationConfig" `  




#### `UpdateDashboard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDashboard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDashboard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.dashboards.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDashboard" `  




#### `UpdateDataset`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDataset](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDataset)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateDataset" `  




#### `UpdateFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateFeedbackLabel" `  




#### `UpdateIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssue" `  




#### `UpdateIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateIssueModel" `  




#### `UpdateNote`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateNote](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateNote)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateNote" `  




#### `UpdatePhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdatePhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdatePhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdatePhraseMatcher" `  




#### `UpdateQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestion" `  




#### `UpdateQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaQuestionTag" `  




#### `UpdateQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateQaScorecard" `  




#### `UpdateSettings`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateSettings](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.settings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateSettings" `  




#### `UpdateView`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UpdateView" `  




#### `UploadConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1.ContactCenterInsights.UploadConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1#google.cloud.contactcenterinsights.v1.ContactCenterInsights.UploadConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.upload - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1.ContactCenterInsights.UploadConversation" `  




### `google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights`

The following audit logs are associated with methods belonging to `google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights`.

#### `AppealAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.AppealAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.AppealAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.appeal - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.AppealAssessment" `  




#### `BulkAnalyzeConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkAnalyzeConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkAnalyzeConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkAnalyzeConversations" `  




#### `BulkDeleteConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteConversations" `  




#### `BulkDeleteFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDeleteFeedbackLabels" `  




#### `BulkDownloadFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDownloadFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDownloadFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.download - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkDownloadFeedbackLabels" `  




#### `BulkUploadFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkUploadFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkUploadFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.upload - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.BulkUploadFeedbackLabels" `  




#### `CalculateStats`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CalculateStats](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CalculateStats)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CalculateStats" `  




#### `CreateAnalysis`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysis](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysis)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysis" `  




#### `CreateAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAnalysisRule" `  




#### `CreateAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessment" `  




#### `CreateAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAssessmentRule" `  




#### `CreateAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedView" `  




#### `CreateAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateAuthorizedViewSet" `  




#### `CreateConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateConversation" `  




#### `CreateDataset`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateDataset](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateDataset)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateDataset" `  




#### `CreateFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateFeedbackLabel" `  




#### `CreateIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssue" `  




#### `CreateIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateIssueModel" `  




#### `CreateNote`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateNote](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateNote)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateNote" `  




#### `CreatePhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreatePhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreatePhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreatePhraseMatcher" `  




#### `CreateQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestion" `  




#### `CreateQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaQuestionTag" `  




#### `CreateQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecard" `  




#### `CreateQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateQaScorecardRevision" `  




#### `CreateView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.CreateView" `  




#### `DeleteAnalysis`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysis](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysis)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysis" `  




#### `DeleteAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAnalysisRule" `  




#### `DeleteAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessment" `  




#### `DeleteAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAssessmentRule" `  




#### `DeleteAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedView" `  




#### `DeleteAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteAuthorizedViewSet" `  




#### `DeleteConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteConversation" `  




#### `DeleteDataset`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteDataset](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteDataset)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteDataset" `  




#### `DeleteFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteFeedbackLabel" `  




#### `DeleteIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssue" `  




#### `DeleteIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteIssueModel" `  




#### `DeleteNote`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteNote](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteNote)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteNote" `  




#### `DeletePhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeletePhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeletePhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeletePhraseMatcher" `  




#### `DeleteQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestion" `  




#### `DeleteQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaQuestionTag" `  




#### `DeleteQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecard" `  




#### `DeleteQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteQaScorecardRevision" `  




#### `DeleteView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeleteView" `  




#### `DeployIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.deploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployIssueModel" `  




#### `DeployQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.deploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DeployQaScorecardRevision" `  




#### `DiagnoseConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DiagnoseConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DiagnoseConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.DiagnoseConversations" `  




#### `ExportInsightsData`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportInsightsData](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportInsightsData)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportInsightsData" `  




#### `ExportIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.export - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ExportIssueModel" `  




#### `FinalizeAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.FinalizeAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.FinalizeAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.finalize - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.FinalizeAssessment" `  




#### `GetAnalysis`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysis](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysis)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysis" `  




#### `GetAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAnalysisRule" `  




#### `GetAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessment" `  




#### `GetAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAssessmentRule" `  




#### `GetAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedView" `  




#### `GetAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetAuthorizedViewSet" `  




#### `GetConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetConversation" `  




#### `GetDataset`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetDataset](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetDataset)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetDataset" `  




#### `GetEncryptionSpec`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetEncryptionSpec](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetEncryptionSpec)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.encryptionSpecs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetEncryptionSpec" `  




#### `GetFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetFeedbackLabel" `  




#### `GetIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssue" `  




#### `GetIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetIssueModel" `  




#### `GetPhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetPhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetPhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetPhraseMatcher" `  




#### `GetQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestion" `  




#### `GetQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaQuestionTag" `  




#### `GetQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecard" `  




#### `GetQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetQaScorecardRevision" `  




#### `GetSettings`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetSettings](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.settings.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetSettings" `  




#### `GetView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.GetView" `  




#### `ImportIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ImportIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ImportIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.create - DATA_WRITE`
    * `contactcenterinsights.issueModels.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ImportIssueModel" `  




#### `IngestConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.IngestConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.IngestConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.IngestConversations" `  




#### `InitializeEncryptionSpec`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.InitializeEncryptionSpec](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.InitializeEncryptionSpec)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.encryptionSpecs.initialize - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.InitializeEncryptionSpec" `  




#### `ListAllFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAllFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAllFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAllFeedbackLabels" `  




#### `ListAnalyses`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalyses](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalyses)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analyses.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalyses" `  




#### `ListAnalysisRules`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalysisRules](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalysisRules)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAnalysisRules" `  




#### `ListAssessmentRules`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessmentRules](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessmentRules)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessmentRules" `  




#### `ListAssessments`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessments](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessments)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAssessments" `  




#### `ListAuthorizedViewSets`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViewSets](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViewSets)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViewSets" `  




#### `ListAuthorizedViews`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViews](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViews)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListAuthorizedViews" `  




#### `ListConversations`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListConversations](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListConversations)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListConversations" `  




#### `ListDatasets`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListDatasets](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListDatasets)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.datasets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListDatasets" `  




#### `ListFeedbackLabels`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListFeedbackLabels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListFeedbackLabels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListFeedbackLabels" `  




#### `ListIssueModels`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssueModels](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssueModels)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssueModels" `  




#### `ListIssues`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssues](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssues)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListIssues" `  




#### `ListNotes`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListNotes](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListNotes)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListNotes" `  




#### `ListPhraseMatchers`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListPhraseMatchers](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListPhraseMatchers)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListPhraseMatchers" `  




#### `ListQaQuestionTags`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestionTags](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestionTags)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestionTags" `  




#### `ListQaQuestions`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestions](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestions)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaQuestions" `  




#### `ListQaScorecardRevisions`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecardRevisions](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecardRevisions)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecardRevisions" `  




#### `ListQaScorecards`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecards](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecards)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListQaScorecards" `  




#### `ListViews`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListViews](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListViews)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.ListViews" `  




#### `PublishAssessment`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.PublishAssessment](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.PublishAssessment)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessments.publish - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.PublishAssessment" `  




#### `QueryMetrics`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.QueryMetrics](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.QueryMetrics)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.QueryMetrics" `  




#### `TuneQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.TuneQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.TuneQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.tune - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.TuneQaScorecardRevision" `  




#### `UndeployIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.undeploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployIssueModel" `  




#### `UndeployQaScorecardRevision`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployQaScorecardRevision](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployQaScorecardRevision)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecardRevisions.undeploy - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UndeployQaScorecardRevision" `  




#### `UpdateAnalysisRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAnalysisRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAnalysisRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.analysisRules.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAnalysisRule" `  




#### `UpdateAssessmentRule`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAssessmentRule](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAssessmentRule)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.assessmentRules.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAssessmentRule" `  




#### `UpdateAuthorizedView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedView" `  




#### `UpdateAuthorizedViewSet`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedViewSet](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedViewSet)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViewSets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateAuthorizedViewSet" `  




#### `UpdateConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateConversation" `  




#### `UpdateFeedbackLabel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateFeedbackLabel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateFeedbackLabel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.feedbackLabels.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateFeedbackLabel" `  




#### `UpdateIssue`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssue](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssue)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issues.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssue" `  




#### `UpdateIssueModel`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssueModel](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssueModel)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.issueModels.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateIssueModel" `  




#### `UpdateNote`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateNote](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateNote)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.notes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateNote" `  




#### `UpdatePhraseMatcher`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdatePhraseMatcher](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdatePhraseMatcher)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.phraseMatchers.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdatePhraseMatcher" `  




#### `UpdateQaQuestion`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestion](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestion)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestion" `  




#### `UpdateQaQuestionTag`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestionTag](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestionTag)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaQuestionTags.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaQuestionTag" `  




#### `UpdateQaScorecard`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaScorecard](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaScorecard)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.qaScorecards.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateQaScorecard" `  




#### `UpdateSettings`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateSettings](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.settings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateSettings" `  




#### `UpdateView`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateView](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateView)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.views.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UpdateView" `  




#### `UploadConversation`

  * **Method** : `[google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UploadConversation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UploadConversation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.conversations.upload - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.UploadConversation" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedViews.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `[google.longrunning.Operations.CancelOperation](https://docs.cloud.google.com/contact-center/insights/docs/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenterinsights.authorizedOperations.cancel - DATA_WRITE`
    * `contactcenterinsights.operations.cancel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.contactcenterinsights.v1.ContactCenterInsights.SearchAuthorizedViews`
  * `google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights.SearchAuthorizedViews`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
