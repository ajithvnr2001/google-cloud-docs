---
url: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ListVpcFlowLogsConfigsResponse
title: Class ListVpcFlowLogsConfigsResponse (1.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:56.759944+00:00
---

# Class ListVpcFlowLogsConfigsResponse (1.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ListVpcFlowLogsConfigsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListVpcFlowLogsConfigsResponse (1.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.38.0 (latest)  1.37.0  1.36.0  1.35.0  1.34.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.1  1.25.3  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.17.3  1.16.0  1.15.1  1.14.0  1.13.3  1.12.0  1.11.0  1.10.0  1.9.1  1.8.2  1.7.1  1.6.0  1.5.4  1.4.0  1.3.3  1.2.1  1.1.0  1.0.2  0.2.0  0.1.1 
    
    
    ListVpcFlowLogsConfigsResponse(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Response for the `ListVpcFlowLogsConfigs` method.

## Attributes  
  
---  
**Name** | **Description**  
`vpc_flow_logs_configs` |  `MutableSequence[[google.cloud.network_management_v1.types.VpcFlowLogsConfig](https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.VpcFlowLogsConfig)]`   
List of VPC Flow Log configurations.   
`next_page_token` |  `str`   
Page token to fetch the next set of configurations.   
`unreachable` |  `MutableSequence[str]`   
Locations that could not be reached (when querying all locations with `-`).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
