---
url: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable/
title: GKE release notes (Stable channel) \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:54.533767+00:00
---

# GKE release notes (Stable channel)  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE release notes (Stable channel) Stay organized with collections  Save and categorize content based on your preferences. 

This page documents Google Kubernetes Engine version updates in the Stable [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). 

For all Google Kubernetes Engine version updates, fixes, known issues, or new features, see [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).

For more detailed information about security-related known issues, see the [security bulletin](https://docs.cloud.google.com/kubernetes-engine/docs/security-bulletins) page.

To view release notes for versions prior to 2020, see the [Release notes archive](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gke-stable-channel-release-notes.xml) directly. 

**Note** : Your clusters might not have the latest released versions. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

## October 08, 2026

Change

#### (2026-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000) is now available in the Stable channel.
  * Version 1.34.11-gke.1044000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.



## October 02, 2026

Change

#### (2026-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)
    * [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)
  * The following versions are no longer available in the Stable channel: 
    * 1.34.10-gke.1328000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1250000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.34 to [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.35 to [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)



## September 23, 2026

Change

#### (2026-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.10-gke.1328000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000) is now available in the Stable channel.
  * Version 1.34.10-gke.1236000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.



## September 17, 2026

Change

#### (2026-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.10-gke.1236000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000) is now available in the Stable channel.
  * Version 1.34.10-gke.1106000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.34 to [1.35.6-gke.1250000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)



## September 08, 2026

Change

#### (2026-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.10-gke.1106000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1106000) is now available in the Stable channel.
  * Version 1.34.10-gke.1079000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.



## September 02, 2026

Change

#### (2026-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410) is now available in the Stable channel.
  * Version 1.34.9-gke.1610001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)



## August 26, 2026

Change

#### (2026-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349) is now available in the Stable channel.
  * Version 1.34.9-gke.1322001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.9-gke.1610001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.9-gke.1610001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)



## August 20, 2026

Change

#### (2026-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.34.9-gke.1322001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.9-gke.1610001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.13-gke.1101000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.13-gke.1109000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1065000
    * 1.34.9-gke.1322000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.9-gke.1322001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.9-gke.1322001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)



## August 14, 2026

Change

#### (2026-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.13-gke.1011000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1287000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1057002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1163012 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1241004 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.35 to [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)



## August 12, 2026

Change

#### (2026-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.12-gke.1270000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1131000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)



## July 30, 2026

Change

#### (2026-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.12-gke.1165000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1278000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)



## July 24, 2026

Change

#### (2026-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)



## July 16, 2026

Change

#### (2026-R30) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348) is now the default version for cluster creation in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.33.12-gke.1059000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1126000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)



## July 10, 2026

Change

#### (2026-R29) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)



## July 09, 2026

Change

#### (2026-R28) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348) is now the default version for cluster creation in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.33.12-gke.1000000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1000000
    * 1.35.5-gke.1000004 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)



Change

#### (2026-R27) Version updates

There are no version updates for 2026-R27.

## June 29, 2026

Change

#### (2026-R26) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.11-gke.1197000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.7-gke.1499000
    * 1.35.3-gke.2190000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1000004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)



## June 26, 2026

Change

#### (2026-R25) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1000004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.11-gke.1074000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.7-gke.1055000
    * 1.35.3-gke.1389002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.33 to [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



Change

#### (2026-R24) Version updates

There are no version updates for 2026-R24.

## June 12, 2026

Change

#### (2026-R23) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)



## June 04, 2026

Change

#### (2026-R22) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347) is now the default version for cluster creation in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.33.11-gke.1013000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1307000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)



## May 27, 2026

Change

#### (2026-R21) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.10-gke.1115000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.10-gke.1176000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1154000
    * 1.34.6-gke.1237000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1234002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1389000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## May 21, 2026

Change

#### (2026-R20) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## May 13, 2026

Change

#### (2026-R19) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.10-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1234002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following versions are no longer available in the Stable channel: 
    * 1.33.10-gke.1067000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1068000
    * 1.35.2-gke.1962000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1234000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.34 to [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.3-gke.1234002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## May 06, 2026

Change

#### (2026-R18) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.13-gke.1059000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1205000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.9-gke.1060000
    * 1.34.5-gke.1076000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1269001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.34 to [1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.2-gke.1962000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## April 29, 2026

Change

#### (2026-R17) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.13-gke.1205000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.2-gke.1962000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.12-gke.1026000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.12-gke.1076000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.12-gke.1127000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.8-gke.1026000
    * 1.33.8-gke.1112000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.8-gke.1169000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.4-gke.1047000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.4-gke.1130000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.4-gke.1193000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.32 to [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.33 to [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
      * 1.34 to [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)



## April 22, 2026

Change

#### (2026-R16) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## April 15, 2026

Change

#### (2026-R15) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## April 09, 2026

Change

#### (2026-R14) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.35 to [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## April 02, 2026

Change

#### (2026-R13) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)



## March 25, 2026

Change

#### (2026-R12) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.11-gke.1264000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.5-gke.2469000
    * 1.34.3-gke.1444000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)



## March 18, 2026

Change

#### (2026-R11) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.11-gke.1211000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.5-gke.2392000
    * 1.34.3-gke.1318000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)



## March 12, 2026

Change

#### (2026-R10) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.11-gke.1174000
    * 1.33.5-gke.2326000
    * 1.34.3-gke.1245000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)



## March 05, 2026

Change

#### (2026-R9) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.11-gke.1038000
    * 1.33.5-gke.2228001
    * 1.34.3-gke.1051003
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)



## February 25, 2026

Change

#### (2026-R8) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * Version 1.33.5-gke.2172001 is no longer available in the Stable channel.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## February 19, 2026

Change

#### (2026-R7) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.9-gke.1734000
    * 1.33.5-gke.2118001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)



## February 11, 2026

Change

#### (2026-R6) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.9-gke.1728000
    * 1.33.5-gke.2100001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## February 04, 2026

Change

#### (2026-R5) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.9-gke.1711000
    * 1.33.5-gke.2072001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## January 29, 2026

Change

#### (2026-R4) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.9-gke.1675000
    * 1.33.5-gke.2019000
    * 1.33.5-gke.2072000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## January 21, 2026

Change

#### (2026-R3) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.31.14-gke.1081000
    * 1.31.14-gke.1114000
    * 1.32.9-gke.1632000
    * 1.33.5-gke.1956000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## January 15, 2026

Change

