---
url: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/Shared.Types/CreateSnapshotRequest/
title: CreateSnapshotRequest \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:06.272612+00:00
---

# CreateSnapshotRequest  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/Shared.Types/CreateSnapshotRequest/




#  CreateSnapshotRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



CreateSnapshotRequest creates a snapshot.

JSON representation  
---  
      
    
    {
      "parent": string,
      "snapshot": {
        object ([Snapshot](https://docs.cloud.google.com/netapp/docs/reference/rest/Shared.Types/Snapshot))
      },
      "snapshotId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The NetApp volume to create the snapshots of, in the format `projects/{projectId}/locations/{location}/volumes/{volumeId}`  
`snapshot` |  `object (`[Snapshot](https://docs.cloud.google.com/netapp/docs/reference/rest/Shared.Types/Snapshot)`)` Required. A snapshot resource  
`snapshotId` |  `string` Required. ID of the snapshot to create. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-23 UTC."],[],[]] 
