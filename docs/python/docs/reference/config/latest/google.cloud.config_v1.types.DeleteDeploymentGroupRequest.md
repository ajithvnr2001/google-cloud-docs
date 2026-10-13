---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest
title: Class DeleteDeploymentGroupRequest (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:37.904356+00:00
---

# Class DeleteDeploymentGroupRequest (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeleteDeploymentGroupRequest (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    DeleteDeploymentGroupRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for Delete DeploymentGroup

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of DeploymentGroup in the format projects/{project_id}/locations/{location_id}/deploymentGroups/{deploymentGroup}   
`request_id` |  `str`   
Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).   
`force` |  `bool`   
Optional. If set to true, any revisions for this deployment group will also be deleted. (Otherwise, the request will only work if the deployment group has no revisions.)   
`deployment_reference_policy` |  `[google.cloud.config_v1.types.DeleteDeploymentGroupRequest.DeploymentReferencePolicy](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeleteDeploymentGroupRequest.DeploymentReferencePolicy)`   
Optional. Policy on how to handle referenced deployments when deleting the DeploymentGroup. If unspecified, the default behavior is to fail the deletion if any deployments currently referenced in the `deployment_units` of the DeploymentGroup or in the latest revision are not deleted.   
  
## Classes 

### DeploymentReferencePolicy
    
    
    DeploymentReferencePolicy(value)

Policy on how to handle referenced deployments when deleting the DeploymentGroup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
