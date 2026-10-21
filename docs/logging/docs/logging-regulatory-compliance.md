---
url: https://docs.cloud.google.com/logging/docs/logging-regulatory-compliance/
title: Regulatory support in Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:41.268160+00:00
---

# Regulatory support in Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logging-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Resources ](https://docs.cloud.google.com/logging/quotas)



Send feedback 

#  Regulatory support in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Cloud Logging that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Cloud Logging APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
logging.googleapis.com | v2 |  SUPPORTED   
  
### Compliance supported regions

Cloud Logging is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4
  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### API fields for sensitive data

#### Resource: No resource

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `logging.googleapis.com` REST API: `POST` `/v2/aggregations:read` RPC methods:

  * `google.logging.v2.LoggingServiceV2.AggregateLogs`

| 

  * `filter`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/data:query` RPC methods:

  * `google.logging.v2.AnalyticsService.QueryData`

| 

  * `query.querySteps.queryBuilderQueryStep.parameters.intArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.intValue`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.fieldSources.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSourceValue.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.boolValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.nullValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.numberValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.structValue.fields.key`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.orderBys.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.sqlQueryStep.parameters.intArray.values`
  * `query.querySteps.sqlQueryStep.parameters.intValue`
  * `query.querySteps.sqlQueryStep.parameters.stringArray.values`
  * `query.querySteps.sqlQueryStep.parameters.stringValue`
  * `query.querySteps.sqlQueryStep.sqlQuery`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/data:queryLocal` RPC methods:

  * `google.logging.v2.AnalyticsService.QueryDataLocal`

| 

  * `query.querySteps.queryBuilderQueryStep.parameters.intArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.intValue`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.fieldSources.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSourceValue.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.boolValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.nullValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.numberValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.structValue.fields.key`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.orderBys.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.sqlQueryStep.parameters.intArray.values`
  * `query.querySteps.sqlQueryStep.parameters.intValue`
  * `query.querySteps.sqlQueryStep.parameters.stringArray.values`
  * `query.querySteps.sqlQueryStep.parameters.stringValue`
  * `query.querySteps.sqlQueryStep.sqlQuery`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/data:querySync` RPC methods:

  * `google.logging.v2.AnalyticsService.QueryDataSync`

| 

  * `sqlQueryStep.parameters.intArray.values`
  * `sqlQueryStep.parameters.intValue`
  * `sqlQueryStep.parameters.stringArray.values`
  * `sqlQueryStep.parameters.stringValue`
  * `sqlQueryStep.sqlQuery`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/entries:copy` RPC methods:

  * `google.logging.v2.ConfigServiceV2.CopyLogEntries`

| 

  * `filter`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/entries:list` RPC methods:

  * `google.logging.v2.LoggingServiceV2.ListLogEntries`

| 

  * `filter`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/entries:readLegacy` RPC methods:

  * `google.logging.v2.LoggingServiceV2.ReadLogEntriesLegacy`

| 

  * `filter`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/entries:redact` RPC methods:

  * `google.logging.v2.ConfigServiceV2.RedactLogEntries`

| 

  * `filter`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/entries:write` RPC methods:

  * `google.logging.v2.LoggingServiceV2.WriteLogEntries`

| 

  * `entries.jsonPayload.fields.key`
  * `entries.jsonPayload.fields.value.boolValue`
  * `entries.jsonPayload.fields.value.nullValue`
  * `entries.jsonPayload.fields.value.numberValue`
  * `entries.jsonPayload.fields.value.stringValue`
  * `entries.protoPayload.typeUrl`
  * `entries.protoPayload.value`
  * `entries.sourceLocation.file`
  * `entries.sourceLocation.function`
  * `entries.textPayload`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/generation:generateQuery` RPC methods:

  * `google.logging.v2.AnalyticsService.GenerateQuery`

| 

  * `prompt`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:extractQueryResources` RPC methods:

  * `google.logging.v2.AnalyticsService.ExtractQueryResources`

| 

  * `query`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:translate` RPC methods:

  * `google.logging.v2.UiSupportService.TranslateQuery`

| 

  * `filter`
  * `histogramQuery.fieldNames`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:translateTableNames` RPC methods:

  * `google.logging.v2.AnalyticsService.TranslateTableNames`

| 

  * `query`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:validate` RPC methods:

  * `google.logging.v2.AnalyticsService.ValidateQuery`

| 

  * `query.querySteps.queryBuilderQueryStep.parameters.intArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.intValue`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.fieldSources.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSourceValue.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.boolValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.nullValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.numberValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.structValue.fields.key`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.orderBys.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.sqlQueryStep.parameters.intArray.values`
  * `query.querySteps.sqlQueryStep.parameters.intValue`
  * `query.querySteps.sqlQueryStep.parameters.stringArray.values`
  * `query.querySteps.sqlQueryStep.parameters.stringValue`
  * `query.querySteps.sqlQueryStep.sqlQuery`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:validateAlerting` RPC methods:

  * `google.logging.v2.AnalyticsService.ValidateAlertingQuery`

| 

  * `query.querySteps.queryBuilderQueryStep.parameters.intArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.intValue`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.fieldSources.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSourceValue.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.boolValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.nullValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.numberValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.structValue.fields.key`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.orderBys.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.sqlQueryStep.parameters.intArray.values`
  * `query.querySteps.sqlQueryStep.parameters.intValue`
  * `query.querySteps.sqlQueryStep.parameters.stringArray.values`
  * `query.querySteps.sqlQueryStep.parameters.stringValue`
  * `query.querySteps.sqlQueryStep.sqlQuery`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:validateAndGetExpression` RPC methods:

  * `google.logging.v2.UiSupportService.ValidateAndGetExpression`

| 

  * `expression.phrase.values`
  * `expression.position.endColumn`
  * `expression.position.endLine`
  * `expression.position.length`
  * `expression.position.startColumn`
  * `expression.position.startLine`
  * `expression.restriction.comparator`
  * `expression.subscriptIndex`
  * `expression.value`
  * `filter`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:validateLocal` RPC methods:

  * `google.logging.v2.AnalyticsService.ValidateQueryLocal`

