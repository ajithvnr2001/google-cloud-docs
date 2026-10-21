---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig/
title: RuntimeConfig \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:10.248430+00:00
---

# RuntimeConfig  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  RuntimeConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * GKEWorkload
    * JSON representation
  * GoogleCloudRun
    * JSON representation
  * AppHubWorkload
    * JSON representation
  * AppHubService
    * JSON representation
  * State



RuntimeConfig represents the runtimes where the application is deployed.

JSON representation  
---  
      
    
    {
      "uri": string,
      "state": enum ([State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#State)),
    
      // Union field runtime can be only one of the following:
      "gkeWorkload": {
        object ([GKEWorkload](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#GKEWorkload))
      },
      "googleCloudRun": {
        object ([GoogleCloudRun](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#GoogleCloudRun))
      }
      // End of list of possible types for union field runtime.
    
      // Union field derived_from can be only one of the following:
      "appHubWorkload": {
        object ([AppHubWorkload](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#AppHubWorkload))
      },
      "appHubService": {
        object ([AppHubService](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#AppHubService))
      }
      // End of list of possible types for union field derived_from.
    }  
  
Fields  
---  
`uri` |  `string` Required. Immutable. The URI of the runtime configuration. For GKE, this is the cluster name. For Cloud Run, this is the service name.  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#State)`)` Output only. The state of the Runtime.  
Union field `runtime`. The type of the runtime. `runtime` can be only one of the following:  
`gkeWorkload` |  `object (`[GKEWorkload](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#GKEWorkload)`)` Output only. Google Kubernetes Engine runtime.  
`googleCloudRun` |  `object (`[GoogleCloudRun](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#GoogleCloudRun)`)` Output only. Cloud Run runtime.  
Union field `derived_from`. Where the runtime is derived from. `derived_from` can be only one of the following:  
`appHubWorkload` |  `object (`[AppHubWorkload](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#AppHubWorkload)`)` Output only. App Hub Workload.  
`appHubService` |  `object (`[AppHubService](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig#AppHubService)`)` Output only. App Hub Service.  
  
## GKEWorkload

GKEWorkload represents the Google Kubernetes Engine runtime.

JSON representation  
---  
      
    
    {
      "cluster": string,
      "deployment": string
    }  
  
Fields  
---  
`cluster` |  `string` Required. Immutable. The name of the GKE cluster. Format: `projects/{project}/locations/{location}/clusters/{cluster}`.  
`deployment` |  `string` Output only. The name of the GKE deployment. Format: `projects/{project}/locations/{location}/clusters/{cluster}/namespaces/{namespace}/deployments/{deployment}`.  
  
## GoogleCloudRun

GoogleCloudRun represents the Cloud Run runtime.

JSON representation  
---  
      
    
    {
      "serviceUri": string
    }  
  
Fields  
---  
`serviceUri` |  `string` Required. Immutable. The name of the Cloud Run service. Format: `projects/{project}/locations/{location}/services/{service}`.  
  
## AppHubWorkload

AppHubWorkload represents the App Hub Workload.

JSON representation  
---  
      
    
    {
      "workload": string,
      "criticality": string,
      "environment": string
    }  
  
Fields  
---  
`workload` |  `string` Required. Output only. Immutable. The name of the App Hub Workload. Format: `projects/{project}/locations/{location}/applications/{application}/workloads/{workload}`.  
`criticality` |  `string` Output only. The criticality of the App Hub Workload.  
`environment` |  `string` Output only. The environment of the App Hub Workload.  
  
## AppHubService

AppHubService represents the App Hub Service.

JSON representation  
---  
      
    
    {
      "apphubService": string,
      "criticality": string,
      "environment": string
    }  
  
Fields  
---  
`apphubService` |  `string` Required. Output only. Immutable. The name of the App Hub Service. Format: `projects/{project}/locations/{location}/applications/{application}/services/{service}`.  
`criticality` |  `string` Output only. The criticality of the App Hub Service.  
`environment` |  `string` Output only. The environment of the App Hub Service.  
  
## State

The state of the runtime in the InsightsConfig. Whether the runtime is linked to the InsightsConfig.

Enums  
---  
`STATE_UNSPECIFIED` | No state specified.  
`LINKED` | The runtime configuration has been linked to the InsightsConfig.  
`UNLINKED` | The runtime configuration has been unlinked to the InsightsConfig.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 
