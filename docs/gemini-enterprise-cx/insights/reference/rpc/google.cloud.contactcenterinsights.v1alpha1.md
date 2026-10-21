---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1
title: Package google.cloud.contactcenterinsights.v1alpha1 \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:31:08.142732+00:00
---

# Package google.cloud.contactcenterinsights.v1alpha1  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Package google.cloud.contactcenterinsights.v1alpha1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ContactCenterInsights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ContactCenterInsights)` (interface)
  * `[Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Analysis)` (message)
  * `[AnalysisResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisResult)` (message)
  * `[AnalysisResult.CallAnalysisMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisResult.CallAnalysisMetadata)` (message)
  * `[AnalysisRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisRule)` (message)
  * `[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotationBoundary)` (message)
  * `[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector)` (message)
  * `[AnnotatorSelector.QaConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.QaConfig)` (message)
  * `[AnnotatorSelector.QaConfig.ScorecardList](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.QaConfig.ScorecardList)` (message)
  * `[AnnotatorSelector.SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.SummarizationConfig)` (message)
  * `[AnnotatorSelector.SummarizationConfig.SummarizationModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.SummarizationConfig.SummarizationModel)` (enum)
  * `[AnswerFeedback](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnswerFeedback)` (message)
  * `[AnswerFeedback.CorrectnessLevel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnswerFeedback.CorrectnessLevel)` (enum)
  * `[AppealAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AppealAssessmentRequest)` (message)
  * `[ArticleSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ArticleSuggestionData)` (message)
  * `[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)` (message)
  * `[Assessment.State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment.State)` (enum)
  * `[AssessmentRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AssessmentRule)` (message)
  * `[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)` (message)
  * `[AuthorizedViewSet](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedViewSet)` (message)
  * `[BulkAnalyzeConversationsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkAnalyzeConversationsMetadata)` (message)
  * `[BulkAnalyzeConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkAnalyzeConversationsRequest)` (message)
  * `[BulkAnalyzeConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkAnalyzeConversationsResponse)` (message)
  * `[BulkDeleteConversationsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteConversationsMetadata)` (message)
  * `[BulkDeleteConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteConversationsRequest)` (message)
  * `[BulkDeleteConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteConversationsResponse)` (message)
  * `[BulkDeleteFeedbackLabelsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteFeedbackLabelsMetadata)` (message)
  * `[BulkDeleteFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteFeedbackLabelsRequest)` (message)
  * `[BulkDeleteFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteFeedbackLabelsResponse)` (message)
  * `[BulkDownloadFeedbackLabelsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsMetadata)` (message)
  * `[BulkDownloadFeedbackLabelsMetadata.DownloadStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsMetadata.DownloadStats)` (message)
  * `[BulkDownloadFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest)` (message)
  * `[BulkDownloadFeedbackLabelsRequest.FeedbackLabelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.FeedbackLabelType)` (enum)
  * `[BulkDownloadFeedbackLabelsRequest.GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.GcsDestination)` (message)
  * `[BulkDownloadFeedbackLabelsRequest.GcsDestination.Format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.GcsDestination.Format)` (enum)
  * `[BulkDownloadFeedbackLabelsRequest.SheetsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.SheetsDestination)` (message)
  * `[BulkDownloadFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsResponse)` (message)
  * `[BulkUploadFeedbackLabelsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsMetadata)` (message)
  * `[BulkUploadFeedbackLabelsMetadata.UploadStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsMetadata.UploadStats)` (message)
  * `[BulkUploadFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest)` (message)
  * `[BulkUploadFeedbackLabelsRequest.GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest.GcsSource)` (message)
  * `[BulkUploadFeedbackLabelsRequest.GcsSource.Format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest.GcsSource.Format)` (enum)
  * `[BulkUploadFeedbackLabelsRequest.SheetsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest.SheetsSource)` (message)
  * `[BulkUploadFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsResponse)` (message)
  * `[CalculateIssueModelStatsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateIssueModelStatsRequest)` (message)
  * `[CalculateIssueModelStatsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateIssueModelStatsResponse)` (message)
  * `[CalculateStatsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsRequest)` (message)
  * `[CalculateStatsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsResponse)` (message)
  * `[CalculateStatsResponse.TimeSeries](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsResponse.TimeSeries)` (message)
  * `[CalculateStatsResponse.TimeSeries.Interval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsResponse.TimeSeries.Interval)` (message)
  * `[CallAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CallAnnotation)` (message)
  * `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)` (message)
  * `[Conversation.CallMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.CallMetadata)` (message)
  * `[Conversation.Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Medium)` (enum)
  * `[Conversation.QualityMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.QualityMetadata)` (message)
  * `[Conversation.QualityMetadata.AgentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.QualityMetadata.AgentInfo)` (message)
  * `[Conversation.Transcript](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript)` (message)
  * `[Conversation.Transcript.TranscriptSegment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript.TranscriptSegment)` (message)
  * `[Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata)` (message)
  * `[Conversation.Transcript.TranscriptSegment.WordInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript.TranscriptSegment.WordInfo)` (message)
  * `[ConversationDataSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationDataSource)` (message)
  * `[ConversationLevelSentiment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationLevelSentiment)` (message)
  * `[ConversationLevelSilence](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationLevelSilence)` (message)
  * `[ConversationParticipant](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationParticipant)` (message)
  * `[ConversationParticipant.Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationParticipant.Role)` (enum)
  * `[ConversationSummarizationSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationSummarizationSuggestionData)` (message)
  * `[ConversationView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationView)` (enum)
  * `[CreateAnalysisOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAnalysisOperationMetadata)` (message)
  * `[CreateAnalysisRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAnalysisRequest)` (message)
  * `[CreateAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAnalysisRuleRequest)` (message)
  * `[CreateAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAssessmentRequest)` (message)
  * `[CreateAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAssessmentRuleRequest)` (message)
  * `[CreateAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAuthorizedViewRequest)` (message)
  * `[CreateAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAuthorizedViewSetRequest)` (message)
  * `[CreateConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateConversationRequest)` (message)
  * `[CreateFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateFeedbackLabelRequest)` (message)
  * `[CreateIssueMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueMetadata)` (message)
  * `[CreateIssueModelMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueModelMetadata)` (message)
  * `[CreateIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueModelRequest)` (message)
  * `[CreateIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueRequest)` (message)
  * `[CreateNoteRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateNoteRequest)` (message)
  * `[CreatePhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreatePhraseMatcherRequest)` (message)
  * `[CreateQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaQuestionRequest)` (message)
  * `[CreateQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaQuestionTagRequest)` (message)
  * `[CreateQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaScorecardRequest)` (message)
  * `[CreateQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaScorecardRevisionRequest)` (message)
  * `[CreateViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateViewRequest)` (message)
  * `[Dataset](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dataset)` (message)
  * `[Dataset.Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dataset.Type)` (enum)
  * `[DatasetValidationWarning](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DatasetValidationWarning)` (enum)
  * `[DeleteAnalysisRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAnalysisRequest)` (message)
  * `[DeleteAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAnalysisRuleRequest)` (message)
  * `[DeleteAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAssessmentRequest)` (message)
  * `[DeleteAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAssessmentRuleRequest)` (message)
  * `[DeleteAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAuthorizedViewRequest)` (message)
  * `[DeleteAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAuthorizedViewSetRequest)` (message)
  * `[DeleteConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteConversationRequest)` (message)
  * `[DeleteFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteFeedbackLabelRequest)` (message)
  * `[DeleteIssueModelMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteIssueModelMetadata)` (message)
  * `[DeleteIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteIssueModelRequest)` (message)
  * `[DeleteIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteIssueRequest)` (message)
  * `[DeleteNoteRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteNoteRequest)` (message)
  * `[DeletePhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeletePhraseMatcherRequest)` (message)
  * `[DeleteQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaQuestionRequest)` (message)
  * `[DeleteQaQuestionTagMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaQuestionTagMetadata)` (message)
  * `[DeleteQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaQuestionTagRequest)` (message)
  * `[DeleteQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaScorecardRequest)` (message)
  * `[DeleteQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaScorecardRevisionRequest)` (message)
  * `[DeleteViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteViewRequest)` (message)
  * `[DeployIssueModelMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeployIssueModelMetadata)` (message)
  * `[DeployIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeployIssueModelRequest)` (message)
  * `[DeployIssueModelResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeployIssueModelResponse)` (message)
  * `[DeployQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeployQaScorecardRevisionRequest)` (message)
  * `[DialogflowIntent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DialogflowIntent)` (message)
  * `[DialogflowInteractionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DialogflowInteractionData)` (message)
  * `[DialogflowSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DialogflowSource)` (message)
  * `[Dimension](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension)` (message)
  * `[Dimension.AgentDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.AgentDimensionMetadata)` (message)
  * `[Dimension.DimensionKey](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.DimensionKey)` (enum)
  * `[Dimension.IssueDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.IssueDimensionMetadata)` (message)
  * `[Dimension.QaQuestionAnswerDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.QaQuestionAnswerDimensionMetadata)` (message)
  * `[Dimension.QaQuestionDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.QaQuestionDimensionMetadata)` (message)
  * `[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.EncryptionSpec)` (message)
  * `[Entity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Entity)` (message)
  * `[Entity.Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Entity.Type)` (enum)
  * `[EntityMentionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.EntityMentionData)` (message)
  * `[EntityMentionData.MentionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.EntityMentionData.MentionType)` (enum)
  * `[ExactMatchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExactMatchConfig)` (message)
  * `[ExportInsightsDataMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataMetadata)` (message)
  * `[ExportInsightsDataRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest)` (message)
  * `[ExportInsightsDataRequest.BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest.BigQueryDestination)` (message)
  * `[ExportInsightsDataRequest.ExportSchemaVersion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest.ExportSchemaVersion)` (enum)
  * `[ExportInsightsDataRequest.WriteDisposition](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest.WriteDisposition)` (enum)
  * `[ExportInsightsDataResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataResponse)` (message)
  * `[ExportIssueModelMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportIssueModelMetadata)` (message)
  * `[ExportIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportIssueModelRequest)` (message)
  * `[ExportIssueModelRequest.GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportIssueModelRequest.GcsDestination)` (message)
  * `[ExportIssueModelResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportIssueModelResponse)` (message)
  * `[FaqAnswerData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FaqAnswerData)` (message)
  * `[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)` (message)
  * `[FinalizeAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FinalizeAssessmentRequest)` (message)
  * `[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GcsSource)` (message)
  * `[GetAnalysisRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAnalysisRequest)` (message)
  * `[GetAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAnalysisRuleRequest)` (message)
  * `[GetAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAssessmentRequest)` (message)
  * `[GetAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAssessmentRuleRequest)` (message)
  * `[GetAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAuthorizedViewRequest)` (message)
  * `[GetAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAuthorizedViewSetRequest)` (message)
  * `[GetConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetConversationRequest)` (message)
  * `[GetEncryptionSpecRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetEncryptionSpecRequest)` (message)
  * `[GetFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetFeedbackLabelRequest)` (message)
  * `[GetIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetIssueModelRequest)` (message)
  * `[GetIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetIssueRequest)` (message)
  * `[GetPhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetPhraseMatcherRequest)` (message)
  * `[GetQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaQuestionRequest)` (message)
  * `[GetQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaQuestionTagRequest)` (message)
  * `[GetQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaScorecardRequest)` (message)
  * `[GetQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaScorecardRevisionRequest)` (message)
  * `[GetSettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetSettingsRequest)` (message)
  * `[GetViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetViewRequest)` (message)
  * `[HoldData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.HoldData)` (message)
  * `[ImportIssueModelMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ImportIssueModelMetadata)` (message)
  * `[ImportIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ImportIssueModelRequest)` (message)
  * `[ImportIssueModelRequest.GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ImportIssueModelRequest.GcsSource)` (message)
  * `[ImportIssueModelResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ImportIssueModelResponse)` (message)
  * `[IngestConversationsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsMetadata)` (message)
  * `[IngestConversationsMetadata.IngestConversationsStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsMetadata.IngestConversationsStats)` (message)
  * `[IngestConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest)` (message)
  * `[IngestConversationsRequest.ConversationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.ConversationConfig)` (message)
  * `[IngestConversationsRequest.GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.GcsSource)` (message)
  * `[IngestConversationsRequest.GcsSource.BucketObjectType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.GcsSource.BucketObjectType)` (enum)
  * `[IngestConversationsRequest.TranscriptObjectConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.TranscriptObjectConfig)` (message)
  * `[IngestConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsResponse)` (message)
  * `[InitializeEncryptionSpecMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.InitializeEncryptionSpecMetadata)` (message)
  * `[InitializeEncryptionSpecRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.InitializeEncryptionSpecRequest)` (message)
  * `[InitializeEncryptionSpecResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.InitializeEncryptionSpecResponse)` (message)
  * `[Intent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Intent)` (message)
  * `[IntentMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IntentMatchData)` (message)
  * `[InterruptionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.InterruptionData)` (message)
  * `[Issue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Issue)` (message)
  * `[IssueAssignment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueAssignment)` (message)
  * `[IssueMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueMatchData)` (message)
  * `[IssueModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel)` (message)
  * `[IssueModel.InputDataConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel.InputDataConfig)` (message)
  * `[IssueModel.ModelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel.ModelType)` (enum)
  * `[IssueModel.State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel.State)` (enum)
  * `[IssueModelLabelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelLabelStats)` (message)
  * `[IssueModelLabelStats.IssueStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelLabelStats.IssueStats)` (message)
  * `[IssueModelResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelResult)` (message)
  * `[ListAllFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAllFeedbackLabelsRequest)` (message)
  * `[ListAllFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAllFeedbackLabelsResponse)` (message)
  * `[ListAnalysesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysesRequest)` (message)
  * `[ListAnalysesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysesResponse)` (message)
  * `[ListAnalysisRulesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysisRulesRequest)` (message)
  * `[ListAnalysisRulesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysisRulesResponse)` (message)
  * `[ListAssessmentRulesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentRulesRequest)` (message)
  * `[ListAssessmentRulesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentRulesResponse)` (message)
  * `[ListAssessmentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentsRequest)` (message)
  * `[ListAssessmentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentsResponse)` (message)
  * `[ListAuthorizedViewSetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewSetsRequest)` (message)
  * `[ListAuthorizedViewSetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewSetsResponse)` (message)
  * `[ListAuthorizedViewsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewsRequest)` (message)
  * `[ListAuthorizedViewsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewsResponse)` (message)
  * `[ListConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListConversationsRequest)` (message)
  * `[ListConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListConversationsResponse)` (message)
  * `[ListFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListFeedbackLabelsRequest)` (message)
  * `[ListFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListFeedbackLabelsResponse)` (message)
  * `[ListIssueModelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssueModelsRequest)` (message)
  * `[ListIssueModelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssueModelsResponse)` (message)
  * `[ListIssuesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssuesRequest)` (message)
  * `[ListIssuesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssuesResponse)` (message)
  * `[ListNotesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListNotesRequest)` (message)
  * `[ListNotesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListNotesResponse)` (message)
  * `[ListPhraseMatchersRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListPhraseMatchersRequest)` (message)
  * `[ListPhraseMatchersResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListPhraseMatchersResponse)` (message)
  * `[ListQaQuestionTagsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionTagsRequest)` (message)
  * `[ListQaQuestionTagsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionTagsResponse)` (message)
  * `[ListQaQuestionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionsRequest)` (message)
  * `[ListQaQuestionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionsResponse)` (message)
  * `[ListQaScorecardRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardRevisionsRequest)` (message)
  * `[ListQaScorecardRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardRevisionsResponse)` (message)
  * `[ListQaScorecardsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardsRequest)` (message)
  * `[ListQaScorecardsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardsResponse)` (message)
  * `[ListViewsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListViewsRequest)` (message)
  * `[ListViewsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListViewsResponse)` (message)
  * `[Note](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note)` (message)
  * `[Note.AssessmentNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note.AssessmentNote)` (message)
  * `[Note.ConversationTurnNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note.ConversationTurnNote)` (message)
  * `[Note.QaQuestionNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note.QaQuestionNote)` (message)
  * `[PhraseMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchData)` (message)
  * `[PhraseMatchRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRule)` (message)
  * `[PhraseMatchRuleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRuleConfig)` (message)
  * `[PhraseMatchRuleGroup](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRuleGroup)` (message)
  * `[PhraseMatchRuleGroup.PhraseMatchRuleGroupType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRuleGroup.PhraseMatchRuleGroupType)` (enum)
  * `[PhraseMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher)` (message)
  * `[PhraseMatcher.PhraseMatcherType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher.PhraseMatcherType)` (enum)
  * `[PublishAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PublishAssessmentRequest)` (message)
  * `[QaAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer)` (message)
  * `[QaAnswer.AnswerSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerSource)` (message)
  * `[QaAnswer.AnswerSource.SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerSource.SourceType)` (enum)
  * `[QaAnswer.AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerValue)` (message)
  * `[QaQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion)` (message)
  * `[QaQuestion.AnswerChoice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.AnswerChoice)` (message)
  * `[QaQuestion.Metrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.Metrics)` (message)
  * `[QaQuestion.PredefinedQuestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.PredefinedQuestionConfig)` (message)
  * `[QaQuestion.PredefinedQuestionConfig.PredefinedQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.PredefinedQuestionConfig.PredefinedQuestionType)` (enum)
  * `[QaQuestion.QaQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.QaQuestionType)` (enum)
  * `[QaQuestion.TuningMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.TuningMetadata)` (message)
  * `[QaQuestionTag](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestionTag)` (message)
  * `[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)` (message)
  * `[QaScorecardResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult)` (message)
  * `[QaScorecardResult.QaTagResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult.QaTagResult)` (message)
  * `[QaScorecardResult.ScoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult.ScoreSource)` (message)
  * `[QaScorecardResult.ScoreSource.SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult.ScoreSource.SourceType)` (enum)
  * `[QaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision)` (message)
  * `[QaScorecardRevision.State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision.State)` (enum)
  * `[QueryInterval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryInterval)` (message)
  * `[QueryMetricsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsMetadata)` (message)
  * `[QueryMetricsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsRequest)` (message)
  * `[QueryMetricsRequest.TimeGranularity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsRequest.TimeGranularity)` (enum)
  * `[QueryMetricsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse)` (message)
  * `[QueryMetricsResponse.Slice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice)` (message)
  * `[QueryMetricsResponse.Slice.DataPoint](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.DataPoint)` (message)
  * `[QueryMetricsResponse.Slice.DataPoint.ConversationMeasure](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.DataPoint.ConversationMeasure)` (message)
  * `[QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore)` (message)
  * `[QueryMetricsResponse.Slice.TimeSeries](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.TimeSeries)` (message)
  * `[QueryPerformanceOverviewMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryPerformanceOverviewMetadata)` (message)
  * `[QueryPerformanceOverviewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryPerformanceOverviewRequest)` (message)
  * `[QueryPerformanceOverviewRequest.AgentSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryPerformanceOverviewRequest.AgentSource)` (message)
  * `[QueryPerformanceOverviewResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryPerformanceOverviewResponse)` (message)
  * `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RedactionConfig)` (message)
  * `[RuntimeAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RuntimeAnnotation)` (message)
  * `[RuntimeAnnotation.UserInput](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RuntimeAnnotation.UserInput)` (message)
  * `[RuntimeAnnotation.UserInput.QuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RuntimeAnnotation.UserInput.QuerySource)` (enum)
  * `[SampleConversationsMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleConversationsMetadata)` (message)
  * `[SampleConversationsMetadata.SampleConversationsStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleConversationsMetadata.SampleConversationsStats)` (message)
  * `[SampleConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleConversationsRequest)` (message)
  * `[SampleConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleConversationsResponse)` (message)
  * `[SampleRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleRule)` (message)
  * `[ScheduleInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ScheduleInfo)` (message)
  * `[SearchAuthorizedViewsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SearchAuthorizedViewsRequest)` (message)
  * `[SearchAuthorizedViewsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SearchAuthorizedViewsResponse)` (message)
  * `[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SentimentData)` (message)
  * `[Settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Settings)` (message)
  * `[Settings.AnalysisConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Settings.AnalysisConfig)` (message)
  * `[SilenceData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SilenceData)` (message)
  * `[SmartComposeSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SmartComposeSuggestionData)` (message)
  * `[SmartReplyData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SmartReplyData)` (message)
  * `[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SpeechConfig)` (message)
  * `[TuneQaScorecardRevisionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionMetadata)` (message)
  * `[TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics)` (message)
  * `[TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics)` (message)
  * `[TuneQaScorecardRevisionMetadata.QaQuestionDatasetValidationResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionMetadata.QaQuestionDatasetValidationResult)` (message)
  * `[TuneQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionRequest)` (message)
  * `[TuneQaScorecardRevisionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionResponse)` (message)
  * `[UndeployIssueModelMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UndeployIssueModelMetadata)` (message)
  * `[UndeployIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UndeployIssueModelRequest)` (message)
  * `[UndeployIssueModelResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UndeployIssueModelResponse)` (message)
  * `[UndeployQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UndeployQaScorecardRevisionRequest)` (message)
  * `[UpdateAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAnalysisRuleRequest)` (message)
  * `[UpdateAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAssessmentRuleRequest)` (message)
  * `[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAuthorizedViewRequest)` (message)
  * `[UpdateAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAuthorizedViewSetRequest)` (message)
  * `[UpdateConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateConversationRequest)` (message)
  * `[UpdateFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateFeedbackLabelRequest)` (message)
  * `[UpdateIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateIssueModelRequest)` (message)
  * `[UpdateIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateIssueRequest)` (message)
  * `[UpdateNoteRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateNoteRequest)` (message)
  * `[UpdatePhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdatePhraseMatcherRequest)` (message)
  * `[UpdateQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaQuestionRequest)` (message)
  * `[UpdateQaQuestionTagMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaQuestionTagMetadata)` (message)
  * `[UpdateQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaQuestionTagRequest)` (message)
  * `[UpdateQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaScorecardRequest)` (message)
  * `[UpdateSettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateSettingsRequest)` (message)
  * `[UpdateViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateViewRequest)` (message)
  * `[UploadConversationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UploadConversationMetadata)` (message)
  * `[UploadConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UploadConversationRequest)` (message)
  * `[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UserInfo)` (message)
  * `[View](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.View)` (message)



