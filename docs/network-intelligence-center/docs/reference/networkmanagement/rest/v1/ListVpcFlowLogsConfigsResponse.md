---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/ListVpcFlowLogsConfigsResponse/
title: ListVpcFlowLogsConfigsResponse \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:34.595214+00:00
---

# ListVpcFlowLogsConfigsResponse  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/ListVpcFlowLogsConfigsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  ListVpcFlowLogsConfigsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response for the `ListVpcFlowLogsConfigs` method.

JSON representation  
---  
      
    
    {
      "vpcFlowLogsConfigs": [
        {
          object ([VpcFlowLogsConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`vpcFlowLogsConfigs[]` |  `object (`[VpcFlowLogsConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig)`)` List of VPC Flow Log configurations.  
`nextPageToken` |  `string` Page token to fetch the next set of configurations.  
`unreachable[]` |  `string` Locations that could not be reached (when querying all locations with `-`).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
