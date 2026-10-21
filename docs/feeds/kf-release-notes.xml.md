---
url: https://docs.cloud.google.com/feeds/kf-release-notes.xml
title: Kf - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:06.232623+00:00
---

# Kf - Release notes

> Source: https://docs.cloud.google.com/feeds/kf-release-notes.xml

tag:google.com,2016:kf-release-notesKf - Release notesGoogle Cloud Platform2025-10-06T00:00:00-07:00October 06, 2025tag:google.com,2016:kf-release-notes#October_06_20252025-10-06T00:00:00-07:002.x.x 

### Changed

Upgrade Tekton version to 1.3.2 and modify 'kf doctor' behavior and label selectors for pods to work with this Tekton version

### Changed

Upgrade ASM to 1.27.1

]]> March 21, 2025tag:google.com,2016:kf-release-notes#March_21_20252025-03-21T00:00:00-07:002.x.x 

### Changed

Upgraded server-side dependencies - Tekton Pipelines, Config Connector 

### Changed

Upgrade upload-pages-artifact dependency

]]> November 19, 2024tag:google.com,2016:kf-release-notes#November_19_20242024-11-19T00:00:00-08:002.x.x 

### Changed

Upgraded server-side dependencies - Tekton Pipelines, ASM

### Changed

Updated Go version used to build images and CLI tools

### Changed

Changed version of php-buildpack to address build issue.

]]> December 18, 2023tag:google.com,2016:kf-release-notes#December_18_20232023-12-18T00:00:00-08:002.x.x 

### Changed

Upgraded server-side dependencies - Tekton Pipelines, ASM & Config Connector

]]> September 27, 2023tag:google.com,2016:kf-release-notes#September_27_20232023-09-27T00:00:00-07:002.x.x 

### Security

Removed permissions on auditor roles that they could use to exec in containers if they used websockets with the Kubernetes API.

### Changed

When spaces are updated, apps in the affected space will be enqueued on a best-effort basis to avoid blocking the main queue used for live interactions.

### Feature

`kf push` now shows the amount of time source uploads took.

### Feature

Kf builds now show the number of files extracted from the uploaded source directory.

### Fixed

The featureflag controller will no longer enqueue all namespaces when feature flags are changed, significantly reducing the load on the controller.

### Feature

Added the ability to change the snapshot modes for Kaniko for faster snapshots and reduced disk I/O during builds.

### Changed

The default snapshot mode for Kaniko builds in the v2 buildpacks is now fast rather than robust.

]]> August 23, 2022tag:google.com,2016:kf-release-notes#August_23_20222022-08-23T00:00:00-07:002.11.5 

### Changed

Added limits to containers.

### Fixed

Fixed `set-env` slowness.

]]> August 22, 2022tag:google.com,2016:kf-release-notes#August_22_20222022-08-22T00:00:00-07:002.11.4 

### Fixed

Fixed issue that liveness probe is not set properly.

]]> August 10, 2022tag:google.com,2016:kf-release-notes#August_10_20222022-08-10T00:00:00-07:002.11.3 

### Fixed

Fix Kf performance issue with high server load. 

]]> July 22, 2022tag:google.com,2016:kf-release-notes#July_22_20222022-07-22T00:00:00-07:002.11.2 

### Changed

Removed NFS sidecar, built the logics into user-container.

]]> July 18, 2022tag:google.com,2016:kf-release-notes#July_18_20222022-07-18T00:00:00-07:002.11.1 

### Fixed

Fixed the issue that App Pod will keep restarting when the mounted NFS volume is larger than cluster's ephemeral storage.

### Fixed

Fixed the issue that will cause delete-service stuck.

]]> July 11, 2022tag:google.com,2016:kf-release-notes#July_11_20222022-07-11T00:00:00-07:002.11.0 

### Fixed

Kf will terminate Istio sidecars on completed tasks and builds freeing up IP addresses and compute resources for clusters running newer versions of Tekton.

### Fixed

Kf will now install with GKE 1.22 clusters.

### Fixed

kf doctor now works with GKE 1.22 clusters.

### Changed

Builds will now be allowed up to 15 minutes to extract or publish images.

]]> July 01, 2022tag:google.com,2016:kf-release-notes#July_01_20222022-07-01T00:00:00-07:002.10.1 

