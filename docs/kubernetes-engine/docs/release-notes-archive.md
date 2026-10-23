---
url: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive/
title: GKE release notes archive \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:55.997008+00:00
---

# GKE release notes archive  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE release notes archive Stay organized with collections  Save and categorize content based on your preferences. 

This page contains a historical archive of all release notes for Google Kubernetes Engine prior to 2020. To view more recent release notes, see the [Release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gke-main-release-notes.xml) directly. 

## December 23, 2019

### Rapid channel  
(1.16.x)

Feature

[Global access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#global_access) for internal TCP/UDP load balancing Services is now Beta. Global access allows internal load balancing IP addresses to be accessed from any region within a VPC. 

## December 13, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### No Channel

##### v.1.12.x

###### 1.12.10-gke.22

##### v.1.15.x

###### 1.15.4-gke.22

Feature

GKE 1.15 is generally available for new clusters. 

###### Upgrading

Before creating GKE v1.15 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#urgent-upgrade-notes). 

### New features

Feature

By default, firewall rules restrict your cluster master to only initiate TCP connections to your nodes on ports 443 (HTTPS) and 10250 (kubelet). For some Kubernetes features, you might need to add firewall rules to allow access on additional ports. For example, in Kubernetes 1.9 and older, kubectl top accesses heapster, which needs a firewall rule to allow TCP connections on port 8080. To grant such access, you can add firewall rules. 

Feature

Node-local DNS caching is now available in beta. This does create a single point of failure. If the node-cache goes down DNS for all Pods on that node will be broken until the cache is up. 

### Known Issues

Issue

There is a low risk that consumers of the published OpenAPI document that made assumptions about the **absence** of schema info for a given type (for example, "no schema info means a resource is a custom resource") could have those assumptions broken once custom resources start publishing schema definitions. 

### Stable channel  
and 1.13.x

##### Stable channel

There are no changes to the Stable channel this week.

##### No channel

  * 1.13.11-gke.15
  * 1.13.12-gke.16



### Regular channel  
and 1.14.x

##### Regular channel

There are no changes to the Regular channel, but 1.15 will be available in this channel in January 2020.

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

##### No channel

  * 1.14.7-gke.25
  * 1.14.8-gke.21
  * 1.14.9-gke.2



### Rapid channel  
(1.16.x)

##### Rapid channel

###### 1.16.0-gke.20

**Note:** Relevant content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE 1.16.0-gke.20 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

### Retired APIs

Deprecated

extensions/v1beta1, apps/v1beta1, and apps/v1beta2 won't be served by default. 

  * All resources under `apps/v1beta1` and `apps/v1beta2` \- use `apps/v1` instead. 
  * `daemonsets`, `deployments`, `replicasets` resources under `extensions/v1beta1` \- use `apps/v1` instead. 
  * `networkpolicies` resources under `extensions/v1beta1` \- use `networking.k8s.io/v1` instead. 
  * `podsecuritypolicies` resources under `extensions/v1beta1` \- use `policy/v1beta1` instead. 



### Changes

Change

New clusters have the `cos-metrics-enabled` flag enabled by default. This change allows kernel crash logs to be collected. You can disable by adding `--metadata cos-metrics-enabled=false` when you create clusters. 

### Fixed

Fixed

All of the versions made available include a fix for the issue where newly created node pools are created successfully but are incorrectly shown as PROVISIONING, as reported on December 6th, 2019. 

### New features

Feature

[Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), which was previously available in beta, is now generally available. 

### Changes

Change

The beta version of Stackdriver Kubernetes Engine Monitoring is no longer supported. 

Deprecated

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated. If you're using Legacy Stackdriver for logging or monitoring, you must [migrate to Stackdriver Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration) before Legacy Stackdriver is decommissioned. For more information, see [Legacy Stackdriver support for GKE deprecation.](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy)

## December 6, 2019

Issue

The December 4, 2019 rollout is paused. Versions that were made available for upgrades and new clusters in that release will no longer be available. This is to address an issue where newly created node pools are created successfully but are incorrectly shown as PROVISIONING. 

## December 4, 2019

### Fixed

We have fixed an issue with cluster upgrade from a version earlier than 1.14.2-gke.10 when gVisor is enabled in the cluster. It's now safe to upgrade to any version greater than 1.14.7-gke.17. This issue was originally noted in the release notes for October 30, 2019.

### Version updates

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

No new v1.12.x versions this week.

### Stable channel  
and 1.13.x

##### Stable channel

There are no changes to the Stable channel this week.

**Note:** Relevant content is also available separately in the [Stable channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable).

##### No channel

###### 1.13.12-gke.14

**Note:** 1.13.12-gke.14 is not yet available in the Stable channel. It is available to clusters that do not use a release channel.

Change

This version updates COS to [cos-stable-73-11647-348-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73#cos-73-11647-348-0) .

### Regular channel  
and 1.14.x

##### Regular channel

There are no changes to the Regular channel this week.

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

##### No channel

###### 1.14.8-gke.18

**Note:** 1.14.8-gke.18 is not yet available in the Stable channel. It is available to clusters that do not use a release channel.

Change

This version updates COS to [cos-stable-73-11647-348-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73#cos-73-11647-348-0) .

### Rapid channel  
(1.15.x)

##### Rapid channel

There are no changes to the Rapid channel this week.

## November 22, 2019

### Fixed

Fixed

The known issue in the COS kernel that may cause kernel panic, previously reported on November 5th, 2019, is resolved. The versions available in this release use updated versions of COS. GKE 1.12 uses [`cos-69-10895-348-0`](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69#cos-69-10895-348-0) and versions 1.13 and 1.14 use [cos-stable-73-11647-348-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73#cos-73-11647-348-0). 

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
1.12.10-gke.15 | 1.12.10-gke.17  
  
#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

##### 1.12.10-gke.20

Fixed

This version uses [`cos-69-10895-348-0`](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69#cos-69-10895-348-0) which fixes the known issue that may cause kernel panics, previously reported on November 5th, 2019. 

### Stable channel  
and 1.13.x

##### Stable channel

There are no changes to the Stable channel this week.

##### No channel

###### 1.13.12-gke.13

Fixed

This version uses [`cos-stable-73-11647-348-0`](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73#cos-73-11647-348-0) which fixes the known issue that may cause kernel panics, previously reported on November 5th, 2019. 

### Regular channel  
and 1.14.x

##### Regular channel

There are no changes to the Regular channel this week.

##### No channel

###### 1.14.8-gke.17

Fixed

This version uses [`cos-stable-73-11647-348-0`](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73#cos-73-11647-348-0) which fixes the known issue that may cause kernel panics, previously reported on November 5th, 2019. 

### Rapid channel  
(1.15.x)

##### Rapid channel

There are no changes to the Rapid channel this week.

#### Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.10-gke.15
  * 1.13.11-gke.5
  * 1.13.11-gke.9
  * 1.13.11-gke.11
  * 1.13.12-gke.2
  * 1.14.7-gke.10
  * 1.14.7-gke.14
  * 1.14.7-gke.17
  * 1.14.8-gke.2



## November 18, 2019

### Fixed

Fixed

The known issue in the COS kernel that may cause nodes to crash, previously reported on November 5th, 2019, is resolved. This release downgrades COS to [cos-73-11647-293-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#cos-73-11647-293-0). 

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
1.13.0-gke.0 to 1.13.11-gke.13 | 1.13.11-gke.14 (Stable channel)  
1.13.12-gke.0 to 1.13.12-gke.7 | 1.13.12-gke.8  
1.14.0-gke.0 to 1.14.7-gke.22 | 1.14.7-gke.23  
1.14.8-gke.0 to 1.14.8-gke.11 | 1.14.8-gke.12 (Regular channel)  
**Note:** 1.15 was unaffected by this issue.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

##### 1.12.10-gke.17

No new v1.12.x versions this week.

### Stable channel  
and 1.13.x

##### Stable channel

###### 1.13.11-gke.14

Fixed

This version includes a fix for a known issue in the COS kernel that may have caused nodes to crash.

**Note:** Relevant content is also available separately in the [Stable channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable).

##### No channel

###### 1.13.12-gke.8

**Note:** 1.13.12-gke.8 is not yet available in the Stable channel. It is available to clusters that do not use a release channel.

Fixed

This version includes a fix for a known issue in the COS kernel that may have caused nodes to crash.

### Regular channel  
and 1.14.x

##### Regular channel

###### 1.14.8-gke.12

Fixed

This version includes a fix for a known issue in the COS kernel that may have caused nodes to crash.

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

##### No channel

###### 1.14.7-gke.23

Fixed

This version includes a fix for a known issue in the COS kernel that may have caused nodes to crash.

### Rapid channel  
(1.15.x)

##### 1.15.4-gke.15

No new v1.15.x versions this week.

## November 11, 2019

### Changes

Change

After November 11, 2019, new clusters and node pools created with `gcloud` have [node auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) enabled by default.

## November 05, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
v1.12.x | 1.12.10-gke.15  
v1.13.x | 1.13.11-gke.5  
v1.14.x | 1.14.7-gke.10  
**Note:** Clusters using [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) are auto-upgraded when new versions are available in their channel as noted in the following sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

##### v1.12.10-gke.17

Fixed

This release includes a patch for the golang vulnerability CVE-2019-17596, fixed in go-boringcrypto 1.13.1 and 1.12.11.

Change

Updated containerd to [1.2.10](https://github.com/containerd/containerd/releases/tag/v1.2.10)

### Stable channel  
(1.13.x)

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

##### v1.13.11-gke.11

**Note:** This version is available to clusters that do not use a release channel.

Fixed

This release includes a patch for the golang vulnerability CVE-2019-17596, fixed in go-boringcrypto 1.13.1 and 1.12.11.

Change

Updated containerd to [1.2.10](https://github.com/containerd/containerd/releases/tag/v1.2.10)

##### v1.13.12-gke.2

**Note:** This version is available to clusters that do not use a release channel.

Fixed

This release includes a patch for the golang vulnerability CVE-2019-17596, fixed in go-boringcrypto 1.13.1 and 1.12.11.

Change

Updated containerd to [1.2.10](https://github.com/containerd/containerd/releases/tag/v1.2.10)

### Regular channel  
(1.14.x)

##### v1.14.7-gke.17

Fixed

This release includes a patch for the golang vulnerability CVE-2019-17596, fixed in go-boringcrypto 1.13.1 and 1.12.11.

##### v1.14.8-gke.2

Fixed

This release includes a patch for the golang vulnerability CVE-2019-17596, fixed in go-boringcrypto 1.13.1 and 1.12.11.

### Rapid channel  
(1.15.x)

##### v1.15.4-gke.18

**Note:** Relevant content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE 1.15.4-gke.18 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For more details, refer to the [release notes for Kubernetes v1.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md).

Fixed

This release includes a patch for the golang vulnerability CVE-2019-17596, fixed in go-boringcrypto 1.13.1 and 1.12.11.

### Known issues

Issue

We have found an issue in COS that might cause kernel panics on nodes.

This impacts node versions: 

  * 1.13.11-gke.9
  * 1.13.11-gke.11
  * 1.13.11-gke.12
  * 1.13.12-gke.1
  * 1.13.12-gke.2
  * 1.13.12-gke.3
  * 1.13.12-gke.4
  * 1.14.7-gke.14
  * 1.14.7-gke.17
  * 1.14.8-gke.1
  * 1.14.8-gke.2
  * 1.14.8-gke.6
  * 1.14.8-gke.7



A patch is being tested and will rollout soon, but we recommend customers avoid these node versions or downgrade to previous, unaffected patches.

### New features

Feature

[Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#surge) are now in beta. Surge upgrades allow you to configure speed and disruption of node upgrades 

### Changes

Change

[Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) has reached General Availability. Node auto-provisioning creates or deletes node pools from your cluster based upon resource requests. 

## October 30, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version

The default version for new clusters is now v1.13.11-gke.9 (previously v1.13.10-gke.0). Clusters enrolled in the stable [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) will be auto-upgraded to this version.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
1.12.x versions | 1.12.10-gke.17  
1.13.x versions | 1.13.11-gke.5  
1.14.x versions | 1.14.7-gke.10  
**Note:** Clusters using [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) are auto-upgraded when new versions are available in the relevant release channels, as noted in the following sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

No new v1.12.x versions this week.

### Stable channel  
and 1.13.x

##### Stable channel

**Note:** Relevant content is also available separately in the [Stable channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable).

###### 1.13.11-gke.9

Change

Update containerd to 1.2.10.

Change

Update COS to cos-u-73-11647-329-0.

Fixed

This release includes a patch for [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253). For more information, see the [security bulletin for October 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#october_16_2019). 

### Regular channel  
and 1.14.x

##### Regular channel

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

###### 1.14.7-gke.10

This version was generally available on [October 18, 2019](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#october_18_2019) and is now available in the Regular [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

Fixed

This release includes a patch for [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253). For more information, see the [security bulletin for October 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#october_16_2019). 

##### No channel

###### 1.14.7-gke.14

**Note:** 1.14.7-gke.14 is not yet available in the Regular channel. It is available to clusters that do not use a release channel.

Change

Update COS to cos-u-73-11647-329-0.

### Rapid channel  
(1.15.x)

##### 1.15.4-gke.17

**Note:** Relevant content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE 1.15.4-gke.17 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

Fixed

Fixes a known issue reported on [October 11, 2019](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid#october_11_2019) regarding fdatasync performance regression on COS/Ubuntu. Node image for Container-Optimized OS updated to [cos-77-12371-89-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#cos-stable-77-12371-89-0). Node image for Ubuntu updated to [ubuntu-gke-1804-d1903-0-v20191011a](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1903-0-v20191011a.manifest)

#### Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.10-gke.15
  * 1.13.7-gke.24
  * 1.13.9-gke.3
  * 1.13.9-gke.11
  * 1.13.10-gke.0
  * 1.13.10-gke.7
  * 1.14.6-gke.1
  * 1.14.6-gke.2
  * 1.14.6-gke.13



### Known Issues

Issue

If you use Sandbox Pods in your GKE cluster and plan to upgrade from a version less than 1.14.2-gke.10 to a version greater than 1.14.2-gke.10, you need to manually run `kubectl delete mutatingwebhookconfiguration gvisor-admission-webhook-config` after the upgrade. 

## October 18, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
1.12.x versions | 1.13.7-gke.24  
1.14.x versions 1.14.6-gke.0 and older | 1.14.6-gke.1  
**Note:** Clusters using [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) are auto-upgraded when new versions are available in the relevant release channels, as noted in the following sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

##### 1.12.10-gke.15

Fixed

This release includes a patch for [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253). For more information, see the [security bulletin for October 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#october_16_2019). 

### Stable channel  
and 1.13.x

##### Stable channel

There are no changes to the Stable channel this week.

**Note:** Relevant content is also available separately in the [Stable channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable).

##### No channel

###### 1.13.11-gke.5

**Note:** 1.13.11-gke.5 is not yet available in the Stable channel. It is available to clusters that do not use a release channel.

Fixed

This release includes a patch for [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253). For more information, see the [security bulletin for October 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#october_16_2019). 

### Regular channel  
and 1.14.x

##### Regular channel

There are no changes to the Regular channel this week.

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

##### No channel

###### 1.14.7-gke.10

**Note:** 1.14.7-gke.10 is not yet available in the Regular channel. It is available to clusters that do not use a release channel.

Fixed

This release includes a patch for [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253). For more information, see the [security bulletin for October 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#october_16_2019). 

### Rapid channel  
(1.15.x)

##### 1.15.4-gke.15

**Note:** Relevant content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE 1.15.4-gke.15 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

Fixed

This release includes a patch for [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253). For more information, see the [security bulletin for October 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#october_16_2019). 

#### Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.9-gke.15
  * 1.12.9-gke.16
  * 1.12.10-gke.5
  * 1.12.10-gke.11



### Security bulletin

Issue

A vulnerability was recently discovered in Kubernetes, described in [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253), which allows any user authorized to make POST requests to execute a remote Denial-of-Service attack on a Kubernetes API server. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#october_16_2019). 

## October 11, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version

The default version for new clusters is now v1.13.10-gke.0 (previously v1.13.7-gke.24). Clusters enrolled in the stable [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) will be auto-upgraded to this version.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
versions older than 1.12.9-gke.13 | 1.12.9-gke.15  
1.13.x versions older than 1.13.7-gke.19 | 1.13.7-gke.24  
1.14.x versions older than 1.14.6-gke.0 | 1.14.6-gke.1  
**Note:** Clusters using [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) are auto-upgraded when new versions are available in the relevant release channels, as noted in the following sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

##### 1.12.10-gke.11

Change

Upgrade containerd to [ 1.2.9](https://github.com/containerd/containerd/releases/tag/v1.2.9)

Change

Node image for Container-Optimized OS updated to [cos-69-10895-348-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#cos-69-10895-348-0). 

Change

Node image for Ubuntu updated to [ubuntu-gke-1804-d1703-0-v20190917](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1703-0-v20190917.manifest)). 

### Stable channel  
(1.13.x)

##### Stable channel

**Note:** Relevant content is also available separately in the [Stable channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable).

###### 1.13.10-gke.0

This version was generally available on [September 16, 2019](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#september_16_2019) and is now available in the Stable [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

Fixed

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more information, see the [security bulletin for September 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#september_16_2019). 

##### No channel

###### 1.13.10-gke.7

**Note:** 1.13.10-gke.7 is not yet available in the Stable channel. It is available to clusters that do not use a release channel.

Change

Upgrade containerd to [ 1.2.9](https://github.com/containerd/containerd/releases/tag/v1.2.9)

Change

Node image for Container-Optimized OS updated to [cos-u-73-11647-293-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#cos-73-11647-293-0). 

Change

Node image for Ubuntu updated to [ubuntu-gke-1804-d1809-0-v20190918](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190918.manifest). Upgrades Nvidia GPU driver to 418 driver, adds Vulkan ICD for graphical workloads, and fixes nvidia-uvm installation order. 

### Regular channel  
(1.14.x)

##### Regular channel

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

###### 1.14.6-gke.1

This version was generally available on [September 9, 2019](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#september_9_2019) and is now available in the Regular [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

##### No channel

###### 1.14.6-gke.13

**Note:** 1.14.6-gke.13 is not yet available in the Regular channel. It is available to clusters that do not use a release channel.

Feature

Enable SecureBoot on master VMs.

Change

Node image for Container-Optimized OS updated to [cos-u-73-11647-293-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#cos-73-11647-293-0). 

Change

Node image for Ubuntu updated to [ubuntu-gke-1804-d1809-0-v20190918](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190918.manifest). Upgrades Nvidia GPU driver to 418 driver, adds Vulkan ICD for graphical workloads, and fixes nvidia-uvm installation order. 

Change

Upgrades GPU device plugin to the latest version with Vulkan support.

Issue

**Do not upgrade to this version if you use** [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). There is a known issue where the gke-metadata-server Pods crashloop if you create or uprade a cluster to 1.14.6-gke.13. 

Fixed

Fixes an issue where cronjobs cannot be scheduled when the total number of existing jobs exceeds 500.

### Rapid channel  
(1.15.x)

##### 1.15.3-gke.18

**Note:** Relevant content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE 1.15.3-gke.18 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

Change

Upgraded Istio to 1.2.5. 

Change

Improvements to gVisor. 

Change

Node image for Container-Optimized OS updated to cos-rc-77-12371-44-0. This update includes upgrading the kernel to 4.19 from 4.14 and upgrading Docker to 19.03 from 18.09.

Change

Node image for Ubuntu updated to ubuntu-gke-1804-d1903-0-v20190917a. This update includes upgrading the kernel to 5 from 4.15 and upgrading Docker to 19.03 from 18.09. 

Issue

**Do not update to this version if you have clusters with hundreds of nodes per cluster or with I/O intensive workloads.** Clusters with these characteristics may be impacted by a known issue in versions 4.19 and 5.0 of the Linux kernel that introduces performance regressions in the `fdatasync` system call. 

#### Versions no longer available

v1.14.3-gke.11 is no longer available for new clusters or upgrades.

### Features

Feature

[Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) is now generally available. 

Feature

[Vertical Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) is now generally available. 

### Changes

Change

Upgrade [Cloud Run on GKE](https://docs.cloud.google.com/run/docs/gke/release-notes) to 0.9.0.

### Fixed issues

Fixed

Fixed a bug with fluentd that would prevent new nodes from starting on large clusters with over 1000 nodes on v1.12.6. 

## October 2, 2019

Feature

[Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) now give you granular control over when automatic maintenance occurs on your clusters. You can specify the start time, duration, and recurrence of a cluster's maintenance window. You can also designate specific periods of time when non-essential automatic maintenance should not occur. 

## September 26, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version

The default version for new clusters is now v1.13.7-gke.24 (previously v1.13.7-gke.8). Clusters enrolled in the stable [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) will be auto-upgraded to this version.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
versions older than 1.12.9-gke.13 | 1.12.9-gke.15  
1.13.x versions older than 1.13.7-gke.19 | 1.13.7-gke.24  
**Note:** Clusters using [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) are auto-upgraded when new versions are available in the relevant release channels, as noted in the following sections.

Auto-upgrades are currently occurring two days behind the [rollout schedule](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#rollout_schedule). Some 1.11 clusters will be upgraded to 1.12 in the week of October 7th.

Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### 1.12.x

No new v1.12.x versions this week.

### Stable channel  
(1.13.x)

No new v1.13.x versions this week.

Change

v1.13.7-gke.24 is now available in the Stable release channel. 

### Regular channel  
(1.14.x)

There are no changes to the Regular channel in this release.

**Note:** 1.14.6-gke.2 is not yet available in the Regular channel. It is available to clusters that do not use a release channel.**Note:** This version was previously available in the Rapid channel.

##### 1.14.6-gke.2

Fixed

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. 

Change

Reduces startup time for GPU nodes running [Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#container-optimized_os). 

### Rapid channel  
(1.15.x)

GKE 1.15.3-gke.1 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

For more details, refer to the [release notes for Kubernetes v1.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md).

Change

Starting with GKE v1.15, the open source [Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/) is no longer natively supported in GKE as a managed add-on. To deploy it manually, follow the [deployment instructions](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#deploying-the-dashboard-ui) in the Kubernetes Dashboard documentation. 

Change

Resizing PersistentVolumes is now a beta feature. As part of this change, resizing a PersisntentVolume no longer requires you to restart the Pod. 

#### Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.7-gke.25
  * 1.12.7-gke.26
  * 1.12.8-gke.10
  * 1.12.8-gke.12
  * 1.12.9-gke.7
  * 1.12.9-gke.13
  * 1.13.6-gke.13
  * 1.13.7-gke.8
  * 1.13.7-gke.19



## September 20, 2019

Feature

[Ingress Controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) v1.6, which was previously available in beta, is generally available for clusters running v1.13.7-gke.5 and higher. 

Along with Ingress Controller, the following are also generally available: 

  * [Configuring load balancing through Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress)
  * [Using multiple SSL certificates in HTTP(s) load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-multi-ssl)
  * [HTTP/2 for load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-http2)



This note has been corrected. [Using Google-managed SSL certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs) is currently in Beta. 

## September 16, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

The release notes for September 16, 2019 were incorrectly published early, on September 9. The incorrect release notes included an announcement of the availability of a security patch that was not actually made available on that date. For more information about the security patch, see the [security bulletin for September 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#september_16_2019).

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
v1.11 | v1.12  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

##### v1.12.10-gke.5

Fixed

Fixes an issue where Vertical Pod Autoscaler would reject valid Pod patches. 

### Stable channel  
(1.13.x)

**Note:** Relevant content is also available separately in the [Stable channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable).

##### 1.13.10-gke.0

**Note:** This version is not yet available in the Stable channel. It is available to clusters that do not use a release channel.

Fixed

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more information, see the [security bulletin for September 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#september_16_2019). 

Change

Reduces startup time for GPU nodes running [Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#container-optimized_os). 

##### v1.13.7-gke.8

This version was generally available on [June 27, 2019](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#june_27_2019) and is now available in the Stable [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

### Regular channel  
(1.14.x)

**Note:** Relevant content is also available separately in the [Regular channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular).

##### v1.14.6-gke.1

**Note:** This version is not yet available in the Regular channel. It is available to clusters that do not use a release channel.

Fixed

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more information, see the [security bulletin for September 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#september_16_2019). 

Change

Reduces startup time for GPU nodes running [Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#container-optimized_os). 

##### v1.14.3-gke.11

This version was generally available on [September 5, 2019](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#september_5_2019) and is now available in the Regular [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

### Rapid channel  
(1.14.x)

##### v1.14.6-gke.1

**Note:** Relevant content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE v1.14.6-gke.1 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For more details, refer to the [release notes for Kubernetes v1.14.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v1146).

Fixed

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more information, see the [security bulletin for September 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#september_16_2019). 

Change

Reduces startup time for GPU nodes running [Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#container-optimized_os). 

### New features

Feature

**Correction:** This note was incorrectly published early. Ingress Controller v1.6 became generally available on September 20, 2019.

Ingress Controller v1.6, which was previously available in beta, is generally available for clusters running v1.13.7-gke.5 and higher. 

Feature

[Network Endpoint Groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing), which allow HTTP(S) load balancers to target Pods directly, are now generally available. 

Feature

[Release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), which provide more control over which automatic upgrades your cluster receives, are generally available. In addition to the Rapid channel, you can now enroll your clusters in the Regular or Stable channel. 

## September 9, 2019

### Correction

The release notes for September 16, 2019 were incorrectly published early, on September 9. The incorrect release notes included an announcement of the availability of a security patch that was not actually made available until the week of September 16, 2019. For more information avbout the patch, see the [security bulletin for September 16, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#september_16_2019).

No GKE releases occurred the week of September 9, 2019.

## September 5, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version

The default version for new clusters is now 1.13.7-gke.8 (previously 1.12.8-gke.10).

#### Scheduled automatic upgrades

Auto-upgrades are no longer paused.

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | upgrade version  
---|---  
1.11.x | 1.12.7-gke.25  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades:

  * 1.11.10-gke.6



#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.12.x

##### 1.12.9-gke.16

Minor bug fixes and performance improvements.

### v1.13.x

##### 1.13.9-gke.3

Bug fixes and performance improvements.

### v1.14.x

##### 1.14.3-gke.11

Feature

GKE 1.14 is generally available. 

**Note:** If you created a v1.14.x cluster using the Rapid channel, you cannot currently modify the cluster to use a non-Rapid version. To keep the cluster running v1.14.x, re-create the cluster without enrolling it in the Rapid channel. 

###### Upgrading

Before [upgrading clusters to GKE v1.14](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster), you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#urgent-upgrade-notes). 

For example, the default RBAC policy no longer grants access to discovery and permission-checking APIs, and you must take specific action to preserve the old behavior for newly-created cluster users. 

###### Differences between GKE v1.14.x and Kubernetes 1.14

GKE v1.14.x has the following differences from [Kubernetes 1.14.x](https://kubernetes.io/blog/2019/03/25/kubernetes-1-14-release-announcement/): 

  * Storage Migrator is not supported on GKE v1.14.x.

  * CSI Inline Volumes (Alpha) are not supported on GKE v1.14.x.

  * Huge Pages is not supported on GKE 1.14.x. If you are interested in support for Huge Pages, [register your interest](https://docs.google.com/forms/d/e/1FAIpQLScxvLni5-6_2m0oUpD1i5ekyiZj7aW30JULLwoQnPy00x5B5Q/viewform?usp=sf_link). 




###### New features

Feature

[Pod Ready++](https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/580-pod-readiness-gates#pod-ready) is generally available and supported on GKE v1.14.x. 

Feature

[Pod priority and preemption](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/) is generally available and supported on GKE v1.14.x.

Feature

The [RunAsGroup](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) feature has been promoted to beta and enabled by default. PodSpec and PodSecurityPolicy objects can be used to control the primary GID of containers on Docker and containerd runtimes. 

Feature

Early-access to test Windows containers is now available. If you are interested in testing Windows containers, fill out [this form](http://j.mp/gke-windows). 

###### Other changes

Change

The `node.k8s.io` API group and `runtimeclasses.node.k8s.io` resource have been migrated to a built-in API. If you were using RuntimeClasses, you must recreate each of them after upgrading, and also delete the `runtimeclasses.node.k8s.io` CRD. RuntimeClasses can no longer be created without a defined handler. 

Change

When creating a new GKE cluster, Stackdriver Kubernetes Engine Monitoring is now the default Stackdriver support option. This is a change from prior versions where Stackdriver Logging and Stackdriver Monitoring were the default Stackdriver support option. For more information, see [Overview of Stackdriver support for GKE](https://docs.cloud.google.com/monitoring/kubernetes-engine). 

Deprecated

OS and Arch information is now recorded in `kubernetes.io/os` and `kubernetes.io/arch` labels on Node objects. The previous labels (`beta.kubernetes.io/os` and `beta.kubernetes.io/arch`) are still recorded, but are deprecated and targeted for removal in Kubernetes 1.18. 

###### Known Issues

Issue

Users with the Quobyte Volume plugin are advised not to upgrade between GKE 1.13.x and 1.14.x due to an issue with Kubernetes 1.14. This will be fixed in an upcoming release. 

Bug fixes and performance improvements.

### Rapid

The following versions are available to clusters enrolled in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

**Note:** This content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

##### 1.14.5-gke.5

GKE 1.14.5-gke.5 is now available in the Rapid release channel. It includes bug fixes and performance improvements. For more details, refer to the [release notes for Kubernetes v1.14](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1144).

### New features

Feature

[Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) is generally available.

Feature

You can now use [Customer-managed encryption keys (beta)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dynamic-provisioning-cmek) to control the encryption used for attached persistent disks in your clusters. This is available as a dynamically provisioned PersistentVolume. 

Feature

Both [containerd on Container-Optimized OS (cos_containerd)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos-containerd) and [containerd on Ubuntu (ubuntu_containerd)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#ubuntu-containerd) node images are generally available.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## August 22, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled automatic upgrades

Auto-upgrades are currently paused.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.11.x

##### 1.11.10-gke.6

Fixed

This version was previously released and is available again. It mitigates against the vulnerability described in the [security bulletin published on August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

### v1.12.x

Multiple v1.12.x versions are available this week: 

##### 1.12.9-gke.13

Fixed

This version mitigates against the vulnerability described in the [security bulletin published on August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

##### 1.12.9-gke.15

Fixed

Fixes an issue that can cause Horizontal Pod Autoscaler to increase the replica count to the maximum, regardless of other autoscaling factors. 

Fixed

Upgrade Istio to 1.1.13, to address address [two vulnerabilities](https://istio.io/blog/2019/istio-security-003-004/) announced by the Istio project. These vulnerabilities can be used to mount a Denial of Service (DoS) attack against services using Istio.

Change

The node image for Container-Optimized OS (COS) is now [cos-69-10895-329-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69). 

### v1.13.x

Multiple v1.13.x versions are available this week: 

##### 1.13.7-gke.19

Fixed

This version mitigates against the vulnerability described in the [security bulletin published on August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

##### 1.13.7-gke.24

Fixed

Fixes an issue that can cause Horizontal Pod Autoscaler to increase the replica count to the maximum during a rolling update, regardless of other autoscaling factors. 

Fixed

Upgrade Istio to 1.1.13, to address address [two vulnerabilities](https://istio.io/blog/2019/istio-security-003-004/) announced by the Istio project. These vulnerabilities can be used to mount a Denial of Service (DoS) attack against services using Istio.

Change

The node image for Container-Optimized OS (COS) is now [cos-73-11647-267-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73). 

### Rapid channel

##### 1.14.3-gke.11

**Note:** This content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE 1.14.3-gke.11 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For more details, refer to the [release notes for Kubernetes v1.14](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md).

Fixed

This version mitigates against the vulnerability described in the [security bulletin published on August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

Fixed

Upgrade Istio to 1.1.13, to address address [two vulnerabilities](https://istio.io/blog/2019/istio-security-003-004/) announced by the Istio project. These vulnerabilities can be used to mount a Denial of Service (DoS) attack against services using Istio.

Change

The node image for Container-Optimized OS (COS) is now [cos-73-11647-267-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73). 

### New features

Feature

[Config Connector](https://docs.cloud.google.com/config-connector) is a Kubernetes addon that allows you to manage your Google Cloud resources through Kubernetes configuration.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## August 12, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Important information about v1.10.x nodes

In addition to GKE's [version policy](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades), Kubernetes has a [version skew policy](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only the three newest minor versions. Older versions are not guaranteed to receive bug fixes or security updates, and the control plane may become incompatible with nodes running unsupported versions.

Specifically, the Kubernetes v1.13.x control plane is not compatible with nodes running v1.10.x. Clusters in such a configuration could become unreachable or fail to run your workloads correctly. Additionally, **security patches are not applied to v1.10.x and below.**

We previously published a notice that Google would enable node auto-upgrade to node pools running v1.10.x or lower, to bring those clusters into a supported configuration and mitigate the incompatibility risk described above. To allow for sufficient time for customers to complete the upgrade themselves, Google postponed upgrading cluster control planes to 1.13 until mid-September 2019. Please plan your manual node upgrade to keep your clusters healthy and up to date.

#### Scheduled automatic upgrades

Auto-upgrades are currently paused.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.11.x

##### 1.11.10-gke.6

Fixed

Fixes the vulnerability announced in the [security bulletin for August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

Fixed

Fixes a problem where Cluster Autoscaler can create too many nodes when scaling up. 

### v1.12.x

Multiple v1.12.x versions are available this week:

##### 1.12.9-gke.13

**Note:** This version contains all the changes in 1.12.9-gke.10, as well as those listed here.

Fixed

Fixes the vulnerability announced in the [security bulletin for August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

Fixed

Fixes a problem where Cluster Autoscaler can create too many nodes when scaling up. 

##### 1.12.9-gke.10

Fixed

Fixes a problem where Vertical Pod Autoscaler would reject valid patches to Pods. 

Fixed

Improvements to Cluster Autoscaler. 

Fixed

Updates Istio to v1.0.9-gke.0. 

##### v1.12.8-gke.12

Fixed

Updates Istio to v1.0.9-gke.0. 

##### 1.12.7-gke.2

Fixed

Updates Istio to v1.0.9-gke.0. 

Fixed

Fixes a [problem](https://github.com/kubernetes/kubernetes/pull/79451) where the kubelet could fail to start a Pod for the first time if the node was not completely configured and the Pod's restart policy was `NEVER`. 

### v1.13.x

Multiple v1.13.x versions are available this week:

##### 1.13.7-gke.19

**Note:** This version contains all the changes in 1.13.7-gke.15, as well as those listed here.

Fixed

Fixes the vulnerability announced in the [security bulletin for August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

Fixed

Fixes a problem where Cluster Autoscaler can create too many nodes when scaling up. 

##### 1.13.7-gke.15

Fixed

Fixes a problem where Vertical Pod Autoscaler would reject valid patches to Pods. 

Fixed

Improvements to Cluster Autoscaler. 

Feature

You can now use [Vulkan](https://www.khronos.org/vulkan/) with GPUs to process graphics workloads. The Vulkan configuration directorhy is mounted on `/etc/vulkan/icd.d` in the container. 

Fixed

Updates Istio to v1.1.10-gke.0. 

Fixed

Fixes a [problem](https://github.com/kubernetes/kubernetes/pull/79451) where the kubelet could fail to start a Pod for the first time if the node was not completely configured and the Pod's restart policy was `NEVER`. 

### Rapid (v1.14.x)

##### 1.14.3-gke.10

**Note:** This content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE 1.14.3-gke.10 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For more details, refer to the [release notes for Kubernetes v1.14](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md).

Fixed

Fixes the vulnerability announced in the [security bulletin for August 5, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

Fixed

Fixes a problem where Cluster Autoscaler can create too many nodes when scaling up. 

Change

In v1.14.3-gke.10 and higher, [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) uses the `gvisor.config.common-webhooks.networking.gke.io` webhook, which is created when the cluster starts and makes sandboxed nodes available faster. 

### Security bulletin

Issue

Kubernetes recently discovered a vulnerability, [CVE-2019-11247](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247), which allows cluster-scoped custom resource instances to be acted on as if they were namespaced objects existing in all Namespaces. This vulnerability is fixed in GKE versions also announced today. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-05-2019). 

### New features

Feature

Clusters running v1.13.6-gke.0 or higher can use [Shielded GKE Nodes (beta)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes), which provide strong, verifiable node identity and integrity to increase the security of your nodes. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## August 1, 2019

**Note:** Auto-upgrades for masters and nodes are currently paused.

### New versions available for upgrades and new clusters

During the week of July 8, 2019, a release resulted in a partial rollout. Release notes were not published at that time. Changes discussed in the rest of this entry were applied **only to the following zones** :

  * `europe-west2-a`
  * `us-east1`
  * `us-east1-d`



In those zones only, the following new versions are available:

  * 1.13.7-gke.15
  * 1.12.9-gke.10
  * 1.12.7-gke.26
  * 1.12.8-gke.12



In those zones only, the following versions are no longer available for new clusters or nodes:

  * 1.11.10-gke.5



In those zones only, clusters running v1.11.x with auto-upgrade enabled were upgraded to v1.12.7-gke.25.

### Security bulletin

Fixed

GKE v1.13.7.x includes patches that mitigate multiple vulnerabilities that are present in v1.13.6. Clusters running any v1.13.6.x version should upgrade to 1.13.7.x, to mitigate against these vulnerabilities, which are described in the following security bulletins: 

  * [June 25, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019)
  * [May 31, 2019](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-31-2019)



### New features

Feature

GKE usage metering (Beta) now supports tracking actual consumption, in addition to resource requests, for clusters running v1.12.8-gke.8 and higher, v1.13.6-gke.7 and higher, or 1.14.2-gke.8 and higher. A new BigQuery table, `gke_cluster_resource_consumption`, is created automatically in the BigQuery dataset. For more information about this and other improvements to Usage Metering, see [Usage metering (Beta)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering). 

Feature

[Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) is supported on regional clusters running v1.12.x or higher. 

## July 29, 2019

Change

VPC-native is **no longer** the default cluster network mode for new clusters created using `gcloud` v256.0.0 or higher. Instead, the routes-based cluster network mode is used by default. We recommend manually enabling [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips), to avoid exhausting routes quota. 

VPC-native clusters are created by default when you use Google Cloud console or `gcloud` versions 251.0.0 through 255.0.0. Routes-based clusters are created by default when using the REST API. 

## June 27, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Important changes to clusters running unsupported versions

In addition to GKE's [version policy](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades), Kubernetes has a [version skew policy](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only the three newest minor versions. Older versions are not guaranteed to receive bug fixes or security updates, and the control plane may become incompatible with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes running v1.10.x. Clusters in such a configuration could become unreachable or fail to run your workloads correctly. Additionally, security patches are not applied to v1.10.x and below.

To keep your clusters operational and to protect Google's infrastructure, we strongly recommend that you upgrade existing nodes to v1.11.x or higher before the end of June 2019. At that time, Google will enable node auto-upgrade on node pools older than v1.11.x, and these nodes will be updated to v1.11.x so that the control plane can be upgraded to v1.13.x and remain compatible with existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

NOTE: As of 1.12 all kubelets are issued certificates from the cluster CA and verification of kubelet certificates is enabled automatically if all nodepools are 1.12+. We have observed that introducing older (pre 1.12) nodepools after certificate verification has started may cause connection problems for kubectl logs/exec/attach/portforward commands, and should be avoided.

#### Versions no longer available for upgrades and new clusters

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.11.8-gke.10
  * 1.11.10-gke.4
  * 1.12.7-gke.10
  * 1.12.7-gke.21
  * 1.12.7-gke.22
  * 1.12.8-gke.6
  * 1.12.8-gke.7
  * 1.12.9-gke.3
  * 1.13.6-gke.5
  * 1.13.6-gke.6
  * 1.13.7-gke.0



#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.11.x

##### 1.11.10-gke.5

Fixed

This version contains a patch for recently discovered TCP vulnerabilities in the Linux kernel. See the associated [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) for more information. 

### v1.12.x

##### 1.12.7-gke.25

Fixed

This version contains a patch for recently discovered TCP vulnerabilities in the Linux kernel. See the associated [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) for more information. 

##### 1.12.8-gke.10

Fixed

This version contains a patch for recently discovered TCP vulnerabilities in the Linux kernel. See the associated [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) for more information. 

##### 1.12.9-gke.7

Fixed

This version contains a patch for recently discovered TCP vulnerabilities in the Linux kernel. See the associated [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) for more information. 

### v1.13.x

##### 1.13.6-gke.13

Fixed

This version contains a patch for recently discovered TCP vulnerabilities in the Linux kernel. See the associated [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) for more information. 

##### 1.13.7-gke.8

Fixed

This version contains a patch for recently discovered TCP vulnerabilities in the Linux kernel. See the associated [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) for more information. 

### Rapid channel

##### 1.14.3-gke.9

Fixed

This version contains a patch for recently discovered TCP vulnerabilities in the Linux kernel. See the associated [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) for more information. 

**Note:** This content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

### Security bulletins

Fixed

Patched versions are now available to address TCP vulnerabilities in the Linux Kernel. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019) In accordance with the documented support policy, patches will not be applied to GKE version 1.10 and older. 

Issue

Kubernetes recently discovered a vulnerability in `kubectl`, CVE-2019-11246. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#june-25-2019). 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Early access to test Windows Containers
  * [Usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) will become generally available



## June 4, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
1.11.9 | 1.12.7-gke.10  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.11.8-gke.6
  * 1.11.9-gke.8
  * 1.11.9-gke.13
  * 1.14.2-gke.1 [Preview]



#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.11.x

No v1.11.x versions this week.

### v1.12.x

v1.12.8-gke.7 includes the following changes:

Change

Improved Node Auto-Provisioning support for multi-zonal clusters with GPUs.

Cloud Run 0.6

### v1.13.x

v1.13.6-gke.6 includes the following changes:

Change

Improved Node Auto-Provisioning support for multi-zonal clusters with GPUs.

Cloud Run 0.6

COS images now use the Nvidia GPU 418.67 driver. Nvidia drivers on COS are now pre-compiled, greatly reducing driver installation time.

Issue

GKE nodes running Kubernetes v1.13.6 are affected by CVE-2019-11245. Information about the impact and mitigation of this vulnerability is available in this [Kubernetes issue report](https://github.com/kubernetes/kubernetes/issues/78308). In addition to security concerns, this bug can cause Pods that must run as a specific UID to fail.

### Rapid channel

Change

v1.14.1-gke.5 is the default for new Rapid channel clusters. This version includes patched node images that address [CVE-2019-11245](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-31-2019).

Issue

GKE nodes running Kubernetes v1.14.2 are affected by CVE-2019-11245. Information about the impact and mitigation of this vulnerability is available in this [Kubernetes issue report](https://github.com/kubernetes/kubernetes/issues/78308). In addition to security concerns, this bug can cause Pods that must run as a specific UID to fail.

### Security bulletin

Issue

GKE nodes running Kubernetes v1.13.6 and v1.14.2 are affected by CVE-2019-11245. Information about the impact and mitigation of this vulnerability is available in this [Kubernetes issue report](https://github.com/kubernetes/kubernetes/issues/78308). In addition to security concerns, this bug can cause Pods that must run as a specific UID to fail.

### Changes

Change

Currently, [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) is the default for new clusters created with `gcloud` or the Google Cloud console. However, VPC-native is not the default for new clusters created with the REST API. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Early access to test Windows Containers
  * [Usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) will become generally available
  * New clusters will begin to default to [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips)



## June 3, 2019

### Corrections

Change

Basic authentication and client certificate issuance are disabled by default for clusters created with GKE 1.12 and higher. We recommend switching your clusters to use OpenID instead. However, you can still enable basic authentication and client certificate issuance manually. 

To learn more about cluster security, see [Hardening your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster). 

This information was inadvertently omitted from the February 27, 2019 release note. However, the documentation about cluster routing was updated. 

Change

The rollout dates for the May 28, 2019 releases are incorrect. Day 2 spanned May 29-30, day 3 is May 31, and day 4 is June 3. 

## May 28, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Important changes to clusters running unsupported versions

In addition to GKE's [version policy](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades), Kubernetes has a [version skew policy](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only the three newest minor versions. Older versions are not guaranteed to receive bug fixes or security updates, and the control plane may become incompatible with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes running v1.10.x. Clusters in such a configuration could become unreachable or fail to run your workloads correctly.

To keep your clusters operational and to protect Google's infrastructure, we strongly recommend that you upgrade existing nodes to v1.11.x or higher before the end of June 2019. At that time, Google will enable node auto-upgrade on node pools older than v1.11.x, and these nodes will be updated to v1.11.x so that the control plane can be upgraded to v1.13.x and remain compatible with existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

#### Scheduled automatic upgrades

No new automatic upgrades this week; previously-announced automatic upgrades may still be ongoing.

Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.11.x

v1.11.10-gke.4 includes the following changes:

Fixed

The node image for Container-Optimized OS (COS) is now [cos-69-10895-242-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69).

The node image for Ubuntu is now [ubuntu-gke-1804-d1703-0-v20190517](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1703-0-v20190517.manifest).

Node images have been updated to fix Microarchitectural Data Sampling (MDS) vulnerabilities announced by Intel. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

The patch alone is not sufficient to mitigate exposure to this vulnerability. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

### v1.12.x

v1.12.8-gke.6 includes the following changes:

Fixed

The node image for Container-Optimized OS (COS) is now [cos-69-10895-242-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69).

The node image for Ubuntu is now [ubuntu-gke-1804-d1703-0-v20190517](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1703-0-v20190517.manifest).

Node images have been updated to fix Microarchitectural Data Sampling (MDS) vulnerabilities announced by Intel. 

The patch alone is not sufficient to mitigate exposure to this vulnerability. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

### v1.13.x

v1.13.6-gke.5 includes the following changes:

Fixed

The node image for Container-Optimized OS (COS) is now [cos-u-73-11647-182-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73).

The node image for Ubuntu is now [ubuntu-gke-1804-d1809-0-v20190517](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190517.manifest).

Node images have been updated to fix Microarchitectural Data Sampling (MDS) vulnerabilities announced by Intel. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

The patch alone is not sufficient to mitigate exposure to this vulnerability. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

### Rapid channel

v1.14.2-gke.2 is the default for new Rapid channel clusters, and includes the following changes:

Feature

GKE Sandbox is supported on v1.14.x clusters running v1.14.2-gke.2 or higher. 

Fixed

The node image for Container-Optimized OS (COS) is now [cos-u-73-11647-182-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73).

The node image for Ubuntu is now [ubuntu-gke-1804-d1809-0-v20190517](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190517.manifest).

  * Node images have been updated to fix Microarchitectural Data Sampling (MDS) vulnerabilities announced by Intel. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

The patch alone is not sufficient to mitigate exposure to this vulnerability. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

  * Nodes using these images are now [shielded VMs](https://docs.cloud.google.com/shielded-vm) with the following properties: 

    * [UEFI](https://uefi.org/sites/default/files/resources/UEFI_Secure_Boot_in_Modern_Computer_Security_Solutions_2013.pdf) boot is enabled.
    * [SecureBoot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) is disabled.
    * [vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) is enabled.
    * [Integrity Monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) is enabled.



Change

The following IP ranges have been added to default non-IP-masq `iptables` rules: 

  * `100.64.0.0/10`
  * `192.0.0.0/24`
  * `192.0.2.0/24`
  * `192.88.99.0/24`
  * `198.18.0.0/15`
  * `198.51.100.0/24`
  * `203.0.113.0/24`
  * `240.0.0.0/4`



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Cloud Run will be upgraded
  * Istio will be upgraded for v1.13.x clusters
  * Early access to test Windows Containers, expected in early June
  * New clusters will begin to default to [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips)



## May 20, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Important changes to clusters running unsupported versions

In addition to GKE's [version policy](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades), Kubernetes has a [version skew policy](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only the three newest minor versions. Older versions are not guaranteed to receive bug fixes or security updates, and the control plane may become incompatible with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes running v1.10.x. Clusters in such a configuration could become unreachable or fail to run your workloads correctly.

To keep your clusters operational and to protect Google's infrastructure, we strongly recommend that you upgrade existing nodes to v1.11.x or higher before the end of June 2019. At that time, Google will enable node auto-upgrade on node pools older than v1.11.x, and these nodes will be updated to v1.11.x so that the control plane can be upgraded to v1.13.x and remain compatible with existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
1.10.x (nodes only, completing) | 1.11.8-gke.6  
1.12.6-gke.10 | 1.12.6-gke.11  
1.14.1-gke.4 and older 1.14.x (Alpha) | 1.14.1-gke.5 (Alpha)  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.11.x

No v1.11.x versions this week.

### v1.12.x

No v1.12.x versions this week.

Change

**Correction:** Istio was not upgraded to 1.1.3 in v1.12.7-gke.17. The [release note for May 13, 2019](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#may_13_2019) has been corrected. 

### v1.13.x

v1.13.6-gke.0 is available.

Feature

This version includes support for [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods). 

Change

Update Istio to v1.1.3.

Change

Node images have been updated as follows:

  * The Node image for Container-Optimized OS nodes is now [cos-u-73-11647-182-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73).
  * The Node image for Ubuntu nodes is now [ubuntu-gke-1804-d1809-0-v20190506](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190506.manifest).



Nodes using these images are now [shielded VMs](https://docs.cloud.google.com/shielded-vm) with the following properties: 

  * [UEFI](https://uefi.org/sites/default/files/resources/UEFI_Secure_Boot_in_Modern_Computer_Security_Solutions_2013.pdf) boot is enabled.
  * [SecureBoot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) is disabled.
  * [vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) is enabled.
  * [Integrity Monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) is enabled.



### Rapid channel

No v1.14.x versions this week.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.12.6-gke.10



### New features

Feature

[Google Cloud Observability Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine) is now generally available for clusters using the following GKE versions: 

  * 1.12.x clusters v1.12.7-gke.17 and newer
  * 1.13.x clusters v1.13.5-gke.10 and newer
  * 1.14.x (Alpha) clusters v1.14.1-gke.5 and newer



Users of the legacy Google Cloud Observability support are encouraged to [migrate to Google Cloud Observability Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration) before support for legacy Google Cloud Observability is removed. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) support for v1.14.x (Alpha) clusters
  * v1.14.x nodes will be [shielded VMs](https://docs.cloud.google.com/shielded-vm)
  * Early access to test Windows Containers, expected in early June



## May 13, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Important changes to clusters running unsupported versions

In addition to GKE's [version policy](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades), Kubernetes has a [version skew policy](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only the three newest minor versions. Older versions are not guaranteed to receive bug fixes or security updates, and the control plane may become incompatible with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes running v1.10.x. Clusters in such a configuration could become unreachable or fail to run your workloads correctly.

To keep your clusters operational and to protect Google's infrastructure, we strongly recommend that you upgrade existing nodes to v1.11.x or higher before the end of June 2019. At that time, Google will enable node auto-upgrade on node pools older than v1.11.x, and these nodes will be updated to v1.11.x so that the control plane can be upgraded to v1.13.x and remain compatible with existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

#### New default version

The default version for new clusters is now 1.12.7-gke.10 (previously 1.11.8-gke.6). If your cluster is using v1.12.6-gke.10, upgrade to this version to avoid a potential issue that causes [auto-repairing nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) to fail.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

**Note:** Node auto-upgrade is no longer paused.Current version | Upgrade version  
---|---  
**All 1.10.x versions** , including v1.10.12-gke.14 (continuing after unpausing node auto-upgrade) | v1.11.8-gke.6  
v1.11.x versions older than v1.11.8-gke.6 | v1.11.8-gke.6  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

### v1.11.x

##### v1.11.9-gke.13

  * Improvements to Vertical Pod Autoscaler
  * Improvements to Cluster Autoscaler
  * Cloud Run for GKE now uses the default Istio sidecar injection behavior
  * Fix an issue that prevented the kubelet from seeing all GPUs available to nodes using the Ubuntu node image.



### v1.12.x

##### v1.12.7-gke.17

  * Upgrade Ingress controller to [1.5.2](https://github.com/kubernetes/ingress-gce/releases/tag/v1.5.2)
  * Improvements to Vertical Pod Autoscaler
  * Improvements to Cluster Autoscaler
  * Fix an issue that prevented the kubelet from seeing all GPUs available to nodes using the Ubuntu node image
  * Fix an issue that sets the dynamic maximum volume count to 16 if your nodes use a custom machine type. The value is now set to 128.



### v1.13.x

##### v1.13.5-gke.10

###### Upgrading to GKE v1.13.x

To prepare to upgrade your clusters, read the [Kubernetes 1.13 release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.13.md#kubernetes-113-release-notes) and the following information. You may need to modify your cluster before upgrading.

Deprecated

`scheduler.alpha.kubernetes.io/critical-pod` is deprecated. To mark Pods as critical, use [Pod priority and preemption](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/). 

Deprecated

`node.status.volumes.attached.devicePath` is deprecated for Container Storage Interface (CSI) volumes and will not be enabled in future releases. 

Deprecated

The built-in `system:csi-external-provisioner` and `system:csi-external-attacher` Roles are no longer automatically created You can create your own Roles and modify your Deployments to use them. 

Deprecated

Support for CSI drivers using 0.3 and older versions of the CSI API is deprecated. Users should upgrade CSI drivers to use the 1.0 API during the deprecation period. 

Issue

Kubernetes cannot distinguish between manually-provisioned zonal and regional persistent disks with the same name. Ensure that persistent disks have unique names across the Google Cloud project. This issue does not occur when using dynamically provisioned persistent disks. 

Issue

If kubelet fails to register a CSI driver, it does not make a second attempt. To work around this issue, restart the CSI driver Pod. 

Issue

After resizing a PersistentVolumeClaim (PVC), the PVC is sometimes left with a spurious `RESIZING` condition when expansion has already completed. The condition is spurious as long as the PVC's reported size is correct. If the value of `pvc.spec.capacity['storage']` matches `pvc.status.capacity['storage']`, the condition is spurious and you can delete or ignore it. 

Issue

The CSI `driver-registrar external` sidecar container v1.0.0 has a known issue where it takes up to a minute to restart. 

Change

DaemonSets now use scheduling features that require kubelet version 1.11 or higher. Google will update kubelet to 1.11 before upgrading clusters to v1.13.x. 

Change

kubelet can no longer delete their Node API objects. 

Change

Use of the `--node-labels` flag to set labels under the `kubernetes.io/` and `k8s.io/` prefix will be subject to restriction by the NodeRestriction admission plugin in future releases. See the [admission plugin documentation](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction) for the list of allowed labels. 

### Rapid channel

##### 1.14.1-gke.5

**Note:** This content is also available separately in the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

GKE v1.14.1-gke.5 (alpha) is now available for testing and validation in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For more details, refer to the [release notes for Kubernetes v1.14](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md).

Change

GKE v1.14.x has the following differences from Kubernetes 1.14.x. 

  * GKE v1.14.x uses `kube-dns` rather than `core-dns`.
  * GKE v1.14.x does not support [Dramatically Simplify Kubernetes Cluster Creation](https://github.com/kubernetes/enhancements/issues/11), a sub-feature of `kubeadm`.
  * GKE v1.14.x does not support [taint-based eviction](https://github.com/kubernetes/kubernetes/issues/69533).



Issue

You cannot yet create an alpha cluster running GKE v1.14.x. If you attempt to use the `--enable-kubernetes-alpha` flag, cluster creation fails. 

### Security bulletin

Issue

If you run untrusted code in your own multi-tenant services within Google Kubernetes Engine, we recommend that you disable Hyper-Threading to mitigate Microarchitectural Data Sampling (MDS) vulnerabilities announced by Intel. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#may-14-2019). 

### New features

Feature

With GKE 1.13.5-gke.10, GKE 1.13 is now generally available for use in production. You can upgrade clusters running older v1.13.x versions manually. 

GKE v1.13.x has the following differences from Kubernetes 1.13: 

  * GKE v1.13.x uses `kube-dns` rather than `core-dns`.
  * GKE v1.13.x does not support [Dramatically Simplify Kubernetes Cluster Creation](https://github.com/kubernetes/enhancements/issues/11), a sub-feature of `kubeadm`.
  * GKE v1.13.x does not support [taint-based eviction](https://github.com/kubernetes/kubernetes/issues/69533). 

For information about upgrading from v1.12.x, see **Upgrading to GKE v1.13.x** in New versions available for upgrades and new clusters. 

Feature

We are introducing [Release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), a new way to keep your GKE clusters up to date. The Rapid release channel is available, and includes v1.14.1-gke.5 (alpha). You can [sign up](https://forms.gle/93EGYaLx6kn9rPEh9) to try release channels and preview GKE v1.14.x. 

Feature

[GKE Sandbox (Beta)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) is now available for clusters running v1.12.7-gke.17 and higher and v1.13.5-gke.15 and higher. You can use GKE Sandbox to isolate untrusted workloads in a sandbox to protect your nodes, other workloads, and cluster metadata from defective or malicious code. 

### Changes

Change

For clusters running v1.12.x or higher and using nodes with less than 1 GB of memory, GKE reserves 255 MiB of memory. This is not a new change, but it was not previously noted. For more details about node resources, see [Allocatable memory and CPU resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#memory_cpu). 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) will be supported on v1.13.x clusters



## April 29, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled automatic upgrades

**Masters only** with auto-upgrade enabled will be upgraded as follows:

Current version | Upgrade version  
---|---  
**All 1.10.x versions** , including v1.10.12-gke.14 (continuing) | 1.11.8-gke.6  
1.13.4-gke.x | 1.13.5-gke.10  
**Note:** Node auto-upgrade is currently disabled. You can continue to upgrade node pools manually. Node auto-upgrade will be re-enabled in the coming weeks.

Rollouts are phased across multiple weeks, to ensure cluster and fleet stability.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

  * 1.12.6-gke.11 
    * Nodes continue to use Docker as the default runtime.
    * Fix a performance regression introduced in 1.12.6-gke.10. This regression caused delays when the kubelet reads the `/sys/fs/cgroup/memory/memory.stat` file to determine a node's memory usage.



The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.11.9-gke.5
  * 1.12.7-gke.7
  * 1.13.4-gke.10
  * 1.13.5-gke.7



### Fixed issues

Fixed

A problem was fixed in the Stackdriver Kubernetes Monitoring (Beta) Metadata agent. This problem caused the agent to generate unnecessary log messages. 

### Changes

Change

[Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) running Kubernetes 1.13 and higher created with the Google Cloud CLI version 242.0.0 and higher have auto-upgrade and auto-repair disabled. Previously, you were required to disable these feature manually. 

### Known issues

Issue

Under certain circumstances, Google-managed SSL certificates (Beta) are not being provisioned in regional clusters. If this happens, you are unable to create or update managed certificates. If you are experiencing this issue, [contact Google Cloud support](https://docs.cloud.google.com/support). 

Issue

Node auto-upgrade is currently disabled. You can still upgrade node pools manually. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Node auto-upgrade will be re-enabled
  * etcd will be upgraded
  * Improvements to Vertical Pod Autoscaler
  * Improvements to Cluster Autoscaler
  * Improvements to Managed Certificates



## April 26, 2019

Due to delays during the [April 22 GKE release rollout](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#april_22_2019), the release will not complete by April 26, 2019 as originally planned. Rollout is expected to complete by April 29, 2019 GMT.

## April 25, 2019

### Changes

Change

**Google Cloud Observability Kubernetes Monitoring users:** Google Cloud Observability Kubernetes Monitoring logging label fields change when you upgrade your GKE clusters to GKE v1.12.6 or higher. The following changes were effective the week of March 26, 2019: 

  * Kubernetes Pod labels, currently located in the `metadata.userLabels` field, are moved to the `labels` field in the LogEntry and the label keys have a prefix prefix of `k8s-pod/`. The filter expressions in your [sinks](https://docs.cloud.google.com/logging/docs/export), [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics), [log exclusions](https://docs.cloud.google.com/logging/docs/exclusions), or queries might need to change. 
  * Google Cloud Observability system labels that are in the `metadata.systemLabels` field are no longer available. 



For detailed information about what changed, see the [release guide](https://docs.cloud.google.com/monitoring/kubernetes-engine/release-guide) for Google Cloud Observability Beta Monitoring and Logging, also known as Google Cloud Observability Kubernetes Monitoring (Beta). 

## April 22, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
**All 1.10.x versions** , including v1.10.12-gke.14 | 1.11.8-gke.6  
  
This roll-out will be phased across multiple weeks.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

  * 1.11.9-gke.8

    * Node image for Container-Optimized OS updated to [cos-69-10895-211-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69)
      * Fix a performance regression introduced in v1.11.x node images older than 1.11.9-gke.8. This regression caused delays when the kubelet reads the `/sys/fs/cgroup/memory/memory.stat` file to determine a node's memory usage.
    * Upgrade Node Problem Detector to [0.6.3](https://github.com/kubernetes/kubernetes/pull/76284)
  * 1.12.7-gke.10

    * Node image for Container-Optimized OS updated to [cos-69-10895-211-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69)
      * Fix a performance regression introduced in v1.12.x node images older than v1.12.6-gke.10. This regression caused delays when the kubelet reads the `/sys/fs/cgroup/memory/memory.stat` file to determine a node's memory usage.
    * Upgrade Node Problem Detector to [0.6.3](https://github.com/kubernetes/kubernetes/pull/76285)
  * 1.13.5-gke.10 (Preview)

    * To create a cluster, use the following command, replacing `my-alpha-cluster with the name of your cluster:
          
          gcloud container clusters create my-alpha-cluster \
            --cluster-version=1.13.5-gke.10 \
            --enable-kubernetes-alpha \
            --no-enable-autorepair
          

    * Upgrade Node Problem Detector to [0.6.3](https://github.com/kubernetes/kubernetes/pull/76286)




The following versions are no longer available for new clusters or cluster upgrades: 

  * **All 1.10.x versions** , including v1.10.12-gke.14



### Fixed issues

Fixed

A known issue in v1.12.6-gke.10 and older has been fixed in 1.12.7-gke.10. This issue causes node auto-repair to fail. Upgrading is recommended. 

Fixed

A known issue in 1.12.7-gke.7 and older has been fixed in 1.12.7-gke.10. The `currentMetrics` field now reports the correct value. The problem only affected reporting and did not impact the functionality of Horizontal Pod Autoscaler. 

### Deprecations

GKE v1.10.x has been deprecated, and is no longer available for new clusters, master upgrades, or node upgrades. 

The `Cluster.FIELDS.initial_node_count` field has been deprecated in favor of `nodePool.initial_node_count` in the `v1` and `v1beta1` GKE APIs. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * etcd will be upgraded
  * Improvements to Vertical Pod Autoscaler
  * Improvements to Cluster Autoscaler
  * Improvements to Managed Certificates



## April 19, 2019

Change

You can now use [Usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) with GKE 1.12.x and 1.13.x clusters. 

## April 18, 2019

Feature

You can now run GKE clusters in region `asia-northeast2` (Osaka, Japan) with zones `asia-northeast2-a`, `asia-northeast2-b`, and `asia-northeast2-c`.

The new region and zones will be included in future rollout schedules.

## April 15, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version

The default version for new clusters has been updated to 1.11.8-gke.6 (previously 1.11.7-gke.12).

#### Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version | Upgrade version  
---|---  
1.10.x versions 1.10.12-gke.13 and older | 1.10.12-gke.14  
1.11.x versions 1.11.8-gke.5 and older | 1.11.8-gke.6  
1.12.x versions 1.12.6-gke.9 and older | 1.12.6-gke.10  
1.13.x versions 1.13.4-gke.9 and older | 1.13.4-gke.10 (Preview)  
  
#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

  * 1.11.9-gke.5 
    * Node image for Container-Optimized OS updated to [cos-69-10895-201-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image.
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries.
      * Apply security update for [CVE-2019-8912](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Node image for Ubuntu updated to [ubuntu-gke-1804-d1703-0-v20190409](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190409.manifest)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image.
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries.
      * Apply security update for [CVE-2019-8912](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Upgrade [Cloud Run on GKE](https://docs.cloud.google.com/run/docs/gke/release-notes) to 0.5.0
    * Upgrade containerd to [1.1.7](https://github.com/containerd/containerd/releases/tag/v1.1.7)
  * 1.12.7-gke.7 
    * Node image for Container-Optimized OS updated to [cos-69-10895-201-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image.
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries.
      * Apply security update for [CVE-2019-8912](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Node image for Ubuntu updated to [ubuntu-gke-1804-d1703-0-v20190409](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190409.manifest)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image.
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries.
      * Apply security update for [CVE-2019-8912](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Upgrade [Cloud Run on GKE](https://docs.cloud.google.com/run/docs/gke/release-notes) to 0.5.0
    * Upgrade containerd to [1.2.6](https://github.com/containerd/containerd/releases/tag/v1.1.7)
  * 1.13.5-gke.7 (Preview)

    * To create a cluster, use the following command, replacing `my-alpha-cluster with the name of your cluster:
          
          gcloud container clusters create my-alpha-cluster \
            --cluster-version=1.13.5-gke.7 \
            --enable-kubernetes-alpha \
            --no-enable-autorepair
          

    * Node image for Container-Optimized OS updated to [cos-u-73-11647-121-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73)

      * Upgrade Docker from 17.03 to 18.09
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries.
      * Apply security update for [CVE-2019-8912](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Node image for Ubuntu updated to [ubuntu-gke-1804-d1809-0-v20190402a](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190402a.manifest)

      * Upgrade Docker from 17.03 to 18.09
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries.
      * Apply security update for [CVE-2019-8912](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Upgrade [Cloud Run on GKE](https://docs.cloud.google.com/run/docs/gke/release-notes) to 0.5.0

    * Upgrade containerd to [1.2.6](https://github.com/containerd/containerd/releases/tag/v1.1.7)

    * Improvements to volume operation metrics

    * Cluster Autoscaler is now supported for GKE 1.13 clusters

    * Fix a problem that caused the `currentMetrics` field for Horizontal Pod Autoscaler with 'AverageValue' target to always report `unknown`. The problem only affected reporting and did not impact the functionality of Horizontal Pod Autoscaler.




The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.10.12-gke.7
  * 1.10.12-gke.9
  * 1.11.6-gke.11
  * 1.11.6-gke.16
  * 1.11.7-gke.12
  * 1.11.7-gke.18
  * 1.11.8-gke.2
  * 1.11.8-gke.4
  * 1.11.8-gke.5
  * 1.12.5-gke.5
  * 1.12.6-gke.7
  * 1.13.4-gke.1
  * 1.13.4-gke.5



### Changes

Change

Improvements have been made to the automated rules for the [add-on resizer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/small-cluster-tuning). It now uses 5 nodes as the inflection point. 

### Known issues

Issue

GKE 1.12.7-gke.7 and older, and 1.13.4-gke.10 and older have a known issue where the `currentMetrics` field for Horizontal Pod Autoscaler with `AverageValue` target always reports `unknown`. The problem only affects reporting and does not impact the functionality of Horizontal Pod Autoscaler. 

This issue has already been fixed in GKE 1.13.5-gke.7. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Version 1.10.x will soon be unvailable for new clusters.
  * The known issue published this week about Horizontal Pod Autoscaler metrics will be fixed in GKE 1.12.x as well.
  * etcd will be upgraded.



## April 2, 2019

Fixed

The following GKE releases contain a security update that addresses [CVE-2019-9900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) and [CVE-2019-9901.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#april-05-2019). 

This release note was expanded with more information after an embargo about the vulnerabilities was lifted. 

  * 1.10.12-gke.14
  * 1.11.6-gke.16
  * 1.11.7-gke.18
  * 1.11.8-gke.6
  * 1.12.6-gke.10
  * 1.13.4-gke.10 (Public preview) 
    * To create a cluster, use the following command, replacing `my-alpha-cluster` with the name of your cluster: 
          
          gcloud container clusters create my-alpha-cluster \
            --cluster-version=1.13.4-gke.10 \
            --enable-kubernetes-alpha \
            --no-enable-autorepair
              




### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## March 26, 2019

### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

  * 1.11.8-gke.5 
    * Improvements to Cluster Autoscaler
    * Improvements to gVisor
  * 1.12.6-gke.7 
    * Improvements to Cluster Autoscaler
    * Update Ingress controller to [1.5.1](https://github.com/kubernetes/ingress-gce/releases/tag/v1.5.1)
    * Update containerd to [1.2.5](https://github.com/containerd/containerd/releases/tag/v1.2.5)
  * 1.13.4-gke.5 (public preview)

    * To create a cluster, use the following command, replacing `my-alpha-cluster` with the name of your cluster: 
          
          gcloud container clusters create my-alpha-cluster \
          --cluster-version=1.13.4-gke.5 \
          --enable-kubernetes-alpha \
          --no-enable-autorepair
          

    * Improvements to Vertical Pod Autoscaler
    * Improvements to gVisor
    * Update Ingress controller to [1.5.1](https://github.com/kubernetes/ingress-gce/releases/tag/v1.5.1)

    * Update containerd to [1.2.5](https://github.com/containerd/containerd/releases/tag/v1.2.5)

    * Cluster Autoscaler is not operational in this GKE version.




### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## March 19, 2019

### GKE 1.13 public preview

GKE 1.13.4-gke.1 is available for [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) as a public preview. The preview period helps Google Cloud to improve the quality of the final GA release, and allows you to test the new version earlier.

To create a cluster using this version, use the following command, replacing `my-alpha-cluster` with the name of your cluster. Use the exact cluster version provided in the command. You can add other configuration options, but do not change any of the ones below.
    
    
    gcloud container clusters create my-alpha-cluster \
      --cluster-version=1.13.4-gke.1 \
      --enable-kubernetes-alpha \
      --no-enable-autorepair
    

**Note:** Preview versions of GKE are not listed in the available cluster versions in Google Cloud console. 

Alpha clusters become unavailable after 30 days.

#### Changes

  * The preview uses `kube-dns` rather than `core-dns`.
  * The preview does not support [Dramatically Simplify Kubernetes Cluster Creation](https://github.com/kubernetes/enhancements/issues/11), a sub-feature of `kubeadm`.
  * The preview does not support [taint-based eviction](https://github.com/kubernetes/kubernetes/issues/69533).



### Version updates

GKE cluster versions have been updated. 

Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades and node upgrades for existing clusters. See [these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) for more information on the Kubernetes versioning scheme. 

  * 1.11.8-gke.4 
    * New Ubuntu node image [ubuntu-gke-1804-d1703-0-v20190307b](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1703-0-v20190307b.manifest)
      * Update Nvidia GPU driver to 410
      * Fix [USN-3887-1: snapd vulnerability](https://usn.ubuntu.com/3887-1/)
    * Update Istio to 1.0.6
    * Improvements to Vertical Pod Autoscaler
    * Fix CVE-2019-1002100. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#march-01-2019).
  * 1.13.4-gke.1 (see GKE 1.13 public preview for limitations and more information) 
    * Includes the fix for CVE-2019-1002100. For more information, see the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#march-01-2019).
    * Known issues 
      * GKE 1.13.4-gke.1 clusters may experience a previously-published known issue related to elevated master error rates, if Namespaces exist with names longer than 44 characters. To work around the issue, use shorter Namespace names.
      * Cluster autoscaler is not operational in this GKE version.



The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.11.5-gke.5
  * 1.11.6-gke.2
  * 1.11.6-gke.3
  * 1.11.6-gke.6
  * 1.11.6-gke.8
  * 1.11.7-gke.4
  * 1.11.7-gke.6



Deprecated

GKE 1.12.5-gke.10 is no longer available for new clusters, master upgrades, or node upgrades. 

Last week, we began to make GKE 1.12.5-gke.10 unavailable for new clusters or upgrades, due to increased error rates. That process completes this week. 

If you have already upgraded to 1.12.5-gke.10 and are experiencing elevated error rates, you can [contact support](https://cloud.google.com/support-hub). 

#### Automated master and node upgrades

The following versions will be updated for masters and nodes with auto-upgrade enabled. Automated upgrades are rolled out over multiple weeks to ensure cluster stability.

  * 1.11.6 Masters and nodes with auto-upgrade enabled which are using versions 1.11.6-gke.10 or earlier will begin to be upgraded to 1.11.7-gke.12.
  * 1.11.7 Masters and nodes with auto-upgrade enabled which are using version 1.11.7-gke.11 or earlier will begin to be upgraded to 1.11.7-gke.12.



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Nodes with auto-upgrade enabled and masters running 1.11.x will be upgraded to 1.11.7-gke.12
  * GKE 1.12.x masters will begin using the containerd runtime with an upcoming release.



## March 14, 2019

Deprecated

GKE 1.12.5-gke.10 is no longer available for new clusters or master upgrades. 

We have received reports of master nodes experiencing elevated error rates when upgrading to version 1.12.5-gke.10 in all regions. Therefore, we have begun the process of making it unavailable for new clusters or upgrades. 

If you have already upgraded to 1.12.5-gke.10 and are experiencing elevated error rates, you can [contact support](https://cloud.google.com/support-hub). 

## March 11, 2019

Feature

You can now run GKE clusters in region `europe-west6` (Zürich, Switzerland) with zones `europe-west6-a`, `europe-west6-b`, and `europe-west6-c`.

The new region and zones will be included in future rollout schedules.

## March 5, 2019

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.12-gke.7 - This version is being made available again after being previously removed.
  * 1.10.12-gke.9
  * 1.11.7-gke.12
  * 1.12.5-gke.10



#### Node image updates

Change

##### Container-Optimized OS with containerd image for GKE 1.11 clusters

The Container-Optimized OS with containerd node image has been upgraded from `cos-69-10895-138-0-c115` to `cos-69-10895-138-0-c116` for clusters running **Kubernetes 1.11+**.

See [COS image release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) and the [containerd v1.1.5 to v1.1.6 changelog](https://github.com/containerd/containerd/compare/v1.1.5...v1.1.6) for more information. 

##### Container-Optimized OS with containerd image for GKE 1.12 clusters

The Container-Optimized OS with containerd node image has been upgraded from `cos-69-10895-138-0-c123` to `cos-69-10895-138-0-c124` for clusters running **Kubernetes 1.12.5-gke.10+** and alpha clusters running **Kubernetes 1.13+**.

`cos-69-10895-138-0-c124` upgrades Docker to v18.09.0.

See [COS image release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) and the [containerd v1.2.3 to v1.2.4 changelog](https://github.com/containerd/containerd/compare/v1.2.3...v1.2.4) for more information. 

### Other Updates

  * GKE Ingress has been upgraded from v1.4.3 to v1.5.0 for clusters running 1.12.5-gke.10+. For details, see the detailed [changelog](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and [release notes](https://github.com/kubernetes/ingress-gce/releases).



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Nodes with auto-upgrade enabled and masters running 1.11.x will be upgraded to 1.11.7-gke.12



## February 27, 2019

GKE 1.12.5-gke.5 is generally available and includes Kubernetes 1.12. Kubernetes 1.12 provides faster auto-scaling, faster affinity scheduling, topology-aware dynamic provisioning of storage, and advanced audit logging. For more information, see [Digging into Kubernetes 1.12](https://cloud.google.com/blog/products/containers-kubernetes/digging-into-kubernetes-1-12) on the Google Cloud blog. 

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.12.5-gke.5



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Known issues

Issue

A known issue in GKE 1.12.5-gke.5 and all 1.11.x versions below 1.11.6 can cause significant delays when the cluster autoscaler adds new nodes to the cluster, if the cluster has hundreds of unschedulable Pods due to resource starvation. It may require a few minutes before all Pods are scheduled, depending on the number of unschedulable Pods and the size of the cluster. The workaround is to add an adequate number of nodes manually. If adding nodes does not resolve the issue, [contact support](https://cloud.google.com/support-hub). 

Issue

A known issue in GKE 1.12.5-gke.5 can cause unbounded memory usage. This is caused by a memory leak in ReflectorMetricsProvider. See [this issue](https://github.com/kubernetes/kubernetes/issues/73587) for further details. This will be fixed in an upcoming patch. 

Issue

A known issue in GKE 1.12.5-gke.5 slows down or stops Pod scheduling in clusters with large numbers of terminated Pods. See [this issue](https://github.com/kubernetes/kubernetes/issues/74412) for further details. This will be fixed in an upcoming patch. 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Nodes with auto-upgrade enabled and masters running 1.10 will begin to be upgraded to 1.11



## February 18, 2019

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version for new clusters

Kubernetes version 1.11.7-gke.4 is the default version for new clusters, available according to this week's rollout schedule.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.11.7-gke.6



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.10.x



#### Node image updates

Change

The Container-Optimized OS node image has been upgraded from `cos-69-10895-123-0` to `cos-69-10895-138-0`. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

GKE Ingress has been upgraded from v1.4.2 to v1.4.3 for clusters running 1.11.7-gke.6+. For details, see the [detailed changelog](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and [release notes](https://github.com/kubernetes/ingress-gce/releases/tag/v1.4.3). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * GKE 1.12 will be made generally available.
  * Nodes with auto-upgrade enabled and masters running 1.10 will begin to be upgraded to 1.11.7-gke.4.



## February 11, 2019

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions will be available for new clusters and for opt-in master upgrades of existing clusters this week according to the rollout schedule:

  * 1.11.6-gke.11
  * 1.11.7-gke.4
  * 1.10.12-gke.7



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.11.6-gke.0



#### Node image updates

Change

The Ubuntu node image has been upgraded to [ `ubuntu-gke-1604-d1703-0-v20190124`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1604-d1703-0-v20190124.manifest) for clusters running **1.10.12-gke.7**. 

The Ubuntu node image has been upgraded to [ `ubuntu-gke-1804-d1703-0-v20190124`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1703-0-v20190124.manifest) for clusters running **1.11.6-gke.11** , **1.11.7-gke.4** and **1.12.5-gke.5 (EAP)**. 

**Changes:**

  * This image contains security patch for [USN-3863-1: APT vulnerability](https://usn.ubuntu.com/3863-1). 
  * This image contains security patch for [CVE-2019-5736.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736)



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

  * [Node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) and [node auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) are supported on Ubuntu nodes with GKE version 1.11.4-gke.8 and above.
  * [Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) is now available in regional clusters with GKE 1.11.7 and above.



## January 28, 2019

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [ these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) to get a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

For information about changes expected in the coming weeks, see Coming soon.

#### New default version for new clusters

GKE version 1.11.6-gke.2 is the default version for new clusters, available according to this week's rollout schedule.

#### New versions available for upgrades and new clusters

The following Kubernetes Engine versions are available, according to this week's rollout schedule, for new clusters and for opt-in master upgrades for existing clusters:

  * 1.11.6-gke.6



#### GKE Ingress controller update

Change

GKE Ingress has been upgraded from v1.4.1 to v1.4.2 for clusters running 1.11.6-gke.6+. For details, see the [change log](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and the [release notes](https://github.com/kubernetes/ingress-gce/releases/tag/v1.4.2). 

### Fixed Issues

Fixed

A bug in version 1.10.x and 1.11.x may lead to periodic persistent disk commit latency spikes exceeding one second. This may trigger master re-elections of GKE components and cause short (a few seconds) periods of unavailability in the cluster control plane. The issue is fixed in version 1.11.6-gke.6. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * 25% of the upgrades from 1.10 to 1.11.6-gke.2 will be complete.
  * Version 1.11.6-gke.8 will be made available.
  * Version 1.10 will be made unavailable.



## January 21, 2019

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [ these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) to get a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

For information about changes expected in the coming weeks, see Coming soon.

#### New default version for new clusters

Kubernetes version 1.10.11-gke.1 is the default version for new clusters, available according to this week's rollout schedule.

#### New versions available for upgrades and new clusters

The following Kubernetes Engine versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.12-gke.1
  * 1.11.6-gke.3



The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.10.6-gke.13
  * 1.10.7-gke.11
  * 1.10.7-gke.13
  * 1.10.9-gke.5
  * 1.10.9-gke.7
  * 1.11.2-gke.26
  * 1.11.3-gke.24
  * 1.11.4-gke.13



#### Scheduled master auto-upgrades

  * Cluster masters running 1.10.x will be upgraded to 1.10.11-gke.1.
  * Cluster masters running 1.11.2 through 1.11.4 will be upgraded to 1.11.5-gke.5.



#### Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.10.x nodes with auto-upgrade enabled will be upgraded to 1.10.11-gke.1.
  * 1.11.2 through 1.11.4 nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.5.



### Changes

Change

GKE will not set `--max-nodes-total`, because `--max-nodes-total` is inaccurate when the cluster uses [Flexible Pod CIDR ranges](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr). This will be gated in 1.11.7+.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * GKE 1.11.6-gke.6 will be available.
  * A new COS image will be available.



## January 14, 2019

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [ these instructions](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#available_versions) to get a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

For information about changes expected in the coming weeks, see Coming soon.

#### New versions available for upgrades and new clusters

The following Kubernetes Engine versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.12-gke.0
  * 1.11.6-gke.0
  * 1.11.6-gke.2



The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.11.2-gke.25
  * 1.11.3-gke.23
  * 1.11.4-gke.12
  * 1.11.5-gke.4



#### Scheduled master auto-upgrades

  * Cluster masters running 1.9.x will be upgraded to 1.10.9-gke.5.
  * Cluster masters running 1.11.2-gke.25 will be upgraded to 1.11.2-gke.26.
  * Cluster masters running 1.11.3-gke.23 will be upgraded to 1.11.3-gke.24.
  * Cluster masters running 1.11.4-gke.12 will be upgraded to 1.11.4-gke.13.
  * Cluster masters running 1.11.5-gke.4 will be upgraded to 1.11.5-gke.5.



#### Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.9.x nodes with auto-upgrade enabled will be upgraded to 1.10.9-gke.5.
  * 1.11.2-gke.25 nodes with auto-upgrade enabled will be upgraded to 1.11.2-gke.26.
  * 1.11.3-gke.23 nodes with auto-upgrade enabled will be upgraded to 1.11.3-gke.24.
  * 1.11.4-gke.12 nodes with auto-upgrade enabled will be upgraded to 1.11.4-gke.13.
  * 1.11.5-gke.4 nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.5.



#### GKE Ingress controller update

The GKE Ingress controller has been upgraded from v1.4.0 to v1.4.1 for clusters running 1.11.6-gke.2+. For details, see the [change log](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and the [release notes](https://github.com/kubernetes/ingress-gce/releases/tag/v1.4.1).

### Fixed Issues

Fixed

If you use Stackdriver Kubernetes Monitoring Beta with structured JSON logging, an issue with the parsing of structured JSON log entries was introduced in GKE v1.11.4-gke.12. See [release guide for Stackdriver Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/release-guide). This is fixed by upgrading your cluster:

  * 1.11.6-gke.2



Fixed

Users of GKE 1.11.2.x, 1.11.3-gke.18, 1.11.4-gke.8, or 1.11.5-gke.2 on clusters that use Calico network policies may experience failures due to a problem recreating the `BGPConfigurations.crd.projectcalico.org` resource. This is fixed by the automatic upgrades to masters and nodes that have auto-upgrade enabled. 

Fixed

A problem in Endpoints API object validation could prevent updates during an upgrade, leading to stale network information for Services. Symptoms of the problem include failed healthchecks with a `502` status code or a message such as `Forbidden: Cannot change NodeName`. This is fixed by the automatic upgrades to masters and nodes that have auto-upgrade enabled. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * All GKE 1.10.x masters will be upgraded to the latest 1.10 version.
  * All GKE 1.11.0 through 1.11.4 masters will be upgraded to the latest 1.11.5 version.



## January 8, 2019

The rollout beginning January 8, 2019 has been paused after two days. This is being done as a caution, so that we can investigate an issue that will be fixed in next week's rollout. This is not a bug in any GKE version currently available or planned to be made available.

## December 17, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

For information about changes expected in the coming weeks, see Coming soon.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.11.2-gke.26
  * 1.11.3-gke.24
  * 1.11.4-gke.13
  * 1.11.5-gke.5



The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.11.2-gke.18
  * 1.11.2-gke.20
  * 1.11.3-gke.18
  * 1.11.4-gke.8



#### Scheduled master auto-upgrades

Remaining cluster masters running GKE 1.9.x will be upgraded to GKE 1.10.9-gke.5 in January 2019.

#### Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.11.2-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.2-gke.25
  * 1.11.3-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.3-gke.23
  * 1.11.4-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.4-gke.12
  * 1.11.5-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.4



### Fixed Issues

Fixed

Users upgrading to GKE 1.11.2.x, 1.11.3-gke.18, 1.11.4-gke.8, or 1.11.5-gke.2 on clusters that use Calico network policies may experience failures due to a problem recreating the `BGPConfigurations.crd.projectcalico.org` resource. This problem does not affect newly-created clusters. This is fixed by upgrading your to one of the following versions: 

  * 1.11.2-gke.25
  * 1.11.3-gke.23
  * 1.11.4-gke.12
  * 1.11.5-gke.4



Fixed

A problem in Endpoints API object validation could prevent updates during an upgrade, leading to stale network information for Services. Symptoms of the problem include failed healthchecks with a `502` status code or a message such as `Forbidden: Cannot change NodeName`. If you encounter this problem, upgrade your cluster to one of the following versions: 

  * 1.11.2-gke.26
  * 1.11.3-gke.24
  * 1.11.4-gke.13
  * 1.11.5-gke.5



This problem can also affect earlier versions of GKE, but the fix is not yet available for those versions. If you are running an earlier version and encounter this issue, [contact support](https://cloud.google.com/support-hub). 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * Remaining GKE 1.9.x masters are expected to be upgraded in January 2019.



## December 10, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

For information about changes expected in the coming weeks, see Coming soon.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.11-gke.1
  * 1.11.2-gke.25
  * 1.11.3-gke.23
  * 1.11.4-gke.12
  * 1.11.5-gke.4



The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.9.x
  * 1.10.6-gke.11



#### Scheduled master auto-upgrades

We will begin upgrading cluster masters running GKE 1.9.x to GKE 1.10.9-gke.5. The upgrade will be completed in January 2019.

#### Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.11.2-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.2-gke.25
  * 1.11.3-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.3-gke.23
  * 1.11.4-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.4-gke.12
  * 1.11.5-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.4



#### Node image updates

Change

Container-Optimized OS node image has been upgraded to `cos-stable-69-10895-91-0` for clusters running **Kubernetes 1.11.2** , **Kubernetes 1.11.3** , **Kubernetes 1.11.4** , and **Kubernetes 1.11.5**..

**Changes:**

  * containerd has been upgraded from 1.1.2 to 1.1.5. Refer to the COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) and the [containerd changelog](https://www.google.com/url?q=https://github.com/containerd/containerd/compare/v1.1.2...v1.1.5&sa=D&ust=1544664090277000&usg=AFQjCNH11OOTWA13hVz45R8LUwfE_ohH1g) for details.



### Fixed Issues

Fixed

Users upgrading to GKE 1.11.3 on clusters that use Calico network policies may experience failures due to a problem recreating the `BGPConfigurations.crd.projectcalico.org` resource. This problem does not affect newly-created clusters. This is fixed by upgrading your GKE 1.11.3 clusters to 1.11.3-gke.23. 

Fixed

Users modifying or upgrading existing GKE 1.11.x clusters that use Alias IP may experience network failures due to a mismatch between the new IP range assigned the Pods and the alias IP address range for the nodes. This is fixed by upgrading your GKE 1.11.x clusters to one of the following versions:

  * 1.11.2-gke.25
  * 1.11.3-gke.23
  * 1.11.4-gke.12
  * 1.11.5-gke.4



### Changes

Change

Node Problem Detector (NPD) has been upgraded from 0.5.0 to 0.6.0 for clusters running GKE 1.10.11-gke.1+ and 1.11.5-gke.1+. For details, see the [upstream pull request](https://github.com/kubernetes/kubernetes/pull/71522). 

### Known Issues

Issue

In GKE v1.11.4-gke.12 and later, if you use Stackdriver Kubernetes Monitoring Beta with structured JSON logging, there is an issue with the parsing of structured JSON log entries. As a workaround, you can downgrade to GKE 1.11.3. For more information, see the [release guide for Stackdriver Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/release-guide#beta_release_1102). 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * All GKE 1.9.x masters will be upgraded to 1.10.9-gke.5.



## December 4, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

For information about changes expected in the coming weeks, see Coming soon.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.11.4-gke.8



#### Node image updates

Change

Ubuntu node image has been upgraded to [ `ubuntu-gke-1804-d1703-0-v20181113.manifest`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1703-0-v20181113.manifest) for clusters running **Kubernetes 1.11.4-gke.8**. 

**Changes:**

  * The following warning is now displayed to SSH clients that connect to Nodes using SSH or to run remote commands on Nodes over an SSH connection: 
        
        WARNING: Any changes on the boot disk of the node must be made via
        DaemonSet in order to preserve them across node (re)creations.
        Node will be (re)created during manual-upgrade, auto-upgrade,
        auto-repair or auto-scaling.




### New features

Feature

  * [GKE Usage metering (beta)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) is now available.



### Changes

Change

  * You can now drain node pools and delete Nodes in parallel.
  * GKE data in Cloud Asset Inventory and Search is now available in near-real-time. Previously, data was dumped at 6-hour intervals.



### Fixed Issues

Fixed

When upgrading to GKE 1.11.x versions prior to GKE 1.11.4-gke.8, a problem with provisioning the ExternalIP on one or more Nodes causes the `kubectl` command to fail. The following error is logged in the `kube-apiserver` log:
    
    
    Failed to getAddresses: no preferred addresses found; known addresses

This issue is fixed in GKE 1.11.4-gke.8. If you can't upgrade to that version, you can work around this issue by following these steps: 

  1. Determine which Nodes have no ExternalIP set:
         
         kubectl get nodes -o wide

Look for entries where the last column is `<none>`.

  2. Restart affected nodes.



### Known Issues

Issue

Users upgrading to GKE 1.11.3 on clusters that use Calico network policies may experience failures due to a problem recreating the `BGPConfigurations.crd.projectcalico.org` resource. This problem does not affect newly-created clusters. This is expected to be fixed in the coming weeks. 

To work around this problem, you can create the `BGPConfigurations.crd.projectcalico.org` resource manually: 

  1. Copy the following script into a file named `bgp.yaml`: 
         
         apiVersion: apiextensions.k8s.io/v1beta1
         kind: CustomResourceDefinition
         metadata:
           name: bgpconfigurations.crd.projectcalico.org
           labels:
             kubernetes.io/cluster-service: "true"
             addonmanager.kubernetes.io/mode: Reconcile
         spec:
           scope: Cluster
           group: crd.projectcalico.org
           version: v1
           names:
             kind: BGPConfiguration
             plural: bgpconfigurations
             singular: bgpconfiguration
             

  2. Apply the change to the affected cluster using the following command: 
         
         kubectl apply -f bgp.yaml




Issue

Users modifying or upgrading existing GKE 1.11.x clusters that use Alias IP may experience network failures due to a mismatch between the new IP range assigned the Pods and the alias IP address range for the nodes. This is expected to be fixed in the coming weeks. 

To work around this problem, follow these steps. Use the name of your node in place of [NODE_NAME], and use your cluster's zone in place of [ZONE]. 

  1. Cordon node that has been affected: 
         
         kubectl cordon [NODE_NAME]

  2. Drain node of all workloads: 
         
         kubectl drain [NODE_NAME]

  3. Delete the Node object from Kubernetes 
         
         kubectl delete nodes [NODE_NAME]

  4. Reboot the Node. This is not optional.
         
         gcloud compute instances reset --zone [ZONE] [NODE_NAME]




### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Coming soon

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes. 

  * We expect to begin upgrading cluster masters running GKE 1.9.x to 1.10.9-gke.5.
  * An updated Container-Optimized OS node image, including [containerd 1.1.5](https://github.com/containerd/containerd/releases/tag/v1.1.5)
  * Support for enabling Node auto-upgrade and auto-repair when creating or modifying node pools for GKE 1.11 clusters running Ubuntu node images



## November 26, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.6-gke.13
  * 1.10.7-gke.13
  * 1.10.9-gke.7
  * 1.11.2-gke.20
  * 1.11.3-gke.18



#### Node image updates

Change

Container-Optimized OS node image has been upgraded to `cos-stable-69-10895-91-0` for clusters running **Kubernetes 1.10.9** and **Kubernetes 1.11.3**.

**Changes:**

  * Bug fix for pod hanging when executing a file in NFS path



See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information. 

Change

Ubuntu node image has been upgraded to [ `ubuntu-gke-1804-bionic-20180921`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-bionic-20180921.manifest) for clusters running **Kubernetes 1.11.3**. 

**Changes:**

  * Add GPU support on Ubuntu



### Known Issues

Issue

When upgrading to GKE 1.11.x versions prior to GKE 1.11.4-gke.8, a problem with provisioning the ExternalIP on one or more Nodes causes some `kubectl` command to fail. The following error is logged in the `kube-apiserver` log: 
    
    
    Failed to getAddresses: no preferred addresses found; known addresses

You can work around this issue by following these steps: 

  1. Determine which Nodes have no ExternalIP set: 
         
         kubectl get nodes -o wide

Look for entries where the last column is `<none>`. 

  2. Restart affected nodes.



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

Vertical Pod Autoscaler (beta) is now available on 1.11.3-gke.11 and higher.

## November 12, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version for new clusters

Kubernetes version 1.9.7-gke.11 is the default version for new clusters, available according to this week's rollout schedule.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.9.7-gke.11
  * 1.10.6-gke.11
  * 1.10.7-gke.11
  * 1.10.9-gke.5
  * 1.11.2-gke.18



#### Scheduled master auto-upgrades

Cluster masters will be auto-upgraded as described below:

  * All clusters running 1.9.7 will be upgraded to 1.9.7-gke.11
  * All clusters running 1.10.6 will be upgraded to 1.10.6-gke.11
  * All clusters running 1.10.7 will be upgraded to 1.10.7-gke.11
  * All clusters running 1.10.9 will be upgraded to 1.10.9-gke.5
  * All clusters running 1.11.2 will be upgraded to 1.11.2-gke.18



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.9.7-gke.7
  * 1.10.6-gke.9
  * 1.10.7-gke.9
  * 1.10.9-gke.3
  * 1.11.2-gke.15



### Known Issues

Issue

When upgrading to GKE 1.11.x versions prior to GKE 1.11.4-gke.8, a problem with provisioning the ExternalIP on one or more Nodes causes some `kubectl` command to fail. The following error is logged in the `kube-apiserver` log: 
    
    
    Failed to getAddresses: no preferred addresses found; known addresses

You can work around this issue by following these steps: 

  1. Determine which Nodes have no ExternalIP set: 
         
         kubectl get nodes -o wide

Look for entries where the last column is 
         
         <none>

. 
  2. Restart affected nodes.



### Other Updates

Change

Patch 2 for Tigera Technical Advisory TTA-2018-001. See the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#november-13-2018) for further details.

Change

Patch for Kubernetes vulnerability [CVE-2018-1002105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1002105). See the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#december-3-2018) for more details. 

## November 5, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New default version for new clusters

Kubernetes version 1.9.7-gke.7 is the default version for new clusters, available according to this week's rollout schedule.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.9.7-gke.7
  * 1.10.6-gke.9
  * 1.10.7-gke.9
  * 1.10.9-gke.3
  * 1.11.2-gke.15



#### Scheduled master auto-upgrades

Cluster masters running will be auto-upgraded as described below:

  * All clusters running 1.9.x will be upgraded to 1.9.7-gke.7
  * All clusters running 1.10.6 will be upgraded to 1.10.6-gke.9
  * All clusters running 1.10.7 will be upgraded to 1.10.7-gke.9
  * All clusters running 1.10.9 will be upgraded to 1.10.9-gke.3
  * All clusters running 1.11.2 will be upgraded to 1.11.2-gke.15



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.9.7-gke.6
  * 1.10.6-gke.6
  * 1.10.7-gke.6
  * 1.10.9-gke.0
  * 1.11.2-gke.9



### Other Updates

Change

Patch 1 for Tigera Technical Advisory TTA-2018-001. See the [security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#november-13-2018) for further details. The November 12th release contains additional fixes that address TTA-2018-001 and we recommend customers upgrade to that release. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## November 1, 2018

### New Features

Feature

[Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) is now available in beta.

## October 30, 2018

### Version updates

GKE cluster versions have been updated as detailed in the following sections. See [supported versions](https://docs.cloud.google.com/kubernetes-engine/supported-versions) for a full list of the Kubernetes versions you can run on your GKE masters and nodes.

#### New versions available for upgrades and new clusters

GKE 1.11.2-gke.9 is now generally available.

  * You can now select Container-Optimized OS with `containerd` images when creating, modifying, or upgrading a cluster to GKE v1.11. Visit [Using Container-Optimized OS with containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd) for details.

  * The CustomResourceDefinition API supports a `versions` list field (and deprecates the previous singular `version` field) that you can use to support multiple versions of custom resources you have developed, to indicate the stability of a given custom resource. All versions must currently use the same schema, so if you need to add a field, you must add it to all versions. Currently, versions only indicate the stability of your custom resource, and do not allow for any difference in functionality among versions. For more information, visit [Versions of CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/).

  * Kubernetes 1.11 introduces beta support for increasing the size of an existing PersistentVolume. To increase the size of a PersistentVolume, edit the PersistentVolumeClaim (PVC) object. Kubernetes expands the file system automatically.

Kubernetes 1.11 also includes alpha support for expanding an online PersistentVolume (one which is in use by a running deployment). To test this feature, use an [alpha cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-alpha-cluster).

Shrinking persistent volumes is not supported. For more details, visit [Resizing a volume containing a file system](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#resizing-a-volume-containing-a-file-system).

  * Subresources allow you to add capabilities to custom resources. You can enable `/status` and `/scale` REST endpoints for a given custom resource. You can access these endpoints to view or modify the behavior of the custom resource, using `PUT`, `POST`, or `PATCH` requests. Visit [Subresources](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#subresources) for details.




Also, 1.10.9-gke.0 is available.

### Scheduled master auto-upgrades

  * Cluster masters running GKE 1.10.6 will be upgraded to 1.10.6-gke.6.
  * Cluster masters running GKE 1.10.7 will be upgraded to 1.10.7-gke.6.



### Fixed Issues

Fixed

GKE 1.10.7-gke.6 and 1.11.2-gke.9 fix an issue that is present in GKE 1.10.6-gke.2 and higher and 1.11.2-gke.4 and higher, where master component logs are missing from Stackdriver Logging. 

### Other Updates

Container-Optimized OS node image has been upgraded to `cos-beta-69-10895-52-0` for clusters running Kubernetes 1.11.2-gke.9, 1.10.9-gke.0, or 1.10.7-gke.6. See [COS image release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

[Cluster templates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster#templates) are now available when creating new GKE clusters in Google Cloud console.

### Changes

Change

The `kubectl` command on new nodes has been upgraded from version 1.9 to 1.10. The `kubectl` version is always one version behind the highest GKE version, to ensure compatibility with all supported versions.

### Known Issues

Issue

In GKE 1.10.6-gke.2 and higher and 1.11.2-gke.4 and higher, master component logs are missing from Stackdriver Logging. This is due to an issue in the version of fluentd used in those versions of GKE.

**Update:** This issue is fixed in GKE 1.10.7-gke.6 and 1.11.2-gke.9, available from October 30, 2018. 

## October 22, 2018

### Fixed

Fixed

**Kubernetes 1.11.0+:** Fixes a bug in kubeDNS where hostnames in SRV records were being incorrectly compressed.

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### Scheduled master auto-upgrades

  * 20% of cluster masters running Kubernetes versions 1.10.6-gke.x will be updated to Kubernetes 1.10.6-gke.6, according to this week's rollout schedule.
  * 20% of cluster masters running Kubernetes versions 1.10.7-gke.x will be updated to Kubernetes 1.10.7-gke.6, according to this week's rollout schedule.



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.10.6-gke.2
  * 1.11.1-gke.1 (EAP)



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

[Authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) is now generally available.

Feature

You can now run GKE clusters in region `asia-east2` (Hong Kong) with zones `asia-east2-a`, `asia-east2-b`, and `asia-east2-c`.

## October 18, 2018

### Changes

Change

[Node autoupgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) are enabled by default for clusters and node pools created with the Google Cloud console.

## October 8, 2018

### Known Issues

Issue

All GKE v1.10.6 releases includes a [problem with Ingress load balancing](https://github.com/kubernetes/ingress-gce/issues/471). The problem was first reported in the release notes for September 18, 2018. 

The problem is fixed in GKE v1.10.7 and higher. However, it cannot be fixed in GKE v1.10.6. **If your cluster uses Ingress, do not upgrade to v1.10.6. Do not use GKE v1.10.6 for new clusters**. If your cluster does not use Ingress for load balancing and you cannot upgrade to GKE v1.10.7 or higher, you can still use GKE v1.10.6. 

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [supported versions](https://docs.cloud.google.com/kubernetes-engine/supported-versions) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes. 

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.6-gke.6
  * 1.10.7-gke.6
  * 1.11.2-gke.9 as EAP



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.10.6-gke.4
  * 1.10.7-gke.2



#### Node image updates

Change

Container-Optimized OS node image `cos-dev-69-10895-23-0` is now available. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information. 

Change

Container-Optimized OS with containerd node image `cos-b-69-10895-52-0-c110` is now available. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## October 2, 2018

### New Features

Feature

[Private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) is now generally available.

## September 21, 2018

### New Features

Feature

[Container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing) is now available in beta.

## September 18, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.6-gke.4
  * 1.10.7-gke.2
  * 1.11.2-gke.4 clusters are now available for whitelisted early-access users. Non-whitelisted users can specify version 1.11.2-gke.4 in [Alpha Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).



#### Scheduled master auto-upgrades

20% of cluster masters running Kubernetes versions 1.9.x will be updated to Kubernetes 1.9.7-gke.6, according to this week's rollout schedule.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.9.6-gke.2
  * 1.9.7-gke.5
  * 1.10.6-gke.3
  * 1.10.7-gke.1
  * 1.11.2-gke.2 (EAP version)
  * 1.11.2-gke.3 (EAP version)



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Fixes

  * 1.10.7-gke.2 fixes [a bug introduced in 1.10.6](https://github.com/kubernetes/ingress-gce/issues/471) that causes the `Ingress-GCE` controller to crash.



## September 5, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * 1.10.6-gke.3
  * 1.10.7-gke.1



#### Scheduled master auto-upgrades

Cluster masters running Kubernetes versions 1.10.x will be updated to Kubernetes 1.10.6-gke.2 according to this week's rollout schedule.

Cluster masters running Kubernetes versions 1.8.x will be updated to Kubernetes 1.9.7-gke.5 according to this week's rollout schedule.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.10.2-gke.4
  * 1.10.4-gke.3
  * 1.10.5-gke.4
  * 1.10.6-gke.1



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Fixes

  * 1.10.7-gke.1 fixes an issue where preempted GPU Pods would restart without proper GPU libraries.



## August 20, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

  * 1.11.2-gke.3 (preview)
  * 1.10.6-gke.2
  * 1.9.7-gke.6



#### Scheduled master auto-upgrades

[Auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) of Kubernetes 1.8.x clusters to 1.9.7-gke.5 continues for the second week. You can always upgrade your Kubernetes 1.8 masters [manually](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).

#### Node image updates

Change

Container-Optimized OS node image has been upgraded from `cos-stable-66-10452-109-0` to `cos-dev-69-10895-23-0` for clusters running Kubernetes 1.10.6-gke.2 and Kubernetes 1.11.2-gke.3. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information. 

Container-Optimized OS node image has been upgraded from `cos-stable-65-10323-98-0-p2` to `cos-stable-65-10323-99-0-p2` for clusters running **Kubernetes 1.9.7-gke.6**. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information. 

These images contain a fix for an [L1 Terminal Fault](https://support.google.com/faqs/answer/9104762) vulnerability. 

Change

Ubuntu node image has been upgraded from `ubuntu-gke-1804-bionic-20180718` to [ `ubuntu-gke-1804-bionic-20180814`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-bionic-amd64-gke-20180814.manifest) for clusters running **Kubernetes 1.11.2-gke.3**. 

Ubuntu node image has been upgraded from `ubuntu-gke-1604-xenial-20180731-1` to [ `ubuntu-gke-1604-xenial-20180814-1`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180814.manifest) for clusters running **Kubernetes 1.10.6-gke.2** and **Kubernetes 1.9.7-gke.6**. 

These images contain a fix for an [L1 Terminal Fault](https://support.google.com/faqs/answer/9104762) vulnerability. 

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

  * [Cloud binary authorization](https://docs.cloud.google.com/binary-authorization/docs) is promoted to Beta for GKE clusters.
  * `GCE-Ingress` has been upgraded to version 1.3.0. HTTP2 support for Ingress is promoted to Beta.
  * Private endpoints are promoted to Beta, for customers using private clusters. At cluster creation time, customers can now choose to use the Kubernetes master's private IP address as their API server endpoint.



### Fixes

  * This week's releases address an [L1 Terminal Fault vulnerability](https://support.google.com/faqs/answer/9104762). Customers running containers from different customers on the same GKE Node, as well as customers using COS images, should prioritize updating those environments.



## August 13, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for opt-in master upgrades for existing clusters:

  * Kubernetes 1.11.2-gke.2 clusters are now available for whitelisted early-access users. Non-whitelisted users can specify version 1.11.0-gke.1 in Alpha Clusters
  * 1.10.6-gke.1



#### Scheduled master auto-upgrades

  * 10 % of cluster masters running Kubernetes versions 1.8.x will be updated to Kubernetes 1.9.7-gke.5, according to this week's rollout schedule.

  * Cluster masters running Kubernetes versions 1.9.x will be updated to Kubernetes 1.9.7-gke.5, according to this week's rollout schedule.

  * Cluster masters running Kubernetes versions 1.10.x will be updated to Kubernetes 1.10.6-gke.1, according to this week's rollout schedule.




#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.8.x



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

  * Containerd integration on the Container-Optimized OS (COS) image is now beta. You can now create a cluster or a node pool with image type `cos_containerd`. Refer to [Container-Optimized OS with containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos-containerd) for details.



### Fixes

  * GKE 1.10.6-gke.1 and higher contains a [critical fix](https://issuetracker.google.com/issues/111881344) for the [Stackdriver Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/release-guide) Beta release. In total, the upgrade fixes the first five [known issues of Stackdriver Kubernetes Monitoring Beta Release 1.10.2](https://docs.cloud.google.com/monitoring/kubernetes-engine/release-guide#beta_release_1102).



## August 6, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [supported versions](https://docs.cloud.google.com/kubernetes-engine/supported-versions) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and opt-in master upgrades for existing clusters:

* **Kubernetes 1.9.7-gke.5** is now **generally available** for use with Kubernetes Engine clusters.

#### New default version for new clusters

* Kubernetes version **1.9.7-gke.5** is the default version for new clusters, available according to this week's rollout schedule.

#### Scheduled master auto-upgrades

Change

Cluster masters running Kubernetes version **1.8.10-gke.0** will be updated to **Kubernetes 1.8.10-gke.2** , according to this week's rollout schedule.

Change

Cluster masters running Kubernetes versions **1.8.12-gke.1** and **1.8.12-gke.2** will be updated to **Kubernetes 1.8.12-gke.3** , according to this week's rollout schedule.

Change

Cluster masters running Kubernetes version **1.9.6-gke.1** will be updated to **Kubernetes 1.9.6-gke.2** , according to this week's rollout schedule.

Change

Cluster masters running Kubernetes versions **1.9.7-gke.0** , **1.9.7-gke.1** , **1.9.7-gke.3** , and **1.9.7-gke.4** will be updated to **Kubernetes 1.9.7-gke.5** , according to this week's rollout schedule.

Change

Cluster masters running Kubernetes versions **1.10.2-gke.0** , **1.10.2-gke.1** , and **1.10.2-gke.3** will be updated to **Kubernetes 1.10.2-gke.4** , according to this week's rollout schedule.

Change

Cluster masters running Kubernetes versions **1.10.4-gke.0** and **1.10.4-gke.2** will be updated to **Kubernetes 1.10.4-gke.3** , according to this week's rollout schedule.

Change

Cluster masters running Kubernetes versions **1.10.5-gke.0** and **1.10.5-gke.3** will be updated to **Kubernetes 1.10.5-gke.4** , according to this week's rollout schedule.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Fixes

Fixed

A patch for Kubernetes vulnerability [CVE-2018-5390](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins-archive#august-6-2018) is now available according to this week's rollout schedule. We recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your nodes as soon as the patch becomes available in your cluster's zone.

## August 3, 2018

### New Features

In a future release, all newly-created Google Kubernetes Engine clusters are [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) by default.

## July 30, 2018

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

  * **Kubernetes 1.10.5-gke.3** is now **generally available** for use with Google Kubernetes Engine clusters.



## July 12, 2018

### New Features

Feature

[Cloud TPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) is now available with GKE in Beta. Run your machine learning workload in a Kubernetes cluster on Google Cloud, and let GKE manage and scale the Cloud TPU resources for you.

### Version updates

GKE cluster versions have been updated. Note: Your clusters might not have these versions available. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and opt-in master upgrades for existing clusters:

  * **Kubernetes 1.8.12-gke.2** is now **generally available** for use with Google Kubernetes Engine clusters.
  * **Kubernetes 1.9.7-gke.4** is now **generally available** for use with Google Kubernetes Engine clusters.
  * **Kubernetes 1.10.5-gke.2** is now **generally available** for use with Google Kubernetes Engine clusters.
  * **Kubernetes 1.11.0-gke.1** clusters are now available for whitelisted early-access users. Non-whitelisted users can specify version 1.11.0-gke.1 in [Alpha Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).



Issue

Enabling/disabling network policy on already created 1.11 clusters may not work properly. 

#### Scheduled master auto-upgrades

Cluster masters running Kubernetes versions 1.8 will be updated to Kubernetes 1.8.10-gke.0 according to this week's rollout schedule.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## July 10, 2018

### New Features

Feature

You can now run GKE clusters in region `us-west2` (Los Angeles) with zones `us-west2-a`, `us-west2-b`, and `us-west2-c`.

## June 28, 2018

### Version Updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.10.5-gke.0** is now **generally available** for use with GKE clusters.

#### New default version for new clusters

Kubernetes version 1.9.7-gke.3 is the default version for new clusters, available according to this week's rollout schedule. 

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and opt- in master upgrades for existing clusters:

  * 1.10.5-gke.0



#### Scheduled master auto-upgrades

Cluster masters running Kubernetes versions older than 1.8.10-gke.0 will be updated to Kubernetes 1.8.10-gke.0 according to this week's rollout schedule.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.8.8-gke.0
  * 1.10.4-gke.0



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Known Issues

Currently, OS Login is not fully compatible with Google Kubernetes Engine clusters running Kubernetes version 1.10.x. The following functionalities of kubectl might not work properly when OS Login is enabled: kubectl logs, proxy, exec, attach, and port-forward. Until OS Login is fully supported, the settings at the project-level are ignored at the nodes level. The settings at project-level are ignored in Kubernetes Engine.

## June 18, 2018

### Version Updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.10.4-gke.2** is now **generally available** for use with GKE clusters.

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and opt- in master upgrades for existing clusters:

  * 1.10.4-gke.2



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.9.7-gke.1
  * 1.10.2-gke.3



### New Features

Feature

[GPUs for Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) is now generally available.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## June 11, 2018

### Version Updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.10.4-gke.0** is now **generally available** for use with GKE clusters.

The base image for this version is `cos-stable-66-10452-101-0`, which contains a fix for an issue that causes deadlock in the Linux kernel.

### New Features

Feature

You can now run GKE clusters in region `europe-north1` (Finland) with zones `europe-north1-a`, `europe-north1-b`, and `europe-north1-c`.

Refer to the rollout schedule below for the specific rollout dates in each zone.

Feature

A new `cos_containerd` image is now available and set by default for trying out the [containerd](https://containerd.io/) integration in the [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) running **Kubernetes 1.10.4-gke.0 and above**. See the [containerd runtime alpha user guide](https://docs.google.com/document/d/1Y9RfPOFqgP_JWfv2XeIG07qE4J5p3nxI_GB9mj9gvGg/edit?usp=sharing) for more information, or learn about the containerd integration in the recent [Kubernetes blog post](https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/).

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## June 04, 2018

#### New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and opt-in master upgrades for existing clusters:

  * 1.9.7-gke.3



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## May 22, 2018

#### New versions available for upgrades and new clusters

Feature

**Kubernetes 1.10.2-gke.3** is now available for use with Kubernetes Engine clusters.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.8.12-gke.0
  * 1.9.7-gke.0
  * 1.10.2-gke.1



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

[Custom Boot Disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-boot-disks) is now available in Beta.

Feature

[Alias IPs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) is now generally available.

## May 16, 2018

### New Features

Feature

[Kubernetes Engine Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc) is now available in Beta.

## May 15, 2018

Change

The rollout of the release has been delayed. Refer to the revised rollout schedule below.

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

Clusters running **Kubernetes 1.9.0 - 1.9.6-gke.0** that have opted into [automatic node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-upgrades) will be upgraded to **Kubernetes 1.9.6-gke.1** according to this week's rollout schedule.

Feature

**Kubernetes 1.10.2-gke.1** is now **generally available** for use with Google Kubernetes Engine clusters.

Feature

**Kubernetes 1.9.7-gke.1** is now **generally available** for use with Google Kubernetes Engine clusters.

Feature

**Kubernetes 1.8.12-gke.1** is now **generally available** for use with Google Kubernetes Engine clusters.

#### New default version for new clusters

The following versions are now default according to this week's rollout schedule:

Change

**Kubernetes 1.8.10-gke.0** is now the default version for new clusters.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

Load balancers and ingresses are now automatically deleted upon cluster deletion.

### Other Updates

Change

The base image has been changed to `cos-stable-66-10452-89-0` for clusters running **Kubernetes 1.10.2-gke.1**.

This image contains a fix for Linux kernel CVE-2018-1000199 and CVEs in ext4 (CVE-2018-1092, CVE-2018-1093, CVE-2018-1094, CVE-2018-1095).

Change

The base image has been changed to `cos-stable-65-10323-85-0` for clusters running **Kubernetes 1.8.12-gke.0** and **Kubernetes 1.9.7-gke.1**.

This image contains a fix for Linux kernel CVE-2018-1000199.

Change

The base image has been changed to [`ubuntu-gke-1604-xenial-20180509-1`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180509-1.9.manifest) for clusters running **Kubernetes 1.9.7-gke.1** and **Kubernetes 1.10.2-gke.1**.

The base image has been changed to [`ubuntu-gke-1604-xenial-20180509`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180509.manifest) for clusters running **Kubernetes 1.8.12-gke.1**.

These images contain a fix for Linux kernel CVE-2018-1000199. Refer to [USN-3641-1](https://usn.ubuntu.com/usn/usn-3641-1) for more information.

## May 7, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### Scheduled master auto-upgrades

Change

100% of cluster masters running Kubernetes versions **1.7.0** and **1.7.12-gke.2** will be updated to **Kubernetes 1.8.8-gke.0** , according to this week's rollout schedule.

Change

100% of cluster masters running Kubernetes versions **1.7.14.gke-1** and **1.7.15-gke.0** will be updated to **Kubernetes 1.8.10-gke.0** , according to this week's rollout schedule.

Change

100% of cluster masters running Kubernetes versions **1.9.X** will be updated to **Kubernetes 1.9.6** , according to this week's rollout schedule.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.7.15-gke.l0
  * 1.9.3-gke.0



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Known Issues

Issue

The Kubernetes Dashboard in version 1.8.8-gke.0 isn't compatible with nodes running versions 1.7.13 through 1.7.15.

## May 1, 2018

### Known Issues

Issue

In **Kubernetes versions 1.9.7, 1.10.0, and 1.10.2** , if an NVIDIA GPU device plugin restarts but the associated kubelet does not, then the node allocatable for the GPU resource `nvidia.com/gpu` stays zero until the kubelet restarts. This prevents new pods from consuming GPU devices.

The most likely scenario when this problem occurs is after a cluster is created or upgraded with Kubernetes 1.9.7, 1.10.0, or 1.10.2 and the cluster master is upgraded to a new version, which triggers an NVIDIA GPU device plugin DaemonSet upgrade. The DaemonSet upgrade causes the NVIDIA GPU device plugin to restart itself.

If you use the GPU feature, do not create or upgrade your cluster with Kubernetes 1.9.7, 1.10.0, or 1.10.2. This issue will be addressed in an upcoming release.

## April 30, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.8.12-gke.0** is now **generally available** for use with Google Kubernetes Engine clusters.

Feature

**Kubernetes 1.9.7-gke.0** is now **generally available** for use with Google Kubernetes Engine clusters.

Feature

**Kubernetes 1.10.2-gke.0** clusters are now available for whitelisted early-access users. Non-whitelisted users can specify version 1.10.2-gke.0 in [Alpha Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

#### Scheduled master auto-upgrades

Change

100% of cluster masters running Kubernetes versions **1.7.x** will be updated to **Kubernetes 1.8.8-gke.0** , according to this week's rollout schedule.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### Other Updates

Change

The base image has been changed to `cos-stable-65-10323-75-0-p` for clusters running **Kubernetes 1.8.12-gke.0**.

Change

The base image has been changed to `cos-stable-65-10323-75-0-p2` for clusters running **Kubernetes 1.9.7-gke.0**.

Change

The base image has been changed to `cos-stable-66-10452-74-0` for clusters running **Kubernetes 1.10.2-gke.0**.

## April 24, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### Scheduled master auto-upgrades

  * 10 % of cluster masters running Kubernetes versions 1.7.x will be updated to Kubernetes 1.8.8-gke.0, according to this week's rollout schedule.
  * Cluster masters running Kubernetes versions 1.8.x will be updated to Kubernetes 1.8.8-gke.0, according to this week's rollout schedule.
  * Cluster masters running Kubernetes versions 1.9.x will be updated to Kubernetes 1.9.3-gke.0, according to this week's rollout schedule.



#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.9.6-gke.0



The following versions are no longer available for new clusters or cluster upgrades: 

  * 1.8.7-gke.1
  * 1.9.2-gke.1
  * 1.9.6-gke.0



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## April 16, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.7.14-gke.1
  * Kubernetes 1.8.9-gke.1
  * Kubernetes 1.9.4-gke.1



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## April 9, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.9.6-gke.1** is now **generally available** for use with Google Kubernetes Engine clusters.

Feature

**Kubernetes 1.10.0-gke.0** clusters are now available for whitelisted early-access users. Non-whitelisted users can specify version 1.10.0-gke.0 in [Alpha Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

#### Scheduled master auto-upgrades

Cluster masters running Kubernetes versions 1.7.x will be updated to Kubernetes 1.7.12-gke.2, according to this week's rollout schedule. 

#### Versions no longer available

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.7.12-gke.1



### Other Updates

Container-Optimized OS node image has been upgraded to `cos-stable-65-10323-69-0-p2` for clusters running **Kubernetes 1.9.6-gke.1**. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information.

Container-Optimized OS node image is using `cos-beta-66-10452-28-0` for clusters running **Kubernetes 1.10.0-gke.0**. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## March 30, 2018

Note: The [March 27, 2018 release](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#march-27-2018) has been rolled back, so this release supersedes the rollout schedule and cluster default version previously stated. 

#### New versions available for upgrades and new clusters

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.9.6-gke.0.** , **Kubernetes 1.8.10-gke.0.** , and **Kubernetes 1.7.15-gke.0.** are now **generally available** for use with Google Kubernetes Engine clusters.

#### New default version for new clusters

The following versions are now default according to this week's rollout schedule:

##### Zonal clusters

Change

The default version has been reverted from the [March 27, 2018 release](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#march-27-2018). **Kubernetes 1.8.8-gke.0** is now the default version for new **zonal** and **regional** clusters.

#### Versions no longer available

Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.9.2-gke.1
  * Kubernetes 1.7.12-gke.2



### Other Updates

The following updates are the same as in the [March 27, 2018 release](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#march-27-2018). They have not been changed by the rollback.

Change

Ubuntu node image has been upgraded to [`ubuntu-gke-1604-xenial-v20180317-1`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180317-1.9.manifest) for clusters running **Kubernetes 1.9.6-gke.0**.

**Issues fixed:**

  * In `ubuntu-gke-1604-xenial-v20180207-1`, used by Kubernetes 1.9.3-gke.0 and 1.9.4-gke.1, new pods could not be scheduled to node where Docker gets restarted.
  * Security fix for [USN-3586-1](https://usn.ubuntu.com/usn/usn-3586-1)



Change

Ubuntu node image has been upgraded to [`ubuntu-gke-1604-xenial-v20180308`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180308.manifest) for clusters running **Kubernetes 2.8.10-gke.0** and **1.7.15-gke.0**. 

**Issue fixed:**

  * Security fix for [USN-3586-1](https://usn.ubuntu.com/usn/usn-3586-1)



Change

Container-Optimized OS node image has been upgraded to `cos-beta-65-10323-12-0` for clusters running **Kubernetes 1.7.15-gke.0**. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information.

## March 27, 2018

**Note:** This release has been rolled back. Refer to the [March 30, 2018 release note](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive#march-30-2018) for the rollout schedule and cluster default version.

#### New versions available for upgrades and new clusters

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.9.6-gke.0.** , **Kubernetes 1.8.10-gke.0.** , and **Kubernetes 1.7.15-gke.0.** are now **generally available** for use with Google Kubernetes Engine clusters.

#### New default version for new clusters

The following versions are now default according to this week's rollout schedule:

##### Zonal clusters

Change

**Kubernetes 1.8.9-gke.1** is now the default version for new **zonal** and **regional** clusters.

#### Versions no longer available

Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.9.2-gke.1
  * Kubernetes 1.8.8-gke.0
  * Kubernetes 1.7.12-gke.2



### Other Updates

Change

Ubuntu node image has been upgraded to [`ubuntu-gke-1604-xenial-v20180317-1`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180317-1.9.manifest) for clusters running **Kubernetes 1.9.6-gke.0**.

**Issues fixed:**

  * In `ubuntu-gke-1604-xenial-v20180207-1`, used by Kubernetes 1.9.3-gke.0 and 1.9.4-gke.1, new pods could not be scheduled to node where Docker gets restarted.
  * Security fix for [USN-3586-1](https://usn.ubuntu.com/usn/usn-3586-1)



Change

Ubuntu node image has been upgraded to [`ubuntu-gke-1604-xenial-v20180308`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180308.manifest) for clusters running **Kubernetes 1.8.10-gke.0** and **1.7.15-gke.0**. 

**Issue fixed:**

  * Security fix for [USN-3586-1](https://usn.ubuntu.com/usn/usn-3586-1)



Change

Container-Optimized OS node image has been upgraded to `cos-beta-65-10323-12-0` for clusters running **Kubernetes 1.7.15-gke.0**. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information.

## March 21, 2018

### New Features

Feature

[Private Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) are now available in Beta.

## March 19, 2018

### Fixed

Fixed

**Kubernetes 1.9.4+:** Fixes a bug that prevented clusters with IP aliases from appearing.

## March 13, 2018

### Fixed

Fixed

A patch for Kubernetes vulnerabilities [ CVE-2017-1002101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) and [ CVE-2017-1002102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102) is now available according to this week's rollout schedule. We recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your nodes as soon as the patch becomes available in your cluster's zone.

### Issues

Issue

**Breaking Change:** Do not upgrade your cluster if your application requires mounting a **secret** , **configMap** , **downwardAPI** , or **projected volume** with **write access**.

To fix security vulnerability [CVE-2017-1002102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102), **Kubernetes 1.9.4-gke.1** , **Kubernetes 1.8.9-gke.1** , and **Kubernetes 1.7.14-gke.1** changed secret, configMap, downwardAPI, and projected volumes to mount read-only, instead of allowing applications to write data and then reverting it automatically. We recommend that you modify your application to accommodate these changes before you upgrade your cluster.

Issue

If your cluster uses [IP Aliases](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases) and was created with the `--enable-ip-alias` flag, upgrading the master to Kubernetes 1.9.4-gke.1 will prevent it from starting properly. This issue will be addressed in an upcoming release.

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.9.4-gke.1** , **Kubernetes 1.8.9-gke.1** , and **Kubernetes 1.7.14-gke.1** are now **generally available** for use with Google Kubernetes Engine clusters.

#### New default version for new clusters

The following versions are now default according to this week's rollout schedule:

##### Zonal clusters

Change

**Kubernetes 1.8.8-gke.0** is now the default version for new **zonal** and **regional** clusters.

#### Scheduled auto-upgrades

Change

Clusters running the following Kubernetes versions will be automatically upgraded as follows, according to the rollout schedule:

  * Regional clusters running **Kubernetes 1.7.x** will be upgraded to **Kubernetes 1.8.7-gke.1**.



This upgrade applies to cluster masters.

#### Versions no longer available

Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.8.7-gke.1



### New Features

Feature

You can now use version aliases with gcloud's `--cluster-version` option to specify Kubernetes versions. Version aliases allow you to specify the latest version or a specific version, without including the `-gke.0` version suffix. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a complete overview of version aliases.

## March 12, 2018

### Issues

Issue

A patch for Kubernetes vulnerabilities [ CVE-2017-1002101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) and [ CVE-2017-1002102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102) will be available in the upcoming release. We recommend that you [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) your nodes as soon as the patch becomes available.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## March 08, 2018

### New Features

Feature

You can now easily debug your Kubernetes services from the [ Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards#services) with port-forwarding and web preview.

## March 06, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### Versions no longer available

Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.7.12-gke.1



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## February 27, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.9.3-gke.0** , **Kubernetes 1.8.8-gke.0** , and **Kubernetes 1.7.12-gke.2** are now **generally available** for use with Google Kubernetes Engine clusters.

#### Scheduled auto-upgrades

Change

Clusters running the following Kubernetes versions will be automatically upgraded as follows, according to the rollout schedule:

  * Clusters running **Kubernetes 1.8.x** will be upgraded to **Kubernetes 1.8.7-gke.1**.
  * Regional clusters running **Kubernetes 1.8.x** will have etcd upgraded to **etcd 3.1.11**.



This upgrade applies to cluster masters.

#### Versions no longer available

Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.8.5-gke.0



Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * Kubernetes 1.8.5-gke.0



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

Beginning with Kubernetes version 1.9.3, you can enable metadata concealment to prevent user Pods from accessing certain VM metadata for your cluster's nodes. For more information, see [Protecting Cluster Metadata](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy).

### Other Updates

Change

Ubuntu node image has been upgraded from `ubuntu-gke-1604-xenial-v20180122` to [`ubuntu-gke-1604-xenial-v20180207`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180207.manifest) for clusters running **Kubernetes 1.7.12-gke.2** and **1.8.8-gke.0**. 

  * Security fix for [USN-3548-2](https://usn.ubuntu.com/usn/usn-3548-2)



Change

Ubuntu node image has been upgraded from `ubuntu-gke-1604-xenial-v20180122` to [`ubuntu-gke-1604-xenial-v20180207-1`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180207.1.9.manifest) for clusters running **Kubernetes 1.9.3-gke.0**. 

  * Security fix for [USN-3548-2](https://usn.ubuntu.com/usn/usn-3548-2)
  * Docker upgraded from 1.12 to 17.03 and default storage driver changed to overlay2
  * _Known issue_ : When Docker gets restarted on a node, new pods cannot be scheduled on that node and they will be stuck in `ContainerCreating` state.



Change

Container-Optimized OS node image has been upgraded from `cos-stable-63-10032-71-0` to `cos-beta-65-10323-12-0` for clusters running **Kubernetes 1.9.3-gke.0** and **1.8.8-gke.0**. See COS image [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more information.

## February 13, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New default version for new clusters

The following versions are now default according to this week's rollout schedule:

##### Zonal clusters

Change

**Kubernetes version 1.8.7-gke.1** is now the default version for new **zonal** and **regional** clusters.

#### Scheduled auto-upgrades

Change

Clusters running the following Kubernetes versions will be automatically upgraded as follows, according to the rollout schedule:

  * Clusters running **Kubernetes 1.6.13-gke.1** and **1.7.12-gke.0** will be upgraded to **Kubernetes 1.7.12-gke.1**.
  * Clusters running **Kubernetes 1.9.1-gke.0** and **1.9.2-gke.0** will be upgraded to **Kubernetes 1.9.2-gke.1**.
  * Clusters running **etcd 2.*** will be upgraded to **etcd 3.0.17-gke.2**.



This upgrade applies to cluster masters.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## February 8, 2018

### New Features

Feature

[GPUs on Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) are now available in Beta.

## February 5, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

The following versions are now available according to this week's rollout schedule:

Feature

**Kubernetes 1.9.2-gke.1** is now **generally available** for use with Google Kubernetes Engine clusters.

#### New default version for new clusters

The following versions are now default according to this week's rollout schedule:

##### Zonal clusters

Change

**Kubernetes version 1.7.12-gke.1** is now the default version for new **zonal** clusters.

##### Regional clusters

Change

**Kubernetes version 1.8.7-gke.1** is now the default version for new **regional** clusters.

The new cluster versions can be used with the latest Ubuntu [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) version, [`ubuntu-gke-1604-xenial-v20180122`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20180122.manifest).

  * Kernel upgraded from 4.4 to 4.13
  * Security fixes for Spectre and Meltdown
  * Support for [Alias IPs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases)



#### Scheduled auto-upgrades

Change

Clusters running the following Kubernetes versions will be automatically upgraded as follows, according to the rollout schedule:

  * Clusters running **Kubernetes 1.6.13-gke.1** and **1.7.x** will be upgraded to **Kubernetes 1.7.12-gke.0**.



This upgrade applies to cluster masters.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

### New Features

Feature

Beginning with Kubernetes version 1.9.x on Google Kubernetes Engine, you can now perform **horizontal pod autoscaling** based on custom metrics from Stackdriver Monitoring (in addition to the default scaling based on CPU utilization). For more information, see [Scaling an Application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps) and the [custom metrics autoscaling tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling).

### Known Issues

Issue

Beginning with Kubernetes version 1.9.x, automatic firewall rules have changed such that workloads in your Google Kubernetes Engine cluster cannot communicate with other Compute Engine VMs that are on the same network, but _outside the cluster_. This change was made for security reasons.

You can replicate the behavior of older clusters (1.8.x and earlier) by [setting a new firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#autofirewall) on your cluster.

## January 31, 2018

### New Features

Feature

[PodSecurityPolicies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) are now available in Beta.

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New default version for new clusters

The following versions are now default according to this week's rollout schedule:

Change

**Kubernetes version 1.7.12-gke.0** is now the default version for new zonal clusters.

Change

**Kubernetes version 1.8.6-gke.0** is now the default version for new regional clusters.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available according to this week's rollout schedule:

  * **Kubernetes 1.8.7-gke.0**
  * **Kubernetes 1.9.2-gke.0** clusters are now available for whitelisted early-access users. Non-whitelisted users can specify version 1.9.2-gke.0 in [Alpha Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## January 16, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available according to this week's rollout schedule:

  * **Kubernetes 1.9.1** clusters are now available for whitelisted early-access users. Non-whitelisted users can specify version 1.9.1 in [Alpha Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).



#### Scheduled auto-upgrades

Change

Clusters running the following Kubernetes versions will be automatically upgraded as follows, according to the rollout schedule:

  * Clusters running **Kubernetes 1.6.x** will be upgraded to **1.7.11-gke.1**.



This upgrade applies to cluster masters.

### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## January 10, 2018

### New Features

Feature

You can now run Container Engine clusters in region `europe-west4` (Netherlands).

Feature

You can now run Container Engine clusters in region `northamerica-northeast1` (Montréal).

## January 9, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New default version for new clusters

Change

**Kubernetes version 1.7.11-gke.1** is now the default version for new clusters, available according to this week's rollout schedule.

#### Scheduled auto-upgrades

Change

Clusters running the following Kubernetes versions will be automatically upgraded as follows, according to the rollout schedule:

  * Clusters running **Kubernetes 1.6.x** will be upgraded to **1.6.13-gke.1**.
  * Clusters running **Kubernetes 1.7.x** will be upgraded to **1.7.11-gke.1**.
  * Clusters running **Kubernetes 1.8.x** will be upgraded to **1.8.5-gke.0**



This upgrade applies to cluster masters and, if [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/node-auto-upgrade) are enabled, all cluster nodes.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available for new clusters and opt-in master and node upgrades according to this week's rollout schedule:

  * **Kubernetes 1.8.6-gke.0**
  * **Kubernetes 1.7.12-gke.0**



#### Versions no longer available

Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * **Kubernetes 1.8.4-gke.1**



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## January 2, 2018

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New default version for new clusters

Change

**Kubernetes version 1.7.11-gke.1** is now the default version for new clusters, available according to this week's rollout schedule.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available for new clusters and opt-in master and node upgrades according to this week's rollout schedule:

  * **Kubernetes 1.8.5-gke.0**



#### Versions no longer available

Change

The following versions are no longer available for new clusters or cluster upgrades: 

  * **Kubernetes 1.6.x** (all versions)
  * **Kubernetes 1.7.8**
  * **Kubernetes 1.7.9**



### Rollout schedule

The rollout schedule is now included in [Upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#rollout_schedule). 

## December 14, 2017

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available for new clusters and opt-in master and node upgrades according to this week's rollout schedule:

  * **Kubernetes 1.8.4-gke.1**
  * **Kubernetes 1.7.11-gke.1**
  * **Kubernetes 1.6.13-gke.1**



These version updates change the default [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) for Kubernetes Engine nodes to [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) version `cos-stable-63-10032-71-0-p`. 

#### Versions no longer available

Change

The following versions are **no longer available** for new clusters or opt-in master and node upgrades:

  * **Kubernetes 1.8.4-gke.0**
  * **Kubernetes 1.7.11-gke.0**
  * **Kubernetes 1.6.13-gke.0**



#### Rollout schedule

Date | Available zones  
---|---  
2017-12-14 | `europe-west2-a`, `us-east1-d`  
2017-12-15 | `asia-east1-a`, `asia-northeast1-a`, `asia-south1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-12-18 | `asia-east1-c`, `asia-northeast1-b`, `asia-south1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-12-19 | `asia-east1-b`, `asia-northeast1-c`, `asia-south1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
## December 5, 2017

### New Features

Feature

[Regional Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) are now available in Beta.

## December 1, 2017

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

### New Features

Feature

[Audit Logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging) is now available in Beta.

## November 28, 2017

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available for new clusters and opt-in master and node upgrades according to this week's rollout schedule:

  * **Kubernetes 1.8.4-gke.0**
  * **Kubernetes 1.7.11-gke.0**
  * **Kubernetes 1.6.13-gke.0**



#### Rollout schedule

Date | Available zones  
---|---  
2017-11-28 | `europe-west2-a`, `us-east1-d`  
2017-11-29 | `asia-east1-a`, `asia-northeast1-a`, `asia-south1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-11-30 | `asia-east1-c`, `asia-northeast1-b`, `asia-south1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-12-1 | `asia-east1-b`, `asia-northeast1-c`, `asia-south1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### Other Updates

Change

[Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) version [m63](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) is now available for use as a Google Kubernetes Engine [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

## November 13, 2017

### Version updates

Kubernetes Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Kubernetes Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available for new clusters and opt-in master and node upgrades according to this week's rollout schedule:

  * **Kubernetes 1.7.10-gke.0**
  * **Kubernetes 1.8.3-gke.0**



### Other Updates

Change

Container Engine is now named **Kubernetes Engine**. See the [Google Cloud blog post](https://cloudplatform.googleblog.com/2017/11/introducing-Certified-Kubernetes-and-Google-Kubernetes-Engine.html).

Change

Kubernetes Engine's `kubectl` version has been updated from 1.8.2 to 1.8.3.

## November 7, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available for new clusters and opt-in master and node upgrades according to this week's rollout schedule:

  * **Kubernetes 1.8.2-gke.0**



#### Rollout schedule

Date | Available zones  
---|---  
2017-11-07 | `europe-west2-a`, `us-east1-d`  
2017-11-08 | `asia-east1-a`, `asia-northeast1-a`, `asia-south1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-11-09 | `asia-east1-c`, `asia-northeast1-b`, `asia-south1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-11-10 | `asia-east1-b`, `asia-northeast1-c`, `asia-south1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### New Features

Feature

Added an option to the `gcloud container clusters create` command: `--enable-basic-auth`. This option allows you to create a cluster with basic authorization enabled.

Feature

Added options to the `gcloud container clusters update` command: `--enable-basic-auth`, `--username`, and `--password`. These options allows you to enable or disable basic authorization and change the username and password for an existing cluster.

## October 31, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following versions are now available for new clusters and opt-in master and node upgrades according to this week's rollout schedule:

  * **Kubernetes 1.7.9-gke.0**



#### Scheduled auto-upgrades

Change

Clusters running the following Kubernetes versions will be automatically upgraded as follows, according to the rollout schedule:

  * Clusters running **Kubernetes 1.6.x** will be upgraded to **1.6.11-gke.0**.
  * Clusters running **Kubernetes 1.7.x** will be upgraded to **1.7.8-gke.0**.
  * Clusters running **Kubernetes 1.8.x** will be upgraded to **1.8.1-gke.1**



This upgrade applies to cluster masters and, if [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/node-auto-upgrade) are enabled, all cluster nodes.

#### New default version for new clusters

Change

**Kubernetes version 1.7.8-gke.0** is now the default version for new clusters, available according to this week's rollout schedule.

#### Rollout schedule

Date | Available zones  
---|---  
2017-10-31 | `europe-west2-a`, `us-east1-d`  
2017-11-1 | `asia-east1-a`, `asia-northeast1-a`, `asia-south1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-11-2 | `asia-east1-c`, `asia-northeast1-b`, `asia-south1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-11-3 | `asia-east1-b`, `asia-northeast1-c`, `asia-south1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### New Features

Feature

You can now run Container Engine clusters in region `asia-south1` (Mumbai).

### Fixes

Fixed

Clusters using the [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) version `cos-stable-61` can be affected by Docker daemon crashes and restarts and become unable to schedule pods.

To mitigate this issue, clusters running Kubernetes versions 1.6.x, 1.7.x, and 1.8.x are slated to automatically upgrade to versions 1.6.11-gke.0, 1.7.8-gke.0, and 1.8.1-gke.1 respectively. These versions have been remapped to use the `cos-stable-60-9592-90-0` node image.

Automatic upgrades must be enabled for this workaround to take effect. If your cluster does not have auto-upgrades enabled, you must manually upgrade your cluster to the appropriate version to employ the workaround.

### Known Issues

Issue

Clusters running Kubernetes version 1.7.6 might see inaccurate memory usage metrics for pods running on the cluster. Clusters are slated to automatically upgrade to version 1.7.8-gke.0 to mitigate this issue. If node auto-upgrades are not enabled for your cluster, you can manually upgrade to 1.7.8-gke.0.

## October 24, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

**Kubernetes version 1.8.1** is now generally available, according to this week's rollout schedule. See the [Google Cloud blog post on Container Engine 1.8](https://cloud.google.com/blog/products/gcp/google-container-engine-kubernetes-18) for more information on the Kubernetes capabilties highlighted in this release.

#### Rollout schedule

Date | Available zones  
---|---  
2017-10-24 | `europe-west2-a`, `us-east1-d`  
2017-10-25 | `asia-east1-a`, `asia-northeast1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-10-26 | `asia-east1-c`, `asia-northeast1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-10-27 | `asia-east1-b`, `asia-northeast1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### New Features

Feature

You can now run [CronJobs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cronjobs) on your Container Engine cluster. CronJob is a Beta feature in Kubernetes version 1.8.

Feature

You can now view the status of your cluster's nodes using the Google Cloud console.

Feature

The Google Cloud console browser-integrated cloud shell can now automatically generate commands for the `kubectl` command-line interface.

Feature

You can now edit your cluster's workloads when viewing them with the Google Cloud console.

### Known Issues

Issue

Kubernetes Third-party Resources, previously deprecated, have been removed in version 1.8. These resources will cease to function on clusters upgrading to version 1.8.1 or later.

Issue

Audit Logging, a beta feature in Kubernetes 1.8, is currently not enabled on Container Engine.

Issue

Horizontal Pod Autoscaling with Custom Metrics, a beta feature in Kubernetes 1.8, is currently not enabled on Container Engine.

### Other Updates

Change

Beta features in the Container Engine API (and `gcloud` command-line interface) are now exposed via the new `v1beta1` [API surface](https://docs.cloud.google.com/kubernetes-engine/reference/rest). To use beta features on Container Engine, you must configure the `gcloud` command-line interface to use the Beta API surface to run `gcloud beta container` commands. See [API organization](https://docs.cloud.google.com/kubernetes-engine/reference/api-organization) for more information.

## October 10, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following Kubernetes versions are now available for new clusters and opt-in master upgrades for existing clusters, according to this week's rollout schedule:

  * 1.7.8
  * 1.6.11



Feature

Clusters running Kubernetes version 1.6.11 can safely upgrade to Kubernetes versions 1.7.x.

#### Rollout schedule

Date | Available zones  
---|---  
2017-10-10 | `europe-west2-a`, `us-east1-d`  
2017-10-11 | `asia-east1-a`, `asia-northeast1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-10-12 | `asia-east1-c`, `asia-northeast1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-10-13 | `asia-east1-b`, `asia-northeast1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### Other Updates

Change

Clusters running Kubernetes versions 1.7.8 and 1.6.11 have upgraded the version of [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) running on cluster nodes from version `cos-stable-60-9592-84-0` to `cos-stable-61-9765-66-0`. See the [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for more details.

This upgrade updates the node's Docker version from 1.13 to 17.03. See the [Docker](https://docs.docker.com/engine/deprecated/) documentation for details on feature deprecations.

## October 3, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

Kubernetes version 1.8.0-gke.0 is now available for early access partners and [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/alpha-clusters) only. To try out v1.8.0-gke.0, [sign up](https://docs.google.com/forms/d/1P7IWVK5a_JMOj5K455KRxmcnR2Gn-qKQUgnTveaPZeo/edit) for the early access program.

#### Scheduled master auto-upgrades

Change

Cluster masters running Kuberenetes versions 1.7.x will be automatically upgraded to Kubernetes v1.7.6-gke.1 according to this week's rollout schedule.

#### Rollout schedule

Date | Available zones  
---|---  
2017-10-03 | `europe-west2-a`, `us-east1-d`  
2017-10-04 | `asia-east1-a`, `asia-northeast1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-10-05 | `asia-east1-c`, `asia-northeast1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-10-06 | `asia-east1-b`, `asia-northeast1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### New Features

Feature

You can now rotate your username for basic authorization on existing clusters, or disable basic authorization by providing an empty username.

### Fixes

Fixed

**Kubernetes 1.7.6-gke.1** : Fixed a regression in `fluentd`. 

Fixed

**Kubernetes 1.7.6-gke.1** : Updated the `kube-dns` add-on to patch `dnsmasq` vulnerabilities announced on October 2. For more information on the vulnerability, see the associated [Kubernetes Security Announcement](https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/kubernetes-dev/QWIzhD3JhhE/AllfBkKLAwAJ).

### Known Issues

Issue

**Kubernetes 1.8.0-gke.0** (early access and alpha clusters only): Clusters created with a subnetwork with an automatically-generated name that contains a hash (e.g. "default-38b01f54907a15a7") might encounter issues where their [internal load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/internal-load-balancing) fail to sync.

This issue also affects clusters that run [legacy networks](https://docs.cloud.google.com/compute/docs/vpc/legacy).

Issue

Container Engine clusters can enter a bad state if you convert your automatically-configured network to a manually-configured one. In this state, [internal load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/internal-load-balancing) might fail to sync, and node pool upgrades might fail.

## September 27, 2017

### New Features

Feature

You can now configure a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/maintenance-window) for your Container Engine clusters. You can use the maintenance window feature to designate specific spans of time for scheduled maintenance and upgrades to your master and nodes. Maintenance window is a **beta** feature on Container Engine.

Feature

Container Engine's [node auto upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/node-auto-upgrades) feature is now generally available.

Feature

The Ubuntu [node image](https://docs.cloud.google.com/kubernetes-engine/docs/node-images) is now generally available for use on your Container Engine cluster nodes.

## September 25, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### Scheduled master auto-upgrades

Change

Cluster masters running Kuberenetes versions 1.7.x will be automatically upgraded to Kubernetes v1.7.5 according to this week's rollout schedule.

Change

Cluster masters running Kuberenetes versions 1.6.x will be automatically upgraded to Kubernetes v1.6.10 according to this week's rollout schedule.

#### Rollout schedule

Date | Available zones  
---|---  
2017-09-25 | `europe-west2-a`, `us-east1-d`  
2017-09-26 | `asia-east1-a`, `asia-northeast1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-09-27 | `asia-east1-c`, `asia-northeast1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-09-28 | `asia-east1-b`, `asia-northeast1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### Fixes

Fixed

**Kubernetes v1.7.5** : Fixed an issue with Kubernetes v1.7.0 to v1.7.4 in which `controller-manager` could become unhealthy and enter a repair loop.

Fixed

**Kubernetes v1.6.10** : Fixed an issue in which a Google Cloud Load Balancer could enter a persistently bad state if an API call failed while the ingress controller was starting.

## September 18, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New default version for new clusters

Change

[Kubernetes v1.7.5](https://github.com/kubernetes/kubernetes/releases/tag/v1.7.5) is the default version for new clusters, available according to this week's rollout schedule below.

#### New versions available for upgrades and new clusters

Feature

The following Kubernetes versions are now available for new clusters and opt-in master upgrades for existing clusters:

  * 1.7.6
  * 1.6.10



#### New versions available for node upgrades and downgrades

Feature

The following Kubernetes versions are now available for _node_ upgrades and downgrades:

  * 1.7.6
  * 1.6.10



#### Rollout schedule

Date | Available zones  
---|---  
2017-09-19 | `europe-west2-a`, `us-east1-d`  
2017-09-20 | `asia-east1-a`, `asia-northeast1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-09-21 | `asia-east1-c`, `asia-northeast1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-09-22 | `asia-east1-b`, `asia-northeast1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### New Features

Feature

Starting in Kubernetes version 1.7.6, the available resources on cluster nodes have been updated to account for the CPU and memory requirement of Kubernetes node daemons. See the [Node documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) in the [cluster architecture overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) for more information.

Feature

You can now [set a cluster network policy](https://docs.cloud.google.com/kubernetes-engine/docs/network-policy) on your Container Engine clusters running Kubernetes version 1.7.6 or later.

### Other Updates

Change

The deprecated `container-vm` node image type has been removed from the list of valid Container Engine node images. Existing clusters and node pools will continue to function, but you can no longer create new clusters and node pools that run the `container-vm` node image.

Issue

Clusters that use the deprecated `container-vm` as a node image cannot be upgraded to Kubernetes v1.7.6 or later.

## September 12, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New versions available for upgrades and new clusters

Feature

The following Kubernetes versions are now available for new clusters and opt-in master upgrades for existing clusters:

  * 1.7.5
  * 1.6.9
  * 1.6.7



#### Scheduled master auto-upgrades

Change

Cluster masters running Kubernetes versions 1.6.x will be upgraded to [Kubernetes v1.6.9](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v169) according to this week's rollout schedule.

#### Rollout schedule

Date | Available zones  
---|---  
2017-09-12 | `europe-west2-a`, `us-east1-d`  
2017-09-13 | `asia-east1-a`, `asia-northeast1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-09-14 | `asia-east1-c`, `asia-northeast1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-09-17 | `asia-east1-b`, `asia-northeast1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### New Features

Feature

You can now use [IP aliases](https://docs.cloud.google.com/kubernetes-engine/docs/ip-aliases) with an existing subnetwork when creating a cluster. IP aliases are a Beta feature in Google Kubernetes Engine version 1.7.5.

## September 05, 2017

### Version updates

Container Engine cluster versions have been updated as detailed in the following sections. See [versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) for a full list of the Kubernetes versions you can run on your Container Engine masters and nodes.

#### New default version for new clusters

Change

[Kubernetes v1.6.9](https://github.com/kubernetes/kubernetes/releases/tag/v1.6.9) is the default version for new clusters, available according to this week's rollout schedule.

#### New versions available for upgrades and new clusters

Feature

[Kubernetes v1.7.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v175) is now available for new clusters and opt-in master upgrades.

#### Versions no longer available

Change

The following Kubernetes versions are _no longer available_ for new clusters or upgrades to existing cluster masters:

  * 1.7.3
  * 1.7.4



#### Rollout schedule

Date | Available zones  
---|---  
2017-09-05 | `europe-west2-a`, `us-east1-d`  
2017-09-06 | `asia-east1-a`, `asia-northeast1-a`, `asia-southeast1-a`, `australia-southeast1-a`, `europe-west1-c`, `europe-west3-a`, `southamerica-east1-a`, `us-central1-b`, `us-east4-b`, `us-west1-a`  
2017-09-07 | `asia-east1-c`, `asia-northeast1-b`, `asia-southeast1-b`, `australia-southeast1-b`, `europe-west1-b`, `europe-west2-b`, `europe-west3-b`, `southamerica-east1-b`, `us-central1-f`, `us-east1-c`, `us-east4-c`, `us-west1-b`  
2017-09-08 | `asia-east1-b`, `asia-northeast1-c`, `australia-southeast1-c`, `europe-west1-d`, `europe-west2-c`, `europe-west3-c`, `southamerica-east1-c`, `us-central1-a`, `us-central1-c`, `us-east1-b`, `us-east4-a`, `us-west1-c`  
  
### Other Updates

Change

Container Engine's `kubectl` version has been updated from 1.7.4 to 1.7.5.

Change

You can now run Container Engine clusters in region `southamerica-east1` (São Paulo).

## August 28, 2017

  * [Kubernetes v1.7.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v174) is available for new clusters and opt-in master upgrades.

  * [Kubernetes v1.6.9](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v169) is available for new clusters and opt-in master upgrades.

  * Clusters with a master version of v1.6.7 and [Node Auto-Upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/node-auto-upgrades) enabled will have nodes upgraded to v1.6.7.

  * Clusters with a master version of v1.7.3 and [Node Auto-Upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/node-auto-upgrades) enabled will have nodes upgraded to v1.7.3.

  * Starting at version v1.7.4, when Cloud Monitoring is enabled for a cluster, [container system metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-container) will start to be pushed by Heapster to Stackdriver Monitoring API. The metrics remain free, though Stackdriver Monitoring API quota will be affected.

  * Clusters running Kubernetes v1.6.9 and v1.7.4 have updated node images:

    * The COS node image was upgraded from `cos-stable-59-9460-73-0` to `cos-stable-60-9592-84-0`. Please see the [COS image release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes) for details. 
      * The new COS image includes an upgrade of Docker, from v1.11.2 to v1.13.1. This Docker upgrade contains many stability and performance fixes. A full list of the Docker features that have been deprecated between v1.11.2 and v1.13.1 is available on [Docker's website](https://docs.docker.com/engine/deprecated/).
      * Three features in Docker v1.13.1 are disabled by default in the COS m60 image, but are planned to be enabled in a later node image release: live-restore, shared PID namespaces and overlay2.
      * **Known issue** : Docker v1.13.1 supports [HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck), which was previously ignored by Docker v1.11.2 on COS m59. Kubernetes supports more powerful liveness/readiness checks for containers, and it currently does not surface or consume the `HEALTHCHECK` status reported by Docker. We encourage users to disable `HEALTHCHECK` in Docker images to reduce unnecessary overhead, especially if performance degradation is observed after node upgrade. Note that `HEALTHCHECK` could be inherited from the base image.
    * Ubuntu node image was upgraded from [`ubuntu-gke-1604-xenial-v20170420-1`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20170420.1.manifest) to [`ubuntu-gke-1604-xenial-v20170816-1`](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-xenial-amd64-gke-20170816.1.manifest). 
      * This patch release is based on Ubuntu 16.04.3 LTS.
      * It includes a fix for the Stackdriver Logging issues in `ubuntu-gke-1604-xenial-v20170420-1`.
      * **Known issue** : [Alias IPs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases) is not supported.
  * **Known Issues upgrading to v1.7:**




There is a known issue with StatefulSets in 1.7.X that causes StatefulSet pods to become unavailable in DNS upon upgrade. We are currently recommending that you not upgrade to 1.7.X if you are using DNS with StatefulSets. A fix is being prepared. Additional information can be found here: https://github.com/kubernetes/kubernetes/issues/48327

  * **Known Issues running Docker v1.13:**



Docker v1.13.1 supports [HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck), which was previously ignored by Docker v1.11.2 on COS m59. Kubernetes supports more powerful liveness/readiness checks for containers, and it currently does not surface or consume the `HEALTHCHECK` status reported by Docker. We encourage users to disable `HEALTHCHECK` in Docker images to reduce unnecessary overhead, especially if performance degradation is observed after node upgrade. Note that `HEALTHCHECK` could be inherited from the base image.

## August 21, 2017

  * When using IP aliases, you can now represent service CIDR blocks by using a secondary range instead of a subnetwork. This means you can use IP aliases without specifying the `--create-subnetwork` option.
  * Cluster etcd fragmentation/compaction fixes.

  * **Known Issues upgrading to v1.7.3:**




There is a known issue with StatefulSets in 1.7.X regarding annotations, so we are currently recommending that you not upgrade to 1.7.X if you are using them. A fix is being prepared. Additional information can be found here: https://github.com/kubernetes/kubernetes/issues/48327

## August 14, 2017

  * Cluster masters running Kubernetes versions 1.7.X will be upgraded to [v1.7.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v173) according to the following schedule:

    * 2017-08-15: europe-west2-a us-east1-d
    * 2017-08-16: asia-east1-a asia-northeast1-a asia-southeast1-a australia-southeast1-a europe-west1-c europe-west3-a us-central1-b us-east4-b us-west1-a
    * 2017-08-17: asia-east1-c asia-northeast1-b asia-southeast1-b australia-southeast1-b europe-west1-b europe-west2-b europe-west3-b us-central1-f us-east1-c us-east4-c us-west1-b
    * 2017-08-18: asia-east1-b asia-northeast1-c australia-southeast1-c europe-west1-d europe-west2-c europe-west3-c us-central1-a us-central1-c us-east1-b us-east4-a us-west1-c
  * You can now specify a minimum CPU size/class for Alpha clusters by using the `--min-cpu-platform` flag with `gcloud alpha container` commands.

  * Cluster resize commands (`gcloud alpha container clusters resize` or `gcloud beta container clusters resize`) now safely drain nodes before removal.

  * Updated Google Container Engine's kubectl from version 1.7.2 to 1.7.3.

  * Added `--logging-service` flag to `gcloud beta container clusters update`. This flag controls the enabling and disabling of Stackdriver Logging integration. Use `--logging-service=logging.googleapis.com` to enable and `--logging-service=none` to disable.

  * Modified the `--scopes` flag in `gcloud beta container clusters create` and `gcloud beta container node-pools create` commands to default to `logging.write,monitoring` and support passing an empty list.




## August 7, 2017

  * [Kubernetes v1.7.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v173) is available for new clusters and opt-in master upgrades.

  * [Kubernetes v1.6.8](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v168) is available for new clusters and opt-in master upgrades.

  * Cluster masters running Kubernetes version v1.6.6 or older will be upgraded to [v1.6.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v167) according to the following schedule:

    * 2017-08-08: europe-west2-a us-east1-d
    * 2017-08-09: asia-east1-a asia-northeast1-a asia-southeast1-a australia-southeast1-a europe-west1-c europe-west3-a us-central1-b us-east4-b us-west1-a
    * 2017-08-10: asia-east1-c asia-northeast1-b asia-southeast1-b australia-southeast1-b europe-west1-b europe-west2-b europe-west3-b us-central1-f us-east1-c us-east4-c us-west1-b
    * 2017-08-11: asia-east1-b asia-northeast1-c australia-southeast1-c europe-west1-d europe-west2-c europe-west3-c us-central1-a us-central1-c us-east1-b us-east4-a us-west1-c
  * Node pools can now be created with an initial node count of 0.

  * Cloud monitoring can only be enabled in clusters that have monitoring scope enabled in all node pools.

  * **Known Issues upgrading to v1.6.7:**

    * Kubernetes 1.6.7 includes version 0.9.5 of the Google Cloud Ingress Controller. This version contains a fix for a bug that caused the controller to incorrectly synchronize Google Cloud URL Maps. Changes to the ingress resource may not have caused the Google Cloud URL Map to update. Using the fixed controller will ensure maps reflect the host and path rules. To avoid potential disruption, validate that all ingress objects contain the desired `host` or `path` rules.



## August 3, 2017

  * Users with access to Kubernetes [Secret](https://kubernetes.io/docs/concepts/configuration/secret) objects can no longer view the secrets' values in Google Container Engine UI. The recommended way to access them is with the `kubectl` tool.



## August 1, 2017

  * The VM firewall rule (e.g. `cluster-<hash>-vms`) for non-legacy auto-mode networks now includes both the primary and reserved VM ranges (10.128/9) if the primary range lies outside of the reserved range.

  * You can now use the beta Ubuntu node image with clusters running Kubernetes version 1.6.4 or higher.

  * You can now run Container Engine clusters in region `europe-west3` (Frankfurt).




## July 26, 2017

  * You can now use the [Google Cloud console](https://console.cloud.google.com/) to add additional zones to, or remove zones from, your existing multi-zone clusters. For more information, see [Multi-Zone Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters).
  * You can now use the [Google Cloud console](https://console.cloud.google.com/) to define [Master Authorized Networks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work) \- a restricted range of IP addresses that are permitted to access your container cluster's Kubernetes master endpoint.



## July 25, 2017

  * [Kubernetes v1.7.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v172) is available for new clusters and opt-in master upgrades.

  * **Known Issues upgrading to v1.7.2:**

    * If you are upgrading nodes from 1.7.0 or 1.7.1 to 1.7.2, you may experience service disruption if you have services of type=LoadBalancer. To mitigate this potential disruption, see the [upgrade instructions for versions 1.7.0 and 1.7.1](https://docs.cloud.google.com/kubernetes-engine/docs/upgrade-notice-1-7-2).
  * [Kubernetes v1.6.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v167) is the default version for new clusters, released according to the following schedule:

    * 2017-07-25: us-east1-d europe-west2-a
    * 2017-07-26: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a asia-southeast1-a us-east4-b australia-southeast1-a
    * 2017-07-27: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b asia-southeast1-b us-east4-c australia-southeast1-b europe-west2-b
    * 2017-07-28: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b us-east4-a us-west1-c australia-southeast1-c europe-west2-c asia-northeast1-c
  * `gcloud beta container clusters create` now supports [enabling authorized networks for Kubernetes Master](https://docs.cloud.google.com/kubernetes-engine/docs/authorized-networks) via `--enable-master-authorized-networks` and `--master-authorized-networks` flags.

  * `gcloud beta container clusters update` now supports [configuring authorized networks for Kubernetes Master](https://docs.cloud.google.com/kubernetes-engine/docs/authorized-networks) via `--enable-master-authorized-networks`, `--no-enable-master-authorized-networks`, and `--master-authorized-networks` flags.

  * `gcloud container clusters create` now allows the Kubernetes Dashboard to be disabled for a new cluster via the `--disable-addons=KubernetesDashboard` flag.

  * `gcloud container clusters update` now allows the Kubernetes Dashboard to be disabled on existing clusters via the `--update-addons=KubernetesDashboard=DISABLED` flag.




## July 18, 2017

  * [Kubernetes v1.7.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v171) is available for new clusters and opt-in master upgrades.

  * Cluster masters running Kubernetes version v1.7.0 will be upgraded to [v1.7.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v171) according to the following schedule:

    * 2017-07-18: us-east1-d europe-west2-a
    * 2017-07-19: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a asia-southeast1-a us-east4-b australia-southeast1-a
    * 2017-07-20: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b asia-southeast1-b us-east4-c australia-southeast1-b europe-west2-b
    * 2017-07-21: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b us-east4-a us-west1-c australia-southeast1-c europe-west2-c asia-northeast1-c
  * Container Engine now respects Kubernetes [Pod Disruption Budgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions), making stateful workloads more stable during upgrades. This also reduces disruptions during node auto-upgrades.

  * `gcloud container clusters get-credentials` now correctly respects the HOMEDRIVE/HOMEPATH and USERPROFILE environment variables when generating the kubectl config file on Windows.

  * **Known Issues with v1.7.1:**

    * Google Cloud Internal Load Balancers created through Kubernetes services (a Beta feature in 1.7) have an issue that causes health-checks to fail preventing them from functioning. This will be fixed in a future patch release.

    * Services of type=LoadBalancer in clusters that have nodes running Kubernetes v1.7 may fail Google Cloud Load Balancer health checks. However, the Load Balancers will continue to forward traffic to backends. This issue will be fixed in future patch release and may require special upgrade actions.




## July 13, 2017

  * New views available in Google Container Engine UI, allowing cross-cluster overview and inspection of various Kubernetes Objects. This new UI will be rolling out in the coming week: 
    * [Workloads](https://console.cloud.google.com/kubernetes/workload): inspect and diagnose your pods and their controllers.
    * [Discovery and load balancing](https://console.cloud.google.com/kubernetes/discovery): view details of your services, ingresses and load balancers.
    * [Configuration](https://console.cloud.google.com/kubernetes/config): survey all config maps and secrets your containers are using.
    * [Storage](https://console.cloud.google.com/kubernetes/storage): browse all storage classes, persistent volumes and claims that your clusters use.



## July 11, 2017

  * [Kubernetes v1.7.0](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v170) This version will be available for new clusters and opt-in master upgrades according to the following planned schedule:

    * 2017-07-11: europe-west2-a
    * 2017-07-12: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a asia-southeast1-a us-east4-b australia-southeast1-a
    * 2017-07-13: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b asia-southeast1-b us-east4-c australia-southeast1-b europe-west2-b
    * 2017-07-14: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b us-east4-a us-west1-c australia-southeast1-c europe-west2-c asia-northeast1-c
  * Kubernetes 1.7 is being made available as an optional version for clusters. Please see the [release announcement](https://cloud.google.com/blog/products/gcp/container-engine-now-runs-kubernetes-1-7-to-drive-enterprise-ready-secure-hybrid-workloads) for more details on new features.

  * You can now use HTTP re-encryption through Google Cloud Load Balancing to allow HTTPS access from the Google Cloud Load Balancer to your service backend. This feature ensures that your data is fully encrypted in all phases of transit, even after it enters Google's global network.

  * Support for all-private IP (RFC-1918) addresses is generally available. These addresses allow you create clusters and access resources in all-private IP ranges, and extends your ability to use Container Engine clusters with existing networks.

  * Support for external source IP preservation is now generally available. This feature allows applications to be fully aware of client IP addresses for Kubernetes services you expose.

  * Cluster autoscaler now supports for scaling node pools to 0 or 1, for when you don't need capacity.

  * Cluster autoscaler can now use a pricing-based expander, which applies additional cost-based constraints to let you use auto-scaling in the most cost-effective manner. This is default as of 1.7.0 and is not user-configurable.

  * Cluster autoscaler now supports balanced scale-outs of similar node groups. This is useful for clusters that span multiple zones.

  * You can now use API Aggregation to extend the Kubernetes API with custom APIs. For example, you can now add existing API solutions such as service catalog, or build your own.

  * The following new features are available on Alpha clusters running Kubernetes version 1.7:

    * Local storage
    * External webhook admission controllers
  * **Known Issues with v1.7.0:**

    * Kubelet certificate rotation is not enabled for Alpha clusters. This issue will be fixed in a future release.
    * Kubernetes services with network load balancers using static IP will cause the kube-controller-manager to crash loop, leading to multiple master repairs. See issue[#48848](https://github.com/kubernetes/kubernetes/issues/48848) for more details. This issue will be fixed in a future release.



## July 10, 2017

  * You can now create clusters with preemptible nodes using the [Google Cloud console](https://console.cloud.google.com/). For more information, see [Preemptible VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms).

  * You can now disable basic authentication for new clusters using the [Google Cloud console](https://console.cloud.google.com/).

  * You can now disable client certificate generation for new clusters using the [Google Cloud console](https://console.cloud.google.com/).




## June 26, 2017

  * **Known Issues with v1.6.6** A bug in the version of fluentd bundled with Kubernetes [v1.6.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v166) causes JSON-formatted logs to be exported as plain text. This issue will be fixed in v1.6.7. Meanwhile v1.6.6 will remain available as an optional version for new cluster creation and opt-in master upgrades, but will not be made the default. See issue [#48018](https://github.com/kubernetes/kubernetes/issues/48108) for more details.
  * There will be no release for the week of July 3rd, since this is a holiday in the US. The next release is planned for the week of July 10th.



## June 20, 2017

  * You can now use [v1.6.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v166) for creating new clusters.
  * Original plan to upgrade container cluster masters to 1.6 this week has been postponed due to a bug in the GLBC ingress controller that causes unintentional overwrites of manual health check edits (See [known issues for v1.6.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md#known-issues-for-v164)). This bug is fixed in 1.6.6.
  * DeleteNodepool now drains all nodes in the pool before deletion.
  * You can now run Container Engine clusters in region `australia-southeast1` (Sydney).



## June 13, 2017

  * [v1.5.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v157) will no longer be available for new clusters and master upgrades.
  * All cluster masters will be upgraded to [v1.6.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v164) in the week of 2017-06-19.



## June 5, 2017

  * Cluster masters running Kubernetes versions v1.6.0 - v1.6.3 will be upgraded to [v1.6.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v164) according to the following schedule: 
    * 2017-06-05: us-east1-d asia-northeast1-c
    * 2017-06-06: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a asia-southeast1-a us-east4-b australia-southeast1-a europe-west2-a
    * 2017-06-07: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b asia-southeast1-b us-east4-c australia-southeast1-b europe-west2-b
    * 2017-06-08: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b us-east4-a us-west1-c australia-southeast1-c europe-west2-c
  * After 2017-06-12, v1.5.7 will no longer be available for new clusters and master upgrades.
  * You can now run Container Engine clusters in region europe-west2 (London).



## June 1, 2017

  * You can now specify a Kubernetes version when creating a cluster using the [Google Cloud console](https://console.cloud.google.com/)
  * You can now change the automatic repair setting for existing node pools in [Google Cloud console](https://console.cloud.google.com/). For more information, see [Node Auto-Repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair).
  * You can now change the image type for existing node pools in [Google Cloud console](https://console.cloud.google.com/). For more information, see [Node Image Migration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).



## May 30, 2017

  * [Kubernetes v1.6.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v164) is the default version for new clusters, released according to the following schedule: 
    * 2017-05-30: us-east1-d asia-northeast1-c
    * 2017-05-31: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a asia-southeast1-a us-east4-b australia-southeast1-a europe-west2-a
    * 2017-06-01: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b asia-southeast1-b us-east4-c australia-southeast1-b europe-west2-b
    * 2017-06-02: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b us-east4-a us-west1-c australia-southeast1-c europe-west2-c



## May 24, 2017

  * [Kubernetes v1.6.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v164) is available for new clusters and opt-in master upgrades.
  * v1.6.1 is no longer available for container cluster node upgrades/downgrades.
  * The default cluster version for new clusters will be changed to [Kubernetes v1.6.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v164) in the week of May 29th.
  * [Kubernetes v1.6.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v163) was skipped due to known issues that have been [fixed in v1.6.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md#other-notable-changes).



## May 17, 2017

  * You can now create clusters with more than 500 nodes in zones `europe-west1-b` and `us-central1-a`.
  * Fixed the known issue with Container Engine's IP Rotation feature where the cluster SSH firewall rule was not being updated.
  * Container Engine integration with [Google Cloud Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels) is now available in Beta. For more information, see [Cluster Labeling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels).



## May 12, 2017

  * You can now use the [Google Cloud console](https://console.cloud.google.com/) to choose whether clusters should use legacy authorization permissions. This option is available in clusters running version 1.6 or later. See the [Role-Based Access Control Documentation](https://docs.cloud.google.com/kubernetes-engine/docs/role-based-access-control) for more information.



## May 10, 2017

  * Cluster masters running Kubernetes versions v1.5.6 and below will be upgraded to [v1.5.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v157) according to the following schedule: 
    * 2017-05-09: us-east1-d asia-northeast1-c
    * 2017-05-10: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a asia-southeast1-a us-east4-b
    * 2017-05-11: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b asia-southeast1-b us-east4-c
    * 2017-05-12: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b us-east4-a us-west1-c
  * v1.6.0 is no longer available for container cluster node upgrades/downgrades.



**Known Issues**

  * A known issue with Container Engine's [IP Rotation](https://docs.cloud.google.com/kubernetes-engine/docs/ip-rotation) feature can cause it to break Kubernetes features that depend on the proxy endpoint (such as `kubectl exec`, `kubectl logs`), as well as cluster metrics exports into Stackdriver. This issue only affects your cluster if you ran `CompleteIPRotation`, and have also disabled the default SSH firewall rule for cluster nodes. There is a simple manual fix; see [IP Rotation known issues](https://docs.cloud.google.com/kubernetes-engine/docs/ip-rotation#known_issues) for details.



## May 3, 2017

  * You can now use the [Google Cloud console](https://console.cloud.google.com/) to choose whether existing node pools should be automatically upgraded when a new Kubernetes version becomes available. See [Node Auto-Upgrade documentation](https://docs.cloud.google.com/kubernetes-engine/docs/node-auto-upgrade) for more information.
  * You can now use the [Google Cloud console](https://console.cloud.google.com/) to scale existing clusters running Kubernetes version 1.6.0 or later up to 5000 nodes in most zones.



## May 2, 2017

  * [Kubernetes v1.5.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v162) is the default version for new clusters. This version will be available for new clusters and opt-in master upgrades according to the following planned schedule: 
    * 2017-05-02: us-east1-d asia-northeast1-c
    * 2017-05-03: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a asia-southeast1-a us-east4-b
    * 2017-05-04: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b asia-southeast1-b us-east4-c
    * 2017-05-05: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b us-east4-a us-west1-c
  * Cluster masters running Kubernetes versions v1.6.0 and v.1.6.1 will be upgraded to [v1.6.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v162).



## April 26, 2017

  * [Kubernetes v1.6.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v162) This version will be available for new clusters and opt-in master upgrades.
  * You can create a cluster with HTTP basic authentication disabled by passing an empty username: `gcloud container clusters create CLUSTER_NAME --username=""` This feature only works with version 1.6.0 and later.
  * Fixed a bug where SetMasterAuth would fail silently on clusters below v1.6.0. SetMasterAuth is only allowed for clusters at v1.6.0 and above.
  * Fixed a bug for clusters at v1.6.0 and above where fluentd pods were mistakenly created on all nodes when logging was disabled.
  * gcloud `kubectl` version is now 1.6.2 instead of 1.6.0.



## April 12, 2017

  * [Kubernetes v1.6.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v161) This version will be available for new clusters and opt-in master upgrades according to the following planned schedule: 
    * 2017-04-12: us-east1-d asia-northeast1-c
    * 2017-04-13: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a
    * 2017-04-14: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b
    * 2017-04-17: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b
  * [Kubernetes v1.5.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v156) is still the default version for new clusters.
  * Container engine hosted masters will be upgraded to v1.5.6 according to the planned schedule mentioned above.
  * Known issue: 
    * `gcloud container clusters update --set-password` (or --generate-password), for setting or rotating your cluster admin password, does not work on clusters running Kubernetes version 1.5.x or earlier. Please use this method only on clusters running Kubernetes version 1.6.x or later.



## April 4, 2017

  * [Kubernetes v1.6.0](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v160) This version will be available for new clusters and opt-in master upgrades according to the following planned schedule: 
    * 2017-04-04: us-east1-d asia-northeast1-c
    * 2017-04-05: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a
    * 2017-04-06: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b
    * 2017-04-07: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b
  * [Kubernetes v1.5.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v156) is still the default version for new clusters.
  * [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) is now generally available. You can create or upgrade clusters and node pools that use Container-Optimized OS by specifying `imageType` values of either `COS` or `GCI`.
  * A new system daemon, node problem detector, is introduced in Kubernetes v1.6 on COS node images. It detects node problems (e.g. kernel/network/container runtime issues) and reports them as node conditions and events.
  * Starting in 1.6, a default StorageClass instance with the gce-pd provisioner is installed. All unbound PVCs that don't specify a StorageClass will automatically use the default provisioner, which is different behavior from previous releases and can be disabled by modifying the default StorageClass and removing the "storageclass.beta.kubernetes.io/is-default-class annotation". This feature replaces alpha dynamic provisioning, but the alpha annotation will still be allowed and will retain the same behavior.
  * `gcloud container clusters create|get-credentials` will now configure kubectl to use the credentials of the active gcloud account by default, instead of using application default credentials. This requires kubectl 1.6.0 or higher. You can update kubectl by running `gcloud components update kubectl`. If you prefer to use application default credentials to authenticate kubectl to Google Container Engine clusters, you can revert to the previous behavior by setting the `container/use_application_default_credentials` property: 
    * `gcloud config set container/use_application_default_credentials true`
    * `export CLOUDSDK_CONTAINER_USE_APPLICATION_DEFAULT_CREDENTIALS=true`
  * Google Cloud CLI kubectl version updating to 1.6.0.
  * New clusters launched at 1.6.0 will use be using etcd3 in the master. Existing cluster masters will be automatically updated to use etcd3 in a future release.
  * Starting in 1.6, [RBAC](https://kubernetes.io/docs/admin/authorization/rbac/) can be used to grant permissions for users and Service Accounts to the cluster's API. To help transition to using RBAC, the cluster's legacy authorization permissions are enabled by default, allowing Kubernetes Service Accounts full access to the API like they had in previous versions of Kubernetes. An option will be rolled out soon to allow the legacy authorization mode to be disabled in order to take full advantage of RBAC.
  * You can now use gcloud to set or rotate the admin password for Container clusters by running 
    * `gcloud container clusters update --set-password`
    * `gcloud container clusters update --generate-password`
  * During node upgrades, Container Engine will now verify and recreate the Managed Instance Group for a node pool (at size 0) if required.



## March 29, 2017

  * [Kubernetes v1.5.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v156) is the default version for new clusters. This version will be available for new clusters and opt-in master upgrades according to the following planned schedule:

    * 2017-03-29: us-east1-d asia-northeast1-c
    * 2017-03-30: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a
    * 2017-03-31: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b
    * 2017-04-03: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b
  * Cluster and node pool create requests will return a 4xx error (instead of 5xx) if an invalid service account is specified.

  * Return a more accurate error message for cluster requests if the Container API is not enabled.




## March 20, 2017

  * Update Google Container Engine's kubectl from version 1.5.3 to 1.5.4.
  * Container engine hosted masters will be upgraded to v1.5.4 according to the following planned schedule: 
    * 2017-03-23: us-east1-d asia-northeast1-c
    * 2017-03-24: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a
    * 2017-03-27: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b
    * 2017-03-28: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b



## March 16, 2017

  * [Kubernetes v1.5.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v154) is the default version for new clusters.
  * Added `--enable-autorepair` flag to `gcloud beta container clusters create`, `gcloud beta container node-pools create` and `gcloud beta container node-pools update`



## March 6, 2017

  * Container Engine node auto-repair now available in Beta. For more information, see https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair
  * [Google Cloud console](https://console.cloud.google.com/) now allows enabling automatic repair for new clusters and node pools.



## March 1, 2017

  * Container Engine hosted masters

    * running v1.4 will be upgraded to v1.4.9.
    * running v1.5 will be upgraded to v1.5.3.

according to the following planned schedule:

    * 2017-03-02: us-east1-d asia-northeast1-c
    * 2017-03-03: europe-west1-c us-central1-b us-west1-a asia-east1-a asia-northeast1-a
    * 2017-03-06: us-central1-f europe-west1-b asia-east1-c us-east1-c us-west1-b asia-northeast1-b
    * 2017-03-07: us-central1-a us-central1-c europe-west1-d asia-east1-b us-east1-b



## February 23, 2017

  * [Kubernetes v1.5.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v153) is the default version for new clusters.
  * Google Cloud CLI kubectl version updating to 1.5.3.



## February 14, 2017

  * It is no longer necessary to disable the HttpLoadBalancing add-on when you create a cluster without adding the compute read/write scope to nodes. Previously, when you created a cluster without adding the compute read/write scope, you were required to disable HttpLoadBalacing.



## January 31, 2017

  * Google Cloud CLI kubectl version updating to 1.5.2.



## January 26, 2017

  * [Kubernetes v1.5.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v152) is the default version for new clusters.

  * The Google Cloud CLI and kubectl 1.5+ support using `gcloud` credentials for authentication. Currently, `gcloud container clusters create` and `gcloud container clusters get-credentials` configure kubectl to use [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) to authenticate to Container Clusters. If these differ from the Identity and Access Management (IAM) role that the Google Cloud CLI is using, kubectl requests can fail authentication (#[30617](https://github.com/kubernetes/kubernetes/issues/30617)). With Google gcloud CLI 140.0.0 and kubectl 1.5+, the Google Cloud CLI can configure kubectl to use its own credentials. This means that if, e.g., the `gcloud` command-line is configured to use a service account, kubectl will authenticate as the same service account.

To enable using the Google Cloud CLI's own credentials, set the `container/use_application_default_credentials` property to false:
        
        export CLOUDSDK_CONTAINER_USE_APPLICATION_DEFAULT_CREDENTIALS=false
        # or
        gcloud config set container/use_application_default_credentials false
        

The current default behavior is to continue using application default credentials. The Google Cloud CLI credentials will be made the default for kubectl configuration (via `gcloud container clusters create|get-credentials`) in a future release.




## January 17, 2017

  * [Kubernetes v1.4.8](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v148) is the default version for new clusters.

  * [Kubernetes v1.5.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v152) is available for new clusters.




## January 10, 2017

  * Rollout of Kubernetes v1.5 as the default for new clusters is postponed until v1.5.2 to fix known issues with v1.5.1.

  * Fixed an issue where Node Upgrades would fail if one of the nodes was not registered with the Master.

  * Google Cloud CLI kubectl version updating to 1.5.1.




**Known Issues with Kubernetes v1.5.1**

  * [#39680](https://github.com/kubernetes/kubernetes/issues/39680) Defining a pod with a resource request of 0 will cause Controller Manager to crashloop.

  * [#38322](https://github.com/kubernetes/kubernetes/issues/38322) Kubelet can evict or refuse to admit critical pods (kube-proxy, static pods) when under memory pressure.




## January 4, 2017

  * Default cluster version for new clusters will be changed to [Kubernetes v1.5.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v151) in the week of January 9th.



## January 3, 2017

  * [Google Cloud console](https://console.cloud.google.com/) now allows setting newly created clusters and node pools to automatically upgrade when a new Kubernetes version becomes available. See [documentation](https://docs.cloud.google.com/kubernetes-engine/docs/node-management) for details.



## December 14, 2016

  * [Kubernetes v1.4.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v147) is the default version for new clusters.
  * [Kubernetes v1.5.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v151) is available for new clusters.
  * Node pools can now opt in to automatically upgrade when a new Kubernetes version becomes available. See [documentation](https://docs.cloud.google.com/kubernetes-engine/docs/node-management) for details.
  * Node pool upgrades can now be rolled back using the `gcloud alpha container node-pools rollback <pool-name>` command. See `gcloud alpha container node-pools rollback --help` for more details.



## December 7, 2016

  * [Google Cloud console](https://console.cloud.google.com/) now allows choosing between Container-VM Image (GCI) and the deprecated container-vm when adding new node pools to existing clusters. To learn more about image types, click [here](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).



## December 5, 2016

  * Container Engine hosted masters running v1.4 will be upgraded to v1.4.6.



## November 29, 2016

  * Increase master disk size in large Google Container Engine clusters. This is needed as in large clusters etcd needs much more IOPS.

  * Change the `gcloud container list-tags` command to support user-specified filters on occurrences and exposes a column summarizing vulnerability information.




## November 15, 2016

  * [Kubernetes v1.4.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v146) is the default version for new clusters.



## November 8, 2016

  * Container Engine hosted masters running v1.4 have been upgraded to v1.4.5.

  * Container Engine hosted masters running v1.3 will be upgraded to v1.4.5 according to the following planned schedule:

    * 2016-11-09: us-east1-d
    * 2016-11-10: asia-east1-a, asia-northeast1-a, europe-west1-c, us-central1-b, us-west1-a
    * 2016-11-11: asia-east1-c, asia-northeast1-b, europe-west1-b, us-central1-f, us-east1-c, us-west1-b
    * 2016-11-14: asia-east1-b, asia-northeast1-c, europe-west1-d, us-central1-a, us-central1-c, us-east1-b



## November 7, 2016

  * [Google Cloud console](https://console.cloud.google.com/) now allows creating temporary clusters with [Kubernetes alpha features](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) enabled.



## November 2, 2016

  * [Google Cloud console](https://console.cloud.google.com/) now allows choosing between Container-VM Image (GCI) and the deprecated container-vm on cluster creation. To learn more about image types, click [here](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

  * [Google Cloud console](https://console.cloud.google.com/) supports [Cluster Autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) on creating clusters, node pools, and editing existing node pools.

  * [Google Cloud console](https://console.cloud.google.com/) now allows specifying boot disk size of node VMs.




## November 1, 2016

  * [Kubernetes v1.4.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v145) is the default version for new clusters.

  * Kubernetes v1.4.5 and v1.3.10 include fixes for CVE-2016-5195 (Dirty Cow), which is a Linux kernel vulnerability that allows privilege escalation. If your clusters are running nodes with lower versions, we strongly encourage you to upgrade them to a version of Kubernetes that includes a node image that is not vulnerable, such as Kubernetes 1.3.10 or 1.4.5. To upgrade a cluster, see https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster.

  * Upgrade operations can now be cancelled using `gcloud alpha container operations cancel <operation_id>`. See `gcloud alpha container operations cancel --help` for more details.




## October 17, 2016

  * [Kubernetes v1.4.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v143) is the default version for new clusters.

  * Reminder that the base OS image for nodes has changed in the 1.4 release. A set of known issues have been identified and have been documented [here](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#limitations). If you suspect that your application or workflow is having problems with new clusters, you may select the old ContainerVM by following the opt-out instructions documented [here](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#opt-out).

  * Rewrote the node upgrade logic to make it less disruptive by waiting for the node to register with the Kubernetes master before upgrading the next node.

  * Added support for new clusters and node-pools to use preemptible VM instances by using the `--preemptible` flag. See `gcloud beta container clusters create --help` and `gcloud beta container node-pools create --help` for more details.




## October 10, 2016

  * [Kubernetes v1.4.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v141) is becoming the default version for new clusters.

  * Reminder that the base OS image for nodes has changed in the 1.4 release. A set of known issues have been identified and have been documented [here](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#limitations). If you suspect that your application or workflow is having problems with new clusters, you may select the old ContainerVM by following the opt-out instructions documented [here](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#opt-out).

  * Fix a bug in `gcloud beta container images list-tags`.

  * Add support for kubernetes labels on new clusters and nodepools by passing `--node-labels=label1=value1,label2=value2...`. See `gcloud container clusters create --help` and `gcloud container nodepools create --help` for more details and examples.

  * Update kubectl to version 1.4.1.




## October 5, 2016

  * Can now specify the cluster-version when creating Google Container Engine clusters.

  * Update kubectl to version 1.4.0.

  * Introduce 1.3.8 as a valid cluster version. 1.3.8 fixes a log rotation leak on the master.




## September 27, 2016

  * [Kubernetes v1.4.0](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v140) is becoming the default version for new clusters.

  * Container-VM Image (GCI), which was introduced earlier this year, is now the default ImageType for new clusters and node-pools. The old container-vm is now deprecated; it will be supported for a limited time. To learn more about how to use GCI, click [here](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

  * Can now create temporary clusters with all kubernetes alpha features enabled via
        
        gcloud alpha container clusters create --enable-kubernetes-alpha
        

See [documentation](https://docs.cloud.google.com/kubernetes-engine/docs/alpha-clusters) for details.

  * Can now add custom kubernetes labels on new clusters and nodepools. via
        
        gcloud alpha container clusters create --node-labels=key1=value1,key2=value2...
        

See `gcloud alpha container clusters create --help` for details.




**Known Issues with v1.4.0 masters and older nodes**

  * init-containers are now supported on Container Engine, but only when master and nodes are running 1.4.0 or higher. Other configurations are not supported.

  * Customers manually upgrading masters to 1.4 should be aware that the lowest node version supported with it is 1.2.




## September 20, 2016

  * Container Engine hosted masters will be upgraded to v1.3.7 in zones according to the following planned schedule:

    * 2016-09-21: us-east1-d
    * 2016-09-22: asia-east1-a, europe-west1-c, us-central1-b, us-west1-a
    * 2016-09-23: asia-east1-c, europe-west1-b, us-central1-f, us-east1-c, us-west1-b
    * 2016-09-26: asia-east1-b, europe-west1-d, us-central1-a, us-central1-c, us-east1-b
  * Google Cloud CLI kubectl version updated to v1.3.7




## September 15, 2016

  * [Kubernetes v1.3.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v137) is the default version for new clusters.

  * Container Engine hosted masters have been upgraded to v1.3.6.

  * **Known Issues with v1.3.6 fixed in v1.3.7**

    * [#32415](https://github.com/kubernetes/kubernetes/issues/32415) Fixes a bug in kubelet hostport logic which flushes KUBE-MARK-MASQ iptables chain.

    * [#30790](https://github.com/kubernetes/kubernetes/issues/30790) Fixes the panic that occurs in the federation controller manager when registering a Container Engine cluster to the federation.




## September 6, 2016

  * Cluster update to add node locations (API: `rest/v1/projects.zones.clusters/update`, CLI: `gcloud beta container clusters update --additional-zones`) will now wait for all nodes to be healthy before marking operation completed (`DONE`).



## August 30, 2016

  * [Kubernetes v1.3.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v135) is the default version for new clusters.

  * **Known Issues with v1.3.5 fixed in v1.3.6**

    * [#27653](https://github.com/kubernetes/kubernetes/issues/27653) Volume manager should be more robust across restarts.

    * [#29997](https://github.com/kubernetes/kubernetes/issues/29997) loadBalancerSourceRanges does not work on Container Engine.

  * **Known Issues with older versions fixed in v1.3.6**

    * [#31219](https://github.com/kubernetes/kubernetes/issues/31219) Graceful termination fails if terminationGracePeriodSeconds > 2

    * [#30828](https://github.com/kubernetes/kubernetes/pull/30828) Netsplit causes pods to get stuck in NotReady for < 1.2 nodes

    * [#29358](https://github.com/kubernetes/kubernetes/issues/29358) Google Compute Engine PD Detach fails if node no longer exists.

  * `cluster.master_auth.password` is no longer required in a `clusters.create` request. If a password is not specified for a cluster, one will be generated.

  * Google Cloud CLI kubectl version updated to v1.3.5

  * Image Type selection for `gcloud container` commands is now GA. Can now use `gcloud container clusters create --image-type=...` `gcloud container clusters upgrade --image-type=...`




## August 17, 2016

  * [Kubernetes v1.3.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v135) is the default version for new clusters.

  * Google Cloud CLI changed the `container/use_client_certificate` property default value to `false`. This makes the `gcloud container clusters create` and `gcloud container clusters get-credentials` commands configure `kubectl` to use Google OAuth2 credentials by default instead of the legacy client certificate.




## August 8, 2016

  * [Kubernetes v1.3.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v134) is the default version for new clusters.

  * Google Cloud CLI kubectl version updated to v1.3.3.




## July 29, 2016

  * [Kubernetes v1.3.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v133) is the default version for new clusters.



## July 22, 2016

  * [Kubernetes v1.3.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v132) is the default version for new clusters.

  * 1.3.0 clusters have been upgraded to 1.3.2 to pick up the fix for bad route creation.

  * Fixed the issues where clusters with a non-default master auth username were unable to authenticate using HTTP Basic Auth.

  * The DNS Replica Auto-Sizer now creates a minimum of 2 replicas except for single node clusters.

  * Google Cloud CLI kubectl version updated to v1.2.5.

  * [Google Cloud console](https://console.cloud.google.com/) now supports CIDR ranges with mask sizes from /8 to /19 on cluster creation.

  * [Google Cloud console](https://console.cloud.google.com/) now supports specifying additional zones on cluster creation.

  * [Google Cloud console](https://console.cloud.google.com/) now supports creating clusters with up to 2000 nodes (across multiple node pools).

  * [Google Cloud console](https://console.cloud.google.com/) now supports specifying a local SSD count on cluster creation and while creating and editing node pools.

  * **Known Issues**

    * [#29051](https://github.com/kubernetes/kubernetes/issues/29051) PVC Volume not detached if pod deleted via namespace. deletion.

    * [#29358](https://github.com/kubernetes/kubernetes/issues/29358) Google Compute Engine PD Detach fails if node no longer exists.

    * [#28616](https://github.com/kubernetes/kubernetes/issues/28616) Mounting (only 'default-token') volume takes a long time when creating a batch of pods (parallelization issue).

    * [#28750](https://github.com/kubernetes/kubernetes/issues/28750) Error while tearing down pod, "device or resource busy" on service account secret.




## July 11, 2016

  * [Kubernetes v1.3.0](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v130) is becoming the default version for new clusters.

  * Existing Google Container Engine cluster masters were upgraded to [Kubernetes v1.2.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md/#v125) over the previous week.

  * Improved error messages when a cluster is already being operated on.

  * Now supports creating clusters and node pools with local SSDs attached to nodes. See [Container Cluster Operations](https://docs.cloud.google.com/kubernetes-engine/docs/clusters/operations#create_a_cluster_with_local_ssd_nodes) for examples.

  * Cluster autoscaling is now available for clusters running v1.3.0. Autoscaling options can be specified on cluster create and update. See [Container Cluster Operations](https://docs.cloud.google.com/kubernetes-engine/docs/clusters/operations#create_a_cluster_with_autoscaling) for examples.

  * Existing single-zone clusters can now be updated to multi-zone clusters by running `gcloud beta container clusters update --additional zones`. See [Container Cluster Operations](https://docs.cloud.google.com/kubernetes-engine/docs/clusters/operations#update_a_running_cluster_to_multi_zone) for examples.

  * **Known issues** :

    * Scaling v1.3.0 clusters after creation (including via cluster autoscaling) can cause bad routes to be created with colliding target CIDRs. Bad routes can be detected and manually fixed via following
          
          * 1. List routes with duplicate destination ranges
           gcloud compute routes list --filter="name ~ gke-$CLUSTER_NAME" --format='value(destRange)' | uniq -d
          

If the above returns any values, the bad routes can be fixed by deleting one of the target instances. A new one will be automatically recreated with a working route.
          
          * 2. Replace $DUPE_RANGE with a destination range from 1.
           gcloud compute routes list --filter="destRange:$DUPE_RANGE"
          
           * 3. Delete one of the target instances listed by 2.
           gcloud compute instances delete $TARGET_INSTANCE
          

    * kubectl authorization for v1.3.0 clusters fails if a the cluster is created with a non-default master auth username (`gcloud container clusters create --username ...`). This can be worked around by authenticating with the cluster certificate instead by running

`kubectl config unset users.gke_$PROJECT_$ZONE_$NAME.username`

on the machine from which you want to run `kubectl`, where `$PROJECT,$ZONE,$NAME` are the cluster's project id, zone and name, respectively.




## July 1, 2016

  * Kubernetes [v1.2.5](https://github.com/kubernetes/kubernetes/releases/tag/v1.2.5) is the default version for new clusters.

  * Fixed a bug where [Google Cloud console](https://console.cloud.google.com/) didn't properly render clusters with no node pools.

  * [Google Cloud console](https://console.cloud.google.com/) supports editing clusters with no node pools.




## June 20, 2016

  * [Google Cloud console](https://console.cloud.google.com/) supports creation and deletion of node pools.

  * (Breaking change) The `--wait` flag for the `gcloud container clusters` command group is now deprecated; please use the `--async` flag instead.




## June 13, 2016

  * Bug fixes.



## June 7, 2016

  * Fixed a bug where `kubectl` for the wrong architecture was installed on Windows. We now install 32- and 64-bit.

  * [Google Cloud console](https://console.cloud.google.com/) supports resizing and upgrading node pools.




## June 3, 2016

  * Bug fixes.



## May 27, 2016

  * `gcloud container clusters update` command is now available for updating cluster settings of an existing container cluster.

  * The `gcloud container node-pools` commands are now available for creating deleting, describing and listing node pools of a cluster.

  * [Google Cloud console](https://console.cloud.google.com/) supports listing node pools. Listed node pools can also be upgraded/downgraded to supported Kubernetes versions.




## May 18, 2016

  * `gcloud alpha container` commands (e.g. create) now support specifying alternate ImageTypes, such as the newly-available Beta [Container-VM Image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images). To try it out, update to the latest gcloud (`gcloud components install alpha ; gcloud components update`) and then create a new cluster: `gcloud alpha container clusters create --image-type=GCI $NAME`. Support for ImageTypes in Google Cloud console will follow at a later date.

  * The `gcloud container clusters list` command now sorts the clusters based on zone and then on cluster name.

  * The `gcloud container clusters create` command now allows specifying `--max-nodes-per-pool` (default 1000) to create multiple node pools for large clusters.




## May 16, 2016

  * Container Engine hosted masters have been upgraded to v1.2.4.

  * Google Cloud CLI `kubectl` version updated to v.1.2.4.

  * CreateCluster calls now accept multiple NodePool objects.




## May 6, 2016

  * Container Engine hosted masters have been upgraded to v1.2.3.

  * Google Cloud CLI `kubectl` version updated to v1.2.3




## April 29, 2016

  * Kubernetes [v1.2.3](https://github.com/kubernetes/kubernetes/releases/tag/v1.2.3) is the default version for new clusters.

  * `gcloud container clusters resize` now allows specifying a node pool via `--node-pool`.




## April 21, 2016

  * Can now create a multi-zone cluster, which is a cluster whose nodes span multiple zones, enabling higher availability of applications running in the cluster. More details on multi-zone clusters can be found at http://kubernetes.io/docs/admin/multiple-zones/. The ability to convert existing clusters to be multi-zone will be coming soon.

  * `gcloud container clusters create` now allows specifying multiple zones within a region for your cluster's nodes to be created in by using the `--additional-zones` flag.

  * Fixed bug that caused `kubectl` component to be missing from gcloud components list on Windows.

  * Google Cloud CLI `kubectl` version updated to v1.2.2




## April 13, 2016

  * Known issue: the "[bastion route](http://stackoverflow.com/questions/31664060/how-to-call-a-service-exposed-by-a-kubernetes-cluster-from-another-kubernetes-cl/31665248#31665248)" workaround for accessing services from outside of a kubernetes cluster no longer works with 1.2.0 - 1.2.2 nodes, due to a change in kube-proxy. If you are using this workaround, we recommend not upgrading nodes to 1.2.x at this time. This will be addressed in a future patch release.



## April 11, 2016

  * Kubernetes [v1.2.2](https://github.com/kubernetes/kubernetes/releases/tag/v1.2.2) is the default version for new clusters.

  * `gcloud alpha container clusters update` now allows enabling/disabling addons for Container Engine clusters via `--update-addons` flag.

  * `gcloud container clusters create` now supports disabling HPA and Ingress controller addons via `--disable-addons` flag.

  * [Google Cloud console](https://console.cloud.google.com/) supports "Google Kubernetes Engine master upgrade" option, which allows proactive upgrade of cluster masters. Note this is the same functionality available via `gcloud container clusters upgrade --master`.




## April 4, 2016

  * Kubernetes [v1.2.1](https://github.com/kubernetes/kubernetes/releases/tag/v1.2.1) is the default version for new clusters.



## March 29, 2016

  * The API Discovery Doc and Client Libraries have been updated.

  * `gcloud container clusters create|get-credentials` will warn|fail respectively if the HOME env var isn't set. The variable is required to store kubectl credentials (kubeconfig).

  * Google Cloud CLI `kubectl` component is now available for Windows.




## March 21, 2016

  * Kubernetes [v1.2.0](https://github.com/kubernetes/kubernetes/releases/tag/v1.2.0) is the default version for new clusters. This update contains significant changes from v1.1, described in detail at [releases-1.2.0](https://github.com/kubernetes/kubernetes/releases/tag/v1.2.0). Major changes include

    * Increased cluster scale by 400% to 1000 nodes with 30,000 pods per cluster.
    * Kubelet supports 100 pods per node with 4x reduced system overhead.
    * Deployment and DaemonSet API now Beta. Job and HorizontalPodAutoscaler APIs moved from Beta to GA.
    * Ingress supports HTTPS.
    * Kube-Proxy now defaults to an iptables-based proxy.
    * Docker v1.9.1.
    * Dynamic configuration for applications via ConfigMap API provides alternative to baking in commandline flags when building container.
    * New kubernetes GUI that enables the same functionality as CLI.
    * Graceful node shutdown via `kubectl drain` command to gracefully evict pods from nodes.
  * Access scopes [service.management](https://www.googleapis.com/auth/service.management) and [servicecontrol](https://www.googleapis.com/auth/servicecontrol) are now enabled by default for new Container Engine clusters

  * Clusters created without compute read/write node scopes must also disable [HttpLoadBalancing](https://cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters#HttpLoadBalancing). Note that disabling compute read/write is only possible via the raw API, not the Google Cloud CLI or the [Google Cloud console](https://console.cloud.google.com/).

  * ClusterUpdates to clusters whose node scopes do not have compute read/write must also specify an AddonsConfig with [HttpLoadBalancing](https://cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters#HttpLoadBalancing) disabled.

  * Google Cloud CLI `kubectl` version updated to 1.2.0.




## March 16, 2016

  * CreateCluster will now succeed if the kubernetes API reports at least 99% of nodes have registered and are healthy within a startup deadline.

  * `gcloud container clusters create` prints a warning if cluster creation finished with > 99% but < 100% of nodes registered/healthy.




## March 2, 2016

  * Container Engine hosted master upgrades from v1.1.7 to v1.1.8 were completed this week.



## February 26, 2016

  * Kubernetes [v1.1.8](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.1.8) is the default version for new clusters.

  * DeleteCluster will fail fast with an error if there are backend services that target the cluster's node group, as existence of such services will block deletion of the nodes.

  * You can now self-initiate an upgrade of a cluster's hosted master to the latest supported Kubernetes version by running `gcloud container clusters upgrade --master`. This lets you access versions ahead of automatic Container Engine hosted master upgrades.




## February 10, 2016

  * Container Engine hosted master upgrades from v1.1.3, v1.1.4 to v1.1.7 were completed this week.

  * Google Cloud CLI `kubectl` version is 1.1.7.




## January 28, 2016

  * Kubernetes [v1.1.7](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.1.7) is the default version for new clusters.



## January 15, 2016

  * Kubernetes [v1.1.4](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.1.4) is the default version for new clusters.

  * Can now run `gcloud container clusters resize` to resize Container Engine clusters.

  * `gcloud container clusters` `describe` and `list` now notify the user when a node upgrade is available.

  * Google Cloud CLI `kubectl` version is 1.1.3.




## January 5, 2016

  * Fixed an issue where [Google Cloud console](https://console.cloud.google.com/) incorrectly disallowed users from creating clusters with Cloud Monitoring enabled.

  * Fixed an issue where users could not create clusters in domain-scoped projects.




## December 8, 2015

  * Kubernetes [v1.1.3](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.1.3) is the default version for new clusters.

  * Added support for custom machine types.

  * Create cluster now checks that the network for the cluster has a route to the default internet gateway. If no such route exists, the request returns with an error immediately, instead of timing out waiting for the nodes to register.

  * [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) now prompts for confirmation.




## December 3, 2015

  * The Google Container Engine v1beta1 API, which was previously deprecated, is now disabled.

  * Container Engine hosted masters were upgraded to v1.1.2 this week, except for clusters with nodes older than v1.0.1, which will be upgraded once v1.1.3 is available.




## November 30, 2015

  * Kubernetes [v1.1.2](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.1.2) is the default version for new clusters.

  * Container Engine now supports manual-subnet networks. Subnetworks are an Alpha feature of Google Compute Engine and you must be whitelisted to use them. See the [Subnetworks](https://docs.cloud.google.com/compute/docs/subnetworks) documentation for whitelist information.

Once whitelisted, the [subnetwork](https://docs.cloud.google.com/compute/docs/subnetworks) is specified in the cluster create request. In the REST API, this is specified as the value of the `subnetwork` field of the [cluster object](https://docs.cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters); when using `gcloud container` commands, pass a `--subnetwork` flag to [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create).

  * Improved reliability of cluster creation and deletion.




## November 18, 2015

  * `kubectl` version is 1.1.1.

  * New API options for disabling the [HTTP load balancer controller](https://docs.cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters#HttpLoadBalancing) and [horizontal pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters#HorizontalPodAutoscaling).




## November 12, 2015

The release documented below is being rolled out over the next few days.

  * Clusters can now be created with up to 250 nodes.

  * The Google Compute Engine load balancer controller addon is added by default to new clusters. [Learn more](https://github.com/kubernetes/kubernetes/blob/master/cluster/addons/cluster-loadbalancing/glbc/README.md).

  * Kubernetes [v1.1.1](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.1.1) is the default version for new clusters.

_Important Note:_ The packaged `kubectl` is version 1.0.7, consequently new Kubernetes 1.1 APIs like autoscaling will not be available via `kubectl` until next week's push of the `kubectl` binary.

Users who want access before then can manually download a 1.1 `kubectl` from:

    * [Linux](https://storage.googleapis.com/kubernetes-release/release/v1.1.1/bin/linux/amd64/kubectl)
    * [OS X](https://storage.googleapis.com/kubernetes-release/release/v1.1.1/bin/darwin/amd64/kubectl)

And then `chmod a+x kubectl; cp kubectl $(which kubectl)` to install it.

  * Kubernetes v0.19.3 and v0.21.4 are no longer supported for nodes.

  * New clusters using the `f1-micro` machine type must contain at least three nodes. This ensures that there is enough memory in the cluster to run more than just a couple of very small pods.

  * `kubectl` version is 1.0.7.




## November 4, 2015

  * Kubernetes [v1.0.7](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.0.7) is the default version for new clusters.

  * Existing clusters will have their masters upgraded from v1.0.6 to v1.0.7 over the coming week.

  * Added support for [subnetworks](https://docs.cloud.google.com/compute/docs/subnetworks#alpha_restrictions) (Alpha).




## October 27, 2015

  * Added a `detail` field to operation objects to show progress details for long-running operations (such as cluster updates).

  * Better categorization of errors caused by projects not being fully initialized with the default service accounts.




## October 19, 2015

  * The `--container-ipv4-cidr` flag has been deprecated in favor of `--cluster-ipv4-cidr`.

  * The current node count of Container Engine clusters is available from the REST API.

  * Metrics in Cloud Monitoring are now available with a much shorter delay.

  * Cluster names now only need to be unique within each zone, not within the entire project.

  * Error messages involving regular expressions have more useful, human-readable hints.




## October 12, 2015

  * You can now specify custom metadata to be added to the nodes when creating a cluster with the [REST API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/create).



## September 25, 2015

  * Cluster self links now contain the project ID rather than the project number.

  * `kubectl` version is 1.0.6.




## September 18, 2015

  * Kubernetes [v1.0.6](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.0.6) is the default version for new clusters.

  * Existing clusters will have their masters upgraded from v1.0.4 to v1.0.6 over the coming week.




## September 4, 2015

  * Fixed a bug where a `CreateCluster` request would be rejected if it contained a `ClusterApiVersion`. Since the field is output-only, it is now silently ignored.



## August 31, 2015

  * To avoid creating clusters without any space for non-system containers, there are now limits on clusters consisting of f1-micro instances:

    * A single-node f1-micro cluster must disable both logging and monitoring.
    * A two-node f1-micro cluster must disable at least one of logging and monitoring.



## August 26, 2015

Google Container Engine is out of beta.

  * All `gcloud beta container` commands are now in the `gcloud container` command group instead.

  * You can now use the Google Container Engine API to enable or disable Google Cloud Monitoring on your cluster. Use the [`desiredMonitoringService` field of the cluster update method](https://docs.cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters/update). When updating this field, the Kubernetes apiserver will be see a brief outage as the master is updated.




## August 14, 2015

  * Kubernetes [v1.0.3](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.0.3) is the default version for new clusters.

  * The `compute` and `devstorage.read_only` auth scopes are no longer required and are no longer automatically added server-side to new clusters. The `gcloud` command and Google Cloud console still add these scopes on the client side when creating new clusters; the REST API does not.

  * Listing container clusters in a non-existent zone now results in a `404: Not Found` error instead of an empty list.

  * The `get-credentials` command has moved to `gcloud beta container clusters get-credentials`. Running `gcloud beta container get-credentials` prints an error redirecting to the new location.

  * The new `gcloud beta container get-server-config` command returns:

    * The default Kubernetes version currently used for new clusters.
    * The list of supported versions for node upgrades (via `gcloud beta container clusters upgrade`).



## August 4, 2015

  * Kubernetes [v1.0.1](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v1.0.1) is the default version for new clusters.

  * `kubectl` version is 1.0.1.

  * Removed the v1beta1 API discovery doc in preparation for deprecation.

  * The `gcloud alpha container` commands target the Container Engine v1 API. The options for `gcloud alpha container clusters create` have been updated accordingly:

    * `--user` renamed `--username`.
    * `--cluster-api-version` removed. Cluster version not selectable in v1 API; new clusters always created at latest supported version.
    * `--image` option removed. Source image not selectable in v1 API; clusters are always created with latest supported ContainerVM image. Note that using an unsupported image (i.e. not ContainerVM) would result in an unusable cluster in most cases anyway.
    * Added `--no-enable-cloud-monitoring` to turn off cloud monitoring (on by default).
    * Added `--disk-size` option for specifying boot disk size of node VMs.



## July 27, 2015

  * A firewall rule is now created at the time of cluster creation to make node VMs accessible via SSH. This ensures that the Kubernetes proxy functionality works.

  * Updated the admission controllers list to match the [recommended list for v1.0](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#is-there-a-recommended-set-of-admission-controllers-to-use).

  * Disabled the `--source-image` option in the v1beta1 API. Attempting to run `gcloud alpha container clusters create --source-image` now returns an error.

  * Removed the option to create clusters in the 172.16.0.0/12 private IP block.




## July 24, 2015

**Upgrade to Kubernetes v1 - Action Required**

Users must upgrade their configuration files to the v1 Kubernetes API before August 5th, 2015. This applies to any Beta Container Engine cluster created before July 21st. 

Google Container Engine will upgrade container cluster masters beginning on August 5th, to use the v1 Kubernetes API. If you'd like to upgrade prior, please [sign up for an early upgrade](https://docs.google.com/forms/d/1dY4h5uuNwnYOM11k17FqDCnyBXpq7VdFEEkLYG4v7Jk/viewform).

This upgrade removes support for the v1beta3 API. All configuration files must be formatted according to the v1 specification to ensure that your cluster remains functional. The v1 API represents the production-ready set of APIs for Kubernetes and Container Engine.

Some helpful resources are:

  * An [upgrade script](https://v1-18.docs.kubernetes.io/docs/tasks/administer-cluster/cluster-management/#switching-your-config-files-to-a-new-api-version) to convert your v1beta3 configuration files to v1.

  * The official [v1 specification reference](http://kubernetes.io/third_party/swagger-ui/).




If your configuration files already use the v1 specification, no action is required.

## July 15, 2015

  * Kubernetes [v0.21.2](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.21.2) is the default version for new clusters.

  * Existing masters running versions 0.19.3 or higher will be upgraded to 0.21.2. Customers should [upgrade their container clusters](https://docs.cloud.google.com/kubernetes-engine/docs/clusters/upgrade) at their convenience. Clusters running versions older than 0.19.3 can not be updated.

  * The `kubectl` version is now 0.20.2.




## July 10, 2015

  * Kubernetes [v0.21.1](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.21.1) is the default version for new clusters.

  * The `kubectl` version is now 0.20.1.




Known issue:

  * The `rolling-update` command will fail when using `kubectl` v0.20.1 with clusters running v0.19.3 of the Kubernetes API. To resolve the issue, specify `--api-version=v1beta3` as a flag to the `rolling-update` command:
        
        kubectl rolling-update --api-version=v1beta3 --image=<foo> ...
        

To find your version of `kubectl`:
        
        kubectl version
        

To find your cluster version:
        
        gcloud container clusters describe CLUSTER_NAME
        




## June 25, 2015

  * The Google [Container Engine REST API](https://docs.cloud.google.com/kubernetes-engine/reference/rest) has been updated to v1.

  * The REST API returns a more accurate error message when the region is out of quota.

  * `gcloud container clusters create` supports specifying disk size for nodes with the `--disk-size` flag.




## June 22, 2015

  * Google Container Engine is now in Beta.

  * Kubernetes master VMs are no longer created for new clusters. They are now run as a hosted service. There is no Compute Engine instance charge for the hosted master. Read more about [pricing details](https://cloud.google.com/kubernetes-engine/pricing).

  * Kubernetes [v0.19.3](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.19.3) is the default version for new clusters.

  * For projects with default regional Compute Engine CPUs quota, container clusters are limited to 3 per region.

  * Documentation updated to use `gcloud beta` command group.

  * Documentation updated to use `apiVersion: v1` in all samples.




Known issue:

  * `kubectl exec` is broken for cluster version 0.19.3.



## June 10, 2015

  * Documentation updated to use v1beta3.

  * Kubernetes [v0.18.2](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.18.2) is the default version for new clusters.




## June 3, 2015

  * Kubernetes [v0.18.0](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.18.0) is the default version for new clusters.

  * Clusters launched with 0.18.0 and above are deployed using Managed Instance Groups.

  * New clusters can no longer be created at v0.16.0.

  * Fixed a race condition that could cause routes to be leaked on cluster deletion.

  * Fail faster and with a helpful message if the project is lacking specific resource quota to create a functioning cluster.




Google Cloud CLI:

  * The `gcloud alpha container clusters create` command always sets `kubectl`'s current context to the newly created cluster.

  * The `clusters create` and `get-credentials` commands look for and write `kubectl` configuration to a `KUBECONFIG` environment variable. This matches the behavior of `kubectl config *` commands.

  * The `gcloud alpha container kubectl` command is disabled. Use simply `kubectl` instead.




## May 22, 2015

  * Kubernetes [v0.17.1](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.17.1) is the default version for new clusters.

  * Kubernetes v0.16.0 is still supported. However, new clusters can no longer be created at Kubernetes v0.17.0 due to the bug listed below.

  * Fixes a bug that was preventing containers from accessing the Google Compute Engine metadata service.

  * Kubernetes service DNS names are now suffixed with `.<namespace>.svc.cluster.local` instead of `.<namespace>.kubernetes.local`.




kubectl 0.17.0 notes:

  * Updated `kubectl cluster-info` to show v1beta3 addresses.

  * Add `kubectl log --previous` support to view last terminated container log.

  * Added displaying external IPs to `kubectl cluster-info`.

  * Print container statuses in `kubectl get pods`.

  * Add `kubectl_label` to custom functions in bash completion.

  * Change `IP` to `IP(S)` in service columns for `kubectl get`.

  * Added `TerminationGracePeriod` field to PodSpec and `grace-period` flag to `kubectl stop`.




## May 13, 2015

  * Kubernetes [v0.17.0](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.17.0) is the default version for new clusters.

  * New clusters can no longer be created at Kubernetes version 0.15.0.

  * Standalone `kubectl` works with Container Engine created clusters without needing to set the `KUBECONFIG` env var.

  * `gcloud alpha container kubectl` is deprecated. The command still works, but prints a warning with directions for using `kubectl` directly.

  * Added a new command, `gcloud alpha container get-credentials`. The command fetches cluster auth and updates the local `kubectl` command.

  * `gcloud alpha container kubectl` and `clusters delete|describe` print more helpful error messages when the cluster cannot be found due to an incorrect zone flag/default.

  * `gcloud alpha container clusters create` exits with non-zero returncode if cluster create succeeded but cert data could not be fetched.




kubectl 0.16.1 notes:

  * Improvements to [`kubectl rolling-update`](https://docs.cloud.google.com/kubernetes-engine/docs/kubectl/rolling-update).

  * Default global `kubeconfig` location changed to `~/.kube/config` from `~/.kube/.kubeconfig`.

  * [`kubectl delete`](https://docs.cloud.google.com/kubernetes-engine/docs/kubectl/delete) now stops resources by default (deletes child resources, e.g. pods managed by replication controller).

  * Flag word separators `-` and `_` made equivalent.

  * Recognize `.yml` extension for schema files.

  * [`kubectl get pods`](https://docs.cloud.google.com/kubernetes-engine/docs/kubectl/get) now prints container statuses.

  * Simplified loading rules for `kubeconfig` (see `kubectl config --help` for details).

  * `--flatten` and `--minify` options for [`kubectl config view`](https://docs.cloud.google.com/kubernetes-engine/docs/kubectl/config-view).

  * Various bugfixes.




## May 8, 2015

  * Master VMs are now created with a data persistent disk to store important cluster data, leaving the boot disk for the OS / software.



## May 2, 2015

  * Kubernetes [v0.16.0](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.16.0) is the default version for new clusters.

  * Clusters that don't have nginx will use bearer token auth instead of basic auth.

  * `KUBE_PROXY_TOKEN` added to `kube-env` metadata.




## April 22, 2015

  * A CIDR can now be requested during cluster creation when using the Google Cloud CLI or the REST API. For the Google Cloud CLI, use the `--container-ipv4-cidr` flag. If not set, the server will choose a CIDR for the cluster.

  * Standalone `kubectl` instructions are now available from `gcloud alpha container kubectl --help`.

  * When fetching cluster credentials after creating a cluster using the Google Cloud CLI, you'll never have to enter the passphrase for your SSH key more than once.

  * The `gcloud alpha container clusters ...` commands default to human-readable (table) output.




## April 16, 2015

Container Engine:

  * Kubernetes [v0.15.0](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.15.0) is the default version for new clusters. v0.14.2 is still supported.

  * The Kubernetes v1beta3 API is now enabled for new clusters.

  * New clusters can no longer be created at kubernetes version 0.13.2.




Google Cloud CLI:

  * The `kubectl` version is now v0.14.1.

  * The deprecated `gcloud alpha container pods|services|replicationcontrollers` commands have been removed. Use [`gcloud alpha container kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/kubectl) instead.




## April 9, 2015

Container Engine:

  * Kubernetes [v0.14.2](https://github.com/GoogleCloudPlatform/kubernetes/releases/tag/v0.14.2) is the default version for new clusters.

  * New clusters can no longer be created at kubernetes version 0.14.1.

  * Cluster creation is more reliable.

  * Clusters created via the [Google Cloud console](https://console.cloud.google.com/) will pre-fill the cluster name with a project-unique name instead of a zone-unique name.

  * API endpoint no longer included in [cluster list](https://console.cloud.google.com/kubernetes/list).




## April 2, 2015

Container Engine:

  * Kubernetes v0.14.1 is the default version for new clusters.

  * New clusters can no longer be created at version 0.11.0.

  * Container Engine's cluster firewall no longer specifies target-tags. This allows pods to make outgoing connections by default (in the private network).




Google Cloud CLI:

  * Clusters created by the Google Cloud CLI now automatically send logs to [Google Cloud Logging](https://docs.cloud.google.com/logging/docs) unless explicitly disabled using the `--no-enable-cloud-logging` flag. Logs are visible in the [logs section of the Google Cloud console](https://console.cloud.google.com/project/_/logs) once your project has enabled the Google Cloud Logging API.

  * You can now access Container Engine clusters with standalone `kubectl` (i.e. without `gcloud alpha container`) after setting an environment variable, which is printed after successful cluster creation and/or the first time accessing a cluster with `gcloud alpha container kubectl`.

  * Gcloud will always try to fetch certificate files for the cluster if they are missing. "WARNING: No certificate files found in..." will resolve itself on a subsequent `gcloud alpha container kubectl` command run if the cluster is healthy.

  * Known issue: `container` commands are included in the `alpha` component, but the kubernetes client (`kubectl`) is still installed with the `preview` component, so users will need both.




## April 1, 2015

  * **All Container Engine commands have moved from`gcloud preview` to** **`gcloud alpha`**. Run `gcloud components update alpha` to install this command group. Documentation has been updated to use the `alpha` commands.



## March 25, 2015

  * Kubernetes v0.13.2 is the default version for new clusters.

  * The `kubectl` version is now v0.13.1.

  * Updated to `container-vm-v20150317`, which starts up more reliably.

  * The default boot disk size for cluster nodes has been increased from 10GB to 100GB.




## February 25, 2015

Google Cloud CLI:

  * The `kubectl` wrapper commands (`gcloud preview container pods|services|replicationcontrollers`) have been deprecated in favor of using `gcloud preview container kubectl` directly. Calling the deprecated commands prints the equivalent `kubectl` command.

  * The `kubectl` version has been bumped to 0.11.0.

  * Fixed a bug that prevented `kubectl update` with `--patch` from working.

  * The `kubectl` command now automatically tries refetching the configuration if the command fails with a stale configuration error.




## February 19, 2015

Google Container Engine:

  * Kubernetes v0.11.0 is the default version for new clusters.

  * Removed support for creating clusters at Kubernetes v0.9.2.

  * Nodes now use the container-vm-v20150129 image.




Google Cloud CLI:

  * Pods created with `gcloud preview container pods create` no longer bind to a host port. As a result the scheduler can assign more than one pod to each host.

  * The version of `kubectl` used by the `gcloud preview container kubectl` command is 0.10.1.




## February 12, 2015

  * Kubernetes v0.10.1 is the default version for new clusters.

  * Removed support for creating clusters at Kubernetes v0.10.0.

  * Improved API enablement flow and error messages when first visiting the Container Engine page of the [Google Cloud console](https://console.cloud.google.com/).




## February 5, 2015

Google Container Engine:

  * Kubernetes v0.10.0 is the default version for new clusters.

  * Removed support for creating clusters at Kubernetes version 0.8.1.




Google Cloud CLI:

  * The `gcloud preview container kubectl` command is upgraded to version 0.9.1:

    * `kubectl create` handles bulk creation from file or directory.
    * The `createall` command has been removed.
    * Added the `kubectl rollingupdate` command, which runs controlled updates of replicated pods.
    * Added the `kubectl run-container` command, which simplifies creation of a (optionally replicated) pod from an image.
    * Added the `kubectl stop` command to cleanly shut down a replication controller.
    * Added `kubectl config ...` commands for managing config for multiple clusters/users. (Note: this is not yet compatible with `gcloud preview container kubectl`).

Refer to the [`kubectl` reference documentation](https://docs.cloud.google.com/kubernetes-engine/docs/kubectl) for more details.




## January 29, 2015

  * Kubernetes v0.9.2 is the default version for new clusters.

  * Removed support for creating clusters at v0.7.1. Existing clusters at this version can still be used and deleted.

  * [SkyDNS](https://github.com/skynetservices/skydns) is supported for services on clusters using v0.9.2 onwards.




## January 21, 2015

  * Improved error messages during pod creation when the source image is invalid.

  * Fixed a bug affecting Compute Engine routes whose `destRange` fields are plain IP addresses.

  * Improved the reliability of cluster creation when provisioning is slow.




## January 15, 2015

  * Kubernetes v0.8.1 is the default version for newly created clusters. Our v0.8.1 support includes changes on the 0.8 branch at 0.8.1.

  * Removed support for creating clusters at Kubernetes v0.8.0. Existing clusters at this version can still be used and deleted.

  * Service accounts and auth scopes can be added to node instances at the time of creation for all pods to use.

  * The command line interface now renders multiple error messages across newlines and tabs, instead of using a comma separator.

  * Machine type information has been fixed in the cluster details page of the Google Cloud console.




## January 8, 2015

  * Kubernetes v0.8.0 is the default version for newly created clusters. Kubernetes v0.7.1 is also supported. Refer to the [Kubernetes release notes](https://github.com/GoogleCloudPlatform/kubernetes/releases) for information about each release. Our v0.7.1 support includes changes on the 0.7 branch at 0.7.1. Our v0.8.0 support includes changes in the 0.7.2 and 0.8.0 releases.

  * Removed support for creating clusters at Kubernetes v0.6.1 and v0.7.0. Existing clusters at these versions can still be used and deleted.

  * The `pods|services|replicationcontrollers create` commands now validate the resource type when creating with `--config-file`. This fixes the known issue in the December 12, 2014 release.




## December 19, 2014

  * Kubernetes v0.7.0 is the default version for newly created clusters.

  * Removed support for creating clusters at Kubernetes v0.4.4 and v0.5.5. Existing clusters at these versions can still be used and deleted.




## December 12, 2014

Known issues:

  * The `pods|services|replicationcontrollers create` commands do not validate the resource type when creating with `--config-file`. The command creates the resource specified in the configuration file, regardless of the command group specified. For example, calling `pods create` and passing a service configuration file creates a service instead of failing.



Updates:

  * Kubernetes v0.6.1 is the default version for newly created clusters.

  * Google Container Engine now reserves a /14 CIDR range for new clusters. Previously, a /16 was reserved.

  * New clusters created with Kubernetes v0.4.4 now use the backports-debian-7-wheezy-v20141108 image. This replaces the previous backports-debian-7-wheezy-v20141021 image.

  * New clusters created with Kubernetes v0.5.5 or v0.6.1 now use the container-vm image, instead of the Debian backports image.

  * The [Service Operations](https://docs.cloud.google.com/kubernetes-engine/docs/services/operations) documentation has been updated to describe the `createExternalLoadBalancer` option.

  * A new `gcloud preview container kubectl` command has been added to the CLI. This is a pass-through command to call the native Kubernetes [kubectl](https://github.com/GoogleCloudPlatform/kubernetes/tree/master/pkg/kubectl) client with arbitrary commands, using the Google Cloud CLI to handle authentication.

  * The `--cluster-name` flag in all CLI commands has been renamed to `--cluster`.

  * New `describe` and `list` support for cluster operations.




## December 5, 2014

  * The syntax for creating a pod with the Google Container Engine command line interface has changed. The name of the pod is now specified as the value of a `--name` flag. See the [Pod Operations](https://docs.cloud.google.com/kubernetes-engine/docs/pods/operations) page for details.

  * Clusters and Operations returned by the API now include a `selfLink` field and Operations also include a `targetLink` field, which contain the full URL of the given resource.

  * Added support for Kubernetes v0.4.4 and Kubernetes v0.5.5. The default version is now v0.4.4. Refer to the [Kubernetes release notes](https://github.com/GoogleCloudPlatform/kubernetes/releases) for information about each release. Our v0.4.4 support includes changes on the 0.4 branch from 0.4.2 through 0.4.4. Our v0.5.5 support includes changes on the 0.5 branch through 0.5.5.

  * Removed support for creating clusters at Kubernetes v0.4.2. Existing clusters at this version can still be used and deleted.




## November 20, 2014

Updates to the `gcloud preview container` commands:

  * New error message that catches cluster creation failure due to missing `default` network.

  * Specify default zone and cluster :
        
        gcloud config set compute/zone ZONE
        gcloud config set container/cluster CLUSTER_NAME
        

There is currently a bug preventing the default cluster name from working if the local configuration cache is missing. If you see a stack trace when omitting `--cluster-name`, repeat the command once with the flag specified. Subsequent commands can omit the flag.

  * The default cluster name is set to the value of the new cluster when a cluster is successfully created.

  * The `gcloud preview container clusters list` command lists clusters across all zones if no `--zone` flag is specified. The `list` command ignores any default zone that may be set.




Documentation updates:

  * A new Getting Started guide has been added: [Hello Wordpress](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-wordpress).



Google Cloud console updates:

  * Cluster error state information is available in the Google Cloud console.



## November 4, 2014

_(Updated November 10, 2014: Added two additional known issues with Google_ _Container Engine.)_

Google Container Engine is a new service that creates and manages [Kubernetes](http://kubernetes.io) clusters for Google Cloud users.

Container Engine is currently in Alpha state; it is suitable for experimentation and is intended to provide an early view of the production service, but customers are strongly encouraged not to run production workloads on it.

The underlying open source Kubernetes project is being actively developed by the community and is not considered ready for production use. This version of Google Container Engine is based on [Kubernetes public build](https://github.com/GoogleCloudPlatform/kubernetes/releases) v0.4.2. While the Kubernetes community is working hard to address community-reported issues as they are reported, there are some known issues in the v0.4.2 release that will be addressed in v0.5 and that will be incorporated into Google Container Engine in the coming days.

**Known issues with the Kubernetes 0.4.2 release**

  1. (Issue #[1730](https://github.com/GoogleCloudPlatform/kubernetes/issues/1730)) **External health checks that use in-container scripts (exec) do not** **work. Process, HTTP and TCP health checks work properly**. Health checks that use in-container shell execution are not functioning; they always report Unknown. This is a result of the transition to `docker exec` introduced in Docker version 1.3. At this time process-level health checks, TCP socket health checks, and HTTP level health checks are functional. This has been addressed in v0.5 and will be available shortly.

  2. (Issue #[1712](https://github.com/GoogleCloudPlatform/kubernetes/issues/1712)) **Pod update operations fails**. In v0.4.2, pod update functionality is not implemented, and a call to the update API returns an unimplemented error. Pods must be updated by tear down and recreate. This will be implemented in v0.5.

  3. (Issue #[974](https://github.com/GoogleCloudPlatform/kubernetes/issues/974)) **Silent failure on internal service port number collision:** Each Kubernetes service needs a unique network port assignment. Currently if you try to create a second service with a port number that conflicts with an existing service, the operation succeeds but the second service will not receive network traffic. This has been fixed, and will be available in v0.5.

  4. (Issue #[1161](https://github.com/GoogleCloudPlatform/kubernetes/issues/1161)) **External service load balancing**. The current Kubernetes design includes a model that does a 1:1 mapping between an externally-exposed port number at the cluster level, and a service. This means that only a single external service can exist on a given port. For now this is a hard limitation of the service.




**Known issues with Google Container Engine**

In addition to issues with the underlying Kubernetes project, there are some known issues with the Google Container Engine tools and API that will be addressed in subsequent releases.

  1. **Kubecfg binary conflicts:** During the Google Cloud SDK installation, kubecfg v0.4.1 is installed and placed on the path by the Google Cloud CLI. Depending on your $PATH variable, this version may conflict with other installed versions from the open source Kubernetes product.

  2. **Containers are assigned private IPs in the range** **10.40.0.0/16 to 10.239.0.0/16**. If you have changed your default network settings from 10.240.0.0/16, clusters may create successfully, but fail during operation.

  3. **All Container Engine nodes are started with and require project level** **read-write scope**. This is temporarily required to support the dynamic mounting of PD-based volumes to nodes. In future releases nodes will revert to default read-only project scope.

  4. **Windows is not currently supported**. The `gcloud preview container` command is built on top of the Kubernetes client's `kubecfg` binary, which is not yet available on Windows.

  5. **The default network is required**. Container Engine relies on the existence of the default network, and tries to create routes that use it. If you don't have a default network, Container Engine cluster creation will fail.

To recreate it:

     1. Go to the [Networks page](https://console.cloud.google.com/project/_/networks/list) in the Google Cloud console and select your project.
     2. Click **New network**.
     3. Enter the following values: 
        * Name: `default`
        * Address range: `10.240.0.0/16`
        * Gateway: `10.240.0.1`
     4. Click **Create**.

Next, recreate the firewall rules:

     1. Click `default` in the **All networks** list.
     2. Click **Create new** next to **Firewall rules**.
     3. Enter the following values: 
        * Name: `default-allow-internal`
        * Source IP ranges: `10.240.0.0/16`
        * Protocols & ports: `tcp:1-65535; udp:1-65535; icmp`
     4. Click **Create**.
     5. Create a second firewall rule with the following values: 
        * Name: `default-allow-ssh`
        * Source IP ranges: `0.0.0.0/0`
        * Protocols & ports: `tcp:22`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
