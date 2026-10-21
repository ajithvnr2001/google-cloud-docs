---
url: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-nochannel/
title: GKE release notes (No channel) \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:58.164218+00:00
---

# GKE release notes (No channel)  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-nochannel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE release notes (No channel) Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** Not enrolling your cluster in a release channel (known as _No channel_ , and formerly as _Static_) is a deprecated configuration option, only allowed for existing customers, and will be removed on June 14, 2027. New customers can't create or update their cluster to use this configuration option. For any clusters not enrolled in a release channel, we recommend that you [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster) before this date. After the removal date, GKE enrolls all remaining clusters in the Stable channel. For more information about this deprecation and how you can achieve the same functionality with release channels, see [Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel).

This page documents Google Kubernetes Engine version updates that are _not_ part of a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), that is, No Channel (formerly _Static_).

For all Google Kubernetes Engine version updates, fixes, known issues, or new features, see [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes). For more detailed information about security-related known issues, see the [security bulletin](https://docs.cloud.google.com/kubernetes-engine/docs/security-bulletins) page.

To view release notes for versions prior to 2020, see the [Release notes archive](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-archive).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gke-no-channel-release-notes.xml) directly. 

**Note** : Your clusters might not have the latest released versions. Rollouts begin on the day of the note and take four or more business days to be completed across all Google Cloud zones.

## October 08, 2026

Change

#### (2026-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.36.4-gke.1391002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.34.12-gke.1153000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)
    * [1.35.8-gke.1919000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)
    * [1.36.4-gke.1391002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)
    * [1.36.4-gke.1495002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)
    * [1.36.4-gke.2046002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)
    * [1.36.4-gke.2202002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)
    * [1.36.4-gke.2304000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)
    * [1.36.4-gke.2326000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)
  * The following node versions are now available: 
    * [1.31.14-gke.2925000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2925000)
    * [1.32.13-gke.2662000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2662000)
    * [1.33.13-gke.1915000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1915000)
    * [1.34.12-gke.1153000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1153000)
    * [1.35.8-gke.1919000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1919000)
    * [1.36.4-gke.1391002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)
    * [1.36.4-gke.1495002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495002)
    * [1.36.4-gke.2046002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046002)
    * [1.36.4-gke.2202002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2202002)
    * [1.36.4-gke.2304000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2304000)
    * [1.36.4-gke.2326000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2326000)
  * The following versions are no longer available: 
    * 1.34.11-gke.1044000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1036000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1380001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.4-gke.1247000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.4-gke.1391000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.4-gke.2046000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
      * 1.36 to [1.36.4-gke.1391002](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391002)



## October 02, 2026

Change

#### (2026-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.34.12-gke.1011000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)
    * [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)
    * [1.35.8-gke.1380001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)
    * [1.35.8-gke.1439001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)
    * [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
    * [1.35.8-gke.1796000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)
    * [1.36.4-gke.2046000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)
  * The following node versions are now available: 
    * [1.31.14-gke.2825000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2825000)
    * [1.32.13-gke.2567000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2567000)
    * [1.33.13-gke.1815000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1815000)
    * [1.34.12-gke.1011000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-12-gke-1011000)
    * [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)
    * [1.35.8-gke.1380001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380001)
    * [1.35.8-gke.1439001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439001)
    * [1.35.8-gke.1626001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626001)
    * [1.35.8-gke.1796000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1796000)
    * [1.36.4-gke.2046000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-2046000)
  * The following versions are no longer available: 
    * 1.34.9-gke.1065000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.10-gke.1328000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1380000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1439000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1626000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1767000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
      * 1.34 to [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
      * 1.35 to [1.35.6-gke.1250001](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250001)
      * 1.36 to [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)



## September 23, 2026

Change

#### (2026-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.8-gke.1225000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1225000) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
    * [1.35.8-gke.1626000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)
    * [1.36.4-gke.1495000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)
  * The following node versions are now available: 
    * [1.31.14-gke.2759000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2759000)
    * [1.32.13-gke.2504000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2504000)
    * [1.33.13-gke.1721000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1721000)
    * [1.34.11-gke.1209000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1209000)
    * [1.35.8-gke.1626000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1626000)
    * [1.36.4-gke.1495000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1495000)
  * The following versions are no longer available: 
    * 1.34.10-gke.1236000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.7-gke.1222000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.4-gke.1082000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.11-gke.1044000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1044000)



## September 17, 2026

Change

#### (2026-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.8-gke.1036000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
    * [1.35.8-gke.1439000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)
    * [1.36.4-gke.1391000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)
  * The following node versions are now available: 
    * [1.31.14-gke.2704000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2704000)
    * [1.32.13-gke.2427000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2427000)
    * [1.33.13-gke.1647000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1647000)
    * [1.34.11-gke.1102000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1102000)
    * [1.35.8-gke.1439000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1439000)
    * [1.36.4-gke.1391000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1391000)
  * The following versions are no longer available: 
    * 1.34.10-gke.1106000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.7-gke.1150000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1640000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.10-gke.1328000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)
      * 1.34 to [1.35.6-gke.1250000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.10-gke.1328000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)
      * 1.35 to [1.35.6-gke.1250000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-6-gke-1250000)
      * 1.36 to [1.36.3-gke.1767000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)



## September 08, 2026

Change

