---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.DeploymentState
title: Class DeploymentState (0.8.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:04.809568+00:00
---

# Class DeploymentState (0.8.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.DeploymentState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeploymentState (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DeploymentState(value)

The state of the deployment resource.

## Enums  
  
---  
**Name** | **Description**  
`DEPLOYMENT_STATE_UNSPECIFIED` | Default value. This value is unused.  
`DEPLOYMENT_STATE_VALIDATING` | Validating the deployment.  
`DEPLOYMENT_STATE_CREATING` | Deployment is being created.  
`DEPLOYMENT_STATE_DELETING` | Deployment is being deleted.  
`DEPLOYMENT_STATE_UPDATING` | Deployment is being updated.  
`DEPLOYMENT_STATE_FAILED` | Deployment has failed. All the changes made by the deployment were successfully rolled back. You can retry or delete a deployment that's in this state.  
`DEPLOYMENT_STATE_READY` | Deployment is successful and ready to use.  
`DEPLOYMENT_STATE_PARTIALLY_DEPLOYED` | Deployment is partially deployed. All the cloud controls weren't deployed successfully. Retrying the operation resumes from the first failed step.  
`DEPLOYMENT_STATE_PARTIALLY_DELETED` | Deployment is partially deleted. All the cloud control deployments weren't deleted successfully. Retrying the operation resumes from the first failed step.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
