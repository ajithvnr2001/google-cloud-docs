---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest.DeploymentReferencePolicy
title: Class DeploymentReferencePolicy (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:38.452542+00:00
---

# Class DeploymentReferencePolicy (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest.DeploymentReferencePolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeploymentReferencePolicy (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    DeploymentReferencePolicy(value)

Policy on how to handle referenced deployments when deleting the DeploymentGroup.

## Enums  
  
---  
**Name** | **Description**  
`DEPLOYMENT_REFERENCE_POLICY_UNSPECIFIED` | The default behavior. If unspecified, the system will act as if `FAIL_IF_ANY_REFERENCES_EXIST` is specified.  
`FAIL_IF_ANY_REFERENCES_EXIST` | Fail the deletion if any deployments currently referenced in the `deployment_units` of the DeploymentGroup or in the latest revision are not deleted.  
`FAIL_IF_METADATA_REFERENCES_EXIST` | Fail the deletion only if any deployments currently referenced in the `deployment_units` of the DeploymentGroup are not deleted. The deletion will proceed even if the deployments in the latest revision of the DeploymentGroup are not deleted.  
`IGNORE_DEPLOYMENT_REFERENCES` | Ignore any deployments currently referenced in the `deployment_units` of the DeploymentGroup or in the latest revision.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
