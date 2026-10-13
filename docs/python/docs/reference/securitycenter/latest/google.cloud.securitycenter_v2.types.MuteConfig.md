---
url: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MuteConfig
title: Class MuteConfig (1.47.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:59.948769+00:00
---

# Class MuteConfig (1.47.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MuteConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MuteConfig (1.47.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.47.0 (latest)  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.1  1.33.1  1.32.1  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.1  1.25.0  1.24.1  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.2  1.17.0  1.16.2  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    MuteConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A mute config is a Cloud SCC resource that contains the configuration to mute create/update events of findings.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. This field will be ignored if provided on config creation. The following list shows some examples of the format: \- `organizations/{organization}/muteConfigs/{mute_config}` \- `organizations/{organization}locations/{location}//muteConfigs/{mute_config}` \- `folders/{folder}/muteConfigs/{mute_config}` \- `folders/{folder}/locations/{location}/muteConfigs/{mute_config}` \- `projects/{project}/muteConfigs/{mute_config}` \- `projects/{project}/locations/{location}/muteConfigs/{mute_config}`  
`description` |  `str`   
A description of the mute config.   
`filter` |  `str`   
Required. An expression that defines the filter to apply across create/update events of findings. While creating a filter string, be mindful of the scope in which the mute configuration is being created. E.g., If a filter contains project = X but is created under the project = Y scope, it might not match any findings. The following field and operator combinations are supported: \- severity: `=`, `:` \- category: `=`, `:` \- resource.name: `=`, `:` \- resource.project_name: `=`, `:` \- resource.project_display_name: `=`, `:` \- resource.folders.resource_folder: `=`, `:` \- resource.parent_name: `=`, `:` \- resource.parent_display_name: `=`, `:` \- resource.type: `=`, `:` \- finding_class: `=`, `:` \- indicator.ip_addresses: `=`, `:` \- indicator.domains: `=`, `:`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the mute config was created. This field is set by the server and will be ignored if provided on config creation.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The most recent time at which the mute config was updated. This field is set by the server and will be ignored if provided on config creation or update.   
`most_recent_editor` |  `str`   
Output only. Email address of the user who last edited the mute config. This field is set by the server and will be ignored if provided on config creation or update.   
`type_` |  `[google.cloud.securitycenter_v2.types.MuteConfig.MuteConfigType](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.MuteConfig.MuteConfigType)`   
Required. The type of the mute config, which determines what type of mute state the config affects. Immutable after creation.   
`expiry_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The expiry of the mute config. Only applicable for dynamic configs. If the expiry is set, when the config expires, it is removed from all findings.   
  
## Classes 

### MuteConfigType
    
    
    MuteConfigType(value)

The type of MuteConfig.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
