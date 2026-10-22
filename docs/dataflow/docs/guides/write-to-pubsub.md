---
url: https://docs.cloud.google.com/dataflow/docs/guides/write-to-pubsub/
title: Write from Dataflow to Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:02.414754+00:00
---

# Write from Dataflow to Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/write-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write from Dataflow to Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to write text data from Dataflow to Pub/Sub by using the Apache Beam `PubSubIO` [I/O connector](https://beam.apache.org/documentation/io/connectors/).

**Note:** Depending on your scenario, consider using one of the [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates). Several of these templates output to Pub/Sub.

## Overview

To write data to Pub/Sub, use the `PubSubIO` connector. The input elements can be either Pub/Sub messages or just the message data. If the input elements are Pub/Sub messages, you can optionally set attributes or an ordering key on each message.

You can use either the Java, Python, or Go version of the `PubSubIO` connector, as follows:

###  Java 

To write to a single topic, call the [`PubsubIO.writeMessages`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.html#writeMessages--) method. This method takes an input collection of `PubsubMessage` objects. The connector also defines convenience methods for writing strings, binary-encoded Avro messages, or binary-encoded protobuf messages. These methods convert the input collection into Pub/Sub messages.

To write to a dynamic set of topics based on the input data, call [`writeMessagesDynamic`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.html#writeMessagesDynamic--). Specify the destination topic for each message by calling `PubsubMessage.withTopic` on the message. For example, you can route messages to different topics based on the value of a particular field in your input data.

For more information, see the [`PubsubIO`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.html) reference documentation.

###  Python 

Call the [`pubsub.WriteToPubSub`](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html#apache_beam.io.gcp.pubsub.WriteToPubSub) method. By default, this method takes an input collection of type `bytes`, representing the message payload. If the `with_attributes` parameter is `True`, the method takes a collection of `PubsubMessage` objects.

For more information, see the [`pubsub` module](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html) reference documentation.

###  Go 

To write data to Pub/Sub, call the [`pubsubio.Write`](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio#Write) method. This method takes an input collection of either `PubSubMessage` objects or byte slices that contain the message payloads.

For more information, see the [`pubsubio` package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio) reference documentation.

For more information about Pub/Sub messages, see [Message format](https://docs.cloud.google.com/pubsub/docs/publisher#message_format) in the Pub/Sub documentation.

**Note:** Pub/Sub messages have a [10 MB size limit](https://docs.cloud.google.com/pubsub/quotas#resource_limits). The Apache Beam `PubSubIO` connector requires additional space for data encoding, which lowers the maximum message size it can process. For example, the SDK for Java has a [7.5 MB message limit](https://github.com/apache/beam/blob/release-2.59.0/sdks/java/io/google-cloud-platform/src/main/java/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.java#L1268) because of base64 encoding.

## Timestamps

Pub/Sub sets a timestamp on each message. This timestamp represents the time when the message is published to Pub/Sub. In a streaming scenario, you might also care about the _event_ timestamp, which is the time when the message data was generated. You can use the Apache Beam [element timestamp](https://beam.apache.org/documentation/programming-guide/#element-timestamps) to represent event time. Sources that create an unbounded `PCollection` often assign each new element a timestamp that corresponds to the event time.

For Java and Python, the Pub/Sub I/O connector can write each element's timestamp as a Pub/Sub message attribute. Message consumers can use this attribute to get the event timestamp.

###  Java 

Call `PubsubIO.Write<T>.withTimestampAttribute` and specify the name of the attribute.

###  Python 

Specify the `timestamp_attribute` parameter when you call `WriteToPubSub`.

## Message delivery

Dataflow supports [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once) of messages within a pipeline. However, the Pub/Sub I/O connector can't guarantee exactly-once delivery of messages through Pub/Sub.

For Java and Python, you can configure the Pub/Sub I/O connector to write each element's unique ID as a message attribute. Message consumers can then use this attribute to deduplicate messages.

###  Java 

Call `PubsubIO.Write<T>.withIdAttribute` and specify the name of the attribute.

###  Python 

Specify the `id_label` parameter when you call `WriteToPubSub`.

### Direct output

If you enable [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes) in your pipeline, then the I/O connector uses _direct output_. In this mode, the connector doesn't checkpoint messages, which enables faster writes. However, retries in this mode might cause duplicate messages with different message IDs, possibly making it harder for message consumers to deduplicate the messages.

For pipelines that use exactly-once mode, you can enable direct output by setting the `streaming_enable_pubsub_direct_output` [service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options). Direct output reduces write latency and results in more efficient processing. Consider this option if your message consumers can handle duplicate messages with non-unique message IDs.

## Examples

The following example creates a `PCollection` of Pub/Sub messages and writes them to a Pub/Sub topic. The topic is specified as a pipeline option. Each message contains payload data and a set of attributes.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.nio.charset.StandardCharsets;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.coders.DefaultCoder;
    import org.apache.beam.sdk.extensions.avro.coders.AvroCoder;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
    import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptor;
    
    
    
    public class PubSubWriteWithAttributes {
      public interface Options extends PipelineOptions {
        @Description("The Pub/Sub topic to write to. Format: projects/<PROJECT>/topics/<TOPIC>")
        String getTopic();
    
        void setTopic(String value);
      }
    
      // A custom datatype for the source data.
      @DefaultCoder(AvroCoder.class)
      static class ExampleData {
        public String name;
        public String product;
        public Long timestamp; // Epoch time in milliseconds
    
        public ExampleData() {}
    
        public ExampleData(String name, String product, Long timestamp) {
          this.name = name;
          this.product = product;
          this.timestamp = timestamp;
        }
      }
    
      // Write messages to a Pub/Sub topic.
      public static void main(String[] args) {
        // Example source data.
        final List<ExampleData> messages = Arrays.asList(
            new ExampleData("Robert", "TV", 1613141590000L),
            new ExampleData("Maria", "Phone", 1612718280000L),
            new ExampleData("Juan", "Laptop", 1611618000000L),
            new ExampleData("Rebeca", "Videogame", 1610000000000L)
        );
    
        // Parse the pipeline options passed into the application. Example:
        //   --runner=DirectRunner --topic=projects/MY_PROJECT/topics/MY_TOPIC"
        // For more information, see https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        var options = PipelineOptionsFactory.fromArgs(args).withValidation().as(Options.class);
        var pipeline = Pipeline.create(options);
        pipeline
            // Create some data to write to Pub/Sub.
            .apply(Create.of(messages))
            // Convert the data to Pub/Sub messages.
            .apply(MapElements
                .into(TypeDescriptor.of(PubsubMessage.class))
                .via((message -> {
                  byte[] payload = message.product.getBytes(StandardCharsets.UTF_8);
                  // Create attributes for each message.
                  HashMap<String, String> attributes = new HashMap<String, String>();
                  attributes.put("buyer", message.name);
                  attributes.put("timestamp", Long.toString(message.timestamp));
                  return new PubsubMessage(payload, attributes);
                })))
            // Write the messages to Pub/Sub.
            .apply(PubsubIO.writeMessages().to(options.getTopic()));
        pipeline.run().waitUntilFinish();
      }
    }

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    from typing import Any, Dict, List
    
    import apache_beam as beam
    from apache_beam.io import PubsubMessage
    from apache_beam.io import WriteToPubSub
    from apache_beam.options.pipeline_options import PipelineOptions
    
    from typing_extensions import Self
    
    
    def item_to_message(item: Dict[str, Any]) -> PubsubMessage:
        # Re-import needed types. When using the Dataflow runner, this
        # function executes on a worker, where the global namespace is not
        # available. For more information, see:
        # https://cloud.google.com/dataflow/docs/guides/common-errors#name-error
        from apache_beam.io import PubsubMessage
    
        attributes = {"buyer": item["name"], "timestamp": str(item["ts"])}
        data = bytes(item["product"], "utf-8")
    
        return PubsubMessage(data=data, attributes=attributes)
    
    
    def write_to_pubsub(argv: List[str] = None) -> None:
        # Parse the pipeline options passed into the application. Example:
        #     --topic=$TOPIC_PATH --streaming
        # For more information, see
        # https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        class MyOptions(PipelineOptions):
            @classmethod
            # Define a custom pipeline option to specify the Pub/Sub topic.
            def _add_argparse_args(cls: Self, parser: argparse.ArgumentParser) -> None:
                parser.add_argument("--topic", required=True)
    
        example_data = [
            {"name": "Robert", "product": "TV", "ts": 1613141590000},
            {"name": "Maria", "product": "Phone", "ts": 1612718280000},
            {"name": "Juan", "product": "Laptop", "ts": 1611618000000},
            {"name": "Rebeca", "product": "Video game", "ts": 1610000000000},
        ]
        options = MyOptions()
    
        with beam.Pipeline(options=options) as pipeline:
            (
                pipeline
                | "Create elements" >> beam.Create(example_data)
                | "Convert to Pub/Sub messages" >> beam.Map(item_to_message)
                | WriteToPubSub(topic=options.topic, with_attributes=True)
            )
    
        print("Pipeline ran successfully.")
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
