---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/
title: Contact Center AI Insights API \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:56.776526+00:00
---

# Contact Center AI Insights API  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Contact Center AI Insights API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1alpha1.projects.locations
  * REST Resource: v1alpha1.projects.locations.analysisRules
  * REST Resource: v1alpha1.projects.locations.assessmentRules
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets.authorizedViews
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.analyses
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels
  * REST Resource: v1alpha1.projects.locations.authorizedViewSets.authorizedViews.operations
  * REST Resource: v1alpha1.projects.locations.conversations
  * REST Resource: v1alpha1.projects.locations.conversations.analyses
  * REST Resource: v1alpha1.projects.locations.conversations.assessments
  * REST Resource: v1alpha1.projects.locations.conversations.assessments.notes
  * REST Resource: v1alpha1.projects.locations.conversations.feedbackLabels
  * REST Resource: v1alpha1.projects.locations.datasets
  * REST Resource: v1alpha1.projects.locations.datasets.conversations
  * REST Resource: v1alpha1.projects.locations.datasets.conversations.analyses
  * REST Resource: v1alpha1.projects.locations.datasets.conversations.feedbackLabels
  * REST Resource: v1alpha1.projects.locations.datasets.insightsdata
  * REST Resource: v1alpha1.projects.locations.encryptionSpec
  * REST Resource: v1alpha1.projects.locations.insightsdata
  * REST Resource: v1alpha1.projects.locations.issueModels
  * REST Resource: v1alpha1.projects.locations.issueModels.issues
  * REST Resource: v1alpha1.projects.locations.operations
  * REST Resource: v1alpha1.projects.locations.phraseMatchers
  * REST Resource: v1alpha1.projects.locations.qaQuestionTags
  * REST Resource: v1alpha1.projects.locations.qaScorecards
  * REST Resource: v1alpha1.projects.locations.qaScorecards.revisions
  * REST Resource: v1alpha1.projects.locations.qaScorecards.revisions.qaQuestions
  * REST Resource: v1alpha1.projects.locations.views
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.analysisRules
  * REST Resource: v1.projects.locations.assessmentRules
  * REST Resource: v1.projects.locations.authorizedViewSets
  * REST Resource: v1.projects.locations.authorizedViewSets.authorizedViews
  * REST Resource: v1.projects.locations.authorizedViewSets.authorizedViews.conversations
  * REST Resource: v1.projects.locations.authorizedViewSets.authorizedViews.conversations.analyses
  * REST Resource: v1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments
  * REST Resource: v1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes
  * REST Resource: v1.projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels
  * REST Resource: v1.projects.locations.authorizedViewSets.authorizedViews.operations
  * REST Resource: v1.projects.locations.conversations
  * REST Resource: v1.projects.locations.conversations.analyses
  * REST Resource: v1.projects.locations.conversations.assessments
  * REST Resource: v1.projects.locations.conversations.assessments.notes
  * REST Resource: v1.projects.locations.conversations.feedbackLabels
  * REST Resource: v1.projects.locations.datasets
  * REST Resource: v1.projects.locations.datasets.conversations
  * REST Resource: v1.projects.locations.datasets.conversations.analyses
  * REST Resource: v1.projects.locations.datasets.conversations.feedbackLabels
  * REST Resource: v1.projects.locations.datasets.insightsdata
  * REST Resource: v1.projects.locations.encryptionSpec
  * REST Resource: v1.projects.locations.insightsdata
  * REST Resource: v1.projects.locations.issueModels
  * REST Resource: v1.projects.locations.issueModels.issues
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.phraseMatchers
  * REST Resource: v1.projects.locations.qaQuestionTags
  * REST Resource: v1.projects.locations.qaScorecards
  * REST Resource: v1.projects.locations.qaScorecards.revisions
  * REST Resource: v1.projects.locations.qaScorecards.revisions.qaQuestions
  * REST Resource: v1.projects.locations.views



## Service: contactcenterinsights.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://contactcenterinsights.googleapis.com/$discovery/rest?version=v1>
  * <https://contactcenterinsights.googleapis.com/$discovery/rest?version=v1alpha1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoints and all URIs below are relative to these service endpoints:

  * `https://contactcenterinsights.googleapis.com`
  * `https://asia-northeast1-contactcenterinsights.googleapis.com`
  * `https://asia-northeast3-contactcenterinsights.googleapis.com`
  * `https://asia-south1-contactcenterinsights.googleapis.com`
  * `https://asia-southeast1-contactcenterinsights.googleapis.com`
  * `https://asia-southeast2-contactcenterinsights.googleapis.com`
  * `https://australia-southeast1-contactcenterinsights.googleapis.com`
  * `https://europe-west1-contactcenterinsights.googleapis.com`
  * `https://europe-west2-contactcenterinsights.googleapis.com`
  * `https://europe-west3-contactcenterinsights.googleapis.com`
  * `https://europe-west4-contactcenterinsights.googleapis.com`
  * `https://europe-west6-contactcenterinsights.googleapis.com`
  * `https://me-west1-contactcenterinsights.googleapis.com`
  * `https://northamerica-northeast1-contactcenterinsights.googleapis.com`
  * `https://northamerica-northeast2-contactcenterinsights.googleapis.com`
  * `https://us-east1-contactcenterinsights.googleapis.com`
  * `https://us-east7-contactcenterinsights.googleapis.com`
  * `https://us-west1-contactcenterinsights.googleapis.com`



## REST Resource: [v1alpha1.projects.locations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations)

