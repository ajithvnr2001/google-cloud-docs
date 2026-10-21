---
url: https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka/
title: Read from Apache Kafka to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:40.769288+00:00
---

# Read from Apache Kafka to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Read from Apache Kafka to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to read data from Apache Kafka to Dataflow and includes performance tips and best practices.

For most use cases, consider using the [Managed I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka) to read from Kafka.

If you need more advanced performance tuning, consider using the `KafkaIO` connector. The `KafkaIO` connector is available for [Java](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.html) or by using the [multi-language pipelines framework](https://beam.apache.org/documentation/programming-guide/#multi-language-pipelines) for [Python](https://beam.apache.org/releases/pydoc/current/apache_beam.io.kafka.html) and [Go](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang/kafkaio).

## Parallelism

The following sections describe how to configure parallelism when reading from Kafka.

### Overview

Parallelism is constrained by two factors: the [maximum number of workers](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#set-range) (`max_num_workers`) and the number of Kafka partitions. Dataflow defaults to a parallelism fanout of 4 x `max_num_workers`. However, fanout is bounded by the number of partitions. For example, if 100 vCPUs are available, but the pipeline only reads from 10 Kafka partitions, the maximum parallelism is 10.

To maximize parallelism, it's recommended to have at least 4 x `max_num_workers` Kafka partitions. If your job uses the [Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner), consider setting parallelism even higher. A good starting point is to have partitions equal to twice the number of worker vCPUs.

### Redistribute

If you can't increase the number of partitions, you can increase parallelism by calling [`KafkaIO.Read.withRedistribute`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withRedistribute--). This method adds a `Redistribute` transform to the pipeline, which provides a hint to Dataflow to redistribute and parallelize the data more efficiently. We strongly recommend you specify optimal number of shards by calling [`KafkaIO.Read.withRedistributeNumKeys`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withRedistributeNumKeys-int-). Using [`KafkaIO.Read.withRedistribute`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withRedistribute--) alone can generate numerous keys, leading to performance issues. For more information, see [Identify stages with high parallelism](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs#high-parallelism). Redistributing the data adds some additional overhead to perform the shuffle step. For more information, see [Prevent fusion](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#prevent_fusion).

To minimize the cost of the redistribute shuffle, call [`KafkaIO.Read.withOffsetDeduplication`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withOffsetDeduplication-java.lang.Boolean-). This mode minimizes the amount of data that needs to be persisted as part of the shuffle, while still providing exactly-once processing.

If exactly-once processing isn't required, you can allow duplicates by calling [`KafkaIO.Read.withAllowDuplicates`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withAllowDuplicates-java.lang.Boolean-).

The following table summarizes the redistribute options:

Option | Processing Mode | Apache Beam | Configuration  
---|---|---|---  
Redistribute input | Exactly-once | v2.60+ | `KafkaIO.Read.withRedistribute()`  
Allow duplicates | At-least-once | v2.60+ | `KafkaIO.Read.withRedistribute().withAllowDuplicates()`  
Offset deduplication | Exactly-once | v2.69+ | `KafkaIO.Read.withRedistribute().withOffsetDeduplication()`  
  
### Load skew

Try to ensure that the load between partitions is relatively even and not skewed. If the load is skewed, it can lead to poor utilization of workers. Workers that read from partitions with lighter load might be relatively idle, while workers that read from partitions with heavy load might fall behind. Dataflow provides metrics for per-partition backlog.

If load is skewed, [dynamic work balancing](https://docs.cloud.google.com/dataflow/docs/dynamic-work-rebalancing) can help to distribute the work. For example, Dataflow might allocate one worker to read from multiple low-volume partitions, and allocate another worker to read from a single high-volume partition. However, two workers cannot read from the same partition, so a heavily loaded partition can still cause the pipeline to fall behind.

## Best practices

This section contains recommendations for reading from Kafka into Dataflow.

### Low-volume topics

A common scenario is to read from many low-volume topics at the same time — for example, one topic per customer. Creating separate Dataflow jobs for each topic is cost-inefficient, because each job requires at least one full worker. Instead, consider the following options:

  * **Merge topics**. Combine topics before they are ingested into Dataflow. Ingesting a few high-volume topics is much more efficient than ingesting many low-volume topics. Each high-volume topic can be handled by a single Dataflow job that fully utilizes its workers.

  * **Read multiple topics**. If you can't combine topics before ingesting them into Dataflow, consider creating a pipeline that reads from multiple topics. This approach allows Dataflow to assign several topics to same worker. There are two ways to implement this approach:

    * _Single read step_. Create a single instance of the `KafkaIO` connector and configure it to read multiple topics. Then filter by topic name to apply different logic per topic. For example code, see Read from multiple topics. Consider this option if all of your topics are collocated in the same cluster. One drawback is that problems with a single sink or transform might cause all of the topics to accumulate backlog.

For more advanced use cases, pass in a set of `KafkaSourceDescriptor` objects that specify the topics to read from. Using `KafkaSourceDescriptor` lets you update the topic list later if needed. This feature requires Java with the Portable Runner.

    * _Multiple read steps_. To read from topics located in different clusters, your pipeline can include several `KafkaIO` instances. While the job is running, you can update individual sources by using [transform mappings](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#Mapping). Setting a new topic or cluster is only supported when using the Portable Runner. Observability is a potential challenge with this approach, because you need to monitor each individual read transform instead of relying on pipeline-level metrics.




### Committing back to Kafka

By default, the `KafkaIO` connector doesn't use Kafka offsets to track progress and doesn't commit back to Kafka. If you call [`commitOffsetsInFinalize`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#commitOffsetsInFinalize--), the connector makes a best effort to commit back to Kafka after records are committed in Dataflow. Committed records in Dataflow might not be fully processed, so if you [cancel](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline) the pipeline, an offset might be committed without the records ever being fully processed.

Because setting `enable.auto.commit=True` commits offsets as soon as they are read from Kafka without any processing by Dataflow, using this option isn't recommended. The recommendation is to set both `enable.auto.commit=False` and [`commitOffsetsInFinalize=True`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#commitOffsetsInFinalize--). If you set `enable.auto.commit` to `True`, data can be lost if the pipeline is interrupted while processing. Records already committed on Kafka might be dropped.

### Watermarks

By default, the `KafkaIO` connector uses the current processing time to assign the [output watermark](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines#watermarks) and the event time. To change this behavior, call [`withTimestampPolicyFactory`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withTimestampPolicyFactory-org.apache.beam.sdk.io.kafka.TimestampPolicyFactory-) and assign a [`TimestampPolicy`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/TimestampPolicy.html). Beam provides implementations of `TimestampPolicy` that calculate the watermark based on either Kafka's log append time or the message creation time.

### Runner considerations

The `KafkaIO` connector has two underlying implementations for Kafka reads, the older [`ReadFromKafkaViaUnbounded`](https://github.com/apache/beam/blob/65b29361eb16280ef69504087896eb2f178e9250/sdks/java/io/kafka/src/main/java/org/apache/beam/sdk/io/kafka/KafkaIO.java#L1666) and the newer [`ReadFromKafkaViaSDF`](https://github.com/apache/beam/blob/65b29361eb16280ef69504087896eb2f178e9250/sdks/java/io/kafka/src/main/java/org/apache/beam/sdk/io/kafka/KafkaIO.java#L1722). Dataflow automatically chooses the best implementation for your job based on your SDK language and job requirements. Avoid explicitly requesting a runner or Kafka implementation unless you require specific features only available in that implementation. For more information about choosing a runner, see [Use Dataflow Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner).

If your pipeline uses [`withTopic`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withTopic-java.lang.String-) or [`withTopics`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withTopics-java.util.List-), the older implementation queries Kafka at pipeline construction time for the available partitions. The machine that creates the pipeline must have permission to connect to Kafka. If you receive a permission error, verify that you have permissions to connect to Kafka locally. You can avoid this problem by using [`withTopicPartitions`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withTopicPartitions-java.util.List-), which doesn't connect to Kafka at pipeline construction time.

### Deploy to production

When you deploy your solution in production, it's recommended to use [Flex templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates). By using a Flex template, the pipeline is launched from a consistent environment, which can help to mitigate local configuration issues.

Logging from `KafkaIO` can be quite verbose. Consider reducing the logging level in production as follows:
    
    
    sdkHarnessLogLevelOverrides='{"org.apache.kafka.clients.consumer.internals.SubscriptionState":"WARN"}'.
    

For more information, see [Set pipeline worker log levels](https://docs.cloud.google.com/dataflow/docs/guides/logging#SettingLevels).

### Configure networking

By default, Dataflow launches instances within your default Virtual Private Cloud (VPC) network. Depending on your Kafka configuration, you might need to configure a different network and subnet for Dataflow. For more information, see [Specify a network and subnetwork](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks). When configuring your network, create [firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) that allow the Dataflow worker machines to reach the Kafka brokers.

If you are using VPC Service Controls, then place the Kafka cluster within the VPC Service Controls perimeter, or else [extend the perimeters to the authorized VPN or Cloud Interconnect](https://docs.cloud.google.com/vpc-service-controls/docs/overview#hybrid_access).

If your Kafka cluster is deployed outside of Google Cloud, you must create a network connection between Dataflow and the Kafka cluster. There are several networking options with different tradeoffs:

  * Connect using a shared RFC 1918 address space, by using one of the following: 
    * [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)
    * [IPsec virtual private network (VPN)](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * Reach your externally hosted Kafka cluster through public IP addresses, by using one of the following: 
    * Public internet
    * [Direct peering](https://docs.cloud.google.com/network-connectivity/docs/direct-peering/direct-peering)
    * [Carrier peering](https://docs.cloud.google.com/network-connectivity/docs/carrier-peering)



Dedicated Interconnect is the best option for predictable performance and reliability, but it can take longer to set up because third parties must provision the new circuits. With a public IP–based topology, you can get started quickly because little networking work needs to be done.

The next two sections describe these options in more detail.

#### Shared RFC 1918 address space

Both Dedicated Interconnect and IPsec VPN give you direct access to RFC 1918 IP addresses in your Virtual Private Cloud (VPC), which can simplify your Kafka configuration. If you're using a VPN–based topology, consider setting up a [high-throughput VPN](https://docs.cloud.google.com/solutions/building-high-throughput-vpns).

By default, Dataflow launches instances on your default [VPC network](https://docs.cloud.google.com/vpc/docs/vpc). In a private network topology with [routes explicitly defined in Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) that connect subnetworks in Google Cloud to that Kafka cluster, you need more control over where to locate your Dataflow instances. You can use Dataflow to configure the `network` and `subnetwork` [execution parameters](https://docs.cloud.google.com/dataflow/pipelines/specifying-exec-params#setting-other-cloud-pipeline-options).

Make sure that the corresponding subnetwork has enough IP addresses available for Dataflow to launch instances on when it attempts to scale out. Also, when you create a separate network for launching your Dataflow instances, ensure that you have a firewall rule that enables TCP traffic among all virtual machines in the project. The default network already has this firewall rule configured.

#### Public IP address space

This architecture uses Transport Layer Security ([TLS](https://wikipedia.org/wiki/Transport_Layer_Security)) to secure traffic between external clients and Kafka, and uses unencrypted traffic for inter-broker communication. When the Kafka listener binds to a network interface that is used for both internal and external communication, configuring the listener is straightforward. However, in many scenarios, the externally advertised addresses of the Kafka brokers in the cluster differ from the internal network interfaces that Kafka uses. In such scenarios, you can use the `advertised.listeners` property:
    
    
    # Configure protocol map
    listener.security.protocol.map=INTERNAL:PLAINTEXT,EXTERNAL:SSL  
    
    # Use plaintext for inter-broker communication
    inter.broker.listener.name=INTERNAL  
    
    # Specify that Kafka listeners should bind to all local interfaces
    listeners=INTERNAL://0.0.0.0:9092,EXTERNAL://0.0.0.0:9093  
    
    # Separately, specify externally visible address
    advertised.listeners=INTERNAL://kafkabroker-n.mydomain.com:9092,EXTERNAL://kafkabroker-n.mydomain.com:9093
    

External clients connect using port 9093 through an "SSL" channel, and internal clients connect using port 9092 through a plaintext channel. When you specify an address under `advertised.listeners`, use DNS names (`kafkabroker-n.mydomain.com`, in this sample) that resolve to the same instance for both external and internal traffic. Using public IP addresses might not work because the addresses might fail to resolve for internal traffic.

### Tune Kafka

Your Kafka cluster and Kafka client settings can have a large impact on performance. In particular, the following settings might be too low. This section gives some suggested starting points, but you should experiment with these values for your particular workload.

  * `unboundedReaderMaxElements`. Defaults to 10,000. A higher value such as 100,000 can increase the size of the [bundles](https://beam.apache.org/documentation/runtime/model/#bundling-and-persistence), which can improve performance significantly if your pipeline includes aggregations. However, a higher value might also increase latency. To set the value, use [`setUnboundedReaderMaxElements`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/runners/dataflow/options/DataflowPipelineDebugOptions.html#setUnboundedReaderMaxElements-java.lang.Integer-). This setting does not apply to the Portable Runner. For the Portable Runner, use the [`sdf_checkpoint_after_output_bytes`](https://docs.cloud.google.com/dataflow/docs/reference/service-options) Dataflow service option.

  * `unboundedReaderMaxReadTimeMs`. Defaults to 10,000 msec. A higher value such as 20,000 msec can increase the bundle size, while a lower value such as 5000 msec can reduce latency or backlog. To set the value, use [`setUnboundedReaderMaxReadTimeMs`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/runners/dataflow/options/DataflowPipelineDebugOptions.html#setUnboundedReaderMaxReadTimeMs-java.lang.Integer-). This setting does not apply to the Portable Runner. For the Portable Runner, use the [`sdf_checkpoint_after_duration`](https://docs.cloud.google.com/dataflow/docs/reference/service-options) Dataflow service option.

  * `max.poll.records`. Defaults to 500. A higher value might perform better by retrieving more incoming records together, especially when using the Portable Runner. To set the value, call [`withConsumerConfigUpdates`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withConsumerConfigUpdates-java.util.Map-).

  * `fetch.max.bytes`. Defaults to 1MB. A higher value might improve throughput by reducing the number of requests, especially when using the Portable Runner. However, setting it too high might increase latency, although downstream processing is more likely to be the main bottleneck. A recommended starting value is 100MB. To set the value, call `withConsumerConfigUpdates`.

  * `max.partition.fetch.bytes`. Defaults to 1MB. This parameter sets maximum amount of data per partition that the server returns. Increasing the value can improve throughput by reducing the number of requests, especially when using the Portable Runner. However, setting it too high might increase latency, although downstream processing is more likely to be the main bottleneck. A recommended starting value is 100MB. To set the value, call `withConsumerConfigUpdates`.

  * `consumerPollingTimeout`. Defaults to 2 seconds. If the consumer client times out before it can read any records, try setting a higher value. This setting is most often relevant when performing cross-region reads or reads with a slow network. To set the value, call [`withConsumerPollingTimeout`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.Read.html#withConsumerPollingTimeout-long-).




Ensure that `receive.buffer.bytes` is large enough to handle the size of the messages. If the value is too small, the logs mights show that consumers are continuously being re-created and seeking to a specific offset.

## Examples

The following code examples show how to create Dataflow pipelines that read from Kafka. When using Application Default Credentials in conjunction with the Google Cloud Managed Service for Apache Kafka provided [callback handler](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-java#create_a_java_producer_application), `kafka-clients` version 3.7.0 or higher is required.

### Read from a single topic

This example uses the [Managed I/O connector](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka). It shows how to read from a Kafka topic and write the message payloads to text files.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.common.collect.ImmutableMap;
    import java.io.UnsupportedEncodingException;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptors;
    
    public class KafkaRead {
    
      public static Pipeline createPipeline(Options options) {
    
        // Create configuration parameters for the Managed I/O transform.
        ImmutableMap<String, Object> config = ImmutableMap.<String, Object>builder()
            .put("bootstrap_servers", options.getBootstrapServer())
            .put("topic", options.getTopic())
            .put("format", "RAW")
            .put("max_read_time_seconds", 15)
            .put("auto_offset_reset_config", "earliest")
            .build();
    
        // Build the pipeline.
        var pipeline = Pipeline.create(options);
        pipeline
            // Read messages from Kafka.
            .apply(Managed.read(Managed.KAFKA).withConfig(config)).getSinglePCollection()
            // Get the payload of each message and convert to a string.
            .apply(MapElements
                .into(TypeDescriptors.strings())
                .via((row -> {
                  var bytes = row.getBytes("payload");
                  try {
                    return new String(bytes, "UTF-8");
                  } catch (UnsupportedEncodingException e) {
                    throw new RuntimeException(e);
                  }
                })))
            // Write the payload to a text file.
            .apply(TextIO
                .write()
                .to(options.getOutputPath())
                .withSuffix(".txt")
                .withNumShards(1));
        return pipeline;
      }
    }

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    import apache_beam as beam
    
    from apache_beam import window
    from apache_beam.io.textio import WriteToText
    from apache_beam.options.pipeline_options import PipelineOptions
    
    
    def read_from_kafka() -> None:
        # Parse the pipeline options passed into the application. Example:
        #     --topic=$KAFKA_TOPIC --bootstrap_server=$BOOTSTRAP_SERVER
        #     --output=$CLOUD_STORAGE_BUCKET --streaming
        # For more information, see
        # https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        class MyOptions(PipelineOptions):
            @staticmethod
            def _add_argparse_args(parser: argparse.ArgumentParser) -> None:
                parser.add_argument("--topic")
                parser.add_argument("--bootstrap_server")
                parser.add_argument("--output")
    
        options = MyOptions()
        with beam.Pipeline(options=options) as pipeline:
            (
                pipeline
                # Read messages from an Apache Kafka topic.
                | beam.managed.Read(
                    beam.managed.KAFKA,
                    config={
                      "bootstrap_servers": options.bootstrap_server,
                      "topic": options.topic,
                      "data_format": "RAW",
                      "auto_offset_reset_config": "earliest",
                      # The max_read_time_seconds parameter is intended for testing.
                      # Avoid using this parameter in production.
                      "max_read_time_seconds": 5
                    }
                )
                # Subdivide the output into fixed 5-second windows.
                | beam.WindowInto(window.FixedWindows(5))
                | WriteToText(
                    file_path_prefix=options.output, file_name_suffix=".txt", num_shards=1
                )
            )
    
    

### Read from multiple topics

This example uses the `KafkaIO` connector. It shows how to read from several Kafka topics and apply separate pipeline logic for each topic.

For more advanced use cases, dynamically pass in a set of [`KafkaSourceDescriptor`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaSourceDescriptor.html) objects, so that you can update the list of topics to read from. This approach requires Java with the Portable Runner.

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.TextIO;
    import org.apache.beam.sdk.io.kafka.KafkaIO;
    import org.apache.beam.sdk.options.Description;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.StreamingOptions;
    import org.apache.beam.sdk.transforms.Filter;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.values.TypeDescriptors;
    import org.apache.kafka.common.serialization.LongDeserializer;
    import org.apache.kafka.common.serialization.StringDeserializer;
    import org.joda.time.Duration;
    import org.joda.time.Instant;
    
    public class KafkaReadTopics {
    
      public static Pipeline createPipeline(Options options) {
        String topic1 = options.getTopic1();
        String topic2 = options.getTopic2();
    
        // Build the pipeline.
        var pipeline = Pipeline.create(options);
        var allTopics = pipeline
            .apply(KafkaIO.<Long, String>read()
                .withTopics(List.of(topic1, topic2))
                .withBootstrapServers(options.getBootstrapServer())
                .withKeyDeserializer(LongDeserializer.class)
                .withValueDeserializer(StringDeserializer.class)
                .withMaxReadTime(Duration.standardSeconds(10))
                .withStartReadTime(Instant.EPOCH)
            );
    
        // Create separate pipeline branches for each topic.
        // The first branch filters on topic1.
        allTopics
            .apply(Filter.by(record -> record.getTopic().equals(topic1)))
            .apply(MapElements
                .into(TypeDescriptors.strings())
                .via(record -> record.getKV().getValue()))
            .apply(TextIO.write()
                .to(topic1)
                .withSuffix(".txt")
                .withNumShards(1)
            );
    
        // The second branch filters on topic2.
        allTopics
            .apply(Filter.by(record -> record.getTopic().equals(topic2)))
            .apply(MapElements
                .into(TypeDescriptors.strings())
                .via(record -> record.getKV().getValue()))
            .apply(TextIO.write()
                .to(topic2)
                .withSuffix(".txt")
                .withNumShards(1)
            );
        return pipeline;
      }
    }

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    import apache_beam as beam
    
    from apache_beam.io.kafka import ReadFromKafka
    from apache_beam.io.textio import WriteToText
    from apache_beam.options.pipeline_options import PipelineOptions
    
    
    def read_from_kafka() -> None:
        # Parse the pipeline options passed into the application. Example:
        #   --bootstrap_server=$BOOTSTRAP_SERVER --output=$STORAGE_BUCKET --streaming
        # For more information, see
        # https://beam.apache.org/documentation/programming-guide/#configuring-pipeline-options
        class MyOptions(PipelineOptions):
            @staticmethod
            def _add_argparse_args(parser: argparse.ArgumentParser) -> None:
                parser.add_argument('--bootstrap_server')
                parser.add_argument('--output')
    
        options = MyOptions()
        with beam.Pipeline(options=options) as pipeline:
            # Read from two Kafka topics.
            all_topics = pipeline | ReadFromKafka(consumer_config={
                    "bootstrap.servers": options.bootstrap_server
                },
                topics=["topic1", "topic2"],
                with_metadata=True,
                max_num_records=10,
                start_read_time=0
            )
    
            # Filter messages from one topic into one branch of the pipeline.
            (all_topics
                | beam.Filter(lambda message: message.topic == 'topic1')
                | beam.Map(lambda message: message.value.decode('utf-8'))
                | "Write topic1" >> WriteToText(
                    file_path_prefix=options.output + '/topic1/output',
                    file_name_suffix='.txt',
                    num_shards=1))
    
            # Filter messages from the other topic.
            (all_topics
                | beam.Filter(lambda message: message.topic == 'topic2')
                | beam.Map(lambda message: message.value.decode('utf-8'))
                | "Write topic2" >> WriteToText(
                    file_path_prefix=options.output + '/topic2/output',
                    file_name_suffix='.txt',
                    num_shards=1))

## What's next

  * [Performance characteristics of Apache Kafka to BigQuery pipelines](https://docs.cloud.google.com/dataflow/docs/guides/kafka-bigquery-performance)
  * [Write to Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/write-to-kafka).
  * Learn more about [Managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
