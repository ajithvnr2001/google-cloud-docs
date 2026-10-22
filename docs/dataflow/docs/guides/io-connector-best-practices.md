---
url: https://docs.cloud.google.com/dataflow/docs/guides/io-connector-best-practices/
title: Apache Beam I/O connector best practices \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:18.632144+00:00
---

# Apache Beam I/O connector best practices  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/io-connector-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Apache Beam I/O connector best practices Stay organized with collections  Save and categorize content based on your preferences. 

Data processing in Dataflow can be highly parallelized. Much of this parallelism is handled automatically by Dataflow. I/O connectors sit at the boundary between your pipeline and other parts of your architecture, such as file storage, databases, and messaging systems. As such, I/O connectors often have specific considerations for achieving parallelism.

## General best practices

The following list describes general best practices for using I/O connectors in Dataflow.

  * Read the Javadoc, Pydoc, or Go documentation for the connectors in your pipeline. For more information, see [I/O connectors](https://beam.apache.org/documentation/io/connectors/) in the Apache Beam documentation.

  * Use the latest version of the Apache Beam SDK. I/O connectors are continually being improved, adding features and fixing known issues.

  * When developing a pipeline, it's important to balance the parallelism of the job. If a job has too little parallelism, it can be slow, and data can build up in the source. However, too much parallelism can overwhelm a sink with too many requests.

  * Don't rely on the ordering of elements. In general, Dataflow does not guarantee the order of elements in a collection.

  * If an I/O connector isn't available in your SDK of choice, consider using the [cross-language framework](https://beam.apache.org/documentation/programming-guide/#use-x-lang-transforms) to use an I/O connector from another SDK. In addition, connectors don't always have feature parity between SDKs. If a connector from another SDK provides a feature that you need, you can use it as a cross-language transform.

  * In general, writing custom I/O connectors is challenging. Use an existing connector whenever possible. If you need to implement a custom I/O connector, read [Developing a new I/O connector](https://beam.apache.org/documentation/io/developing-io-overview/).

  * If a pipeline fails, check for errors logged by I/O connectors. See [Troubleshoot Dataflow errors](https://docs.cloud.google.com/dataflow/docs/guides/common-errors).

  * When performing writes from Dataflow to a connector, consider using an [ErrorHandler](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/errorhandling/ErrorHandler.html) to handle any failed writes or malformed reads. This type of error handling is supported for the following Java I/Os in Apache Beam versions 2.55.0 and later: `BigQueryIO`, `BigtableIO`, `PubSubIO`, `KafkaIO`, `FileIO`, `TextIO`, and `AvroIO`.




For an example of performance benchmarks in a Dataflow streaming pipeline, see [Performance characteristics of Pub/Sub to BigQuery pipelines](https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-performance).

## Best practices for individual I/O connectors

The following topics list best practices for individual I/O connectors:

I/O connector| Read| Write  
---|---|---  
Apache Iceberg | [Read from Apache Iceberg](https://docs.cloud.google.com/dataflow/docs/guides/read-from-iceberg) | [Write to Apache Iceberg](https://docs.cloud.google.com/dataflow/docs/guides/write-to-iceberg)  
Apache Kafka | [Read from Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka) | [Write to Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/write-to-kafka)  
BigQuery | [Read from BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigquery) | [Write to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigquery)  
Bigtable | [Read from Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigtable) | [Write to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigtable)  
Cloud Storage | [Read from Cloud Storage](https://docs.cloud.google.com/dataflow/docs/guides/read-from-cloud-storage) | [Write to Cloud Storage](https://docs.cloud.google.com/dataflow/docs/guides/write-to-cloud-storage)  
Pub/Sub | [Read from Pub/Sub](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub) | [Write to Pub/Sub](https://docs.cloud.google.com/dataflow/docs/guides/write-to-pubsub)  
  
## Google-supported I/O connectors

The following table lists the Apache Beam I/O connectors supported by Dataflow. For a full list of Apache Beam I/O connectors, including those developed by the Apache Beam community and supported by other runners, see [I/O connectors](https://beam.apache.org/documentation/io/connectors/) in the Apache Beam documentation.

I/O connector name | Java | Python | Go  
---|---|---|---  
AvroIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/extensions/avro/io/AvroIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.avroio.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/avroio)  
BigQueryIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.bigquery.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/bigqueryio)  
BigTableIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/BigtableIO.html) | [Sink supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.bigtableio.html) | [Sink supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/bigtableio)  
DatastoreIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/datastore/DatastoreIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.datastore.v1new.datastoreio.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/datastoreio)  
FhirIO (healthcare) | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/healthcare/FhirIO.html) | Not available | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/fhirio)  
FileIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/FileIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.fileio.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/fileio)  
GcsFileSystem | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/extensions/gcp/storage/GcsFileSystemRegistrar.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.gcsfilesystem.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/filesystem/gcs)  
JdbcIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/jdbc/JdbcIO.html) | [Cross-language support](https://beam.apache.org/releases/pydoc/current/apache_beam.io.jdbc.html) | [Cross-language support](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang/jdbcio)  
KafkaIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/kafka/KafkaIO.html) | [Cross-language support](https://beam.apache.org/releases/pydoc/current/apache_beam.io.kafka.html) | [Cross-language support](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang/kafkaio)  
LocalFileSystem | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/LocalFileSystemRegistrar.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.localfilesystem.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/filesystem/local)  
ParquetIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/parquet/ParquetIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.parquetio.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/parquetio)  
PubSubIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/pubsubio)  
SpannerIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/spanner/SpannerIO.html) | [Cross-language support](https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.spanner.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/spannerio)  
TextIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/TextIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.textio.html) | [Supported](https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio)  
TFRecordIO | [Supported](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/TFRecordIO.html) | [Supported](https://beam.apache.org/releases/pydoc/current/apache_beam.io.tfrecordio.html) | Not available  
  
## What's next

  * Read the Apache Beam documentation for [I/O connectors](https://beam.apache.org/documentation/io/connectors/).
  * [Performance characteristics of Pub/Sub to BigQuery pipelines](https://docs.cloud.google.com/dataflow/docs/guides/pubsub-bigquery-performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