### Breaking

Removed `kf migrate` command.

### Changed

Changed go version to 1.17.

]]> June 01, 2022tag:google.com,2016:kf-release-notes#June_01_20222022-06-01T00:00:00-07:002.10.0 

### Changed

Added support for mapping GID and UID for NFS.

### Fixed

Fixed issue that unbind-service will not retry when failed.

### Changed

Fixed terminal size for Kf ssh.

]]> April 15, 2022tag:google.com,2016:kf-release-notes#April_15_20222022-04-15T00:00:00-07:002.9.0 

### Changed

Add Config Connector as a dependency of Kf. 

]]> March 21, 2022tag:google.com,2016:kf-release-notes#March_21_20222022-03-21T00:00:00-07:002.8.1 

### Fixed

Fixed bug in App controller, made App.Status.RouteConditions as an optional field.

]]> March 15, 2022tag:google.com,2016:kf-release-notes#March_15_20222022-03-15T00:00:00-07:002.7.3 

### Fixed

Fixed bug in App controller, made `App.Status.RouteConditions` as an optional field.

]]> March 03, 2022tag:google.com,2016:kf-release-notes#March_03_20222022-03-03T00:00:00-08:002.8.0 

### Feature

Add a feature that supports adding node selectors for Kf Builds to isolate Kf Build pods in specific node pool.

### Changed

Remove Config Connector as a dependency of Kf.

]]> February 01, 2022tag:google.com,2016:kf-release-notes#February_01_20222022-02-01T00:00:00-08:002.7.2 

### Fixed

Bug fix for Kf Build garbage collection.

### Feature

Added buildTimeout configuration feature. 

]]> January 27, 2022tag:google.com,2016:kf-release-notes#January_27_20222022-01-27T00:00:00-08:002.7.1 

### Changed

Support for Anthos Service Mesh v1.12

]]> December 14, 2021tag:google.com,2016:kf-release-notes#December_14_20212021-12-14T00:00:00-08:002.7 

### Feature

Added [`buildDisableIstioSidecar`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#enable_or_disable_the_istio_sidecar) configuration feature.

### Feature

Added [`buildPodResources`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#build_pod_resource_limits) configuration feature.

### Feature

Added [`controllerCACerts`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#self_signed_certificates_for_service_brokers) configuration feature.

### Feature

Added [`buildRetentionCount`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#build_retention) configuration feature.

### Feature

Added [V3 Google stack](https://cloud.google.com/migrate/kf/docs/2.7/concepts/v2-vs-v3-buildpacks#configure_stacks) as build option.

### Feature

Added [V3 kf-v2-to-v3-shim stack](https://cloud.google.com/migrate/kf/docs/2.7/concepts/v2-vs-v3-buildpacks#v2_to_v3_buildpack_migration) as build option.

### Fixed

Fixed an issue that could prevent SIGTERM from reaching an app.

### Fixed

Fixed an issue that caused extra reconciliation loops and logs.

### Changed

Improved CLI performance.

### Changed

Improved subresource API server resilience.

### Changed

Updated Config Connect to v1.66.0.

### Changed

Updated Tekton to v0.29.0.

### Changed

Support for Anthos Service Mesh (ASM) v1.11+, which recommends ingress gateways be outside of the `istio-system` namespace.

### Changed

Changed build ImagePullPolicy default from always download to prefer cached.

### Changed

Improved Workload Identity reliability.

]]> October 28, 2021tag:google.com,2016:kf-release-notes#October_28_20212021-10-28T00:00:00-07:002.6.1 

### Changed

VCAP_APPLICATION route string no longer includes trailing slash.

### Fixed

Resolved a scenario that could result in extra reconciliation loops and logs.

### Fixed

Addressed a v2 buildpack condition that could prevent SIGTERM signals from propagating.

]]> October 20, 2021tag:google.com,2016:kf-release-notes#October_20_20212021-10-20T00:00:00-07:002.6 

### Announcement

Anthos clusters on VMware (GKE on-prem) support promoted to GA.

### Announcement

Anthos clusters on bare metal support promoted to GA.

### Feature

New [`wrap-v2-buildpack`](https://cloud.google.com/migrate/kf/docs/2.6/cli/kf-wrap-v2-buildpack) **experimental** command available. 

**Known issue:** some buildpacks (ex: https://github.com/cloudfoundry/java-buildpack) produce directories that do not work with the `pack` CLI.

### Feature

Added support for `kubectl explain` to [inspect Kf CRDs](https://cloud.google.com/migrate/kf/docs/2.6/concepts/kf-dependencies#get_crd_details).

### Fixed

Fixed condition where CLI may not always show build logs.

### Fixed

Fixed issue where `kf doctor` expects the ASM ingress gateway deployment to be in the `kf` namespace.

### Fixed

Addressed scenario where the Kf operator could overwrite ASM Gateway customization.

### Changed

Config Connector dependency updated to v1.60.

### Changed

Tekton dependency updated to v0.26.0.

]]> September 28, 2021tag:google.com,2016:kf-release-notes#September_28_20212021-09-28T00:00:00-07:002.5.4 

### Fixed

Removed downstream lifecycle dependency for v2 buildpacks that could result in `kf push` failing.

]]> September 16, 2021tag:google.com,2016:kf-release-notes#September_16_20212021-09-16T00:00:00-07:002.5.3 

### Changed

Improved `kf doctor` reliability for Anthos on-prem clusters.

### Fixed

Fixed an error that can occur during the initialization of the subresource API.

]]> September 08, 2021tag:google.com,2016:kf-release-notes#September_08_20212021-09-08T00:00:00-07:002.5.2 

