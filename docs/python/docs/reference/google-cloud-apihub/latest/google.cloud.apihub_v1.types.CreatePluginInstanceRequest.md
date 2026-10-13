---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginInstanceRequest
title: Class CreatePluginInstanceRequest (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:32.772239+00:00
---

# Class CreatePluginInstanceRequest (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreatePluginInstanceRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    CreatePluginInstanceRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The CreatePluginInstance method's request.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}`  
`plugin_instance_id` |  `str`   
Optional. The ID to use for the plugin instance, which will become the final component of the plugin instance's resource name. This field is optional. \- If provided, the same will be used. The service will throw an error if the specified id is already used by another plugin instance in the plugin resource. \- If not provided, a system generated id will be used. This value should be 4-63 characters, and valid characters are /`a-z][A-Z]`[0-9]-\\_/.   
`plugin_instance` |  `[google.cloud.apihub_v1.types.PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance)`   
Required. The plugin instance to create.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