#### (2026-R2) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.31.13-gke.1139000
    * 1.32.9-gke.1239000
    * 1.33.5-gke.1308000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.31 to [1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.32 to [1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## January 07, 2026

Change

#### (2026-R1) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.31.13-gke.1023000
    * 1.32.9-gke.1108000
    * 1.33.5-gke.1162000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## January 05, 2026

Change

#### (2025-R54) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## December 29, 2025

Change

#### (2025-R53) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## December 18, 2025

Change

#### (2025-R52) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## December 10, 2025

Change

#### (2025-R51) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## December 05, 2025

Change

#### (2025-R50) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.31.13-gke.1008000
    * 1.32.9-gke.1092000
    * 1.33.5-gke.1125000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## November 28, 2025

Change

#### (2025-R49) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## November 20, 2025

Change

#### (2025-R48) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## November 14, 2025

Change

#### (2025-R47) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Stable channel.

## November 07, 2025

Change

#### (2025-R46) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.31.12-gke.1265000
    * 1.32.9-gke.1072000
    * 1.33.5-gke.1080000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 29, 2025

Change

#### (2025-R45) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.31.12-gke.1220000
    * 1.32.9-gke.1010000
    * 1.33.4-gke.1350000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 22, 2025

Change

#### (2025-R44) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Stable channel: 
    * 1.31.11-gke.1036000
    * 1.32.8-gke.1170000
    * 1.33.4-gke.1245000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.31 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)



## October 15, 2025

Change

#### (2025-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Stable channel: 
    * 1.32.8-gke.1134000
    * 1.33.4-gke.1172000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
      * 1.32 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
      * 1.33 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)



## October 08, 2025

Change

#### (2025-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.14-gke.1108000
    * 1.30.14-gke.1130000
    * 1.32.8-gke.1108000
    * 1.33.4-gke.1134000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
      * 1.33 to [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)



## October 02, 2025

Change

#### (2025-R41) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.14-gke.1059000
    * 1.32.6-gke.1060000
    * 1.33.3-gke.1136000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 29, 2025

Change

#### (2025-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.14-gke.1036000
    * 1.32.8-gke.1026000
    * 1.33.4-gke.1036000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.



## September 18, 2025

Change

#### (2025-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.14-gke.1011000
    * 1.32.7-gke.1079000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.



## September 11, 2025

Change

#### (2025-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1414000
    * 1.32.7-gke.1016000
    * 1.33.2-gke.1043000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.



## September 03, 2025

Change

#### (2025-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1390000
    * 1.31.11-gke.1002000
    * 1.32.6-gke.1125000
    * 1.33.2-gke.1240000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.



## August 27, 2025

Change

#### (2025-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1372000
    * 1.31.10-gke.1067000
    * 1.32.6-gke.1096000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.



## August 21, 2025

Change

#### (2025-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1340000
    * 1.31.10-gke.1034000
    * 1.32.6-gke.1025000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 14, 2025

Change

#### (2025-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1333000
    * 1.31.10-gke.1021000
    * 1.32.6-gke.1013000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 06, 2025

Change

#### (2025-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1320000
    * 1.31.9-gke.1287000
    * 1.32.4-gke.1767000
    * 1.33.2-gke.1111000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 01, 2025

Change

#### (2025-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1279000
    * 1.31.9-gke.1218000
    * 1.32.4-gke.1698000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.



## July 25, 2025

Change

#### (2025-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1086000
    * 1.30.12-gke.1151000
    * 1.30.12-gke.1168000
    * 1.30.12-gke.1208000
    * 1.30.12-gke.1246000
    * 1.31.8-gke.1113000
    * 1.31.9-gke.1005000
    * 1.31.9-gke.1044001
    * 1.31.9-gke.1119000
    * 1.31.9-gke.1176000
    * 1.32.2-gke.1297002
    * 1.32.4-gke.1415000
    * 1.32.4-gke.1603000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.



## July 16, 2025

Change

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)



## July 11, 2025

Change

#### (2025-R29) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)



## July 02, 2025

Change

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)



## June 27, 2025

Change

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)



## June 18, 2025

Change

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.12-gke.1033000
    * 1.31.8-gke.1045000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.



## June 12, 2025

Change

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.11-gke.1217000
    * 1.31.7-gke.1390000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.



## June 05, 2025

Change

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.11-gke.1157000
    * 1.31.7-gke.1265000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.



Change

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

## May 30, 2025

Change

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.11-gke.1131000
    * 1.31.7-gke.1212000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.



Change

#### (2025-R21) Version updates

There are no version updates for 2025-R21.

## May 23, 2025

Change

#### (2025-R20) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.10-gke.1070000
    * 1.31.6-gke.1064001
    * 1.32.2-gke.1182003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## May 16, 2025

Change

#### (2025-R19) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)



## May 09, 2025

Change

#### (2025-R18) Version updates

There are no new releases in the Stable channel.

## May 02, 2025

Change

#### (2025-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version 1.32.1-gke.1357001 is no longer available in the Stable channel.
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## April 28, 2025

Change

#### (2025-R16) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.29.13-gke.1038000
    * 1.29.13-gke.1169000



## April 18, 2025

Change

#### (2025-R15) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available in the Stable channel: 
    * 1.29.13-gke.1109000
    * 1.30.9-gke.1127000
    * 1.30.9-gke.1201000
    * 1.30.10-gke.1022000
    * 1.31.5-gke.1169000
    * 1.31.5-gke.1233000
    * 1.31.6-gke.1020000
    * 1.31.6-gke.1064000
    * 1.32.2-gke.1182001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.



## April 08, 2025

Change

#### (2025-R14) Version updates

There are no new releases in the Stable channel.

## April 02, 2025

Change

#### (2025-R13) Version updates

There are no new releases in the Stable channel.

## March 26, 2025

Change

#### (2025-R12) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)



## March 19, 2025

Change

#### (2025-R11) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)



## March 12, 2025

Change

#### (2025-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available in the Stable channel: 
    * 1.30.9-gke.1046000
    * 1.31.5-gke.1068000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.



## March 05, 2025

Change

#### (2025-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Stable channel: 
    * 1.29.13-gke.1006000
    * 1.30.9-gke.1009000
    * 1.31.5-gke.1023000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) with this release.



## February 26, 2025

Change

#### (2025-R08) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available in the Stable channel: 
    * 1.29.12-gke.1270000
    * 1.30.8-gke.1261000
    * 1.31.4-gke.1372000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.



## February 18, 2025

Change

#### (2025-R07) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available in the Stable channel: 
    * 1.29.12-gke.1143001
    * 1.30.8-gke.1162001
    * 1.31.4-gke.1256000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## February 11, 2025

Change

#### (2025-R06) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.15-gke.1480000
    * 1.28.15-gke.1503000
    * 1.29.12-gke.1120001
    * 1.30.8-gke.1128001
    * 1.30.8-gke.1162000
    * 1.31.4-gke.1183000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.12-gke.1143001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.12-gke.1143001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## February 06, 2025

Change

#### (2025-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1143001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.15-gke.1435000
    * 1.29.12-gke.1055000
    * 1.29.12-gke.1055001
    * 1.30.8-gke.1051000
    * 1.30.8-gke.1051001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.12-gke.1120001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.12-gke.1120001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.



