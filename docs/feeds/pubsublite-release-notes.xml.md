---
url: https://docs.cloud.google.com/feeds/pubsublite-release-notes.xml
title: Pub/Sub Lite - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:23:06.786827+00:00
---

# Pub/Sub Lite - Release notes

> Source: https://docs.cloud.google.com/feeds/pubsublite-release-notes.xml

tag:google.com,2016:pubsublite-release-notesPub/Sub Lite - Release notesGoogle Cloud Platform2026-06-09T00:00:00-07:00June 09, 2026tag:google.com,2016:pubsublite-release-notes#June_09_20262026-06-09T00:00:00-07:00Announcement 

The [Pub/Sub Lite to Managed Service for Apache Kafka migration guide](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) has been updated to use the latest client libraries and to use [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview) in Managed Service for Apache Kafka.

]]> June 17, 2024tag:google.com,2016:pubsublite-release-notes#June_17_20242024-06-17T00:00:00-07:00Deprecated 

Pub/Sub Lite is deprecated. Effective March 18, 2026, Pub/Sub Lite will be turned down.

  * Current customers: Pub/Sub Lite remains functional until March 18, 2026. If you have not used Pub/Sub Lite within the 90-day period preceding September 24, 2024 (June 26, 2024 - September 24, 2024), you won't be able to access Pub/Sub Lite starting on September 24, 2024.

  * New customers: Pub/Sub Lite is no longer available for new customers after September 24th, 2024




You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-apache-kaftka-for-bigquery) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

]]> January 23, 2023tag:google.com,2016:pubsublite-release-notes#January_23_20232023-01-23T00:00:00-08:00Feature 

You can now migrate your producers from Apache Kafka to Pub/Sub Lite with only configuration changes. To check the feasibility of the migration and to perform the migration workflow, refer to the [Kafka to Pub/Sub Lite migration guide](https://cloud.google.com/pubsub/lite/docs/kafka-migration). This feature is in public preview.

]]> December 19, 2022tag:google.com,2016:pubsublite-release-notes#December_19_20222022-12-19T00:00:00-08:00Feature 

Pub/Sub Lite now supports [export subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub). You can use an export subscription to export Pub/Sub Lite messages to a destination Pub/Sub topic. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

]]> November 18, 2022tag:google.com,2016:pubsublite-release-notes#November_18_20222022-11-18T00:00:00-08:00Feature 

The [Kafka Connector library](https://github.com/googleapis/java-pubsub-group-kafka-connector) for Pub/Sub and Pub/Sub Lite is now generally available.

]]> September 29, 2022tag:google.com,2016:pubsublite-release-notes#September_29_20222022-09-29T00:00:00-07:00Feature 

The [Kafka Connector library](https://github.com/googleapis/java-pubsub-group-kafka-connector) for Pub/Sub and Pub/Sub Lite is now in preview.

]]> September 13, 2022tag:google.com,2016:pubsublite-release-notes#September_13_20222022-09-13T00:00:00-07:00Feature 

Pub/Sub Lite is now available in Tel Aviv (`me-west1`).

]]> May 25, 2022tag:google.com,2016:pubsublite-release-notes#May_25_20222022-05-25T00:00:00-07:00Feature 

The [Kafka Shim Java client library](https://github.com/googleapis/java-pubsublite-kafka) for Pub/Sub Lite is now GA.

]]> February 03, 2022tag:google.com,2016:pubsublite-release-notes#February_03_20222022-02-03T00:00:00-08:00Feature 

Pub/Sub Lite now supports regional Lite topics that [replicate data to a secondary zone](https://docs.cloud.google.com/pubsub/lite/docs/topics#data_replication_in_a_lite_topic).

]]> September 24, 2021tag:google.com,2016:pubsublite-release-notes#September_24_20212021-09-24T00:00:00-07:00Feature 

Pub/Sub Lite reservations allow you to reserve and share throughput capacity among multiple topics in a region.

  * For more information, see [Creating and managing Lite reservations](https://docs.cloud.google.com/pubsub/lite/docs/reservations).

]]> July 19, 2021tag:google.com,2016:pubsublite-release-notes#July_19_20212021-07-19T00:00:00-07:00Feature 

The [Pub/Sub Lite Python client library](https://github.com/googleapis/python-pubsublite) is now GA.

]]> July 08, 2021tag:google.com,2016:pubsublite-release-notes#July_08_20212021-07-08T00:00:00-07:00Feature 

The [Pub/Sub Lite Go client library](https://pkg.go.dev/cloud.google.com/go/pubsublite) is now GA.

]]> May 04, 2021tag:google.com,2016:pubsublite-release-notes#May_04_20212021-05-04T00:00:00-07:00Feature 

Pub/Sub Lite is now available in the following regions:

  * Hong Kong (`asia-east2`)
  * Tokyo (`asia-northeast1`)
  * Osaka (`asia-northeast2`)
  * Seoul (`asia-northeast3`)
  * Mumbai (`asia-south1`)
  * Jakarta (`asia-southeast2`)
  * Warsaw (`europe-central2`)
  * Montreal (`northamerica-northeast1`)
  * Sao Paulo (`southamerica-east1`)
  * Northern Virginia (`us-east4`)
  * Salt Lake City (`us-west3`)
  * Las Vegas (`us-west4`)



For the full list of available regions, see [Pub/Sub Lite locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).

]]> March 22, 2021tag:google.com,2016:pubsublite-release-notes#March_22_20212021-03-22T00:00:00-07:00Feature 

Pub/Sub Lite now supports [increasing the number of partitions in a topic](https://docs.cloud.google.com/pubsub/lite/docs/topics#scaling_throughput_capacity).

]]> February 24, 2021tag:google.com,2016:pubsublite-release-notes#February_24_20212021-02-24T00:00:00-08:00Feature 

An [Apache Spark connector](https://github.com/googleapis/java-pubsublite-spark) is now available for Pub/Sub Lite, allowing you to read messages from Pub/Sub Lite in your Spark clusters.

]]> November 19, 2020tag:google.com,2016:pubsublite-release-notes#November_19_20202020-11-19T00:00:00-08:00Feature 

The Pub/Sub Lite [Python client library](https://github.com/googleapis/python-pubsublite) is now in Beta.

]]> October 30, 2020tag:google.com,2016:pubsublite-release-notes#October_30_20202020-10-30T00:00:00-07:00Feature 

A [Kafka Shim Java client library](https://github.com/googleapis/java-pubsublite-kafka) is now available for Pub/Sub Lite, allowing you to use the Kafka API with Pub/Sub Lite as a backend.

]]> October 09, 2020tag:google.com,2016:pubsublite-release-notes#October_09_20202020-10-09T00:00:00-07:00Feature 

[Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) is now available in GA.

]]> May 26, 2020tag:google.com,2016:pubsublite-release-notes#May_26_20202020-05-26T00:00:00-07:00Feature 

[Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) is now available at the [beta launch stage](https://cloud.google.com/products/#product-launch-stages).

]]> May 18, 2020tag:google.com,2016:pubsublite-release-notes#May_18_20202020-05-18T00:00:00-07:00Feature 

The Pub/Sub Lite [Java client library](https://github.com/googleapis/java-pubsublite) is now in Beta.

]]>
