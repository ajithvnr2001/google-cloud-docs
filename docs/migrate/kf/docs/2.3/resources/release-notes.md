---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/resources/release-notes/
title: Kf version 2.3 release notes \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:36.993062+00:00
---

# Kf version 2.3 release notes  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/resources/release-notes/

Version 2.3

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Resources ](https://docs.cloud.google.com/migrate/kf/docs/2.3/resources)



Send feedback 

#  Kf version 2.3 release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Kf. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/kf-release-notes.xml) directly. 

## August 10, 2026

2.12.2

Change

  * Upgraded Go compiler and dependencies to 1.26.5 to resolve standard library vulnerabilities CVE-2026-39822 and CVE-2026-42505.



## January 29, 2026

2.11.31

Change

  * Update Copyright year (via ./hack/go-generate.sh)
  * Retry get Sourcepackage operation from listers with exponential backoff



## December 31, 2025

2.11.30

Change

  * Upgrade Tekton version to 1.6.0
  * Upgrade ASM to 1.27.4
  * Upgrade Config Connector to 1.141.0
  * Correct sample app



## October 06, 2025

2.11.29

Change

Upgrade ASM to 1.27.1

2.11.29

Change

Upgrade Tekton version to 1.3.2 and modify 'kf doctor' behavior and label selectors for pods to work with this Tekton version

## March 21, 2025

2.11.28

Change

Upgraded server-side dependencies - Tekton Pipelines, Config Connector

2.11.28

Change

Upgrade upload-pages-artifact dependency

## November 19, 2024

2.11.27

Change

Updated Go version used to build images and CLI tools

2.x.x

Change

Upgraded server-side dependencies - Tekton Pipelines, ASM

2.11.27

Change

Changed version of php-buildpack to address build issue.

## December 18, 2023

2.11.25

Change

Upgraded server-side dependencies - Tekton Pipelines, ASM & Config Connector

## September 27, 2023

2.11.21

Security

Removed permissions on auditor roles that they could use to exec in containers if they used websockets with the Kubernetes API.

2.11.21

Change

When spaces are updated, apps in the affected space will be enqueued on a best-effort basis to avoid blocking the main queue used for live interactions.

2.11.21

Feature

`kf push` now shows the amount of time source uploads took.

2.11.21

Fixed

The featureflag controller will no longer enqueue all namespaces when feature flags are changed, significantly reducing the load on the controller.

2.11.21

Change

The default snapshot mode for Kaniko builds in the v2 buildpacks is now fast rather than robust.

2.11.21

Feature

Kf builds now show the number of files extracted from the uploaded source directory.

2.11.21

Feature

Added the ability to change the snapshot modes for Kaniko for faster snapshots and reduced disk I/O during builds.

## August 23, 2022

2.11.5

Fixed

Fixed `set-env` slowness.

2.11.5

Change

Added limits to containers.

## August 22, 2022

2.11.4

Fixed

Fixed issue that liveness probe is not set properly.

## August 10, 2022

2.11.3

Fixed

Fix Kf performance issue with high server load.

## July 22, 2022

2.11.2

Change

Removed NFS sidecar, built the logics into user-container.

## July 18, 2022

2.11.1

Fixed

Fixed the issue that will cause delete-service stuck.

2.11.1

Fixed

Fixed the issue that App Pod will keep restarting when the mounted NFS volume is larger than cluster's ephemeral storage.

## July 11, 2022

2.11.0

Change

Builds will now be allowed up to 15 minutes to extract or publish images.

2.11.0

Fixed

Kf will now install with GKE 1.22 clusters.

2.11.0

Fixed

kf doctor now works with GKE 1.22 clusters.

2.11.0

Fixed

Kf will terminate Istio sidecars on completed tasks and builds freeing up IP addresses and compute resources for clusters running newer versions of Tekton.

## July 01, 2022

2.10.1

Breaking

Removed `kf migrate` command.

2.10.1

Change

Changed go version to 1.17.

## June 01, 2022

2.10.0

Change

Added support for mapping GID and UID for NFS.

2.10.0

Change

Fixed terminal size for Kf ssh.

2.10.0

Fixed

Fixed issue that unbind-service will not retry when failed.

## April 15, 2022

2.9.0

Change

Add Config Connector as a dependency of Kf.

## March 21, 2022

2.8.1

Fixed

Fixed bug in App controller, made App.Status.RouteConditions as an optional field.

## March 15, 2022

2.7.3

Fixed

Fixed bug in App controller, made `App.Status.RouteConditions` as an optional field.

## March 03, 2022

2.8.0

Change

Remove Config Connector as a dependency of Kf.

2.8.0

Feature

Add a feature that supports adding node selectors for Kf Builds to isolate Kf Build pods in specific node pool.

## February 01, 2022

2.7.2

Fixed

Bug fix for Kf Build garbage collection.

2.7.2

Feature

Added buildTimeout configuration feature.

## January 27, 2022

2.7.1

Change

Support for Anthos Service Mesh v1.12

## December 14, 2021

2.7

Feature

Added [`buildRetentionCount`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#build_retention) configuration feature.

2.7

Feature

Added [V3 Google stack](https://cloud.google.com/migrate/kf/docs/2.7/concepts/v2-vs-v3-buildpacks#configure_stacks) as build option.

2.7

Feature

Added [`controllerCACerts`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#self_signed_certificates_for_service_brokers) configuration feature.

2.7

Feature

Added [`buildPodResources`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#build_pod_resource_limits) configuration feature.

2.7

Feature

Added [V3 kf-v2-to-v3-shim stack](https://cloud.google.com/migrate/kf/docs/2.7/concepts/v2-vs-v3-buildpacks#v2_to_v3_buildpack_migration) as build option.

2.7

Feature

Added [`buildDisableIstioSidecar`](https://cloud.google.com/migrate/kf/docs/2.7/how-to/customizing-features#enable_or_disable_the_istio_sidecar) configuration feature.

2.7

Fixed

Fixed an issue that caused extra reconciliation loops and logs.

2.7

Fixed

Fixed an issue that could prevent SIGTERM from reaching an app.

2.7

Change

Improved CLI performance.

2.7

Change

Changed build ImagePullPolicy default from always download to prefer cached.

2.7

Change

Updated Config Connect to v1.66.0.

2.7

Change

Improved subresource API server resilience.

2.7

Change

Updated Tekton to v0.29.0.

2.7

Change

Improved Workload Identity reliability.

2.7

Change

Support for Anthos Service Mesh (ASM) v1.11+, which recommends ingress gateways be outside of the `istio-system` namespace.

## October 28, 2021

2.6.1

Fixed

Addressed a v2 buildpack condition that could prevent SIGTERM signals from propagating.

2.6.1

Change

VCAP_APPLICATION route string no longer includes trailing slash.

2.6.1

Fixed

Resolved a scenario that could result in extra reconciliation loops and logs.

## October 20, 2021

2.6

Announcement

Anthos clusters on VMware (GKE on-prem) support promoted to GA.

2.6

Announcement

Anthos clusters on bare metal support promoted to GA.

2.6

Feature

New [`wrap-v2-buildpack`](https://cloud.google.com/migrate/kf/docs/2.6/cli/kf-wrap-v2-buildpack) **experimental** command available. 

**Known issue:** some buildpacks (ex: https://github.com/cloudfoundry/java-buildpack) produce directories that do not work with the `pack` CLI.

2.6

Feature

Added support for `kubectl explain` to [inspect Kf CRDs](https://cloud.google.com/migrate/kf/docs/2.6/concepts/kf-dependencies#get_crd_details).

2.6

Fixed

Fixed condition where CLI may not always show build logs.

2.6

Fixed

Addressed scenario where the Kf operator could overwrite ASM Gateway customization.

2.6

Fixed

Fixed issue where `kf doctor` expects the ASM ingress gateway deployment to be in the `kf` namespace.

2.6

Change

Config Connector dependency updated to v1.60.

2.6

Change

Tekton dependency updated to v0.26.0.

## September 28, 2021

2.5.4

Fixed

Removed downstream lifecycle dependency for v2 buildpacks that could result in `kf push` failing.

## September 16, 2021

2.5.3

Change

Improved `kf doctor` reliability for Anthos on-prem clusters.

2.5.3

Fixed

Fixed an error that can occur during the initialization of the subresource API.

## September 08, 2021

2.5.2

Announcement

Kf for Anthos on-prem (Vsphere) is now available on the [Public Previews page](https://cloud.google.com/migrate/kf/docs/2.5/early-access/early-access).

2.5.2

Change

Changed flag and manifest validation for route and task fields so manifest routes are ignored when creating tasks.

2.5.2

Fixed

Addressed a potential panic in the kf build-logs command.

## August 17, 2021

2.5.1

Change

Kf CLI can now override the manifest.yaml app name.

2.5.1

Change

When deleting resources, Kf will now delete any sub resources before returning success on the deletion request.

## July 30, 2021

2.5

Announcement

New features may now start in preview and GA with the next Kf release.

2.5

Announcement

New Early Access program (currently private preview).

2.5

Feature

Automated assessment and migration of your existing CF foundation.

2.5

Feature

[PREVIEW] Support for Anthos clusters on VMware via the Early Access program.

2.5

Feature

[PREVIEW] Schedule Tasks to run at recurring intervals specified using the unix-cron format.

2.5

Feature

[PREVIEW] NFS broker automatically configures NFS mounts on your cluster for Apps to bind to.

2.5

Fixed

Minor reliability improvements.

2.5

Fixed

Resolved race condition that could cause the first brokered service instance to fail.

2.5

Change

Support for ASM 1.10.

## June 29, 2021

2.4.1

Feature

Kf Cloud Service Broker for Google Cloud for Google managed services.

2.4.1

Fixed

Prevent creating a GSA policy when the GoogleProjectId field is not set.

2.4.1

Change

Allow customization of external-gateway in kfsystem.yaml.

## June 15, 2021

2.4

Feature

Allow target command to take arg instead of flag.

2.4

Feature

Kf Operator to manage Kf installation.

2.4

Feature

Added Operator diagnostics to kf doctor.

2.4

Change

Config Connector is now required.

2.4

Change

Removed internal routing dependency on internal-gateway.

2.4

Change

Inline environment variable printing in kf env.

2.4

Change

Updated Tekton to 0.23.0.

2.4

Change

Config Connector can manage the Kf Google Service Account (GSA).

2.4

Fixed

Only check for timeout error for deprovisioning service instances.

2.4

Fixed

Fixes manifest parsing bug.

2.4

Fixed

Make targeting a non-existent Space an error.

## May 27, 2021

2.3.2

Fixed

Prevent panic in reconcilers when a Space is not found.

## April 22, 2021

2.3.1

Fixed

Allow long-running source uploads.

## March 31, 2021

2.3.0

Feature

Kf supports source code upload without workstation write access to Artifact Registry.

2.3.0

Feature

Kf supports Role-based access control in Spaces.

2.3.0

Feature

Kf doctor supports running per-object commands.

2.3.0

Fixed

Resolved issue with health-check-type=process.

2.3.0

Fixed

Ensure a ServiceBroker cannot be deleted if there is still an active ServiceInstance depending on it.

2.3.0

Fixed

Ensure a Space cannot be deleted if a ServiceInstance was not deleted.

2.3.0

Fixed

Run binding before push so VCAP_SERVICES is correct on the first deploy.

2.3.0

Fixed

Ensure log tailing prints the correct number of lines.

2.3.0

Change

Updated the ASM version to 1.9.1.

## February 11, 2021

2.2.0

Feature

Added `health-check-http-endpoint` flag to `kf push` command.

2.2.0

Change

Changed the kf CLI to use kubectl kubeconfig loading logic.

2.2.0

Feature

Added support for Task.

2.2.0

Change

Made `hostname` as an optional field when creating a route.

2.2.0

Feature

Added feature flags `enable_dockerfile_builds`, `enable_custom_buildpacks` and `enable_custom_stacks`.

2.2.0

Change

Updated the Tekton version to 0.19.0.

2.2.0

Fixed

Make routes available in `VCAP_APPLICATION`.

2.2.0

Feature

Added `--as` and `--as-group` global flags to support impersonation.

2.2.0

Feature

Added support for Node Selector.

## December 14, 2020

2.1.0

Fixed

Updated the Istio version to 1.7 and fixes the injection label.

2.1.0

Feature

Added support for the `kf-domains` subcommand so developers can look up which domains they can use in a Space. Operators can continue to use `kf configure-space` to modify domains.

2.1.0

Change

`kf doctor` now checks for correct Istio injection labels on spaces managed by Kf.

2.1.0

Feature

Added autoscaling capabilities to Kf.

2.1.0

Feature

Kf now shows a tip to run `kf bindings` after binding a service.

2.1.0

Feature

Added support for Nodes to `kf doctor`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
