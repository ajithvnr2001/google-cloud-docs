---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-to-gcs/
title: Stream Pub/Sub Lite to Cloud Storage using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:07.114946+00:00
---

# Stream Pub/Sub Lite to Cloud Storage using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-to-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Stream Pub/Sub Lite to Cloud Storage using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This sample shows how to create an Apache Beam streaming pipeline that reads messages from Pub/Sub Lite, group the messages using a fixed-sized windowing function, and writes them to Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Stream Pub/Sub Lite messages by using Dataflow](https://docs.cloud.google.com/pubsub/lite/docs/stream-messages-dataflow)



## Code sample

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.proto.[SequencedMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SequencedMessage.html);
    import org.apache.beam.examples.common.WriteOneFilePerWindow;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.gcp.pubsublite.PubsubLiteIO;
    import org.apache.beam.sdk.io.gcp.pubsublite.SubscriberOptions;
    import org.apache.beam.sdk.options.Default;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.options.Validation.Required;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.windowing.FixedWindows;
    import org.apache.beam.sdk.transforms.windowing.Window;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.joda.time.Duration;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    public class PubsubliteToGcs {
      /*
       * Define your own configuration options. Add your arguments to be processed
       * by the command-line parser.
       */
      public interface PubsubliteToGcsOptions extends StreamingOptions {
        @Description("Your Pub/Sub Lite subscription.")
        @Required
        String getSubscription();
    
        void setSubscription(String value);
    
        @Description("Window size of output files in minutes.")
        @Default.Integer(1)
        Integer getWindowSize();
    
        void setWindowSize(Integer value);
    
        @Description("Filename prefix of output files.")
        @Required
        String getOutput();
    
        void setOutput(String value);
      }
    
      private static final Logger LOG = LoggerFactory.getLogger(PubsubliteToGcs.class);
    
      public static void main(String[] args) throws InterruptedException {
        // The maximum number of shards when writing output files.
        int numShards = 1;
    
        PubsubliteToGcsOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubsubliteToGcsOptions.class);
    
        options.setStreaming(true);
    
        SubscriberOptions subscriberOptions =
            SubscriberOptions.newBuilder()
                .setSubscriptionPath([SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).parse(options.getSubscription()))
                .build();
    
        Pipeline pipeline = Pipeline.create(options);
        pipeline
            .apply("Read From Pub/Sub Lite", PubsubLiteIO.read(subscriberOptions))
            .apply(
                "Convert messages",
                MapElements.into(TypeDescriptors.strings())
                    .via(
                        (SequencedMessage sequencedMessage) -> {
                          String data = sequencedMessage.getMessage().getData().toStringUtf8();
                          LOG.info("Received: " + data);
                          long publishTime = sequencedMessage.getPublishTime().getSeconds();
                          return data + "\t" + publishTime;
                        }))
            .apply(
                "Apply windowing function",
                Window
                    // Group the elements using fixed-sized time intervals based on the element
                    // timestamp (using the default event time trigger). The element timestamp
                    // is the publish timestamp associated with a message.
                    //
                    // NOTE: If data is not being continuously ingested, such as with a batch or
                    // intermittent publisher, the final window will never close as the watermark
                    // will not advance. If this is a possibility with your pipeline, you should
                    // add an additional processing time trigger to force window closure after
                    // enough time has passed. See
                    // https://beam.apache.org/documentation/programming-guide/#triggers
                    // for more information.
                    .<String>into(FixedWindows.of(Duration.standardMinutes(options.getWindowSize()))))
            .apply("Write elements to GCS", new WriteOneFilePerWindow(options.getOutput(), numShards));
    
        // Execute the pipeline. You may add `.waitUntilFinish()` to observe logs in your console, but
        // `waitUntilFinish()` will not work in Dataflow Flex Templates.
        pipeline.run();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
