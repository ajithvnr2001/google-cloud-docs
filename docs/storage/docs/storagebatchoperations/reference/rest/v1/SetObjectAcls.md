---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls/
title: SetObjectAcls \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:39:08.863446+00:00
---

# SetObjectAcls  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  SetObjectAcls Stay organized with collections  Save and categorize content based on your preferences. 

Describes options for setting object ACLs.

JSON representation  
---  
      
    
    {
      "accessControlsUpdates": {
        object ([AccessControlsUpdates](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls#AccessControlsUpdates))
      }
    }  
  
Fields  
---  
`accessControlsUpdates` |  `object (`[AccessControlsUpdates](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls#AccessControlsUpdates)`)` Required. Add, update, or remove grants from the object's existing ACLs.  
  
## AccessControlsUpdates

Represents updates to existing access-control entries on an object.

JSON representation  
---  
      
    
    {
      "grants": [
        {
          object ([ObjectAccessControl](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls#ObjectAccessControl))
        }
      ],
      "removeEntities": [
        string
      ]
    }  
  
Fields  
---  
`grants[]` |  `object (`[ObjectAccessControl](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/SetObjectAcls#ObjectAccessControl)`)` Optional. Grants to add or update. If a grant for same entity exists, its role is updated.  
`removeEntities[]` |  `string` Optional. Entities for which all grants should be removed. An entity can't be in both `grants` and `removeEntities`.  
  
## ObjectAccessControl

Represents an access control entry on an object.

JSON representation  
---  
      
    
    {
      "entity": string,
      "role": string
    }  
  
Fields  
---  
`entity` |  `string` Required. The entity holding the permission, in one of the following forms:

  * `allUsers`
  * `allAuthenticatedUsers`

  
`role` |  `string` Required. The role to grant. Acceptable values are:

  * `READER` \- gives read access to the object.
  * `OWNER` \- gives owner access to the object.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