## January 29, 2025

Change

#### (2025-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1120001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.15-gke.1342000
    * 1.29.10-gke.1280000
    * 1.30.5-gke.1713000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 23, 2025

Change

#### (2025-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
  * Version 1.30.6-gke.1596000 is no longer available in the Stable channel.



## January 14, 2025

Change

#### (2025-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.28.15-gke.1020000
    * 1.29.10-gke.1054000
    * 1.29.10-gke.1155000
    * 1.30.5-gke.1699000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## January 07, 2025

Change

#### (2025-R01) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)



## December 26, 2024

Change

**(2024-R50) Version updates**

There are no new releases in the Stable channel.

## December 18, 2024

Change

**(2024-R49) Version updates**

There are no new releases in the Stable channel.

## December 12, 2024

Change

#### (2024-R48) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.28.14-gke.1340000
    * 1.29.9-gke.1496000
    * 1.30.5-gke.1443001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## December 10, 2024

Change

#### (2024-R47) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.14-gke.1099000
    * 1.28.14-gke.1217000
    * 1.29.9-gke.1177000
    * 1.30.5-gke.1014003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## November 27, 2024

Change

#### (2024-R46) Version updates

There are no new releases in the Stable channel.

## November 19, 2024

Change

#### (2024-R45) Version updates

There are no new releases in the Stable channel.

## November 13, 2024

Change

#### (2024-R44) Version updates

GKE cluster versions have been updated.

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)



## November 06, 2024

Change

#### (2024-R43) Version updates

There are no new releases in the Stable channel.

## October 30, 2024

Change

#### (2024-R42) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.28.14-gke.1004000
    * 1.29.8-gke.1278000
    * 1.30.5-gke.1014001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## October 25, 2024

Change

#### (2024-R41) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.13-gke.1119000
    * 1.29.8-gke.1211000
    * 1.30.4-gke.1348001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## October 17, 2024

Change

#### (2024-R40) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.13-gke.1049000
    * 1.29.8-gke.1096000
    * 1.30.3-gke.1969002
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.



## October 11, 2024

Change

#### (2024-R39) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
  * The following versions are no longer available in the Stable channel: 
    * 1.27.16-gke.1148001
    * 1.27.16-gke.1258000
    * 1.27.16-gke.1287000
    * 1.28.13-gke.1024000
    * 1.29.8-gke.1057000
    * 1.30.3-gke.1969001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## October 03, 2024

Change

#### (2024-R38) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.13-gke.1006000
    * 1.29.8-gke.1031000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.8-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.8-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.



## September 26, 2024

Change

#### (2024-R37) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.27.16-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
  * The following versions are no longer available in the Stable channel: 
    * 1.27.16-gke.1051001
    * 1.28.12-gke.1052000
    * 1.28.12-gke.1179000
    * 1.29.7-gke.1104000
    * 1.29.7-gke.1274000
    * 1.30.2-gke.1587003
    * 1.30.3-gke.1639000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## September 19, 2024

Change

#### (2024-R36) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)



## September 11, 2024

Change

#### (2024-R35) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302) is now the default version for cluster creation in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * Version 1.27.16-gke.1008000 is no longer available in the Stable channel.
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.16-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.16-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.



## September 06, 2024

Change

#### (2024-R34) Version updates

There are no new releases in the Stable channel.

Change

#### (2024-R33) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) is now the default version for cluster creation in the Stable channel.
  * Version [1.27.16-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) is now available in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.27.15-gke.1252000
    * 1.28.11-gke.1260000
    * 1.29.6-gke.1326000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.



## August 28, 2024

Change

#### (2024-R32) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)



## August 20, 2024

Change

#### (2024-R31) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.27.15-gke.1154000
    * 1.28.11-gke.1172000
    * 1.29.6-gke.1254000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## August 14, 2024

Change

#### (2024-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
  * The following versions are no longer available in the Stable channel: 
    * 1.27.14-gke.1059002
    * 1.28.11-gke.1019001
    * 1.29.6-gke.1038001
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302) with this release.



## August 12, 2024

Change

### (2024-R29) Version updates

There are no new releases in the Stable channel.

## August 07, 2024

Change

### (2024-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## July 31, 2024

Change

### (2024-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.27.14-gke.1042001
    * 1.28.10-gke.1075001
    * 1.29.5-gke.1091002
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## July 23, 2024

Change

### (2024-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)



## July 17, 2024

Change

### (2024-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) is now the default version in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.27.13-gke.1201002
    * 1.28.9-gke.1289002
    * 1.28.10-gke.1058001
    * 1.29.4-gke.1043004
    * 1.29.5-gke.1091001
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.



## July 10, 2024

Change

### (2024-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1058001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1091001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following versions are no longer available in the Stable channel: 
    * 1.26.15-gke.1090000
    * 1.26.15-gke.1090004
    * 1.26.15-gke.1191000
    * 1.26.15-gke.1191001
    * 1.26.15-gke.1300000
    * 1.26.15-gke.1300001
    * 1.27.13-gke.1070000
    * 1.27.13-gke.1070002
    * 1.27.13-gke.1166000
    * 1.27.13-gke.1166001
    * 1.27.13-gke.1201000
    * 1.28.9-gke.1069000
    * 1.28.9-gke.1069002
    * 1.28.9-gke.1209000
    * 1.28.9-gke.1209001
    * 1.28.9-gke.1289000
    * 1.29.4-gke.1043002
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## July 08, 2024

Change

### (2024-R23) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.13-gke.1070002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) is now the default version in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.26.15-gke.1090004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.15-gke.1090004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.13-gke.1070002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.13-gke.1070002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.9-gke.1069002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## July 03, 2024

Change

### (2024-R22) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.26.15-gke.1090004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1191001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1300001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1070002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.27.13-gke.1166001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1069002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1209001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)



## June 26, 2024

Change

