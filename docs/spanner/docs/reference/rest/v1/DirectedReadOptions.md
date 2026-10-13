---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions/
title: DirectedReadOptions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:17.479798+00:00
---

# DirectedReadOptions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  DirectedReadOptions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * IncludeReplicas
    * JSON representation
  * ReplicaSelection
    * JSON representation
  * Type
  * ExcludeReplicas
    * JSON representation



The `DirectedReadOptions` can be used to indicate which replicas or regions should be used for non-transactional reads or queries.

`DirectedReadOptions` can only be specified for a read-only transaction, otherwise the API returns an `INVALID_ARGUMENT` error.

JSON representation  
---  
      
    
    {
    
      // Union field replicas can be only one of the following:
      "includeReplicas": {
        object ([IncludeReplicas](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#IncludeReplicas))
      },
      "excludeReplicas": {
        object ([ExcludeReplicas](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#ExcludeReplicas))
      }
      // End of list of possible types for union field replicas.
    }  
  
Fields  
---  
Union field `replicas`. Required. At most one of either `include_replicas` or `exclude_replicas` should be present in the message. `replicas` can be only one of the following:  
`includeReplicas` |  `object (`[IncludeReplicas](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#IncludeReplicas)`)` `Include_replicas` indicates the order of replicas (as they appear in this list) to process the request. If `autoFailoverDisabled` is set to `true` and all replicas are exhausted without finding a healthy replica, Spanner waits for a replica in the list to become available, requests might fail due to `DEADLINE_EXCEEDED` errors.  
`excludeReplicas` |  `object (`[ExcludeReplicas](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#ExcludeReplicas)`)` `Exclude_replicas` indicates that specified replicas should be excluded from serving requests. Spanner doesn't route requests to the replicas in this list.  
  
## IncludeReplicas

An `IncludeReplicas` contains a repeated set of `ReplicaSelection` which indicates the order in which replicas should be considered.

JSON representation  
---  
      
    
    {
      "replicaSelections": [
        {
          object ([ReplicaSelection](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#ReplicaSelection))
        }
      ],
      "autoFailoverDisabled": boolean
    }  
  
Fields  
---  
`replicaSelections[]` |  `object (`[ReplicaSelection](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#ReplicaSelection)`)` The directed read replica selector.  
`autoFailoverDisabled` |  `boolean` If `true`, Spanner doesn't route requests to a replica outside the <`includeReplicas` list when all of the specified replicas are unavailable or unhealthy. Default value is `false`.  
  
## ReplicaSelection

The directed read replica selector. Callers must provide one or more of the following fields for replica selection:

  * `location` \- The location must be one of the regions within the multi-region configuration of your database.
  * `type` \- The type of the replica.



Some examples of using replica_selectors are:

  * `location:us-east1` \--> The "us-east1" replica(s) of any available type is used to process the request.
  * `type:READ_ONLY` \--> The "READ_ONLY" type replica(s) in the nearest available location are used to process the request.
  * `location:us-east1 type:READ_ONLY` \--> The "READ_ONLY" type replica(s) in location "us-east1" is used to process the request.

JSON representation  
---  
      
    
    {
      "location": string,
      "type": enum ([Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#Type))
    }  
  
Fields  
---  
`location` |  `string` The location or region of the serving requests, for example, "us-east1".  
`type` |  `enum (`[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#Type)`)` The type of replica.  
  
## Type

Indicates the type of replica.

Enums  
---  
`TYPE_UNSPECIFIED` | Not specified.  
`READ_WRITE` | sessions.read-write replicas support both reads and writes.  
`READ_ONLY` | sessions.read-only replicas only support reads (not writes).  
  
## ExcludeReplicas

An ExcludeReplicas contains a repeated set of ReplicaSelection that should be excluded from serving requests.

JSON representation  
---  
      
    
    {
      "replicaSelections": [
        {
          object ([ReplicaSelection](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#ReplicaSelection))
        }
      ]
    }  
  
Fields  
---  
`replicaSelections[]` |  `object (`[ReplicaSelection](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions#ReplicaSelection)`)` The directed read replica selector.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
