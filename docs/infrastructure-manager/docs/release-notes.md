---
url: https://docs.cloud.google.com/infrastructure-manager/docs/release-notes/
title: Infrastructure Manager release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:00:32.277740+00:00
---

# Infrastructure Manager release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/infrastructure-manager/docs/resources)



Send feedback 

#  Infrastructure Manager release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Infrastructure Manager. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/inframanager-release-notes.xml) directly. 

## September 15, 2026

Feature

Infrastructure Manager now supports the `us` multi-regional location in General Availability (GA).

You can now create and manage deployments, revisions, and previews in the `us` multi-region (`projects/PROJECT_ID/locations/us`). Deployments in the `us` multi-region benefit from metadata and state file redundancy across data centers in the United States.

For more information, see [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations).

## May 11, 2026

Feature

You can use deployment groups to manage related deployments as a single logical resource.

For more information, see [Manage deployment groups](https://docs.cloud.google.com/infrastructure-manager/docs/deployment-groups).

## January 12, 2026

Change

Infrastructure Manager is available in the following regions:

  * `me-central2`



For more information about regions, see [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations).

## January 05, 2026

Announcement

Infrastructure Manager will deprecate support for Terraform version `1.2.3` on **January 8, 2026**. 

If you have [enabled auto-migration](https://docs.cloud.google.com/infrastructure-manager/docs/terraform-version-deprecation#auto-migration), your deployments using Terraform version `1.2.3` will be migrated automatically to Terraform version `1.5.7`.

We recommend that you upgrade your deployment Terraform version from `1.2.3` to version `1.5.7` before the version `1.2.3.` end of support date on **February 8, 2026**.

For more information, see [Terraform version management policy](https://docs.cloud.google.com/infrastructure-manager/docs/terraform-version-deprecation) documentation.

## August 29, 2025

Feature

You can use Infrastructure Manager maintained Terraform providers when you create or update a deployment or preview deployment. For more information about using Infra Manager maintained Terraform providers, see [Use the Terraform provider for Google Cloud](https://docs.cloud.google.com/infrastructure-manager/docs/terraform#terraform-provider).

Feature

You can connect your repositories to Infrastructure Manager using Developer Connect proxies. For more information, see [Deploy infrastructure using Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources#dc-git), or [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment#dc-git).

## July 07, 2025

Feature

You can use preview deployments to view resource drift using Infrastructure Manager. For more information about viewing resource drift, see [View resource change and drift details](https://docs.cloud.google.com/infrastructure-manager/docs/export-view-preview-results#view_resource_change_and_drift_details).

Change

Infrastructure Manager is available in the following regions:

  * `africa-south1`
  * `europe-north2`
  * `europe-southwest1`
  * `europe-west8`
  * `europe-west9`
  * `europe-west10`
  * `europe-west12`
  * `me-central1`
  * `me-west1`
  * `northamerica-south1`
  * `us-east5`
  * `us-south1`



For more information about regions, see [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations).

## December 12, 2024

Feature

You can use Infrastructure Manager (Infra Manager) to preview, create, manage, and delete deployments in Google Cloud Console. Use the [Terraform blueprint catalog](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints) to find sample blueprints you can deploy with Infra Manager. 

For more information about creating a deployment using Infra Manager via Google Cloud Console, see [Deploy infrastructure using Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources#console).

Feature

Infra Manager is available in the following regions:

**Asia Pacific**

  * asia-northeast1
  * asia-northeast2
  * asia-east2
  * asia-south1
  * asia-south2
  * asia-southeast1
  * asia-southeast2
  * australia-southeast1
  * australia-southeast2



**Europe**

  * europe-north1
  * europe-central2
  * europe-west3
  * europe-west4
  * europe-west6



**Americas**

  * us-east1
  * us-east4
  * us-west1
  * us-west2
  * us-west3
  * us-west4
  * northamerica-northeast2
  * southamerica-west1



For more information, see [Locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations).

**Note:** Due to dependencies on Cloud Build, certain regions may not be available for Infra Manager.

## April 19, 2024

Change

Infrastructure manager supports the following versions of Terraform when creating a [preview of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment). For more details, see [Supported Terraform Versions](https://docs.cloud.google.com/infrastructure-manager/docs/terraform#terraform_versions).

  * Terraform version 1.2.3
  * Terraform version 1.3.10
  * Terraform version 1.4.7
  * Terraform version 1.5.7



## March 14, 2024

Feature

Infrastructure Manager supports the deployment of infrastructure from Terraform configurations in a private Git repository.

Feature

Infrastructure Manager supports an automated workflow with Git repositories using Cloud Build. For more information, see [Automate the deployment of Google Cloud resources](https://docs.cloud.google.com/infrastructure-manager/docs/automate-git).

Feature

Infrastructure Manager can [validate and enforce quota limits](https://docs.cloud.google.com/infrastructure-manager/docs/quotas#quota_validation), preventing infrastructure that exceeds quota limits from being deployed.

Change

Information about the runtime environment of Infrastructure Manager is published as part of the overview of Infrastructure Manager. For details, see [runtime environment](https://docs.cloud.google.com/infrastructure-manager/docs/overview#runtime_environment).

Change

Infrastructure manager supports the following versions of Terraform when creating a deployment. For more details, see [Supported Terraform Versions](https://docs.cloud.google.com/infrastructure-manager/docs/terraform).

  * Terraform version 1.2.3
  * Terraform version 1.3.10
  * Terraform version 1.4.7
  * Terraform version 1.5.7



Change

Infrastructure Manager is available in the following regions:

  * `asia-northeast3` (Seoul)
  * `europe-west2` (London)
  * `northamerica-northeast1` (Montréal)
  * `southamerica-east1` (São Paulo)



For more information, see [Locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations).

## January 11, 2024

Feature

Preview of deployments are available. For more information, see [Preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).

Change

For some deployments that initially fail, Infrastructure Manager retries the deployment a limited number of times.

## October 26, 2023

Change

Infrastructure Manager has [client libraries](https://docs.cloud.google.com/infrastructure-manager/docs/reference/libraries) for the following languages:

  * C++ ([GA](https://cloud.google.com/terms/service-terms))
  * C# ([Beta](https://cloud.google.com/terms/service-terms))
  * Go ([Beta](https://cloud.google.com/terms/service-terms))
  * Java ([Beta](https://cloud.google.com/terms/service-terms))
  * Node.js ([Beta](https://cloud.google.com/terms/service-terms))
  * PHP ([Beta](https://cloud.google.com/terms/service-terms))
  * Python ([Beta](https://cloud.google.com/terms/service-terms))
  * Ruby ([GA](https://cloud.google.com/terms/service-terms))



## October 13, 2023

Feature

The [`gcloud` CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager) for Infrastructure Manager are generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 28, 2023

Feature

The integration of Infrastructure Manager with VPC Service Controls is in [Preview](https://cloud.google.com/products#product-launch-stages) and is ready for broader testing and use, but is not fully supported for production environments. Refer to [VPC-SC supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_infrastructure_manager) page for more info.

## August 21, 2023

Announcement

Infrastructure Manager is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Feature

This release includes `gcloud` CLI support in [alpha](https://docs.cloud.google.com/sdk/gcloud#release_levels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
