---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances/create/
title: Method: projects.instances.create \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:17.111588+00:00
---

# Method: projects.instances.create  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Method: projects.instances.create Stay organized with collections  Save and categorize content based on your preferences. 

Create an instance within a project.

Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serveNodes is set to non-zero, then the cluster is manually scaled. If clusterConfig.cluster_autoscaling_config is non-empty, then autoscaling is enabled.

### HTTP request

`POST https://bigtableadmin.googleapis.com/v2/{parent=projects/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The unique name of the project in which to create the new instance. Values are of the form `projects/{project}`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `bigtable.instances.create`
  * `bigtable.clusters.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instanceId": string,
      "instance": {
        object ([Instance](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances#Instance))
      },
      "clusters": {
        string: {
          object ([Cluster](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#Cluster))
        },
        ...
      }
    }  
  
Fields  
---  
`instanceId` |  `string` Required. The ID to be used when referring to the new instance within its project, e.g., just `myinstance` rather than `projects/myproject/instances/myinstance`.  
`instance` |  `object (`[Instance](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances#Instance)`)` Required. The instance to create. Fields marked `OutputOnly` must be left blank.  
`clusters` |  `map (key: string, value: object (`[Cluster](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters#Cluster)`))` Required. The clusters to be created within the instance, mapped by desired cluster ID, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`. Fields marked `OutputOnly` must be left blank.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigtable.admin`
  * `https://www.googleapis.com/auth/bigtable.admin.cluster`
  * `https://www.googleapis.com/auth/bigtable.admin.instance`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin.cluster`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-03 UTC."],[],[]] 