### Announcement

Kf for Anthos on-prem (Vsphere) is now available on the [Public Previews page](https://cloud.google.com/migrate/kf/docs/2.5/early-access/early-access).

### Fixed

Addressed a potential panic in the kf build-logs command.

### Changed

Changed flag and manifest validation for route and task fields so manifest routes are ignored when creating tasks.

]]> August 17, 2021tag:google.com,2016:kf-release-notes#August_17_20212021-08-17T00:00:00-07:002.5.1 

### Changed

Kf CLI can now override the manifest.yaml app name.

### Changed

When deleting resources, Kf will now delete any sub resources before returning success on the deletion request.

]]> July 30, 2021tag:google.com,2016:kf-release-notes#July_30_20212021-07-30T00:00:00-07:002.5 

### Announcement

New features may now start in preview and GA with the next Kf release.

### Announcement

New Early Access program (currently private preview).

### Feature

Automated assessment and migration of your existing CF foundation.

### Feature

[PREVIEW] NFS broker automatically configures NFS mounts on your cluster for Apps to bind to.

### Feature

[PREVIEW] Schedule Tasks to run at recurring intervals specified using the unix-cron format.

### Feature

[PREVIEW] Support for Anthos clusters on VMware via the Early Access program.

### Fixed

Minor reliability improvements.

### Fixed

Resolved race condition that could cause the first brokered service instance to fail.

### Changed

Support for ASM 1.10.

]]> June 29, 2021tag:google.com,2016:kf-release-notes#June_29_20212021-06-29T00:00:00-07:002.4.1 

### Feature

Kf Cloud Service Broker for Google Cloud for Google managed services.

### Fixed

Prevent creating a GSA policy when the GoogleProjectId field is not set.

### Changed

Allow customization of external-gateway in kfsystem.yaml.

]]> June 15, 2021tag:google.com,2016:kf-release-notes#June_15_20212021-06-15T00:00:00-07:002.4 

### Feature

Kf Operator to manage Kf installation. 

### Feature

Added Operator diagnostics to kf doctor.

### Feature

Allow target command to take arg instead of flag.

### Changed

Config Connector can manage the Kf Google Service Account (GSA).

### Changed

Removed internal routing dependency on internal-gateway.

### Changed

Inline environment variable printing in kf env.

### Changed

Config Connector is now required.

### Changed

Updated Tekton to 0.23.0.

### Fixed

Only check for timeout error for deprovisioning service instances.

### Fixed

Make targeting a non-existent Space an error.

### Fixed

Fixes manifest parsing bug.

]]> May 27, 2021tag:google.com,2016:kf-release-notes#May_27_20212021-05-27T00:00:00-07:002.3.2 

### Fixed

Prevent panic in reconcilers when a Space is not found.

]]>
