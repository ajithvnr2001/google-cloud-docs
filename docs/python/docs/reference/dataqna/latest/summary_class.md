---
url: https://docs.cloud.google.com/python/docs/reference/dataqna/latest/summary_class/
title: Package Classes (0.14.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:24.534185+00:00
---

# Package Classes (0.14.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataqna/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.0  0.11.0  0.10.17  0.9.0  0.8.2  0.7.1  0.6.3  0.5.1  0.4.0  0.3.3  0.2.1  0.1.1 

Summary of entries of Classes for dataqna.

## Classes 

### [AutoSuggestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.auto_suggestion_service.AutoSuggestionServiceAsyncClient)

This stateless API provides automatic suggestions for natural language queries for the data sources in the provided project and location.

The service provides a resourceless operation `suggestQueries` that can be called to get a list of suggestions for a given incomplete query and scope (or list of scopes) under which the query is to be interpreted.

There are two types of suggestions, ENTITY for single entity suggestions and TEMPLATE for full sentences. By default, both types are returned.

Example Request:

::

GetSuggestions({ parent: "locations/us/projects/my-project" scopes: "//bigquery.googleapis.com/projects/my-project/datasets/my-dataset/tables/my-table" query: "top it" })

The service will retrieve information based on the given scope(s) and give suggestions based on that (e.g. "top item" for "top it" if "item" is a known dimension for the provided scope).

::

suggestions { suggestion_info { annotated_suggestion { text_formatted: "top item by sum of usd_revenue_net" markups { type: DIMENSION start_char_index: 4 length: 4 } markups { type: METRIC start_char_index: 19 length: 15 } } query_matches { start_char_index: 0 length: 6 } } suggestion_type: TEMPLATE ranking_score: 0.9 } suggestions { suggestion_info { annotated_suggestion { text_formatted: "item" markups { type: DIMENSION start_char_index: 4 length: 2 } } query_matches { start_char_index: 0 length: 6 } } suggestion_type: ENTITY ranking_score: 0.8 }

### [AutoSuggestionServiceClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.auto_suggestion_service.AutoSuggestionServiceClient)

This stateless API provides automatic suggestions for natural language queries for the data sources in the provided project and location.

The service provides a resourceless operation `suggestQueries` that can be called to get a list of suggestions for a given incomplete query and scope (or list of scopes) under which the query is to be interpreted.

There are two types of suggestions, ENTITY for single entity suggestions and TEMPLATE for full sentences. By default, both types are returned.

Example Request:

::

GetSuggestions({ parent: "locations/us/projects/my-project" scopes: "//bigquery.googleapis.com/projects/my-project/datasets/my-dataset/tables/my-table" query: "top it" })

The service will retrieve information based on the given scope(s) and give suggestions based on that (e.g. "top item" for "top it" if "item" is a known dimension for the provided scope).

::

suggestions { suggestion_info { annotated_suggestion { text_formatted: "top item by sum of usd_revenue_net" markups { type: DIMENSION start_char_index: 4 length: 4 } markups { type: METRIC start_char_index: 19 length: 15 } } query_matches { start_char_index: 0 length: 6 } } suggestion_type: TEMPLATE ranking_score: 0.9 } suggestions { suggestion_info { annotated_suggestion { text_formatted: "item" markups { type: DIMENSION start_char_index: 4 length: 2 } } query_matches { start_char_index: 0 length: 6 } } suggestion_type: ENTITY ranking_score: 0.8 }

### [QuestionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceAsyncClient)

Service to interpret natural language queries. The service allows to create `Question` resources that are interpreted and are filled with one or more interpretations if the question could be interpreted. Once a `Question` resource is created and has at least one interpretation, an interpretation can be chosen for execution, which triggers a query to the backend (for BigQuery, it will create a job). Upon successful execution of that interpretation, backend specific information will be returned so that the client can retrieve the results from the backend.

The `Question` resources are named `projects/*/locations/*/questions/*`.

The `Question` resource has a singletion sub-resource `UserFeedback` named `projects/*/locations/*/questions/*/userFeedback`, which allows access to user feedback.

### [QuestionServiceClient](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.services.question_service.QuestionServiceClient)

Service to interpret natural language queries. The service allows to create `Question` resources that are interpreted and are filled with one or more interpretations if the question could be interpreted. Once a `Question` resource is created and has at least one interpretation, an interpretation can be chosen for execution, which triggers a query to the backend (for BigQuery, it will create a job). Upon successful execution of that interpretation, backend specific information will be returned so that the client can retrieve the results from the backend.

The `Question` resources are named `projects/*/locations/*/questions/*`.

The `Question` resource has a singletion sub-resource `UserFeedback` named `projects/*/locations/*/questions/*/userFeedback`, which allows access to user feedback.

### [AnnotatedString](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.AnnotatedString)

Describes string annotation from both semantic and formatting perspectives. Example:

User Query:

top countries by population in Africa

0 4 14 17 28 31 37

Table Data:

  * "country" - dimension
  * "population" - metric
  * "Africa" - value in the "continent" column



text_formatted = `"top countries by population in Africa"`

html_formatted = `"top <b>countries</b> by <b>population</b> in <i>Africa</i>"`

::

markups = [ {DIMENSION, 4, 12}, // 'countries' {METRIC, 17, 26}, // 'population' {FILTER, 31, 36} // 'Africa' ]

Note that html formattings for 'DIMENSION' and 'METRIC' are the same, while semantic markups are different.

### [SemanticMarkup](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.AnnotatedString.SemanticMarkup)

Semantic markup denotes a substring (by index and length) with markup information.

### [SemanticMarkupType](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.AnnotatedString.SemanticMarkupType)

Semantic markup types.

### [BigQueryJob](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.BigQueryJob)

BigQuery job information. This can be used to query the BigQuery API and retrieve the current job's status (using `jobs.get <https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get>`__).

### [CreateQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.CreateQuestionRequest)

Request to create a question resource.

### [DataQuery](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.DataQuery)

Representation of the data query for the backend. This is provided for informational purposes only. Clients should not use it to send it to the backend directly, but rather use the `execute` RPC to trigger the execution. Using the `execute` RPC is needed in order to track the state of a question and report on it correctly to the data administrators.

### [DebugFlags](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.DebugFlags)

Configuriation of debug flags.

### [ExecuteQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecuteQuestionRequest)

Request to execute an interpretation.

### [ExecutionInfo](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecutionInfo)

Information about the backend status (such as BigQuery) of the execution.

### [JobExecutionState](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.ExecutionInfo.JobExecutionState)

Enum of possible job execution statuses.

### [GetQuestionRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.GetQuestionRequest)

A request to get a previously created question.

### [GetUserFeedbackRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.GetUserFeedbackRequest)

Request to get user feedback.

### [HumanReadable](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.HumanReadable)

Human readable interpretation.

### [InterpretEntity](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretEntity)

Query entities of an interpretation.

### [InterpretError](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretError)

Details on the failure to interpret the question.

### [InterpretAmbiguityDetails](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretError.InterpretAmbiguityDetails)

Details about a query that was too ambiguous. Currently, the message has no fields and its presence signals that there was ambiguity.

### [InterpretErrorCode](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretError.InterpretErrorCode)

The interpret error code provides an error category why the interpretation failed.

### [InterpretErrorDetails](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretError.InterpretErrorDetails)

Details on interpretation failure.

### [InterpretIncompleteQueryDetails](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretError.InterpretIncompleteQueryDetails)

Details about an incomplete query.

### [InterpretUnsupportedDetails](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretError.InterpretUnsupportedDetails)

Details about unsupported parts in a query.

### [Interpretation](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Interpretation)

An interpretation of a natural language query.

### [InterpretationStructure](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretationStructure)

Information about the interpretation structure that helps to understand and visualize the response.

### [ColumnInfo](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretationStructure.ColumnInfo)

Information about a column.

### [VisualizationType](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.InterpretationStructure.VisualizationType)

Enumeration of visualzation types to use for query response data.

### [Question](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Question)

The question resource represents a natural language query, its settings, understanding generated by the system, and answer retrieval status. A question cannot be modified.

### [SuggestQueriesRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.SuggestQueriesRequest)

Request for query suggestions.

### [SuggestQueriesResponse](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.SuggestQueriesResponse)

Response to SuggestQueries.

### [Suggestion](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.Suggestion)

A suggestion for a query with a ranking score.

### [SuggestionInfo](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.SuggestionInfo)

Detailed information about the suggestion.

### [MatchInfo](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.SuggestionInfo.MatchInfo)

MatchInfo describes which part of suggestion matched with data in user typed query. This can be used to highlight matching parts in the UI. This is different from the annotations provided in annotated_suggestion. The annotated_suggestion provides information about the semantic meaning, while this provides information about how it relates to the input.

Example: user query: `top products`

::

annotated_suggestion { text_formatted = "top product_group" html_formatted = "top **product_group** " markups { {type: TEXT, start_char_index: 0, length: 3} {type: DIMENSION, start_char_index: 4, length: 13} } }

query_matches { { start_char_index: 0, length: 3 } { start_char_index: 4, length: 7} }

### [SuggestionType](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.SuggestionType)

The type of suggestion.

### [UpdateUserFeedbackRequest](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UpdateUserFeedbackRequest)

Request to updates user feedback.

### [UserFeedback](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UserFeedback)

Feedback provided by a user.

### [UserFeedbackRating](https://docs.cloud.google.com/python/docs/reference/dataqna/latest/google.cloud.dataqna_v1alpha.types.UserFeedback.UserFeedbackRating)

Enumeration of feedback ratings.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
