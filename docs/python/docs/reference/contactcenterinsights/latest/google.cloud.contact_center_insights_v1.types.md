---
url: https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types
title: Package types (1.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:45.410528+00:00
---

# Package types (1.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.28.0 (latest)  1.27.0  1.26.0  1.25.0  1.24.0  1.23.3  1.22.0  1.21.0  1.20.0  1.19.1  1.18.0  1.17.5  1.16.0  1.15.0  1.14.1  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.0  1.6.1  1.5.0  1.4.5  1.3.2  1.2.1  1.1.0  1.0.0  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

API documentation for `contact_center_insights_v1.types` package.

## Classes 

### [Analysis](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Analysis)

The analysis resource.

### [AnalysisResult](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.AnalysisResult)

The result of an analysis.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnalysisRule](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.AnalysisRule)

The CCAI Insights project wide analysis rule. This rule will be applied to all conversations that match the filter defined in the rule. For a conversation matches the filter, the annotators specified in the rule will be run. If a conversation matches multiple rules, a union of all the annotators will be run. One project can have multiple analysis rules.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationBoundary](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.AnnotationBoundary)

A point in a conversation that marks the start or the end of an annotation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotatorSelector](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.AnnotatorSelector)

Selector of all available annotators and phrase matchers to run.

### [AnswerFeedback](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.AnswerFeedback)

The feedback that the customer has about a certain answer in the conversation.

### [ArticleSuggestionData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ArticleSuggestionData)

Agent Assist Article Suggestion data.

### [BulkAnalyzeConversationsMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkAnalyzeConversationsMetadata)

The metadata for a bulk analyze conversations operation.

### [BulkAnalyzeConversationsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkAnalyzeConversationsRequest)

The request to analyze conversations in bulk.

### [BulkAnalyzeConversationsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkAnalyzeConversationsResponse)

The response for a bulk analyze conversations operation.

### [BulkDeleteConversationsMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkDeleteConversationsMetadata)

The metadata for a bulk delete conversations operation.

### [BulkDeleteConversationsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkDeleteConversationsRequest)

The request to delete conversations in bulk.

### [BulkDeleteConversationsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkDeleteConversationsResponse)

The response for a bulk delete conversations operation.

### [BulkDownloadFeedbackLabelsMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsMetadata)

Metadata for the BulkDownloadFeedbackLabel endpoint.

### [BulkDownloadFeedbackLabelsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsRequest)

Request for the BulkDownloadFeedbackLabel endpoint.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BulkDownloadFeedbackLabelsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsResponse)

Response for the BulkDownloadFeedbackLabel endpoint.

### [BulkUploadFeedbackLabelsMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsMetadata)

Metadata for the Bulk Upload Feedback Labels API.

### [BulkUploadFeedbackLabelsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsRequest)

The request for bulk uploading feedback labels.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BulkUploadFeedbackLabelsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsResponse)

Response for the Bulk Upload Feedback Labels API.

### [CalculateIssueModelStatsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CalculateIssueModelStatsRequest)

Request to get statistics of an issue model.

### [CalculateIssueModelStatsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CalculateIssueModelStatsResponse)

Response of querying an issue model's statistics.

### [CalculateStatsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CalculateStatsRequest)

The request for calculating conversation statistics.

### [CalculateStatsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CalculateStatsResponse)

The response for calculating conversation statistics.

### [CallAnnotation](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CallAnnotation)

A piece of metadata that applies to a window of a call.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Conversation](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Conversation)

The conversation resource.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationDataSource](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ConversationDataSource)

The conversation source, which is a combination of transcript and audio.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationLevelSentiment](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ConversationLevelSentiment)

One channel of conversation-level sentiment data.

### [ConversationLevelSilence](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ConversationLevelSilence)

Conversation-level silence data.

### [ConversationParticipant](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ConversationParticipant)

The call participant speaking for a given utterance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationSummarizationSuggestionData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ConversationSummarizationSuggestionData)

Conversation summarization suggestion data.

### [ConversationView](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ConversationView)

Represents the options for viewing a conversation.
    
    
        - Defaults to `FULL` in `GetConversationRequest`.
        - Defaults to `BASIC` in `ListConversationsRequest`.
    FULL (2):
        Populates all fields in the conversation.
    BASIC (1):
        Populates all fields in the conversation
        except the transcript.
    

### [CreateAnalysisOperationMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateAnalysisOperationMetadata)

Metadata for a create analysis operation.

### [CreateAnalysisRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateAnalysisRequest)

The request to create an analysis.

### [CreateAnalysisRuleRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateAnalysisRuleRequest)

The request to create a analysis rule. analysis_rule_id will be generated by the server.

### [CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateConversationRequest)

