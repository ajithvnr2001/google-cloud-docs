---
url: https://docs.cloud.google.com/api-keys/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:39.820327+00:00
---

# Access control with IAM  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Guides ](https://docs.cloud.google.com/api-keys/docs/how-to)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

API Keys uses [Identity and Access Management](https://docs.cloud.google.com/iam) to manage access to the keys. This page explains the IAM roles and permissions related to API Keys and how to use them to control access.

## IAM permissions

The following table shows the required permissions for each API Keys API method. This information is also documented in the [API Reference](https://docs.cloud.google.com/api-keys/docs/reference/rest).

Method | Required Permission(s)  
---|---  
`projects.locations.keys.create` |  `apikeys.keys.create`  
`projects.locations.keys.delete` | `apikeys.keys.delete`  
`projects.locations.keys.get` | `apikeys.keys.get`  
`projects.locations.keys.getKeyString` | `apikeys.keys.getKeyString`  
`projects.locations.keys.list` | `apikeys.keys.list`  
`projects.locations.keys.patch` | `apikeys.keys.update`  
`projects.locations.keys.undelete` | `apikeys.keys.undelete`  
`operations.get` |  `serviceusage.operations.get`  
  
`keys.lookupKey` |  `apikeys.keys.undelete`  
  
  
## IAM roles

With Identity and Access Management, permissions are granted by binding users to roles. For more information about roles and permissions see [Understanding Roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

The following table lists the predefined roles that apply to API Keys.

Role | Permissions  
---|---  
`roles/viewer` |  apikeys.keys.get  
apikeys.keys.lookup  
apikeys.keys.list  
apikeys.keys.getKeyString  
  
`roles/editor` and  
`roles/owner` |  apikeys.keys.get  
apikeys.keys.lookup  
apikeys.keys.list  
apikeys.keys.getKeyString  
apikeys.keys.create  
apikeys.keys.delete  
apikeys.keys.undelete  
apikeys.keys.update  
serviceusage.operations.get  
  
`roles/serviceusage.apiKeysViewer` |  apikeys.keys.get  
apikeys.keys.lookup  
apikeys.keys.list  
apikeys.keys.getKeyString  
  
`roles/serviceusage.apiKeysAdmin` |  apikeys.keys.get  
apikeys.keys.lookup  
apikeys.keys.list  
apikeys.keys.getKeyString  
apikeys.keys.create  
apikeys.keys.delete  
apikeys.keys.undelete  
apikeys.keys.update  
serviceusage.operations.get  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
