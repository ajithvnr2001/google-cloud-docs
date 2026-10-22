---
url: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular/
title: GKE release notes (Regular channel) \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:06.070541+00:00
---

# GKE release notes (Regular channel)  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE release notes (Regular channel) Stay organized with collections  Save and categorize content based on your preferences. 

This page documents Google Kubernetes Engine version updates in the Regular [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). 

For all Google Kubernetes Engine version updates, fixes, known issues, or new features, see [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).

For more detailed information about security-related known issues, see the [security bulletin](https://docs.cloud.google.com/kubernetes-engine/docs/security-bulletins) page.

To view release notes for versions prior to 2020, see the [Release notes archive](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gke-regular-channel-release-notes.xml) directly. 

**Note** : Your clusters might not have the latest released versions. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

## October 14, 2026

Change

#### (2026-R44) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.1495002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.12-gke.1011000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)
    * [1.35.8-gke.1796000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)
    * [1.36.4-gke.1495003](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)
    * [1.36.4-gke.2046002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)
    * [1.36.4-gke.2046003](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046003)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.11-gke.1102000
    * 1.35.8-gke.1439001
    * 1.36.4-gke.1391002
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
      * 1.34 to [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
      * 1.35 to [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
      * 1.36 to [1.36.4-gke.1495003](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495003)



## October 08, 2026

Change

#### (2026-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.1391002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
    * [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
    * [1.36.4-gke.1391002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)
    * [1.36.4-gke.1495002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.11-gke.1056000
    * 1.35.8-gke.1380001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1225000
    * 1.36.4-gke.1247000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.4-gke.1391000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
      * 1.34 to [1.35.8-gke.1439001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
      * 1.35 to [1.35.8-gke.1439001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)
      * 1.36 to [1.36.4-gke.1391002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)



## October 02, 2026

Change

#### (2026-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
    * [1.35.8-gke.1380001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)
    * [1.35.8-gke.1439001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)
    * [1.36.4-gke.1391000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.11-gke.1044000
    * 1.35.8-gke.1380000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1767000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
      * 1.34 to [1.35.8-gke.1380001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
      * 1.35 to [1.35.8-gke.1380001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)
      * 1.36 to [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)



## September 23, 2026

Change

#### (2026-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.8-gke.1225000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
    * [1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
    * [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.10-gke.1328000
    * 1.35.8-gke.1036000
    * 1.36.4-gke.1082000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)
      * 1.34 to [1.35.8-gke.1225000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)
      * 1.35 to [1.35.8-gke.1225000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)



## September 17, 2026

Change

#### (2026-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.8-gke.1036000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)
    * [1.35.8-gke.1225000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)
    * [1.36.4-gke.1082000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.10-gke.1236000
    * 1.35.7-gke.1222000
    * 1.36.3-gke.1640000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1328000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)
      * 1.34 to [1.35.8-gke.1036000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1328000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)
      * 1.35 to [1.35.8-gke.1036000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)
      * 1.36 to [1.36.3-gke.1767000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)



## September 08, 2026

Change

#### (2026-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.7-gke.1222000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.10-gke.1328000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)
    * [1.35.8-gke.1036000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)
    * [1.36.3-gke.1767000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.10-gke.1106000
    * 1.35.7-gke.1150000
    * 1.36.3-gke.1537000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1236000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)
      * 1.34 to [1.35.7-gke.1222000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1236000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1236000)
      * 1.35 to [1.35.7-gke.1222000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)
      * 1.36 to [1.36.3-gke.1640000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)



## September 02, 2026

Change

#### (2026-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.10-gke.1079000
    * 1.35.7-gke.1027000
    * 1.36.2-gke.2064000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.34 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
      * 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)



## August 26, 2026

Change

#### (2026-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available in the Regular channel: 
    * 1.34.9-gke.1655001
    * 1.35.6-gke.1710000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.34 to [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.35 to [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)



## August 20, 2026

Change

#### (2026-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.13-gke.1269000
    * 1.33.13-gke.1329000
    * 1.34.9-gke.1610000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1655000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1641000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)



## August 14, 2026

Change

#### (2026-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.13-gke.1109000
    * 1.34.9-gke.1322000
    * 1.35.6-gke.1258000
    * 1.36.2-gke.1346000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)



## August 12, 2026

Change

#### (2026-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.13-gke.1101000
    * 1.34.9-gke.1287000
    * 1.35.6-gke.1250000
    * 1.36.2-gke.1498000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)



## July 30, 2026

Change

#### (2026-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.1498000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.13-gke.1011000
    * 1.34.9-gke.1131000
    * 1.35.6-gke.1127000
    * 1.36.0-gke.4447000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.4681000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.2-gke.1346000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)



## July 24, 2026

Change

#### (2026-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.2-gke.1346000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.12-gke.1270000
    * 1.34.9-gke.1065000
    * 1.35.6-gke.1049000
    * 1.36.0-gke.3712000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## July 16, 2026

Change

#### (2026-R30) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.12-gke.1165000
    * 1.34.8-gke.1278000
    * 1.35.5-gke.1241004
    * 1.36.0-gke.3070003 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.3302004 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## July 10, 2026

Change

#### (2026-R29) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.3302004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## July 09, 2026

Change

#### (2026-R28) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.33.12-gke.1116000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1218000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1163012
    * 1.36.0-gke.2684000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



Change

#### (2026-R27) Version updates

There are no version updates for 2026-R27.

## June 29, 2026

Change

#### (2026-R26) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.12-gke.1059000
    * 1.34.8-gke.1126000
    * 1.35.5-gke.1057002
    * 1.36.0-gke.2459000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## June 26, 2026

Change

#### (2026-R25) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.12-gke.1000000
    * 1.34.8-gke.1000000
    * 1.35.5-gke.1000000
    * 1.35.5-gke.1057000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)



Change

#### (2026-R24) Version updates

There are no version updates for 2026-R24.

## June 12, 2026

Change

#### (2026-R23) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.11-gke.1197000
    * 1.34.7-gke.1499000
    * 1.35.3-gke.2190000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## June 04, 2026

Change

#### (2026-R22) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.11-gke.1074000
    * 1.34.7-gke.1055000
    * 1.35.3-gke.1389002
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.33 to [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.34 to [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## May 27, 2026

Change

#### (2026-R21) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.11-gke.1013000
    * 1.34.6-gke.1307000
    * 1.35.3-gke.1389000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.33 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.34 to [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## May 21, 2026

Change

#### (2026-R20) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now available in the Regular channel.



## May 13, 2026

Change

#### (2026-R19) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
  * The following versions are no longer available in the Regular channel: 
    * 1.33.10-gke.1176000
    * 1.34.6-gke.1237000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.33 to [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)



## May 06, 2026

Change

#### (2026-R18) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.13-gke.1258000
    * 1.32.13-gke.1318000
    * 1.33.10-gke.1115000
    * 1.34.6-gke.1154000
    * 1.35.3-gke.1234000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.10-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.33 to [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.34 to [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.10-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.34 to [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 29, 2026

Change

#### (2026-R17) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.13-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.12-gke.1127000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1059000
    * 1.32.13-gke.1090000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1147000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1205000
    * 1.33.8-gke.1169000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.9-gke.1060000
    * 1.33.9-gke.1117000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.9-gke.1166000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.10-gke.1067000
    * 1.34.4-gke.1193000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.5-gke.1076000
    * 1.34.5-gke.1153000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.5-gke.1208000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1068000
    * 1.35.1-gke.1396002
    * 1.35.2-gke.1269001
    * 1.35.2-gke.1485000
    * 1.35.2-gke.1842000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1962000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.32 to [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.33 to [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.34 to [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.33 to [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.34 to [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 22, 2026

Change

#### (2026-R16) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 15, 2026

Change

#### (2026-R15) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.32.13-gke.1205000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.2-gke.1962000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## April 09, 2026

Change

#### (2026-R14) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.32.13-gke.1147000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1842000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## April 02, 2026

Change

#### (2026-R13) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.32.13-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1117000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1153000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1485000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## March 25, 2026

Change

#### (2026-R12) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.1-gke.1396002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.12-gke.1076000
    * 1.33.8-gke.1112000
    * 1.34.4-gke.1130000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.33 to [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)



## March 18, 2026

Change

#### (2026-R11) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.1-gke.1396002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.12-gke.1026000
    * 1.33.8-gke.1026000
    * 1.34.4-gke.1047000
    * 1.35.0-gke.2745005 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.0-gke.3047002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.1-gke.1396001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.33 to [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
      * 1.35 to [1.35.1-gke.1396002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)



## March 12, 2026

Change

#### (2026-R10) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.1-gke.1396001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.11-gke.1264000
    * 1.33.5-gke.2469000
    * 1.34.3-gke.1444000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.33 to [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)



## March 05, 2026

Change

#### (2026-R9) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2745005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.11-gke.1211000
    * 1.33.5-gke.2392000
    * 1.34.3-gke.1318000
    * 1.35.0-gke.2398002
    * 1.35.0-gke.2745004
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2745005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 25, 2026

Change

#### (2026-R8) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2745004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.11-gke.1174000
    * 1.33.5-gke.2326000
    * 1.34.3-gke.1245000
    * 1.35.0-gke.2232003
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2398002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 19, 2026

Change

#### (2026-R7) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2232003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2398002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.11-gke.1038000
    * 1.33.5-gke.2228001
    * 1.34.3-gke.1051003
    * 1.35.0-gke.2232000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2232003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 11, 2026

Change

#### (2026-R6) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * Version 1.33.5-gke.2172001 is no longer available in the Regular channel.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.35 to [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 04, 2026

Change

#### (2026-R5) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation in the Regular channel.
  * Version [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now available in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.32.9-gke.1734000
    * 1.33.5-gke.2118001
    * 1.34.1-gke.3971002
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)



## January 29, 2026

Change

#### (2026-R4) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3971002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available in the Regular channel: 
    * 1.32.9-gke.1728000
    * 1.33.5-gke.2100000
    * 1.33.5-gke.2118000
    * 1.34.1-gke.3947002
    * 1.34.1-gke.3971001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3971002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 21, 2026

Change

#### (2026-R3) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3947002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3971001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.14-gke.1156000
    * 1.31.14-gke.1166000
    * 1.32.9-gke.1711000
    * 1.33.5-gke.2072000
    * 1.34.1-gke.3899001
    * 1.34.1-gke.3947000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3947002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 15, 2026

Change

#### (2026-R2) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.14-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3947000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.14-gke.1114000
    * 1.32.9-gke.1675000
    * 1.33.5-gke.2019000
    * 1.34.1-gke.3355004
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.31 to [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.32 to [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3899001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 07, 2026

Change

#### (2026-R1) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3899001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.13-gke.1139000
    * 1.31.14-gke.1033000
    * 1.31.14-gke.1081000
    * 1.32.9-gke.1239000
    * 1.32.9-gke.1575000
    * 1.32.9-gke.1632000
    * 1.33.5-gke.1308000
    * 1.33.5-gke.1862000
    * 1.33.5-gke.1956000
    * 1.34.1-gke.2909002
    * 1.34.1-gke.3084002
    * 1.34.1-gke.3355002
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.31 to [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.32 to [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3355004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 05, 2026

Change

#### (2025-R54) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## December 29, 2025

Change

#### (2025-R53) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## December 18, 2025

Change

#### (2025-R52) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

There are no new releases in the Regular channel.

## December 10, 2025

Change

#### (2025-R51) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.31.14-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1862000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.13-gke.1454000
    * 1.32.9-gke.1548000
    * 1.33.5-gke.1791000



## December 05, 2025

Change

#### (2025-R50) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1454000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1548000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1791000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2909002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3084002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.13-gke.1040000
    * 1.31.13-gke.1123000
    * 1.31.13-gke.1231000
    * 1.31.13-gke.1377000
    * 1.32.9-gke.1130000
    * 1.32.9-gke.1207000
    * 1.32.9-gke.1330000
    * 1.32.9-gke.1462000
    * 1.33.5-gke.1201000
    * 1.33.5-gke.1350000
    * 1.33.5-gke.1521000
    * 1.33.5-gke.1697000
    * 1.34.1-gke.2909000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.2909002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## November 28, 2025

Change

#### (2025-R49) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1377000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1462000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2909000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.1-gke.2909000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## November 20, 2025

Change

#### (2025-R48) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1330000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1521000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## November 14, 2025

Change

#### (2025-R47) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## November 07, 2025

Change

#### (2025-R46) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.13-gke.1023000
    * 1.32.9-gke.1108000
    * 1.33.5-gke.1162000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 29, 2025

Change

#### (2025-R45) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.13-gke.1008000
    * 1.32.9-gke.1092000
    * 1.33.5-gke.1125000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 22, 2025

Change

#### (2025-R44) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.12-gke.1265000
    * 1.32.9-gke.1072000
    * 1.33.5-gke.1080000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 15, 2025

Change

#### (2025-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Regular channel: 
    * 1.31.12-gke.1220000
    * 1.32.9-gke.1010000
    * 1.33.4-gke.1350000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 08, 2025

Change

#### (2025-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.14-gke.1150000
    * 1.30.14-gke.1267000
    * 1.31.11-gke.1036000
    * 1.32.8-gke.1170000
    * 1.33.4-gke.1245000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.31 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)



## October 02, 2025

Change

#### (2025-R41) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.14-gke.1130000
    * 1.31.12-gke.1110000
    * 1.32.8-gke.1134000
    * 1.33.4-gke.1172000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 29, 2025

Change

#### (2025-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.14-gke.1108000
    * 1.31.12-gke.1083000
    * 1.32.8-gke.1108000
    * 1.33.4-gke.1134000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 18, 2025

Change

#### (2025-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.14-gke.1059000
    * 1.31.12-gke.1060000
    * 1.32.8-gke.1026000
    * 1.33.4-gke.1036000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 11, 2025

Change

#### (2025-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.14-gke.1036000
    * 1.31.12-gke.1014000
    * 1.32.7-gke.1079000
    * 1.33.3-gke.1136000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 03, 2025

Change

#### (2025-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.14-gke.1011000
    * 1.31.11-gke.1101000
    * 1.32.7-gke.1016000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.



## August 27, 2025

Change

#### (2025-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1414000
    * 1.31.11-gke.1064000
    * 1.32.6-gke.1125000
    * 1.33.2-gke.1240000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.



## August 21, 2025

Change

#### (2025-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1390000
    * 1.31.11-gke.1002000
    * 1.32.6-gke.1096000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 14, 2025

Change

#### (2025-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1372000
    * 1.31.10-gke.1067000
    * 1.32.6-gke.1060000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 06, 2025

Change

#### (2025-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1340000
    * 1.31.10-gke.1034000
    * 1.32.6-gke.1025000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 01, 2025

Change

#### (2025-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1333000
    * 1.31.10-gke.1021000
    * 1.32.6-gke.1013000
    * 1.33.2-gke.1111000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.



## July 25, 2025

Change

#### (2025-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1168000
    * 1.30.12-gke.1208000
    * 1.30.12-gke.1246000
    * 1.30.12-gke.1279000
    * 1.30.12-gke.1320000
    * 1.31.9-gke.1044001
    * 1.31.9-gke.1119000
    * 1.31.9-gke.1176000
    * 1.31.9-gke.1218000
    * 1.31.9-gke.1287000
    * 1.32.4-gke.1415000
    * 1.32.4-gke.1603000
    * 1.32.4-gke.1698000
    * 1.32.4-gke.1767000
    * 1.33.1-gke.1107000
    * 1.33.1-gke.1386000
    * 1.33.1-gke.1584000
    * 1.33.1-gke.1744000
    * 1.33.2-gke.1043000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.



## July 16, 2025

Change

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## July 11, 2025

Change

#### (2025-R29) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## July 02, 2025

Change

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)



## June 27, 2025

Change

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)



## June 18, 2025

Change

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1151000
    * 1.31.9-gke.1005000
    * 1.32.4-gke.1353003
    * 1.33.0-gke.2248000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.



## June 12, 2025

Change

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1086000
    * 1.31.8-gke.1113000
    * 1.32.4-gke.1236007
    * 1.32.4-gke.1353001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.



## June 05, 2025

Change

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.12-gke.1033000
    * 1.31.8-gke.1045000
    * 1.32.4-gke.1106006
    * 1.32.4-gke.1236006
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.



Change

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

## May 30, 2025

Change

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.11-gke.1217000
    * 1.31.7-gke.1390000
    * 1.32.3-gke.1927009
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.



Change

#### (2025-R21) Version updates

There are no version updates for 2025-R21.

## May 23, 2025

Change

#### (2025-R20) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.11-gke.1157000
    * 1.31.7-gke.1265000
    * 1.32.3-gke.1785003
    * 1.32.3-gke.1927002
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.



## May 16, 2025

Change

#### (2025-R19) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1927002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.11-gke.1131000
    * 1.31.7-gke.1212000
    * 1.32.2-gke.1297002
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.



## May 09, 2025

Change

#### (2025-R18) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.10-gke.1070000
    * 1.31.6-gke.1064001
    * 1.32.2-gke.1182003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## May 02, 2025

Change

#### (2025-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)



## April 28, 2025

Change

#### (2025-R16) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are no longer available in the Regular channel: 
    * 1.29.14-gke.1018000
    * 1.29.14-gke.1067000



## April 18, 2025

Change

#### (2025-R15) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available in the Regular channel: 
    * 1.30.10-gke.1022000
    * 1.31.6-gke.1020000
    * 1.31.6-gke.1064000
    * 1.32.1-gke.1357001
    * 1.32.2-gke.1182001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## April 08, 2025

Change

#### (2025-R14) Version updates

There are no new releases in the Regular channel.

## April 02, 2025

Change

#### (2025-R13) Version updates

There are no new releases in the Regular channel.

## March 26, 2025

Change

#### (2025-R12) Version updates

There are no new releases in the Regular channel.

## March 19, 2025

Change

#### (2025-R11) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now available in the Regular channel.
  * Version 1.32.2-gke.1182000 is no longer available in the Regular channel.



## March 12, 2025

Change

#### (2025-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.29.14-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available in the Regular channel: 
    * 1.29.13-gke.1169000
    * 1.30.9-gke.1201000
    * 1.31.5-gke.1233000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.



## March 05, 2025

Change

#### (2025-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
  * The following versions are no longer available in the Regular channel: 
    * 1.29.13-gke.1109000
    * 1.30.9-gke.1127000
    * 1.31.5-gke.1169000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.



## February 26, 2025

Change

#### (2025-R08) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available in the Regular channel: 
    * 1.29.13-gke.1038000
    * 1.30.9-gke.1046000
    * 1.31.5-gke.1068000
    * 1.32.1-gke.1200003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) with this release.



## February 18, 2025

Change

#### (2025-R07) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Regular channel: 
    * 1.29.13-gke.1006000
    * 1.30.9-gke.1009000
    * 1.31.5-gke.1023000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.



## February 11, 2025

Change

#### (2025-R06) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.15-gke.1612000
    * 1.28.15-gke.1641000
    * 1.29.12-gke.1270000
    * 1.30.8-gke.1261000
    * 1.31.4-gke.1372000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) with this release.



## February 06, 2025

Change

#### (2025-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.15-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.15-gke.1503000
    * 1.29.12-gke.1143000
    * 1.29.12-gke.1143001
    * 1.30.8-gke.1162000
    * 1.30.8-gke.1162001
    * 1.31.4-gke.1256000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 29, 2025

Change

#### (2025-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1143001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.15-gke.1480000
    * 1.29.12-gke.1120000
    * 1.30.8-gke.1128000
    * 1.31.4-gke.1183000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 23, 2025

Change

#### (2025-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.15-gke.1435000
    * 1.29.12-gke.1055000
    * 1.30.8-gke.1051000
    * 1.31.3-gke.1162000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 14, 2025

Change

#### (2025-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.15-gke.1342000
    * 1.28.15-gke.1362000
    * 1.29.10-gke.1280000
    * 1.30.6-gke.1596000
    * 1.30.7-gke.1084000
    * 1.31.1-gke.2105000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.3-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313) with this release.



## January 07, 2025

Change

#### (2025-R01) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.15-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.7-gke.1084000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.3-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.15-gke.1159000
    * 1.29.10-gke.1227000
    * 1.30.6-gke.1125000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) with this release.



## December 26, 2024

Change

**(2024-R50) Version updates**

There are no new releases in the Regular channel.

## December 18, 2024

Change

**(2024-R49) Version updates**

There are no new releases in the Regular channel.

## December 12, 2024

Change

#### (2024-R48) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.15-gke.1020000
    * 1.28.15-gke.1080000
    * 1.29.10-gke.1054000
    * 1.29.10-gke.1155000
    * 1.30.5-gke.1699000
    * 1.30.5-gke.1713000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) with this release.



## December 10, 2024

Change

#### (2024-R47) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.15-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.14-gke.1340000
    * 1.28.14-gke.1376000
    * 1.29.9-gke.1496000
    * 1.29.9-gke.1541000
    * 1.30.5-gke.1443001
    * 1.31.1-gke.1846000
    * 1.31.1-gke.2008000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## November 27, 2024

Change

#### (2024-R46) Version updates

There are no new releases in the Regular channel.

## November 19, 2024

Change

#### (2024-R45) Version updates

There are no new releases in the Regular channel.

## November 13, 2024

Change

#### (2024-R44) Version updates

GKE cluster versions have been updated.

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.28.14-gke.1376000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.9-gke.1541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.2008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)



## November 06, 2024

Change

#### (2024-R43) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.28.14-gke.1217000
    * 1.29.9-gke.1341000
    * 1.30.5-gke.1355000
    * 1.31.1-gke.1678000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## October 30, 2024

Change

#### (2024-R42) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available in the Regular channel: 
    * 1.28.14-gke.1099000
    * 1.29.9-gke.1177000
    * 1.30.5-gke.1014001
    * 1.30.5-gke.1014003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## October 25, 2024

Change

#### (2024-R41) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## October 17, 2024

Change

#### (2024-R40) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are no longer available in the Regular channel: 
    * 1.28.14-gke.1004000
    * 1.29.8-gke.1278000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.



## October 11, 2024

Change

#### (2024-R39) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.16-gke.1342000
    * 1.27.16-gke.1373000
    * 1.28.13-gke.1119000
    * 1.29.8-gke.1211000
    * 1.30.4-gke.1348000
    * 1.30.4-gke.1348001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## October 03, 2024

Change

#### (2024-R38) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1373000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.16-gke.1287000
    * 1.28.13-gke.1049000
    * 1.29.8-gke.1096000
    * 1.30.3-gke.1969001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.



## September 26, 2024

Change

#### (2024-R37) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.16-gke.1148001
    * 1.27.16-gke.1258000
    * 1.28.13-gke.1006000
    * 1.28.13-gke.1024000
    * 1.29.8-gke.1031000
    * 1.29.8-gke.1057000
    * 1.30.3-gke.1639000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.



## September 19, 2024

Change

#### (2024-R36) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## September 11, 2024

Change

#### (2024-R35) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.16-gke.1148000
    * 1.28.12-gke.1179000
    * 1.29.7-gke.1274000
    * 1.30.3-gke.1969000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.



## September 06, 2024

Change

#### (2024-R34) Version updates

There are no new releases in the Regular channel.

Change

#### (2024-R33) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version for cluster creation in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.16-gke.1051000
    * 1.27.16-gke.1082000
    * 1.28.12-gke.1052000
    * 1.29.7-gke.1104000
    * 1.30.3-gke.1225000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## August 28, 2024

Change

#### (2024-R32) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)



## August 20, 2024

Change

#### (2024-R31) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) is now the default version in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.27.16-gke.1008000
    * 1.28.11-gke.1315000
    * 1.29.7-gke.1008000
    * 1.30.2-gke.1587003
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## August 14, 2024

Change

#### (2024-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.15-gke.1252000
    * 1.28.11-gke.1260000
    * 1.29.6-gke.1326000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.



## August 12, 2024

Change

### (2024-R29) Version updates

There are no new releases in the Regular channel.

## August 07, 2024

Change

### (2024-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.15-gke.1154000
    * 1.28.11-gke.1172000
    * 1.29.6-gke.1254000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## July 31, 2024

Change

### (2024-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
  * The following versions are no longer available in the Regular channel: 
    * 1.27.14-gke.1059002
    * 1.28.11-gke.1019001
    * 1.29.6-gke.1038001
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302) with this release.



## July 23, 2024

Change

### (2024-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)



## July 17, 2024

Change

### (2024-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.27.14-gke.1042001
    * 1.27.14-gke.1059001
    * 1.28.10-gke.1075001
    * 1.29.5-gke.1091002
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## July 10, 2024

Change

### (2024-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.27.14-gke.1059001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.15-gke.1320000
    * 1.26.15-gke.1320002
    * 1.26.15-gke.1381000
    * 1.26.15-gke.1381001
    * 1.26.15-gke.1390000
    * 1.26.15-gke.1390001
    * 1.27.13-gke.1201000
    * 1.27.13-gke.1201002
    * 1.27.14-gke.1022000
    * 1.27.14-gke.1022001
    * 1.27.14-gke.1042000
    * 1.28.9-gke.1289000
    * 1.28.9-gke.1289002
    * 1.28.10-gke.1058000
    * 1.28.10-gke.1058001
    * 1.28.10-gke.1075000
    * 1.29.4-gke.1043002
    * 1.29.4-gke.1043004
    * 1.29.5-gke.1060000
    * 1.29.5-gke.1060001
    * 1.29.5-gke.1091000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.



## July 08, 2024

Change

### (2024-R23) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) is now the default version in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.15-gke.1320002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.15-gke.1320002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## July 03, 2024

Change

### (2024-R22) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1320002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1381001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1390001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.27.14-gke.1022001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.10-gke.1058001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.5-gke.1060001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)



## June 26, 2024

Change

#### (2024-R21) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1091000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)



## June 18, 2024

Change

#### (2024-R20) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.15-gke.1090000
    * 1.27.13-gke.1166000
    * 1.28.9-gke.1209000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.13-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## June 12, 2024

Change

#### (2024-R19) Version updates

  * The following versions are no longer available in the Regular channel: 
    * 1.27.13-gke.1070000
    * 1.28.9-gke.1000000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.13-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## June 07, 2024

Change

Updated [2024-R13 release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#May_08_2024) to indicate that control planes and nodes with auto-upgrade enabled in the Regular channel were _not_ upgraded from version 1.28 to version 1.29.1-gke.1589018. That release note was published by mistake.

## June 06, 2024

Change

#### (2024-R18) Version updates

  * Version [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.15-gke.1300000
    * 1.27.13-gke.1000000
    * 1.29.1-gke.1589020
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## May 28, 2024

Change

#### (2024-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1300000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.15-gke.1243000
    * 1.27.12-gke.1115000
    * 1.28.8-gke.1095000
    * 1.28.9-gke.1069000
    * 1.29.4-gke.1043001
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.13-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.13-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## May 21, 2024

Change

#### (2024-R16) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1243000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1069000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.4-gke.1043001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.15-gke.1191000
    * 1.28.7-gke.1026000



## May 17, 2024

Change

#### (2024-R14) Version updates

There are no version updates for 2024-R14.

#### (2024-R15) Version updates

  * Version [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1191000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.8-gke.200
    * 1.27.11-gke.1062001
    * 1.27.11-gke.1062003
    * 1.28.7-gke.1026001
    * 1.29.1-gke.1589018
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.1-gke.1589020](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## May 08, 2024

Change

The 2024-R13 release notes were updated on June 7th, 2024 with the following:

**Regular channel**

Control planes and nodes with auto-upgrade enabled in the Regular channel were **not** upgraded from version 1.28 to version 1.29.1-gke.1589018. That release note was published by mistake

Change

#### (2024-R13) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1026001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.1-gke.1589020](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.14-gke.1044000
    * 1.29.1-gke.1589017
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.29.1-gke.1589018](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.1-gke.1589018](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## May 01, 2024

Change

#### (2024-R12) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) is now available in the Regular channel.
  * Version 1.27.11-gke.1062000 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.



## April 30, 2024

Change

#### (2024-R11) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712)
    * [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
  * The following versions are no longer available in the Regular channel: 
    * 1.25.16-gke.1537000
    * 1.25.16-gke.1570000
    * 1.26.14-gke.1006000
    * 1.27.10-gke.1055000
    * 1.28.3-gke.1286000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.



## April 18, 2024

Change

#### (2024-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) is now the default version in the Regular channel.
  * Version [1.25.16-gke.1570000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) is now available in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.25.16-gke.1460000
    * 1.27.8-gke.1067004
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) with this release.



## April 08, 2024

Change

#### (2024-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * There are no new releases in the Regular release channel.



## March 20, 2024

Change

**(2024-R08) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.1-gke.1589018](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available in the Regular channel: 
    * 1.26.13-gke.1144000
    * 1.27.9-gke.1092000
    * 1.28.5-gke.1217000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.14-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.14-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.



## March 07, 2024

Change

**(2024-R07) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.29.1-gke.1589017](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available in the Regular channel: 
    * 1.25.16-gke.1360000
    * 1.26.13-gke.1052000
    * 1.29.0-gke.1381000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.29.1-gke.1589017](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## March 04, 2024

Change

**(2024-R06) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * There are no new releases in the Regular release channel.



## February 23, 2024

Change

#### (2024-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
  * The following versions are no longer available in the Regular channel: 
    * 1.25.16-gke.1268000
    * 1.26.12-gke.1111000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.16-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.13-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.13-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.



## February 13, 2024

Change

#### (2024-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.25.16-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.10-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
  * The following versions are no longer available in the Regular channel: 
    * 1.25.16-gke.1041000
    * 1.26.11-gke.1055000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.12-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12612) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.12-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12612) with this release.



## February 08, 2024

Change

#### (2024-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278) is now the default version in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.26.6-gke.1700
    * 1.27.3-gke.100
    * 1.28.3-gke.1118000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611) with this release.



## January 26, 2024

Change

#### (2024-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Regular channel: 
    * [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.12-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12612)
    * [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278)
    * [1.27.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1279)
    * [1.28.5-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1285)
    * [1.29.0-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1290)
  * The following versions are no longer available in the Regular channel: 
    * 1.24.17-gke.2266000
    * 1.24.17-gke.2364000
    * 1.25.15-gke.1115000
    * 1.26.10-gke.1101000
    * 1.27.7-gke.1121000
    * 1.27.8-gke.1067000
    * 1.28.3-gke.1203001
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## January 11, 2024

Change

#### (2024-R01) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.24.17-gke.2364000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611)
    * [1.27.8-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278)
    * [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Regular channel: 
    * 1.24.17-gke.2230000
    * 1.25.13-gke.200
    * 1.26.10-gke.1073000
    * 1.27.7-gke.1056000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.7-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277) with this release.



## December 12, 2023

Change

#### (2023-R26) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.26.10-gke.1073000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.28.3-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Regular channel: 
    * 1.24.17-gke.200
    * 1.27.3-gke.1700
    * 1.27.5-gke.200
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.7-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277) with this release.



## December 04, 2023

Change

#### (2023-R25) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Regular channel: 
    * 1.24.16-gke.500
    * 1.25.12-gke.500
    * 1.26.7-gke.500
    * 1.27.4-gke.900
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.13-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12513) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.13-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12513) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.28 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## November 17, 2023

Change

#### (2023-R24) Version updates

  * There are no new releases in the Regular release channel.



## November 09, 2023

Change

#### (2023-R23) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.13-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12513)
    * [1.26.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1268)
    * [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275)
  * The following versions are no longer available in the Regular channel: 
    * 1.24.15-gke.1700
    * 1.25.11-gke.1700
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to [1.25.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12512) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to [1.25.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12512) with this release.



## October 05, 2023

Change

#### (2023-R19) Version updates

  * There are no new releases in the Regular release channel.



## September 05, 2023

Change

#### (2023-R18) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416)
    * [1.25.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12512)
    * [1.26.7-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1267)
    * [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274)
  * The following versions are no longer available in the Regular channel: 1.23.17-gke.10000, 1.24.14-gke.2700, 1.25.10-gke.2700, 1.26.5-gke.2700
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.11-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12511) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1266) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1266) with this release.



## August 08, 2023

Change

#### (2023-R17) Version updates

  * Version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.23.17-gke.10000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415)
    * [1.25.11-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12511)
    * [1.26.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1266)
    * [1.27.3-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.17-gke.14100
    * 1.23.17-gke.8400
    * 1.24.14-gke.1400
    * 1.25.10-gke.1400
    * 1.26.5-gke.1400
    * 1.27.2-gke.1200
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.10000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) with this release.



## July 26, 2023

Change

#### (2023-R16) Version updates

  * Version [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.22.17-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.18800
    * 1.22.17-gke.12700
    * 1.23.17-gke.7000
    * 1.24.14-gke.1200
    * 1.25.10-gke.1200
    * 1.26.5-gke.1200
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.17-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.10-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## July 07, 2023

Change

#### (2023-R15) Version updates

  * The following versions are now available in the Regular channel: 

    * [1.23.17-gke.7000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
  * The following versions are no longer available in the Regular channel:

    * 1.23.17-gke.6800
    * 1.24.13-gke.2500
    * 1.25.9-gke.2300
    * 1.26.3-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.7000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.




## June 27, 2023

Change

#### (2023-R14) Version updates

  * Version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.17-gke.11400
    * 1.23.17-gke.5600
    * 1.24.12-gke.1000
    * 1.25.8-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## June 15, 2023

Change

#### (2023-R13) Version updates

  * Version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.22.17-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259)
    * [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.17-gke.8000
    * 1.23.17-gke.2000
    * 1.25.8-gke.500
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.17-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.27 to version [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) with this release.



## June 07, 2023

Change

#### (2023-R12) Version updates

  * Version [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) is now available in the Regular channel.
  * Version 1.24.12-gke.500 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.



## June 05, 2023

Change

#### (2023-R11) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
    * [1.26.3-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.17-gke.7500
    * 1.23.17-gke.1700
    * 1.24.11-gke.1000
    * 1.26.2-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.3-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263) with this release.



## May 09, 2023

Change

#### (2023-R10) Version updates

  * Version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) is now the default version.
  * The following versions are now available in the Regular channel: 
    * [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.17-gke.6100
    * 1.23.17-gke.300
    * 1.24.10-gke.2300
    * 1.25.7-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.



## April 19, 2023

Change

#### (2023-R09) Version updates

  * Version [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.23.17-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.26.2-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1262)
  * Version 1.23.16-gke.2500 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.17-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.17-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.26 to version [1.26.2-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1262) with this release.



## March 31, 2023

Change

#### (2023-R08) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411)
    * [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257)
  * Version [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) is now the default version in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.18100
    * 1.22.17-gke.5400
    * 1.24.9-gke.3200
    * 1.25.6-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.22.17-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257) with this release.



## March 22, 2023

Change

#### (2023-R07) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410)
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.15800
    * 1.22.17-gke.4000
    * 1.23.16-gke.1100
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.



## March 03, 2023

Change

#### (2023-R06) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.17-gke.3100
    * 1.23.16-gke.200
    * 1.25.6-gke.200
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.



## February 22, 2023

Change

#### (2023-R05) Version updates

  * Version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.6-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256)
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.14600
    * 1.22.16-gke.2000
    * 1.23.14-gke.1800
    * 1.24.9-gke.2000
    * 1.25.5-gke.2000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.16-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.6-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.



## February 10, 2023

Change

#### (2023-R04) Version updates

  * Version [1.24.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) is now the default version in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.7100
    * 1.21.14-gke.8500
    * 1.22.15-gke.1000
    * 1.22.15-gke.2500
    * 1.22.16-gke.1300
    * 1.23.14-gke.401
    * 1.24.8-gke.2000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.16-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.



## February 02, 2023

Change

#### (2023-R02) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.24.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255)
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.5300
    * 1.24.7-gke.900
    * 1.25.4-gke.2100
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255) with this release.



## January 13, 2023

Change

#### (2023-R02) Version updates

  * Version [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) is now the default version in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.14-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) with this release.



## January 05, 2023

Change

#### (2023-R01) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.22.16-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216)
    * [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314)
    * [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248)
    * [1.25.4-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.15-gke.100
    * 1.23.13-gke.900
    * 1.24.5-gke.600
    * 1.25.3-gke.800
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.14-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.14-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.4-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254) with this release.



## December 14, 2022

Change

#### (2022-R28) Version updates

  * Version [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247) is now the default version in the Regular channel
  * The following versions are now available in the Regular channel: 
    * [1.22.16-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216)
    * [1.23.14-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314)
    * [1.25.3-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1253)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.13-gke.1000
    * 1.23.12-gke.1600
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.25 to version [1.25.3-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1253) with this release.



## December 05, 2022

Change

#### (2022-R27) Version updates

  * Version [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) is now the default version in the Regular channel
  * The following versions are now available in the Regular channel: 
    * [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313)
    * [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247)
  * The following versions are no longer available in the Regular channel: 
    * 1.22.12-gke.2300
    * 1.23.12-gke.100
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.13-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12213) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.23.12-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.12-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) with this release.



