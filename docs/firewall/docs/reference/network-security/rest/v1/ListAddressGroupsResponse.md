---
url: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/ListAddressGroupsResponse/
title: ListAddressGroupsResponse \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:06.341184+00:00
---

# ListAddressGroupsResponse  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/ListAddressGroupsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Reference ](https://docs.cloud.google.com/firewall/docs/apis)



Send feedback 

#  ListAddressGroupsResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response returned by the ListAddressGroups method.

JSON representation  
---  
      
    
    {
      "addressGroups": [
        {
          object ([AddressGroup](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.addressGroups#AddressGroup))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`addressGroups[]` |  `object (`[AddressGroup](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.addressGroups#AddressGroup)`)` List of AddressGroups resources.  
`nextPageToken` |  `string` If there might be more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-24 UTC."],[],[]] 
