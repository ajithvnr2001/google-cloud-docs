---
url: https://docs.cloud.google.com/feeds/cloud-tasks-release-notes.xml
title: Cloud Tasks - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:25.813690+00:00
---

# Cloud Tasks - Release notes

> Source: https://docs.cloud.google.com/feeds/cloud-tasks-release-notes.xml

tag:google.com,2016:cloud-tasks-release-notesCloud Tasks - Release notesGoogle Cloud Platform2026-09-30T00:00:00-07:00September 30, 2026tag:google.com,2016:cloud-tasks-release-notes#September_30_20262026-09-30T00:00:00-07:00v2 & v2beta3 

### Feature

Cloud Tasks support for the following is generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

  * [Set retry parameters when creating a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task) and override the queue-level retry configuration for the task.
  * [Create a batch of tasks](https://docs.cloud.google.com/tasks/docs/create-tasks#create-batch-tasks) and add the batch to an existing queue.
  * [Delete a batch of tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks#delete-batch-tasks) from a queue.

]]> July 21, 2026tag:google.com,2016:cloud-tasks-release-notes#July_21_20262026-07-21T00:00:00-07:00v2beta3 

### Feature

Cloud Tasks support for the following is available in [Preview](https://cloud.google.com/products#product-launch-stages):

  * [Set retry parameters when creating a task](https://docs.cloud.google.com/tasks/docs/configure-retry-task) and override the queue-level retry configuration for the task.
  * [Create a batch of tasks](https://docs.cloud.google.com/tasks/docs/create-tasks#create-batch-tasks) and add the batch to an existing queue.
  * [Delete a batch of tasks](https://docs.cloud.google.com/tasks/docs/manage-queues-and-tasks#delete-batch-tasks) from a queue.

]]> July 14, 2026tag:google.com,2016:cloud-tasks-release-notes#July_14_20262026-07-14T00:00:00-07:00v2 

### Change

Cloud Tasks is available in the following [locations](https://docs.cloud.google.com/tasks/docs/locations):

  * `me-central1` (Doha, Qatar)
  * `me-central2` (Dammam, Saudi Arabia)

]]> January 06, 2025tag:google.com,2016:cloud-tasks-release-notes#January_06_20252025-01-06T00:00:00-08:00v2 & v2beta3 

### Feature

To help ensure CMEK usage across an organization, [Cloud Tasks is integrated with two organization policy constraints](https://docs.cloud.google.com/tasks/docs/use-cmek#org-policy).

]]> March 18, 2024tag:google.com,2016:cloud-tasks-release-notes#March_18_20242024-03-18T00:00:00-07:00v2 

### Announcement

For tasks that have HTTP targets (as opposed to App Engine targets), the option to set routing for tasks at the queue level is now at General Availability (GA). If you set routing at the queue level, you do not have to set routing for each individual task. To learn more, see [Configure routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#routing).

### Announcement

The [`BufferTask`](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#buffertask_method) method for creating tasks is now at General Availability (GA).

]]> October 18, 2023tag:google.com,2016:cloud-tasks-release-notes#October_18_20232023-10-18T00:00:00-07:00v2 & v2beta3 

### Feature

Support for Customer Managed Encryption Keys (CMEK) is now available for Cloud Tasks. To learn more, see the [documentation on using CMEK with Cloud Tasks](https://docs.cloud.google.com/tasks/docs/use-cmek).

]]> June 15, 2023tag:google.com,2016:cloud-tasks-release-notes#June_15_20232023-06-15T00:00:00-07:00v2 & v2beta3 

### Feature

Cloud Asset Inventory support for Cloud Tasks is now in [Preview](https://cloud.google.com/products#product-launch-stages). For details, see the [Cloud Asset Inventory release note](https://docs.cloud.google.com/asset-inventory/docs/release-notes#June_15_2023).

]]> April 18, 2023tag:google.com,2016:cloud-tasks-release-notes#April_18_20232023-04-18T00:00:00-07:00v2beta3 

### Feature

