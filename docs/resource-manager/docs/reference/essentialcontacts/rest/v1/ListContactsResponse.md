---
url: https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/ListContactsResponse/
title: ListContactsResponse \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:44.170275+00:00
---

# ListContactsResponse  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/ListContactsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  ListContactsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for the ListContacts method.

JSON representation  
---  
      
    
    {
      "contacts": [
        {
          object ([Contact](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/folders.contacts#Contact))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`contacts[]` |  `object (`[Contact](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/folders.contacts#Contact)`)` The contacts for the specified resource.  
`nextPageToken` |  `string` If there are more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken` and the rest of the parameters the same as the original request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-18 UTC."],[],[]] 
