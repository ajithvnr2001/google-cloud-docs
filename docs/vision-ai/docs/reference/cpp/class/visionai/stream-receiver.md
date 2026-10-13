---
url: https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver/
title: visionai::StreamReceiver Class Reference \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:07.870173+00:00
---

# visionai::StreamReceiver Class Reference  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# visionai::StreamReceiver

`#include <streams.h>`

`[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver)` is the client through which users receive `Packet`s from a stream. 

## Summary

Each instance of the `[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver)` represents a single connection to a specific stream. Once created, the user may repeatedly call `Receive`.

Example - Repeatedly receive `Packet`s from a specific stream.
    
    
    // First populate the options.
    StreamReceiver::Options options;
    options.service_connection_options = ...;
    options.stream_id = "my-stream";
    
    // Create an instance of the `StreamReceiver`.
    auto stream_receiver_statusor = [StreamReceiver::Create](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver_1a9ba22af96a675a0e6e2a46622f3374ff)(options);
    if (!stream_receiver.ok()) {
      // An error occurred during the setup of the receiver.
      // You can fix the problem and try again.
    }
    auto stream_receiver = std::move(*stream_receiver_statusor);
    
    // Now you can repeatedly receive Packets.
    while (true) {
      Packet p;
      auto status = stream_receiver->Receive(&p);
      if (!status.ok()) {
        // An error occurred. If the error is transient, then you can retry
        // with the same receiver. Otherwise, create a new instance to retry.
      }
    }
    
    // When no more packets are desired, destroy the receiver.
    stream_receiver->reset();

### Constructors and Destructors  
  
---  
`StreamReceiver()`   
  
`StreamReceiver(const [StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) &)`   
  
`~StreamReceiver()`   
  
  
### Public static functions  
  
---  
`Create(const [Options](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/struct/visionai/stream-receiver/options#structvisionai_1_1_stream_receiver_1_1_options) &)` |  `absl::StatusOr< std::unique_ptr< [StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) > >` Create a readily usable instance of a `[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver)`.   
  
### Public functions  
  
---  
`Receive(Packet *packet)` |  `absl::Status` Receive a `Packet` from a stream.   
`Receive(absl::Duration timeout, Packet *packet)` |  `absl::Status`  
`operator=(const [StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) &)=delete` |  `[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) &`  
  
### Structs  
  
---  
[visionai::StreamReceiver::Options](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/struct/visionai/stream-receiver/options) |  [Options](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/struct/visionai/stream-receiver/options#structvisionai_1_1_stream_receiver_1_1_options) to configure the `[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver)`.   
  
## Public static functions

### Create
    
    
    absl::StatusOr< std::unique_ptr< [StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) > > Create(
      const [Options](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/struct/visionai/stream-receiver/options#structvisionai_1_1_stream_receiver_1_1_options) &
    )

Create a readily usable instance of a `[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver)`. 

## Public functions

### Receive
    
    
    absl::Status Receive(
      Packet *packet
    )

Receive a `Packet` from a stream. 

Returns OK on success. Otherwise, returns the following possible errors:

NOT_FOUND: This is only possible with the second overload. It is returned when there are no `Packet`s in the server before `timeout` has run out. You may immediately retry with the same receiver instance.

OUT_OF_RANGE: This indicates that the last packet in the event has been delivered. You can create a new `[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver)` to read from a different event.

Other error codes: To retry, create a new instance of the `[StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver)` and `Receive` through that.

The first overload blocks until either there is a new `Packet` or until a non-transient error has occurred.

The second overload blocks up to `timeout` before returning NOT_FOUND. Otherwise, either yields a `Packet` or returns a non-transient error. 

### Receive
    
    
    absl::Status Receive(
      absl::Duration timeout,
      Packet *packet
    )

### StreamReceiver
    
    
     StreamReceiver()=default

### StreamReceiver
    
    
     StreamReceiver(
      const [StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) &
    )=delete

### operator=
    
    
    [StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) & operator=(
      const [StreamReceiver](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/class/visionai/stream-receiver#classvisionai_1_1_stream_receiver) &
    )=delete

### ~StreamReceiver
    
    
     ~StreamReceiver()=default

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