For tasks that have HTTP targets (as opposed to App Engine targets), you can now set routing for tasks at the queue level. If you set routing at the queue level, you do not have to set routing for each individual task. To learn more, see [Configure routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#routing).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now create tasks by sending an HTTP request to your queue. To learn more, read about the new `BufferTask` method to [Create tasks](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#creating_http_target_tasks).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> January 31, 2023tag:google.com,2016:cloud-tasks-release-notes#January_31_20232023-01-31T00:00:00-08:00v2 

### Feature

Support for resource location organization policies for Cloud Tasks is now at [General Availability](https://cloud.google.com/products#product-launch-stages). To learn more, see the Resource Manager [entry for Cloud Tasks](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services#cloud-tasks).

]]> January 09, 2023tag:google.com,2016:cloud-tasks-release-notes#January_09_20232023-01-09T00:00:00-08:00v2 

### Feature

Support for VPC Service Controls is now at [General Availability](https://cloud.google.com/products#product-launch-stages). To learn more, see [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/tasks/docs/use-vpc-service-controls).

]]> November 14, 2022tag:google.com,2016:cloud-tasks-release-notes#November_14_20222022-11-14T00:00:00-08:00v2 

### Feature

Support for internal ingress from Cloud Tasks to Cloud Run and Cloud Functions is now at [General Availability](https://cloud.google.com/products#product-launch-stages).

]]> November 09, 2022tag:google.com,2016:cloud-tasks-release-notes#November_09_20222022-11-09T00:00:00-08:00v2 

### Feature

Support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_tasks) is in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> December 13, 2021tag:google.com,2016:cloud-tasks-release-notes#December_13_20212021-12-13T00:00:00-08:00v2 

### Change

You can now create Cloud Tasks queues in multiple GCP Regions around the world. If you are using HTTP Targets, you no longer need to deploy an App Engine application.

]]> June 25, 2021tag:google.com,2016:cloud-tasks-release-notes#June_25_20212021-06-25T00:00:00-07:00v2 

### Announcement

A [Service Level Agreement](https://cloud.google.com/tasks/sla) (SLA) for Cloud Tasks is now in effect.

]]> June 16, 2021tag:google.com,2016:cloud-tasks-release-notes#June_16_20212021-06-16T00:00:00-07:00v2 

### Feature

Cloud Tasks is now available in `us-west1`, `asia-east1`, and `asia-southeast1`.

]]> February 24, 2021tag:google.com,2016:cloud-tasks-release-notes#February_24_20212021-02-24T00:00:00-08:00v2 

### Change

Maximum push task size is now increased to 1 MB.

]]> January 14, 2021tag:google.com,2016:cloud-tasks-release-notes#January_14_20212021-01-14T00:00:00-08:00v2beta3 

### Feature

Two [Queue](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues#resource:-queue) fields that in previous versions were output only are now configurable.

  * `taskTtl` is the maximum amount of time that a task is retained in this queue.
  * `tombstoneTtl` is the amount of time the task tombstone is retained after a task is deleted or executed. The tombstone is used in task de-duplication. For more information on this process, see [Create Task Request](https://docs.cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks/create#body.request_body.FIELDS.task).



These fields are also available in v2beta2.

]]> December 16, 2020tag:google.com,2016:cloud-tasks-release-notes#December_16_20202020-12-16T00:00:00-08:00v2 

### Change

The relationship between your queues and your App Engine app has changed. If your queues only manage tasks with HTTP Targets, you no longer need to have an **enabled** App Engine app. For more information, see [Create Cloud Tasks queues](https://docs.cloud.google.com/tasks/docs/creating-queues).

]]> November 20, 2019tag:google.com,2016:cloud-tasks-release-notes#November_20_20192019-11-20T00:00:00-08:00v2 

### Feature

[HTTP Targets](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) GA release.

]]> May 20, 2019tag:google.com,2016:cloud-tasks-release-notes#May_20_20192019-05-20T00:00:00-07:00v2 

### Feature

[HTTP Targets](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) Beta release.

]]> April 09, 2019tag:google.com,2016:cloud-tasks-release-notes#April_09_20192019-04-09T00:00:00-07:00v2 

### Feature

Cloud Tasks GA release.

]]> September 26, 2018tag:google.com,2016:cloud-tasks-release-notes#September_26_20182018-09-26T00:00:00-07:00v2 

### Feature

Cloud Tasks Beta release.

]]>
