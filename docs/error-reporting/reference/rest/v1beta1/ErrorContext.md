---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext/
title: ErrorContext \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:57:24.056843+00:00
---

# ErrorContext  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  ErrorContext Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * HttpRequestContext
    * JSON representation
  * SourceLocation
    * JSON representation
  * SourceReference
    * JSON representation



A description of the context in which an error occurred. This data should be provided by the application when reporting an error, unless the error report has been generated automatically from Google App Engine logs.

JSON representation  
---  
      
    
    {
      "httpRequest": {
        object ([HttpRequestContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext#HttpRequestContext))
      },
      "user": string,
      "reportLocation": {
        object ([SourceLocation](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext#SourceLocation))
      },
      "sourceReferences": [
        {
          object ([SourceReference](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext#SourceReference))
        }
      ]
    }  
  
Fields  
---  
`httpRequest` |  `object (`[HttpRequestContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext#HttpRequestContext)`)` The HTTP request which was processed when the error was triggered.  
`user` |  `string` The user who caused or was affected by the crash. This can be a user ID, an email address, or an arbitrary token that uniquely identifies the user. When sending an error report, leave this field empty if the user was not logged in. In this case the Error Reporting system will use other data, such as remote IP address, to distinguish affected users. See `affectedUsersCount` in `ErrorGroupStats`.  
`reportLocation` |  `object (`[SourceLocation](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext#SourceLocation)`)` The location in the source code where the decision was made to report the error, usually the place where it was logged. For a logged exception this would be the source line where the exception is logged, usually close to the place where it was caught.  
`sourceReferences[]` |  `object (`[SourceReference](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext#SourceReference)`)` Source code that was used to build the executable which has caused the given error message.  
  
## HttpRequestContext

HTTP request data that is related to a reported error. This data should be provided by the application when reporting an error, unless the error report has been generated automatically from Google App Engine logs.

JSON representation  
---  
      
    
    {
      "method": string,
      "url": string,
      "userAgent": string,
      "referrer": string,
      "responseStatusCode": integer,
      "remoteIp": string
    }  
  
Fields  
---  
`method` |  `string` The type of HTTP request, such as `GET`, `POST`, etc.  
`url` |  `string` The URL of the request.  
`userAgent` |  `string` The user agent information that is provided with the request.  
`referrer` |  `string` The referrer information that is provided with the request.  
`responseStatusCode` |  `integer` The HTTP response status code for the request.  
`remoteIp` |  `string` The IP address from which the request originated. This can be IPv4, IPv6, or a token which is derived from the IP address, depending on the data that has been provided in the error report.  
  
## SourceLocation

Indicates a location in the source code of the service for which errors are reported. `functionName` must be provided by the application when reporting an error, unless the error report contains a `message` with a supported exception stack trace. All fields are optional for the later case.

JSON representation  
---  
      
    
    {
      "filePath": string,
      "lineNumber": integer,
      "functionName": string
    }  
  
Fields  
---  
`filePath` |  `string` The source code filename, which can include a truncated relative path, or a full path from a production machine.  
`lineNumber` |  `integer` 1-based. 0 indicates that the line number is unknown.  
`functionName` |  `string` Human-readable name of a function or method. The value can include optional context like the class or package name. For example, `my.package.MyClass.method` in case of Java.  
  
## SourceReference

A reference to a particular snapshot of the source tree used to build and deploy an application.

JSON representation  
---  
      
    
    {
      "repository": string,
      "revisionId": string
    }  
  
Fields  
---  
`repository` |  `string` Optional. A URI string identifying the repository. Example: "https://github.com/GoogleCloudPlatform/kubernetes.git"  
`revisionId` |  `string` The canonical and persistent identifier of the deployed revision. Example (git): "0035781c50ec7aa23385dc841529ce8a4b70db1b"  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
