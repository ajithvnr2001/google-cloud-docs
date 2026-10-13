---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadRecreateInstallScript/
title: Method: projects.locations.networkMonitoringProviders.monitoringPoints.downloadRecreateInstallScript \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:42.721745+00:00
---

# Method: projects.locations.networkMonitoringProviders.monitoringPoints.downloadRecreateInstallScript  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadRecreateInstallScript/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.networkMonitoringProviders.monitoringPoints.downloadRecreateInstallScript Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Downloads an install script for a specific Container MonitoringPoint.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1alpha1/{name=projects/*/locations/*/networkMonitoringProviders/*/monitoringPoints/*}:downloadRecreateInstallScript`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Resource name of the MonitoringPoint. Format: projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}/monitoringPoints/{monitoring_point}  
  
### Query parameters

Parameters  
---  
`hostname` |  `string` Optional. The hostname of the MonitoringPoint, e.g. "test-vm"  
  
### Request body

The request body must be empty.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `networkmanagement.monitoringPoints.downloadConfig`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-17 UTC."],[],[]] 
