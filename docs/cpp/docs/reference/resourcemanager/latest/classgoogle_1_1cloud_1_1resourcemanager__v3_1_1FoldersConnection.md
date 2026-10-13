---
url: https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/classgoogle_1_1cloud_1_1resourcemanager__v3_1_1FoldersConnection/
title: Class FoldersConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:31.270378+00:00
---

# Class FoldersConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/classgoogle_1_1cloud_1_1resourcemanager__v3_1_1FoldersConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class FoldersConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`FoldersConnection`](https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/classgoogle_1_1cloud_1_1resourcemanager__v3_1_1FoldersConnection) object for [`FoldersClient`](https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/classgoogle_1_1cloud_1_1resourcemanager__v3_1_1FoldersClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`FoldersClient`](https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/classgoogle_1_1cloud_1_1resourcemanager__v3_1_1FoldersClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`FoldersClient`](https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/classgoogle_1_1cloud_1_1resourcemanager__v3_1_1FoldersClient).

To create a concrete instance, see [`MakeFoldersConnection()`](https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/namespacegoogle_1_1cloud_1_1resourcemanager__v3).

For mocking, see [`resourcemanager_v3_mocks::MockFoldersConnection`](https://docs.cloud.google.com/cpp/docs/reference/resourcemanager/latest/classgoogle_1_1cloud_1_1resourcemanager__v3__mocks_1_1MockFoldersConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual GetFolder(google::cloud::resourcemanager::v3::GetFolderRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::GetFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::resourcemanager::v3::Folder >` |   
  
### virtual ListFolders(google::cloud::resourcemanager::v3::ListFoldersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::ListFoldersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::resourcemanager::v3::Folder >` |   
  
### virtual SearchFolders(google::cloud::resourcemanager::v3::SearchFoldersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::SearchFoldersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::resourcemanager::v3::Folder >` |   
  
### virtual CreateFolder(google::cloud::resourcemanager::v3::CreateFolderRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::CreateFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual CreateFolder(NoAwaitTag, google::cloud::resourcemanager::v3::CreateFolderRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::resourcemanager::v3::CreateFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateFolder(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual UpdateFolder(google::cloud::resourcemanager::v3::UpdateFolderRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::UpdateFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual UpdateFolder(NoAwaitTag, google::cloud::resourcemanager::v3::UpdateFolderRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::resourcemanager::v3::UpdateFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateFolder(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual MoveFolder(google::cloud::resourcemanager::v3::MoveFolderRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::MoveFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual MoveFolder(NoAwaitTag, google::cloud::resourcemanager::v3::MoveFolderRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::resourcemanager::v3::MoveFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual MoveFolder(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual DeleteFolder(google::cloud::resourcemanager::v3::DeleteFolderRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::DeleteFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual DeleteFolder(NoAwaitTag, google::cloud::resourcemanager::v3::DeleteFolderRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::resourcemanager::v3::DeleteFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteFolder(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual UndeleteFolder(google::cloud::resourcemanager::v3::UndeleteFolderRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::resourcemanager::v3::UndeleteFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual UndeleteFolder(NoAwaitTag, google::cloud::resourcemanager::v3::UndeleteFolderRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::resourcemanager::v3::UndeleteFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UndeleteFolder(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::resourcemanager::v3::Folder > >` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::TestIamPermissionsResponse >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
