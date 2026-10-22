---
url: https://docs.cloud.google.com/deploy/docs/release-notes/
title: Cloud Deploy release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:26.973516+00:00
---

# Cloud Deploy release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Resources ](https://docs.cloud.google.com/deploy/docs/resources)



Send feedback 

#  Cloud Deploy release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Deploy. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/clouddeploy-release-notes.xml) directly. 

## July 10, 2026

Change

The Cloud Deploy image now uses a Google-specific fork of Skaffold. The Skaffold version that you see if you run `gcloud deploy releases describe`, or if you view the release in the Google Cloud Console, is now `cd-skaffold` instead of a version number.

## June 15, 2026

Change

The Cloud Deploy image now uses Kubectl Kustomize.

By default, Cloud Deploy now uses the [Kustomize built into kubectl](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kustomize/). Previously, the default version of Kustomize was the version embedded in the Cloud Deploy image. Now it's the version used by kubectl.

You can still use kustomize directly (not through kubectl) by specifying the kustomize version when you create a release.

## April 14, 2026

Change

Support for [deploying Cloud Run worker pools](https://docs.cloud.google.com/deploy/docs/run-targets) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 23, 2026

Feature

You can now [analyze the performance of your deployed applications](https://docs.cloud.google.com/deploy/docs/analysis) using the monitoring platform of your choice and [automatically trigger actions](https://docs.cloud.google.com/deploy/docs/automation-rules) such as rollbacks. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

Feature

You can now provide user-defined actions using [`tasks`](https://docs.cloud.google.com/deploy/docs/tasks). This includes [deploy hooks](https://docs.cloud.google.com/deploy/docs/hooks), [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment), [analysis](https://docs.cloud.google.com/deploy/docs/analysis), and [custom target types](https://docs.cloud.google.com/deploy/docs/custom-targets). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

## March 02, 2026

Feature

Cloud Deploy is now available in the following region: asia-southeast3 (Bangkok)

## February 11, 2026

Feature

You can now [deploy containerized workloads to Cloud Run worker pools](https://docs.cloud.google.com/deploy/docs/run-targets#create_your_worker_pool_definitions) (in [Preview](https://cloud.google.com/products#product-launch-stages)).

## January 23, 2026

Change

The limit on deployment minutes per delivery pipeline has been removed. The only quota now enforced in Cloud Deploy is the system limit of 18,000 API requests per minute per region. [Learn more](https://docs.cloud.google.com/deploy/quotas).

## December 12, 2025

Change

We now [upgrade the tools used for deployments more frequently](https://docs.cloud.google.com/deploy/docs/select-tool-version). This includes tools like Skaffold, Kubectl, and Helm. You can also [select specific versions](https://docs.cloud.google.com/deploy/docs/select-tool-version#how_select) of these tools when you create a release.

## September 02, 2025

Feature

You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud Deploy resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/deploy/docs/custom-org-policy).

## May 23, 2025

Change

Cloud Deploy now uses Skaffold 2.16 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), as of May 23, 2025, for all target types.

## March 31, 2025

Announcement

Cloud Deploy support for [timed promote](https://docs.cloud.google.com/deploy/docs/automation-rules#timedpromote_rule) is now [generally available](https://cloud.google.com/products#product-launch-stages).

Announcement

Cloud Deploy support for [deploy policies](https://docs.cloud.google.com/deploy/docs/deploy-policy) is now [generally available](https://cloud.google.com/products#product-launch-stages).

Announcement

Cloud Deploy support for [repair rollout automation](https://docs.cloud.google.com/deploy/docs/automation-rules#repairrollout_rule) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## March 26, 2025

Change

Cloud Deploy is now available in the following regions:

  * `northamerica-south1` (Mexico)
  * `europe-north2` (Stockholm)



## March 21, 2025

Change

Cloud Deploy now uses Skaffold 2.14 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), as of March 21, 2025, for all target types.

## January 13, 2025

Feature

You can now connect to your [GKE cluster's DNS-based endpoint](https://docs.cloud.google.com/blog/products/containers-kubernetes/new-dns-based-endpoint-for-the-gke-control-plane), simplifying networking configuration when talking to private clusters from Cloud Deploy. [Learn more](https://docs.cloud.google.com/deploy/docs/gke-targets#dns-based-endpoint).

## November 20, 2024

Feature

You can now [automatically promote](https://docs.cloud.google.com/deploy/docs/automation-rules#timedpromote_rule) releases across targets at scheduled times, in [preview](https://cloud.google.com/products#product-launch-stages).

## October 16, 2024

Feature

You can now automatically [retry failed rollouts, and automatically roll back](https://docs.cloud.google.com/deploy/docs/automation-rules#repairrollout_rule) to the most recent successful rollout, in [preview](https://cloud.google.com/products#product-launch-stages).

## October 10, 2024

Feature

You can now block rollouts during a specified time window, using [deploy policies](https://docs.cloud.google.com/deploy/docs/deploy-policy), in [preview](https://cloud.google.com/products#product-launch-stages).

Change

Cloud Deploy now uses Skaffold 2.13 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), as of October 4, 2024, for all target types.

## August 19, 2024

Change

Cloud Deploy is now available in the following region: `africa-south1` (Johannesburg)

## June 28, 2024

Feature

You can now [set the logging level](https://docs.cloud.google.com/deploy/docs/execution-environment#changing_log_level) to `debug`, or the equivalent, for Skaffold, gcloud, and kubectl, using the `verbose` flag in each target's execution environment.

## June 27, 2024

Feature

Cloud Deploy now supports deploying using a proxy for Google Kubernetes Engine targets. [Learn more](https://docs.cloud.google.com/deploy/docs/gke-targets#deploy_using_a_proxy).

## May 06, 2024

Change

Cloud Deploy now uses Skaffold 2.11 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions) for all target types.

## March 11, 2024

Announcement

Cloud Deploy support for [deploy automation](https://docs.cloud.google.com/deploy/docs/automation) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## March 04, 2024

Announcement

Cloud Deploy support for [custom targets](https://docs.cloud.google.com/deploy/docs/custom-targets) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## February 07, 2024

Change

Cloud Deploy now uses Skaffold 2.10 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions) for all target types.

## February 05, 2024

Change

Google Cloud Deploy is now available in the following regions:

  * me-central1 (Doha)
  * me-central2 (Dammam)
  * europe-west12 (Turin)
  * europe-west10 (Berlin)



## December 18, 2023

Feature

You can now define [custom target types](https://docs.cloud.google.com/deploy/docs/custom-targets) and deploy to targets of those types, in [preview](https://cloud.google.com/products#product-launch-stages).

Feature

You can now access [sample custom targets](https://github.com/GoogleCloudPlatform/cloud-deploy-samples/tree/main/custom-targets/), including the following:

  * Terraform
  * Infrastructure Manager
  * GitOps
  * Vertex AI
  * Helm



## December 05, 2023

Change

Google Cloud Deploy is now available in the following regions:

  * europe-southwest1 (Madrid)
  * europe-west8 (Milan)
  * europe-west9 (Paris)
  * me-west1 (Israel)
  * us-east5 (Columbus)
  * us-south1 (Dallas)



## November 16, 2023

Feature

You can now [configure alerts](https://docs.cloud.google.com/deploy/docs/alerts#available_alerts) for Cloud Deploy release render failures.

## November 13, 2023

Feature

Cloud Deploy now supports [delivery pipeline automation](https://docs.cloud.google.com/deploy/docs/automation), including automated release promotion and automated rollout phase advancement, in [preview](https://cloud.google.com/products#product-launch-stages).

## November 08, 2023

Feature

Configuring Google Cloud operations suite alerts [is now supported](https://docs.cloud.google.com/deploy/docs/alerts) in the Cloud Deploy console.

## October 30, 2023

Announcement

Cloud Deploy support for [deploy hooks](https://docs.cloud.google.com/deploy/docs/hooks) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## October 27, 2023

Change

Cloud Deploy now uses Skaffold 2.8 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions) for all target types.

## October 23, 2023

Feature

You can now [deploy Cloud Run jobs](https://docs.cloud.google.com/deploy/docs/run-targets#create_your_job_definitions), in addition to Cloud Run services.

## September 28, 2023

Issue

When you create a release using the gcloud CLI version 445, 446, or 447, you might encounter an error where gcloud requires the `clouddeploy.config.get` permission. To fix this issue, upgrade to gcloud CLI version 448 or greater.

## September 19, 2023

Announcement

Cloud Deploy now supports [workforce identity federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

## August 23, 2023

Announcement

Cloud Deploy support for [deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## August 07, 2023

Feature

You can now specify custom actions to perform before and/or after deploying, using [deploy hooks](https://docs.cloud.google.com/deploy/docs/hooks), supported in [preview](https://cloud.google.com/products#product-launch-stages).

## July 24, 2023

Feature

You can now create delivery pipelines, targets, and releases [using the Google Cloud console](https://docs.cloud.google.com/deploy/docs/deploy-app-in-console).

Feature

You can now [configure `routeUpdateWaitTime`](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#gateway) for HTTPRoute resource propagation with GKE/Anthos Gateway API canary deployment.

Change

Google Cloud Deploy now uses Skaffold 2.6 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions) for all target types.

## July 19, 2023

Announcement

Cloud Deploy has completed Google Cloud [data residency](https://cloud.google.com/terms/data-residency) requirements.

## July 17, 2023

Feature

Cloud Deploy now provides the ability to [pass deploy parameters](https://docs.cloud.google.com/deploy/docs/parameters) to your manifests, per delivery pipeline, per target, and per release (in [preview](https://cloud.google.com/products#product-launch-stages)).

## July 12, 2023

Change

Cloud Deploy now supports Skaffold version 2.6. The [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions) remains 2.3.

## June 26, 2023

Announcement

Cloud Deploy support for the [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary) is now [generally available](https://cloud.google.com/products#product-launch-stages).

Announcement

Cloud Deploy support for [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## June 22, 2023

Feature

You can now [prevent Cloud Deploy from overprovisioning GKE and Anthos pods](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#what_happens_during_an_automated_or_custom-automated_canary) during a canary deployment.

## June 07, 2023

Announcement

As of June 6, 2023, Google Cloud Deploy is ready to support [HIPAA](https://docs.cloud.google.com/security/compliance/hipaa) compliance.

## June 01, 2023

Change

The price of an active delivery pipeline is reduced. Also, single-target delivery pipelines no longer incur a charge. Underlying service charges continue to apply. See the Google Cloud Deploy [pricing page](https://cloud.google.com/deploy/pricing) for details.

## May 16, 2023

Feature

[Security insights](https://docs.cloud.google.com/deploy/docs/securing/security-insights) for container images are now available on the [release details](https://docs.cloud.google.com/deploy/docs/view-release) page.

## May 05, 2023

Feature

You can now perform [deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment#run_the_verification_container_on_the_application_cluster) in the same cluster where your application is running (GKE and Anthos only).

## April 28, 2023

Change

Google Cloud Deploy now uses Skaffold 2.3 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions) for all target types.

## April 04, 2023

Feature

Google Cloud Deploy now provides the ability to use a [canary deployment strategy](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary), supported in [preview](https://cloud.google.com/products#product-launch-stages).

## March 06, 2023

Feature

Google Cloud Deploy now provides the ability to [deploy to multiple targets at the same time](https://docs.cloud.google.com/deploy/docs/deploy-app-parallel), supported in [preview](https://cloud.google.com/products/#product-launch-stages).

## February 27, 2023

Announcement

The ability to [verify your deployment](https://docs.cloud.google.com/deploy/docs/verify-deployment) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## February 17, 2023

Change

Google Cloud Deploy now uses Skaffold 2.0 as the [default Skaffold version](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions) for all target types.

## February 08, 2023

Announcement

The ability to [deploy to Cloud Run](https://docs.cloud.google.com/deploy/docs/run-targets) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## January 31, 2023

Announcement

As of November 30, 2022, Google Cloud Deploy has achieved the following compliance certifications:

  * [ISO/IEC 27001](https://docs.cloud.google.com/security/compliance/iso-27001)
  * [ISO/IEC 27017](https://docs.cloud.google.com/security/compliance/iso-27017)
  * [ISO/IEC 27018](https://docs.cloud.google.com/security/compliance/iso-27018)
  * [ISO/IEC 27701](https://docs.cloud.google.com/security/compliance/iso-27701)



Announcement

As of December 15, 2022, Google Cloud Deploy has achieved the following compliance certifications:

  * [SOC-1](https://docs.cloud.google.com/security/compliance/soc-1)
  * [SOC-2](https://docs.cloud.google.com/security/compliance/soc-2)
  * [SOC-3](https://docs.cloud.google.com/security/compliance/soc-3)



## January 20, 2023

Change

Google Cloud Deploy now supports Skaffold version 2.0. The default Skaffold version remains 1.39.

## September 22, 2022

Feature

Google Cloud Deploy now provides the ability to [verify your deployment](https://docs.cloud.google.com/deploy/docs/verify-deployment), supported in [preview](https://cloud.google.com/products/#product-launch-stages).

## September 15, 2022

Change

Google Cloud Deploy is now available in the following regions:

  * asia-northeast2 (Osaka)
  * asia-south1 (Mumbai)
  * asia-south2 (Delhi)
  * asia-southeast1 (Singapore)
  * asia-southeast2 (Jakarta)
  * australia-southeast2 (Melbourne)
  * europe-central2 (Warsaw)
  * europe-north1 (Finland)
  * europe-west4 (Netherlands)
  * europe-west6 (Zurich)
  * northamerica-northeast2 (Toronto)
  * southamerica-west1 (Santiago)
  * us-west3 (Salt Lake City)
  * us-west4 (Las Vegas)



## September 13, 2022

Feature

[Deploying your application to Cloud Run](https://docs.cloud.google.com/deploy/docs/deploy-app-run) is now supported in [preview](https://cloud.google.com/products/#product-launch-stages).

## August 18, 2022

Change

Google Cloud Deploy now [supports Skaffold version 1.39.1](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), as the default.

## July 27, 2022

Feature

You can now have Google Cloud Deploy [generate a `skaffold.yaml` configuration file for you](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#generating_your_skaffoldyaml) when you create a release, based on a single Kubernetes manifest which you provide. This configuration file is suitable for learning and onboarding.

## July 25, 2022

Feature

You can now [view and compare](https://docs.cloud.google.com/deploy/docs/view-release) Kubernetes and Skaffold confguration files for releases, using Google Cloud Console.

## July 11, 2022

Feature

You can now [permanently abandon a release](https://docs.cloud.google.com/deploy/docs/abandon-release) using Google Cloud Deploy.

Feature

You can now [suspend a delivery pipeline](https://https://cloud.google.com/deploy/docs/suspend-pipeline) using Google Cloud Deploy.

## June 29, 2022

Change

Google Cloud Deploy is now available in the following regions:

  * `asia-east2` (Hong Kong)
  * `europe-west2` (London)
  * `europe-west3` (Frankfurt)
  * `us-east4` (N. Virginia)
  * `us-west2` (Los Angeles)



## June 28, 2022

Announcement

The ability to [deploy to Anthos user clusters](https://docs.cloud.google.com/deploy/docs/anthos-targets) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## June 07, 2022

Announcement

The [Google Cloud Terraform provider](https://registry.terraform.io/providers/hashicorp/google/) now supports creating Google Cloud Deploy [delivery pipelines](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/clouddeploy_delivery_pipeline) and [targets](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/clouddeploy_target).

## June 03, 2022

Feature

Google Cloud Deploy is now available in the following region: `australia-southeast1` (Syndey)

## June 01, 2022

Change

Google Cloud Deploy support for Skaffold version 1.37.1 has been updated to [version 1.37.2](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), which is now the default Skaffold version.

## May 17, 2022

Announcement

Google Cloud Deploy support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## May 10, 2022

Feature

Google Cloud Deploy now lets you [change the timeout](https://docs.cloud.google.com/deploy/docs/deploying-application#change_the_deployment_timeout) for Cloud Build operations, from the default setting of 1 hour.

## May 06, 2022

Change

Google Cloud Deploy now [supports Skaffold version 1.37.1](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), as the default.

## March 01, 2022

Change

Google Cloud Deploy is now available in the following region: `asia-northeast3` (Seoul)

## February 28, 2022

Feature

[Deploying your application to Anthos user clusters](https://docs.cloud.google.com/deploy/docs/anthos-targets) is now supported in [preview](https://cloud.google.com/products/#product-launch-stages).

## February 03, 2022

Change

Google Cloud Deploy is now available in the following [regions](https://cloud.google.com/about/locations):

  * `northamerica-northeast1` (Montréal)
  * `asia-northeast1` (Tokyo)



## January 20, 2022

Change

Google Cloud Deploy support for Skaffold version 1.35.1 has been updated to [version 1.35.2](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), which is now the default Skaffold version.

## January 19, 2022

Announcement

Google Cloud Deploy now has [beta stage](https://cloud.google.com/products/#product-launch-stages) support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs).

Feature

You can now [roll back targets](https://docs.cloud.google.com/deploy/docs/roll-back) from the delivery pipeline visualization in Google Cloud Console.

Announcement

[Google Cloud Deploy](https://docs.cloud.google.com/deploy/docs) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## January 17, 2022

Feature

Google Cloud Deploy now [automatically applies provenance labels](https://docs.cloud.google.com/deploy/docs/labels-annotations#automatic_labels_from) to deployed resources.

## January 12, 2022

Feature

You can now view a list of documentation relevant to your current screen, including tutorials, by clicking the **Learn** button on the Google Cloud Deploy page in Google Cloud Console.

Feature

You can now [view deployment metrics](https://docs.cloud.google.com/deploy/docs/metrics) on the Google Cloud Deploy page in Google Cloud Console.

## January 10, 2022

Change

Google Cloud Deploy now [supports Skaffold version 1.35.1](https://docs.cloud.google.com/deploy/docs/using-skaffold/select-skaffold#supported_versions), as the default.

## September 20, 2021

Announcement

[Google Cloud Deploy](https://docs.cloud.google.com/deploy/docs) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 17, 2021

Breaking

Resource names, such as release name, are now validated for conformance with [AIP-122](https://google.aip.dev/122). If you created any Google Cloud Deploy resources with names that don't conform, those resources might not work.

## September 15, 2021

Breaking

The 3-part cluster specification is no longer supported in target configuration. The only accepted format is now as follows:
    
    
    gke:
      cluster: projects/[project_name]/locations/[location]/clusters/[cluster_name]
    

Breaking

In the `release` resource, the `archive_uri` output field is replaced with `artifact_uri`. This reflects the fact that the Skaffold configuration and rendered manifest are no longer stored together as a tar file in a Google Cloud Storage bucket. They are now stored as files in GCS, in a folder corresponding to each render operation.

Deprecated

The `promoteRelease` API is removed. Users can call [`releases.rollouts.create`](https://docs.cloud.google.com/deploy/docs/release-notes/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/create) to promote a release through the API.

## August 20, 2021

Feature

Cloud Deploy now supports configuring custom execution environments for render and deploy activity. You can choose the default pool or a private pool, default or custom service account, and the default or alternative Cloud Storage bucket.

## August 11, 2021

Feature

Deployment targets are now shareable among multiple delivery pipelines. See [Target definitions](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
