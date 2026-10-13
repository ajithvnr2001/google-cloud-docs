---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data
title: REST Resource: organizations.environments.apis.revisions.debugsessions.data \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:50.113595+00:00
---

# REST Resource: organizations.environments.apis.revisions.debugsessions.data  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.environments.apis.revisions.debugsessions.data Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DebugSessionTransaction
    * JSON representation
  * Point
    * JSON representation
  * Result
    * JSON representation
  * Access
    * JSON representation
  * Get
    * JSON representation
  * Set
    * JSON representation
  * Remove
    * JSON representation
  * Methods



## Resource: DebugSessionTransaction

A transaction contains all of the debug information of the entire message flow of an API call processed by the runtime plane. The information is collected and recorded at critical points of the message flow in the runtime apiproxy.

JSON representation  
---  
      
    
    {
      "completed": boolean,
      "point": [
        {
          object ([Point](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Point))
        }
      ]
    }  
  
Fields  
---  
`completed` |  `boolean` Flag indicating whether a transaction is completed or not  
`point[]` |  `object (`[Point](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Point)`)` List of debug data collected by runtime plane at various defined points in the flow.  
  
## Point

Point is a group of information collected by runtime plane at critical points of the message flow of the processed API request. This is a list of supported point IDs, categorized to three major buckets. For each category, debug points that we are currently supporting are listed below: - Flow status debug points: StateChange FlowInfo Condition Execution DebugMask Error - Flow control debug points: FlowCallout Paused Resumed FlowReturn BreakFlow Error - Runtime debug points: ScriptExecutor FlowCalloutStepDefinition CustomTarget StepDefinition Oauth2ServicePoint RaiseFault NodeJS

The detail information of the given debug point is stored in a list of results.

JSON representation  
---  
      
    
    {
      "id": string,
      "results": [
        {
          object ([Result](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Result))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Name of a step in the transaction.  
`results[]` |  `object (`[Result](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Result)`)` List of results extracted from a given debug point.  
  
## Result

Result is short for "action result", could be different types identified by "actionResult" field. Supported types: 1. DebugInfo : generic debug info collected by runtime recorded as a list of properties. For example, the contents could be virtual host info, state change result, or execution metadata. Required fields : properties, timestamp

  1. RequestMessage: information of a http request. Contains headers, request URI and http methods type.Required fields : headers, uri, verb

  2. ResponseMessage: information of a http response. Contains headers, reason phrase and http status code. Required fields : headers, reasonPhrase, statusCode

  3. ErrorMessage: information of a http error message. Contains detail error message, reason phrase and status code. Required fields : content, headers, reasonPhrase, statusCode

  4. VariableAccess: a list of variable access actions, can be Get, Set and Remove. Required fields : accessList


JSON representation  
---  
      
    
    {
      "ActionResult": string,
      "properties": {
        object ([Properties](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Properties))
      },
      "timestamp": string,
      "headers": [
        {
          object ([Property](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Property))
        }
      ],
      "uRI": string,
      "verb": string,
      "accessList": [
        {
          object ([Access](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Access))
        }
      ],
      "reasonPhrase": string,
      "statusCode": string,
      "content": string
    }  
  
Fields  
---  
`ActionResult` |  `string` Type of the action result. Can be one of the five: DebugInfo, RequestMessage, ResponseMessage, ErrorMessage, VariableAccess  
`properties` |  `object (`[Properties](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Properties)`)` Name value pairs used for DebugInfo ActionResult.  
`timestamp` |  `string` Timestamp of when the result is recorded. Its format is dd-mm-yy hh:mm:ss:xxx. For example, `"timestamp" : "12-08-19 00:31:59:960"`  
`headers[]` |  `object (`[Property](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Property)`)` A list of HTTP headers. for example, '"headers" : [ { "name" : "Content-Length", "value" : "83" }, { "name" : "Content-Type", "value" : "application/json" } ]'  
`uRI` |  `string` The relative path of the api proxy. for example, `"uRI" : "/iloveapis"`  
`verb` |  `string` HTTP method verb  
`accessList[]` |  `object (`[Access](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Access)`)` A list of variable access actions agaist the api proxy. Supported values: Get, Set, Remove.  
`reasonPhrase` |  `string` HTTP response phrase  
`statusCode` |  `string` HTTP response code  
`content` |  `string` Error message content. for example, "content" : "{"fault":{"faultstring":"API timed out","detail":{"errorcode":"flow.APITimedOut"}}}"  
  
## Access

JSON representation  
---  
      
    
    {
    
      // Union field action can be only one of the following:
      "Get": {
        object ([Get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Get))
      },
      "Set": {
        object ([Set](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Set))
      },
      "Remove": {
        object ([Remove](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Remove))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
Union field `action`.`action` can be only one of the following:  
`Get` |  `object (`[Get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Get)`)`  
`Set` |  `object (`[Set](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Set)`)`  
`Remove` |  `object (`[Remove](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data#Remove)`)`  
  
## Get

Get action. For example, "Get" : { "name" : "target.name", "value" : "default" }

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string`  
`value` |  `string`  
  
## Set

Set action. For example, "Set" : { "name" : "target.name", "success" : true, "value" : "default" }

JSON representation  
---  
      
    
    {
      "name": string,
      "success": boolean,
      "value": string
    }  
  
Fields  
---  
`name` |  `string`  
`success` |  `boolean`  
`value` |  `string`  
  
## Remove

Remove action. For example, "Remove" : { "name" : "target.name", "success" : true }

JSON representation  
---  
      
    
    {
      "name": string,
      "success": boolean
    }  
  
Fields  
---  
`name` |  `string`  
`success` |  `boolean`  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/get)`

|  Gets the debug data from a transaction.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data/list)`

|  Lists the transaction IDs from a debug session.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
