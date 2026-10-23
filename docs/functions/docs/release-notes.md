---
url: https://docs.cloud.google.com/functions/docs/release-notes/
title: Cloud Run functions (formerly known as Cloud Functions) release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:04.137350+00:00
---

# Cloud Run functions (formerly known as Cloud Functions) release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/release-notes/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Resources ](https://docs.cloud.google.com/functions/docs/resources)



Send feedback 

#  Cloud Run functions (formerly known as Cloud Functions) release notes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Functions (2nd gen) is now Cloud Run functions. The [Cloud Functions API](https://docs.cloud.google.com/functions/docs/apis) is still supported for performing operations on functions. 

This page documents production updates to Cloud Run functions. We recommend that Cloud Run functions developers periodically check this list for any new announcements. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/functions-release-notes.xml) directly. 

## October 22, 2026

Security

All supported versions of [PHP 8.2](https://docs.cloud.google.com/functions/docs/runtime-support#php) and later are patched. Take immediate protective action by redeploying your resources with updated dependencies.

See [Responding to core PHP vulnerabilities](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619) for more information.

## October 21, 2026

Security

This note is incorrect; follow guidance in the entry for October 22, 2026.

Patch updates to [supported PHP runtimes](https://docs.cloud.google.com/functions/docs/runtime-support#php) are available with deployments from source: `8.5.12`, `8.4.27`, `8.3.36`, and `8.2.35`. Functions with automatic base image updates enabled have already been patched. If you have disabled automatic base image updates, take immediate action to protect your workloads by redeploying your workloads with updated dependencies and redeploying. See [Responding to core PHP vulnerabilities](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619) for more information.

## September 01, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## August 19, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates align more closely with the [Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more information, see [Runtime support schedule](https://docs.cloud.google.com/functions/docs/runtime-support#go).

## August 10, 2026

Feature

The [Cloud Run functions upgrade tool](https://docs.cloud.google.com/functions/1stgendocs/migrating/upgrade-gen1-functions) is in [General Availability](https://cloud.google.com/products#product-launch-stages). Use this tool to upgrade 1st gen functions to Cloud Run functions.

## July 27, 2026

Feature

Support for the [Node.js 26 runtime](https://docs.cloud.google.com/static/functions/docs/concepts/execution-environment#node.js) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 17, 2026

Feature

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#ruby) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## March 12, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## March 03, 2026

Feature

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#ruby) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 27, 2026

Feature

Support for [PHP 8.5 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#php) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 24, 2026

Feature

Support for the ability to configure [Direct VPC egress for 2nd gen functions](https://docs.cloud.google.com/functions/docs/running/direct-vpc) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 19, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 18, 2026

Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#.net) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 02, 2026

Feature

Support for [PHP 8.5 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#php) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 27, 2026

Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#.net) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 06, 2026

Feature

You can now configure [Direct VPC egress for 2nd gen functions](https://docs.cloud.google.com/functions/docs/running/direct-vpc). This support is at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## December 22, 2025

Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#java) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## December 19, 2025

Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#python) is in [General Availability](https://cloud.google.com/products#product-launch-stages). Starting from Python version 3.14 and later, the Python Buildpack uses the uv package manager as the default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies#dependencies).

## November 20, 2025

Feature

Support for [Node.js 24 runtime](https://docs.cloud.google.com/static/functions/docs/concepts/execution-environment#node.js) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## November 12, 2025

Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#python) is in [Preview](https://cloud.google.com/products#product-launch-stages). Starting from Python version 3.14 and later, the Python Buildpack uses the uv package manager as the default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies#dependencies).

## October 31, 2025

Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#java) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 07, 2025

Feature

Cloud Run functions (1st gen) supports the [Node.js 22 runtime](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## October 01, 2025

Feature

Cloud Run functions now provides an [upgrade tool](https://docs.cloud.google.com/functions/1stgendocs/migrating/upgrade-gen1-functions) for upgrading 1st gen functions to Cloud Run. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 21, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## July 30, 2025

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [Preview](https://cloud.google.com/products#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

Feature

Support for [Node.js 24 runtime](https://docs.cloud.google.com/static/functions/docs/concepts/execution-environment#node.js) is in [Preview](https://cloud.google.com/products#product-launch-stages). Node.js 24 is in the Current release state and enters long-term support (LTS) in October 2025. For more information, see [Node.js v24.0.0 (Current) ](https://nodejs.org/en/blog/release/v24.0.0) in the Node.js website.

## July 15, 2025

Feature

Support for the [Go 1.24 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 17, 2025

Feature

Support for the [Ruby 3.4 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#ruby) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Support for the [PHP 8.4 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#php) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## May 30, 2025

Feature

For Java functions that use `functions-framework` version 1.4.0 or later, you can now use the logging class `java.util.logging.Logger` to add a [unique execution ID](https://docs.cloud.google.com/run/docs/runtimes/java#execution_id) to log outputs.

## May 13, 2025

Feature

Labels you previously set for your Cloud Run functions using either `gcloud functions` commands or the Cloud Functions v2 API propagate to Cloud Run when you [deploy your functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions). For more information on creating labels in Cloud Run, see [Configure labels for services](https://docs.cloud.google.com/run/docs/configuring/services/labels#set-labels).

## May 05, 2025

Feature

Support for the [Python 3.13 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#python) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Support for the [Ruby 3.4 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#ruby) is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Support for the [PHP 8.4 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#php) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 21, 2025

Feature

Cloud Run functions now supports the [Python 3.13 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#python) at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## March 03, 2025

Feature

Cloud Run functions now supports the [Go 1.23 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## February 19, 2025

Feature

Support for [deploying v2 functions](https://docs.cloud.google.com/run/docs/deploy-functions) in Cloud Run is now in general availability (GA). This lets you customize your function as you would a Cloud Run service. This change removes support for creating, deploying, or updating v2 functions in the Google Cloud console. However, you can still manage functions created with the Cloud Functions v2 API using the Cloud Functions gcloud CLI, the Cloud Functions v2 API, or the Cloud Run Cloud Console. See [Cloud Run functions comparison](https://docs.cloud.google.com/run/docs/functions/comparison) for more details.

## February 11, 2025

Feature

Cloud Run functions created with the Cloud Functions (v2) API (`cloudfunctions.googleapis.com`) can now be detached so that they can only be managed through the Cloud Run Admin API (`run.googleapis.com`). When the detach operation completes, your function will retain its `cloudfunctions.net` URLs and triggers, and can only be managed using the Cloud Run Admin API. Note that the detach operation is irreversible. For more information see [Manage functions](https://docs.cloud.google.com/functions/docs/managing).

## December 09, 2024

Feature

You can now create [custom organization policies](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#custom-constraints) for Serverless VPC Access connectors and apply them to projects, folders, or organizations. This support is at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## November 19, 2024

Feature

Cloud Run functions now supports the [Go 1.23 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## November 18, 2024

Feature

Cloud Run functions now supports the [Node.js 22 runtime](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## October 10, 2024

Feature

You can now [manage function resources using custom constraints](https://docs.cloud.google.com/functions/docs/securing/custom-constraints) that get enforced at the project level. This support is at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## September 30, 2024

Feature

You can now [manage function resources using custom constraints](https://docs.cloud.google.com/functions/docs/securing/custom-constraints) that get enforced at the project level. This support is at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## September 23, 2024

Change

The [runtime support schedule for some PHP runtimes](https://docs.cloud.google.com/functions/docs/runtime-support#php) has been extended to match [PHP's public support schedule](https://www.php.net/supported-versions.php).

## August 26, 2024

Change

The Cloud Run functions (cloud functions v2 API) [build process](https://docs.cloud.google.com/functions/docs/building#image_registry) now supports cross-project Artifact Registry repositories for greater configurability. This support is at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## August 21, 2024

Announcement

Cloud Functions has been renamed to Cloud Run functions. 

  * Cloud Functions (1st gen) is now known as Cloud Run functions (1st gen).
  * Cloud Functions (2nd gen) is now known as Cloud Run functions.



Learn more in the [blog post](https://cloud.google.com/blog/products/serverless/google-cloud-functions-is-now-cloud-run-functions).

You can also deploy new functions, and modify existing functions that were created with the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis) in [Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions). This enables you to customize your function as you would a Cloud Run service.

## July 31, 2024

Feature

Cloud Functions now supports the [Ruby 3.3 runtime](https://docs.cloud.google.com/functions/docs/runtime-support#ruby) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## July 11, 2024

Announcement

Starting in July 2024, Cloud Build has changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying functions for the first time may be using a default Cloud Build service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) for building a function. If you are impacted by this change you can do one of the following:

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).
  * Add the [Cloud Build Service Account role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`) to the default Compute Service Account.
  * Create a [custom build service account](https://docs.cloud.google.com/functions/docs/securing/build-custom-sa#grant_permissions) for function deployments.



## June 28, 2024

Change

Cloud Functions 1st gen and 2nd gen now support [custom service accounts for Cloud Build](https://docs.cloud.google.com/functions/docs/securing/build-custom-sa) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## June 27, 2024

Change

To simplify searches and improve your documentation experience, we have split the [1st generation](https://docs.cloud.google.com/functions/1stgendocs/concepts/overview) and [2nd generation](https://docs.cloud.google.com/functions/docs/concepts/overview) documentation into separate documentation sets.

## June 24, 2024

Feature

Cloud Functions (2nd gen) now supports fully automatic security updates. For details, see the document [Execution environment security](https://docs.cloud.google.com/functions/docs/securing#updating).

## June 18, 2024

Change

You can now enable execution ID in the logs for 2nd gen Python functions that use `functions-framework >= 3.7.0` and 2nd gen Node.js functions that use `functions-framework >= 3.4.0` by setting the runtime environment variable `LOG_EXECUTION_ID` to `true`.

Feature

Cloud Functions has added support for a new runtime, [Ruby 3.3](https://docs.cloud.google.com/functions/docs/concepts/ruby-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## May 17, 2024

Feature

Cloud Functions (2nd gen) now supports the [Node.js 22](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime) runtime at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## March 26, 2024

Feature

Cloud Functions (2nd gen) now supports the Go 1.22 runtime at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## March 06, 2024

Feature

Cloud Functions (1st gen) now supports [custom service accounts](https://docs.cloud.google.com/functions/docs/securing/build-custom-sa) for Cloud Build, at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## February 26, 2024

Feature

Cloud Functions now supports the PHP 8.3 and Java 21 runtimes at the [General Availability release level](https://cloud.google.com/products#product-launch-stages) for 2nd gen functions.

Feature

Cloud Functions now supports the Go 1.22 runtime at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## February 12, 2024

Feature

Cloud Functions now supports the [PHP 8.3 runtime](https://docs.cloud.google.com/functions/docs/concepts/php-runtime) at the [Preview release level](https://cloud.google.com/products#product-launch-stages) for 2nd gen functions.

## January 23, 2024

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#update-connector) is now available at the [General Availability release level](https://cloud.google.com/products#product-launch-stages). This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## January 15, 2024

Change

Cloud Functions (1st gen) now uses Artifact Registry as the default container registry. See [Customize the Cloud Functions build process](https://docs.cloud.google.com/functions/docs/building) for details.

## January 10, 2024

Feature

Cloud Functions now supports the [.NET 8](https://docs.cloud.google.com/functions/docs/concepts/dotnet-runtime) runtime at the [General Availability release level](https://cloud.google.com/products#product-launch-stages) for 2nd gen functions.

## January 08, 2024

Feature

Cloud Functions (2nd gen) now supports [custom service accounts](https://docs.cloud.google.com/functions/docs/securing/build-custom-sa) for Cloud Build, at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## December 21, 2023

Change

A warning message now appears before you publish a container image to a public repository.

## December 11, 2023

Feature

The new region `me-west1` is now available. See [Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## December 06, 2023

Feature

Cloud Functions (2nd gen) now supports the [Java 21](https://docs.cloud.google.com/functions/docs/concepts/java-runtime) runtime at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

Feature

Cloud Functions (2nd gen) now supports the [.NET 8](https://docs.cloud.google.com/functions/docs/concepts/dotnet-runtime) runtime at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## November 14, 2023

Change

The ability to optionally configure 2nd gen functions with user-specified [concurrency](https://docs.cloud.google.com/functions/docs/configuring/concurrency#set-concurrency-gcf) and [vCPU](https://docs.cloud.google.com/functions/docs/configuring/memory#set-vcpu) is now available at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## November 08, 2023

Feature

Cloud Functions now supports on-deployment security updates (1st gen and 2nd gen) and fully automatic security updates (1st gen only). For details, see [Execution environment security](https://docs.cloud.google.com/functions/docs/securing/execution-environment-security).

## November 06, 2023

Feature

Cloud Functions now supports the [Python 3.12](https://docs.cloud.google.com/functions/docs/concepts/python-runtime) runtime at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## October 16, 2023

Feature

Cloud Functions now supports the [Python 3.12](https://docs.cloud.google.com/functions/docs/concepts/python-runtime) runtime at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## October 11, 2023

Feature

Cloud Functions (2nd gen) now supports [Shared VPC ingress](https://docs.cloud.google.com/functions/docs/networking/network-settings#ingress_settings) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages). Shared VPC traffic is now considered "internal" for functions that are connected to the Shared VPC network.

## September 07, 2023

Feature

Cloud Functions now supports the [Go 1.21](https://docs.cloud.google.com/functions/docs/concepts/go-runtime) runtime at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## August 29, 2023

Change

Cloud Functions (2nd gen) is now the default choice in the Google Cloud console user interface.

## August 16, 2023

Feature

Cloud Functions now supports [pre-deployment testing](https://docs.cloud.google.com/functions/docs/running/predeploy-test) in the Google Cloud console at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## August 14, 2023

Feature

Cloud Functions now supports the [Go 1.21](https://docs.cloud.google.com/functions/docs/concepts/go-runtime) runtime at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## August 07, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/functions/docs/networking/network-settings#ingress_settings) now results in a `404` rather than `403` error code.

## July 31, 2023

Feature

The following new regions are now available: `europe-southwest1`, `europe-west8`, `europe-west9`, `us-south1`, and `us-east5`. See [Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## June 27, 2023

Change

Cloud Functions now supports [performance recommendations](https://docs.cloud.google.com/functions/docs/configuring/recommender) that analyze cold starts and suggest setting up minimum instances to improve function performance at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## June 26, 2023

Feature

The [Node.js 20 runtime](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime) is now available for Google Cloud Functions at the [GA release level](https://cloud.google.com/products#product-launch-stages). Note that Node.js 20 will enter long-term support (LTS) in October and is the Node.js "Current" release until then. The Node.js community encourages you to explore the new features and benefits included in this release. For more information, see the [Node.js 20 announcement](https://nodejs.org/en/blog/announcements/v20-release-announce).

## June 23, 2023

Feature

The Java runtime now supports projects that use [Maven wrappers](https://docs.cloud.google.com/functions/docs/writing/specifying-dependencies-java#declaring_and_managing_dependencies).

## June 16, 2023

Feature

Cloud Functions 2nd gen now supports [deterministic URLs](https://docs.cloud.google.com/functions/docs/calling/http#url) (similar to 1st gen), at the [General Availability release level](https://cloud.google.com/products#product-launch-stages). This change will not just affect new 2nd gen functions. Previously deployed 2nd gen functions will be retroactively assigned a deterministic `cloudfunctions.net` URL. The function's previous `run.app` URL will continue to work also. If your 2nd gen function was last deployed before June 15th, 2023, be sure to redeploy it before using `cloudfunctions.net` URL as an [auth token audience](https://docs.cloud.google.com/run/docs/configuring/custom-audiences).

## June 14, 2023

Change

Cloud Functions now supports [customer-managed encryption keys](https://docs.cloud.google.com/functions/docs/securing/cmek) for 2nd gen functions at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## June 09, 2023

Feature

You can now create and then [configure Serverless VPC Access connector](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#configuring) for your function directly from the _Create_ form in the Google Cloud console at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## June 01, 2023

Feature

You can use the [Pnpm](https://pnpm.io/installation) package manager to configure dependencies for Node.js runtimes. [Learn how to configure your runtime](https://docs.cloud.google.com/functions/docs/writing/specifying-dependencies-nodejs#configuring_deployment_dependencies).

## May 16, 2023

Feature

You can now [restrict new deployments by product generation](https://docs.cloud.google.com/functions/docs/securing/gen-org-policy) (1st gen or 2nd gen). This feature is at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## May 15, 2023

Feature

Cloud Functions has added support for a new runtime, [PHP 8.2](https://docs.cloud.google.com/functions/docs/concepts/php-runtime), at the [General Availability release level](https://cloud.google.com/products#product-launch-stages). PHP 8.2 adds significant new functionality over PHP 8.1 and uses Ubuntu 22.04 for its base O/S image.

Feature

Cloud Functions now supports [2nd gen Firestore triggers](https://docs.cloud.google.com/functions/docs/calling/cloud-firestore) through Eventarc at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## May 08, 2023

Feature

Cloud Functions now supports the [Node.js 20](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime) runtime at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## April 20, 2023

Change

There is a change in retry policy for 1st gen functions that use Pub/Sub subscriptions. Newly created 1st gen functions with "retry on failure" enabled will now use exponential backoff, configured with a minimum backoff of 10 seconds and a maximum backoff of 600 seconds. This new policy replaces the old "retry immediately" policy. This policy is applied to new 1st gen functions the first time you deploy them. It is not retroactively applied to existing functions, even if you redeploy them. 2nd gen functions will continue to use an exponential backoff strategy. For details, see [Retrying event-driven functions](https://docs.cloud.google.com/functions/docs/bestpractices/retries).

## April 18, 2023

Feature

Cloud Functions (2nd gen) has added support at the [Preview release level](https://cloud.google.com/products#product-launch-stages) for accepting requests from the Shared VPC network that a function is [connected to](https://docs.cloud.google.com/functions/docs/networking/connecting-shared-vpc), including when [Ingress](https://docs.cloud.google.com/functions/docs/networking/network-settings#ingress_settings) is configured as "Internal" or "Internal and Cloud Load Balancing."

## April 11, 2023

Breaking

All 1st and 2nd gen Google Cloud Functions using the [Node.js runtime](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime) now automatically run the `npm run build` command during deployment if they define an npm `build` script in their `package.json` file. This feature is rolling out over the next few days.

**Important** : If you prefer to prevent your build from running the `npm run build` script, you can either:

  * Add a `gcp-build` script with an empty value in your `package.json` file: `"gcp-build":""`

  * Set the environment variable `GOOGLE_NODE_RUN_SCRIPTS` to the empty string to prevent all scripts from running -- for example, by including the [`--set-build-env-vars=GOOGLE_NODE_RUN_SCRIPTS=""`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--set-build-env-vars) option with your `gcloud functions deploy` command.




For details about configuring `package.json`, see [Node.js buildpack configuration](https://docs.cloud.google.com/docs/buildpacks/nodejs#google_node_run_scripts). For details about setting environment variables see [setting environment variables](https://docs.cloud.google.com/docs/buildpacks/set-environment-variables).

## April 06, 2023

Feature

Cloud Functions now supports the use of the [Yarn 2 package manager](https://docs.cloud.google.com/docs/buildpacks/nodejs) with private Node.js modules.

## April 04, 2023

Change

You can now use uppercase letters and underscores in the function name you specify for a 2nd gen function when you [deploy](https://docs.cloud.google.com/functions/docs/deploy#basics) the function.

## April 03, 2023

Feature

Cloud Functions has added support for a new runtime, [PHP 8.2](https://docs.cloud.google.com/functions/docs/concepts/php-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## March 27, 2023

Feature

Cloud Functions has added support for a new runtime, [Go 1.20](https://docs.cloud.google.com/functions/docs/concepts/go-runtime), at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## March 17, 2023

Feature

Cloud Functions has added support for [customer-managed encryption keys](https://docs.cloud.google.com/functions/docs/securing/cmek) for 2nd gen functions at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## February 28, 2023

Feature

Cloud Functions now supports the [Python 3.11](https://docs.cloud.google.com/functions/docs/concepts/python-runtime) runtime at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## February 27, 2023

Feature

New [performance recommendations](https://docs.cloud.google.com/functions/docs/configuring/recommender) are supported for Cloud Functions, which analyze cold starts and suggest setting up minimum instances to improve function performance. At the [Preview release level](https://cloud.google.com/products#product-launch-stages).

Feature

Cloud Functions has added support for a new runtime, [Ruby 3.2](https://docs.cloud.google.com/functions/docs/concepts/ruby-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## February 13, 2023

Feature

Cloud Functions has added support for a new runtime, [Go 1.20](https://docs.cloud.google.com/functions/docs/concepts/go-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## January 30, 2023

Change

We've added support dates for language runtimes that have reached end of support from their open source communities. Please refer to the [Runtimes Support Schedule](https://docs.cloud.google.com/functions/docs/runtime-support) for future updates to runtime languages

## January 18, 2023

Feature

The ability to optionally configure 2nd gen functions with user-specified [concurrency](https://docs.cloud.google.com/functions/docs/configuring/concurrency#set-concurrency-gcf) and [vCPU](https://docs.cloud.google.com/functions/docs/configuring/memory#set-vcpu) is now available in preview.

Feature

Cloud Functions now supports the [Node.js 18](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime) runtime at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## January 10, 2023

Feature

Cloud Functions has added support for a new runtime, [Python 3.11](https://docs.cloud.google.com/functions/docs/concepts/python-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## January 06, 2023

Feature

Cloud Functions now supports the following runtimes at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

  * [Go 1.18](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)
  * [Go 1.19](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)



## December 21, 2022

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#update-connector) is now available in preview. This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## December 13, 2022

Feature

The `cloudfunctions.googleapis.com/v2` API now supports reading 1st gen functions, using the [get](https://docs.cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions/get) and [list](https://docs.cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions/list) methods. Function responses contain an [Environment](https://docs.cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions#Environment) field that differentiates between 1st and 2nd gen functions. 

You can use the [filter](https://docs.cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions/list#query-parameters) field to restrict the response to only 2nd gen functions, for example: `filter=environment="GEN_2"`. 

Note that 1st gen functions in `europe-west5` can't be read from the v2 API as the region is not available yet in 2nd gen.

If you are using an older version of gcloud, the `gcloud functions list` command may show 1st gen functions twice. Updating to a newer version of gcloud should fix this.

## November 22, 2022

Feature

Cloud Functions has added support for a new runtime, [Node.js 18](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## November 14, 2022

Announcement

Cloud Functions container runtimes have been patched against CVE-2022-3786 and CVE-2022-3602. Affected runtime languages are:

  * Java 17
  * Python 3.10
  * Go 1.18/1.19
  * .NET 6



You should redeploy functions using the affected runtime languages as soon as possible. Google does not automatically update the base image in use for already-deployed functions. Google will automatically apply the most updated runtime version to the redeployed function.

## November 08, 2022

Change

Cloud Functions has added support for the following new runtimes at the [Preview release level](https://cloud.google.com/products#product-launch-stages):

  * [Go 1.18](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)
  * [Go 1.19](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)



## October 24, 2022

Change

Cloud Functions now supports the [.NET Core 6.0](https://docs.cloud.google.com/functions/docs/concepts/dotnet-runtime) runtime at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## September 12, 2022

Feature

Cloud Functions has added support for a new runtime, [.NET Core 6.0](https://docs.cloud.google.com/functions/docs/concepts/dotnet-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## August 03, 2022

Change

Cloud Functions has released Cloud Functions (2nd gen), available at the [General Availability release level](https://cloud.google.com/products#product-launch-stages). Cloud Functions (2nd gen) is Google Cloud's next-generation Functions-as-a-Service offering. This new version of Cloud Functions comes with an advanced feature set, giving you more powerful infrastructure, advanced control over performance and scalability, more control around the functions runtime, and triggers from over 90 event sources.

See [Cloud Functions version comparison](https://docs.cloud.google.com/functions/docs/concepts/version-comparison) for details.

## July 06, 2022

Change

Cloud Functions (1st gen) now supports [Google-managed Artifact Registry](https://docs.cloud.google.com/functions/docs/building#image_registry_options) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

Change

Cloud Functions now supports the following runtimes at the [General Availability release level](https://cloud.google.com/products#product-launch-stages):

  * [Python 3.10](https://docs.cloud.google.com/functions/docs/concepts/python-runtime)
  * [PHP 8.1](https://docs.cloud.google.com/functions/docs/concepts/php-runtime)



## July 01, 2022

Change

Cloud Functions now supports [PHP 8.1](https://docs.cloud.google.com/functions/docs/concepts/php-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## June 30, 2022

Change

Cloud Functions now supports [Python 3.10](https://docs.cloud.google.com/functions/docs/concepts/python-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## June 27, 2022

Change

Cloud Functions now supports [Java 17](https://docs.cloud.google.com/functions/docs/concepts/java-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## June 14, 2022

Change

The Python 3.10 runtime (preview) now uses [Ubuntu 22](https://docs.cloud.google.com/functions/docs/concepts/python-runtime#execution_environment).

## June 06, 2022

Change

The Java 17 runtime (preview) now uses [Ubuntu 22](https://docs.cloud.google.com/functions/docs/concepts/java-runtime#execution_environment).

## May 25, 2022

Announcement

We have updated the [documentation](https://docs.cloud.google.com/functions/docs/concepts/exec#runtimes) to clarify that to get the updates and security patches for runtimes and their dependencies, you need to deploy a function. Security patches are not applied otherwise.

## May 04, 2022

Change

Cloud Functions now supports [Ruby 3.0](https://docs.cloud.google.com/functions/docs/concepts/ruby-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## May 03, 2022

Feature

Cloud Functions has added support for the following new runtimes at the [Preview release level](https://cloud.google.com/products#product-launch-stages):

  * [Python 3.10](https://docs.cloud.google.com/functions/docs/concepts/python-runtime)
  * [PHP 8.1](https://docs.cloud.google.com/functions/docs/concepts/php-runtime)



## April 01, 2022

Feature

Cloud Functions (1st gen) has added support for [Google-managed Artifact Registry](https://docs.cloud.google.com/functions/docs/building#image_registry_options) at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## March 31, 2022

Change

Cloud Functions (1st gen) support for [customer-managed encryption keys](https://docs.cloud.google.com/functions/docs/securing/cmek) (CMEK) is now at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## March 24, 2022

Feature

Support for Serverless VPC Access connectors in Shared VPC host projects is now at the [General Availability release level](https://cloud.google.com/products#product-launch-stages). Learn about the [advantages](https://docs.cloud.google.com/functions/docs/networking/connecting-shared-vpc#host-project) of this method and how to [configure connectors in host projects](https://docs.cloud.google.com/functions/docs/networking/shared-vpc-host-project).

## March 21, 2022

Feature

Support for [Firebase Remote Config, Firebase Alerts, and Firebase Test Lab triggers](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source) is now in [Preview](https://cloud.google.com/products#product-launch-stages). This only applies to Cloud Functions (2nd gen).

## March 14, 2022

Feature

Cloud Functions has added support for the following new runtimes at the [Preview release level](https://cloud.google.com/products#product-launch-stages):

  * [Java 17](https://docs.cloud.google.com/functions/docs/concepts/java-runtime)
  * [Ruby 3.0](https://docs.cloud.google.com/functions/docs/concepts/ruby-runtime)



## March 07, 2022

Feature

Added [Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function) support for [Cloud Functions (2nd gen)](https://docs.cloud.google.com/functions/docs/2nd-gen).

## February 16, 2022

Feature

Cloud Functions has added support for low-configuration access to private dependencies on Artifact Registry in in [Node.js](https://docs.cloud.google.com/functions/docs/writing/specifying-dependencies-nodejs#using_private_modules) and [Python](https://docs.cloud.google.com/functions/docs/writing/specifying-dependencies-python#using_private_dependencies).

## February 14, 2022

Feature

Cloud Functions has released Cloud Functions (2nd gen), available at the [Preview release level](https://cloud.google.com/products#product-launch-stages). Cloud Functions (2nd gen) is Google Cloud's next-generation Functions-as-a-Service offering. This new version of Cloud Functions comes with an advanced feature set, giving you more powerful infrastructure, advanced control over performance and scalability, more control around the functions runtime, and triggers from over 90 event sources.

See the [Cloud Functions (2nd gen) documentation](https://docs.cloud.google.com/functions/docs/2nd-gen) for details.

## January 25, 2022

Change

Cloud Functions support for [secrets](https://docs.cloud.google.com/functions/docs/configuring/secrets) is now at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## December 08, 2021

Feature

Cloud Functions has added support for [customer-managed encryption keys](https://docs.cloud.google.com/functions/docs/securing/cmek), available at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## December 07, 2021

Change

Cloud Functions support for [setting a minimum number of instances](https://docs.cloud.google.com/functions/docs/configuring/min-instances) is now at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## December 02, 2021

Feature

[Internal ingress from Workflows](https://docs.cloud.google.com/workflows/docs/calling-run-functions#internal_ingress) to Cloud Functions is now at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## November 22, 2021

Feature

Cloud Functions is now available in the following region:

`us-west1` (Oregon)

See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## November 17, 2021

Change

Cloud Functions now supports the following runtimes at the [General Availability release level](https://cloud.google.com/products#product-launch-stages):

  * [Node.js 16](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime)
  * [Go 1.16](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)



## September 15, 2021

Change

Cloud Functions now supports [PHP 7.4 ](https://docs.cloud.google.com/functions/docs/concepts/php-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## September 09, 2021

Change

[Firestore triggers for Cloud Functions](https://docs.cloud.google.com/functions/docs/calling/cloud-firestore) are now supported at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## September 03, 2021

Feature

Cloud Functions has added support for a new runtime, [Go 1.16](https://docs.cloud.google.com/functions/docs/concepts/go-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## August 30, 2021

Feature

Cloud Functions adds support for [setting a minimum number of instances](https://docs.cloud.google.com/functions/docs/configuring/min-instances), available at the [Preview release level](https://cloud.google.com/products#product-launch-stages). For more information, see the [blog post](https://cloud.google.com/blog/products/serverless/cloud-functions-supports-min-instances).

## August 26, 2021

Feature

Cloud Functions has added support for a new runtime, [Node 16](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime), at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

## August 24, 2021

Feature

Cloud Functions offers a native integration with [Secret Manager](https://docs.cloud.google.com/functions/docs/configuring/secrets), available at the [Preview release level](https://cloud.google.com/products#product-launch-stages). For more information, see the [blog post](https://cloud.google.com/blog/products/serverless/cloud-functions-integrates-with-google-secret-manager).

## August 10, 2021

Feature

The use of [private worker pools](https://docs.cloud.google.com/functions/docs/building#securing_your_build_with_private_pools) is now available for building your functions.

## July 07, 2021

Feature

Cloud Functions now logs [pending queue requests abort](https://docs.cloud.google.com/functions/docs/troubleshooting#scalability) error messages.

## July 02, 2021

Change

Cloud Functions now supports [.NET](https://docs.cloud.google.com/functions/docs/concepts/dotnet-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages). This runtime is based on .NET Core 3.1.

## June 28, 2021

Feature

Cloud Functions is now available in the following region:

`asia-east1` (Taiwan)

See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## June 14, 2021

Feature

Cloud Functions is now available in the following region:

  * `asia-southeast1` (Singapore)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## June 07, 2021

Change

Cloud Functions now supports [Ruby 2.6 and 2.7](https://docs.cloud.google.com/functions/docs/concepts/ruby-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## April 19, 2021

Change

Cloud Functions now supports the following runtimes at the [General Availability release level](https://cloud.google.com/products#product-launch-stages):

  * [Node.js 14](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime)
  * [Python 3.9](https://docs.cloud.google.com/functions/docs/concepts/python-runtime)



Feature

Cloud Functions has added support for a new runtime, [PHP 7.4](https://docs.cloud.google.com/functions/docs/concepts/php-runtime), in Preview.

## April 12, 2021

Feature

Cloud Functions is now available in the following region:

  * `europe-central2` (Warsaw)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## March 18, 2021

Change

[Shared VPC on Cloud Functions](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) is now at general availability (GA).

## February 04, 2021

Feature

There is now a [security level feature](https://docs.cloud.google.com/functions/docs/writing/http#security_levels) for HTTP functions that controls whether the function's URL supports HTTPS only, or both HTTP and HTTPS.

## January 13, 2021

Feature

Cloud Functions has added support for a new runtime, [Node 14](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime), in Preview.

Cloud Functions has added support for a new runtime, [Python 3.9](https://docs.cloud.google.com/functions/docs/concepts/python-runtime), in Preview.

## January 11, 2021

Feature

Cloud Functions has added support for a new runtime, Ruby, in Preview. This runtime supports Ruby 2.6 and Ruby 2.7.

  * [The Ruby Runtime](https://docs.cloud.google.com/functions/docs/concepts/ruby-runtime)
  * [Blog post](https://cloud.google.com/blog/products/application-development/ruby-comes-to-cloud-functions)



## November 19, 2020

Feature

Cloud Functions has added support for a new runtime, .NET, in Preview. This runtime is based on .NET Core 3.1.

  * [The .NET runtime](https://docs.cloud.google.com/functions/docs/concepts/dotnet-runtime)
  * [Blog post](https://cloud.google.com/blog/products/application-development/introducing-net-google-cloud-functions)



## November 16, 2020

Change

Cloud Functions now supports [Node.js 12](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## November 11, 2020

Change

Cloud Functions now supports [Python 3.8](https://docs.cloud.google.com/functions/docs/concepts/python-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## October 13, 2020

Feature

In runtimes that use buildpacks you can now configure aspects of your build by setting build configuration variables. See [Using Environment Variables](https://docs.cloud.google.com/functions/docs/env-var) for more information. In Preview.

## August 26, 2020

Change

Cloud Functions Node 10 runtime now builds container images in the user's project, providing direct access to build logs and removing the preset build-time quota.

## August 14, 2020

Change

Cloud Functions now supports [Java 11](https://docs.cloud.google.com/functions/docs/concepts/java-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## August 05, 2020

Deprecated

The Go 1.11 runtime is deprecated as of 2020-08-05. To ensure that your functions are on a supported version of Go, migrate them to [Go 1.13](https://docs.cloud.google.com/functions/docs/concepts/go-runtime). For more discussion of Cloud Functions runtime support policy, see [Runtime Support](https://docs.cloud.google.com/functions/docs/runtime-support).

Feature

Cloud Functions Java 11, Python 3.7 or 3.8, and Go 1.13 runtimes now build container images in the user's project, providing direct access to build logs and removing the preset build-time quota. 

See [Building Cloud Functions](https://docs.cloud.google.com/functions/docs/building) for details.

## July 31, 2020

Feature

Cloud Functions is now available in the following regions:

  * `asia-south1` (Mumbai)
  * `asia-southeast2` (Jakarta)
  * `asia-northeast3` (Seoul)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## July 23, 2020

Feature

[Serverless VPC Access support for Shared VPC](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc#shared-vpc) is now available in Beta.

## July 15, 2020

Feature

Cloud Functions has added support for a new runtime, [Node 12](https://docs.cloud.google.com/functions/docs/concepts/nodejs-runtime), in Beta.

Cloud Functions has added support for a new runtime, [Python 3.8](https://docs.cloud.google.com/functions/docs/concepts/python-runtime), in Beta.

## July 10, 2020

Feature

Cloud Functions is now available in the following regions:

  * `us-west2` (Los Angeles)
  * `us-west4`
  * `southamerica-east1` (Sao Paulo)
  * `asia-northeast2` (Osaka)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## July 07, 2020

Feature

External HTTP(S) Load Balancing is now supported for Google Cloud Functions via [Serverless network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-serverless-negs).

Notably, this feature allows you to use [Cloud CDN](https://cloud.google.com/cdn) and [Cloud Armor](https://cloud.google.com/security/products/armor) with Google Cloud Functions.

This feature is available in Beta.

## June 19, 2020

Feature

Cloud Functions is now available in the following regions:

  * `australia-southeast1` (Sydney)
  * `northamerica-northeast1` (Montreal)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## June 12, 2020

Feature

Cloud Functions is now available in the following regions:

  * `europe-west6` (Zurich)
  * `us-west3` (Salt Lake City)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## June 05, 2020

Deprecated

The Node.js 8 runtime is deprecated as of 2020-06-05. To ensure that your functions are on a supported version of Node.js, migrate them to [Node.js 10](https://docs.cloud.google.com/functions/docs/concepts/nodejs-10-runtime).

For more discussion of Cloud Functions runtime support policy, see [Runtime Support](https://docs.cloud.google.com/functions/docs/runtime-support).

## May 28, 2020

Change

Cloud Functions now supports [Go 1.13](https://docs.cloud.google.com/functions/docs/concepts/go-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## May 26, 2020

Feature

Cloud Functions has added support for a new runtime, Java 11, in Beta:

  * [The Java Runtime](https://docs.cloud.google.com/functions/docs/concepts/java-runtime)



## May 18, 2020

Change

Cloud Functions now supports [Node.js 10](https://docs.cloud.google.com/functions/docs/concepts/nodejs-10-runtime) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## March 31, 2020

Change

Cloud Functions now supports [Connecting to Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/connect-functions) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

  * The Beta release introduced improved security when accessing Cloud SQL from functions via the `/cloudsql` filesystem path. Most functions have been automatically upgraded. In some cases, you may see warning messages in Stackdriver logging to help you complete the required upgrade steps.



## March 24, 2020

Change

Cloud Functions now supports [VPC Service Controls](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

Change

Cloud Functions now supports [network settings](https://docs.cloud.google.com/functions/docs/networking/network-settings) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## February 13, 2020

Change

HTTP functions now require authentication by default. See [Managing Access via IAM](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam) for details.

## January 31, 2020

Feature

Cloud Functions has added the [network settings](https://docs.cloud.google.com/functions/docs/networking/network-settings) feature at the [Beta release level](https://cloud.google.com/products#product-launch-stages). Network settings enable you to control network ingress and egress on individual functions.

Feature

Cloud Functions now supports [VPC Service Controls](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls) at the [Beta release level](https://cloud.google.com/products#product-launch-stages). VPC Service Controls is a feature that allows you to set up a secure perimeter to guard against data exfiltration.

## January 29, 2020

Feature

Cloud Functions is now available in the following region:

  * `europe-west3` (Frankfurt)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## January 14, 2020

Feature

Cloud Functions has added support for a new runtime, Go 1.13, in Beta:

  * [The Go Runtime](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)



## December 11, 2019

Change

Cloud Functions now supports [Serverless VPC Access](https://docs.cloud.google.com/functions/docs/connecting-vpc) at the [General Availability release level](https://cloud.google.com/products#product-launch-stages).

## November 26, 2019

Change

The [`ListFunctions`](https://docs.cloud.google.com/functions/docs/reference/rpc/google.cloud.functions.v1#google.cloud.functions.v1.CloudFunctionsService.ListFunctions) API method now handles unreachable locations when the specified location is `"-"` to list functions across all locations. Previously, if one or more locations were unreachable, the entire `ListFunctions` request would fail. Now the request will return functions from all reachable locations along with an "unreachable" field containing a list of location names that did not respond successfully. Learn more about working with [unreachable resources](https://aip.dev/217).

## November 12, 2019

Change

Cloud Functions now supports [IAM](https://docs.cloud.google.com/iam) policies to [control access to HTTP functions](https://docs.cloud.google.com/functions/docs/securing) at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## October 14, 2019

Change

The max instances feature is now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels):

  * [Controlling Scaling Behavior](https://docs.cloud.google.com/functions/docs/max-instances)
  * Note that when you have set a max instances limit, you may encounter a scenario where there are insufficient instances to meet incoming traffic load. Requests that time out due to unavailability of instances send a [429 response](https://docs.cloud.google.com/functions/docs/max-instances#request_handling_when_all_instances_are_busy).



## July 01, 2019

Feature

Cloud Functions is now available in the following region:

  * `us-east4` (Northern Virginia)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## June 26, 2019

Feature

Cloud Functions now supports [IAM](https://docs.cloud.google.com/iam) policies to [control access to HTTP functions](https://docs.cloud.google.com/functions/docs/securing) in beta. During beta, functions will be deployed publicly and you can restrict access by setting IAM policies.

## June 06, 2019

Deprecated

With the end-of-life of Node 6, the [Cloud Functions Local Emulator](https://github.com/googlearchive/cloud-functions-emulator) tool for Google Cloud Functions for Node 6 is no longer being maintained and is marked as deprecated. Use the [Functions Framework](https://docs.cloud.google.com/functions/docs/functions-framework) to run a function locally.

## April 19, 2019

Change

Completed rollout of update to the Go Cloud Functions runtime. Go has been updated from version 1.11.5 to 1.11.6. All function deployments should get this version automatically.

## April 18, 2019

Deprecated

The Node.js 6 runtime is deprecated as of 2019-04-18. On 2019-04-30, Node.js 6 will reach its [end-of-life](https://github.com/nodejs/Release) and will no longer receive updates from the Node.js maintainers. To ensure that your functions are on a supported version of Node.js, migrate them to [Node.js 8 or Node.js 10](https://docs.cloud.google.com/functions/docs/migrating/nodejs-runtimes). After 2020-04-22, function deployments that use Node.js 6 will be blocked. Cloud Functions that continue to use Node.js 6 after this time may be disabled.

For more discussion of Cloud Functions runtime support policy, see [Runtime Support](https://docs.cloud.google.com/functions/docs/runtime-support).

## April 09, 2019

Feature

Cloud Functions now supports [Serverless VPC Access](https://docs.cloud.google.com/functions/docs/connecting-vpc), which is available at the [Beta release level](https://cloud.google.com/products#product-launch-stages). This feature enables your functions to connect to internal resources in your VPC network, such as Compute Engine VM instances, Cloud Memorystore for Redis instances, and more.

## April 04, 2019

Change

Now when you deploy a function for the first time using the `gcloud` command-line tool or the API, you must specify your function's runtime explicitly. If you are using `gcloud`, include the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag. If you are using the API, set the `runtime` field when creating a [`CloudFunction`](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#CloudFunction). You do not need to specify the runtime on subsequent function deployments.

## April 03, 2019

Feature

Cloud Functions has added support for a new runtime, Node.js 10, in Beta:

  * [The Node.js 10 Runtime](https://docs.cloud.google.com/functions/docs/concepts/nodejs-10-runtime)



## April 01, 2019

Change

  * Cloud Functions is now available in 2 new regions. See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details:

  * `europe-west2` (London)

  * `asia-east2` (Hong Kong)




Change

Made the following changes:

  * The following runtimes are now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels):

  * [Node.js 8 runtime](https://docs.cloud.google.com/functions/docs/concepts/nodejs-8-runtime)

  * [Python 3.7 runtime](https://docs.cloud.google.com/functions/docs/concepts/python-runtime)

  * [Go 1.11 runtime](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)




## March 29, 2019

Change

Completed rollout of update to the Go Cloud Functions runtime. Go has been updated from version 1.11 to 1.11.5. All function deployments should get this version automatically.

## March 28, 2019

Feature

The [max instances](https://docs.cloud.google.com/functions/docs/max-instances) feature is now at [Beta Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels). This feature allows you to limit the degree to which your function scales up in response to inbound request load.

## March 22, 2019

Fixed

Fixed an issue where events would no longer be delivered to a background function if the function hadn't been triggered at least once in the last 30 days. This fix will be automatically applied to any new functions. The fix will be applied to existing functions upon re-deployment.

## February 27, 2019

Change

  * The `requests` package installed for Python functions was upgraded from 2.19.1 to 2.21.0.



Change

Made the following changes:

  * The default function calls quota has been raised to 40,000,000 in all regions.



## February 20, 2019

Change

Completed rollout of update to the Node.js 6 Cloud Functions runtime. Node.js 6 has been updated from version 6.14.0 to 6.16.0.

## February 14, 2019

Fixed

Fixed an issue where functions would, under some circumstances, be triggered multiple times when a single event was delivered. Note that event delivery follows an [at least once guarantee](https://docs.cloud.google.com/functions/docs/concepts/events-triggers#triggers), which means that, rarely, event re-delivery can occur.

## February 06, 2019

Change

Started rolling out an update of the Node.js 6 runtime to version 6.16.0. Node.js 6 functions deployed after February 4, 2019 may start to receive the updated version.

Change

Completed rollout of update to the Node.js 8 Cloud Functions runtime. Node.js 8 has been updated from version 8.14.0 to 8.15.0.

## January 16, 2019

Feature

Cloud Functions has added support for a new runtime, Go, in Beta:

  * [The Go Runtime](https://docs.cloud.google.com/functions/docs/concepts/go-runtime)



## January 15, 2019

Change

Started rolling out an update of the Node.js 8 runtime to version 8.15.0. Node.js 8 functions deployed after January 14, 2019 might start to use the updated version.

## December 20, 2018

Change

Completed rollout of update to the Node.js 8 Cloud Functions runtime. Node.js 8 has been updated from version 8.11.1 to 8.14.0. The update of Node.js 6 from version 6.14.0 to 6.15.0 has been rolled back. Node.js 6 is still at 6.14.0, and now won't be updated until January 2019.

## December 17, 2018

Change

Started a gradual rollout of updates to the Node.js 6 and Node.js 8 Cloud Functions runtimes. Node.js 6 will be updated from version 6.14.0 to 6.15.0. Node.js 8 will be updated from version 8.11.1 to 8.14.0. We will update the status in the release notes when the rollout has completed.

## December 04, 2018

Change

The environment variables feature is now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels):

  * [Using Environment Variables](https://docs.cloud.google.com/functions/docs/env-var)



## November 06, 2018

Change

The Google Cloud Functions Python runtime has been updated to version 3.7.1.

## July 24, 2018

Feature

  * The Cloud Functions `gcloud` commands are now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels). The `beta` label is no longer required (unless you are deploying a function written in Node.js 8 or Python, which are Beta features).



Feature

  * Support for new runtimes: Node.js 8 and Python, in Beta.



Feature

Cloud Functions is now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels) and is recommended for production loads. This release includes:

## July 12, 2018

Feature

Launched the environment variables feature to open beta:

  * [Using Environment Variables](https://docs.cloud.google.com/functions/docs/env-var)



## June 21, 2018

Feature

Added documentation describing how to connect to Cloud SQL:

  * [Connecting to Cloud SQL](https://docs.cloud.google.com/functions/docs/sql)



## June 20, 2018

Feature

Cloud Functions is now available in the following regions:

  * `us-central1` (Iowa)
  * `us-east1` (South Carolina)
  * `europe-west1` (Belgium)
  * `asia-northeast1` (Tokyo)



See [Cloud Functions Locations](https://docs.cloud.google.com/functions/docs/locations) for details.

## June 07, 2018

Deprecated

The v1beta2 version of the Cloud Functions API was part of our Beta launch. New users should use the v1 API, and existing users should [migrate](https://docs.cloud.google.com/functions/docs/migrating) to the v1 API.

## May 15, 2018

Change

Google Cloud Functions Node.js runtime updated to v6.14.0.

## February 09, 2018

Feature

Added documentation describing best practices for testing and deploying Cloud Functions:

  * [Testing and CI/CD](https://docs.cloud.google.com/functions/docs/bestpractices/testing)



Change

Introduced a set of more powerful, finer-grained trigger types for Cloud Storage and changed the format for Cloud Storage and Cloud Pub/Sub events. For details, see [Google Cloud Storage Triggers](https://docs.cloud.google.com/functions/docs/calling/storage) and [Google Cloud Pub/Sub Triggers](https://docs.cloud.google.com/functions/docs/calling/pubsub).

## January 05, 2018

Feature

Added documentation describing the Cloud Functions execution environment:

  * [Execution Environment](https://docs.cloud.google.com/functions/docs/concepts/exec)



## December 22, 2017

Feature

Added documentation describing best practices for designing, implementing, testing, and deploying Cloud Functions:

  * [Tips & Tricks](https://docs.cloud.google.com/functions/docs/bestpractices/tips)



## November 09, 2017

Change

Google Cloud Functions Node.js runtime updated to v6.11.5.

## November 07, 2017

Feature

Added documentation on optimizing networking, which reduces the likelihood that you will run out of DNS or connection quotas:

  * [Optimizing Networking](https://docs.cloud.google.com/functions/docs/writing/networking)



## October 30, 2017

Feature

Added documentation on how to retry background functions:

  * [Retrying Background Functions](https://docs.cloud.google.com/functions/docs/writing/retries)



## October 19, 2017

Feature

Released Google Cloud Functions v1 API: [API Reference](https://docs.cloud.google.com/functions/docs/apis).

## July 17, 2017

Change

Google Cloud Functions Node.js runtime updated to v6.11.1.

## May 16, 2017

Feature

Added ImageMagick tutorial:

  * [ImageMagick tutorial](https://docs.cloud.google.com/functions/docs/tutorials/imagemagick)



## May 09, 2017

Feature

Added Cloud Spanner tutorial:

  * [Using Cloud Spanner with Cloud Functions](https://docs.cloud.google.com/functions/docs/tutorials/use-cloud-spanner)



## March 21, 2017

Feature

Added support page and supported services document:

  * [Support & Community](https://docs.cloud.google.com/functions/docs/support)

  * [Supported Services](https://docs.cloud.google.com/functions/docs/concepts/services)




## March 09, 2017

Feature

**Beta release** of Google Cloud Functions.

Feature

Added new guides:

  * [Events and Triggers](https://docs.cloud.google.com/functions/docs/concepts/events-triggers)

  * [Access Control](https://docs.cloud.google.com/functions/docs/concepts/iam)

  * [Cloud Functions Local Emulator](https://docs.cloud.google.com/functions/docs/emulator)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
