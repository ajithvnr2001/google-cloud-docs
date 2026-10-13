---
url: https://docs.cloud.google.com/deployment-manager/docs/reference/latest/
title: API Reference \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:03.528521+00:00
---

# API Reference  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/reference/latest/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  API Reference Stay organized with collections  Save and categorize content based on your preferences. 

This API reference is organized by resource type. Each resource type has one or more data representations and one or more methods.

## Resource types

  1. Deployments 
  2. Manifests 
  3. Operations 
  4. Resources 
  5. Types 



##  Deployments 

For Deployments Resource details, see the [resource representation](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments#resource) page.

Method | HTTP request | Description  
---|---|---  
URIs relative to https://www.googleapis.com/deploymentmanager/v2/projects, unless otherwise noted  
[cancelPreview](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/cancelPreview) |  `POST /project/global/deployments/deployment/cancelPreview` |  Cancels and removes the preview currently associated with the deployment.   
[delete](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/delete) |  `DELETE /project/global/deployments/deployment` |  Deletes a deployment and all of the resources in the deployment.   
[get](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/get) |  `GET /project/global/deployments/deployment` |  Gets information about a specific deployment.   
[getIamPolicy](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/getIamPolicy) |  `GET /project/global/deployments/resource/getIamPolicy` |  Gets the access control policy for a resource. May be empty if no such policy or resource exists.   
[insert](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/insert) |  `POST /project/global/deployments` |  Creates a deployment and all of the resources described by the deployment manifest.   
[list](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/list) |  `GET /project/global/deployments` |  Lists all deployments for a given project.   
[patch](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/patch) |  `PATCH /project/global/deployments/deployment` |  Patches a deployment and all of the resources described by the deployment manifest. This method supports [patch semantics](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/performance#patch).   
[setIamPolicy](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/setIamPolicy) |  `POST /project/global/deployments/resource/setIamPolicy` |  Sets the access control policy on the specified resource. Replaces any existing policy.   
[stop](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/stop) |  `POST /project/global/deployments/deployment/stop` |  Stops an ongoing operation. This does not roll back any work that has already been completed, but prevents any new work from being started.   
[testIamPermissions](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/testIamPermissions) |  `POST /project/global/deployments/resource/testIamPermissions` |  Returns permissions that a caller has on the specified resource.   
[update](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/update) |  `PUT /project/global/deployments/deployment` |  Updates a deployment and all of the resources described by the deployment manifest.   
  
##  Manifests 

For Manifests Resource details, see the [resource representation](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/manifests#resource) page.

Method | HTTP request | Description  
---|---|---  
URIs relative to https://www.googleapis.com/deploymentmanager/v2/projects, unless otherwise noted  
[get](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/manifests/get) |  `GET /project/global/deployments/deployment/manifests/manifest` |  Gets information about a specific manifest.   
[list](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/manifests/list) |  `GET /project/global/deployments/deployment/manifests` |  Lists all manifests for a given deployment.   
  
##  Operations 

For Operations Resource details, see the [resource representation](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/operations#resource) page.

Method | HTTP request | Description  
---|---|---  
URIs relative to https://www.googleapis.com/deploymentmanager/v2/projects, unless otherwise noted  
[get](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/operations/get) |  `GET /project/global/operations/operation` |  Gets information about a specific operation.   
[list](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/operations/list) |  `GET /project/global/operations` |  Lists all operations for a project.   
  
##  Resources 

For Resources Resource details, see the [resource representation](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/resources#resource) page.

Method | HTTP request | Description  
---|---|---  
URIs relative to https://www.googleapis.com/deploymentmanager/v2/projects, unless otherwise noted  
[get](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/resources/get) |  `GET /project/global/deployments/deployment/resources/resource` |  Gets information about a single resource.   
[list](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/resources/list) |  `GET /project/global/deployments/deployment/resources` |  Lists all resources in a given deployment.   
  
##  Types 

For Types Resource details, see the [resource representation](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/types#resource) page.

Method | HTTP request | Description  
---|---|---  
URIs relative to https://www.googleapis.com/deploymentmanager/v2/projects, unless otherwise noted  
[list](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/types/list) |  `GET /project/global/types` |  Lists all resource types for Deployment Manager.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
