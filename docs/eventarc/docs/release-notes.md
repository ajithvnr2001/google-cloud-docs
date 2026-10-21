---
url: https://docs.cloud.google.com/eventarc/docs/release-notes/
title: Eventarc Release Notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:41.368448+00:00
---

# Eventarc Release Notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Resources ](https://docs.cloud.google.com/eventarc/docs/resources)



Send feedback 

#  Eventarc Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

Advanced  Standard 

This page documents production updates to Eventarc. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/eventarc-release-notes.xml) directly. 

## September 30, 2026

Feature

Eventarc support for [creating triggers](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) for [direct events from Firebase Authentication](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#firebase-auth) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 10, 2026

Change

When configuring Eventarc triggers for Cloud Run destinations (including Cloud Run functions), you can specify a single delivery attempt with no retries. For more information, see [Retries for Cloud Run destinations](https://docs.cloud.google.com/eventarc/docs/retry-events#run-targets).

## April 22, 2026

Feature

Eventarc support for [creating triggers](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers) for [direct events from Gemini Cloud Assist](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#gemini-cloud-assist-preview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 02, 2026

Change

Eventarc Standard is available in the `asia-southeast3` (Bangkok, Thailand) [region](https://docs.cloud.google.com/eventarc/docs/locations#regions).

## November 11, 2025

Feature

Eventarc Advanced support for [using access policies to control access](https://docs.cloud.google.com/eventarc/advanced/docs/control-publishing-access) when publishing event messages to an Eventarc Advanced bus is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 24, 2025

Feature

Eventarc Advanced support for [publishing events from multiple projects](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources#multiple-projects) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 01, 2025

Change

There is a limit of one `MessageBus` resource per project per region, and a limit of one `GoogleApiSource` resource per project per region. For more information, see [Quotas and limits](https://docs.cloud.google.com/eventarc/docs/quotas).

Announcement

[Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/overview) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Change

Eventarc Advanced is available in the `asia-south1` (Mumbai, India), `europe-north1` (Hamina, Finland), and `us-east4` (Ashburn, Virginia, North America) [regions](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).

## May 15, 2025

Feature

Support for creating custom organization policy constraints in [Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/custom-constraints) and in [Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs/custom-constraints) is generally available for some Eventarc resources.

## April 11, 2025

Fixed

For applicable events, if a context attribute value size limit is exceeded, you are notified through a publishing error (Eventarc Advanced), or attribute names for truncated values are listed in an extension attribute (Eventarc Standard). For more information, see [Quotas and limits](https://docs.cloud.google.com/eventarc/docs/quotas).

## March 17, 2025

Change

Eventarc Standard is available in the `europe-north2` (Stockholm, Sweden) [region](https://docs.cloud.google.com/eventarc/docs/locations).

## January 29, 2025

Feature

To help ensure CMEK usage across an organization, [Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek#org-policy) and [Eventarc Standard](https://docs.cloud.google.com/eventarc/docs/use-cmek#org-policy) are integrated with two organization policy constraints.

## November 08, 2024

Change

Eventarc Standard is available in the `northamerica-south1` (Mexico, North America) [region](https://docs.cloud.google.com/eventarc/docs/locations).

## October 31, 2024

Feature

Eventarc is available in [Preview](https://cloud.google.com/products#product-launch-stages) in a new edition: [Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/overview) lets you receive, filter, transform, route, and deliver messages between different services, apps, and systems.

[Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs/overview) continues to deliver events from provider to destination by letting you define triggers that filter events.

## August 15, 2024

Feature

Eventarc support for [creating triggers](https://docs.cloud.google.com/eventarc/docs/event-providers-targets#triggers) for [direct events from Apigee API hub](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#apigee-api-hub) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## May 01, 2024

Feature

Eventarc support for [creating triggers](https://docs.cloud.google.com/eventarc/docs/targets#triggers) for [direct events from Cloud Speech-to-Text](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-speech-to-text) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 02, 2024

Feature

Eventarc support for [creating triggers](https://docs.cloud.google.com/eventarc/docs/targets#triggers) for [direct events from Cloud Deploy](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-deploy) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 19, 2024

Feature

Eventarc support for [creating triggers](https://docs.cloud.google.com/eventarc/docs/targets#triggers) for [direct events from Network Services](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#network-services) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 06, 2024

Feature

Eventarc support for [creating triggers](https://cloud.google.com/eventarc/docs/targets#triggers) for [direct events from Batch](https://cloud.google.com/eventarc/docs/reference/supported-events#batch) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## February 26, 2024

Change

Eventarc is available in the `us-west8` (Phoenix, Arizona, North America) [region](https://docs.cloud.google.com/eventarc/docs/locations).

## January 31, 2024

Change

Eventarc is available in the `africa-south1` (Johannesburg, South Africa) [region](https://docs.cloud.google.com/eventarc/docs/locations#africa).

## January 29, 2024

Feature

Eventarc support for [creating triggers](https://cloud.google.com/eventarc/docs/targets#triggers) for direct events from [Cloud Firestore](https://docs.cloud.google.com/eventarc/docs/event-types#cloud-firestore) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## January 25, 2024

Feature

Eventarc support for [creating triggers](https://cloud.google.com/eventarc/docs/targets#triggers) for direct events from [Cloud Firestore with authentication context](https://cloud.google.com/eventarc/docs/event-types#cloud-firestore-preview), is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 21, 2023

Change

Eventarc is available in the `europe-west10` (Berlin, Germany) [region](https://docs.cloud.google.com/eventarc/docs/locations#europe).

## December 13, 2023

Change

[Trigger updates](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-update) are applied to events generated _after_ the update. If the trigger is updated before a generated event is delivered, the event is routed according to the original filtering, and delivered within three days of the event generation.

## November 15, 2023

Change

Eventarc is available in the `me-central2` (Dammam, Kingdom of Saudi Arabia) [region](https://docs.cloud.google.com/eventarc/docs/locations#middle_east).

## October 20, 2023

Feature

Eventarc support for internal HTTP endpoints as event destinations is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see the [guide](https://docs.cloud.google.com/eventarc/docs/vpc-endpoints/route-vpc-internal-endpoint-events) and the [tutorial](https://docs.cloud.google.com/eventarc/docs/vpc-endpoints/receive-vpc-events).

## August 31, 2023

Feature

Eventarc support for [creating triggers](https://cloud.google.com/eventarc/docs/targets) for direct events from the following [sources](https://cloud.google.com/eventarc/docs/reference/supported-events) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)): 

  * AlloyDB for PostgreSQL
  * API Gateway
  * Apigee Registry
  * Backup for GKE
  * BeyondCorp
  * Certificate Manager
  * Cloud Data Fusion
  * Cloud Dataplex
  * Cloud Functions
  * Cloud Memorystore for Memcached
  * Database Migration
  * Dataflow
  * Dataproc Metastore
  * Datastream
  * Firebase Alerts
  * Firebase Remote Config
  * Firebase Test Lab
  * GKE Hub
  * Google Cloud Memorystore for Redis
  * Network Connectivity
  * Network Management
  * Transcoder
  * User-managed notebooks (Notebooks)
  * Vision AI
  * VM Migration
  * Workflows



## August 16, 2023

Deprecated

Eventarc support for direct events from Cloud IoT is retired from August 16, 2023.

## June 23, 2023

Feature

Eventarc support for [creating triggers](https://cloud.google.com/eventarc/docs/targets) for direct events from the following [sources](https://cloud.google.com/eventarc/docs/reference/supported-events) is available in [Preview](https://cloud.google.com/products#product-launch-stages): 

  * AlloyDB for PostgreSQL
  * Backup for GKE
  * Cloud Dataplex
  * Dataproc Metastore
  * GKE Hub
  * Google Cloud Memorystore for Redis
  * Network Connectivity
  * Network Management
  * User-managed notebooks (Notebooks)
  * Vision AI
  * VM Migration



## June 02, 2023

Feature

Eventarc support for [creating triggers](https://cloud.google.com/eventarc/docs/targets) for [direct Transcoder API events](https://cloud.google.com/eventarc/docs/event-types#transcoder-preview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 10, 2023

Change

Eventarc is available in the `europe-west12` (Turin, Italy) and `me-central1` (Doha, Qatar) [regions](https://docs.cloud.google.com/eventarc/docs/locations).

## April 17, 2023

Feature

Support for [creating triggers](https://docs.cloud.google.com/eventarc/docs/targets#triggers) for direct events from [Cloud Firestore](https://docs.cloud.google.com/eventarc/docs/event-types#cloud-firestore-preview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 03, 2023

Feature

Support for specifying the encoding of the event payload data as either `application/json` or `application/protobuf` through an [`eventDataContentType` field](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers#resource:-trigger) is available.

## March 28, 2023

Feature

Eventarc support for [creating triggers](https://docs.cloud.google.com/eventarc/docs/targets) for direct events from [Cloud Dataflow](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#cloud-dataflow-preview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 21, 2023

Feature

Support for triggering a workflow within a [service perimeter using VPC Service Controls](https://docs.cloud.google.com/eventarc/docs/using-vpc-service-controls) is generally available ([GA](https://cloud.google.com/products#section-23)).

## February 13, 2023

Change

Eventarc is available in the `me-west1` (Tel Aviv, Israel) [region](https://docs.cloud.google.com/eventarc/docs/locations#middle_east).

## February 09, 2023

Change

You can filter and search for instructions to create an Eventarc trigger based on the [event provider, event destination, and event type](https://docs.cloud.google.com/eventarc/docs/event-providers-targets).

## December 15, 2022

Feature

Eventarc support for [creating triggers](https://cloud.google.com/eventarc/docs/targets) for direct events from the following [sources](https://cloud.google.com/eventarc/docs/reference/supported-events) is available in [Preview](https://cloud.google.com/products#product-launch-stages): 

  * API Gateway
  * Apigee Registry
  * BeyondCorp
  * Certificate Manager
  * Cloud Data Fusion
  * Cloud Functions
  * Cloud Memorystore for Memcached
  * Database Migration
  * Datastream
  * Eventarc
  * Workflows



## December 02, 2022

Feature

Eventarc support for [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## October 17, 2022

Feature

[Eventarc triggers for Workflows](https://docs.cloud.google.com/eventarc/docs/workflows/create-triggers) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 14, 2022

Feature

Eventarc support for direct events from [Cloud IoT](https://docs.cloud.google.com/eventarc/docs/targets) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 02, 2022

Feature

Support for the delivery of [third-party events](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview) from third-party SaaS providers to interested subscribers is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 25, 2022

Change

Eventarc is available in the following [regions](https://docs.cloud.google.com/eventarc/docs/locations#americas):

  * `us-east5` (Columbus, Ohio, North America)
  * `us-south1` (Dallas, Texas, North America)



## July 14, 2022

Feature

Eventarc support for [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek) using the Cloud Console is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 30, 2022

Feature

Eventarc support for [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/eventarc/docs/use-cmek) using the Google Cloud CLI is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 28, 2022

Change

Eventarc is available in this [region](https://docs.cloud.google.com/eventarc/docs/locations): `europe-southwest1` (Madrid, Spain).

## June 27, 2022

Feature

Support for [Firebase Realtime Database](https://docs.cloud.google.com/eventarc/docs/targets) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 30, 2022

Feature

A [dedicated user interface](https://docs.cloud.google.com/eventarc/docs/create-trigger-console) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## May 16, 2022

Change

Eventarc is available in the following [regions](https://docs.cloud.google.com/eventarc/docs/locations#europe):

  * `europe-west8` (Milan, Italy)
  * `europe-west9` (Paris, France)



## May 12, 2022

Feature

[Eventarc for Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/eventarc/docs/gke/creating-triggers) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 11, 2022

Change

Eventarc is available in the following [regions](https://docs.cloud.google.com/eventarc/docs/locations):

  * `australia-southeast2` (Melbourne, Australia)
  * `northamerica-northeast2` (Toronto, Ontario, North America)
  * `southamerica-west1` (Santiago, Chile, South America)



## April 04, 2022

Change

Eventarc is available in the [`asia-south2` (Delhi, India)](https://docs.cloud.google.com/eventarc/docs/locations#asia-pacific) region.

## March 31, 2022

Feature

Support for [creating an Eventarc trigger for a Workflows destination](https://docs.cloud.google.com/eventarc/docs/create-trigger-console) on the [Eventarc page](https://console.cloud.google.com/eventarc/triggers/create) in the Cloud Console is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 21, 2022

Feature

Support for [Firebase Alerts triggers](https://docs.cloud.google.com/eventarc/docs/targets) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 07, 2022

Feature

Support for [Firebase Remote Config and Firebase Test Lab triggers](https://docs.cloud.google.com/eventarc/docs/targets) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 28, 2022

Feature

[Eventarc triggers for Workflows](https://docs.cloud.google.com/eventarc/docs/workflows/create-triggers) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 24, 2022

Announcement

Eventarc is [HIPAA](https://docs.cloud.google.com/security/compliance/hipaa-compliance), [SOC 1](https://docs.cloud.google.com/security/compliance/soc-1), [SOC 2](https://docs.cloud.google.com/security/compliance/soc-2), and [SOC 3](https://docs.cloud.google.com/security/compliance/soc-3)-compliant.

## February 22, 2022

Feature

Support for [applying a path pattern when filtering](https://docs.cloud.google.com/eventarc/docs/path-patterns) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 11, 2022

Announcement

Eventarc is [Payment Card Industry Data Security Standard (PCI DSS)-compliant](https://docs.cloud.google.com/security/compliance/pci-dss).

## December 22, 2021

Feature

Support for [Cloud Storage triggers](https://docs.cloud.google.com/eventarc/docs/creating-triggers#cloud-storage) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## December 16, 2021

Feature

[Eventarc for Cloud Run for Anthos](https://docs.cloud.google.com/eventarc/docs/anthos/creating-triggers) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 13, 2021

Feature

A [dedicated user interface](https://docs.cloud.google.com/eventarc/docs/create-trigger-console) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 28, 2021

Feature

Support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_eventarc) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 13, 2021

Feature

Eventarc can be configured for [data location](https://cloud.google.com/terms/data-residency) and is supported as a [resource location](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#eventarc).

## September 01, 2021

Feature

Support for [Cloud Storage triggers](https://docs.cloud.google.com/eventarc/docs/creating-triggers#cloud-storage) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 17, 2021

Change

Support for 17 regions. See [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

## July 23, 2021

Feature

Support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_eventarc) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## July 22, 2021

Feature

Eventarc is a Cloud Asset Inventory [supported resource type](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types#supported_resource_types).

## April 09, 2021

Feature

The Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) is granted to the Pub/Sub service account by default.

## January 26, 2021

Announcement

[Eventarc](https://docs.cloud.google.com/eventarc/docs) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
