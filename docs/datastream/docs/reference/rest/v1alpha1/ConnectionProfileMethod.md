---
url: https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/ConnectionProfileMethod/
title: ConnectionProfileMethod \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:04.953848+00:00
---

# ConnectionProfileMethod  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/ConnectionProfileMethod/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)



Send feedback 

#  ConnectionProfileMethod Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ProfileType
  * ConnectivityOption



Connection Profile method specifying the connection type and the available connectivity options

JSON representation  
---  
      
    
    {
      "profileType": enum ([ProfileType](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/ConnectionProfileMethod#ProfileType)),
      "connectivityOptions": [
        enum ([ConnectivityOption](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/ConnectionProfileMethod#ConnectivityOption))
      ]
    }  
  
Fields  
---  
`profileType` |  `enum (`[ProfileType](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/ConnectionProfileMethod#ProfileType)`)` Profile type.  
`connectivityOptions[]` |  `enum (`[ConnectivityOption](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/ConnectionProfileMethod#ConnectivityOption)`)` Eligible connectivity options.  
  
## ProfileType

The possible Connection Profile types.

Enums  
---  
`PROFILE_TYPE_UNSPECIFIED` | Unspecified profile type.  
`ORACLE` | Oracle profile type.  
`GCS` | Cloud Storage profile type.  
  
## ConnectivityOption

The possible connectivity options.

Enums  
---  
`CONNECTIVITY_OPTION_UNSPECIFIED` | Unspecified connectivity option.  
`STATIC_IP_CONNECTIVITY` | Static IP connectivity.  
`FORWARD_SSH_CONNECTIVITY` | Forward SSH connectivity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
