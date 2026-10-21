---
url: https://docs.cloud.google.com/pubsub/lite/docs/release-notes/
title: Pub/Sub Lite Release Notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:56:43.860943+00:00
---

# Pub/Sub Lite Release Notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Resources ](https://docs.cloud.google.com/pubsub/lite/docs/resources)



Send feedback 

#  Pub/Sub Lite Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains production updates and feature announcements for the Pub/Sub Lite service. For language-specific updates about Pub/Sub Lite [ Client Library](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries) releases, use the following links: [Go](https://github.com/googleapis/google-cloud-go/releases), [Java](https://github.com/googleapis/java-pubsublite/releases), and [Python](https://github.com/googleapis/python-pubsublite/releases). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/pubsublite-release-notes.xml) directly. 

## June 09, 2026

Announcement

The [Pub/Sub Lite to Managed Service for Apache Kafka migration guide](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) has been updated to use the latest client libraries and to use [Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview) in Managed Service for Apache Kafka.

## June 17, 2024

Deprecated

Pub/Sub Lite is deprecated. Effective March 18, 2026, Pub/Sub Lite will be turned down.

  * Current customers: Pub/Sub Lite remains functional until March 18, 2026. If you have not used Pub/Sub Lite within the 90-day period preceding September 24, 2024 (June 26, 2024 - September 24, 2024), you won't be able to access Pub/Sub Lite starting on September 24, 2024.

  * New customers: Pub/Sub Lite is no longer available for new customers after September 24th, 2024




You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-apache-kaftka-for-bigquery) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

## January 23, 2023

Feature

You can now migrate your producers from Apache Kafka to Pub/Sub Lite with only configuration changes. To check the feasibility of the migration and to perform the migration workflow, refer to the [Kafka to Pub/Sub Lite migration guide](https://cloud.google.com/pubsub/lite/docs/kafka-migration). This feature is in public preview.

## December 19, 2022

Feature

Pub/Sub Lite now supports [export subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub). You can use an export subscription to export Pub/Sub Lite messages to a destination Pub/Sub topic. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## November 18, 2022

Feature

The [Kafka Connector library](https://github.com/googleapis/java-pubsub-group-kafka-connector) for Pub/Sub and Pub/Sub Lite is now generally available.

## September 29, 2022

Feature

The [Kafka Connector library](https://github.com/googleapis/java-pubsub-group-kafka-connector) for Pub/Sub and Pub/Sub Lite is now in preview.

## September 13, 2022

Feature

Pub/Sub Lite is now available in Tel Aviv (`me-west1`).

## May 25, 2022

Feature

The [Kafka Shim Java client library](https://github.com/googleapis/java-pubsublite-kafka) for Pub/Sub Lite is now GA.

## February 03, 2022

Feature

Pub/Sub Lite now supports regional Lite topics that [replicate data to a secondary zone](https://docs.cloud.google.com/pubsub/lite/docs/topics#data_replication_in_a_lite_topic).

## September 24, 2021

Feature

Pub/Sub Lite reservations allow you to reserve and share throughput capacity among multiple topics in a region.

  * For more information, see [Creating and managing Lite reservations](https://docs.cloud.google.com/pubsub/lite/docs/reservations).



## July 19, 2021

Feature

The [Pub/Sub Lite Python client library](https://github.com/googleapis/python-pubsublite) is now GA.

## July 08, 2021

Feature

The [Pub/Sub Lite Go client library](https://pkg.go.dev/cloud.google.com/go/pubsublite) is now GA.

## May 04, 2021

Feature

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

## March 22, 2021

Feature

Pub/Sub Lite now supports [increasing the number of partitions in a topic](https://docs.cloud.google.com/pubsub/lite/docs/topics#scaling_throughput_capacity).

## February 24, 2021

Feature

An [Apache Spark connector](https://github.com/googleapis/java-pubsublite-spark) is now available for Pub/Sub Lite, allowing you to read messages from Pub/Sub Lite in your Spark clusters.

## November 19, 2020

Feature

The Pub/Sub Lite [Python client library](https://github.com/googleapis/python-pubsublite) is now in Beta.

## October 30, 2020

Feature

A [Kafka Shim Java client library](https://github.com/googleapis/java-pubsublite-kafka) is now available for Pub/Sub Lite, allowing you to use the Kafka API with Pub/Sub Lite as a backend.

## October 09, 2020

Feature

[Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) is now available in GA.

## May 26, 2020

Feature

[Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) is now available at the [beta launch stage](https://cloud.google.com/products/#product-launch-stages).

## May 18, 2020

Feature

The Pub/Sub Lite [Java client library](https://github.com/googleapis/java-pubsublite) is now in Beta.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
