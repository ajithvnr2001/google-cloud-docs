---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CanaryDeployment
title: Class CanaryDeployment (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:43.782692+00:00
---

# Class CanaryDeployment (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CanaryDeployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CanaryDeployment (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    CanaryDeployment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

CanaryDeployment represents the canary deployment configuration

## Attributes  
  
---  
**Name** | **Description**  
`percentages` |  `MutableSequence[int]`   
Required. The percentage based deployments that will occur as a part of a `Rollout`. List is expected in ascending order and each integer n is 0 <= n="">< 100.="" if="" the="" gatewayservicemesh="" is="" configured="" for="" kubernetes,="" then="" the="" range="" for="" n="" is="" 0=""><= n=""><= 100.="">  
`verify` |  `bool`   
Optional. Whether to run verify tests after each percentage deployment via `skaffold verify`.   
`predeploy` |  `[google.cloud.deploy_v1.types.Predeploy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Predeploy)`   
Optional. Configuration for the predeploy job of the first phase. If this is not configured, there will be no predeploy job for this phase.   
`postdeploy` |  `[google.cloud.deploy_v1.types.Postdeploy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Postdeploy)`   
Optional. Configuration for the postdeploy job of the last phase. If this is not configured, there will be no postdeploy job for this phase.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
