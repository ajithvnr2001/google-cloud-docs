---
url: https://docs.cloud.google.com/cpp/docs/reference/logging/latest/classgoogle_1_1cloud_1_1logging__v2_1_1ConfigServiceV2Connection/
title: Class ConfigServiceV2Connection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:55.906824+00:00
---

# Class ConfigServiceV2Connection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/logging/latest/classgoogle_1_1cloud_1_1logging__v2_1_1ConfigServiceV2Connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ConfigServiceV2Connection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`ConfigServiceV2Connection`](https://docs.cloud.google.com/cpp/docs/reference/logging/latest/classgoogle_1_1cloud_1_1logging__v2_1_1ConfigServiceV2Connection) object for [`ConfigServiceV2Client`](https://docs.cloud.google.com/cpp/docs/reference/logging/latest/classgoogle_1_1cloud_1_1logging__v2_1_1ConfigServiceV2Client). 

This interface defines virtual methods for each of the user-facing overload sets in [`ConfigServiceV2Client`](https://docs.cloud.google.com/cpp/docs/reference/logging/latest/classgoogle_1_1cloud_1_1logging__v2_1_1ConfigServiceV2Client). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`ConfigServiceV2Client`](https://docs.cloud.google.com/cpp/docs/reference/logging/latest/classgoogle_1_1cloud_1_1logging__v2_1_1ConfigServiceV2Client).

To create a concrete instance, see [`MakeConfigServiceV2Connection()`](https://docs.cloud.google.com/cpp/docs/reference/logging/latest/namespacegoogle_1_1cloud_1_1logging__v2).

For mocking, see [`logging_v2_mocks::MockConfigServiceV2Connection`](https://docs.cloud.google.com/cpp/docs/reference/logging/latest/classgoogle_1_1cloud_1_1logging__v2__mocks_1_1MockConfigServiceV2Connection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListBuckets(google::logging::v2::ListBucketsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::ListBucketsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::logging::v2::LogBucket >` |   
  
### virtual GetBucket(google::logging::v2::GetBucketRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::GetBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogBucket >` |   
  
### virtual CreateBucketAsync(google::logging::v2::CreateBucketRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::CreateBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::LogBucket > >` |   
  
### virtual CreateBucketAsync(NoAwaitTag, google::logging::v2::CreateBucketRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::logging::v2::CreateBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateBucketAsync(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::LogBucket > >` |   
  
### virtual UpdateBucketAsync(google::logging::v2::UpdateBucketRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UpdateBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::LogBucket > >` |   
  
### virtual UpdateBucketAsync(NoAwaitTag, google::logging::v2::UpdateBucketRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::logging::v2::UpdateBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateBucketAsync(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::LogBucket > >` |   
  
### virtual CreateBucket(google::logging::v2::CreateBucketRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::CreateBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogBucket >` |   
  
### virtual UpdateBucket(google::logging::v2::UpdateBucketRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UpdateBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogBucket >` |   
  
### virtual DeleteBucket(google::logging::v2::DeleteBucketRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::DeleteBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual UndeleteBucket(google::logging::v2::UndeleteBucketRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UndeleteBucketRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual ListViews(google::logging::v2::ListViewsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::ListViewsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::logging::v2::LogView >` |   
  
### virtual GetView(google::logging::v2::GetViewRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::GetViewRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogView >` |   
  
### virtual CreateView(google::logging::v2::CreateViewRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::CreateViewRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogView >` |   
  
### virtual UpdateView(google::logging::v2::UpdateViewRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UpdateViewRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogView >` |   
  
### virtual DeleteView(google::logging::v2::DeleteViewRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::DeleteViewRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual ListSinks(google::logging::v2::ListSinksRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::ListSinksRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::logging::v2::LogSink >` |   
  
### virtual GetSink(google::logging::v2::GetSinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::GetSinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogSink >` |   
  
### virtual CreateSink(google::logging::v2::CreateSinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::CreateSinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogSink >` |   
  
### virtual UpdateSink(google::logging::v2::UpdateSinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UpdateSinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogSink >` |   
  
### virtual DeleteSink(google::logging::v2::DeleteSinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::DeleteSinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CreateLink(google::logging::v2::CreateLinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::CreateLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::Link > >` |   
  
### virtual CreateLink(NoAwaitTag, google::logging::v2::CreateLinkRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::logging::v2::CreateLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateLink(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::Link > >` |   
  
### virtual DeleteLink(google::logging::v2::DeleteLinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::DeleteLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::LinkMetadata > >` |   
  
### virtual DeleteLink(NoAwaitTag, google::logging::v2::DeleteLinkRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::logging::v2::DeleteLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteLink(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::LinkMetadata > >` |   
  
### virtual ListLinks(google::logging::v2::ListLinksRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::ListLinksRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::logging::v2::Link >` |   
  
### virtual GetLink(google::logging::v2::GetLinkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::GetLinkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::Link >` |   
  
### virtual ListExclusions(google::logging::v2::ListExclusionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::ListExclusionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::logging::v2::LogExclusion >` |   
  
### virtual GetExclusion(google::logging::v2::GetExclusionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::GetExclusionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogExclusion >` |   
  
### virtual CreateExclusion(google::logging::v2::CreateExclusionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::CreateExclusionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogExclusion >` |   
  
### virtual UpdateExclusion(google::logging::v2::UpdateExclusionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UpdateExclusionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::LogExclusion >` |   
  
### virtual DeleteExclusion(google::logging::v2::DeleteExclusionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::DeleteExclusionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual GetCmekSettings(google::logging::v2::GetCmekSettingsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::GetCmekSettingsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::CmekSettings >` |   
  
### virtual UpdateCmekSettings(google::logging::v2::UpdateCmekSettingsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UpdateCmekSettingsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::CmekSettings >` |   
  
### virtual GetSettings(google::logging::v2::GetSettingsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::GetSettingsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::Settings >` |   
  
### virtual UpdateSettings(google::logging::v2::UpdateSettingsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::UpdateSettingsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::logging::v2::Settings >` |   
  
### virtual CopyLogEntries(google::logging::v2::CopyLogEntriesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::logging::v2::CopyLogEntriesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::CopyLogEntriesResponse > >` |   
  
### virtual CopyLogEntries(NoAwaitTag, google::logging::v2::CopyLogEntriesRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::logging::v2::CopyLogEntriesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CopyLogEntries(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::logging::v2::CopyLogEntriesResponse > >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
