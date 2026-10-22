---
url: https://docs.cloud.google.com/dataflow/docs/dynamic-work-rebalancing/
title: Dynamic work rebalancing \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:19.340948+00:00
---

# Dynamic work rebalancing  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/dynamic-work-rebalancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dynamic work rebalancing Stay organized with collections  Save and categorize content based on your preferences. 

The Dynamic Work Rebalancing feature of the Dataflow service allows the service to dynamically repartition work based on runtime conditions. These conditions might include the following:

  * Imbalances in work assignments
  * Workers taking longer than expected to finish
  * Workers finishing faster than expected



The Dataflow service automatically detects these conditions and can dynamically assign work to unused or underused workers to decrease the overall processing time of your job. For more information about how Dataflow distributes and scales execution, see [Understanding parallelism in Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/parallelism).

## Limitations

Dynamic work rebalancing only happens when the Dataflow service is processing some input data in parallel: when reading data from an external input source, when working with a materialized intermediate `PCollection`, or when working with the result of an aggregation like `GroupByKey`. If a large number of steps in your job are [fused](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#fusion_optimization), your job has fewer intermediate `PCollection`s, and dynamic work rebalancing is limited to the number of elements in the source materialized `PCollection`. If you want to ensure that dynamic work rebalancing can be applied to a particular `PCollection` in your pipeline, you can [prevent fusion](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#prevent_fusion) in a few different ways to ensure dynamic parallelism.

Dynamic work rebalancing cannot reparallelize data finer than a single record. If your data contains individual records that cause large delays in processing time, they might still delay your job. Dataflow can't subdivide and redistribute an individual "hot" record to multiple workers.

### Java

If you set a fixed number of shards for the final output of your pipeline (for example, by writing data using `TextIO.Write.withNumShards`), Dataflow limits parallelization based on the number of shards that you choose.

### Python

If you set a fixed number of shards for the final output of your pipeline (for example, by writing data using `beam.io.WriteToText(..., num_shards=...)`), Dataflow limits parallelization based on the number of shards that you choose.

### Go

If you set a fixed number of shards for the final output of your pipeline, Dataflow limits parallelization based on the number of shards that you choose.

**Note:** The fixed-shards limitation can be considered temporary, and might be subject to change in future releases of the Dataflow service.

## Working with Custom Data Sources

### Java

If your pipeline uses a custom data source that you provide, you must implement the method `splitAtFraction` to allow your source to work with the dynamic work rebalancing feature.

**Caution:** Using dynamic work rebalancing with custom data sources is an advanced use case. If you choose to implement `splitAtFraction`, it's critical that you test your code extensively and with maximum code coverage.

If you implement `splitAtFraction` incorrectly, records from your source might appear to get duplicated or dropped. See the [API reference information on RangeTracker](https://beam.apache.org/documentation/sdks/javadoc/current/index.html?org/apache/beam/sdk/io/range/RangeTracker.html) for help and tips on implementing `splitAtFraction`.

### Python

If your pipeline uses a custom data source that you provide, your `RangeTracker` must implement `try_claim`, `try_split`, `position_at_fraction`, and `fraction_consumed` to allow your source to work with the dynamic work rebalancing feature.

See the [API reference information on RangeTracker](https://beam.apache.org/documentation/sdks/pydoc/current/apache_beam.io.iobase.html#apache_beam.io.iobase.RangeTracker) for more information.

### Go

If your pipeline uses a custom data source that you provide, you must implement a valid `RTracker` to allow your source to work with the dynamic work rebalancing feature.

For more information, see the [RTracker API reference information](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core/sdf#RTracker).

Dynamic work rebalancing uses the return value of the `getProgress()` method of your custom source to activate. The default implementation for `getProgress()` returns `null`. To ensure autoscaling activates, make sure your custom source overrides `getProgress()` to return an appropriate value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
