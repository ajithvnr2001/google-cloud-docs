---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/release-notes/
title: Google Cloud Managed Service for Apache Kafka release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:05:01.282211+00:00
---

# Google Cloud Managed Service for Apache Kafka release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/resources)



Send feedback 

#  Google Cloud Managed Service for Apache Kafka release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google Cloud Managed Service for Apache Kafka. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/managedkafka-release-notes.xml) directly. 

## October 14, 2026

Feature

Performance of the [Cloud Storage Sink connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-storage-connector) has been improved. The improvements include reduced out-of-memory errors, higher maximum throughput, and avoiding creating a large number of small files.

## October 12, 2026

Announcement

The Service Level Agreement (SLA) for Managed Service for Apache Kafka now covers the Produce API. For more information, see [Managed Service for Apache Kafka Service Level Agreement](https://cloud.google.com/terms/managed-service-for-apache-kafka/sla).

## October 09, 2026

Change

The format for bootstrap addresses and broker URLs has changed for new Managed Service for Apache Kafka clusters. To learn how to get a cluster's bootstrap address, see [View a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).

## September 10, 2026

Feature

You can configure a Managed Service for Apache Kafka cluster as a public cluster to let client applications connect over the public internet. For more information, see [Connect clients to a public cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka#connect-clients-to-a-public-cluster).

## August 27, 2026

Feature

You can now configure the disk capacity per broker when you create a Kafka cluster and increase it later. For more information, see [Configure broker disk size](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/brokers/configure-disk-size).

## July 31, 2026

Feature

You can generate synthetic data for a Managed Service for Apache Kafka cluster by using Dataflow. For more information, see [Generate synthetic data for a Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-synthetic-data).

## July 27, 2026

Feature

You can now create a Cloud SQL for PostgreSQL Source connector and a Generic PostgreSQL Source connector for Kafka Connect.

A Cloud SQL for PostgreSQL Source connector or Generic PostgreSQL Source connector is an instance of a [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html). It reads row-level changes from a PostgreSQL database and writes them to topics in a Managed Service for Apache Kafka cluster.

For more information, see [Create a Cloud SQL for PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector), [Create a Generic PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-generic-postgres-source-connector), and [Troubleshoot a PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-postgres-source-connector).

## July 07, 2026

Feature

Managed Service for Apache Kafka now supports topic compression with `zstd`.

## April 17, 2026

Feature

The [Managed Service for Apache Kafka remote MCP server](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/use-managed-service-for-apache-kafka-mcp) is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

## March 03, 2026

Feature

You can now use the [Managed Service for Apache Kafka remote MCP server](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/use-managed-service-for-apache-kafka-mcp) to enable LLM agents to create and manage your Kafka clusters and Kafka Connect clusters, as well as create and manage related resources such as topics, consumer groups, connectors, and ACLs.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## December 10, 2025

Feature

Using `gcloud` or the REST API, you can now view the following information about a Managed Service for Apache Kafka cluster:

  * Broker node IDs and indexes
  * The zones where brokers are located
  * The Kafka version that the cluster is running



For more information, see [View a Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster).

## December 08, 2025

Deprecated

The `additionalSubnets` field in the [`ConnectNetworkConfig`](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.connectClusters#connectnetworkconfig) REST API resource is deprecated. Connect cluster workers can reach any endpoint that is accessible from `primarySubnet` subnetwork.

Change

Kafka Connect cluster workers can now reach any endpoint that is accessible from the worker (primary) subnetwork. Previously, to extend worker connectivity to other subnets within the same VPC network, you had to specify these subnets in the cluster configuration. The `additionalSubnets` field is now ignored, and this configuration setting has been removed from the Google Cloud console. For more information, see [Worker (primary) subnet](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#worker-subnet).

## October 01, 2025

Feature

Support for Kafka Connect is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). Kafka Connect lets you stream data at scale between Managed Service for Apache Kafka clusters and other systems, such as external Kafka deployments, BigQuery, Cloud Storage, or Pub/Sub. For more information, see [Kafka Connect overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview).

## September 24, 2025

Feature

Integration with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_kafka) is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## September 17, 2025

Feature

Managed Service for Apache Kafka now supports [Organization Policy Service custom constraints](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/custom-constraints). Custom constraints allow you to restrict specific operations on Managed Service for Apache Kafka resources.

## September 09, 2025

Feature

General availability: You can now use mutual TLS (mTLS) for certificate-based authentication with your Managed Service for Apache Kafka brokers. This feature is available for clusters created after June 24, 2025. For more information, see [Authentication types for Kafka brokers](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka).

## September 04, 2025

Feature

Integration with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_kafka) is in [preview](https://cloud.google.com/products#product-launch-stages).

## September 02, 2025

Feature

Managed Service for Apache Kafka now supports [HIPAA Compliance on Google Cloud](https://docs.cloud.google.com/security/compliance/hipaa).

## July 15, 2025

Feature

The Google Cloud Managed Service for Apache Kafka service creates new brokers automatically based on the memory and vCPU configuration of the cluster. When you update a cluster's size, the service now performs a safety check to verify that individual brokers have sufficient capacity for their portion of the traffic. For more information, see [Update the memory and vCPUs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster#update-memory-vCPUs).

## July 09, 2025

Feature

General availability: Metrics for all Google Cloud Managed Service for Apache Kafka resources are now available, with some exceptions. Exceptions include the `request_count` and `topic_error_count` metrics for Kafka clusters and Kafka Connect connectors. For a list of supported metrics, see [Metrics for Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-managedkafka).

## May 29, 2025

Feature

Public preview: Google Managed Service for Apache Kafka now offers schema registry support. For more information about the feature, see the [schema registry overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview) or [get started with an Avro producer in Java](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-avro).

## May 06, 2025

Feature

General availability: Managed Service for Apache Kafka now supports configuring standard Apache Kafka ACLs using [REST](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.acls), [gRPC](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rpc/google.cloud.managedkafka.v1#acl), and [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls). For more information, see [Access control with IAM and Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control).

## March 31, 2025

Feature

Public preview: Google Cloud Managed Service for Apache Kafka now supports Kafka Connect. Kafka Connect provides a curated set of built-in connector plugins hosted in Connect clusters. Configure these connector plugins to create connectors that let you stream data at scale between Managed Service for Apache Kafka clusters and other systems, such as external Kafka deployments, BigQuery, Cloud Storage, or Pub/Sub. For more information, see [Kafka Connect overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview).

## December 19, 2024

Announcement

Documentation is now available to help you choose between Pub/Sub and Google Cloud Managed Service for Apache Kafka. The comparison is based on factors such as operational ease, portability, existing Kafka setup, and integration with other Google Cloud products. A detailed feature comparison table is also included. For more information, see [Choose Cloud Managed Service for Apache Kafka or Pub/Sub](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/choose-kafka-pubsub).

## December 13, 2024

Feature

Google Cloud Managed Service for Apache Kafka now supports moving open source Kafka data to Google Cloud using various Dataflow templates. You can move Kafka data to Cloud Managed Service for Apache Kafka, BigQuery, and Cloud Storage. For more information about these data movement use cases, see [Move Kafka data in Google Cloud](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/move-kafka-data).

## November 12, 2024

Announcement

Google Cloud Managed Service for Apache Kafka is now in General Availability (GA).

## October 02, 2024

Announcement

Google Cloud Managed Service for Apache Kafka clusters now run on Apache Kafka version 3.7.1.

## August 09, 2024

Change

Apache Kafka for BigQuery is now called Google Cloud Managed Service for Apache Kafka.

## July 24, 2024

Feature

Client library samples for Python are now added to all relevant pages. For more information, see [Apache Kafka for BigQuery client libraries](https://docs.cloud.google.com/managed-kafka/docs/reference/libraries).

## July 10, 2024

Feature

Terraform samples are now available for creating clusters and topics. For more information, see [Provision Apache Kafka for BigQuery resources with Terraform](https://docs.cloud.google.com/managed-kafka/docs/terraform).

## June 27, 2024

Feature

Client library samples for Java and Go are now added to all relevant pages. For more information, see [Apache Kafka for BigQuery client libraries](https://docs.cloud.google.com/managed-kafka/docs/reference/libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