| 

  * `query.querySteps.queryBuilderQueryStep.parameters.intArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.intValue`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.fieldSources.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSourceValue.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.boolValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.nullValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.numberValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.structValue.fields.key`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.orderBys.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.sqlQueryStep.parameters.intArray.values`
  * `query.querySteps.sqlQueryStep.parameters.intValue`
  * `query.querySteps.sqlQueryStep.parameters.stringArray.values`
  * `query.querySteps.sqlQueryStep.parameters.stringValue`
  * `query.querySteps.sqlQueryStep.sqlQuery`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:validateQueryAlerting` RPC methods:

  * `google.logging.v2.AnalyticsService.ValidateQueryAlerting`

| 

  * `query.querySteps.queryBuilderQueryStep.parameters.intArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.intValue`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringArray.values`
  * `query.querySteps.queryBuilderQueryStep.parameters.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.fieldSources.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.fieldSourceValue.projectedField.regexExtraction`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.boolValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.nullValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.numberValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.stringValue`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.filter.leafPredicate.literalValue.structValue.fields.key`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.orderBys.fieldSource.projectedField.regexExtraction`
  * `query.querySteps.sqlQueryStep.parameters.intArray.values`
  * `query.querySteps.sqlQueryStep.parameters.intValue`
  * `query.querySteps.sqlQueryStep.parameters.stringArray.values`
  * `query.querySteps.sqlQueryStep.parameters.stringValue`
  * `query.querySteps.sqlQueryStep.sqlQuery`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/query:writeRedactedQuery` RPC methods:

  * `google.logging.v2.AnalyticsService.WriteRedactedQuery`

| 

  * `queries`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2/searches:suggest` RPC methods:

  * `google.logging.v2.InsightsService.SuggestSearches`

| 

  * `fieldValues.fieldValues.value`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2beta1/entries:list` RPC methods:

  * `google.logging.v2.LoggingServiceV2.ListLogEntries`

| 

  * `filter`

  
Service: `logging.googleapis.com` REST API: `POST` `/v2beta1/entries:write` RPC methods:

  * `google.logging.v2.LoggingServiceV2.WriteLogEntries`

| 

  * `entries.jsonPayload.fields.key`
  * `entries.jsonPayload.fields.value.boolValue`
  * `entries.jsonPayload.fields.value.nullValue`
  * `entries.jsonPayload.fields.value.numberValue`
  * `entries.jsonPayload.fields.value.stringValue`
  * `entries.protoPayload.typeUrl`
  * `entries.protoPayload.value`
  * `entries.sourceLocation.file`
  * `entries.sourceLocation.function`
  * `entries.textPayload`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Bucket specifics | 

  * `bucket.description`
  * `bucket.indexConfigs.fieldPath`
  * `bucket.restrictedFields`
  * `bucket.tags.key`
  * `bucket.tags.value`

  
Configuration settings | 

  * `bucket.cmekSettings.kmsKey`
  * `cmekSettings.kmsKeyName`
  * `settings.defaultStorageLocation`
  * `settings.kmsKeyName`
  * `settings.name`
  * `settings.storageLocation`

  
Data filtering and selection | 

  * `exclusion.filter`
  * `filter`
  * `notificationRule.filter`
  * `savedQuery.loggingQuery.filter`
  * `sink.filter`
  * `view.filter`

  
Notification rule settings | 

  * `notificationRule.alertPolicyDetails.condition`
  * `notificationRule.alertPolicyDetails.userLabels.key`
  * `notificationRule.alertPolicyDetails.verbosityLabels.key`
  * `notificationRule.notificationChannels`
  * `notificationRule.valueExtractors.key`
  * `notificationRule.valueExtractors.value`

  
Paging and ordering | 

  * `listQuery.orderBy`
  * `orderBy`
  * `pageToken`
  * `savedQuery.opsAnalyticsQuery.queryBuilder.orderBys.field`

  
Query specifics | 

  * `analyticsView.sqlQuery`
  * `query.querySteps.alertingQueryStep.thresholdCondition.valueThreshold.valueColumn`
  * `query.querySteps.queryBuilderQueryStep.queryBuilder.searchTerm`
  * `query.querySteps.sqlQueryStep.parameters.name`
  * `savedQuery.opsAnalyticsQuery.queryBuilder.resourceNames`
  * `savedQuery.opsAnalyticsQuery.sqlQueryText`

  
Resource attributes | 

  * `internalLabels.key`
  * `internalLabels.value`
  * `labels.key`
  * `labels.value`
  * `resource.labels.key`
  * `resource.labels.value`

  
Resource identification | 

  * `analyticsViewId`
  * `bucketId`
  * `linkId`
  * `name`
  * `parent`
  * `viewId`

  
Saved query configuration | 

  * `savedQuery.description`
  * `savedQuery.displayName`
  * `savedQuery.loggingQuery.summaryFields.field`
  * `savedQuery.opsAnalyticsQuery.queryBuilder.fieldSources.projectedField.regexExtraction`
  * `savedQuery.opsAnalyticsQuery.queryBuilder.filter.leafPredicate.fieldSource.projectedField.regexExtraction`

  
Update mask | 

  * `updateMask.paths`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
