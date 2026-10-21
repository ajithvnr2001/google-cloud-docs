---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action/
title: Action \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:46.996437+00:00
---

# Action  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Action Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * CloudSQLFailover
    * JSON representation
  * L7LBHTTPFault
    * JSON representation
  * HTTPAbort
    * JSON representation
  * HTTPDelay
    * JSON representation
  * GCEFailCompute
    * JSON representation
  * MigElement
    * JSON representation
  * InstanceList
    * JSON representation
  * GKEFailCompute
    * JSON representation



The action to be performed by the experiment.

JSON representation  
---  
      
    
    {
    
      // Union field action can be only one of the following:
      "cloudSqlFailover": {
        object ([CloudSQLFailover](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#CloudSQLFailover))
      },
      "l7LbHttpFault": {
        object ([L7LBHTTPFault](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#L7LBHTTPFault))
      },
      "gceFailCompute": {
        object ([GCEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#GCEFailCompute))
      },
      "gkeFailCompute": {
        object ([GKEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#GKEFailCompute))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
Union field `action`. Details about the fault-injection action. `action` can be only one of the following:  
`cloudSqlFailover` |  `object (`[CloudSQLFailover](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#CloudSQLFailover)`)` Specifies a CloudSQLFailover action.  
`l7LbHttpFault` |  `object (`[L7LBHTTPFault](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#L7LBHTTPFault)`)` Specifies an L7LBHTTPFault action.  
`gceFailCompute` |  `object (`[GCEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#GCEFailCompute)`)` Specifies a GCEFailCompute action.  
`gkeFailCompute` |  `object (`[GKEFailCompute](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#GKEFailCompute)`)` Specifies a GKEFailCompute action.  
  
## CloudSQLFailover

CloudSQLFailover causes a Cloud SQL primary instance to fail over to another instance.

JSON representation  
---  
      
    
    {
      "instance": string
    }  
  
Fields  
---  
`instance` |  `string` Required. The identifying name of the Cloud SQL instance to fail over. Format: `projects/{project}/instances/{instance}`  
  
## L7LBHTTPFault

Injection of HTTP faults into a layer 7 load balancer.

JSON representation  
---  
      
    
    {
      "forwardingRule": string,
      "backendService": string,
    
      // Union field fault can be only one of the following:
      "abort": {
        object ([HTTPAbort](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#HTTPAbort))
      },
      "delay": {
        object ([HTTPDelay](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#HTTPDelay))
      }
      // End of list of possible types for union field fault.
    }  
  
Fields  
---  
`forwardingRule` |  `string` Required. The identifying name of the forwarding rule resource where the faults will be injected. Format: `projects/{project}/regions/{region}/forwardingRules/{forwardingRule}` or `projects/{project}/global/forwardingRules/{forwardingRule}`  
`backendService` |  `string` Optional. Optional identifying name of the backend service to inject faults into. Format: `projects/{project}/regions/{region}/backendServices/{backendService}` or `projects/{project}/global/backendServices/{backendService}` If not specified, all backend services connected to the forwardingRule will be affected.  
Union field `fault`. The fault to be injected. Can inject either an HTTP error code or a delay. `fault` can be only one of the following:  
`abort` |  `object (`[HTTPAbort](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#HTTPAbort)`)` Returns an HTTP error code for some requests.  
`delay` |  `object (`[HTTPDelay](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#HTTPDelay)`)` Delays some HTTP responses.  
  
## HTTPAbort

Artificially return a specific HTTP status code for a percentage of requests.

JSON representation  
---  
      
    
    {
      "statusCode": integer,
      "percentage": integer
    }  
  
Fields  
---  
`statusCode` |  `integer` Required. HTTP status code to return. In the range 500 to 599, inclusive.  
`percentage` |  `integer` Required. Percentage of requests to abort, in the range 0 to 100, inclusive.  
  
## HTTPDelay

Artificially delay HTTP responses for a percentage of requests.

JSON representation  
---  
      
    
    {
      "percentage": integer,
      "delay": string
    }  
  
Fields  
---  
`percentage` |  `integer` Required. Percentage of requests to delay, in the range 0 to 100, inclusive.  
`delay` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. Delay duration.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## GCEFailCompute

GCEFailCompute specifies which instances to fail.

JSON representation  
---  
      
    
    {
    
      // Union field specifier can be only one of the following:
      "secureTagValue": string,
      "mig": {
        object ([MigElement](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#MigElement))
      },
      "location": string,
      "instances": {
        object ([InstanceList](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#InstanceList))
      }
      // End of list of possible types for union field specifier.
    }  
  
Fields  
---  
Union field `specifier`. Use one of these elements to specify which GCE instance(s) to fail. `specifier` can be only one of the following:  
`secureTagValue` |  `string` Specifies a group of non-MIG (Managed Instance Group) instances by secure tag. See <https://cloud.google.com/firewall/docs/tags-firewalls-overview> for more details on tags. Format: `{project}/{tag_key}/{tag_value}`.  
`mig` |  `object (`[MigElement](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#MigElement)`)` Specifies a managed instance group. Can be zonal or regional.  
`location` |  `string` Specifies that an entire zone or region should be affected.  
`instances` |  `object (`[InstanceList](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Action#InstanceList)`)` Specifies a list of instances.  
  
## MigElement

Details specifying a Managed Instance Group (MIG) and optionally a zone within it.

JSON representation  
---  
      
    
    {
      "instanceGroupManager": string,
      "location": string
    }  
  
Fields  
---  
`instanceGroupManager` |  `string` Required. Specifies the manager of a managed instance group. Can be zonal or regional. Format: `projects/{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}` or `projects/{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}`  
`location` |  `string` Optional. Optionally specify a zone location to further restrict a regional MIG.  
  
## InstanceList

A GCEFailCompute option for failing multiple instances by name.

JSON representation  
---  
      
    
    {
      "instances": [
        string
      ]
    }  
  
Fields  
---  
`instances[]` |  `string` Required. Specifies instances by name. Format: `projects/{project}/zones/{zone}/instances/{instance}`  
  
## GKEFailCompute

GKEFailCompute specifies infrastructure or workload to fail.

JSON representation  
---  
      
    
    {
      "cluster": string,
      "location": string,
      "k8sNamespace": [
        string
      ]
    }  
  
Fields  
---  
`cluster` |  `string` Required. Options for selecting which GKE resources to fail. The GKE cluster resource name. Format: `projects/{project}/locations/{location}/clusters/{cluster}`  
`location` |  `string` Optional. Specifies a zone or region location.  
`k8sNamespace[]` |  `string` Optional. Specifies one or more Kubernetes namespaces.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
