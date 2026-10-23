---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/release-notes/
title: Config Sync release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:08.582617+00:00
---

# Config Sync release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/resources)



Send feedback 

#  Config Sync release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Config Sync. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecations. Previously, Config Sync and Policy Controller were released together. If you're looking for Policy Controller announcements after version 1.18.0, go to the [Policy Controller release notes](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/release-notes). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/anthosconfig-release-notes.xml) directly. 

## September 21, 2026

1.25.1

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.25.1

Fixed

Fixed an issue with duration histograms to ensure accurate latency reporting for sub-second operations.

## August 24, 2026

1.25.0

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.25.0

Feature

You can now disable monitoring for specific custom `RootSync` or `RepoSync` objects by setting the `spec.monitoring.enabled` field to `false`. This disables metric telemetry collection and exporting for that reconciler, which can help reduce cluster resource consumption. For more information, see [Disable monitoring](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync#disable-monitoring).

## July 27, 2026

1.24.3

Change

Upgraded bundled Helm version from v3.20.2 to [v3.21.1](https://github.com/helm/helm/releases/tag/v3.21.1) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

1.24.3

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

## June 25, 2026

1.24.2

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.24.2

Change

Upgraded the Open Telemetry image from 0.150.0 to 0.152.0 to pick up vulnerability fixes. To understand the changes in each release, review the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

## June 04, 2026

1.24.1

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

## May 11, 2026

1.24.0

Fixed

Removed the readinessProbe and deprecated health checks for the otel-agent sidecar to align its configuration with other containers.

1.24.0

Feature

Changed `logLevel` configuration to support values as low as -10 to reduce log verbosity in Config Sync containers.

1.24.0

Feature

Added support for token-based authentication when using OCI images from third-party registries.

## March 26, 2026

1.23.3

Breaking

Upgraded the Open Telemetry image from v0.127.0 to v0.133.0 to pick up vulnerability fixes. This change promotes the `pkg.translator.prometheus.NormalizeName` feature gate to stable. To understand the changes in each release, review the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

1.23.3

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.23.3

Change

Upgraded bundled Helm version from v3.18.6 to [v3.20.0](https://github.com/helm/helm/releases/tag/v3.20.0) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

## February 26, 2026

1.23.2

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

## January 29, 2026

1.23.1

Breaking

Upgraded the Open Telemetry image from v0.119.0 to v0.127.0. This version removes the deprecated OpenCensus receiver. This change impacts only custom metric solutions that use the OpenCensus receiver. To understand the changes in each release, review the [change logs](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases)

1.23.1

Fixed

Resolved an issue where metrics for deleted ResourceGroups continued to show outdated values.

1.23.1

Change

Upgraded bundled Helm version from v3.15.3 to [3.18.6](https://github.com/helm/helm/releases/tag/v3.18.6) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

1.23.1

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

## December 04, 2025

1.23.0

Announcement

You can now control the scheduling of Config Sync pods using the Kubernetes-native resource [MutatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/). For more information, see [Customize node placement of Config Sync system pods](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/custom-node-placement) to get started.

1.23.0

Change

Config Sync's internal observability library has been updated from OpenCensus to OpenTelemetry, improving performance and aligning with industry standards with no breaking changes to metrics or functionality.

1.23.0

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.23.0

Change

Config Sync now supports the `client.lifecycle.config.k8s.io/mutation: ignore` annotation for compatibility with other controllers. This enhancement provides more consistent behavior and correctly reports the resource status.

## October 09, 2025

1.22.2

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

## September 18, 2025

1.22.1

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.22.1

Change

Upgraded the Open Telemetry image from v0.118.0 to v0.119.0 to pick up vulnerability fixes. To understand the changes in each release, review the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

## September 02, 2025

1.22.0

Announcement

Config Sync is now available as part of the standard GKE offering and no longer requires GKE Enterprise. For more details on the removal of GKE Enterprise, see the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#September_02_2025).

## August 21, 2025

1.22.0

Feature

Config Sync now supports syncing from Secure Source Manager git repositories. For more information, see [Grant access to Git](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

1.22.0

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.22.0

Announcement

Announcing experimental features: help shape the future of Config Sync features by providing direct feedback.

  * Introducing PostSync, a feature that lets you run custom actions like cleanup scripts or notifications right after your configurations are synced. We're looking for your feedback to shape its future! Check out the [Post Sync discussion](https://github.com/GoogleContainerTools/kpt-config-sync/discussions/1830) to share your thoughts, suggestions, and bug reports before December 1, 2025.



## July 24, 2025

1.21.3

Fixed

Fixed a regression introduced in 1.21.0 that occasionally caused Config Sync to become stuck when applying [mutation ignored objects](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/concepts/configs#ignoring).

1.21.3

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.21.3

Fixed

Fixed an issue where Config Sync waited longer than intended between retry attempts after failing to sync from Helm and OCI sources.

1.21.3

Fixed

Updated the git-sync image from v4.3.0 to v4.4.2, which fixes an issue that could cause the git-sync container to crash loop. For more information see [git-sync releases](https://github.com/kubernetes/git-sync/releases).

## June 26, 2025

1.21.2

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.21.2

Fixed

Fixed an issue which prevented a resource conflict metric from being recorded in rare cases.

1.21.2

Fixed

Fixed an issue with the nomos CLI which prevented setting up autocomplete by using the `nomos completion` command. For more information see [Use the nomos command-line tool](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/nomos-command).

## May 29, 2025

1.21.1

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

## May 01, 2025

1.21.0

Breaking

Installing Policy Controller through the ConfigManagement API is no longer supported. For instructions installing Policy Controller, see [Installing Policy Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/policy-controller/docs/how-to/installing-policy-controller). For instructions migrating existing Policy Controller instances, see [Migrate from the ConfigManagement API to the PolicyController API](https://docs.cloud.google.com/kubernetes-engine/enterprise/policy-controller/docs/how-to/migrate-policy-controller-api). This note was added on May 16, 2025.

1.21.0

Fixed

Fixed an issue impacting the [Ignore object mutations](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/concepts/configs#ignoring) feature. The `client.lifecycle.config.k8s.io/mutation: ignore` annotation was not always effective, causing Config Sync to potentially overwrite changes made directly to annotated resources in the cluster. Config Sync now correctly ignores mutations on these resources.

1.21.0

Feature

The `nomos vet` command now supports a `--threshold` flag to proactively validate the number of objects in your Config Sync repository. You can use this flag in validation pipelines to prevent sync failures caused by exceeding the underlying `etcd` size limits when your repository contains a large number of objects. For more information, see [Enforce the maximum number of objects to sync](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/nomos-command#threshold).

1.21.0

Breaking

The Config Sync auto-upgrades feature is now unavailable. You can no longer configure auto-upgrade settings and must [manually upgrade the Config Sync version](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/upgrade-config-sync#manually-upgrade). If you currently use auto-upgrades, you must first [disable auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/upgrade-config-sync#disable-auto-upgrades) before you can manually update Config Sync.

1.21.0

Breaking

Upgraded the Open Telemetry Collector image from v0.103.0 to v0.118.0. This upgrade includes a breaking change where the default OTLP component endpoint is now `localhost` instead of `0.0.0.0`. You will be impacted only if you use a customized configuration for the built-in Otel Collector within Config Sync, and you can explicitly specify `0.0.0.0` for endpoints to ensure that your monitoring solution continues to function correctly. To understand the changes in each release, review the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

1.21.0

Fixed

Fixed an issue where drift prevention incorrectly blocked modifications of abandoned resources.

1.21.0

Fixed

Fixed an issue preventing ResourceGroup objects from being garbage collected when their corresponding RootSync or RepoSync objects were deleted.

1.21.0

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

1.21.0

Feature

Deleting a RootSync or RepoSync now removes its management metadata from all managed objects. This allows objects to be adopted by their new managers, simplifying the procedure for splitting a large configuration repository across multiple RootSync or RepoSync objects. For more information, see [Break up a repository into multiple repositories](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/breaking-up-repo).

1.21.0

Fixed

Fixed several issues to improve ResourceGroup status reporting and reliability.

## March 27, 2025

1.20.3

Change

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

## March 06, 2025

1.20.2

Fixed

Fixed an issue where ConfigManagement uninstall could get stuck when Policy Controller was enabled via ConfigManagement. This was caused by Policy Controller finalizers not being properly removed during the uninstallation process.

## January 30, 2025

1.20.1

Fixed

Fixed an issue that was causing Container Registry and Artifact Registry authentication tokens to expire before being refreshed. For more information, see known issue [Unable to generate access token for OCI source](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/known-issues#oci-access-token).

1.20.1

Fixed

Fixed an issue that incorrectly reported managed resources as `"Not Found"` when an API Service backend became unhealthy. For more information, see known issue [API discovery errors can cause managed objects to incorrectly be marked as "Not Found"](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/known-issues#api-discovery-errors).

## December 05, 2024

1.20.0

Breaking

Improved the manual installation process for Config Sync. When [you install Config Sync manually using kubectl (not recommended)](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/installing-kubectl), Config Sync is now deployed directly without relying on the Config Management Operator. This change results in simplified architecture and reduced resource use on your cluster. If you manually installed Config Sync using kubectl, follow the [guide to uninstall the Config Management Operator](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/installing-kubectl#upgrade) before you upgrade.

1.20.0

Breaking

Hierarchy Controller is no longer available to install. If Hierarchy Controller is still configured, Config Sync upgrades are blocked. To upgrade Config Sync, [disable Hierarchy Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/migrate-hierarchy-controller). This release note was updated on May 9, 2025. The previous note suggested [Hierarchical Namespace Controller (HNC)](https://github.com/kubernetes-retired/hierarchical-namespaces) as a migration option, but HNC is now archived.

1.20.0

Feature

When you use Config Sync to manage configurations that are stored in OCI repositories (such as Artifact Registry), you can now enhance your security posture with custom signature verification. Config Sync integrates with your existing signature verification server deployed as a Kubernetes admission webhook, which helps ensure only trusted OCI images are used in your deployments. See the [Sync OCI artifacts guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/sync-oci-artifacts-from-artifact-registry#verify-oci) for setup instructions.

1.20.0

Feature

Introduced a new field for stopping and resuming syncing. This field is available on clusters with Config Sync [auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/upgrade-config-sync#auto-upgrade-config) or with Config Sync version 1.20.0. The new field makes it easier to pause syncing by setting the [`spec.configSync.stopSyncing`](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/reference/gcloud-apply-fields#config_sync) field to `true`.

1.20.0

Fixed

Fixed an issue that could cause sync delays due to retry backoff problems. This fix helps ensure more timely and consistent updates to your clusters.

1.20.0

Fixed

Upgraded the `git-sync` dependency from v4.2.4 to v4.3.0 to pick up a fix for [lingering Git lock files](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/known-issues#ligering-git-lock) and other vulnerability fixes.

1.20.0

Change

To optimize resource use, Config Sync installations managed through Fleet no longer include the ConfigManagement Operator or the `ConfigManagement` CRD. These components are automatically removed when you upgrade to version 1.20.0 or later. This change reduces Config Sync's resource consumption in your cluster. See [Config Sync architecture](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/concepts/architecture) for details.

1.20.0

Fixed

Fixed a bug that prevented the `applyset.kubernetes.io/part-of` label from being correctly removed from managed objects when they were no longer managed by Config Sync. This fix improves the accuracy of label information.

## October 17, 2024

1.19.2

Fixed

Improved the security of the `git-sync` container by upgrading the base image to address known vulnerabilities.

## September 26, 2024

1.19.1

Feature

Config Sync now supports GitHub App authentication for GitHub repositories. See [Grant access to Git](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/installing-config-sync#git-creds-secret) for more information. This release note was added on October 4, 2024.

1.19.1

Announcement

You can now configure Config Sync [fleet defaults](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/installing-config-sync#configure-fleet) with gcloud commands starting in gcloud version 494.0.0. See the [Config Sync gcloud documentation](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/config-management) for reference.

1.19.1

Change

Upgraded the `git-sync` dependency from v4.2.3 to v4.2.4.

## August 29, 2024

1.19.0

Breaking

The `spec.git` and `spec.enableLegacyFields` fields of the ConfigManagement object have been removed. The `spec.enableMultiRepo` field is now set to `true` by default, automatically enabling the RootSync API. [RootSync](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields) provides the same core functionality, along with additional features. 

If you currently configure Git settings within a ConfigManagement object, to avoid disruptions, before upgrading you **must** [migrate this configuration to a RootSync object](https://docs.cloud.google.com/anthos-config-management/docs/how-to/migrate-multi-repo).

1.19.0

Breaking

Terraform version 5.41.0 introduced a new field to the `google_gke_hub_feature_membership`: `config_sync.enabled`. Because the default value of this field is `false`, it causes Config Sync installations to fail when Terraform is upgraded to version 5.41.0. For more information, including workarounds, see the [known issue entry](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/known-issues#config-sync-enabled-false-terraform). This issue affects all supported Config Sync versions. This note was added on September 11, 2024.

1.19.0

Announcement

Hierarchy Controller will not be available after December, 2024. After December, 2024, you can't install Hierarchy Controller and Config Sync will be blocked from upgrades if Hierarchy Controller is configured as a `configmanagement` fleet feature or through the `ConfigManagement` API. To continue using similar functionality, [migrate from Hierarchy Controller to Hierarchical Namespace Controller](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/migrate-hierarchy-controller). This note was added on September 6, 2024 and edited on September 9, 2024 for clarification.

1.19.0

Feature

Optimized Config Sync resource usage by implementing watch filtering with [ApplySet](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/reference/labels-and-annotations) ("applyset.kubernetes.io/" labels and annotations). This reduces reconciler Deployment memory consumption by limiting events and cached objects to those relevant to the managed package. For more information on the resource usage optimization, see [Config Sync Watch Filtering v1.18 vs v1.19](https://github.com/GoogleContainerTools/kpt-config-sync/tree/main/docs/watch-filtering).

1.19.0

Change

Upgraded the Open Telemetry image from 0.102.0 to 0.103.0 to pick up vulnerability fixes. To understand the changes in each release, review the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

1.19.0

Feature

Config Sync now enables loading files from directories beyond the Kustomize root during rendering. For more information, refer to [Configure Kubernetes with Kustomize](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/concepts/kustomize).

1.19.0

Fixed

Fixed some inaccuracies in status updates and metrics reports.

1.19.0

Change

Upgraded bundled Helm version from v3.14.4 to [v3.15.3](https://github.com/helm/helm/releases/tag/v3.15.3) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

1.19.0

Feature

Improved support for [private registries](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/updating-private-registry). If you've configured a private registry for your cluster, Config Sync now automatically detects and updates the image references within its reconciler Deployments to point to the corresponding images in your private registry.

## July 25, 2024

1.18.3

Fixed

Fixed a regression in 1.17.3 causing SSH authentication failures with GitHub. This was resolved by upgrading the `git-sync` dependency from v4.2.1 to v4.2.3. For more details, please refer to [Fixed: Git SSH Authentication Failure with GitHub](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/known-issues#git-ssh-auth-username).

1.18.3

Fixed

Fixed a regression introduced in 1.17.0 that caused Config Sync to crash when connecting to certain Kubernetes clusters. GKE clusters were not affected by this issue. For more details, please refer to [Fixed: Config Sync reconciler is crashlooping](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/known-issues#config-sync-kubeconfig).

1.18.3

Change

Improved error handling in the `oci-sync` container by adding exponential backoff.

1.18.3

Change

Upgraded bundled Kustomize version from v5.3.0 to [v5.4.2](https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize%2Fv5.4.2) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/kubernetes-sigs/kustomize/releases).

## June 27, 2024

1.18.2

Fixed

Resolved an issue that prevented the `declared_resources` metric from decrementing when an object became unmanaged by Config Sync.

1.18.2

Change

Upgraded the Open Telemetry image from v0.99.0 to v0.102.0 to pick up vulnerability fixes. To understand the changes in each release, review the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

1.18.2

Breaking

Reverted an undocumented change to a metric name. The Cloud Monitoring metric `current_declared_resources` (introduced in version 1.16.1) has been renamed to its original name, `declared_resources`. For reference see [Monitor Config Sync with Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring).

## May 30, 2024

1.18.1

Change

Upgraded the Open Telemetry image from v0.91.0-gke.9 to v0.99.0-gke.1 to pick up vulnerability fixes. To understand the changes in each release, review the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

1.18.1

Fixed

Fixed an issue where Config Sync installation would fail when using a private registry with a specified port in the image URL.

1.18.1

Change

Upgraded bundled Helm version from v3.14.3 to [v3.14.4](https://github.com/helm/helm/releases/tag/v3.14.4) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

## May 02, 2024

1.18.0

Breaking

Manually installing Policy Controller through the [ConfigManagement](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/configmanagement-fields) object is no longer supported. Instead, use [Policy Controller Google Cloud CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller) to install and configure Policy Controller. This note was added on July 2, 2024.

1.18.0

Announcement

Dynamic namespace selection using the `spec.mode` field in the NamespaceSelector CRD is now generally available (GA). This feature supports deploying namespace-scoped resources in matching Namespaces statically-declared in the source of truth and dynamically present on the cluster. For more information, refer to [NamespaceSelector mode](https://docs.cloud.google.com/anthos-config-management/docs/how-to/namespace-scoped-objects#namespaceselector_mode).

1.18.0

Change

Reduced memory footprint in reconcilers by not loading the OpenAPI when the Config Sync admission webhook is disabled.

1.18.0

Change

When syncing from Helm, Config Sync now retries faster on errors with exponential backoff.

1.18.0

Fixed

Mitigated an issue periodically occurring that could cause an error when the authentication token expires for Cloud Source Repositories, prompted by a race condition between the `gcenode-askpass-sidecar` container validating the credentials and the `git-sync` container trying to use those credentials. This note was added on June 18, 2024.

1.18.0

Announcement

Policy Controller now has its own release notes page. For future announcements, visit [Policy Controller release notes](https://docs.cloud.google.com/kubernetes-engine/enterprise/policy-controller/docs/release-notes).

1.18.0

Change

On Autopilot clusters, the `helm-sync` container CPU request is changed from 150m to 250m, and memory request is changed from 256Mi to 384Mi. For information on resource requirements, see [Resource requests](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#resource_requests).

1.18.0

Breaking

Installing Policy Controller 1.18.0 or newer will fail unless you first enable the `anthospolicycontroller.googleapis.com` API. For more information on directly installing and managing Policy Controller, see [Install Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller#gcloud-policy-controller).

1.18.0

Change

Policy Controller bundles have been updated to the following versions: `cis-gke-v1.5.0`: `202403.0`, `nist-sp-800-190`: `202403.0`, `nist-sp-800-53-r5`: `202403.0`, `pci-dss-v3.2.1`: `202403.0`, `pci-dss-v4.0`: `202403.0`, `policy-essentials-v2022`: `202403.0`, `pss-baseline-v2022`: `202403.1`, `pss-restricted-v2022`: `202403.1`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

1.18.0

Feature

Config Sync now supports specifying CA certificates for helm and OCI source types. This is surfaced on the `caCertSecretRef` field on the RootSync and RepoSync APIs. For more information, refer to [RootSync and RepoSync fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields).

1.18.0

Change

Upgraded bundled Helm version from v3.13.3 to [v3.14.3](https://github.com/helm/helm/releases/tag/v3.14.3) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

## March 21, 2024

1.17.3

Feature

The constraint template library includes a new template: `K8sPSSRunAsNonRoot`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.17.3

Fixed

Fixed a regression introduced in 1.16.0 that limits the length of the Secret name referenced in the `spec.git.secretRef.name` field of the RootSync object.

1.17.3

Change

Policy Controller bundles have been updated to the following versions: `cis-gke-v1.4.0`: `202402.0-preview`, `nist-sp-800-190`: `202402.0`, `nist-sp-800-53-r5`: `202402.0`, `pci-dss-v3.2.1`: `202402.0`, `pss-baseline-v2022`: `202402.0`, `pss-restricted-v2022`: `202402.0`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

1.17.3

Fixed

Fixed a regression introduced in 1.17.0 that caused Config Sync to sometimes [fail to pull the latest commit from a Git branch](https://docs.cloud.google.com/anthos-config-management/docs/how-to/known-issues#git-sync-issue) by upgrading git-sync (Config Sync dependency for pulling from git) from v4.1.0 to v4.2.1.

## February 22, 2024

1.17.2

Feature

The constraint template library includes a new template: `K8sCronJobAllowedRepos`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.17.2

Feature

The constraint template library includes a new template: `K8sRestrictAdmissionController`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.17.2

Feature

Added the authentication type `k8sserviceaccount` for syncing from OCI images and Helm charts hosted in Artifact Registry. For more details, see [Grant Config Sync read-only access to OCI](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#oci-access) and [Grant Config Sync read-only access to Helm](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#helm-access).

1.17.2

Fixed

Fixed the unrecognized label error in the `otel-collector` configuration that caused kustomize metrics to be rejected.

1.17.2

Feature

Simplified the steps to export metrics to Cloud Monitoring. For more details, see [Configure Cloud Monitoring with Workload Identity](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitor-config-sync-cloud-monitoring#custom-monitoring).

## February 16, 2024

1.17.0

Breaking

Upgraded git-sync (Config Sync dependency for pulling from git) from v3.6.9 to v4.1.0 to pick up enhancements, such as improved efficiency and race condition fixes. This contains a breaking change that short commit SHA is no longer accepted in the `spec.git.revision` field of RootSync and RepoSync. If you want to sync from a Git commit, use a full commit SHA in the `spec.git.revision` field. For more details, please refer to [Configuration for the Git repository](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuring-git-repo). This release note was updated February 16, 2024 with a correction to the version number.

## January 25, 2024

1.17.1

Fixed

Fixed a performance issue where the config-management-operator was continuously updating the webhook definition, causing unnecessary churn in the apiserver and etcd.

1.17.1

Fixed

Fixed a race condition that could cause deadlock when uninstalling Config Sync. This issue could sometimes occur if a RepoSync was managed by a RootSync with foreground deletion propagation enabled.

1.17.1

Change

Upgraded bundled Helm version from v3.13.1 to [v3.13.3](https://github.com/helm/helm/releases/tag/v3.13.3) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

1.17.1

Feature

The constraint template library includes a new template: `K8sDisallowInteractiveTTY`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.17.1

Fixed

Fixed an issue that could cause RootSyncs and RepoSyncs to be reported as Current before they had been reconciled.

1.17.1

Fixed

Fixed an issue where RepoSync Secrets were not garbage collected when switching between Secret refs or types.

1.17.1

Change

Upgraded bundled Kustomize version from v5.1.1 to [v5.3.0](https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize%2Fv5.3.0) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/kubernetes-sigs/kustomize/releases).

1.17.1

Fixed

Fixed an issue where the log level could not be set for the otel-agent container.

1.17.1

Change

Policy Controller bundles have been updated to the following versions: `cis-k8s-v1.5.1`: `202312.1`, `cost-reliability-v2023`: `202312.0`, `nist-sp-800-190`: `202312.1`, `nist-sp-800-53-r5`: `202312.1`, `nsa-cisa-k8s-v1.2`: `202312.1`, `pci-dss-v3.2.1`: `202312.1`, `psp-v2022`: `202312.0`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

## December 11, 2023

1.17.0

Breaking

Added validation to block declaration in the source of truth of the Config Sync controller namespaces, including `resource-group-system` and `config-management-monitoring` namespaces. For reference see [KNV1034: IllegalNamespaceError](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors#knv1034). This note was updated on January 10, 2024

1.17.0

Change

The constraint template library's `K8sNoExternalServices` template now supports the `"networking.gke.io/load-balancer-type": "Internal"` annotation. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8snoexternalservices).

1.17.0

Breaking

The `nomos` command-line tool now requires the kubectl plugin `gke-gcloud-auth-plugin` to be installed to interact with GKE, and your KUBECONFIG must be configured to use it by calling `gcloud container clusters get-credentials`. Versions of the gcloud CLI older than 430.0.0 also require setting `USE_GKE_GCLOUD_AUTH_PLUGIN=True`. For reference, see [Prerequisites](https://docs.cloud.google.com/anthos-config-management/docs/how-to/nomos-command#prerequisites) for the nomos command-line tool.

1.17.0

Feature

The constraint template library includes a new template: `K8sRequireAdmissionController`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.17.0

Feature

Added a new field `spec.mode` in the NamespaceSelector CRD as a preview feature to support selecting namespace-scoped resources matching both statically-declared Namespaces in the source of truth and those dynamically present on the cluster. For more details, please refer to [Limit which namespaces a config affects](https://docs.cloud.google.com/anthos-config-management/docs/how-to/namespace-scoped-objects#namespaceselectors).

1.17.0

Change

Reduced Config Sync reconciler default CPU and memory requests on GKE Standard clusters. Increased Config Sync reconciler default CPU and memory requests to avoid throttling and reduce time to sync by up to 25%, and increased default limits on GKE Autopilot clusters to avoid out of memory errors for most workloads. For reference see [Resource requests](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#resource_requests).

1.17.0

Feature

Added known_hosts support for Git connection over SSH in RootSync and RepoSync APIs. For more details on SSH key pair see [Install Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#ssh-key-pair).

1.17.0

Change

Policy Controller bundles have been updated to the following versions: `asm-policy-v0.0.1`: `202311.0`, `cis-k8s-v1.5.1`: `202311.0`, `cost-reliability-v2023`: `202311.0`, `nist-sp-800-190`: `202311.0`, `nist-sp-800-53-r5`: `202311.0`, `nsa-cisa-k8s-v1.2`: `202311.0`, `pci-dss-v3.2.1`: `202311.0`, `policy-essentials-v2022`: `202311.0`, `psp-v2022`: `202311.0`, `pss-baseline-v2022`: `202311.0`, `pss-restricted-v2022`: `202311.0`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

1.17.0

Breaking

Upgraded git-sync (Config Sync dependency for pulling from git) from v3.6.9 to v4.0.0 to pick up enhancements, such as improved efficiency and race condition fixes. This contains a breaking change that short commit SHA is no longer accepted in the `spec.git.revision` field of RootSync and RepoSync. If you want to sync from a Git commit, use a full commit SHA in the `spec.git.revision` field. For more details, please refer to [Configuration for the Git repository](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuring-git-repo). This release note is incorrect; see entry for February 16, 2024.

1.17.0

Fixed

Fixed an issue with the nomos CLI not authenticating correctly when run inside a Kubernetes Pod. Now, to authenticate to another cluster while inside a pod, you must explicitly set KUBECONFIG to point to the kubectl config, otherwise the downward API is used to authenticate with the local cluster.

1.17.0

Feature

Added a new field `spec.override.namespaceStrategy` in the RootSync API to control whether Namespaces should be created implicitly or not if Namespace configs are missing from the source of truth. For reference see [RootSync and RepoSync fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#rootsync_and_reposync_fields).

1.17.0

Feature

Added a new field `spec.override.roleRefs` in the RootSync API to customize root reconciler permissions other than cluster-admin. For reference see [RootSync and RepoSync fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#rootsync_and_reposync_fields).

## November 13, 2023

1.16.3

Change

Policy Controller bundles have been updated to the following versions: `asm-policy-v0.0.1`: `202310.0`, `cis-k8s-v1.5.1`: `202310.0`, `cost-reliability-v2023`: `202310.0-preview`, `nist-sp-800-190`: `202310.0`, `nist-sp-800-53-r5`: `202310.0`, `nsa-cisa-k8s-v1.2`: `202310.0`, `pci-dss-v3.2.1`: `202310.0`, `policy-essentials-v2022`: `202310.0`, `psp-v2022`: `202310.0`, `pss-baseline-v2022`: `202310.0`, `pss-restricted-v2022`: `202310.0`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

1.16.3

Change

The constraint template library's `K8sPSPAllowedUsers`, `K8sPSPAllowPrivilegeEscalationContainer`, `K8sPSPAutomountServiceAccountTokenPod`, `K8sPSPCapabilities`, `K8sPSPFlexVolumes`, `K8sPSPForbiddenSysctls`, `K8sPSPFSGroup`, `K8sPSPHostFilesystem`, `K8sPSPHostNamespace`, `K8sPSPHostNetworkingPorts`, `K8sPSPPrivilegedContainer`, `K8sPSPProcMount`, `K8sPSPReadOnlyRootFilesystem`, `K8sPSPSELinuxV2`, `K8sPSPVolumeTypes`, and `K8sRequiredProbes` no longer raise violations during updates of existing objects for immutable fields.

1.16.3

Announcement

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [ a1f01f4 ](https://github.com/open-policy-agent/gatekeeper/tree/a1f01f4)).

1.16.3

Change

Updated the Open Telemetry image from 0.86.0 to 0.87.0 to address security vulnerabilities. For more information about these changes, see the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

## October 19, 2023

1.16.2

Announcement

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [3e66ee2](https://github.com/open-policy-agent/gatekeeper/tree/3e66ee2)).

1.16.2

Change

Policy Controller bundles have been updated to the following versions: `asm-policy-v0.0.1`: `202309.0`, `cis-k8s-v1.5.1`: `202309.0`, `cost-reliability-v2023`: `202309.0`, `nist-sp-800-190`: `202309.0`, `nist-sp-800-53-r5`: `202309.0`, `nsa-cisa-k8s-v1.2`: `202309.0`, `pci-dss-v3.2.1`: `202309.0`, `policy-essentials-v2022`: `202309.0`, `psp-v2022`: `202309.0`, `pss-baseline-v2022`: `202309.0`, `pss-restricted-v2022`: `202309.0`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

1.16.2

Fixed

Fixed a recurring transient error in the RootSync and RepoSync API. Transient errors are retried internally and surfaced to RootSync and RepoSync if failed eventually.

1.16.2

Change

Updated the Open Telemetry image from 0.54.0 to 0.86.0 to address security vulnerabilities. `otelcontribcol:v0.86.0` contains breaking changes. For more information about these changes, see the full changelog for [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md).

1.16.2

Feature

The constraint template library includes a new template: `K8sPSPWindowsHostProcess`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.16.2

Feature

The constraint template library includes a new template: `K8sAvoidUseOfSystemMastersGroup`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

## September 21, 2023

1.16.1

Fixed

Fixed a repeating error in the `otel-collector` deployment log that has been occuring since Anthos Config Management version 1.15.0.

1.16.1

Fixed

Fixed an issue related to metric labels `commit` and `type` that could cause an increase in Google Cloud Monitoring metric write throughput. The issue was resolved by preventing high-cardinality labels `commit` and `type` from being sent to Google Cloud Monitoring. The two labels were introduced in Anthos Config Management version [1.15.0](https://docs.cloud.google.com/anthos-config-management/docs/release-notes#May_04_2023). For information on the labels, see [Config Sync Metric Labels](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync#metric_labels).

1.16.1

Fixed

The constraint template library's `K8sRestrictRbacSubjects` template now returns all violation messages for `ClusterRoleBinding` or `RoleBinding` with more than one violation. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srestrictrbacsubjects).

1.16.1

Change

Supported configuring the period that Config Sync waits before re-pulling the latest chart with the field `spec.helm.period` in RootSync or RepoSync. The default is 1 hour. For more information, see [RootSync and RepoSync fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields).

## August 21, 2023

1.16.0

Fixed

Fixed an issue causing Config Sync to prematurely stop tracking managed resource objects when pruning them before they are deleted from the cluster. Those objects will now appear in the Cloud Console and nomos status until the deletion has reconciled.

1.16.0

Issue

There is a memory issue in the reconciler due to the discovery client loading the OpenAPI for schema validations. The issue is only observed on Autopilot clusters with many CRDs installed. You can increase the memory request with the override.resources API. To learn more, see [Configuration for overriding the resource requests and limits of a root or namespace reconciler](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#override-resources).

1.16.0

Feature

Added a new `configsync.gke.io/deletion-propagation-policy` annotation for use on RootSync and RepoSync, for configuring foreground cascading deletion as a preview feature. When set to `Foreground`, the resource objects managed by it will be deleted when the RootSync or RepoSync is deleted. To learn more, see [Bulk delete objects](https://docs.cloud.google.com/anthos-config-management/docs/how-to/managing-objects#bulk_delete_objects).

1.16.0

Announcement

ExpansionTemplates APIs promoted to `v1beta1`.

1.16.0

Feature

Added a new field `spec.helm.valuesFileRefs` in RootSync and RepoSync to allow specifying Helm values files in ConfigMaps. For reference, see [Configuration for the Helm repository](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository).

1.16.0

Feature

Added the `spec.override.logLevels` field to RootSync and RepoSync, for configuring the log level of the containers of reconciler Pods. For more information, see [RootSync and RepoSync fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields) and [General best practices](https://docs.cloud.google.com/anthos-config-management/docs/how-to/troubleshooting-config-sync#general_best_practices).

1.16.0

Change

The constraint template library's `K8sRequireDaemonsets` template now supports restricting the use of `NodeSelector` in required `Daemonset` using the new `restrictNodeSelector` parameter. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequiredaemonsets).

1.16.0

Feature

Policy Controller add new bundles: `nist-sp-800-190`, `nist-sp-800-53-r5`, and `nsa-cisa-k8s-v1.2`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

1.16.0

Change

Increased the default timeout for Kubernetes API requests from 5 seconds to 15 seconds. This allows more requests to succeed with fewer retries when the control plane is under load, and reduces the need to override the timeout with `spec.override.apiServerTimeout` in RootSync and RepoSync. To learn more, see [Configuration for overriding the resource requests and limits of a root or namespace reconciler](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#override-resources).

1.16.0

Change

Policy Controller bundles have been updated to the following versions: `cis-k8s-v1.5.1`: `202307.1`, `pci-dss-v3.2.1`: `202307.0`, `policy-essentials-v2022`: `202307.1`, `pss-baseline-v2022`: `202307.0`, `pss-restricted-v2022`: `202307.0`. For reference, see [Policy Controller bundles overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller-bundles).

1.16.0

Issue

Known Issue for Policy Controller: If you're using [ExpansionTemplates](https://open-policy-agent.github.io/gatekeeper/website/docs/expansion/) and [mutators](https://docs.cloud.google.com/anthos-config-management/docs/how-to/mutation), Policy Controller will not apply the mutators for the generated resources.

1.16.0

Change

Reduced the resource requirements for the reconciler Pod when no Kustomize rendering is needed. For information on resource requirements, see [Resource requests](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#resource_requests).

1.16.0

Breaking

The constraint template library's `GkeSpotVMTerminationGrace` template adds the `includePodOnSpotNodes` parameter, which requires [enabling referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential). For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#gkespotvmterminationgrace).

1.16.0

Announcement

The Config Sync feature to sync directly from Helm repositories (including OCI-based ones) is generally available (GA). Google Artifact Registry is the preferred Helm registry. To learn more, see [Sync Helm charts from Artifact Registry](https://docs.cloud.google.com/anthos-config-management/docs/how-to/sync-helm-charts-from-artifact-registry) and [Configuration for the Helm repository](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository).

1.16.0

Feature

Added the `spec.configSync.metricsGcpServiceAccountEmail` field to the [gcloud apply spec fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields) to remove 2 manual [steps](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitor-config-sync-cloud-monitoring#custom-monitoring) required to export Config Sync metrics from a cluster with [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled to Cloud Monitoring. This note was updated on September 7, 2023.

1.16.0

Fixed

Fixed an issue preventing Config Sync from pruning managed resources correctly when the apiGroup of those resources is renamed in the source of truth.

1.16.0

Change

Upgraded bundled Kustomize version from v5.1.0 to [v5.1.1](https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize%2Fv5.1.1) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/kubernetes-sigs/kustomize/releases).

1.16.0

Announcement

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [616aa8f](https://github.com/open-policy-agent/gatekeeper/tree/616aa8f)).

1.16.0

Feature

The Helm chart version field `spec.helm.version` in RootSync and RepoSync can now be specified as a range of values from which Config Sync pulls the latest values. For reference see [Configuration for the Helm repository](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository).

## July 27, 2023

1.15.3

Change

Upgraded bundled Kustomize version from v5.0.3 to [v5.1.0](https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize%2Fv5.1.0) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/kubernetes-sigs/kustomize/releases).

1.15.3

Change

Upgraded bundled Helm version from v3.11.3 to [v3.12.2](https://github.com/helm/helm/releases/tag/v3.12.2) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/helm/helm/releases).

1.15.3

Feature

The constraint template library includes a new template: `K8sPodResourcesBestPractices`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.15.3

Change

The constraint template library has been updated to use the `templates.gatekeeper.sh/v1` API, which includes strict validation of parameter fields, for all templates. For a list of template parameter fields, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.15.3

Announcement

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [6aad7b6](https://github.com/open-policy-agent/gatekeeper/tree/6aad7b6)).

1.15.3

Feature

The constraint template library includes a new template: `GkeSpotVMTerminationGrace`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

## June 28, 2023

1.15.2

Feature

The constraint template library includes a new template: `K8sRestrictRoleRules`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.15.2

Fixed

Fixed a formatting issue in `nomos status --name`. For more information, see [nomos status flags](https://docs.cloud.google.com/anthos-config-management/docs/how-to/nomos-command#nomos_status_flags).

1.15.2

Feature

The constraint template library includes a new template: `K8sRestrictAutomountServiceAccountTokens`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.15.2

Feature

The constraint template library includes a new template: `K8sRequireBinAuthZ`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

## June 06, 2023

1.15.1

Announcement

The [Anthos Config Management SKU](https://docs.cloud.google.com/skus?currency=USD&filter=anthos+config) and [Anthos Policy Controller SKU](https://docs.cloud.google.com/skus?currency=USD&filter=anthos+policy) are end-of-sale. As of September 4, 2023, you must have an Anthos license to use Anthos Config Management. If you are using the Anthos Config Management SKU, migrate to an Anthos license by [enabling the Anthos API](https://console.cloud.google.com/apis/enableflow?apiid=anthos.googleapis.com&redirect=https://console.cloud.google.com&_ga=2.256554185.315189636.1684167698-397708036.1683827821) on your project.

## May 25, 2023

1.15.1

Change

Upgraded bundled Kustomize version from v5.0.1 to [v5.0.3](https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize%2Fv5.0.3) to pick up vulnerability fixes. To understand the changes in each release, review the [changelogs](https://github.com/kubernetes-sigs/kustomize/releases).

1.15.1

Feature

Added a new field `spec.helm.deployNamespace` in the RootSync API to support specifying which namespace to deploy the rendered chart. For more information, see [RootSync and RepoSync fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository).

1.15.1

Change

The constraint template library's `K8sStorageClass` template now supports an allowed list of storage classes using the new `allowedStorageClasses` parameter. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sstorageclass).

1.15.1

Feature

The constraint template library includes a new template: `K8sHorizontalPodAutoscaler`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.15.1

Fixed

The constraint template library's `K8sReplicaLimits` template now includes the object's actual kind instead of always deployment in violation messages. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8sreplicalimits).

## May 05, 2023

1.15.0

Deprecated

The `spec.git` fields of the `ConfigManagement` object are deprecated and are scheduled for shut down on or after May 15, 2024. The [`RootSync` API](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields) offers the same functionality and other benefits like syncing from multiple sources and improved observability. For information about the benefits and instructions for migrating your Git configuration to the `RootSync` object, see [Migrate your `ConfigManagement` object](https://docs.cloud.google.com/anthos-config-management/docs/how-to/migrate-multi-repo).

## May 04, 2023

1.15.0

Announcement

Depending on the frequency of production repository commits and variance in Kubernetes Kinds being deployed, the two new [metric labels](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync#metric_labels) `commit` and `type` introduced in this release can cause an increase in Google Cloud Monitoring metric write throughput. This can result in an increase of monthly billing. The affected metrics are apply_duration_seconds, api_duration_seconds, declared_resources, apply_operations_total. To avoid an increase in billing or if these metrics are not needed, follow the instructions to [patch the otel collector deployment with ConfigMap](https://github.com/GoogleContainerTools/kpt-config-sync/blob/v1.15/docs/custom-metric-filter.md#patch-the-otel-collector-deployment-with-configmap) and remove the affected metrics from the `filter/cloudmonitoring` allowlist. This note was updated on August 7, 2023.

1.15.0

Breaking

Upgraded bundled Kustomize version from v4.5.2 to [v5.0.1](https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize%2Fv5.0.1). Config Sync leverages the Kustomize executable to render the configurations under the hood. To understand the changes in each release, review the [changelogs](https://github.com/kubernetes-sigs/kustomize/releases). Kustomize v5.0.0 contains breaking changes. For more information about these changes, see the full changelog for [Kustomize v5.0.0](https://github.com/kubernetes-sigs/kustomize/releases/tag/kustomize%2Fv5.0.0). This note was updated on May 18, 2023.

1.15.0

Breaking

The constraint template library's `K8sEnforceConfigManagement` template adds new `requireDriftPrevention` and `requireRootSync` parameters, which requires [enabling referential constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/creating-policy-controller-constraints#referential). For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8senforceconfigmanagement).

1.15.0

Feature

The constraint template library includes a new template: `K8sDisallowedRepos`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.15.0

Feature

The constraint template library includes a new template: `K8sRestrictNfsUrls`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.15.0

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [effa347](https://github.com/open-policy-agent/gatekeeper/tree/effa347)).

1.15.0

Change

Upgraded bundled Helm version from v3.6.3 to v3.11.3. Config Sync leverages the Helm executable to render the configurations under the hood. For more information, see the changelog for [Helm v3.11.3](https://github.com/helm/helm/releases/tag/v3.11.3). This note was updated on May 22, 2023.

1.15.0

Change

Changed error message `ResourceFightWarning` to [`ResourceFightError`](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors#knv2005) so that resource fighting conflict can be exposed as errors in `nomos status` and `RootSync`/`RepoSync` status.

1.15.0

Feature

Added a `--name` flag to `nomos status` to support filtering status by RootSync or RepoSync names. For more information, see [nomos status flags](https://docs.cloud.google.com/anthos-config-management/docs/how-to/nomos-command#nomos_status_flags)

1.15.0

Feature

Added new metric labels: `commit` and `type`. These tags make it easier to detect when an error has been resolved. If you have a custom otel-collector ConfigMap, you should update it to filter out these tags for the Kubernetes exporter. For more information, see [Config Sync Metric Labels](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync#metric_labels).

1.15.0

Feature

The constraint template library includes a new template: `K8sContainerEphemeralStorageLimit`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

## March 23, 2023

1.14.3

Change

The constraint template library's `K8sPodsRequireSecurityContext` template now supports an exempt-list of Images using the new `exemptImages` parameter. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spodsrequiresecuritycontext).

1.14.3

Feature

The constraint template library includes a new template: `VerifyDeprecatedAPI`. For reference, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.3

Change

Config Sync disallows RootSync and RepoSync to do self management and a [KNV1069 SelfManageError](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors#knv1069) will be reported. This note was updated on April 12, 2023 and on May 11, 2023.

1.14.3

Change

The constraint template library's `K8sRequireCosNodeImage` template now supports an exempt-list of OS images using the new `exemptOsImages` parameter. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8srequirecosnodeimage).

1.14.3

Feature

Alpha release of AssignImage mutator, which allows mutation of Docker image paths. For reference, see [AssignImage](https://open-policy-agent.github.io/gatekeeper/website/docs/next/mutation/#assignimage) under Mutation in the OPA Gatekeeper documentation.

1.14.3

Change

Stopped exposing the "unable to load /repo/source/error.json" transient error in the RootSync and RepoSync API.

1.14.3

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [8170c5f](https://github.com/open-policy-agent/gatekeeper/tree/8170c5f)).

1.14.3

Fixed

Fixed an issue of accidental deletion of resources caused by a race condition between *-sync, hydration-controller and reconciler containers.

1.14.3

Fixed

Fixed an issue in the `nomos` CLI so that it works for standalone Config Sync.

1.14.3

Fixed

Fixed an issue where users are seeing an inaccurate `PENDING` instead of `INSTALLED` state on Policy Controller status. This change is added for `gcloud` version 427.0.0. This note was updated on April 19, 2023.

1.14.3

Fixed

Fixed an issue causing a Kubernetes `Service` object not syncing without the `.spec.ports` field being specified.

## February 23, 2023

1.14.2

Fixed

Increased the `helm-sync` container CPU request to 50m. For information on resource requirements, see [Resource requests](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#resource_requests).

1.14.2

Fixed

Updated the `spec.override.resources` field on RootSync and RepoSync objects to let you override the default resource amounts (for example, CPU or memory) requested by the `helm-sync` container.

## January 26, 2023

1.14.1

Fixed

Fixed an issue where the nomos image did not contain the nomos CLI.

1.14.1

Change

Config Sync now includes [resource-related metrics labels](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync#metric_labels) in Google Cloud Monitoring. These labels were previously added to the Prometheus monitoring pipeline in Config Sync version 1.14.0. The labels are available under the "Group By" filter options in the Google Cloud Console. For more information on metrics, see [Monitoring Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync).

1.14.1

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [c61db24](https://github.com/open-policy-agent/gatekeeper/tree/c61db24)).

1.14.1

Change

The constraint template library's `K8sPSPForbiddenSysctls` template now supports an allow-list of sysctls using the new `allowedSysctls` parameter. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8spspforbiddensysctls).

## December 08, 2022

1.14.0

Breaking

The following five metrics are removed because these metrics aren't needed for monitoring system performance or health:

  * `rendering_count`
  * `skip_rendering_count`
  * `resource_override_count`
  * `git_sync_depth_override_count`
  * `no_ssl_verify_count`



For information on current metrics, see [Monitor Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync).

1.14.0

Feature

The constraint template library includes a new template: `K8sRequireDefaultDenyEgressPolicy`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Feature

The following enhancements are made to Config Sync metrics:

  * Enhanced the histogram distribution bounds for the `parser_duration_seconds` and `apply_duration_seconds` metrics to support longer durations.
  * Enhanced the `last_sync_timestamp` metric to prevent timeseries with empty commits.
  * Added a new label called `controller` into the `apply_operations` metric to track whether the operation is from the applier or the remediator.
  * Support the `errorclass` label of the `reconciler_errors` metric correctly.



For more details, see [Monitor Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync).

1.14.0

Feature

The constraint template library includes a new template: `K8sBlockObjectsOfType`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Feature

The constraint template library includes a new template: `K8sRestrictRbacSubjects`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Feature

The constraint template library includes a new template: `K8sEnforceConfigManagement`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Feature

The constraint template library includes a new template: `K8sEnforceCloudArmorBackendConfig`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Feature

The constraint template library includes a new template: `K8sRequireDaemonsets`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Breaking

Config Sync now ignores validating and applying any resource configuration that has the annotation `config.kubernetes.io/local-config` with any value except for "false", instead of ignoring only when the value is "true". This is consistent with [its behavior in kpt](https://kpt.dev/reference/annotations/local-config/).

1.14.0

Feature

The constraint template library includes a new template: `K8sRequireValidRangesForNetworks`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Feature

Added resource tags to all Config Sync metrics to identify the source component. For more information, see [Config Sync Metric Tags](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync#metric_tags).

1.14.0

Feature

Added a field `spec.override.apiServerTimeout` in RootSync and RepoSync, for configuring the timeout for requests to the API server.

1.14.0

Announcement

The first edition of the Config Sync Service Level Indicators (SLIs) is published. You can set up alerts based on these SLIs, and get alerts if a threshold is hit. To learn more about the Config Sync SLIs, see [Use Config Sync SLIs](https://docs.cloud.google.com/anthos-config-management/docs/how-to/config-sync-slis).

1.14.0

Fixed

Fixed a known compatibility issue in Config Sync that was announced in Anthos Config Management 1.13.1 affecting Autopilot on GKE 1.23 and later. Config Sync is now compatible with Autopilot clusters on all supported GKE versions.

1.14.0

Feature

The constraint template library includes a new template: `K8sBlockAllIngress`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Feature

The constraint template library includes a new template: `K8sBlockCreationWithDefaultServiceAccount`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.14.0

Fixed

Various reliability and stability improvements to Config Sync.

## October 27, 2022

1.13.1

Feature

Added the [spec.helm.values](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository) field in RootSync and RepoSync to allow overriding the default values that accompany the Helm chart.

1.13.1

Issue

GKE version 1.23 introduced a change that made 1.23 Autopilot clusters incompatible with Config Sync. To work around this issue, use Config Sync on an Autopilot cluster with version 1.22 or earlier. This note was updated on November 4, 2022.

1.13.1

Breaking

Changed the default Helm release namespace from `config-management-system` to `default`, if [`spec.helm.namespace`](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository) isn't specified. Note that the value specified in [`spec.helm.namespace`](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository) is only used as the value of `Release.Namespace` declared in your Helm template; otherwise, the namespace `default` will be used.

1.13.1

Issue

The [409.0.0 Google Cloud CLI release](https://docs.cloud.google.com/sdk/docs/release-notes#40900_2022-11-08) introduced two bugs for Anthos Config Management. The [version](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/config-management/version) command incorrectly prints "NA" instead of the current version. The [status](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/config-management/status) command prints an incorrect message about unreachable regions. This note was updated on November 10, 2022.

1.13.1

Fixed

Fixed a Prometheus exporter error in the otel-collector by resolving a discrepancy between components regarding the description of the [`pipeline_error_observed` metric](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync#understand_the_pipeline_error_observed_metric).

1.13.1

Change

The constraint template library's `K8sHttpsOnly` template now supports Ingress blocks which do not include `tls:` using the new `tlsOptional: true` parameter. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8shttpsonly).

1.13.1

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [600a68d](https://github.com/open-policy-agent/gatekeeper/tree/600a68d)).

1.13.1

Fixed

Config Sync now handles exporting metrics correctly with the right permissions and resource names after the update to Open Telemetry v0.54.0 which was introduced in ACM 1.12.2.

1.13.1

Feature

The constraint template library includes a new template: `K8sBlockLoadBalancer`. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

## September 15, 2022

1.13.0

Fixed

Increased the resource-group-controller container memory request to 200Mi to avoid OOMKilled on Autopilot clusters.

1.13.0

Feature

The Google Cloud Console now shows the sync status for all syncs in clusters registered to fleet. It also allows for drilling down to see the reconciliation status for individual resources. To learn more, see [View Config Sync status in the Google Cloud console](https://docs.cloud.google.com/anthos-config-management/docs/how-to/view-config-sync-status-cluster).

1.13.0

Change

The contraint template library's `K8sEmptyDirHasSizeLimit` template now supports regular expression matching of exempt volume names by using the new `exemptVolumesRegex` parameter. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8semptydirhassizelimit).

1.13.0

Fixed

Fixed an issue that could cause accidental pruning when API resource discovery requests failed.

1.13.0

Breaking

On October 31, 2022, we will introduce a new billing SKU for Policy Controller which is a part of Anthos Config Management. However, we won't make any changes to the pricing or billing model.

Customers who use Policy Controller do not need to take any action.

Non-Anthos customers will see a new SKU appear on their monthly bill, but there is no change in pricing. The SKU "Anthos Configuration Management" (81D5-A275-98BF) will be replaced with the SKU "Anthos Policy Controller" (6707-0251-B8E2).

Anthos customers will not see a change as their usage of Policy Controller is covered by their Anthos license.

1.13.0

Feature

The constraint template library includes a new template: `K8sStorageClass`. Requires Anthos Config Management version 1.12.1 or higher. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.13.0

Feature

Config Sync supports syncing from private Helm repositories (including OCI-based ones) as a preview feature. Google Artifact Registry is the preferred Helm registry. To learn more, see [Sync Helm charts from Artifact Registry](https://docs.cloud.google.com/anthos-config-management/docs/how-to/sync-helm-charts-from-artifact-registry).

1.13.0

Fixed

Stopped the `nomos` command line tool from panicing when `nomos status` is unable to fetch ResourceGroups.

1.13.0

Fixed

Config Sync now handles empty `initContainers` fields in managed configs correctly.

1.13.0

Announcement

Anthos Config Management release 1.10 is no longer supported with the release of Anthos Config Management 1.13. For reference, see [Get support](https://docs.cloud.google.com/anthos-config-management/docs/get-support#version_support_policy).

1.13.0

Change

The contraint template library's `K8sMemoryRequestEqualsLimit` template now supports regular expression matching of exempt container names by using the new `exemptContainersRegex` parameter. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library#k8smemoryrequestequalslimit).

1.13.0

Fixed

Added optimizations to the reconciler and reconciler-manager to reduce API requests by avoiding unnecessary resource object updates.

1.13.0

Announcement

The Config Sync feature to sync configurations stored as OCI images in Google Artifact Registry or Container Registry is generally available (GA). To learn more, see [Sync OCI artifacts from Artifact Registry](https://docs.cloud.google.com/anthos-config-management/docs/how-to/sync-oci-artifacts-from-artifact-registry).

1.13.0

Feature

Config Sync now supports user-provided CA certificates for verifying HTTPS connections to Git servers. To learn more, see [Configuration of the Git Repository](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#configuring-git-repo).

1.13.0

Announcement

Config Sync is [open sourced](https://github.com/GoogleContainerTools/kpt-config-sync). We are open to contributions and bug fixes if you want to get involved in development of Config Sync. You can also use the repository to track ongoing work, or build from source to try out bleeding-edge functionalities.

## August 18, 2022

1.12.2

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [8f1ef8c](https://github.com/open-policy-agent/gatekeeper/tree/8f1ef8c)).

1.12.2

Fixed

Updated the built-in Open Telemetry image to [v0.54.0](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.54.0) to include a bug fix for using ADC with Cloud Spanner receiver.

1.12.2

Fixed

Fixed the reconciler Pod CrashLoopBackoff issue caused by the `git-sync` container starting before the `gcenode-askpass-sidecar`.

1.12.2

Fixed

Added `cluster-autoscaler.kubernetes.io/safe-to-evict: "true"` annotation to the reconciler Pod so that it does not block Cluster Autoscaler scale down.

## July 21, 2022

1.12.1

Fixed

Fixed the resource name length validation issue caused by long RepoSync names or long namespace names. The new maximum length is 253 characters, instead of 63 characters.

1.12.1

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [c370036](https://github.com/open-policy-agent/gatekeeper/tree/c370036)).

1.12.1

Feature

The constraint template library includes a new template: `K8sRequireCosNodeImage`. For reference, see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

## June 30, 2022

1.12.0

Change

The template library's `K8sProhibitRoleWildcardAccess` template now supports regular expression matching of `clusterRole` names by using the new `regexMatch` field.

1.12.0

Announcement

Policy Controller now supports Cloud Monitoring. It will automatically export runtime metrics for both Cloud Monitoring and Prometheus. Users can also configure which monitoring backends metrics are exported to. To learn more, see [Monitor Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-policy-controller#configure_metrics_export).

1.12.0

Feature

Config Sync supports syncing configurations stored as OCI images in Google Artifact Registry or Container Registry as a [preview](https://cloud.google.com/products#product-launch-stages) feature. To learn more, see [Publish config images to Artifact Registry](https://docs.cloud.google.com/anthos-config-management/docs/how-to/publish-config-registry).

1.12.0

Feature

Added a field [`spec.override.reconcileTimeout`](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#reconcile-timeout) in RootSync and RepoSync, for configuring the threshold for how long to wait for resources in an apply group to reconcile before giving up. An apply group consists of resources without direct or indirect [dependencies](https://docs.cloud.google.com/anthos-config-management/docs/how-to/declare-resource-dependency) on each others.

1.12.0

Change

This release includes several Config Sync performance improvements:

  * Config Sync reconciler now watches resources for status updates instead of polling, leading to faster, more responsive, and more efficient detection of object failure and reconciliation. This change also significantly reduces memory allocations for unchanged objects.
  * Disable client-side throttling when server-side throttling is enabled (enabled by default on Kubernetes v1.20 and later). This significantly reduced sync latency at scale.



1.12.0

Change

The template library's `K8sNoExternalServices` template supports a new field: `cloudPlatform`.

1.12.0

Breaking

Shell access is disabled by default in the Config Sync `hydration-controller` container. This disables the ability to use Kustomize remote bases. To use Kustomize remote bases, enable shell access by [setting the field](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields#enable-shell-in-rendering) `spec.override.enableShellInRendering: true` in RootSync and RepoSync.

1.12.0

Change

Config Sync removed resource limits from `reconciler-manager`, `reconciler`, and `git-importer` to make them burstable.

1.12.0

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [206bbe9](https://github.com/open-policy-agent/gatekeeper/tree/206bbe9)).

1.12.0

Feature

The constraint template library includes a new template: `K8sRequiredResources`. For reference see [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/latest/reference/constraint-template-library).

1.12.0

Announcement

Anthos Config Management is now compatible with GKE Autopilot with some cluster requirements. Policy Controller mutations are not compatible with Autopilot. Config Sync resource requests and limits adjustments will be further adjusted by GKE Autopilot. To learn more, see [Install Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#cluster-requirements).

1.12.0

Change

Config Sync increased resource limits of `admission-webhook` (cpu: 1, memory: 2Gi) and `otel-agent` (cpu: 1, memory: 1Gi).

1.12.0

Fixed

Fixed the issue causing reconciler to throw an error when deleting an object that was already deleted.

1.12.0

Fixed

Fixed the issue causing git-importer to wipe out non-blocking validation errors before retrying.

1.12.0

Fixed

Fixed the issue causing the Config Sync webhook deployment to report readiness prematurely by adding a readiness probe that waits for the TLS certificate to be generated and injected by the sidecar.

1.12.0

Fixed

Fixed two issues when resources are marked unmanaged using the `configmanagement.gke.io/managed: disabled` annotation:

  * If a repo contains unmanaged resources on the initial sync, the sync fails.
  * If a resource was deleted in the same commit where another resource is marked unmanaged, the deleted resource is not properly pruned.



## May 19, 2022

1.11.2

Fixed

Fixed metrics to use correct reconciler Pod name for multiple RootSync and RepoSync objects. The metrics are documented at [Config Sync metrics](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync#metrics)

## April 21, 2022

1.11.1

Feature

ConfigSync ignores the hidden directories `.github`, `.gitlab`, and the hidden file `.gitlab-ci.yml`.

1.11.1

Feature

Added support for using Fleet Workload Identity to authenticate to Git repositories in Cloud Source Repositories. To learn more, see [Grant Config Sync read-only access to Git](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#git-creds-secret).

1.11.1

Feature

Added a new `--timeout` flag to the `nomos bugreport` command. This flag configures the timeout for connecting to the cluster.

1.11.1

Fixed

Fixed the issue where `nomos bugreport` blocks on IO when the number of managed resources exceeds the buffer limit.

## March 24, 2022

1.11.0

Feature

Updated the `spec.override.resources` field on RootSync and RepoSync to let you override the default resource amounts (for example, CPU or memory) requested by the corresponding containers of the reconciler Deployment. To learn more, see [Troubleshoot Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/troubleshooting-config-sync).

1.11.0

Feature

Added new fields to the ResourceGroup inventory object to distinguish between actuation status and reconciliation status, as well as the intended actuation strategy (apply or delete) before actuation.

1.11.0

Feature

New Nomos CLI ARM binaries for Linux and Mac (darwin) are now available. Users on these platforms can now install with `gcloud components install nomos`. The new binary versions will be included in [Anthos Config Management downloads](https://docs.cloud.google.com/anthos-config-management/docs/downloads).

1.11.0

Feature

You can now specify apply and delete ordering using the new `config.kubernetes.io/depends-on` annotation. To learn more, see [Declare resource dependencies between resource objects](https://docs.cloud.google.com/anthos-config-management/docs/how-to/declare-resource-dependency).

1.11.0

Change

Increased the `reconciler-manager` container memory request to 50Mi and memory limit to 200Mi.

1.11.0

Feature

Added dependency enforcement to skip apply of objects whose dependencies are not successfully applied and fully reconciled.

1.11.0

Change

Increased the `admission-webhook` container memory request to 100Mi and memory limit to 250Mi.

1.11.0

Feature

Added support for multiple RootSync objects on the same cluster and multiple RepoSync objects in the same namespace. To learn more, see [Configure syncing from multiple repositories](https://docs.cloud.google.com/anthos-config-management/docs/how-to/multiple-repositories).

1.11.0

Fixed

Fixed individual resource object status to correspond to actuation and reconciliation of the latest specification from Git, not just reconciliation status of the last specification that was successfully applied.

1.11.0

Change

Increased the `config-management-operator` container memory request to 100Mi.

## February 24, 2022

1.10.2

Change

The template library's K8sRestrictRoleBindings template now supports regular expression matching of role/clusterRole names by using the regexMatch field.

1.10.2

Change

The template library's K8sProhibitRoleWildcardAccess template now allows roles and clusterRoles specified in the constraint to be exempted from the policy.

1.10.2

Fixed

Fixed a memory leak in the Config Sync reconciler container that led to high memory utilization or Pod restarts due to out-of-memory errors.

1.10.2

Fixed

Fixed an issue in the hydration-controller container causing the reconciler Pod crash looping when there is a malformed or missing `kustomization.yaml` in the base directory.

1.10.2

Change

A set of template library's templates now include the `exemptImages` parameter, which exempts specific containers from the policy. Those templates are:

  * K8sPSPAllowPrivilegeEscalationContainer
  * K8sPSPAppArmor
  * K8sPSPCapabilities
  * K8sContainerLimits
  * K8sContainerRatios
  * K8sPSPHostNetworkingPorts
  * K8sImageDigests
  * K8sPSPPrivilegedContainer
  * K8sPSPProcMount
  * K8sPSPReadOnlyRootFilesystem
  * K8sPSPSeccomp
  * K8sPSPSELinuxV2
  * K8sPSPAllowedUsers
  * K8sContainerLimits



1.10.2

Feature

The constraint template library includes new templates: K8sPSPAutomountServiceAccountTokenPod, RestrictNetworkExclusions, and K8sDisallowAnonymous.

1.10.2

Change

The template library's K8sContainerRatios template supports a new field: cpuRatio.

## January 27, 2022

1.10.1

Breaking

Eliminated duplicate metrics and reduced nonessential tags. For a full list of metrics, see [Monitor Config Sync in multi-repo mode](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-multi-repo).

1.10.1

Change

This release note was updated on January 28, 2022. The update removed information about a change to the K8sRestrictRoleBindings template that is not yet available.

1.10.1

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [a478ae6](https://github.com/open-policy-agent/gatekeeper/tree/a478ae6)).

1.10.1

Change

This release note was updated on January 31, 2022. The update removed information about two new templates K8sPSPAutomountServiceAccountTokenPod and RestrictNetworkExclusions that are not yet available.

1.10.1

Change

This release note was updated on January 31, 2022. The update removed information about a new field cpuRatio that is not yet available.

1.10.1

Fixed

Fixed the issue in legacy mode (not using [RootSync and RepoSync APIs](https://docs.cloud.google.com/anthos-config-management/docs/reference/rootsync-reposync-fields)) where unmanaged namespaces (with the `configmanagement.gke.io/managed:disabled` annotation) were deleted in the cluster when they were deleted from the repository.

1.10.1

Fixed

Fixed the issue where `nomos bugreport` could leak Git proxy credentials if present in the git-sync ConfigMap.

## December 09, 2021

1.10.0

Breaking

This note was updated on December 14, 2021:  
Config Sync admission webhook is disabled by default. In addition, you can configure to enable and disable Config Sync admission webhook. Config Sync blocks drifts in the cluster when the admission webhook is enabled. To learn more, see [Prevent config drift](https://docs.cloud.google.com/anthos-config-management/docs/how-to/prevent-config-drift).

  * If you install Config Sync using Google Cloud Console or gcloud, you can enable the webhook by adding the following setting to your `apply-spec.yaml` configuration file: `spec.configSync.preventDrift: true` (requires Cloud SDK 367.0.0 or later)
  * If you install Config Sync manually with `kubectl`, you can enable the webhook by adding the following setting to your `config-management-operator.yaml` configuration file: `spec.preventDrift: true`



1.10.0

Breaking

Policy Controller has deprecated the K8sPSPSELinux (v1) ConstraintTemplate. The K8sPSPSELinuxV2 template has been available since Anthos Config Management 1.5.2. Constraints created against K8sPSPSELinux (v1) are not compatible with the K8sPSPSELinuxV2 template. Customers using constraints based on the K8sPSPSELinux (v1) template will need to recreate those constraints against K8sPSPSELinuxV2.

1.10.0

Announcement

The Config Sync feature to render Kustomize configurations and Helm charts is generally available (GA). To learn more, see [Use a repo with Kustomize configurations and Helm charts](https://docs.cloud.google.com/anthos-config-management/docs/how-to/use-repo-kustomize-helm).

1.10.0

Announcement

The Policy Controller feature to support mutation is generally available (GA). To learn more, see [Mutate Resources](https://docs.cloud.google.com/anthos-config-management/docs/how-to/mutation).

1.10.0

Change

Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [c36e3d8](https://github.com/open-policy-agent/gatekeeper/tree/c36e3d8)).

1.10.0

Fixed

Fixed the issue causing `nomos hydrate` not to render Kustomize configs if it references files in parent directories.

1.10.0

Fixed

Fixed the issue in RootSync and RepoSync APIs causing proxy to incorrectly fail validation when auth is set to `cookiefile` or `none`.

1.10.0

Feature

`nomos status` surfaces messages from resource conditions when the managed resources are not ready or healthy.

1.10.0

Feature

Added a new metric `pipeline_error_observed` to capture if there is any error from different stages: rendering, sync, source, readiness.

1.10.0

Feature

Use [`nomos migrate`](https://docs.cloud.google.com/anthos-config-management/docs/how-to/nomos-command#migrate) to easily enable the RootSync and RepoSync APIs in the cluster. These APIs provide you with additional features and gives you the flexibility to sync to a single repository, or multiple repositories.

1.10.0

Change

Increased memory request for `git-sync` container to 200Mi.

1.10.0

Fixed

Fixed the issue causing some resources not to be applied when the status updates of all the resources in a Git repository take longer than 1 minute.

1.10.0

Fixed

This note was updated on December 14, 2021:  
Reduced the latency to sync a root repository in RootSync and RepoSync APIs by reducing GET calls to the API server.

1.10.0

Fixed

Fixed the issue causing `nomos vet --namespace` to fail because it incorrectly defaults `--source-format` to `hierarchy`.

## October 28, 2021

1.9.1

Fixed

Fixed the issue causing `nomos hydrate` to incorrectly require cluster objects to exist in the `clusterregistry` directory for unstructured repositories.

1.9.1

Change

Increased git-importer memory limit to 500Mi.

1.9.1

Fixed

Fixed the issue causing the namespace to be only synced to one of the clusters when the config for a namespace is defined multiple times with different `configmanagement.gke.io/cluster-selector` or `configsync.gke.io/cluster-name-selector` annotations.

1.9.1

Change

Config Sync will not block deletion requests if the object has non-nil `metadata.deletionTimestamp`.

1.9.1

Fixed

Fixed the issue causing `nomos hydrate` not to generate the configurations for clusters selected by the `configsync.gke.io/cluster-name-selector` annotation.

## September 23, 2021

1.9.0

Change

When encountering [KNV1021: UnknownObjectError](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors#knv1021), Config Sync applies other resources that aren't affected by this error.

1.9.0

Feature

The [`nomos vet`](https://docs.cloud.google.com/anthos-config-management/docs/how-to/nomos-command#vet) command supports rendering and it supports rendering Kustomize configurations or Helm charts. It provides a `--keep-output` flag to preserve the rendered output.

1.9.0

Breaking

In `nomos` versions earlier than 1.9.0, the `nomos status` command reports an incorrect status for clusters using an Anthos Config Management version of 1.9.0 or later. Before upgrading to Anthos Config Management 1.9.0 or later, [download](https://docs.cloud.google.com/anthos-config-management/docs/downloads#nomos_command) the latest `nomos` CLI tool.

1.9.0

Announcement

We strongly recommend that all Config Sync users enable multi-repo mode. It provides you with additional features and gives you the flexibility to sync to a single repository, or multiple repositories. If you are using `kubectl` to install and manage Config Sync, you can enable multi-repo mode by setting `spec.enableMultiRepo: true` in your `ConfigManagement` object. For more details, see [Syncing from multiple repositories](https://docs.cloud.google.com/anthos-config-management/docs/how-to/multi-repo#root-sync).

1.9.0

Change

Updated Config Sync CPU requests to fit inside a default GKE cluster and for better resource utilization.

1.9.0

Fixed

Fixed the issue causing the reconciler image version not getting updated, when upgrading from Anthos Config Management version 1.6.2. This was caused by an immutable label added in Anthos Config Management 1.6.2 and removed in 1.7.0.

1.9.0

Feature

The [`nomos hydrate`](https://docs.cloud.google.com/anthos-config-management/docs/how-to/nomos-command#hydrate) command supports rendering unstructured source format and it supports rendering Kustomize configurations or Helm charts.

1.9.0

Feature

Config Sync ignores validating and applying any resource configuration in the Git repo with the annotation `config.kubernetes.io/local-config: "true"`.

1.9.0

Breaking

The Anthos Config Management operator is now installed into the `config-management-system` namespace rather than the `kube-system` namespace. If you are running custom monitoring or installation processes you need to update those processes. For specific instructions, see [Manually installing Config Sync and Policy Controller with kubectl](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-kubectl).

1.9.0

Feature

Config Sync supports rendering Kustomize configurations and Helm charts in [multi-repo mode](https://docs.cloud.google.com/anthos-config-management/docs/how-to/multi-repo). The Git repository must have a `kustomization.yaml` file in the root of the sync directory to trigger the rendering process. To learn more, see [Use a repo with Kustomize configurations and Helm charts](https://docs.cloud.google.com/anthos-config-management/docs/how-to/use-repo-kustomize-helm).

## August 26, 2021

1.8.2

Feature

Config Sync supports storing HTTPS/HTTP proxy credentials inside the `git-creds` Secret, using `https_proxy` or `http_proxy` as a key, to avoid exposing these credentials as plaintext.

1.8.2

Feature

Anthos Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [07e2fd0](https://github.com/open-policy-agent/gatekeeper/tree/07e2fd0)).

1.8.2

Fixed

Fixed the issue causing Config Sync not to report sync errors when it fails to access Git repos.

1.8.2

Change

`kube-rbac-proxy` has been removed since Hierarchy Controller does not expose any sensitive metrics, and `kube-rbac-proxy` is no longer actively maintained.

1.8.2

Feature

Config Sync provides a way for users to override some system values:

  * Use the `spec.override.resources` field of a RootSync or RepoSync object to override the resource limits for the `reconciler` container and the `git-sync` container.
  * Use the `spec.override.gitSyncDepth` field of a RootSync or RepoSync object to override the number of git commits to fetch from the git repository.
  * Set the `spec.git.noSSLVerify` field of a RootSync or RepoSync object to `true` to disable Git SSL certificate verification.



1.8.2

Fixed

Fixed the issue causing Config Sync not to pick up the latest schema of the CustomResourceDefinitions synced from Git repos.

1.8.2

Fixed

Fixed the issue causing a root or namespace reconciler to fail to be updated after switching from the auth type from `none`|`gcenode`|`gcpserviceaccount` to other types.

## July 22, 2021

1.8.1

Change

This note was updated on August 5, 2021: the issue in the ResourceGroup Controller was fixed.

1.8.1

Fixed

An issue that caused Config Sync monitoring Pods fail to start in a cluster with PodSecurityPolicy enabled has been fixed.

1.8.1

Change

Cluster selectors and namespace selectors annotations are removed from the result of `nomos hydrate` so that it can pass `nomos vet` and can be synced directly to the cluster by Config Sync.

1.8.1

Fixed

An issue introduced in 1.8.0 `nomos hydrate` that breaks support for `--clusters` has been fixed.

1.8.1

Fixed

An issue in ResourceGroup Controller that failed to update statuses of the managed resources has been fixed.

## July 01, 2021

1.8.0

Change

This release note was updated on September 29, 2021: 

  * The issue with Config Sync causing excessive updates of resources has been fixed.



1.8.0

Change

This release note was updated on August 5, 2021: 

  * The issue in `nomos hydrate` has been fixed.
  * A bug in `nomos hydrate` has been identified.
  * `nomos status` has been updated to show resource level status when MultiRepo is enabled.



1.8.0

Feature

Config Management is now available on GKE. Config Management enables you to use [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller). GKE users can also now install Config Sync using the Cloud Console or by using the gcloud command-line tool. To learn more, see [Installing Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync).

1.8.0

Feature

Config Sync now supports accessing Cloud Source Repositories through a Google service account when Workload Identity is enabled in your cluster. To learn more, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#git-creds-secret).

1.8.0

Announcement

This release note contains information about 1.8.0 features that are now more widely available.

1.8.0

Change

The following commands have been promoted to beta:

  * `gcloud container hub config-management apply`
  * `gcloud container hub config-management disable`
  * `gcloud container hub config-management enable`
  * `gcloud container hub config-management status`
  * `gcloud container hub config-management unmanage`
  * `gcloud container hub config-management upgrade`
  * `gcloud container hub config-management version`



1.8.0

Feature

You can now configure your cluster with the same settings used by another cluster by using `gcloud fetch-for-apply`. To learn more, see [Configuring Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#configuring-config-sync).

1.8.0

Breaking

The config file format for the [`gcloud apply`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/apply) command has changed. For more information on the new file format, see [gcloud apply spec fields](https://docs.cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields).

1.8.0

Issue

A bug in `nomos hydrate` breaks support for `--clusters`.

1.8.0

Feature

`nomos status` shows resource level status when MultiRepo is enabled.

1.8.0

Feature

Config Sync cluster selectors support CustomResourceDefinitions.

1.8.0

Fixed

The issue where `nomos hydrate` command attempts to connect to the API Server even if `--no-api-server-check` is passed has been fixed.

## June 24, 2021

1.8.0

Breaking

Config Connector can no longer be installed via Anthos Config Management. Upgrading to Anthos Config Management v1.8.0 will not affect an existing Config Connector installation, but that installation can no longer be managed with Anthos Config Management. To install or upgrade Config Connector alongside Anthos Config Management v1.8.0 or later, see [Advanced installation options > Upgrading from non-operator installations](https://docs.cloud.google.com/config-connector/docs/how-to/advanced-install#upgrading_from_non-operator_installations) in the Config Connector documentation. The version of Config Connector supported in earlier versions of Anthos Config Management will stop working on Kubernetes versions greater than or equal to 1.19.

1.8.0

Change

The Hierarchy Controller admission webhook serving port has switched from 9443 to 10250. If you use Hierarchy Controller in private GKE clusters you no longer need to add a firewall rule to open port 9443.

1.8.0

Change

The Anthos Policy Controller admission webhook serving port is switched from 8443 to 10250. If you use Policy Controller in private GKE clusters you no longer need to add a firewall rule to open port 8443.

1.8.0

Change

The Config Sync admission webhook serving port is switched from 8676 to 10250. If you use Config Sync in multi-repo mode in private GKE clusters, you no longer need to add a firewall rule to open port 8676.

1.8.0

Fixed

All Anthos Config Management components have been updated to remove use of `v1beta1` APIs scheduled to be removed in Kubernetes 1.22. See the [Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-22) for more details.

1.8.0

Feature

Anthos Policy Controller now supports the ability for users to mutate resources as a preview feature. For more information see [Mutating resources](https://docs.cloud.google.com/anthos-config-management/docs/how-to/mutation).

1.8.0

Feature

Anthos Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [f6c2fe8](https://github.com/open-policy-agent/gatekeeper/tree/f6c2fe8)).

1.8.0

Change

Editing rights to Hierarchical Resource Quotas are now aggregated into the cluster-wide 'edit' and 'admin' Cluster Roles.

## May 26, 2021

1.7.2

Change

Increased reconciler memory limit to 300Mi.

1.7.2

Issue

The output of the `nomos hydrate` command does not pass `nomos vet` and cannot be synced using Config Sync without modifying the output. To work around this, we recommend removing the following annotations: `configmanagement.gke.io/cluster-name` , `configmanagement.gke.io/source-path` and removing label `configsync.gke.io/declared-version` from the output so that the output can be successfully synced.

1.7.2

Change

Hierarchy Controller has been updated to use HNC v0.8.0.

1.7.2

Issue

The `nomos hydrate` command attempts to connect to the API Server even if `--no-api-server-check` is passed. This behavior can be safely ignored in CI as if the CLI is unable to connect to the API Server it will not produce errors resulting from being unable to connect.

## May 20, 2021

1.7.0

Breaking

If [Syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-to/multi-repo) is enabled on a private GKE cluster, it's required to [add a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#step_3_add_a_firewall_rule) to allow port `8676`.

## May 13, 2021

1.7.1

Feature

Anthos Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [9b5e4cf](https://github.com/open-policy-agent/gatekeeper/tree/9b5e4cf)).

1.7.1

Fixed

Config Sync container images are now correctly updated when Anthos Config Management is upgraded.

1.7.1

Fixed

A bug in Anthos Config Management 1.7.0 which broke `nomos hydrate --no-api-server-check` has been fixed.

1.7.1

Fixed

A bug in Anthos Config Management 1.7.0 which caused `nomos status` to return errors when both unstructured repos and Hierarchy Controller were being used has been fixed.

1.7.1

Fixed

The Config Sync admission webhook in Anthos Config Management 1.7.0 would block requests when a managed resource in the cluster copied annotations to another resource.

## April 13, 2021

1.7.0

Breaking

Anthos Config Management v1.7.0 included several Kubernetes library updates, one of these updates made checks for `Resource` types [more strict](https://github.com/kubernetes/kubernetes/issues/94275). As a consequence, Config Sync users upgrading from an older version of Anthos Config Management may see errors in the form `KNV9998: failed to encode declared fields: internal error: ....resources.limits.cpu: expected string, got &value.valueUnstructured{Value:2}`. As a workaround, all resource declarations should be [specified as strings](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## April 05, 2021

1.7.0

Change

This release note was updated on September 29, 2021:

  * An issue with Config Sync causing excessive updates of resources has been identified.



1.7.0

Change

Anthos Config Management images are no longer included in Anthos on VMWare clusters. To learn more, see [Changes to Anthos Config Management updates](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/upgrading#version_170_changes_to_updates).

1.7.0

Feature

The ability to sync from multiple Git repositories is now a generally-available feature. To learn more, see [Syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-to/multi-repo).

1.7.0

Breaking

Config Sync configured with `sourceFormat: unstructured` will have errors during syncing if the Git repository specifies a ClusterSelector with an invalid `metadata.name` field.

1.7.0

Change

This release note was updated on August 27, 2021. The update adds information about how to resolve an upgrade issue.

1.7.0

Breaking

Config Sync configured with `sourceFormat: unstructured` will have errors during syncing if the Git repository includes a "Repo" resource.

1.7.0

Fixed

A memory leak in the Anthos Config Management Operator Pod that led to high memory utilization or Pod restarts due to out-of-memory errors has been corrected.

1.7.0

Fixed

Preview versions of multi-repo occasionally used excessive CPU usage and sent unnecessary queries to the apiserver master node, resulting in an unhealthy cluster. This issue has been corrected.

1.7.0

Issue

Config Sync multi-repo mode can't update the reconciler deployment image version when upgrading from 1.6.2 or later because of a new label removed from the immutable label selector. The workaround is to manually delete the reconciler by running `kubectl delete deployment -n config-management-system -l app=reconciler`. For more information, see [Error: reconciler deployments failed to be upgraded](https://docs.cloud.google.com/anthos-config-management/docs/how-to/troubleshooting-config-sync#error_reconciler_deployments_failed_to_be_upgraded).

1.7.0

Issue

Customers using Anthos Policy Controller who have upgraded since Anthos Config Management 1.5.1 need to update the timeoutSeconds in their ValidatingWebhookConfigurations from "5" to "3" to avoid issues with Kubernetes leader elections.

## February 25, 2021

1.6.2

Feature

Hierarchy Controller now includes a preview of Hierarchical Resource Quotas (HRQs). HRQs are drop-in replacements for Kubernetes Resource Quotas, but apply to resources in both a namespace as well as all of its descendants. To learn more, see [Using hierarchical resource quotas](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-to/using-hierarchical-resource-quotas).

1.6.2

Change

This release note was updated on March 5, 2021. The update removed information about a feature that is not yet available.

1.6.2

Change

This release note was updated on April 24, 2021. The update adds information about how to resolve an issue.

1.6.2

Change

This release note was updated on August 27, 2021. The update adds information about how to resolve an upgrade issue.

1.6.2

Fixed

The Anthos Config Management Operator Deployment now specifies `resources.limits` for `config-management-operator:manager`.

1.6.2

Issue

Config Sync multi-repo mode can't update the reconciler deployment image version in the upgrade process because of a new label added to the immutable label selector. The workaround is to manually delete the reconciler by running `kubectl delete deployment -n config-management-system -l app=reconciler`. For more information, see [Error: reconciler deployments failed to be upgraded ](https://cloud.google.com/anthos-config-management/docs/how-to/troubleshooting-config-sync#error_reconciler_deployments_failed_to_be_upgraded).

1.6.2

Issue

Config Sync multi-repo mode can't sync Git repositories using `ssh` as the authentication method. If this issue affects you, please [contact support](https://support.google.com/cloud/) so we can suggest ways to handle your required use cases while we correct this issue.

## January 28, 2021

1.6.1

Issue

Anthos Config Management Operator and Config Sync Pods get high memory utilization or OOMKilled due to memory leak.

1.6.1

Fixed

The `nomos status` output has been fixed for multi-repo clusters to distinctly show status of multiple namespace repos synced to the clusters.

1.6.1

Feature

Hierarchy Controller is upgraded to include HNC v0.7.0. This release introduces [Exceptions](https://github.com/kubernetes-sigs/multi-tenancy/blob/master/incubator/hnc/docs/user-guide/concepts.md#basic-exceptions). Exceptions let you use Kubernetes label selectors to precisely control where certain objects are propagated.

This release also removes support for the v1alpha1 API. If you were using Hierarchy Controller 1.5.1 or earlier, you must either update to Hierarchy Controller 1.5.2 or 1.6.0, and follow the [HNC v0.6.0 directions](https://github.com/kubernetes-sigs/multi-tenancy/releases/tag/hnc-v0.6.0) to upgrade to v1alpha2.

1.6.1

Fixed

The `nomos status` output has been fixed for multi-repo clusters to show `git.syncBranch` when `git.syncRev` is not specified (`git.syncRev` defaults to HEAD) to provide a consistent experience with mono-repo clusters.

## January 08, 2021

1.6.0

Issue

Config Sync unintentionally started using the absolute path in the file system with `spec.git.policyDir`. This has no effect on Config Sync running on the cluster, but breaks validation when running `nomos vet` manually against hierarchical repositories. The issue will be corrected in 1.6.1.

## December 10, 2020

1.6.0

Feature

Anthos Policy Controller now includes additional policies covering many of the CIS Kubernetes Benchmark 1.5.1 controls. To learn more, see the [Constraint template library](https://docs.cloud.google.com/anthos-config-management/docs/reference/constraint-template-library).

1.6.0

Feature

Anthos Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [1de87b6](https://github.com/open-policy-agent/gatekeeper/tree/1de87b6)).

1.6.0

Fixed

Support for Git submodules has been fixed in this version.

## November 16, 2020

1.5.2

Issue

A leading forward slash "/" in `spec.git.policyDir` will not match anything in Config Sync versions 1.5.2 and 1.6.0. For example:

`policyDir: "/dirname"`

will not match a top-level directory `dirname`. Because `policyDir` is always applied at the top of the directory structure, the workaround is to remove the leading forward slash.

This issue has been corrected in Config Sync 1.6.1; the forward slash will be ignored as it was in 1.5.1 and previous versions.

1.5.2

Fixed

The default timeout for Policy Controller's ValidatingWebhookConfiguration has been reduced to avoid interference with Kubernetes leader election processes.

1.5.2

Issue

There is an issue where enabling referential constraints does not take effect for the audit container. This affects Anthos Config Management versions 1.5.0, 1.5.1, and 1.5.2.

1.5.2

Change

Hierarchy Controller is upgraded to include [HNC v0.6.0](https://github.com/kubernetes-sigs/multi-tenancy/releases/tag/hnc-v0.6.0). This release introduces support for v1alpha2, and will automatically update all your existing HNC objects. We recommend backing up these objects before upgrading in case there are any problems with the upgrade process. For more information, see the [release notes for HNC v0.6.0](https://github.com/kubernetes-sigs/multi-tenancy/releases/tag/hnc-v0.6.0).

## October 29, 2020

1.5.1

Feature

Anthos Config Management now includes the ability to sync from multiple Git repositories. This is a preview feature. To learn more, see [Syncing from multiple repositories](https://docs.cloud.google.com/anthos-config-management/docs/how-to/multi-repo).

1.5.1

Fixed

The installed product version was being misreported as "anthos-config-management" in ACM 1.5.0. The correct product version is now being reported.

1.5.1

Issue

**Note:** this issue applies only to ACM in multi-repo mode.

When the enableLegacyFields is set to true, the ACM operator will create a RootSync resource automatically, but any subsequent changes to the RootSync resource will not be noticed by the operator. This will be fixed in a subsequent release. As a workaround, if the RootSync resource resource is modified, add or modify an unused annotation on the ConfigManagement resource to cause the operator to reconcile changes in the RootSync resource.

1.5.1

Change

The `nomos status` output has been modified significantly to provide a consistent experience for both mono-repo and multi-repo clusters.

1.5.1

Fixed

(Fixed on October 30, 2020) The version of Anthos Configuration Management included in the Anthos On-Prem release 1.5.1-gke.8 had initially referenced a version of the nomos image that had not be moved into the gcr.io/gke-on-prem-release repository, thus preventing a successful installation and/or upgrade of Anthos Configuration Management. This image has since been pushed to the repository to correct the issue for customers not using private registries. Customers using private registries will need to upgrade to 1.5.2 when it is available, or manually copy the nomos:v1.5.1-rc.7 image into their private repository.

## September 24, 2020

1.5.0

Feature

Anthos Config Management now includes [Config Connector](https://docs.cloud.google.com/config-connector) v1.19.1.

1.5.0

Feature

Binary Authorization can now be enabled through the Anthos Config Management Operator. See [Setting up with Anthos Config Management](https://docs.cloud.google.com/binary-authorization/docs/enabling-config-management) for details.

1.5.0

Change

The `syncer` and `importer` Containers now both run in the `git-importer` Pod in the `importer` Container. Any resource patches that were previously targeted to the `syncer` container will need to be updated to target the `importer` container.

1.5.0

Issue

Anthos Config Management installs a `resource-group-controller` Deployment which fails on non-GKE clusters. This Deployment is unnecessary and does not cause any other issues.

1.5.0

Feature

Anthos Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [15d56e3](https://github.com/open-policy-agent/gatekeeper/tree/15d56e3)).

1.5.0

Change

The `nomos` CLI tool is now available via `gcloud`. Please see the [downloads](https://docs.cloud.google.com/anthos-config-management/downloads) page for more information.

1.5.0

Change

This release includes several logging and performance improvements.

## August 27, 2020

1.4.2

Feature

Anthos Policy Controller has been updated to include a more recent build of OPA Gatekeeper ([hash: 1de87b6](https://github.com/open-policy-agent/gatekeeper/commit/1de87b6d3c2ed3609e69b789d722e28285873861)).

1.4.2

Feature

Anthos Config Management now includes [Config Connector](https://docs.cloud.google.com/config-connector) v1.15.1.

1.4.2

Change

This release includes several logging and performance improvements.

1.4.2

Issue

An issue with git submodule support is preventing syncing of configuration stored in submodule repositories. If this affects you, please [contact support](https://docs.cloud.google.com/support-hub) so we can suggest ways to handle your required use cases while we correct this.

## July 30, 2020

1.3.3

Fixed

Updated the git-sync image to fix security vulnerability [CVE-2019-5482](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5482).

## July 23, 2020

1.4.1

Feature

Anthos Config Management now includes Hierarchy Controller as a beta feature. For more information on this component, see the [Hierarchy Controller overview](https://docs.cloud.google.com/anthos-config-management/docs/concepts/hierarchy-controller).

1.4.1

Feature

[Config Connector](https://docs.cloud.google.com/config-connector) has been updated in Anthos Config Management to version 1.13.1.

1.4.1

Change

This release improves the handling of GitHub repositories with very large histories.

1.4.1

Change

Prior to this release, Config Sync and `kubectl` controllers and processes used the same annotation (`kubectl.kubernetes.io/last-applied-configuration`) to calculate three-way merge patches. The shared annotation sometimes resulted in resource fights, causing unnecessary removal of each other's fields. Config Sync now uses its own annotation, which prevents resource clashes.

In most cases, this change will be transparent to you. However, there are two cases where some previously unspecified behavior will change.

The first case is when you have run `kubectl apply` on an unmanaged resource in a cluster, and you later add that same resource to the GitHub repo. Previously, Config Sync would have pruned any fields that were previously applied but not declared in the GitHub repo. Now, Config Sync writes the declared fields to the resource and leaves undeclared fields in place. If you want to remove those fields, do one of the following:

  * Get a local copy of the resource from GitHub and `kubectl apply` it.
  * Use `kubectl edit --save-config` to remove the fields directly.



The second case is when you stop managing a resource on the cluster or even stop all of Config Sync on a cluster. In this case, if you want to prune fields from a previously managed resource, you will see different behavior. Previously, you could get a local copy of the resource from GitHub, remove the unwanted fields, and `kubectl apply` it. Now, `kubectl apply` no longer prunes the missing fields. If you want to remove those fields, do one of the following:

  * Call `kubectl apply set-last-applied` with the unmodified resource from GitHub, then remove unwanted fields and `kubectl apply` it again without the `set-last-applied` flag.
  * Use `kubectl edit --save-config` to remove the fields directly.



1.4.1

Change

This release includes several logging and performance improvements.

1.4.1

Change

Policy Controller users may now enable [\--log-denies](https://github.com/open-policy-agent/gatekeeper/blob/master/README.md#log-denies) to log all denies and dryrun failures. This is useful when trying to see what is being denied or fails dry-run and for keeping a log to debug cluster problems without looking through the status of all constraints. This is configured by setting `spec.policyController.logDeniesEnabled: true` in the configuration file for the Operator. There is an example in the section on [Installing Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller).

1.4.1

Change

The use of unsecured HTTP for GitHub repo connections or in an http_proxy is now discouraged, and support for unsecured HTTP will be removed in a future release. HTTPS will continue to be supported for GitHub repo and local proxy connections.

1.4.1

Change

This release includes several fixes and improvements for the `nomos` command line utility.

1.4.1

Fixed

In error messages, links to error docs are now more concise.

## June 25, 2020

1.4.0

Feature

Anthos Config Management is now Generally Available on AKS (Kubernetes v1.16 or higher) and EKS (Kubernetes v1.16 or higher).

1.4.0

Issue

Config Connector is not currently supported on EKS or AKS, as it is unable to run on these providers.

1.4.0

Change

The following Policy Controller constraint templates have been added to the Default Template Library:

  * allowedserviceportname
  * destinationruletlsenabled
  * disallowedauthzprefix
  * policystrictonly
  * sourcenotallauthz



The following constraint templates have been updated:

  * k8sblockprocessnamespacesharing
  * k8sdisallowedrolebindingsubjects
  * k8semptydirhassizelimit
  * k8slocalstoragerequiresafetoevict
  * k8smemoryrequestequalslimit
  * k8snoexternalservices
  * k8spspallowedusers
  * k8spspallowprivilegeescalationcontainer
  * k8spspapparmor
  * k8spspcapabilities
  * k8spspflexvolumes
  * k8spspforbiddensysctls
  * k8spspfsgroup
  * k8spsphostfilesystem
  * k8spsphostnamespace
  * k8spsphostnetworkingports
  * k8spspprivilegedcontainer
  * k8spspprocmount
  * k8spspreadonlyrootfilesystem
  * k8spspseccomp
  * k8spspselinux
  * k8spspvolumetypes



See the [Default Template Library documentation](https://docs.cloud.google.com/anthos-config-management/docs/reference/constraint-template-library) for more information.

1.4.0

Change

Anthos Policy Controller has been updated to include a more recent build of OPA Gatekeeper (hash: [25ca799](https://github.com/open-policy-agent/gatekeeper/tree/25ca7993efb26079156e24d4c9bc8b8a2e83c3ef)).

This new build of OPA Gatekeeper includes a number of bug fixes and performance improvements, and adds three new monitoring metrics:

  * gatekeeper_sync
  * gatekeeper_sync_duration_seconds
  * gatekeeper_sync_last_run_time



1.4.0

Issue

Anthos Config Management is not issuing errors when it encounters certain types of malformed configurations in a resource definition. This may result in the Kubernetes API Server ignoring the malformed fields and applying the default value for the field instead.

1.4.0

Issue

Policy Controller may fail to start successfully when synced resources are marked for deletion.

This issue will be addressed in the upstream OPA Gatekeeper project in a future release. For more information see the [relevant issue](https://github.com/open-policy-agent/gatekeeper/issues/660) in the Gatekeeper project.

1.4.0

Fixed

The `nomos` CLI tool now supports the `KUBECONFIG` environment variable in a way that matches the [`kubectl` behavior](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#the-kubeconfig-environment-variable) with multiple delimited configuration files.

1.4.0

Fixed

Anthos Config Management no longer gets into a continuous `PATCH` loop when encountering unmanaged resources with config-management annotations and a missing `last-applied-configuration` annotation.

1.4.0

Change

This release includes several logging and performance improvements.

## June 15, 2020

1.3.2

Issue

A regression in Anthos Config Management 1.3.2 results in unnecessary patches to the API server for the `gatekeeper-system` namespace and spurious logging for error `KNV2005`. This "fight" results when the `gatekeeper-system` namespace is managed in the Git repo, and two Anthos Config Management components (the operator and syncer) are both trying to reconcile the state of the namespace with the API server. The only workaround at this time is to [unmanage](https://docs.cloud.google.com/anthos-config-management/docs/how-to/managing-objects#unmanaged-namespaces) the `gatekeeper-system` namespace. The issue will be fixed in Anthos Config Management 1.4.1.

## May 21, 2020

1.3.2

Change

This release includes several performance and memory improvements. 

In order to help prevent accidental deletion, Anthos Config Management will no longer allow a user to remove all namespaces or cluster-scoped resources in a single commit. If you wish to delete the full set of resources under management, it now requires two steps: remove all but one in a first commit, allow ACM to sync those changes, then remove the final resource in a second commit.

1.3.2

Change

Anthos Config Management now supports a GKE-only authentication mechanism based on the service account of the cluster's node pool. Documentation on its use is [here](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#git-creds-gcenode).

1.3.2

Change

Anthos Config Management will now attempt to detect when resources that it manages are also managed by other controllers. Documentation on this behavior is available in [error `knv2005`](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors#knv2005) which ACM will log in that case.

1.3.2

Feature

Anthos Config Management now includes [Config Connector](https://docs.cloud.google.com/config-connector) v1.8.0.

1.3.2

Change

Policy Controller has been upgraded to include a newer version of [Open Policy Agent Gatekeeper](https://github.com/open-policy-agent/gatekeeper/tree/480baac44179d75d418b88fbd2c80581fcf183dd).

This version includes updates to improve the management of policy resources. As a consequence, finalizers are no longer used to manage Constraints and Constraint Templates.

The following metrics have been made obsolete due to these changes and have been removed:

  * gatekeeper_watch_manager_is_running

  * gatekeeper_watch_manager_last_restart_check_time

  * gatekeeper_watch_manager_last_restart_time

  * gatekeeper_watch_manager_restart_attempts




The following metrics were removed and will be re-implemented in a later version:

  * gatekeeper_watch_manager_intended_watch_gvk

  * gatekeeper_watch_manager_watched_gvk




1.3.2

Change

[Error documentation](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors) has been updated to add more information on error codes. Errors that are no longer encountered in the product have been removed. Most error references have been embellished with examples and steps for remediation.

## April 23, 2020

1.3.1

Feature

Policy Agent now allows configuration of namespaces that will bypass the admission controller. For more information, see [Excluding Namespaces from Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-exclude-namespaces)

1.3.1

Change

Anthos Config Management images are now included in the Google-provided system images for [Binary Authorization](https://docs.cloud.google.com/binary-authorization).

1.3.1

Issue

If you define a CRD with an integer field that has min/max values, Anthos Config Management will be unable to update the CRD.

1.3.1

Fixed

Anthos Config Management v1.3.1 now supports Kubernetes v1.16 and higher. Earlier versions of Anthos Config Management relied on APIs that have been [deprecated in Kubernetes v1.16](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-16).

1.3.1

Fixed

The Anthos Config Management Syncer pod now reports when it detects that it is fighting with another process over a resource.

1.3.1

Change

You can now [exempt Namespaces](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-exclude-namespaces) from Policy Controller enforcement

1.3.1

Fixed

Anthos Config Management no longer allows managing resources in unmanaged Namespaces.

1.3.1

Fixed

Anthos Config Management no longer overwrites undeclared labels and annotations on Namespaces.

## March 24, 2020

1.3.0

Change

Anthos Policy Controller is now Generally Available

1.3.0

Change

Anthos Config Management now includes the generally-available version of Config Connector.

1.3.0

Change

Anthos Config Management now supports the use of a [Personal Access Tokens](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) for authentication against supported Git providers. More information can be found in [Installing Anthos Config Management](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing).

1.3.0

Change

Anthos Config Management now supports the use of an HTTP or HTTPS proxy to connect with your Git host. More information can be found at [Installing Anthos Config Management](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing).

## February 21, 2020

1.2.2

Issue

GKE On-prem 1.2.2 includes images for ACM 1.2.1. Upgrading from ACM 1.2.1 to ACM 1.3 is a valid, tested, safe upgrade path.

1.2.2

Fixed

Minor updates and bug fixes.

## February 10, 2020

1.2.1

Fixed

Previously, adding an [APIService](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension) to the repo will leave Anthos Config Management in a bad state, with the error message "[KNV2002](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors#knv2002): failed to get server resources: unable to retrieve the complete list of server APIs." This issue has been mitigated; Anthos Config Management will now sync APIService objects correctly.

1.2.1

Feature

Anthos Config Management v1.2.1 is generally available for use in production.

1.2.1

Feature

A new CLI subcommand is available. `nomos bugreport` bundles up Anthos Config Management log information into a Zip file, which can be attached to a Google support ticket.

1.2.1

Feature

Anthos Config Management now can optionally support an unstructured repository, though some features that relied on hierarchical namespaces are disabled in this mode. More information can be found [here](https://docs.cloud.google.com/anthos-config-management/docs/how-to/unstructured-repo).

1.2.1

Issue

Currently, Config Connector can only be installed on a single cluster. If multiple Config Connector instances attempt to create or mutate the same Google Cloud resource, conflicts or errors may occur, and you may exhaust quota for a given resource.

1.2.1

Feature

Git repos with submodules are now also supported by Anthos Configuration Management out of the box without additional configuration. This allows delegation of config authoring in a Git-idiomatic way. For more information, please see [Git's documentation on submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

1.2.1

Issue

It is not currently possible to downgrade to v1.0.x after upgrading to a more recent version of Anthos Config Management.

## December 20, 2019

1.2.0

Feature

Anthos Config Management v1.2.0 is generally available for use in production.

This release has minor bug fixes and performance improvements.

## September 19, 2019

1.1.0

Deprecated

The `nomos view` command is deprecated and is not included in v1.1 or higher of the `nomos` command.

If you need to continue using `nomos view`, do not upgrade the `nomos` command from v1.0. It will remain forward-compatible for the foreseeable future.

1.1.0

Issue

It is not currently possible to downgrade to v1.0.x after upgrading to v1.1.0.

1.1.0

Change

The [`nomos hydrate`](https://docs.cloud.google.com/anthos-config-management/docs/how-to/nomos-command#hydrate) command is a replacement for the `nomos view` command, and reports your Anthos Config Management configuration in a human-readable way.

To use `nomos hydrate`, upgrade the `nomos` command to v1.1.

If you need to continue using `nomos view`, do not upgrade the nomos command from v1.0. It will remain forward-compatible for the foreseeable future.

You can read about a [known issue with nomos view](https://docs.cloud.google.com/anthos-config-management/docs/release-notes#known_issue_nomos_view).

1.1.0

Issue

Currently, Config Connector can only be installed on a single cluster. If multiple Config Connector instances attempt to create or mutate the same Google Cloud Platform resource, conflicts or errors may occur, and you may exhaust quota for a given resource.

1.1.0

Feature

You can now enable integration with [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) (beta), a Kubernetes addon that allows you to manage your Google Cloud Platform resources through Kubernetes configuration. You can sync configs for Google Cloud Platform resources with your Anthos Config Management repo and apply them automatically. For more information, see [Installing Config Connector](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-connector).

1.1.0

Change

Anthos Config Management can now be installed on clusters using PodSecurityPolicies.

1.1.0

Feature

Anthos Config Management v1.1.0 is generally available for use in production.

1.1.0

Change

The `apiVersion` for the ConfigManagement CustomResource has changed. No action is required; the CustomResource is upgraded automatically when you upgrade to v1.1.0. You can read more about [configuring Anthos Config Management](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#configuring-config-management-operator).

1.1.0

Change

Managed CRDs (CustomResourceDefinitions) are now Namespace-scoped by default, instead of cluster-scoped. This matches the semantics of the `kubectl` command.

If a CRD explicitly specifies a scope, Anthos Config Management honors that scope.

1.1.0

Feature

[Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) (Beta) is a Kubernetes dynamic admission controller that checks, audits, and enforces your clusters' compliance with policies related to security, regulations, or business rules. It is built using [Gatekeeper](https://github.com/open-policy-agent/gatekeeper), an open source project.

1.1.0

Issue

Adding an [APIService](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension) to the repo will leave Anthos Config Management in a bad state, with the error message [KNV2002](https://docs.cloud.google.com/anthos-config-management/docs/reference/errors#knv2002): failed to get server resources: unable to retrieve the complete list of server APIs." This issue will affect both new and existing clusters syncing from this repo. To correct the issue:

  * find the name of the `git-importer` and `syncer` pods using `kubectl get pods -n config-management-system`
  * copy those names and restart the pods with `kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx`
  * These steps are required once for each cluster.



Once the pods for a cluster are restarted, syncing will be back to normal.

1.1.0

Issue

`nomos view` can fail to parse CRDs (Custom Resource Definitions) that exist in the local clone of the repo but have not yet been synced to a cluster.

To work around this issue, use `nomos hydrate` instead of `nomos view`.

## June 14, 2019

1.0.0

Feature

You can now sync CustomResourceDefinitions (CRDs). Anthos Config Management can now sync any type of Kubernetes object. For more information, see [Configuring CustomResourceDefinitions](https://docs.cloud.google.com/anthos-config-management/docs/configs#configuring-CustomResourceDefinitions).

1.0.0

Change

The following changes have been made to the canonical example repository:

  * The [canonical example repo](https://github.com/GoogleCloudPlatform/csp-config-management) has moved. If you use this repo or a fork, update your Git repository's remotes or create a separate clone of the new repo to ensure that you receive updates.

  * The filesystem standard and the value of the Repo object's spec.version for this version of Anthos Config Management are both `1.0.0`.

  * A new branch named `1.0.0` contains configs compatible with Anthos Config Management v1.0.0.




1.0.0

Change

We improved the [instructions for setting up SSH keys](https://docs.cloud.google.com/anthos-config-management/docs/installing#git-creds-secret) for authenticating to a Git repository.

1.0.0

Change

The product name is now Anthos Config Management.

1.0.0

Change

New [metrics](https://docs.cloud.google.com/anthos-config-management/docs/monitoring) allow you to monitor counts, latencies, and timestamps of specific operations.

1.0.0

Feature

Anthos Config Management v1.0.0 is generally available for use in production.

To upgrade to this version, follow the instructions for [upgrading](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing#upgrading).

You must update all `nomos` binaries when you upgrade to Anthos Config Management v1.0.0.

Versions older than v1.0.0 are no longer available. If you participated in the early-access program for Anthos Config Management, you must upgrade to v1.0.0.

1.0.0

Feature

We document how to [stop Anthos Config Management from syncing configs](https://docs.cloud.google.com/anthos-config-management/docs/stopping-resuming-syncing) as quickly as possible. This allows you to mitigate the potential for propagating unintended configs to clusters.

1.0.0

Feature

The [`nomos status`](https://docs.cloud.google.com/anthos-config-management/docs/nomos-command#status) subcommand provides a top-level view of the state of Anthos Config Management on all enrolled clusters, including errors and sync status. It reports on all clusters that `kubectl` can access.

1.0.0

Change

The `nomos version` command now provides version details for the Config Management Operator on each configured cluster, as well as the version of the `nomos` command itself.

1.0.0

Change

An [example NetworkPolicy](https://docs.cloud.google.com/anthos-config-management/docs/configs#network-policy-config) illustrates some methods for enforcing good security practices across your clusters.

1.0.0

Breaking

HierarchicalResourceQuotas are no longer supported.

## March 29, 2019

0.13.1

Feature

You can now manage the `default` Namespace as well as Namespaces with names beginning with `kube`-.

0.13.1

Change

The `git-policy-importer` application has been renamed to `git-importer`.

0.13.1

Change

The `nomos-cluster-policy` ClusterConfig has been renamed to `config-management-cluster-config`. After upgrading, both ClusterConfig objects both exist on the cluster. This does not impact the functionality of the cluster, but you may see spurious log messages if the older ClusterConfig is still present. You can remove the old ClusterConfig to avoid these log messages:
    
    
    kubectl delete clusterconfig nomos-cluster-policy
    

0.13.1

Fixed

Previously, if a config change removed a controller object (for example, a Deployment that has a ReplicaSet), removing the controller object did not remove objects it controlled. All of a controller object's child objects are now correctly removed when the controller object itself is removed.

0.13.1

Fixed

Previously, if your repo contained only configs for Namespaces and no other configs, the Namespace configs would fail to sync. Repos now sync correctly even if it only contains configs for Namespaces.

0.13.1

Feature

Anthos Config Management v0.13.1 (beta) is a maintenance release, and is compatible with Anthos Config Management v0.13.0.

To upgrade from v0.13.0 on an existing cluster, [deploy the new Config Management Operator](https://docs.cloud.google.com/anthos-config-management/docs/installing#installing). You may need to remove an object that is no longer used, to prevent spurious log messages. See the release note about the change below.

0.13.1

Issue

Syncing of CustomResourceDefinitions is not currently supported. If CustomResourceDefinition has been applied to the cluster, you can sync associated CustomResources.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and higher.

## March 20, 2019

0.13.0

Change

The `nomos-resource-quota` object, which combines all of a Namespace's effective ResourceQuotas into a single one that is more efficient for Kubernetes to check and enforce, has been renamed to `config-management-resource-quota`.

0.13.0

Change

The Nomos object has been renamed to the ConfigManagement object and is now cluster-scoped.

0.13.0

Change

Annotations, rather than labels, are now used to determine that Anthos Config Management is managing a Kubernetes object.

0.13.0

Change

Syncs are no longer required, and are now silently ignored by the Config Management Operator. You can now create a config for any object in your cluster except a CustomResourceDefinition or the Config Management Operator itself.

0.13.0

Change

The `nomos.dev/` API group has been renamed to `configmanagement.gke.io/`.

0.13.0

Issue

Syncing of CustomResourceDefinitions is not currently supported. If a CustomResourceDefinition has been applied to the cluster, you can sync associated CustomResources.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and higher.

0.13.0

Change

The `nomos-system` Namespace has been renamed to `config-management-system`.

0.13.0

Breaking

Anthos Config Management 13.0.0 is the second beta release of Anthos Config Management. It represents a major change from v0.11.6, is not backward-compatible with any prior release, and cannot be installed on a cluster with a previous installation of Anthos Config Management. Backward-incompatible releases will always use a new minor version number.

0.13.0

Change

Prometheus now uses the `gkeconfig` Namespace.

0.13.0

Feature

You can now share a ResourceQuota among multiple Namespaces with a common abstract namespace directory. See [Aggregate ResourceQuotas](https://docs.cloud.google.com/anthos-config-management/docs/namespace-scoped-objects#resourcequota-aggregate).

## March 04, 2019

0.11.6

Change

Moved repository format to Filesystem Standard v0.1.0.

0.11.6

Change

Moved installation to use the Config Management Operator.

0.11.6

Issue

In some cases, local changes to managed resources made by `kubectl apply` can result in the removal of the `nomos.dev/managed: enabled` label, causing the resource to become unmanaged. As a workaround, use `kubectl edit` instead, or include the label in the YAML manifest you are applying.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and higher. If changes are manually applied to managed Kubernetes objects, Anthos Config Management effectively reverts those changes as soon as it notices a difference between the config in the repo and the object in the cluster.

For more information, see [Managing and unmanaging objects](https://docs.cloud.google.com/anthos-config-management/docs/how-to/configs).

0.11.6

Feature

Added support for NamespaceSelectors.

0.11.6

Issue

Syncing of CustomResourceDefinitions is not currently supported. If a CustomResourceDefinition has been applied to the cluster, you can sync associated CustomResources.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and higher.

0.11.6

Feature

Added support for syncing all Kubernetes resources generically. For current limitations, see the list of known issues for this release.

0.11.6

Breaking

This is the beta release of Anthos Config Management. It represents a major change from v0.10.4, and cannot be installed on a cluster with a previous installation of Anthos Config Management. An existing installation of the alpha from v0.10.4 or earlier will conflict with a new installation of v0.11.6 due to changes in the repository structure.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