## November 04, 2022

Change

#### (2022-R26) Version updates

  * Version [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.21.14-gke.8500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214)
    * [1.22.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.12-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312)
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.4300
    * 1.22.12-gke.500
    * 1.23.8-gke.1900
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) with this release.



## October 19, 2022

Change

#### (2022-R25) Version updates

  * Version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312)
    * [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245)
  * The following versions are no longer available in the Regular channel: 
    * 1.21.14-gke.2700
    * 1.22.12-gke.300
    * 1.24.2-gke.1900
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) with this release.



## October 05, 2022

Change

(2022-R24) Version updates 

  * The following versions are now available in the Regular channel: 

    * [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.13-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12213)



## September 23, 2022

Change

#### (2022-R23) Version updates

  * Version [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) is now the default version in the Regular channel.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.




## September 13, 2022

Change

#### (2022-R22) Version updates

  * Version [1.22.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) is now the default version in the Regular channel.

  * The following versions are now available in the Regular channel:

    * [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
  * The following versions are no longer available in the Regular channel:

    * 1.20.15-gke.12800
    * 1.21.14-gke.2100
    * 1.22.11-gke.400
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.22.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.




## September 02, 2022

Change

#### (2022-R21) Version updates

  * The following versions are now available in the Regular channel:

    * [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238)
  * The following versions are no longer available in the Regular channel:

    * 1.21.14-gke.700
    * 1.23.7-gke.1400
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.14-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.11-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12211) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.




