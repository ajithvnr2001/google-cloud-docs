---
url: https://docs.cloud.google.com/cpp/docs/reference/video/latest/classgoogle_1_1cloud_1_1video__livestream__v1_1_1LivestreamServiceConnectionIdempotencyPolicy/
title: Class LivestreamServiceConnectionIdempotencyPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:00.245234+00:00
---

# Class LivestreamServiceConnectionIdempotencyPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/video/latest/classgoogle_1_1cloud_1_1video__livestream__v1_1_1LivestreamServiceConnectionIdempotencyPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class LivestreamServiceConnectionIdempotencyPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

## Functions 

### virtual clone() const

Create a new copy of this object. 

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< LivestreamServiceConnectionIdempotencyPolicy >` |   
  
### virtual CreateChannel(google::cloud::video::livestream::v1::CreateChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::CreateChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListChannels(google::cloud::video::livestream::v1::ListChannelsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::ListChannelsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetChannel(google::cloud::video::livestream::v1::GetChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::GetChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteChannel(google::cloud::video::livestream::v1::DeleteChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::DeleteChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateChannel(google::cloud::video::livestream::v1::UpdateChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::UpdateChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual StartChannel(google::cloud::video::livestream::v1::StartChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::StartChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual StopChannel(google::cloud::video::livestream::v1::StopChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::StopChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual StartDistribution(google::cloud::video::livestream::v1::StartDistributionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::StartDistributionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual StopDistribution(google::cloud::video::livestream::v1::StopDistributionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::StopDistributionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateInput(google::cloud::video::livestream::v1::CreateInputRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::CreateInputRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListInputs(google::cloud::video::livestream::v1::ListInputsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::ListInputsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetInput(google::cloud::video::livestream::v1::GetInputRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::GetInputRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteInput(google::cloud::video::livestream::v1::DeleteInputRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::DeleteInputRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateInput(google::cloud::video::livestream::v1::UpdateInputRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::UpdateInputRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual PreviewInput(google::cloud::video::livestream::v1::PreviewInputRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::PreviewInputRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateEvent(google::cloud::video::livestream::v1::CreateEventRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::CreateEventRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListEvents(google::cloud::video::livestream::v1::ListEventsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::ListEventsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetEvent(google::cloud::video::livestream::v1::GetEventRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::GetEventRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteEvent(google::cloud::video::livestream::v1::DeleteEventRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::DeleteEventRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListClips(google::cloud::video::livestream::v1::ListClipsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::ListClipsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetClip(google::cloud::video::livestream::v1::GetClipRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::GetClipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateClip(google::cloud::video::livestream::v1::CreateClipRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::CreateClipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteClip(google::cloud::video::livestream::v1::DeleteClipRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::DeleteClipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateDvrSession(google::cloud::video::livestream::v1::CreateDvrSessionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::CreateDvrSessionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListDvrSessions(google::cloud::video::livestream::v1::ListDvrSessionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::ListDvrSessionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetDvrSession(google::cloud::video::livestream::v1::GetDvrSessionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::GetDvrSessionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteDvrSession(google::cloud::video::livestream::v1::DeleteDvrSessionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::DeleteDvrSessionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateDvrSession(google::cloud::video::livestream::v1::UpdateDvrSessionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::UpdateDvrSessionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateAsset(google::cloud::video::livestream::v1::CreateAssetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::CreateAssetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteAsset(google::cloud::video::livestream::v1::DeleteAssetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::DeleteAssetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetAsset(google::cloud::video::livestream::v1::GetAssetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::GetAssetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListAssets(google::cloud::video::livestream::v1::ListAssetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::ListAssetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetPool(google::cloud::video::livestream::v1::GetPoolRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::GetPoolRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdatePool(google::cloud::video::livestream::v1::UpdatePoolRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::video::livestream::v1::UpdatePoolRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
