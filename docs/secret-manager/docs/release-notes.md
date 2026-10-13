---
url: https://docs.cloud.google.com/secret-manager/docs/release-notes/
title: Secret Manager release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:01.216212+00:00
---

# Secret Manager release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/secret-manager/docs/resources)



Send feedback 

#  Secret Manager release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Secret Manager. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

For updates to the Secret Manager integration with Google Kubernetes Engine (GKE), including the Secret Manager add-on and secret synchronization, see [GKE integration release notes](https://docs.cloud.google.com/secret-manager/docs/gke-release-notes).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/secretmanager-release-notes.xml) directly. 

## September 14, 2026

Feature

Parameter Manager supports CRC32C checksums to verify data integrity when you add or access parameter versions.

For more information, see [Data integrity assurance](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/data-integrity).

## September 08, 2026

Feature

Parameter Manager supports using tags to group and organize parameters and conditionally manage access control using Identity and Access Management (IAM) policies.

For more information, see [Create and manage tags](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-and-manage-tags).

## August 12, 2026

Fixed

Parameter Manager enforces the location organization policy (`constraints/gcp.resourceLocations`) on resources in the `global` location.

If your organization policy restricts allowed resource locations, you must explicitly allow the `global` location in the policy. Otherwise, attempts to create global resources fail.

This helps ensure that Parameter Manager consistently applies the location organization policy checks to global resources.

For more information, see [Defining resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations).

## July 27, 2026

Feature

Automatic rotation of regional Cloud SQL database credentials in Secret Manager is available in [Preview](https://cloud.google.com/products#product-launch-stages). This feature lets you automatically generate secure passwords, update target Cloud SQL database instances (PostgreSQL or SQL Server), and rotate secret versions on a configured schedule without custom Cloud Run functions.

For more information, see [Automatic rotation of Cloud SQL secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/autorotation-of-cloudsql-secrets-rs).

## July 12, 2026

Feature

Parameter templates are available in [Preview](https://cloud.google.com/products#product-launch-stages). This feature lets you define standardized configuration blueprints and securely substitute environment-specific variables from parameter versions during deployment.

For more information, see [Parameter templates overview](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-templates-overview).

## June 19, 2026

Feature

Secret Manager supports multi-region storage. You can choose between a single region or a multi-region location when you create a regional secret in the Google Cloud console.

For more information, see [Create a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret).

## June 18, 2026

Feature

Secret Manager is available in the following multi-regions:

  * United States (`us`)
  * European Union (`eu`)
  * Canada (`ca`)
  * India (`in`)



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations#location-mr).

## May 20, 2026

Feature

Secret Manager and Parameter Manager integrate with the Agent Development Kit (ADK) to retrieve secrets and parameters securely at runtime. This integration prevents the exposure of sensitive credentials to the LLM context window or conversation history.

For more information, see the following resources:

  * [Manage secrets for external services in Agent Development Kit](https://docs.cloud.google.com/secret-manager/docs/integrate-secret-manager-with-adk)
  * [Parameter Manager integration with Agent Development Kit](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/parameter-manager-adk-integration)



## April 16, 2026

Feature

The integrated secret synchronization feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can automatically synchronize secrets from Secret Manager into Kubernetes Secret objects within your Google Kubernetes Engine (GKE) clusters.

For more information, see [Synchronize secrets to Kubernetes Secrets](https://docs.cloud.google.com/secret-manager/docs/sync-k8-secrets).

## April 07, 2026

Feature

Parameter Manager supports the `latest` identifier, which lets you fetch the most recent parameter value without specifying a version ID. When you use the gcloud CLI or REST API, you can use `latest` to retrieve the most recent version of a parameter.

For more information, see [Access a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version).

## February 06, 2026

Feature

**Parameter version comparison** : You can compare two versions of a parameter to identify changes in their payload. This feature lets you audit modifications over time and debug issues related to specific parameter updates.

For more information, see [Compare parameter versions](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/compare-parameter-versions).

## January 20, 2026

Feature

Secret Manager is available in the following region:

  * `asia-southeast3` (Bangkok)



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## October 13, 2025

Feature

**Preview:** Integrated secret synchronization feature is now available in preview. You can automatically synchronize secrets from Secret Manager into Kubernetes Secret objects within your Google Kubernetes Engine (GKE) clusters. This process allows applications to access secrets from Secret Manager using standard Kubernetes methods, such as environment variables or volume mounts. Applications that are already configured to read secrets from Kubernetes Secret object can now seamlessly read secrets in Secret Manager.

For more information, see [Synchronize secrets to Kubernetes Secrets](https://docs.cloud.google.com/secret-manager/docs/sync-k8-secrets).

## September 01, 2025

Feature

**Automatic secret rotation with the Secret Manager add-on for Google Kubernetes Engine (GKE)** : You can configure the Secret Manager add-on to automatically rotate secrets so that secrets updated in Secret Manager after initial pod deployment are automatically and periodically pushed to the pod. This feature is now Generally available (GA). 

For more information, see [Configure automatic rotation of secrets](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component#configure_automatic_rotation_of_secrets).

## July 09, 2025

Feature

**Enhanced tagging capabilities for Secret Manager** : You can now add tags directly at the time of secret creation. This new feature lets you provide essential metadata for your resources and helps with better organization, cost tracking, and automated policy application from the time a secret is created. In addition to this, _tagging for regional secrets_ is now fully supported, both during secret creation and for existing regional secrets. For more information, see the documentation on tags for [global secrets](https://docs.cloud.google.com/secret-manager/docs/create-and-manage-tags) and [regional secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/create-manage-tags-regional-secrets).

**Soft-enforced rate limits for modifying secrets and secret versions** : We have introduced soft-enforced rate limits for the following operations in Secret Manager:

  * `AddSecretVersion`
  * `UpdateSecret`
  * `EnableSecretVersion`
  * `DisableSecretVersion`
  * `DestroySecretVersion`



Soft enforcement lets us continue serving requests beyond the defined quota as long as our backend systems can comfortably handle the increased load. For details, see the [Quotas and limits](https://docs.cloud.google.com/secret-manager/quotas) documentation.

## June 23, 2025

Libraries

### Go

#### [1.15.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.7...secretmanager/v1.15.0) (2025-06-17)

##### Features

  * **secretmanager:** Update secret manager protos for tags ([#12406](https://github.com/googleapis/google-cloud-go/issues/12406)) ([feb078b](https://github.com/googleapis/google-cloud-go/commit/feb078b04ab541dd3bdceb2ac1f24938bb0354a3))



## April 21, 2025

Libraries

### Go

#### [1.14.7](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.6...secretmanager/v1.14.7) (2025-04-15)

##### Bug Fixes

  * **secretmanager:** Update google.golang.org/api to 0.229.0 ([3319672](https://github.com/googleapis/google-cloud-go/commit/3319672f3dba84a7150772ccb5433e02dab7e201))



## April 04, 2025

Feature

The Secret Manager add-on for Google Kubernetes Engine (GKE) now supports the automatic rotation of secrets. You can configure the Secret Manager add-on to automatically rotate secrets so that secrets updated in Secret Manager after initial pod deployment are automatically and periodically pushed to the pod. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). 

For more information, see [Configure automatic rotation of secrets](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component#configure_automatic_rotation_of_secrets).

## March 27, 2025

Feature

Parameter Manager, an extension to the Secret Manager service, is now Generally available (GA). Parameter Manager lets you store, access, and manage the lifecycle of workload parameters. You can interact with Parameter Manager using the console, gcloud CLI, REST API, and client libraries.

For information, see the Parameter Manager [documentation](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview).

## March 17, 2025

Libraries

### Go

#### [1.14.6](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.5...secretmanager/v1.14.6) (2025-03-13)

##### Bug Fixes

  * **secretmanager:** Update golang.org/x/net to 0.37.0 ([1144978](https://github.com/googleapis/google-cloud-go/commit/11449782c7fb4896bf8b8b9cde8e7441c84fb2fd))



## March 03, 2025

Feature

Secret Manager is now available in the following region:

  * europe-north2 (Stockholm)



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## February 28, 2025

Feature

Parameter Manager, currently in [Preview](https://cloud.google.com/products#product-launch-stages), now offers a console for storing, accessing, and managing the lifecycle of your workload parameters. For more information, see the [Parameter Manager documentation](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter).

## February 17, 2025

Libraries

### Go

#### [1.14.5](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.4...secretmanager/v1.14.5) (2025-02-12)

##### Bug Fixes

  * **secretmanager:** Upgrade Go gRPC Protobuf generation ([90140b1](https://github.com/googleapis/google-cloud-go/commit/90140b17da6378fa87d4bec0d404c18a78d6b02a))



## February 03, 2025

Libraries

### Go

#### [1.14.4](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.3...secretmanager/v1.14.4) (2025-01-30)

##### Documentation

  * **secretmanager:** Fix link in Markdown comments ([aa54375](https://github.com/googleapis/google-cloud-go/commit/aa54375c195b1bf8653de26400f342438a8d6f85))
  * **secretmanager:** Updated comment for `customer_managed_encryption` in message `.google.cloud.secretmanager.v1.Secret` ([aa54375](https://github.com/googleapis/google-cloud-go/commit/aa54375c195b1bf8653de26400f342438a8d6f85))
  * **secretmanager:** Updated comment for `customer_managed_encryption` in message `.google.cloud.secretmanager.v1.SecretVersion` ([aa54375](https://github.com/googleapis/google-cloud-go/commit/aa54375c195b1bf8653de26400f342438a8d6f85))
  * **secretmanager:** Updated comment for `name` in message `.google.cloud.secretmanager.v1.Topic` ([aa54375](https://github.com/googleapis/google-cloud-go/commit/aa54375c195b1bf8653de26400f342438a8d6f85))
  * **secretmanager:** Updated comment for `Replication` ([aa54375](https://github.com/googleapis/google-cloud-go/commit/aa54375c195b1bf8653de26400f342438a8d6f85))
  * **secretmanager:** Updated comment for `scheduled_destroy_time` in message `.google.cloud.secretmanager.v1.SecretVersion` ([aa54375](https://github.com/googleapis/google-cloud-go/commit/aa54375c195b1bf8653de26400f342438a8d6f85))



## January 06, 2025

Libraries

### Go

#### [1.14.3](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.2...secretmanager/v1.14.3) (2025-01-02)

##### Bug Fixes

  * **secretmanager:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))



## December 06, 2024

Feature

Parameter Manager, an extension to the Secret Manager service, is available in [Preview](https://cloud.google.com/products#product-launch-stages). You can use Parameter Manager to store, access, and manage the lifecycle of your workload parameters. For more information, see [Parameter Manager overview](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview).

## November 19, 2024

Feature

Creating [custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#custom-organization-policies) with Secret Manager resources is now in General Availability ([GA](https://cloud.google.com/products#product-launch-stages)). You can use custom organization policies to enhance secret security by enforcing rotation schedules, annotations, and expirations for secrets. You can also use custom organization policies to restrict secret types to manage costs. To learn more about using custom organization policies in Secret Manager, see [Use custom organization policies](https://docs.cloud.google.com/secret-manager/docs/secret-manager-custom-constraints).

## November 17, 2024

Feature

Secret Manager is now available in the following region:

  * northamerica-south1



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## October 28, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.14.2](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.1...secretmanager/v1.14.2) (2024-10-23)

##### Bug Fixes

  * **secretmanager:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **secretmanager:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([2b8ca4b](https://github.com/googleapis/google-cloud-go/commit/2b8ca4b4127ce3025c7a21cc7247510e07cc5625))



## October 14, 2024

Feature

Creating regional secrets using Secret Manager is now in Generally Availability ([GA](https://cloud.google.com/products#product-launch-stages)). Regional secrets let you store your sensitive data within a specific geographic location, ensuring it remains in that region at all times – whether at rest, in use, or in transit. Regional secrets are crucial for meeting data residency requirements and complying with regulatory mandates.

For information about all tasks related to creating and managing regional secrets, see the [Regional service documentation](https://docs.cloud.google.com/secret-manager/regional-secrets/global-regionalized-service-comparison).

## September 16, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.14.1](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.0...secretmanager/v1.14.1) (2024-09-12)

##### Bug Fixes

  * **secretmanager:** Bump dependencies ([2ddeb15](https://github.com/googleapis/google-cloud-go/commit/2ddeb1544a53188a7592046b98913982f1b0cf04))



## September 10, 2024

Feature

Secret Manager is now enabled for use with Cloud KMS Autokey.

Using keys generated by Autokey can help you consistently align with industry standards and recommended practices for data security, including the HSM protection level, separation of duties, key rotation, location, and key specificity. Keys requested using Autokey function identically to other Cloud HSM keys with the same settings.

For more information, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek). To learn more about Cloud KMS Autokey, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

## August 26, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.14.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.13.6...secretmanager/v1.14.0) (2024-08-20)

##### Features

  * **secretmanager:** Add support for Go 1.23 iterators ([84461c0](https://github.com/googleapis/google-cloud-go/commit/84461c0ba464ec2f951987ba60030e37c8a8fc18))



## August 23, 2024

Feature

You can now create regional secrets using Secret Manager. When you create a regional secret, you specify the location where you want it to be stored. Your secret data remains within the chosen location at all times, whether it's at rest, in use, or in transit. This capability allows you to meet data residency requirements, which mandate that data remains within specified geographic boundaries, often due to regulatory or compliance reasons. The feature is in [Preview](https://cloud.google.com/products#product-launch-stages). 

For more information, see [Data residency and regional secrets](https://docs.cloud.google.com/secret-manager/docs/regional-secrets-overview).

## August 21, 2024

Feature

You can attach tags to secrets to conditionally grant or deny access to Secret Manager resources. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a secret has a specific tag. This feature is in [Preview](http://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage tags](https://docs.cloud.google.com/secret-manager/docs/create-and-manage-tags).

## August 20, 2024

Feature

Secret Manager add-on for Google Kubernetes Engine (GKE) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). With the add-on, you can access the secrets stored in Secret Manager as volumes mounted in Kubernetes Pods. You can install the Secret Manager add-on on both Standard clusters and Autopilot clusters. The Secret Manager add-on is a Google managed and officially supported version of the open source Kubernetes Secrets Store CSI driver. 

For more information, see [Use Secret Manager add-on with Google Kubernetes Engine](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component).

## August 12, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.13.6](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.13.5...secretmanager/v1.13.6) (2024-08-08)

##### Bug Fixes

  * **secretmanager:** Update google.golang.org/api to v0.191.0 ([5b32644](https://github.com/googleapis/google-cloud-go/commit/5b32644eb82eb6bd6021f80b4fad471c60fb9d73))



## July 29, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.13.5](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.13.4...secretmanager/v1.13.5) (2024-07-24)

##### Bug Fixes

  * **secretmanager:** Update dependencies ([257c40b](https://github.com/googleapis/google-cloud-go/commit/257c40bd6d7e59730017cf32bda8823d7a232758))



## July 15, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.13.4](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.13.3...secretmanager/v1.13.4) (2024-07-10)

##### Bug Fixes

  * **secretmanager:** Bump google.golang.org/grpc@v1.64.1 ([8ecc4e9](https://github.com/googleapis/google-cloud-go/commit/8ecc4e9622e5bbe9b90384d5848ab816027226c5))



## July 08, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.13.3](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.13.2...secretmanager/v1.13.3) (2024-07-01)

##### Bug Fixes

  * **secretmanager:** Bump google.golang.org/api@v0.187.0 ([8fa9e39](https://github.com/googleapis/google-cloud-go/commit/8fa9e398e512fd8533fd49060371e61b5725a85b))



## July 01, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.13.2](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.13.1...secretmanager/v1.13.2) (2024-06-26)

##### Bug Fixes

  * **secretmanager:** Enable new auth lib ([b95805f](https://github.com/googleapis/google-cloud-go/commit/b95805f4c87d3e8d10ea23bd7a2d68d7a4157568))



## June 12, 2024

Feature

Delayed destruction of secret versions is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). You can [set up a duration for delayed destruction](https://docs.cloud.google.com/secret-manager/docs/delay-destruction-of-secret-versions#set-up-delay-duration) at the time of creating or updating a secret. When a destruction delay duration is configured for a secret, destroying a version of that secret will disable the version and prevent its use. However, it won't be immediately destroyed. Instead, it will remain scheduled for destruction for the specified delay duration. After that duration expires, the version will be permanently destroyed. Secret Manager administrators can restore a secret version that is scheduled for destruction by either enabling or disabling it during the delay period.

## May 27, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.13.1](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.13.0...secretmanager/v1.13.1) (2024-05-22)

##### Bug Fixes

  * **secretmanager:** Enable cloud.google.com/go/auth ([#10248](https://github.com/googleapis/google-cloud-go/issues/10248)) ([532d8fb](https://github.com/googleapis/google-cloud-go/commit/532d8fb10a75186ca71ebf46ae73ecd09918c103))



## May 06, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.13.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.12.0...secretmanager/v1.13.0) (2024-05-01)

##### Features

  * **secretmanager:** Add Secret Version Delayed Destroy changes for client libraries ([1d757c6](https://github.com/googleapis/google-cloud-go/commit/1d757c66478963d6cbbef13fee939632c742759c))



##### Bug Fixes

  * **secretmanager:** Bump x/net to v0.24.0 ([ba31ed5](https://github.com/googleapis/google-cloud-go/commit/ba31ed5fda2c9664f2e1cf972469295e63deb5b4))



## April 02, 2024

Feature

**Preview:** Delayed destruction of secret versions is now available in Preview. By default, secret versions are destroyed immediately upon request. You can enable delayed destruction at the secret level and provide a destruction delay duration such that when a version belonging to this secret is destroyed, the destruction is not immediate. Instead, the secret version is disabled for use and remains scheduled for destruction for the configured delay duration. When the destruction delay duration expires, the version is destroyed. The Secret Manager Admin can restore a secret version that is scheduled for destruction by enabling or disabling the version. 

To learn more, see [Delay destruction of secret versions](https://docs.cloud.google.com/secret-manager/docs/delay-destruction-of-secret-versions).

## March 25, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.12.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.11.6...secretmanager/v1.12.0) (2024-03-19)

##### Features

  * **secretmanager:** New client apiv1beta2 ([#9610](https://github.com/googleapis/google-cloud-go/issues/9610)) ([443914f](https://github.com/googleapis/google-cloud-go/commit/443914f20df975e5075050e970f62941b66b2d28))



## March 18, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.11.6](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.11.5...secretmanager/v1.11.6) (2024-03-14)

##### Bug Fixes

  * **secretmanager:** Update protobuf dep to v1.33.0 ([30b038d](https://github.com/googleapis/google-cloud-go/commit/30b038d8cac0b8cd5dd4761c87f3f298760dd33a))



## March 07, 2024

Feature

**Preview:** Secret Manager add-on for Google Kubernetes Engine (GKE) is now available in preview. With the add-on, you can access the secrets stored in Secret Manager as volumes mounted in Kubernetes Pods. You can install the Secret Manager add-on on both Standard clusters and Autopilot clusters. The Secret Manager add-on is a Google managed and officially supported version of the open source [Kubernetes Secrets Store CSI driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver). 

For more information, see [Use Secret Manager add-on with Google Kubernetes Engine](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component).

## February 05, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.11.5](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.11.4...secretmanager/v1.11.5) (2024-01-30)

##### Bug Fixes

  * **secretmanager:** Enable universe domain resolution options ([fd1d569](https://github.com/googleapis/google-cloud-go/commit/fd1d56930fa8a747be35a224611f4797b8aeb698))



## January 31, 2024

Feature

Secret Manager is now available in the following region:

  * africa-south1



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## December 18, 2023

Feature

Generally available: Key Access Justifications is now generally available with Secret Manager. Key Access Justifications works by adding a field to your Cloud External Key Manager requests that allows you to view the reason for each request. You can automatically approve or deny these requests, based on the justification. For more information, see [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview).

## November 06, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.11.4](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.11.3...secretmanager/v1.11.4) (2023-11-01)

##### Bug Fixes

  * **secretmanager:** Bump google.golang.org/api to v0.149.0 ([8d2ab9f](https://github.com/googleapis/google-cloud-go/commit/8d2ab9f320a86c1c0fab90513fc05861561d0880))



## October 31, 2023

Feature

**Preview:** Key Access Justifications is now available in preview with Secret Manager. Key Access Justifications provides a justification for every request to access keys stored in an external key manager. It lets you approve or deny the access request based on the provided justification. 

For more information, refer to the [overview](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) of Key Access Justifcations.

## October 30, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.11.3](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.11.2...secretmanager/v1.11.3) (2023-10-26)

##### Bug Fixes

  * **secretmanager:** Update grpc-go to v1.59.0 ([81a97b0](https://github.com/googleapis/google-cloud-go/commit/81a97b06cb28b25432e4ece595c55a9857e960b7))



## October 16, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.11.2](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.11.1...secretmanager/v1.11.2) (2023-10-12)

##### Bug Fixes

  * **secretmanager:** Update golang.org/x/net to v0.17.0 ([174da47](https://github.com/googleapis/google-cloud-go/commit/174da47254fefb12921bbfc65b7829a453af6f5d))



## September 20, 2023

Feature

Secret Manager is now available in the following region:

  * me-central2



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## August 22, 2023

Feature

Secret Manager is now available in the following region:

  * europe-west10



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## June 26, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.11.1](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.11.0...secretmanager/v1.11.1) (2023-06-20)

##### Bug Fixes

  * **secretmanager:** REST query UpdateMask bug ([df52820](https://github.com/googleapis/google-cloud-go/commit/df52820b0e7721954809a8aa8700b93c5662dc9b))



## June 05, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.11.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.10.1...secretmanager/v1.11.0) (2023-05-30)

##### Features

  * **secretmanager:** Update all direct dependencies ([b340d03](https://github.com/googleapis/google-cloud-go/commit/b340d030f2b52a4ce48846ce63984b28583abde6))



## May 15, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.10.1](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.10.0...secretmanager/v1.10.1) (2023-05-08)

##### Bug Fixes

  * **secretmanager:** Update grpc to v1.55.0 ([1147ce0](https://github.com/googleapis/google-cloud-go/commit/1147ce02a990276ca4f8ab7a1ab65c14da4450ef))



## April 03, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.16.1](https://github.com/googleapis/python-secret-manager/compare/v2.16.0...v2.16.1) (2023-03-23)

##### Documentation

  * Fix formatting of request arg in docstring ([#409](https://github.com/googleapis/python-secret-manager/issues/409)) ([925d05a](https://github.com/googleapis/python-secret-manager/commit/925d05af92f2b60978db307f5be891c9784a1bb1))



## March 30, 2023

Feature

Secret Manager is now available in the following region:

  * me-central1



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## March 23, 2023

Feature

Secret Manager is now available in the following region:

  * europe-west12



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## March 13, 2023

Feature

Support for [aliases](https://docs.cloud.google.com/secret-manager/docs/assign-alias-to-secret-version) in Secret Manager is now [generally available](https://cloud.google.com/products/#product-launch-stages). You can use an alias to get and access a version using a resource path name. A given alias string can only be bound to a single version. You can, however, assign multiple aliases to a secret version.

## March 08, 2023

Feature

Support for [Annotations](https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-annotations) in Secret Manager is now [generally available](https://cloud.google.com/products/#product-launch-stages). Annotations are used to define custom metadata about a secret.

## March 06, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.16.0](https://github.com/googleapis/python-secret-manager/compare/v2.15.1...v2.16.0) (2023-02-28)

##### Features

  * Enable "rest" transport in Python for services supporting numeric enums ([10c02e5](https://github.com/googleapis/python-secret-manager/commit/10c02e52e99182886f2e96b2834aefb41436b28b))



## January 30, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.15.1](https://github.com/googleapis/python-secret-manager/compare/v2.15.0...v2.15.1) (2023-01-20)

##### Bug Fixes

  * Add context manager return types ([2b85fae](https://github.com/googleapis/python-secret-manager/commit/2b85fae2b2a493bdff797164d99d021d8e2e9e4e))



##### Documentation

  * Add documentation for enums ([2b85fae](https://github.com/googleapis/python-secret-manager/commit/2b85fae2b2a493bdff797164d99d021d8e2e9e4e))



## January 16, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.15.0](https://github.com/googleapis/python-secret-manager/compare/v2.14.0...v2.15.0) (2023-01-10)

##### Features

  * Add support for Python 3.11 ([#386](https://github.com/googleapis/python-secret-manager/issues/386)) ([0c68091](https://github.com/googleapis/python-secret-manager/commit/0c68091480407804e05164fbfda0b74f79c0bf05))



## January 09, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.10.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.9.0...secretmanager/v1.10.0) (2023-01-04)

##### Features

  * **secretmanager:** Add REST client ([06a54a1](https://github.com/googleapis/google-cloud-go/commit/06a54a16a5866cce966547c51e203b9e09a25bc0))



### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.14.0](https://github.com/googleapis/python-secret-manager/compare/v2.13.0...v2.14.0) (2023-01-04)

##### Features

  * Update public API to include annotation support ([#381](https://github.com/googleapis/python-secret-manager/issues/381)) ([68bbbe5](https://github.com/googleapis/python-secret-manager/commit/68bbbe59302d653f849cbac31321208224ad5413))



## December 19, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.13.0](https://github.com/googleapis/python-secret-manager/compare/v2.12.6...v2.13.0) (2022-12-14)

##### Features

  * Add support for `google.cloud.secretmanager.__version__` ([5530112](https://github.com/googleapis/python-secret-manager/commit/5530112ecb5a932d3abe875dcaabaf6ca7a108d5))
  * Add typing to proto.Message based class attributes ([5530112](https://github.com/googleapis/python-secret-manager/commit/5530112ecb5a932d3abe875dcaabaf6ca7a108d5))
  * Regenerate client for v1beta1 ([dc9b1e3](https://github.com/googleapis/python-secret-manager/commit/dc9b1e38da2ecf6470ff5669f14ebad86dda4756))



##### Bug Fixes

  * Add dict typing for client_options ([5530112](https://github.com/googleapis/python-secret-manager/commit/5530112ecb5a932d3abe875dcaabaf6ca7a108d5))
  * **deps:** Require google-api-core >=1.34.0, >=2.11.0 ([dc9b1e3](https://github.com/googleapis/python-secret-manager/commit/dc9b1e38da2ecf6470ff5669f14ebad86dda4756))
  * Drop usage of pkg_resources ([dc9b1e3](https://github.com/googleapis/python-secret-manager/commit/dc9b1e38da2ecf6470ff5669f14ebad86dda4756))
  * Fix timeout default values ([dc9b1e3](https://github.com/googleapis/python-secret-manager/commit/dc9b1e38da2ecf6470ff5669f14ebad86dda4756))



##### Documentation

  * **samples:** Snippetgen handling of repeated enum field ([5530112](https://github.com/googleapis/python-secret-manager/commit/5530112ecb5a932d3abe875dcaabaf6ca7a108d5))
  * **samples:** Snippetgen should call await on the operation coroutine before calling result ([dc9b1e3](https://github.com/googleapis/python-secret-manager/commit/dc9b1e38da2ecf6470ff5669f14ebad86dda4756))



## November 14, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/secret-manager](https://github.com/googleapis/nodejs-secret-manager)

#### [4.1.4](https://github.com/googleapis/nodejs-secret-manager/compare/v4.1.3...v4.1.4) (2022-11-11)

##### Bug Fixes

  * **deps:** Use google-gax v3.5.2 ([#413](https://github.com/googleapis/nodejs-secret-manager/issues/413)) ([1652509](https://github.com/googleapis/nodejs-secret-manager/commit/16525099e4a28b466ebfa067a001124d253c8992))



## November 07, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.9.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.8.0...secretmanager/v1.9.0) (2022-11-03)

##### Features

  * **secretmanager:** rewrite signatures in terms of new location ([3c4b2b3](https://github.com/googleapis/google-cloud-go/commit/3c4b2b34565795537aac1661e6af2442437e34ad))



## October 31, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.8.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.7.0...secretmanager/v1.8.0) (2022-10-25)

##### Features

  * **secretmanager:** start generating stubs dir ([de2d180](https://github.com/googleapis/google-cloud-go/commit/de2d18066dc613b72f6f8db93ca60146dabcfdcc))



## October 17, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.1.8](https://github.com/googleapis/java-secretmanager/compare/v2.1.7...v2.1.8) (2022-10-13)

##### ⚠ BREAKING CHANGES

  * Release gapic-generator-java v2.0.0 (#557)



##### Features

  * Add `gcf-owl-bot[bot]` to `ignoreAuthors` ([#485](https://github.com/googleapis/java-secretmanager/issues/485)) ([1e08041](https://github.com/googleapis/java-secretmanager/commit/1e080418f12bcdc9d158684d19ce369161a1d5a5))
  * Add CustomerManagedEncryptionKey support, ReplicationStatus to SecretVersion ([#217](https://github.com/googleapis/java-secretmanager/issues/217)) ([0d306e8](https://github.com/googleapis/java-secretmanager/commit/0d306e8e6eee7bdf96fb6d80d7a67c4181d87f4c))
  * Added expire_time and ttl fields to Secret ([#355](https://github.com/googleapis/java-secretmanager/issues/355)) ([0dc2188](https://github.com/googleapis/java-secretmanager/commit/0dc2188e1e9b79f6ddbd5e509480e6fedfc7128e))
  * Added topic field to Secret ([#389](https://github.com/googleapis/java-secretmanager/issues/389)) ([32286cc](https://github.com/googleapis/java-secretmanager/commit/32286ccdff4e39afbb4a4bf1602f735ac119f43f))
  * Checksums in Secret Manager ([#687](https://github.com/googleapis/java-secretmanager/issues/687)) ([4e5ee16](https://github.com/googleapis/java-secretmanager/commit/4e5ee1621fbfeffb3b9da1cdd360684f812a63b9))
  * Etags in Secret Manager ([#481](https://github.com/googleapis/java-secretmanager/issues/481)) ([b2b9934](https://github.com/googleapis/java-secretmanager/commit/b2b993438c3ebad007cf968f82ae4da7b1eabe1c))
  * In Secret Manager, users can now use filter to customize the output of ListSecrets/ListSecretVersions calls ([#544](https://github.com/googleapis/java-secretmanager/issues/544)) ([bd2d8b3](https://github.com/googleapis/java-secretmanager/commit/bd2d8b3a4f60fa042b5fafca1a57249d150e8f8f))
  * Release gapic-generator-java v2.0.0 ([#557](https://github.com/googleapis/java-secretmanager/issues/557)) ([39419ba](https://github.com/googleapis/java-secretmanager/commit/39419ba94374404447bb59f653fb14482f12cfa9))
  * Rotation for Secrets ([#425](https://github.com/googleapis/java-secretmanager/issues/425)) ([0d2e4b4](https://github.com/googleapis/java-secretmanager/commit/0d2e4b435f8847d0211bb9bf694fef0878364c26))
  * Tune Secret Manager auto retry parameters ([#536](https://github.com/googleapis/java-secretmanager/issues/536)) ([dcb0303](https://github.com/googleapis/java-secretmanager/commit/dcb0303b25c0e8daf64b5e8ec20bda1b473c3f30))



##### Bug Fixes

  * Add `shopt -s nullglob` to dependencies script ([#522](https://github.com/googleapis/java-secretmanager/issues/522)) ([4349b80](https://github.com/googleapis/java-secretmanager/commit/4349b8099d620fd8c4d8a4e17d1623e8dde17119))
  * **java:** Add -ntp flag to native image testing command ([#1299](https://github.com/googleapis/java-secretmanager/issues/1299)) ([#648](https://github.com/googleapis/java-secretmanager/issues/648)) ([a617941](https://github.com/googleapis/java-secretmanager/commit/a6179419d8ae93480cc79ef432308dde7c4431ac))
  * **java:** Java 17 dependency arguments ([#1266](https://github.com/googleapis/java-secretmanager/issues/1266)) ([#632](https://github.com/googleapis/java-secretmanager/issues/632)) ([d023065](https://github.com/googleapis/java-secretmanager/commit/d0230655d72b7ae4e44cd15aa7525046ede4e046))
  * Next release from 2.1.x will be 2.1.8 ([#890](https://github.com/googleapis/java-secretmanager/issues/890)) ([81d0755](https://github.com/googleapis/java-secretmanager/commit/81d07554474c33c1b3224a508d3a4ef52947cc65))
  * Release scripts from issuing overlapping phases ([#445](https://github.com/googleapis/java-secretmanager/issues/445)) ([dda6b9a](https://github.com/googleapis/java-secretmanager/commit/dda6b9ab661a34db0263fbb74dca1f3d8c45d5eb))
  * Typo ([#440](https://github.com/googleapis/java-secretmanager/issues/440)) ([a74fda1](https://github.com/googleapis/java-secretmanager/commit/a74fda1c3e2ebb34ad1d5711bb753c7ff8c25455))
  * Update dependencies.sh to not break on mac ([#518](https://github.com/googleapis/java-secretmanager/issues/518)) ([7db26b9](https://github.com/googleapis/java-secretmanager/commit/7db26b91d8acf609f4404305b7417637fb48963b))
  * Update repo name ([#368](https://github.com/googleapis/java-secretmanager/issues/368)) ([77ecec0](https://github.com/googleapis/java-secretmanager/commit/77ecec01eb733b0b1871591dade7743d9f35bb29))



##### Documentation

  * Generate sample code in the Java microgenerator ([#370](https://github.com/googleapis/java-secretmanager/issues/370)) ([092bc28](https://github.com/googleapis/java-secretmanager/commit/092bc28f3991e4894d530e02dc408ce905134310))
  * Remote redundant comments ([#213](https://github.com/googleapis/java-secretmanager/issues/213)) ([a1b84ed](https://github.com/googleapis/java-secretmanager/commit/a1b84ed70a5b2688952d35647cdc7a96b935d3d8))
  * **sample:** Add sample for Native Image Support ([#711](https://github.com/googleapis/java-secretmanager/issues/711)) ([1afd3aa](https://github.com/googleapis/java-secretmanager/commit/1afd3aa9a4bc7b4223716c966b7791bbcd096725))



##### Dependencies

  * **java:** Update actions/github-script action to v5 ([#1339](https://github.com/googleapis/java-secretmanager/issues/1339)) ([#683](https://github.com/googleapis/java-secretmanager/issues/683)) ([f009d46](https://github.com/googleapis/java-secretmanager/commit/f009d46b8d53e9f5b8981711a53212ea8774ced2))
  * Regenerating with new Protobuf (2.1.x) ([#886](https://github.com/googleapis/java-secretmanager/issues/886)) ([75dfede](https://github.com/googleapis/java-secretmanager/commit/75dfedefb4dc554b46d0f9f397d04b91b2befc31))
  * Update actions/github-script action to v6 ([#699](https://github.com/googleapis/java-secretmanager/issues/699)) ([60c04dd](https://github.com/googleapis/java-secretmanager/commit/60c04dd9dfc4bc345cfb6f19b868aa5787e21682))
  * Update actions/setup-java action to v3 ([#708](https://github.com/googleapis/java-secretmanager/issues/708)) ([19d54ed](https://github.com/googleapis/java-secretmanager/commit/19d54ed4c9ec111354635d3b081b8a7d0a73835c))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.10.0 ([#232](https://github.com/googleapis/java-secretmanager/issues/232)) ([26aa078](https://github.com/googleapis/java-secretmanager/commit/26aa078e8343cd9de52bb22e2413d5a05bf406a3))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.10.2 ([#245](https://github.com/googleapis/java-secretmanager/issues/245)) ([3bd711f](https://github.com/googleapis/java-secretmanager/commit/3bd711fef39c66b61be2943de8bdc6559d5b484d))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.12.1 ([#260](https://github.com/googleapis/java-secretmanager/issues/260)) ([dae6856](https://github.com/googleapis/java-secretmanager/commit/dae68562475b1ce8e733d0908a2762a2ca40310d))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.13.0 ([#269](https://github.com/googleapis/java-secretmanager/issues/269)) ([2f3cf77](https://github.com/googleapis/java-secretmanager/commit/2f3cf77b4357555228c98482844a77723a1ca13c))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.14.1 ([#289](https://github.com/googleapis/java-secretmanager/issues/289)) ([ec5dd68](https://github.com/googleapis/java-secretmanager/commit/ec5dd6897f0af6617686c1e1102fe6973251270d))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.15.0 ([#299](https://github.com/googleapis/java-secretmanager/issues/299)) ([b4cbfe2](https://github.com/googleapis/java-secretmanager/commit/b4cbfe27d966c8033347669f2c317047dd0341c6))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.16.0 ([#318](https://github.com/googleapis/java-secretmanager/issues/318)) ([b980767](https://github.com/googleapis/java-secretmanager/commit/b98076740ab48e36a42b5bc6d813fe1de3215e0e))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.16.1 ([#331](https://github.com/googleapis/java-secretmanager/issues/331)) ([bb3a6ce](https://github.com/googleapis/java-secretmanager/commit/bb3a6ce4617604421102bb4231060e67882fb1a4))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.17.0 ([#336](https://github.com/googleapis/java-secretmanager/issues/336)) ([eda2c70](https://github.com/googleapis/java-secretmanager/commit/eda2c7072ad4f8b0d86637e0d9a8625ed0c5e641))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.18.0 ([#350](https://github.com/googleapis/java-secretmanager/issues/350)) ([e4cdc01](https://github.com/googleapis/java-secretmanager/commit/e4cdc011892bcc2ad81ef2062ba87d29bd6ae158))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.19.0 ([#382](https://github.com/googleapis/java-secretmanager/issues/382)) ([fdfe07e](https://github.com/googleapis/java-secretmanager/commit/fdfe07e3549a2948c69e86d1dfce87d2772a3674))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.20.0 ([#394](https://github.com/googleapis/java-secretmanager/issues/394)) ([7371c34](https://github.com/googleapis/java-secretmanager/commit/7371c34e22c000ce2f896be600aecbb676e33ed6))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.20.1 ([#409](https://github.com/googleapis/java-secretmanager/issues/409)) ([a6b4dd0](https://github.com/googleapis/java-secretmanager/commit/a6b4dd042c65101641731ef713a19c50eedeb7a9))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.21.0 ([#432](https://github.com/googleapis/java-secretmanager/issues/432)) ([b3a2562](https://github.com/googleapis/java-secretmanager/commit/b3a256254793f3f6d36d8b322370fbc9dfdf36f8))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.21.1 ([#449](https://github.com/googleapis/java-secretmanager/issues/449)) ([4e6371f](https://github.com/googleapis/java-secretmanager/commit/4e6371f2a8684f6840850f9c4f7df24eab62d54d))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.8.2 ([#182](https://github.com/googleapis/java-secretmanager/issues/182)) ([d2cbbe8](https://github.com/googleapis/java-secretmanager/commit/d2cbbe877f7c753b692a75c1662d6d598719ee45))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.8.3 ([#185](https://github.com/googleapis/java-secretmanager/issues/185)) ([f078a2d](https://github.com/googleapis/java-secretmanager/commit/f078a2d475d01520196f120631674fdc76aa9de3))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.8.6 ([#194](https://github.com/googleapis/java-secretmanager/issues/194)) ([db5479f](https://github.com/googleapis/java-secretmanager/commit/db5479fc315e161e5c18f19f663f8aaa5d9be5f9))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v0.9.0 ([#212](https://github.com/googleapis/java-secretmanager/issues/212)) ([3591255](https://github.com/googleapis/java-secretmanager/commit/3591255c296b1f4e71f5b26451754c688757ddfa))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v1 ([#459](https://github.com/googleapis/java-secretmanager/issues/459)) ([f39f53b](https://github.com/googleapis/java-secretmanager/commit/f39f53b899acf17fe0c786c2cf5097f948ecf53d))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v1.1.0 ([#473](https://github.com/googleapis/java-secretmanager/issues/473)) ([01de433](https://github.com/googleapis/java-secretmanager/commit/01de433cb20db0ca34f39a2eacd2d3c446f5bfba))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v1.2.0 ([#484](https://github.com/googleapis/java-secretmanager/issues/484)) ([0006e34](https://github.com/googleapis/java-secretmanager/commit/0006e34ed6ddc98b4b111b51ec99d29477c12ebd))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v1.3.0 ([#503](https://github.com/googleapis/java-secretmanager/issues/503)) ([2190697](https://github.com/googleapis/java-secretmanager/commit/2190697ac4bce37d5c9a0bcb80db0862792bcfc7))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v1.4.0 ([#525](https://github.com/googleapis/java-secretmanager/issues/525)) ([322a7f6](https://github.com/googleapis/java-secretmanager/commit/322a7f68c6017a017ea58b840be4ea5c6e27ef48))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2 ([#552](https://github.com/googleapis/java-secretmanager/issues/552)) ([ed61ecb](https://github.com/googleapis/java-secretmanager/commit/ed61ecbd643c187a1cb272fdbc499c633fc19155))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.0.1 ([#558](https://github.com/googleapis/java-secretmanager/issues/558)) ([c2699f6](https://github.com/googleapis/java-secretmanager/commit/c2699f665edb48646e8c9251b4f416a5ae68cd13))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.1.0 ([#569](https://github.com/googleapis/java-secretmanager/issues/569)) ([deb6928](https://github.com/googleapis/java-secretmanager/commit/deb6928e421190a437ca1a4f7987c7bc0f65f247))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.10.0 ([#749](https://github.com/googleapis/java-secretmanager/issues/749)) ([1220d7d](https://github.com/googleapis/java-secretmanager/commit/1220d7dc5090f25df74363db3d0b561f6b5115f9))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.2.0 ([#582](https://github.com/googleapis/java-secretmanager/issues/582)) ([f7031c2](https://github.com/googleapis/java-secretmanager/commit/f7031c2eacf09b9bf5c4bb918ff3611535e19659))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.2.1 ([#599](https://github.com/googleapis/java-secretmanager/issues/599)) ([f4ad7ed](https://github.com/googleapis/java-secretmanager/commit/f4ad7ede46502eac5f0cd7e8fd9941e02cb805bb))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.3.0 ([#607](https://github.com/googleapis/java-secretmanager/issues/607)) ([f0c849e](https://github.com/googleapis/java-secretmanager/commit/f0c849e5be202856775dc6d5d7460972b382c53a))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.4.0 ([#626](https://github.com/googleapis/java-secretmanager/issues/626)) ([2c7b4c4](https://github.com/googleapis/java-secretmanager/commit/2c7b4c45c6df9fb5aa3dc03f2c6788263f625030))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.5.0 ([#642](https://github.com/googleapis/java-secretmanager/issues/642)) ([ff7164a](https://github.com/googleapis/java-secretmanager/commit/ff7164a3564dcdf050b031e1764455f72ed746ab))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.5.1 ([#647](https://github.com/googleapis/java-secretmanager/issues/647)) ([b33aec5](https://github.com/googleapis/java-secretmanager/commit/b33aec52ee7cac1e4007063c0ddeac8415f0fb7e))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.6.0 ([#667](https://github.com/googleapis/java-secretmanager/issues/667)) ([81e43ec](https://github.com/googleapis/java-secretmanager/commit/81e43ec2072feef103f9a8e44806847dc4143fb8))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.7.0 ([#686](https://github.com/googleapis/java-secretmanager/issues/686)) ([161430c](https://github.com/googleapis/java-secretmanager/commit/161430c57627c08ad8f70db55894d19e09726913))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.8.0 ([#717](https://github.com/googleapis/java-secretmanager/issues/717)) ([b6d3f9a](https://github.com/googleapis/java-secretmanager/commit/b6d3f9afb98d0f261e9b1c3b0893602d27ab15c9))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v2.9.0 ([#739](https://github.com/googleapis/java-secretmanager/issues/739)) ([6a58447](https://github.com/googleapis/java-secretmanager/commit/6a58447eb25ddc6e9b5a2df45d86dab0e02cedc5))
  * Update dependency com.google.cloud:native-image-support to v0.12.10 ([#731](https://github.com/googleapis/java-secretmanager/issues/731)) ([3e9211a](https://github.com/googleapis/java-secretmanager/commit/3e9211ac7904a4699e4d7a07ce34c0155e277e6f))
  * Update dependency com.google.cloud:native-image-support to v0.12.11 ([#738](https://github.com/googleapis/java-secretmanager/issues/738)) ([afe2969](https://github.com/googleapis/java-secretmanager/commit/afe2969f5d496492dbaf75d1c171363bb68624b6))
  * Update dependency com.google.cloud:native-image-support to v0.12.6 ([#723](https://github.com/googleapis/java-secretmanager/issues/723)) ([a2803ca](https://github.com/googleapis/java-secretmanager/commit/a2803caa7228e9ce057aa1a12ff9ab031dbfea59))
  * Update dependency com.google.cloud:native-image-support to v0.12.7 ([#727](https://github.com/googleapis/java-secretmanager/issues/727)) ([fa8e4ed](https://github.com/googleapis/java-secretmanager/commit/fa8e4ed94a0944c277a10b4520cfce233d422a4a))
  * Update dependency com.google.cloud:native-image-support to v0.12.8 ([#729](https://github.com/googleapis/java-secretmanager/issues/729)) ([1a9d2b8](https://github.com/googleapis/java-secretmanager/commit/1a9d2b87d340d8009615bfcfae527287eeedf38d))
  * Update dependency com.google.cloud:native-image-support to v0.12.9 ([#730](https://github.com/googleapis/java-secretmanager/issues/730)) ([60e8336](https://github.com/googleapis/java-secretmanager/commit/60e8336aaeec4c792ec97f5c64681ef70ef9b085))
  * Update dependency com.google.cloud:native-image-support to v0.13.1 ([#750](https://github.com/googleapis/java-secretmanager/issues/750)) ([68273d1](https://github.com/googleapis/java-secretmanager/commit/68273d152e12093327484adeb8e63ff042e7dec8))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.15.3 ([#395](https://github.com/googleapis/java-secretmanager/issues/395)) ([99aa3a0](https://github.com/googleapis/java-secretmanager/commit/99aa3a098df6dd0857c99323ee0e1d61d64f9b78))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.15.5 ([#402](https://github.com/googleapis/java-secretmanager/issues/402)) ([5d72dad](https://github.com/googleapis/java-secretmanager/commit/5d72dadfe6d2749fcc6656e05ab9b3b1ec639be0))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.15.6 ([#414](https://github.com/googleapis/java-secretmanager/issues/414)) ([cbe8d24](https://github.com/googleapis/java-secretmanager/commit/cbe8d24141a3034a850678df53d1492e84ed41a4))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.15.8 ([#428](https://github.com/googleapis/java-secretmanager/issues/428)) ([eb0714c](https://github.com/googleapis/java-secretmanager/commit/eb0714c3afa4364d443f41c391b4e3b0c0cae62f))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.17.0 ([#468](https://github.com/googleapis/java-secretmanager/issues/468)) ([3980505](https://github.com/googleapis/java-secretmanager/commit/3980505a7b7f791efda6293e73b8be05c8833db2))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.17.1 ([#490](https://github.com/googleapis/java-secretmanager/issues/490)) ([f94276f](https://github.com/googleapis/java-secretmanager/commit/f94276fd3408237ed4a4037352410d9d573625d8))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.17.2 ([#499](https://github.com/googleapis/java-secretmanager/issues/499)) ([2d487b4](https://github.com/googleapis/java-secretmanager/commit/2d487b41975e8ba02a8422abe924d2f5d1db9d0a))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.17.3 ([#510](https://github.com/googleapis/java-secretmanager/issues/510)) ([b10a496](https://github.com/googleapis/java-secretmanager/commit/b10a49637c2150d71f2ff3f7a5e27eca29d55297))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.18.0 ([#604](https://github.com/googleapis/java-secretmanager/issues/604)) ([91bd508](https://github.com/googleapis/java-secretmanager/commit/91bd508eae26eb397e22ff6689c444b49d955dfc))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.18.1 ([#618](https://github.com/googleapis/java-secretmanager/issues/618)) ([35dfb27](https://github.com/googleapis/java-secretmanager/commit/35dfb275ed0cf7f299d7366576c24c9f03f00ce5))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.19.1 ([#630](https://github.com/googleapis/java-secretmanager/issues/630)) ([de25d2a](https://github.com/googleapis/java-secretmanager/commit/de25d2afc1d2b60ca71d94f8e547657751b35059))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.19.2 ([#663](https://github.com/googleapis/java-secretmanager/issues/663)) ([9561bc0](https://github.com/googleapis/java-secretmanager/commit/9561bc0543e06b079de2ffad4fa00af218a101bd))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.19.3 ([#675](https://github.com/googleapis/java-secretmanager/issues/675)) ([1431f9c](https://github.com/googleapis/java-secretmanager/commit/1431f9cd2d3a8a413677c5a9ea2caa187c7b57d1))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.19.4 ([#685](https://github.com/googleapis/java-secretmanager/issues/685)) ([180e572](https://github.com/googleapis/java-secretmanager/commit/180e572a1ad9be4453aca12f3ab92d92f720144f))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.20.0 ([#744](https://github.com/googleapis/java-secretmanager/issues/744)) ([48cb944](https://github.com/googleapis/java-secretmanager/commit/48cb9440758caf1f5b48bdb052a207102338f20e))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.10 ([#724](https://github.com/googleapis/java-secretmanager/issues/724)) ([604a9bc](https://github.com/googleapis/java-secretmanager/commit/604a9bc50dbe6971faabcfe8af1c4fe18a5667e1))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.11 ([#735](https://github.com/googleapis/java-secretmanager/issues/735)) ([6123ddc](https://github.com/googleapis/java-secretmanager/commit/6123ddc964d7fbe9f33d603c06a730a0fd09ea46))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.10 ([#725](https://github.com/googleapis/java-secretmanager/issues/725)) ([6a71213](https://github.com/googleapis/java-secretmanager/commit/6a71213fd203075e7752dfbde51ec7fdea4d4646))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.11 ([#736](https://github.com/googleapis/java-secretmanager/issues/736)) ([d54de52](https://github.com/googleapis/java-secretmanager/commit/d54de52a459ae593f604bed99ba139e373105d17))



### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.12.6](https://github.com/googleapis/python-secret-manager/compare/v2.12.5...v2.12.6) (2022-10-10)

##### Bug Fixes

  * **deps:** Allow protobuf 3.19.5 ([#364](https://github.com/googleapis/python-secret-manager/issues/364)) ([4042d9e](https://github.com/googleapis/python-secret-manager/commit/4042d9e5165391ba5a79bcc5a160c6390098c134))



## October 10, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.3.10](https://github.com/googleapis/java-secretmanager/compare/v2.3.9...v2.3.10) (2022-10-05)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.4 ([#881](https://github.com/googleapis/java-secretmanager/issues/881)) ([6404316](https://github.com/googleapis/java-secretmanager/commit/640431626a308d74c3ea6f76ca597bc84e47612d))



### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.12.5](https://github.com/googleapis/python-secret-manager/compare/v2.12.4...v2.12.5) (2022-09-29)

##### Bug Fixes

  * **deps:** Require protobuf >= 3.20.2 ([#361](https://github.com/googleapis/python-secret-manager/issues/361)) ([4758816](https://github.com/googleapis/python-secret-manager/commit/475881678aaa2a62c097e49d071a870ac0faff4e))



### Node.js

### Changes for [@google-cloud/certificate-manager](https://github.com/googleapis/nodejs-certificate-manager)

#### [0.6.0](https://github.com/googleapis/nodejs-certificate-manager/compare/v0.5.0...v0.6.0) (2022-10-04)

##### Features

  * Added support for Private Trust to Certificate Manager API ([#55](https://github.com/googleapis/nodejs-certificate-manager/issues/55)) ([d9ff953](https://github.com/googleapis/nodejs-certificate-manager/commit/d9ff953cc5ea584970e831171a91b4320832fd3d))



##### Bug Fixes

  * Allow passing gax instance to client constructor ([#49](https://github.com/googleapis/nodejs-certificate-manager/issues/49)) ([f8f86e5](https://github.com/googleapis/nodejs-certificate-manager/commit/f8f86e5b29e5e7dc2896f8bd71c1de8804a0d92b))
  * Better support for fallback mode ([#44](https://github.com/googleapis/nodejs-certificate-manager/issues/44)) ([75c72a9](https://github.com/googleapis/nodejs-certificate-manager/commit/75c72a92beb6890ec4429cb3ecdcf8d40238a175))
  * Change import long to require ([#45](https://github.com/googleapis/nodejs-certificate-manager/issues/45)) ([1dc45d7](https://github.com/googleapis/nodejs-certificate-manager/commit/1dc45d71c836a8f87ed6b4f5fc0a3750034cb84f))
  * Do not import the whole google-gax from proto JS ([#1553](https://github.com/googleapis/nodejs-certificate-manager/issues/1553)) ([#48](https://github.com/googleapis/nodejs-certificate-manager/issues/48)) ([96e4038](https://github.com/googleapis/nodejs-certificate-manager/commit/96e403827bf1ac75c6c4d38f100db9a6f9bd8b35))
  * Preserve default values in x-goog-request-params header ([#51](https://github.com/googleapis/nodejs-certificate-manager/issues/51)) ([13c6ab0](https://github.com/googleapis/nodejs-certificate-manager/commit/13c6ab08318349e4061ff52e4fd6b62c9f3482dd))
  * Remove pip install statements ([#1546](https://github.com/googleapis/nodejs-certificate-manager/issues/1546)) ([#47](https://github.com/googleapis/nodejs-certificate-manager/issues/47)) ([c5002fd](https://github.com/googleapis/nodejs-certificate-manager/commit/c5002fd71850233f5aac6daffb3fb09ace696229))
  * use google-gax v3.3.0 ([96e4038](https://github.com/googleapis/nodejs-certificate-manager/commit/96e403827bf1ac75c6c4d38f100db9a6f9bd8b35))



## October 03, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.3.9](https://github.com/googleapis/java-secretmanager/compare/v2.3.8...v2.3.9) (2022-09-30)

##### Dependencies

  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.7 ([#876](https://github.com/googleapis/java-secretmanager/issues/876)) ([6d296f3](https://github.com/googleapis/java-secretmanager/commit/6d296f37bb1b37d7f93c331b325aecb0a28bdd6e))



#### [2.3.8](https://github.com/googleapis/java-secretmanager/compare/v2.3.7...v2.3.8) (2022-09-28)

##### Dependencies

  * Update dependency cachetools to v5 ([#871](https://github.com/googleapis/java-secretmanager/issues/871)) ([704f6ea](https://github.com/googleapis/java-secretmanager/commit/704f6ea37e7ddd9ef608f944d4e2d5d3123d79c1))
  * Update dependency certifi to v2022.9.24 ([#853](https://github.com/googleapis/java-secretmanager/issues/853)) ([a766f63](https://github.com/googleapis/java-secretmanager/commit/a766f63b951be02389fdebdb2f24955375e07662))
  * Update dependency charset-normalizer to v2.1.1 ([#857](https://github.com/googleapis/java-secretmanager/issues/857)) ([7194dfe](https://github.com/googleapis/java-secretmanager/commit/7194dfed17ae9c42a5b7478b9730521024d4dd89))
  * Update dependency click to v8.1.3 ([#865](https://github.com/googleapis/java-secretmanager/issues/865)) ([cd510ec](https://github.com/googleapis/java-secretmanager/commit/cd510ec93782030909ba0b7f533145933e04c48f))
  * Update dependency gcp-releasetool to v1.8.8 ([#854](https://github.com/googleapis/java-secretmanager/issues/854)) ([fadf34f](https://github.com/googleapis/java-secretmanager/commit/fadf34fa2401689c242d1f4e83375be9d9978641))
  * Update dependency google-api-core to v2.10.1 ([#866](https://github.com/googleapis/java-secretmanager/issues/866)) ([ad6b71b](https://github.com/googleapis/java-secretmanager/commit/ad6b71bee2e77f07465c3be49f71bffc2ea2bbda))
  * Update dependency google-auth to v2.12.0 ([#858](https://github.com/googleapis/java-secretmanager/issues/858)) ([b778051](https://github.com/googleapis/java-secretmanager/commit/b7780512cd0d52e2224c6eaf28e11583e3a7290f))
  * Update dependency google-cloud-core to v2.3.2 ([#855](https://github.com/googleapis/java-secretmanager/issues/855)) ([e82616f](https://github.com/googleapis/java-secretmanager/commit/e82616ff253da33b436f0d01cf72fe3e392ae3eb))
  * Update dependency google-cloud-storage to v2.5.0 ([#859](https://github.com/googleapis/java-secretmanager/issues/859)) ([4b67316](https://github.com/googleapis/java-secretmanager/commit/4b6731664a0e71eab5c6b509b0eb199f76ed428b))
  * Update dependency google-crc32c to v1.5.0 ([#860](https://github.com/googleapis/java-secretmanager/issues/860)) ([ccc2cab](https://github.com/googleapis/java-secretmanager/commit/ccc2cabdd641676f3a269f5eb99a6f1f0f304f82))
  * Update dependency googleapis-common-protos to v1.56.4 ([#856](https://github.com/googleapis/java-secretmanager/issues/856)) ([bcf0af9](https://github.com/googleapis/java-secretmanager/commit/bcf0af9b7f29fd9bcc57a06a01a3b7dbcef8cd0b))
  * Update dependency importlib-metadata to v4.12.0 ([#861](https://github.com/googleapis/java-secretmanager/issues/861)) ([c91100b](https://github.com/googleapis/java-secretmanager/commit/c91100b1ab1f5d9513e816679c87033e5f6834e4))
  * Update dependency jeepney to v0.8.0 ([#862](https://github.com/googleapis/java-secretmanager/issues/862)) ([ea77200](https://github.com/googleapis/java-secretmanager/commit/ea77200360d19e349932046e13b84adc49dfe5fb))
  * Update dependency markupsafe to v2.1.1 ([#863](https://github.com/googleapis/java-secretmanager/issues/863)) ([2f83987](https://github.com/googleapis/java-secretmanager/commit/2f83987545d16079dfb0f9ee38127f8cf5c71b4e))
  * Update dependency protobuf to v3.20.2 ([#864](https://github.com/googleapis/java-secretmanager/issues/864)) ([8745302](https://github.com/googleapis/java-secretmanager/commit/8745302f573b73970b98609863e1210f7eeb39c4))
  * Update dependency protobuf to v4 ([#872](https://github.com/googleapis/java-secretmanager/issues/872)) ([9604cf1](https://github.com/googleapis/java-secretmanager/commit/9604cf1223cfe35dac4e2969155c6f376b1d3d36))
  * Update dependency pyjwt to v2.5.0 ([#867](https://github.com/googleapis/java-secretmanager/issues/867)) ([537a64d](https://github.com/googleapis/java-secretmanager/commit/537a64d3329466bb5782a59a6dfab65c1f25ae92))
  * Update dependency requests to v2.28.1 ([#868](https://github.com/googleapis/java-secretmanager/issues/868)) ([92bdf04](https://github.com/googleapis/java-secretmanager/commit/92bdf0421a1d130a5c7ba7fdf1899fdbb99a0151))
  * Update dependency typing-extensions to v4.3.0 ([#869](https://github.com/googleapis/java-secretmanager/issues/869)) ([ca16bc0](https://github.com/googleapis/java-secretmanager/commit/ca16bc03e3de29b2f46b29b0808279fcf8481256))
  * Update dependency zipp to v3.8.1 ([#870](https://github.com/googleapis/java-secretmanager/issues/870)) ([7f543f6](https://github.com/googleapis/java-secretmanager/commit/7f543f657707a9143c23a0ad9427d109a2bc2757))



## September 26, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.7.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.6.0...secretmanager/v1.7.0) (2022-09-21)

##### Features

  * **secretmanager:** remove beta client that no longer has source protos ([9f303f9](https://github.com/googleapis/google-cloud-go/commit/9f303f9efc2e919a9a6bd828f3cdb1fcb3b8b390))



#### [1.6.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.5.0...secretmanager/v1.6.0) (2022-09-19)

##### Features

  * **secretmanager:** start generating proto message types ([563f546](https://github.com/googleapis/google-cloud-go/commit/563f546262e68102644db64134d1071fc8caa383))



### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.3.7](https://github.com/googleapis/java-secretmanager/compare/v2.3.6...v2.3.7) (2022-09-22)

##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.14 ([#846](https://github.com/googleapis/java-secretmanager/issues/846)) ([f2985b5](https://github.com/googleapis/java-secretmanager/commit/f2985b589e2e107f346f2264c837890f1fae8bfc))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.14 ([#847](https://github.com/googleapis/java-secretmanager/issues/847)) ([27f5fa8](https://github.com/googleapis/java-secretmanager/commit/27f5fa8836ecb53b617588e33f48818b773ad65f))



#### [2.3.6](https://github.com/googleapis/java-secretmanager/compare/v2.3.5...v2.3.6) (2022-09-21)

##### Dependencies

  * Update dependency org.junit.vintage:junit-vintage-engine to v5.9.1 ([#842](https://github.com/googleapis/java-secretmanager/issues/842)) ([4bec542](https://github.com/googleapis/java-secretmanager/commit/4bec542060b480f3e75f0c9dbd39ed24d4c0892f))



#### [2.3.5](https://github.com/googleapis/java-secretmanager/compare/v2.3.4...v2.3.5) (2022-09-20)

##### Dependencies

  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.6 ([#832](https://github.com/googleapis/java-secretmanager/issues/832)) ([a2595c8](https://github.com/googleapis/java-secretmanager/commit/a2595c8f98fef63844269d3080cad81d06aa5a9e))



### Node.js

### Changes for [@google-cloud/secret-manager](https://github.com/googleapis/nodejs-secret-manager)

#### [4.1.3](https://github.com/googleapis/nodejs-secret-manager/compare/v4.1.2...v4.1.3) (2022-09-22)

##### Bug Fixes

  * Preserve default values in x-goog-request-params header ([#403](https://github.com/googleapis/nodejs-secret-manager/issues/403)) ([af162f0](https://github.com/googleapis/nodejs-secret-manager/commit/af162f09e23d2e850c33bf0af8f77e9302b44e61))



## September 19, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.3.4](https://github.com/googleapis/java-secretmanager/compare/v2.3.3...v2.3.4) (2022-09-15)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.3 ([#833](https://github.com/googleapis/java-secretmanager/issues/833)) ([a462455](https://github.com/googleapis/java-secretmanager/commit/a462455a2c0f63479cff12a5f19a7d5b2cd244d8))



## September 12, 2022

Feature

Cloud Secret Manager is now available in the following region:

  * me-west1



For more information, see [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.3.3](https://github.com/googleapis/java-secretmanager/compare/v2.3.2...v2.3.3) (2022-09-09)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.2 ([#827](https://github.com/googleapis/java-secretmanager/issues/827)) ([b2162a7](https://github.com/googleapis/java-secretmanager/commit/b2162a76e1def8116fc7c01cd95000449f2c9503))



#### [2.3.2](https://github.com/googleapis/java-secretmanager/compare/v2.3.1...v2.3.2) (2022-09-06)

##### Dependencies

  * Update dependency com.google.protobuf ([6bf4745](https://github.com/googleapis/java-secretmanager/commit/6bf474519e658e56d015c661574c84c501c2c9b8))



### Node.js

### Changes for [@google-cloud/secret-manager](https://github.com/googleapis/nodejs-secret-manager)

#### [4.1.2](https://github.com/googleapis/nodejs-secret-manager/compare/v4.1.1...v4.1.2) (2022-09-01)

##### Bug Fixes

  * Allow passing gax instance to client constructor ([#399](https://github.com/googleapis/nodejs-secret-manager/issues/399)) ([02d820f](https://github.com/googleapis/nodejs-secret-manager/commit/02d820fd521c58263eaa46e98d6b98bac8d973d3))
  * Do not import the whole google-gax from proto JS ([#1553](https://github.com/googleapis/nodejs-secret-manager/issues/1553)) ([#398](https://github.com/googleapis/nodejs-secret-manager/issues/398)) ([e16be85](https://github.com/googleapis/nodejs-secret-manager/commit/e16be85ab62f69a5680ec09149f9fade8ddcaf54))



## September 05, 2022

Feature

Secret Manager now supports using annotations to define custom metadata about the secret. The metadata in an annotation can be small or large, structured or unstructured, and can include characters. You can add annotations to secrets when you create a new secret or when you edit an existing secret. For information, see [Creating and managing annotations](https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-annotations).

## August 29, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.12.4](https://github.com/googleapis/python-secret-manager/compare/v2.12.3...v2.12.4) (2022-08-24)

##### Documentation

  * **samples:** Added sample for creating Secret with UserManaged replication ([#328](https://github.com/googleapis/python-secret-manager/issues/328)) ([c5fe7ff](https://github.com/googleapis/python-secret-manager/commit/c5fe7ff0f2914e97f653e28bd0c4a9e155a8942f))



## August 22, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.12.3](https://github.com/googleapis/python-secret-manager/compare/v2.12.2...v2.12.3) (2022-08-11)

##### Bug Fixes

  * **deps:** allow protobuf < 5.0.0 ([#335](https://github.com/googleapis/python-secret-manager/issues/335)) ([34c5858](https://github.com/googleapis/python-secret-manager/commit/34c5858cbd1971f270e73d2af3b45ecaa4adb7e2))
  * **deps:** require proto-plus >= 1.22.0 ([34c5858](https://github.com/googleapis/python-secret-manager/commit/34c5858cbd1971f270e73d2af3b45ecaa4adb7e2))



## August 15, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.3.1](https://github.com/googleapis/java-secretmanager/compare/v2.3.0...v2.3.1) (2022-08-03)

##### Bug Fixes

  * enable longpaths support for windows test ([#1485](https://github.com/googleapis/java-secretmanager/issues/1485)) ([#804](https://github.com/googleapis/java-secretmanager/issues/804)) ([892845c](https://github.com/googleapis/java-secretmanager/commit/892845cda168071dca0f8bda29bd878c07f9386d))



##### Dependencies

  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3 ([#811](https://github.com/googleapis/java-secretmanager/issues/811)) ([9e84f35](https://github.com/googleapis/java-secretmanager/commit/9e84f356a3610b16d9988ebc112d4766b289aeb3))
  * update dependency com.google.protobuf:protobuf-java-util to v3.21.3 ([#808](https://github.com/googleapis/java-secretmanager/issues/808)) ([17cc2d2](https://github.com/googleapis/java-secretmanager/commit/17cc2d2fa1c1d12906d088691f6a86638e9a2404))
  * update dependency com.google.protobuf:protobuf-java-util to v3.21.4 ([#809](https://github.com/googleapis/java-secretmanager/issues/809)) ([5ae26ff](https://github.com/googleapis/java-secretmanager/commit/5ae26fff4de3be3fe66ae94c984c0557099bf29e))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.13 ([#802](https://github.com/googleapis/java-secretmanager/issues/802)) ([0749cd2](https://github.com/googleapis/java-secretmanager/commit/0749cd2d9fc3f29e9b49e7e76a7fb88af316e5d4))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.13 ([#803](https://github.com/googleapis/java-secretmanager/issues/803)) ([e2d693b](https://github.com/googleapis/java-secretmanager/commit/e2d693b6e2d734a389df61e5b97642d6adbb732d))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.9.0 ([#810](https://github.com/googleapis/java-secretmanager/issues/810)) ([5c5bfb1](https://github.com/googleapis/java-secretmanager/commit/5c5bfb1c1b0185c3c3304c267a633d4354484795))



### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.12.2](https://github.com/googleapis/python-secret-manager/compare/v2.12.1...v2.12.2) (2022-08-08)

##### Documentation

  * **samples:** add sample to update secret with alias ([#307](https://github.com/googleapis/python-secret-manager/issues/307)) ([dab8e16](https://github.com/googleapis/python-secret-manager/commit/dab8e166a77aff67b6b750f5b1c753f0b2c17169))



## August 01, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.12.1](https://github.com/googleapis/python-secret-manager/compare/v2.12.0...v2.12.1) (2022-07-26)

##### Bug Fixes

  * wrong package name google-cloud-secretmanager ([#325](https://github.com/googleapis/python-secret-manager/issues/325)) ([1693fd1](https://github.com/googleapis/python-secret-manager/commit/1693fd1bda20e487995adb84d030c1903491388c))



## July 25, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-secret-manager](https://github.com/googleapis/python-secret-manager)

#### [2.12.0](https://github.com/googleapis/python-secret-manager/compare/v2.11.1...v2.12.0) (2022-07-16)

##### Features

  * add audience parameter ([bf4130e](https://github.com/googleapis/python-secret-manager/commit/bf4130efb313041e3451ba0e10181aa2f0c05987))



##### Bug Fixes

  * **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#320](https://github.com/googleapis/python-secret-manager/issues/320)) ([311a877](https://github.com/googleapis/python-secret-manager/commit/311a8779c3311aef4d10b85a1e1b2462c5aefff4))
  * require python 3.7+ ([#317](https://github.com/googleapis/python-secret-manager/issues/317)) ([971a802](https://github.com/googleapis/python-secret-manager/commit/971a802403e44ef98a4250789f825024c67b9d3f))



## July 21, 2022

Feature

Secret Manager now supports accessing secret versions using aliases. For information, see [Assign an alias to a secret version](https://docs.cloud.google.com/secret-manager/docs/managing-secret-versions#alias).

## July 04, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-secretmanager](https://github.com/googleapis/java-secretmanager)

#### [2.3.0](https://github.com/googleapis/java-secretmanager/compare/v2.2.0...v2.3.0) (2022-07-01)

##### Features

  * Enable REST transport for most of Java and Go clients ([#790](https://github.com/googleapis/java-secretmanager/issues/790)) ([d51c8fa](https://github.com/googleapis/java-secretmanager/commit/d51c8fa85243d4b71b805a67141168898542a851))



##### Documentation

  * **sample:** clean up README for native image sample ([#785](https://github.com/googleapis/java-secretmanager/issues/785)) ([67260d7](https://github.com/googleapis/java-secretmanager/commit/67260d74d7c5f05dc08957267ae809eb3ea66281))



##### Dependencies

  * update dependency com.google.cloud:google-cloud-shared-dependencies to v2.13.0 ([#789](https://github.com/googleapis/java-secretmanager/issues/789)) ([71aae1d](https://github.com/googleapis/java-secretmanager/commit/71aae1d94136082ed323a6591e5cfe6a0d02875c))
  * update dependency com.google.protobuf:protobuf-java-util to v3.21.0 ([#779](https://github.com/googleapis/java-secretmanager/issues/779)) ([d38f1db](https://github.com/googleapis/java-secretmanager/commit/d38f1dbd5fea21d3edc06045e5c892313a0524b4))
  * update dependency com.google.protobuf:protobuf-java-util to v3.21.1 ([#780](https://github.com/googleapis/java-secretmanager/issues/780)) ([6c613da](https://github.com/googleapis/java-secretmanager/commit/6c613daee4f406e501ad92742fc7dae0d4172298))
  * update dependency com.google.protobuf:protobuf-java-util to v3.21.2 ([#791](https://github.com/googleapis/java-secretmanager/issues/791)) ([d7d4ea9](https://github.com/googleapis/java-secretmanager/commit/d7d4ea9d26ca5b1fe44d052b8f7c1f5527a1dabc))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.12 ([#787](https://github.com/googleapis/java-secretmanager/issues/787)) ([a2e0e97](https://github.com/googleapis/java-secretmanager/commit/a2e0e977ae70f38c8cf1e61d4245a34ebd0d1af5))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.12 ([#788](https://github.com/googleapis/java-secretmanager/issues/788)) ([8662fe6](https://github.com/googleapis/java-secretmanager/commit/8662fe687369eab23a185eba0bf9a48110d5856b))



## February 03, 2022

Feature

Secret manager now supports [data checksums](https://docs.cloud.google.com/secret-manager/docs/data-integrity) when adding or accessing a secret version.

## December 14, 2021

Feature

[Access Transparency](https://docs.cloud.google.com/cloud-provider-access-management/access-transparency/docs/overview) supports Secret Manager in Preview stage.

## November 16, 2021

Change

Secret Manager is now available in the [Santiago (southamerica-west1)](https://docs.cloud.google.com/secret-manager/docs/locations#south-america) region.

## November 05, 2021

Change

Secret Manager filtering support to customize the output of ListSecrets and ListSecretVersions is now generally available. For more information, see [Filtering](https://docs.cloud.google.com/secret-manager/docs/filtering).

## August 27, 2021

Feature

Cloud Audit Logs and Platform Logs are now available directly in the Secret Manager UI. See the [Secret Manager page](https://console.cloud.google.com/security/secret-manager) to learn more.

## August 24, 2021

Feature

The [Analyze Policy API](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy) now support Secret Manager types: * `secretmanager.googleapis.com/Secret` * `secretmanager.googleapis.com/SecretVersion`

## August 03, 2021

Feature

Secret Manager is now available in `northamerica-northeast2` (Toronto). See [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations) for more information.

## July 20, 2021

Change

Secret Manager now supports using a filter to customize the output of `ListSecrets` and `ListSecretVersions`. For more information, see [Filtering](https://docs.cloud.google.com/secret-manager/docs/filtering).

Feature

[ETags for optimistic concurrency control](https://docs.cloud.google.com/secret-manager/docs/etags) are generally available (GA) in Secret Manager.

## July 01, 2021

Feature

Secret Manager now offers a limited number of free resources as part of the [Google Cloud Free](https://docs.cloud.google.com/free/docs/gcp-free-tier) program.

For more details on free resources, see [Secret Manager pricing](https://cloud.google.com/secret-manager/pricing).

## June 30, 2021

Feature

Secret Manager now has a guide for rotating secrets and binding a secret version to your application.

To learn more, see [Rotation of secrets](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations).

## June 29, 2021

Feature

Secret Manager is now available in `asia-south2` (Delhi). See [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations) for more information.

Feature

Secret Manager now has a guide for using Cloud Asset Inventory to identify and audit secrets.

To learn more, see [Analyze secrets with Cloud Asset Inventory](https://docs.cloud.google.com/secret-manager/docs/analyze-resources).

## June 21, 2021

Feature

Secret Manager is now available in `australia-southeast2` (Melbourne). See [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations) for more information.

## May 24, 2021

Change

The [Secret Manager SLA](https://cloud.google.com/secret-manager/sla) has been updated.

## May 14, 2021

Feature

Secret Manager now supports etags for optimistic concurrency control. This feature is available in Preview.

See [Etags](https://docs.cloud.google.com/secret-manager/docs/etags) to learn more.

## May 12, 2021

Feature

Secret Manager integration with Cloud Run

Cloud Run now provides UI, command line, and YAML support for [using secrets](https://docs.cloud.google.com/run/docs/configuring/secrets). This feature is available in Preview.

## April 02, 2021

Announcement

Secret Manager now has a Best Practices guide.

Learn more about [Secret Manager best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).

## March 31, 2021

Feature

Secret Manager Event Notifications is generally available.

Secret Manager Event Notifications lets you configure secrets to send messages to Pub/Sub topics whenever a change is made to the secret or one of its versions.

Learn more at [enabling event notifications](https://docs.cloud.google.com/secret-manager/docs/event-notifications).

## March 30, 2021

Feature

Secret Manager Rotation is generally available.

Secret Manager Rotation sends messages to Pub/Sub topics based on the provided rotation frequency and rotation time. 

Learn more at [creating and managing rotation policies](https://docs.cloud.google.com/secret-manager/docs/secret-rotation).

Feature

Secret Manager Expiration is generally available.

Learn more at [creating and managing expiring secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-expiring-secrets).

## March 24, 2021

Feature

The `europe-central2` region is now available. See [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations) for more information.

## March 09, 2021

Feature

Secret Manager support for Customer-Managed Encryption Keys (CMEK) is now generally available. 

Learn more by reading [Enabling CMEK in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

## February 25, 2021

Feature

Event notifications is now available in Preview. 

Event notifications sends information about changes to your secrets and secret versions to Pub/Sub. These notifications can be used to trigger arbitrary workflows, such as restarting an application when a new secret version is added, or notifying security engineers when a secret is deleted. 

Learn more at [Enabling event notifications](https://docs.cloud.google.com/secret-manager/docs/event-notifications).

## January 28, 2021

Feature

Secret Manager Expiration is available for all customers via public preview.

Learn more at [Creating and Managing Expiring Secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-expiring-secrets).

## November 02, 2020

Feature

Secret Manager support for Customer-Managed Encryption Keys (CMEK) is available to all customers via public preview.

Learn more at [Enabling CMEK in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

## October 29, 2020

Feature

Secret Manager Integration with Cloud Asset Inventory

Secret Manager metadata can be queried in Cloud Asset Inventory (CAI). This integration enables users to query Secret Manager metadata at multiple granularities (project, folder, organization), query data over time, and export to other systems. 

Learn more at [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types).

## September 21, 2020

Feature

Secret Manager is available in all regions. 

See more details at [Secret Manager locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## July 20, 2020

Feature

Secret Manager adds support for the following curated IAM roles:

  * Secret Manager Secret Version Adder (`roles/secretmanager.secretVersionAdder` )
  * Secret Manager Secret Version Manager (`roles/secretmanager.secretVersionManager`)



To learn more, see [IAM and access control](https://docs.cloud.google.com/secret-manager/docs/access-control).

## July 13, 2020

Feature

Secret Manager resources can now be stored in the `australia-southeast1` region. To learn more, see [Locations](https://docs.cloud.google.com/secret-manager/docs/locations).

## March 11, 2020

Feature

[Secret Manager](https://docs.cloud.google.com/secret-manager) is generally available

## December 10, 2019

Feature

Launch of Secret Manager to Beta. Secret Manager provides a secure and convenient way to store API keys, passwords, certificates, and other credentials. Secret Manager is accessible via:

  * [REST API](https://docs.cloud.google.com/secret-manager/docs/reference/rest)
  * [RPC API](https://docs.cloud.google.com/secret-manager/docs/reference/rpc)
  * [Cloud Console user interface](https://docs.cloud.google.com/secret-manager/docs/quickstart-secret-manager-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