## August 18, 2022

Change

#### (2022-R20) Version updates

  * Version [1.22.11-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12211) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.20.15-gke.12800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.14-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.24.2-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.15-gke.11400
    * 1.21.13-gke.900
    * 1.22.10-gke.600
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.20.15-gke.12800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.22.11-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12211) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.24 to version [1.24.2-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242) with this release.



## August 04, 2022

Change

#### (2022-R19) Version updates

  * The following versions are now available in the Regular channel:

    * [1.20.15-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.11-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12211)
  * The following versions are no longer available in the Regular channel:

    * 1.20.15-gke.9900
    * 1.21.12-gke.2200
    * 1.22.8-gke.202
    * 1.23.5-gke.1503
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.20.15-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237) with this release.




## July 26, 2022

Change

#### (2022-R18) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237)
  * Version [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210) is now the default version in the Regular channel
  * The following versions are no longer available in the Regular channel: 
    * 1.23.5-gke.1501
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.20.15-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210) with this release.



## July 19, 2022

Change

#### (2022-R17) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.20.15-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113)
    * [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.15-gke.8700
    * 1.21.12-gke.1700
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.



## June 30, 2022

Change

#### (2022-R16) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.20.15-gke.8700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.15-gke.8200
    * 1.21.12-gke.1500
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.



## June 23, 2022

Change

#### (2022-R15) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.20.15-gke.8200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.15-gke.8000
    * 1.21.11-gke.1900
    * 1.22.8-gke.201
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.20.15-gke.8200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.



## June 13, 2022

Change

#### (2022-R14) Version updates

  * Version [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
    * [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
    * [1.23.5-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.15-gke.6000
    * 1.21.11-gke.1100
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to version [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to version [1.23.5-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.



## May 26, 2022

Change

#### (2022-R13) Version updates

  * Version [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) is now the default version in the Regular channel.
  * Version 1.22.8-gke.200 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.



## May 19, 2022

Change

#### (2022-R12) Version updates

  * Version [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 

    * [1.20.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
    * [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
  * The following versions are no longer available in the Regular channel: 

    * 1.20.15-gke.5200
    * 1.21.9-gke.1002
    * 1.21.10-gke.400
    * 1.21.10-gke.2000
    * 1.21.11-gke.900
    * 1.22.6-gke.300
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.




## May 11, 2022

Change

#### (2022-R11) Version updates

  * Version [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 

    * [1.20.15-gke.5200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
  * The following versions are no longer available in the Regular channel:

    * 1.20.15-gke.5000
    * 1.21.6-gke.1503
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.15-gke.5200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.




## May 03, 2022

Change

#### (2022-R10) Version updates

  * The following versions are now available in the Regular channel: 

    * [1.20.15-gke.5000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
    * [1.23.5-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235)
  * The following versions are no longer available in the Regular channel:

    * 1.20.15-gke.4100
    * 1.21.5-gke.1805
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.15-gke.5000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.15-gke.5000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to [1.23.5-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.




## April 21, 2022

Change

#### (2022-R9) Version updates

  * Version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.20.15-gke.4100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
  * Version 1.20.15-gke.3600 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to version [1.19.16-gke.9200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.20.15-gke.4100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.



## April 11, 2022

Change

#### (2022-R8) Version updates

  * Version [1.20.15-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now available in the Regular channel.
  * Version 1.20.15-gke.2500 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to version [1.19.16-gke.8300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.20.15-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to version [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.



## March 31, 2022

Change

#### (2022-R07) Version updates

  * Version [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.21.5-gke.1805](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215).
    * [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216).
    * [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110).
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.



## March 21, 2022

Change

#### (2022-R6) Version updates

  * The following versions are now available in the Regular channel:

    * [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.10-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110)
  * The following versions are no longer available in the Regular channel:

    * 1.20.15-gke.1000
    * 1.21.6-gke.1503
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.




## March 14, 2022

Change

#### (2022-R5) Version updates

  * Version [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) is now the default version in the Regular channel.
  * Version [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now available in the Regular channel.
  * Version 1.20.15-gke.300 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) with this release.



## March 07, 2022

Change

#### (2022-R4) Version updates

  * The following versions are now available in the Regular channel: 
    * [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015).
    * [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219).
    * [1.22.6-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226).
  * The following versions are no longer available in the Regular channel: 

    * 1.20.12-gke.1500
    * 1.21.5-gke.1805
    * 1.22.3-gke.1500
    * 1.22.4-gke.1501
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.22.6-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) with this release.




## February 24, 2022

Change

#### (2022-R03) Version updates

  * Version [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now the default version in the Regular channel.
  * Version [1.21.5-gke.1805](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) is now available in the Regular channel.
  * Version [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now available in the Regular channel.
  * Version [1.22.4-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1224) is now available in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.20.11-gke.1801
    * 1.21.5-gke.1802
    * 1.21.6-gke.1500
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.22.4-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1224) with this release.



## February 03, 2022

Change

#### (2022-R02) Version updates

  * Version [1.22.3-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223) is now available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.



## January 21, 2022

Change

#### (2022-R01) Version updates

  * Version [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now the default version in the Regular channel.
  * Version [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now available in the Regular channel.
  * Version 1.21.5-gke.1302 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.



## December 06, 2021

Change

#### (2021-R34) Version updates

  * The following control plane and node versions are now available in the Regular channel: 
    * [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012)
    * [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.10-gke.2100, 1.21.3-gke.2003
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.11-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011) with this release.



## November 15, 2021

Change

#### (2021-R33) Version updates

  * Version [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) is now the default version in the Regular channel.
  * Version [1.20.11-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011) is now available in the Regular channel.
  * Version 1.20.10-gke.1600 is no longer available in the Regular channel.
  * The following control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded with this release: 
    * From version 1.19 to [1.20.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010)
    * From version 1.20 to [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
    * From version 1.21 to [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)



## October 29, 2021

Change

#### Revisions for 2021-R32

_2021-12-03 update_ : Revised upgrade versions. Control planes and nodes with auto-upgrade enabled will be upgraded:

  * From version 1.19 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010).



Change

#### (2021-R32) Version updates

  * Version [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.20.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010)
    * [1.21.3-gke.2003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213)
    * [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.9-gke.1001
    * 1.20.10-gke.301
    * 1.21.3-gke.2001
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.3-gke.2003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## October 15, 2021

Change

#### (2021-R31) Version updates

  * Version [1.20.10-gke.1600 ](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) is now available in the Regular channel.



## October 01, 2021

Change

#### (2021-R30) Version updates

  * Version [1.20.10-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) is now the default version in the Regular channel.
  * Version [1.21.3-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) is now available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.10-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.21 to [1.21.3-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## September 17, 2021

Change

#### (2021-R29) Version updates

  * Version [1.20.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) is now the default version in the Regular channel.
  * Version [1.20.10-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) is now available in the Regular channel.
  * Version 1.20.9-gke.701 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) with this release.



## September 07, 2021

Change

#### (2021-R28) Version updates

  * Version [1.20.9-gke.701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) is now the default version in the Regular channel.
  * The following control plane and node versions are now available in the Regular channel: 
    * [1.20.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
    * [1.20.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
  * The following versions are no longer available in the Regular channel: 
    * 1.20.9-gke.700
    * 1.20.9-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.9-gke.701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) with this release.



## August 20, 2021

Change

#### (2021-R27) Version updates

  * Version [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version in the Regular channel.
  * Version [1.20.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) is now available in the Regular channel.
  * Version 1.20.8-gke.900 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.



## August 12, 2021

Change

#### (2021-R26) Version updates

Version [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now available in the Regular channel.

## August 03, 2021

Change

#### (2021-R25) Version updates

There are no new releases in the Regular release channel.

## July 27, 2021

Change

#### (2021-R24) Version updates

  * Version [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.19.9-gke.1900
    * 1.19.11-gke.1701
    * 1.19.12-gke.1100
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.



## July 20, 2021

Change

#### (2021-R23) Version updates

  * Version [1.19.12-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) is now available in the Regular channel.
  * Version [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now available in the Regular channel.
  * Version 1.20.7-gke.1800 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.



## July 09, 2021

Change

#### (2021-R22) Version updates

  * Version [1.19.11-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11911) is now available in the Regular channel.
  * Version [1.20.7-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) is now available in the Regular channel.
  * Version 1.19.10-gke.1700 is no longer available in the Regular channel.
  * Version 1.20.6-gke.1000 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.7-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) with this release.



## June 25, 2021

Change

#### (2021-R21) Version updates

  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version in the Regular channel.
  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now available in the Regular channel.
  * Version 1.19.10-gke.1600 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to [1.19.10-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.19.10-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) with this release.



## June 16, 2021

Change

#### (2021-R20) Version updates

  * Version [1.19.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now the default version in the Regular channel.
  * Version [1.19.10-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now available in the Regular channel.
  * Version 1.19.9-gke.1900 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to [1.19.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.19.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) with this release.



## June 09, 2021

Change

#### (2021-R19) Version updates

  * Version [1.19.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now available in the Regular channel.
  * Version [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) is now available in the Regular channel.
  * Version 1.19.9-gke.1400 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.20 to [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) with this release.



## May 28, 2021

Change

#### (2021-R18) Version updates

  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version in the Regular channel.



## May 19, 2021

Change

#### (2021-R17) Version updates

  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now available in the Regular channel.
  * Version 1.18.17-gke.700 is no longer available in the Regular channel.



## May 12, 2021

Change

#### (2021-R16) Version updates

  * Version [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version in the Regular channel.
  * Version 1.18.17-gke.100 is no longer available in the Regular channel.
  * Version 1.19.8-gke.1600 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to version [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.



## May 04, 2021

Change

#### (2021-R15) Version updates

  * Version [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version in the Regular channel.
  * The following versions are now available in the Regular channel: 
    * [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817)
    * [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199)
  * Version 1.18.16-gke.2100 is no longer available in the Regular channel.
  * The following control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded with this release: 
    * From version 1.17 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).
    * From version 1.18 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).



## April 27, 2021

Change

#### (2021-R14) Version updates

  * Version [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now the default version in the Regular channel.
  * Version [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now available in the Regular channel.
  * Version 1.18.16-gke.502 is no longer available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.17 to version [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11816) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to version [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11816) with this release.



## April 20, 2021

Change

#### (2021-R13) Version updates

  * Version [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) is now available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.19 to version [1.19.8-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) with this release.



## April 14, 2021

Change

#### (2021-R12) Version updates

  * Version [1.19.8-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) is now available in the Regular channel.
  * Version 1.18.16-gke.302 is no longer available in the Regular channel.



## April 06, 2021

Change

#### (2021-R11) Version updates

  * Version [1.18.16-gke.502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now the default version.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.17 to version [1.18.16-gke.502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to version [1.18.16-gke.502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.



## March 29, 2021

Change

  * Version [1.18.16-gke.302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now the default version in the Regular channel.
  * Version [1.18.16-gke.502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now available in the Regular channel.
  * The following versions are no longer available in the Regular channel: 
    * 1.18.15-gke.1501
    * 1.18.15-gke.1502
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to version [1.18.16-gke.302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.



## March 23, 2021

Announcement

Starting tomorrow, March 24, 2021, the mechanism we use to create GKE release notes will change. Although this change does not affect the content of the notes, it does affect the presentation and underlying syntax. If you subscribe to the XML feed for this page, entries for March 24 and earlier will be updated as a result of changes to formatting and syntax; the content itself did not change.

The feed URL will also change from `https://cloud.google.com/feeds/kubernetes-engine-release-notes.xml` to `https://cloud.google.com/feeds/gke-main-release-notes.xml`. We will automatically redirect from the old URL to the new one.

## March 16, 2021

Change

#### (2021-R9) Version updates

  * Version [1.18.15-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now the default version in the Regular channel.
  * Version [1.18.15-gke.1502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available in the Regular channel.
  * Version [1.18.16-gke.302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now available in the Regular channel.
  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.18 to version [1.18.15-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) with this release.
  * Version 1.18.12-gke.1210 is no longer available in the Regular channel.



## March 05, 2021

Change

#### (2021-R8) Version updates

  * Version [1.18.15-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available in the Regular channel.
  * Version 1.18.15-gke.1102 is no longer available in the Regular channel.



## February 25, 2021

Change

#### (2021-R7) Version updates

  * Version [1.18.15-gke.1102](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available in the Regular channel.
  * Version 1.18.12-gke-1206 is no longer available in the Regular channel.
  * Auto-upgrading control planes in the Regular channel automatically upgrade from version 1.18 to version [1.18.12-gke.1210](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version [1.18.12-gke.1210](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## February 17, 2021

Change

#### (2021-R6) Version updates

  * Version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Regular channel. This version is now the default.
  * Version 1.17.14-gke.1600 is no longer available in the Regular channel.
  * Version 1.17.15-gke.800 is no longer available in the Regular channel.
  * Auto-upgrading control planes in the Regular channel automatically upgrade from version 1.17 to version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## February 09, 2021

Change

#### (2021-R5) Version updates

  * Version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) is now available in the Regular channel. This version is now the default.
  * Version [1.18.12-gke.1210](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Regular channel.
  * Version 1.18.12-gke.1205 is no longer available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.18 to version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## February 02, 2021

Change

#### (2021-R4) Version updates

  * Version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) is now available in the Regular channel.
  * Version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Regular channel.



## January 25, 2021

Change

#### (2021-R3) Version updates

  * Version [1.17.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available in the Regular channel. This version is now the default.
  * Version 1.17.14-gke.400 is no longer available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.17.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) with this release.



## January 19, 2021

Change

#### (2021-R2) Version updates

  * Version [1.17.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available in the Regular channel.
  * Version [1.18.12-gke.1205](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Regular channel.
  * Version 1.17.14-gke.1200 is no longer available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.18 to version [1.18.12-gke.1205](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## January 08, 2021

Change

#### (2021-R1) Version updates

  * Version [1.17.14-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available in the Regular channel. This version is now the default.
  * Version 1.17.13-gke.2600 is no longer available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.17.14-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) with this release.



## December 14, 2020

Change

#### (R41) Version updates

  * Version [1.17.13-gke.2600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available in the Regular channel. This version is now the default.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.17.13-gke.2600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) with this release.



## December 07, 2020

Change

#### (R40) Version updates

  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.17.13-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) with this release.



## December 01, 2020

Change

#### (R39) Version updates

  * Version [1.17.13-gke.1401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available in the Regular channel.
  * Version 1.17.13-gke.1400 is no longer available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.17.13-gke.1401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) with this release.
  * 1.17.13-gke.2001 is now the default version in the Regular channel.



## November 25, 2020

Issue

#### Auto-upgrade status

GKE Auto-Upgrade is currently suspended for control planes, and nodes. Manual upgrades are available.

## November 24, 2020

Change

The November 17, 2020 release removed the following GKE version: Version 1.17.12-gke.1504 is no longer available in the Regular channel.

## November 17, 2020

Change

#### (R38) Version updates

This note was updated on November 24, 2020.

  * Version [1.17.13-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.17 to version [1.17.13-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) with this release.



## November 12, 2020

Change

#### (R36) Version updates

  * Version [1.17.13-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available in the Regular channel.



## November 04, 2020

Change

#### (R36) Version updates

  * Version [1.17.12-gke.1504](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11712) is now available in the Regular channel.
  * Version [1.17.13-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available in the Regular channel.



## October 20, 2020

Change

#### (R34) Version updates

  * Version [1.17.12-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11712) is now available in the Regular channel.
  * Version [1.17.12-gke.1504](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11712) is now available in the Regular channel.
  * Version 1.17.12-gke.1504 is the new default version in the Regular channel.
  * Version 1.17.9-gke.1504 is no longer available in the Regular channel.
  * Version 1.17.9-gke.6300 is no longer available in the Regular channel.



## October 02, 2020

Change

#### (R32) Version updates

  * Version [1.17.9-gke.6300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Regular channel.
  * Version 1.17.9-gke.1504 is the new default version in the Regular channel.
  * Auto-upgrading control planes upgrade from versions 1.16 and 1.17 to version 1.17.9-gke.1504 during this release.
  * Version 1.16.13-gke.401 is no longer available.



## September 15, 2020

Change

#### (R30) Version updates

  * Version 1.16.13-gke.401 is the new default version in the Regular channel.
  * Auto-upgrading control planes upgrade from version 1.16 to version 1.16.13-gke.401 during this release.
  * Version [1.17.9-gke.1504](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Regular channel. 
    * This version is not yet the default version or an upgrade target.
    * To learn more about the changes contained in 1.17, see the following GKE and Kubernetes release notes: 
      * [1.17 changes.](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#1.17-changes)
      * [Changes.](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#changes)
      * [Deprecations and removals.](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#deprecations-and-removals)



## September 14, 2020

Change

#### (R29.1) Version updates

  * Version [1.16.13-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available in the Regular channel.



## August 20, 2020

Change

#### (R27) Version updates

  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.16.11-gke.5 to version [1.16.13-gke.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) with this release.
  * Version 1.16.11-gke.5 is no longer available.



## August 06, 2020

Change

#### (R26) Version updates

  * Version [1.16.3-gke.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1163) is now available in the Regular channel.
  * The COS image for GKE 1.16.3-gke.1 is [cos-81-12871-181-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m81#cos-81-12871-181-0).



## July 28, 2020

Change

#### (R25) Version updates

  * Version [1.16.13-gke.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.16.9-gke.6 to version [1.16.11-gke.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11611) with this release.



## July 22, 2020

Change

#### (R24) Version updates

  * Version [1.16.12-gke.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11612) is now available in the Regular channel.
  * Version [1.16.11-gke.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11611) is now available in the Regular channel.

This version is now the default.




## July 13, 2020

Fixed

A bug in gVisor has been fixed. Default gVisor node labels are now applied when user-specified labels.

Change

#### (R23) Version updates

  * Version [1.16.11-gke.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11611) is now available in the Regular channel.
  * Auto-upgrading nodes in the Regular channel automatically upgrade from version 1.16.8-gke.15 to version [1.16.9-gke.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1169) with this release.



## June 29, 2020

Change

[1.16.9-gke.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1169) is now available.

## June 01, 2020

Change

Auto-upgrading nodes in the Regular release channel automatically upgrade to version [1.16.8-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1168) in this release.

## May 19, 2020

Change

Existing clusters in the Regular release channel automatically upgrade to version [1.16.8-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1168) in this release.

## May 13, 2020

Change

[1.16.8-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1168) is now generally available for new clusters. Existing clusters and nodes will not automatically upgrade in this release.

Breaking

**Important**

Before you migrate to GKE 1.16, you **must** review:

  * [Deprecated APIs in 1.16.](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#deprecations-information)
  * [Known issues.](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#known-issues)
  * [Urgent upgrade notes.](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#urgent-upgrade-notes)



## April 01, 2020

Change

[1.15.9-gke.24](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v1158) is now available in the Regular release channel.

**Important:** Existing clusters enrolled in the Regular release channel will be auto-upgraded to this version.

## March 16, 2020

Feature

You can now use [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) to create node pools with preemptible VMs from clusters running in the Regular release channel.

Change

[1.15.9-gke.22](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v1158) is now available in the Regular release channel.

## March 06, 2020

Change

[1.15.9-gke.8](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v1158) is now available in the Regular release channel.

**Important:** Existing clusters enrolled in the Regular release channel will be auto-upgraded to this version.

## February 04, 2020

Change

1.15.7-gke.23 is now available in the Regular release channel.

**Important:** Existing clusters enrolled in the Regular release channel will be auto-upgraded to this version.

## January 22, 2020

Change

1.14.8-gke.33 is now available in the Regular release channel.

**Important:** Existing clusters enrolled in the Regular release channel will be auto-upgraded to this version.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
