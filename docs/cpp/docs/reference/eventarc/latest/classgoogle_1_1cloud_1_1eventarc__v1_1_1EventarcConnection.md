---
url: https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection/
title: Class EventarcConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:27:59.810773+00:00
---

# Class EventarcConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class EventarcConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection) object for [`EventarcClient`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`EventarcClient`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`EventarcClient`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient).

To create a concrete instance, see [`MakeEventarcConnection()`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/namespacegoogle_1_1cloud_1_1eventarc__v1).

For mocking, see [`eventarc_v1_mocks::MockEventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1__mocks_1_1MockEventarcConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual GetTrigger(google::cloud::eventarc::v1::GetTriggerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetTriggerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Trigger >` |   
  
### virtual ListTriggers(google::cloud::eventarc::v1::ListTriggersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListTriggersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Trigger >` |   
  
### virtual CreateTrigger(google::cloud::eventarc::v1::CreateTriggerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateTriggerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### virtual CreateTrigger(NoAwaitTag, google::cloud::eventarc::v1::CreateTriggerRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateTriggerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateTrigger(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### virtual UpdateTrigger(google::cloud::eventarc::v1::UpdateTriggerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateTriggerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### virtual UpdateTrigger(NoAwaitTag, google::cloud::eventarc::v1::UpdateTriggerRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateTriggerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateTrigger(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### virtual DeleteTrigger(google::cloud::eventarc::v1::DeleteTriggerRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteTriggerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### virtual DeleteTrigger(NoAwaitTag, google::cloud::eventarc::v1::DeleteTriggerRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteTriggerRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteTrigger(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Trigger > >` |   
  
### virtual GetChannel(google::cloud::eventarc::v1::GetChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Channel >` |   
  
### virtual ListChannels(google::cloud::eventarc::v1::ListChannelsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListChannelsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Channel >` |   
  
### virtual CreateChannel(google::cloud::eventarc::v1::CreateChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### virtual CreateChannel(NoAwaitTag, google::cloud::eventarc::v1::CreateChannelRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateChannel(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### virtual UpdateChannel(google::cloud::eventarc::v1::UpdateChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### virtual UpdateChannel(NoAwaitTag, google::cloud::eventarc::v1::UpdateChannelRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateChannel(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### virtual DeleteChannel(google::cloud::eventarc::v1::DeleteChannelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### virtual DeleteChannel(NoAwaitTag, google::cloud::eventarc::v1::DeleteChannelRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteChannelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteChannel(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Channel > >` |   
  
### virtual GetProvider(google::cloud::eventarc::v1::GetProviderRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetProviderRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Provider >` |   
  
### virtual ListProviders(google::cloud::eventarc::v1::ListProvidersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListProvidersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Provider >` |   
  
### virtual GetChannelConnection(google::cloud::eventarc::v1::GetChannelConnectionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetChannelConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::ChannelConnection >` |   
  
### virtual ListChannelConnections(google::cloud::eventarc::v1::ListChannelConnectionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListChannelConnectionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::ChannelConnection >` |   
  
### virtual CreateChannelConnection(google::cloud::eventarc::v1::CreateChannelConnectionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateChannelConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` |   
  
### virtual CreateChannelConnection(NoAwaitTag, google::cloud::eventarc::v1::CreateChannelConnectionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateChannelConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateChannelConnection(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` |   
  
### virtual DeleteChannelConnection(google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` |   
  
### virtual DeleteChannelConnection(NoAwaitTag, google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteChannelConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteChannelConnection(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::ChannelConnection > >` |   
  
### virtual GetGoogleChannelConfig(google::cloud::eventarc::v1::GetGoogleChannelConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetGoogleChannelConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleChannelConfig >` |   
  
### virtual UpdateGoogleChannelConfig(google::cloud::eventarc::v1::UpdateGoogleChannelConfigRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateGoogleChannelConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleChannelConfig >` |   
  
### virtual GetMessageBus(google::cloud::eventarc::v1::GetMessageBusRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetMessageBusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::MessageBus >` |   
  
### virtual ListMessageBuses(google::cloud::eventarc::v1::ListMessageBusesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListMessageBusesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::MessageBus >` |   
  
### virtual ListMessageBusEnrollments(google::cloud::eventarc::v1::ListMessageBusEnrollmentsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListMessageBusEnrollmentsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::ListMessageBusEnrollmentsResponse >` |   
  
### virtual CreateMessageBus(google::cloud::eventarc::v1::CreateMessageBusRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateMessageBusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### virtual CreateMessageBus(NoAwaitTag, google::cloud::eventarc::v1::CreateMessageBusRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateMessageBusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateMessageBus(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### virtual UpdateMessageBus(google::cloud::eventarc::v1::UpdateMessageBusRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateMessageBusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### virtual UpdateMessageBus(NoAwaitTag, google::cloud::eventarc::v1::UpdateMessageBusRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateMessageBusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateMessageBus(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### virtual DeleteMessageBus(google::cloud::eventarc::v1::DeleteMessageBusRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteMessageBusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### virtual DeleteMessageBus(NoAwaitTag, google::cloud::eventarc::v1::DeleteMessageBusRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteMessageBusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteMessageBus(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::MessageBus > >` |   
  
### virtual GetEnrollment(google::cloud::eventarc::v1::GetEnrollmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetEnrollmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Enrollment >` |   
  
### virtual ListEnrollments(google::cloud::eventarc::v1::ListEnrollmentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListEnrollmentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Enrollment >` |   
  
### virtual CreateEnrollment(google::cloud::eventarc::v1::CreateEnrollmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateEnrollmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### virtual CreateEnrollment(NoAwaitTag, google::cloud::eventarc::v1::CreateEnrollmentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateEnrollmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateEnrollment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### virtual UpdateEnrollment(google::cloud::eventarc::v1::UpdateEnrollmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateEnrollmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### virtual UpdateEnrollment(NoAwaitTag, google::cloud::eventarc::v1::UpdateEnrollmentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateEnrollmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateEnrollment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### virtual DeleteEnrollment(google::cloud::eventarc::v1::DeleteEnrollmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteEnrollmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### virtual DeleteEnrollment(NoAwaitTag, google::cloud::eventarc::v1::DeleteEnrollmentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteEnrollmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteEnrollment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Enrollment > >` |   
  
### virtual GetPipeline(google::cloud::eventarc::v1::GetPipelineRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetPipelineRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::Pipeline >` |   
  
### virtual ListPipelines(google::cloud::eventarc::v1::ListPipelinesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListPipelinesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::Pipeline >` |   
  
### virtual CreatePipeline(google::cloud::eventarc::v1::CreatePipelineRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreatePipelineRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### virtual CreatePipeline(NoAwaitTag, google::cloud::eventarc::v1::CreatePipelineRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreatePipelineRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreatePipeline(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### virtual UpdatePipeline(google::cloud::eventarc::v1::UpdatePipelineRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdatePipelineRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### virtual UpdatePipeline(NoAwaitTag, google::cloud::eventarc::v1::UpdatePipelineRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdatePipelineRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdatePipeline(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### virtual DeletePipeline(google::cloud::eventarc::v1::DeletePipelineRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeletePipelineRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### virtual DeletePipeline(NoAwaitTag, google::cloud::eventarc::v1::DeletePipelineRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeletePipelineRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeletePipeline(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::Pipeline > >` |   
  
### virtual GetGoogleApiSource(google::cloud::eventarc::v1::GetGoogleApiSourceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::GetGoogleApiSourceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::eventarc::v1::GoogleApiSource >` |   
  
### virtual ListGoogleApiSources(google::cloud::eventarc::v1::ListGoogleApiSourcesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::ListGoogleApiSourcesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::eventarc::v1::GoogleApiSource >` |   
  
### virtual CreateGoogleApiSource(google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### virtual CreateGoogleApiSource(NoAwaitTag, google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::CreateGoogleApiSourceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateGoogleApiSource(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### virtual UpdateGoogleApiSource(google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### virtual UpdateGoogleApiSource(NoAwaitTag, google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::UpdateGoogleApiSourceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateGoogleApiSource(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### virtual DeleteGoogleApiSource(google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### virtual DeleteGoogleApiSource(NoAwaitTag, google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::eventarc::v1::DeleteGoogleApiSourceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteGoogleApiSource(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::eventarc::v1::GoogleApiSource > >` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` |   
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
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
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
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