#### (2024-R21) Version updates

  * Version [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.27.13-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
  * The following versions are no longer available in the Stable channel: 
    * 1.27.11-gke.1062004
    * 1.28.9-gke.1000000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.9-gke.1069000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## June 18, 2024

Change

#### (2024-R20) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.26.15-gke.1191000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1300000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
  * The following versions are no longer available in the Stable channel: 
    * 1.28.7-gke.1026001
    * 1.28.8-gke.1095000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## June 12, 2024

Change

#### (2024-R19) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
    * [1.28.9-gke.1069000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * Version 1.27.13-gke.1000000 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## June 06, 2024

Change

#### (2024-R18) Version updates

  * Version [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.27.13-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
  * The following versions are no longer available in the Stable channel: 
    * 1.27.11-gke.1062003
    * 1.27.12-gke.1115000
    * 1.28.8-gke.1095000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.



## June 05, 2024

Change

Updated [2024-R03 release notes](https://cloud.google.com/kubernetes-engine/docs/release-notes#February_08_2024) to indicate that control planes and nodes with auto-upgrade enabled in the Stable channel were upgraded from version 1.27 to version 1.27.7-gke.1121002, not 1.28.3-gke.1203001 as previously stated.

## May 28, 2024

Change

#### (2024-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version 1.26.14-gke.1044001 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.



## May 21, 2024

Change

#### (2024-R16) Version updates

  * Version [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) is now available in the Stable channel.
  * Version 1.28.7-gke.1026000 is no longer available in the Stable channel.



## May 17, 2024

Change

#### (2024-R14) Version updates

There are no version updates for 2024-R14.

#### (2024-R15) Version updates

  * Version [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712)
    * [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
  * The following versions are no longer available in the Stable channel: 
    * 1.26.8-gke.200
    * 1.26.14-gke.1044000
    * 1.27.11-gke.1062001
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.26.14-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.7-gke.1026001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) with this release.



## May 08, 2024

Change

#### (2024-R13) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.26.14-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1026001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
  * The following versions are no longer available in the Stable channel: 
    * 1.26.13-gke.1144000
    * 1.27.8-gke.1067004
    * 1.27.11-gke.1062000
    * 1.28.3-gke.1118000
    * 1.28.3-gke.1286000



## May 01, 2024

Change

#### (2024-R12) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) is now the default version in the Stable channel.
  * Version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) is now available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.



## April 30, 2024

Change

#### (2024-R11) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are no longer available in the Stable channel: 
    * 1.25.16-gke.1460000
    * 1.25.16-gke.1537000



## April 18, 2024

Change

#### (2024-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
  * The following versions are no longer available in the Stable channel: 
    * 1.25.15-gke.1115000
    * 1.25.16-gke.1041000
    * 1.26.11-gke.1055000
    * 1.27.7-gke.1121002
    * 1.28.3-gke.1203001
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) with this release.



## April 08, 2024

Change

#### (2024-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * There are no new releases in the Stable release channel.



## March 20, 2024

Change

**(2024-R08) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
  * Version 1.26.10-gke.1101000 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.



## March 07, 2024

Change

**(2024-R07) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611) with this release.



## March 04, 2024

Change

**(2024-R06) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278) is now the default version in the Stable channel.



## February 23, 2024

Change

#### (2024-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * There are no new releases in the Stable release channel.



## February 13, 2024

Change

#### (2024-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * There are no new releases in the Stable release channel.



## February 08, 2024

Change

The 2024-R03 release notes were updated on June 5th, 2024 with the following:

**Stable channel**

Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version 1.27.7-gke.1121002 with this release, not 1.28.3-gke.1203001 as previously stated.

Change

#### (2024-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.7-gke.1121002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277) is now the default version in the Stable channel.
  * Version [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) is now available in the Stable channel.
  * Version 1.27.3-gke.100 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## January 26, 2024

Change

#### (2024-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Stable channel: 
    * [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611)
    * [1.27.7-gke.1121002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278)
    * [1.28.3-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Stable channel: 
    * 1.24.17-gke.200
    * 1.24.17-gke.2266000
    * 1.25.10-gke.2700
    * 1.25.13-gke.200
    * 1.27.4-gke.900
    * 1.27.5-gke.200
    * 1.27.7-gke.1121000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.7-gke.1121002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.3-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## January 11, 2024

Change

#### (2024-R01) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Stable channel: 
    * 1.24.16-gke.500
    * 1.25.12-gke.500
    * 1.26.7-gke.500
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1268) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.28 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28) with this release.



## December 12, 2023

Change

#### (2023-R26) Version updates

There are no new releases in the Stable channel.

## December 04, 2023

Change

#### (2023-R25) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.13-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12513)
    * [1.26.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1268)
    * [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275)
  * The following versions are no longer available in the Stable channel: 
    * 1.24.15-gke.1700
    * 1.26.5-gke.2700
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.7-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1267) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274) with this release.



## November 17, 2023

Change

#### (2023-R24) Version updates

  * There are no new releases in the Stable release channel.



## November 09, 2023

Change

#### (2023-R23) Version updates

  * Version 1.24.14-gke.2700 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## October 05, 2023

Change

#### (2023-R19) Version updates

  * The following version is no longer available in the Stable channel: 1.26.5-gke.2100



## September 05, 2023

Change

#### (2023-R18) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416)
    * [1.25.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12512)
    * [1.26.7-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1267)
    * [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274)
  * The following versions are no longer available in the Stable channel: 1.23.17-gke.8400, 1.24.14-gke.1400, 1.25.10-gke.2100, 1.27.3-gke.1700
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.



## August 08, 2023

Change

#### (2023-R17) Version updates

  * Version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415)
    * [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.3-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following versions are no longer available in the Stable channel: 
    * 1.22.17-gke.12700
    * 1.23.17-gke.7700
    * 1.24.14-gke.1200
    * 1.25.10-gke.1200
    * 1.26.5-gke.1400
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.5-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## July 26, 2023

Change

#### (2023-R16) Version updates

  * Version [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.23.17-gke.7700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.18800
    * 1.23.17-gke.6800
    * 1.24.13-gke.2500
    * 1.25.9-gke.2300
    * 1.26.5-gke.1200
    * 1.27.2-gke.1200
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.17-gke.7700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) with this release.



## July 07, 2023

Change

#### (2023-R15) Version updates

  * Version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272)
  * The following versions are no longer available in the Stable channel: 
    * 1.23.17-gke.5600
    * 1.24.12-gke.1000
    * 1.25.8-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.27 to version [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) with this release.



## June 27, 2023

Change

#### (2023-R14) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259)
  * The following versions are no longer available in the Stable channel: 
    * 1.22.17-gke.8000
    * 1.23.17-gke.2000
    * 1.24.12-gke.500
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.



## June 15, 2023

Change

#### (2023-R13) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413)
    * [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
  * Version 1.24.11-gke.1000 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.26 to version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## June 07, 2023

Change

#### (2023-R12) Version updates

  * Version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) is now the default version in the Stable channel.
  * Version 1.21.14-gke.18100 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.



## June 05, 2023

Change

