---
url: https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java/
title: Java task patterns \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:49.219022+00:00
---

# Java task patterns  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Java task patterns Stay organized with collections  Save and categorize content based on your preferences. 

The [ecommerce sample application](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-retail-pipeline) demonstrates best practices for using Dataflow to implement streaming data analytics and real-time AI. The example contains task patterns that show the best way to accomplish Java programming tasks. These tasks are commonly needed to create ecommerce applications.

The application contains the following Java task patterns:

  * Use Apache Beam schemas to work with structured data
  * Use JsonToRow to convert JSON data
  * Use the `AutoValue` code generator to generate plain old Java objects (POJOs)
  * Queue unprocessable data for further analysis
  * Apply data validation transforms serially
  * Use `DoFn.StartBundle` to micro-batch calls to external services
  * Use an appropriate side-input pattern



## Use Apache Beam schemas to work with structured data

You can use [Apache Beam schemas](https://beam.apache.org/documentation/programming-guide/#schemas) to make processing structured data easier.

Converting your objects to [Rows](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/values/Row.html) lets you produce very clean Java code, which makes your [directed acyclic graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) building exercise easier. You can also reference object properties as fields within the analytics statements that you create, instead of having to call methods.

### Example

[CountViewsPerProduct.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/transforms/clickstream/CountViewsPerProduct.java)

## Use JsonToRow to convert JSON data

Processing JSON strings in Dataflow is a common need. For example, JSON strings are processed when streaming clickstream information captured from web applications. To process JSON strings, you need to convert them into either [Rows](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/values/Row.html) or [plain old Java objects (POJOs)](https://en.wikipedia.org/wiki/Plain_old_Java_object) during pipeline processing.

You can use the Apache Beam built-in transform [JsonToRow](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/JsonToRow.html) to convert JSON strings to Rows. However, if you want a queue for processing unsuccessful messages, you need to build that separately, see Queuing unprocessable data for further analysis.

If you need to convert a JSON string to a POJO using [AutoValue](https://github.com/google/auto/tree/master/value), register a schema for the type by using the `@DefaultSchema(AutoValueSchema.class)` annotation, then use the [Convert](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/schemas/transforms/Convert.html) utility class. The resulting code is similar to the following:
    
    
    PCollection<String> json = ...
    
    PCollection<MyUserType>  = json
      .apply("Parse JSON to Beam Rows", JsonToRow.withSchema(expectedSchema))
      .apply("Convert to a user type with a compatible schema registered", Convert.to(MyUserType.class))
    

For more information, including what different Java types you can infer schemas from, see [Creating Schemas](https://beam.apache.org/documentation/programming-guide/#creating-schemas).

If JsonToRow does not work with your data, [Gson](https://github.com/google/gson/blob/master/UserGuide.md) is an alternative. Gson is fairly relaxed in its default processing of data, which might require you to build more validation into the data conversion process.

### Examples

  * [ClickstreamProcessing.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/transforms/clickstream/ClickstreamProcessing.java)
  * [JSONUtils.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/utils/JSONUtils.java)



## Use the `AutoValue` code generator to generate POJOs

[Apache Beam schemas](https://beam.apache.org/documentation/programming-guide/#schemas) are often the best way to represent objects in a pipeline, because of the way they let you work with structured data. Nevertheless, at times a [plain old Java object (POJO)](https://en.wikipedia.org/wiki/Plain_old_Java_object) is needed, such as when dealing with key-value objects or handling object state. Hand building POJOs requires you to code overrides for the `equals()` and `hashcode()` methods, which can be time consuming and error prone. Incorrect overrides might result in inconsistent application behavior or data loss.

To generate POJOs, use the [`AutoValue`](https://github.com/google/auto/tree/master/value) class builder. This option ensures that the necessary overrides are used and lets you avoid potential errors. `AutoValue` is heavily used within the Apache Beam codebase, so familiarity with this class builder is useful if you want to develop Apache Beam pipelines on Dataflow using Java.

You can also `AutoValue` with Apache Beam schemas if you add an `@DefaultSchema(AutoValueSchema.class)` annotation. For more information, see [Creating Schemas](https://beam.apache.org/documentation/programming-guide/#creating-schemas).

For more information about `AutoValue`, see [Why `AutoValue?`](https://docs.google.com/presentation/d/14u_h-lMn7f1rXE1nDiLX0azS3IkgjGl5uxp5jGJ75RE/edit#slide=id.g2a5e9c4a8_00) and the [`AutoValue` docs](https://github.com/google/auto/blob/master/value/userguide/index.md).

### Example

[Clickstream.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/data-objects/src/main/java/com/google/dataflow/sample/retail/dataobjects/ClickStream.java)

## Queue unprocessable data for further analysis

In production systems, it is important to handle problematic data. If possible, you validate and correct data in-stream. When correction isn't possible, log the value to an unprocessed messages queue, sometimes called a dead-letter queue, for later analysis. Issues commonly occur when converting data from one format to another, for example when converting JSON strings to [Rows](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/values/Row.html).

To address this issue, use a multi-output transform to shuttle the elements containing the unprocessed data into another [PCollection](https://beam.apache.org/documentation/programming-guide/#pcollections) for further analysis. This processing is a common operation that you might want to use in many places in a pipeline. Try to make the transform generic enough to use in multiple places. First, create an error object to wrap common properties, including the original data. Next, create a sink transform that has multiple options for the destination.

### Examples

  * [JSONUtils.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/utils/JSONUtils.java)
  * [ErrorMsg.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/transforms/ErrorMsg.java)
  * [DeadLetterSink.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/transforms/DeadLetterSink.java)



## Apply data validation transforms serially

Data collected from external systems often needs cleaning. Structure your pipeline so that it can correct problematic data in-stream when possible. Send the data to a queue for further analysis when needed.

Because a single message might suffer from multiple issues that need correction, plan out the needed [directed acyclic graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph). If an element contains data with multiple defects, you must ensure that the element flows through the appropriate transforms.

For example, imagine an element with the following values, neither of which should be null:

`{"itemA": null,"itemB": null}`

Make sure the element flows through transforms that correct both potential issues:

`badElements.apply(fixItemA).apply(fixItemB)`

Your pipeline might have more serial steps, but [fusion](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#fusion_optimization) helps to minimize the processing overhead introduced.

### Example

[ValidateAndCorrectCSEvt.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/transforms/clickstream/ValidateAndCorrectCSEvt.java)

## Use `DoFn.StartBundle` to micro-batch calls to external services

You might need to invoke external APIs as part of your pipeline. Because a pipeline distributes work across many compute resources, making a single call for each element flowing through the system can overwhelm an external service endpoint. This issue is particularly common when you haven't applied any reducing functions.

To avoid this issue, batch calls to external systems.

You can batch calls using a `GroupByKey` transform or using the Apache Beam Timer API. However, these approaches both require [shuffling](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch), which introduces some processing overhead and the need for a [magic number](https://en.wikipedia.org/wiki/Magic_number_\(programming\)) to determine the key space.

Instead, use the [`StartBundle`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/DoFn.StartBundle.html) and [`FinishBundle`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/DoFn.FinishBundle.html) lifecycle elements to batch your data. With these options, no shuffling is needed.

One minor downside to this option is that bundle sizes are dynamically determined by the implementation of the runner based on what's currently happening inside the pipeline and its workers. In stream mode, bundles are often small in size. Dataflow bundling is influenced by backend factors like sharding usage, how much data is available for a particular key, and the throughput of the pipeline.

### Example

[EventItemCorrectionService.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/core/transforms/clickstream/validation/EventItemCorrectionService.java)

## Use an appropriate side-input pattern for data enrichment

In streaming analytics applications, data is often enriched with additional information that might be useful for further analysis. For example, if you have the store ID for a transaction, you might want to add information about the store location. This additional information is often added by taking an element and bringing in information from a lookup table.

For lookup tables that are both slowly changing and smaller in size, bringing the table into the pipeline as a singleton class that implements the `Map<K,V>` interface works well. This option lets you avoid having each element do an API call for its lookup. After you include a copy of a table in the pipeline, you need to update it periodically to keep it fresh.

To handle slow updating side inputs, use the Apache Beam [Side input patterns](https://beam.apache.org/documentation/patterns/side-inputs/).

### Caching

Side inputs are loaded in memory and are therefore cached automatically.

You can set the size of the cache by using the `--setWorkerCacheMb` option.

You can share the cache across `DoFn` instances and use external triggers to refresh the cache.

### Example

[SlowMovingStoreLocationDimension.java](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/blob/master/retail/retail-java-applications/data-engineering-dept/business-logic/src/main/java/com/google/dataflow/sample/retail/businesslogic/externalservices/SlowMovingStoreLocationDimension.java)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
