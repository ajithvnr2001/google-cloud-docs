---
url: https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types
title: Package types (0.15.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:01.838367+00:00
---

# Package types (0.15.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.15.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.2 (latest)  0.15.1  0.14.0  0.13.0  0.12.0  0.11.15  0.10.0  0.9.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.3  0.3.1  0.2.1  0.1.0 

API documentation for `bigquery_migration_v2alpha.types` package.

## Classes 

### [AssessmentOrchestrationResultDetails](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.AssessmentOrchestrationResultDetails)

Details for an assessment task orchestration result.

### [AssessmentTaskDetails](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.AssessmentTaskDetails)

Assessment task config.

### [BteqOptions](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.BteqOptions)

BTEQ translation task related settings.

### [CreateMigrationWorkflowRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.CreateMigrationWorkflowRequest)

Request to create a migration workflow resource.

### [DatasetReference](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.DatasetReference)

Reference to a BigQuery dataset.

### [DeleteMigrationWorkflowRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.DeleteMigrationWorkflowRequest)

A request to delete a previously created migration workflow.

### [ErrorDetail](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ErrorDetail)

Provides details for errors, e.g. issues that where encountered when processing a subtask.

### [ErrorLocation](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ErrorLocation)

Holds information about where the error is located.

### [Filter](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.Filter)

The filter applied to fields of translation details.

### [GetMigrationSubtaskRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.GetMigrationSubtaskRequest)

A request to get a previously created migration subtasks.

### [GetMigrationWorkflowRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.GetMigrationWorkflowRequest)

A request to get a previously created migration workflow.

### [IdentifierSettings](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.IdentifierSettings)

Settings related to SQL identifiers.

### [ListMigrationSubtasksRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationSubtasksRequest)

A request to list previously created migration subtasks.

### [ListMigrationSubtasksResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationSubtasksResponse)

Response object for a `ListMigrationSubtasks` call.

### [ListMigrationWorkflowsRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationWorkflowsRequest)

A request to list previously created migration workflows.

### [ListMigrationWorkflowsResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationWorkflowsResponse)

Response object for a `ListMigrationWorkflows` call.

### [MigrationSubtask](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.MigrationSubtask)

A subtask for a migration which carries details about the configuration of the subtask. The content of the details should not matter to the end user, but is a contract between the subtask creator and subtask worker.

### [MigrationTask](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.MigrationTask)

A single task for a migration which has details about the configuration of the task.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MigrationTaskOrchestrationResult](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.MigrationTaskOrchestrationResult)

Additional information from the orchestrator when it is done with the task orchestration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MigrationWorkflow](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.MigrationWorkflow)

A migration workflow which specifies what needs to be done for an EDW migration.

### [Point](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.Point)

A single data point in a time series.

### [ResourceErrorDetail](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ResourceErrorDetail)

Provides details for errors and the corresponding resources.

### [SqlTranslationError](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.SqlTranslationError)

The detailed error object if the SQL translation job fails.

### [SqlTranslationErrorDetail](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.SqlTranslationErrorDetail)

Structured error object capturing the error message and the location in the source text where the error occurs.

### [SqlTranslationWarning](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.SqlTranslationWarning)

The detailed warning object if the SQL translation job is completed but not semantically correct.

### [StartMigrationWorkflowRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.StartMigrationWorkflowRequest)

A request to start a previously created migration workflow.

### [TeradataOptions](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TeradataOptions)

Teradata SQL specific translation task related settings.

### [TimeInterval](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TimeInterval)

A time interval extending just after a start time through an end time. If the start time is the same as the end time, then the interval represents a single point in time.

### [TimeSeries](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TimeSeries)

The metrics object for a SubTask.

### [TranslateQueryRequest](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TranslateQueryRequest)

The request of translating a SQL query to Standard SQL.

### [TranslateQueryResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TranslateQueryResponse)

The response of translating a SQL query to Standard SQL.

### [TranslationFileMapping](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TranslationFileMapping)

Mapping between an input and output file to be translated in a subtask.

### [TranslationTaskDetails](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TranslationTaskDetails)

The translation task config to capture necessary settings for a translation task and subtask.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TypedValue](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.TypedValue)

A single strongly-typed value.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