#### (2023-R11) Version updates

  * Version [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
  * The following versions are no longer available in the Stable channel: 
    * 1.22.17-gke.7500
    * 1.23.17-gke.1700
    * 1.24.10-gke.2300
    * 1.25.8-gke.500
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.



## May 09, 2023

Change

#### (2023-R10) Version updates

  * Version [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) is now the default version.
  * The following versions are now available in the Stable channel: 
    * [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.15800
    * 1.22.17-gke.5400
    * 1.23.16-gke.1400
    * 1.24.9-gke.3200
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.25 to version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.



## April 19, 2023

Change

#### (2023-R09) Version updates

  * Version [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) is now available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.



## March 31, 2023

Change

#### (2023-R08) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
  * Version [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) is now the default version in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.14600
    * 1.22.17-gke.4000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.



## March 22, 2023

Change

#### (2023-R07) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410)
  * The following versions are no longer available in the Stable channel: 
    * 1.22.17-gke.3100
    * 1.23.16-gke.1100
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.



## March 03, 2023

Change

#### (2023-R06) Version updates

  * Version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.14100
    * 1.23.14-gke.1800
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.



## February 22, 2023

Change

#### (2023-R05) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
  * The following versions are no longer available in the Stable channel: 
    * 1.22.16-gke.2000
    * 1.24.9-gke.1500
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.



## February 10, 2023

Change

#### (2023-R04) Version updates

  * Version [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) is now available in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.5300
    * 1.21.14-gke.7100
    * 1.21.14-gke.8500
    * 1.22.15-gke.2500
    * 1.23.13-gke.900
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.16-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.



## February 02, 2023

Change

#### (2023-R02) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.21.14-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.24.9-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.4300
    * 1.24.8-gke.401
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.9-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.



## January 13, 2023

Change

#### (2023-R02) Version updates

  * Version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) is now the default version in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.



## January 05, 2023

Change

#### (2023-R01) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.22.16-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216)
    * [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314)
    * [1.24.8-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248)
  * The following versions are no longer available in the Stable channel: 
    * 1.22.15-gke.100
    * 1.23.11-gke.300
    * 1.24.7-gke.900
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.8-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) with this release.



## December 14, 2022

Change

#### (2022-R28) Version updates

  * Version 1.23.13-gke.900 is now the default version in the Stable channel
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313) with this release.



## December 05, 2022

Change

#### (2022-R27) Version updates

  * Version [1.23.11-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12311) is now the default version in the Stable channel
  * The following versions are now available in the Stable channel: 
    * [1.21.14-gke.8500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313)
    * [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247)
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.3000
    * 1.22.12-gke.2300
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to version [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247) with this release.



## November 04, 2022

Change

#### (2022-R26) Version updates

  * Version [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) is now the default version in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.24 to [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) with this release.



## October 19, 2022

Change

#### (2022-R25) Version updates

  * Version [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.11-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12311)
  * The following versions are no longer available in the Stable channel: 
    * 1.21.14-gke.2700
    * 1.22.12-gke.1200
    * 1.23.8-gke.1900
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.21.14-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to [1.23.11-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12311) with this release.



## October 05, 2022

Change

(2022-R24) Version updates 

  * The following versions are now available in the Stable channel: 
    * [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)



## September 23, 2022

Change

