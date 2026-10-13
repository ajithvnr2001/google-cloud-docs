---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/ListOperationsResponse/
title: ListOperationsResponse \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:08.275704+00:00
---

# ListOperationsResponse  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/ListOperationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  ListOperationsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



ListOperationsResponse is the result of ListOperationsRequest.

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.operations#Operation))
        }
      ],
      "missingZones": [
        string
      ]
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.operations#Operation)`)` A list of operations in the project in the specified zone.  
`missingZones[]` |  `string` If any zones are listed here, the list of operations returned may be missing the operations from those zones.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-15 UTC."],[],[]] 
