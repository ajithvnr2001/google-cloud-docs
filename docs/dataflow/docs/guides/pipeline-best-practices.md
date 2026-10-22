---
url: https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices/
title: Dataflow pipeline best practices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:14.541729+00:00
---

# Dataflow pipeline best practices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow pipeline best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines best practices to use when developing your Dataflow pipelines. Using these best practices has the following benefits:

  * Improve pipeline observability and performance
  * Improve developer productivity
  * Enhance pipeline testability



The Apache Beam code examples on this page use Java, but the content applies to the Apache Beam Java, Python, and Go SDKs.

## Questions to consider

When designing your pipeline, consider the following questions:

  * Where is your pipeline's input data stored? How many sets of input data do you have?
  * What does your data look like?
  * What do you want to do with your data?
  * Where should your pipeline's output data go?
  * Does your Dataflow job use [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/concept-platform-controls)?



## Use templates

To accelerate pipeline development, instead of building a pipeline by writing Apache Beam code, use a [Dataflow template](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates) when possible. Templates have the following benefits:

  * Templates are reusable.
  * Templates let you customize each job by changing specific pipeline parameters.
  * Anyone you provide permissions to can use the template to deploy the pipeline. For example, a developer can create a job from a template, and a data scientist in the organization can deploy that template at a later time.



You can use a [Google-provided template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates), or you can [create your own template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates). Some Google-provided templates allow you to add custom logic as a pipeline step. For example, the [Pub/Sub to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery) provides a parameter to run a JavaScript user-defined function (UDF) that's stored in Cloud Storage.

