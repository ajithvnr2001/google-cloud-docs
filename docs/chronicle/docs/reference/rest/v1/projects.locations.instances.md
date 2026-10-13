---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:16.991145+00:00
---

# REST Resource: projects.locations.instances  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * Methods



## Resource: Instance

A Instance represents an instantiation of the Instance product.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of this instance. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
## Methods  
  
---  
  
### `[computeAllFindingsRefinementActivities](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/computeAllFindingsRefinementActivities)`

|  Returns findings refinement activity for all findings refinements.  
  
### `[extractSyslog](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/extractSyslog)`

|  ExtractSyslog extracts structured part of log from a unstructured log by running a grok regex over it.  
  
### `[findEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findEntity)`

|  Identifies the entity type and retrieves relevant data associated with a specified indicator.  
  
### `[findEntityAlerts](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findEntityAlerts)`

|  Get alerts for an entity.  
  
### `[findRelatedEntities](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findRelatedEntities)`

|  Finds all the entities associated with provided entity.  
  
### `[findUdmFieldValues](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findUdmFieldValues)`

|  Finds ingested UDM field values that match a query.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/get)`

|  Gets a Instance.  
  
### `[getBigQueryExport](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getBigQueryExport)`

|  Get the BigQuery export configuration for a Chronicle instance.  
  
### `[getEnrichmentCombination](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getEnrichmentCombination)`

|  Get the EnrichmentCombination.  
  
### `[getRiskConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getRiskConfig)`

|  Queries the instance to get the Risk Configurations used for the computation of Entity Risk Score.  
  
### `[getThreatCollectionFilterSet](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/getThreatCollectionFilterSet)`

|  Get the set of threat collection filter options.  
  
### `[listAllFindingsRefinementDeployments](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/listAllFindingsRefinementDeployments)`

|  Lists all findings refinement deployments.  
  
### `[queryProductSourceStats](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/queryProductSourceStats)`

|  Gets available product sources along with their stats.  
  
### `[searchEntities](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/searchEntities)`

|  Identifies the entity type and retrieves relevant data associated with a specified indicator.  
  
### `[summarizeEntitiesFromQuery](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntitiesFromQuery)`

|  Parses the query and identifies the entities contained within the search query.  
  
### `[summarizeEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/summarizeEntity)`

|  Returns all entity data over specified time.  
  
### `[udmSearch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/udmSearch)`

|  Performs a UDM search that returns matching events for the query.  
  
### `[updateBigQueryExport](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/updateBigQueryExport)`

|  Update the BigQuery export configuration for a Chronicle instance.  
  
### `[updateRiskConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/updateRiskConfig)`

|  Updates RiskConfig used for the computation of Entity Risk Score.  
  
### `[validateQuery](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery)`

|  Validates UDM search query by compiling the query.  
  
### `[verifyReferenceList](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyReferenceList)`

|  VerifyReferenceList validates list content and returns line errors, if any.  
  
### `[verifyRuleText](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/verifyRuleText)`

|  Verifies the given rule text.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