Request to create a conversation.

### [CreateFeedbackLabelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateFeedbackLabelRequest)

The request for creating a feedback label.

### [CreateIssueModelMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateIssueModelMetadata)

Metadata for creating an issue model.

### [CreateIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateIssueModelRequest)

The request to create an issue model.

### [CreatePhraseMatcherRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreatePhraseMatcherRequest)

Request to create a phrase matcher.

### [CreateQaQuestionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateQaQuestionRequest)

The request for creating a QaQuestion.

### [CreateQaScorecardRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateQaScorecardRequest)

The request for creating a QaScorecard.

### [CreateQaScorecardRevisionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateQaScorecardRevisionRequest)

The request for creating a QaScorecardRevision.

### [CreateViewRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CreateViewRequest)

The request to create a view.

### [DatasetValidationWarning](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DatasetValidationWarning)

Enum for the different types of issues a tuning dataset can have. These warnings are currentlyraised when trying to validate a dataset for tuning a scorecard.

### [DeleteAnalysisRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteAnalysisRequest)

The request to delete an analysis.

### [DeleteAnalysisRuleRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteAnalysisRuleRequest)

The request to delete a analysis rule.

### [DeleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteConversationRequest)

The request to delete a conversation.

### [DeleteFeedbackLabelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteFeedbackLabelRequest)

The request for deleting a feedback label.

### [DeleteIssueModelMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteIssueModelMetadata)

Metadata for deleting an issue model.

### [DeleteIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteIssueModelRequest)

The request to delete an issue model.

### [DeleteIssueRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteIssueRequest)

The request to delete an issue.

### [DeletePhraseMatcherRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeletePhraseMatcherRequest)

The request to delete a phrase matcher.

### [DeleteQaQuestionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteQaQuestionRequest)

The request for deleting a QaQuestion.

### [DeleteQaScorecardRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteQaScorecardRequest)

The request for deleting a QaScorecard.

### [DeleteQaScorecardRevisionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteQaScorecardRevisionRequest)

The request to delete a QaScorecardRevision.

### [DeleteViewRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeleteViewRequest)

The request to delete a view.

### [DeployIssueModelMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeployIssueModelMetadata)

Metadata for deploying an issue model.

### [DeployIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeployIssueModelRequest)

The request to deploy an issue model.

### [DeployIssueModelResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeployIssueModelResponse)

The response to deploy an issue model.

### [DeployQaScorecardRevisionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DeployQaScorecardRevisionRequest)

The request to deploy a QaScorecardRevision

### [DialogflowIntent](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DialogflowIntent)

The data for a Dialogflow intent. Represents a detected intent in the conversation, e.g. MAKES_PROMISE.

### [DialogflowInteractionData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DialogflowInteractionData)

Dialogflow interaction data.

### [DialogflowSource](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.DialogflowSource)

A Dialogflow source of conversation data.

### [Dimension](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Dimension)

A dimension determines the grouping key for the query. In SQL terms, these would be part of both the "SELECT" and "GROUP BY" clauses.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EncryptionSpec](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.EncryptionSpec)

A customer-managed encryption key specification that can be applied to all created resources (e.g. `Conversation`).

### [Entity](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Entity)

The data for an entity annotation. Represents a phrase in the conversation that is a known entity, such as a person, an organization, or location.

### [EntityMentionData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.EntityMentionData)

The data for an entity mention annotation. This represents a mention of an `Entity` in the conversation.

### [ExactMatchConfig](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExactMatchConfig)

Exact match configuration.

### [ExportInsightsDataMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExportInsightsDataMetadata)

Metadata for an export insights operation.

### [ExportInsightsDataRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExportInsightsDataRequest)

The request to export insights.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportInsightsDataResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExportInsightsDataResponse)

Response for an export insights operation.

### [ExportIssueModelMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExportIssueModelMetadata)

Metadata used for export issue model.

### [ExportIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExportIssueModelRequest)

Request to export an issue model.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportIssueModelResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ExportIssueModelResponse)

Response from export issue model

### [FaqAnswerData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.FaqAnswerData)

Agent Assist frequently-asked-question answer data.

### [FeedbackLabel](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.FeedbackLabel)

Represents a conversation, resource, and label provided by the user.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GcsSource)

A Cloud Storage source of conversation data.

### [GetAnalysisRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetAnalysisRequest)

The request to get an analysis.

### [GetAnalysisRuleRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetAnalysisRuleRequest)

The request for getting a analysis rule.

### [GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetConversationRequest)

The request to get a conversation.

### [GetEncryptionSpecRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetEncryptionSpecRequest)

The request to get location-level encryption specification.