Methods  
---  
`[bulkDeleteFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/bulkDeleteFeedbackLabels)` |  `POST /v1alpha1/{parent=projects/*/locations/*}:bulkDeleteFeedbackLabels`   
Delete feedback labels in bulk using a filter.  
`[bulkDownloadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/bulkDownloadFeedbackLabels)` |  `POST /v1alpha1/{parent=projects/*/locations/*}:bulkDownloadFeedbackLabels`   
Download feedback labels in bulk from an external source.  
`[bulkUploadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/bulkUploadFeedbackLabels)` |  `POST /v1alpha1/{parent=projects/*/locations/*}:bulkUploadFeedbackLabels`   
Upload feedback labels from an external source in bulk.  
`[getEncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/getEncryptionSpec)` |  `GET /v1alpha1/{name=projects/*/locations/*/encryptionSpec}`   
Gets location-level encryption key specification.  
`[getSettings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/getSettings)` |  `GET /v1alpha1/{name=projects/*/locations/*/settings}`   
Gets project-level settings.  
`[listAllFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/listAllFeedbackLabels)` |  `GET /v1alpha1/{parent=projects/*/locations/*}:listAllFeedbackLabels`   
List all feedback labels by project number.  
`[queryMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/queryMetrics)` |  `POST /v1alpha1/{location=projects/*/locations/*}:queryMetrics`   
Query metrics.  
`[queryPerformanceOverview](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/queryPerformanceOverview)` |  `POST /v1alpha1/{parent=projects/*/locations/*}:queryPerformanceOverview`   
Generates a summary of predefined performance metrics for a set of conversations.  
`[updateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/updateSettings)` |  `PATCH /v1alpha1/{settings.name=projects/*/locations/*/settings}`   
Updates project-level settings.  
  
