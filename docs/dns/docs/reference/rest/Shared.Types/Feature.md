---
url: https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/Feature/
title: Feature \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:31.823899+00:00
---

# Feature  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/Shared.Types/Feature/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Feature Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation

JSON representation  
---  
      
    
    {
      "name": string,
      "booleanValue": boolean,
      "doubleValue": number,
      "stringValues": [
        string
      ],
      "int64Value": string,
      "featureCount": string,
      "integerValue": integer,
      "timestampSequences": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string`  
`booleanValue` |  `boolean` Exactly one of the following should be filled in.  
`doubleValue` |  `number`  
`stringValues[]` |  `string`  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Useful for timestamps, or for numerical features where it is helpful for decision scripts to have exact values.  
`featureCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Useful for applications that need to know how many times a specific feature occurs  
`integerValue` |  `integer` integer value field is deprecated and shall only be used for passing the following features hardcoded in spamiam::SpamIAmMessage: spamiam::OrkutSenderId spamiam::OrkutPostnumReports spamiam::BloggerNumComments spamiam::BloggerNumCommentsByOthers Another hard-coded spamiam feature is spamiam::BlogName, which can be specified via string value.  
`timestampSequences[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This field should only be used to store a sequence of timestamps associated with the feature.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
