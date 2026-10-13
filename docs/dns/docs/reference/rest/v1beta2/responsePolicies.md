---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/
title: REST Resource: responsePolicies \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:28.481605+00:00
---

# REST Resource: responsePolicies  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: responsePolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ResponsePolicy
    * JSON representation
  * Network
    * JSON representation
  * GKECluster
    * JSON representation
  * Methods



## Resource: ResponsePolicy

A Response Policy is a collection of selectors that apply to queries made against one or more Virtual Private Cloud networks.

JSON representation  
---  
      
    
    {
      "id": string,
      "responsePolicyName": string,
      "description": string,
      "networks": [
        {
          object ([Network](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies#Network))
        }
      ],
      "gkeClusters": [
        {
          object ([GKECluster](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies#GKECluster))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "kind": string
    }  
  
Fields  
---  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Unique identifier for the resource; defined by the server (output only).  
`responsePolicyName` |  `string` User assigned name for this Response Policy.  
`description` |  `string` User-provided description for this Response Policy.  
`networks[]` |  `object (`[Network](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies#Network)`)` responsePolicies.list of network names specifying networks to which this policy is applied.  
`gkeClusters[]` |  `object (`[GKECluster](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies#GKECluster)`)` The list of Google Kubernetes Engine clusters to which this response policy is applied.  
`labels` |  `map (key: string, value: string)` User labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`kind` |  `string`  
  
## Network

JSON representation  
---  
      
    
    {
      "networkUrl": string,
      "kind": string
    }  
  
Fields  
---  
`networkUrl` |  `string` The fully qualified URL of the VPC network to bind to. This should be formatted like `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`  
`kind` |  `string`  
  
## GKECluster

JSON representation  
---  
      
    
    {
      "gkeClusterName": string,
      "kind": string
    }  
  
Fields  
---  
`gkeClusterName` |  `string` The resource name of the cluster to bind this response policy to. This should be specified in the format like: projects/*/locations/*/clusters/*. This is referenced from GKE projects.locations.clusters.get API: <https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/get>  
`kind` |  `string`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/create)`

|  Creates a new Response Policy  
  
### `[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/delete)`

|  Deletes a previously created Response Policy.  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/get)`

|  Fetches the representation of an existing Response Policy.  
  
### `[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/list)`

|  Enumerates all Response Policies associated with a project.  
  
### `[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/patch)`

|  Applies a partial update to an existing Response Policy.  
  
### `[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/update)`

|  Updates an existing Response Policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
