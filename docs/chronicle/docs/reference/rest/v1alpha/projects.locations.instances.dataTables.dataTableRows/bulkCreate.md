---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows/bulkCreate/
title: Method: dataTableRows.bulkCreate \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:31.951575+00:00
---

# Method: dataTableRows.bulkCreate  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows/bulkCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: dataTableRows.bulkCreate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CreateDataTableRowRequest
    * JSON representation



**Full name** : projects.locations.instances.dataTables.dataTableRows.bulkCreate

Create data table rows in bulk.

### HTTP request

`POST https://{endpoint}/v1alpha/{parent}/dataTableRows:bulkCreate`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource id of the data table. Format: /projects/{project}/locations/{location}/instances/{instance}/dataTables/{dataTable}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([CreateDataTableRowRequest](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows/bulkCreate#CreateDataTableRowRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[CreateDataTableRowRequest](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows/bulkCreate#CreateDataTableRowRequest)`)` Required. Data table rows to create. A maximum of 1000 rows (for sync requests) or 2000 rows (for async requests) can be created in a single request. Total size of the rows should be less than 4MB.  
  
### Response body

Response message with created data table rows.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataTableRows": [
        {
          object ([DataTableRow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows#DataTableRow))
        }
      ]
    }  
  
Fields  
---  
`dataTableRows[]` |  `object (`[DataTableRow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows#DataTableRow)`)` DataTableRows created  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.dataTableRows.bulkCreate`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CreateDataTableRowRequest

Request to create data table row.

JSON representation  
---  
      
    
    {
      "parent": string,
      "dataTableRow": {
        object ([DataTableRow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows#DataTableRow))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource id of the data table. Format: /projects/{project}/locations/{location}/instances/{instance}/dataTables/{dataTable}  
`dataTableRow` |  `object (`[DataTableRow](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataTables.dataTableRows#DataTableRow)`)` Required. The data table row to create.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
