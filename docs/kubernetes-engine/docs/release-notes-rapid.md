---
url: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid/
title: GKE release notes (Rapid channel) \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:09.937982+00:00
---

# GKE release notes (Rapid channel)  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE release notes (Rapid channel) Stay organized with collections  Save and categorize content based on your preferences. 

This page documents Google Kubernetes Engine version updates in the Rapid [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). 

For all Google Kubernetes Engine version updates, fixes, known issues, or new features, see [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).

For more detailed information about security-related known issues, see the [security bulletin](https://docs.cloud.google.com/kubernetes-engine/docs/security-bulletins) page.

To view release notes for versions prior to 2020, see the [Release notes archive](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gke-rapid-channel-release-notes.xml) directly. 

**Note** : Your clusters might not have the latest released versions. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

## October 14, 2026

Change

#### (2026-R44) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.37.1-gke.1552000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.12-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1209000)
    * [1.35.8-gke.1975000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1975000)
    * [1.36.4-gke.2377000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2377000)
    * [1.37.1-gke.1697000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1697000)
  * [Alpha version](https://cloud.google.com/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2884000+preview is now available for GKE alpha clusters in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.12-gke.1011000
    * 1.35.8-gke.1796000
    * 1.36.4-gke.2046002
    * 1.36.4-gke.2202002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.4-gke.2304000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.37.0-gke.3503000
  * Alpha version 1.38.0-gke.1002000+preview is no longer available in the Rapid channel.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.12-gke.1153000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)
      * 1.34 to [1.35.8-gke.1919000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)
      * 1.35 to [1.36.4-gke.2326000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.12-gke.1153000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)
      * 1.35 to [1.35.8-gke.1919000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)
      * 1.36 to [1.36.4-gke.2326000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)
      * 1.37 to [1.37.1-gke.1552000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)



## October 08, 2026

Change

#### (2026-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.2046002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.12-gke.1153000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)
    * [1.35.8-gke.1919000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)
    * [1.36.4-gke.2046002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)
    * [1.36.4-gke.2202002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)
    * [1.36.4-gke.2304000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)
    * [1.36.4-gke.2326000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)
    * [1.37.1-gke.1552000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-1-gke-1552000)
  * [Alpha version](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2743000+preview is now available for GKE alpha clusters in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.11-gke.1209000
    * 1.35.8-gke.1626001
    * 1.36.4-gke.1495000
    * 1.36.4-gke.2046000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.12-gke.1011000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)
      * 1.34 to [1.35.8-gke.1796000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)
      * 1.35 to [1.36.4-gke.2046002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.12-gke.1011000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)
      * 1.35 to [1.35.8-gke.1796000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)
      * 1.36 to [1.36.4-gke.2046002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)



## October 02, 2026

Change

#### (2026-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.1495000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.12-gke.1011000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)
    * [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
    * [1.35.8-gke.1796000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)
    * [1.36.4-gke.2046000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)
  * [Alpha version](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.2240000+preview is now available for GKE alpha clusters in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.11-gke.1102000
    * 1.35.8-gke.1439000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1626000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.4-gke.1391000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
      * 1.34 to [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
      * 1.35 to [1.36.4-gke.1495000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
      * 1.35 to [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
      * 1.36 to [1.36.4-gke.1495000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)



## September 23, 2026

Change

#### (2026-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.1391000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
    * [1.35.8-gke.1626000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)
    * [1.36.4-gke.1495000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)
  * [Alpha version](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) 1.38.0-gke.1002000+preview is now available for GKE alpha clusters in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.11-gke.1056000
    * 1.35.8-gke.1380000
    * 1.36.4-gke.1247000
    * 1.37.0-gke.3165000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
      * 1.34 to [1.35.8-gke.1439000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)
      * 1.35 to [1.36.4-gke.1391000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
      * 1.35 to [1.35.8-gke.1439000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)
      * 1.36 to [1.36.4-gke.1391000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)
      * 1.37 to [1.37.0-gke.3503000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)



## September 17, 2026

Change

#### (2026-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
    * [1.35.8-gke.1439000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)
    * [1.36.4-gke.1391000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)
    * [1.37.0-gke.3503000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3503000)
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.11-gke.1044000
    * 1.35.8-gke.1225000
    * 1.36.4-gke.1082000
    * 1.37.0-gke.2941000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
      * 1.34 to [1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
      * 1.35 to [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
      * 1.35 to [1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
      * 1.36 to [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)
      * 1.37 to [1.37.0-gke.3165000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3165000)



## September 08, 2026

Change

#### (2026-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.1082000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
    * [1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
    * [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)
    * [1.37.0-gke.3165000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-3165000)
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.10-gke.1328000
    * 1.35.8-gke.1036000
    * 1.36.3-gke.1767000
    * 1.37.0-gke.2155000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)
      * 1.34 to [1.35.8-gke.1225000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)
      * 1.35 to [1.36.4-gke.1082000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)
      * 1.35 to [1.35.8-gke.1225000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000)
      * 1.36 to [1.36.4-gke.1082000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1082000)
      * 1.37 to [1.37.0-gke.2941000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.37#1-37-0-gke-2941000)



## September 02, 2026

Change

#### (2026-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)
    * [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)
    * [1.37.0-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)
    * [1.37.0-gke.2941000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.10-gke.1236000
    * 1.35.7-gke.1222000
    * 1.35.8-gke.1026000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1640000
  * The following alpha versions are no longer available in the Rapid channel: 
    * 1.37.0-gke.2034000+preview
    * 1.37.0-gke.2048000+preview
    * 1.37.0-gke.2074000+preview
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.34 to [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
      * 1.35 to [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.35 to [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
      * 1.36 to [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
      * 1.37 to [1.37.0-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)



## August 26, 2026

Change

#### (2026-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following [alpha versions](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) are now available for GKE alpha clusters in the Rapid channel: 
    * [1.37.0-gke.2034000+preview](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)
    * [1.37.0-gke.2048000+preview](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)
    * [1.37.0-gke.2074000+preview](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370)
  * The following versions are no longer available in the Rapid channel: 
    * 1.34.10-gke.1106000
    * 1.35.7-gke.1150000
    * 1.36.3-gke.1537000
  * Alpha version 1.37.0-gke.1173000+preview is no longer available in the Rapid channel.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.34 to [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
      * 1.35 to [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.35 to [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
      * 1.36 to [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)



## August 20, 2026

Change

#### (2026-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.13-gke.1414000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.13-gke.1462000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.10-gke.1079000
    * 1.35.7-gke.1027000
    * 1.36.2-gke.2064000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.34 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
      * 1.35 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
      * 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)



## August 14, 2026

Change

#### (2026-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.33.13-gke.1462000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * [Alpha version](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) [1.37.0-gke.1173000+preview](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md#v1370) is now available for GKE alpha clusters in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.13-gke.1329000
    * 1.34.9-gke.1655000
    * 1.35.6-gke.1710000
    * 1.36.3-gke.1244000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1253000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.34 to [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
      * 1.35 to [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)



## August 12, 2026

Change

#### (2026-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.33.13-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1244000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
    * [1.36.3-gke.1253000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.13-gke.1269000
    * 1.34.9-gke.1610000
    * 1.35.6-gke.1641000
    * 1.36.2-gke.2281000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)



## July 30, 2026

Change

#### (2026-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.2281000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.13-gke.1109000
    * 1.34.9-gke.1322000
    * 1.35.6-gke.1258000
    * 1.35.6-gke.1638000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.2-gke.1498000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.35 to [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)



## July 24, 2026

Change

#### (2026-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.2-gke.1498000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1638000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.13-gke.1101000
    * 1.34.9-gke.1287000
    * 1.35.6-gke.1250000
    * 1.36.0-gke.4681000
    * 1.36.2-gke.1346000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.35 to [1.36.2-gke.1498000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.2-gke.1498000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)



## July 16, 2026

Change

#### (2026-R30) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.0-gke.4681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.1498000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.13-gke.1011000
    * 1.34.9-gke.1131000
    * 1.35.6-gke.1127000
    * 1.36.0-gke.4447000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.35 to [1.36.0-gke.4681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.0-gke.4681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## July 10, 2026

Change

#### (2026-R29) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.2-gke.1346000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.12-gke.1270000
    * 1.34.9-gke.1065000
    * 1.35.6-gke.1049000
    * 1.36.0-gke.3712000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.35 to [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## July 09, 2026

Change

#### (2026-R28) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.12-gke.1208000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1284000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1324000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.3302004
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.34 to [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.35 to [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



Change

#### (2026-R27) Version updates

There are no version updates for 2026-R27.

## June 29, 2026

Change

#### (2026-R26) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.0-gke.3302004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.3302004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.12-gke.1165000
    * 1.34.8-gke.1278000
    * 1.35.5-gke.1241004
    * 1.36.0-gke.3070003
    * 1.36.0-gke.3302001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1284000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1324000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.35 to [1.36.0-gke.3302004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1284000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1324000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.3302004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## June 26, 2026

Change

#### (2026-R25) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.33.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1284000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1324000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.3302001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.12-gke.1116000
    * 1.33.12-gke.1166000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1218000
    * 1.35.5-gke.1163000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1241000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.2684000
    * 1.36.0-gke.3009002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.35 to [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



Change

#### (2026-R24) Version updates

There are no version updates for 2026-R24.

## June 12, 2026

Change

#### (2026-R23) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.12-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1241000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.3009002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.12-gke.1059000
    * 1.34.8-gke.1126000
    * 1.35.5-gke.1057000
    * 1.36.0-gke.2459000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1163000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1163000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## June 04, 2026

Change

#### (2026-R22) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1163000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.12-gke.1000000
    * 1.34.8-gke.1000000
    * 1.35.5-gke.1000000
    * 1.36.0-gke.2253000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## May 27, 2026

Change

#### (2026-R21) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.11-gke.1074000
    * 1.33.11-gke.1197000
    * 1.34.7-gke.1055000
    * 1.34.7-gke.1499000
    * 1.35.3-gke.1993000
    * 1.35.3-gke.2190000
    * 1.36.0-gke.1575000
    * 1.36.0-gke.1759000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.34 to [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.2253000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## May 21, 2026

Change

#### (2026-R20) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.2253000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## May 13, 2026

Change

#### (2026-R19) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1993000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.36.0-gke.1759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.33.11-gke.1137000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.7-gke.1321000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1737000
    * 1.36.0-gke.1379000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.34 to [1.35.3-gke.1993000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.35 to [1.35.3-gke.1993000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
      * 1.36 to [1.36.0-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## May 06, 2026

Change

#### (2026-R18) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1737000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.33.11-gke.1137000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1321000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1993000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.36.0-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.13-gke.1362000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1407000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.11-gke.1013000
    * 1.34.6-gke.1307000
    * 1.35.3-gke.1522000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.33 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.34 to [1.35.3-gke.1737000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.3-gke.1737000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 29, 2026

Change

#### (2026-R17) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1522000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1407000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1737000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.36.0-gke.1379000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.13-gke.1090000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1147000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1205000
    * 1.32.13-gke.1258000
    * 1.32.13-gke.1318000
    * 1.33.9-gke.1117000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.9-gke.1166000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.10-gke.1067000
    * 1.33.10-gke.1115000
    * 1.33.10-gke.1176000
    * 1.34.5-gke.1153000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.5-gke.1208000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1068000
    * 1.34.6-gke.1154000
    * 1.34.6-gke.1237000
    * 1.35.2-gke.1485000
    * 1.35.2-gke.1842000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1962000
    * 1.35.3-gke.1234000
    * 1.35.3-gke.1389000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.13-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.32 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.33 to [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.34 to [1.35.3-gke.1522000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.13-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.33 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.3-gke.1522000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
      * 1.36 to [1.36.0-gke.1379000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## April 22, 2026

Change

#### (2026-R16) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1522000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 15, 2026

Change

#### (2026-R15) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 09, 2026

Change

#### (2026-R14) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 02, 2026

Change

#### (2026-R13) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1205000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.2-gke.1962000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## March 25, 2026

Change

#### (2026-R12) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.2-gke.1485000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1147000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1842000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.13-gke.1059000
    * 1.33.9-gke.1060000
    * 1.34.5-gke.1076000
    * 1.35.2-gke.1269001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.13-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.32 to [1.33.9-gke.1117000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
      * 1.33 to [1.34.5-gke.1153000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
      * 1.34 to [1.35.2-gke.1485000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.13-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.33 to [1.33.9-gke.1117000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
      * 1.34 to [1.34.5-gke.1153000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
      * 1.35 to [1.35.2-gke.1485000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## March 18, 2026

Change

#### (2026-R11) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1117000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1153000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
    * [1.35.2-gke.1485000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.12-gke.1127000
    * 1.33.8-gke.1169000
    * 1.34.4-gke.1193000
    * 1.35.1-gke.1396001
    * 1.35.2-gke.1269000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support) in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.32 to [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
      * 1.33 to [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
      * 1.34 to [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.33 to [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
      * 1.34 to [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
      * 1.35 to [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## March 12, 2026

Change

#### (2026-R10) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.12-gke.1076000
    * 1.33.8-gke.1112000
    * 1.34.4-gke.1130000
    * 1.35.1-gke.1616000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.33 to [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)



## March 05, 2026

Change

#### (2026-R9) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.1-gke.1396001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.1-gke.1396001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
    * [1.35.1-gke.1616000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.12-gke.1026000
    * 1.33.8-gke.1026000
    * 1.34.4-gke.1047000
    * 1.35.0-gke.3047001
    * 1.35.1-gke.1396000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.33 to [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
      * 1.34 to [1.35.1-gke.1396001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
      * 1.35 to [1.35.1-gke.1396001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)



## February 25, 2026

Change

#### (2026-R8) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.3047001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.3047001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.1-gke.1396000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.11-gke.1264000
    * 1.33.5-gke.2469000
    * 1.34.3-gke.1444000
    * 1.35.0-gke.2745003
    * 1.35.0-gke.3047000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.33 to [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
      * 1.34 to [1.35.0-gke.3047001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
      * 1.35 to [1.35.0-gke.3047001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 19, 2026

Change

#### (2026-R7) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.2745003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2745003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.11-gke.1211000
    * 1.33.5-gke.2392000
    * 1.34.3-gke.1318000
    * 1.35.0-gke.2398000
    * 1.35.0-gke.2745000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.34 to [1.35.0-gke.2745003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2745003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 11, 2026

Change

#### (2026-R6) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.2398000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2745000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.11-gke.1174000
    * 1.33.5-gke.2326000
    * 1.34.3-gke.1245000
    * 1.35.0-gke.2232000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.34 to [1.35.0-gke.2398000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2398000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 04, 2026

Change

#### (2026-R5) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2398000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.11-gke.1038000
    * 1.32.11-gke.1153001
    * 1.33.5-gke.2228001
    * 1.33.5-gke.2288001
    * 1.34.3-gke.1051003
    * 1.34.3-gke.1136000
    * 1.35.0-gke.1795000
    * 1.35.0-gke.2180000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## January 29, 2026

Change

#### (2026-R4) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.1795000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.11-gke.1153001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2288001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2180000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.11-gke.1075000
    * 1.33.5-gke.2172000
    * 1.33.5-gke.2228000
    * 1.34.3-gke.1051000
    * 1.35.0-gke.1624000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.1795000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## January 21, 2026

Change

#### (2026-R3) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.1624000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.32.11-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2228000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.1795000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.14-gke.1175000
    * 1.31.14-gke.1214000
    * 1.32.9-gke.1734000
    * 1.33.5-gke.2118000
    * 1.34.1-gke.3971000
    * 1.35.0-gke.1403000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.3-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.1624000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## January 15, 2026

Change

#### (2026-R2) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.1403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1214000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.1624000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.14-gke.1166000
    * 1.32.9-gke.1728000
    * 1.33.5-gke.2100000
    * 1.34.1-gke.3947000
    * 1.35.0-gke.1340000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.31 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.1-gke.3971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.32 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
      * 1.35 to [1.35.0-gke.1403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## January 07, 2026

Change

#### (2026-R1) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.0-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.35.0-gke.1403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.13-gke.1139000
    * 1.31.13-gke.1454000
    * 1.31.14-gke.1045000
    * 1.31.14-gke.1081000
    * 1.31.14-gke.1114000
    * 1.31.14-gke.1156000
    * 1.32.9-gke.1239000
    * 1.32.9-gke.1548000
    * 1.32.9-gke.1592000
    * 1.32.9-gke.1632000
    * 1.32.9-gke.1675000
    * 1.32.9-gke.1711000
    * 1.33.5-gke.1862000
    * 1.33.5-gke.1894000
    * 1.33.5-gke.1956000
    * 1.33.5-gke.2019000
    * 1.33.5-gke.2072000
    * 1.34.0-gke.2201000
    * 1.34.1-gke.2541000
    * 1.34.1-gke.3355002
    * 1.34.1-gke.3403002
    * 1.34.1-gke.3556000
    * 1.34.1-gke.3759000
    * 1.34.1-gke.3899000
    * 1.35.0-gke.1272000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.14-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.31 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.1-gke.3947000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.14-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.32 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3947000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
      * 1.35 to [1.35.0-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## January 05, 2026

Change

#### (2025-R54) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3947000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.35.0-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## December 29, 2025

Change

#### (2025-R53) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.35.0-gke.1272000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.35 to [1.35.0-gke.1272000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## December 18, 2025

Change

#### (2025-R52) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
    * [1.34.1-gke.2541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## December 10, 2025

Change

#### (2025-R51) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3403002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3556000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.13-gke.1231000
    * 1.31.13-gke.1377000
    * 1.32.9-gke.1330000
    * 1.32.9-gke.1462000
    * 1.34.1-gke.3355001
    * 1.34.1-gke.3403001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## December 05, 2025

Change

#### (2025-R50) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.1-gke.3355001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1592000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1894000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3403001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.14-gke.1033000
    * 1.32.9-gke.1575000
    * 1.33.5-gke.1350000
    * 1.33.5-gke.1521000
    * 1.33.5-gke.1697000
    * 1.33.5-gke.1791000
    * 1.34.1-gke.2037001
    * 1.34.1-gke.2037002
    * 1.34.1-gke.2541000
    * 1.34.1-gke.2909000
    * 1.34.1-gke.2980000
    * 1.34.1-gke.3084001
    * 1.34.1-gke.3225000
    * 1.34.1-gke.3355000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.5-gke.1862000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.1-gke.3355001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.5-gke.1862000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3355001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## November 28, 2025

Change

#### (2025-R49) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.31.14-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1862000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## November 20, 2025

Change

#### (2025-R48) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.31.13-gke.1454000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1548000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1791000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2980000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3084001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## November 14, 2025

Change

#### (2025-R47) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.31.13-gke.1377000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1462000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2037002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2909000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * Version 1.34.1-gke.1829001 is no longer available in the Rapid channel.



## November 07, 2025

Change

#### (2025-R46) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.1-gke.2037001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.13-gke.1231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1330000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1521000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2037001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.13-gke.1123000
    * 1.32.9-gke.1207000
    * 1.33.5-gke.1308000
    * 1.34.1-gke.2037000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.1-gke.2037001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.2037001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## October 29, 2025

Change

#### (2025-R45) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2037000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.13-gke.1040000
    * 1.32.9-gke.1130000
    * 1.33.5-gke.1201000
    * 1.34.0-gke.2201000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.33 to [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## October 22, 2025

Change

#### (2025-R44) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
    * [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.13-gke.1023000
    * 1.32.9-gke.1108000
    * 1.33.5-gke.1162000
    * 1.34.1-gke.1293000
    * 1.34.1-gke.1431000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)



## October 15, 2025

Change

#### (2025-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.1431000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.12-gke.1265000
    * 1.31.13-gke.1008000
    * 1.32.9-gke.1072000
    * 1.32.9-gke.1092000
    * 1.33.5-gke.1080000
    * 1.33.5-gke.1125000
    * 1.34.0-gke.2201000
    * 1.34.1-gke.1127000
    * 1.34.1-gke.1279000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## October 08, 2025

Change

#### (2025-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.14-gke.1267000
    * 1.30.14-gke.1316000
    * 1.30.14-gke.1325000
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



## October 02, 2025

Change

#### (2025-R41) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.12-gke.1110000
    * 1.32.8-gke.1170000
    * 1.34.0-gke.1662000
    * 1.34.0-gke.2011000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.



## September 29, 2025

Change

#### (2025-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.14-gke.1150000
    * 1.33.4-gke.1245000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 18, 2025

Change

#### (2025-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * [1.34.0-gke.2011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.14-gke.1130000
    * 1.31.12-gke.1060000
    * 1.31.12-gke.1083000
    * 1.32.8-gke.1108000
    * 1.32.8-gke.1134000
    * 1.33.4-gke.1172000
    * 1.34.0-gke.1477000
    * 1.34.0-gke.1497000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.



## September 11, 2025

Change

#### (2025-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.14-gke.1059000
    * 1.30.14-gke.1108000
    * 1.31.12-gke.1014000
    * 1.32.8-gke.1026000
    * 1.33.4-gke.1036000
    * 1.33.4-gke.1134000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 03, 2025

Change

#### (2025-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * [1.34.0-gke.1477000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
    * [1.34.0-gke.1497000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.14-gke.1036000
    * 1.31.11-gke.1101000
    * 1.32.7-gke.1079000
    * 1.33.3-gke.1136000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.1477000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.



## August 27, 2025

Change

#### (2025-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.14-gke.1011000
    * 1.31.11-gke.1064000
    * 1.31.11-gke.1135000
    * 1.32.7-gke.1016000
    * 1.32.8-gke.1005000
    * 1.33.3-gke.1392000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.



## August 21, 2025

Change

#### (2025-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
    * [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1414000
    * 1.31.11-gke.1036000
    * 1.32.6-gke.1125000
    * 1.33.2-gke.1240000
    * 1.33.3-gke.1250000
    * 1.33.3-gke.1266000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.



## August 14, 2025

Change

#### (2025-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
    * [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1390000
    * 1.31.11-gke.1002000
    * 1.32.6-gke.1096000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 06, 2025

Change

#### (2025-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1372000
    * 1.31.10-gke.1067000
    * 1.32.6-gke.1060000
    * 1.33.2-gke.4780000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 01, 2025

Change

#### (2025-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1340000
    * 1.31.10-gke.1034000
    * 1.32.6-gke.1025000
    * 1.33.2-gke.4655000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## July 25, 2025

Change

#### (2025-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1208000
    * 1.30.12-gke.1246000
    * 1.30.12-gke.1279000
    * 1.30.12-gke.1320000
    * 1.30.12-gke.1333000
    * 1.31.9-gke.1119000
    * 1.31.9-gke.1176000
    * 1.31.9-gke.1218000
    * 1.31.9-gke.1287000
    * 1.31.10-gke.1021000
    * 1.32.4-gke.1415000
    * 1.32.4-gke.1603000
    * 1.32.4-gke.1698000
    * 1.32.4-gke.1767000
    * 1.32.6-gke.1013000
    * 1.33.1-gke.1584000
    * 1.33.1-gke.1744000
    * 1.33.1-gke.1959000
    * 1.33.2-gke.1043000
    * 1.33.2-gke.1111000
    * 1.33.2-gke.1384000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.



## July 16, 2025

Change

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## July 11, 2025

Change

#### (2025-R29) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## July 02, 2025

Change

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## June 27, 2025

Change

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## June 18, 2025

Change

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1168000
    * 1.31.9-gke.1044001
    * 1.33.1-gke.1386000
    * 1.33.1-gke.1545000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.



## June 12, 2025

Change

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1151000
    * 1.31.9-gke.1005000
    * 1.32.4-gke.1353001
    * 1.32.4-gke.1415001
    * 1.32.4-gke.1533000
    * 1.33.0-gke.2248000
    * 1.33.1-gke.1107000
    * 1.33.1-gke.1375000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.



## June 05, 2025

Change

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available in the Rapid channel: 
    * 1.31.8-gke.1113000
    * 1.31.9-gke.1044000
    * 1.32.4-gke.1236006
    * 1.32.4-gke.1353000
    * 1.32.4-gke.1415000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.



Change

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

## May 30, 2025

Change

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1086000
    * 1.31.9-gke.1005000
    * 1.33.0-gke.1868000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.



Change

#### (2025-R21) Version updates

There are no version updates for 2025-R21.

## May 23, 2025

Change

#### (2025-R20) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1353000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.12-gke.1033000
    * 1.31.7-gke.1390000
    * 1.31.8-gke.1045000
    * 1.32.3-gke.1927002
    * 1.32.4-gke.1106000
    * 1.32.4-gke.1236000
    * 1.33.0-gke.1552000
    * 1.33.0-gke.1712000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.0-gke.1868000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.



## May 16, 2025

Change

#### (2025-R19) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.4-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.0-gke.1868000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.11-gke.1157000
    * 1.30.11-gke.1217000
    * 1.31.7-gke.1265000
    * 1.32.3-gke.1785003
    * 1.33.0-gke.1582000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.3-gke.1927002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.3-gke.1927002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.



## May 09, 2025

Change

#### (2025-R18) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.3-gke.1927002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.3-gke.1927002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.4-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.0-gke.1552000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
    * [1.33.0-gke.1582000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
    * [1.33.0-gke.1712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.11-gke.1131000
    * 1.31.7-gke.1212000
    * 1.32.2-gke.1297002
    * 1.32.3-gke.1785000
    * 1.32.3-gke.1927000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.0-gke.1552000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.



## May 02, 2025

Change

#### (2025-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1927000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available in the Rapid channel: 
    * 1.30.10-gke.1070000
    * 1.30.10-gke.1102000
    * 1.31.6-gke.1064001
    * 1.31.6-gke.1099001
    * 1.32.2-gke.1182003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## April 28, 2025

Change

#### (2025-R16) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1785000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available in the Rapid channel: 
    * 1.29.14-gke.1067000
    * 1.29.14-gke.1086000
    * 1.29.15-gke.1170000
    * 1.30.11-gke.1131000
    * 1.31.7-gke.1013002
    * 1.31.7-gke.1212000
    * 1.32.3-gke.1717000



## April 18, 2025

Change

#### (2025-R15) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.29.15-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.6-gke.1099001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1717000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available in the Rapid channel: 
    * 1.29.14-gke.1132000
    * 1.29.15-gke.1017000
    * 1.29.15-gke.1058000
    * 1.29.15-gke.1108000
    * 1.29.15-gke.1134000
    * 1.30.10-gke.1145000
    * 1.30.10-gke.1227000
    * 1.30.10-gke.1227001
    * 1.30.11-gke.1008001
    * 1.30.11-gke.1072000
    * 1.30.11-gke.1093000
    * 1.31.5-gke.1169001
    * 1.31.5-gke.1233001
    * 1.31.6-gke.1020001
    * 1.31.6-gke.1064000
    * 1.31.6-gke.1099000
    * 1.31.6-gke.1140000
    * 1.31.6-gke.1221000
    * 1.31.6-gke.1221001
    * 1.31.7-gke.1013001
    * 1.31.7-gke.1112000
    * 1.31.7-gke.1149000
    * 1.32.2-gke.1182001
    * 1.32.2-gke.1182002
    * 1.32.2-gke.1297001
    * 1.32.2-gke.1400003
    * 1.32.2-gke.1652000
    * 1.32.2-gke.1652003
    * 1.32.3-gke.1057001
    * 1.32.3-gke.1170000
    * 1.32.3-gke.1440000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## April 08, 2025

Change

#### (2025-R14) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.29.15-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1149000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1440000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)



## April 02, 2025

Change

#### (2025-R13) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.29.15-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.5-gke.1169001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.31.5-gke.1233001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.31.6-gke.1020001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.7-gke.1013002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.31.7-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1182002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)



## March 26, 2025

Change

#### (2025-R12) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.29.15-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.10-gke.1227001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.30.11-gke.1008001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.6-gke.1221001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.7-gke.1013001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1652003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1057001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)



## March 19, 2025

Change

#### (2025-R11) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.29.15-gke.1017000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1221000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1400003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1652000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available in the Rapid channel: 
    * 1.32.2-gke.1182000
    * 1.32.2-gke.1400001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## March 12, 2025

Change

#### (2025-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1182000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.29.14-gke.1132000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1140000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1297001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1400001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available in the Rapid channel: 
    * 1.29.14-gke.1018000
    * 1.30.10-gke.1022000
    * 1.31.6-gke.1020000
    * 1.32.1-gke.1357001
    * 1.32.1-gke.1729000
    * 1.32.2-gke.1297000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.14-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.6-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.2-gke.1182000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.14-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.6-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.2-gke.1182000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## March 05, 2025

Change

#### (2025-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.29.14-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1102000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1297000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available in the Rapid channel: 
    * 1.29.14-gke.1020000
    * 1.30.10-gke.1042000
    * 1.31.6-gke.1027000



## February 26, 2025

Change

#### (2025-R08) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.1-gke.1729000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.29.14-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.29.14-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.6-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available in the Rapid channel: 
    * 1.29.13-gke.1109000
    * 1.29.13-gke.1169000
    * 1.30.9-gke.1201000
    * 1.30.9-gke.1231000
    * 1.31.5-gke.1169000
    * 1.31.5-gke.1233000
    * 1.32.1-gke.1489001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.



## February 18, 2025

Change

#### (2025-R07) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.1-gke.1489001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.9-gke.1231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.1-gke.1729000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Rapid channel: 
    * 1.29.13-gke.1038000
    * 1.30.9-gke.1046000
    * 1.30.9-gke.1127000
    * 1.31.5-gke.1068000
    * 1.32.1-gke.1200003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) with this release.



## February 11, 2025

Change

#### (2025-R06) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1489001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1641000
    * 1.28.15-gke.1673000
    * 1.28.15-gke.1720000
    * 1.29.13-gke.1006000
    * 1.30.9-gke.1009000
    * 1.31.5-gke.1023000
    * 1.32.0-gke.1448000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.



## February 06, 2025

Change

#### (2025-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1720000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
    * [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1612000
    * 1.29.12-gke.1270000
    * 1.30.9-gke.1027000
    * 1.31.4-gke.1372000
    * 1.32.0-gke.1538000
    * 1.32.1-gke.1200000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.15-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.15-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) with this release.



## January 29, 2025

Change

#### (2025-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1673000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1200000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1503000
    * 1.29.12-gke.1143000
    * 1.30.8-gke.1261000
    * 1.30.8-gke.1282000
    * 1.31.4-gke.1256000
    * 1.32.1-gke.1002000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 23, 2025

Change

#### (2025-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.8-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1480000
    * 1.29.12-gke.1120000
    * 1.30.8-gke.1162000
    * 1.30.8-gke.1224000
    * 1.31.4-gke.1183000
    * 1.32.0-gke.1709000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 14, 2025

Change

#### (2025-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1224000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.32.0-gke.1709000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1320)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1488000
    * 1.29.12-gke.1126000
    * 1.30.8-gke.1128000
    * 1.30.8-gke.1133000
    * 1.31.4-gke.1249000
    * 1.32.0-gke.1577000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.



## January 07, 2025

Change

#### (2025-R01) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1133000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1249000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.32.0-gke.1538000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1320)
    * [1.32.0-gke.1577000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1320)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1342000
    * 1.28.15-gke.1362000
    * 1.28.15-gke.1388000
    * 1.28.15-gke.1435000
    * 1.29.10-gke.1280000
    * 1.29.11-gke.1012000
    * 1.29.11-gke.1045000
    * 1.29.12-gke.1055000
    * 1.30.6-gke.1596000
    * 1.30.7-gke.1084000
    * 1.30.7-gke.1136000
    * 1.30.8-gke.1051000
    * 1.31.3-gke.1006000
    * 1.31.3-gke.1056000
    * 1.31.3-gke.1121001
    * 1.31.3-gke.1162000
    * 1.31.4-gke.1072000
    * 1.31.4-gke.1177000
    * 1.32.0-gke.1358000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.0-gke.1448000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1320) with this release.



## December 26, 2024

Change

**(2024-R50) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.32.0-gke.1448000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1320)



## December 18, 2024

Change

**(2024-R49) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.32.0-gke.1358000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1320)
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.0-gke.1358000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1320) with this release.



## December 17, 2024

Announcement

**1.32 is now available in the Rapid channel**

Kubernetes 1.32 is now available in the Rapid channel. For more information about the content of Kubernetes 1.32, read the [Kubernetes 1.32 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#changelog-since-v1310).

## December 12, 2024

Change

#### (2024-R48) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1388000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.11-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12911)
    * [1.30.7-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.31.3-gke.1121001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
    * [1.31.3-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1344000
    * 1.30.7-gke.1077000
    * 1.31.3-gke.1023000



## December 10, 2024

Change

#### (2024-R47) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.3-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1344000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.11-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12911)
    * [1.30.7-gke.1077000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.30.7-gke.1084000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.31.3-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
    * [1.31.3-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.15-gke.1020000
    * 1.28.15-gke.1041000
    * 1.28.15-gke.1080000
    * 1.28.15-gke.1159000
    * 1.29.10-gke.1054000
    * 1.29.10-gke.1071000
    * 1.29.10-gke.1155000
    * 1.29.10-gke.1227000
    * 1.30.5-gke.1699000
    * 1.30.5-gke.1713000
    * 1.30.6-gke.1059000
    * 1.30.6-gke.1125000
    * 1.31.1-gke.2105000
    * 1.31.2-gke.1354000
    * 1.31.2-gke.1384000
    * 1.31.2-gke.1518000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.3-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.3-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313) with this release.



## November 27, 2024

Change

#### (2024-R46) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.3-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)



## November 19, 2024

Change

#### (2024-R45) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.2-gke.1518000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)



## November 13, 2024

Change

#### (2024-R44) Version updates

GKE cluster versions have been updated.

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.2-gke.1354000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
    * [1.31.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.14-gke.1376000
    * 1.29.9-gke.1541000
    * 1.30.5-gke.1628000
    * 1.31.1-gke.1846000
    * 1.31.2-gke.1115000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## November 06, 2024

Change

#### (2024-R43) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1071000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.2-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.14-gke.1340000
    * 1.28.15-gke.1015000
    * 1.29.9-gke.1496000
    * 1.29.10-gke.1043000
    * 1.30.5-gke.1443001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.14-gke.1376000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.9-gke.1541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.5-gke.1628000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.14-gke.1376000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.9-gke.1541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.5-gke.1628000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## October 30, 2024

Change

#### (2024-R42) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.15-gke.1015000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.14-gke.1217000
    * 1.29.9-gke.1341000
    * 1.30.5-gke.1355000
    * 1.31.1-gke.1678000
    * 1.31.1-gke.2008000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## October 25, 2024

Change

#### (2024-R41) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.14-gke.1376000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1628000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.2008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.14-gke.1099000
    * 1.29.9-gke.1177000
    * 1.30.5-gke.1145000
    * 1.31.1-gke.1146000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## October 17, 2024

Change

#### (2024-R40) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.14-gke.1175000
    * 1.31.1-gke.1621000



## October 11, 2024

Change

#### (2024-R39) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.1-gke.1146000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.28.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1621000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1373000
    * 1.27.16-gke.1478000
    * 1.29.8-gke.1278000
    * 1.30.5-gke.1014000
    * 1.31.1-gke.1000000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.5-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.1-gke.1146000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.5-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.1-gke.1146000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## October 03, 2024

Change

#### (2024-R38) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.1-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) is now the default version for cluster creation in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1342000
    * 1.28.13-gke.1119000
    * 1.28.14-gke.1004000
    * 1.29.8-gke.1211000
    * 1.30.4-gke.1348000
    * 1.31.0-gke.1577000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1373000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.5-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.1-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1373000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.5-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.1-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## September 26, 2024

Change

#### (2024-R37) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.0-gke.1577000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1478000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1146000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1287000
    * 1.28.13-gke.1049000
    * 1.29.8-gke.1096000
    * 1.30.3-gke.1969001
    * 1.30.4-gke.1476000
    * 1.31.0-gke.1506000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.0-gke.1577000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.0-gke.1577000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) with this release.



## September 19, 2024

Change

#### (2024-R36) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1373000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
    * [1.30.4-gke.1476000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.5-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1296000
    * 1.28.13-gke.1078000
    * 1.29.8-gke.1157000
    * 1.30.3-gke.1969000
    * 1.30.4-gke.1282000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.0-gke.1506000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## September 11, 2024

Change

#### (2024-R35) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.0-gke.1506000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1296000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1078000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.31.0-gke.1577000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1234000
    * 1.27.16-gke.1234001
    * 1.27.16-gke.1258000
    * 1.28.13-gke.1024000
    * 1.28.13-gke.1042000
    * 1.29.8-gke.1031000
    * 1.29.8-gke.1057000
    * 1.30.4-gke.1129000
    * 1.30.4-gke.1213000
    * 1.31.0-gke.1058000
    * 1.31.0-gke.1324000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.0-gke.1506000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) with this release.



## September 06, 2024

Change

#### (2024-R34) Version updates

There are no new releases in the Rapid channel.

Change

#### (2024-R33) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.0-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) is now the default version for cluster creation in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1234001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1213000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.31.0-gke.1506000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1148000
    * 1.28.13-gke.1006000
    * 1.29.7-gke.1274000
    * 1.30.3-gke.1639000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.3-gke.1969000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.3-gke.1969000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## August 28, 2024

Change

#### (2024-R32) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1129000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.31.0-gke.1324000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1082000
    * 1.28.12-gke.1090000
    * 1.28.12-gke.1179000
    * 1.29.7-gke.1174000
    * 1.30.3-gke.1225000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## August 20, 2024

Change

#### (2024-R31) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
    * [1.31.0-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1051000
    * 1.28.12-gke.1052000
    * 1.29.7-gke.1104000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.12-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.12-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.7-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.7-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.0-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) with this release.



Deprecated

#### Deprecated APIs in 1.31

  * The following Beta versions of graduated APIs were [deprecated in 1.29](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-29) in favor of newer versions: 
    * `flowcontrol.apiserver.k8s.io/v1beta3 FlowSchema, PriorityLevelConfiguration`
      * deprecated since 1.29, will no longer be served in 1.32
      * instead, use `flowcontrol.apiserver.k8s.io/v1`, available since 1.29
  * The `status.nodeInfo.kubeProxyVersion` field in the Node API is deprecated and will not be populated starting in v1.33. The field is currently populated with the kubelet version, not the kube-proxy version, and might not accurately reflect the kube-proxy version in use. For more information, see [KEP-4004](https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/4004-deprecate-kube-proxy-version).



Announcement

#### 1.31 is now available in the Rapid channel

Kubernetes 1.31 is now available in the Rapid channel. For more information about the content of Kubernetes 1.31, read the [Kubernetes 1.31 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#changelog-since-v1300).

Feature

#### New features

The following features are new in Kubernetes 1.31:

  * [Field selectors for custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#custom-resource-field-selectors) is beta and enabled by default.
  * [matchLabelKeys](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#matchlabelkeys) and [mismatchLabelKeys](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#mismatchlabelkeys) for Pod Affinity and Pod Anti Affinity are beta and enabled by default.
  * [Traffic distribution for Services](https://kubernetes.io/docs/concepts/services-networking/service/#traffic-distribution) is beta and enabled by default.
  * [Transition kubectl from SPDY to WebSockets](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/4006-transition-spdy-to-websockets) is beta and enabled by default.
  * [Recursive Read-only (RRO) mounts](https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts) is beta and enabled by default.
  * [Job success/completion policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#success-policy) is beta and enabled by default.
  * [Always Honor PersistentVolume Reclaim Policy](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolume-deletion-protection-finalizer) is beta and enabled by default.
  * [procMount security context option](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#proc-access) is beta and enabled by default.



Deprecated

#### Deprecated in-tree volume support

  * The Ceph CephFS (`kubernetes.io/cephfs`) and RBD (`kubernetes.io/rbd`) volume plugins are [deprecated since 1.28](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#urgent-upgrade-notes) and are removed in 1.31. 
  * To determine if you have volumes/pods using RBD or Ceph volumes, run the following commands. If either of them print output, then you are using a deprecated volume type.

    * `kubectl describe pv | egrep \-i 'Type: \*(RBD|CephFS)'`
    * `kubectl describe pod \-A | egrep \-i 'Type: \*(RBD|CephFS)'`
  * Switch to use an RBD or CephFS CSI driver (like the CSI drivers provided at <https://github.com/ceph/ceph-csi/>), or a Google Cloud-managed solution like [Filestore](https://docs.cloud.google.com/filestore/docs/csi-driver). 

  * For more information, refer to the [OSS Kubernetes announcement](https://groups.google.com/a/kubernetes.io/g/dev/c/U0--uNBae0Q/m/yhmcWHi3AAAJ?utm_medium=email&utm_source=footer) and <https://github.com/ceph/ceph-csi/>




## August 14, 2024

Change

#### (2024-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.16-gke.1008000
    * 1.28.11-gke.1315000
    * 1.29.7-gke.1008000
    * 1.30.2-gke.1587003
    * 1.30.3-gke.1451000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## August 12, 2024

Change

### (2024-R29) Version updates

There are no new releases in the Rapid channel.

## August 07, 2024

Change

### (2024-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1451000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.15-gke.1252000
    * 1.29.6-gke.1326000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.



## July 31, 2024

Change

### (2024-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.14-gke.1059002
    * 1.27.15-gke.1125000
    * 1.28.11-gke.1260000
    * 1.28.11-gke.1289000
    * 1.29.6-gke.1038001
    * 1.29.6-gke.1137000
    * 1.30.1-gke.1329003
    * 1.30.2-gke.1394003
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302) with this release.



## July 23, 2024

Change

### (2024-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.11-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.2-gke.1394003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
    * [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.11-gke.1172000
    * 1.30.2-gke.1394000
    * 1.30.2-gke.1587000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.



## July 17, 2024

Change

### (2024-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.30.2-gke.1587000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
  * The following versions are no longer available in the Rapid channel: 
    * 1.27.15-gke.1154000
    * 1.28.11-gke.1019001
    * 1.28.11-gke.1170000
    * 1.29.6-gke.1254000
    * 1.30.2-gke.1447000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.



## July 10, 2024

Change

### (2024-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.27.15-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1137000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.30.2-gke.1394000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
    * [1.30.2-gke.1447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1404000
    * 1.26.15-gke.1404002
    * 1.26.15-gke.1469000
    * 1.26.15-gke.1469001
    * 1.27.14-gke.1059000
    * 1.27.14-gke.1100000
    * 1.27.14-gke.1100002
    * 1.27.15-gke.1012000
    * 1.27.15-gke.1012003
    * 1.28.10-gke.1089000
    * 1.28.10-gke.1089002
    * 1.28.10-gke.1148000
    * 1.28.10-gke.1148001
    * 1.28.11-gke.1019000
    * 1.29.5-gke.1091000
    * 1.29.5-gke.1091002
    * 1.29.6-gke.1038000
    * 1.30.1-gke.1329000
    * 1.30.2-gke.1023000
    * 1.30.2-gke.1023004
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## July 08, 2024

Change

### (2024-R23) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.1-gke.1329003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301) is now the default version in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1404002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.15-gke.1404002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.10-gke.1089002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.1-gke.1329003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301) with this release.



## July 03, 2024

Change

### (2024-R22) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1404002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1469001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.14-gke.1100002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.15-gke.1012003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.10-gke.1089002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.10-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.30.1-gke.1329003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
    * [1.30.2-gke.1023004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)



## June 26, 2024

Change

#### (2024-R21) Version updates

  * Version [1.30.1-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.15-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.10-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.11-gke.1019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.30.2-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1390000
    * 1.26.15-gke.1436000
    * 1.27.14-gke.1042000
    * 1.27.14-gke.1093000
    * 1.28.10-gke.1075000
    * 1.28.10-gke.1141000
    * 1.29.5-gke.1121000
    * 1.29.5-gke.1192000
    * 1.30.1-gke.1156000
    * 1.30.1-gke.1500000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1404000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.15-gke.1404000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.10-gke.1089000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.1-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301) with this release.



## June 18, 2024

Change

#### (2024-R20) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1436000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1141000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.30.1-gke.1500000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1381000
    * 1.27.14-gke.1022000
    * 1.28.10-gke.1058000
    * 1.29.5-gke.1060000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.15-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.14-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.10-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.5-gke.1091000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.5-gke.1091000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.



## June 12, 2024

Change

#### (2024-R19) Version updates

  * Version [1.30.1-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1404000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1089000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.30.1-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1320000
    * 1.27.13-gke.1201000
    * 1.28.9-gke.1289000
    * 1.29.4-gke.1670000
    * 1.30.0-gke.1167000
    * 1.30.1-gke.1261000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.15-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.14-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.10-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.5-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.5-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.1-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301) with this release.



## June 06, 2024

Change

#### (2024-R18) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1091000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.30.1-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1372001
    * 1.30.1-gke.1139000



## May 28, 2024

Change

#### (2024-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1372001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.30.1-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
    * [1.30.1-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1300000
    * 1.26.15-gke.1360000
    * 1.27.13-gke.1166000
    * 1.27.14-gke.1011000
    * 1.28.9-gke.1209000
    * 1.28.10-gke.1012000
    * 1.29.4-gke.1165000
    * 1.29.5-gke.1010000
    * 1.30.1-gke.1015000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.13-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.4-gke.1670000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.4-gke.1670000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## May 21, 2024

Change

#### (2024-R16) Version updates

  * Version [1.30.0-gke.1167000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1300) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.30.1-gke.1015000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
  * The following versions are no longer available in the Rapid channel: 
    * 1.28.9-gke.1250000
    * 1.29.3-gke.1282000
    * 1.29.3-gke.1282001
    * 1.29.3-gke.1282005
    * 1.29.4-gke.1447001
    * 1.29.4-gke.1542000
    * 1.30.0-gke.1457000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.4-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.4-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## May 17, 2024

Change

#### (2024-R14) Version updates

There are no version updates for 2024-R14.

#### (2024-R15) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.3-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.3-gke.1282005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.4-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1447001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1542000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1670000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1191000
    * 1.27.13-gke.1000000
    * 1.28.9-gke.1000000
    * 1.29.4-gke.1043000
    * 1.29.4-gke.1447000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1300000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.13-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## May 08, 2024

Change

#### (2024-R13) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.3-gke.1282001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1300000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.4-gke.1447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.30.0-gke.1457000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1300)
  * The following versions are no longer available in the Rapid channel: 
    * 1.26.15-gke.1158000
    * 1.26.15-gke.1243000
    * 1.27.12-gke.1190000
    * 1.27.13-gke.1070000
    * 1.28.8-gke.1175000
    * 1.28.9-gke.1069000
    * 1.29.3-gke.1093006
    * 1.29.3-gke.1282000
    * 1.29.4-gke.1165000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.3-gke.1282001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.3-gke.1282001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) with this release.



## May 01, 2024

Change

#### (2024-R12) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.3-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1243000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1069000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.3-gke.1282001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.4-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.30.0-gke.1167000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1300)
  * Version 1.29.3-gke.1093000 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1191000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.13-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.3-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.3-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.0-gke.1167000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1300) with this release.



Feature

#### New APIs in 1.30

The following APIs are new in Kubernetes 1.30:

  * `admissionregistration.k8s.io/v1` `ValidatingAdmissionPolicyBinding` and `ValidatingAdmissionPolicy`



Deprecated

#### Deprecated features in 1.30

The Ceph CephFS (`kubernetes.io/cephfs`) and RBD (`kubernetes.io/rbd`) volume plugins are deprecated since 1.28 and will be removed in a future release.

To determine if you have volumes/pods using RBD or Ceph volumes, run the following commands. If either of them print output, then you are using a deprecated volume type:

  * `kubectl describe pv | egrep -i 'Type: *(RBD|CephFS)'`
  * `kubectl describe pod -A | egrep -i 'Type: *(RBD|CephFS)'`



Switch to use an RBD or CephFS CSI driver (like the CSI drivers provided in the [Ceph CSI driver project](https://github.com/ceph/ceph-csi/)), or a Google Cloud-managed solution like [Filestore](https://docs.cloud.google.com/filestore/docs/csi-driver). For more information, refer to the OSS Kubernetes announcement and to the [Ceph CSI driver project](https://github.com/ceph/ceph-csi/).

Announcement

#### 1.30 is now available in the Rapid channel

Kubernetes 1.30 is now available in the Rapid channel. For more information about the content of Kubernetes 1.30, read the [Kubernetes 1.30 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#changelog-since-v1290).

Feature

#### New features in 1.30

The following features are new in Kubernetes 1.30:

  * [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) is GA and now enabled by default.
  * [Validation Ratcheting](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-ratcheting) is beta and enabled by default, and makes CustomResourceDefinitions even safer and easier to manage.



Deprecated

#### Deprecated APIs in 1.30

The following Beta versions of graduated APIs were previously deprecated in 1.29 in favor of newer versions:

  * `flowcontrol.apiserver.k8s.io/v1beta3 FlowSchema, PriorityLevelConfiguration`: Deprecated since 1.29, will no longer be served in 1.32. Instead, use `flowcontrol.apiserver.k8s.io/v1`, which is available since Kubernetes 1.29
  * The `status.nodeInfo.kubeProxyVersion` field in the Node API is deprecated and will not be populated starting in v1.33. The field is currently populated with the kubelet version, not the kube-proxy version, and might not accurately reflect the kube-proxy version in use. For more information, see [KEP-4004](https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/4004-deprecate-kube-proxy-version).



## April 30, 2024

Change

#### (2024-R11) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.26.15-gke.1191000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.3-gke.1093006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.4-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1711000
    * 1.25.16-gke.1759000
    * 1.26.15-gke.1090000
    * 1.27.12-gke.1115000
    * 1.28.8-gke.1095000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1158000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.12-gke.1190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.8-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.8-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288) with this release.



## April 18, 2024

Change

#### (2024-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.3-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.15-gke.1158000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.12-gke.1190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712)
    * [1.28.8-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
    * [1.29.3-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1596000
    * 1.25.16-gke.1648000
    * 1.26.14-gke.1076000
    * 1.26.14-gke.1133000
    * 1.27.11-gke.1118000
    * 1.27.11-gke.1202000
    * 1.28.7-gke.1026000
    * 1.28.7-gke.1226000
    * 1.29.1-gke.1589017
    * 1.29.2-gke.1521000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.29.3-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.3-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293) with this release.



## April 08, 2024

Change

#### (2024-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712)
    * [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
    * [1.29.3-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)



## March 20, 2024

Change

**(2024-R08) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1648000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1133000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1202000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1226000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.2-gke.1521000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1292)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1570000
    * 1.26.14-gke.1044000
    * 1.27.11-gke.1062000
    * 1.28.3-gke.1286000
    * 1.28.7-gke.1100000
    * 1.29.2-gke.1217000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.14-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.11-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) with this release.



## March 07, 2024

Change

**(2024-R07) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.1-gke.1589017](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.1-gke.1589017](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
    * [1.29.2-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1292)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1537000
    * 1.26.14-gke.1006000
    * 1.27.11-gke.1018000
    * 1.28.6-gke.1456000
    * 1.29.0-gke.1381000
    * 1.29.1-gke.1589000
    * 1.29.2-gke.1060000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1570000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.1-gke.1589017](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## March 04, 2024

Change

**(2024-R06) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1570000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.2-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1292)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1460000
    * 1.26.13-gke.1144000
    * 1.27.10-gke.1207000
    * 1.28.6-gke.1369000
    * 1.29.1-gke.1575000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.14-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.11-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.11-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.1-gke.1589000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## February 23, 2024

Change

#### (2024-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.6-gke.1456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1589000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1497000
    * 1.26.13-gke.1189000
    * 1.27.10-gke.1152000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.10-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.10-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.1-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## February 13, 2024

Change

#### (2024-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1497000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1189000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.10-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
    * [1.28.6-gke.1369000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1360000
    * 1.26.13-gke.1052000
    * 1.27.10-gke.1055000
    * 1.28.6-gke.1095000
    * 1.28.6-gke.1289000
    * 1.29.1-gke.1016000
    * 1.29.1-gke.1425000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.10-gke.1152000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.10-gke.1152000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.0-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1290) with this release.



## February 08, 2024

Change

#### (2024-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.10-gke.1152000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
    * [1.28.6-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1425000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.16-gke.1268000
    * 1.26.12-gke.1111000
    * 1.27.9-gke.1092000
    * 1.28.5-gke.1217000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.13-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.10-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.10-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.29.1-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## January 26, 2024

Change

#### (2024-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.0-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1290) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.25.16-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.10-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
    * [1.28.6-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available in the Rapid channel: 
    * 1.24.17-gke.2364000
    * 1.24.17-gke.2472000
    * 1.25.16-gke.1041000
    * 1.26.11-gke.1055000
    * 1.27.8-gke.1067000
    * 1.28.3-gke.1203001
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.12-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12612) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1279) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## January 11, 2024

Change

#### (2024-R01) Version updates

  * Version [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.2472000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.12-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12612)
    * [1.27.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1279)
    * [1.28.5-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1285)
    * [1.29.0-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1290)
  * The following versions are no longer available in the Rapid channel: 
    * 1.24.17-gke.2347000
    * 1.25.16-gke.1020000
    * 1.26.10-gke.1235000
    * 1.27.5-gke.200
    * 1.27.7-gke.1293000
    * 1.28.4-gke.1083000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.17-gke.2364000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.8-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



Change

#### 1.29 is now available in the Rapid channel

Kubernetes 1.29 is now available in the Rapid channel. For more information about the content of Kubernetes 1.29, read the [Kubernetes 1.29 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#urgent-upgrade-notes).

Change

#### New APIs

  * `flowcontrol.apiserver.k8s.io/v1 FlowSchema`, `PriorityLevelConfiguration`
    * Notable changes in `flowcontrol.apiserver.k8s.io/v1`: 
      * The PriorityLevelConfiguration `spec.limited.nominalConcurrencyShares` field only defaults to 30 when unspecified, and an explicit value of 0 is not changed to 30.



Deprecated

#### Deprecated in-tree volume support

  * The Ceph CephFS (`kubernetes.io/cephfs`) and RBD (`kubernetes.io/rbd`) volume plugins are deprecated in 1.28 and will be removed in a future release.
  * To determine if you have volumes or Pods using RBD or Ceph volumes, run the following commands. If either of them print output, then you are using a deprecated volume type. 
    * `kubectl describe pv | egrep -i 'Type: *(RBD|CephFS)'`
    * `kubectl describe pod -A | egrep -i 'Type: *(RBD|CephFS)'`
  * Switch to use an RBD or CephFS CSI driver, such as the drivers provided in the [Ceph CSI](https://github.com/ceph/ceph-csi/) GitHub repo, or use a Google-managed solution such as [Filestore](https://docs.cloud.google.com/filestore/docs/csi-driver).
  * For more information, refer to the [OSS Kubernetes announcement](https://groups.google.com/a/kubernetes.io/g/dev/c/U0--uNBae0Q/m/yhmcWHi3AAAJ) and the [Ceph CSI](https://github.com/ceph/ceph-csi/) GitHub repo.



Deprecated

#### Removed SHA-1 certificate support

  * Starting from version 1.29, GKE no longer supports webhook backends that use TLS certificates signed with the insecure SHA-1 algorithm. To prevent impact on your clusters, you must replace incompatible certificates of [webhook servers](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#configure-admission-webhooks-on-the-fly) and [extension API servers](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) before upgrading your clusters to version 1.29.
  * GKE will not auto-upgrade clusters with webhook backends using incompatible certificates to 1.29 until you replace the certificates or until version 1.28 reaches end of life. For more information, refer to [Ensure compatibility of TLS certificates before upgrading to GKE 1.29](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/sha1-1-29).



Deprecated

#### Deprecated APIs

  * The following Beta versions of graduated APIs are [deprecated in 1.29](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-29) in favor of newer versions: 
    * `flowcontrol.apiserver.k8s.io/v1beta3 FlowSchema`, `PriorityLevelConfiguration`
      * Deprecated since 1.29
      * Instead, use `flowcontrol.apiserver.k8s.io/v1`, available since 1.29
  * The `status.nodeInfo.kubeProxyVersion` field in the Node API is deprecated and will not be populated starting in version 1.33. The field is currently populated with the kubelet version, not the kube-proxy version, and might not accurately reflect the kube-proxy version in use. For more information, see [KEP-4004](https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/4004-deprecate-kube-proxy-version).



Deprecated

#### Removed APIs

The following Beta versions of graduated APIs are [removed in 1.29](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-29) in favor of newer versions:

  * `flowcontrol.apiserver.k8s.io/v1beta2 FlowSchema`, `PriorityLevelConfiguration`
    * Deprecated since 1.26
    * Instead, use `flowcontrol.apiserver.k8s.io/v1beta3` available since 1.26, or `flowcontrol.apiserver.k8s.io/v1`, available since 1.29



Change

#### New Features

  * The beta [ValidatingAdmissionPolicy feature](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) can be opted into by [enabling the beta APIs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis#available-beta-apis).
  * `initContainers` can now be configured as [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) and kept running alongside normal containers in a Pod. This is only supported by nodes running version 1.29 or later, so avoid using this feature in Pods if there are nodes running earlier versions in the cluster.



## December 12, 2023

Change

#### (2023-R26) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.2364000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611)
    * [1.27.8-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278)
    * [1.28.4-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1284)
  * The following versions are no longer available in the Rapid channel: 
    * 1.24.17-gke.2266000
    * 1.25.15-gke.1115000
    * 1.26.10-gke.1101000
    * 1.27.7-gke.1121000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.17-gke.2347000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.16-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.10-gke.1235000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.10-gke.1235000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## December 04, 2023

Change

#### (2023-R25) Version updates

  * Version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.2347000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.10-gke.1235000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
    * [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Rapid channel: 
    * 1.24.17-gke.200
    * 1.24.17-gke.2113000
    * 1.24.17-gke.2155000
    * 1.24.17-gke.2230000
    * 1.25.13-gke.200
    * 1.25.14-gke.1421000
    * 1.25.14-gke.1474000
    * 1.25.15-gke.1083000
    * 1.26.8-gke.200
    * 1.26.9-gke.1437000
    * 1.26.9-gke.1507000
    * 1.26.10-gke.1073000
    * 1.27.4-gke.900
    * 1.27.6-gke.1248000
    * 1.27.6-gke.1445000
    * 1.27.7-gke.1088000
    * 1.28.2-gke.1157000
    * 1.28.3-gke.1090000
    * 1.28.3-gke.1118000
    * 1.28.3-gke.1203000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## November 17, 2023

Change

#### (2023-R24) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.15-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.26.10-gke.1073000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1088000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.27.7-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.28.3-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
    * [1.28.3-gke.1203000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Rapid channel: 
    * 1.24.17-gke.2198000
    * 1.24.17-gke.2211000
    * 1.25.15-gke.1033000
    * 1.25.15-gke.1049000
    * 1.26.10-gke.1024000
    * 1.26.10-gke.1038000
    * 1.27.7-gke.1038000
    * 1.27.7-gke.1056000
    * 1.28.3-gke.1098000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.10-gke.1073000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.10-gke.1073000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.3-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## November 09, 2023

Change

#### (2023-R23) Version updates

  * Version [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.2198000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.24.17-gke.2211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.15-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.25.15-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.26.10-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.26.10-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.27.7-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.28.3-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
    * [1.28.3-gke.1098000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following versions are no longer available in the Rapid channel: 
    * 1.25.12-gke.500
    * 1.26.7-gke.500
    * 1.27.6-gke.1506000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.24.17-gke.2198000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to [1.25.15-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to [1.26.10-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to [1.28.3-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## October 19, 2023

Change

#### (2023-R22) Version updates

There are no version updates for 2023-R21.

  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.14-gke.1474000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12514)
    * [1.26.9-gke.1507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1269)
    * [1.27.6-gke.1506000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1276)
    * [1.28.2-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1282)
  * The following versions are no longer available in the Rapid channel: 1.28.1-gke.201, 1.28.1-gke.1066000



## October 13, 2023

Change

#### (2023-R20) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.2113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.14-gke.1421000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12514)
    * [1.26.9-gke.1437000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1269)
    * [1.27.6-gke.1445000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1276)
  * The following versions are no longer available in the Rapid channel: 1.24.17-gke.1963000, 1.25.14-gke.1256000, 1.26.9-gke.1256000



## October 05, 2023

Change

#### (2023-R19) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.27.6-gke.1248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1276)
    * [1.28.1-gke.1066000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1281)



## September 07, 2023

Issue

With the recently released version of GKE, version 1.28, you cannot yet use the [SidecarContainer](https://github.com/kubernetes/enhancements/issues/753) feature with [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters). Pods defining restartable Init containers will not start. This is a known issue that will be resolved in a future release.

## September 05, 2023

Change

#### (2023-R18) Version updates

  * Version [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.13-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12513)
    * [1.26.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1268)
    * [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275)
    * [1.28.1-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1281)
  * The following versions are no longer available in the Rapid channel: 1.23.17-gke.10000, 1.23.17-gke.10700, 1.24.16-gke.500, 1.25.11-gke.1700, 1.26.6-gke.1700, 1.27.3-gke.1700
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12512) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.7-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1267) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.28 to version [1.28.1-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1281) with this release.



Deprecated

#### Deprecated API versions

These APIs are still served in version 1.28 but are in a deprecation period:

  * The following Beta versions of graduated APIs will be [removed in 1.29](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-29) in favor of newer versions: 
    * `flowcontrol.apiserver.k8s.io/v1beta2 FlowSchema, PriorityLevelConfiguration`
      * deprecated since 1.26
      * use `flowcontrol.apiserver.k8s.io/v1beta3` instead, available since 1.26.



Change

#### 1.28 is now available in the Rapid channel

Kubernetes 1.28 is now available in the Rapid channel. For more information about the content of Kubernetes 1.28, read the [Kubernetes 1.28 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#urgent-upgrade-notes).

Change

#### New APIs

  * The `kubectl auth whoami command` and the `authentication.k8s.io/v1 SelfSubjectReview API` enables checking the authenticated user information as seen by the server.



Deprecated

#### Deprecated in-tree volume support

  * The Ceph CephFS (`kubernetes.io/cephfs`) and RBD (`kubernetes.io/rbd`) volume plugins are deprecated in 1.28 and will be removed in a future release.
  * To determine if you have volumes or Pods using RBD or Ceph volumes, run the following commands. If either of them print output, then you are using a deprecated volume type. 
    * `kubectl describe pv | egrep -i 'Type: *(RBD|CephFS)'`
    * `kubectl describe pod -A | egrep -i 'Type: *(RBD|CephFS)'`
  * Switch to use an RBD or CephFS CSI driver, such as the drivers provided in the [Ceph CSI](https://github.com/ceph/ceph-csi/) GitHub repo, or use a Google-managed solution such as [Filestore](https://docs.cloud.google.com/filestore/docs/csi-driver). For more information, refer to the [OSS Kubernetes announcement](https://groups.google.com/a/kubernetes.io/g/dev/c/U0--uNBae0Q/m/yhmcWHi3AAAJ?utm_medium=email&utm_source=footer) and the [Ceph CSI](https://github.com/ceph/ceph-csi/) GitHub repo.



## August 08, 2023

Change

#### (2023-R17) Version updates

  * Version [1.27.3-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.23.17-gke.10700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416)
    * [1.25.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12512)
    * [1.26.7-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1267)
    * [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.14100
    * 1.23.17-gke.8400
    * 1.24.15-gke.1700
    * 1.25.10-gke.2700
    * 1.26.5-gke.2700
    * 1.27.3-gke.100
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.10000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.11-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12511) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1266) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.27.3-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.3-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) with this release.



## July 26, 2023

Change

#### (2023-R16) Version updates

  * Version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.23.17-gke.10000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415)
    * [1.25.11-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12511)
    * [1.26.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1266)
    * [1.27.3-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.18800
    * 1.23.17-gke.7700
    * 1.24.14-gke.2700
    * 1.25.10-gke.2100
    * 1.26.5-gke.2100
    * 1.27.2-gke.2100
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) with this release.



## July 07, 2023

Change

#### (2023-R15) Version updates

  * Version [1.27.2-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.12700
    * 1.23.17-gke.7000
    * 1.24.14-gke.2100
    * 1.25.10-gke.1400
    * 1.26.5-gke.1400
    * 1.27.2-gke.1200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.7700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.5-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.5-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.2-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) with this release.



## June 27, 2023

Change

#### (2023-R14) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.23.17-gke.7700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.2-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272)
  * The following versions are no longer available in the Rapid channel: 
    * 1.23.17-gke.6800
    * 1.24.14-gke.1400
    * 1.25.10-gke.1200
    * 1.26.5-gke.1200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.7000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.14-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.10-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## June 15, 2023

Change

#### (2023-R13) Version updates

  * Version [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.7000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.11400
    * 1.23.17-gke.5600
    * 1.24.14-gke.1200
    * 1.25.9-gke.2300
    * 1.26.3-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## June 07, 2023

Change

#### (2023-R12) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.8000
    * 1.23.17-gke.2000
    * 1.23.17-gke.3600
    * 1.24.13-gke.2500
    * 1.25.8-gke.1000
    * 1.26.4-gke.500
    * 1.26.4-gke.1400
    * 1.27.1-gke.400
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) with this release.



## June 05, 2023

Change

#### (2023-R11) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413)
    * [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259)
    * [1.26.4-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1264)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.9400
    * 1.23.17-gke.1700
    * 1.24.13-gke.500
    * 1.25.9-gke.400
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) with this release.



## May 16, 2023

Change

#### 1.27 is now available in the Rapid channel

Kubernetes 1.27 is now available in the Rapid channel. For more information about the content of Kubernetes 1.27, read the [Kubernetes 1.27 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#urgent-upgrade-notes).

Change

#### Removed API versions

The following Beta versions of graduated APIs will be [removed in 1.27](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-27) in favor of newer versions:

  * storage.k8s.io/v1beta1 CSIStorageCapacity

    * deprecated since 1.24
    * use storage.k8s.io/v1 instead, available since 1.24



Deprecated

#### Deprecated API versions

These APIs are still served in version 1.27 but are in a deprecation period:

  * The following Beta versions of graduated APIs will be [removed in 1.29](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-29) in favor of newer versions:

    * flowcontrol.apiserver.k8s.io/v1beta2 FlowSchema, PriorityLevelConfiguration

      * deprecated since 1.26
      * use flowcontrol.apiserver.k8s.io/v1beta3 instead, available since 1.26



## May 09, 2023

Change

#### (2023-R10) Version updates

  * Version [1.26.3-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263) is now the default version.
  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.13-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413)
    * [1.25.9-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259)
    * [1.26.4-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1264)
    * [1.27.1-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1271)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.7500
    * 1.23.17-gke.300
    * 1.24.12-gke.1000
    * 1.25.8-gke.500
    * 1.26.3-gke.400
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.13-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.3-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.27 to version [1.27.1-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1271) with this release.



## April 19, 2023

Change

#### (2023-R09) Version updates

  * Version [1.26.3-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
    * [1.26.3-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.6100
    * 1.23.16-gke.2500
    * 1.24.12-gke.500
    * 1.25.7-gke.1000
    * 1.26.2-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.17-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.3-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263) with this release.



## March 31, 2023

Change

#### (2023-R08) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
    * [1.26.3-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263)
  * Version [1.26.2-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1262) is now the default version in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.5400
    * 1.23.16-gke.1400
    * 1.24.11-gke.1000
    * 1.25.6-gke.1000
    * 1.26.1-gke.1500
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.22.17-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to [1.26.2-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1262) with this release.



## March 22, 2023

Change

#### (2023-R07) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411)
    * [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257)
    * [1.26.2-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1262)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.18100
    * 1.22.17-gke.4300
    * 1.24.10-gke.2300
    * 1.25.6-gke.200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.



## March 03, 2023

Change

#### (2023-R06) Version updates

  * Version [1.26.1-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1261) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.15800
    * 1.22.17-gke.4000
    * 1.23.16-gke.1100
    * 1.24.10-gke.1200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.



## February 22, 2023

Change

#### (2023-R05) Version updates

  * Version [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410)
    * [1.26.1-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1261)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.17-gke.3100
    * 1.23.16-gke.200
    * 1.24.9-gke.3200
    * 1.26.1-gke.200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.1-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1261) with this release.



## February 10, 2023

Change

#### (2023-04) Version updates

  * Version [1.25.6-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.16-gke.2000
    * 1.22.17-gke.1400
    * 1.22.17-gke.1900
    * 1.23.15-gke.1400
    * 1.23.15-gke.1900
    * 1.24.8-gke.2000
    * 1.24.9-gke.1500
    * 1.24.9-gke.2000
    * 1.25.5-gke.2000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.16-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.6-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.



## February 03, 2023

Fixed

The [`POD_FINDER_IP_MISMATCH`](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#January_27_2023) errors that caused Pods to fail to access Google Cloud APIs are fixed in the following GKE versions in the Rapid release channel:

  * 1.22.17-gke.3100 or later
  * 1.23.16-gke.200 or later
  * 1.24.9-gke.3200 or later
  * 1.25.6-gke.200 or later
  * 1.26.1-gke.400 or later



To fix the issue, upgrade your nodes to any of these versions.

## February 02, 2023

Change

#### (2023-R02) Version updates

  * Version [1.25.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.6-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256)
    * [1.26.1-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1261)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.14600
    * 1.22.16-gke.1300
    * 1.23.14-gke.1800
    * 1.24.8-gke.401
    * 1.25.5-gke.1500
    * 1.26.0-gke.2000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.16-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.15-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12315) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.1-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1261) with this release.



## January 13, 2023

Change

#### (2023-R02) Version updates

  * Version [1.25.5-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.15-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12315)
    * [1.24.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255)
    * [1.26.0-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1260)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.14100
    * 1.22.15-gke.2500
    * 1.23.14-gke.401
    * 1.24.7-gke.900
    * 1.25.4-gke.2100
    * 1.26.0-gke.1500
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.16-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.8-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.8-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.5-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.0-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1260) with this release.



## January 09, 2023

Change

The release notes for [1.26 available in the Rapid channel](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid#126_is_now_available_in_the_rapid_channel) were modified with an additional notable change:

  * New node pools created on 1.26 will default to use the [cgroupv2 resource management subsystem](https://kubernetes.io/docs/concepts/architecture/cgroups/) enabling the [latest container resource management capabilities](https://kubernetes.io/blog/2022/08/31/cgroupv2-ga-1-25/). [Node System Configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#cgroup-mode-options) can be used to switch between cgroup settings.



## January 05, 2023

Change

_2023-01-09 update_ : Added an additional Notable change to 1.26 for this release note.

Change

#### (2023-R01) Version updates

  * Version [1.25.4-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.15-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12315)
    * [1.24.9-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.5-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255)
    * [1.26.0-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1260)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.8500
    * 1.22.15-gke.1000
    * 1.23.13-gke.900
    * 1.24.6-gke.1500
    * 1.25.4-gke.1600
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.14-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.4-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.26 to version [1.26.0-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1260) with this release.



Deprecated

#### Removed API versions

The following Beta versions of graduated APIs will be [removed in 1.26](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26) in favor of newer versions:

  * flowcontrol.apiserver.k8s.io/v1beta1 FlowSchema, PriorityLevelConfiguration 
    * deprecated since 1.23
    * use flowcontrol.apiserver.k8s.io/v1beta2 instead, available since 1.23
  * autoscaling/v2beta2 HorizontalPodAutoscaler 
    * deprecated since 1.23
    * use autoscaling/v2 instead, available since 1.23 (or autoscaling/v1)



Change

#### New API versions

  * flowcontrol.apiserver.k8s.io/v1beta3 FlowSchema, PriorityLevelConfiguration 
    * The PriorityLevelConfiguration `spec.limited.assuredConcurrencyShares` field is renamed to `spec.limited.nominalConcurrencyShares`



Change

#### Notable changes

  * kubectl 1.26 removes compiled-in support for Azure and Google Cloud authentication methods. 
    * The removal doesn't affect operators that are deployed in the cluster and use Kubernetes service accounts to communicate with the API server, Kubernetes service account authentication continues to work as-is.
    * GKE has released an updated authentication plugin, gke-gcloud-auth-plugin. This plugin uses the client-go Credential Plugins framework to provide authentication tokens to communicate with GKE clusters.
    * For more information, see [Deprecated authentication plugin for Kubernetes clients](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/auth-plugin) and [Install required plugins](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin).
    * New node pools created on 1.26 will default to use the [cgroupv2 resource management subsystem](https://kubernetes.io/docs/concepts/architecture/cgroups/) enabling the [latest container resource management capabilities](https://kubernetes.io/blog/2022/08/31/cgroupv2-ga-1-25/). [Node System Configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#cgroup-mode-options) can be used to switch between cgroup settings.



Deprecated

#### Deprecated API versions

These APIs are still served in version 1.26 but are in a deprecation period:

  * The following Beta versions of graduated APIs will be removed in 1.27 in favor of newer versions: 
    * storage.k8s.io/v1beta1 CSIStorageCapacity
    * deprecated since 1.24
    * use storage.k8s.io/v1 instead, available since 1.24
  * The following Beta versions of graduated APIs will be removed in 1.29 in favor of newer versions: 
    * flowcontrol.apiserver.k8s.io/v1beta2 FlowSchema, PriorityLevelConfiguration
    * deprecated since 1.26
    * use flowcontrol.apiserver.k8s.io/v1beta3 instead, available since 1.26



Change

#### 1.26 is now available in the Rapid channel

Kubernetes 1.26 is now available in the Rapid channel. Before upgrading, read the [Kubernetes 1.26 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#urgent-upgrade-notes), especially the action required and deprecation sections.

## December 14, 2022

Change

#### (2022-R28) Version updates

  * Version [1.25.4-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254) is now the default version in the Rapid channel
  * The following versions are now available in the Rapid channel: 
    * [1.22.16-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216)
    * [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314)
    * [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248)
    * [1.25.4-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254)
  * The following versions are no longer available in the Rapid channel: 
    * 1.22.15-gke.100
    * 1.23.12-gke.1600
    * 1.24.5-gke.600
    * 1.25.3-gke.800
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.4-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254) with this release.



## December 05, 2022

Change

#### (2022-R27) Version updates

  * Version [1.25.3-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1253) is now the default version in the Rapid channel
  * The following versions are now available in the Rapid channel: 
    * [1.22.16-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216)
    * [1.23.14-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314)
    * [1.24.8-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248)
    * [1.25.4-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.7100
    * 1.21.14-gke.9500
    * 1.22.14-gke.300
    * 1.23.12-gke.100
    * 1.24.4-gke.800
    * 1.25.2-gke.1700
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.8500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.12-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1246) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1246) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.3-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1253) with this release.



## November 04, 2022

Change

#### (2022-R26) Version updates

  * Version [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.9500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313)
    * [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247)
    * [1.25.3-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1253)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.5300
    * 1.22.13-gke.1000
    * 1.23.11-gke.300
    * 1.24.3-gke.2100
    * 1.25.1-gke.500
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.22.14-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12214) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to [1.25.2-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1252) with this release.



## October 19, 2022

Change

#### (2022-R25) Version updates

  * Version [1.24.4-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1244) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.8500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.12-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312)
    * [1.24.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1246)
    * [1.25.2-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1252)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.14-gke.4300
    * 1.22.12-gke.2300
    * 1.23.10-gke.1000
    * 1.24.3-gke.900
    * 1.25.0-gke.1100
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.22.13-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12213) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.23.11-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12311) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.24.4-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1244) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to [1.24.4-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1244) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to [1.25.1-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1251) with this release.



## October 05, 2022

Change

(2022-R24) Version updates

  * The following versions are now available in the Rapid channel: 

    * [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312)
    * [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245)
    * [1.25.1-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1251)



## September 23, 2022

Change

#### (2022-R23) Version updates

  * Version [1.24.3-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) is now the default version in the Rapid channel. 
  * The following versions are now available in the Rapid channel: 

    * [1.22.14-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12214)
    * [1.23.11-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12311)
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.3-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.3-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) with this release.




## September 14, 2022

Change

#### 1.25 is now available in the Rapid channel

Kubernetes 1.25 is now available in the Rapid channel. Before upgrading, read the [Kubernetes 1.25 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#urgent-upgrade-notes), especially the action required and deprecation sections.

Change

#### Notable changes

Support for the deprecated `quobyte` and `storageOS` volume types is removed in 1.25.

Deprecated

#### Deprecated API versions

These APIs are still served in version 1.25 but are in a deprecation period:

  * The following Beta versions of graduated APIs will be [removed in 1.26](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26) in favor of newer versions: 
    * flowcontrol.apiserver.k8s.io/v1beta1 FlowSchema, PriorityLevelConfiguration 
      * deprecated since 1.23
      * use flowcontrol.apiserver.k8s.io/v1beta2 instead, available since 1.23
    * autoscaling/v2beta2 HorizontalPodAutoscaler 
      * deprecated since 1.23
      * use autoscaling/v2 instead, available since 1.23 (or autoscaling/v1)
  * The following Beta versions of graduated APIs will be [removed in 1.27](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-27) in favor of newer versions: 
    * storage.k8s.io/v1beta1 CSIStorageCapacity, deprecated since 1.24



Deprecated

#### Removed API versions

  * [PodSecurityPolicy](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)
    * policy/v1beta1 PodSecurityPolicy
    * Deprecated in 1.21 and removed in 1.25.
    * 1.24 is the last version supporting the beta PodSecurityPolicy feature. Use of this feature must be discontinued before clusters will upgrade to 1.25. See [PodSecurityPolicy deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/podsecuritypolicy) for more information.
  * The following Beta versions of graduated APIs are [removed in 1.25](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-25) in favor of their newer versions: 
    * discovery.k8s.io/v1beta1 EndpointSlice, deprecated since 1.21
    * policy/v1beta1 PodDisruptionBudget, deprecated since 1.21
    * batch/v1beta1 CronJob, deprecated since 1.21
    * node.k8s.io/v1beta1 RuntimeClass
    * autoscaling/v2beta1 HorizontalPodAutoscaler



## September 13, 2022

Change

#### (2022-R22) Version updates

  * Version [1.24.3-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) is now the default version in the Rapid channel
  * The following versions are now available in the Rapid channel:

    * [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.13-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12213)
    * [1.23.10-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12310)
    * [1.24.4-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1244)
    * [1.25.0-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1250)
  * The following versions are no longer available in the Rapid channel:

    * 1.20.15-gke.13700
    * 1.21.14-gke.3000
    * 1.22.12-gke.1200
    * 1.23.9-gke.2100
    * 1.24.3-gke.200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.10-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12310) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.3-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.3-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.25 to version [1.25.0-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1250) with this release.




## September 02, 2022

Change

#### (2022-R21) Version updates

  * The following versions are now available in the Rapid channel:

    * [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.23.9-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1239)
    * [1.24.3-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243)
  * Version [1.24.3-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) is now the default version in the Rapid channel.

  * The following versions are no longer available in the Rapid channel:

    * 1.21.14-gke.2700
    * 1.22.12-gke.500
    * 1.23.9-gke.900
    * 1.24.2-gke.1900
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.9-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1239) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.3-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.3-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) with this release.




## August 18, 2022

Change

#### (2022-R20) Version updates

  * Version [1.24.2-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.20.15-gke.13700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.14-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.23.9-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1239)
    * [1.24.3-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243)
  * The following versions are no longer available in the Rapid channel: 
    * 1.20.15-gke.13400
    * 1.21.14-gke.2100
    * 1.22.12-gke.300
    * 1.23.8-gke.1900
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.20.15-gke.13700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.9-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1239) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.24.2-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242) with this release.



## August 04, 2022

Change

#### (2022-R19) Version updates

  * The following versions are now available in the Rapid channel:

    * [1.20.15-gke.13400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.24.3-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243)
  * Version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) is now the default version in the Rapid channel.

  * The following versions are no longer available in the Rapid channel:

    * 1.21.14-gke.700
    * 1.22.10-gke.600
    * 1.22.11-gke.400
    * 1.23.6-gke.2200
    * 1.23.7-gke.1400
    * 1.23.8-gke.400
    * 1.24.2-gke.300
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.20.15-gke.13400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.2-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242) with this release.




## July 26, 2022

Change

#### (2022-R18) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238)
    * [1.24.2-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242)
  * Version [1.23.8-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) is now the default version in the Rapid channel
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.13-gke.900
    * 1.22.9-gke.2000
    * 1.23.6-gke.1700
    * 1.24.1-gke.1800
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.20.15-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.8-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.23.8-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.2-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242) with this release.



## July 19, 2022

Change

#### (2022-R17) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.11-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12211)
    * [1.23.8-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238)
    * [1.24.2-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.12-gke.2200
    * 1.22.9-gke.1500
    * 1.23.6-gke.1501
    * 1.24.1-gke.1400
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.1-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1241) with this release.



## June 30, 2022

Change

#### (2022-R16) Version updates

  * Version [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237) is now the default version in the Rapid channel.
  * Version [1.24.1-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1241) is now available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.15-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237) with this release.



## June 23, 2022

Change

#### (2022-R15) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113)
    * [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210)
    * [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237)
    * [1.24.1-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1241)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.12-gke.1700
    * 1.22.9-gke.1300
    * 1.23.6-gke.1500
    * 1.24.0-gke.1801
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.16-gke.11800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.1-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1241) with this release.



## June 13, 2022

Change

#### (2022-R14) Version updates

  * Version [1.23.6-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/%20CHANGELOG-1.21.md#v12112)
    * [1.22.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1229)
    * [1.23.6-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
    * [1.23.6-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
    * [1.24.0-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1240)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.12-gke.1500
    * 1.22.8-gke.2200
    * 1.23.5-gke.2400
    * 1.24.0-gke.1000
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.16-gke.11000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.9-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1229) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.23.6-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to version [1.23.6-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to version [1.24.0-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1240) with this release.



## May 26, 2022

Change

#### (2022-R13) Version updates

  * Version [1.23.5-gke.2400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) is now the default version in the Rapid channel.

  * The following versions are now available in the Rapid channel: 

    * [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
    * [1.22.9-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1229)
    * [1.23.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
    * [1.24.0-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1240)
  * The following versions are no longer available in the Rapid channel: 

    * 1.21.11-gke.1900
    * 1.22.8-gke.201
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to [1.20.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.23.5-gke.2400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.24 to [1.24.0-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1240) with this release.




Change

#### 1.24 is now available in the Rapid channel

Kubernetes 1.24 is now available in the Rapid channel. Before upgrading, read the [Kubernetes 1.24 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#urgent-upgrade-notes), especially the action required and deprecation sections.

Change

#### New API versions

  * storage.k8s.io/v1 CSIStorageCapacity



Change

#### Notable changes

  * GKE does not support node images that use Docker as the runtime in GKE version 1.24 and later. For more information, see [migrating from Docker to containerd](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd).
  * `Secret` API objects containing service account tokens are not automatically created in 1.24. 
    * This change improves security by reducing readable, permanent, Secret-based tokens to ones that have been explicitly requested, and improves performance by reducing the amount of persisted Secret data and [avoiding unnecessary utilization of application-layer secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets#limitations).
    * **Existing Secret-based tokens from previous versions remain valid on upgrade**.
    * Secret-based tokens are not used by nodes or pods on version 1.21 and later.
    * Only node versions 1.22 and later are supported running against 1.24 clusters.
    * Clients retrieving tokens directly from the API can still obtain a token using these methods supported in all available GKE versions: 
      * Preferred: Use the [TokenRequest API](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/) to obtain time-bound tokens that are not readable by other API clients. The [`kubectl create token`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-token-em-) command is available in kubectl 1.24+ to simplify use of this API from the command line.
      * Secret-based tokens can still be obtained by [creating a Secret object and waiting for it to be populated with a token](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#manually-create-a-service-account-api-token).
    * Examples of incorrect ways to obtain Secret-based tokens from the API include: 
      * Scanning the `secrets[*].name` field of a ServiceAccount object; this field lists secrets usable by pods running as that service account, not for other purposes, and secrets in that list have never been guaranteed to be service account token secrets.
      * Looking for existing Secret objects of type `kubernetes.io/service-account-token` created by other clients; a Secret created by another client is owned by that client, and cannot be assumed to be stable for use by other clients.
  * Kubernetes 1.24 [deprecates support for insecure serving certificates signed with a SHA-1 hash](https://go.dev/doc/go1.18#sha1). Aggregated API servers, admission webhooks, and custom resource conversion webhooks using TLS certificates that are signed by SHA-1 should replace the serving certificates as soon as possible.

    * At cluster version 1.24.0 and later, GKE provides a Cloud Audit log to check if your cluster contains an affected service. You can use the following filter to search for the logs of a 1.24+ cluster:
          
          logName: "projects/$PROJECT/logs/cloudaudit.googleapis.com%2Factivity"
          resource.type = "k8s_cluster"
          operation.producer = "k8s.io"
          "invalid-cert.kubernetes.io"
          ```
          

    * If you are not affected you won't see any logs. If you do see such an audit log, it will include the name of the service (whether webhook or aggregated API).




Issue

Nodes on version 1.24.0-gke.1000 with more than 80GB of memory will fail to start successfully due to a known bug, which will be resolved in future 1.24 versions.

Deprecated

#### Deprecated API versions

These APIs are still served in version 1.24 but are in a deprecation period:

  * [PodSecurityPolicy](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)

    * policy/v1beta1 PodSecurityPolicy
    * Deprecated in 1.21 with [removal targeted](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#psp-v125) for version 1.25.
    * 1.24 is the last version supporting the beta PodSecurityPolicy feature. Use of this feature must be discontinued before clusters will upgrade to 1.25. For more information, see [PodSecurityPolicy deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/podsecuritypolicy).
  * The following Beta versions of graduated APIs will be [removed in 1.25](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) in favor of their newer versions:

    * discovery.k8s.io/v1beta1 EndpointSlice, deprecated since 1.21
    * policy/v1beta1 PodDisruptionBudget, deprecated since 1.21
    * batch/v1beta1 CronJob, deprecated since 1.21
    * node.k8s.io/v1beta1 RuntimeClass
    * autoscaling/v2beta1 HorizontalPodAutoscaler
  * The following Beta versions of graduated APIs will be [removed in 1.26](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26) in favor of newer versions:

    * flowcontrol.apiserver.k8s.io/v1beta1 FlowSchema, PriorityLevelConfiguration 
      * deprecated since 1.23
      * use flowcontrol.apiserver.k8s.io/v1beta2 instead, available since 1.23
    * autoscaling/v2beta2 HorizontalPodAutoscaler 
      * deprecated since 1.23
      * use autoscaling/v2 instead, available since 1.23 (or autoscaling/v1)
  * The following Beta versions of graduated APIs will be [removed in 1.27](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-27) in favor of new versions:

    * storage.k8s.io/v1beta1 CSIStorageCapacity, deprecated since 1.24



## May 19, 2022

Change

#### (2022-R12) Version updates

  * The following versions are now available in the Rapid channel: 

    * [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
    * [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
    * [1.22.9-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1229)
    * [1.23.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
  * The following versions are no longer available in the Rapid channel: 

    * 1.21.11-gke.1100
    * 1.22.7-gke.1500
    * 1.22.8-gke.200
    * 1.23.5-gke.1500
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.5-gke.2400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.




## May 11, 2022

Change

#### (2022-R11) Version updates

  * Version [1.22.8-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) is now the default version in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.22.8-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.8-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.



## May 03, 2022

Change

#### (2022-R10) Version updates

  * The following versions are now available in the Rapid channel: 

    * [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
    * [1.22.8-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
    * [1.23.5-gke.2400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235)
  * The following versions are no longer available in the Rapid channel: 

    * 1.21.11-gke.900
    * 1.22.7-gke.1300
    * 1.23.5-gke.200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.18 to [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to [1.20.15-gke.4100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.5-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.




## April 21, 2022

Change

#### (2022-R9) Version updates

  * The following versions are now available in the Rapid channel: 
    * [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
    * [1.23.5-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.10-gke.2000
    * 1.22.7-gke.900
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.18 to version [1.19.16-gke.9200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.



## April 11, 2022

Change

#### (2022-R8) Version updates

  * Version [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) is now the default version in the Rapid channel.
  * Version [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now available in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.10-gke.1500
    * 1.22.7-gke.300
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.18 to version [1.19.16-gke.8300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to version [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.



## March 31, 2022

Change

#### (2022-R07) Version updates

  * Version [1.22.7-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110).
    * [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228).
    * [1.23.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235).
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.10-gke.1300
    * 1.23.4-gke.1600
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.10-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.10-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.



## March 21, 2022

Change

#### (2022-R6) Version updates

  * Version [1.22.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel:

    * [1.21.10-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110)
    * [1.22.7-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227)
    * [1.23.4-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1234)
  * The following versions are no longer available in the Rapid channel:

    * 1.21.10-gke.400
    * 1.22.6-gke.1500
    * 1.23.4-gke.1300
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.10-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.10-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.7-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.4-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1234) with this release.




## March 14, 2022

Change

#### (2022-R5) Version updates

  * Version [1.22.7-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel:

    * [1.21.10-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110)
    * [1.22.7-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227)
    * [1.23.4-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1234)
  * The following versions are no longer available in the Rapid channel:

    * 1.21.9-gke.1002
    * 1.22.6-gke.1000
    * 1.23.4-gke.300
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.10-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.10-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.22 to [1.22.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.23 to [1.23.4-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1234) with this release.




Issue

If you specify `--enable-dataplane-v2` in a Windows LTSC node pool running GKE version 1.22.7-gke.1300, Windows nodes cannot join the cluster.

## March 07, 2022

Change

#### (2022-R4) Version updates

  * Version [1.22.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) is now the default version in the Rapid channel.

  * The following versions are now available in the Rapid channel:

    * [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219).
    * [1.21.10-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110).
    * [1.22.7-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227).
    * [1.22.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227).
    * [1.23.4-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1234).
  * The following versions are no longer available in the Rapid channel: 

    * 1.21.9-gke.300
    * 1.21.9-gke.1001
    * 1.22.4-gke.1501
    * 1.22.6-gke.300
    * 1.23.3-gke.1100
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.4-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1234) with this release.




## February 24, 2022

Change

#### (2022-R03) Version updates

  * Version [1.22.6-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) is now the default version in the Rapid channel.
  * Version [1.21.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) is now available in the Rapid channel.
  * Version [1.22.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) is now available in the Rapid channel.
  * Version [1.22.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) is now available in the Rapid channel.
  * Version [1.23.3-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1233) is now available in the Rapid channel.
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.6-gke.1500
    * 1.22.3-gke.700
    * 1.22.3-gke.1500
    * 1.23.2-gke.300
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.3-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1233) with this release.



## February 10, 2022

Fixed

Versions 1.21.9-gke.300, 1.22.6-gke.300, and 1.23.2-gke.300 contain a fix for a race condition which could result in erroneously detaching all endpoints from network endpoint groups for a short period.

## February 03, 2022

Change

#### (2022-R02) Version updates

  * Version [1.22.4-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1224) is now the default version in the Rapid channel.
  * Version [1.21.9-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) is now available in the Rapid channel.
  * Version [1.22.6-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) is now available in the Rapid channel.
  * Version [1.23.2-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1232) is now available in the Rapid channel.
  * Version 1.21.5-gke.1802 is no longer available in the Rapid channel.
  * Version 1.23.1-gke.500 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.4-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1224) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.2-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1232) with this release.



## January 21, 2022

Change

#### (2022-R01) Version updates

  * Version [1.22.3-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223) is now the default version in the Rapid channel.
  * Version [1.22.4-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1224) is now available in the Rapid channel.
  * Version [1.23.1-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1231) is now available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.3-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.23 to [1.23.1-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1231) with this release.



Change

#### Notable changes and bug fixes

Kubernetes 1.23 is built with go1.17, which requires aggregated API servers, admission webhooks, and custom resource conversion webhooks to use TLS certificates that include the service DNS name as a subjectAltName.

  * Before upgrading to 1.23, ensure any non-local aggregated API servers, admission webhooks, and custom resource conversion webhooks in your cluster are served using valid TLS certificates.
  * At cluster version 1.22.3-gke.700 or higher, GKE provides a Cloud Audit log to check if your cluster contains an affected service. You can use the following filter to search for the logs:
        
        logName: "projects/$PROJECT/logs/cloudaudit.googleapis.com%2Factivity"
        resource.type = "k8s_cluster"
        operation.producer = "k8s.io"
        "invalid-cert.webhook.gke.io"
        

  * If you are not affected you won't see any logs. If you do see such an audit log, it will include the name of the service (whether webhook or aggregated API).




Change

#### 1.23 is now available in the Rapid channel

Kubernetes 1.23 is now available in the Rapid channel. Before upgrading, read the [Kubernetes 1.23 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#urgent-upgrade-notes), especially the action required and deprecation sections.

Feature

#### Notable features

##### Beta: PodSecurity admission

`PodSecurity` replaces the deprecated `PodSecurityPolicy` admission controller (which will be removed in 1.25). `PodSecurity` is an admission controller that enforces [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) on Pods in a Namespace based on specific namespace labels that set the enforcement level. In 1.23, the PodSecurity feature is enabled by default, and applies to namespaces that opt into enforcement. Refer to the [PodSecurity documentation](https://kubernetes.io/docs/concepts/security/pod-security-admission/) and [PodSecurityPolicy migration guide](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/) for more information.

Change

#### New API versions

  * flowcontrol.apiserver.k8s.io/v1beta2 FlowSchema, PriorityLevelConfiguration
  * autoscaling/v2 HorizontalPodAutoscaler



Deprecated

#### Deprecated API versions

These APIs are still served in version 1.23 but are in a deprecation period:

  * [PodSecurityPolicy](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)
    * policy/v1beta1 PodSecurityPolicy
    * Deprecated in 1.21 with [removal targeted](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#psp-v125) for version 1.25.
  * The following Beta versions of graduated APIs will be [removed in 1.25](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) in favor of their GA versions: 
    * discovery.k8s.io/v1beta1 EndpointSlice, deprecated since 1.21
    * policy/v1beta1 PodDisruptionBudget, deprecated since 1.21
    * batch/v1beta1 CronJob, deprecated since 1.21
    * node.k8s.io/v1beta RuntimeClass
    * autoscaling/v2beta1 HorizontalPodAutoscaler
  * The following Beta versions of graduated APIs will be [removed in 1.26](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26) in favor of newer versions: 
    * flowcontrol.apiserver.k8s.io/v1beta1 FlowSchema, PriorityLevelConfiguration 
      * deprecated since 1.23
      * use flowcontrol.apiserver.k8s.io/v1beta2 instead, available since 1.23
    * autoscaling/v2beta2 HorizontalPodAutoscaler 
      * deprecated since 1.23
    * use autoscaling/v2 instead, available since 1.23 (or autoscaling/v1)



## December 06, 2021

Change

#### (2021-R34) Version updates

  * Version [1.22.3-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223) is now the default version in the Rapid channel.
  * The following control plane and node versions are now available in the Rapid channel: 
    * [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216)
    * [1.22.3-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.5-gke.1302, 1.22.2-gke.1901



## November 15, 2021

Change

#### (2021-R33) Version updates

  * Version [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) is now the default version in the Rapid channel.
  * Version [1.22.3-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223) is now available in the Rapid channel.
  * The following control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded with this release: 
    * From version 1.20 to [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
    * From version 1.21 to [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
    * From version 1.22 to [1.22.3-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223)



## October 29, 2021

Change

#### Revisions for 2021-R32

_2021-12-03 update_ : Revised upgrade versions. Control planes and nodes with auto-upgrade enabled will be upgraded:

  * From version 1.20 to [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215).



Change

#### (2021-R32) Version updates

  * Version [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
    * [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
    * [1.22.2-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1222)
  * The following versions are no longer available in the Rapid channel: 
    * 1.21.4-gke.2300
    * 1.21.5-gke.1300
    * 1.22.2-gke.1300
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.2-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1222) with this release.



## October 15, 2021

Change

#### (2021-R31) Version updates

  * Version [1.21.4-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel:

    * [1.21.5-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
    * [1.22.2-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1222)
  * The following versions are no longer available in the Rapid channel:

    * 1.21.4-gke.1801
    * 1.22.1-gke.1602
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.4-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) with this release.

  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.2-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1222) with this release.




Issue

GKE Windows clusters using the persistent disk CSI driver ​might experience volume mount issues with existing `PersistentVolumeClaim` or `PersistentVolume` resources if upgraded to one the following versions. Please do not upgrade your Windows node pools to the following versions in the Rapid channel:

  * 1.22.1-gke.1602 or later



The fix will be available in a future GKE 1.22 release.

## October 01, 2021

Change

#### (2021-R30) Version updates

  * Version [1.21.4-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) is now the default version in the Rapid channel.
  * The following control plane and node versions are now available in the Rapid channel: 
    * [1.21.4-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214)
    * [1.22.1-gke.1602](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1221)
  * Version 1.21.4-gke.301 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.4-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.22 to [1.22.1-gke.1602](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1221) with this release.



Deprecated

#### Removed API versions in 1.22

The following Beta versions of previously graduated APIs are removed in 1.22 in favor of the GA versions. All existing objects can be interacted with via the stable APIs. Update API clients and manifests to use the GA APIs before upgrading. For more information, see the [Kubernetes 1.22 deprecated APIs guide](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22).

  * admissionregistration.k8s.io/v1beta1, MutatingWebhookConfiguration
  * admissionregistration.k8s.io/v1beta1, ValidatingWebhookConfiguration
  * apiextensions.k8s.io/v1beta1, CustomResourceDefinition
  * apiregistration.k8s.io/v1beta1, APIService
  * authentication.k8s.io/v1beta1, TokenReview
  * authorization.k8s.io/v1beta1, LocalSubjectAccessReview
  * authorization.k8s.io/v1beta1, SelfSubjectAccessReview
  * authorization.k8s.io/v1beta1, SubjectAccessReview
  * certificates.k8s.io/v1beta1, CertificateSigningRequest
  * coordination.k8s.io/v1beta1, Lease
  * extensions/v1beta1, Ingress
  * networking.k8s.io/v1beta1, Ingress
  * networking.k8s.io/v1beta1, IngressClass
  * rbac.authorization.k8s.io/v1beta1, ClusterRole
  * rbac.authorization.k8s.io/v1beta1, ClusterRoleBinding
  * rbac.authorization.k8s.io/v1beta1, Role
  * rbac.authorization.k8s.io/v1beta1, RoleBinding
  * scheduling.k8s.io/v1beta1, PriorityClass
  * storage.k8s.io/v1beta1, CSIDriver
  * storage.k8s.io/v1beta1, CSINode
  * storage.k8s.io/v1beta1, StorageClass
  * storage.k8s.io/v1beta1, VolumeAttachment



Change

#### 1.22 is now available in the Rapid channel

Kubernetes 1.22 is now available in the Rapid channel. Before upgrading, read the [Kubernetes 1.22 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#changelog-since-v1210), especially the action required and deprecation sections.

Feature

#### Notable features in 1.22

##### GA: Server-side Apply

_Server-side Apply_ is a new object merge algorithm, as well as tracking of field ownership, running on the Kubernetes API server. Server-side Apply helps users and controllers create and modify their resources via declarative configurations by sending their fully specified intent. Refer to [server-side apply documentation](https://kubernetes.io/docs/reference/using-api/server-side-apply/) for more information. Improvements in 1.22 include:

  * scale subresource ownership is tracked correctly ([#98377](https://github.com/kubernetes/kubernetes/pull/98377))
  * label selector fields are applied atomically ([#97989](https://github.com/kubernetes/kubernetes/pull/97989))



##### Beta: DaemonSet maxSurge

`DaemonSet` objects now support a `maxSurge` rollout parameter, which allows running updated pods for the DaemonSet on nodes before removing old pods. Refer to the [DaemonSet API documentation](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#rollingupdatedaemonset-v1-apps) for more information.

##### Beta: Suspended jobs

`Job` objects can now be created or placed in a suspended state, to allow higher-level control over ordering and scheduling of batch workloads. Refer to the [Job documentation](https://kubernetes.io/docs/concepts/workloads/controllers/job/#suspending-a-job) for more information.

##### Beta: podAffinity namespace selection

Pod affinity rules can now specify namespaced using a label selector, in addition to a fixed list of namespace names. Refer to the [pod affinity documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#namespace-selector) for more information.

Change

#### New API versions in 1.22

The `pods/eviction` subresource now accepts `policy/v1` eviction requests in addition to `policy/v1beta1` eviction requests ([#100724](https://github.com/kubernetes/kubernetes/pull/100724))

Deprecated

#### Deprecated API versions

These APIs are still served in version 1.22 but are in a deprecation period, and will be removed in 1.25:

  * [PodSecurityPolicy](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)
    * policy/v1beta1 PodSecurityPolicy
    * Deprecated in 1.21 with [removal targeted](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#psp-v125) for version 1.25.
  * The following Beta versions of graduated APIs will be [removed in 1.25](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) in favor of their GA versions: 
    * discovery.k8s.io/v1beta1 EndpointSlice, deprecated since 1.21
    * policy/v1beta1 PodDisruptionBudget, deprecated since 1.21
    * batch/v1beta1 CronJob, deprecated since 1.21



Change

#### Notable changes and bug fixes in 1.22

  * The `terminationGracePeriodSeconds` field on pod specs and container probes should not be negative. Negative values of `terminationGracePeriodSeconds` will be treated as the value `1` on the delete path. Immutable field validation will be relaxed in order to update negative values. In a future release, negative values will not be permitted. ([#98866](https://github.com/kubernetes/kubernetes/pull/98866))

  * As a mitigation for [CVE-2021-25740](https://github.com/kubernetes/kubernetes/issues/103675), newly created Kubernetes 1.22 clusters no longer include write access to the Endpoints API in the `edit` and `admin` roles by default. Existing clusters upgraded to Kubernetes 1.22 retain previous permissions in those roles. For instructions to re-add Endpoints write access to the `edit` and `admin` roles in newly created 1.22 clusters, refer to the [RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#write-access-for-endpoints).




## September 17, 2021

Change

#### (2021-R29) Version updates

  * Version [1.21.4-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) is now the default version in the Rapid channel.
  * Version [1.21.4-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) is now available in the Rapid channel.
  * Version 1.21.3-gke.2001 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.4-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214) with this release.



## September 07, 2021

Change

#### (2021-R28) Version updates

  * Version [1.21.3-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) is now the default version in the Rapid channel.
  * The following control plane and node versions are now available in the Rapid channel: 
    * [1.21.3-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213)
    * [1.21.4-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214)
  * Version 1.21.3-gke.2000 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.3-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## August 20, 2021

Change

#### (2021-R27) Version updates

  * Version [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version in the Rapid channel.
  * The following control plane and node versions are now available in the Rapid channel: 
    * [1.20.9-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
    * [1.21.3-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213)
  * The following versions are no longer available in the Rapid channel: 
    * 1.20.8-gke.2100
    * 1.21.3-gke.900
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.3-gke.901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## August 12, 2021

Change

#### (2021-R26) Version updates

  * The following control plane and node versions are now available in the Rapid channel: 
    * [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208)
    * [1.21.3-gke.901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213)
    * [1.21.3-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213)
  * The following control plane and node versions are no longer available in the Rapid channel: 
    * 1.20.9-gke.700
    * 1.21.3-gke.100
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.3-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## August 03, 2021

Change

#### (2021-R25) Version updates

  * Version [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version in the Rapid channel.
  * Version [1.20.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) is now available in the Rapid channel.
  * Version [1.21.3-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) is now available in the Rapid channel.
  * Version 1.20.8-gke.700 is no longer available in the Rapid channel.
  * Version 1.21.2-gke.600 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to version [1.21.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## July 27, 2021

Change

#### (2021-R24) Version updates

  * Version [1.21.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) is now available in the Rapid channel.



## July 20, 2021

Change

#### (2021-R23) Version updates

  * Version [1.20.8-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version in the Rapid channel.
  * Version [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now available in the Rapid channel.
  * Version 1.20.7-gke.2200 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.20.8-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.



## July 09, 2021

Change

#### (2021-R22) Version updates

  * Version [1.20.7-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) is now the default version.
  * Version [1.20.8-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now available in the Rapid channel.
  * Version [1.21.2-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1212) is now available in the Rapid channel.
  * Version 1.20.6-gke.1400 is no longer available in the Rapid channel.
  * Version 1.20.7-gke.1800 is no longer available in the Rapid channel.
  * Version 1.21.1-gke.2200 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.20.7-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.2-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1212) with this release.



## June 25, 2021

Change

#### (2021-R21) Version updates

  * Version [1.20.7-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) is now available in the Rapid channel.
  * Version [1.21.1-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) is now available in the Rapid channel.
  * Version 1.21.1-gke.1800 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to [1.20.7-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.20.7-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.1-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) with this release.



## June 16, 2021

Change

#### (2021-R20) Version updates

  * Version [1.20.7-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) is now available in the Rapid channel.
  * Version [1.21.1-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) is now available in the Rapid channel.
  * Version 1.21.1-gke.400 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.1-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) with this release.



## June 09, 2021

Change

#### (2021-R19) Version updates

  * Version [1.20.6-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) is now the default version in the Rapid channel.
  * Version [1.21.1-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) is now available in the Rapid channel.
  * Version 1.20.6-gke.1000 is no longer available in the Rapid channel.
  * Version 1.21.1-gke.100 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to [1.20.6-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.1-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) with this release.



## May 28, 2021

Change

#### (2021-R18) Version updates

  * Version [1.20.6-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) is now available in the Rapid channel.
  * Version [1.21.1-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) is now available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.21 to [1.21.1-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1211) with this release.



Change

#### 1.21 New Beta and Stable APIs

The following Stable APIs are new in 1.21:

  * batch/v1 CronJob
  * policy/v1 PodDisruptionBudget
  * discovery.k8s.io/v1 EndpointSlice



The following Beta APIs are new in 1.21:

  * storage.k8s.io/v1beta1 CSIStorageCapacity



Feature

#### 1.21 Features

The following features are introduced in version 1.21:

#### CronJob (GA)

The CronJob API has graduated to General Availability (GA), bringing performance improvements and allowing scheduled jobs to be run using a stable API.

  * This resource is now available in the `batch/v1` group/version.
  * The `batch/v1beta1` group/version is deprecated, and will be removed in version 1.25. See the [migration guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) for details.



#### PodDisruptionBudget (GA)

The PodDisruptionBudget has graduated to GA, allowing pod evictions to be controlled using a stable API.

  * This resource is now available in the `policy/v1` group/version.
  * The `policy/v1beta1` group/version is deprecated, and will be removed in version 1.25. See the [migration guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) for details.



#### EndpointSlice (GA)

The EndpointSlice API has graduated to GA, bringing performance improvements over the v1 Endpoints API.

  * This more scalable API for service discovery is now enabled on all clusters and is promoted to `discovery.k8s.io/v1`.
  * The `discovery.k8s.io/v1beta1` group/version is deprecated, and will be removed in version 1.25. See the [migration guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) for details.



#### Default namespace label (Beta)

Namespace API objects now have a `kubernetes.io/metadata.name` label matching their `metadata.name` field to allow selecting any namespace by its name using a label selector. This can be used for objects which select namespaces by label, such as [admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-namespaceselector) and [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/#targeting-a-namespace-by-its-name).

#### Bound service account token volumes (Beta)

  * The API credentials injected into containers at `/var/run/secrets/kubernetes.io/serviceaccount/token` are now time-limited, auto-refreshed, and invalidated when the containing pod is deleted.
  * By default, injected tokens are given an extended lifetime so they remain valid even after a new refreshed token is provided. The metric `serviceaccount_stale_tokens_total` and the audit annotation `authentication.k8s.io/stale-token` can be used to monitor for workloads that depend on the extended lifetime and are continuing to use tokens even after a refreshed token is provided to the container.
  * Clients should reload the token from disk periodically (once per minute is recommended) to ensure they use the refreshed token. `k8s.io/client-go` version 11.0.0+ and 0.15.0+ reload tokens automatically.



Change

#### 1.21 available in the Rapid channel

Kubernetes version 1.21 is now available in the Rapid channel. Before upgrading, read the [Kubernetes 1.21 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#changelog-since-v1200), especially the action required and deprecation sections.

Deprecated

#### 1.21 Deprecated APIs

The following APIs are deprecated in the 1.21 release:

  * [PodSecurityPolicy](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/)
    * policy/v1beta1 PodSecurityPolicy
    * Deprecated in 1.21 with [removal targeted](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#psp-v125) for version 1.25.
  * The following Beta versions of newly graduated APIs will be [removed in 1.25](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25) in favor of GA versions: 
    * discovery.k8s.io/v1beta1 EndpointSlice
    * policy/v1beta1 PodDisruptionBudget
    * batch/v1beta1 CronJob
  * The following Beta versions of previously graduated APIs will be [removed in 1.22](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-22) in favor of GA versions: 
    * admissionregistration.k8s.io/v1beta1, MutatingWebhookConfiguration
    * admissionregistration.k8s.io/v1beta1, ValidatingWebhookConfiguration
    * apiextensions.k8s.io/v1beta1, CustomResourceDefinition
    * apiregistration.k8s.io/v1beta1, APIService
    * authentication.k8s.io/v1beta1, TokenReview
    * authorization.k8s.io/v1beta1, LocalSubjectAccessReview
    * authorization.k8s.io/v1beta1, SelfSubjectAccessReview
    * authorization.k8s.io/v1beta1, SubjectAccessReview
    * certificates.k8s.io/v1beta1, CertificateSigningRequest
    * coordination.k8s.io/v1beta1, Lease
    * extensions/v1beta1, Ingress
    * networking.k8s.io/v1beta1, Ingress
    * networking.k8s.io/v1beta1, IngressClass
    * rbac.authorization.k8s.io/v1beta1, ClusterRole
    * rbac.authorization.k8s.io/v1beta1, ClusterRoleBinding
    * rbac.authorization.k8s.io/v1beta1, Role
    * rbac.authorization.k8s.io/v1beta1, RoleBinding
    * scheduling.k8s.io/v1beta1, PriorityClass
    * storage.k8s.io/v1beta1, CSIDriver
    * storage.k8s.io/v1beta1, CSINode
    * storage.k8s.io/v1beta1, StorageClass
    * storage.k8s.io/v1beta1, VolumeAttachment



Change

In Kubernetes 1.21, newly provisioned PersistentVolumes by gce-pd will use the `topology.kubernetes.io/zone` GA label instead of the `failure-domain.beta.kubernetes.io/zone` beta label.

## May 20, 2021

Issue

In GKE version 1.20 and later, audit logging does not occur for [Binary Authorization fail open events](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs#fail_open_events_in).

## May 19, 2021

Change

#### (2021-R17) Version updates

  * Version [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) is now the default version in the Rapid channel.
  * Version 1.19.9-gke.1900 is no longer available in the Rapid channel.
  * Version 1.19.10-gke.1000 is no longer available in the Rapid channel.
  * The following control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded with this release: 
    * From version 1.18 to [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199).
    * From version 1.19 to [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206).
    * From version 1.20 to [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206).



## May 12, 2021

Change

#### (2021-R16) Version updates

  * Version [1.19.10-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now available in the Rapid channel.
  * Version [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) is now available in the Rapid channel.
  * Version 1.20.5-gke.2000 is no longer available in the Rapid channel.
  * The following control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded with this release: 
    * From version 1.18 to [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199).
    * From version 1.19 to [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199).
    * From version 1.20 to [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206).



## May 04, 2021

Change

#### (2021-R15) Version updates

  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version in the Rapid channel.
  * Version 1.19.9-gke.1400 is no longer available in the Rapid channel.
  * The following control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded with this release: 
    * From version 1.18 to [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199).
    * From version 1.19 to [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199).



## April 29, 2021

Fixed

Fixes for the following GKE Autopilot clusters issues are rolling out to the Rapid release channel:

  * Pods with a priority lower than -10 would not trigger scale up.
  * Pod anti-affinity might cause overscaling.



## April 27, 2021

Change

#### (2021-R14) Version updates

  * Version [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version in the Rapid channel.
  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now available in the Rapid channel.
  * Version [1.20.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205) is now available in the Rapid channel.
  * Version 1.19.9-gke.700 is no longer available in the Rapid channel.
  * Version 1.20.5-gke.1300 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.18 to version [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205) with this release.



## April 20, 2021

Change

#### (2021-R13) Version updates

  * Version [1.19.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version in the Rapid channel.
  * Version [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now available in the Rapid channel.
  * Version [1.20.5-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205) is now available in the Rapid channel.
  * Version 1.19.9-gke.100 is no longer available in the Rapid channel.
  * Version 1.20.5-gke.800 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.18 to version [1.19.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.5-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205) with this release.



## April 14, 2021

Change

#### (2021-R12) Version updates

  * Version [1.19.9-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version in the Rapid channel.
  * Version [1.19.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now available in the Rapid channel.
  * Version [1.20.5-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205) is now available in the Rapid channel.
  * Version 1.19.8-gke.2000 is no longer available in the Rapid channel.
  * Version 1.20.5-gke.101 is no longer available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.18 to version [1.19.9-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.9-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.5-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205) with this release.



## April 06, 2021

Change

#### (2021-R11) Version updates

  * Version [1.19.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) is now the default version.
  * The following versions are now available in the Rapid channel: 
    * [1.19.9-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199)
    * [1.20.5-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205)
  * The following versions are no longer available in the Rapid channel: 
    * 1.19.8-gke.1600
    * 1.20.4-gke.2200
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.18 to version [1.19.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.5-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1205) with this release.



## March 29, 2021

Change

  * Version [1.19.8-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) is now the default version in the Rapid channel.
  * The following versions are now available in the Rapid channel: 
    * [1.19.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198)
    * [1.20.4-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1204)
  * The following versions are no longer available in the Rapid channel: 
    * 1.19.8-gke.1000
    * 1.20.4-gke.1800
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.8-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.4-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1204) with this release.



## March 23, 2021

Announcement

Starting tomorrow, March 24, 2021, the mechanism we use to create GKE release notes will change. Although this change does not affect the content of the notes, it does affect the presentation and underlying syntax. If you subscribe to the XML feed for this page, entries for March 24 and earlier will be updated as a result of changes to formatting and syntax; the content itself did not change.

The feed URL will also change from `https://docs.cloud.google.com/static/feeds/gke-main-release-notes.xml` to `https://docs.cloud.google.com/feeds/gke-main-release-notes.xml`. We will automatically redirect from the old URL to the new one.

Change

Windows Server, version 1909 is reaching [end of support on May 11, 2021](https://docs.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2021#products-governed-by-the-modern-policy). Newer Windows Server image versions are available in GKE versions 1.19.8-gke.1600+ and 1.20.4-gke.500+.

## March 16, 2021

Change

#### (2021-R9) Version updates

  * Version [1.19.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) is now the default version in the Rapid channel.
  * Version [1.19.8-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) is now available in the Rapid channel.
  * Version [1.20.4-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1204) is now available in the Rapid channel.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.19 to version [1.19.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) with this release.
  * Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.20 to version [1.20.4-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1204) with this release.
  * Version 1.19.7-gke.2503 is no longer available in the Rapid channel.
  * Version 1.20.4-gke.400 is no longer available in the Rapid channel.



## March 05, 2021

Change

#### (2021-R8) Version updates

  * Version [1.19.7-gke.2503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) is now available in the Rapid channel. This version is now the default.
  * Version [1.19.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198) is now available in the Rapid channel.
  * Version [1.20.4-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1204) is now available in the Rapid channel.
  * Auto-upgrading nodes and control planes in the Rapid channel upgrade from version 1.19 to version [1.19.7-gke.2503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) with this release.
  * Auto-upgrading nodes and control planes in the Rapid channel upgrade from version 1.20 to version [1.20.4-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1204) with this release.
  * Version 1.19.7-gke.1500 is no longer available in the Rapid channel.
  * Version 1.20.2-gke.2500 is no longer available in the Rapid channel.



## February 25, 2021

Fixed

[Non-deterministic treatment of objects with invalid `ownerReferences`](https://github.com/kubernetes/kubernetes/issues/65200) was fixed in version 1.20. Run the [`kubectl-check-ownerreferences`](https://github.com/kubernetes-sigs/kubectl-check-ownerreferences) tool prior to upgrade to locate existing objects with invalid `ownerReferences`.

  * A namespaced object with an `ownerReference` to another namespaced object which does not exist in the same namespace is now consistently treated as having a missing owner and is deleted.

  * A cluster-scoped object with an `ownerReference` to a namespaced object is now consistently treated as having an unresolvable owner, and is ignored by the garbage collector.

  * Starting in version 1.20, when a namespace mismatch between a child and owner object is detected, an event with a reason code of `OwnerRefInvalidNamespace` is recorded.




Change

#### (2021-R7) Version updates

  * Version [1.19.7-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) is the new default version in the Rapid channel.
  * Version [1.19.7-gke.2503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) is now available in the Rapid channel.
  * Version [1.20.2-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1202) is now available in the Rapid channel. Before upgrading to 1.20.2-gke.2500, read the 1.20 available in the Rapid channel section in the release notes.
  * Version 1.19.7-gke.1302 is no longer available in the Rapid channel.
  * Auto-upgrading control planes in the Rapid channel automatically upgrade from version 1.19 to version [1.19.7-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) with this release.
  * Auto-upgrading control planes in the Rapid channel automatically upgrade from version 1.20 to version [1.20.2-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1202) with this release.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.19 to version [1.19.7-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) with this release.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.20 to version [1.20.2-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1202) with this release.



Change

As of version 1.20, the kubelet no longer creates the `target_path` for NodePublishVolume in accordance with the CSI spec. If you have self-managed CSI drivers deployed in your cluster, ensure that they are idempotent and do any necessary mount creation or verification. For more information, see Kubernetes issue [#88759](https://github.com/kubernetes/kubernetes/pull/88759).

Change

Starting in version 1.20, timeouts on exec probes are honored, and default to 1 second if unspecified. If you have Pods using exec probes, ensure that they can easily complete in 1 second or explicitly set an appropriate timeout. For more information, see [Configure Probes](https://docs.k8s.io/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes).

Change

The `metadata.selfLink` field, [deprecated since version 1.16](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#deprecations-and-removals), is no longer populated in version 1.20. See Kubernetes [issue #1164](https://github.com/kubernetes/enhancements/issues/1164) for details. A related bug in the [`k8s.io/client-go` library](https://github.com/kubernetes/client-go) in the `GetReference` function was fixed in versions 0.15.9 or later, 0.16.4 or later, and 0.17.0 or later. Clients using the `GetReference` function should upgrade to one of those versions of `client-go` or newer in order to work correctly against an API Server running version 1.20 or later.

Change

#### 1.20 available in the Rapid channel

Kubernetes 1.20 is now available in the Rapid channel. Before upgrading to 1.20.2-gke.2500, read the [Kubernetes 1.20 ReleaseNotes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1190) especially the [Urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#urgent-upgrade-notes) and [Deprecations](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation) sections.

Change

**RuntimeClass graduated to GA in version 1.20** : The `node.k8s.io/v1beta1` RuntimeClass API has graduated to `node.k8s.io/v1` with no changes. API clients and manifests should switch to using the `node.k8s.io/v1` API after version 1.20. The `node.k8s.io/v1beta1` API is deprecated and will no longer be served starting in version 1.25.

## February 17, 2021

Change

#### (2021-R6) Version updates

  * Version [1.19.7-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) is now available in the Rapid channel. This version is now the default.
  * Version [1.19.7-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) is now available in the Rapid channel.
  * Version 1.18.12-gke.1206 is no longer available in the Rapid channel.
  * Version 1.19.7-gke.800 is no longer available in the Rapid channel.
  * Auto-upgrading control planes in the Rapid channel automatically upgrade from version 1.18 to version [1.19.7-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) with this release.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.19.7-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) with this release.



## February 09, 2021

Change

#### (2021-R5) Version updates

  * Version [1.18.12-gke.1210](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel. This version is now the default.
  * Version [1.19.7-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) is now available in the Rapid channel.
  * Version 1.18.12-gke.1205 is no longer available in the Rapid channel.
  * Version 1.19.6-gke.1700 is no longer available in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.19 to version [1.19.7-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) with this release.



## February 02, 2021

Change

#### (2021-R4) Version updates

  * Version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel.
  * Version [1.19.7-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1197) is now available in the Rapid channel.
  * Version 1.19.6-gke.600 is no longer available in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.19 to version [1.19.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1196) with this release.



## January 28, 2021

Issue

For clusters using a 1.19 version, with the [Container-Optimized OS with Containerd (`cos_containerd`)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos-containerd) node image, [`dockerd`](https://docs.docker.com/engine/reference/commandline/dockerd/) (the Docker Daemon) is not running at boot. It needs to be started manually. This issue will be fixed in a future release.

## January 25, 2021

Change

#### (2021-R3) Version updates

  * Version [1.19.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1196) is now available in the Rapid channel.



## January 19, 2021

Change

**Note:** This release note has been updated since it was originally published. The update adds an authentication change with 1.19.

Change

[Basic authentication with a password](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication#legacy-auth) has been removed in Kubernetes 1.19. Clusters upgraded to 1.19 can no longer use basic authentication to authenticate users to the control plane.

Change

#### (2021-R2) Version updates

  * Version [1.18.12-gke.1205](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel. This version is now the default.
  * Version [1.19.6-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1196) is now available in the Rapid channel. Before upgrading to 1.19.6-gke.600, read the 1.19 available in the Rapid channel section in the release notes.
  * Version 1.18.12-gke.1200 is no longer available in the Rapid channel.
  * Version 1.18.12-gke.1202 is no longer available in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.12-gke.1205](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.19 to version [1.19.6-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1196) with this release.



Feature

Seccomp (secure computing mode) support for Kubernetes has graduated to General Availability (GA). This feature can be used to increase the workload security by restricting the system calls for a Pod (applies to all containers) or individual containers.

A new `seccompProfile` field is added to Pod and Container securityContext objects, starting in Kubernetes 1.19.
    
    
    securityContext:
      seccompProfile:
        # "Unconfined", "RuntimeDefault", or "Localhost"
        type: Localhost
        # only necessary if type == Localhost
        localhostProfile: my-profiles/profile-allow.json
    

The alpha seccomp annotations `seccomp.security.alpha.kubernetes.io/pod` and `container.seccomp.security.alpha.kubernetes.io/…`are deprecated in favor of the GA API field. The alpha annotations will not be honored in Kubernetes 1.22+.

If you are currently using Seccomp annotations on Pods or Containers, you should identify and transition workloads using the annotations to set the API fields before 1.21 is released on GKE (approximately in June 2021). No change on PodSecurityPolicy is required, as it supports [both annotation and field seccomp profiles](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#seccomp). You can follow the recommended steps below:

  1. Locate Seccomp annotation usages. In your Kubernetes manifest files, search for "seccomp.security.alpha.kubernetes.io/pod" and "container.seccomp.security.alpha.kubernetes.io/"".

  2. Add or update securityContext fields. Based on your annotation usage, add or update (if securityContext already exists) the securityContext field in Pod or Container spec. The annotations can be left in place, but must match the securityContext API field.

Current annotation usage | Add or update securityContext  
---|---  
`seccomp.security.alpha.kubernetes.io/pod` | In Pod's securityContext, add seccompProfile field.  
`container.seccomp.security.alpha.kubernetes.io/CONTAINER_NAME` | In CONTAINER_NAME's securityContext, add seccompProfile field.  
  3. Set values for seccompProfile. The `type` field of seccompProfile corresponds to the annotation value, and `localhostProfile` field corresponds to the path following `localhost` annotation value.

Current annotation value | seccompProfile value  
---|---  
`unconfined` | `seccompProfile:  
type: Unconfined`  
`runtime/default`  
or `docker/default` | `seccompProfile:  
type: RuntimeDefault`  
`localhost/path/to/profile.json` | `seccompProfile:  
type: Localhost  
localhostProfile: path/to/profile.json`  



For more details, see the following pages:

  * [Restrict a Container's Syscalls with Seccomp](https://kubernetes.io/docs/tutorials/clusters/seccomp/)
  * [Seccomp to GA](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/135-seccomp)



Feature

The widely used [Ingress API](https://kubernetes.io/docs/concepts/services-networking/ingress/) has graduated to general availability in Kubernetes 1.19. The v1beta1 Ingress API is deprecated, and will no longer be served in 1.22+. Before 1.21, identify and transition clients and manifests using the v1beta1 Ingress API to use `networking.k8s.io/v1`.

Clusters with Google Cloud's operations suite enabled can use the following query to identify clients that access the Ingress v1beta1 APIs:
    
    
    resource.type="k8s_cluster"
    resource.labels.cluster_name="$CLUSTER_NAME"
    protoPayload.authenticationInfo.principalEmail:("system:serviceaccount" OR "@")
    protoPayload.request.apiVersion=("extensions/v1beta1" OR "networking.k8s.io/v1beta1")
    protoPayload.request.kind="Ingress"
    NOT ("kube-system")
    

Identify and transition clients and manifests using the v1beta1 Ingress APIs to use `networking.k8s.io/v1` before 1.21 is released on GKE (approximately in June 2021), then verify no clients are using the v1beta1 API during the 1.21 timeframe. Workloads using the v1beta1 APIs need to be upgraded before your cluster is upgraded to GKE 1.22.

To migrate manifests to networking.k8s.io/v1:

  1. Rename the `spec.backend` field (if specified) to `spec.defaultBackend`
  2. Rename each `backend.serviceName` field to `backend.service.name`
  3. Rename each numeric `backend.servicePort` field to `backend.service.port.number`
  4. Rename each string `backend.servicePort` field to `backend.service.port.name`
  5. Specify a `pathType` field for each defined path. Options are `Prefix`, `Exact`, and `ImplementationSpecific`. To match the undefined v1beta1 behavior, use `ImplementationSpecific`.



As an example, to migrate this v1beta1 manifest to v1:

### v1beta1 manifest
    
    
    apiVersion: networking.k8s.io/v1beta1
    kind: Ingress
    metadata:
      name: example
    spec:
      backend:
        serviceName: default-backend
        servicePort: 80
      rules:
      - http:
          paths:
          - path: /testpath
            backend:
              serviceName: test
              servicePort: 80
    

### v1 manifest
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: example
    spec:
      defaultBackend:
        service:
          name: default-backend
          port:
            number: 80
      rules:
      - http:
          paths:
          - path: /testpath
            pathType: ImplementationSpecific
            backend:
              service:
                name: test
                port:
                  number: 80
    

Feature

The CertificateSigningRequest API has graduated to `certificates.k8s.io/v1` in Kubernetes 1.19. The v1beta1 CertificateSigningRequest API is deprecated and will no longer be served in 1.22+.

Clusters with Google Cloud's operations suite enabled can use the following query to identify clients that access the CertificateSigningRequest v1beta1 APIs:
    
    
    resource.type="k8s_cluster"
    resource.labels.cluster_name="$CLUSTER_NAME"
    protoPayload.authenticationInfo.principalEmail:("system:serviceaccount" OR "@")
    protoPayload.request.apiVersion="certificates.k8s.io/v1beta1"
    NOT ("kube-system")
    

Identify and transition clients and manifests using the v1beta1 CertificateSigningRequest API to use `certificates.k8s.io/v1` before 1.21 is released on GKE (approximately in June 2021), then verifying no clients are using the v1beta1 API during the 1.21 timeframe. Workloads using the v1beta1 API need to be upgraded before your cluster is upgraded to GKE 1.22.

Differences between the v1beta1 and v1 API are as follows:

  * For API clients requesting certificates:

    * [spec.signerName](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers) is now required, and requests for `kubernetes.io/legacy-unknown` are not allowed to be created using the `certificates.k8s.io/v1` API
    * `spec.usages` is now required, cannot contain duplicate values, and must only contain known usages
  * For API clients approving or signing certificates:

    * `status.conditions` cannot contain duplicate types
    * `status.conditions[*].status` is now required
    * `status.certificate` must be PEM-encoded, and must contain only `CERTIFICATE` blocks



Change

#### 1.19 available in the Rapid channel

Kubernetes 1.19 is now available in Rapid channel. Before upgrading to 1.19.6-gke.600, read [Kubernetes 1.19 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md) especially the [Urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#urgent-upgrade-notes) section.

## January 08, 2021

Change

#### (2021-R1) Version updates

  * Version [1.18.12-gke.1201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel. This version is now the default.
  * Version [1.18.12-gke.1205](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.12-gke.1201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## December 14, 2020

Change

#### (R41) Version updates

  * Version [1.18.12-gke.1201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## December 07, 2020

Change

#### (R40) Version updates

  * Version [1.18.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel.
  * Version 1.18.12-gke.300 is now the default in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.
  * Version 1.18.10-gke.2701 is no longer available in the Rapid channel.



## December 01, 2020

Change

#### (R39) Version updates

  * Version [1.18.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available in the Rapid channel. This version is now the default.
  * 1.18.10-gke.2701 is now the default version in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.10-gke.2701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) with this release.
  * Version 1.18.10-gke.2101 is no longer available in the Rapid channel.



## November 25, 2020

Issue

**Auto-upgrade status**

GKE Auto-Upgrade is currently suspended for control planes, and nodes. Manual upgrades are available.

## November 24, 2020

Change

The November 17, 2020 release removed the following GKE version:

  * Version 1.18.10-gke.1500 is no longer available in the Rapid channel.



## November 12, 2020

Change

#### (R38) Version updates

This note was updated on November 24, 2020.

  * Version [1.18.10-gke.2701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) is now available in the Rapid channel. This version is now the default.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.10-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) with this release.
  * The [issue](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#September_28_2020) from September 28, 2020 with Container Threat Detection on GKE 1.18 is resolved in GKE versions versions 1.18.9-gke.1300 and later and 1.19.2-gke.2000 and later.



Fixed

The [issue](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#September_28_2020) from September 28, 2020 with Container Threat Detection on GKE 1.18 is resolved in GKE versions versions 1.18.9-gke.1300 and later and 1.19.2-gke.2000 and later.

Change

#### (R37) Version updates

  * Version [1.18.10-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) is now available in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.10-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) with this release.
  * Version 1.18.10-gke.1500 is the new default version in the Rapid channel.



## November 04, 2020

Change

#### (R36) Version updates

  * Version [1.18.10-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) is now available in the Rapid channel.

This release sets `sysctl net.netfilter.nf_conntrack_tcp_be_liberal=1` on the node image. This discourages `netfilter` from resetting TCP connections.

  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18 to version [1.18.10-gke.601](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) with this release.




## October 28, 2020

Change

#### (R35) Version updates

  * Version [1.18.10-gke.601](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11810) is now available in the Rapid channel.
  * Version 1.18.9-gke.1501 is no longer available in the Rapid channel.



## October 20, 2020

Change

#### (R34) Version updates

  * Version [1.18.9-gke.2501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1189) is now available in the Rapid channel.
  * Version 1.18.9-gke.2501 is the new default version for clusters in the Rapid channel.
  * Version 1.18.9-gke.801 is no longer available in the Rapid channel.



## October 12, 2020

Change

#### (R33) Version updates

  * Version [1.18.9-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1189) is now available in the Rapid channel.
  * Version 1.18.9-gke.801 is the new default version for clusters in the Rapid channel.
  * Version 1.17.9-gke.1504 is no longer available in the Rapid channel.
  * Version 1.18.6-gke.4801 is no longer available in the Rapid channel.
  * Auto-upgrading control planes upgrade from versions 1.17, 1.18 to version 1.18.9-gke.801 during this release.



## October 02, 2020

Change

#### (R32) Version updates

  * Version [1.18.9-gke.801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1189) is now available in the Rapid channel.



## September 25, 2020

Change

#### (R31) Version updates

  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.18.6-gke.3504 to version [1.18.6-gke.4801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1186) with this release.
  * Version 1.18.6-gke.3504 is no longer available in the Rapid channel.



## September 15, 2020

Change

#### (R30) Version updates

  * Version [1.18.6-gke.4801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1186) is now available in the Rapid channel.
  * Version 1.18.6-gke.3504 is the new default version in the Rapid channel.
  * Version 1.17.9-gke.1503 is no longer available in the Rapid channel.
  * Version 1.18.6-gke.3503 is no longer available in the Rapid channel.
  * Auto-upgrading nodes and control planes upgrade from version 1.17 to version 1.17.9-gke.1504 during this release.



## September 14, 2020

Issue

There is a known issue that prevents creating Rapid channel clusters on 1.18. To create a 1.18 cluster on the Rapid channel, create a Rapid channel cluster on 1.17, and then manually upgrade to 1.18.

Change

#### (R29.1) Version updates

  * Version [1.17.9-gke.1504](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Rapid channel. This version is now the default.



## September 03, 2020

Change

#### (R29) Version updates

  * Version [1.18.6-gke.3503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1186) is now available in the Rapid channel.



## August 27, 2020

Change

#### (R28) Version updates

  * Version 1.17.9-gke.1703 is no longer available.



## August 20, 2020

Change

#### (R27) Version updates

  * Version [1.17.9-gke.1703](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Rapid channel.
  * Version [1.17.9-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Rapid channel. This version is now the default.
  * Version 1.17.9-gke.600 is no longer available.



## August 06, 2020

Change

#### (R26) Version updates

  * Version [1.17.9-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Rapid channel.
  * Version [1.17.9-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Rapid channel.



## July 28, 2020

Change

#### (R25) Version updates

  * Version [1.17.9-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available in the Rapid channel.
  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.17.7-gke.15 to version [1.17.8-gke.17](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1178) with this release.



## July 22, 2020

Change

#### (R24) Version updates

  * Version [1.17.8-gke.17](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1178) is now available in the Rapid channel.

This version includes node image upgrades for Ubuntu (`ubuntu-gke-1804-1-17-v20200610`) and Windows Server (`windows-server-1909-dc-core-uefi-gke-v1592940889` and `windows-server-2019-dc-core-uefi-gke-v1592939281`).

  * Version [1.17.7-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1177) is now available in the Rapid channel.

This version is now the default.

  * Auto-upgrading nodes in the Rapid channel automatically upgrade from version 1.17.6-gke.11 to version [1.17.7-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1177) with this release.




## July 13, 2020

Fixed

A bug in gVisor has been fixed. Default gVisor node labels are now applied when user-specified labels.

Change

#### (R23) Version updates

  * Version [1.17.7-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1177) is now available in the Rapid channel.



## June 29, 2020

Change

[1.17.6-gke.11](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1176) is now available.

## June 23, 2020

Change

[1.17.6-gke.7](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1176) is now available.

## June 08, 2020

Change

[1.17.6-gke.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1176) is now available.

## June 01, 2020

Change

[1.17.5-gke.9](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1175) is now available.

## May 27, 2020

Issue

Due to a newly discovered issue, version 1.17.5-gke.6 is no longer available.

## May 19, 2020

Change

All GKE clusters running 1.17.3-gke.3 and up will have etcd upgraded to 3.4.7-0-gke.1. All new GKE clusters with 1.17.3-gke.3 and up will be created with etcd 3.4.7-0-gke.1.

Change

[1.17.5-gke.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1175) is now available in the Rapid release channel.

## May 13, 2020

Change

[1.17.5-gke.0](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1175) is now available in the Rapid release channel.

## April 27, 2020

Feature

The [RunAsUsername](https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/#set-the-username-for-a-pod) feature is now beta and allows specifying the username when running a Windows container.

Change

[1.17.4-gke.10](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1174) is now available in the Rapid release channel.

Although clusters in the Rapid channel upgrade automatically, you should still review:

  * [Known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#known-issues)
  * [Urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#deprecations-and-removals)



Deprecated

The following node labels are deprecated:

Cluster Versions | Deprecated Label | New Label  
---|---|---  
1.14+ | beta.kubernetes.io/os | kubernetes.io/os  
1.14+ | beta.kubernetes.io/arch | kubernetes.io/arch  
1.17+ | beta.kubernetes.io/instance-type | node.kubernetes.io/instance-type  
1.17+ | failure-domain.beta.kubernetes.io/zone | topology.kubernetes.io/zone  
1.17+ | failure-domain.beta.kubernetes.io/region | topology.kubernetes.io/region  
  
You must identify any node selectors using beta labels and modify them to use GA labels.

Deprecated

RBAC in the `apps/v1alpha1` and `apps/v1beta1` API versions are deprecated in 1.17 and will no longer be served in 1.20. Update your manifests and API clients to use the `rbac.authorization.k8s.io/v1` APIs before 1.20 to avoid any issues.

Feature

The RuntimeClass scheduler simplifies [scheduling Windows Pods to appropriate nodes](https://kubernetes.io/docs/concepts/containers/runtime-class/#scheduling)

## April 15, 2020

Change

[1.16.8-gke.9](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid) is now available in the Rapid release channel.

## April 07, 2020

Change

[1.16.8-gke.8](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#changelog-since-v1167) is now available in the Rapid release channel. The node image for Container-Optimized OS is updated to [cos-77-12371-208-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m77).

## April 01, 2020

Change

[1.16.8-gke.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#changelog-since-v1167) is now available in the Rapid release channel.

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

## March 26, 2020

Change

[1.16.8-gke.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#changelog-since-v1167) is now available in the Rapid release channel.

## March 20, 2020

Change

[1.16.6-gke.18](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#changelog-since-v1165) is now available in the Rapid release channel.

## March 16, 2020

Change

[1.16.6-gke.13](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#changelog-since-v1165) is now available in the Rapid release channel.

## March 06, 2020

Feature

The user interface for creating clusters in [Google Cloud Console](https://console.cloud.google.com/kubernetes/add) has been redesigned. The new design makes it easier to follow GKE best practices.

Change

[1.16.6-gke.12](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#changelog-since-v1165) is now available in the Rapid release channel.

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

## February 24, 2020

Feature

[Ingress for Internal HTTP(S) Load Balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) is now available in Beta. This enables private L7 load balancing inside the VPC that can be deployed with Ingress resources.

## February 18, 2020

Change

1.16.5-gke.2 is now available in the Rapid release channel.

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

Change

Node image for Container-Optimized OS updated to [cos-77-12371-141-0](https://docs.cloud.google.com/container-optimized-os/docs/release-notes).

## February 11, 2020

Change

1.16.4-gke.30 is now available in the Rapid release channel.

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

## February 04, 2020

Change

1.16.4-gke.27 is now available in the Rapid release channel.

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

## January 29, 2020

Change

1.16.4-gke.25 is now available in the Rapid release channel.

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

## January 27, 2020

Feature

The ability to [create clusters with node pools running Microsoft Windows Server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows) is now in Beta.

## January 22, 2020

Change

1.16.4-gke.22 is now available in the Rapid release channel.

Change

Added ability to specify minimum CPU Platform for auto-provisioned node pools.

**Important:** Existing clusters enrolled in the Rapid release channel will be auto-upgraded to this version.

## January 08, 2020

Issue

**Do not update to version 1.16.0-gke.20 if you depend on HPA.** Horizontal Pod Autoscaling is not working in this version due to a recently discovered issue. A fix will be released with GKE 1.16.3+.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