### [GetFeedbackLabelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetFeedbackLabelRequest)

The request for getting a feedback label.

### [GetIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetIssueModelRequest)

The request to get an issue model.

### [GetIssueRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetIssueRequest)

The request to get an issue.

### [GetPhraseMatcherRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetPhraseMatcherRequest)

The request to get a a phrase matcher.

### [GetQaQuestionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetQaQuestionRequest)

The request for a QaQuestion.

### [GetQaScorecardRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetQaScorecardRequest)

The request for a QaScorecard. By default, returns the latest revision.

### [GetQaScorecardRevisionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetQaScorecardRevisionRequest)

The request for a QaScorecardRevision.

### [GetSettingsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetSettingsRequest)

The request to get project-level settings.

### [GetViewRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.GetViewRequest)

The request to get a view.

### [HoldData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.HoldData)

The data for a hold annotation.

### [ImportIssueModelMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ImportIssueModelMetadata)

Metadata used for import issue model.

### [ImportIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ImportIssueModelRequest)

Request to import an issue model.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportIssueModelResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ImportIssueModelResponse)

Response from import issue model

### [IngestConversationsMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IngestConversationsMetadata)

The metadata for an IngestConversations operation.

### [IngestConversationsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IngestConversationsRequest)

The request to ingest conversations.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IngestConversationsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IngestConversationsResponse)

The response to an IngestConversations operation.

### [InitializeEncryptionSpecMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.InitializeEncryptionSpecMetadata)

Metadata for initializing a location-level encryption specification.

### [InitializeEncryptionSpecRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.InitializeEncryptionSpecRequest)

The request to initialize a location-level encryption specification.

### [InitializeEncryptionSpecResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.InitializeEncryptionSpecResponse)

The response to initialize a location-level encryption specification.

### [Intent](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Intent)

The data for an intent. Represents a detected intent in the conversation, for example MAKES_PROMISE.

### [IntentMatchData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IntentMatchData)

The data for an intent match. Represents an intent match for a text segment in the conversation. A text segment can be part of a sentence, a complete sentence, or an utterance with multiple sentences.

### [InterruptionData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.InterruptionData)

The data for an interruption annotation.

### [Issue](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Issue)

The issue resource.

### [IssueAssignment](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IssueAssignment)

Information about the issue.

### [IssueMatchData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IssueMatchData)

The data for an issue match annotation.

### [IssueModel](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IssueModel)

The issue model resource.

### [IssueModelLabelStats](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IssueModelLabelStats)

Aggregated statistics about an issue model.

### [IssueModelResult](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IssueModelResult)

Issue Modeling result on a conversation.

### [ListAllFeedbackLabelsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsRequest)

The request for listing all feedback labels.

### [ListAllFeedbackLabelsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsResponse)

The response for listing all feedback labels.

### [ListAnalysesRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListAnalysesRequest)

The request to list analyses.

### [ListAnalysesResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListAnalysesResponse)

The response to list analyses.

### [ListAnalysisRulesRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListAnalysisRulesRequest)

The request to list analysis rules.

### [ListAnalysisRulesResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListAnalysisRulesResponse)

The response of listing views.

### [ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListConversationsRequest)

Request to list conversations.

### [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListConversationsResponse)

The response of listing conversations.

### [ListFeedbackLabelsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsRequest)

The request for listing feedback labels.

### [ListFeedbackLabelsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsResponse)

The response for listing feedback labels.

### [ListIssueModelsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListIssueModelsRequest)

Request to list issue models.

### [ListIssueModelsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListIssueModelsResponse)

The response of listing issue models.

### [ListIssuesRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListIssuesRequest)

Request to list issues.

### [ListIssuesResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListIssuesResponse)

The response of listing issues.

### [ListPhraseMatchersRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListPhraseMatchersRequest)

Request to list phrase matchers.

### [ListPhraseMatchersResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListPhraseMatchersResponse)

The response of listing phrase matchers.

### [ListQaQuestionsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListQaQuestionsRequest)

Request to list QaQuestions.

### [ListQaQuestionsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListQaQuestionsResponse)

The response from a ListQaQuestions request.

### [ListQaScorecardRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsRequest)

Request to list QaScorecardRevisions

### [ListQaScorecardRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsResponse)

The response from a ListQaScorecardRevisions request.

### [ListQaScorecardsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListQaScorecardsRequest)

Request to list QaScorecards.

### [ListQaScorecardsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListQaScorecardsResponse)

The response from a ListQaScorecards request.

### [ListViewsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListViewsRequest)

The request to list views.

### [ListViewsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.ListViewsResponse)

The response of listing views.

### [PhraseMatchData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.PhraseMatchData)

