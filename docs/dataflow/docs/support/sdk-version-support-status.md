---
url: https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status/
title: SDK version support status \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:50.221770+00:00
---

# SDK version support status  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  SDK version support status Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the Dataflow support status for the Apache Beam SDK and Dataflow SDK releases:

  * Apache Beam SDK support-level definitions
  * Apache Beam 2.x SDKs
  * Dataflow 2.x SDKs



For instructions on installing or upgrading SDK versions in your project, see [Install or update the Apache Beam SDK](https://docs.cloud.google.com/dataflow/docs/guides/installing-beam-sdk).

## Apache Beam SDK support-level definitions

The following are the Dataflow support levels for the Apache Beam SDK:

  * **Supported** : Apache Beam SDK versions are supported by Dataflow from their release date until their deprecation date.
  * **Deprecated** : When an SDK version is deprecated, it continues to work with Dataflow but might be decommissioned in the future. Before an SDK version is decommissioned, customers are notified and given time to upgrade their environments. Requests for jobs submitted from deprecated SDK versions result in a warning message. It's recommended that you update environments that use a deprecated version of an SDK to a supported version, but deprecated SDK versions continue to work with Dataflow.
  * **Decommissioned** : Decommissioned SDK versions no longer work with Dataflow. Requests for jobs submitted from decommissioned SDK versions result in an error. To use the SDK with Dataflow, you must update your environment to an SDK version that is not decommissioned. It's recommended that you update the SDK to a supported version. SDK versions are rarely decommissioned. Before an SDK version is decommissioned, customers are notified and given time to upgrade their environments.



The previous definitions don't apply to SDKs or features that have never been supported.

## Apache Beam 2.x SDKs

[Apache Beam](http://beam.apache.org/) is an open source, community-led project. Google and Google Cloud are part of the Apache Beam community, but we don't own the project or control the release process. We might open bugs or submit patches to the Apache Beam codebase on behalf of Dataflow customers. We cannot create hotfixes or official releases of Apache Beam on demand. See the [Apache Beam policies](https://beam.apache.org/community/policies/) page for more details about release policies.

Dataflow supports specific Apache Beam SDK components for the SDK releases listed on this page. These components have been tested thoroughly with Dataflow. Experimental features are not supported.

See the [Apache Beam release notes](https://beam.apache.org/get-started/downloads/#releases) for change information.

**Note:** Development SDK versions (marked as `-SNAPSHOT` for Java and `.dev` for Python and Go) are unsupported.

The following tables contain the support status for the Apache Beam 2.x SDKs, including the Apache Beam Python SDK, Apache Beam Java SDK, and the Apache Beam Go SDK:

### Java

SDK version | Status | Supported components | Details  
---|---|---|---  
2.77.0 | Supported |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
|  This version will be deprecated on October 7, 2027.  
2.76.0 | Supported |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
|  This version will be deprecated on August 31, 2027.  
2.75.0 | Supported |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
|  This version will be deprecated on July 8, 2027. **Known issue:** Pipelines with a moderate to heavy Cloud Storage read workload might experience a performance regression. This issue affects Apache Beam versions 2.74.0 and 2.75.0 and will be fixed in 2.76.0. To resolve this issue, downgrade to Apache Beam 2.73.0. See [Apache Beam GitHub issue #39548](https://github.com/apache/beam/issues/39548).  
2.74.0 | Supported |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
|  This version will be deprecated on June 2, 2027. **Known issue:** Pipelines with a moderate to heavy Cloud Storage read workload might experience a performance regression. This issue affects Apache Beam versions 2.74.0 and 2.75.0 and will be fixed in 2.76.0. To resolve this issue, downgrade to Apache Beam 2.73.0. See [Apache Beam GitHub issue #39548](https://github.com/apache/beam/issues/39548).  
2.73.0 | Supported |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| This version will be deprecated on April 29, 2027.  
2.72.0 | Supported |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| This version will be deprecated on March 30, 2027.  
2.71.0 | Supported |  **Warning:** `Spanner Change Stream` Dataflow query ended early in high cpu utilization due to accidentally advancing the restriction tracker to the unbounded end timestamp of the original range. See [Apache Beam GitHub issue #39821](https://github.com/apache/beam/issues/39821) for details. To mitigate the problem, downgrade to 2.66.0 (or before), or upgrade to 2.72.0 (or later)". org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| This version will be deprecated on January 22, 2027.  
2.70.0 | Supported |  **Warning:** `Spanner Change Stream` Dataflow query ended early in high cpu utilization due to accidentally advancing the restriction tracker to the unbounded end timestamp of the original range. See [Apache Beam GitHub issue #39821](https://github.com/apache/beam/issues/39821) for details. To mitigate the problem, downgrade to 2.66.0 (or before), or upgrade to 2.72.0 (or later)". org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| This version will be deprecated on December 16, 2026.  
2.69.0 | Supported |  **Warning:** `Spanner Change Stream` Dataflow query ended early in high cpu utilization due to accidentally advancing the restriction tracker to the unbounded end timestamp of the original range. See [Apache Beam GitHub issue #39821](https://github.com/apache/beam/issues/39821) for details. To mitigate the problem, downgrade to 2.66.0 (or before), or upgrade to 2.72.0 (or later)". org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| This version will be deprecated on October 28, 2026.  
2.68.0 | Deprecated |  **Warning:** `Spanner Change Stream` Dataflow pipeline stopped with `succeeded` state or reading become stuck due to watermark of partition moving backwards. See [Apache Beam GitHub issue #36470](https://github.com/apache/beam/issues/36470) for details. To mitigate the problem, downgrade to 2.66.0 (or before), or upgrade to 2.69.0 (or later)". **Warning:** `Spanner Change Stream` Dataflow query ended early in high cpu utilization due to accidentally advancing the restriction tracker to the unbounded end timestamp of the original range. See [Apache Beam GitHub issue #39821](https://github.com/apache/beam/issues/39821) for details. To mitigate the problem, downgrade to 2.66.0 (or before), or upgrade to 2.72.0 (or later)". org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on September 22, 2026.  
2.67.0 | Supported |  **Warning:** `Spanner Change Stream` Dataflow pipeline stopped with `succeeded` state or reading become stuck due to watermark of partition moving backwards. See [Apache Beam GitHub issue #36470](https://github.com/apache/beam/issues/36470) for details. To mitigate the problem, downgrade to 2.66.0 (or before), or upgrade to 2.69.0 (or later)". **Warning:** `Spanner Change Stream` Dataflow query ended early in high cpu utilization due to accidentally advancing the restriction tracker to the unbounded end timestamp of the original range. See [Apache Beam GitHub issue #39821](https://github.com/apache/beam/issues/39821) for details. To mitigate the problem, downgrade to 2.66.0 (or before), or upgrade to 2.72.0 (or later)". org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| This version will be deprecated on August 12, 2026.  
2.66.0 | Supported |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| This version will be deprecated on July 1, 2026.  
2.65.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on May 12, 2026.  
2.64.0 | Deprecated |  **Warning:** The version of protobuf installed in this version has a [bug](https://github.com/protocolbuffers/protobuf/issues/20599) leading to incompatibilities with clients using 3.x versions of Protobuf. You can see an example of this in [GitHub repository issue #2191](https://github.com/GoogleCloudPlatform/DataflowTemplates/issues/2191). This issue has been seen in SpannerIO in particular and manifests as a `NoClassDefFoundError`. org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on March 31, 2026.  
2.63.0 | Deprecated |  **Warning:** The version of protobuf installed in this version has a [bug](https://github.com/protocolbuffers/protobuf/issues/20599) leading to incompatibilities with clients using 3.x versions of Protobuf. You can see an example of this in [GitHub repository issue #2191](https://github.com/GoogleCloudPlatform/DataflowTemplates/issues/2191). This issue has been seen in SpannerIO in particular and manifests as a `NoClassDefFoundError`. **Warning:** On Dataflow, when Java SDK is used, Coders that extend CustomCoder (excluding SchemaCoder and RowCoder) are update incompatible with previous versions (prior to 2.63) of the same transform. This includes PubSubIO's read. See [Apache Beam GitHub issue #34933](https://github.com/apache/beam/issues/34933). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on February 18, 2026.  
2.62.0 | Deprecated |  **Warning:** Using `FileBasedIO (like GCSIO)` and accessing very large number of file paths, can degrade functionalities such as metrics monitoring, job reload/restart. See [Apache Beam GitHub issue #34052](https://github.com/apache/beam/issues/34052) for details. Immediately upgrade to 2.63.0 or later. org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on January 21, 2026. **Known issue:** On Dataflow Streaming Appliance jobs, commits can fail with KeyCommitTooLargeException when a key outputs >180MB of results. Bug affects versions 2.60.x to 2.62.x, fix will be released with 2.63.0. To resolve this issue, downgrade to Apache Beam 2.59.0 or upgrade to Apache Beam 2.63.0 or enable [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine#use). See [Apache Beam GitHub issue #33588](https://github.com/apache/beam/issues/33588).  
2.61.0 | Deprecated |  **Warning:** When you use `Managed.write(ICEBERG)` to write to partitioned tables, the sink might incorrectly assign partition values in the DataFile metadata. See the [Apache Beam GitHub issue #33497](https://github.com/apache/beam/issues/33497). For Portable Runner pipelines, `Managed.write(ICEBERG)` will be automatically upgraded to a version with the fix. **Warning:** Using `FileBasedIO (like GCSIO)` and accessing very large number of file paths, can degrade functionalities such as metrics monitoring, job reload/restart. See [Apache Beam GitHub issue #34052](https://github.com/apache/beam/issues/34052) for details. Immediately upgrade to 2.63.0 or later. org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on November 25, 2025. **Known issue:** On Dataflow Streaming Appliance jobs, commits can fail with KeyCommitTooLargeException when a key outputs >180MB of results. Bug affects versions 2.60.x to 2.62.x, fix will be released with 2.63.0. To resolve this issue, downgrade to Apache Beam 2.59.0 or upgrade to Apache Beam 2.63.0 or enable [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine#use). See [Apache Beam GitHub issue #33588](https://github.com/apache/beam/issues/33588).  
2.60.0 | Deprecated |  **Warning:** When you use `Managed.write(ICEBERG)` to write to partitioned tables, the sink might incorrectly assign partition values in the DataFile metadata. See the [Apache Beam GitHub issue #33497](https://github.com/apache/beam/issues/33497). For Portable Runner pipelines, `Managed.write(ICEBERG)` will be automatically upgraded to a version with the fix. **Warning:** Using `FileBasedIO (like GCSIO)` and accessing very large number of file paths, can degrade functionalities such as metrics monitoring, job reload/restart. See [Apache Beam GitHub issue #34052](https://github.com/apache/beam/issues/34052) for details. Immediately upgrade to 2.63.0 or later. org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on October 17, 2025. **Known issue:** On Dataflow Streaming Appliance jobs, commits can fail with KeyCommitTooLargeException when a key outputs >180MB of results. Bug affects versions 2.60.x to 2.62.x, fix will be released with 2.63.0. To resolve this issue, downgrade to Apache Beam 2.59.0 or upgrade to Apache Beam 2.63.0 or enable [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine#use). See [Apache Beam GitHub issue #33588](https://github.com/apache/beam/issues/33588).  
2.59.0 | Deprecated |  **Warning:** When you use `Managed.write(ICEBERG)` to write to partitioned tables, the sink might incorrectly assign partition values in the DataFile metadata. See the [Apache Beam GitHub issue #33497](https://github.com/apache/beam/issues/33497). For Portable Runner pipelines, `Managed.write(ICEBERG)` will be automatically upgraded to a version with the fix. **Warning:** Using `FileBasedIO (like GCSIO)` and accessing very large number of file paths, can degrade functionalities such as metrics monitoring, job reload/restart. See [Apache Beam GitHub issue #32649](https://github.com/apache/beam/issues/32649) for details. Immediately upgrade to 2.63.0 or later. org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on September 11, 2025.  
2.58.1 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on August 16, 2025.  
2.58.0 | Deprecated |  **Warning:** When you use `KafkaIO.read()` or `KafkaIO.readBytes()` with Portable Runner, offsets aren't committed when you configure them with `commitOffsetsInFinalize`. See the [Apache Beam GitHub issue #32196](https://github.com/apache/beam/issues/32196). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on August 6, 2025.  
2.57.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on June 26, 2025.  
2.56.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-iceberg  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
org.apache.beam:beam-sdks-java-managed  
| Deprecated on May 1, 2025.  
2.55.1 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on April 8, 2025.  
2.55.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on March 25, 2025. **Known issue:** The `WriteToJson` transform in cross-language pipelines fails with an error. To resolve this issue, upgrade to Apache Beam 2.55.1. For more information, see [Issue #30776: Beam YAML `WriteToJson` fails](https://github.com/apache/beam/issues/30776).  
2.54.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on February 14, 2025.  
2.53.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on January 4, 2025.  
2.52.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on November 17, 2024.  
2.51.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on October 12, 2024.  
2.50.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on August 30, 2024.  
2.49.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on July 17, 2024.  
2.48.0 | Deprecated |  **Warning:** In version 2.48.0, when you use Pub/Sub sinks with batch jobs, your pipeline might incorrectly receive the error `SizeLimitExceededException` for any messages that are larger than 100 bytes. For more information, see the [Apache Beam GitHub issue #27000](https://github.com/apache/beam/issues/27000). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on May 31, 2024.  
2.47.0 | Deprecated |  **Warning:** In versions 2.45.0 to 2.47.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink and exactly-once semantics or when using the [`autoSchemaUpdate`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withAutoSchemaUpdate-boolean-) option, your streaming pipelines might have issues with data consistency. This issue occurs because of the ordering mismatch between the user-specified data schema and the schema defined in BigQuery. For more information, see the [Apache Beam GitHub issue #26789](https://github.com/apache/beam/issues/26789). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on May 10, 2024.  
2.46.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). **Warning:** In versions 2.45.0 to 2.47.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink and exactly-once semantics or when using the [`autoSchemaUpdate`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withAutoSchemaUpdate-boolean-) option, your streaming pipelines might have issues with data consistency. This issue occurs because of the ordering mismatch between the user-specified data schema and the schema defined in BigQuery. For more information, see the [Apache Beam GitHub issue #26789](https://github.com/apache/beam/issues/26789). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on March 10, 2024.  
2.45.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). **Warning:** In versions 2.45.0 to 2.47.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink and exactly-once semantics or when using the [`autoSchemaUpdate`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html#withAutoSchemaUpdate-boolean-) option, your streaming pipelines might have issues with data consistency. This issue occurs because of the ordering mismatch between the user-specified data schema and the schema defined in BigQuery. For more information, see the [Apache Beam GitHub issue #26789](https://github.com/apache/beam/issues/26789). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on February 15, 2024.  
2.44.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on January 13, 2024.  
2.43.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on November 17, 2023.  
2.42.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on October 17, 2023.  
2.41.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on August 23, 2023.  
2.40.0 | Deprecated |  **Warning:** If your pipeline writes to BigQuery, do NOT use 2.40.0. Under certain circumstances, if the sink is idle, an invalid timestamp can be emitted, throwing an exception and preventing the job from being drained. In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on June 27, 2023.  
2.39.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on May 25, 2023.  
2.38.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on April 20, 2023.  
2.37.0 | Deprecated |  **Warning:** In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on March 4, 2023.  
2.36.0 | Deprecated |  **Warning:** If your pipeline reads from a Spanner database, do NOT use 2.34.0 to 2.36.0. Immediately upgrade to 2.37.0 or later. In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on February 7, 2023.  
2.35.0 | Deprecated |  **Warning:** If your pipeline reads from a Spanner database, do NOT use 2.34.0 to 2.36.0. Immediately upgrade to 2.37.0 or later. In versions 2.35.0 to 2.46.0, when using the `STORAGE_WRITE_API` method with a BigQuery sink, your batch pipelines might have issues with data consistency due to the handling of unrelated transient errors. For more information, see the [Apache Beam GitHub issue #26521](https://github.com/apache/beam/issues/26521). org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-io-jdbc  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on December 29, 2022.  
2.34.0 | Deprecated |  **Warning:** If your pipeline reads from a Spanner database, do NOT use 2.34.0 – 2.36.0. Immediately upgrade to 2.37.0 or later.  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
org.apache.beam:beam-sdks-java-extensions-sql  
| Deprecated on November 11, 2022.  
2.33.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
| Deprecated on October 7, 2022.  
2.32.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
| Deprecated on August 25, 2022.  
2.31.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
| Deprecated on July 8, 2022.  
2.30.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
| Deprecated on June 10, 2022.   
2.29.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on April 29, 2022. Known issue: If you use Portable Runner, by default Dataflow will use a Java 8 SDK container regardless of user Java version. To work around for Java 11, you can override the default SDK image by providing pipeline option `--worker_harness_container_image=gcr.io/cloud-dataflow/v1beta3/beam_java11_sdk:2.29.0`. See [Apache Beam issue tracker](https://issues.apache.org/jira/browse/BEAM-12337) for more information.   
2.28.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on February 22, 2022.  
2.27.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on January 7, 2022. This release adds support for JDK 11.  
2.26.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on December 11, 2021.  
2.25.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on October 23, 2021.  
2.24.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on September 18, 2021. **Known issue:** If you use timers that reset, rather than timers that are set and only fired once, you shouldn't upgrade to 2.24.0. When a timer fires but is reset prior to being executed, a watermark hold can be leaked, causing your pipeline job to be stuck. See the [Apache Beam issue tracker](https://jira.apache.org/jira/browse/BEAM-10991) for more information.   
2.23.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on July 29, 2021.  
2.22.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
Google Cloud I/O connectors under module org.apache.beam:beam-runners-google-cloud-dataflow-java: bigquery, bigtable, datastore, healthcare, pubsub, spanner  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on June 8, 2021.  
2.21.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on May 27, 2021.  
2.20.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on April 15, 2021.  
2.19.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on February 4, 2021.  
2.18.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on January 23, 2021.  
2.17.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on January 6, 2021.  
2.16.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on October 7, 2020.  
2.15.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on August 23, 2020. **Known issues:**

  * Dataflow users who use schema features (including SQL transforms) shouldn't upgrade to 2.15.0 due to a known issue. See the [Apache Beam issue tracker](https://jira.apache.org/jira/browse/BEAM-8111) for more information.

  
2.14.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on August 1, 2020.  
2.13.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on June 6, 2020. This release adds experimental support for JDK 9 and later versions. See the [Apache Beam issue tracker](https://jira.apache.org/jira/browse/BEAM-2530) for more information.  
2.12.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated on April 25, 2020. **Known issues:**

  * The Dataflow runner has an incorrect logging configuration that might cause all logs to be missing. To work around this issue, add `slf4j-jdk14` to your runtime dependencies.

  
2.11.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated as of March 1, 2020. **Known issues:**

  * The Dataflow runner has an incorrect logging configuration that might cause all logs to be missing. To work around this issue, add `slf4j-jdk14` to your runtime dependencies.

  
2.10.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated as of February 11, 2020. **Known issues:**

  * SDK 2.10.0 depends on [gcsio client library](https://mvnrepository.com/artifact/com.google.cloud.bigdataoss/gcsio) version 1.9.13, which has known issues: 
    * Reading side inputs can result in [sending many requests](https://github.com/GoogleCloudPlatform/bigdata-interop/pull/152) to Cloud Storage. As a result, Dataflow jobs can fail with HTTP 429 errors from Cloud Storage.
    * Apache Beam ParquetIO [fails when reading files](https://github.com/GoogleCloudPlatform/bigdata-interop/commit/8f6443bfd6ee821c5667dd2811cf3fe03167b755) from Cloud Storage.
To work around these issues, either upgrade to SDK 2.11.0, or override the gcsio client library version to 1.9.16 or later.
  * The Dataflow runner has an incorrect logging configuration that might cause all logs to be missing. To work around this issue, add `slf4j-jdk14` to your runtime dependencies.

  
2.9.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated as of December 13, 2019. **Known issues:**

  * If you enable the [Streaming Engine (Beta) experiment](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#dataflow-streaming-engine), don't upgrade to SDK 2.9.0 due to a known issue. If you choose to use SDK 2.9.0, you must also set the `enable_conscrypt_security_provider` experimental flag to enable Conscrypt, which has known stability issues.
  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.8.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated as of October 25, 2019. **Known issues:**

  * Pipelines might become stuck due to an issue with the Conscrypt library. If you see errors in Stackdriver Logging with stack traces that include Conscrypt related calls, you might be affected by this issue. To resolve the issue, upgrade to SDK 2.9.0 or higher.
  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.7.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated as of October 3, 2019. **Known issues:**

  * Pipelines might become stuck due to an issue with the Conscrypt library. If you see errors in Stackdriver Logging with stack traces that include Conscrypt related calls, you might be affected by this issue. To resolve the issue, upgrade to SDK 2.9.0 or higher.
  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.6.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated as of August 8, 2019. **Known issues:**

  * Pipelines might become stuck due to an issue with the Conscrypt library. If you see errors in Stackdriver Logging with stack traces that include Conscrypt related calls, you might be affected by this issue. To resolve the issue, upgrade to SDK 2.9.0 or higher.
  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.5.0 | Deprecated |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
org.apache.beam:beam-sdks-java-io-kafka  
|  Deprecated as of June 6, 2019. **Known issues:**

  * Pipelines might become stuck due to an issue with the Conscrypt library. If you see errors in Stackdriver Logging with stack traces that include Conscrypt related calls, you might be affected by this issue. To resolve the issue, upgrade to SDK 2.9.0 or higher.
  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.4.0 | Decommissioned |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
|  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.3.0 | Decommissioned |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
|  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.2.0 | Decommissioned |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
|  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.1.0 | Decommissioned |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
|  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.0.0 | Decommissioned |  org.apache.beam:beam-sdks-java-core  
org.apache.beam:beam-sdks-java-io-google-cloud-platform  
org.apache.beam:beam-sdks-java-extensions-google-cloud-platform-core  
org.apache.beam:beam-sdks-java-extensions-protobuf  
org.apache.beam:beam-runners-direct-java  
org.apache.beam:beam-runners-google-cloud-dataflow-java  
org.apache.beam:beam-model-pipeline  
org.apache.beam:beam-runners-core-construction-java  
org.apache.beam:beam-model-job-management  
|  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Apache Beam Java SDKs 2.9.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
  
### Python

SDK version | Status | Supported components | Details  
---|---|---|---  
2.77.0 | Supported |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on October 7, 2027.  
2.76.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on August 31, 2027.  
2.75.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on July 8, 2027.  
2.74.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on June 2, 2027.  
2.73.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on April 29, 2027.  
2.72.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on March 30, 2027.  
2.71.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on January 22, 2027.  
2.70.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on December 16, 2026.  
2.69.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on October 28, 2026.  
2.68.0 | Deprecated |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on September 22, 2026.  
2.67.0 | Supported |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  This version will be deprecated on August 12, 2026.  
2.66.0 | Deprecated |  **Warning:** For Bigtable pipelines, use [cross-language transforms](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) with the Bigtable connector instead of `apache_beam.io.gcp.bigtableio`. Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on October 1, 2026.  
2.65.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on May 12, 2026.  
2.64.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on March 31, 2026.  
2.63.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on February 18, 2026.  
2.62.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on January 21, 2026.  
2.61.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on November 25, 2025.  
2.60.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on October 17, 2025.  
2.59.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on September 11, 2025.  
2.58.1 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on August 16, 2025. **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.58.0 | Deprecated |  **Warning:** When you use `io.kafka.ReadFromKafka`, offsets aren't committed when you configure them with `commit_offset_in_finalize`. See the [Apache Beam GitHub issue #32196](https://github.com/apache/beam/issues/32196). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on August 6, 2025. **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.57.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on June 26, 2025. **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.56.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on May 1, 2025. **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.55.1 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on April 8, 2025. **Known issue:** Python pipelines that use this SDK might experience occasional stuckness. For more information, see the [Apache Beam GitHub issue #30867](https://github.com/apache/beam/issues/30867). **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.55.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on March 25, 2025. **Known issue:** The `WriteToJson` transform in cross-language pipelines fails with an error. To resolve this issue, upgrade to Apache Beam 2.55.1. For more information, see [Issue #30776: Beam YAML `WriteToJson` fails](https://github.com/apache/beam/issues/30776). **Known issue:** Python pipelines that use this SDK might experience occasional stuckness. For more information, see the [Apache Beam GitHub issue #30867](https://github.com/apache/beam/issues/30867). **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.54.0 | Deprecated |  **Warning:** Pipelines that have large materialized side inputs might experience a performance regression on Apache Beam Python SDK versions 2.52.0 to 2.54.0. For more information and a workaround, see the [Apache Beam GitHub issue #30360](https://github.com/apache/beam/issues/30360). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql, yaml  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on February 14, 2025. **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.53.0 | Deprecated |  **Warning:** Pipelines that have large materialized side inputs might experience a performance regression on Apache Beam Python SDK versions 2.52.0 to 2.54.0. For more information and a workaround, see the [Apache Beam GitHub issue #30360](https://github.com/apache/beam/issues/30360). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on January 4, 2025. **Known issue:** Pipelines that read data from Cloud Storage by using GcsIO, either directly or indirectly, such as with BigQueryIO, might experience data corruption on the Apache Beam Python SDK versions 2.53.0 to 2.58.1. For more information, see the [Apache Beam GitHub issue #32169](https://github.com/apache/beam/issues/32169).  
2.52.0 | Deprecated |  **Warning:** Pipelines that have large materialized side inputs might experience a performance regression on Apache Beam Python SDK versions 2.52.0 to 2.54.0. For more information and a workaround, see the [Apache Beam GitHub issue #30360](https://github.com/apache/beam/issues/30360). **Warning:** Python streaming pipelines that use this SDK version might experience occasional crashes or get stuck. For more information, see the [Apache Beam GitHub issue #27330](https://github.com/apache/beam/issues/27330). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on November 17, 2024.  
2.51.0 | Deprecated |  **Warning:** If your pipeline uses the BigQuery Storage Read API, pin Fast Avro for Python (fastavro) to version 1.8.3 or earlier. For more information, see the [Apache Beam GitHub issue #28811](https://github.com/apache/beam/issues/28811). **Warning:** Long-running pipelines that use the Apache Beam Python SDK versions 2.47.0 to 2.51.0 might experience a memory leak or get stuck. For more information, see the [Apache Beam GitHub issue #28246](https://github.com/apache/beam/issues/28246). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on October 12, 2024.  
2.50.0 | Deprecated |  **Warning:** If your pipeline uses the BigQuery Storage Read API, pin Fast Avro for Python (fastavro) to version 1.8.3 or earlier. For more information, see the [Apache Beam GitHub issue #28811](https://github.com/apache/beam/issues/28811). **Warning:** When writing to Bigtable using Apache Beam's multi-language feature, we recommend that you don't use versions 2.49.0 and 2.50.0 due to an issue with Apache Beam defaulting record timestamps to Unix epoch time when timestamps are not explicitly set. This might result in cells being overwritten and might also result in deleted records if your table has an age-based garbage collection policy. For more information, see the [Apache Beam GitHub issue #28632](https://github.com/apache/beam/issues/28632). **Warning:** Long-running pipelines that use the Apache Beam Python SDK versions 2.47.0 to 2.51.0 might experience a memory leak or get stuck. For more information, see the [Apache Beam GitHub issue #28246](https://github.com/apache/beam/issues/28246). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on August 30, 2024.  
2.49.0 | Deprecated |  **Warning:** If your pipeline uses the BigQuery Storage Read API, pin Fast Avro for Python (fastavro) to version 1.8.3 or earlier. For more information, see the [Apache Beam GitHub issue #28811](https://github.com/apache/beam/issues/28811). **Warning:** When writing to Bigtable using Apache Beam's multi-language feature, we recommend that you don't use versions 2.49.0 and 2.50.0 due to an issue with Apache Beam defaulting record timestamps to Unix epoch time when timestamps are not explicitly set. This might result in cells being overwritten and might also result in deleted records if your table has an age-based garbage collection policy. For more information, see the [Apache Beam GitHub issue #28632](https://github.com/apache/beam/issues/28632). **Warning:** Long-running pipelines that use the Apache Beam Python SDK versions 2.47.0 to 2.51.0 might experience a memory leak or get stuck. For more information, see the [Apache Beam GitHub issue #28246](https://github.com/apache/beam/issues/28246). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on July 17, 2024.  
2.48.0 | Deprecated |  **Warning:** Long-running pipelines that use the Apache Beam Python SDK versions 2.47.0 to 2.51.0 might experience a memory leak or get stuck. For more information, see the [Apache Beam GitHub issue #28246](https://github.com/apache/beam/issues/28246). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on May 31, 2024.  
2.47.0 | Deprecated |  **Warning:** Long-running pipelines that use the Apache Beam Python SDK versions 2.47.0 to 2.51.0 might experience a memory leak or get stuck. For more information, see the [Apache Beam GitHub issue #28246](https://github.com/apache/beam/issues/28246). Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on May 10, 2024.  
2.46.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on March 10, 2025.  
2.45.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on February 15, 2024.  
2.44.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on January 13, 2024.  
2.43.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on November 17, 2023.  
2.42.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on October 17, 2023.  
2.41.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on August 23, 2023.  
2.40.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, ml.inference (excluding PytorchModelHandlerKeyedTensor and SklearnModelHandlerPandas), options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on June 27, 2023.  
2.39.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on May 25, 2023.  
2.38.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on April 20, 2023.  
2.37.0 | Deprecated |  **Warning:** If your pipeline reads from Cloud Storage, do NOT use 2.32.0 – 2.37.0. Immediately upgrade to 2.38.0 or later. **Warning:** If your pipeline reads from Datastore, do NOT use 2.34.0 – 2.37.0. Immediately upgrade to 2.38.0 or later.  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on March 4, 2023. **Known issues:**

  * When you use `WriteToBigQuery` with the `ignore_unknown_columns` parameter set to `true`, the parameter value is ignored. This issue is fixed in version 2.38.0. See [BEAM-14039](https://issues.apache.org/jira/browse/BEAM-14039) for details.

  
2.36.0 | Deprecated |  **Warning:** If your pipeline reads from Cloud Storage, do NOT use 2.32.0 – 2.37.0. Immediately upgrade to 2.38.0 or later. **Warning:** If your pipeline reads from Datastore, do NOT use 2.34.0 – 2.37.0. Immediately upgrade to 2.38.0 or later.  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.   
|  Deprecated on February 7, 2023. **Known issues:**

  * When you use `WriteToBigQuery` with the `ignore_unknown_columns` parameter set to `true`, the parameter value is ignored. This issue is fixed in version 2.38.0. See [BEAM-14039](https://issues.apache.org/jira/browse/BEAM-14039) for details.

  
2.35.0 | Deprecated |  **Warning:** If your pipeline reads from Cloud Storage, do NOT use 2.32.0 – 2.37.0. Immediately upgrade to 2.38.0 or later. **Warning:** If your pipeline reads from Datastore, do NOT use 2.34.0 – 2.37.0. Immediately upgrade to 2.38.0 or later.  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
The connectors under apache_beam.io.jdbc: ReadFromJdbc, WriteToJdbc.  
|  Deprecated on December 29, 2022.  
2.34.0 | Deprecated |  **Warning:** If your pipeline reads from Cloud Storage, do NOT use 2.32.0 – 2.37.0. Immediately upgrade to 2.38.0 or later. **Warning:** If your pipeline reads from Datastore, do NOT use 2.34.0 – 2.37.0. Immediately upgrade to 2.38.0 or later.  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints, sql  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on November 11, 2022.  
2.33.0 | Deprecated |  **Warning:** If your pipeline reads from Cloud Storage, do NOT use 2.32.0 – 2.37.0. Immediately upgrade to 2.38.0 or later.  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on October 7, 2022.  
2.32.0 | Deprecated |  **Warning:** If your pipeline reads from Cloud Storage, do NOT use 2.32.0 – 2.37.0. Immediately upgrade to 2.38.0 or later.  Core Python SDK library under module apache_beam: submodules coders, dataframe, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on August 25, 2022.  
2.31.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe (preview), metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem, filesystems, fileio  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on July 8, 2022.  
2.30.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe (preview), metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on June 10, 2022.  
2.29.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe (preview), metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on April 29, 2022.  
2.28.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe (preview), metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on February 22, 2022.  
2.27.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe (preview), metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on January 7, 2022.  
2.26.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, dataframe (preview), metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on December 11, 2021.  
2.25.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on October 23, 2021.  
2.24.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on September 18, 2021. Also, the Apache Beam SDK 2.24.0 version is the last to support Python 2 and Python 3.5. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.23.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on July 29, 2021. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.22.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp: bigquery, datastore, pubsub  
|  Deprecated on June 8, 2021. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.21.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
|  Deprecated on May 27, 2021. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.20.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
|  Deprecated on April 15, 2021. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.19.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
|  Deprecated on February 4, 2021. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.18.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
|  Deprecated on January 23, 2021. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.17.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
|  Deprecated on January 6, 2021. Dataflow no longer supports pipelines using Python 2. Read more information on the [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#dataflow) page.  
2.16.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
| Deprecated on October 7, 2020.   
2.15.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
| Deprecated on August 23, 2020.   
2.14.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
|  Deprecated on August 1, 2020. **Known issues:**

  * The MongoDB source added in this release has a known issue that can result in data loss. See [BEAM-7866](https://issues.apache.org/jira/browse/BEAM-7866) for details.

  
2.13.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
| Deprecated as of June 6, 2020.   
2.12.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
| Deprecated as of April 25, 2020.   
2.11.0 | Deprecated |  Core Python SDK library under module apache_beam: submodules coders, metrics, options, portability, runners.dataflow, runners.direct, transforms, typehints  
File-based sources and sinks and related modules under module apache_beam.io: textio, avroio, parquetio, tfrecordio, gcsfilesystem, localfilesystem  
Google Cloud I/O connectors under module apache_beam.io.gcp  
| Deprecated as of March 1, 2020.  
2.10.0 | Deprecated |  | Deprecated as of February 11, 2020.   
2.9.0 | Deprecated |  | Deprecated as of December 13, 2019.   
2.8.0 | Deprecated |  | Deprecated as of October 25, 2019.   
2.7.0 | Deprecated |  |  Deprecated as of October 3, 2019.  
2.6.0 | Deprecated |  | Deprecated as of August 8, 2019.   
2.5.0 | Deprecated |  | Deprecated as of June 6, 2019.   
2.4.0 | Deprecated |  |  Deprecated as of March 20, 2019.   
2.3.0 | Deprecated |  |  Deprecated as of January 30, 2019.  
  
2.2.0 | Deprecated |  |  Deprecated as of December 2, 2018.  
  
2.1.1  
2.1.0 | Deprecated |  |  Deprecated as of August 23, 2018.  
  
2.0.0 | Deprecated |  |  Deprecated as of May 17, 2018.  
  
  
### Go

SDK version | Status | Supported components | Details  
---|---|---|---  
2.77.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on October 7, 2027.  
2.76.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on August 31, 2027.  
2.75.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on July 8, 2027.  
2.74.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on June 2, 2027.  
2.73.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on April 29, 2027.  
2.72.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on March 30, 2027.  
2.71.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on January 22, 2027.  
2.70.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on December 16, 2026.  
2.69.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on October 28, 2026.  
2.68.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on September 22, 2026.  
2.67.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on August 12, 2026.  
2.66.0 | Supported |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| This version will be deprecated on July 1, 2026.  
2.65.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on May 12, 2026.  
2.64.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on March 31, 2026.  
2.63.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on February 18, 2026.  
2.62.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on January 21, 2026.  
2.61.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on November 25, 2025.  
2.60.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on October 17, 2025.  
2.59.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on September 11, 2025.  
2.58.1 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on August 16, 2025.  
2.58.0 | Deprecated |  **Warning:** When you use `io.xlang.kafkaio.Read`, offsets aren't committed when you configure them with `CommitOffsetInFinalize`. See the [Apache Beam GitHub issue #32196](https://github.com/apache/beam/issues/32196). Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on August 6, 2025.  
2.57.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on June 26, 2025.  
2.56.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on May 1, 2025.  
2.55.1 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on April 8, 2025.  
2.55.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on March 25, 2025.  
2.54.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on February 14, 2025.  
2.53.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on January 4, 2025.  
2.52.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on November 17, 2024.  
2.51.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on October 12, 2024.  
2.50.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on August 30, 2024.  
2.49.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on July 17, 2024.  
2.48.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on May 31, 2024.  
2.47.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on May 10, 2024.  
2.46.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on March 10, 2024.  
2.45.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on February 15, 2024.  
2.44.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on January 13, 2024.  
2.43.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on November 17, 2023.  
2.42.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on October 17, 2023.  
2.41.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on August 23, 2023.  
2.40.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on June 27, 2023.  
2.39.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on May 25, 2023.  
2.38.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/pubsubio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on April 20, 2023.  
2.37.0 | Deprecated |  Packages under the following directories:  
\- [Core Beam Go SDK package](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/core)  
\- [beam/transforms](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/transforms)  
\- [beam/io/textio](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
\- [beam/io/xlang](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang)  
| Deprecated on March 4, 2023.  
  
## Dataflow 2.x SDKs

**Dataflow SDK Deprecation Notice:** The Dataflow SDK 2.5.0 is the last Dataflow SDK release that is separate from the Apache Beam SDK releases. The Dataflow service supports official Apache Beam SDK releases as documented in the [SDK version support status page](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status). 

**Note:** Development SDK versions (marked as `-SNAPSHOT` for Java and `.dev` for Python) are unsupported.

The following tables contain the support status for the Dataflow 2.x SDKs, including the Dataflow Java SDK and the Dataflow Python SDK: 

### Java

See the [Dataflow SDK 2.x for Java release notes](https://docs.cloud.google.com/dataflow/release-notes/release-notes-java-2) for change information.

SDK version | Status | Details  
---|---|---  
2.5.0 | Deprecated |  Deprecated as of June 6, 2019. **Known issue:**

  * In a specific case, users of Dataflow Java SDKs 2.5.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.4.0 | Decommissioned |  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Dataflow Java SDKs 2.5.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.3.0 | Decommissioned |  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Dataflow Java SDKs 2.5.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.2.0 | Decommissioned |  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Dataflow Java SDKs 2.5.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.1.0 | Decommissioned |  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Dataflow Java SDKs 2.5.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.0.0 | Decommissioned |  Decommissioned as of Aug 12, 2020. This version is decommissioned due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). **Known issue:**

  * In a specific case, users of Dataflow Java SDKs 2.5.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
2.0.0-beta3  
2.0.0-beta2  
2.0.0-beta1  
| Decommissioned |  Decommissioned as of February 28, 2018. **Known issue:**

  * In a specific case, users of Dataflow Java SDKs 2.5.0 and earlier might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true: 
    * You're reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.
    * The file size (decompressed) is larger than 2.14 GB.
    * The input stream runs into an error (and is recreated) after 2.14 GB is read.
As a workaround, don't set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and filename with the [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  
  
### Python

See the [Dataflow SDK 2.x for Python release notes](https://docs.cloud.google.com/dataflow/release-notes/release-notes-python) for change information.

SDK version | Status | Details  
---|---|---  
2.5.0 | Deprecated | Deprecated as of June 6, 2019.  
2.4.0 | Deprecated |  Deprecated as of March 20, 2019.  
  
2.3.0 | Deprecated |  Deprecated as of January 30, 2019.  
  
2.2.0 | Deprecated |  Deprecated as of December 2, 2018.  
  
2.1.1 | Deprecated |  Deprecated as of August 23, 2018.  
Fixes a compatibility issue with the Python `six` package.  
See the [release notes](https://docs.cloud.google.com/dataflow/release-notes/release-notes-python#211_september_22_2017) for more information.   
2.1.0 | Deprecated |  Deprecated as of August 23, 2018.  
This release has a compatibility issue with the Python `six` 1.11.0 package.  
See the [Release Notes](https://docs.cloud.google.com/dataflow/release-notes/release-notes-python#210_september_1_2017) for more information.   
2.0.0 | Deprecated |  Deprecated as of May 17, 2018.  
This release has a compatibility issue with the Python `six` 1.11.0 package.  
See the [Release Notes](https://docs.cloud.google.com/dataflow/release-notes/release-notes-python#200_may_31_2017) for more information.   
0.6.0  
0.5.5  
0.5.1  
0.4.4  
0.4.3  
0.4.2  
0.4.1  
0.4.0  
| Decommissioned | Decommissioned as of January 29, 2018.  
0.2.7 and earlier versions | Decommissioned |  Decommissioned as of March 23, 2017.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
