---
url: https://docs.cloud.google.com/scheduler/docs/release-notes/
title: Cloud Scheduler release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:43.237947+00:00
---

# Cloud Scheduler release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Resources ](https://docs.cloud.google.com/scheduler/docs/resources)



Send feedback 

#  Cloud Scheduler release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Scheduler. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloudscheduler-release-notes.xml) directly. 

## September 24, 2026

Change

Cloud Scheduler is available in the following [locations](https://docs.cloud.google.com/scheduler/docs/locations):

  * `asia-south2` (Delhi, India)
  * `europe-west12` (Turin, Italy)
  * `northamerica-northeast2` (Toronto, Ontario, Canada)



## September 18, 2026

Change

Cloud Scheduler is available in the following [location](https://docs.cloud.google.com/scheduler/docs/locations):

  * `asia-southeast3` (Bangkok, Thailand)



## July 29, 2026

Change

Cloud Scheduler is available in the following [locations](https://docs.cloud.google.com/scheduler/docs/locations):

  * `europe-west8` (Milan, Italy)
  * `europe-west9` (Paris, France)
  * `us-south1` (Dallas, United States)



## April 17, 2026

Change

Cloud Scheduler is available in the following [locations](https://docs.cloud.google.com/scheduler/docs/locations):

  * `europe-west4` (Eemshaven, Netherlands)
  * `me-central1` (Doha, Qatar)
  * `me-central2` (Dammam, Saudi Arabia)
  * `me-west1` (Tel Aviv, Israel)



## September 29, 2025

Change

VPC Service Controls support for Cloud Scheduler jobs has been extended to Google Cloud APIs that are VPC Service Controls-compliant. For more information, see [Secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).

## August 18, 2023

Change

Support for Cloud Scheduler to call the following resources internally is in [GA](https://cloud.google.com/products#product-launch-stages):

  * Cloud Functions
  * Cloud Run



Feature

VPC Service Controls support for Cloud Scheduler jobs with the following targets is now in [GA](https://cloud.google.com/products#product-launch-stages):

  * Cloud Functions
  * Cloud Run
  * Dataflow API
  * Data Pipelines



To learn more, see the documentation on how to [secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).

## April 14, 2023

Change

Support for Cloud Scheduler to call the following resources internally is in [Preview](https://cloud.google.com/products#product-launch-stages):

  * Cloud Functions
  * Cloud Run



Feature

VPC Service Controls support for Cloud Scheduler jobs with the following targets is now in [Preview](https://cloud.google.com/products#product-launch-stages):

  * Cloud Functions
  * Cloud Run
  * Dataflow API
  * Data Pipelines



To learn more, see the documentation on how to [secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).

## August 26, 2022

Feature

Support for using VPC Service Controls with Cloud Scheduler is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). To get started, check out the documentation on how to [secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).

## June 09, 2022

Feature

Cloud Scheduler jobs that are paused can now be edited. See [Create and configure cron jobs](https://docs.cloud.google.com/scheduler/docs/creating).

## February 11, 2022

Change

Cloud Scheduler jobs for HTTP or Pub/Sub Targets can be deployed in multiple GCP Regions around the world and no longer require that an App Engine application be deployed.

## June 16, 2021

Change

Cloud Scheduler is now available in `us-west1`, `asia-east1`, and `asia-southeast1`.

## April 22, 2021

Feature

The Cloud Scheduler Console UI now has support for three additional options:

  * Headers for HTTP and App Engine targets
  * Message attributes for Pub/Sub targets
  * Retry config for all targets



## March 01, 2021

Change

The maximum job size (payload) is now 1 MB total, including ~1KB request overhead.

## February 04, 2021

Feature

Two new headers, [X-CloudScheduler-JobName and X-CloudScheduler-ScheduleTime](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#appenginehttptarget), have been added to the default headers for AppEngineHttpTarget and HttpTarget. These can be used to help with job deduplication.

## March 04, 2019

Feature

Cloud Scheduler GA release.

## November 06, 2018

Feature

Cloud Scheduler Beta release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
