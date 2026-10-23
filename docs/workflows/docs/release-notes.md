---
url: https://docs.cloud.google.com/workflows/docs/release-notes/
title: Workflows release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:39:33.958183+00:00
---

# Workflows release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Resources ](https://docs.cloud.google.com/workflows/docs/resources)



Send feedback 

#  Workflows release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Workflows. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/workflows-release-notes.xml) directly. 

## February 17, 2026

v1

Change

Workflows is available in the following additional [region](https://docs.cloud.google.com/workflows/docs/locations): `asia-southeast3` (Bangkok, Thailand).

## March 28, 2025

v1

Feature

Support for a [Kubernetes API connector](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/Overview) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). The connector allows you to interact with Kubernetes objects in a Google Kubernetes Engine cluster. For more information, see [Access Kubernetes API objects using a connector](https://docs.cloud.google.com/workflows/docs/access-kubernetes-api).

## February 28, 2025

v1

Feature

Support to [create and manage tags](https://docs.cloud.google.com/workflows/docs/create-manage-tags) is available. You can use tags to group workflows and other resources for reporting, auditing, and access control.

## February 19, 2025

v1

Change

Workflows is available in the following additional [region](https://docs.cloud.google.com/workflows/docs/locations): `europe-north2` (Stockholm, Sweden).

## February 07, 2025

v1

Change

Support for retrieving the [detailed history of a workflow execution (expected iterations, in-scope variables)](https://docs.cloud.google.com/workflows/docs/debug-steps) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 06, 2025

v1

Feature

Support for [creating custom organization policy constraints](https://docs.cloud.google.com/workflows/docs/custom-constraints) is available.

## January 28, 2025

v1

Breaking

Workflows doesn't support HTTP requests to the IP-based endpoints of Google Kubernetes Engine cluster control planes. To ensure that your workflow functions as expected, you must access the DNS-based endpoints. For more information about the scope and impact, see the [service announcement](https://docs.cloud.google.com/workflows/docs/service-announcements#2025-01-28).

## October 28, 2024

v1

Feature

Two standard library functions to support common hashing algorithms have been added: [`compute_checksum`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_checksum) and [`compute_hmac`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_hmac).

## September 30, 2024

v1

Feature

A [math.floor](https://docs.cloud.google.com/workflows/docs/reference/stdlib/math/floor) function has been added to return the largest integer less than or equal to a given number.

## September 13, 2024

v1

Change

The maximum number of [concurrent workflow executions](https://docs.cloud.google.com/workflows/quotas#quotas) has increased from 7,500 to 10,000.

## September 03, 2024

v1

Feature

Support for [execution backlogging](https://docs.cloud.google.com/workflows/docs/executing-workflow#manage_execution_backlogging) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Backlogged executions automatically run as soon as execution concurrency quota becomes available.

## June 17, 2024

v1

Feature

Support for a [Vertex AI API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/Overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Learn how to [access Vertex AI models from a workflow](https://docs.cloud.google.com/workflows/docs/tutorials/use-vertex-ai-models).

## May 31, 2024

v1

Feature

Support for the following connectors is generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

  * [AI platform training and prediction](https://docs.cloud.google.com/workflows/docs/reference/googleapis/ml/Overview)
  * [Application Integration](https://docs.cloud.google.com/workflows/docs/reference/googleapis/integrations/Overview)
  * [Batch API](https://docs.cloud.google.com/workflows/docs/reference/googleapis/batch/Overview)
  * [BigQuery Data Transfer](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/Overview)
  * [Cloud Resource Manager](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/Overview)
  * [Google Forms](https://docs.cloud.google.com/workflows/docs/reference/googleapis/forms/Overview)
  * [Google Sheets](https://docs.cloud.google.com/workflows/docs/reference/googleapis/sheets/Overview)
  * [Transcoder API](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/Overview)



## May 30, 2024

v1

Change

The maximum number of [concurrent workflow executions](https://docs.cloud.google.com/workflows/quotas#quotas) has increased from 5,000 to 7,500.

## April 22, 2024

v1

Change

Workflows is available in the following additional [region](https://docs.cloud.google.com/workflows/docs/locations): `me-central1` (Doha, Qatar).

## March 04, 2024

v1

Fixed

An issue that allowed [jumps](https://docs.cloud.google.com/workflows/docs/reference/syntax/jumps) in or out of parallel branches, parallel loops, and `for` loops is resolved. Only these jumps are allowed:

  * To steps within the same [parallel branch or loop](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#jumps)
  * Between steps belonging to the same [for loop](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#jump-in-loop)



## February 19, 2024

v1

Change

The maximum number of [concurrent workflow executions](https://docs.cloud.google.com/workflows/quotas#quotas) has increased from 3,000 to 5,000.

## January 31, 2024

v1

Change

Workflows is available in the following additional [region](https://docs.cloud.google.com/workflows/docs/locations): `africa-south1` (Johannesburg, South Africa).

## January 11, 2024

v1

Feature

Support for [invoking a VPC Service Controls-compliant private endpoint](https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

v1

Feature

Support for [defining environment variables at deployment time](https://docs.cloud.google.com/workflows/docs/use-environment-variables) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). See the blog post: [Custom Environment Variables in Workflows](https://medium.com/google-cloud/custom-environment-variables-in-workflows-a72851049cb3).

## December 15, 2023

v1

Feature

Support to [view the history of a workflow execution as a list of step entries](https://docs.cloud.google.com/workflows/docs/debug-steps) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). See the blog post: [Announcing Workflows execution steps history](https://docs.cloud.google.com/blog/products/application-development/announcing-workflows-execution-steps-history).

**Note:** To view the step entries in the Google Cloud console on the **Execution details** page, you must have a role that contains the `workflows.workflows.get`, `workflows.executions.get`, and `workflows.stepEntries.list` permissions.

## November 17, 2023

v1

Feature

Support for a [Kubernetes API connector](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/Overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages). The connector allows you to interact with Kubernetes objects in a Google Kubernetes Engine cluster. For more information, see [Access Kubernetes API objects using a connector](https://docs.cloud.google.com/workflows/docs/access-kubernetes-api). 

See the blog post: [Deploy and manage Kubernetes applications with Workflows](https://docs.cloud.google.com/blog/products/application-development/use-workflows-to-deploy-and-manage-kubernetes).

## October 31, 2023

v1

Change

Workflows is available in the following additional [region](https://docs.cloud.google.com/workflows/docs/locations): `europe-west10` (Berlin, Germany).

## October 26, 2023

v1

Change

A connection reset error is tagged as a `ConnectionError` and not a `ConnectionFailedError`, and it is not retried for non-idempotent requests. For more information, see [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types) and [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying).

## September 19, 2023

v1

Change

Workflows is available in the following additional [region](https://docs.cloud.google.com/workflows/docs/locations): `me-central2` (Dammam, Saudi Arabia).

## July 06, 2023

v1

Feature

Support for [defining environment variables at deployment time](https://docs.cloud.google.com/workflows/docs/use-environment-variables) is available in [Preview](https://cloud.google.com/products#product-launch-stages). See the blog post: [Custom Environment Variables in Workflows](https://medium.com/google-cloud/custom-environment-variables-in-workflows-a72851049cb3).

## June 30, 2023

v1

Feature

Three functions are available: [`map.merge`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/merge) takes two maps, creates a copy of the first map, and adds items from the second map to the copy; [`map.merge_nested`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/merge_nested) recursively adds items from a map to a copy of another map; [`uuid.generate`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/uuid/generate) returns a random universally unique identifier.

v1

Feature

Support for [invoking a VPC Service Controls-compliant private endpoint](https://docs.cloud.google.com/workflows/docs/invoke-private-endpoint-vpc) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 26, 2023

v1

Feature

Support for [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/workflows/docs/use-cmek) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## June 19, 2023

v1

Fixed

An issue with how Workflows handles HTTP headers with duplicate keys is resolved. The values associated with duplicate header keys are merged into a comma-separated list as described in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110). Previously, all but one of the values associated with duplicate keys would be dropped.

## June 15, 2023

v1

Feature

Cloud Asset Inventory support for Workflows is now publicly available. For details, see the [Cloud Asset Inventory release note](https://docs.cloud.google.com/asset-inventory/docs/release-notes#June_15_2023).

## May 17, 2023

v1

Feature

Support for a [Batch API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/batch/Overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 10, 2023

v1

Change

You can apply [call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) to a workflow definition as well as to the execution of a workflow, and specify the level of logging required. The execution log level takes precedence over any workflow log level, unless the execution log level is not specified.

## May 01, 2023

v1

Feature

The [Cloud Workflows service agent](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.serviceAgent) has the ability to consume quota and billing for a project through the [`serviceusage.services.use`](https://docs.cloud.google.com/service-usage/docs/access-control#permissions) permission. This allows workflows to count quota and apply billing to the correct project when making calls to other Google APIs.

## April 14, 2023

v1

Feature

[Use the Workflows JSON schema in your IDE](https://docs.cloud.google.com/workflows/docs/use-workflows-json-schema-with-ide) to provide syntax support when creating a workflow. See the Google Cloud Blog post: [Workflows gets an updated JSON Schema](https://docs.cloud.google.com/blog/products/application-development/integrated-workflows-inside-your-ide-of-choice-help-you-develop).

v1

Feature

Workflows support for [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/workflows/docs/use-cmek) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 21, 2023

v1

Feature

Support for triggering a workflow using Eventarc within a [VPC Service Controls perimeter](https://docs.cloud.google.com/eventarc/docs/using-vpc-service-controls) is generally available ([GA](https://cloud.google.com/products#section-23)).

## March 16, 2023

v1

Feature

Support for a [Transcoder API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/Overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 02, 2023

v1

Change

Workflows is available in the following additional [regions](https://docs.cloud.google.com/workflows/docs/locations):

  * `asia-northeast3` (Seoul, South Korea)
  * `asia-southeast2` (Jakarta, Indonesia)
  * `me-west1` (Tel Aviv, Israel)
  * `southamerica-west1` (Santiago, Chile)



v1

Feature

Support for [limiting the maximum number of concurrent branches or iterations](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#concurrency) within a `parallel` step is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## February 21, 2023

v1

Fixed

An issue where one [shared variable](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#variables) in a subworkflow overwrote another in a calling subworkflow during a workflow's execution is resolved. This affected calling a subworkflow with a parallel step from within a parallel step.

## January 10, 2023

v1

Feature

A [`get_type` function](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#type_functions) that returns a string indicating an argument's data type is available.

## January 04, 2023

v1

Feature

Support for an [Application Integration connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/integrations/Overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 15, 2022

v1

Feature

A workflow's source and details can now be [updated independently through the Cloud Console](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#update_a_workflow) using the Source and Details tabs for quicker editing.

## December 09, 2022

v1

Feature

A [`list.prepend` function](https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/prepend) is available to support creating a copy of a list with a new element added to the beginning.

## November 08, 2022

v1

Change

Workflows is available in the following additional [regions](https://docs.cloud.google.com/workflows/docs/locations):

  * `asia-east2` (Hong Kong, China)
  * `europe-central2` (Warsaw, Poland)
  * `europe-southwest1` (Madrid, Spain)
  * `europe-west9` (Paris, France)
  * `northamerica-northeast2` (Toronto, Canada)
  * `us-east5` (Columbus, United States)
  * `us-south1` (Dallas, United States)
  * `us-west2` (Los Angeles, United States)
  * `us-west3` (Salt Lake City, United States)



## October 24, 2022

v1

Feature

Support for [limiting the maximum number of concurrent branches or iterations](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#concurrency) within a `parallel` step is available in [Preview](https://cloud.google.com/products#product-launch-stages).

v1

Change

Eventarc event-triggered requests are limited by the [execution API write request](https://docs.cloud.google.com/workflows/quotas#request_limit) on workflows. Events that exceed the limit follow the [Eventarc retry policy](https://docs.cloud.google.com/eventarc/docs/retry-events).

## October 17, 2022

v1

Feature

Support for [Eventarc triggers for Workflows](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## October 12, 2022

v1

Change

The [memory available](https://docs.cloud.google.com/workflows/quotas#resource_limit) for workflow variables and runtime arguments (including Eventarc events) has been doubled to 512 KB per execution.

## October 05, 2022

v1

Feature

Support for [parallel steps](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 23, 2022

v1

Announcement

Workflows is [FedRAMP Moderate-compliant](https://docs.cloud.google.com/security/compliance/fedramp).

## September 13, 2022

v1

Feature

Execution results include the current or final step of the [workflow execution](https://docs.cloud.google.com/workflows/docs/monitor#access-results).

## September 06, 2022

v1

Feature

Support for connectors for [Google Forms](https://docs.cloud.google.com/workflows/docs/reference/googleapis/forms/Overview) and [Google Sheets](https://docs.cloud.google.com/workflows/docs/reference/googleapis/sheets/Overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 29, 2022

v1

Feature

Added support to deploy a workflow using a cross-project service account through the [Google Cloud console](https://docs.cloud.google.com/workflows/docs/authentication#deploy_a_workflow_with_a_cross-project_service_account).

## August 05, 2022

v1

Feature

Added `skip_polling` so that [connectors](https://docs.cloud.google.com/workflows/docs/reference/googleapis) can execute asynchronously without waiting for the operation to complete.

## August 02, 2022

v1

Change

Workflows is available in the following additional [regions](https://docs.cloud.google.com/workflows/docs/locations):

  * `asia-northeast2` (Osaka, Japan)
  * `asia-south2` (Delhi, India)
  * `australia-southeast2` (Melbourne, Australia)
  * `europe-north1` (Hamina, Finland)
  * `europe-west2` (London, England)
  * `europe-west3` (Frankfurt, Germany)
  * `southamerica-east1` (Osasco, São Paulo, Brazil)
  * `us-east4` (Ashburn, Virginia, United States)
  * `us-west4` (Las Vegas, Nevada, United States)



v1

Feature

The following functions have been added:

  * `text.url_encode` [returns a string with percent-encoded reserved characters, including spaces](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode)
  * `text.url_encode_plus` [returns a string with percent-encoded reserved characters, and spaces replaced by pluses](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode_plus)
  * `text.url_decode` [returns a string with pluses and percent-escaped characters converted to UTF-8](https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_decode)



## July 11, 2022

v1

Feature

Added support to deploy a workflow using a [cross-project service account](https://docs.cloud.google.com/workflows/docs/authentication#deploy_a_workflow_with_a_cross-project_service_account) through the Google Cloud CLI.

## July 01, 2022

v1

Breaking

To reduce naming conflicts and improve memory usage, local scoping now applies to any variable created inside an [`except` block](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors#variable-scope). 

If you are assigning a variable inside an `except` block and want to access the variable outside of the block, [assign the variable before the block to place it in the surrounding scope](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-outer-scope).

## June 21, 2022

v1

Feature

Workflows can [invoke private on‑premises, Compute Engine, Google Kubernetes Engine (GKE), or other Google Cloud endpoints](https://docs.cloud.google.com/workflows/docs/enable-iap-call-private-endpoints) that are Identity-Aware Proxy (IAP)-enabled.

## June 20, 2022

v1

Announcement

Support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_workflows) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## June 13, 2022

v1

Feature

[Parallel steps](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps) are available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## June 01, 2022

v1

Change

Workflows is available in the `europe-west8` (Milan, Italy) [region](https://docs.cloud.google.com/workflows/docs/locations).

## May 16, 2022

v1

Breaking

[Workflows using callbacks](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) that were deployed on or before January 11, 2022 must be redeployed to continue executing workflows without failures.

## May 12, 2022

v1

Feature

A `Status` field that tracks the current steps and progress of an execution is available in [Preview](https://cloud.google.com/products#product-launch-stages). See the [Workflows Executions REST API Overview](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions#status).

v1

Feature

The following functions have been added:

  * `default` and `if` support [conditions within expressions](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#conditional-functions)
  * `map.get` [performs a safe lookup on a map](https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/get), returning `null` if a key is not found



## April 21, 2022

v1

Feature

[Call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 06, 2022

v1

Announcement

Terraform support to [create an Eventarc trigger that invokes Workflows](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 31, 2022

v1

Feature

Support for [creating an Eventarc trigger](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc#create_a_trigger_using_the_console) on the [Workflows page](https://console.cloud.google.com/workflows/create) in the Cloud Console is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 25, 2022

v1

Change

Workflows is available in the following [regions](https://docs.cloud.google.com/workflows/docs/locations):

  * `asia-east1` (Changhua County, Taiwan)
  * `asia-northeast1` (Tokyo, Japan)
  * `asia-south1` (Mumbai, India)
  * `australia-southeast1` (Sydney, Australia)
  * `northamerica-northeast1` (Montréal, Québec)
  * `us-west1` (The Dalles, Oregon)



## March 07, 2022

v1

Feature

Support for the following connectors is available in [Preview](https://cloud.google.com/products#product-launch-stages):

  * [AI platform training and prediction](https://docs.cloud.google.com/workflows/docs/reference/googleapis/ml/Overview)
  * [BigQuery data transfer](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/Overview)
  * [Cloud Resource Manager](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/Overview)



## March 03, 2022

v1

Announcement

Support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_workflows) is in [Beta stage](https://cloud.google.com/products/#product-launch-stages).

## February 28, 2022

v1

Feature

[Eventarc triggers for Workflows](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 18, 2022

v1

Feature

[Checking for the existence of a key in a list](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists#check-key) is supported.

## January 31, 2022

v1

Announcement

Workflows is [Payment Card Industry Data Security Standard (PCI DSS)-compliant](https://docs.cloud.google.com/security/compliance/pci-dss).

## January 28, 2022

v1

Change

Workflows is available in the following [regions](https://docs.cloud.google.com/workflows/docs/locations):

  * `europe-west1` (Belgium)
  * `europe-west6` (Zurich)
  * `us-east1` (South Carolina)



## January 24, 2022

v1

Feature

[Callback endpoints](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) are generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## January 18, 2022

v1

Announcement

Workflows is now certified as [SOC 1-compliant](https://docs.cloud.google.com/security/compliance/soc-1).

## January 05, 2022

v1

Feature

Workflows can invoke Cloud Functions or Cloud Run services that have [ingress restricted to internal traffic](https://docs.cloud.google.com/workflows/docs/calling-run-functions#internal_ingress).

## December 10, 2021

v1

Feature

[Dynamic keys](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps) are supported.

## December 07, 2021

v1

Change

[Resource limits](https://docs.cloud.google.com/workflows/quotas) for variable memory and argument size have been increased to 256 KB.

## December 06, 2021

v1

Feature

A [Workflows Service Level Agreement (SLA)](https://cloud.google.com/workflows/sla) is available and applicable.

## November 19, 2021

v1

Feature

Workflows can be [scheduled](https://docs.cloud.google.com/workflows/docs/schedule-workflow#console) through the Workflows page in the Cloud Console.

## November 17, 2021

v1

Feature

The following functions have been added: 

  * [`sys.sleep_until`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep_until) — Suspends execution until the given time
  * [`time.format`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/format) — Formats timestamp as a human-readable string
  * [`time.parse`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/parse) — Parses ISO 8601-compatible string into a timestamp



## October 28, 2021

v1

Feature

A [built-in environment variable](https://docs.cloud.google.com/workflows/docs/reference/environment-variables), `GOOGLE_CLOUD_SERVICE_ACCOUNT_NAME`, is supported to access the service account name for a workflow execution.

## September 14, 2021

v1

Feature

[Call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#apply-call-logging) is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## September 13, 2021

v1

Feature

[Connectors](https://docs.cloud.google.com/workflows/docs/connectors) are generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 07, 2021

v1

Feature

Support for [callback endpoints](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 02, 2021

v1

Feature

Support for [iterating](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration) over a sequence of numbers or through a collection of data is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## July 28, 2021

v1

Feature

A [`list.concat`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/concat) function has been added to support adding an element to a list.

## July 23, 2021

v1

Feature

[Platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#workflows) are supported by Cloud Logging.

## June 25, 2021

v1

Feature

Syntax for updating [list values](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists#updating-list-values) and [map values](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps#insert-map-values) is supported.

## June 07, 2021

v1

Feature

String processing functions are available in the `text` module of the [Workflows standard library](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview).

## May 31, 2021

v1

Feature

Visualization support while editing the Workflows iteration syntax is available through the [Google Cloud Console](https://console.cloud.google.com/workflows).

## May 10, 2021

v1

Feature

Workflows is [HIPAA compliant](https://docs.cloud.google.com/security/compliance/hipaa-compliance).

## January 25, 2021

v1

Announcement

Workflows is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

v1

Feature

[Connectors](http://cloud.google.com/workflows/docs/connectors) are available in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 10, 2020

v1beta

Feature

Workflows launched a visualization feature. The [Google Cloud Console](https://console.cloud.google.com/workflows) displays a visualization of the workflow during editing.

## December 08, 2020

v1beta

Feature

Workflows is available in the following regions:

  * `asia-southeast1` (Singapore)
  * `europe-west4` (Netherlands)



## August 25, 2020

v1beta

Announcement

Beta launch of [Workflows](https://docs.cloud.google.com/workflows).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