Because Google-provided templates are open source under the Apache License 2.0, you can use them as the basis for new pipelines. The templates are also useful as code examples. View the template code in the [GitHub repository](https://github.com/GoogleCloudPlatform/DataflowTemplates/tree/main/).

## Assured Workloads

Assured Workloads helps enforce security and compliance requirements for Google Cloud customers. For example, [EU Regions and Support with Sovereignty Controls](https://docs.cloud.google.com/assured-workloads/docs/concept-platform-controls#eu-sovereignty-controls) helps enforce data residency and data sovereignty promises for EU-based customers. To provide these features, some Dataflow features are restricted or limited. If you use Assured Workloads with Dataflow, all of the resources that your pipeline accesses must be located in your organization's [Assured Workloads project or folder](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations). These resources include:

  * Cloud Storage buckets
  * BigQuery datasets
  * Pub/Sub topics and subscriptions
  * Firestore datasets
  * I/O connectors



In Dataflow, for streaming jobs created after March 7, 2024, all user data is encrypted with CMEK.

For streaming jobs created before March 7, 2024, data keys used in key-based operations, such as windowing, grouping, and joining, are not protected by CMEK encryption. To enable this encryption for your jobs, [drain or cancel the job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline), and then restart it. For more information, see [Encryption of pipeline state artifacts](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys#artifact-encryption).

## Share data across pipelines

There is no Dataflow-specific cross pipeline communication mechanism for sharing data or processing context between pipelines. You can use durable storage like Cloud Storage or an in-memory cache like App Engine to share data between pipeline instances.

## Schedule jobs

You can automate pipeline execution in the following ways:

  * Use [Dataflow data pipelines](https://docs.cloud.google.com/dataflow/docs/guides/data-pipelines) to create recurrent job schedules and understand where resources are spent over multiple job executions.
  * Use Cloud Scheduler.
  * Use the Apache Airflow [Dataflow Operator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataflow.html), one of several [Google Cloud Operators](https://docs.cloud.google.com/composer/docs/how-to/using/writing-dags#operators) in a [Managed Service for Apache Airflow workflow](https://docs.cloud.google.com/composer/docs/how-to/using/writing-dags).
  * Run custom (cron) job processes on Compute Engine.



## Best practices for writing pipeline code

The following sections provide best practices to use when you create pipelines by writing Apache Beam code.

### Structure your Apache Beam code

To create pipelines, it's common to use the generic [`ParDo`](https://beam.apache.org/documentation/programming-guide/#pardo) parallel processing Apache Beam transform. When you apply a `ParDo` transform, you provide code in the form of a `DoFn` object. `DoFn` is an Apache Beam SDK class that defines a distributed processing function.

You can think of your `DoFn` code as small, independent entities: there can potentially be many instances running on different machines, each with no knowledge of the others. As such, we recommend creating _pure functions_ , which are ideal for the parallel and distributed nature of `DoFn` elements. Pure functions have the following characteristics:

  * Pure functions don't depend on hidden or external state.
  * They have no observable side effects.
  * They are deterministic.



The pure function model is not strictly rigid. When your code doesn't depend on things that aren't assured by the Dataflow service, state information or external initialization data can be valid for `DoFn` and other function objects.

When structuring your `ParDo` transforms and creating your `DoFn` elements, consider the following guidelines:

  * When you use [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once), the Dataflow service processes every element in your input `PCollection` by a `DoFn` instance _exactly once_.
  * The Dataflow service doesn't guarantee how many times a `DoFn` is invoked.
  * The Dataflow service doesn't guarantee exactly how the distributed elements are grouped. It does not guarantee which, if any, elements are processed together.
  * The Dataflow service doesn't guarantee the exact number of `DoFn` instances created over the course of a pipeline.
  * The Dataflow service is fault-tolerant and might retry your code multiple times if the workers encounter issues.
  * The Dataflow service might create backup copies of your code. Issues might occur with manual side effects, such as if your code relies on or creates temporary files with non-unique names.
  * The Dataflow service serializes element processing per `DoFn` instance. Your code doesn't need to be strictly thread-safe, but any state shared between multiple `DoFn` instances must be thread-safe.



### Create libraries of reusable transforms

The Apache Beam programming model lets you reuse transforms. By creating a shared library of common transforms, you can improve reusability, testability, and code ownership by different teams.

Consider the following two Java code examples, which both read payment events. Assuming that both pipelines perform the same processing, they can use the same transforms through a shared library for the remaining processing steps.

The first example is from an unbounded Pub/Sub source:
    
    
    PipelineOptions options = PipelineOptionsFactory.create();
    
    Pipeline p = Pipeline.create(options)
    
    // Initial read transform
    PCollection<PaymentEvent> payments =
        p.apply("Read from topic",
            PubSubIO.readStrings().withTimestampAttribute(...).fromTopic(...))
            .apply("Parse strings into payment events",
                ParDo.of(new ParsePaymentEventFn()));
    

The second example is from a bounded relational database source:
    
    
    PipelineOptions options = PipelineOptionsFactory.create();
    
    Pipeline p = Pipeline.create(options);
    
    PCollection<PaymentEvent> payments =
        p.apply(
            "Read from database table",
            JdbcIO.<PaymentEvent>read()
                .withDataSourceConfiguration(...)
                .withQuery(...)
                .withRowMapper(new RowMapper<PaymentEvent>() {
                  ...
                }));
    

How you implement code reusability best practices varies by programming language and by build tool. For example, if you use [Maven](https://maven.apache.org/), you can separate transform code into its own module. You can then include the module as a submodule in larger [multi-module projects](https://maven.apache.org/guides/mini/guide-multiple-modules.html) for different pipelines, as shown in the following code example:
    
    
    // Reuse transforms across both pipelines
    payments
        .apply("ValidatePayments", new PaymentTransforms.ValidatePayments(...))
        .apply("ProcessPayments", new PaymentTransforms.ProcessPayments(...))
      ...
    

For more information, see the following Apache Beam documentation pages:

  * [Requirements for writing user code for Apache Beam transforms](https://beam.apache.org/documentation/programming-guide/#requirements-for-writing-user-code-for-beam-transforms)
  * [`PTransform` style guide](https://beam.apache.org/contribute/ptransform-style-guide/): a style guide for writers of new reusable `PTransform` collections



### Use dead-letter queues for error handling

Sometimes your pipeline can't process elements. Data issues are a common cause. For example, an element that contains badly formatted JSON can cause parsing failures.

Although you can catch exceptions within the [`DoFn.ProcessElement`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/DoFn.ProcessElement.html) method, log the error, and drop the element, this approach both loses the data and prevents the data from being inspected later for manual handling or troubleshooting.

Instead, use a pattern called a _dead-letter queue_ (unprocessed messages queue). Catch exceptions in the `DoFn.ProcessElement` method and log errors. Instead of dropping the failed element, use branching outputs to write failed elements into a separate `PCollection` object. These elements are then written to a data sink for later inspection and handling with a separate transform.

The following Java code example shows how to implement the dead-letter queue pattern.
    
    
    TupleTag<Output> successTag = new TupleTag<>() {};
    TupleTag<Input> deadLetterTag = new TupleTag<>() {};
    
    PCollection<Input> input = /* ... */;
    
    PCollectionTuple outputTuple =
        input.apply(ParDo.of(new DoFn<Input, Output>() {
          @Override
          void processElement(ProcessContext c) {
            try {
              c.output(process(c.element()));
            } catch (Exception e) {
              LOG.severe("Failed to process input {} -- adding to dead-letter file",
                  c.element(), e);
              c.sideOutput(deadLetterTag, c.element());
            }
          }).withOutputTags(successTag, TupleTagList.of(deadLetterTag)));
    
    // Write the dead-letter inputs to a BigQuery table for later analysis
    outputTuple.get(deadLetterTag)
        .apply(BigQueryIO.write(...));
    
    // Retrieve the successful elements...
    PCollection<Output> success = outputTuple.get(successTag);
    // and continue processing ...
    

Use [Cloud Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring) to apply different monitoring and alerting policies for your pipeline's dead-letter queue. For example, you can visualize the number and size of elements processed by your dead-letter transform and configure alerting to trigger if certain threshold conditions are met.

#### Handle schema mutations

You can handle data that has unexpected but valid schemas by using a dead-letter pattern, which writes failed elements to a separate `PCollection` object. In some cases, you want to automatically handle elements that reflect a mutated schema as valid elements. For example, if an element's schema reflects a mutation like the addition of new fields, you can adapt the schema of the data sink to accommodate mutations.

Automatic schema mutation relies on the branching-output approach used by the dead-letter pattern. However, in this case it triggers a transform that mutates the destination schema whenever additive schemas are encountered. For an example of this approach, see [How to handle mutating JSON schemas in a streaming pipeline, with Square Enix](https://cloud.google.com/blog/products/gcp/how-to-handle-mutating-json-schemas-in-a-streaming-pipeline-with-square-enix) on the Google Cloud blog.

### Decide how to join datasets

Joining datasets is a common use case for data pipelines. You can use side inputs or the `CoGroupByKey` transform to perform joins in your pipeline. Each has benefits and downsides.

[Side inputs](https://beam.apache.org/documentation/programming-guide/#side-inputs) provide a flexible way to solve common data processing problems, such as data enrichment and keyed lookups. Unlike `PCollection` objects, side inputs are mutable and can be determined at runtime. For example, the values in a side input might be computed by another branch in your pipeline or determined by calling a remote service.

Dataflow supports side inputs by persisting data into persistent storage, similar to a shared disk. This configuration makes the complete side input available to all workers.

However, side input sizes can be very large and might not fit into worker memory. Reading from a large side input can cause performance issues if workers need to constantly read from persistent storage.

The [`CoGroupByKey`](https://beam.apache.org/documentation/programming-guide/#cogroupbykey) transform is a [core Apache Beam transform](https://beam.apache.org/documentation/programming-guide/#core-beam-transforms) that merges (flattens) multiple `PCollection` objects and groups elements that have a common key. Unlike a side input, which makes the entire side input data available to each worker, `CoGroupByKey` performs a shuffle (grouping) operation to distribute data across workers. `CoGroupByKey` is therefore ideal when the `PCollection` objects that you want to join are very large and don't fit into worker memory.

Follow these guidelines to help decide whether to use side inputs or `CoGroupByKey`:

  * Use side inputs when one of the `PCollection` objects you are joining is disproportionately smaller than the others, and the smaller `PCollection` object fits into worker memory. Caching the side input entirely into memory makes it fast and efficient to fetch elements.
  * Use side inputs when you have a `PCollection` object that must be joined multiple times in your pipeline. Instead of using multiple `CoGroupByKey` transforms, create a single side input that can be reused by multiple `ParDo` transforms.
  * Use `CoGroupByKey` if you need to fetch a large proportion of a `PCollection` object that significantly exceeds worker memory.



For more information, see [Troubleshoot Dataflow out of memory errors](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom).

### Minimize expensive per-element operations

A `DoFn` instance processes batches of elements called [bundles](https://beam.apache.org/documentation/runtime/model/#bundling-and-persistence), which are atomic units of work that consist of zero or more elements. Individual elements are then processed by the [`DoFn.ProcessElement`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/DoFn.ProcessElement.html) method, which runs for every element. Because the `DoFn.ProcessElement` method is called for every element, any time-consuming or computationally expensive operations that are invoked by that method run for every single element processed by the method.

If you need to perform costly operations only once for a batch of elements, include those operations in the `DoFn.Setup` method or the `DoFn.StartBundle` method instead of in the `DoFn.ProcessElement` element. Examples include the following operations:

  * Parsing a configuration file that controls some aspect of the `DoFn` instance's behavior. Only invoke this action one time, when the `DoFn` instance is initialized, by using the [`DoFn.Setup`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/DoFn.Setup.html) method.

  * Instantiating a short-lived client that is reused across all elements in a bundle, such as when all elements in the bundle are sent over a single network connection. Invoke this action one time per bundle by using the [`DoFn.StartBundle`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/DoFn.StartBundle.html) method.




### Limit batch sizes and concurrent calls to external services

When you call external services, you can reduce per-call overheads by using the [`GroupIntoBatches`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/GroupIntoBatches.html) transform. This transform creates batches of elements of a specified size. Batching sends elements to an external service as one payload instead of individually.

In combination with batching, limit the maximum number of parallel (concurrent) calls to the external service by choosing appropriate keys to partition the incoming data. The number of partitions determines the maximum parallelization. For example, if every element is given the same key, a downstream transform for calling the external service doesn't run in parallel.

Consider one of the following approaches to produce keys for elements:

  * Choose an attribute of the dataset to use as data keys, such as user IDs.
  * Generate data keys to split elements randomly over a fixed number of partitions, where the number of possible key values determines the number of partitions. You need to create enough partitions for parallelism. Each partition needs to have enough elements for the `GroupIntoBatches` transform to be useful.



The following Java code example shows how to randomly split elements over ten partitions:
    
    
    // PII or classified data which needs redaction.
    PCollection<String> sensitiveData = ...;
    
    int numPartitions = 10; // Number of parallel batches to create.
    PCollection<KV<Long, Iterable<String>>> batchedData =
        sensitiveData
            .apply("Assign data into partitions",
                ParDo.of(new DoFn<String, KV<Long, String>>() {
                  Random random = new Random();
    
                  @ProcessElement
                  public void assignRandomPartition(ProcessContext context) {
                    context.output(
                      KV.of(randomPartitionNumber(), context.element()));
                  }
                  private static int randomPartitionNumber() {
                    return random.nextInt(numPartitions);
                  }
                }))
            .apply("Create batches of sensitive data",
                GroupIntoBatches.<Long, String>ofSize(100L));
    
    // Use batched sensitive data to fully utilize Redaction API,
    // which has a rate limit but allows large payloads.
    batchedData
        .apply("Call Redaction API in batches", callRedactionApiOnBatch());
    

### Process slow per-element operations concurrently

When your `DoFn` performs slow per-element operations (such as calling an external machine learning model or web API), synchronous execution inside the `DoFn.ProcessElement` blocks worker threads until each operation completes. This blocking limits throughput and can cause bundle timeouts or high retry rates.

Even with optimal key partitioning, per-key serialization ensures that only one element is processed at a time per key. However, wrapping your `DoFn` class with `AsyncWrapper` breaks this constraint by processing elements concurrently in a background thread pool and returning control to the main runner before processing finishes. Using Beam state and timers, `AsyncWrapper` preserves [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once).

When you design a pipeline that uses `AsyncWrapper`, follow these guidelines:

  * **Partition incoming data with keys** : `AsyncWrapper` requires key-value input `KV<K, InputT>`. To distribute work across multiple workers and prevent serialization bottlenecks, partition your incoming dataset across an appropriate number of distinct keys.
  * **Limit worker concurrency** : Use the `parallelism` parameter to set the maximum number of concurrent operations allowed per worker node.
  * **Ensure thread safety** : If you set `parallelism` greater than 1 and your `DoFn` is stateful, your `DoFn` must also be thread-safe.
  * **Avoid bundle-level aggregation** : Don't use batching or aggregation logic inside `StartBundle` or `FinishBundle`, because `AsyncWrapper` invokes these lifecycle methods per element.
  * **Don't use tagged outputs** : Tagged multi-outputs (additional output tags) aren't supported.
  * **Tuning execution (Java)** : By default, tasks execute on the shared JVM `ForkJoinPool`. Set `useThreadPool=true` to isolate execution to a dedicated fixed thread pool sized to your configured parallelism. This approach avoids contention with other `ForkJoinPool` consumers in the same JVM.
  * **Tuning execution (Python)** : In the Python SDK however, `AsyncWrapper` supports an additional `use_asyncio=True` mode that executes coroutines inside an `asyncio` event loop instead of a background thread pool.



The following Java code examples show how to wrap a `DoFn` with `AsyncWrapper`:
    
    
    import org.apache.beam.sdk.transforms.AsyncWrapper;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.WithKeys;
    import org.apache.beam.sdk.values.KV;
    import org.apache.beam.sdk.values.PCollection;
    import org.joda.time.Duration;
    
    // Define a synchronous DoFn that makes slow external service calls.
    public class CallSlowExternalServiceFn extends DoFn<String, String> {
      private transient ExternalServiceClient externalServiceClient;
    
      @Setup
      public void setup() {
        externalServiceClient = new ExternalServiceClient();
      }
    
      @ProcessElement
      public void processElement(@Element String element, OutputReceiver<String> receiver) {
        String result = externalServiceClient.call(element);
        receiver.output(result);
      }
    }
    
    // Partition incoming data across distinct keys to distribute worker load.
    PCollection<KV<String, String>> keyedData = inputData.apply(
        WithKeys.of(element -> element.substring(0, 1))); // or your actual partition key
    
    // Wrap the DoFn with AsyncWrapper.
    PCollection<String> results = keyedData.apply(
        "Process Asynchronously",
        ParDo.of(
            new AsyncWrapper<String, String, String>(
                new CallSlowExternalServiceFn(),
                /* parallelism= */ 20,
                /* timerFrequency= */ Duration.standardSeconds(5),
                /* maxItemsToBuffer= */ 50,
                /* timeout= */ Duration.standardSeconds(1),
                /* maxWaitTime= */ Duration.millis(500),
                /* idFn= */ null, // defaults to element identity for deduplication
                /* useThreadPool= */ true)));
    

### Identify performance issues caused by fused steps

Dataflow builds a graph of steps that represents your pipeline based on the transforms and data that you used to construct it. This graph is called the [pipeline execution graph](https://docs.cloud.google.com/dataflow/docs/guides/job-graph).

When you deploy your pipeline, Dataflow might modify your pipeline's execution graph to improve performance. For example, Dataflow might fuse some operations together, a process known as [fusion optimization](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#fusion-and-combine-optimizations), to avoid the performance and cost impact of writing every intermediate `PCollection` object in your pipeline.

In some cases, Dataflow might incorrectly determine the optimal way to fuse operations in the pipeline, which can limit your job's ability to make use of all available workers. In those cases, you can prevent operations from being fused.

Consider the following example Apache Beam code. A [`GenerateSequence`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/GenerateSequence.html) transform creates a small bounded `PCollection` object, which is then further processed by two downstream `ParDo` transforms.

The `Find Primes Less-than-N` transform might be computationally expensive and is likely to run slowly for large numbers. In contrast, the `Increment Number` transform probably completes quickly.
    
    
    import com.google.common.math.LongMath;
    ...
    
    public class FusedStepsPipeline {
    
      final class FindLowerPrimesFn extends DoFn<Long, String> {
        @ProcessElement
        public void processElement(ProcessContext c) {
          Long n = c.element();
          if (n > 1) {
            for (long i = 2; i < n; i++) {
              if (LongMath.isPrime(i)) {
                c.output(Long.toString(i));
              }
            }
          }
        }
      }
    
      public static void main(String[] args) {
        Pipeline p = Pipeline.create(options);
    
        PCollection<Long> sequence = p.apply("Generate Sequence",
            GenerateSequence
                .from(0)
                .to(1000000));
    
        // Pipeline branch 1
        sequence.apply("Find Primes Less-than-N",
            ParDo.of(new FindLowerPrimesFn()));
    
        // Pipeline branch 2
        sequence.apply("Increment Number",
            MapElements.via(new SimpleFunction<Long, Long>() {
              public Long apply(Long n) {
                return ++n;
              }
            }));
    
        p.run().waitUntilFinish();
      }
    }
    

The following diagram shows a graphical representation of the pipeline in the Dataflow monitoring interface.

![Representation of pipeline flow in the Dataflow interface.](https://docs.cloud.google.com/static/dataflow/images/building-production-ready-data-pipelines-using-dataflow-developing-pipeline-flow.png)

The [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview) shows that the same slow rate of processing occurs for both transforms, specifically 13 elements-per-second. You might expect the `Increment Number` transform to process elements quickly, but instead it appears to be tied to the same rate of processing as `Find Primes Less-than-N`.

The reason is that Dataflow fused the steps into a single stage, which prevents them from running independently. You can use the [`gcloud dataflow jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe) command to find more information:
    
    
    gcloud dataflow jobs describe --full job-id --format json
    

In the resulting output, the fused steps are described in the [`ExecutionStageSummary`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#executionstagesummary) object in the [`ComponentTransform`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.ComponentTransform) array:
    
    
    ...
    
        "executionPipelineStage": [
          {
            "componentSource": [
              ...
            ],
            "componentTransform": [
              {
                "name": "s1",
                "originalTransform": "Generate Sequence/Read(BoundedCountingSource)",
                "userName": "Generate Sequence/Read(BoundedCountingSource)"
              },
              {
                "name": "s2",
                "originalTransform": "Find Primes Less-than-N",
                "userName": "Find Primes Less-than-N"
              },
              {
                "name": "s3",
                "originalTransform": "Increment Number/Map",
                "userName": "Increment Number/Map"
              }
            ],
            "id": "S01",
            "kind": "PAR_DO_KIND",
            "name": "F0"
          }
    
    ...
    

In this scenario, because the `Find Primes Less-than-N` transform is the slow step, breaking the fusion before that step is an appropriate strategy. One method to unfuse steps is to insert a [`GroupByKey`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/GroupByKey.html) transform and ungroup before the step, as shown in the following Java code example.
    
    
    sequence
        .apply("Map Elements", MapElements.via(new SimpleFunction<Long, KV<Long, Void>>() {
          public KV<Long, Void> apply(Long n) {
            return KV.of(n, null);
          }
        }))
        .apply("Group By Key", GroupByKey.<Long, Void>create())
        .apply("Emit Keys", Keys.<Long>create())
        .apply("Find Primes Less-than-N", ParDo.of(new FindLowerPrimesFn()));
    

You can also combine these unfusing steps into a reusable composite transform.

After you unfuse the steps, when you run the pipeline, `Increment Number` completes in a matter of seconds, and the much longer-running `Find Primes Less-than-N` transform runs in a separate stage.

This example applies a group and ungroup operation to unfuse steps. You can use other approaches for other circumstances. In this case, handling duplicate output is not an issue, given the consecutive output of the `GenerateSequence` transform. [`KV`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/values/KV.html) objects with duplicate keys are deduplicated to a single key in the group (`GroupByKey`) transform and the ungroup ([`Keys`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/Keys.html)) transform. To retain duplicates after the group and ungroup operations, create key-value pairs by using the following steps:

  1. Use a random key and the original input as the value.
  2. Group using the random key.
  3. Emit the values for each key as the output.



You can also use a [`Reshuffle`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/Reshuffle.html) transform to prevent fusion of surrounding transforms. However, the side effects of the `Reshuffle` transform are not portable across different [Apache Beam runners](https://beam.apache.org/documentation/runners/capability-matrix/).

For more information about parallelism and fusion optimization, see [Pipeline lifecycle](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle).

### Use Apache Beam metrics to collect pipeline insights

Apache Beam metrics is a utility class that produces metrics for reporting the properties of a running pipeline. When you [use Cloud Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring#custom-metrics), Apache Beam metrics are available as Cloud Monitoring custom metrics.

The following example shows Apache Beam [`Counter` metrics](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/metrics/Counter.html) used in a `DoFn` subclass.

The example code uses two counters. One counter tracks JSON parsing failures (`malformedCounter`), and the other counter tracks whether the JSON message is valid but contains an empty payload (`emptyCounter`). In Cloud Monitoring, the custom metric names are `custom.googleapis.com/dataflow/malformedJson` and `custom.googleapis.com/dataflow/emptyPayload`. You can use the custom metrics to create visualizations and alerting policies in Cloud Monitoring.
    
    
    final TupleTag<String> errorTag = new TupleTag<String>(){};
    final TupleTag<MockObject> successTag = new TupleTag<MockObject>(){};
    
    final class ParseEventFn extends DoFn<String, MyObject> {
    
      private final Counter malformedCounter = Metrics.counter(ParseEventFn.class, "malformedJson");
      private final Counter emptyCounter = Metrics.counter(ParseEventFn.class, "emptyPayload");
      private Gson gsonParser;
    
      @Setup
      public setup() {
        gsonParser = new Gson();
      }
    
      @ProcessElement
      public void processElement(ProcessContext c) {
        try {
          MyObject myObj = gsonParser.fromJson(c.element(), MyObject.class);
          if (myObj.getPayload() != null) {
            //  Output the element if non-empty payload
            c.output(successTag, myObj);
          }
          else {
            // Increment empty payload counter
            emptyCounter.inc();
          }
        }
        catch (JsonParseException e) {
          // Increment malformed JSON counter
          malformedCounter.inc();
          // Output the element to dead-letter queue
          c.output(errorTag, c.element());
        }
      }
    }
    

## Secure Cloud Storage buckets against pipeline attacks

To secure Cloud Storage buckets against a Dataflow pipeline attack, you must understand how a compromise can happen.

An attacker rarely targets Cloud Storage directly. Instead, they exploit a vulnerability called _shadow resource poisoning_. In this scenario, an attacker compromises the Cloud Storage bucket containing your Dataflow templates, metadata, or custom Python user-defined functions (UDFs) to inject malicious code. When Dataflow autoscales and starts a new worker VM, it pulls the compromised code from Cloud Storage, runs it, steals the worker's service account token, and extracts data from your source buckets.

To help stop this attack entry point, you need to lock down the Cloud Storage buckets that feed Dataflow, secure the pipelines themselves, and strictly limit the permissions on the Cloud Storage buckets.

### Protect Cloud Storage buckets

To help protect the point of injection, secure the buckets you use for Dataflow templates, staging files, and code dependencies. By implementing strict write-access controls on these buckets, you prevent unauthorized code from entering your worker environment.

  * **Isolate your buckets:** Separate your data buckets from your operational code buckets. Dataflow uses the `--stagingLocation` and `--tempLocation` flags. Keep these in a highly restricted, dedicated bucket completely separate from raw input or output data.
  * **Enforce uniform bucket-level access (UBLA):** Enable UBLA on all Dataflow-related buckets. This disables legacy, error-prone access control lists (ACLs) and ensures that only centralized Identity and Access Management (IAM) policies dictate who can access the files.
  * **Lock down write permissions:** Grant your CI/CD service account `roles/storage.objectAdmin` (write/delete) on your staging and template buckets. Grant developers and other service accounts, at most, `roles/storage.objectViewer` (read-only).
  * **Enable Object Versioning and Object Retention:** Enable Object Versioning on your template buckets. If a malicious actor or compromised account overwrites a template, you can instantly get an alert about the new version and revert changes. Combined with an Object Retention policy, this helps prevent bad actors from deleting your staging dependencies.



### Harden the Dataflow execution environment

To help maintain a secure execution environment and protect against data theft, restrict worker communication.

  * **Block internet egress (strict private networking):** When launching Dataflow, pass `--usePublicIps=false`. Also, configure your VPC firewall rules to block all egress to the public internet from your Dataflow subnets. If a worker is compromised, it can't open a reverse shell or exfiltrate data to an attacker-controlled external IP address.
  * **Enforce VPC Service Controls (VPC-SC):** Place your Cloud Storage data buckets and your Dataflow project inside a strict VPC-SC security perimeter. VPC-SC acts as a network wall that overrides IAM permissions. Even if an attacker steals a valid worker service account token, VPC-SC blocks any request to copy data from your Cloud Storage bucket to a bucket outside your organization's perimeter.



### Implement strict least privilege on data buckets

If a Dataflow worker is compromised, its affected area is defined by the IAM permissions of its service account.

  * **Avoid using the default Compute Engine service account:** This account defaults to having broad Editor permissions over the entire project. Use a dedicated, user-managed worker service account by using the `--serviceAccount` flag.
  * **Bucket-specific IAM roles:** Don't grant your Dataflow worker service account project-level storage roles, such as `roles/storage.admin`. Instead, grant rights directly on the specific buckets: 
    * **Input bucket:** Grant the `roles/storage.objectViewer` (read-only) role.
    * **Output bucket:** Grant the `roles/storage.objectCreator` (write-only, meaning it can create objects but can't read or overwrite existing data) role.
    * **Staging/temp bucket:** Grant the `roles/storage.objectAdmin` (read, write, and delete) roles.



### Secure custom containers and software supply chain

If you use custom Docker images for your Dataflow dependencies by using `--sdkContainerImage`, an attacker might try to poison the image registry rather than a Cloud Storage bucket.

  * **Scan Artifact Registry:** Store your custom worker images in Artifact Registry and enable **Vulnerability Scanning**.
  * **Use immutable image digests:** Instead of referencing an image by a mutable tag such as `us-docker.pkg.dev/my-project/dataflow-worker:latest`, specify the exact, unchangeable cryptographic SHA digest in your pipeline options:
        
        **--sdkContainerImage =**us-docker.pkg.dev/my-project/dataflow-worker@sha256:7b9c...`
        

This helps ensure that the exact code you scanned and approved in CI/CD is what runs on the workers, entirely blocking image-substitution attacks.




### Use logging to catching anomalies

Secure configurations help to stop the attack, but you should also set up Cloud Logging alerts for the following triggers:

  1. Events on your Dataflow template or staging Cloud Storage buckets that originate from a non-CI/CD identity, such as `storage.objects.update` or `storage.objects.create` requests.
  2. High volumes of `storage.objects.get` requests from unexpected IP addresses or unusual spikes in data volume moving through Dataflow, which might indicate an active exfiltration attempt.



## Migrate a pipeline between Google Cloud projects

Dataflow jobs are bound to the Google Cloud project where you created them. You can't move a job directly to a different project. To move a pipeline to another project, you stop the existing job and recreate it in the new project. For a detailed guide on this process, see [Migrate pipeline jobs to another Google Cloud project](https://docs.cloud.google.com/dataflow/docs/guides/migrate-your-jobs).

## Learn more

The following pages provide more information about how to structure your pipeline, how to choose which transforms to apply to your data, and what to consider when choosing your pipeline's input and output methods.

  * [Develop and test Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/develop-and-test-pipelines).
  * [Design your pipeline](https://beam.apache.org/documentation/pipelines/design-your-pipeline/).
  * [Create your pipeline](https://beam.apache.org/documentation/pipelines/create-your-pipeline/).



For more information about building your user code, see the [requirements for user-provided functions](https://beam.apache.org/documentation/programming-guide/#requirements-for-writing-user-code-for-beam-transforms). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
