---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations/getAwsServerConfig/
title: Method: projects.locations.getAwsServerConfig \u00a0|\u00a0 GKE Multi-Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:53.136416+00:00
---

# Method: projects.locations.getAwsServerConfig  |  GKE Multi-Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations/getAwsServerConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE Multi-Cloud Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations)



Send feedback 

#  Method: projects.locations.getAwsServerConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * AwsK8sVersionInfo
    * JSON representation



GKE-on-AWS is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement> for more details.

Returns information, such as supported AWS regions and Kubernetes versions, on a given Google Cloud location.

### HTTP request

`GET https://{endpoint}/v1/{name=projects/*/locations/*/awsServerConfig}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `[AwsServerConfig](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations/getAwsServerConfig#body.AwsServerConfig)` resource to describe.`AwsServerConfig` names are formatted as `projects/<project-id>/locations/<region>/awsServerConfig`.See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names.  
  
### Request body

The request body must be empty.

### Response body

GKE-on-AWS is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement> for more details.

AwsServerConfig is the configuration of GKE cluster on AWS.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "validVersions": [
        {
          object ([AwsK8sVersionInfo](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations/getAwsServerConfig#AwsK8sVersionInfo))
        }
      ],
      "supportedAwsRegions": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the config.  
`validVersions[]` |  `object (`[AwsK8sVersionInfo](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations/getAwsServerConfig#AwsK8sVersionInfo)`)` List of all released Kubernetes versions, including ones which are end of life and can no longer be used. Filter by the `enabled` property to limit to currently available versions. Valid versions supported for both create and update operations  
`supportedAwsRegions[]` |  `string` The list of supported AWS regions.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `gkemulticloud.awsServerConfigs.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AwsK8sVersionInfo

GKE-on-AWS is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement> for more details.

Kubernetes version information of GKE cluster on AWS.

JSON representation  
---  
      
    
    {
      "version": string,
      "enabled": boolean,
      "endOfLife": boolean,
      "endOfLifeDate": {
        object ([Date](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/Date))
      },
      "releaseDate": {
        object ([Date](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/Date))
      }
    }  
  
Fields  
---  
`version` |  `string` Kubernetes version name.  
`enabled` |  `boolean` Optional. True if the version is available for cluster creation. If a version is enabled for creation, it can be used to create new clusters. Otherwise, cluster creation will fail. However, cluster upgrade operations may succeed, even if the version is not enabled.  
`endOfLife` |  `boolean` Optional. True if this cluster version belongs to a minor version that has reached its end of life and is no longer in scope to receive security and bug fixes.  
`endOfLifeDate` |  `object (`[Date](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/Date)`)` Optional. The estimated date (in Pacific Time) when this cluster version will reach its end of life. Or if this version is no longer supported (the `endOfLife` field is true), this is the actual date (in Pacific time) when the version reached its end of life.  
`releaseDate` |  `object (`[Date](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/Date)`)` Optional. The date (in Pacific Time) when the cluster version was released.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
