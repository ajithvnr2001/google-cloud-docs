---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/
title: REST Resource: changes \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:16.905447+00:00
---

# REST Resource: changes  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: changes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Change
    * JSON representation
  * Methods



## Resource: Change

A Change represents a set of `ResourceRecordSet` additions and deletions applied atomically to a ManagedZone. ResourceRecordSets within a ManagedZone are modified by creating a new Change element in the Changes collection. In turn the Changes collection also records the past modifications to the `ResourceRecordSets` in a `ManagedZone`. The current state of the `ManagedZone` is the sum effect of applying all `Change` elements in the `Changes` collection in sequence.

JSON representation  
---  
      
    
    {
      "additions": [
        {
          object ([ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet))
        }
      ],
      "deletions": [
        {
          object ([ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet))
        }
      ],
      "startTime": string,
      "id": string,
      "status": enum ([OperationStatus](https://docs.cloud.google.com/dns/docs/reference/rest/v1/OperationStatus)),
      "isServing": boolean,
      "kind": string
    }  
  
Fields  
---  
`additions[]` |  `object (`[ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet)`)` Which ResourceRecordSets to add?  
`deletions[]` |  `object (`[ResourceRecordSet](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet)`)` Which ResourceRecordSets to remove? Must match existing data exactly.  
`startTime` |  `string` The time that this operation was started by the server (output only). This is in RFC3339 text format.  
`id` |  `string` Unique identifier for the resource; defined by the server (output only).  
`status` |  `enum (`[OperationStatus](https://docs.cloud.google.com/dns/docs/reference/rest/v1/OperationStatus)`)` Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet.  
`isServing` |  `boolean` If the DNS queries for the zone will be served.  
`kind` |  `string`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/create)`

|  Atomically updates the ResourceRecordSet collection.  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/get)`

|  Fetches the representation of an existing Change.  
  
### `[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/list)`

|  Enumerates Changes to a ResourceRecordSet collection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
