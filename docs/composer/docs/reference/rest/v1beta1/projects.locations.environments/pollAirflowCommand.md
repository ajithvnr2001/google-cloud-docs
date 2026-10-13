---
url: https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/pollAirflowCommand/
title: Method: projects.locations.environments.pollAirflowCommand \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:22.955544+00:00
---

# Method: projects.locations.environments.pollAirflowCommand  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/pollAirflowCommand/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Reference ](https://docs.cloud.google.com/composer/docs/apis)



Send feedback 

#  Method: projects.locations.environments.pollAirflowCommand Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Line
    * JSON representation
  * ExitInfo
    * JSON representation
  * Try it!



Polls Airflow CLI command execution and fetches logs.

### HTTP request

`POST https://composer.googleapis.com/v1beta1/{environment=projects/*/locations/*/environments/*}:pollAirflowCommand`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`environment` |  `string` The resource name of the environment in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `environment`:

  * `composer.environments.executeAirflowCommand`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "executionId": string,
      "pod": string,
      "podNamespace": string,
      "nextLineNumber": integer
    }  
  
Fields  
---  
`executionId` |  `string` The unique ID of the command execution.  
`pod` |  `string` The name of the pod where the command is executed.  
`podNamespace` |  `string` The namespace of the pod where the command is executed.  
`nextLineNumber` |  `integer` Line number from which new logs should be fetched.  
  
### Response body

Response to PollAirflowCommandRequest.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "output": [
        {
          object ([Line](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/pollAirflowCommand#Line))
        }
      ],
      "outputEnd": boolean,
      "exitInfo": {
        object ([ExitInfo](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/pollAirflowCommand#ExitInfo))
      }
    }  
  
Fields  
---  
`output[]` |  `object (`[Line](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/pollAirflowCommand#Line)`)` Output from the command execution. It may not contain the full output and the caller may need to poll for more lines.  
`outputEnd` |  `boolean` Whether the command execution has finished and there is no more output.  
`exitInfo` |  `object (`[ExitInfo](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/pollAirflowCommand#ExitInfo)`)` The result exit status of the command.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudcomposer.readonly`
  * ` https://www.googleapis.com/auth/cloudcomposer`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Line

Contains information about a single line from logs.

JSON representation  
---  
      
    
    {
      "lineNumber": integer,
      "content": string
    }  
  
Fields  
---  
`lineNumber` |  `integer` Number of the line.  
`content` |  `string` Text content of the log line.  
  
## ExitInfo

Information about how a command ended.

JSON representation  
---  
      
    
    {
      "exitCode": integer,
      "error": string
    }  
  
Fields  
---  
`exitCode` |  `integer` The exit code from the command execution.  
`error` |  `string` Error message. Empty if there was no error.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-29 UTC."],[],[]] 