## REST Resource: [v1alpha1.projects.locations.analysisRules](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.analysisRules)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.analysisRules/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/analysisRules`   
Creates a analysis rule.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.analysisRules/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/analysisRules/*}`   
Deletes a analysis rule.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.analysisRules/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/analysisRules/*}`   
Get a analysis rule.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.analysisRules/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/analysisRules`   
Lists analysis rules.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.analysisRules/patch)` |  `PATCH /v1alpha1/{analysisRule.name=projects/*/locations/*/analysisRules/*}`   
Updates a analysis rule.  
  
## REST Resource: [v1alpha1.projects.locations.assessmentRules](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.assessmentRules)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.assessmentRules/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/assessmentRules`   
Creates an assessment rule.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.assessmentRules/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/assessmentRules/*}`   
Deletes an assessment rule.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.assessmentRules/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/assessmentRules/*}`   
Get an assessment rule.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.assessmentRules/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/assessmentRules`   
Lists assessment rules.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.assessmentRules/patch)` |  `PATCH /v1alpha1/{assessmentRule.name=projects/*/locations/*/assessmentRules/*}`   
Updates an assessment rule.  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/authorizedViewSets`   
Create AuthorizedViewSet  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*}`   
Deletes an AuthorizedViewSet.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*}`   
Get AuthorizedViewSet  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/authorizedViewSets`   
List AuthorizedViewSets  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets/patch)` |  `PATCH /v1alpha1/{authorizedViewSet.name=projects/*/locations/*/authorizedViewSets/*}`   
Updates an AuthorizedViewSet.  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets.authorizedViews](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*}/authorizedViews`   
Create AuthorizedView  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}`   
Deletes an AuthorizedView.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}`   
Get AuthorizedView  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*}/authorizedViews`   
List AuthorizedViewSets  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/patch)` |  `PATCH /v1alpha1/{authorizedView.name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}`   
Updates an AuthorizedView.  
`[queryMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/queryMetrics)` |  `POST /v1alpha1/{location=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}:queryMetrics`   
Query metrics.  
`[queryPerformanceOverview](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/queryPerformanceOverview)` |  `POST /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}:queryPerformanceOverview`   
Generates a summary of predefined performance metrics for a set of conversations.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews/search)` |  `GET /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*}/authorizedViews:search`   
SearchAuthorizedViewSets  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations)

Methods  
---  
`[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/bulkAnalyze)` |  `POST /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/conversations:bulkAnalyze`   
Analyzes multiple conversations in a single request.  
`[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/calculateStats)` |  `GET /v1alpha1/{location=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/conversations:calculateStats`   
Gets conversation statistics.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}`   
Gets a conversation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/conversations`   
Lists conversations.  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.analyses](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/analyses`   
Creates an analysis.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/analyses/*}`   
Deletes an analysis.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/analyses/*}`   
Gets an analysis.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/analyses`   
Lists analyses.  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments)

Methods  
---  
`[appeal](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/appeal)` |  `POST /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}:appeal`   
Appeal an Assessment.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/assessments`   
Create Assessment.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}`   
Delete an Assessment.  
`[finalize](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/finalize)` |  `POST /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}:finalize`   
Finalize an Assessment.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}`   
Get Assessment.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/assessments`   
List Assessments.  
`[publish](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/publish)` |  `POST /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}:publish`   
Publish an Assessment.  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}/notes`   
Create Note.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*/notes/*}`   
Deletes a Note.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}/notes`   
List Notes.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/patch)` |  `PATCH /v1alpha1/{note.name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*/notes/*}`   
Update Note.  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/feedbackLabels`   
Create feedback label.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/feedbackLabels/*}`   
Delete feedback label.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/feedbackLabels/*}`   
Get feedback label.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/feedbackLabels`   
List feedback labels.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/patch)` |  `PATCH /v1alpha1/{feedbackLabel.name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/feedbackLabels/*}`   
Update feedback label.  
  
## REST Resource: [v1alpha1.projects.locations.authorizedViewSets.authorizedViews.operations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.operations/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.operations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.operations/list)` |  `GET /v1alpha1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha1.projects.locations.conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations)

Methods  
---  
`[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/bulkAnalyze)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/conversations:bulkAnalyze`   
Analyzes multiple conversations in a single request.  
`[bulkDelete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/bulkDelete)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/conversations:bulkDelete`   
Deletes multiple conversations in a single request.  
`[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/calculateStats)` |  `GET /v1alpha1/{location=projects/*/locations/*}/conversations:calculateStats`   
Gets conversation statistics.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/conversations`   
Creates a conversation.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/conversations/*}`   
Gets a conversation.  
`[ingest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/ingest)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/conversations:ingest`   
Imports conversations and processes them according to the user's configuration.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/conversations`   
Lists conversations.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/patch)` |  `PATCH /v1alpha1/{conversation.name=projects/*/locations/*/conversations/*}`   
Updates a conversation.  
`[upload](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/upload)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/conversations:upload`   
Create a long-running conversation upload operation.  
  
## REST Resource: [v1alpha1.projects.locations.conversations.analyses](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.analyses)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.analyses/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/conversations/*}/analyses`   
Creates an analysis.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.analyses/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/conversations/*/analyses/*}`   
Deletes an analysis.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.analyses/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/conversations/*/analyses/*}`   
Gets an analysis.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.analyses/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/conversations/*}/analyses`   
Lists analyses.  
  
## REST Resource: [v1alpha1.projects.locations.conversations.assessments](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments)

Methods  
---  
`[appeal](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments/appeal)` |  `POST /v1alpha1/{name=projects/*/locations/*/conversations/*/assessments/*}:appeal`   
Appeal an Assessment.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/conversations/*}/assessments`   
Create Assessment.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/conversations/*/assessments/*}`   
Delete an Assessment.  
`[finalize](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments/finalize)` |  `POST /v1alpha1/{name=projects/*/locations/*/conversations/*/assessments/*}:finalize`   
Finalize an Assessment.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/conversations/*/assessments/*}`   
Get Assessment.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/conversations/*}/assessments`   
List Assessments.  
`[publish](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments/publish)` |  `POST /v1alpha1/{name=projects/*/locations/*/conversations/*/assessments/*}:publish`   
Publish an Assessment.  
  
## REST Resource: [v1alpha1.projects.locations.conversations.assessments.notes](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments.notes)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments.notes/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/conversations/*/assessments/*}/notes`   
Create Note.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments.notes/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/conversations/*/assessments/*/notes/*}`   
Deletes a Note.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments.notes/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/conversations/*/assessments/*}/notes`   
List Notes.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.assessments.notes/patch)` |  `PATCH /v1alpha1/{note.name=projects/*/locations/*/conversations/*/assessments/*/notes/*}`   
Update Note.  
  
## REST Resource: [v1alpha1.projects.locations.conversations.feedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/conversations/*}/feedbackLabels`   
Create feedback label.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/conversations/*/feedbackLabels/*}`   
Delete feedback label.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/conversations/*/feedbackLabels/*}`   
Get feedback label.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/conversations/*}/feedbackLabels`   
List feedback labels.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/patch)` |  `PATCH /v1alpha1/{feedbackLabel.name=projects/*/locations/*/conversations/*/feedbackLabels/*}`   
Update feedback label.  
  
## REST Resource: [v1alpha1.projects.locations.datasets](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets)

Methods  
---  
`[bulkDeleteFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkDeleteFeedbackLabels)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*}:bulkDeleteFeedbackLabels`   
Delete feedback labels in bulk using a filter.  
`[bulkDownloadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkDownloadFeedbackLabels)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*}:bulkDownloadFeedbackLabels`   
Download feedback labels in bulk from an external source.  
`[bulkUploadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkUploadFeedbackLabels)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*}:bulkUploadFeedbackLabels`   
Upload feedback labels from an external source in bulk.  
`[listAllFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/listAllFeedbackLabels)` |  `GET /v1alpha1/{parent=projects/*/locations/*/datasets/*}:listAllFeedbackLabels`   
List all feedback labels by project number.  
  
## REST Resource: [v1alpha1.projects.locations.datasets.conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations)

Methods  
---  
`[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations/bulkAnalyze)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*}/conversations:bulkAnalyze`   
Analyzes multiple conversations in a single request.  
`[bulkDelete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations/bulkDelete)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*}/conversations:bulkDelete`   
Deletes multiple conversations in a single request.  
`[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations/calculateStats)` |  `POST /v1alpha1/{location=projects/*/locations/*/datasets/*}/conversations:calculateStats`   
Gets conversation statistics.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/datasets/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/datasets/*/conversations/*}`   
Gets a conversation.  
`[ingest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations/ingest)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*}/conversations:ingest`   
Imports conversations and processes them according to the user's configuration.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/datasets/*}/conversations`   
Lists conversations.  
  
## REST Resource: [v1alpha1.projects.locations.datasets.conversations.analyses](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.analyses)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.analyses/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*/conversations/*}/analyses`   
Creates an analysis.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.analyses/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/datasets/*/conversations/*/analyses/*}`   
Deletes an analysis.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.analyses/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/datasets/*/conversations/*/analyses/*}`   
Gets an analysis.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.analyses/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/datasets/*/conversations/*}/analyses`   
Lists analyses.  
  
## REST Resource: [v1alpha1.projects.locations.datasets.conversations.feedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.feedbackLabels)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.feedbackLabels/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*/conversations/*}/feedbackLabels`   
Create feedback label.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.feedbackLabels/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/datasets/*/conversations/*/feedbackLabels/*}`   
Delete feedback label.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.feedbackLabels/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/datasets/*/conversations/*/feedbackLabels/*}`   
Get feedback label.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.feedbackLabels/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/datasets/*/conversations/*}/feedbackLabels`   
List feedback labels.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.conversations.feedbackLabels/patch)` |  `PATCH /v1alpha1/{feedbackLabel.name=projects/*/locations/*/datasets/*/conversations/*/feedbackLabels/*}`   
Update feedback label.  
  
## REST Resource: [v1alpha1.projects.locations.datasets.insightsdata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.insightsdata)

Methods  
---  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets.insightsdata/export)` |  `POST /v1alpha1/{parent=projects/*/locations/*/datasets/*}/insightsdata:export`   
Export insights data to a destination defined in the request body.  
  
## REST Resource: [v1alpha1.projects.locations.encryptionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.encryptionSpec)

Methods  
---  
`[initialize](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.encryptionSpec/initialize)` |  `POST /v1alpha1/{encryptionSpec.name=projects/*/locations/*/encryptionSpec}:initialize`   
Initializes a location-level encryption key specification.  
  
## REST Resource: [v1alpha1.projects.locations.insightsdata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.insightsdata)

Methods  
---  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.insightsdata/export)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/insightsdata:export`   
Export insights data to a destination defined in the request body.  
  
## REST Resource: [v1alpha1.projects.locations.issueModels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels)

Methods  
---  
`[calculateIssueModelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/calculateIssueModelStats)` |  `GET /v1alpha1/{issueModel=projects/*/locations/*/issueModels/*}:calculateIssueModelStats`   
Gets an issue model's statistics.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/issueModels`   
Creates an issue model.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/issueModels/*}`   
Deletes an issue model.  
`[deploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/deploy)` |  `POST /v1alpha1/{name=projects/*/locations/*/issueModels/*}:deploy`   
Deploys an issue model.  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/export)` |  `POST /v1alpha1/{name=projects/*/locations/*/issueModels/*}:export`   
Exports an issue model to the provided destination.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/issueModels/*}`   
Gets an issue model.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/import)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/issueModels:import`   
Imports an issue model from a Cloud Storage bucket.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/issueModels`   
Lists issue models.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/patch)` |  `PATCH /v1alpha1/{issueModel.name=projects/*/locations/*/issueModels/*}`   
Updates an issue model.  
`[undeploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels/undeploy)` |  `POST /v1alpha1/{name=projects/*/locations/*/issueModels/*}:undeploy`   
Undeploys an issue model.  
  
## REST Resource: [v1alpha1.projects.locations.issueModels.issues](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels.issues)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels.issues/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/issueModels/*}/issues`   
Creates an issue.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels.issues/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/issueModels/*/issues/*}`   
Deletes an issue.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels.issues/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/issueModels/*/issues/*}`   
Gets an issue.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels.issues/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/issueModels/*}/issues`   
Lists issues.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels.issues/patch)` |  `PATCH /v1alpha1/{issue.name=projects/*/locations/*/issueModels/*/issues/*}`   
Updates an issue.  
  
## REST Resource: [v1alpha1.projects.locations.operations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.operations/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.operations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.operations/list)` |  `GET /v1alpha1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha1.projects.locations.phraseMatchers](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.phraseMatchers)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.phraseMatchers/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/phraseMatchers`   
Creates a phrase matcher.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.phraseMatchers/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/phraseMatchers/*}`   
Deletes a phrase matcher.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.phraseMatchers/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/phraseMatchers/*}`   
Gets a phrase matcher.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.phraseMatchers/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/phraseMatchers`   
Lists phrase matchers.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.phraseMatchers/patch)` |  `PATCH /v1alpha1/{phraseMatcher.name=projects/*/locations/*/phraseMatchers/*}`   
Updates a phrase matcher.  
  
## REST Resource: [v1alpha1.projects.locations.qaQuestionTags](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaQuestionTags)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaQuestionTags/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/qaQuestionTags`   
Creates a QaQuestionTag.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaQuestionTags/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/qaQuestionTags/*}`   
Deletes a QaQuestionTag.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaQuestionTags/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/qaQuestionTags/*}`   
Gets a QaQuestionTag.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaQuestionTags/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/qaQuestionTags`   
Lists the question tags.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaQuestionTags/patch)` |  `PATCH /v1alpha1/{qaQuestionTag.name=projects/*/locations/*/qaQuestionTags/*}`   
Updates a QaQuestionTag.  
  
## REST Resource: [v1alpha1.projects.locations.qaScorecards](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/qaScorecards`   
Create a QaScorecard.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/qaScorecards/*}`   
Deletes a QaScorecard.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/qaScorecards/*}`   
Gets a QaScorecard.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/qaScorecards`   
Lists QaScorecards.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards/patch)` |  `PATCH /v1alpha1/{qaScorecard.name=projects/*/locations/*/qaScorecards/*}`   
Updates a QaScorecard.  
  
## REST Resource: [v1alpha1.projects.locations.qaScorecards.revisions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/qaScorecards/*}/revisions`   
Creates a QaScorecardRevision.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}`   
Deletes a QaScorecardRevision.  
`[deploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/deploy)` |  `POST /v1alpha1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}:deploy`   
Deploy a QaScorecardRevision.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}`   
Gets a QaScorecardRevision.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/qaScorecards/*}/revisions`   
Lists all revisions under the parent QaScorecard.  
`[tuneQaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/tuneQaScorecardRevision)` |  `POST /v1alpha1/{parent=projects/*/locations/*/qaScorecards/*/revisions/*}:tuneQaScorecardRevision`   
Fine tune one or more QaModels.  
`[undeploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions/undeploy)` |  `POST /v1alpha1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}:undeploy`   
Undeploy a QaScorecardRevision.  
  
## REST Resource: [v1alpha1.projects.locations.qaScorecards.revisions.qaQuestions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions.qaQuestions)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions.qaQuestions/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/qaScorecards/*/revisions/*}/qaQuestions`   
Create a QaQuestion.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions.qaQuestions/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/qaScorecards/*/revisions/*/qaQuestions/*}`   
Deletes a QaQuestion.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions.qaQuestions/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/qaScorecards/*/revisions/*/qaQuestions/*}`   
Gets a QaQuestion.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions.qaQuestions/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/qaScorecards/*/revisions/*}/qaQuestions`   
Lists QaQuestions.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions.qaQuestions/patch)` |  `PATCH /v1alpha1/{qaQuestion.name=projects/*/locations/*/qaScorecards/*/revisions/*/qaQuestions/*}`   
Updates a QaQuestion.  
  
## REST Resource: [v1alpha1.projects.locations.views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.views)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.views/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/views`   
Creates a view.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.views/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/views/*}`   
Deletes a view.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.views/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/views/*}`   
Gets a view.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.views/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/views`   
Lists views.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.views/patch)` |  `PATCH /v1alpha1/{view.name=projects/*/locations/*/views/*}`   
Updates a view.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations)

Methods  
---  
`[bulkDeleteFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/bulkDeleteFeedbackLabels)` |  `POST /v1/{parent=projects/*/locations/*}:bulkDeleteFeedbackLabels`   
Delete feedback labels in bulk using a filter.  
`[bulkDownloadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/bulkDownloadFeedbackLabels)` |  `POST /v1/{parent=projects/*/locations/*}:bulkDownloadFeedbackLabels`   
Download feedback labels in bulk from an external source.  
`[bulkUploadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/bulkUploadFeedbackLabels)` |  `POST /v1/{parent=projects/*/locations/*}:bulkUploadFeedbackLabels`   
Upload feedback labels from an external source in bulk.  
`[getEncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/getEncryptionSpec)` |  `GET /v1/{name=projects/*/locations/*/encryptionSpec}`   
Gets location-level encryption key specification.  
`[getSettings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/getSettings)` |  `GET /v1/{name=projects/*/locations/*/settings}`   
Gets project-level settings.  
`[listAllFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/listAllFeedbackLabels)` |  `GET /v1/{parent=projects/*/locations/*}:listAllFeedbackLabels`   
List all feedback labels by project number.  
`[queryMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/queryMetrics)` |  `POST /v1/{location=projects/*/locations/*}:queryMetrics`   
Query metrics.  
`[queryPerformanceOverview](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/queryPerformanceOverview)` |  `POST /v1/{parent=projects/*/locations/*}:queryPerformanceOverview`   
Generates a summary of predefined performance metrics for a set of conversations.  
`[updateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/updateSettings)` |  `PATCH /v1/{settings.name=projects/*/locations/*/settings}`   
Updates project-level settings.  
  
## REST Resource: [v1.projects.locations.analysisRules](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/create)` |  `POST /v1/{parent=projects/*/locations/*}/analysisRules`   
Creates a analysis rule.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/delete)` |  `DELETE /v1/{name=projects/*/locations/*/analysisRules/*}`   
Deletes a analysis rule.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/get)` |  `GET /v1/{name=projects/*/locations/*/analysisRules/*}`   
Get a analysis rule.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/list)` |  `GET /v1/{parent=projects/*/locations/*}/analysisRules`   
Lists analysis rules.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/patch)` |  `PATCH /v1/{analysisRule.name=projects/*/locations/*/analysisRules/*}`   
Updates a analysis rule.  
  
## REST Resource: [v1.projects.locations.assessmentRules](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/create)` |  `POST /v1/{parent=projects/*/locations/*}/assessmentRules`   
Creates an assessment rule.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/delete)` |  `DELETE /v1/{name=projects/*/locations/*/assessmentRules/*}`   
Deletes an assessment rule.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/get)` |  `GET /v1/{name=projects/*/locations/*/assessmentRules/*}`   
Get an assessment rule.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/list)` |  `GET /v1/{parent=projects/*/locations/*}/assessmentRules`   
Lists assessment rules.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.assessmentRules/patch)` |  `PATCH /v1/{assessmentRule.name=projects/*/locations/*/assessmentRules/*}`   
Updates an assessment rule.  
  
## REST Resource: [v1.projects.locations.authorizedViewSets](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets/create)` |  `POST /v1/{parent=projects/*/locations/*}/authorizedViewSets`   
Create AuthorizedViewSet  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizedViewSets/*}`   
Deletes an AuthorizedViewSet.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets/get)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*}`   
Get AuthorizedViewSet  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets/list)` |  `GET /v1/{parent=projects/*/locations/*}/authorizedViewSets`   
List AuthorizedViewSets  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets/patch)` |  `PATCH /v1/{authorizedViewSet.name=projects/*/locations/*/authorizedViewSets/*}`   
Updates an AuthorizedViewSet.  
  
## REST Resource: [v1.projects.locations.authorizedViewSets.authorizedViews](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/create)` |  `POST /v1/{parent=projects/*/locations/*/authorizedViewSets/*}/authorizedViews`   
Create AuthorizedView  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}`   
Deletes an AuthorizedView.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/get)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}`   
Get AuthorizedView  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/list)` |  `GET /v1/{parent=projects/*/locations/*/authorizedViewSets/*}/authorizedViews`   
List AuthorizedViewSets  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/patch)` |  `PATCH /v1/{authorizedView.name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}`   
Updates an AuthorizedView.  
`[queryMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/queryMetrics)` |  `POST /v1/{location=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}:queryMetrics`   
Query metrics.  
`[queryPerformanceOverview](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/queryPerformanceOverview)` |  `POST /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}:queryPerformanceOverview`   
Generates a summary of predefined performance metrics for a set of conversations.  
`[search](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/search)` |  `GET /v1/{parent=projects/*/locations/*/authorizedViewSets/*}/authorizedViews:search`   
SearchAuthorizedViewSets  
  
## REST Resource: [v1.projects.locations.authorizedViewSets.authorizedViews.conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations)

Methods  
---  
`[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations/bulkAnalyze)` |  `POST /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/conversations:bulkAnalyze`   
Analyzes multiple conversations in a single request.  
`[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations/calculateStats)` |  `GET /v1/{location=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/conversations:calculateStats`   
Gets conversation statistics.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations/get)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}`   
Gets a conversation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations/list)` |  `GET /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/conversations`   
Lists conversations.  
  
## REST Resource: [v1.projects.locations.authorizedViewSets.authorizedViews.conversations.analyses](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/create)` |  `POST /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/analyses`   
Creates an analysis.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/analyses/*}`   
Deletes an analysis.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/get)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/analyses/*}`   
Gets an analysis.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses/list)` |  `GET /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/analyses`   
Lists analyses.  
  
## REST Resource: [v1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments)

Methods  
---  
`[appeal](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/appeal)` |  `POST /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}:appeal`   
Appeal an Assessment.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/create)` |  `POST /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/assessments`   
Create Assessment.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}`   
Delete an Assessment.  
`[finalize](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/finalize)` |  `POST /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}:finalize`   
Finalize an Assessment.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/get)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}`   
Get Assessment.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/list)` |  `GET /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/assessments`   
List Assessments.  
`[publish](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments/publish)` |  `POST /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}:publish`   
Publish an Assessment.  
  
## REST Resource: [v1.projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/create)` |  `POST /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}/notes`   
Create Note.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*/notes/*}`   
Deletes a Note.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/list)` |  `GET /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*}/notes`   
List Notes.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes/patch)` |  `PATCH /v1/{note.name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/assessments/*/notes/*}`   
Update Note.  
  
## REST Resource: [v1.projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/create)` |  `POST /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/feedbackLabels`   
Create feedback label.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/feedbackLabels/*}`   
Delete feedback label.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/get)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/feedbackLabels/*}`   
Get feedback label.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/list)` |  `GET /v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*}/feedbackLabels`   
List feedback labels.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.feedbackLabels/patch)` |  `PATCH /v1/{feedbackLabel.name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/conversations/*/feedbackLabels/*}`   
Update feedback label.  
  
## REST Resource: [v1.projects.locations.authorizedViewSets.authorizedViews.operations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.operations/get)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.operations/list)` |  `GET /v1/{name=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations)

Methods  
---  
`[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/bulkAnalyze)` |  `POST /v1/{parent=projects/*/locations/*}/conversations:bulkAnalyze`   
Analyzes multiple conversations in a single request.  
`[bulkDelete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/bulkDelete)` |  `POST /v1/{parent=projects/*/locations/*}/conversations:bulkDelete`   
Deletes multiple conversations in a single request.  
`[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/calculateStats)` |  `GET /v1/{location=projects/*/locations/*}/conversations:calculateStats`   
Gets conversation statistics.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/create)` |  `POST /v1/{parent=projects/*/locations/*}/conversations`   
Creates a conversation.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/get)` |  `GET /v1/{name=projects/*/locations/*/conversations/*}`   
Gets a conversation.  
`[ingest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/ingest)` |  `POST /v1/{parent=projects/*/locations/*}/conversations:ingest`   
Imports conversations and processes them according to the user's configuration.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/list)` |  `GET /v1/{parent=projects/*/locations/*}/conversations`   
Lists conversations.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/patch)` |  `PATCH /v1/{conversation.name=projects/*/locations/*/conversations/*}`   
Updates a conversation.  
`[upload](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/upload)` |  `POST /v1/{parent=projects/*/locations/*}/conversations:upload`   
Create a long-running conversation upload operation.  
  
## REST Resource: [v1.projects.locations.conversations.analyses](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses/create)` |  `POST /v1/{parent=projects/*/locations/*/conversations/*}/analyses`   
Creates an analysis.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses/delete)` |  `DELETE /v1/{name=projects/*/locations/*/conversations/*/analyses/*}`   
Deletes an analysis.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses/get)` |  `GET /v1/{name=projects/*/locations/*/conversations/*/analyses/*}`   
Gets an analysis.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses/list)` |  `GET /v1/{parent=projects/*/locations/*/conversations/*}/analyses`   
Lists analyses.  
  
## REST Resource: [v1.projects.locations.conversations.assessments](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments)

Methods  
---  
`[appeal](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments/appeal)` |  `POST /v1/{name=projects/*/locations/*/conversations/*/assessments/*}:appeal`   
Appeal an Assessment.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments/create)` |  `POST /v1/{parent=projects/*/locations/*/conversations/*}/assessments`   
Create Assessment.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/conversations/*/assessments/*}`   
Delete an Assessment.  
`[finalize](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments/finalize)` |  `POST /v1/{name=projects/*/locations/*/conversations/*/assessments/*}:finalize`   
Finalize an Assessment.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments/get)` |  `GET /v1/{name=projects/*/locations/*/conversations/*/assessments/*}`   
Get Assessment.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments/list)` |  `GET /v1/{parent=projects/*/locations/*/conversations/*}/assessments`   
List Assessments.  
`[publish](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments/publish)` |  `POST /v1/{name=projects/*/locations/*/conversations/*/assessments/*}:publish`   
Publish an Assessment.  
  
## REST Resource: [v1.projects.locations.conversations.assessments.notes](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/create)` |  `POST /v1/{parent=projects/*/locations/*/conversations/*/assessments/*}/notes`   
Create Note.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/conversations/*/assessments/*/notes/*}`   
Deletes a Note.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/list)` |  `GET /v1/{parent=projects/*/locations/*/conversations/*/assessments/*}/notes`   
List Notes.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/patch)` |  `PATCH /v1/{note.name=projects/*/locations/*/conversations/*/assessments/*/notes/*}`   
Update Note.  
  
## REST Resource: [v1.projects.locations.conversations.feedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels/create)` |  `POST /v1/{parent=projects/*/locations/*/conversations/*}/feedbackLabels`   
Create feedback label.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels/delete)` |  `DELETE /v1/{name=projects/*/locations/*/conversations/*/feedbackLabels/*}`   
Delete feedback label.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels/get)` |  `GET /v1/{name=projects/*/locations/*/conversations/*/feedbackLabels/*}`   
Get feedback label.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels/list)` |  `GET /v1/{parent=projects/*/locations/*/conversations/*}/feedbackLabels`   
List feedback labels.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels/patch)` |  `PATCH /v1/{feedbackLabel.name=projects/*/locations/*/conversations/*/feedbackLabels/*}`   
Update feedback label.  
  
## REST Resource: [v1.projects.locations.datasets](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets)

Methods  
---  
`[bulkDeleteFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets/bulkDeleteFeedbackLabels)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*}:bulkDeleteFeedbackLabels`   
Delete feedback labels in bulk using a filter.  
`[bulkDownloadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets/bulkDownloadFeedbackLabels)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*}:bulkDownloadFeedbackLabels`   
Download feedback labels in bulk from an external source.  
`[bulkUploadFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets/bulkUploadFeedbackLabels)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*}:bulkUploadFeedbackLabels`   
Upload feedback labels from an external source in bulk.  
`[listAllFeedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets/listAllFeedbackLabels)` |  `GET /v1/{parent=projects/*/locations/*/datasets/*}:listAllFeedbackLabels`   
List all feedback labels by project number.  
  
## REST Resource: [v1.projects.locations.datasets.conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations)

Methods  
---  
`[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations/bulkAnalyze)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*}/conversations:bulkAnalyze`   
Analyzes multiple conversations in a single request.  
`[bulkDelete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations/bulkDelete)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*}/conversations:bulkDelete`   
Deletes multiple conversations in a single request.  
`[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations/calculateStats)` |  `POST /v1/{location=projects/*/locations/*/datasets/*}/conversations:calculateStats`   
Gets conversation statistics.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/datasets/*/conversations/*}`   
Deletes a conversation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations/get)` |  `GET /v1/{name=projects/*/locations/*/datasets/*/conversations/*}`   
Gets a conversation.  
`[ingest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations/ingest)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*}/conversations:ingest`   
Imports conversations and processes them according to the user's configuration.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations/list)` |  `GET /v1/{parent=projects/*/locations/*/datasets/*}/conversations`   
Lists conversations.  
  
## REST Resource: [v1.projects.locations.datasets.conversations.analyses](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.analyses)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.analyses/create)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*/conversations/*}/analyses`   
Creates an analysis.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.analyses/delete)` |  `DELETE /v1/{name=projects/*/locations/*/datasets/*/conversations/*/analyses/*}`   
Deletes an analysis.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.analyses/get)` |  `GET /v1/{name=projects/*/locations/*/datasets/*/conversations/*/analyses/*}`   
Gets an analysis.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.analyses/list)` |  `GET /v1/{parent=projects/*/locations/*/datasets/*/conversations/*}/analyses`   
Lists analyses.  
  
## REST Resource: [v1.projects.locations.datasets.conversations.feedbackLabels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.feedbackLabels)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.feedbackLabels/create)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*/conversations/*}/feedbackLabels`   
Create feedback label.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.feedbackLabels/delete)` |  `DELETE /v1/{name=projects/*/locations/*/datasets/*/conversations/*/feedbackLabels/*}`   
Delete feedback label.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.feedbackLabels/get)` |  `GET /v1/{name=projects/*/locations/*/datasets/*/conversations/*/feedbackLabels/*}`   
Get feedback label.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.feedbackLabels/list)` |  `GET /v1/{parent=projects/*/locations/*/datasets/*/conversations/*}/feedbackLabels`   
List feedback labels.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.conversations.feedbackLabels/patch)` |  `PATCH /v1/{feedbackLabel.name=projects/*/locations/*/datasets/*/conversations/*/feedbackLabels/*}`   
Update feedback label.  
  
## REST Resource: [v1.projects.locations.datasets.insightsdata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.insightsdata)

Methods  
---  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.datasets.insightsdata/export)` |  `POST /v1/{parent=projects/*/locations/*/datasets/*}/insightsdata:export`   
Export insights data to a destination defined in the request body.  
  
## REST Resource: [v1.projects.locations.encryptionSpec](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.encryptionSpec)

Methods  
---  
`[initialize](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.encryptionSpec/initialize)` |  `POST /v1/{encryptionSpec.name=projects/*/locations/*/encryptionSpec}:initialize`   
Initializes a location-level encryption key specification.  
  
## REST Resource: [v1.projects.locations.insightsdata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.insightsdata)

Methods  
---  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.insightsdata/export)` |  `POST /v1/{parent=projects/*/locations/*}/insightsdata:export`   
Export insights data to a destination defined in the request body.  
  
## REST Resource: [v1.projects.locations.issueModels](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels)

Methods  
---  
`[calculateIssueModelStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/calculateIssueModelStats)` |  `GET /v1/{issueModel=projects/*/locations/*/issueModels/*}:calculateIssueModelStats`   
Gets an issue model's statistics.  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/create)` |  `POST /v1/{parent=projects/*/locations/*}/issueModels`   
Creates an issue model.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/delete)` |  `DELETE /v1/{name=projects/*/locations/*/issueModels/*}`   
Deletes an issue model.  
`[deploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/deploy)` |  `POST /v1/{name=projects/*/locations/*/issueModels/*}:deploy`   
Deploys an issue model.  
`[export](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/export)` |  `POST /v1/{name=projects/*/locations/*/issueModels/*}:export`   
Exports an issue model to the provided destination.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/get)` |  `GET /v1/{name=projects/*/locations/*/issueModels/*}`   
Gets an issue model.  
`[import](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/import)` |  `POST /v1/{parent=projects/*/locations/*}/issueModels:import`   
Imports an issue model from a Cloud Storage bucket.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/list)` |  `GET /v1/{parent=projects/*/locations/*}/issueModels`   
Lists issue models.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/patch)` |  `PATCH /v1/{issueModel.name=projects/*/locations/*/issueModels/*}`   
Updates an issue model.  
`[undeploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels/undeploy)` |  `POST /v1/{name=projects/*/locations/*/issueModels/*}:undeploy`   
Undeploys an issue model.  
  
## REST Resource: [v1.projects.locations.issueModels.issues](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels.issues)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels.issues/create)` |  `POST /v1/{parent=projects/*/locations/*/issueModels/*}/issues`   
Creates an issue.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels.issues/delete)` |  `DELETE /v1/{name=projects/*/locations/*/issueModels/*/issues/*}`   
Deletes an issue.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels.issues/get)` |  `GET /v1/{name=projects/*/locations/*/issueModels/*/issues/*}`   
Gets an issue.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels.issues/list)` |  `GET /v1/{parent=projects/*/locations/*/issueModels/*}/issues`   
Lists issues.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels.issues/patch)` |  `PATCH /v1/{issue.name=projects/*/locations/*/issueModels/*/issues/*}`   
Updates an issue.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.phraseMatchers](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/create)` |  `POST /v1/{parent=projects/*/locations/*}/phraseMatchers`   
Creates a phrase matcher.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/phraseMatchers/*}`   
Deletes a phrase matcher.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/get)` |  `GET /v1/{name=projects/*/locations/*/phraseMatchers/*}`   
Gets a phrase matcher.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/list)` |  `GET /v1/{parent=projects/*/locations/*}/phraseMatchers`   
Lists phrase matchers.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers/patch)` |  `PATCH /v1/{phraseMatcher.name=projects/*/locations/*/phraseMatchers/*}`   
Updates a phrase matcher.  
  
## REST Resource: [v1.projects.locations.qaQuestionTags](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaQuestionTags)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaQuestionTags/create)` |  `POST /v1/{parent=projects/*/locations/*}/qaQuestionTags`   
Creates a QaQuestionTag.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaQuestionTags/delete)` |  `DELETE /v1/{name=projects/*/locations/*/qaQuestionTags/*}`   
Deletes a QaQuestionTag.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaQuestionTags/get)` |  `GET /v1/{name=projects/*/locations/*/qaQuestionTags/*}`   
Gets a QaQuestionTag.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaQuestionTags/list)` |  `GET /v1/{parent=projects/*/locations/*}/qaQuestionTags`   
Lists the question tags.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaQuestionTags/patch)` |  `PATCH /v1/{qaQuestionTag.name=projects/*/locations/*/qaQuestionTags/*}`   
Updates a QaQuestionTag.  
  
## REST Resource: [v1.projects.locations.qaScorecards](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards/create)` |  `POST /v1/{parent=projects/*/locations/*}/qaScorecards`   
Create a QaScorecard.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards/delete)` |  `DELETE /v1/{name=projects/*/locations/*/qaScorecards/*}`   
Deletes a QaScorecard.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards/get)` |  `GET /v1/{name=projects/*/locations/*/qaScorecards/*}`   
Gets a QaScorecard.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards/list)` |  `GET /v1/{parent=projects/*/locations/*}/qaScorecards`   
Lists QaScorecards.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards/patch)` |  `PATCH /v1/{qaScorecard.name=projects/*/locations/*/qaScorecards/*}`   
Updates a QaScorecard.  
  
## REST Resource: [v1.projects.locations.qaScorecards.revisions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions/create)` |  `POST /v1/{parent=projects/*/locations/*/qaScorecards/*}/revisions`   
Creates a QaScorecardRevision.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}`   
Deletes a QaScorecardRevision.  
`[deploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions/deploy)` |  `POST /v1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}:deploy`   
Deploy a QaScorecardRevision.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}`   
Gets a QaScorecardRevision.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/qaScorecards/*}/revisions`   
Lists all revisions under the parent QaScorecard.  
`[tuneQaScorecardRevision](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions/tuneQaScorecardRevision)` |  `POST /v1/{parent=projects/*/locations/*/qaScorecards/*/revisions/*}:tuneQaScorecardRevision`   
Fine tune one or more QaModels.  
`[undeploy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions/undeploy)` |  `POST /v1/{name=projects/*/locations/*/qaScorecards/*/revisions/*}:undeploy`   
Undeploy a QaScorecardRevision.  
  
## REST Resource: [v1.projects.locations.qaScorecards.revisions.qaQuestions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/create)` |  `POST /v1/{parent=projects/*/locations/*/qaScorecards/*/revisions/*}/qaQuestions`   
Create a QaQuestion.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/qaScorecards/*/revisions/*/qaQuestions/*}`   
Deletes a QaQuestion.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/get)` |  `GET /v1/{name=projects/*/locations/*/qaScorecards/*/revisions/*/qaQuestions/*}`   
Gets a QaQuestion.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/list)` |  `GET /v1/{parent=projects/*/locations/*/qaScorecards/*/revisions/*}/qaQuestions`   
Lists QaQuestions.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards.revisions.qaQuestions/patch)` |  `PATCH /v1/{qaQuestion.name=projects/*/locations/*/qaScorecards/*/revisions/*/qaQuestions/*}`   
Updates a QaQuestion.  
  
## REST Resource: [v1.projects.locations.views](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views)

Methods  
---  
`[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/create)` |  `POST /v1/{parent=projects/*/locations/*}/views`   
Creates a view.  
`[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/delete)` |  `DELETE /v1/{name=projects/*/locations/*/views/*}`   
Deletes a view.  
`[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/get)` |  `GET /v1/{name=projects/*/locations/*/views/*}`   
Gets a view.  
`[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/list)` |  `GET /v1/{parent=projects/*/locations/*}/views`   
Lists views.  
`[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.views/patch)` |  `PATCH /v1/{view.name=projects/*/locations/*/views/*}`   
Updates a view.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