#### (2026-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.7-gke.1222000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
    * [1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
    * [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)
  * The following node versions are now available: 
    * [1.31.14-gke.2689000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)
    * [1.32.13-gke.2411000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)
    * [1.33.13-gke.1636000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)
    * [1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
    * [1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
    * [1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)
  * The following versions are no longer available: 
    * 1.34.10-gke.1079000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.7-gke.1027000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1537000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.35 to [1.35.7-gke.1222000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)
      * 1.36 to [1.36.3-gke.1640000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1640000)



## September 02, 2026

Change

#### (2026-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)
    * [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)
  * The following node versions are now available: 
    * [1.31.14-gke.2667000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.2393000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.11-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13411)
    * [1.35.8-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.36.4-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1364)
  * The following versions are no longer available: 
    * 1.34.9-gke.1610001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1710000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.8-gke.1026000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.2-gke.2064000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
      * 1.36 to [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)



## August 26, 2026

Change

#### (2026-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following node versions are now available: 
    * [1.31.14-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.2337000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.10-gke.1328000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.35.8-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1358)
    * [1.36.3-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available: 
    * 1.34.9-gke.1322001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1641000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.9-gke.1610001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.9-gke.1610001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)



## August 20, 2026

Change

#### (2026-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.34.9-gke.1322001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.9-gke.1610001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following node versions are now available: 
    * [1.31.14-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.2314000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1322001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.9-gke.1610001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.9-gke.1655001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.34.10-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1222000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1640000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available: 
    * 1.33.13-gke.1101000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.13-gke.1109000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.13-gke.1269000
    * 1.33.13-gke.1329000
    * 1.33.13-gke.1414000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.13-gke.1462000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1322000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1610000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1655000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1258000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.2-gke.1498000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.33 to [1.34.9-gke.1322001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.9-gke.1322001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)



## August 14, 2026

Change

#### (2026-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.13-gke.1462000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following node versions are now available: 
    * [1.31.14-gke.2579000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.2268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1462000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.10-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available: 
    * 1.33.13-gke.1011000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1278000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1287000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1057002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1163012 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1241004 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.2-gke.1346000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1244000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.3-gke.1253000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.35 to [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)



## August 12, 2026

Change

#### (2026-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.13-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1244000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
    * [1.36.3-gke.1253000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following node versions are now available: 
    * [1.31.14-gke.2543000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.2231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.10-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v13410)
    * [1.35.7-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1357)
    * [1.36.3-gke.1244000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
    * [1.36.3-gke.1253000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1363)
  * The following versions are no longer available: 
    * 1.33.12-gke.1270000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.9-gke.1131000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1127000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.2-gke.2281000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.35 to [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)



## July 30, 2026

Change

#### (2026-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.2281000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following node versions are now available: 
    * [1.30.14-gke.2866000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.2175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1329000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.2281000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available: 
    * 1.33.12-gke.1165000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1126000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1049000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.6-gke.1638000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.4447000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.4681000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.33 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.34 to [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
      * 1.35 to [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.2-gke.1346000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)



## July 24, 2026

Change

#### (2026-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1638000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following node versions are now available: 
    * [1.30.14-gke.2846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2437000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.2137000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1638000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.35.6-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.2064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available: 
    * 1.35.5-gke.1241004 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.3712000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
      * 1.35 to [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## July 16, 2026

Change

#### (2026-R30) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.1498000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following node versions are now available: 
    * [1.30.14-gke.2825000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1930000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1322000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.2-gke.1498000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following versions are no longer available: 
    * 1.33.12-gke.1059000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1000000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1163012 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.3070003 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.3302004 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
      * 1.36 to [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## July 10, 2026

Change

#### (2026-R29) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.2-gke.1346000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)
  * The following node versions are now available: 
    * [1.30.14-gke.2816000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1913000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.2-gke.1346000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1362)



## July 09, 2026

Change

#### (2026-R28) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following node versions are now available: 
    * [1.30.14-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1844000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.13-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13313)
    * [1.34.9-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.4447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available: 
    * 1.33.12-gke.1000000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.12-gke.1116000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.12-gke.1208000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.7-gke.1499000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1218000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.8-gke.1284000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1000004 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1324000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.2684000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



Change

#### (2026-R27) Version updates

There are no version updates for 2026-R27.

## June 29, 2026

Change

#### (2026-R26) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.3302004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following node versions are now available: 
    * [1.30.14-gke.2746000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1829000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.9-gke.1065000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1349)
    * [1.35.6-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1356)
    * [1.36.0-gke.3302004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available: 
    * 1.33.11-gke.1197000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.7-gke.1055000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.2190000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1000000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.2459000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.3302001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
      * 1.35 to [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## June 26, 2026

Change

#### (2026-R25) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.33.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1284000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1000004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1324000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.3302001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following node versions are now available: 
    * [1.30.14-gke.2710000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.12-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.33.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1284000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1000004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1163012](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1241004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.35.5-gke.1324000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.3302001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following versions are no longer available: 
    * 1.33.11-gke.1074000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.12-gke.1166000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1307000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1389002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1057000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1163000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.5-gke.1241000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.36.0-gke.3009002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.5-gke.1057002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)



Change

#### (2026-R24) Version updates

There are no version updates for 2026-R24.

## June 12, 2026

Change

#### (2026-R23) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.12-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1241000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3009002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * The following node versions are now available: 
    * [1.30.14-gke.2681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.2074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1729000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.12-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1241000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
    * [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.2684000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3009002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
    * [1.36.0-gke.3070003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.33 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
      * 1.34 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
      * 1.36 to [1.36.0-gke.2459000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#v1360)



## June 04, 2026

Change

#### (2026-R22) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1163000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following node versions are now available: 
    * [1.30.14-gke.2608000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1986000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1657000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.12-gke.1116000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1163000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following versions are no longer available: 
    * 1.33.11-gke.1013000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1154000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1389000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1993000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## May 27, 2026

Change

#### (2026-R21) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following node versions are now available: 
    * [1.30.14-gke.2558000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1967000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1592000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.12-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.5-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following versions are no longer available: 
    * 1.33.10-gke.1115000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.10-gke.1176000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1068000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.6-gke.1237000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1234000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1234002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1737000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
      * 1.34 to [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
      * 1.35 to [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## May 21, 2026

Change

#### (2026-R20) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)
  * The following node versions are now available: 
    * [1.30.14-gke.2530000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1942000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1551000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.12-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13312)
    * [1.34.8-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1348)
    * [1.35.3-gke.1389002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.35.5-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1355)



## May 13, 2026

Change

#### (2026-R19) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1234002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following node versions are now available: 
    * [1.30.14-gke.2458000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1868000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1492000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1197000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1499000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1234002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
    * [1.35.3-gke.2190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following versions are no longer available: 
    * 1.33.9-gke.1060000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.10-gke.1067000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.11-gke.1137000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.7-gke.1321000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1962000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.3-gke.1522000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.34 to [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)



## May 06, 2026

Change

#### (2026-R18) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.33.11-gke.1137000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1321000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1993000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following node versions are now available: 
    * [1.30.14-gke.2441000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1850000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1449000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1137000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1321000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1993000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following versions are no longer available: 
    * 1.32.13-gke.1059000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1205000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1258000
    * 1.32.13-gke.1318000
    * 1.32.13-gke.1362000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1407000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.8-gke.1026000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.5-gke.1076000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.1-gke.1396002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1269001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1485000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
      * 1.34 to [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 29, 2026

Change

#### (2026-R17) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.13-gke.1407000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1737000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following node versions are now available: 
    * [1.30.14-gke.2415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1823000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1407000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1074000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.7-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1347)
    * [1.35.3-gke.1737000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following versions are no longer available: 
    * 1.32.12-gke.1026000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.12-gke.1076000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.12-gke.1127000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1090000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.32.13-gke.1147000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.5-gke.2469000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.8-gke.1112000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.8-gke.1169000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.9-gke.1117000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.9-gke.1166000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.4-gke.1047000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.4-gke.1130000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.4-gke.1193000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.5-gke.1153000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.5-gke.1208000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1842000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.32 to [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
      * 1.33 to [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
      * 1.34 to [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
      * 1.35 to [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 22, 2026

Change

#### (2026-R16) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.32.13-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1522000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following node versions are now available: 
    * [1.30.14-gke.2407000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1816000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.11-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13311)
    * [1.34.6-gke.1307000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1522000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 15, 2026

Change

#### (2026-R15) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.32.13-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following node versions are now available: 
    * [1.30.14-gke.2369000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1790000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1237000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1389000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 09, 2026

Change

#### (2026-R14) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
  * The following node versions are now available: 
    * [1.30.14-gke.2320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1723000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)



## April 02, 2026

Change

#### (2026-R13) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.32.13-gke.1205000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.2-gke.1962000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following node versions are now available: 
    * [1.30.14-gke.2286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1205000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
    * [1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
    * [1.35.2-gke.1962000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)



## March 25, 2026

Change

#### (2026-R12) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.35.1-gke.1396002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.13-gke.1147000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1842000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following node versions are now available: 
    * [1.30.14-gke.2250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1634000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1147000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1842000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available: 
    * 1.32.11-gke.1264000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.5-gke.2392000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.3-gke.1444000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.1-gke.1396001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
      * 1.34 to [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)



## March 18, 2026

Change

#### (2026-R11) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.13-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1117000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1153000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.1-gke.1396002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
    * [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
    * [1.35.2-gke.1485000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following node versions are now available: 
    * [1.30.14-gke.2215000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1117000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1153000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.1-gke.1396002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
    * [1.35.2-gke.1269001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
    * [1.35.2-gke.1485000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available: 
    * 1.32.11-gke.1211000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.33.5-gke.2326000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.34.3-gke.1318000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.0-gke.2745005 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.0-gke.3047001 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.0-gke.3047002 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
    * 1.35.2-gke.1269000 is [deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support). This version will be removed in 90 days, or at the end of support, if sooner.
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
      * 1.35 to [1.35.1-gke.1396002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)



## March 12, 2026

Change

#### (2026-R10) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following node versions are now available: 
    * [1.30.14-gke.2192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1576000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.13-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213)
    * [1.33.9-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339)
    * [1.34.5-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345)
    * [1.35.2-gke.1269000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
  * The following versions are no longer available: 
    * 1.32.11-gke.1174000
    * 1.33.5-gke.2228001
    * 1.34.3-gke.1245000
    * 1.35.1-gke.1616000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.32 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
      * 1.33 to [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)



## March 05, 2026

Change

#### (2026-R9) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2745005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.1-gke.1396001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
    * [1.35.1-gke.1616000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following node versions are now available: 
    * [1.30.14-gke.2154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1526000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.12-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2745005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.1-gke.1396001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
    * [1.35.1-gke.1616000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following versions are no longer available: 
    * 1.32.11-gke.1038000
    * 1.33.5-gke.2172001
    * 1.34.3-gke.1051003
    * 1.35.0-gke.2398002
    * 1.35.0-gke.2745003
    * 1.35.0-gke.2745004
    * 1.35.1-gke.1396000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2745005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 25, 2026

Change

#### (2026-R8) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2745004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.1-gke.1396000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following node versions are now available: 
    * [1.30.14-gke.2117000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1476000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.12-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1112000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2745004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.1-gke.1396000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351)
  * The following versions are no longer available: 
    * 1.33.5-gke.2118001
    * 1.35.0-gke.2232003
    * 1.35.0-gke.2398000
    * 1.35.0-gke.3047000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2398002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 19, 2026

Change

#### (2026-R7) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2232003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2398002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2745003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following node versions are now available: 
    * [1.30.14-gke.2071000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1423000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.12-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212)
    * [1.33.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338)
    * [1.34.4-gke.1047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344)
    * [1.35.0-gke.2232003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2398002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2745003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.3047000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available: 
    * 1.32.9-gke.1734000
    * 1.33.5-gke.2100001
    * 1.35.0-gke.2232000
    * 1.35.0-gke.2745000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
      * 1.35 to [1.35.0-gke.2232003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 11, 2026

Change

#### (2026-R6) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2398000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2745000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following node versions are now available: 
    * [1.30.14-gke.2026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1376000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.11-gke.1264000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1444000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2398000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
    * [1.35.0-gke.2745000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)
  * The following versions are no longer available: 
    * 1.32.9-gke.1728000
    * 1.33.5-gke.2072001
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.32 to [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.33 to [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.35 to [1.35.0-gke.2232000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1350)



## February 04, 2026

Change

#### (2026-R5) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following node versions are now available: 
    * [1.30.14-gke.1991000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.11-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1318000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available: 
    * 1.32.9-gke.1711000
    * 1.32.11-gke.1153001
    * 1.33.5-gke.2019000
    * 1.33.5-gke.2100000
    * 1.33.5-gke.2288001
    * 1.34.1-gke.3971002
    * 1.34.3-gke.1136000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.32 to [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
      * 1.33 to [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)



## January 29, 2026

Change

#### (2026-R4) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.11-gke.1153001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2288001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3971002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following node versions are now available: 
    * [1.29.15-gke.2725000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1973000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1319000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.11-gke.1153001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.32.11-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2100001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2118001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2172001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2228001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2288001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.33.5-gke.2326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3971002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.3-gke.1051003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
    * [1.34.3-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available: 
    * 1.32.9-gke.1675000
    * 1.32.11-gke.1075000
    * 1.33.5-gke.1956000
    * 1.33.5-gke.2072000
    * 1.33.5-gke.2118000
    * 1.33.5-gke.2172000
    * 1.33.5-gke.2228000
    * 1.34.1-gke.3947002
    * 1.34.1-gke.3971001
    * 1.34.3-gke.1051000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2072001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3971002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 21, 2026

Change

#### (2026-R3) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.32.11-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2228000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3947002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3971001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following node versions are now available: 
    * [1.29.15-gke.2680000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1922000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1243000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.11-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2228000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3947002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3971001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available: 
    * 1.31.14-gke.1081000
    * 1.31.14-gke.1114000
    * 1.31.14-gke.1156000
    * 1.31.14-gke.1166000
    * 1.31.14-gke.1175000
    * 1.31.14-gke.1214000
    * 1.32.9-gke.1632000
    * 1.33.5-gke.1308000
    * 1.34.1-gke.3899001
    * 1.34.1-gke.3947000
    * 1.34.1-gke.3971000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.31 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.32 to [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3947002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 15, 2026

Change

#### (2026-R2) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.14-gke.1214000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following node versions are now available: 
    * [1.29.15-gke.2660000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1901000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1214000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.11-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13211)
    * [1.33.5-gke.2172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.3-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1343)
  * The following versions are no longer available: 
    * 1.31.13-gke.1139000
    * 1.32.9-gke.1239000
    * 1.33.5-gke.1162000
    * 1.34.1-gke.3355002
    * 1.34.1-gke.3355004
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.31 to [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.32 to [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3899001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 07, 2026

Change

#### (2026-R1) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3899001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following node versions are now available: 
    * [1.28.15-gke.3290000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2629000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1870000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1734000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3899001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available: 
    * 1.31.13-gke.1023000
    * 1.31.13-gke.1454000
    * 1.31.14-gke.1033000
    * 1.31.14-gke.1045000
    * 1.32.9-gke.1108000
    * 1.32.9-gke.1548000
    * 1.32.9-gke.1575000
    * 1.32.9-gke.1592000
    * 1.33.5-gke.1125000
    * 1.33.5-gke.1201000
    * 1.33.5-gke.1862000
    * 1.33.5-gke.1894000
    * 1.34.0-gke.2201000
    * 1.34.1-gke.2541000
    * 1.34.1-gke.2909002
    * 1.34.1-gke.3084002
    * 1.34.1-gke.3355001
    * 1.34.1-gke.3403002
    * 1.34.1-gke.3556000
    * 1.34.1-gke.3759000
    * 1.34.1-gke.3899000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.31 to [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
      * 1.32 to [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.3355004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## January 05, 2026

Change

#### (2025-R54) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.31.14-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3947000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following node versions are now available: 
    * [1.28.15-gke.3285000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2617000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1861000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1728000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3947000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## December 29, 2025

Change

#### (2025-R53) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following node versions are now available: 
    * [1.28.15-gke.3280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2613000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1855000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1156000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3899000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## December 18, 2025

Change

#### (2025-R52) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
    * [1.34.1-gke.2541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following node versions are now available: 
    * [1.28.15-gke.3251000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2585000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1114000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1675000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
    * [1.34.1-gke.3759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## December 10, 2025

Change

#### (2025-R51) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.31.14-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3403002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3556000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following node versions are now available: 
    * [1.28.15-gke.3225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2553000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1794000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3403002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3556000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available: 
    * 1.31.13-gke.1231000
    * 1.31.13-gke.1377000
    * 1.32.9-gke.1330000
    * 1.32.9-gke.1462000
    * 1.33.5-gke.1791000
    * 1.34.1-gke.2037001
    * 1.34.1-gke.3403001



## December 05, 2025

Change

#### (2025-R50) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.14-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1592000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1894000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2909002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3084002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3355001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3403001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following node versions are now available: 
    * [1.28.15-gke.3202000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2520000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1760000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1592000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1894000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.2909002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3084002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3355001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3403001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following versions are no longer available: 
    * 1.31.13-gke.1008000
    * 1.31.13-gke.1040000
    * 1.31.13-gke.1123000
    * 1.31.14-gke.1033000
    * 1.32.9-gke.1092000
    * 1.32.9-gke.1130000
    * 1.32.9-gke.1207000
    * 1.32.9-gke.1575000
    * 1.33.5-gke.1080000
    * 1.33.5-gke.1350000
    * 1.33.5-gke.1521000
    * 1.33.5-gke.1697000
    * 1.34.1-gke.1829001
    * 1.34.1-gke.2037002
    * 1.34.1-gke.2541000
    * 1.34.1-gke.2909000
    * 1.34.1-gke.2980000
    * 1.34.1-gke.3084001
    * 1.34.1-gke.3225000
    * 1.34.1-gke.3355000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
      * 1.34 to [1.34.1-gke.2909002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## November 28, 2025

Change

#### (2025-R49) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.31.14-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1862000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2037001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2037002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2909000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2980000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3084001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * The following node versions are now available: 
    * [1.28.15-gke.3188000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2505000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1746000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.14-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
    * [1.32.9-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1862000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2037001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2037002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2909000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.2980000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3084001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
    * [1.34.1-gke.3355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.34 to [1.34.1-gke.2909000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)



## November 20, 2025

Change

#### (2025-R48) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.31.13-gke.1454000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1548000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1791000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.3163000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2467000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1719000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1454000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1548000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1791000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## November 14, 2025

Change

#### (2025-R47) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.31.13-gke.1377000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1462000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.3096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2380000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1658000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1377000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1462000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## November 07, 2025

Change

#### (2025-R46) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.13-gke.1231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1330000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1521000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.2966000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1525000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1330000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1521000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available: 
    * 1.31.12-gke.1265000
    * 1.32.9-gke.1072000
    * 1.33.4-gke.1350000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 29, 2025

Change

#### (2025-R45) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.2857000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1426000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available: 
    * 1.31.12-gke.1220000
    * 1.32.9-gke.1010000
    * 1.33.4-gke.1245000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)



## October 22, 2025

Change

#### (2025-R44) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.2793000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2085000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1408000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available: 
    * 1.31.11-gke.1036000
    * 1.32.8-gke.1170000
    * 1.33.4-gke.1172000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.31 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
      * 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)



## October 15, 2025

Change

#### (2025-R43) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.2002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1349000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available: 
    * 1.32.8-gke.1134000
    * 1.33.4-gke.1134000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.32 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
      * 1.33 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)



## October 08, 2025

Change

#### (2025-R42) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available: 
    * 1.30.14-gke.1108000
    * 1.30.14-gke.1130000
    * 1.30.14-gke.1150000
    * 1.30.14-gke.1267000
    * 1.30.14-gke.1316000
    * 1.30.14-gke.1325000
    * 1.32.6-gke.1060000
    * 1.32.8-gke.1108000
  * Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: 
    * GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades: 
      * 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.31 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
      * 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
      * 1.32 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
      * 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)



## October 02, 2025

Change

#### (2025-R41) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    * [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available: 
    * 1.30.14-gke.1059000
    * 1.31.12-gke.1110000
    * 1.32.6-gke.1025000
    * 1.33.3-gke.1136000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 29, 2025

Change

#### (2025-R40) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following node versions are now available: 
    * [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  * The following versions are no longer available: 
    * 1.30.14-gke.1036000
    * 1.31.12-gke.1083000
    * 1.32.8-gke.1026000
    * 1.33.4-gke.1036000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 18, 2025

Change

#### (2025-R39) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following node versions are now available: 
    * [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    * [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available: 
    * 1.30.14-gke.1011000
    * 1.31.12-gke.1060000
    * 1.32.7-gke.1079000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 11, 2025

Change

#### (2025-R38) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following node versions are now available: 
    * [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available: 
    * 1.30.12-gke.1414000
    * 1.31.12-gke.1014000
    * 1.32.7-gke.1016000
    * 1.33.2-gke.1043000
    * 1.33.2-gke.1240000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.



## September 03, 2025

Change

#### (2025-R37) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following node versions are now available: 
    * [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available: 
    * 1.30.12-gke.1390000
    * 1.31.11-gke.1002000
    * 1.31.11-gke.1101000
    * 1.32.6-gke.1125000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.



## August 27, 2025

Change

#### (2025-R36) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following node versions are now available: 
    * [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available: 
    * 1.30.12-gke.1372000
    * 1.31.10-gke.1067000
    * 1.31.11-gke.1064000
    * 1.31.11-gke.1135000
    * 1.32.6-gke.1096000
    * 1.32.8-gke.1005000
    * 1.33.2-gke.1111000
    * 1.33.3-gke.1392000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.



## August 21, 2025

Change

#### (2025-R35) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
    * [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following node versions are now available: 
    * [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    * [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    * [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
    * [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  * The following versions are no longer available: 
    * 1.30.12-gke.1340000
    * 1.31.10-gke.1034000
    * 1.32.6-gke.1013000
    * 1.33.1-gke.1584000
    * 1.33.3-gke.1250000
    * 1.33.3-gke.1266000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 14, 2025

Change

#### (2025-R34) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
    * [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following node versions are now available: 
    * [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
    * [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following versions are no longer available: 
    * 1.30.12-gke.1333000
    * 1.31.10-gke.1021000
    * 1.32.4-gke.1767000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 06, 2025

Change

#### (2025-R33) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following node versions are now available: 
    * [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    * [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
    * [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  * The following versions are no longer available: 
    * 1.30.12-gke.1320000
    * 1.31.9-gke.1287000
    * 1.32.4-gke.1698000
    * 1.33.2-gke.4780000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.



## August 01, 2025

Change

#### (2025-R32) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following node versions are now available: 
    * [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available: 
    * 1.30.12-gke.1279000
    * 1.31.9-gke.1218000
    * 1.32.2-gke.1297002
    * 1.32.4-gke.1415000
    * 1.33.2-gke.4655000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.



## July 25, 2025

Change

#### (2025-R31) Version updates

**Note** : Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following node versions are now available: 
    * [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
    * [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following versions are no longer available: 
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
    * 1.32.2-gke.1182003
    * 1.32.4-gke.1353003
    * 1.32.4-gke.1603000
    * 1.33.1-gke.1107000
    * 1.33.1-gke.1386000
    * 1.33.1-gke.1744000
    * 1.33.1-gke.1959000
    * 1.33.2-gke.1384000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.



## July 16, 2025

Change

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following node versions are now available: 
    * [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## July 11, 2025

Change

#### (2025-R29) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following node versions are now available: 
    * [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1614000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## July 02, 2025

Change

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
    * [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  * The following node versions are now available: 
    * [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1607000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
    * [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
    * [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## June 27, 2025

Change

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following node versions are now available: 
    * [1.28.15-gke.2445000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1594000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)



## June 18, 2025

Change

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following node versions are now available: 
    * [1.27.16-gke.2894000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2428000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1549000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available: 
    * 1.30.12-gke.1033000
    * 1.31.8-gke.1045000
    * 1.32.4-gke.1236007
    * 1.33.0-gke.2248000
    * 1.33.1-gke.1545000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.



## June 12, 2025

Change

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following node versions are now available: 
    * [1.27.16-gke.2874000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1523000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available: 
    * 1.30.11-gke.1217000
    * 1.31.7-gke.1390000
    * 1.32.4-gke.1106006
    * 1.32.4-gke.1353001
    * 1.32.4-gke.1415001
    * 1.32.4-gke.1533000
    * 1.33.1-gke.1375000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.



## June 05, 2025

Change

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
    * [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following node versions are now available: 
    * [1.27.16-gke.2853000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2380000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1493000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
    * [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
    * [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  * The following versions are no longer available: 
    * 1.30.11-gke.1157000
    * 1.31.7-gke.1265000
    * 1.31.9-gke.1044000
    * 1.32.3-gke.1927009
    * 1.32.4-gke.1236006
    * 1.32.4-gke.1353000
    * 1.32.4-gke.1415000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.



Change

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

## May 30, 2025

Change

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following node versions are now available: 
    * [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following versions are no longer available: 
    * 1.30.11-gke.1131000
    * 1.31.7-gke.1212000
    * 1.31.9-gke.1005000
    * 1.32.3-gke.1785003
    * 1.32.4-gke.1106000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.



Change

#### (2025-R21) Version updates

There are no version updates for 2025-R21.

## May 23, 2025

Change

#### (2025-R20) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1353000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following node versions are now available: 
    * [1.27.16-gke.2810000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1395000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
    * [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
    * [1.32.4-gke.1353000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following versions are no longer available: 
    * 1.30.10-gke.1070000
    * 1.31.6-gke.1064001
    * 1.32.3-gke.1927002
    * 1.32.4-gke.1236000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.3-gke.1927009](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.



## May 16, 2025

Change

#### (2025-R19) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.4-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following node versions are now available: 
    * [1.27.16-gke.2771000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.4-gke.1236000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323) with this release.



## May 09, 2025

Change

#### (2025-R18) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.3-gke.1927002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.4-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following node versions are now available: 
    * [1.27.16-gke.2732000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
    * [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
    * [1.32.3-gke.1785003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.3-gke.1927002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
    * [1.32.4-gke.1106000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  * The following versions are no longer available: 
    * 1.31.6-gke.1020000
    * 1.32.3-gke.1785000
    * 1.32.3-gke.1927000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.



## May 02, 2025

Change

#### (2025-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1927000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following node versions are now available: 
    * [1.27.16-gke.2703000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1927000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available: 
    * 1.30.10-gke.1102000
    * 1.31.6-gke.1099001
    * 1.32.1-gke.1357001
    * 1.32.2-gke.1182001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.



## April 28, 2025

Change

#### (2025-R16) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1785000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following node versions are now available: 
    * [1.27.16-gke.2682000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2142000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1193000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.3-gke.1785000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available: 
    * 1.29.13-gke.1038000
    * 1.29.13-gke.1169000
    * 1.29.14-gke.1018000
    * 1.29.14-gke.1067000
    * 1.29.14-gke.1086000
    * 1.29.15-gke.1170000
    * 1.30.9-gke.1127000
    * 1.30.11-gke.1131000
    * 1.31.7-gke.1013002
    * 1.31.7-gke.1212000
    * 1.32.3-gke.1717000



## April 18, 2025

Change

#### (2025-R15) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.29.15-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.6-gke.1099001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1717000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following node versions are now available: 
    * [1.27.16-gke.2664000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1131000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.6-gke.1099001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.7-gke.1212000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1297002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1717000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following versions are no longer available: 
    * 1.29.13-gke.1109000
    * 1.29.14-gke.1132000
    * 1.29.15-gke.1017000
    * 1.29.15-gke.1058000
    * 1.29.15-gke.1108000
    * 1.29.15-gke.1134000
    * 1.30.9-gke.1046000
    * 1.30.9-gke.1201000
    * 1.30.10-gke.1022000
    * 1.30.10-gke.1145000
    * 1.30.10-gke.1227000
    * 1.30.10-gke.1227001
    * 1.30.11-gke.1008001
    * 1.30.11-gke.1072000
    * 1.30.11-gke.1093000
    * 1.31.5-gke.1169000
    * 1.31.5-gke.1169001
    * 1.31.5-gke.1233000
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
    * 1.32.1-gke.1729000
    * 1.32.2-gke.1182002
    * 1.32.2-gke.1297001
    * 1.32.2-gke.1400003
    * 1.32.2-gke.1652000
    * 1.32.2-gke.1652003
    * 1.32.3-gke.1057001
    * 1.32.3-gke.1170000
    * 1.32.3-gke.1440000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.6-gke.1064001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322) with this release.



## April 08, 2025

Change

#### (2025-R14) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.29.15-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1149000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1440000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following node versions are now available: 
    * [1.27.16-gke.2650000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2097000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.11-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.7-gke.1149000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1182003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1440000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)



## April 02, 2025

Change

#### (2025-R13) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
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
  * The following node versions are now available: 
    * [1.27.16-gke.2633000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
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

  * The following versions are now available: 
    * [1.29.15-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.10-gke.1227001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.30.11-gke.1008001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
    * [1.31.6-gke.1221001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.7-gke.1013001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
    * [1.32.2-gke.1652003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.3-gke.1057001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1323)
  * The following node versions are now available: 
    * [1.27.16-gke.2595000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
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

  * The following versions are now available: 
    * [1.29.15-gke.1017000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1221000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1400003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1652000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following node versions are now available: 
    * [1.27.16-gke.2573000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.2003000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.15-gke.1017000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    * [1.30.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1221000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1400003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1652000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available: 
    * 1.32.2-gke.1182000
    * 1.32.2-gke.1400001



## March 12, 2025

Change

#### (2025-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.29.14-gke.1132000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1140000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1297001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1400001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following node versions are now available: 
    * [1.27.16-gke.2528000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1940000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.14-gke.1132000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1140000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1297001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
    * [1.32.2-gke.1400001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available: 
    * 1.30.9-gke.1009000
    * 1.31.5-gke.1068000
    * 1.32.1-gke.1489001
    * 1.32.2-gke.1297000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316) with this release.



## March 05, 2025

Change

#### (2025-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.29.14-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1102000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1297000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following node versions are now available: 
    * [1.27.16-gke.2489000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1897000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.14-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1102000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1297000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available: 
    * 1.29.13-gke.1006000
    * 1.29.13-gke.1109000
    * 1.29.14-gke.1020000
    * 1.30.8-gke.1261000
    * 1.30.10-gke.1042000
    * 1.31.5-gke.1023000
    * 1.31.6-gke.1027000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.



## February 26, 2025

Change

#### (2025-R08) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.29.14-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.29.14-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.6-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following node versions are now available: 
    * [1.27.16-gke.2477000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1881000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.14-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.29.14-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.10-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.30.10-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.31.6-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.2-gke.1182000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1322)
  * The following versions are no longer available: 
    * 1.29.12-gke.1270000
    * 1.30.8-gke.1162001
    * 1.30.9-gke.1231000
    * 1.31.4-gke.1372000
    * 1.32.1-gke.1200003
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) with this release.



## February 18, 2025

Change

#### (2025-R07) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.9-gke.1231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.1-gke.1729000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following node versions are now available: 
    * [1.27.16-gke.2440000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.2451000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1844000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.14-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12914)
    * [1.30.9-gke.1231000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.30.10-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13010)
    * [1.31.6-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1316)
    * [1.32.1-gke.1729000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available: 
    * 1.29.12-gke.1143001
    * 1.30.8-gke.1128001
    * 1.31.4-gke.1256000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.



## February 11, 2025

Change

#### (2025-R06) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
    * [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
    * [1.32.1-gke.1489001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following node versions are now available: 
    * [1.27.16-gke.2387000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1781000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1233000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
    * [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
    * [1.32.1-gke.1357001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
    * [1.32.1-gke.1489001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321)
  * The following versions are no longer available: 
    * 1.28.15-gke.1480000
    * 1.28.15-gke.1503000
    * 1.28.15-gke.1612000
    * 1.28.15-gke.1641000
    * 1.28.15-gke.1673000
    * 1.28.15-gke.1720000
    * 1.29.12-gke.1120001
    * 1.30.8-gke.1051000
    * 1.30.8-gke.1162000
    * 1.31.4-gke.1183000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.1-gke.1200003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1321) with this release.



## February 06, 2025

Change

#### (2025-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1720000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following node versions are now available: 
    * [1.27.16-gke.2342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1720000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.9-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1169000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available: 
    * 1.28.15-gke.1435000
    * 1.29.12-gke.1055000
    * 1.29.12-gke.1055001
    * 1.29.12-gke.1143000
    * 1.30.5-gke.1713000
    * 1.30.8-gke.1051001
    * 1.30.9-gke.1027000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 29, 2025

Change

#### (2025-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1673000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1120001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1143001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.8-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.9-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following node versions are now available: 
    * [1.27.16-gke.2296000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1673000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1120001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1143001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.13-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.8-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1128001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1162001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.9-gke.1027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.30.9-gke.1046000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available: 
    * 1.28.15-gke.1342000
    * 1.29.10-gke.1280000
    * 1.29.12-gke.1120000
    * 1.30.5-gke.1699000
    * 1.30.8-gke.1128000
    * 1.30.8-gke.1282000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 23, 2025

Change

#### (2025-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.8-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following node versions are now available: 
    * [1.27.16-gke.2270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1641000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12913)
    * [1.30.8-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.9-gke.1009000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1309)
    * [1.31.5-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1315)
  * The following versions are no longer available: 
    * 1.30.6-gke.1596000
    * 1.30.8-gke.1224000
    * 1.31.3-gke.1006000
    * 1.31.3-gke.1162000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314) with this release.



## January 14, 2025

Change

#### (2025-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1224000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following node versions are now available: 
    * [1.27.16-gke.2246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1612000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1270000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1224000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1261000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available: 
    * 1.28.15-gke.1020000
    * 1.28.15-gke.1362000
    * 1.28.15-gke.1488000
    * 1.29.10-gke.1054000
    * 1.29.10-gke.1155000
    * 1.29.12-gke.1126000
    * 1.30.5-gke.1443001
    * 1.30.6-gke.1125000
    * 1.30.7-gke.1084000
    * 1.30.8-gke.1133000
    * 1.31.1-gke.2105000
    * 1.31.4-gke.1249000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.3-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313) with this release.



## January 07, 2025

Change

#### (2025-R01) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.29.12-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.30.8-gke.1133000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1249000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following node versions are now available: 
    * [1.27.16-gke.2142000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1503000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1126000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.29.12-gke.1143000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1133000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.30.8-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1249000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.31.4-gke.1256000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following versions are no longer available: 
    * 1.28.15-gke.1159000
    * 1.28.15-gke.1388000
    * 1.29.10-gke.1227000
    * 1.29.11-gke.1012000
    * 1.29.11-gke.1045000
    * 1.30.7-gke.1136000
    * 1.31.3-gke.1056000
    * 1.31.3-gke.1121001
    * 1.31.4-gke.1072000
    * 1.31.4-gke.1177000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.



## December 26, 2024

Change

**(2024-R50) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following node versions are now available: 
    * [1.27.16-gke.2122000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1480000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1120000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1128000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
    * [1.31.4-gke.1183000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)



## December 18, 2024

Change

**(2024-R49) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)
  * The following node versions are now available: 
    * [1.27.16-gke.2081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1435000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.12-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12912)
    * [1.30.8-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1308)
    * [1.31.4-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1314)



## December 12, 2024

Change

#### (2024-R48) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1388000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.11-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12911)
    * [1.30.7-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.31.3-gke.1121001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
    * [1.31.3-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following node versions are now available: 
    * [1.27.16-gke.2051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1388000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.11-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12911)
    * [1.30.7-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.31.3-gke.1121001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
    * [1.31.3-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following versions are no longer available: 
    * 1.28.14-gke.1340000
    * 1.28.15-gke.1080000
    * 1.28.15-gke.1344000
    * 1.29.9-gke.1496000
    * 1.29.10-gke.1155000
    * 1.30.5-gke.1014003
    * 1.30.5-gke.1713000
    * 1.30.7-gke.1077000
    * 1.31.3-gke.1023000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## December 10, 2024

Change

#### (2024-R47) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1344000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.11-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12911)
    * [1.30.7-gke.1077000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.30.7-gke.1084000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.31.3-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
    * [1.31.3-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following node versions are now available: 
    * [1.27.16-gke.2027000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1344000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1362000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.11-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12911)
    * [1.30.7-gke.1077000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.30.7-gke.1084000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1307)
    * [1.31.3-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
    * [1.31.3-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following versions are no longer available: 
    * 1.28.14-gke.1099000
    * 1.28.14-gke.1217000
    * 1.28.14-gke.1376000
    * 1.28.15-gke.1041000
    * 1.29.9-gke.1177000
    * 1.29.9-gke.1541000
    * 1.29.10-gke.1071000
    * 1.30.5-gke.1014001
    * 1.30.5-gke.1355000
    * 1.30.6-gke.1059000
    * 1.31.1-gke.1846000
    * 1.31.1-gke.2008000
    * 1.31.2-gke.1354000
    * 1.31.2-gke.1384000
    * 1.31.2-gke.1518000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## November 27, 2024

Change

#### (2024-R46) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.3-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)
  * The following node versions are now available: 
    * [1.27.16-gke.2019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1280000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.3-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1313)



## November 19, 2024

Change

#### (2024-R45) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.2-gke.1518000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
  * The following node versions are now available: 
    * [1.27.16-gke.1836000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1159000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1227000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.2-gke.1518000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)



## November 13, 2024

Change

#### (2024-R44) Version updates

GKE cluster versions have been updated.

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.28.15-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.1-gke.2008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.2-gke.1354000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
    * [1.31.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
  * The following node versions are now available: 
    * [1.27.16-gke.1784000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.6-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1306)
    * [1.31.2-gke.1354000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
    * [1.31.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
  * The following versions are no longer available: 
    * 1.30.5-gke.1628000
    * 1.31.1-gke.1678000
    * 1.31.2-gke.1115000



## November 06, 2024

Change

#### (2024-R43) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1071000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.2-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
  * The following node versions are now available: 
    * [1.28.15-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1071000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.2-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1312)
  * The following versions are no longer available: 
    * 1.28.14-gke.1217000
    * 1.28.15-gke.1015000
    * 1.29.9-gke.1341000
    * 1.29.10-gke.1043000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## October 30, 2024

Change

#### (2024-R42) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.15-gke.1015000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following node versions are now available: 
    * [1.27.16-gke.1742000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.15-gke.1015000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.28.15-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    * [1.29.10-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.29.10-gke.1054000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12910)
    * [1.30.5-gke.1699000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.2105000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available: 
    * 1.28.14-gke.1004000
    * 1.29.8-gke.1278000
    * 1.30.4-gke.1348000
    * 1.30.4-gke.1348001
    * 1.31.1-gke.1146000
    * 1.31.1-gke.2008000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.



## October 25, 2024

Change

#### (2024-R41) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.28.14-gke.1376000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.30.5-gke.1628000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1146000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.2008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following node versions are now available: 
    * [1.27.16-gke.1712000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1376000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1541000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1014003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.30.5-gke.1628000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
    * [1.31.1-gke.1146000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.1846000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
    * [1.31.1-gke.2008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311)
  * The following versions are no longer available: 
    * 1.28.13-gke.1119000
    * 1.29.8-gke.1211000
    * 1.30.3-gke.1969002
    * 1.30.5-gke.1145000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.1-gke.1678000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1311) with this release.



## October 17, 2024

Change

#### (2024-R40) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following node versions are now available: 
    * [1.27.16-gke.1681000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1496000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1443001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available: 
    * 1.28.13-gke.1049000
    * 1.28.14-gke.1175000
    * 1.29.8-gke.1096000
    * 1.30.3-gke.1969001
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) with this release.



## October 11, 2024

Change

#### (2024-R39) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.28.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following node versions are now available: 
    * [1.27.16-gke.1576000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.28.14-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1341000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1355000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available: 
    * 1.27.16-gke.1148001
    * 1.27.16-gke.1258000
    * 1.27.16-gke.1287000
    * 1.27.16-gke.1342000
    * 1.27.16-gke.1373000
    * 1.27.16-gke.1478000
    * 1.28.13-gke.1024000
    * 1.29.8-gke.1057000
    * 1.30.2-gke.1587003
    * 1.30.5-gke.1014000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## October 03, 2024

Change

#### (2024-R38) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
    * [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following node versions are now available: 
    * [1.30.3-gke.1969002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
    * [1.30.4-gke.1348001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.5-gke.1014001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available: 
    * 1.28.13-gke.1006000
    * 1.29.8-gke.1031000
    * 1.30.3-gke.1639000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.



## September 26, 2024

Change

#### (2024-R37) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.27.16-gke.1478000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following node versions are now available: 
    * [1.27.16-gke.1478000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1099000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.9-gke.1177000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1299)
    * [1.30.5-gke.1145000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available: 
    * 1.27.16-gke.1051001
    * 1.28.12-gke.1052000
    * 1.28.12-gke.1179000
    * 1.29.7-gke.1104000
    * 1.29.7-gke.1274000
    * 1.30.3-gke.1969000
    * 1.30.4-gke.1476000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298) with this release.



## September 19, 2024

Change

#### (2024-R36) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.27.16-gke.1373000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1476000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.5-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following node versions are now available: 
    * [1.27.16-gke.1373000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.14-gke.1004000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12814)
    * [1.29.8-gke.1278000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1476000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.5-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1305)
  * The following versions are no longer available: 
    * 1.27.16-gke.1296000
    * 1.28.13-gke.1078000
    * 1.29.8-gke.1157000
    * 1.30.4-gke.1129000
    * 1.30.4-gke.1213000
    * 1.30.4-gke.1282000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.0-gke.1506000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1310) with this release.



## September 11, 2024

Change

#### (2024-R35) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following control plane and node versions are now available: 
    * [1.27.16-gke.1296000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1342000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1078000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.28.13-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.29.8-gke.1211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
    * [1.30.4-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
    * [1.30.4-gke.1348000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
  * The following versions are no longer available: 
    * 1.27.16-gke.1008000
    * 1.27.16-gke.1148000
    * 1.27.16-gke.1234000
    * 1.27.16-gke.1234001
    * 1.28.13-gke.1042000
    * 1.29.6-gke.1326000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813) with this release.



## September 06, 2024

Change

#### (2024-R34) Version updates

There are no updates for clusters not enrolled in a release channel.

Change

#### (2024-R33) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) is now the default version for cluster creation.
  * The following versions are now available: 
    * [1.27.16-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1234001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1213000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
  * The following node versions are now available: 
    * [1.27.16-gke.1051001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1234001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.28.13-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1213000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
  * The following versions are no longer available: 
    * 1.27.15-gke.1252000
    * 1.27.16-gke.1051000
    * 1.27.16-gke.1082000
    * 1.28.11-gke.1260000
    * 1.29.6-gke.1254000
    * 1.29.7-gke.1008000
    * 1.30.3-gke.1225000
  * Auto-upgrade targets are now available for the following minor versions: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
  * The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades: 
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## August 28, 2024

Change

#### (2024-R32) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.27.16-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1129000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
  * The following node versions are now available: 
    * [1.27.16-gke.1258000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1057000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.4-gke.1129000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1304)
  * The following versions are no longer available: 
    * 1.28.12-gke.1090000
    * 1.29.7-gke.1174000



## August 20, 2024

Change

#### (2024-R31) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) is now the default version.
  * The following versions are now available: 
    * [1.27.16-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following node versions are now available: 
    * [1.27.16-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.13-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12813)
    * [1.29.8-gke.1031000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1298)
    * [1.30.3-gke.1969000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available: 
    * 1.27.15-gke.1154000
    * 1.27.16-gke.1008000
    * 1.28.11-gke.1172000
    * 1.28.11-gke.1315000
    * 1.29.6-gke.1038001
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303) with this release.



## August 14, 2024

Change

#### (2024-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297) is now the default version.
  * The following versions are now available: 
    * [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following node versions are now available: 
    * [1.27.16-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1179000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available: 
    * 1.27.14-gke.1059002
    * 1.28.11-gke.1019001
    * 1.29.5-gke.1091002
    * 1.30.1-gke.1329003
    * 1.30.3-gke.1451000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## August 12, 2024

Change

### (2024-R29) Version updates

There are no updates for clusters not enrolled in a release channel.

## August 07, 2024

Change

### (2024-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version.
  * The following versions are now available: 
    * [1.27.16-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1451000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following node versions are now available: 
    * [1.27.16-gke.1082000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1174000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.3-gke.1451000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## July 31, 2024

Change

### (2024-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version.
  * The following versions are now available: 
    * [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.1-gke.1329003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
    * [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
    * [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following node versions are now available: 
    * [1.27.16-gke.1051000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.12-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12812)
    * [1.29.7-gke.1104000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
    * [1.30.1-gke.1329003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1301)
    * [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302)
    * [1.30.3-gke.1225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1303)
  * The following versions are no longer available: 
    * 1.27.14-gke.1042001
    * 1.27.15-gke.1125000
    * 1.28.9-gke.1289002
    * 1.28.10-gke.1075001
    * 1.28.11-gke.1289000
    * 1.29.6-gke.1137000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.2-gke.1587003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v1302) with this release.



## July 23, 2024

Change

### (2024-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.11-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
  * The following node versions are now available: 
    * [1.27.16-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
    * [1.28.11-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.28.11-gke.1315000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.7-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1297)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.



## July 17, 2024

Change

### (2024-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) is now the default version.
  * The following versions are now available: 
    * [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * The following node versions are now available: 
    * [1.27.15-gke.1252000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1260000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1326000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * The following versions are no longer available: 
    * 1.27.13-gke.1070002
    * 1.27.13-gke.1201002
    * 1.27.14-gke.1059001
    * 1.27.15-gke.1154000
    * 1.28.10-gke.1058001
    * 1.28.11-gke.1170000
    * 1.29.4-gke.1043004
    * 1.29.5-gke.1091001
    * 1.29.6-gke.1254000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296) with this release.



## July 10, 2024

Change

### (2024-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) is now the default version.
  * The following versions are now available: 
    * [1.27.14-gke.1059001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.15-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.5-gke.1091001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.29.6-gke.1137000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * The following node versions are now available: 
    * [1.27.14-gke.1059001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.15-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.27.15-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.11-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.28.11-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.5-gke.1091001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.29.6-gke.1137000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
    * [1.29.6-gke.1254000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * The following versions are no longer available: 
    * 1.26.15-gke.1090000
    * 1.26.15-gke.1090004
    * 1.26.15-gke.1191000
    * 1.26.15-gke.1191001
    * 1.26.15-gke.1300000
    * 1.26.15-gke.1300001
    * 1.26.15-gke.1320000
    * 1.26.15-gke.1320002
    * 1.26.15-gke.1381000
    * 1.26.15-gke.1381001
    * 1.26.15-gke.1390000
    * 1.26.15-gke.1390001
    * 1.26.15-gke.1404000
    * 1.26.15-gke.1404002
    * 1.26.15-gke.1469000
    * 1.26.15-gke.1469001
    * 1.27.11-gke.1062004
    * 1.27.13-gke.1070000
    * 1.27.13-gke.1166000
    * 1.27.13-gke.1166001
    * 1.27.13-gke.1201000
    * 1.27.14-gke.1022000
    * 1.27.14-gke.1022001
    * 1.27.14-gke.1042000
    * 1.27.14-gke.1059000
    * 1.27.14-gke.1100000
    * 1.27.14-gke.1100002
    * 1.27.15-gke.1012000
    * 1.27.15-gke.1012003
    * 1.28.9-gke.1000000
    * 1.28.9-gke.1069000
    * 1.28.9-gke.1069002
    * 1.28.9-gke.1209000
    * 1.28.9-gke.1209001
    * 1.28.9-gke.1289000
    * 1.28.10-gke.1058000
    * 1.28.10-gke.1075000
    * 1.28.10-gke.1089000
    * 1.28.10-gke.1089002
    * 1.28.10-gke.1148000
    * 1.28.10-gke.1148001
    * 1.28.11-gke.1019000
    * 1.29.4-gke.1043002
    * 1.29.5-gke.1060000
    * 1.29.5-gke.1060001
    * 1.29.5-gke.1091000
    * 1.29.6-gke.1038000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295) with this release.



## July 08, 2024

Change

### (2024-R23) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) is now the default version.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.26.15-gke.1320002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.15-gke.1320002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.13-gke.1070002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.13-gke.1070002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## July 03, 2024

Change

### (2024-R22) Version updates

  * The following cluster and node versions are now available: 
    * [1.26.15-gke.1090004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1191001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1300001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1320002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1381001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1390001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1404002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1469001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1070002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.27.13-gke.1166001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.27.13-gke.1201002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.27.14-gke.1022001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.14-gke.1042001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.14-gke.1059002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.14-gke.1100002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.15-gke.1012003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.9-gke.1069002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1209001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1289002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.10-gke.1058001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.10-gke.1075001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.10-gke.1089002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.10-gke.1148001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.11-gke.1019001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.4-gke.1043004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.5-gke.1060001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.29.5-gke.1091002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
    * [1.29.6-gke.1038001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)



## June 26, 2024

Change

#### (2024-R21) Version updates

  * The following versions are now available: 
    * [1.26.15-gke.1469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.15-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.10-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.11-gke.1019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * The following node versions are now available: 
    * [1.26.15-gke.1469000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.27.15-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12715)
    * [1.28.10-gke.1148000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.28.11-gke.1019000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12811)
    * [1.29.6-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1296)
  * The following versions are no longer available: 
    * 1.26.15-gke.1436000
    * 1.27.11-gke.1062003
    * 1.27.14-gke.1093000
    * 1.28.10-gke.1141000
    * 1.29.5-gke.1121000
    * 1.29.5-gke.1192000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713) with this release.



## June 18, 2024

Change

#### (2024-R20) Version updates

  * The following versions are now available: 
    * [1.26.15-gke.1191000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1300000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1436000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1141000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following node versions are now available: 
    * [1.26.15-gke.1436000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1141000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following versions are no longer available: 
    * 1.28.7-gke.1026001
    * 1.28.8-gke.1095000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## June 12, 2024

Change

#### (2024-R19) Version updates

  * The following versions are now available: 
    * [1.26.15-gke.1404000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
    * [1.28.9-gke.1069000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.10-gke.1089000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following node versions are now available: 
    * [1.26.15-gke.1404000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1089000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following versions are no longer available: 
    * 1.27.13-gke.1000000
    * 1.29.3-gke.1282001
    * 1.29.4-gke.1670000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## June 06, 2024

Change

#### (2024-R18) Version updates

  * Version [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) is now the default version.
  * The following versions are now available: 
    * [1.26.15-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1091000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following node versions are now available: 
    * [1.26.15-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1042000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1075000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.5-gke.1091000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following versions are no longer available: 
    * 1.26.15-gke.1300000
    * 1.26.15-gke.1372001
    * 1.27.11-gke.1062001
    * 1.27.12-gke.1115000
    * 1.28.8-gke.1095000
    * 1.29.1-gke.1589020
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294) with this release.



## May 28, 2024

Change

#### (2024-R17) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.26.15-gke.1372001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.14-gke.1022000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1058000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.4-gke.1043002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.5-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following versions are no longer available: 
    * 1.26.14-gke.1044001
    * 1.26.15-gke.1243000
    * 1.26.15-gke.1360000
    * 1.27.14-gke.1011000
    * 1.28.7-gke.1026000
    * 1.28.9-gke.1069000
    * 1.28.10-gke.1012000
    * 1.29.4-gke.1043001
    * 1.29.4-gke.1165000
    * 1.29.5-gke.1010000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289) with this release.



## May 21, 2024

Change

#### (2024-R16) Version updates

  * The following versions are now available: 
    * [1.26.15-gke.1243000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.26.15-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.27.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.4-gke.1043001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1670000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.5-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following node versions are now available: 
    * [1.26.15-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.11-gke.1062004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.27.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12714)
    * [1.28.10-gke.1012000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12810)
    * [1.29.4-gke.1043001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.5-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1295)
  * The following versions are no longer available: 
    * 1.26.15-gke.1191000
    * 1.27.11-gke.1062000
    * 1.28.9-gke.1250000
    * 1.29.1-gke.1589018
    * 1.29.3-gke.1282005
    * 1.29.4-gke.1043000
    * 1.29.4-gke.1447000
    * 1.29.4-gke.1447001
    * 1.29.4-gke.1542000



## May 17, 2024

Change

#### (2024-R14) Version updates

There are no version updates for 2024-R14.

#### (2024-R15) Version updates

  * Version [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288) is now the default version.
  * The following versions are now available: 
    * [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.27.13-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1069000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.3-gke.1282005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.4-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1447001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1542000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following node versions are now available: 
    * [1.26.15-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.28.9-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.3-gke.1282005](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.4-gke.1447001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1542000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
    * [1.29.4-gke.1670000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following versions are no longer available: 
    * 1.26.8-gke.200
    * 1.26.14-gke.1044000
    * 1.27.8-gke.1067004
    * 1.29.3-gke.1282000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.1-gke.1589020](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## May 08, 2024

Change

#### (2024-R13) Version updates

  * The following control plane and node versions are now available: 
    * [1.26.14-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.26.15-gke.1300000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.11-gke.1062003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.27.13-gke.1166000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.7-gke.1026001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.28.9-gke.1209000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.1-gke.1589020](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
    * [1.29.3-gke.1282001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.4-gke.1447000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following versions are no longer available: 
    * 1.26.13-gke.1144000
    * 1.26.15-gke.1158000
    * 1.26.15-gke.1243000
    * 1.27.12-gke.1190000
    * 1.27.13-gke.1070000
    * 1.28.3-gke.1118000
    * 1.28.3-gke.1286000
    * 1.28.8-gke.1175000
    * 1.28.9-gke.1069000
    * 1.29.1-gke.1589017
    * 1.29.3-gke.1093000
    * 1.29.3-gke.1093006
    * 1.29.4-gke.1165000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.1-gke.1589018](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## May 01, 2024

Change

#### (2024-R12) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following control plane and node versions are now available: 
    * [1.26.15-gke.1243000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.13-gke.1070000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1069000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.4-gke.1165000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.



## April 30, 2024

Change

#### (2024-R11) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following control plane and node versions are now available: 
    * [1.26.15-gke.1191000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.11-gke.1062001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.27.13-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12713)
    * [1.28.9-gke.1000000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1289)
    * [1.29.3-gke.1093006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
    * [1.29.4-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1294)
  * The following versions are no longer available: 
    * 1.25.16-gke.1460000
    * 1.25.16-gke.1537000
    * 1.25.16-gke.1570000
    * 1.25.16-gke.1711000
    * 1.25.16-gke.1759000
    * 1.26.14-gke.1006000
    * 1.27.7-gke.1121002
    * 1.27.10-gke.1055000
    * 1.28.5-gke.1217000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712) with this release.



## April 18, 2024

Change

#### (2024-R10) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) is now the default version.
  * The following control plane versions are now available: 
    * [1.25.16-gke.1570000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.25.16-gke.1759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.15-gke.1158000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.12-gke.1190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712)
    * [1.28.8-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
    * [1.29.3-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
  * The following node versions are now available: 
    * [1.25.16-gke.1759000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.15-gke.1158000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.12-gke.1190000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712)
    * [1.28.8-gke.1175000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
    * [1.29.3-gke.1282000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)
  * The following versions are no longer available: 
    * 1.25.15-gke.1115000
    * 1.25.16-gke.1041000
    * 1.25.16-gke.1596000
    * 1.25.16-gke.1648000
    * 1.26.11-gke.1055000
    * 1.26.14-gke.1076000
    * 1.26.14-gke.1133000
    * 1.27.3-gke.100
    * 1.27.11-gke.1118000
    * 1.27.11-gke.1202000
    * 1.28.3-gke.1203001
    * 1.28.7-gke.1226000
    * 1.29.0-gke.1381000
    * 1.29.2-gke.1521000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287) with this release.



## April 08, 2024

Change

#### (2024-R09) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following cluster and node versions are now available: 
    * [1.25.16-gke.1711000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.15-gke.1090000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12615)
    * [1.27.12-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12712)
    * [1.28.8-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1288)
    * [1.29.3-gke.1093000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1293)



## March 20, 2024

Change

**(2024-R08) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following cluster and node versions are now available: 
    * [1.25.16-gke.1648000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1133000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1202000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1226000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.1-gke.1589018](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
    * [1.29.2-gke.1521000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1292)
  * The following versions are no longer available: 
    * 1.25.16-gke.1570000
    * 1.26.10-gke.1101000
    * 1.27.9-gke.1092000
    * 1.28.7-gke.1100000
    * 1.29.2-gke.1217000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.27.10-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.10-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.5-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1285) with this release.



## March 07, 2024

Change

**(2024-R07) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following cluster and node versions are now available: 
    * [1.25.16-gke.1596000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1076000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1100000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.1-gke.1589017](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
    * [1.29.2-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1292)
  * The following versions are no longer available: 
    * 1.25.16-gke.1360000
    * 1.26.13-gke.1052000
    * 1.27.11-gke.1018000
    * 1.28.6-gke.1456000
    * 1.29.1-gke.1589000
    * 1.29.2-gke.1060000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.29.1-gke.1589017](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291) with this release.



## March 04, 2024

Change

**(2024-R06) Version updates**

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following control plane and node versions are now available: 
    * [1.25.16-gke.1570000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1062000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.7-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1287)
    * [1.29.2-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1292)
  * The following versions are no longer available: 
    * 1.27.10-gke.1207000
    * 1.28.6-gke.1369000
    * 1.29.1-gke.1575000



## February 23, 2024

Change

#### (2024-R05) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following versions are now available: 
    * [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.6-gke.1456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1589000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following node versions are now available: 
    * [1.25.16-gke.1537000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.14-gke.1006000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12614)
    * [1.27.11-gke.1018000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12711)
    * [1.28.6-gke.1456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1589000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available: 
    * 1.25.16-gke.1268000
    * 1.25.16-gke.1497000
    * 1.26.12-gke.1111000
    * 1.26.13-gke.1189000
    * 1.27.10-gke.1152000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.16-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.16-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.



## February 13, 2024

Change

#### (2024-R04) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following control plane and node versions are now available: 
    * [1.25.16-gke.1497000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1189000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.10-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
    * [1.28.6-gke.1369000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available: 
    * 1.28.6-gke.1095000
    * 1.28.6-gke.1289000
    * 1.29.1-gke.1016000
    * 1.29.1-gke.1425000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1279) with this release.



## February 08, 2024

Change

#### (2024-R03) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * Version [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278) is now the default version.
  * The following versions are now available: 
    * [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.10-gke.1152000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
    * [1.28.6-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1425000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following node versions are now available: 
    * [1.25.16-gke.1460000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1144000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.10-gke.1152000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
    * [1.28.6-gke.1289000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.1-gke.1425000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available: 
    * 1.26.5-gke.2100
    * 1.26.6-gke.1700
    * 1.27.2-gke.1200



## January 26, 2024

Change

#### (2024-R02) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

  * The following control plane and node versions are now available: 
    * [1.25.16-gke.1360000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.13-gke.1052000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12613)
    * [1.27.7-gke.1121002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278)
    * [1.27.10-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12710)
    * [1.28.6-gke.1095000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1286)
    * [1.29.0-gke.1381000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1290)
    * [1.29.1-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v1291)
  * The following versions are no longer available: 
    * 1.24.17-gke.200
    * 1.24.17-gke.2266000
    * 1.24.17-gke.2364000
    * 1.24.17-gke.2472000
    * 1.25.10-gke.2700
    * 1.25.13-gke.200
    * 1.27.4-gke.900
    * 1.27.5-gke.200
    * 1.27.7-gke.1121000
    * 1.27.8-gke.1067000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.8-gke.1067004](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## January 11, 2024

Change

#### (2024-R01) Version updates

  * The following control plane versions are now available: 
    * [1.24.17-gke.2472000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.12-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12612)
    * [1.27.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1279)
    * [1.28.5-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1285)
  * The following node versions are now available: 
    * [1.24.17-gke.2472000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1268000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.12-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12612)
    * [1.27.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1279)
    * [1.28.5-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1285)
  * The following control plane versions are no longer available: 
    * 1.24.16-gke.500
    * 1.24.17-gke.2230000
    * 1.24.17-gke.2347000
    * 1.25.12-gke.500
    * 1.25.16-gke.1020000
    * 1.26.7-gke.500
    * 1.26.10-gke.1073000
    * 1.26.10-gke.1235000
    * 1.27.7-gke.1056000
    * 1.27.7-gke.1293000
    * 1.28.4-gke.1083000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.7-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277) with this release.



## December 12, 2023

Change

#### (2023-R26) Version updates

  * The following control plane versions are now available: 
    * [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.24.17-gke.2364000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.10-gke.1073000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611)
    * [1.27.7-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.27.8-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278)
    * [1.28.3-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
    * [1.28.4-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1284)
  * The following node versions are now available: 
    * [1.24.17-gke.2364000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1041000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.11-gke.1055000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12611)
    * [1.27.8-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1278)
    * [1.28.3-gke.1118000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
    * [1.28.4-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1284)
  * The following control plane versions are no longer available: 
    * 1.27.3-gke.1700
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.10-gke.1073000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.7-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277) with this release.



## December 04, 2023

Change

#### (2023-R25) Version updates

  * The following control plane and node versions are now available: 
    * [1.24.17-gke.2347000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.16-gke.1020000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12516)
    * [1.26.10-gke.1235000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
    * [1.28.3-gke.1286000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283)
  * The following control plane versions are no longer available: 
    * 1.24.15-gke.1700
    * 1.24.17-gke.2113000
    * 1.24.17-gke.2155000
    * 1.24.17-gke.2230000
    * 1.25.11-gke.1700
    * 1.25.14-gke.1421000
    * 1.25.14-gke.1474000
    * 1.25.15-gke.1083000
    * 1.26.5-gke.2700
    * 1.26.9-gke.1437000
    * 1.26.9-gke.1507000
    * 1.26.10-gke.1073000
    * 1.27.2-gke.2100
    * 1.27.6-gke.1248000
    * 1.27.6-gke.1445000
    * 1.27.7-gke.1088000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.7-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1267) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.28 to version [1.28.3-gke.1203001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v1283) with this release.



## November 17, 2023

Change

#### (2023-R24) Version updates

  * The following control plane and node versions are now available: 
    * [1.24.17-gke.2230000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.24.17-gke.2266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.15-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.25.15-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.26.10-gke.1073000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.26.10-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1088000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.27.7-gke.1121000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
  * The following control plane versions are no longer available: 
    * 1.24.17-gke.2198000
    * 1.24.17-gke.2211000
    * 1.25.15-gke.1033000
    * 1.25.15-gke.1049000
    * 1.26.10-gke.1024000
    * 1.26.10-gke.1038000
    * 1.27.7-gke.1038000
    * 1.27.7-gke.1056000



## November 09, 2023

Change

#### (2023-R23) Version updates

  * The following control plane and node versions are now available: 
    * [1.24.17-gke.2198000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.24.17-gke.2211000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.15-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.25.15-gke.1049000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12515)
    * [1.26.10-gke.1024000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.26.10-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v12610)
    * [1.27.7-gke.1038000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
    * [1.27.7-gke.1056000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1277)
  * The following control plane versions are no longer available: 
    * 1.24.14-gke.2700
    * 1.27.6-gke.1506000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1266) with this release.



## October 19, 2023

Change

#### (2023-R22) Version updates

There are no version updates for 2023-R21.

  * The following control plane and node versions are now available: 
    * [1.24.17-gke.2155000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.14-gke.1474000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12514)
    * [1.26.9-gke.1507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1269)
    * [1.27.6-gke.1506000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1276)



## October 13, 2023

Change

#### (2023-R20) Version updates

  * The following control plane and node versions are now available: 
    * [1.24.17-gke.2113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.14-gke.1421000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12514)
    * [1.26.9-gke.1437000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1269)
    * [1.27.6-gke.1445000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1276)
  * The following control plane versions are no longer available: 1.24.17-gke.1963000, 1.25.14-gke.1256000, 1.26.9-gke.1256000



## October 05, 2023

Change

#### (2023-R19) Version updates

  * The following control plane and node versions are now available: 
    * [1.27.6-gke.1248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1276)
    * [1.27.6-gke.1248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1276)



## September 05, 2023

Change

#### (2023-R18) Version updates

  * The following control plane and node versions are now available: 
    * [1.24.17-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12417)
    * [1.25.13-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12513)
    * [1.26.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1268)
    * [1.27.5-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1275)
  * The following control plane versions are no longer available: 1.23.17-gke.8400, 1.23.17-gke.10000, 1.23.17-gke.10700, 1.24.14-gke.1400, 1.24.14-gke.2100, 1.25.10-gke.2100, 1.26.5-gke.1400

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.




## August 08, 2023

Change

#### (2023-R17) Version updates

  * Version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.23.17-gke.10700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12416)
    * [1.25.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12512)
    * [1.26.7-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1267)
    * [1.27.4-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1274)
  * The following control plane versions are no longer available: 
    * 1.22.17-gke.12700
    * 1.22.17-gke.14100
    * 1.23.17-gke.7700
    * 1.24.14-gke.1200
    * 1.25.10-gke.1200
    * 1.25.10-gke.1400
    * 1.26.5-gke.1200
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.5-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273) with this release.



## July 26, 2023

Change

#### (2023-R16) Version updates

  * Version [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.23.17-gke.10000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.15-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12415)
    * [1.25.11-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12511)
    * [1.26.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1266)
    * [1.27.3-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.18800
    * 1.23.17-gke.6800
    * 1.23.17-gke.7000
    * 1.24.13-gke.2500
    * 1.25.8-gke.1000
    * 1.25.9-gke.2300
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.23.17-gke.7700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.



## July 07, 2023

Change

#### (2023-R15) Version updates

  * The following control plane and node versions are now available: 

    * [1.22.17-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.8400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.3-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1273)
  * The following control plane versions are no longer available: 

    * 1.22.17-gke.8000
    * 1.22.17-gke.11400
    * 1.23.17-gke.5600
    * 1.24.12-gke.500
    * 1.24.12-gke.1000
    * 1.24.13-gke.500
    * 1.26.3-gke.1000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) with this release.




## June 27, 2023

Change

#### (2023-R14) Version updates

  * Version [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.23.17-gke.7700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.2-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272)
  * The following node versions are now available: 
    * [1.22.17-gke.13400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
  * The following control plane versions are no longer available: 
    * 1.23.17-gke.2000
    * 1.23.17-gke.3600
    * 1.25.8-gke.500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.



## June 15, 2023

Change

#### (2023-R13) Version updates

  * Version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.22.17-gke.12700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.7000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
    * [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272)
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.18100
    * 1.24.11-gke.1000
    * 1.26.4-gke.500
    * 1.26.4-gke.1400
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.27 to version [1.27.2-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v1272) with this release.



## June 07, 2023

Change

#### (2023-R12) Version updates

  * The following control plane versions are now available: 
    * [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
  * The following node versions are now available: 
    * [1.23.17-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12414)
    * [1.25.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v12510)
    * [1.26.5-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1265)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.



## June 05, 2023

Change

#### (2023-R11) Version updates

  * The following control plane and node versions are now available: 
    * [1.22.17-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.5600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.13-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413)
    * [1.25.9-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259)
    * [1.26.4-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1264)
  * The following control plane versions are no longer available: 
    * 1.22.17-gke.7500
    * 1.22.17-gke.9400
    * 1.23.17-gke.1700
    * 1.24.10-gke.2300
    * 1.25.7-gke.1000
    * 1.25.9-gke.400
    * 1.26.2-gke.1000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.3-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263) with this release.



## May 09, 2023

Change

#### (2023-R10) Version updates

  * Version [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258) is now the default version.
  * The following control plane versions are now available: 
    * [1.22.17-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.13-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12413)
    * [1.25.9-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1259)
    * [1.26.4-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1264)
  * The following versions are no longer available: 
    * 1.21.14-gke.8500
    * 1.21.14-gke.15800
    * 1.22.17-gke.5400
    * 1.22.17-gke.6100
    * 1.23.16-gke.1400
    * 1.23.16-gke.2500
    * 1.23.17-gke.300
    * 1.24.9-gke.3200
    * 1.24.10-gke.1200
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411) with this release.



## April 19, 2023

Change

#### (2023-R09) Version updates

  * Version [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.22.17-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
    * [1.26.2-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1262)
    * [1.26.3-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.26 to version [1.26.2-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1262) with this release.



## March 31, 2023

Change

#### (2023-R08) Version updates

  * The following control plane versions are now available: 
    * [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
  * The following node versions are now available: 
    * [1.22.17-gke.7500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12412)
    * [1.25.8-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1258)
    * [1.26.1-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1261)
    * [1.26.3-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#v1263)
  * Version [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) is now the default version.
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.14600
    * 1.22.17-gke.4000
    * 1.22.17-gke.4300
    * 1.23.14-gke.1800
    * 1.23.15-gke.1400
    * 1.23.15-gke.1900
    * 1.23.16-gke.200
    * 1.23.16-gke.1100
    * 1.24.9-gke.2000
    * 1.25.6-gke.1000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257) with this release.



## March 22, 2023

Change

#### (2023-R07) Version updates

  * The following control plane and node versions are now available: 
    * [1.21.14-gke.18800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.17-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12317)
    * [1.24.11-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12411)
    * [1.25.7-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1257)
  * The following control plane versions are no longer available:

    * 1.21.14-gke.14100
    * 1.22.17-gke.3100
    * 1.25.6-gke.200
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.




## March 03, 2023

Change

#### (2023-R06) Version updates

  * The following control plane and node versions are now available: 

    * [1.21.14-gke.18100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.10-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410)
  * The following control plane versions are no longer available: 

    * 1.23.13-gke.900
    * 1.23.14-gke.401
    * 1.24.8-gke.2000
    * 1.24.9-gke.1500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) with this release.




## February 22, 2023

Change

#### (2023-R05) Version updates

  * Version [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.22.17-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.10-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v12410)
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.7100
    * 1.22.15-gke.1000
    * 1.22.15-gke.2500
    * 1.22.16-gke.1300
    * 1.22.16-gke.2000
    * 1.25.5-gke.2000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.6-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256) with this release.



## February 10, 2023

Change

#### (2023-R04) Version updates

  * Version [1.24.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.22.17-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.25.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256)
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.5300
    * 1.22.17-gke.1400
    * 1.22.17-gke.1900
    * 1.24.7-gke.900
    * 1.24.8-gke.401
    * 1.25.5-gke.1500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.5-gke.2000](https://githb.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255) with this release.



## February 02, 2023

Change

#### (2023-R02) Version updates

  * The following control plane and node versions are now available: 
    * [1.21.14-gke.15800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.3100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.16-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12316)
    * [1.24.9-gke.3200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.6-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1256)
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.4300
    * 1.25.4-gke.2100
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.5-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255) with this release.



## January 13, 2023

Change

#### (2023-R02) Version updates

  * Version [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.21.14-gke.14600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.15-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12315)
    * [1.24.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.5-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255)
  * The following control plane versions are no longer available: 
    * 1.23.11-gke.300
    * 1.23.12-gke.100
    * 1.23.12-gke.1600
    * 1.24.5-gke.600
    * 1.24.6-gke.1500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247) with this release.



## January 05, 2023

Change

#### (2023-R01) Version updates

  * The following control plane and node versions are now available: 
    * [1.21.14-gke.14100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.17-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12217)
    * [1.23.15-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12315)
    * [1.24.9-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1249)
    * [1.25.5-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1255)
  * The following control plane versions are no longer available: 
    * 1.22.15-gke.100
    * 1.25.3-gke.800
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.22.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.4-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254) with this release.



## December 14, 2022

Change

#### (2022-R28) Version updates

  * Version [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247) is now the default version
  * The following control plane and node versions are now available: 
    * [1.22.16-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216)
    * [1.23.14-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314)
    * [1.24.8-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248)
    * [1.25.3-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1253)
    * [1.25.4-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1254)
  * The following control plane versions are no longer available: 
    * 1.22.13-gke.1000
    * 1.22.14-gke.300
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313) with this release.
    * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.25 to version [1.25.3-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md#v1253) with this release.



## December 05, 2022

Change

#### (2022-R27) Version updates

  * Version [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.22.16-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12216)
    * [1.23.14-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12314)
    * [1.24.8-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1248)
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.3000
    * 1.21.14-gke.9500
    * 1.22.12-gke.2300
    * 1.23.8-gke.1900
    * 1.23.9-gke.900
    * 1.23.9-gke.2100
    * 1.23.10-gke.1000
    * 1.24.4-gke.800
  * The following node version is no longer available: 1.21.14-gke.9500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.23.11-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12311) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245) with this release.



## November 04, 2022

Change

#### (2022-R26) Version updates

  * Version [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.21.14-gke.9500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12313)
    * [1.24.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1247)
  * The following control plane versions are no longer available: 
    * 1.22.12-gke.500
    * 1.22.12-gke.1200
    * 1.24.3-gke.2100
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to [1.24.4-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1244) with this release.



## October 19, 2022

Change

#### (2022-R25) Version updates

  * Version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.21.14-gke.8500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.12-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312)
    * [1.24.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1246)
  * The following control plane versions are no longer available: 
    * 1.21.14-gke.2700
    * 1.22.12-gke.300
    * 1.24.2-gke.1900
    * 1.24.3-gke.200
    * 1.24.3-gke.900
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.21.14-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to [1.24.3-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243) with this release.



## October 05, 2022

Change

#### (2022-R24) Version updates

  * The following control plane and node versions are now available: 

    * [1.21.14-gke.7100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.15-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12215)
    * [1.23.12-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12312)
    * [1.24.5-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1245)



## September 23, 2022

Change

#### (2022-R23) Version updates

  * Version [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) is now the default version.
  * The following control plane and node versions are now available: 

    * [1.22.14-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12214)
    * [1.23.11-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12311)
  * The following control plane versions are no longer available: 

    * 1.21.14-gke.700
    * 1.21.14-gke.2100
    * 1.22.11-gke.400
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.




## September 13, 2022

Change

#### (2022-R22) Version updates

  * Version [1.22.12-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.21.14-gke.5300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.13-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12213)
    * [1.23.10-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v12310)
    * [1.24.4-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1244)
  * The following control plane versions are no longer available: 

    * 1.20.15-gke.11400
    * 1.20.15-gke.12800
    * 1.20.15-gke.13400
    * 1.20.15-gke.13700
    * 1.21.13-gke.900
    * 1.22.10-gke.600
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212) with this release.




## September 02, 2022

Change

#### (2022-R21) Version updates

  * The following control plane and node versions are now available:

    * [1.21.14-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.23.9-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1239)
    * [1.24.3-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243)
  * The following control plane versions are no longer available: 

    * 1.21.12-gke.2200
    * 1.23.7-gke.1400
    * 1.23.8-gke.400
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.14-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.23.8-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1238) with this release.




## August 18, 2022

Change

#### (2022-R20) Version updates

  * Version [1.22.11-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12211) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.20.15-gke.13700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.14-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.23.9-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1239)
    * [1.24.3-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243)
  * The following control plane versions are no longer available: 
    * 1.20.15-gke.9900
    * 1.21.12-gke.1700
    * 1.22.8-gke.201
    * 1.22.8-gke.202
    * 1.22.8-gke.2200
    * 1.22.9-gke.1300
    * 1.22.9-gke.1500
    * 1.22.9-gke.2000
    * 1.23.5-gke.1503
    * 1.23.5-gke.2400
    * 1.23.6-gke.1500
    * 1.23.6-gke.1501
    * 1.23.6-gke.1700
    * 1.23.6-gke.2200
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.20.15-gke.11400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237) with this release.



## August 04, 2022

Change

#### (2022-R19) Version updates

  * The following control plane and node versions are now available:

    * [1.20.15-gke.13400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.14-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12114)
    * [1.22.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12212)
    * [1.24.3-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1243)
  * The following control plane versions are no longer available: 

    * 1.21.12-gke.1500
    * 1.24.2-gke.300
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.2-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1242) with this release.




## June 30, 2022

Change

#### (2022-R16) Version updates

  * Control plane and node version [1.24.1-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1241) is now available.
  * The following control plane versions are no longer available: 
    * 1.19.16-gke.9400
    * 1.19.16-gke.11000
    * 1.19.16-gke.11800
    * 1.19.16-gke.13800
    * 1.19.16-gke.14000
    * 1.19.16-gke.14500
    * 1.19.16-gke.15700
    * 1.20.15-gke.6000
    * 1.20.15-gke.8000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.24 to version [1.24.1-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1241) with this release.



## June 23, 2022

Change

#### (2022-R15) Version updates

  * The following control plane and node versions are now available: 
    * [1.19.16-gke.15700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.13-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12113)
    * [1.22.10-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v12210)
    * [1.23.7-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1237)
    * [1.24.1-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#v1241)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.



## June 13, 2022

Change

#### (2022-R14) Version updates

  * Version [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) is now the default version.
  * Control plane version [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) is now available.
  * The following control plane and node versions are now available: 
    * [1.19.16-gke.14500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.8700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
    * [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
    * [1.22.9-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1229)
    * [1.23.5-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235)
    * [1.23.6-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
    * [1.23.6-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
  * Control plane version 1.21.11-gke.900 is no longer available.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to version [1.22.8-gke.202](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to version [1.23.5-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.



## May 26, 2022

Change

#### (2022-R13) Version updates

  * Version [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) is now the default version.
  * The following control plane and node version are now available:

    * [1.19.16-gke.14000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.8200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
    * [1.22.9-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1229)
    * [1.23.6-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
  * The following control plane versions are no longer available: 

    * 1.19.16-gke.10800
    * 1.20.15-gke.3400
    * 1.20.15-gke.3600
    * 1.20.15-gke.4100
    * 1.20.15-gke.5000
    * 1.20.15-gke.5200
    * 1.21.10-gke.400
    * 1.21.10-gke.1300
    * 1.21.10-gke.1500
    * 1.21.10-gke.2000
    * 1.22.6-gke.300
    * 1.22.6-gke.1000
    * 1.22.7-gke.300
    * 1.22.7-gke.900
    * 1.22.7-gke.1300
    * 1.22.7-gke.1500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.20.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228) with this release.




## May 19, 2022

Change

#### (2022-R12) Version updates

  * Version [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now the default version.
  * The following control plane and node versions are now available:

    * [1.19.16-gke.13800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.8000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12112)
    * [1.22.8-gke.201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
    * [1.22.9-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1229)
    * [1.23.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1236)
  * The following control plane versions are no longer available: 

    * 1.19.16-gke.9400
    * 1.19.16-gke.9900
    * 1.21.9-gke.1002
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.16-gke.10800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) with this release.




## May 11, 2022

Change

#### (2022-R11) Version updates

  * Version [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111) is now the default version.
  * The following control plane versions are no longer available: 
    * 1.21.6-gke.1503
    * 1.21.9-gke.300
    * 1.21.9-gke.1001
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.16-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.16-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.23 to [1.23.5-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235) with this release.



## May 03, 2022

Change

### Page: No Channel

#### (2022-R10) Version updates

  * The following control plane and node versions are now available: 

    * [1.19.16-gke.11800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
    * [1.22.8-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228)
    * [1.23.5-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235)
    * [1.23.5-gke.2400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md#v1235)
  * The following control plane versions are no longer available:

    * 1.19.16-gke.9200
    * 1.20.15-gke.2500
    * 1.21.5-gke.1805 
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.




## April 21, 2022

Change

#### (2022-R9) Version updates

  * Version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.19.16-gke.11000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.5200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
  * The following control plane versions are no longer available: 
    * 1.19.16-gke.8300
    * 1.20.15-gke.1000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.19.16-gke.9200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.20.15-gke.3400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.20.15-gke.3400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to version [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110) with this release.



## April 11, 2022

Change

#### (2022-R8) Version updates

  * The following control plane and node versions are now available: 
    * [1.19.16-gke.10800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.5000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.11-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12111)
  * The following control plane versions are no longer available: 
    * 1.19.16-gke.6800
    * 1.20.15-gke.300
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.19.16-gke.8300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.



## March 31, 2022

Change

#### (2022-R07) Version updates

  * Version [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now the default version.

  * The following control plane and node versions are now available:

    * [1.19.16-gke.9900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916).
    * [1.20.15-gke.4100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015).
    * [1.21.10-gke.2000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110).
    * [1.22.8-gke.200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1228).
  * The following control plane versions are no longer available:

    * 1.19.16-gke.6100
    * 1.20.12-gke.1500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.16-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.19.16-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.




## March 21, 2022

Change

#### (2022-R6) Version updates

  * The following control plane and node versions are now available:

    * [1.19.16-gke.9400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.15-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.10-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110)
    * [1.22.7-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.




## March 14, 2022

Change

#### (2022-R5) Version updates

  * Version [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) is now the default version.
  * The following control plane and node versions are now available:

    * [1.19.16-gke.9200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1196)
    * [1.20.15-gke.3400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
    * [1.21.10-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110)
    * [1.22.7-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227)
  * The following control plane versions are no longer available:

    * 1.19.16-gke.3600
    * 1.20.11-gke.1300
    * 1.20.11-gke.1801
    * 1.22.4-gke.1501
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.16-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) with this release.




Issue

If you specify `--enable-dataplane-v2` in a Windows LTSC node pool running GKE version 1.22.7-gke.1300, Windows nodes cannot join the cluster.

## March 07, 2022

Change

#### (2022-R4) Version updates

  * The following control plane and node versions are now available: 
    * [1.19.16-gke.8300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916).
    * [1.20.15-gke.2500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015).
    * [1.21.9-gke.1002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219).
    * [1.21.10-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v12110).
    * [1.22.7-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227).
    * [1.22.7-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1227).
  * The following control plane versions are no longer available: 

    * 1.19.16-gke.1500
    * 1.21.5-gke.1802
    * 1.22.3-gke.1500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.16-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.16-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.




## February 24, 2022

Change

#### (2022-R03) Version updates

  * Version [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now the default version.
  * Control plane and node version [1.19.16-gke.6800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
  * Control plane and node version [1.20.15-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015)
  * Control plane and node version [1.21.5-gke.1805](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
  * Control plane and node version [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216)
  * Control plane and node version [1.21.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219)
  * Control plane and node version [1.22.3-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1223)
  * Control plane and node version [1.22.4-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1224)
  * Control plane and node version [1.22.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226)
  * Node version [1.18.20-gke.6101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) is now available.
  * Node version [1.21.6-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now available.
  * Node version [1.21.9-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) is now available.
  * The following control plane versions are no longer available: 
    * 1.19.15-gke.1801
    * 1.21.6-gke.1500 
  * Node version 1.21.6-gke.1500 is no longer available.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.6-gke.1503](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.22 to [1.22.6-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) with this release.



## February 10, 2022

Fixed

Versions 1.21.9-gke.300, 1.22.6-gke.300, and 1.23.2-gke.300 contain a fix for a race condition which could result in erroneously detaching all endpoints from network endpoint groups for a short period.

## February 03, 2022

Change

#### (2022-R02) Version updates

  * Control plane and node version [1.19.16-gke.6100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) is now available.
  * Control plane and node version [1.20.15-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12015) is now available.
  * Control plane and node version [1.21.9-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1219) is now available.
  * Control plane and node version [1.22.6-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#v1226) is now available.
  * Control plane version 1.21.5-gke.1302 is no longer available.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.16-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.16-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) with this release.



## January 21, 2022

Change

#### (2022-R01) Version updates

  * Version [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216) is now the default version.
  * Control plane and node version [1.19.16-gke.3600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916) is now available.
  * The following control plane versions are no longer available: 
    * 1.19.15-gke.1300
    * 1.20.10-gke.1600
    * 1.20.10-gke.2100
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.15-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) with this release.



## December 06, 2021

Change

#### (2021-R34) Version updates

  * The following control plane versions are no longer available: 
    * 1.19.13-gke.1900, 1.19.14-gke.301, 1.19.14-gke.1900, 1.19.14-gke.2300, 1.19.15-gke.500
    * 1.21.3-gke.2003, 1.21.4-gke.2300, 1.21.4-gke.2302, 1.21.5-gke.1300
  * The following control planes and nodes with auto-upgrade enabled will be upgraded with this release: 
    * From version 1.18 to [1.19.15-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * From version 1.19 to [1.20.11-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)
    * From version 1.20 to [1.20.11-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)
    * From version 1.21 to [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)



## November 19, 2021

Change

The [2021-R33](https://cloud.google.com/kubernetes-engine/docs/release-notes#2021-r33_version_updates) release notes for **No channel** were updated with the following additions:

  * The following control plane and node versions are now available: 
    * 1.19.16-gke.1500
    * 1.20.12-gke.1500
    * 1.21.6-gke.1500



## November 15, 2021

Change

_2021-11-19 update_ : Added new control plane and node versions for the 2021-R33 release in _No channel_.

Change

#### (2021-R33) Version updates

  * Version [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.19.16-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11916)
    * [1.20.12-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12012)
    * [1.21.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1216)
  * The following control plane versions are no longer available: 
    * 1.20.10-gke.301
    * 1.21.3-gke.2001
  * The following control planes and nodes with auto-upgrade enabled will be upgraded with this release: 
    * From version 1.18 to [1.19.15-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * From version 1.19 to [1.19.15-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)



## October 29, 2021

Change

#### Revisions for 2021-R32

_2021-12-03 update_ : Revised upgrade versions. Control planes and nodes with auto-upgrade enabled will be upgraded:

  * From version 1.18 to [1.19.14-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11914).
  * From version 1.19 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010).



Change

#### (2021-R32) Version updates

  * The following control plane and node versions are now available: 
    * [1.19.15-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * [1.20.11-gke.1801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)
    * [1.21.3-gke.2003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213)
    * [1.21.4-gke.2302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214)
    * [1.21.5-gke.1302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
    * [1.21.5-gke.1802](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
  * The following control plane versions are no longer available: 
    * 1.19.13-gke.1200
    * 1.20.9-gke.1001
    * 1.20.9-gke.2100
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.14-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11914) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.3-gke.2003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## October 15, 2021

Change

#### (2021-R31) Version updates

  * Version [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) is now the default version.
  * The following control plane and node versions are now available:

    * [1.19.15-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * [1.20.11-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12011)
    * [1.21.5-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1215)
  * Control plane version 1.19.13-gke.701 is no longer available.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.13-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) with this release.

  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.




## October 01, 2021

Change

#### (2021-R30) Version updates

  * Version [1.20.10-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.19.14-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11914)
    * [1.19.15-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11915)
    * [1.20.10-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010)
    * [1.21.3-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213)
    * [1.21.4-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1214)
  * The following control plane versions are no longer available: 
    * 1.18.20-gke.3001
    * 1.18.20-gke.3300
    * 1.18.20-gke.4100
    * 1.18.20-gke.4501
    * 1.18.20-gke.6000
    * 1.19.12-gke.2101
    * 1.20.8-gke.2101
    * 1.20.9-gke.701
    * 1.20.9-gke.1000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.13-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.20.10-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.21 to [1.21.3-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#v1213) with this release.



## September 17, 2021

Change

#### (2021-R29) Version updates

  * Version [1.20.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) is now the default version.
  * Control plane version [1.20.9-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209) is now available.
  * The following control plane and node versions are now available: 
    * [1.18.20-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.14-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11914)
    * [1.20.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v12010)
  * The following control plane versions are no longer available: 
    * 1.17.17-gke.9100
    * 1.18.20-gke.901
    * 1.18.20-gke.2300
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.18.20-gke.3001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1182) with this release.



## September 07, 2021

Change

This note was updated on September 24, 2021. Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.

Change

#### (2021-R28) Version updates

  * Version [1.20.8-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.18.20-gke.3001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.18.20-gke.4501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912)
    * [1.19.13-gke.701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913)
    * [1.19.14-gke.301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11914)
    * [1.20.8-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208)
    * [1.20.9-gke.701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
    * [1.20.9-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
  * The following control plane versions are no longer available: 
    * 1.18.20-gke.3000
    * 1.18.20-gke.4500
    * 1.19.12-gke.2100
    * 1.19.13-gke.700
    * 1.19.14-gke.300
    * 1.20.8-gke.2100
    * 1.20.9-gke.700
    * 1.20.9-gke.1000
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.12-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.20.8-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.



## August 20, 2021

Change

#### (2021-R27) Version updates

  * Version [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.18.20-gke.4100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.13-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913)
    * [1.20.9-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
  * The following control plane versions are no longer available: 
    * 1.18.20-gke.501
    * 1.19.9-gke.1900
    * 1.19.10-gke.1000
    * 1.19.10-gke.1001
    * 1.19.10-gke.1601
    * 1.19.10-gke.1701
    * 1.19.11-gke.1701
    * 1.19.11-gke.2101
    * 1.19.12-gke.700
    * 1.19.12-gke.900
    * 1.19.12-gke.1100
    * 1.20.8-gke.700
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to [1.18.20-gke.901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to [1.19.12-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912) with this release.



## August 12, 2021

Change

#### (2021-R26) Version updates

  * The following control plane and node versions are now available: 
    * [1.18.20-gke.901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.18.20-gke.3300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.13-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913)
    * [1.20.9-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
  * The following control plane versions are no longer available: 
    * 1.17.17-gke.3700
    * 1.17.17-gke.4400
    * 1.17.17-gke.4900
    * 1.17.17-gke.5400
    * 1.17.17-gke.6000
    * 1.17.17-gke.6700
    * 1.17.17-gke.7200
    * 1.17.17-gke.7800
    * 1.17.17-gke.8200
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.



## August 03, 2021

Change

#### (2021-R25) Version updates

  * The following control plane and node versions are now available: 
    * [1.18.20-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.13-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11913)
    * [1.20.9-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1209)
  * The following control plane versions are no longer available: 
    * 1.18.17-gke.1901
    * 1.18.19-gke.1701
    * 1.18.19-gke.2101
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.20-gke.501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820) with this release.



## July 27, 2021

Change

#### (2021-R24) Version updates

  * Version [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) is now the default version.
  * The following control plane and node versions are now available: 
    * [1.18.20-gke.2300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.12-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912)
    * [1.20.8-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208)
  * The following control plane versions are no longer available: 
    * 1.18.18-gke.1101
    * 1.18.18-gke.1701
    * 1.20.7-gke.1800
    * 1.20.7-gke.2200
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.20.8-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208) with this release.



## July 20, 2021

Change

#### (2021-R23) Version updates

  * The following control plane and node versions are now available: 
    * [1.19.12-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912)
    * [1.19.12-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912)
    * [1.20.8-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208)
  * The following control plane versions are no longer available: 
    * 1.18.17-gke.1900
    * 1.19.9-gke.1400
    * 1.20.6-gke.1000
    * 1.20.6-gke.1400
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.20.7-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207) with this release.



## July 09, 2021

Change

#### (2021-R22) Version updates

  * The following versions are now available: 
    * [1.18.18-gke.1101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11818)
    * [1.18.18-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11818)
    * [1.18.19-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11819)
    * [1.18.19-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11819)
    * [1.18.20-gke.900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.10-gke.1001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910)
    * [1.19.10-gke.1601](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910)
    * [1.19.10-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910)
    * [1.19.11-gke.1701](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11911)
    * [1.19.11-gke.2101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11911)
    * [1.19.12-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11912)
    * [1.20.8-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208)
  * The following versions are no longer available: 
    * 1.18.18-gke.1100
    * 1.18.18-gke.1700
    * 1.18.19-gke.1700
    * 1.18.19-gke.2100
    * 1.19.10-gke.1600
    * 1.19.10-gke.1700
    * 1.19.11-gke.1700
    * 1.19.11-gke.2100



## June 25, 2021

Change

#### (2021-R21) Version updates

  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version.
  * The following versions are now available: 
    * [1.18.19-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11819)
    * [1.18.20-gke.501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11820)
    * [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199)
    * [1.19.11-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11911)
    * [1.20.6-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206)
    * [1.20.7-gke.2200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207)
  * The following versions are no longer available: 
    * 1.17.17-gke.3700
    * 1.17.17-gke.4400
    * 1.17.17-gke.4900
    * 1.17.17-gke.5400
    * 1.17.17-gke.6000
    * 1.17.17-gke.6700
    * 1.17.17-gke.7200
    * 1.17.17-gke.7800
    * 1.17.17-gke.8200
    * 1.17.17-gke.9100
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.17 to version [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.19.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) with this release.



## June 16, 2021

Change

#### (2021-R20) Version updates

  * Version [1.19.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now the default version.
  * The following versions are now available: 
    * [1.18.19-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11819)
    * [1.19.11-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11911)
    * [1.20.7-gke.1800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1207)
  * The following versions are no longer available: 
    * 1.18.17-gke.1200
    * 1.18.17-gke.1201
    * 1.19.9-gke.1400
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.19 to version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) with this release.



## June 09, 2021

Change

#### (2021-R19) Version updates

  * Version [1.18.17-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version.
  * The following versions are now available: 
    * [1.17.17-gke.9100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717)
    * [1.18.17-gke.1201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817)
    * [1.18.17-gke.1901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817)
    * [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206)
  * The following versions are no longer available: 
    * 1.18.17-gke.100
    * 1.18.17-gke.700
    * 1.19.8-gke.1600
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.17-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.20 to version [1.20.6-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1206) with this release.



## May 28, 2021

Change

#### (2021-R18) Version updates

  * Version [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version.
  * Version [1.18.18-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11818) is now available.
  * Version [1.19.10-gke.1700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now available.
  * Version 1.18.17-gke.100 is no longer available.
  * Version 1.19.8-gke.1600 is no longer available.



## May 19, 2021

Change

#### (2021-R17) Version updates

  * Version [1.17.17-gke.8200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.18.18-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11818) is now available.
  * Version [1.19.10-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now available.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.17 to version [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) with this release.



## May 12, 2021

Change

#### (2021-R16) Version updates

  * Version [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199) is now the default version.
  * Version [1.17.17-gke.7800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.19.10-gke.1000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v11910) is now available.
  * The following versions are no longer available: 
    * 1.18.15-gke.1501
    * 1.18.15-gke.1502
    * 1.18.16-gke.1201
    * 1.18.16-gke.2100
    * 1.18.16-gke.300
    * 1.18.16-gke.302
    * 1.18.16-gke.502
  * The following control planes and nodes with auto-upgrade enabled will be upgraded with this release: 
    * From version 1.17 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).
    * From version 1.18 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).
    * From version 1.19 to [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198).



## May 04, 2021

Change

#### (2021-R15) Version updates

  * Version [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817) is now the default version.
  * Version [1.17.17-gke.7200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * The following versions are no longer available: 
    * 1.16.15-gke.12500
    * 1.16.15-gke.14800
    * 1.17.17-gke.1101
    * 1.17.17-gke.1500
    * 1.17.17-gke.2800
    * 1.17.17-gke.3000
  * The following control planes and nodes with auto-upgrade enabled will be upgraded with this release: 
    * From version 1.17 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).
    * From version 1.18 to [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817).
    * From version 1.19 to [1.19.8-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198).



## April 27, 2021

Change

#### (2021-R14) Version updates

  * The following versions are now available: 
    * [1.17.17-gke.6700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717)
    * [1.18.17-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817)
    * [1.19.9-gke.1900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.



## April 20, 2021

Change

#### (2021-R13) Version updates

  * Version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now the default version.
  * The following versions are now available: 
    * [1.17.17-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717)
    * [1.18.17-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817)
    * [1.19.9-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1199)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.16 to version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.17 to version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.



## April 14, 2021

Change

#### (2021-R12) Version updates

  * Version [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now the default version.
  * The following versions are now available: 
    * [1.17.17-gke.5400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717)
    * [1.18.17-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817)
    * [1.19.8-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1198)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.16 to version [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.17 to version [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.



## April 06, 2021

Change

#### (2021-R11) Version updates

  * The following versions are now available: 
    * [1.16.15-gke.14800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615)
    * [1.17.17-gke.4900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717)
    * [1.18.17-gke.100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11817)
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.16-gke.502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.



## March 29, 2021

Change

#### (2021-R10) Version updates

  * Version [1.17.17-gke.2800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now the default version.
  * The following versions are now available: 
    * [1.17.17-gke.4400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717)
    * [1.18.16-gke.502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816)
    * [1.18.16-gke.1201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816)
    * [1.18.16-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816)
  * The following versions are no longer available: 
    * 1.15.12-gke.6002
    * 1.16.15-gke.10600
    * 1.16.15-gke.11800
    * 1.16.15-gke.7801
    * 1.17.15-gke.800
    * 1.17.17-gke.1100
    * 1.18.12-gke.1210
    * 1.18.14-gke.1200
    * 1.18.14-gke.1600
    * 1.18.15-gke.1100
    * 1.18.15-gke.1102
    * 1.18.15-gke.1500
    * 1.18.16-gke.1200
    * 1.18.16-gke.500
  * Control planes and nodes with auto-upgrade enabled will be upgraded from versions 1.17 and earlier to version [1.17.17-gke.2800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.18 to version [1.18.16-gke.302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) with this release.



## March 23, 2021

Announcement

Starting tomorrow, March 24, 2021, the mechanism we use to create GKE release notes will change. Although this change does not affect the content of the notes, it does affect the presentation and underlying syntax. If you subscribe to the XML feed for this page, entries for March 24 and earlier will be updated as a result of changes to formatting and syntax; the content itself did not change.

The feed URL will also change from `https://cloud.google.com/feeds/kubernetes-engine-release-notes.xml` to `https://cloud.google.com/feeds/gke-main-release-notes.xml`. We will automatically redirect from the old URL to the new one.

## March 16, 2021

Change

#### (2021-R9) Version updates

  * Version [1.17.17-gke.3700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.18.15-gke.1502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available.
  * Version [1.18.16-gke.302](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now available.
  * Version [1.18.16-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now available.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from versions 1.17 and earlier to version [1.17.17-gke.1101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.
  * Control planes and nodes with auto-upgrade enabled will be upgraded from versions 1.18 to version [1.18.15-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) with this release.



## March 05, 2021

Change

#### (2021-R8) Version updates

  * Version [1.17.17-gke.1101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available. This version is now the default.
  * Version [1.17.17-gke.3000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.18.15-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available.
  * Version [1.18.16-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now available.
  * Auto-upgrading nodes and control planes upgrade from versions 1.17 and earlier to version [1.17.17-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) with this release.



## February 25, 2021

Change

#### (2021-R7) Version updates

  * Version [1.16.15-gke.7801](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.16.15-gke.12500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.17-gke.1101](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.17.17-gke.2800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.18.16-gke.300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11816) is now available.
  * Version 1.18.12-gke.1206 is no longer available.
  * Auto-upgrading control planes automatically upgrade from version 1.18 to version [1.18.12-gke.1210](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.
  * Auto-upgrading nodes automatically upgrade from version 1.18 to version [1.18.12-gke.1210](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## February 17, 2021

Change

This note was updated on February 23, 2021. Version 1.15.12-gke.6002 is still available in this channel for R6.

Change

#### (2021-R6) Version updates

  * Version [1.16.15-gke.11800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.17-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.18.15-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available.

  * Version 1.16.15-gke.6000 is no longer available.

  * Version 1.16.15-gke.6900 is no longer available.

  * Version 1.16.15-gke.7300 is no longer available.

  * Version 1.17.14-gke.1600 is no longer available.

  * Version 1.17.15-gke.300 is no longer available.

  * Version 1.18.12-gke.1205 is no longer available.

  * Version 1.18.15-gke.800 is no longer available.

  * Auto-upgrading control planes automatically upgrade from version 1.15 to version [1.16.15-gke.7800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.




## February 09, 2021

Change

#### (2021-R5) Version updates

  * Version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) is now available. This version is now the default.
  * Version [1.16.15-gke.11000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.17-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.18.12-gke.1210](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available.
  * Version [1.18.15-gke.1100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available.
  * Version 1.16.15-gke.4901 is no longer available.
  * Version 1.17.14-gke.400 is no longer available.
  * Auto-upgrading control planes automatically upgrade from version 1.15 to version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.
  * Auto-upgrading control planes automatically upgrade from version 1.16 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading control planes automatically upgrade from version 1.17 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes automatically upgrade from version 1.15 to version 1.17.15-gke.800 with this release. version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes automatically upgrade from version 1.16 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes automatically upgrade from version 1.17 to version [1.17.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11715) with this release.
  * Auto-upgrading nodes automatically upgrade from version 1.18 to version [1.18.12-gke.1206](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



Change

This note was updated on February 23, 2021 to include the following control plane auto-upgrades for this channel: 1.15 to 1.16.15-gke.6000 and 1.16 and 1.17 to 1.17.15-gke.800. The node upgrades from 1.15, 1.16, and 1.17 to version 1.17.15-gke.800 were added to this channel.

## February 02, 2021

Change

This note was updated on February 10, 2021. The node auto-upgrade from 1.15 to version 1.16.15-gke.6000 was removed from this channel.

Change

#### (2021-R4) Version updates

  * Version [1.16.15-gke.10600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.17-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11717) is now available.
  * Version [1.18.15-gke.800](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11815) is now available.
  * Version 1.17.14-gke.1200 is no longer available.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.18 to version [1.18.12-gke.1205](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) with this release.



## January 25, 2021

Change

#### (2021-R3) Version updates

  * Version [1.17.16-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11716) is now available.
  * Version [1.18.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11814) is now available.
  * Version 1.17.13-gke.2600 is no longer available.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.17 to version [1.17.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) with this release.



## January 19, 2021

Change

_March 3, 2021 update_ : This release note was updated to add version 1.17.16- gke.1300, which was made available in this release.

Change

#### (2021-R2) Version updates

  * Version [1.17.16-gke.1300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11716) is now available.
  * Version [1.18.12-gke.1201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available.
  * Version [1.18.12-gke.1205](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available.
  * Version [1.18.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11814) is now available.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.15 to version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.



## January 08, 2021

Change

#### (2021-R1) Version updates

  * Version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available. This version is now the default.
  * Version [1.17.14-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available.
  * Version 1.14.10-gke.50 is no longer available.
  * Version 1.14.10-gke.902 is no longer available.
  * Version 1.14.10-gke.1504 is no longer available.
  * Version 1.15.12-gke.20 is no longer available.
  * Version 1.15.12-gke.4000 is no longer available.
  * Version 1.15.12-gke.4002 is no longer available.
  * Version 1.15.12-gke.5000 is no longer available.
  * Version 1.15.12-gke.6001 is no longer available.
  * Version 1.16.15-gke.4300 is no longer available.
  * Version 1.16.15-gke.4301 is no longer available.
  * Version 1.16.15-gke.5500 is no longer available.
  * Version 1.17.13-gke.2001 is no longer available.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.14 to version [1.15.12-gke.6002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) with this release.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.16 to version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.17 to version [1.17.14-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) with this release.



## December 14, 2020

Change

#### (R41) Version updates

  * Version [1.16.15-gke.7300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.14-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.14 to version [1.15.12-gke.6001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) with this release.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.16 to version [1.16.15-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.
  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.17 to version [1.17.13-gke.2600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) with this release.



## December 07, 2020

Change

#### (R40) Version updates

  * Version [1.15.12-gke.6002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.15-gke.6900](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.14-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available.
  * Version [1.18.12-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v11812) is now available.

This version is available in preview.

  * Version [1.19.4-gke.1200](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1194) is now available.

This version is available in preview. Before creating GKE v1.19 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#urgent-upgrade-notes).

  * Auto-upgrading nodes automatically upgrade from version 1.14 to version [1.15.12-gke.6001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) with this release.

  * Auto-upgrading nodes automatically upgrade from version 1.16 to version [1.16.15-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) with this release.

  * Auto-upgrading nodes automatically upgrade from version 1.17 to version [1.17.13-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) with this release.

  * Version 1.19.4-gke.700 is no longer available.




## December 01, 2020

Change

#### (R39) Version updates

  * Version [1.16.15-gke.4301](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.16.15-gke.6000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.13-gke.1401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available.
  * Version [1.17.14-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11714) is now available.

This release sets `sysctl net.netfilter.nf_conntrack_tcp_be_liberal=1` on the node image. This discourages netfilter from resetting TCP connections.

  * Version [1.19.4-gke.700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1194) is now available.

This version is available in preview. Before creating GKE v1.19 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#urgent-upgrade-notes).

  * Version 1.19.3-gke.2100 is no longer available.

  * Version 1.19.3-gke.2700 is no longer available.

  * Auto-upgrading nodes in the no channel automatically upgrade from version 1.17 to version [1.17.13-gke.1401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) with this release.




## November 24, 2020

Change

The November 17, 2020 release removed the following GKE versions.

  * Version 1.16.13-gke.401 is no longer available.
  * Version 1.19.3-gke.1500 is no longer available.



## November 17, 2020

Change

This note was updated on November 24, 2020.

Change

#### (R38) Version updates

  * Version [1.16.15-gke.5500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.13-gke.2600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available.
  * Version [1.19.3-gke.2700](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1193) is now available.

This version is available in preview. Before creating GKE v1.19 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#urgent-upgrade-notes).




## November 12, 2020

Change

#### (R37) Version updates

  * Version [1.16.15-gke.4901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.13-gke.2001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available.
  * Version [1.19.3-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1193) is now available.

This version is available in preview. Before creating GKE v1.19 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#urgent-upgrade-notes).

  * Version 1.16.13-gke.404 is the new default version.




## November 06, 2020

Change

  * Version [1.16.13-gke.404](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available.
  * Version [1.16.15-gke.4300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.13-gke.1400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available.
  * Version [1.19.3-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1193) is now available.

This version is available in preview. Before creating GKE v1.19 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#urgent-upgrade-notes).




## October 28, 2020

Change

#### (R35) Version updates

  * Version [1.16.15-gke.3500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.13-gke.600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11713) is now available.
  * Version [1.19.3-gke.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#v1193) is now available.
  * Auto-upgrading nodes and control planes upgrade from version 1.14 to version 1.15.12-gke.20 during this release.
  * Auto-upgrading nodes and control planes upgrade from version 1.17 to version 1.17.12-gke.1504 during this release.



## October 20, 2020

Change

#### (R34) Version updates

  * Version [1.14.10-gke.1504](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.
  * Version [1.15.12-gke.4002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.15.12-gke.6001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.13-gke.403](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available.
  * Version [1.16.15-gke.2601](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.12-gke.1504](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11712) is now available.
  * Version [1.17.12-gke.2502](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11712) is now available.
  * Auto-upgrading nodes and control planes upgrade from version 1.14 to version 1.15.12-gke.20 during this release.
  * Auto-upgrading control planes upgrade from version 1.15 to version 1.16.13-gke.401 during this release.



## October 12, 2020

Change

#### (R33) Version updates

  * Version [1.14.10-gke.901](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.
  * Version [1.15.12-gke.5000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.15-gke.1600](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.12-gke.1501](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11712) is now available.
  * Auto-upgrading nodes and control planes upgrade from version 1.14 to version 1.15.12-gke.20 during this release.



## October 02, 2020

Change

#### (R32) Version updates

  * Version [1.15.12-gke.4000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.15-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11615) is now available.
  * Version [1.17.12-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v11712) is now available.
  * Version 1.16.13-gke.401 is the new default version for clusters with no channel.
  * Auto-upgrading control planes upgrade from version 1.14 to version 1.14.10-gke.50 during this release.
  * Auto-upgrading control planes upgrade from version 1.15 to version 1.15.12-gke.20 during this release.
  * Auto-upgrading nodes control planes upgrade from version 1.16 to version 1.16.13-gke.401 during this release.



## September 25, 2020

Change

#### (R31) Version updates

  * Version [1.17.9-gke.6300](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#v1179) is now available.
  * Auto-upgrading control planes upgrade from version 1.16 to version 1.16.13-gke.401 during this release.
  * Auto-upgrading control planes upgrade from version 1.17 to version 1.17.9-gke.1504 during this release.



## September 15, 2020

Change

#### (R30) Version updates

  * Version 1.15.12-gke.20 is the new default version for clusters with no channel.



## September 14, 2020

Change

#### (R29.1) Version updates

  * Version [1.14.10-gke.50](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.
  * Version [1.15.12-gke.20](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.13-gke.401](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available.



## September 03, 2020

Change

#### (R29) Version updates

  * Version [1.15.12-gke.17](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.13-gke.400](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available.
  * Auto-upgrading nodes upgrade from version 1.14 to version 1.15.12-gke.2 during this release if they have not already done so.



## August 27, 2020

Change

#### (R28) Version updates

  * Auto-upgrading nodes begin upgrading from version 1.14 to version 1.15.12-gke.2 in this release. The auto-upgrades will continue gradually over the course of several releases.



## August 20, 2020

Change

#### (R27) Version updates

  * Version [1.18.6-gke.2100](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1186) is now available.

This version is available in preview. Before creating GKE 1.18 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#urgent-upgrade-notes).




## August 06, 2020

Change

#### (R26) Version updates

  * Version [1.15.12-gke.16](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.18.6-gke.1500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1186) is now available.

This version is available in preview. Before creating GKE 1.18 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#urgent-upgrade-notes).




## July 28, 2020

Change

#### (R25) Version updates

  * Version [1.15.12-gke.13](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.13-gke.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11613) is now available.

This version includes node image upgrades for Ubuntu (`ubuntu-gke-1804-1-16-v20200610`).

  * Version [1.18.6-gke.500](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1186) is now available.

This version is available in preview. Before creating GKE 1.18 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#urgent-upgrade-notes).




## July 22, 2020

Change

#### (R24) Version updates

  * Version [1.18.4-gke.1201](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#v1184) is now available.

This version is available in preview. Before creating GKE 1.18 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#urgent-upgrade-notes).




## July 13, 2020

Change

#### (R23) Version updates

  * Version [1.14.10-gke.46](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.
  * Version [1.15.12-gke.9](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.
  * Version [1.16.11-gke.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11611) is now available.



## June 29, 2020

Change

  * [1.14.10-gke.45](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.

  * [1.15.12-gke.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.

  * [1.16.10-gke.8](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v11610) is now available.




## June 23, 2020

Change

  * [1.14.10-gke.42](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.

  * [1.15.12-gke.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.




## June 08, 2020

Change

  * [1.14.10-gke.41](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.

  * [1.15.11-gke.17](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11511) is now available.

  * [1.15.12-gke.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11512) is now available.

  * [1.16.9-gke.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1169) is now available.




## June 01, 2020

Change

  * [1.14.10-gke.40](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.

  * [1.15.11-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11511) is now available.

  * [1.16.9-gke.2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1168) is now available.




## May 19, 2020

Change

  * [1.16.8-gke.17](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1168) is now available.

  * [1.15.11-gke.14](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11511) is now available. In clusters using version 1.15.11-gke.14, NodeLocal DNSCache now reaches out to custom stubDomains using UDP. For more information, see [Setting up NodeLocal DNSCache](https://cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache#details).




## May 13, 2020

Change

[1.15.11-gke.13](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11511) is now available.

Change

[1.16.8-gke.15](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#v1168) is now generally available for new clusters. Existing clusters and nodes will not automatically upgrade in this release.

**Important:** Before you migrate to GKE 1.16, you **must** review:

  * [Deprecated APIs in 1.16.](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-16)
  * [Known issues.](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#known-issues)
  * [Urgent upgrade notes.](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#urgent-upgrade-notes)



## May 04, 2020

Change

[1.15.11-gke.12](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v11510) is now available.

## April 27, 2020

Change

  * [1.14.10-gke.37](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v11410) is now available.

  * [1.15.11-gke.11](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#v11511) is now available.




## April 15, 2020

Change

  * [1.14.10-gke.36](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1149) is now available.

  * [1.15.11-gke.9](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v11510) is now available. This version updates Calico to 3.8.7. This version fixes an issue where Calico Pods would fail to initialize after restarting. The issue occurred because the Calico CNI script tried to overwrite a file which was referenced by Kubelet at the same time. For more information on the fix, see the [open source documentation](https://github.com/projectcalico/cni-plugin/pull/84).

  * [1.17.4-gke.6](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#changelog-since-v1173) is now available in [alpha clusters](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).




## April 07, 2020

Change

[1.15.11-gke.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v11510) is now available.

## April 01, 2020

Change

  * [1.14.10-gke.34](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1149) is now available.

  * [1.15.11-gke.3](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v11510) is now available.

  * [1.17.4-gke.2 preview](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#changelog-since-v1173) is now available.

Before creating GKE 1.17 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#urgent-upgrade-notes).




## March 26, 2020

Change

[1.15.11-gke.1](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v11510) is now available. The node image for Container-Optimized OS is updated to [cos-77-12371-183-0](https://cloud.google.com/container-optimized-os/docs/release-notes#cos-77-12371-183-0).

## March 20, 2020

Change

  * [1.14.10-gke.32](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1149) is now available.

  * [1.15.9-gke.26](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v1158) is now available.

  * [1.17.3-gke.7 is now available to preview.](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#changelog-since-v1172) is now available.

Before creating GKE 1.17 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#urgent-upgrade-notes).




## March 16, 2020

Change

  * [1.14.10-gke.30](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1149) is now available.

  * [1.15.9-gke.24](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v1158) is now available.

  * [1.17.3-gke.4](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#changelog-since-v1172) is now available for preview.

Before creating GKE 1.17 clusters, you **must** review the [known issues](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#known-issues) and [urgent upgrade notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#urgent-upgrade-notes).




## March 06, 2020

Change

##### v.1.13.x

  * There are no new 1.13 versions this week.



##### v.1.14.x

  * [1.14.10-gke.27](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-since-v1149)



##### v.1.15.x

  * [1.15.9-gke.22](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#changelog-since-v1159)



## February 25, 2020

Change

##### v.1.13.x

  * There are no new 1.13 versions this week.



##### v.1.14.x

  * 1.14.10-gke.17



##### v.1.15.x

  * 1.15.9-gke.12



## February 18, 2020

Change

##### v.1.13.x

  * 1.13.12-gke.30



##### v.1.14.x

  * 1.14.10-gke.24



##### v.1.15.x

  * 1.15.9-gke.9



Change

Node image for Container-Optimized OS updated to [cos-77-12371-141-0](https://cloud.google.com/container-optimized-os/docs/release-notes#cos-stable-77-12371-141-0).

## February 11, 2020

Change

##### v.1.13.x

  * 1.13.12-gke.25



##### v.1.14.x

  * 1.14.10-gke.17



##### v.1.15.x

  * 1.15.9-gke.8



## February 04, 2020

Change

##### v.1.13.x

  * There are no new 1.13 versions this week.



##### v.1.14.x

  * 1.14.10-gke.21



##### v.1.15.x

  * 1.15.8-gke.3



## January 29, 2020

Change

##### v.1.13.x

  * There are no new 1.13 versions this week.



##### v.1.14.x

  * There are no new 1.14 versions this week.



##### v.1.15.x

  * 1.15.8-gke.2



## January 22, 2020

Change

##### v.1.13.x

  * 1.13.11-gke.23

  * 1.13.12-gke.25




##### v.1.14.x

  * 1.14.7-gke.40
  * 1.14.8-gke.33
  * 1.14.9-gke.23
  * 1.14.10-gke.17



##### v.1.15.x

  * 1.15.7-gke.23



## January 07, 2020

Change

##### v.1.13.x

  * 1.13.12-gke.17



##### v.1.14.x

  * 1.14.10-gke.0



##### v.1.15.x

  * 1.15.7-gke.2



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
