---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/
title: Cloud Asset API \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:02.876675+00:00
---

# Cloud Asset API  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Cloud Asset API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Asset API manages the history and inventory of Google Cloud resources.

  * REST Resource: v1p7beta1
  * REST Resource: v1p7beta1.operations
  * REST Resource: v1p2beta1.feeds
  * REST Resource: v1p2beta1.operations
  * REST Resource: v1p1beta1.iamPolicies
  * REST Resource: v1p1beta1.resources
  * REST Resource: v1
  * REST Resource: v1.assets
  * REST Resource: v1.effectiveIamPolicies
  * REST Resource: v1.feeds
  * REST Resource: v1.operations
  * REST Resource: v1.savedQueries



## Service: cloudasset.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://cloudasset.googleapis.com/$discovery/rest?version=v1>
  * <https://cloudasset.googleapis.com/$discovery/rest?version=v1p7beta1>
  * <https://cloudasset.googleapis.com/$discovery/rest?version=v1p2beta1>
  * <https://cloudasset.googleapis.com/$discovery/rest?version=v1p1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudasset.googleapis.com`



## REST Resource: [v1p7beta1](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel)

Methods  
---  
`[exportAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/TopLevel/exportAssets)` |  `POST /v1p7beta1/{parent=*/*}:exportAssets`   
Exports assets with time and resource types to a given Cloud Storage location/BigQuery table.  
  
## REST Resource: [v1p7beta1.operations](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/operations)

Methods  
---  
`[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p7beta1/operations/get)` |  `GET /v1p7beta1/{name=*/*/operations/*/**}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1p2beta1.feeds](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds)

Methods  
---  
`[create](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/create)` |  `POST /v1p2beta1/{parent=*/*}/feeds`   
Creates a feed in a parent project/folder/organization to listen to its asset updates.  
`[delete](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/delete)` |  `DELETE /v1p2beta1/{name=*/*/feeds/*}`   
Deletes an asset feed.  
`[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/get)` |  `GET /v1p2beta1/{name=*/*/feeds/*}`   
Gets details about an asset feed.  
`[list](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/list)` |  `GET /v1p2beta1/{parent=*/*}/feeds`   
Lists all asset feeds in a parent project/folder/organization.  
`[patch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/feeds/patch)` |  `PATCH /v1p2beta1/{feed.name=*/*/feeds/*}`   
Updates an asset feed configuration.  
  
## REST Resource: [v1p2beta1.operations](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/operations)

Methods  
---  
`[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p2beta1/operations/get)` |  `GET /v1p2beta1/{name=*/*/operations/*/**}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1p1beta1.iamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies)

Methods  
---  
`[searchAll](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/iamPolicies/searchAll)` |  `GET /v1p1beta1/{scope=*/*}/iamPolicies:searchAll`   
Searches all the IAM policies within a given accessible Resource Manager scope (project/folder/organization).  
  
## REST Resource: [v1p1beta1.resources](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/resources)

Methods  
---  
`[searchAll](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/resources/searchAll)` |  `GET /v1p1beta1/{scope=*/*}/resources:searchAll`   
Searches all the resources within a given accessible Resource Manager scope (project/folder/organization).  
  
## REST Resource: [v1](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel)

Methods  
---  
`[analyzeIamPolicy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy)` |  `GET /v1/{analysisQuery.scope=*/*}:analyzeIamPolicy`   
Analyzes IAM policies to answer which identities have what accesses on which resources.  
`[analyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning)` |  `POST /v1/{analysisQuery.scope=*/*}:analyzeIamPolicyLongrunning`   
Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination.  
`[analyzeMove](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeMove)` |  `GET /v1/{resource=*/*}:analyzeMove`   
Analyze moving a resource to a specified destination without kicking off the actual move.  
`[analyzeOrgPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicies)` |  `GET /v1/{scope=*/*}:analyzeOrgPolicies`   
Analyzes organization policies under a scope.  
`[analyzeOrgPolicyGovernedAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets)` |  `GET /v1/{scope=*/*}:analyzeOrgPolicyGovernedAssets`   
Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope.  
`[analyzeOrgPolicyGovernedContainers](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedContainers)` |  `GET /v1/{scope=*/*}:analyzeOrgPolicyGovernedContainers`   
Analyzes organization policies governed containers (projects, folders or organization) under a scope.  
`[batchGetAssetsHistory](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/batchGetAssetsHistory)` |  `GET /v1/{parent=*/*}:batchGetAssetsHistory`   
Batch gets the update history of assets that overlap a time window.  
`[exportAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/exportAssets)` |  `POST /v1/{parent=*/*}:exportAssets`   
Exports assets with time and resource types to a given Cloud Storage location/BigQuery table.  
`[queryAssets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/queryAssets)` |  `POST /v1/{parent=*/*}:queryAssets`   
Issue a job that queries assets using a SQL statement compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).  
`[searchAllIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllIamPolicies)` |  `GET /v1/{scope=*/*}:searchAllIamPolicies`   
Searches all IAM policies within the specified scope, such as a project, folder, or organization.  
`[searchAllResources](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources)` |  `GET /v1/{scope=*/*}:searchAllResources`   
Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization.  
  
## REST Resource: [v1.assets](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/assets)

Methods  
---  
`[list](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/assets/list)` |  `GET /v1/{parent=*/*}/assets`   
Lists assets with time and resource types and returns paged results in response.  
  
## REST Resource: [v1.effectiveIamPolicies](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies)

Methods  
---  
`[batchGet](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet)` |  `GET /v1/{scope=*/*}/effectiveIamPolicies:batchGet`   
Gets effective IAM policies for a batch of resources.  
  
## REST Resource: [v1.feeds](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds)

Methods  
---  
`[create](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/create)` |  `POST /v1/{parent=*/*}/feeds`   
Creates a feed in a parent project/folder/organization to listen to its asset updates.  
`[delete](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/delete)` |  `DELETE /v1/{name=*/*/feeds/*}`   
Deletes an asset feed.  
`[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/get)` |  `GET /v1/{name=*/*/feeds/*}`   
Gets details about an asset feed.  
`[list](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/list)` |  `GET /v1/{parent=*/*}/feeds`   
Lists all asset feeds in a parent project/folder/organization.  
`[patch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/patch)` |  `PATCH /v1/{feed.name=*/*/feeds/*}`   
Updates an asset feed configuration.  
  
## REST Resource: [v1.operations](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/operations)

Methods  
---  
`[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/operations/get)` |  `GET /v1/{name=*/*/operations/*/**}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.savedQueries](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries)

Methods  
---  
`[create](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/create)` |  `POST /v1/{parent=*/*}/savedQueries`   
Creates a saved query in a parent project/folder/organization.  
`[delete](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/delete)` |  `DELETE /v1/{name=*/*/savedQueries/*}`   
Deletes a saved query.  
`[get](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/get)` |  `GET /v1/{name=*/*/savedQueries/*}`   
Gets details about a saved query.  
`[list](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/list)` |  `GET /v1/{parent=*/*}/savedQueries`   
Lists all saved queries in a parent project/folder/organization.  
`[patch](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/patch)` |  `PATCH /v1/{savedQuery.name=*/*/savedQueries/*}`   
Updates a saved query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
