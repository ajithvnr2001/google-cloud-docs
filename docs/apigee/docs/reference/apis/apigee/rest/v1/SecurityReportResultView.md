---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportResultView/
title: SecurityReportResultView \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:58.333479+00:00
---

# SecurityReportResultView  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportResultView/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SecurityReportResultView Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response for security report result view APIs.

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([SecurityReportMetadata](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportMetadata))
      },
      "rows": array,
      "state": string,
      "code": integer,
      "error": string
    }  
  
Fields  
---  
`metadata` |  `object (`[SecurityReportMetadata](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/SecurityReportMetadata)`)` Metadata contains information like metrics, dimenstions etc of the security report.  
`rows` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Rows of security report result. Each row is a JSON object.Example: {sum(message_count): 1, developerApp: "(not set)",…}  
`state` |  `string` State of retrieving ResultView.  
`code` |  `integer` Error code when there is a failure.  
`error` |  `string` Error message when there is a failure.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
