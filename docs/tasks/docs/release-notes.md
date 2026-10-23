---
url: https://docs.cloud.google.com/tasks/docs/release-notes/
title: Cloud Tasks release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:58.250652+00:00
---

# Cloud Tasks release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Resources ](https://docs.cloud.google.com/tasks/docs/resources)



Send feedback 

#  Cloud Tasks release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Tasks. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloud-tasks-release-notes.xml) directly. 

## October 19, 2026

v2

Change

Cloud Tasks is available in the following [locations](https://docs.cloud.google.com/tasks/docs/locations):

  * `asia-south2` (Delhi, India)
  * `northamerica-northeast2` (Toronto, Canada)



## September 30, 2026

v2 & v2beta3

Feature

Cloud Tasks support for the following is generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

  * [Set retry parameters when creating a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task) and override the queue-level retry configuration for the task.
  * [Create a batch of tasks](https://docs.cloud.google.com/tasks/docs/create-tasks#create-batch-tasks) and add the batch to an existing queue.
  * [Delete a batch of tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks#delete-batch-tasks) from a queue.



## July 21, 2026

v2beta3

Feature

Cloud Tasks support for the following is available in [Preview](https://cloud.google.com/products#product-launch-stages):

  * [Set retry parameters when creating a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task) and override the queue-level retry configuration for the task.
  * [Create a batch of tasks](https://docs.cloud.google.com/tasks/docs/create-tasks#create-batch-tasks) and add the batch to an existing queue.
  * [Delete a batch of tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks#delete-batch-tasks) from a queue.



## July 14, 2026

v2

Change

Cloud Tasks is available in the following [locations](https://docs.cloud.google.com/tasks/docs/locations):

  * `me-central1` (Doha, Qatar)
  * `me-central2` (Dammam, Saudi Arabia)



## January 06, 2025

v2 & v2beta3

Feature

To help ensure CMEK usage across an organization, [Cloud Tasks is integrated with two organization policy constraints](https://docs.cloud.google.com/tasks/docs/use-cmek#org-policy).

## March 18, 2024

v2

Announcement

For tasks that have HTTP targets (as opposed to App Engine targets), the option to set routing for tasks at the queue level is now at General Availability (GA). If you set routing at the queue level, you do not have to set routing for each individual task. To learn more, see [Configure routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#routing).

v2

Announcement

The [`BufferTask`](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#buffertask_method) method for creating tasks is now at General Availability (GA).

## October 18, 2023

v2 & v2beta3

Feature

Support for Customer Managed Encryption Keys (CMEK) is now available for Cloud Tasks. To learn more, see the [documentation on using CMEK with Cloud Tasks](https://docs.cloud.google.com/tasks/docs/use-cmek).

## June 15, 2023

v2 & v2beta3

Feature

Cloud Asset Inventory support for Cloud Tasks is now in [Preview](https://cloud.google.com/products#product-launch-stages). For details, see the [Cloud Asset Inventory release note](https://docs.cloud.google.com/asset-inventory/docs/release-notes#June_15_2023).

## April 18, 2023

v2beta3

Feature

For tasks that have HTTP targets (as opposed to App Engine targets), you can now set routing for tasks at the queue level. If you set routing at the queue level, you do not have to set routing for each individual task. To learn more, see [Configure routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#routing).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

v2beta3

Feature

You can now create tasks by sending an HTTP request to your queue. To learn more, read about the new `BufferTask` method to [Create tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#creating_http_target_tasks).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 31, 2023

v2

Feature

Support for resource location organization policies for Cloud Tasks is now at [General Availability](https://cloud.google.com/products#product-launch-stages). To learn more, see the Resource Manager [entry for Cloud Tasks](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#cloud-tasks).

## January 09, 2023

v2

Feature

Support for VPC Service Controls is now at [General Availability](https://cloud.google.com/products#product-launch-stages). To learn more, see [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/tasks/docs/use-vpc-service-controls).

## November 14, 2022

v2

Feature

Support for internal ingress from Cloud Tasks to Cloud Run and Cloud Functions is now at [General Availability](https://cloud.google.com/products#product-launch-stages).

## November 09, 2022

v2

Feature

Support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_tasks) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 13, 2021

v2

Change

You can now create Cloud Tasks queues in multiple GCP Regions around the world. If you are using HTTP Targets, you no longer need to deploy an App Engine application.

## June 25, 2021

v2

Announcement

A [Service Level Agreement](https://cloud.google.com/tasks/sla) (SLA) for Cloud Tasks is now in effect.

## June 16, 2021

v2

Feature

Cloud Tasks is now available in `us-west1`, `asia-east1`, and `asia-southeast1`.

## February 24, 2021

v2

Change

Maximum push task size is now increased to 1 MB.

## January 14, 2021

v2beta3

Feature

Two [Queue](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#resource:-queue) fields that in previous versions were output only are now configurable.

  * `taskTtl` is the maximum amount of time that a task is retained in this queue.
  * `tombstoneTtl` is the amount of time the task tombstone is retained after a task is deleted or executed. The tombstone is used in task de-duplication. For more information on this process, see [Create Task Request](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#body.request_body.FIELDS.task).



These fields are also available in v2beta2.

## December 16, 2020

v2

Change

The relationship between your queues and your App Engine app has changed. If your queues only manage tasks with HTTP Targets, you no longer need to have an **enabled** App Engine app. For more information, see [Create Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues).

## November 20, 2019

v2

Feature

[HTTP Targets](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) GA release.

## May 20, 2019

v2

Feature

[HTTP Targets](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) Beta release.

## April 09, 2019

v2

Feature

Cloud Tasks GA release.

## September 26, 2018

v2

Feature

Cloud Tasks Beta release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
