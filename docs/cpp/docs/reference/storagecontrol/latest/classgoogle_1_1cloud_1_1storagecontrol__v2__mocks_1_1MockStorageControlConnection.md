---
url: https://docs.cloud.google.com/cpp/docs/reference/storagecontrol/latest/classgoogle_1_1cloud_1_1storagecontrol__v2__mocks_1_1MockStorageControlConnection/
title: Class MockStorageControlConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:25.526279+00:00
---

# Class MockStorageControlConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storagecontrol/latest/classgoogle_1_1cloud_1_1storagecontrol__v2__mocks_1_1MockStorageControlConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class MockStorageControlConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0 

A class to mock `StorageControlConnection`. 

Application developers may want to test their code with simulated responses, including errors, from an object of type `StorageControlClient`. To do so, construct an object of type `StorageControlClient` with an instance of this class. Then use the Google Test framework functions to program the behavior of this mock.

###### See Also

[This example](https://cloud.google.com/cpp/docs/reference/bigquery/latest/bigquery-read-mock) for how to test your application with GoogleTest. While the example showcases types from the BigQuery library, the underlying principles apply for any pair of `*Client` and `*Connection`. 

## Functions 

### virtual options()

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateFolder(google::storage::control::v2::CreateFolderRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::CreateFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::Folder >` |   
  
### virtual DeleteFolder(google::storage::control::v2::DeleteFolderRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::DeleteFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual GetFolder(google::storage::control::v2::GetFolderRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::Folder >` |   
  
### virtual ListFolders(google::storage::control::v2::ListFoldersRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ListFoldersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storage::control::v2::Folder >` |   
  
### virtual RenameFolder(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::control::v2::Folder > >` |   
  
### virtual DeleteFolderRecursive(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::control::v2::DeleteFolderRecursiveMetadata > >` |   
  
### virtual GetStorageLayout(google::storage::control::v2::GetStorageLayoutRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetStorageLayoutRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::StorageLayout >` |   
  
### virtual CreateManagedFolder(google::storage::control::v2::CreateManagedFolderRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::CreateManagedFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::ManagedFolder >` |   
  
### virtual DeleteManagedFolder(google::storage::control::v2::DeleteManagedFolderRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::DeleteManagedFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual GetManagedFolder(google::storage::control::v2::GetManagedFolderRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetManagedFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::ManagedFolder >` |   
  
### virtual ListManagedFolders(google::storage::control::v2::ListManagedFoldersRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ListManagedFoldersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storage::control::v2::ManagedFolder >` |   
  
### virtual UpdateManagedFolder(google::storage::control::v2::UpdateManagedFolderRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::UpdateManagedFolderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::ManagedFolder >` |   
  
### virtual CreateAnywhereCache(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::control::v2::AnywhereCache > >` |   
  
### virtual UpdateAnywhereCache(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::control::v2::AnywhereCache > >` |   
  
### virtual DisableAnywhereCache(google::storage::control::v2::DisableAnywhereCacheRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::DisableAnywhereCacheRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::AnywhereCache >` |   
  
### virtual PauseAnywhereCache(google::storage::control::v2::PauseAnywhereCacheRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::PauseAnywhereCacheRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::AnywhereCache >` |   
  
### virtual ResumeAnywhereCache(google::storage::control::v2::ResumeAnywhereCacheRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ResumeAnywhereCacheRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::AnywhereCache >` |   
  
### virtual GetAnywhereCache(google::storage::control::v2::GetAnywhereCacheRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetAnywhereCacheRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::AnywhereCache >` |   
  
### virtual ListAnywhereCaches(google::storage::control::v2::ListAnywhereCachesRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ListAnywhereCachesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storage::control::v2::AnywhereCache >` |   
  
### virtual CreateRapidCache(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::control::v2::RapidCache > >` |   
  
### virtual UpdateRapidCache(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::control::v2::RapidCache > >` |   
  
### virtual DisableRapidCache(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storage::control::v2::RapidCache > >` |   
  
### virtual GetRapidCache(google::storage::control::v2::GetRapidCacheRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetRapidCacheRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::RapidCache >` |   
  
### virtual ListRapidCaches(google::storage::control::v2::ListRapidCachesRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ListRapidCachesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storage::control::v2::RapidCache >` |   
  
### virtual GetProjectIntelligenceConfig(google::storage::control::v2::GetProjectIntelligenceConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetProjectIntelligenceConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceConfig >` |   
  
### virtual UpdateProjectIntelligenceConfig(google::storage::control::v2::UpdateProjectIntelligenceConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::UpdateProjectIntelligenceConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceConfig >` |   
  
### virtual GetFolderIntelligenceConfig(google::storage::control::v2::GetFolderIntelligenceConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetFolderIntelligenceConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceConfig >` |   
  
### virtual UpdateFolderIntelligenceConfig(google::storage::control::v2::UpdateFolderIntelligenceConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::UpdateFolderIntelligenceConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceConfig >` |   
  
### virtual GetOrganizationIntelligenceConfig(google::storage::control::v2::GetOrganizationIntelligenceConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetOrganizationIntelligenceConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceConfig >` |   
  
### virtual UpdateOrganizationIntelligenceConfig(google::storage::control::v2::UpdateOrganizationIntelligenceConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::UpdateOrganizationIntelligenceConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceConfig >` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::TestIamPermissionsResponse >` |   
  
### virtual GetIntelligenceFinding(google::storage::control::v2::GetIntelligenceFindingRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetIntelligenceFindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceFinding >` |   
  
### virtual ListIntelligenceFindings(google::storage::control::v2::ListIntelligenceFindingsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ListIntelligenceFindingsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storage::control::v2::IntelligenceFinding >` |   
  
### virtual SummarizeIntelligenceFindings(google::storage::control::v2::SummarizeIntelligenceFindingsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::SummarizeIntelligenceFindingsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storage::control::v2::FindingSummary >` |   
  
### virtual GetIntelligenceFindingRevision(google::storage::control::v2::GetIntelligenceFindingRevisionRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::GetIntelligenceFindingRevisionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::IntelligenceFindingRevision >` |   
  
### virtual ListIntelligenceFindingRevisions(google::storage::control::v2::ListIntelligenceFindingRevisionsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ListIntelligenceFindingRevisionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storage::control::v2::IntelligenceFindingRevision >` |   
  
### virtual ViewObjectFullContext(google::storage::control::v2::ViewObjectFullContextRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storage::control::v2::ViewObjectFullContextRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storage::control::v2::ObjectFullContext >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