The data for a matched phrase matcher. Represents information identifying a phrase matcher for a given match.

### [PhraseMatchRule](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.PhraseMatchRule)

The data for a phrase match rule.

### [PhraseMatchRuleConfig](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.PhraseMatchRuleConfig)

Configuration information of a phrase match rule.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PhraseMatchRuleGroup](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.PhraseMatchRuleGroup)

A message representing a rule in the phrase matcher.

### [PhraseMatcher](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.PhraseMatcher)

The phrase matcher resource.

### [QaAnswer](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QaAnswer)

An answer to a QaQuestion.

### [QaQuestion](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QaQuestion)

A single question to be scored by the Insights QA feature.

### [QaScorecard](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QaScorecard)

A QaScorecard represents a collection of questions to be scored during analysis.

### [QaScorecardResult](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QaScorecardResult)

The results of scoring a single conversation against a QaScorecard. Contains a collection of QaAnswers and aggregate score.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QaScorecardRevision](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QaScorecardRevision)

A revision of a QaScorecard.

Modifying published scorecard fields would invalidate existing scorecard results — the questions may have changed, or the score weighting will make existing scores impossible to understand. So changes must create a new revision, rather than modifying the existing resource.

### [QueryMetricsMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QueryMetricsMetadata)

The metadata from querying metrics.

### [QueryMetricsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QueryMetricsRequest)

The request for querying metrics.

### [QueryMetricsResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.QueryMetricsResponse)

The response for querying metrics.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RedactionConfig](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.RedactionConfig)

DLP resources used for redaction while ingesting conversations. DLP settings are applied to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversation coming from CCAI Platform. They are not applied to conversations ingested from the `CreateConversation` endpoint or the Dialogflow / Agent Assist runtime integrations. When using Dialogflow / Agent Assist runtime integrations, redaction should be performed in Dialogflow / Agent Assist.

### [RuntimeAnnotation](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.RuntimeAnnotation)

An annotation that was generated during the customer and agent interaction.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SentimentData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.SentimentData)

The data for a sentiment annotation.

### [Settings](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.Settings)

The CCAI Insights project wide settings. Use these settings to configure the behavior of Insights. View these settings with `getsettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/getSettings>`__ and change the settings with`updateSettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/updateSettings>`__.

### [SilenceData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.SilenceData)

The data for a silence annotation.

### [SmartComposeSuggestionData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.SmartComposeSuggestionData)

Agent Assist Smart Compose suggestion data.

### [SmartReplyData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.SmartReplyData)

Agent Assist Smart Reply data.

### [SpeechConfig](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.SpeechConfig)

Speech-to-Text configuration. Speech-to-Text settings are applied to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversation coming from CCAI Platform. They are not applied to conversations ingested from the `CreateConversation` endpoint.

### [TuneQaScorecardRevisionMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionMetadata)

Metadata for TuneQaScorecardRevision endpoint.

### [TuneQaScorecardRevisionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionRequest)

Request for TuneQaScorecardRevision endpoint.

### [TuneQaScorecardRevisionResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionResponse)

Response for TuneQaScorecardRevision endpoint.

### [UndeployIssueModelMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UndeployIssueModelMetadata)

Metadata for undeploying an issue model.

### [UndeployIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UndeployIssueModelRequest)

The request to undeploy an issue model.

### [UndeployIssueModelResponse](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UndeployIssueModelResponse)

The response to undeploy an issue model.

### [UndeployQaScorecardRevisionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UndeployQaScorecardRevisionRequest)

The request to undeploy a QaScorecardRevision

### [UpdateAnalysisRuleRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateAnalysisRuleRequest)

The request to update a analysis rule.

### [UpdateConversationRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateConversationRequest)

The request to update a conversation.

### [UpdateFeedbackLabelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateFeedbackLabelRequest)

The request for updating a feedback label.

### [UpdateIssueModelRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateIssueModelRequest)

The request to update an issue model.

### [UpdateIssueRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateIssueRequest)

The request to update an issue.

### [UpdatePhraseMatcherRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdatePhraseMatcherRequest)

The request to update a phrase matcher.

### [UpdateQaQuestionRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateQaQuestionRequest)

The request for updating a QaQuestion.

### [UpdateQaScorecardRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateQaScorecardRequest)

The request for updating a QaScorecard.

### [UpdateSettingsRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateSettingsRequest)

The request to update project-level settings.

### [UpdateViewRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UpdateViewRequest)

The request to update a view.

### [UploadConversationMetadata](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UploadConversationMetadata)

The metadata for an `UploadConversation` operation.

### [UploadConversationRequest](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.UploadConversationRequest)

Request to upload a conversation.

### [View](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.View)

The View resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
