---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/routers/getRoutePolicy/
title: Method: routers.getRoutePolicy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:08.102265+00:00
---

# Method: routers.getRoutePolicy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/routers/getRoutePolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: routers.getRoutePolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Returns specified Route Policy

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/routers/{router}/getRoutePolicy?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
`router` |  `string` Name of the Router resource to query for the route policy. The name should conform to RFC1035.  
  
### Query parameters

Parameters  
---  
`policy` |  `string` The Policy name for this request. Name must conform to RFC1035  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resource": {
        "name": string,
        "type": enum,
        "terms": [
          {
            "priority": integer,
            "match": {
              "expression": string,
              "title": string,
              "description": string,
              "location": string
            },
            "actions": [
              {
                "expression": string,
                "title": string,
                "description": string,
                "location": string
              }
            ]
          }
        ],
        "fingerprint": string,
        "description": string
      }
    }  
  
Fields  
---  
`resource` |  `object`  
`resource.name` |  `string` Route Policy name, which must be a resource ID segment and unique within all the router's Route Policies. Name should conform to RFC1035.  
`resource.type` |  `enum`  
`resource.terms[]` |  `object` routers.list of terms (the order in the list is not important, they are evaluated in order of priority). Order of policies is not retained and might change when getting policy later.  
`resource.terms[].priority` |  `integer` The evaluation priority for this term, which must be between 0 (inclusive) and 2^31 (exclusive), and unique within the list.  
`resource.terms[].match` |  `object` CEL expression evaluated against a route to determine if this term applies. When not set, the term applies to all routes.  
`resource.terms[].match.expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`resource.terms[].match.title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`resource.terms[].match.description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`resource.terms[].match.location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
`resource.terms[].actions[]` |  `object` CEL expressions to evaluate to modify a route when this term matches.  
`resource.terms[].actions[].expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`resource.terms[].actions[].title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`resource.terms[].actions[].description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`resource.terms[].actions[].location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
`resource.fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the Route Policy being applied to this Router, which is essentially a hash of the Route Policy used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update Route Policy. You must always provide an up-to-date fingerprint hash in order to update or change labels.To see the latest fingerprint, make a `getRoutePolicy()` request to retrieve a Route Policy.A base64-encoded string.  
`resource.description` |  `string` An optional description of route policy.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.routers.getRoutePolicy`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