#### (2022-R23) Version updates

  * Version [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) is now the default version in the Stable channel.

  * The following versions are now available in the Stable channel: 

    * [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
  * The following versions are no longer available in the Stable channel: 

    * 1.21.14-gke.700
    * 1.22.12-gke.500
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.




Change

_2022-09-22_ update: Updated new default versions for the [2022-R22](https://cloud.google.com/kubernetes-engine/docs/release-notes-stable#September_13_2022) release in the _Stable channel_.

## September 13, 2022

Change

#### (2022-R22) Version updates

  * Version [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel:

    * [1.21.14-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
  * The following versions are no longer available in the Stable channel:

    * 1.20.15-gke.11400
    * 1.21.13-gke.900
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.




## September 02, 2022

Change

#### (2022-R21) Version updates

  * The following versions are now available in the Stable channel:

    * [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238)
  * Version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) is now the default version in the Stable channel.

  * The following versions are no longer available in the Stable channel:

    * 1.21.12-gke.2200
    * 1.22.10-gke.600
    * 1.23.7-gke.1400
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.




## August 18, 2022

Change

#### (2022-R20) Version updates

  * Version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) is now the default version in the Stable channel.
  * Version [1.20.15-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now available in the Stable channel.
  * Version 1.20.15-gke.9900 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.20.15-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.



## August 04, 2022

Change

#### (2022-R19) Version updates

  * The following versions are now available in the Stable channel:

    * [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
  * Version 1.21.12-gke.2200 is now the default version in the Stable channel

  * The following versions are no longer available in the Stable channel:

    * 1.21.12-gke.1700
    * 1.22.8-gke.201
    * 1.22.8-gke.202
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210) with this release.




## July 26, 2022

Change

#### (2022-R18) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.20.15-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113)
    * [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210)
    * [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237)
  * Version 1.21.12-gke.1700 is now the default version in the Stable channel
  * The following versions are no longer available in the Stable channel: 
    * 1.20.15-gke.8700
    * 1.21.12-gke.1500
    * 1.22.8-gke.200
    * 1.23.6-gke.2200
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.20.15-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237) with this release.



## July 19, 2022

Change

#### (2022-R17) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.20.15-gke.8700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
    * [1.23.6-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
  * The following versions are no longer available in the Stable channel: 
    * 1.20.15-gke.8200
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.23 to version [1.23.6-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236) with this release.



## June 30, 2022

Change

#### (2022-R16) Version updates

  * Version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.20.15-gke.8200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
  * The following versions are no longer available in the Stable channel: 
    * 1.19.16-gke.11800
    * 1.19.16-gke.13800
    * 1.20.15-gke.8000
    * 1.21.11-gke.1900
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.



## June 23, 2022

Change

#### (2022-R15) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.19.16-gke.13800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
  * The following versions are no longer available in the Stable channel: 
    * 1.19.16-gke.11000
    * 1.20.15-gke.6000
    * 1.21.11-gke.1100
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.



## June 13, 2022

Change

#### (2022-R14) Version updates

  * Version [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now the default version in the Stable channel.
  * Version [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) is now available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.



## May 26, 2022

Change

#### (2022-R13) Version updates

  * Version [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now the default version in the Stable channel.

  * The following versions are now available in the Stable channel: 

    * [1.19.16-gke.11800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
  * The following versions are no longer available in the Stable channel: 

    * 1.19.16-gke.10800
    * 1.20.15-gke.5200
    * 1.21.11-gke.900
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.20.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to version [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.




## May 19, 2022

Change

#### (2022-R12) Version updates

  * Version [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now the default version in the Stable channel.

  * The following versions are now available in the Stable channel: 

    * [1.19.16-gke.11000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
    * [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
  * The following versions are no longer available in the Stable channel: 

    * 1.19.16-gke.9900
    * 1.20.15-gke.3400
    * 1.20.15-gke.3600
    * 1.20.15-gke.4100
    * 1.21.10-gke.2000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.16-gke.10800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.




## May 11, 2022

Change

#### (2022-R11) Version updates

  * The following versions are now available in the Stable channel: 

    * [1.19.16-gke.10800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.5200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
  * Version 1.19.16-gke.9400 is no longer available in the Stable channel.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.16-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.16-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.




## May 03, 2022

Change

#### (2022-R10) Version updates

  * Version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) is now the default version in the Stable channel.

  * The following versions are now available in the Stable channel:

    * [1.19.16-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.4100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
  * The following versions are no longer available in the Stable channel: 

    * 1.19.16-gke.9200
    * 1.20.15-gke.2500
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.22 to [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.




## April 21, 2022

Change

#### (2022-R9) Version updates

  * Version [1.20.15-gke.3400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now the default version in the Stable channel.

  * The following versions are now available in the Stable channel:

    * [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
  * The following versions are no longer available in the Stable channel:

    * 1.19.16-gke.8300
    * 1.20.15-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.19.16-gke.9200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.20.15-gke.3400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.20.15-gke.3400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.




## April 11, 2022

Change

#### (2022-R8) Version updates

  * Version [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel: 
    * [1.19.16-gke.9200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.3400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110)
  * The following versions are no longer available in the Stable channel: 
    * 1.19.16-gke.6800
    * 1.20.15-gke.300
    * 1.21.5-gke.1805
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.19.16-gke.8300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to version [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.



## March 31, 2022

Change

#### (2022-R07) Version updates

  * The following versions are now available in the Stable channel:

    * [1.19.16-gke.8300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916).
    * [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015).
  * The following versions are no longer available in the Stable channel:

    * 1.19.16-gke.6100
    * 1.20.12-gke.1500
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.16-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.16-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.




## March 21, 2022

Change

#### (2022-R6) Version updates

  * Version [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now the default version in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.



## March 14, 2022

Change

#### (2022-R5) Version updates

  * Version [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel:

    * [1.19.16-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
  * The following versions are no longer available in the Stable channel:

    * 1.19.16-gke.3600
    * 1.20.11-gke.1801
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.16-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.




## March 07, 2022

Change

#### (2022-R4) Version updates

  * The following versions are now available in the Stable channel:

    * [1.19.16-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916).
    * [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015).
  * The following versions are no longer available in the Stable channel: 

    * 1.19.16-gke.1500 
    * 1.20.11-gke.1300
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.16-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.16-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.21.5-gke.1805](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.




## February 24, 2022

Change

#### (2022-R03) Version updates

  * Version [1.19.16-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) is now available in the Stable channel.
  * Version [1.21.5-gke.1805](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) is now available in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.19.15-gke.1801
    * 1.21.5-gke.1802
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.21.5-gke.1805](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.



## February 03, 2022

Change

#### (2022-R02) Version updates

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.16-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.16-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.



## January 21, 2022

Change

#### (2022-R01) Version updates

  * Version [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012) is now the default version in the Stable channel.
  * Version [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) is now available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.21 to [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.



## December 06, 2021

Change

#### (2021-R34) Version updates

  * Version [1.20.11-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011) is now the default version in the Stable channel.
  * The following control plane and node versions are now available in the Stable channel: 
    * [1.19.15-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * [1.19.16-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.11-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)
    * [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012)
  * The following versions are no longer available in the Stable channel: 
    * 1.19.15-gke.500, 1.19.15-gke.1300, 1.20.10-gke.1600
  * The following control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded with this release: 
    * From version 1.18 to [1.19.15-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * From version 1.19 to [1.20.11-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)
    * From version 1.20 to [1.20.11-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)



## November 15, 2021

Change

#### (2021-R33) Version updates

  * The following control plane and node versions are now available: 
    * [1.19.15-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * [1.20.11-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)
  * Version 1.19.14-gke.1900 is no longer available in the Stable channel.
  * The following control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded with this release: 
    * From version 1.18 to [1.19.15-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * From version 1.19 to [1.19.15-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)



## October 29, 2021

Change

#### Revisions for 2021-R32

_2021-12-03 update_ : Revised upgrade versions. Control planes and nodes with auto-upgrade enabled will be upgraded:

  * From version 1.18 to [1.19.14-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1914).
  * From version 1.19 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010).



Change

#### (2021-R32) Version updates

  * Version [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) is now the default version in the Stable channel.
  * Version [1.19.15-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1915) is now available in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.19.13-gke.1900
    * 1.20.10-gke.301
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.14-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11914) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.



## October 15, 2021

Change

#### (2021-R31) Version updates

  * Version [1.19.13-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) is now the default version in the Stable channel.
  * The following versions are now available in the Stable channel:

    * [1.19.14-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11914)
    * [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010)
  * Version 1.19.13-gke.1200 is no longer available in the Stable channel.

  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.13-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) with this release.




## October 01, 2021

Change

#### (2021-R30) Version updates

  * Version [1.19.13-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) is now the default version.
  * The following control plane and node versions are now available in the Stable channel: 
    * [1.19.13-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913)
    * [1.20.10-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010)
  * The following versions are no longer available in the Stable channel: 
    * 1.19.13-gke.701
    * 1.20.9-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.13-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.20.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) with this release.



## September 17, 2021

Change

#### (2021-R29) Version updates

  * Version [1.19.13-gke.701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) is now the default version in the Stable channel.
  * Version [1.19.13-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) is now available in the Stable channel.
  * Version [1.20.9-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) is now available in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.18.20-gke.901
    * 1.18.20-gke.3001
    * 1.19.12-gke.2101
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.13-gke.701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.20 to [1.20.9-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) with this release.



## September 07, 2021

Change

This note was updated on September 24, 2021. Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.

Change

#### (2021-R28) Version updates

  * Version [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) is now the default version in the Stable channel.
  * The following control plane and node versions are now available in the Stable channel: 
    * [1.18.20-gke.3001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912)
    * [1.19.13-gke.701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913)
  * The following versions are no longer available in the Stable channel: 
    * 1.18.20-gke.3000
    * 1.19.12-gke.2100
    * 1.19.13-gke.700
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.



## August 20, 2021

Change

#### (2021-R27) Version updates

There are no new releases in the Stable channel.

## August 12, 2021

Change

#### (2021-R26) Version updates

  * Version [1.19.12-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) is now the default version in the Stable channel.
  * Version [1.18.20-gke.901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) is now available in the Stable channel.
  * Version 1.19.11-gke.2101 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 and version 1.19 to [1.19.12-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.



## August 03, 2021

Change

#### (2021-R25) Version updates

  * Version [1.18.20-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) is now the default version in the Stable channel.
  * Version 1.18.20-gke.501 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.20-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) with this release.



## July 27, 2021

Change

#### (2021-R24) Version updates

  * Version [1.18.20-gke.501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) is now the default version in the Stable channel.
  * Version [1.18.20-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) is now available in the Stable channel.
  * Version [1.19.12-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) is now available in the Stable channel.
  * Version 1.18.19-gke.1701 is no longer available in the Stable channel.
  * Version 1.19.10-gke.1000 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.20-gke.501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.19.11-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11911) with this release.



## July 20, 2021

Change

#### (2021-R23) Version updates

  * Version [1.18.19-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11819) is now the default version in the Stable channel.
  * Version [1.18.20-gke.501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) is now available in the Stable channel.
  * Version 1.18.17-gke.1901 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.19-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11819) with this release.



## July 09, 2021

Change

#### (2021-R22) Version updates

  * Version [1.18.19-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11819) is now available in the Stable channel.
  * Version [1.19.11-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11911) is now available in the Stable channel.
  * Version 1.18.18-gke.1700 is no longer available in the Stable channel.



## June 25, 2021

Change

#### (2021-R21) Version updates

  * Version [1.18.18-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11818) is now available in the Stable channel.
  * Version 1.18.17-gke.1900 is no longer available in the Stable channel.
  * Version 1.18.18-gke.1100 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.17 to version [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.



## June 16, 2021

Change

#### (2021-R20) Version updates

  * Version [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version in the Stable channel.
  * Version [1.18.18-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11818) is now available in the Stable channel.
  * Version 1.18.17-gke.1200 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.



## June 09, 2021

Change

#### (2021-R19) Version updates

  * Version [1.18.17-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version in the Stable channel.
  * Version [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now available in the Stable channel.
  * Version [1.19.10-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.17-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.19 to version [1.19.10-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) with this release.



## May 28, 2021

Change

#### (2021-R18) Version updates

  * Version [1.18.17-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version in the Stable channel.
  * Version [1.18.17-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now available in the Stable channel.
  * Version 1.17.17-gke.4900 is no longer available in the Stable channel.
  * Version 1.17.17-gke.5400 is no longer available in the Stable channel.
  * Version 1.18.17-gke.700 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.17-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.



## May 19, 2021

Change

#### (2021-R17) Version updates

  * Version [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version in the Stable channel.
  * Version [1.18.17-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now available in the Stable channel.
  * Version 1.18.17-gke.100 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.17 to version [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.



## May 12, 2021

Change

#### (2021-R16) Version updates

  * Version [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now available in the Stable channel.
  * The following control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded with this release: 
    * From version 1.17 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).
    * From version 1.18 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).



## May 04, 2021

Change

#### (2021-R15) Version updates

  * Version [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version in the Stable channel.
  * Version [1.17.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.17.17-gke.3700
    * 1.18.16-gke.2100
  * The following control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded with this release: 
    * From version 1.17 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).
    * From version 1.18 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).



## April 27, 2021

Change

#### (2021-R14) Version updates

  * Version [1.17.17-gke.4900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available in the Stable channel.
  * Version [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now available in the Stable channel
  * Version 1.18.16-gke.302 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.



## April 20, 2021

Change

#### (2021-R13) Version updates

  * Version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now the default version in the Stable channel.
  * Version [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now available in the Stable channel.
  * Version 1.17.17-gke.3000 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.16 to version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.17 to version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.18 to version [1.18.16-gke.302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.



## April 14, 2021

Change

#### (2021-R12) Version updates

  * Version [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now the default version in the Stable channel.
  * Version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available in the Stable channel.
  * Version 1.17.17-gke.2800 is no longer available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.16 to version [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.17 to version [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.



## April 06, 2021

Change

#### (2021-R11) Version updates

  * The following versions are now available in the Stable channel: 
    * [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717)
    * [1.18.16-gke.302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816)



## March 29, 2021

Change

#### (2021-R10) Version updates

  * Version [1.17.17-gke.2800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now the default version in the Stable channel.
  * The following versions are no longer available in the Stable channel: 
    * 1.16.15-gke.7801
    * 1.17.17-gke.1101
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from versions 1.17 and earlier to version [1.17.17-gke.2800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.



## March 23, 2021

Announcement

Starting tomorrow, March 24, 2021, the mechanism we use to create GKE release notes will change. Although this change does not affect the content of the notes, it does affect the presentation and underlying syntax. If you subscribe to the XML feed for this page, entries for March 24 and earlier will be updated as a result of changes to formatting and syntax; the content itself did not change.

The feed URL will also change from `https://cloud.google.com/feeds/kubernetes-engine-release-notes.xml` to `https://cloud.google.com/feeds/gke-main-release-notes.xml`. We will automatically redirect from the old URL to the new one.

## March 16, 2021

Change

#### (2021-R9) Version updates

  * Version [1.17.17-gke.2800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available in the Stable channel.
  * Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from versions 1.17 and earlier to version [1.17.17-gke.1101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Version 1.17.17-gke.1100 is no longer available in the Stable channel.



## March 05, 2021

Change

#### (2021-R8) Version updates

  * Version [1.17.17-gke.1101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available in the Stable channel. This version is now the default.
  * Auto-upgrading nodes and control planes in the Stable channel upgrade from versions 1.17 and earlier to version [1.17.17-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Version 1.15.12-gke.6002 is no longer available in the Stable channel.
  * Version 1.16.15-gke.7800 is no longer available in the Stable channel.
  * Version 1.17.15-gke.800 is no longer available in the Stable channel.



## February 25, 2021

Change

#### (2021-R7) Version updates

  * Version [1.16.15-gke.7801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available in the Stable channel.
  * Version [1.17.17-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available in the Stable channel.
  * Version [1.17.17-gke.1101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available in the Stable channel.



## February 17, 2021

Change

February 23, 2021 updates: version 1.15.12-gke.6002 is still available; it is not removed from the Stable channel.

Change

#### (2021-R6) Version updates

  * Version 1.16.15-gke.6000 is no longer available in the Stable channel.
  * Auto-upgrading control planes in the Stable channel automatically upgrade from version 1.0.0 to version [1.16.15-gke.7800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.



## February 09, 2021

Change

February 10, 2021 updates: The node auto-upgrade from 1.15 to version 1.16.15-gke.6000 was removed from the Stable channel. The version 1.17.14-gke.1600 is no longer available in the Stable channel.

Change

#### (2021-R5) Version updates

  * Version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) is now available in the Stable channel. This version is now the default.
  * Version 1.17.14-gke.1600 is no longer available in the Stable channel.
  * Auto-upgrading control planes in the Stable channel automatically upgrade from version 1.15 to version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.
  * Auto-upgrading control planes in the Stable channel automatically upgrade from version 1.16 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading control planes in the Stable channel automatically upgrade from version 1.17 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.15 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.16 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.17 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.



Change

February 23, 2021 updates: The auto-upgrade from 1.15 to version 1.16.15-gke.6000 was changed from nodes to control planes. The control plane auto-upgrades from 1.16 and 1.17 to 1.17.15-gke.800 was added to this channel. The node upgrades from 1.15, 1.16, and 1.17 to version 1.17.15-gke.800 were added to this channel.

## February 02, 2021

Change

This note was updated on February 10, 2021. The node auto-upgrade from 1.15 to version 1.16.15-gke.6000 was removed from this channel.

Change

#### (2021-R4) Version updates

  * Version [1.16.15-gke.7800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available in the Stable channel.
  * Version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) is now available in the Stable channel.



## January 19, 2021

Change

#### (2021-R2) Version updates

  * Version [1.17.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available in the Stable channel.
  * Version 1.17.14-gke.1200 is no longer available in the Stable channel.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.15 to version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.17 to version [1.17.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) with this release.



## January 08, 2021

Change

#### (2021-R1) Version updates

  * Version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available in the Stable channel. This version is now the default.
  * Version [1.17.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available in the Stable channel.
  * Version 1.15.12-gke.20 is no longer available in the Stable channel.
  * Version 1.15.12-gke.6001 is no longer available in the Stable channel.
  * Version 1.16.15-gke.4300 is no longer available in the Stable channel.
  * Version 1.16.15-gke.4301 is no longer available in the Stable channel.
  * Version 1.16.15-gke.4901 is no longer available in the Stable channel.
  * Version 1.16.15-gke.5500 is no longer available in the Stable channel.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.16 to version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.



## December 14, 2020

Change

#### (R41) Version updates

  * Version [1.16.15-gke.4901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available in the Stable channel. This version is now the default.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.16 to version [1.16.15-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.



## December 07, 2020

Change

#### (R40) Version updates

  * Version [1.15.12-gke.6002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available in the Stable channel.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.16 to version [1.16.15-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.



## December 01, 2020

Change

#### (R39) Version updates

  * Version [1.16.15-gke.4901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available in the Stable channel.
  * Version [1.16.15-gke.4301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available in the Stable channel.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.16 to version [1.16.13-gke.404](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) with this release.



## November 25, 2020

Issue

GKE Auto-Upgrade is currently suspended for control planes, and nodes. Manual upgrades are available.

## November 24, 2020

Change

The November 17, 2020 release removed the following GKE version.

  * Version 1.16.13-gke.401 is no longer available in the Stable channel.



## November 17, 2020

Change

#### (R38) Version updates

  * 1.16.15-gke.4300 is now the default version in the Stable.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.16 to version [1.16.13-gke.404](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) with this release.



Change

This note was updated on November 24, 2020.

## November 12, 2020

Change

#### (R37) Version updates

  * There are no new releases in the Stable release channel.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.15 to version [1.16.13-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) with this release.



## November 04, 2020

Change

#### (R36) Version updates

  * Version [1.15.12-gke.6001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available in the Stable channel.



## October 20, 2020

Change

#### (R34) Version updates

  * Version [1.16.13-gke.403](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available in the Stable channel.
  * Auto-upgrading control planes from version 1.15 to version 1.16.13-gke.401 during this release.



## October 12, 2020

Change

#### (R33) Version updates

  * Auto-upgrading control planes upgrade from version 1.14 to version 1.15.12-gke.20 during this release.
  * Auto-upgrading control planes upgrade from version 1.15 to version 1.16.13-gke.401 during this release.



## October 02, 2020

Change

#### (R32) Version updates

  * Version 1.16.13-gke.401 is the new default version in the Stable channel.
  * Version 1.16.13-gke.1 is no longer available in the Stable channel.
  * Auto-upgrading nodes and control planes upgrade from version 1.15 to version 1.15.12-gke.20 during this release.
  * Auto-upgrading nodes and control planes upgrade from version 1.16 to version 1.16.13-gke.401 during this release.



## September 25, 2020

Announcement

**Coming soon**

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes.

GKE will begin gradually upgrading clusters in the Stable channel to GKE 1.16 beginning on or after October 6, 2020. To read about API deprecations in 1.16, see [Kubernetes 1.16 deprecated APIs](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-16).

Change

#### (R31) Version updates

  * Version [1.16.13-gke.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available in the Stable channel.
  * Version [1.16.13-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available in the Stable channel.



## September 15, 2020

Change

#### (R30) Version updates

  * Version 1.15.12-gke.20 is the new default version in the Stable channel.
  * Version 1.15.12-gke.2 is no longer available in the Stable channel.



## September 14, 2020

Change

#### (R29.1) Version updates

  * Version [1.16.13-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available in the Stable channel.



Issue

There is a known issue that prevents creating Stable channel clusters on 1.16. To create a 1.16 cluster on the Stable channel, create a Stable channel cluster on 1.15, and then manually upgrade to 1.16.

## September 03, 2020

Change

#### (R29) Version updates

  * Version [1.16.13-gke.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available in the Stable channel.
  * Version 1.15.12-gke.9 is no longer available in the Stable channel.



Announcement

Google Kubernetes Engine will begin gradually upgrading clusters in the [Stable channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels) to GKE 1.16 in an upcoming release. To read about API deprecations in 1.16, see [Kubernetes 1.16 deprecated APIs](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-16).

## August 27, 2020

Change

#### (R28) Version updates

  * Auto-upgrading nodes in the Stable channel continue upgrading from version 1.14 to 1.15.12-gke.2 during this release. All auto-upgrading nodes that have not yet upgraded to 1.15.12-gke.2 will upgrade during the R28 rollout.



## July 28, 2020

Change

#### (R25) Version updates

  * GKE continues to upgrade control planes in clusters on the Stable channel to 1.15.12-gke.2. Upgrades will proceed gradually over several GKE releases.
  * GKE begins to upgrade nodes in clusters on the Stable channel to 1.15.12-gke.2. Upgrades will proceed gradually over several GKE releases.



## July 22, 2020

Change

#### (R24) Version updates

  * Version [1.15.12-gke.9](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available in the Stable channel.
  * Auto-upgrading nodes in the Stable channel automatically upgrade from version 1.14 to version [1.15.12-gke.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) with this release.



## July 13, 2020

Fixed

A bug in gVisor has been fixed. Default gVisor node labels are now applied when user-specified labels.

Announcement

We expect the following changes in the coming weeks. This information is not a guarantee, but is provided to help you plan for upcoming changes.

  * In the next release (R24), GKE will begin to upgrade control planes in clusters on the **Stable channel** to 1.15.12-gke.2. Upgrades will proceed gradually over several GKE releases.

  * In an upcoming release, GKE will begin to upgrade nodes in clusters on the **Stable channel** to 1.15.12-gke.2. Upgrades will proceed gradually over several GKE releases.




Change

#### (R23) Version updates

  * Version [1.14.10-gke.46](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available in the Stable channel.
  * Version [1.15.12-gke.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available in the Stable channel.



## May 13, 2020

Change

[1.14.10-gke.36](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available in the Stable release channel.

## March 26, 2020

Change

[1.14.10-gke.27](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1149) is now available in the Stable release channel.

## March 16, 2020

Change

[1.14.10-gke.24](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1149) is now available in the Stable release channel.

## February 11, 2020

Change

1.14.10-gke.17 is the default for new Stable channel clusters.

**Important:** Existing clusters enrolled in the Stable release channel will be auto-upgraded to this version.

## January 22, 2020

Change

1.13.11-gke.23 is the default for new Stable channel clusters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
