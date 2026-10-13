---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments
title: REST Resource: nodes.deployments \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:36.242299+00:00
---

# REST Resource: nodes.deployments  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  REST Resource: nodes.deployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Deployment
    * JSON representation
  * Methods



## Resource: Deployment

The Deployment.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "sasUserIds": [
        string
      ],
      "defaultBillingMode": enum ([BillingMode](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment.BillingMode)),
      "allowedBillingModes": [
        enum ([BillingMode](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment.BillingMode))
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name.  
`displayName` |  `string` The deployment's display name.  
`sasUserIds[]` |  `string` User ID used by the devices belonging to this deployment. Each deployment should be associated with one unique user ID.  
`defaultBillingMode` |  `enum (`[BillingMode](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment.BillingMode)`)` Default billing mode for the deployment and devices under it.  
`allowedBillingModes[]` |  `enum (`[BillingMode](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment.BillingMode)`)` The allowed billing modes under this deployment.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments/delete)`

|  Deletes a `[deployment](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.  
  
### `[get](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments/get)`

|  Returns a requested `[deployment](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.  
  
### `[list](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments/list)`

|  Lists `[deployments](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.  
  
### `[move](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments/move)`

|  Moves a `[deployment](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)` under another `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.nodes#Node)` or `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.  
  
### `[patch](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.deployments/patch)`

|  Updates an existing `[deployment](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments#Deployment)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
