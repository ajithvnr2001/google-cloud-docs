---
url: https://docs.cloud.google.com/deployment-manager/v2beta1/operations/
title: Operations \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:39.817606+00:00
---

# Operations  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta1/operations/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Operations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

Represents an Operations resource. An operation is returned for every request that modifies data.

For a list of methods for this resource, see the end of this page.

## Resource representations

An operation resource, used to manage asynchronous API requests.
    
    
    {
      "selfLink": string,
      "id": unsigned long,
      "creationTimestamp": string,
      "name": string,
      "zone": string,
      "clientOperationId": string,
      "operationType": string,
      "targetLink": string,
      "targetId": unsigned long,
      "status": string,
      "statusMessage": string,
      "user": string,
      "progress": integer,
      "insertTime": string,
      "startTime": string,
      "endTime": string,
      "warnings": [
        {
          "code": (value),
          "message": string,
          "data": [
            {
              "key": string,
              "value": string
            }
          ]
        }
      ],
      "error": {
        "errors": [
          {
            "code": string,
            "location": string,
            "message": string
          }
        ]
      },
      "httpErrorStatusCode": integer,
      "httpErrorMessage": string,
      "region": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`clientOperationId` | `string` | [Output Only] An optional identifier specified by the client when the mutation was initiated. Must be unique for all operation resources in the project. |   
`creationTimestamp` | `string` | [Output Only] Creation timestamp in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |   
`endTime` | `string` | [Output Only] The time that this operation was completed. This is in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. |   
`error` | `object` | [Output Only] If errors occurred during processing of this operation, this field will be populated. |   
`error.errors[]` | `list` | [Output Only] The array of errors encountered while processing this operation. |   
`error.errors[].code` | `string` | [Output Only] The error type identifier for this error. |   
`error.errors[].location` | `string` | [Output Only] Indicates the field in the request which caused the error. This property is optional. |   
`error.errors[].message` | `string` | [Output Only] An optional, human-readable error message. |   
`httpErrorMessage` | `string` | [Output Only] If operation fails, the HTTP error message returned, e.g. `NOT FOUND`. |   
`httpErrorStatusCode` | `integer` | [Output Only] If operation fails, the HTTP error status code returned, e.g. `404`. |   
`id` | `unsigned long` | [Output Only] Unique identifier for the resource; defined by the server. |   
`insertTime` | `string` | [Output Only] The time that this operation was requested. This is in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. |   
`name` | `string` | [Output Only] Name of the operation. |   
`operationType` | `string` | [Output Only] Type of the operation. Examples include `insert`, or `delete`. |   
`progress` | `integer` | [Output Only] An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess at when the operation will be complete. This number should be monotonically increasing as the operation progresses. |   
`region` | `string` | [Output Only] URL of the region where the operation resides. |   
`selfLink` | `string` | [Output Only] Self link for the manifest. |   
`startTime` | `string` | [Output Only] The time that this operation was started by the server. This is in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. |   
`status` | `string` | [Output Only] Status of the operation. Can be one of the following: `PENDING`, `RUNNING`, or `DONE`. |   
`statusMessage` | `string` | [Output Only] An optional textual description of the current status of the operation. |   
`targetId` | `unsigned long` | [Output Only] Unique target ID which identifies a particular incarnation of the target. |   
`targetLink` | `string` | [Output Only] URL of the resource the operation is mutating. |   
`user` | `string` | [Output Only] User who requested the operation, for example, `user@example.com`. |   
`warnings[]` | `list` | [Output Only] If warning messages generated during processing of this operation, this field will be populated. |   
`warnings[].code` | `any value` | [Output Only] The warning type identifier for this warning. |   
`warnings[].data[]` | `list` | [Output Only] Metadata for this warning in 'key: value' format. |   
`warnings[].data[].key` | `string` | [Output Only] A key for the warning data. |   
`warnings[].data[].value` | `string` | [Output Only] A warning data value corresponding to the key. |   
`warnings[].message` | `string` | [Output Only] Optional human-readable details for this warning. |   
`zone` | `string` | [Output Only] URL of the zone where the operation resides. |   
  
## Methods

[get](https://docs.cloud.google.com/deployment-manager/v2beta1/operations/get)
    Gets information about a specific operation.
[list](https://docs.cloud.google.com/deployment-manager/v2beta1/operations/list)
    Lists all operations for a project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
