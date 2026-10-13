---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test/
title: Method: projects.locations.goldengateConnectionAssignments.test \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:48.374433+00:00
---

# Method: projects.locations.goldengateConnectionAssignments.test  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Method: projects.locations.goldengateConnectionAssignments.test Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * TestType
  * ResultType
  * TestConnectionAssignmentError
    * JSON representation



Tests a single GoldengateConnectionAssignment.

### HTTP request

Choose a location:

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  
`POST https://oracledatabase.googleapis.com/v1/{name=projects/*/locations/*/goldengateConnectionAssignments/*}:test`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the connection assignment for which to test connection. projects/{project}/locations/{region}/goldengateConnectionAssignments/{goldengateConnectionAssignment}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "type": enum ([TestType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#TestType))
    }  
  
Fields  
---  
`type` |  `enum (`[TestType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#TestType)`)` Optional. The type of the test of the assigned connection. The only type actually supported is DEFAULT.  
  
### Response body

The result of the connectivity test performed between the Goldengate deployment and the associated database / service.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resultType": enum ([ResultType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#ResultType)),
      "error": {
        object ([TestConnectionAssignmentError](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#TestConnectionAssignmentError))
      },
      "errors": [
        {
          object ([TestConnectionAssignmentError](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#TestConnectionAssignmentError))
        }
      ]
    }  
  
Fields  
---  
`resultType` |  `enum (`[ResultType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#ResultType)`)` Type of the result i.e. Success, Failure or Timeout.  
`error` |  `object (`[TestConnectionAssignmentError](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#TestConnectionAssignmentError)`)` Error details if test connection failed.  
`errors[]` |  `object (`[TestConnectionAssignmentError](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test#TestConnectionAssignmentError)`)` List of test connection assignment error objects.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/oracle-database`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `oracledatabase.goldenGateConnectionAssignments.test`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## TestType

The type of test to perform.

Enums  
---  
`TEST_TYPE_UNSPECIFIED` | The default value. This value is unused.  
`DEFAULT` | The default connection test.  
  
## ResultType

Type of the result.

Enums  
---  
`RESULT_TYPE_UNSPECIFIED` | Result type is unspecified.  
`SUCCEEDED` | Test connection succeeded.  
`FAILED` | Test connection failed.  
`TIMED_OUT` | Test connection timed out.  
  
## TestConnectionAssignmentError

Error details for goldengateConnectionAssignments.test.

JSON representation  
---  
      
    
    {
      "code": string,
      "message": string,
      "action": string,
      "issue": string
    }  
  
Fields  
---  
`code` |  `string` A short error code that defines the error, meant for programmatic parsing.  
`message` |  `string` A human-readable error message.  
`action` |  `string` The text describing the action required to fix the issue.  
`issue` |  `string` The text describing the root cause of the reported issue.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
