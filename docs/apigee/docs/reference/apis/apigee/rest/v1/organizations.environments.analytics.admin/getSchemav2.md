---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2/
title: Method: organizations.environments.analytics.admin.getSchemav2 \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:47.488267+00:00
---

# Method: organizations.environments.analytics.admin.getSchemav2  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.analytics.admin.getSchemav2 Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * SchemaElement
    * JSON representation
  * SchemaProperty
    * JSON representation
  * Try it!



Gets a list of metrics and dimensions that can be used to create analytics queries and reports. Each schema element contains the name of the field, its associated type, and a flag indicating whether it is a standard or custom field.

### HTTP request

`GET https://apigee.googleapis.com/v1/{name=organizations/*/environments/*/analytics/admin/schemav2}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Path to the schema. Use the following structure in your request: `organizations/{org}/environments/{env}/analytics/admin/schemav2`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.environments.get`

  
  
### Query parameters

Parameters  
---  
`type` |  `string` Required. Name of the dataset for which you want to retrieve the schema. For example: `fact` or `agg_cus1`  
`disableCache` |  `boolean` Flag that specifies whether the schema is be read from the database or cache. Set to `true` to read the schema from the database. Defaults to cache.  
  
### Request body

The request body must be empty.

### Response body

Response for Schema call

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dimensions": [
        {
          object ([SchemaElement](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2#SchemaElement))
        }
      ],
      "metrics": [
        {
          object ([SchemaElement](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2#SchemaElement))
        }
      ],
      "meta": [
        string
      ]
    }  
  
Fields  
---  
`dimensions[]` |  `object (`[SchemaElement](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2#SchemaElement)`)` List of schema fields grouped as dimensions.  
`metrics[]` |  `object (`[SchemaElement](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2#SchemaElement)`)` List of schema fields grouped as dimensions that can be used with an aggregate function such as `sum`, `avg`, `min`, and `max`.  
`meta[]` |  `string` Additional metadata associated with schema. This is a legacy field and usually consists of an empty array of strings.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



## SchemaElement

Message type for the schema element

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([SchemaProperty](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2#SchemaProperty))
      }
    }  
  
Fields  
---  
`name` |  `string` Name of the field.  
`properties` |  `object (`[SchemaProperty](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin/getSchemav2#SchemaProperty)`)` Properties for the schema field. For example: { "createTime": "2016-02-26T10:23:09.592Z", "custom": "false", "type": "string" }  
  
## SchemaProperty

Properties for the schema field.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "custom": string,
      "type": string
    }  
  
Fields  
---  
`createTime` |  `string` Time the field was created in RFC3339 string form. For example: `2016-02-26T10:23:09.592Z`.  
`custom` |  `string` Flag that specifies whether the field is standard in the dataset or a custom field created by the customer. `true` indicates that it is a custom field.  
`type` |  `string` Data type of the field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