## ContactCenterInsights

An API that lets users analyze and explore their business conversation data.

AppealAssessment  
---  
` rpc AppealAssessment(`[AppealAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AppealAssessmentRequest)`) returns (`[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)`) ` Appeal an Assessment.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessments.appeal`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
BulkAnalyzeConversations  
---  
` rpc BulkAnalyzeConversations(`[BulkAnalyzeConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkAnalyzeConversationsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Analyzes multiple conversations in a single request.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedAnalyses.create`
  * `contactcenterinsights.analyses.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
BulkDeleteConversations  
---  
` rpc BulkDeleteConversations(`[BulkDeleteConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteConversationsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes multiple conversations in a single request.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedConversations.delete`
  * `contactcenterinsights.datasetConversations.delete`
  * `contactcenterinsights.conversations.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
BulkDeleteFeedbackLabels  
---  
` rpc BulkDeleteFeedbackLabels(`[BulkDeleteFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteFeedbackLabelsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Delete feedback labels in bulk using a filter.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.delete`
  * `contactcenterinsights.datasetFeedbackLabels.delete`
  * `contactcenterinsights.feedbackLabels.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
BulkDownloadFeedbackLabels  
---  
` rpc BulkDownloadFeedbackLabels(`[BulkDownloadFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Download feedback labels in bulk from an external source. Currently supports exporting Quality AI example conversations with transcripts and question bodies.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.download`
  * `contactcenterinsights.feedbackLabels.download`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
BulkUploadFeedbackLabels  
---  
` rpc BulkUploadFeedbackLabels(`[BulkUploadFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Upload feedback labels from an external source in bulk. Currently supports labeling Quality AI example conversations.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.upload`
  * `contactcenterinsights.feedbackLabels.upload`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CalculateIssueModelStats  
---  
` rpc CalculateIssueModelStats(`[CalculateIssueModelStatsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateIssueModelStatsRequest)`) returns (`[CalculateIssueModelStatsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateIssueModelStatsResponse)`) ` Gets an issue model's statistics.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `issueModel` resource:

  * `contactcenterinsights.issueModels.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CalculateStats  
---  
` rpc CalculateStats(`[CalculateStatsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsRequest)`) returns (`[CalculateStatsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsResponse)`) ` Gets conversation statistics.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `location` resource:

  * `contactcenterinsights.authorizedConversations.list`
  * `contactcenterinsights.datasetConversations.list`
  * `contactcenterinsights.conversations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAnalysis  
---  
` rpc CreateAnalysis(`[CreateAnalysisRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAnalysisRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates an analysis. The long running operation is done when the analysis has completed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedAnalyses.create`
  * `contactcenterinsights.analyses.create`
  * `contactcenterinsights.datasetAnalyses.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAnalysisRule  
---  
` rpc CreateAnalysisRule(`[CreateAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAnalysisRuleRequest)`) returns (`[AnalysisRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisRule)`) ` Creates a analysis rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.analysisRules.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAssessment  
---  
` rpc CreateAssessment(`[CreateAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAssessmentRequest)`) returns (`[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)`) ` Create Assessment.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedAssessments.create`
  * `contactcenterinsights.assessments.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAssessmentRule  
---  
` rpc CreateAssessmentRule(`[CreateAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAssessmentRuleRequest)`) returns (`[AssessmentRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AssessmentRule)`) ` Creates an assessment rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.assessmentRules.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAuthorizedView  
---  
` rpc CreateAuthorizedView(`[CreateAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAuthorizedViewRequest)`) returns (`[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)`) ` Create AuthorizedView

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.authorizedViews.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAuthorizedViewSet  
---  
` rpc CreateAuthorizedViewSet(`[CreateAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateAuthorizedViewSetRequest)`) returns (`[AuthorizedViewSet](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedViewSet)`) ` Create AuthorizedViewSet

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.authorizedViewSets.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateConversation  
---  
` rpc CreateConversation(`[CreateConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateConversationRequest)`) returns (`[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)`) ` Creates a conversation. Note that this method does not support audio transcription or redaction. Use `conversations.upload` instead.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedConversations.create`
  * `contactcenterinsights.datasetConversations.create`
  * `contactcenterinsights.conversations.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateFeedbackLabel  
---  
` rpc CreateFeedbackLabel(`[CreateFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateFeedbackLabelRequest)`) returns (`[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)`) ` Create feedback label.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.create`
  * `contactcenterinsights.feedbackLabels.create`
  * `contactcenterinsights.datasetFeedbackLabels.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateIssue  
---  
` rpc CreateIssue(`[CreateIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates an issue.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.issues.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateIssueModel  
---  
` rpc CreateIssueModel(`[CreateIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueModelRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates an issue model.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.issueModels.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateNote  
---  
` rpc CreateNote(`[CreateNoteRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateNoteRequest)`) returns (`[Note](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note)`) ` Create Note.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.notes.create`
  * `contactcenterinsights.authorizedNotes.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreatePhraseMatcher  
---  
` rpc CreatePhraseMatcher(`[CreatePhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreatePhraseMatcherRequest)`) returns (`[PhraseMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher)`) ` Creates a phrase matcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.phraseMatchers.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateQaQuestion  
---  
` rpc CreateQaQuestion(`[CreateQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaQuestionRequest)`) returns (`[QaQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion)`) ` Create a QaQuestion.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaQuestions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateQaQuestionTag  
---  
` rpc CreateQaQuestionTag(`[CreateQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaQuestionTagRequest)`) returns (`[QaQuestionTag](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestionTag)`) ` Creates a QaQuestionTag.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaQuestionTags.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateQaScorecard  
---  
` rpc CreateQaScorecard(`[CreateQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaScorecardRequest)`) returns (`[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)`) ` Create a QaScorecard.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaScorecards.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateQaScorecardRevision  
---  
` rpc CreateQaScorecardRevision(`[CreateQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateQaScorecardRevisionRequest)`) returns (`[QaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision)`) ` Creates a QaScorecardRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaScorecardRevisions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateView  
---  
` rpc CreateView(`[CreateViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateViewRequest)`) returns (`[View](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.View)`) ` Creates a view.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.views.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAnalysis  
---  
` rpc DeleteAnalysis(`[DeleteAnalysisRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAnalysisRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an analysis.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.analyses.delete`
  * `contactcenterinsights.authorizedAnalyses.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAnalysisRule  
---  
` rpc DeleteAnalysisRule(`[DeleteAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAnalysisRuleRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a analysis rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.analysisRules.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAssessment  
---  
` rpc DeleteAssessment(`[DeleteAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAssessmentRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete an Assessment.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessments.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAssessmentRule  
---  
` rpc DeleteAssessmentRule(`[DeleteAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAssessmentRuleRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an assessment rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessmentRules.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAuthorizedView  
---  
` rpc DeleteAuthorizedView(`[DeleteAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAuthorizedViewRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an AuthorizedView.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.authorizedViews.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAuthorizedViewSet  
---  
` rpc DeleteAuthorizedViewSet(`[DeleteAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteAuthorizedViewSetRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an AuthorizedViewSet.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.authorizedViewSets.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteConversation  
---  
` rpc DeleteConversation(`[DeleteConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteConversationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a conversation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.authorizedConversations.delete`
  * `contactcenterinsights.conversations.delete`
  * `contactcenterinsights.datasetConversations.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteFeedbackLabel  
---  
` rpc DeleteFeedbackLabel(`[DeleteFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteFeedbackLabelRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Delete feedback label.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.authorizedFeedbackLabels.delete`
  * `contactcenterinsights.datasetFeedbackLabels.delete`
  * `contactcenterinsights.feedbackLabels.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteIssue  
---  
` rpc DeleteIssue(`[DeleteIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteIssueRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an issue.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issues.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteIssueModel  
---  
` rpc DeleteIssueModel(`[DeleteIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteIssueModelRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes an issue model.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issueModels.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteNote  
---  
` rpc DeleteNote(`[DeleteNoteRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteNoteRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a Note.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.notes.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeletePhraseMatcher  
---  
` rpc DeletePhraseMatcher(`[DeletePhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeletePhraseMatcherRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a phrase matcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.phraseMatchers.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteQaQuestion  
---  
` rpc DeleteQaQuestion(`[DeleteQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaQuestionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a QaQuestion.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaQuestions.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteQaQuestionTag  
---  
` rpc DeleteQaQuestionTag(`[DeleteQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaQuestionTagRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a QaQuestionTag.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaQuestionTags.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteQaScorecard  
---  
` rpc DeleteQaScorecard(`[DeleteQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaScorecardRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a QaScorecard.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaScorecards.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteQaScorecardRevision  
---  
` rpc DeleteQaScorecardRevision(`[DeleteQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaScorecardRevisionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a QaScorecardRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaScorecardRevisions.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteView  
---  
` rpc DeleteView(`[DeleteViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteViewRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a view.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.views.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeployIssueModel  
---  
` rpc DeployIssueModel(`[DeployIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeployIssueModelRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deploys an issue model. Returns an error if a model is already deployed. An issue model can only be used in analysis after it has been deployed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issueModels.deploy`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeployQaScorecardRevision  
---  
` rpc DeployQaScorecardRevision(`[DeployQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeployQaScorecardRevisionRequest)`) returns (`[QaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision)`) ` Deploy a QaScorecardRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaScorecardRevisions.deploy`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ExportInsightsData  
---  
` rpc ExportInsightsData(`[ExportInsightsDataRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Export insights data to a destination defined in the request body.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.datasetConversations.list`
  * `contactcenterinsights.conversations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ExportIssueModel  
---  
` rpc ExportIssueModel(`[ExportIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportIssueModelRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports an issue model to the provided destination.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issueModels.export`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
FinalizeAssessment  
---  
` rpc FinalizeAssessment(`[FinalizeAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FinalizeAssessmentRequest)`) returns (`[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)`) ` Finalize an Assessment.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessments.finalize`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAnalysis  
---  
` rpc GetAnalysis(`[GetAnalysisRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAnalysisRequest)`) returns (`[Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Analysis)`) ` Gets an analysis.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.analyses.get`
  * `contactcenterinsights.authorizedAnalyses.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAnalysisRule  
---  
` rpc GetAnalysisRule(`[GetAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAnalysisRuleRequest)`) returns (`[AnalysisRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisRule)`) ` Get a analysis rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.analysisRules.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAssessment  
---  
` rpc GetAssessment(`[GetAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAssessmentRequest)`) returns (`[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)`) ` Get Assessment.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessments.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAssessmentRule  
---  
` rpc GetAssessmentRule(`[GetAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAssessmentRuleRequest)`) returns (`[AssessmentRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AssessmentRule)`) ` Get an assessment rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessmentRules.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAuthorizedView  
---  
` rpc GetAuthorizedView(`[GetAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAuthorizedViewRequest)`) returns (`[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)`) ` Get AuthorizedView

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.authorizedViews.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAuthorizedViewSet  
---  
` rpc GetAuthorizedViewSet(`[GetAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetAuthorizedViewSetRequest)`) returns (`[AuthorizedViewSet](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedViewSet)`) ` Get AuthorizedViewSet

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.authorizedViewSets.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetConversation  
---  
` rpc GetConversation(`[GetConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetConversationRequest)`) returns (`[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)`) ` Gets a conversation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.authorizedConversations.get`
  * `contactcenterinsights.conversations.get`
  * `contactcenterinsights.datasetConversations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetEncryptionSpec  
---  
` rpc GetEncryptionSpec(`[GetEncryptionSpecRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetEncryptionSpecRequest)`) returns (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.EncryptionSpec)`) ` Gets location-level encryption key specification.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.encryptionSpecs.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetFeedbackLabel  
---  
` rpc GetFeedbackLabel(`[GetFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetFeedbackLabelRequest)`) returns (`[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)`) ` Get feedback label.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.authorizedFeedbackLabels.get`
  * `contactcenterinsights.datasetFeedbackLabels.get`
  * `contactcenterinsights.feedbackLabels.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetIssue  
---  
` rpc GetIssue(`[GetIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetIssueRequest)`) returns (`[Issue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Issue)`) ` Gets an issue.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issues.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetIssueModel  
---  
` rpc GetIssueModel(`[GetIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetIssueModelRequest)`) returns (`[IssueModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel)`) ` Gets an issue model.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issueModels.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetPhraseMatcher  
---  
` rpc GetPhraseMatcher(`[GetPhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetPhraseMatcherRequest)`) returns (`[PhraseMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher)`) ` Gets a phrase matcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.phraseMatchers.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetQaQuestion  
---  
` rpc GetQaQuestion(`[GetQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaQuestionRequest)`) returns (`[QaQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion)`) ` Gets a QaQuestion.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaQuestions.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetQaQuestionTag  
---  
` rpc GetQaQuestionTag(`[GetQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaQuestionTagRequest)`) returns (`[QaQuestionTag](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestionTag)`) ` Gets a QaQuestionTag.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaQuestionTags.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetQaScorecard  
---  
` rpc GetQaScorecard(`[GetQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaScorecardRequest)`) returns (`[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)`) ` Gets a QaScorecard.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaScorecards.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetQaScorecardRevision  
---  
` rpc GetQaScorecardRevision(`[GetQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetQaScorecardRevisionRequest)`) returns (`[QaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision)`) ` Gets a QaScorecardRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaScorecardRevisions.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetSettings  
---  
` rpc GetSettings(`[GetSettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetSettingsRequest)`) returns (`[Settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Settings)`) ` Gets project-level settings.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.settings.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetView  
---  
` rpc GetView(`[GetViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GetViewRequest)`) returns (`[View](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.View)`) ` Gets a view.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.views.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ImportIssueModel  
---  
` rpc ImportIssueModel(`[ImportIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ImportIssueModelRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Imports an issue model from a Cloud Storage bucket.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.issueModels.create`
  * `contactcenterinsights.issueModels.import`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
IngestConversations  
---  
` rpc IngestConversations(`[IngestConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Imports conversations and processes them according to the user's configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.datasetConversations.create`
  * `contactcenterinsights.conversations.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
InitializeEncryptionSpec  
---  
` rpc InitializeEncryptionSpec(`[InitializeEncryptionSpecRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.InitializeEncryptionSpecRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Initializes a location-level encryption key specification. An error will result if the location has resources already created before the initialization. After the encryption specification is initialized at a location, it is immutable and all newly created resources under the location will be encrypted with the existing specification.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.encryptionSpecs.initialize`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAllFeedbackLabels  
---  
` rpc ListAllFeedbackLabels(`[ListAllFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAllFeedbackLabelsRequest)`) returns (`[ListAllFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAllFeedbackLabelsResponse)`) ` List all feedback labels by project number.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.list`
  * `contactcenterinsights.datasetFeedbackLabels.list`
  * `contactcenterinsights.feedbackLabels.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAnalyses  
---  
` rpc ListAnalyses(`[ListAnalysesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysesRequest)`) returns (`[ListAnalysesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysesResponse)`) ` Lists analyses.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedAnalyses.list`
  * `contactcenterinsights.analyses.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAnalysisRules  
---  
` rpc ListAnalysisRules(`[ListAnalysisRulesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysisRulesRequest)`) returns (`[ListAnalysisRulesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAnalysisRulesResponse)`) ` Lists analysis rules.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.analysisRules.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAssessmentRules  
---  
` rpc ListAssessmentRules(`[ListAssessmentRulesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentRulesRequest)`) returns (`[ListAssessmentRulesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentRulesResponse)`) ` Lists assessment rules.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.assessmentRules.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAssessments  
---  
` rpc ListAssessments(`[ListAssessmentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentsRequest)`) returns (`[ListAssessmentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAssessmentsResponse)`) ` List Assessments.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedAssessments.list`
  * `contactcenterinsights.assessments.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAuthorizedViewSets  
---  
` rpc ListAuthorizedViewSets(`[ListAuthorizedViewSetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewSetsRequest)`) returns (`[ListAuthorizedViewSetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewSetsResponse)`) ` List AuthorizedViewSets

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.authorizedViewSets.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAuthorizedViews  
---  
` rpc ListAuthorizedViews(`[ListAuthorizedViewsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewsRequest)`) returns (`[ListAuthorizedViewsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListAuthorizedViewsResponse)`) ` List AuthorizedViewSets

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.authorizedViews.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListConversations  
---  
` rpc ListConversations(`[ListConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListConversationsRequest)`) returns (`[ListConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListConversationsResponse)`) ` Lists conversations.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedConversations.list`
  * `contactcenterinsights.datasetConversations.list`
  * `contactcenterinsights.conversations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListFeedbackLabels  
---  
` rpc ListFeedbackLabels(`[ListFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListFeedbackLabelsRequest)`) returns (`[ListFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListFeedbackLabelsResponse)`) ` List feedback labels.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.list`
  * `contactcenterinsights.feedbackLabels.list`
  * `contactcenterinsights.datasetFeedbackLabels.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListIssueModels  
---  
` rpc ListIssueModels(`[ListIssueModelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssueModelsRequest)`) returns (`[ListIssueModelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssueModelsResponse)`) ` Lists issue models.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.issueModels.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListIssues  
---  
` rpc ListIssues(`[ListIssuesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssuesRequest)`) returns (`[ListIssuesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListIssuesResponse)`) ` Lists issues.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.issues.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListNotes  
---  
` rpc ListNotes(`[ListNotesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListNotesRequest)`) returns (`[ListNotesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListNotesResponse)`) ` List Notes.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.notes.list`
  * `contactcenterinsights.authorizedNotes.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListPhraseMatchers  
---  
` rpc ListPhraseMatchers(`[ListPhraseMatchersRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListPhraseMatchersRequest)`) returns (`[ListPhraseMatchersResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListPhraseMatchersResponse)`) ` Lists phrase matchers.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.phraseMatchers.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListQaQuestionTags  
---  
` rpc ListQaQuestionTags(`[ListQaQuestionTagsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionTagsRequest)`) returns (`[ListQaQuestionTagsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionTagsResponse)`) ` Lists the question tags.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaQuestionTags.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListQaQuestions  
---  
` rpc ListQaQuestions(`[ListQaQuestionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionsRequest)`) returns (`[ListQaQuestionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaQuestionsResponse)`) ` Lists QaQuestions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaQuestions.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListQaScorecardRevisions  
---  
` rpc ListQaScorecardRevisions(`[ListQaScorecardRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardRevisionsRequest)`) returns (`[ListQaScorecardRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardRevisionsResponse)`) ` Lists all revisions under the parent QaScorecard.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaScorecardRevisions.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListQaScorecards  
---  
` rpc ListQaScorecards(`[ListQaScorecardsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardsRequest)`) returns (`[ListQaScorecardsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListQaScorecardsResponse)`) ` Lists QaScorecards.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaScorecards.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListViews  
---  
` rpc ListViews(`[ListViewsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListViewsRequest)`) returns (`[ListViewsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ListViewsResponse)`) ` Lists views.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.views.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
PublishAssessment  
---  
` rpc PublishAssessment(`[PublishAssessmentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PublishAssessmentRequest)`) returns (`[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)`) ` Publish an Assessment.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessments.publish`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
QueryMetrics  
---  
` rpc QueryMetrics(`[QueryMetricsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Query metrics.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `location` resource:

  * `contactcenterinsights.authorizedConversations.list`
  * `contactcenterinsights.conversations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
QueryPerformanceOverview  
---  
` rpc QueryPerformanceOverview(`[QueryPerformanceOverviewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryPerformanceOverviewRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Generates a summary of predefined performance metrics for a set of conversations. Conversations can be specified by specifying a time window and an agent id, for now. The summary includes a comparison of metrics computed for conversations in the previous time period, and also a comparison with peers in the same time period.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedConversations.list`
  * `contactcenterinsights.conversations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
SearchAuthorizedViews  
---  
` rpc SearchAuthorizedViews(`[SearchAuthorizedViewsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SearchAuthorizedViewsRequest)`) returns (`[SearchAuthorizedViewsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SearchAuthorizedViewsResponse)`) ` SearchAuthorizedViewSets

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
TuneQaScorecardRevision  
---  
` rpc TuneQaScorecardRevision(`[TuneQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Fine tune one or more QaModels.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `contactcenterinsights.qaScorecardRevisions.tune`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UndeployIssueModel  
---  
` rpc UndeployIssueModel(`[UndeployIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UndeployIssueModelRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Undeploys an issue model. An issue model can not be used in analysis after it has been undeployed.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issueModels.undeploy`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UndeployQaScorecardRevision  
---  
` rpc UndeployQaScorecardRevision(`[UndeployQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UndeployQaScorecardRevisionRequest)`) returns (`[QaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision)`) ` Undeploy a QaScorecardRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaScorecardRevisions.undeploy`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateAnalysisRule  
---  
` rpc UpdateAnalysisRule(`[UpdateAnalysisRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAnalysisRuleRequest)`) returns (`[AnalysisRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisRule)`) ` Updates a analysis rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.analysisRules.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateAssessmentRule  
---  
` rpc UpdateAssessmentRule(`[UpdateAssessmentRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAssessmentRuleRequest)`) returns (`[AssessmentRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AssessmentRule)`) ` Updates an assessment rule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.assessmentRules.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateAuthorizedView  
---  
` rpc UpdateAuthorizedView(`[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAuthorizedViewRequest)`) returns (`[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)`) ` Updates an AuthorizedView.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.authorizedViews.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateAuthorizedViewSet  
---  
` rpc UpdateAuthorizedViewSet(`[UpdateAuthorizedViewSetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateAuthorizedViewSetRequest)`) returns (`[AuthorizedViewSet](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedViewSet)`) ` Updates an AuthorizedViewSet.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.authorizedViewSets.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateConversation  
---  
` rpc UpdateConversation(`[UpdateConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateConversationRequest)`) returns (`[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)`) ` Updates a conversation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.authorizedConversations.update`
  * `contactcenterinsights.conversations.update`
  * `contactcenterinsights.datasetConversations.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateFeedbackLabel  
---  
` rpc UpdateFeedbackLabel(`[UpdateFeedbackLabelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateFeedbackLabelRequest)`) returns (`[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)`) ` Update feedback label.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.authorizedFeedbackLabels.update`
  * `contactcenterinsights.datasetFeedbackLabels.update`
  * `contactcenterinsights.feedbackLabels.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateIssue  
---  
` rpc UpdateIssue(`[UpdateIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateIssueRequest)`) returns (`[Issue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Issue)`) ` Updates an issue.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issues.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateIssueModel  
---  
` rpc UpdateIssueModel(`[UpdateIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateIssueModelRequest)`) returns (`[IssueModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel)`) ` Updates an issue model.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.issueModels.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateNote  
---  
` rpc UpdateNote(`[UpdateNoteRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateNoteRequest)`) returns (`[Note](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note)`) ` Update Note.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.notes.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdatePhraseMatcher  
---  
` rpc UpdatePhraseMatcher(`[UpdatePhraseMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdatePhraseMatcherRequest)`) returns (`[PhraseMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher)`) ` Updates a phrase matcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.phraseMatchers.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateQaQuestion  
---  
` rpc UpdateQaQuestion(`[UpdateQaQuestionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaQuestionRequest)`) returns (`[QaQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion)`) ` Updates a QaQuestion.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaQuestions.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateQaQuestionTag  
---  
` rpc UpdateQaQuestionTag(`[UpdateQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaQuestionTagRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a QaQuestionTag.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaQuestionTags.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateQaScorecard  
---  
` rpc UpdateQaScorecard(`[UpdateQaScorecardRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaScorecardRequest)`) returns (`[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)`) ` Updates a QaScorecard.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.qaScorecards.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateSettings  
---  
` rpc UpdateSettings(`[UpdateSettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateSettingsRequest)`) returns (`[Settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Settings)`) ` Updates project-level settings.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.settings.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateView  
---  
` rpc UpdateView(`[UpdateViewRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateViewRequest)`) returns (`[View](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.View)`) ` Updates a view.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contactcenterinsights.views.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UploadConversation  
---  
` rpc UploadConversation(`[UploadConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UploadConversationRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Create a long-running conversation upload operation. This method differs from `CreateConversation` by allowing audio transcription and optional DLP redaction.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedConversations.upload`
  * `contactcenterinsights.datasetConversations.upload`
  * `contactcenterinsights.conversations.upload`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## Analysis

The analysis resource.

Fields  
---  
`name` |  `string` Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}  
`request_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the analysis was requested.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the analysis was created, which occurs when the long-running operation completes.  
`analysis_result` |  `[AnalysisResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisResult)` Output only. The result of the analysis, which is populated when the analysis finishes.  
`annotator_selector` |  `[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector)` To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.  
  
## AnalysisResult

The result of an analysis.

Fields  
---  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which the analysis ended.  
Union field `metadata`. Metadata discovered during analysis. `metadata` can be only one of the following:  
`call_analysis_metadata` |  `[CallAnalysisMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisResult.CallAnalysisMetadata)` Call-specific metadata created by the analysis.  
  
## CallAnalysisMetadata

Call-specific metadata created during analysis.

Fields  
---  
`annotations[]` |  `[CallAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CallAnnotation)` A list of call annotations that apply to this call.  
`entities` |  `map<string, `[Entity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Entity)`>` All the entities in the call.  
`sentiments[]` |  `[ConversationLevelSentiment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationLevelSentiment)` Overall conversation-level sentiment for each channel of the call.  
`silence` |  `[ConversationLevelSilence](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationLevelSilence)` Overall conversation-level silence during the call.  
`intents` |  `map<string, `[Intent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Intent)`>` All the matched intents in the call.  
`phrase_matchers` |  `map<string, `[PhraseMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchData)`>` All the matched phrase matchers in the call.  
`issue_model_result` |  `[IssueModelResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelResult)` Overall conversation-level issue modeling result.  
`qa_scorecard_results[]` |  `[QaScorecardResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult)` Results of scoring QaScorecards.  
  
## AnalysisRule

The CCAI Insights project wide analysis rule. This rule will be applied to all conversations that match the filter defined in the rule. For a conversation matches the filter, the annotators specified in the rule will be run. If a conversation matches multiple rules, a union of all the annotators will be run. One project can have multiple analysis rules.

Fields  
---  
`name` |  `string` Identifier. The resource name of the analysis rule. Format: projects/{project}/locations/{location}/analysisRules/{analysis_rule}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this analysis rule was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which this analysis rule was updated.  
`conversation_filter` |  `string` Filter for the conversations that should apply this analysis rule. An empty filter means this analysis rule applies to all conversations. Refer to <https://cloud.google.com/gemini-enterprise-cx/insights/filtering> for details.  
`annotator_selector` |  `[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector)` Selector of annotators to run and the phrase matchers to use for conversations that matches the conversation_filter. If not specified, NO annotators will be run.  
`analysis_percentage` |  `double` Percentage of conversations that we should apply this analysis setting automatically, between [0, 1]. For example, 0.1 means 10%. Conversations are sampled in a determenestic way. The original runtime_percentage & upload percentage will be replaced by defining filters on the conversation.  
`active` |  `bool` If true, apply this rule to conversations. Otherwise, this rule is inactive and saved as a draft.  
`display_name` |  `string` Display Name of the analysis rule.  
  
## AnnotationBoundary

A point in a conversation that marks the start or the end of an annotation.

Fields  
---  
`transcript_index` |  `int32` The index in the sequence of transcribed pieces of the conversation where the boundary is located. This index starts at zero.  
Union field `detailed_boundary`. A detailed boundary, which describes a more specific point. `detailed_boundary` can be only one of the following:  
`word_index` |  `int32` The word index of this boundary with respect to the first word in the transcript piece. This index starts at zero.  
  
## AnnotatorSelector

Selector of all available annotators and phrase matchers to run.

Fields  
---  
`run_interruption_annotator` |  `bool` Whether to run the interruption annotator.  
`run_silence_annotator` |  `bool` Whether to run the silence annotator.  
`run_phrase_matcher_annotator` |  `bool` Whether to run the active phrase matcher annotator(s).  
`phrase_matchers[]` |  `string` The list of phrase matchers to run. If not provided, all active phrase matchers will be used. If inactive phrase matchers are provided, they will not be used. Phrase matchers will be run only if run_phrase_matcher_annotator is set to true. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher}  
`run_sentiment_annotator` |  `bool` Whether to run the sentiment annotator.  
`run_entity_annotator` |  `bool` Whether to run the entity annotator.  
`run_intent_annotator` |  `bool` Whether to run the intent annotator.  
`run_issue_model_annotator` |  `bool` Whether to run the issue model annotator. A model should have already been deployed for this to take effect.  
`issue_models[]` |  `string` The issue model to run. If not provided, the most recently deployed topic model will be used. The provided issue model will only be used for inference if the issue model is deployed and if run_issue_model_annotator is set to true. If more than one issue model is provided, only the first provided issue model will be used for inference.  
`run_summarization_annotator` |  `bool` Whether to run the summarization annotator.  
`summarization_config` |  `[SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.SummarizationConfig)` Configuration for the summarization annotator.  
`run_qa_annotator` |  `bool` Whether to run the QA annotator.  
`qa_config` |  `[QaConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.QaConfig)` Configuration for the QA annotator.  
  
## QaConfig

Configuration for the QA feature.

Fields  
---  
Union field `scorecard_source`. Which scorecards should be scored. `scorecard_source` can be only one of the following:  
`scorecard_list` |  `[ScorecardList](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.QaConfig.ScorecardList)` A manual list of scorecards to score.  
  
## ScorecardList

Container for a list of scorecards.

Fields  
---  
`qa_scorecard_revisions[]` |  `string` List of QaScorecardRevisions.  
  
## SummarizationConfig

Configuration for summarization.

Fields  
---  
Union field `model_source`. Summarization must use either a preexisting conversation profile or one of the supported default models. `model_source` can be only one of the following:  
`conversation_profile` |  `string` Resource name of the Dialogflow conversation profile. Format: projects/{project}/locations/{location}/conversationProfiles/{conversation_profile}  
`summarization_model` |  `[SummarizationModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector.SummarizationConfig.SummarizationModel)` Default summarization model to be used.  
`generator` |  `string` The resource name of the existing created generator. Format: projects//locations//generators/  
  
## SummarizationModel

Summarization model to use, if `conversation_profile` is not used.

Enums  
---  
`SUMMARIZATION_MODEL_UNSPECIFIED` | Unspecified summarization model.  
`BASELINE_MODEL` | The CCAI baseline model. This model is deprecated and will be removed in the future. We recommend using `generator` instead.This item is deprecated!  
`BASELINE_MODEL_V2_0` | The CCAI baseline model, V2.0. This model is deprecated and will be removed in the future. We recommend using `generator` instead.This item is deprecated!  
  
## AnswerFeedback

The feedback that the customer has about a certain answer in the conversation.

Fields  
---  
`correctness_level` |  `[CorrectnessLevel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnswerFeedback.CorrectnessLevel)` The correctness level of an answer.  
`clicked` |  `bool` Indicates whether an answer or item was clicked by the human agent.  
`displayed` |  `bool` Indicates whether an answer or item was displayed to the human agent in the agent desktop UI.  
  
## CorrectnessLevel

The correctness level of an answer.

Enums  
---  
`CORRECTNESS_LEVEL_UNSPECIFIED` | Correctness level unspecified.  
`NOT_CORRECT` | Answer is totally wrong.  
`PARTIALLY_CORRECT` | Answer is partially correct.  
`FULLY_CORRECT` | Answer is fully correct.  
  
## AppealAssessmentRequest

The message to appeal an assessment.

Fields  
---  
`name` |  `string` Required. The name of the assessment to appeal.  
  
## ArticleSuggestionData

Agent Assist Article Suggestion data.

Fields  
---  
`title` |  `string` Article title.  
`uri` |  `string` Article URI.  
`confidence_score` |  `float` The system's confidence score that this article is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`metadata` |  `map<string, string>` Map that contains metadata about the Article Suggestion and the document that it originates from.  
`query_record` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record}  
`source` |  `string` The knowledge document that this answer was extracted from. Format: projects/{project}/knowledgeBases/{knowledge_base}/documents/{document}  
  
## Assessment

The assessment resource.

Fields  
---  
`name` |  `string` Identifier. The resource name of the assessment. Format: projects/{project}/locations/{location}/conversations/{conversation}/assessments/{assessment}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the assessment was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the assessment was last updated.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment.State)` Output only. The state of the assessment.  
`agent_info` |  `[AgentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.QualityMetadata.AgentInfo)` Information about the agent the assessment is for.  
  
## State

The state of the assessment. Defaults to DRAFT.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unspecified. This value should not be used.  
`DRAFT` | The default state of all new assessments.  
`PUBLISHED` | The assessment has been published.  
`APPEALED` | The assessment has been appealed.  
`FINALIZED` | The assessment has been finalized.  
  
## AssessmentRule

The CCAI Insights project wide assessment rule. This assessment rule will be applied to all conversations from the previous sampling cycle that match the sample rule defined in the assessment rule. One project can have multiple assessment rules.

Fields  
---  
`name` |  `string` Identifier. The resource name of the assessment rule. Format: projects/{project}/locations/{location}/assessmentRules/{assessment_rule}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this assessment rule was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which this assessment rule was updated.  
`active` |  `bool` If true, apply this rule to conversations. Otherwise, this rule is inactive.  
`sample_rule` |  `[SampleRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleRule)` The sample rule for the assessment rule.  
`schedule_info` |  `[ScheduleInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ScheduleInfo)` Schedule info for the assessment rule.  
`display_name` |  `string` Display Name of the assessment rule.  
  
## AuthorizedView

An AuthorizedView represents a view of accessible Insights resources (for example, Conversation and Scorecard). Who have read access to the AuthorizedView resource will have access to these Insight resources as well.

Fields  
---  
`name` |  `string` Identifier. The resource name of the AuthorizedView. Format: projects/{project}/locations/{location}/authorizedViewSets/{authorized_view_set}/authorizedViews/{authorized_view}  
`display_name` |  `string` Display Name. Limit 64 characters.  
`conversation_filter` |  `string` A filter to reduce conversation results to a specific subset. The AuthorizedView's assigned permission (read/write) could be applied to the subset of conversations.If conversation_filter is empty, there is no restriction on the conversations that the AuthorizedView can access.Having _authorizedViews.get_ access to the AuthorizedView means having the same read/write access to the Conversations (as well as metadata/annotations linked to the conversation) that this AuthorizedView has.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the authorized view was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the authorized view was updated.  
  
## AuthorizedViewSet

An AuthorizedViewSet contains a set of AuthorizedView resources.

Fields  
---  
`name` |  `string` Identifier. The resource name of the AuthorizedViewSet. Format: projects/{project}/locations/{location}/authorizedViewSets/{authorized_view_set}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create time.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Update time.  
`display_name` |  `string` Display Name. Limit 64 characters.  
  
## BulkAnalyzeConversationsMetadata

The metadata for a bulk analyze conversations operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation finished running.  
`request` |  `[BulkAnalyzeConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkAnalyzeConversationsRequest)` The original request for bulk analyze.  
`completed_analyses_count` |  `int32` The number of requested analyses that have completed successfully so far.  
`failed_analyses_count` |  `int32` The number of requested analyses that have failed so far.  
`total_requested_analyses_count` |  `int32` Total number of analyses requested. Computed by the number of conversations returned by `filter` multiplied by `analysis_percentage` in the request.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Output only. Partial errors during bulk analyze operation that might cause the operation output to be incomplete.  
  
## BulkAnalyzeConversationsRequest

The request to analyze conversations in bulk.

Fields  
---  
`parent` |  `string` Required. The parent resource to create analyses in.  
`filter` |  `string` Required. Filter used to select the subset of conversations to analyze.  
`analysis_percentage` |  `float` Required. Percentage of selected conversation to analyze, between [0, 100].  
`annotator_selector` |  `[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector)` To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.  
  
## BulkAnalyzeConversationsResponse

The response for a bulk analyze conversations operation.

Fields  
---  
`successful_analysis_count` |  `int32` Count of successful analyses.  
`failed_analysis_count` |  `int32` Count of failed analyses.  
  
## BulkDeleteConversationsMetadata

The metadata for a bulk delete conversations operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation finished running.  
`request` |  `[BulkDeleteConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteConversationsRequest)` The original request for bulk delete.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Partial errors during bulk delete conversations operation that might cause the operation output to be incomplete.  
  
## BulkDeleteConversationsRequest

The request to delete conversations in bulk.

Fields  
---  
`parent` |  `string` Required. The parent resource to delete conversations from. Format: projects/{project}/locations/{location}  
`filter` |  `string` Filter used to select the subset of conversations to delete.  
`max_delete_count` |  `int32` Maximum number of conversations to delete.  
`force` |  `bool` If set to true, all of this conversation's analyses will also be deleted. Otherwise, the request will only succeed if the conversation has no analyses.  
  
## BulkDeleteConversationsResponse

This type has no fields.

The response for a bulk delete conversations operation.

## BulkDeleteFeedbackLabelsMetadata

Metadata for the BulkDeleteFeedbackLabels endpoint.

Fields  
---  
`request` |  `[BulkDeleteFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDeleteFeedbackLabelsRequest)` Output only. The original request for delete.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Partial errors during deletion operation that might cause the operation output to be incomplete.  
  
## BulkDeleteFeedbackLabelsRequest

Request for the BulkDeleteFeedbackLabels endpoint.

Fields  
---  
`parent` |  `string` Required. The parent resource for new feedback labels.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset. Supports disjunctions (OR) and conjunctions (AND).Supported fields:

  * `issue_model_id`
  * `qa_question_id`
  * `qa_scorecard_id`
  * `min_create_time`
  * `max_create_time`
  * `min_update_time`
  * `max_update_time`
  * `feedback_label_type`: QUALITY_AI, TOPIC_MODELING

  
  
## BulkDeleteFeedbackLabelsResponse

This type has no fields.

Response for the BulkDeleteFeedbackLabels endpoint.

## BulkDownloadFeedbackLabelsMetadata

Metadata for the BulkDownloadFeedbackLabel endpoint.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[BulkDownloadFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest)` Output only. The original request for download.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Partial errors during ingest operation that might cause the operation output to be incomplete.  
`download_stats` |  `[DownloadStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsMetadata.DownloadStats)` Output only. Statistics for BulkDownloadFeedbackLabels operation.  
  
## DownloadStats

Statistics for BulkDownloadFeedbackLabels operation.

Fields  
---  
`processed_object_count` |  `int32` The number of objects processed during the download operation.  
`successful_download_count` |  `int32` The number of new feedback labels downloaded during this operation. Different from "processed" because some labels might not be downloaded because an error.  
`total_files_written` |  `int32` Total number of files written to the provided Cloud Storage bucket.  
`file_names[]` |  `string` Output only. Full name of the files written to Cloud storage.  
  
## BulkDownloadFeedbackLabelsRequest

Request for the BulkDownloadFeedbackLabel endpoint.

Fields  
---  
`parent` |  `string` Required. The parent resource for new feedback labels.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset. Supports disjunctions (OR) and conjunctions (AND).Supported fields:

  * `issue_model_id`
  * `qa_question_id`
  * `qa_scorecard_id`
  * `min_create_time`
  * `max_create_time`
  * `min_update_time`
  * `max_update_time`
  * `feedback_label_type`: QUALITY_AI, TOPIC_MODELING

  
`max_download_count` |  `int32` Optional. Limits the maximum number of feedback labels that will be downloaded. The first `N` feedback labels will be downloaded.  
`feedback_label_type` |  `[FeedbackLabelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.FeedbackLabelType)` Optional. The type of feedback labels that will be downloaded.  
`conversation_filter` |  `string` Optional. Filter parent conversations to download feedback labels for. When specified, the feedback labels will be downloaded for the conversations that match the filter. If `template_qa_scorecard_id` is set, all the conversations that match the filter will be paired with the questions under the scorecard for labeling.  
`template_qa_scorecard_id[]` |  `string` Optional. If set, a template for labeling conversations and scorecard questions will be created from the conversation_filter and the questions under the scorecard(s). The feedback label `filter` will be ignored.  
Union field `destination`. Configuration for an external data store to which the feedback labels will be written to. `destination` can be only one of the following:  
`gcs_destination` |  `[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.GcsDestination)` A cloud storage bucket destination.  
`sheets_destination` |  `[SheetsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.SheetsDestination)` A sheets document destination.  
  
## FeedbackLabelType

Possible feedback label types that will be downloaded.

Enums  
---  
`FEEDBACK_LABEL_TYPE_UNSPECIFIED` | Unspecified format  
`QUALITY_AI` | Downloaded file will contain all Quality AI labels from the latest scorecard revision.  
`TOPIC_MODELING` | Downloaded file will contain only Topic Modeling labels.  
`AGENT_ASSIST_SUMMARY` | Agent Assist Summarization labels.  
  
## GcsDestination

Google Cloud Storage Object details to write the feedback labels to.

Fields  
---  
`format` |  `[Format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkDownloadFeedbackLabelsRequest.GcsDestination.Format)` Required. File format in which the labels will be exported.  
`object_uri` |  `string` Required. The Google Cloud Storage URI to write the feedback labels to. The file name will be used as a prefix for the files written to the bucket if the output needs to be split across multiple files, otherwise it will be used as is. The file extension will be appended to the file name based on the format selected. E.g. `gs://bucket_name/object_uri_prefix`  
`add_whitespace` |  `bool` Optional. Add whitespace to the JSON file. Makes easier to read, but increases file size. Only applicable for JSON format.  
`always_print_empty_fields` |  `bool` Optional. Always print fields with no presence. This is useful for printing fields that are not set, like implicit 0 value or empty lists/maps. Only applicable for JSON format.  
`records_per_file_count` |  `int64` Optional. The number of records per file. Applicable for either format.  
  
## Format

All permissible file formats. See `records_per_file_count` to override the default number of records per file.

Enums  
---  
`FORMAT_UNSPECIFIED` | Unspecified format.  
`CSV` | CSV format. 1,000 labels are stored per CSV file by default.  
`JSON` | JSON format. 1 label stored per JSON file by default.  
  
## SheetsDestination

Google Sheets document details to write the feedback labels to.

Fields  
---  
`spreadsheet_uri` |  `string` Required. The Google Sheets document to write the feedback labels to. Retrieved from Google Sheets URI. E.g. `https://docs.google.com/spreadsheets/d/1234567890` The spreadsheet must be shared with the Insights P4SA. The spreadsheet ID written to will be returned as `file_names` in the BulkDownloadFeedbackLabelsMetadata.  
`sheet_title` |  `string` Optional. The title of the new sheet to write the feedback labels to.  
  
## BulkDownloadFeedbackLabelsResponse

This type has no fields.

Response for the BulkDownloadFeedbackLabel endpoint.

## BulkUploadFeedbackLabelsMetadata

Metadata for the Bulk Upload Feedback Labels API.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[BulkUploadFeedbackLabelsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest)` Output only. The original request for ingest.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Partial errors during ingest operation that might cause the operation output to be incomplete.  
`upload_stats` |  `[UploadStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsMetadata.UploadStats)` Output only. Statistics for BulkUploadFeedbackLabels operation.  
  
## UploadStats

Statistics for BulkUploadFeedbackLabels operation.

Fields  
---  
`processed_object_count` |  `int32` The number of objects processed during the upload operation.  
`failed_validation_count` |  `int32` The number of objects skipped because of failed validation  
`successful_upload_count` |  `int32` The number of new feedback labels added during this ingest operation.  
  
## BulkUploadFeedbackLabelsRequest

The request for bulk uploading feedback labels.

Fields  
---  
`parent` |  `string` Required. The parent resource for new feedback labels.  
`validate_only` |  `bool` Optional. If set, upload will not happen and the labels will be validated. If not set, then default behavior will be to upload the labels after validation is complete.  
Union field `source`. Configuration for an external data store containing objects that will be converted to FeedbackLabels. `source` can be only one of the following:  
`gcs_source` |  `[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest.GcsSource)` A cloud storage bucket source.  
`sheets_source` |  `[SheetsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest.SheetsSource)` A sheets document source.  
  
## GcsSource

Google Cloud Storage Object details to get the feedback label file from.

Fields  
---  
`format` |  `[Format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.BulkUploadFeedbackLabelsRequest.GcsSource.Format)` Required. File format which will be ingested.  
`object_uri` |  `string` Required. The Google Cloud Storage URI of the file to import. Format: `gs://bucket_name/object_name`  
  
## Format

All permissible file formats.

Enums  
---  
`FORMAT_UNSPECIFIED` | Unspecified format.  
`CSV` | CSV format.  
`JSON` | JSON format.  
  
## SheetsSource

Google Sheets document details to get the feedback label file from.

Fields  
---  
`spreadsheet_uri` |  `string` Required. The Google Sheets document to write the feedback labels to. Retrieved from Google Sheets URI. E.g. `https://docs.google.com/spreadsheets/d/1234567890` The spreadsheet must be shared with the Insights P4SA.  
  
## BulkUploadFeedbackLabelsResponse

This type has no fields.

Response for the Bulk Upload Feedback Labels API.

## CalculateIssueModelStatsRequest

Request to get statistics of an issue model.

Fields  
---  
`issue_model` |  `string` Required. The resource name of the issue model to query against.  
  
## CalculateIssueModelStatsResponse

Response of querying an issue model's statistics.

Fields  
---  
`current_stats` |  `[IssueModelLabelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelLabelStats)` The latest label statistics for the queried issue model. Includes results on both training data and data labeled after deployment.  
  
## CalculateStatsRequest

The request for calculating conversation statistics.

Fields  
---  
`location` |  `string` Required. The location of the conversations.  
`filter` |  `string` A filter to reduce results to a specific subset. This field is useful for getting statistics about conversations with specific properties.  
  
## CalculateStatsResponse

The response for calculating conversation statistics.

Fields  
---  
`average_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The average duration of all conversations. The average is calculated using only conversations that have a time duration.  
`average_turn_count` |  `int32` The average number of turns per conversation.  
`conversation_count` |  `int32` The total number of conversations.  
`smart_highlighter_matches` |  `map<string, int32>` A map associating each smart highlighter display name with its respective number of matches in the set of conversations.  
`custom_highlighter_matches` |  `map<string, int32>` A map associating each custom highlighter resource name with its respective number of matches in the set of conversations.  
`issue_matches  
**(deprecated)**` |  `map<string, int32>` This item is deprecated!A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: `projects/<Project-ID>/locations/<Location-ID>/issueModels/<Issue-Model-ID>/issues/<Issue-ID>` Deprecated, use `issue_matches_stats` field instead.  
`issue_matches_stats` |  `map<string, `[IssueStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelLabelStats.IssueStats)`>` A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: `projects/<Project-ID>/locations/<Location-ID>/issueModels/<Issue-Model-ID>/issues/<Issue-ID>`  
`conversation_count_time_series` |  `[TimeSeries](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsResponse.TimeSeries)` A time series representing the count of conversations created over time that match that requested filter criteria.  
  
## TimeSeries

A time series representing conversations over time.

Fields  
---  
`interval_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The duration of each interval.  
`points[]` |  `[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CalculateStatsResponse.TimeSeries.Interval)` An ordered list of intervals from earliest to latest, where each interval represents the number of conversations that transpired during the time window.  
  
## Interval

A single interval in a time series.

Fields  
---  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The start time of this interval.  
`conversation_count` |  `int32` The number of conversations created in this interval.  
  
## CallAnnotation

A piece of metadata that applies to a window of a call.

Fields  
---  
`channel_tag` |  `int32` The channel of the audio where the annotation occurs. For single-channel audio, this field is not populated.  
`annotation_start_boundary` |  `[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotationBoundary)` The boundary in the conversation where the annotation starts, inclusive.  
`annotation_end_boundary` |  `[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotationBoundary)` The boundary in the conversation where the annotation ends, inclusive.  
Union field `data`. The data in the annotation. `data` can be only one of the following:  
`interruption_data` |  `[InterruptionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.InterruptionData)` Data specifying an interruption.  
`sentiment_data` |  `[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SentimentData)` Data specifying sentiment.  
`silence_data` |  `[SilenceData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SilenceData)` Data specifying silence.  
`hold_data` |  `[HoldData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.HoldData)` Data specifying a hold.  
`entity_mention_data` |  `[EntityMentionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.EntityMentionData)` Data specifying an entity mention.  
`intent_match_data` |  `[IntentMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IntentMatchData)` Data specifying an intent match.  
`phrase_match_data` |  `[PhraseMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchData)` Data specifying a phrase match.  
`issue_match_data` |  `[IssueMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueMatchData)` Data specifying an issue match.  
  
## Conversation

The conversation resource.

Fields  
---  
`name` |  `string` Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation}  
`data_source` |  `[ConversationDataSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationDataSource)` The source of the audio and transcription for the conversation.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the conversation was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the conversation was updated.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which the conversation started.  
`language_code` |  `string` A user-specified language code for the conversation.  
`agent_id` |  `string` An opaque, user-specified string representing the human agent who handled the conversation.  
`labels` |  `map<string, string>` A map for the user to specify any custom fields. A maximum of 100 labels per conversation is allowed, with a maximum of 256 characters per entry.  
`quality_metadata` |  `[QualityMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.QualityMetadata)` Conversation metadata related to quality management.  
`metadata_json` |  `string` Input only. JSON metadata encoded as a string. This field is primarily used by Insights integrations with various telephony systems and must be in one of Insight's supported formats.  
`transcript` |  `[Transcript](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript)` Output only. The conversation transcript.  
`medium` |  `[Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Medium)` Immutable. The conversation medium, if unspecified will default to PHONE_CALL.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The duration of the conversation.  
`turn_count` |  `int32` Output only. The number of turns in the conversation.  
`latest_analysis` |  `[Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Analysis)` Output only. The conversation's latest analysis, if one exists.  
`latest_summary` |  `[ConversationSummarizationSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationSummarizationSuggestionData)` Output only. Latest summary of the conversation.  
`runtime_annotations[]` |  `[RuntimeAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RuntimeAnnotation)` Output only. The annotations that were generated during the customer and agent interaction.  
`dialogflow_intents` |  `map<string, `[DialogflowIntent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DialogflowIntent)`>` Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/{project}/agent/{agent}/intents/{intent}  
`obfuscated_user_id` |  `string` Obfuscated user ID which the customer sent to us.  
Union field `metadata`. Metadata that applies to the conversation. `metadata` can be only one of the following:  
`call_metadata` |  `[CallMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.CallMetadata)` Call-specific metadata.  
Union field `expiration`. A time to live expiration setting, can be either a specified timestamp or a duration from the time that the conversation creation request was received. Conversations with an expiration set will be removed up to 24 hours after the specified time. `expiration` can be only one of the following:  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted.  
`ttl` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time.  
  
## CallMetadata

Call-specific metadata.

Fields  
---  
`customer_channel` |  `int32` The audio channel that contains the customer.  
`agent_channel` |  `int32` The audio channel that contains the agent.  
  
## Medium

Possible media for the conversation.

Enums  
---  
`MEDIUM_UNSPECIFIED` | Default value, if unspecified will default to PHONE_CALL.  
`PHONE_CALL` | The format for conversations that took place over the phone.  
`CHAT` | The format for conversations that took place over chat.  
  
## QualityMetadata

Conversation metadata related to quality management.

Fields  
---  
`customer_satisfaction_rating` |  `int32` An arbitrary integer value indicating the customer's satisfaction rating.  
`wait_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The amount of time the customer waited to connect with an agent.  
`menu_path` |  `string` An arbitrary string value specifying the menu path the customer took.  
`agent_info[]` |  `[AgentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.QualityMetadata.AgentInfo)` Information about agents involved in the call.  
  
## AgentInfo

Information about an agent involved in the conversation.

Fields  
---  
`agent_id` |  `string` A user-specified string representing the agent.  
`display_name` |  `string` The agent's name.  
`team  
**(deprecated)**` |  `string` This item is deprecated!A user-specified string representing the agent's team. Deprecated in favor of the `teams` field.  
`teams[]` |  `string` User-specified strings representing the agent's teams.  
`disposition_code` |  `string` A user-provided string indicating the outcome of the agent's segment of the call.  
`agent_type` |  `[Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationParticipant.Role)` The agent type, e.g. HUMAN_AGENT.  
`location` |  `string` The agent's location.  
  
## Transcript

A message representing the transcript of a conversation.

Fields  
---  
`transcript_segments[]` |  `[TranscriptSegment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript.TranscriptSegment)` A list of sequential transcript segments that comprise the conversation.  
  
## TranscriptSegment

A segment of a full transcript.

Fields  
---  
`message_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time that the message occurred, if provided.  
`text` |  `string` The text of this segment.  
`confidence` |  `float` A confidence estimate between 0.0 and 1.0 of the fidelity of this segment. A default value of 0.0 indicates that the value is unset.  
`words[]` |  `[WordInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript.TranscriptSegment.WordInfo)` A list of the word-specific information for each word in the segment.  
`language_code` |  `string` The language code of this segment as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".  
`channel_tag` |  `int32` For conversations derived from multi-channel audio, this is the channel number corresponding to the audio from that channel. For audioChannelCount = N, its output values can range from '1' to 'N'. A channel tag of 0 indicates that the audio is mono.  
`segment_participant` |  `[ConversationParticipant](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationParticipant)` The participant of this segment.  
`dialogflow_segment_metadata` |  `[DialogflowSegmentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata)` CCAI metadata relating to the current transcript segment.  
`sentiment` |  `[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SentimentData)` The sentiment for this transcript segment.  
  
## DialogflowSegmentMetadata

Metadata from Dialogflow relating to the current transcript segment.

Fields  
---  
`smart_reply_allowlist_covered` |  `bool` Whether the transcript segment was covered under the configured smart reply allowlist in Agent Assist.  
  
## WordInfo

Word-level info for words in a transcript.

Fields  
---  
`start_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Time offset of the start of this word relative to the beginning of the total conversation.  
`end_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Time offset of the end of this word relative to the beginning of the total conversation.  
`word` |  `string` The word itself. Includes punctuation marks that surround the word.  
`confidence` |  `float` A confidence estimate between 0.0 and 1.0 of the fidelity of this word. A default value of 0.0 indicates that the value is unset.  
  
## ConversationDataSource

The conversation source, which is a combination of transcript and audio.

Fields  
---  
`metadata_uri` |  `string` Cloud Storage URI that points to a file that contains the conversation metadata.  
Union field `source`. The source of the conversation. `source` can be only one of the following:  
`gcs_source` |  `[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.GcsSource)` A Cloud Storage location specification for the audio and transcript.  
`dialogflow_source` |  `[DialogflowSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DialogflowSource)` The source when the conversation comes from Dialogflow.  
  
## ConversationLevelSentiment

One channel of conversation-level sentiment data.

Fields  
---  
`channel_tag` |  `int32` The channel of the audio that the data applies to.  
`sentiment_data` |  `[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SentimentData)` Data specifying sentiment.  
  
## ConversationLevelSilence

Conversation-level silence data.

Fields  
---  
`silence_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Amount of time calculated to be in silence.  
`silence_percentage` |  `float` Percentage of the total conversation spent in silence.  
  
## ConversationParticipant

The call participant speaking for a given utterance.

Fields  
---  
`dialogflow_participant  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. Use `dialogflow_participant_name` instead. The name of the Dialogflow participant. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant}  
`obfuscated_external_user_id` |  `string` Obfuscated user ID from Dialogflow.  
`role` |  `[Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationParticipant.Role)` The role of the participant.  
Union field `participant`.`participant` can be only one of the following:  
`dialogflow_participant_name` |  `string` The name of the participant provided by Dialogflow. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant}  
`user_id` |  `string` A user-specified ID representing the participant.  
  
## Role

The role of the participant.

Enums  
---  
`ROLE_UNSPECIFIED` | Participant's role is not set.  
`HUMAN_AGENT` | Participant is a human agent.  
`AUTOMATED_AGENT` | Participant is an automated agent.  
`END_USER` | Participant is an end user who conversed with the contact center.  
`ANY_AGENT` | Participant is either a human or automated agent.  
  
## ConversationSummarizationSuggestionData

Conversation summarization suggestion data.

Fields  
---  
`text` |  `string` The summarization content that is concatenated into one string.  
`text_sections` |  `map<string, string>` The summarization content that is divided into sections. The key is the section's name and the value is the section's content. There is no specific format for the key or value.  
`confidence` |  `float` The confidence score of the summarization.  
`metadata` |  `map<string, string>` A map that contains metadata about the summarization and the document from which it originates.  
`answer_record` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record}  
`conversation_model` |  `string` The name of the model that generates this summary. Format: projects/{project}/locations/{location}/conversationModels/{conversation_model}  
`generator_id` |  `string` Agent Assist generator ID.  
  
## ConversationView

Represents the options for viewing a conversation.

Enums  
---  
`CONVERSATION_VIEW_UNSPECIFIED` | The conversation view is not specified.

  * Defaults to `FULL` in `GetConversationRequest`.
  * Defaults to `BASIC` in `ListConversationsRequest`.

  
`FULL` | Populates all fields in the conversation.  
`BASIC` | Populates all fields in the conversation except the transcript.  
  
## CreateAnalysisOperationMetadata

Metadata for a create analysis operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`conversation` |  `string` Output only. The Conversation that this Analysis Operation belongs to.  
`annotator_selector` |  `[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector)` Output only. The annotator selector used for the analysis (if any).  
  
## CreateAnalysisRequest

The request to create an analysis.

Fields  
---  
`parent` |  `string` Required. The parent resource of the analysis.  
`analysis` |  `[Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Analysis)` Required. The analysis to create.  
  
## CreateAnalysisRuleRequest

The request to create a analysis rule. analysis_rule_id will be generated by the server.

Fields  
---  
`parent` |  `string` Required. The parent resource of the analysis rule. Required. The location to create a analysis rule for. Format: `projects/<Project ID>/locations/<Location ID>` or `projects/<Project Number>/locations/<Location ID>`  
`analysis_rule` |  `[AnalysisRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisRule)` Required. The analysis rule resource to create.  
  
## CreateAssessmentRequest

The request to create an assessment.

Fields  
---  
`parent` |  `string` Required. The parent resource of the assessment.  
`assessment` |  `[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)` Required. The assessment to create.  
  
## CreateAssessmentRuleRequest

The request to create an assessment rule.

Fields  
---  
`parent` |  `string` Required. The parent resource of the assessment rule. Required. The location to create a assessment rule for. Format: `projects/<Project ID>/locations/<Location ID>` or `projects/<Project Number>/locations/<Location ID>`  
`assessment_rule` |  `[AssessmentRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AssessmentRule)` Required. The assessment rule resource to create.  
`assessment_rule_id` |  `string` Optional. A unique ID for the new AssessmentRule. This ID will become the final component of the AssessmentRule's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.  
  
## CreateAuthorizedViewRequest

The request for creating a AuthorizedView.

Fields  
---  
`parent` |  `string` Required. The parent resource of the AuthorizedView.  
`authorized_view` |  `[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)` Required. The AuthorizedView to create.  
`authorized_view_id` |  `string` Optional. A unique ID for the new AuthorizedView. This ID will become the final component of the AuthorizedView's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. See aip.dev/122#resource-id-segments  
  
## CreateAuthorizedViewSetRequest

The request for creating a AuthorizedViewSet.

Fields  
---  
`parent` |  `string` Required. The parent resource of the AuthorizedViewSet.  
`authorized_view_set` |  `[AuthorizedViewSet](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedViewSet)` Required. The AuthorizedViewSet to create.  
`authorized_view_set_id` |  `string` Optional. A unique ID for the new AuthorizedViewSet. This ID will become the final component of the AuthorizedViewSet's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. See aip.dev/122#resource-id-segments  
  
## CreateConversationRequest

Request to create a conversation.

Fields  
---  
`parent` |  `string` Required. The parent resource of the conversation.  
`conversation` |  `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)` Required. The conversation resource to create.  
`conversation_id` |  `string` A unique ID for the new conversation. This ID will become the final component of the conversation's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `[a-z][0-9]-`  
  
## CreateFeedbackLabelRequest

The request for creating a feedback label.

Fields  
---  
`parent` |  `string` Required. The parent resource of the feedback label.  
`feedback_label_id` |  `string` Optional. The ID of the feedback label to create. If one is not specified it will be generated by the server.  
`feedback_label` |  `[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)` Required. The feedback label to create.  
  
## CreateIssueMetadata

Metadata for creating an issue.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[CreateIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueRequest)` The original request for creation.  
  
## CreateIssueModelMetadata

Metadata for creating an issue model.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[CreateIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.CreateIssueModelRequest)` The original request for creation.  
  
## CreateIssueModelRequest

The request to create an issue model.

Fields  
---  
`parent` |  `string` Required. The parent resource of the issue model.  
`issue_model` |  `[IssueModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel)` Required. The issue model to create.  
  
## CreateIssueRequest

The request to create an issue.

Fields  
---  
`parent` |  `string` Required. The parent resource of the issue.  
`issue` |  `[Issue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Issue)` Required. The values for the new issue.  
  
## CreateNoteRequest

The message to create a note.

Fields  
---  
`parent` |  `string` Required. The parent resource of the note.  
`note` |  `[Note](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note)` Required. The note resource to create.  
  
## CreatePhraseMatcherRequest

Request to create a phrase matcher.

Fields  
---  
`parent` |  `string` Required. The parent resource of the phrase matcher. Required. The location to create a phrase matcher for. Format: `projects/<Project ID>/locations/<Location ID>` or `projects/<Project Number>/locations/<Location ID>`  
`phrase_matcher` |  `[PhraseMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher)` Required. The phrase matcher resource to create.  
  
## CreateQaQuestionRequest

The request for creating a QaQuestion.

Fields  
---  
`parent` |  `string` Required. The parent resource of the QaQuestion.  
`qa_question` |  `[QaQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion)` Required. The QaQuestion to create.  
`qa_question_id` |  `string` Optional. A unique ID for the new question. This ID will become the final component of the question's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `[a-z][0-9]-`.  
  
## CreateQaQuestionTagRequest

The request for creating a QaQuestionTag.

Fields  
---  
`parent` |  `string` Required. The parent resource of the QaQuestionTag.  
`qa_question_tag` |  `[QaQuestionTag](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestionTag)` Required. The QaQuestionTag to create.  
`qa_question_tag_id` |  `string` Optional. A unique ID for the new QaQuestionTag. This ID will become the final component of the QaQuestionTag's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `[a-z][0-9]-`.  
  
## CreateQaScorecardRequest

The request for creating a QaScorecard.

Fields  
---  
`parent` |  `string` Required. The parent resource of the QaScorecard.  
`qa_scorecard` |  `[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)` Required. The QaScorecard to create.  
`qa_scorecard_id` |  `string` Optional. A unique ID for the new QaScorecard. This ID will become the final component of the QaScorecard's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `[a-z][0-9]-`.  
  
## CreateQaScorecardRevisionRequest

The request for creating a QaScorecardRevision.

Fields  
---  
`parent` |  `string` Required. The parent resource of the QaScorecardRevision.  
`qa_scorecard_revision` |  `[QaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision)` Required. The QaScorecardRevision to create.  
`qa_scorecard_revision_id` |  `string` Optional. A unique ID for the new QaScorecardRevision. This ID will become the final component of the QaScorecardRevision's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `[a-z][0-9]-`.  
  
## CreateViewRequest

The request to create a view.

Fields  
---  
`parent` |  `string` Required. The parent resource of the view. Required. The location to create a view for. Format: `projects/<Project ID>/locations/<Location ID>` or `projects/<Project Number>/locations/<Location ID>`  
`view` |  `[View](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.View)` Required. The view resource to create.  
  
## Dataset

Dataset resource represents a collection of conversations that may be bounded (Static Dataset, e.g. golden dataset for training), or unbounded (Dynamic Dataset, e.g. live traffic, or agent training traffic)

Fields  
---  
`name` |  `string` Immutable. Identifier. Resource name of the dataset. Format: projects/{project}/locations/{location}/datasets/{dataset}  
`display_name` |  `string` Display name for the dataaset  
`description` |  `string` Dataset description.  
`type` |  `[Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dataset.Type)` Dataset usage type.  
`ttl` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Option TTL for the dataset.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Dataset create time.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Dataset update time.  
  
## Type

Type of datasat: For evals or sampled from live traffic.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value for unspecified.  
`EVAL` | For evals only.  
`LIVE` | Dataset with new conversations coming in regularly (Insights legacy conversations and AI trainer)  
  
## DatasetValidationWarning

Enum for the different types of issues a tuning dataset can have. These warnings are currentlyraised when trying to validate a dataset for tuning a scorecard.

Enums  
---  
`DATASET_VALIDATION_WARNING_UNSPECIFIED` | Unspecified data validation warning.  
`TOO_MANY_INVALID_FEEDBACK_LABELS` | A non-trivial percentage of the feedback labels are invalid.  
`INSUFFICIENT_FEEDBACK_LABELS` | The quantity of valid feedback labels provided is less than the recommended minimum.  
`INSUFFICIENT_FEEDBACK_LABELS_PER_ANSWER` | One or more of the answers have less than the recommended minimum of feedback labels.  
`ALL_FEEDBACK_LABELS_HAVE_THE_SAME_ANSWER` | All the labels in the dataset come from a single answer choice.  
  
## DeleteAnalysisRequest

The request to delete an analysis.

Fields  
---  
`name` |  `string` Required. The name of the analysis to delete.  
  
## DeleteAnalysisRuleRequest

The request to delete a analysis rule.

Fields  
---  
`name` |  `string` Required. The name of the analysis rule to delete.  
  
## DeleteAssessmentRequest

The request to delete an assessment.

Fields  
---  
`name` |  `string` Required. The name of the assessment to delete.  
`force` |  `bool` Optional. If set to true, all of this assessment's notes will also be deleted. Otherwise, the request will only succeed if it has no notes.  
  
## DeleteAssessmentRuleRequest

The request to delete an assessment rule.

Fields  
---  
`name` |  `string` Required. The name of the assessment rule to delete.  
  
## DeleteAuthorizedViewRequest

The request for deleting an authorized view.

Fields  
---  
`name` |  `string` Required. The name of the AuthorizedView to delete.  
  
## DeleteAuthorizedViewSetRequest

The request for deleting a AuthorizedViewSet.

Fields  
---  
`name` |  `string` Required. The name of the AuthorizedViewSet to delete.  
`force` |  `bool` Optional. If set to true, all of this AuthorizedViewSet's child resources will also be deleted. Otherwise, the request will only succeed if it has none.  
  
## DeleteConversationRequest

The request to delete a conversation.

Fields  
---  
`name` |  `string` Required. The name of the conversation to delete.  
`force` |  `bool` If set to true, all of this conversation's analyses will also be deleted. Otherwise, the request will only succeed if the conversation has no analyses.  
  
## DeleteFeedbackLabelRequest

The request for deleting a feedback label.

Fields  
---  
`name` |  `string` Required. The name of the feedback label to delete.  
  
## DeleteIssueModelMetadata

Metadata for deleting an issue model.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[DeleteIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteIssueModelRequest)` The original request for deletion.  
  
## DeleteIssueModelRequest

The request to delete an issue model.

Fields  
---  
`name` |  `string` Required. The name of the issue model to delete.  
  
## DeleteIssueRequest

The request to delete an issue.

Fields  
---  
`name` |  `string` Required. The name of the issue to delete.  
  
## DeleteNoteRequest

The request to delete a note.

Fields  
---  
`name` |  `string` Required. The name of the note to delete.  
  
## DeletePhraseMatcherRequest

The request to delete a phrase matcher.

Fields  
---  
`name` |  `string` Required. The name of the phrase matcher to delete.  
  
## DeleteQaQuestionRequest

The request for deleting a QaQuestion.

Fields  
---  
`name` |  `string` Required. The name of the QaQuestion to delete.  
  
## DeleteQaQuestionTagMetadata

The metadata for deleting a QaQuestionTag Resource.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[DeleteQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeleteQaQuestionTagRequest)` Output only. The original request.  
  
## DeleteQaQuestionTagRequest

The request for deleting a QaQuestionTag.

Fields  
---  
`name` |  `string` Required. The name of the QaQuestionTag to delete.  
  
## DeleteQaScorecardRequest

The request for deleting a QaScorecard.

Fields  
---  
`name` |  `string` Required. The name of the QaScorecard to delete.  
`force` |  `bool` Optional. If set to true, all of this QaScorecard's child resources will also be deleted. Otherwise, the request will only succeed if it has none.  
  
## DeleteQaScorecardRevisionRequest

The request to delete a QaScorecardRevision.

Fields  
---  
`name` |  `string` Required. The name of the QaScorecardRevision to delete.  
`force` |  `bool` Optional. If set to true, all of this QaScorecardRevision's child resources will also be deleted. Otherwise, the request will only succeed if it has none.  
  
## DeleteViewRequest

The request to delete a view.

Fields  
---  
`name` |  `string` Required. The name of the view to delete.  
  
## DeployIssueModelMetadata

Metadata for deploying an issue model.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[DeployIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DeployIssueModelRequest)` The original request for deployment.  
  
## DeployIssueModelRequest

The request to deploy an issue model.

Fields  
---  
`name` |  `string` Required. The issue model to deploy.  
  
## DeployIssueModelResponse

This type has no fields.

The response to deploy an issue model.

## DeployQaScorecardRevisionRequest

The request to deploy a QaScorecardRevision

Fields  
---  
`name` |  `string` Required. The name of the QaScorecardRevision to deploy.  
  
## DialogflowIntent

The data for a Dialogflow intent. Represents a detected intent in the conversation, e.g. MAKES_PROMISE.

Fields  
---  
`display_name` |  `string` The human-readable name of the intent.  
  
## DialogflowInteractionData

Dialogflow interaction data.

Fields  
---  
`dialogflow_intent_id` |  `string` The Dialogflow intent resource path. Format: projects/{project}/agent/{agent}/intents/{intent}  
`confidence` |  `float` The confidence of the match ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
  
## DialogflowSource

A Dialogflow source of conversation data.

Fields  
---  
`dialogflow_conversation` |  `string` Output only. The name of the Dialogflow conversation that this conversation resource is derived from. Format: projects/{project}/locations/{location}/conversations/{conversation}  
`audio_uri` |  `string` Cloud Storage URI that points to a file that contains the conversation audio.  
  
## Dimension

A dimension determines the grouping key for the query. In SQL terms, these would be part of both the "SELECT" and "GROUP BY" clauses.

Fields  
---  
`dimension_key` |  `[DimensionKey](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.DimensionKey)` The key of the dimension.  
Union field `dimension_metadata`. Output-only metadata about the dimension. `dimension_metadata` can be only one of the following:  
`issue_dimension_metadata` |  `[IssueDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.IssueDimensionMetadata)` Output only. Metadata about the issue dimension.  
`agent_dimension_metadata` |  `[AgentDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.AgentDimensionMetadata)` Output only. Metadata about the agent dimension.  
`qa_question_dimension_metadata` |  `[QaQuestionDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.QaQuestionDimensionMetadata)` Output only. Metadata about the QA question dimension.  
`qa_question_answer_dimension_metadata` |  `[QaQuestionAnswerDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension.QaQuestionAnswerDimensionMetadata)` Output only. Metadata about the QA question-answer dimension.  
  
## AgentDimensionMetadata

Metadata about the agent dimension.

Fields  
---  
`agent_id` |  `string` Optional. A user-specified string representing the agent.  
`agent_display_name` |  `string` Optional. The agent's name  
`agent_team` |  `string` Optional. A user-specified string representing the agent's team.  
  
## DimensionKey

The key of the dimension.

Enums  
---  
`DIMENSION_KEY_UNSPECIFIED` | The key of the dimension is unspecified.  
`ISSUE` | The dimension is keyed by issues.  
`ISSUE_NAME` | The dimension is keyed by issue names.  
`AGENT` | The dimension is keyed by agents.  
`AGENT_TEAM` | The dimension is keyed by agent teams.  
`QA_QUESTION_ID` | The dimension is keyed by QaQuestionIds. Note that: We only group by the QuestionId and not the revision-id of the scorecard this question is a part of. This allows for showing stats for the same question across different scorecard revisions.  
`QA_QUESTION_ANSWER_VALUE` | The dimension is keyed by QaQuestionIds-Answer value pairs. Note that: We only group by the QuestionId and not the revision-id of the scorecard this question is a part of. This allows for showing distribution of answers per question across different scorecard revisions.  
`CONVERSATION_PROFILE_ID` | The dimension is keyed by the conversation profile ID.  
`MEDIUM` | The dimension is keyed by the conversation medium.  
  
## IssueDimensionMetadata

Metadata about the issue dimension.

Fields  
---  
`issue_id` |  `string` The issue ID.  
`issue_display_name` |  `string` The issue display name.  
`issue_model_id` |  `string` The parent issue model ID.  
  
## QaQuestionAnswerDimensionMetadata

Metadata about the QA question-answer dimension. This is useful for showing the answer distribution for questions for a given scorecard.

Fields  
---  
`qa_scorecard_id` |  `string` Optional. The QA scorecard ID.  
`qa_question_id` |  `string` Optional. The QA question ID.  
`question_body` |  `string` Optional. The full body of the question.  
`answer_value` |  `string` Optional. The full body of the question.  
  
## QaQuestionDimensionMetadata

Metadata about the QA question dimension.

Fields  
---  
`qa_scorecard_id` |  `string` Optional. The QA scorecard ID.  
`qa_question_id` |  `string` Optional. The QA question ID.  
`question_body` |  `string` Optional. The full body of the question.  
  
## EncryptionSpec

A customer-managed encryption key specification that can be applied to all created resources (e.g. `Conversation`).

Fields  
---  
`name` |  `string` Immutable. The resource name of the encryption key specification resource. Format: projects/{project}/locations/{location}/encryptionSpec  
`kms_key` |  `string` Required. The name of customer-managed encryption key that is used to secure a resource and its sub-resources. If empty, the resource is secured by our default encryption key. Only the key in the same location as this resource is allowed to be used for encryption. Format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{key}`  
  
## Entity

The data for an entity annotation. Represents a phrase in the conversation that is a known entity, such as a person, an organization, or location.

Fields  
---  
`display_name` |  `string` The representative name for the entity.  
`type` |  `[Type](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Entity.Type)` The entity type.  
`metadata` |  `map<string, string>` Metadata associated with the entity.For most entity types, the metadata is a Wikipedia URL (`wikipedia_url`) and Knowledge Graph MID (`mid`), if they are available. For the metadata associated with other entity types, see the Type table below.  
`salience` |  `float` The salience score associated with the entity in the [0, 1.0] range.The salience score for an entity provides information about the importance or centrality of that entity to the entire document text. Scores closer to 0 are less salient, while scores closer to 1.0 are highly salient.  
`sentiment` |  `[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SentimentData)` The aggregate sentiment expressed for this entity in the conversation.  
  
## Type

The type of the entity. For most entity types, the associated metadata is a Wikipedia URL (`wikipedia_url`) and Knowledge Graph MID (`mid`). The table below lists the associated fields for entities that have different metadata.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified.  
`PERSON` | Person.  
`LOCATION` | Location.  
`ORGANIZATION` | Organization.  
`EVENT` | Event.  
`WORK_OF_ART` | Artwork.  
`CONSUMER_GOOD` | Consumer product.  
`OTHER` | Other types of entities.  
`PHONE_NUMBER` | Phone number.The metadata lists the phone number (formatted according to local convention), plus whichever additional elements appear in the text:

  * `number` \- The actual number, broken down into sections according to local convention.
  * `national_prefix` \- Country code, if detected.
  * `area_code` \- Region or area code, if detected.
  * `extension` \- Phone extension (to be dialed after connection), if detected.

  
`ADDRESS` | Address.The metadata identifies the street number and locality plus whichever additional elements appear in the text:

  * `street_number` \- Street number.
  * `locality` \- City or town.
  * `street_name` \- Street/route name, if detected.
  * `postal_code` \- Postal code, if detected.
  * `country` \- Country, if detected.
  * `broad_region` \- Administrative area, such as the state, if detected.
  * `narrow_region` \- Smaller administrative area, such as county, if detected.
  * `sublocality` \- Used in Asian addresses to demark a district within a city, if detected.

  
`DATE` | Date.The metadata identifies the components of the date:

  * `year` \- Four digit year, if detected.
  * `month` \- Two digit month number, if detected.
  * `day` \- Two digit day number, if detected.

  
`NUMBER` | Number.The metadata is the number itself.  
`PRICE` | Price.The metadata identifies the `value` and `currency`.  
  
## EntityMentionData

The data for an entity mention annotation. This represents a mention of an `Entity` in the conversation.

Fields  
---  
`entity_unique_id` |  `string` The key of this entity in conversation entities. Can be used to retrieve the exact `Entity` this mention is attached to.  
`type` |  `[MentionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.EntityMentionData.MentionType)` The type of the entity mention.  
`sentiment` |  `[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SentimentData)` Sentiment expressed for this mention of the entity.  
  
## MentionType

The supported types of mentions.

Enums  
---  
`MENTION_TYPE_UNSPECIFIED` | Unspecified.  
`PROPER` | Proper noun.  
`COMMON` | Common noun (or noun compound).  
  
## ExactMatchConfig

Exact match configuration.

Fields  
---  
`case_sensitive` |  `bool` Whether to consider case sensitivity when performing an exact match.  
  
## ExportInsightsDataMetadata

Metadata for an export insights operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[ExportInsightsDataRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest)` The original request for export.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Partial errors during export operation that might cause the operation output to be incomplete.  
`completed_export_count` |  `int32` The number of conversations that were exported successfully.  
`failed_export_count` |  `int32` The number of conversations that failed to be exported.  
  
## ExportInsightsDataRequest

The request to export insights.

Fields  
---  
`parent` |  `string` Required. The parent resource to export data from.  
`filter` |  `string` A filter to reduce results to a specific subset. Useful for exporting conversations with specific properties.  
`kms_key` |  `string` A fully qualified KMS key name for BigQuery tables protected by CMEK. Format: projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}/cryptoKeyVersions/{version}  
`write_disposition` |  `[WriteDisposition](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest.WriteDisposition)` Options for what to do if the destination table already exists.  
`export_schema_version` |  `[ExportSchemaVersion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest.ExportSchemaVersion)` Optional. Version of the export schema.  
Union field `destination`. Exporter destination. `destination` can be only one of the following:  
`big_query_destination` |  `[BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportInsightsDataRequest.BigQueryDestination)` Specified if sink is a BigQuery table.  
  
## BigQueryDestination

A BigQuery Table Reference.

Fields  
---  
`project_id` |  `string` A project ID or number. If specified, then export will attempt to write data to this project instead of the resource project. Otherwise, the resource project will be used.  
`dataset` |  `string` Required. The name of the BigQuery dataset that the snapshot result should be exported to. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.  
`table` |  `string` The BigQuery table name to which the insights data should be written. If this table does not exist, the export call returns an INVALID_ARGUMENT error.  
  
## ExportSchemaVersion

Version of the export schema, default to version 3 if not specified.

Enums  
---  
`EXPORT_SCHEMA_VERSION_UNSPECIFIED` | Unspecified. Defaults to EXPORT_V3.  
`EXPORT_V1` | Export schema version 1.  
`EXPORT_V2` | Export schema version 2.  
`EXPORT_V3` | Export schema version 3.  
`EXPORT_V4` | Export schema version 4.  
`EXPORT_V5` | Export schema version 5.  
`EXPORT_V6` | Export schema version 6.  
`EXPORT_V7` | Export schema version 7.  
`EXPORT_VERSION_LATEST_AVAILABLE` | Export schema version latest available.  
  
## WriteDisposition

Specifies the action that occurs if the destination table already exists.

Enums  
---  
`WRITE_DISPOSITION_UNSPECIFIED` | Write disposition is not specified. Defaults to WRITE_TRUNCATE.  
`WRITE_TRUNCATE` | If the table already exists, BigQuery will overwrite the table data and use the schema from the load.  
`WRITE_APPEND` | If the table already exists, BigQuery will append data to the table.  
  
## ExportInsightsDataResponse

This type has no fields.

Response for an export insights operation.

## ExportIssueModelMetadata

Metadata used for export issue model.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation finished running.  
`request` |  `[ExportIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportIssueModelRequest)` The original export request.  
  
## ExportIssueModelRequest

Request to export an issue model.

Fields  
---  
`name` |  `string` Required. The issue model to export.  
Union field `Destination`.`Destination` can be only one of the following:  
`gcs_destination` |  `[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExportIssueModelRequest.GcsDestination)` Google Cloud Storage URI to export the issue model to.  
  
## GcsDestination

Google Cloud Storage Object URI to save the issue model to.

Fields  
---  
`object_uri` |  `string` Required. Format: `gs://<bucket-name>/<object-name>`  
  
## ExportIssueModelResponse

This type has no fields.

Response from export issue model

## FaqAnswerData

Agent Assist frequently-asked-question answer data.

Fields  
---  
`answer` |  `string` The piece of text from the `source` knowledge base document.  
`confidence_score` |  `float` The system's confidence score that this answer is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`question` |  `string` The corresponding FAQ question.  
`metadata` |  `map<string, string>` Map that contains metadata about the FAQ answer and the document that it originates from.  
`query_record` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record}  
`source` |  `string` The knowledge document that this answer was extracted from. Format: projects/{project}/knowledgeBases/{knowledge_base}/documents/{document}.  
  
## FeedbackLabel

Represents a conversation, resource, and label provided by the user. Can take the form of a string label or a QaAnswer label. QaAnswer labels are used for Quality AI example conversations. String labels are used for Topic Modeling. AgentAssistSummary labels are used for Agent Assist Summarization.

Fields  
---  
`name` |  `string` Immutable. Resource name of the FeedbackLabel. Format: projects/{project}/locations/{location}/conversations/{conversation}/feedbackLabels/{feedback_label}  
`labeled_resource` |  `string` Name of the resource to be labeled. Supported resources are:

  * `projects/{project}/locations/{location}/qaScorecards/{scorecard}/revisions/{revision}/qaQuestions/{question}`
  * `projects/{project}/locations/{location}/issueModels/{issue_model}`
  * `projects/{project}/locations/{location}/generators/{generator_id}`

  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create time of the label.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Update time of the label.  
Union field `label_type`. Label type. `label_type` can be only one of the following:  
`label` |  `string` String label used for Topic Modeling.  
`qa_answer_label` |  `[AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerValue)` QaAnswer label used for Quality AI example conversations.  
  
## FinalizeAssessmentRequest

The message to finalize an assessment. Finalizing makes an assessment and its notes immutable.

Fields  
---  
`name` |  `string` Required. The name of the assessment to finalize.  
  
## GcsSource

A Cloud Storage source of conversation data.

Fields  
---  
`audio_uri` |  `string` Cloud Storage URI that points to a file that contains the conversation audio.  
`transcript_uri` |  `string` Immutable. Cloud Storage URI that points to a file that contains the conversation transcript.  
  
## GetAnalysisRequest

The request to get an analysis.

Fields  
---  
`name` |  `string` Required. The name of the analysis to get.  
  
## GetAnalysisRuleRequest

The request for getting a analysis rule.

Fields  
---  
`name` |  `string` Required. The name of the AnalysisRule to get.  
  
## GetAssessmentRequest

The request to get an assessment.

Fields  
---  
`name` |  `string` Required. The name of the assessment to get.  
  
## GetAssessmentRuleRequest

The request for getting an assessment rule.

Fields  
---  
`name` |  `string` Required. The name of the assessment rule to get.  
  
## GetAuthorizedViewRequest

The request for getting a AuthorizedView.

Fields  
---  
`name` |  `string` Required. The name of the AuthorizedView to get.  
  
## GetAuthorizedViewSetRequest

The request for getting a AuthorizedViewSet.

Fields  
---  
`name` |  `string` Required. The name of the AuthorizedViewSet to get.  
  
## GetConversationRequest

The request to get a conversation.

Fields  
---  
`name` |  `string` Required. The name of the conversation to get.  
`view` |  `[ConversationView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationView)` The level of details of the conversation. Default is `FULL`.  
  
## GetEncryptionSpecRequest

The request to get location-level encryption specification.

Fields  
---  
`name` |  `string` Required. The name of the encryption spec resource to get.  
  
## GetFeedbackLabelRequest

The request for getting a feedback label.

Fields  
---  
`name` |  `string` Required. The name of the feedback label to get.  
  
## GetIssueModelRequest

The request to get an issue model.

Fields  
---  
`name` |  `string` Required. The name of the issue model to get.  
  
## GetIssueRequest

The request to get an issue.

Fields  
---  
`name` |  `string` Required. The name of the issue to get.  
  
## GetPhraseMatcherRequest

The request to get a a phrase matcher.

Fields  
---  
`name` |  `string` Required. The name of the phrase matcher to get.  
  
## GetQaQuestionRequest

The request for a QaQuestion.

Fields  
---  
`name` |  `string` Required. The name of the QaQuestion to get.  
  
## GetQaQuestionTagRequest

The request for a QaQuestionTag.

Fields  
---  
`name` |  `string` Required. The name of the QaQuestionTag to get.  
  
## GetQaScorecardRequest

The request for a QaScorecard. By default, returns the latest revision.

Fields  
---  
`name` |  `string` Required. The name of the QaScorecard to get.  
  
## GetQaScorecardRevisionRequest

The request for a QaScorecardRevision.

Fields  
---  
`name` |  `string` Required. The name of the QaScorecardRevision to get.  
  
## GetSettingsRequest

The request to get project-level settings.

Fields  
---  
`name` |  `string` Required. The name of the settings resource to get.  
  
## GetViewRequest

The request to get a view.

Fields  
---  
`name` |  `string` Required. The name of the view to get.  
  
## HoldData

This type has no fields.

The data for a hold annotation.

## ImportIssueModelMetadata

Metadata used for import issue model.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation finished running.  
`request` |  `[ImportIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ImportIssueModelRequest)` The original import request.  
  
## ImportIssueModelRequest

Request to import an issue model.

Fields  
---  
`parent` |  `string` Required. The parent resource of the issue model.  
`create_new_model` |  `bool` Optional. If set to true, will create an issue model from the imported file with randomly generated IDs for the issue model and corresponding issues. Otherwise, replaces an existing model with the same ID as the file.  
Union field `Source`.`Source` can be only one of the following:  
`gcs_source` |  `[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ImportIssueModelRequest.GcsSource)` Google Cloud Storage source message.  
  
## GcsSource

Google Cloud Storage Object URI to get the issue model file from.

Fields  
---  
`object_uri` |  `string` Required. Format: `gs://<bucket-name>/<object-name>`  
  
## ImportIssueModelResponse

Response from import issue model

Fields  
---  
`issue_model` |  `[IssueModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel)` The issue model that was imported.  
  
## IngestConversationsMetadata

The metadata for an IngestConversations operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[IngestConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest)` Output only. The original request for ingest.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Output only. Partial errors during ingest operation that might cause the operation output to be incomplete.  
`ingest_conversations_stats` |  `[IngestConversationsStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsMetadata.IngestConversationsStats)` Output only. Statistics for IngestConversations operation.  
  
## IngestConversationsStats

Statistics for IngestConversations operation.

Fields  
---  
`processed_object_count` |  `int32` Output only. The number of objects processed during the ingest operation.  
`duplicates_skipped_count` |  `int32` Output only. The number of objects skipped because another conversation with the same transcript uri had already been ingested.  
`successful_ingest_count` |  `int32` Output only. The number of new conversations added during this ingest operation.  
`failed_ingest_count` |  `int32` Output only. The number of objects which were unable to be ingested due to errors. The errors are populated in the partial_errors field.  
  
## IngestConversationsRequest

The request to ingest conversations.

Fields  
---  
`parent` |  `string` Required. The parent resource for new conversations.  
`conversation_config` |  `[ConversationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.ConversationConfig)` Configuration that applies to all conversations.  
`redaction_config` |  `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RedactionConfig)` Optional. DLP settings for transcript redaction. Optional, will default to the config specified in Settings.  
`speech_config` |  `[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SpeechConfig)` Optional. Default Speech-to-Text configuration. Optional, will default to the config specified in Settings.  
Union field `source`. Configuration for an external data store containing objects that will be converted to conversations. `source` can be only one of the following:  
`gcs_source` |  `[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.GcsSource)` A cloud storage bucket source. Note that any previously ingested objects from the source will be skipped to avoid duplication.  
Union field `object_config`. Configuration for converting individual `source` objects to conversations. `object_config` can be only one of the following:  
`transcript_object_config` |  `[TranscriptObjectConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.TranscriptObjectConfig)` Configuration for when `source` contains conversation transcripts.  
`sample_size` |  `int32` Optional. If set, this fields indicates the number of objects to ingest from the Cloud Storage bucket. If empty, the entire bucket will be ingested. Unless they are first deleted, conversations produced through sampling won't be ingested by subsequent ingest requests.  
  
## ConversationConfig

Configuration that applies to all conversations.

Fields  
---  
`agent_id` |  `string` Optional. An opaque, user-specified string representing a human agent who handled all conversations in the import. Note that this will be overridden if per-conversation metadata is provided through the `metadata_bucket_uri`.  
`agent_channel` |  `int32` Optional. Indicates which of the channels, 1 or 2, contains the agent. Note that this must be set for conversations to be properly displayed and analyzed.  
`customer_channel` |  `int32` Optional. Indicates which of the channels, 1 or 2, contains the agent. Note that this must be set for conversations to be properly displayed and analyzed.  
  
## GcsSource

Configuration for Cloud Storage bucket sources.

Fields  
---  
`bucket_uri` |  `string` Optional. The Cloud Storage bucket containing source objects. Avoid passing this. Pass this through one of `transcript_bucket_uri` or `audio_bucket_uri`.  
`bucket_object_type` |  `[BucketObjectType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IngestConversationsRequest.GcsSource.BucketObjectType)` Optional. Specifies the type of the objects in `bucket_uri`. Avoid passing this. This is inferred from the `transcript_bucket_uri`, `audio_bucket_uri`.  
`custom_metadata_keys[]` |  `string` Optional. Custom keys to extract as conversation labels from metadata files in `metadata_bucket_uri`. Keys not included in this field will be ignored. Note that there is a limit of 100 labels per conversation.  
`transcript_bucket_uri` |  `string` Optional. The Cloud Storage path to the conversation transcripts. Note that: [1] Transcript files are expected to be in JSON format. [2] Transcript, audio, metadata files must be in separate buckets / folders. [3] A source file and its corresponding metadata file must share the same name to be properly ingested, E.g. `gs://bucket/audio/conversation1.mp3` and `gs://bucket/metadata/conversation1.json`.  
`audio_bucket_uri` |  `string` Optional. The Cloud Storage path to the conversation audio file. Note that: [1] Audio files will be transcribed if not already. [2] Audio files and transcript files must be in separate buckets / folders. [3] A source file and its corresponding audio file must share the same name to be properly ingested, E.g. `gs://bucket/transcript/conversation1.json` and `gs://bucket/audio/conversation1.mp3`.  
`metadata_bucket_uri` |  `string` Optional. The Cloud Storage path to the conversation metadata. Note that: [1] Metadata files are expected to be in JSON format. [2] Metadata and source files (transcripts or audio) must be in separate buckets / folders. [3] A source file and its corresponding metadata file must share the same name to be properly ingested, E.g. `gs://bucket/audio/conversation1.mp3` and `gs://bucket/metadata/conversation1.json`.  
  
## BucketObjectType

Enums  
---  
`BUCKET_OBJECT_TYPE_UNSPECIFIED` | The object type is unspecified and will default to `TRANSCRIPT`.  
`TRANSCRIPT` | The object is a transcript.  
`AUDIO` | The object is an audio file.  
  
## TranscriptObjectConfig

Configuration for processing transcript objects.

Fields  
---  
`medium` |  `[Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Medium)` Required. The medium transcript objects represent.  
  
## IngestConversationsResponse

This type has no fields.

The response to an IngestConversations operation.

## InitializeEncryptionSpecMetadata

Metadata for initializing a location-level encryption specification.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[InitializeEncryptionSpecRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.InitializeEncryptionSpecRequest)` Output only. The original request for initialization.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Partial errors during initializing operation that might cause the operation output to be incomplete.  
  
## InitializeEncryptionSpecRequest

The request to initialize a location-level encryption specification.

Fields  
---  
`encryption_spec` |  `[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.EncryptionSpec)` Required. The encryption spec used for CMEK encryption. It is required that the kms key is in the same region as the endpoint. The same key will be used for all provisioned resources, if encryption is available. If the `kms_key_name` field is left empty, no encryption will be enforced.  
  
## InitializeEncryptionSpecResponse

This type has no fields.

The response to initialize a location-level encryption specification.

## Intent

The data for an intent. Represents a detected intent in the conversation, for example MAKES_PROMISE.

Fields  
---  
`id` |  `string` The unique identifier of the intent.  
`display_name` |  `string` The human-readable name of the intent.  
  
## IntentMatchData

The data for an intent match. Represents an intent match for a text segment in the conversation. A text segment can be part of a sentence, a complete sentence, or an utterance with multiple sentences.

Fields  
---  
`intent_unique_id` |  `string` The id of the matched intent. Can be used to retrieve the corresponding intent information.  
  
## InterruptionData

This type has no fields.

The data for an interruption annotation.

## Issue

The issue resource.

Fields  
---  
`name` |  `string` Immutable. The resource name of the issue. Format: projects/{project}/locations/{location}/issueModels/{issue_model}/issues/{issue}  
`display_name` |  `string` The representative name for the issue.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this issue was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time that this issue was updated.  
`sample_utterances[]` |  `string` Output only. Resource names of the sample representative utterances that match to this issue.  
`display_description` |  `string` Representative description of the issue.  
  
## IssueAssignment

Information about the issue.

Fields  
---  
`issue` |  `string` Resource name of the assigned issue.  
`score` |  `double` Score indicating the likelihood of the issue assignment. currently bounded on [0,1].  
`display_name` |  `string` Immutable. Display name of the assigned issue. This field is set at time of analysis and immutable since then.  
  
## IssueMatchData

The data for an issue match annotation.

Fields  
---  
`issue_assignment` |  `[IssueAssignment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueAssignment)` Information about the issue's assignment.  
  
## IssueModel

The issue model resource.

Fields  
---  
`name` |  `string` Immutable. The resource name of the issue model. Format: projects/{project}/locations/{location}/issueModels/{issue_model}  
`display_name` |  `string` The representative name for the issue model.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this issue model was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the issue model was updated.  
`issue_count` |  `int64` Output only. Number of issues in this issue model.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel.State)` Output only. State of the model.  
`input_data_config` |  `[InputDataConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel.InputDataConfig)` Configs for the input data that used to create the issue model.  
`training_stats` |  `[IssueModelLabelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelLabelStats)` Output only. Immutable. The issue model's label statistics on its training data.  
`model_type` |  `[ModelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel.ModelType)` Type of the model.  
`language_code` |  `string` Language of the model.  
  
## InputDataConfig

Configs for the input data used to create the issue model.

Fields  
---  
`medium  
**(deprecated)**` |  `[Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation.Medium)` This item is deprecated!Medium of conversations used in training data. This field is being deprecated. To specify the medium to be used in training a new issue model, set the `medium` field on `filter`.  
`training_conversations_count` |  `int64` Output only. Number of conversations used in training. Output only.  
`filter` |  `string` A filter to reduce the conversations used for training the model to a specific subset. Refer to <https://cloud.google.com/gemini-enterprise-cx/insights/filtering> for details.  
  
## ModelType

Type of the model.

Enums  
---  
`MODEL_TYPE_UNSPECIFIED` | Unspecified model type.  
`TYPE_V1` | Type V1.  
`TYPE_V2` | Type V2.  
  
## State

State of the model.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`UNDEPLOYED` | Model is not deployed but is ready to deploy.  
`DEPLOYING` | Model is being deployed.  
`DEPLOYED` | Model is deployed and is ready to be used. A model can only be used in analysis if it's in this state.  
`UNDEPLOYING` | Model is being undeployed.  
`DELETING` | Model is being deleted.  
  
## IssueModelLabelStats

Aggregated statistics about an issue model.

Fields  
---  
`analyzed_conversations_count` |  `int64` Number of conversations the issue model has analyzed at this point in time.  
`unclassified_conversations_count` |  `int64` Number of analyzed conversations for which no issue was applicable at this point in time.  
`issue_stats` |  `map<string, `[IssueStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModelLabelStats.IssueStats)`>` Statistics on each issue. Key is the issue's resource name.  
  
## IssueStats

Aggregated statistics about an issue.

Fields  
---  
`issue` |  `string` Issue resource. Format: projects/{project}/locations/{location}/issueModels/{issue_model}/issues/{issue}  
`labeled_conversations_count` |  `int64` Number of conversations attached to the issue at this point in time.  
`display_name` |  `string` Display name of the issue.  
  
## IssueModelResult

Issue Modeling result on a conversation.

Fields  
---  
`issue_model` |  `string` Issue model that generates the result. Format: projects/{project}/locations/{location}/issueModels/{issue_model}  
`issues[]` |  `[IssueAssignment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueAssignment)` All the matched issues.  
  
## ListAllFeedbackLabelsRequest

The request for listing all feedback labels.

Fields  
---  
`parent` |  `string` Required. The parent resource of all feedback labels per project.  
`page_size` |  `int32` Optional. The maximum number of feedback labels to return in the response. A valid page size ranges from 0 to 100,000 inclusive. If the page size is zero or unspecified, a default page size of 100 will be chosen. Note that a call might return fewer results than the requested page size.  
`page_token` |  `string` Optional. The value returned by the last `ListAllFeedbackLabelsResponse`. This value indicates that this is a continuation of a prior `ListAllFeedbackLabels` call and that the system should return the next page of data.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset in the entire project. Supports disjunctions (OR) and conjunctions (AND).Supported fields:

  * `issue_model_id`
  * `qa_question_id`
  * `min_create_time`
  * `max_create_time`
  * `min_update_time`
  * `max_update_time`
  * `feedback_label_type`: QUALITY_AI, TOPIC_MODELING

  
  
## ListAllFeedbackLabelsResponse

The response for listing all feedback labels.

Fields  
---  
`feedback_labels[]` |  `[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)` The feedback labels that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListAnalysesRequest

The request to list analyses.

Fields  
---  
`parent` |  `string` Required. The parent resource of the analyses.  
`page_size` |  `int32` The maximum number of analyses to return in the response. If this value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` The value returned by the last `ListAnalysesResponse`; indicates that this is a continuation of a prior `ListAnalyses` call and the system should return the next page of data.  
`filter` |  `string` A filter to reduce results to a specific subset. Useful for querying conversations with specific properties.  
  
## ListAnalysesResponse

The response to list analyses.

Fields  
---  
`analyses[]` |  `[Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Analysis)` The analyses that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListAnalysisRulesRequest

The request to list analysis rules.

Fields  
---  
`parent` |  `string` Required. The parent resource of the analysis rules.  
`page_size` |  `int32` Optional. The maximum number of analysis rule to return in the response. If this value is zero, the service will select a default size. A call may return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListAnalysisRulesResponse`; indicates that this is a continuation of a prior `ListAnalysisRules` call and the system should return the next page of data.  
  
## ListAnalysisRulesResponse

The response of listing views.

Fields  
---  
`analysis_rules[]` |  `[AnalysisRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisRule)` The analysis_rule that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListAssessmentRulesRequest

The request to list assessment rules.

Fields  
---  
`parent` |  `string` Required. The parent resource of the assessment rules.  
`page_token` |  `string` Optional. The value returned by the last `ListAssessmentRulesResponse`; indicates that this is a continuation of a prior `ListAssessmentRules` call and the system should return the next page of data.  
`page_size` |  `int32` Optional. The maximum number of assessment rule to return in the response. If this value is zero, the service will select a default size. A call may return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
  
## ListAssessmentRulesResponse

The response of listing assessment rules.

Fields  
---  
`assessment_rules[]` |  `[AssessmentRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AssessmentRule)` The assessment rules that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListAssessmentsRequest

The request to list assessments.

Fields  
---  
`parent` |  `string` Required. The parent resource of the assessments. To list all assessments in a location, substitute the conversation ID with a '-' character.  
`page_token` |  `string` Optional. The value returned by the last `ListAssessmentRulesResponse`; indicates that this is a continuation of a prior `ListAssessmentRules` call and the system should return the next page of data.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset. Supported filters include:

  * `state` \- The state of the assessment
  * `agent_info.agent_id` \- The ID of the agent the assessment is for

  
`page_size` |  `int32` The maximum number of assessments to list. If zero, the service will select a default size. A call may return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
  
## ListAssessmentsResponse

The response of listing assessments.

Fields  
---  
`assessments[]` |  `[Assessment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Assessment)` The assessments that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListAuthorizedViewSetsRequest

The request for listing AuthorizedViewSets.

Fields  
---  
`parent` |  `string` Required. The parent resource of the AuthorizedViewSets.  
`page_size` |  `int32` Optional. The maximum number of view sets to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListAuthorizedViewSetsResponse`. This value indicates that this is a continuation of a prior `ListAuthorizedViewSets` call and that the system should return the next page of data.  
`filter` |  `string` Optional. The filter expression to filter authorized view sets listed in the response.  
`order_by` |  `string` Optional. The order by expression to order authorized view sets listed in the response.  
  
## ListAuthorizedViewSetsResponse

The response from a ListAuthorizedViewSet request.

Fields  
---  
`authorized_view_sets[]` |  `[AuthorizedViewSet](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedViewSet)` The AuthorizedViewSets under the parent.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListAuthorizedViewsRequest

The request for listing AuthorizedViews.

Fields  
---  
`parent` |  `string` Required. The parent resource of the AuthorizedViews. If the parent is set to `-`, all AuthorizedViews under the location will be returned.  
`page_size` |  `int32` Optional. The maximum number of view to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListAuthorizedViewsResponse`. This value indicates that this is a continuation of a prior `ListAuthorizedViews` call and that the system should return the next page of data.  
`filter` |  `string` Optional. The filter expression to filter authorized views listed in the response.  
`order_by` |  `string` Optional. The order by expression to order authorized views listed in the response.  
  
## ListAuthorizedViewsResponse

The response from a ListAuthorizedViews request.

Fields  
---  
`authorized_views[]` |  `[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)` The AuthorizedViews under the parent.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListConversationsRequest

Request to list conversations.

Fields  
---  
`parent` |  `string` Required. The parent resource of the conversation.  
`page_size` |  `int32` The maximum number of conversations to return in the response. A valid page size ranges from 0 to 100,000 inclusive. If the page size is zero or unspecified, a default page size of 100 will be chosen. Note that a call might return fewer results than the requested page size.  
`page_token` |  `string` The value returned by the last `ListConversationsResponse`. This value indicates that this is a continuation of a prior `ListConversations` call and that the system should return the next page of data.  
`filter` |  `string` A filter to reduce results to a specific subset. Useful for querying conversations with specific properties.  
`order_by` |  `string` Optional. The attribute by which to order conversations in the response. If empty, conversations will be ordered by descending creation time. Supported values are one of the following:

  * create_time
  * customer_satisfaction_rating
  * duration
  * latest_analysis
  * start_time
  * turn_count

The default sort order is ascending. To specify order, append `asc` or `desc` (`create_time desc`). For more details, see [Google AIPs Ordering](https://google.aip.dev/132#ordering).  
`view` |  `[ConversationView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationView)` The level of details of the conversation. Default is `BASIC`.  
  
## ListConversationsResponse

The response of listing conversations.

Fields  
---  
`conversations[]` |  `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)` The conversations that match the request.  
`next_page_token` |  `string` A token which can be sent as `page_token` to retrieve the next page. If this field is set, it means there is another page available. If it is not set, it means no other pages are available.  
  
## ListFeedbackLabelsRequest

The request for listing feedback labels.

Fields  
---  
`parent` |  `string` Required. The parent resource of the feedback labels.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset. Supports disjunctions (OR) and conjunctions (AND). Automatically sorts by conversation ID. To sort by all feedback labels in a project see ListAllFeedbackLabels.Supported fields:

  * `issue_model_id`
  * `qa_question_id`
  * `qa_scorecard_id`
  * `min_create_time`
  * `max_create_time`
  * `min_update_time`
  * `max_update_time`
  * `feedback_label_type`: QUALITY_AI, TOPIC_MODELING

  
`page_size` |  `int32` Optional. The maximum number of feedback labels to return in the response. A valid page size ranges from 0 to 100,000 inclusive. If the page size is zero or unspecified, a default page size of 100 will be chosen. Note that a call might return fewer results than the requested page size.  
`page_token` |  `string` Optional. The value returned by the last `ListFeedbackLabelsResponse`. This value indicates that this is a continuation of a prior `ListFeedbackLabels` call and that the system should return the next page of data.  
  
## ListFeedbackLabelsResponse

The response for listing feedback labels.

Fields  
---  
`feedback_labels[]` |  `[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)` The feedback labels that match the request.  
`next_page_token` |  `string` The next page token.  
  
## ListIssueModelsRequest

Request to list issue models.

Fields  
---  
`parent` |  `string` Required. The parent resource of the issue model.  
  
## ListIssueModelsResponse

The response of listing issue models.

Fields  
---  
`issue_models[]` |  `[IssueModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel)` The issue models that match the request.  
  
## ListIssuesRequest

Request to list issues.

Fields  
---  
`parent` |  `string` Required. The parent resource of the issue.  
  
## ListIssuesResponse

The response of listing issues.

Fields  
---  
`issues[]` |  `[Issue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Issue)` The issues that match the request.  
  
## ListNotesRequest

The message to list notes.

Fields  
---  
`parent` |  `string` Required. The parent resource of the notes.  
`page_size` |  `int32` Optional. The maximum number of notes to return in the response. If zero the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListNotesResponse`. This value indicates that this is a continuation of a prior `ListNotes` call and that the system should return the next page of data.  
  
## ListNotesResponse

The response of listing notes.

Fields  
---  
`notes[]` |  `[Note](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note)` The notes that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListPhraseMatchersRequest

Request to list phrase matchers.

Fields  
---  
`parent` |  `string` Required. The parent resource of the phrase matcher.  
`page_size` |  `int32` The maximum number of phrase matchers to return in the response. If this value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` The value returned by the last `ListPhraseMatchersResponse`. This value indicates that this is a continuation of a prior `ListPhraseMatchers` call and that the system should return the next page of data.  
`filter` |  `string` A filter to reduce results to a specific subset. Useful for querying phrase matchers with specific properties.  
  
## ListPhraseMatchersResponse

The response of listing phrase matchers.

Fields  
---  
`phrase_matchers[]` |  `[PhraseMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher)` The phrase matchers that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListQaQuestionTagsRequest

Request to list QaQuestionsTags.

Fields  
---  
`parent` |  `string` Required. The parent resource of the QaQuestionTags.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset. Supports disjunctions (OR) and conjunctions (AND). Supported fields include the following:

  * `project_id` \- id of the project to list tags for
  * `qa_scorecard_revision_id` \- id of the scorecard revision to list tags for
  * `qa_question_id - id of the question to list tags for`

  
  
## ListQaQuestionTagsResponse

The response from a ListQaQuestionTags request.

Fields  
---  
`qa_question_tags[]` |  `[QaQuestionTag](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestionTag)` The parent resource of the questions.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListQaQuestionsRequest

Request to list QaQuestions.

Fields  
---  
`parent` |  `string` Required. The parent resource of the questions.  
`page_size` |  `int32` Optional. The maximum number of questions to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListQaQuestionsResponse`. This value indicates that this is a continuation of a prior `ListQaQuestions` call and that the system should return the next page of data.  
  
## ListQaQuestionsResponse

The response from a ListQaQuestions request.

Fields  
---  
`qa_questions[]` |  `[QaQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion)` The QaQuestions under the parent.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListQaScorecardRevisionsRequest

Request to list QaScorecardRevisions

Fields  
---  
`parent` |  `string` Required. The parent resource of the scorecard revisions. To list all revisions of all scorecards, substitute the QaScorecard ID with a '-' character.  
`page_size` |  `int32` Optional. The maximum number of scorecard revisions to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListQaScorecardRevisionsResponse`. This value indicates that this is a continuation of a prior `ListQaScorecardRevisions` call and that the system should return the next page of data.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset. Useful for querying scorecard revisions with specific properties.  
  
## ListQaScorecardRevisionsResponse

The response from a ListQaScorecardRevisions request.

Fields  
---  
`qa_scorecard_revisions[]` |  `[QaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision)` The QaScorecards under the parent.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListQaScorecardsRequest

Request to list QaScorecards.

Fields  
---  
`parent` |  `string` Required. The parent resource of the scorecards.  
`page_size` |  `int32` Optional. The maximum number of scorecards to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListQaScorecardsResponse`. This value indicates that this is a continuation of a prior `ListQaScorecards` call and that the system should return the next page of data.  
  
## ListQaScorecardsResponse

The response from a ListQaScorecards request.

Fields  
---  
`qa_scorecards[]` |  `[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)` The QaScorecards under the parent.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListViewsRequest

The request to list views.

Fields  
---  
`parent` |  `string` Required. The parent resource of the views.  
`page_size` |  `int32` The maximum number of views to return in the response. If this value is zero, the service will select a default size. A call may return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` The value returned by the last `ListViewsResponse`; indicates that this is a continuation of a prior `ListViews` call and the system should return the next page of data.  
  
## ListViewsResponse

The response of listing views.

Fields  
---  
`views[]` |  `[View](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.View)` The views that match the request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## Note

The conversation assessment note resource.

Fields  
---  
`name` |  `string` Identifier. The resource name of the note. Format: projects/{project}/locations/{location}/conversations/{conversation}/assessments/{assessment}/notes/{note}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the note was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the note was last updated.  
`note_creator` |  `[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UserInfo)` Output only. The user that created the note.  
Union field `note_type`. The type of the note. `note_type` can be only one of the following:  
`conversation_turn_note` |  `[ConversationTurnNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note.ConversationTurnNote)` The note is associated with a conversation turn.  
`qa_question_note` |  `[QaQuestionNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note.QaQuestionNote)` The note is associated with a QA question in one of the conversation's scorecard results.  
`assessment_note` |  `[AssessmentNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note.AssessmentNote)` The note is associated to the entire parent assessment.  
`content` |  `string` The note content.  
  
## AssessmentNote

This type has no fields.

A note about the entire parent assessment.

## ConversationTurnNote

A note about a conversation turn.

Fields  
---  
`turn_index` |  `int32` The conversation turn index that the note is associated with.  
  
## QaQuestionNote

A note about a QA question.

Fields  
---  
`qa_question` |  `string` The question resource that the note is associated with.  
  
## PhraseMatchData

The data for a matched phrase matcher. Represents information identifying a phrase matcher for a given match.

Fields  
---  
`phrase_matcher` |  `string` The unique identifier (the resource name) of the phrase matcher.  
`display_name` |  `string` The human-readable name of the phrase matcher.  
  
## PhraseMatchRule

The data for a phrase match rule.

Fields  
---  
`query` |  `string` Required. The phrase to be matched.  
`negated` |  `bool` Specifies whether the phrase must be missing from the transcript segment or present in the transcript segment.  
`config` |  `[PhraseMatchRuleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRuleConfig)` Provides additional information about the rule that specifies how to apply the rule.  
  
## PhraseMatchRuleConfig

Configuration information of a phrase match rule.

Fields  
---  
Union field `config`. The configuration of the phrase match rule. `config` can be only one of the following:  
`exact_match_config` |  `[ExactMatchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ExactMatchConfig)` The configuration for the exact match rule.  
  
## PhraseMatchRuleGroup

A message representing a rule in the phrase matcher.

Fields  
---  
`type` |  `[PhraseMatchRuleGroupType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRuleGroup.PhraseMatchRuleGroupType)` Required. The type of this phrase match rule group.  
`phrase_match_rules[]` |  `[PhraseMatchRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRule)` A list of phrase match rules that are included in this group.  
  
## PhraseMatchRuleGroupType

Specifies how to combine each phrase match rule for whether there is a match.

Enums  
---  
`PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED` | Unspecified.  
`ALL_OF` | Must meet all phrase match rules or there is no match.  
`ANY_OF` | If any of the phrase match rules are met, there is a match.  
  
## PhraseMatcher

The phrase matcher resource.

Fields  
---  
`name` |  `string` The resource name of the phrase matcher. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher}  
`revision_id` |  `string` Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567  
`version_tag` |  `string` The customized version tag to use for the phrase matcher. If not specified, it will default to `revision_id`.  
`revision_create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added.  
`display_name` |  `string` The human-readable name of the phrase matcher.  
`type` |  `[PhraseMatcherType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher.PhraseMatcherType)` Required. The type of this phrase matcher.  
`active` |  `bool` Applies the phrase matcher only when it is active.  
`phrase_match_rule_groups[]` |  `[PhraseMatchRuleGroup](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatchRuleGroup)` A list of phase match rule groups that are included in this matcher.  
`activation_update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the activation status was updated.  
`role_match` |  `[Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationParticipant.Role)` The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the phrase matcher was updated.  
  
## PhraseMatcherType

Specifies how to combine each phrase match rule group to determine whether there is a match.

Enums  
---  
`PHRASE_MATCHER_TYPE_UNSPECIFIED` | Unspecified.  
`ALL_OF` | Must meet all phrase match rule groups or there is no match.  
`ANY_OF` | If any of the phrase match rule groups are met, there is a match.  
  
## PublishAssessmentRequest

The message to publish an assessment. Draft and appealed assessments can be published. Publishing simply changes the state of the assessment to published, allowing the console and authorized views to filter on the state.

Fields  
---  
`name` |  `string` Required. The name of the assessment to publish.  
  
## QaAnswer

An answer to a QaQuestion.

Fields  
---  
`qa_question` |  `string` The QaQuestion answered by this answer.  
`conversation` |  `string` The conversation the answer applies to.  
`question_body` |  `string` Question text. E.g., "Did the agent greet the customer?"  
`answer_value` |  `[AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerValue)` The main answer value, incorporating any manual edits if they exist.  
`tags[]` |  `string` User-defined list of arbitrary tags. Matches the value from QaScorecard.ScorecardQuestion.tags. Used for grouping/organization and for weighting the score of each answer.  
`answer_sources[]` |  `[AnswerSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerSource)` List of all individual answers given to the question.  
  
## AnswerSource

A question may have multiple answers from varying sources, one of which becomes the "main" answer above. AnswerSource represents each individual answer.

Fields  
---  
`source_type` |  `[SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerSource.SourceType)` What created the answer.  
`answer_value` |  `[AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer.AnswerValue)` The answer value from this source.  
  
## SourceType

What created the answer.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | Source type is unspecified.  
`SYSTEM_GENERATED` | Answer was system-generated; created during an Insights analysis.  
`MANUAL_EDIT` | Answer was created by a human via manual edit.  
  
## AnswerValue

Message for holding the value of a `[QaAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer)`. `[QaQuestion.AnswerChoice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.AnswerChoice)` defines the possible answer values for a question.

Fields  
---  
`key` |  `string` A short string used as an identifier. Matches the value used in QaQuestion.AnswerChoice.key.  
Union field `value`. The answer value may be one of a few different types. `value` can be only one of the following:  
`str_value` |  `string` String value.  
`num_value` |  `double` Numerical value.  
`bool_value` |  `bool` Boolean value.  
`na_value` |  `bool` A value of "Not Applicable (N/A)". Should only ever be `true`.  
`score` |  `double` Output only. Numerical score of the answer.  
`potential_score` |  `double` Output only. The maximum potential score of the question.  
`normalized_score` |  `double` Output only. Normalized score of the questions. Calculated as score / potential_score.  
  
## QaQuestion

A single question to be scored by the Insights QA feature.

Fields  
---  
`name` |  `string` Identifier. The resource name of the question. Format: projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}/revisions/{revision}/qaQuestions/{qa_question}  
`abbreviation` |  `string` Short, descriptive string, used in the UI where it's not practical to display the full question body. E.g., "Greeting".  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this question was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the question was updated.  
`question_type` |  `[QaQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.QaQuestionType)` The type of question.  
`predefined_question_config` |  `[PredefinedQuestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.PredefinedQuestionConfig)` The configuration of the predefined question. This field will only be set if the Question Type is predefined.  
`question_body` |  `string` Question text. E.g., "Did the agent greet the customer?"  
`answer_instructions` |  `string` Instructions describing how to determine the answer.  
`answer_choices[]` |  `[AnswerChoice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.AnswerChoice)` A list of valid answers to the question, which the LLM must choose from.  
`tags[]` |  `string` Questions are tagged for categorization and scoring. Tags can either be: - Default Tags: These are predefined categories. They are identified by their string value (e.g., "BUSINESS", "COMPLIANCE", and "CUSTOMER"). - Custom Tags: These are user-defined categories. They are identified by their full resource name (e.g., projects/{project}/locations/{location}/qaQuestionTags/{qa_question_tag}). Both default and custom tags are used to group questions and to influence the scoring of each question.  
`order` |  `int32` Defines the order of the question within its parent scorecard revision.  
`metrics` |  `[Metrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.Metrics)` Metrics of the underlying tuned LLM over a holdout/test set while fine tuning the underlying LLM for the given question. This field will only be populated if and only if the question is part of a scorecard revision that has been tuned.  
`tuning_metadata` |  `[TuningMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.TuningMetadata)` Metadata about the tuning operation for the question.This field will only be populated if and only if the question is part of a scorecard revision that has been tuned.  
  
## AnswerChoice

Message representing a possible answer to the question.

Fields  
---  
`key` |  `string` A short string used as an identifier.  
Union field `value`. The answer value may be one of a few different types. `value` can be only one of the following:  
`str_value` |  `string` String value.  
`num_value` |  `double` Numerical value.  
`bool_value` |  `bool` Boolean value.  
`na_value` |  `bool` A value of "Not Applicable (N/A)". If provided, this field may only be set to `true`. If a question receives this answer, it will be excluded from any score calculations.  
`score` |  `double` Numerical score of the answer, used for generating the overall score of a QaScorecardResult. If the answer uses na_value, this field is unused.  
  
## Metrics

A wrapper representing metrics calculated against a test-set on a LLM that was fine tuned for this question.

Fields  
---  
`accuracy` |  `double` Output only. Accuracy of the model. Measures the percentage of correct answers the model gave on the test set.  
  
## PredefinedQuestionConfig

Configuration for a predefined question. This field will only be set if the Question Type is predefined.

Fields  
---  
`type` |  `[PredefinedQuestionType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion.PredefinedQuestionConfig.PredefinedQuestionType)` The type of the predefined question.  
  
## PredefinedQuestionType

Enum representing the type of the predefined question.

Enums  
---  
`PREDEFINED_QUESTION_TYPE_UNSPECIFIED` | The type of the predefined question is unspecified.  
`CONVERSATION_OUTCOME` | A prebuilt classifier classfying the outcome of the conversation. For example, if the customer issue mentioned in a conversation has been resolved or not.  
`CONVERSATION_OUTCOME_ESCALATION_INITIATOR_ROLE` | A prebuilt classifier classfying the initiator of the conversation escalation. For example, if it was initiated by the customer or the agent.  
  
## QaQuestionType

Enum representing the type of the question.

Enums  
---  
`QA_QUESTION_TYPE_UNSPECIFIED` | The type of the question is unspecified.  
`CUSTOMIZABLE` | The default question type. The question is fully customizable by the user.  
`PREDEFINED` | The question type is using a predefined model provided by CCAI teams. Users are not allowed to edit the question_body, answer_choices, upload feedback labels for the question nor fine-tune the question. However, users may edit other fields like question tags, question order, etc.  
  
## TuningMetadata

Metadata about the tuning operation for the question. Will only be set if a scorecard containing this question has been tuned.

Fields  
---  
`total_valid_label_count` |  `int64` Total number of valid labels provided for the question at the time of tuining.  
`dataset_validation_warnings[]` |  `[DatasetValidationWarning](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DatasetValidationWarning)` A list of any applicable data validation warnings about the question's feedback labels.  
`tuning_error` |  `string` Error status of the tuning operation for the question. Will only be set if the tuning operation failed.  
  
## QaQuestionTag

A tag is a resource which aims to categorize a set of questions across multiple scorecards, e.g., "Customer Satisfaction","Billing", etc.

Fields  
---  
`name` |  `string` Identifier. Resource name for the QaQuestionTag Format projects/{project}/locations/{location}/qaQuestionTags/{qa_question_tag} In the above format, the last segment, i.e., qa_question_tag, is a server-generated ID corresponding to the tag resource.  
`display_name` |  `string` Required. A user-specified display name for the tag.  
`qa_question_ids[]` |  `string` Optional. The list of Scorecard Question IDs that the tag applies to. Each QaQuestionId is represented as a full resource name containing the Question ID. Lastly, Since a tag may not necessarily be referenced by any Scorecard Questions, we treat this field as optional.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the question tag was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the question tag was updated.  
  
## QaScorecard

A QaScorecard represents a collection of questions to be scored during analysis.

Fields  
---  
`name` |  `string` Identifier. The scorecard name. Format: projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}  
`display_name` |  `string` The user-specified display name of the scorecard.  
`description` |  `string` A text description explaining the intent of the scorecard.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this scorecard was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the scorecard was updated.  
`is_default` |  `bool` Whether the scorecard is the default one for the project. A default scorecard cannot be deleted and will always appear first in scorecard selector.  
  
## QaScorecardResult

The results of scoring a single conversation against a QaScorecard. Contains a collection of QaAnswers and aggregate score.

Fields  
---  
`name` |  `string` Identifier. The name of the scorecard result. Format: projects/{project}/locations/{location}/qaScorecardResults/{qa_scorecard_result}  
`qa_scorecard_revision` |  `string` The QaScorecardRevision scored by this result.  
`conversation` |  `string` The conversation scored by this result.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp that the revision was created.  
`agent_id` |  `string` ID of the agent that handled the conversation.  
`qa_answers[]` |  `[QaAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaAnswer)` Set of QaAnswers represented in the result.  
`qa_tag_results[]` |  `[QaTagResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult.QaTagResult)` Collection of tags and their scores.  
`score_sources[]` |  `[ScoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult.ScoreSource)` List of all individual score sets.  
`score` |  `double` The overall numerical score of the result, incorporating any manual edits if they exist.  
`potential_score` |  `double` The maximum potential overall score of the scorecard. Any questions answered using `na_value` are excluded from this calculation.  
`normalized_score` |  `double` The normalized score, which is the score divided by the potential score. Any manual edits are included if they exist.  
  
## QaTagResult

Tags and their corresponding results.

Fields  
---  
`tag` |  `string` The tag the score applies to.  
`score` |  `double` The score the tag applies to.  
`potential_score` |  `double` The potential score the tag applies to.  
`normalized_score` |  `double` The normalized score the tag applies to.  
  
## ScoreSource

A scorecard result may have multiple sets of scores from varying sources, one of which becomes the "main" answer above. A ScoreSource represents each individual set of scores.

Fields  
---  
`source_type` |  `[SourceType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult.ScoreSource.SourceType)` What created the score.  
`qa_tag_results[]` |  `[QaTagResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardResult.QaTagResult)` Collection of tags and their scores.  
`score` |  `double` The overall numerical score of the result.  
`potential_score` |  `double` The maximum potential overall score of the scorecard. Any questions answered using `na_value` are excluded from this calculation.  
`normalized_score` |  `double` The normalized score, which is the score divided by the potential score.  
  
## SourceType

What created the score.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | Source type is unspecified.  
`SYSTEM_GENERATED_ONLY` | Score is derived only from system-generated answers.  
`INCLUDES_MANUAL_EDITS` | Score is derived from both system-generated answers, and includes any manual edits if they exist.  
  
## QaScorecardRevision

A revision of a QaScorecard.

Modifying published scorecard fields would invalidate existing scorecard results — the questions may have changed, or the score weighting will make existing scores impossible to understand. So changes must create a new revision, rather than modifying the existing resource.

Fields  
---  
`name` |  `string` Identifier. The name of the scorecard revision. Format: projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}/revisions/{revision}  
`snapshot` |  `[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)` The snapshot of the scorecard at the time of this revision's creation.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp that the revision was created.  
`alternate_ids[]` |  `string` Output only. Alternative IDs for this revision of the scorecard, e.g., `latest`.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecardRevision.State)` Output only. State of the scorecard revision, indicating whether it's ready to be used in analysis.  
  
## State

Enum representing the set of states a scorecard revision may be in.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`EDITABLE` | The scorecard revision can be edited.  
`TRAINING` | Scorecard model training is in progress.  
`TRAINING_FAILED` | Scorecard revision model training failed.  
`READY` | The revision can be used in analysis.  
`DELETING` | Scorecard is being deleted.  
`TRAINING_CANCELLED` | Scorecard model training was explicitly cancelled by the user.  
  
## QueryInterval

A time window for querying conversations.

Fields  
---  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. The start time of the time window.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. The end time of the time window.  
  
## QueryMetricsMetadata

The metadata from querying metrics.

Fields  
---  
`result_is_truncated` |  `bool` Whether the result rows were truncated because the result row size is too large to materialize.  
  
## QueryMetricsRequest

The request for querying metrics.

Fields  
---  
`location` |  `string` Required. The location of the data. "projects/{project}/locations/{location}"  
`filter` |  `string` Required. Filter to select a subset of conversations to compute the metrics. Must specify a window of the conversation create time to compute the metrics. The returned metrics will be from the range [DATE(starting create time), DATE(ending create time)).  
`time_granularity` |  `[TimeGranularity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsRequest.TimeGranularity)` The time granularity of each data point in the time series. Defaults to NONE if this field is unspecified.  
`dimensions[]` |  `[Dimension](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension)` The dimensions that determine the grouping key for the query. Defaults to no dimension if this field is unspecified. If a dimension is specified, its key must also be specified. Each dimension's key must be unique.If a time granularity is also specified, metric values in the dimension will be bucketed by this granularity.Up to one dimension is supported for now.  
`measure_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Measures to return. Defaults to all measures if this field is unspecified. A valid mask should traverse from the `measure` field from the response. For example, a path from a measure mask to get the conversation count is "conversation_measure.count".  
  
## TimeGranularity

A time granularity divides the time line into discrete time periods. This is useful for defining buckets over which filtering and aggregation should be performed.

Enums  
---  
`TIME_GRANULARITY_UNSPECIFIED` | The time granularity is unspecified and will default to NONE.  
`NONE` | No time granularity. The response won't contain a time series. This is the default value if no time granularity is specified.  
`DAILY` | Data points in the time series will aggregate at a daily granularity. 1 day means [midnight to midnight).  
`HOURLY` | Data points in the time series will aggregate at a daily granularity. 1 HOUR means [01:00 to 02:00).  
`PER_MINUTE` | Data points in the time series will aggregate at a daily granularity. PER_MINUTE means [01:00 to 01:01).  
`PER_5_MINUTES` | Data points in the time series will aggregate at a 1 minute granularity. PER_5_MINUTES means [01:00 to 01:05).  
`MONTHLY` | Data points in the time series will aggregate at a monthly granularity. 1 MONTH means [01st of the month to 1st of the next month).  
  
## QueryMetricsResponse

The response for querying metrics.

Fields  
---  
`location` |  `string` Required. The location of the data. "projects/{project}/locations/{location}"  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The metrics last update time.  
`slices[]` |  `[Slice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice)` A slice contains a total and (if the request specified a time granularity) a time series of metric values. Each slice contains a unique combination of the cardinality of dimensions from the request.  
`macro_average_slice` |  `[Slice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice)` The macro average slice contains aggregated averages across the selected dimension. i.e. if group_by agent is specified this field will contain the average across all agents. This field is only populated if the request specifies a Dimension.  
  
## Slice

A slice contains a total and (if the request specified a time granularity) a time series of metric values. Each slice contains a unique combination of the cardinality of dimensions from the request.

For example, if the request specifies a single ISSUE dimension and it has a cardinality of 2 (i.e. the data used to compute the metrics has 2 issues in total), the response will have 2 slices:

  * Slice 1 -> dimensions=[Issue 1]
  * Slice 2 -> dimensions=[Issue 2]

Fields  
---  
`dimensions[]` |  `[Dimension](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dimension)` A unique combination of dimensions that this slice represents.  
`total` |  `[DataPoint](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.DataPoint)` The total metric value. The interval of this data point is [starting create time, ending create time) from the request.  
`time_series` |  `[TimeSeries](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.TimeSeries)` A time series of metric values. This is only populated if the request specifies a time granularity other than NONE.  
  
## DataPoint

A data point contains the metric values mapped to an interval.

Fields  
---  
`interval` |  `[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.type#google.type.Interval)` The interval that this data point represents.

  * If this is the total data point, the interval is [starting create time, ending create time) from the request.
  * If this a data point from the time series, the interval is [time, time + time granularity from the request).

  
Union field `measure`. The measure included in this data point. `measure` can be only one of the following:  
`conversation_measure` |  `[ConversationMeasure](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.DataPoint.ConversationMeasure)` The measure related to conversations.  
  
## ConversationMeasure

The measure related to conversations.

Fields  
---  
`qa_tag_scores[]` |  `[QaTagScore](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore)` Average QA normalized score for all the tags.  
`conversation_count` |  `int32` The conversation count.  
`average_silence_percentage` |  `float` The average silence percentage.  
`average_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The average duration.  
`average_turn_count` |  `float` The average turn count.  
`average_agent_sentiment_score` |  `float` The average agent's sentiment score.  
`average_client_sentiment_score` |  `float` The average client's sentiment score.  
`average_customer_satisfaction_rating` |  `double` The average customer satisfaction rating.  
`average_qa_normalized_score` |  `double` Average QA normalized score. Will exclude 0's in average calculation.  
`average_qa_question_normalized_score` |  `double` Average QA normalized score averaged for questions averaged across all revisions of the parent scorecard. Will be only populated if the request specifies a dimension of QA_QUESTION_ID.  
  
## QaTagScore

Average QA normalized score for the tag.

Fields  
---  
`tag` |  `string` Tag name.  
`average_tag_normalized_score` |  `double` Average tag normalized score per tag.  
  
## TimeSeries

A time series of metric values.

Fields  
---  
`data_points[]` |  `[DataPoint](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryMetricsResponse.Slice.DataPoint)` The data points that make up the time series .  
  
## QueryPerformanceOverviewMetadata

This type has no fields.

The metadata for querying performance overview.

## QueryPerformanceOverviewRequest

The request for summarizing performance according to different metrics for conversations over a specified time window.

Fields  
---  
`parent` |  `string` Required. The parent resource of the conversations to derive performance stats from. "projects/{project}/locations/{location}"  
`filter` |  `string` Optional. Filter to select a subset of conversations to compute the performance overview. Supports the same filters as the filter field in QueryMetricsRequest. The source and query interval/comparison query interval should not be included here.  
`query_interval` |  `[QueryInterval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryInterval)` Required. The time window of the conversations to derive performance stats from.  
Union field `source`. The type of source of conversations to derive performance from. `source` can be only one of the following:  
`agent_performance_source` |  `[AgentSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryPerformanceOverviewRequest.AgentSource)` Conversations are from a single agent.  
`comparison_query_interval` |  `[QueryInterval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QueryInterval)` The time window of the conversations to compare the performance to.  
  
## AgentSource

The entity whose performance is being queried is a single agent.

Fields  
---  
`agent_id` |  `string` Required. Agent id to query performance overview for.  
  
## QueryPerformanceOverviewResponse

The response for querying performance overview.

Fields  
---  
`summary_text` |  `string` The summary text of the performance.  
  
## RedactionConfig

DLP resources used for redaction while ingesting conversations. DLP settings are applied to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversation coming from CCAI Platform. They are not applied to conversations ingested from the `CreateConversation` endpoint or the Dialogflow / Agent Assist runtime integrations. When using Dialogflow / Agent Assist runtime integrations, redaction should be performed in Dialogflow / Agent Assist.

Fields  
---  
`deidentify_template` |  `string` The fully-qualified DLP deidentify template resource name. Format: `projects/{project}/deidentifyTemplates/{template}`  
`inspect_template` |  `string` The fully-qualified DLP inspect template resource name. Format: `projects/{project}/locations/{location}/inspectTemplates/{template}`  
  
## RuntimeAnnotation

An annotation that was generated during the customer and agent interaction.

Fields  
---  
`annotation_id` |  `string` The unique identifier of the annotation. Format: projects/{project}/locations/{location}/conversationDatasets/{dataset}/conversationDataItems/{data_item}/conversationAnnotations/{annotation}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which this annotation was created.  
`start_boundary` |  `[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotationBoundary)` The boundary in the conversation where the annotation starts, inclusive.  
`end_boundary` |  `[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotationBoundary)` The boundary in the conversation where the annotation ends, inclusive.  
`answer_feedback` |  `[AnswerFeedback](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnswerFeedback)` The feedback that the customer has about the answer in `data`.  
`user_input` |  `[UserInput](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RuntimeAnnotation.UserInput)` Explicit input used for generating the answer  
Union field `data`. The data in the annotation. `data` can be only one of the following:  
`article_suggestion` |  `[ArticleSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ArticleSuggestionData)` Agent Assist Article Suggestion data.  
`faq_answer` |  `[FaqAnswerData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FaqAnswerData)` Agent Assist FAQ answer data.  
`smart_reply` |  `[SmartReplyData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SmartReplyData)` Agent Assist Smart Reply data.  
`smart_compose_suggestion` |  `[SmartComposeSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SmartComposeSuggestionData)` Agent Assist Smart Compose suggestion data.  
`dialogflow_interaction` |  `[DialogflowInteractionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DialogflowInteractionData)` Dialogflow interaction data.  
`conversation_summarization_suggestion` |  `[ConversationSummarizationSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.ConversationSummarizationSuggestionData)` Conversation summarization suggestion data.  
  
## UserInput

Explicit input used for generating the answer

Fields  
---  
`query` |  `string` Query text. Article Search uses this to store the input query used to generate the search results.  
`generator_name` |  `string` The resource name of associated generator. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`query_source` |  `[QuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RuntimeAnnotation.UserInput.QuerySource)` Query source for the answer.  
  
## QuerySource

The source of the query.

Enums  
---  
`QUERY_SOURCE_UNSPECIFIED` | Unknown query source.  
`AGENT_QUERY` | The query is from agents.  
`SUGGESTED_QUERY` | The query is a query from previous suggestions, e.g. from a preceding SuggestKnowledgeAssist response.  
  
## SampleConversationsMetadata

The metadata for an SampleConversations operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[SampleConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleConversationsRequest)` Output only. The original request for sample conversations to dataset.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.rpc#google.rpc.Status)` Output only. Partial errors during sample conversations operation that might cause the operation output to be incomplete.  
`sample_conversations_stats` |  `[SampleConversationsStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleConversationsMetadata.SampleConversationsStats)` Output only. Statistics for SampleConversations operation.  
  
## SampleConversationsStats

Statistics for SampleConversations operation.

Fields  
---  
`successful_sample_count` |  `int32` Output only. The number of new conversations added during this sample operation.  
`failed_sample_count` |  `int32` Output only. The number of objects which were unable to be sampled due to errors. The errors are populated in the partial_errors field.  
  
## SampleConversationsRequest

The request to sample conversations to a dataset.

Fields  
---  
`parent` |  `string` Required. The parent resource of the dataset.  
`sample_rule` |  `[SampleRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SampleRule)` Optional. The sample rule used for sampling conversations.  
Union field `destination`. The destination of the sampled conversations. `destination` can be only one of the following:  
`destination_dataset` |  `[Dataset](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Dataset)` The dataset resource to copy the sampled conversations to.  
  
## SampleConversationsResponse

This type has no fields.

The response to an SampleConversations operation.

## SampleRule

Message for sampling conversations.

Fields  
---  
`dimension` |  `string` Optional. Group by dimension to sample the conversation. If no dimension is provided, the sampling will be applied to the project level. Current supported dimensions is 'quality_metadata.agent_info.agent_id'.  
`conversation_filter` |  `string` To specify the filter for the conversions that should apply this sample rule. An empty filter means this sample rule applies to all conversations.  
Union field `SampleVolume`. Determines how the conversations are selected. `SampleVolume` can be only one of the following:  
`sample_percentage` |  `double` Percentage of conversations that we should sample based on the dimension between [0, 100].  
`sample_row` |  `int64` Number of the conversations that we should sample based on the dimension.  
  
## ScheduleInfo

Message for schedule info.

Fields  
---  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Start time of the schedule. If not specified, will start as soon as the schedule is created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` End time of the schedule. If not specified, will keep scheduling new pipelines for execution util the schedule is no longer active or deleted.  
`schedule` |  `string` The groc expression. Format: `every [number] [time_unit] [synchronized]` Time units can be: minutes, hours Synchronized is optional and indicates that the schedule should be synchronized to the start of the interval: every 5 minutes synchronized means 00:00, 00:05 ... Otherwise the start time is random within the interval. Example: `every 5 minutes` could be 00:02, 00:07, 00:12, ...  
`time_zone` |  `string` The timezone to use for the groc expression. If not specified, defaults to UTC.  
  
## SearchAuthorizedViewsRequest

The request for listing AuthorizedViews.

Fields  
---  
`parent` |  `string` Required. The parent resource of the AuthorizedViews. If the parent is set to `-`, all AuthorizedViews under the location will be returned.  
`page_size` |  `int32` Optional. The maximum number of view to return in the response. If the value is zero, the service will select a default size. A call might return fewer objects than requested. A non-empty `next_page_token` in the response indicates that more data is available.  
`page_token` |  `string` Optional. The value returned by the last `ListAuthorizedViewsResponse`. This value indicates that this is a continuation of a prior `ListAuthorizedViews` call and that the system should return the next page of data.  
`query` |  `string` Optional. The query expression to search authorized views.  
`order_by` |  `string` Optional. The order by expression to order authorized views listed in the response.  
  
## SearchAuthorizedViewsResponse

The response from a ListAuthorizedViews request.

Fields  
---  
`authorized_views[]` |  `[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)` The AuthorizedViews under the parent.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## SentimentData

The data for a sentiment annotation.

Fields  
---  
`magnitude` |  `float` A non-negative number from 0 to infinity which represents the absolute magnitude of sentiment regardless of score.  
`score` |  `float` The sentiment score between -1.0 (negative) and 1.0 (positive).  
  
## Settings

The CCAI Insights project wide settings. Use these settings to configure the behavior of Insights. View these settings with [`getsettings`](https://cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/getSettings) and change the settings with [`updateSettings`](https://cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/updateSettings).

Fields  
---  
`name` |  `string` Immutable. The resource name of the settings resource. Format: projects/{project}/locations/{location}/settings  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the settings was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which the settings were last updated.  
`language_code` |  `string` A language code to be applied to each transcript segment unless the segment already specifies a language code. Language code defaults to "en-US" if it is neither specified on the segment nor here.  
`conversation_ttl` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The default TTL for newly-created conversations. If a conversation has a specified expiration, that value will be used instead. Changing this value will not change the expiration of existing conversations. Conversations with no expire time persist until they are deleted.  
`pubsub_notification_settings` |  `map<string, string>` A map that maps a notification trigger to a Pub/Sub topic. Each time a specified trigger occurs, Insights will notify the corresponding Pub/Sub topic.Keys are notification triggers. Supported keys are:

  * "all-triggers": Notify each time any of the supported triggers occurs.
  * "create-analysis": Notify each time an analysis is created.
  * "create-conversation": Notify each time a conversation is created.
  * "export-insights-data": Notify each time an export is complete.
  * "ingest-conversations": Notify each time an IngestConversations LRO is complete.
  * "update-conversation": Notify each time a conversation is updated via UpdateConversation.
  * "upload-conversation": Notify when an UploadConversation LRO is complete.

Values are Pub/Sub topics. The format of each Pub/Sub topic is: projects/{project}/topics/{topic}  
`analysis_config` |  `[AnalysisConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Settings.AnalysisConfig)` Default analysis settings.  
`redaction_config` |  `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RedactionConfig)` Default DLP redaction resources to be applied while ingesting conversations. This applies to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversations coming from CCAI Platform.  
`speech_config` |  `[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SpeechConfig)` Optional. Default Speech-to-Text resources to use while ingesting audio files. Optional, CCAI Insights will create a default if not provided. This applies to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversations coming from CCAI Platform.  
  
## AnalysisConfig

Default configuration when creating Analyses in Insights.

Fields  
---  
`runtime_integration_analysis_percentage` |  `double` Percentage of conversations created using Dialogflow runtime integration to analyze automatically, between [0, 100].  
`upload_conversation_analysis_percentage` |  `double` Percentage of conversations created using the UploadConversation endpoint to analyze automatically, between [0, 100].  
`annotator_selector` |  `[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnnotatorSelector)` To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.  
  
## SilenceData

This type has no fields.

The data for a silence annotation.

## SmartComposeSuggestionData

Agent Assist Smart Compose suggestion data.

Fields  
---  
`suggestion` |  `string` The content of the suggestion.  
`confidence_score` |  `double` The system's confidence score that this suggestion is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`metadata` |  `map<string, string>` Map that contains metadata about the Smart Compose suggestion and the document from which it originates.  
`query_record` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record}  
  
## SmartReplyData

Agent Assist Smart Reply data.

Fields  
---  
`reply` |  `string` The content of the reply.  
`confidence_score` |  `double` The system's confidence score that this reply is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`metadata` |  `map<string, string>` Map that contains metadata about the Smart Reply and the document from which it originates.  
`query_record` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record}  
  
## SpeechConfig

Speech-to-Text configuration. Speech-to-Text settings are applied to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversation coming from CCAI Platform. They are not applied to conversations ingested from the `CreateConversation` endpoint.

Fields  
---  
`speech_recognizer` |  `string` The fully-qualified Speech Recognizer resource name. Format: `projects/{project_id}/locations/{location}/recognizer/{recognizer}`  
  
## TuneQaScorecardRevisionMetadata

Metadata for TuneQaScorecardRevision endpoint.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[TuneQaScorecardRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionRequest)` Output only. The original request.  
`qa_question_dataset_validation_results[]` |  `[QaQuestionDatasetValidationResult](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionMetadata.QaQuestionDatasetValidationResult)` Output only. The results of data validation per question in the request.  
`qa_question_dataset_tuning_metrics[]` |  `[QaQuestionDatasetTuningMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics)` Output only. The metrics for each QaQuestion in the TuneScorecardRevision request.  
`tuning_completion_ratio` |  `double` Output only. The percentage of the tuning job that has completed. Always between 0 and 1 where 0 indicates the job has not started i.e. 0% and 1 indicates the job has completed i.e. 100%.  
  
## QaQuestionDatasetTuningMetrics

Contains performance metrics for each QaQuestion in the TuneScorecardRevision request.

Fields  
---  
`question` |  `string` Output only. The resource path of the question whose dataset was evaluated for tuning.  
`metrics` |  `[Metrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics)` Output only. The metrics for the question's dataset.  
  
## Metrics

Performance metrics for the question's dataset calculated over the tuned model.

Fields  
---  
`accuracy` |  `double` Accuracy of the question's dataset.  
  
## QaQuestionDatasetValidationResult

Contains validation results for a question in the tuning request.

Fields  
---  
`question` |  `string` Output only. The resource path of the question whose dataset was evaluated for tuning.  
`dataset_validation_warnings[]` |  `[DatasetValidationWarning](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.DatasetValidationWarning)` A list of any applicable data validation warnings about the question's feedback labels.  
`valid_feedback_labels_count` |  `int32` The number of valid feedback labels in the question's dataset.  
  
## TuneQaScorecardRevisionRequest

Request for TuneQaScorecardRevision endpoint.

Fields  
---  
`parent` |  `string` Required. The parent resource for new fine tuning job instance.  
`filter` |  `string` Required. Filter for selecting the feedback labels that needs to be used for training. This filter can be used to limit the feedback labels used for tuning to a feedback labels created or updated for a specific time-window etc.  
`validate_only` |  `bool` Optional. Run in validate only mode, no fine tuning will actually run. Data quality validations like training data distributions will run. Even when set to false, the data quality validations will still run but once the validations complete we will proceed with the fine tune, if applicable.  
  
## TuneQaScorecardRevisionResponse

This type has no fields.

Response for TuneQaScorecardRevision endpoint.

## UndeployIssueModelMetadata

Metadata for undeploying an issue model.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[UndeployIssueModelRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UndeployIssueModelRequest)` The original request for undeployment.  
  
## UndeployIssueModelRequest

The request to undeploy an issue model.

Fields  
---  
`name` |  `string` Required. The issue model to undeploy.  
  
## UndeployIssueModelResponse

This type has no fields.

The response to undeploy an issue model.

## UndeployQaScorecardRevisionRequest

The request to undeploy a QaScorecardRevision

Fields  
---  
`name` |  `string` Required. The name of the QaScorecardRevision to undeploy.  
  
## UpdateAnalysisRuleRequest

The request to update a analysis rule.

Fields  
---  
`analysis_rule` |  `[AnalysisRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AnalysisRule)` Required. The new analysis rule.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to be updated. If the update_mask is not provided, the update will be applied to all fields.  
  
## UpdateAssessmentRuleRequest

The request to update an assessment rule.

Fields  
---  
`assessment_rule` |  `[AssessmentRule](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AssessmentRule)` Required. The new assessment rule.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to be updated. If the update_mask is not provided, the update will be applied to all fields.  
  
## UpdateAuthorizedViewRequest

The request for updating an AuthorizedView.

Fields  
---  
`authorized_view` |  `[AuthorizedView](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedView)` Required. The AuthorizedView to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to be updated. All possible fields can be updated by passing `*`, or a subset of the following updateable fields can be provided:

  * `conversation_filter`
  * `display_name`

  
  
## UpdateAuthorizedViewSetRequest

The request for updating an AuthorizedViewSet.

Fields  
---  
`authorized_view_set` |  `[AuthorizedViewSet](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.AuthorizedViewSet)` Required. The AuthorizedViewSet to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to be updated. All possible fields can be updated by passing `*`, or a subset of the following updateable fields can be provided:

  * `display_name`

  
  
## UpdateConversationRequest

The request to update a conversation.

Fields  
---  
`conversation` |  `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)` Required. The new values for the conversation.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The list of fields to be updated. All possible fields can be updated by passing `*`, or a subset of the following updateable fields can be provided:

  * `agent_id`
  * `language_code`
  * `labels`
  * `metadata`
  * `quality_metadata`
  * `call_metadata`
  * `start_time`
  * `expire_time` or `ttl`
  * `data_source.gcs_source.audio_uri` or `data_source.dialogflow_source.audio_uri`

  
`allow_missing` |  `bool` Optional. Defaults to false. If set to true, and the conversation is not found, a new conversation will be created. In this situation, `update_mask` is ignored.  
  
## UpdateFeedbackLabelRequest

The request for updating a feedback label.

Fields  
---  
`feedback_label` |  `[FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.FeedbackLabel)` Required. The feedback label to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The list of fields to be updated.  
  
## UpdateIssueModelRequest

The request to update an issue model.

Fields  
---  
`issue_model` |  `[IssueModel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.IssueModel)` Required. The new values for the issue model.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The list of fields to be updated.  
  
## UpdateIssueRequest

The request to update an issue.

Fields  
---  
`issue` |  `[Issue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Issue)` Required. The new values for the issue.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The list of fields to be updated.  
  
## UpdateNoteRequest

The request to update a note.

Fields  
---  
`note` |  `[Note](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Note)` Required. The note to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to be updated. If the update_mask is empty, all updateable fields will be updated. Acceptable fields include: * `content`  
  
## UpdatePhraseMatcherRequest

The request to update a phrase matcher.

Fields  
---  
`phrase_matcher` |  `[PhraseMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.PhraseMatcher)` Required. The new values for the phrase matcher.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The list of fields to be updated.  
  
## UpdateQaQuestionRequest

The request for updating a QaQuestion.

Fields  
---  
`qa_question` |  `[QaQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestion)` Required. The QaQuestion to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The list of fields to be updated. All possible fields can be updated by passing `*`, or a subset of the following updateable fields can be provided:

  * `abbreviation`
  * `answer_choices`
  * `answer_instructions`
  * `order`
  * `question_body`
  * `tags`

  
  
## UpdateQaQuestionTagMetadata

The metadata for updating a QaQuestionTag Resource.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[UpdateQaQuestionTagRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UpdateQaQuestionTagRequest)` Output only. The original request.  
  
## UpdateQaQuestionTagRequest

The request for updating a QaQuestionTag.

Fields  
---  
`qa_question_tag` |  `[QaQuestionTag](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaQuestionTag)` Required. The QaQuestionTag to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to be updated. All possible fields can be updated by passing `*`, or a subset of the following updateable fields can be provided:

  * `qa_question_tag_name` \- the name of the tag
  * `qa_question_ids` \- the list of questions the tag applies to

  
  
## UpdateQaScorecardRequest

The request for updating a QaScorecard.

Fields  
---  
`qa_scorecard` |  `[QaScorecard](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.QaScorecard)` Required. The QaScorecard to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The list of fields to be updated. All possible fields can be updated by passing `*`, or a subset of the following updateable fields can be provided:

  * `description`
  * `display_name`

  
  
## UpdateSettingsRequest

The request to update project-level settings.

Fields  
---  
`settings` |  `[Settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Settings)` Required. The new settings values.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The list of fields to be updated.  
  
## UpdateViewRequest

The request to update a view.

Fields  
---  
`view` |  `[View](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.View)` Required. The new view.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` The list of fields to be updated.  
  
## UploadConversationMetadata

The metadata for an `UploadConversation` operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`request` |  `[UploadConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.UploadConversationRequest)` Output only. The original request.  
`analysis_operation` |  `string` Output only. The operation name for a successfully created analysis operation, if any.  
`applied_redaction_config` |  `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RedactionConfig)` Output only. The redaction config applied to the uploaded conversation.  
  
## UploadConversationRequest

Request to upload a conversation.

Fields  
---  
`parent` |  `string` Required. The parent resource of the conversation.  
`conversation` |  `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.Conversation)` Required. The conversation resource to create.  
`conversation_id` |  `string` Optional. A unique ID for the new conversation. This ID will become the final component of the conversation's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `[a-z][0-9]-`  
`redaction_config` |  `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.RedactionConfig)` Optional. DLP settings for transcript redaction. Will default to the config specified in Settings.  
`speech_config` |  `[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.cloud.contactcenterinsights.v1alpha1#google.cloud.contactcenterinsights.v1alpha1.SpeechConfig)` Optional. Speech-to-Text configuration. Will default to the config specified in Settings.  
  
## UserInfo

Information about a user.

Fields  
---  
`username` |  `string` The user's username.  
  
## View

The View resource.

Fields  
---  
`name` |  `string` Immutable. The resource name of the view. Format: projects/{project}/locations/{location}/views/{view}  
`display_name` |  `string` The human-readable display name of the view.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which this view was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The most recent time at which the view was updated.  
`value` |  `string` A filter to reduce conversation results to a specific subset. Refer to <https://cloud.google.com/gemini-enterprise-cx/insights/filtering> for details.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
