---
url: https://docs.cloud.google.com/mainframe-connector/docs/pubsub-publish-configuration/
title: Pub/Sub configuration \u00a0|\u00a0 Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:40.688687+00:00
---

# Pub/Sub configuration  |  Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/pubsub-publish-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  Pub/Sub configuration Stay organized with collections  Save and categorize content based on your preferences. 

You can configure Mainframe Connector transcoder's Pub/Sub publish formatting by adding the required configuration in a JSON file, and specifying this file using the `--input-parameter pubsub-publish-configuration`=[DataPath](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#datapath) option with the [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) command. You must define the Pub/Sub publish configuration as specified in section [PubsubConfiguration](https://docs.cloud.google.com/mainframe-connector/docs/pubsub-publish-configuration#pubsubpublishconfiguration).

This page describes the various Pub/Sub parameters you can configure as input parameters for transcoding. The `PubsubPublishConfiguration` object contains all Pub/Sub decoder configuration options.

## PubsubPublishConfiguration

The `PubsubPublishConfiguration` object lets you configure the messages that get sent to Pub/Sub and is used with the [`qsam decode`](https://docs.cloud.google.com/mainframe-connector/docs/api-command-reference#qsam_decode) command.

JSON representation  
---  
      
    
    {
        "attributes_configuration": object (AttributesConfiguration),
        "batching_settings": object (BatchingSettings),
        "concurrency_control_settings": object (ConcurrencyControlSettings),
        "flow_control_settings": object (FlowControlSettings),
        "ordering_key_configuration": object (OrderingKeyConfiguration),
        "spillover_configuration": object (SpilloverConfiguration)  
    }
      
  
Fields  
---  
`attributes_configuration` |  `object (`AttributesConfiguration`)` Specify the attributes configuration. You can specify the configuration as key-value pairs that can be attached to a Pub/Sub message. The configuration can then be used for message filtering or to convey additional metadata.  
`batching_settings` |  `object (`BatchingSettings`)` Specify the batch settings for publishing messages. By default, batch processing is disabled. For more information, see [Publish with batch settings](https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publisher-batch-settings).  
`concurrency_control_settings` |  `object (`ConcurrencyControlSettings`)` Specify the concurrency and message processing settings for the publisher client. These settings control the parallelism for publishing messages, acknowledging successful deliveries, and handling any errors during the publishing process. For more information, see [Concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control-messages).  
`flow_control_settings` |  `object (`FlowControlSettings`)` Specify the flow control settings to be used for publishing messages. By default, flow control settings are disabled. For more information, see [Publish messages with flow control settings](https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publisher-flow-control).  
`ordering_key_configuration` |  `object (`OrderingKeyConfiguration`)` Specify the ordering key configuration. This configuration verifies that messages with the same ordering key are delivered in order. If you don't set this configuration, message ordering is not guaranteed.  
`spillover_configuration` |  `object (`SpilloverConfiguration`)` Specify the configuration for how spillover messages are sent. If not set, spillover messages are sent to the input topic with a `_spillover` suffix.   
For example, if the input topic is `projects/project_example/topics/topic_example`, the default spillover topic would be `projects/project_example/topics/topic_example_spillover`.  
  
## AttributesConfiguration

The `AttributesConfiguration` message specifies a fixed set of attributes that define how attributes are sourced for Pub/Sub messages.

JSON representation  
---  
      
    
    {
        "attributes": object (Attributes)  
    }
      
  
Fields  
---  
`attributes` |  `object (`Attributes`)` A collection of fixed key-value attributes to be attached to the Pub/Sub messages.  
  
### Attributes

The `Attributes` message specifies a collection of `Attribute` key-value pairs that define how the attributes are determined.

JSON representation  
---  
      
    
    {
        "attribute": object (Attribute)  
    }
      
  
Fields  
---  
`attribute` |  `object (`Attribute`)` Specify a collection of key-value pairs.  
  
#### Attribute

The `Attribute` message represents a single key-value pair used as a Pub/Sub message attribute.

JSON representation  
---  
      
    
    {
        "key": string,
        "value": string  
    }
      
  
Fields  
---  
`key` |  `string` Specify the key of the attribute.  
`value` |  `string` Specify the value of the attribute.  
  
## BatchingSettings

The `BatchingSettings` message lets you specify the batch settings for publishing messages to Pub/Sub. You should verify your batch settings are configured to respect the defined [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas). To disable batch processing, set `message_count_threshold=1`.

JSON representation  
---  
      
    
    {
        "delay_threshold": string,
        "element_count_threshold": long,
        "request_byte_threshold": long  
    }
      
  
Fields  
---  
`delay_threshold` |  `string` Specify the delay threshold to use for batch processing. After the amount of time defined by `delay_threshold` has elapsed (counting from the first message added), the messages are wrapped up in a batch and sent. We recommend that you don't set this value too high, otherwise, calls might appear to never complete. If you prioritize real-time or near real-time processing, you'll want a lower delay threshold (a few tens or hundreds of milliseconds). This verifies messages are sent quickly. If you're dealing with large-scale batch processing where immediate delivery isn't critical, a higher threshold (a few seconds) might be acceptable to allow for larger, more efficient batches. For more information on duration format, see `[Duration](https://www.threeten.org/threetenbp/apidocs/org/threeten/bp/Duration.html#parse\(java.lang.CharSequence\))`. If a delay threshold of 0 seconds is provided, it is considered as if a delay threshold was not provided, and the default is used. The default value is 1 ms.  
`element_count_threshold` |  `long` Specify the message count threshold to use for batch processing. After the number of messages defined by `message_count_threshold` are accumulated, they are wrapped up in a batch and sent, even if the delay threshold hasn't elapsed yet. If your messages are consistently small, consider increasing the message count threshold. The default value is 1.  
`request_byte_threshold` |  `long` Specify the maximum size in bytes of messages to accumulate before sending a batch to Pub/Sub. This applies even if neither the delay or message count thresholds have been exceeded yet. If your messages are consistently small, consider increasing the byte threshold. The default value is 1 byte.  
  
## ConcurrencyControlSettings

The `ConcurrencyControlSettings` message lets you configure the parallelism of message publishing. These settings influence how many messages can be sent concurrently.

JSON representation  
---  
      
    
    {
        "publishing_threads": int,
        "result_processing_threads": int  
    }
      
  
Fields  
---  
`publishing_threads` |  `int` Specify the number of processing threads to publish messages. The value should be equal or less than the number of cores available. If the number of threads is 0, publishing is handled synchronously.  
`result_processing_threads` |  `int` Specify the number of threads for processing Pub/Sub message results. This includes acknowledging successfully sent messages and handling any errors that occur during publishing. A value of 0 means result processing parallelism is handled synchronously. The default value is 1.  
  
## FlowControlSettings

The `FlowControlSettings` message lets you specify how the publisher client manages the flow of messages to Pub/Sub. These settings prevent the client from consuming excessive resources or overwhelming Pub/Sub.

JSON representation  
---  
      
    
    {
        "limit_exceeded_behavior": enum (LimitExceededBehavior),
        "max_outstanding_element_count": long,
        "max_outstanding_request_bytes": long  
    }
      
  
Fields  
---  
`limit_exceeded_behavior` |  `enum (`LimitExceededBehavior`)` Specify the behavior when flow control limits are exceeded. The default value is `BLOCK`.  
`max_outstanding_element_count` |  `long` Specify the maximum number of messages that can be outstanding (sent but not yet acknowledged by Pub/Sub). If your mainframe has abundant memory and you want to push very high throughput, you can try increasing the count.  
`max_outstanding_request_bytes` |  `long` Specifies the maximum total size in bytes of outstanding messages.  
  
## OrderingKeyConfiguration

The `OrderingKeyConfiguration` message specifies a static string as the ordering key that defines how the ordering key for Pub/Sub messages is determined.

JSON representation  
---  
      
    
    {
        "key": string  
    }
      
  
Fields  
---  
`key` |  `string` The string value to use as the ordering key for the Pub/Sub message.  
  
## SpilloverConfiguration

The `SpilloverConfiguration` message defines how to specify an alternative topic for spillover messages. You can specify either a full topic name or a suffix to append to the input topic name. These two options are mutually exclusive; you must choose one.

JSON representation  
---  
      
    
    {
        "name": string,
        "suffix": string  
    }
      
  
Fields  
---  
`name` |  `string` Specify the full resource name of an alternative topic for spillover messages in the format `projects/{project}/topics/{topic}`.  
`suffix` |  `string` Specify a suffix to append to the input topic name for spillover messages. For example, if the input topic is `projects/project_example/topics/my-topic`, and the suffix is `_errors`, the spillover topic would be `projects/project_example/topics/my-topic_errors`.  
  
## Enums

### LimitExceededBehavior

The `LimitExceededBehavior` enum lets you configure the behavior when flow control limits are exceeded.

Enums  
---  
`BLOCK` | The Pub/Sub publisher will block when limits are exceeded. This prevents publishing further messages until resources become available.  
`IGNORE` | The Pub/Sub publisher will ignore limits and continue publishing when limits are exceeded. This may lead to increased resource consumption.  
`THROW_EXCEPTION` | The Pub/Sub publisher will throw an exception when limits are exceeded, indicating a failure to publish.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
