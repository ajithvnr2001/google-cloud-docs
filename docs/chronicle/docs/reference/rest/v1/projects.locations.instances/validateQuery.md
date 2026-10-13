---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery/
title: Method: instances.validateQuery \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:29.928872+00:00
---

# Method: instances.validateQuery  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.validateQuery Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Dialect
  * ErrorType
  * CompilationErrorPosition
    * JSON representation



**Full name** : projects.locations.instances.validateQuery

Validates UDM search query by compiling the query.

### HTTP request

`GET https://{endpoint}/v1/{instance}:validateQuery`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance this request is sent to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`rawQuery` |  `string` Query to compile and validate. Example: 'ip=/172.*/ AND metadata.event_type!="NETWORK_CONNECTION" AND ( target.ip = "3.225.179.73" OR target.ip = "23.47.48.70")'  
`dialect` |  `enum (`[Dialect](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery#Dialect)`)` Query dialect.  
`allowUnreplacedPlaceholders` |  `boolean` Optional. If true, allows for unreplaced $placeholder values. Otherwise, they would result in error.  
`isFederatedQuery` |  `boolean` Optional. If true, the query is a federated query.  
  
### Request body

The request body must be empty.

### Response body

Returns syntax error, if request's rawQuery is invalidated.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "errorType": enum ([ErrorType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery#ErrorType)),
      "errorText": string,
      "queryType": enum ([QueryType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries#QueryType)),
      "errorPosition": {
        object ([CompilationErrorPosition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery#CompilationErrorPosition))
      },
      "warning": string
    }  
  
Fields  
---  
`errorType` |  `enum (`[ErrorType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery#ErrorType)`)` The type of the error.  
`errorText` |  `string` The parse error message.  
`queryType` |  `enum (`[QueryType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.users.searchQueries#QueryType)`)` Query type obtained from the request  
`errorPosition` |  `object (`[CompilationErrorPosition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/validateQuery#CompilationErrorPosition)`)` Captures the position of the error in the query.  
`warning` |  `string` Non-blocking warning message for valid queries (e.g. rewrite warnings).  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.events.validateQuery`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Dialect

The dialect a UDM Search Query is written in.

Enums  
---  
`DIALECT_UNSPECIFIED` | Unknown dialect.  
`DIALECT_LEGACY` | Legacy Structured Query dialect.  
`DIALECT_UDM_SEARCH` | UDM Search dialect.  
`DIALECT_STATS` | Stats Query Dialect  
`DIALECT_SQL` | SQL Dialect  
`DIALECT_RULE_SQL` | GoogleSQL query dialect specifically used for defining SecOps Detection Rules.  
`DIALECT_DASHBOARD_SQL` | GoogleSQL query dialect specifically used for defining Dashboards queries.  
  
## ErrorType

Error type encountered during compilation of search query.

Enums  
---  
`ERROR_TYPE_UNSPECIFIED` | The default error type.  
`INVALID_QUERY_TYPE` | The query has invalid type.  
`INVALID_FIELD_PATH_TYPE` | The field path in the query is invalid.  
`UNCLOSED_BRACKET_TYPE` | The query contains unclosed bracket.  
`BACKEND_ERROR_TYPE` | General backend error.  
`UNCLOSED_QUOTES_TYPE` | The query contains unclosed quotes.  
`QUERY_TOO_LARGE_TYPE` | The query is too large to be processed.  
  
## CompilationErrorPosition

Captures the position of the error in the query.

JSON representation  
---  
      
    
    {
      "startLine": integer,
      "startColumn": integer,
      "endLine": integer,
      "endColumn": integer
    }  
  
Fields  
---  
`startLine` |  `integer` The start line of the error in the query.  
`startColumn` |  `integer` The start column of the error in the query.  
`endLine` |  `integer` The end line of the error in the query.  
`endColumn` |  `integer` The end column of the error in the query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
