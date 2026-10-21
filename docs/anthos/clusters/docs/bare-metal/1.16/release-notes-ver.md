---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/release-notes-ver/
title: Distributed Cloud 1.16 release notes \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:02.706990+00:00
---

# Distributed Cloud 1.16 release notes  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/release-notes-ver/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Distributed Cloud 1.16 release notes Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/release-notes-ver)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document lists production updates to Distributed Cloud. We recommend that Google Distributed Cloud developers periodically check this list for any new announcements.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/anthos-bare-metal-release-notes.xml) directly. 

## August 26, 2024

Announcement

### Release 1.16.12

Google Distributed Cloud for bare metal 1.16.12 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.12 runs on Kubernetes 1.27.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.12: 

  * High-severity container vulnerabilities:

    * [CVE-2019-16884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16884)

    * [CVE-2021-30465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30465)

    * [CVE-2021-33194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33194)

    * [CVE-2021-38561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38561)

    * [CVE-2021-43565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43565)

    * [CVE-2021-43816](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43816)

    * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)

    * [CVE-2022-27191](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27191)

    * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)

    * [CVE-2022-32149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32149)

    * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)

    * [CVE-2022-43945](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43945)

    * [CVE-2023-47038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47038)

    * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)

    * [CVE-2024-0567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0567)

    * [CVE-2024-7348](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7348)

    * [CVE-2024-36971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36971)

    * [CVE-2024-36978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36978)

    * [CVE-2024-38583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38583)

    * [CVE-2024-39480](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39480)

    * [CVE-2024-39495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39495)

    * [CVE-2024-40902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-40902)

    * [CVE-2024-41087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41087)

    * [CVE-2024-41092](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41092)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-19921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19921)

    * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)

    * [CVE-2021-32760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32760)

    * [CVE-2021-41103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41103)

    * [CVE-2021-43784](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43784)

    * [CVE-2022-23471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23471)

    * [CVE-2022-29162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29162)

    * [CVE-2022-29526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29526)

    * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)

    * [CVE-2023-25153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25153)

    * [CVE-2023-25173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25173)

    * [CVE-2023-28642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28642)

    * [CVE-2023-48795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)

    * [CVE-2024-27019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27019)

    * [CVE-2024-36288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36288)

    * [CVE-2024-38662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38662)

    * [CVE-2024-38780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38780)

    * [CVE-2024-39292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39292)

    * [CVE-2024-39475](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39475)

    * [CVE-2024-39476](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39476)

    * [CVE-2024-39482](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39482)

    * [CVE-2024-39484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39484)

    * [CVE-2024-39489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39489)

    * [CVE-2024-39493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-39493)

    * [CVE-2024-41089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41089)

    * [CVE-2024-41095](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41095)

    * [CVE-2024-42070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42070)

    * [CVE-2024-42076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42076)

    * [CVE-2024-42077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42077)

    * [CVE-2024-42082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42082)

    * [GHSA-7ww5-4wqc-m92c](https://github.com/advisories/GHSA-7ww5-4wqc-m92c)

  * Low-severity container vulnerabilities:

    * [CVE-2022-27943](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27943)

    * [CVE-2022-48303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48303)

    * [CVE-2023-25809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25809)

    * [GHSA-5j5w-g665-5m35](https://github.com/advisories/GHSA-5j5w-g665-5m35)

    * [GHSA-77vh-xpmg-72qh](https://github.com/advisories/GHSA-77vh-xpmg-72qh)

    * [GHSA-c9cp-9c75-9v8c](https://github.com/advisories/GHSA-c9cp-9c75-9v8c)

    * [GHSA-xr7q-jx4m-x55m](https://github.com/advisories/GHSA-xr7q-jx4m-x55m)




Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 25, 2024

Announcement

### Release 1.16.11

Google Distributed Cloud for bare metal 1.16.11 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.11 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.11: 

  * High-severity container vulnerabilities:

    * [CVE-2020-22218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-22218)
  * Medium-severity container vulnerabilities:

    * [CVE-2024-35255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35255)



Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## July 03, 2024

Security

### Security bulletin (all minor versions)

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that can be used to obtain access to a remote shell, enabling attackers to gain root access. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts. This vulnerability has a Critical severity.

For mitigation steps and more details, see the [GCP-2024-040](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040) security bulletin.

## July 01, 2024

Announcement

### Release 1.16.10

Google Distributed Cloud for bare metal 1.16.10 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.10 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

Fixed

**Fixes:**

  * Fixed an issue where upgraded clusters didn't get label updates that match the labels applied for newly created clusters, for a given version.



Change

The following container image security vulnerabilities have been fixed in 1.16.10: 

  * High-severity container vulnerabilities:

    * [CVE-2023-6270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6270)

    * [CVE-2023-52434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52434)

    * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)

    * [CVE-2024-0985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0985)

    * [CVE-2024-26882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26882)

    * [CVE-2024-26883](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26883)

    * [CVE-2024-26884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26884)

    * [CVE-2024-26898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26898)

    * [CVE-2024-26907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26907)

    * [CVE-2024-26934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26934)

    * [CVE-2024-27020](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27020)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-7042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7042)

    * [CVE-2023-47233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47233)

    * [CVE-2023-52429](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52429)

    * [CVE-2023-52435](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52435)

    * [CVE-2023-52458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52458)

    * [CVE-2024-0340](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0340)

    * [CVE-2024-0607](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0607)

    * [CVE-2024-22099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22099)

    * [CVE-2024-23849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23849)

    * [CVE-2024-23851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23851)

    * [CVE-2024-24857](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24857)

    * [CVE-2024-24858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24858)

    * [CVE-2024-24861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24861)

    * [CVE-2024-25739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25739)

    * [CVE-2024-26600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26600)

    * [CVE-2024-26602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26602)

    * [CVE-2024-26606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26606)

    * [CVE-2024-26901](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26901)

    * [CVE-2024-26903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26903)

    * [CVE-2024-26910](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26910)

    * [CVE-2024-27013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27013)

    * [CVE-2024-28122](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28122)

    * [CVE-2024-28182](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28182)

    * [CVE-2024-32473](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32473)

    * [CVE-2024-35978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35978)

    * [CVE-2024-35982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35982)

    * [CVE-2024-35984](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35984)

    * [CVE-2024-35997](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35997)

    * [CVE-2024-36902](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36902)

    * [GHSA-6xv5-86q9-7xr8](https://github.com/advisories/GHSA-6xv5-86q9-7xr8)

  * Low-severity container vulnerabilities:

    * [CVE-2021-4440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4440)

    * [CVE-2022-38096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38096)

    * [CVE-2022-48655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48655)

    * [CVE-2023-52447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52447)

    * [CVE-2023-52489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52489)

    * [CVE-2023-52492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52492)

    * [CVE-2023-52493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52493)

    * [CVE-2023-52497](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52497)

    * [CVE-2023-52616](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52616)

    * [CVE-2023-52627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52627)

    * [CVE-2023-52637](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52637)

    * [CVE-2023-52672](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52672)

    * [CVE-2024-0841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0841)

    * [CVE-2024-23850](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23850)

    * [CVE-2024-26581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26581)

    * [CVE-2024-26593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26593)

    * [CVE-2024-26601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26601)

    * [CVE-2024-26610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26610)

    * [CVE-2024-26627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26627)

    * [CVE-2024-26643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26643)

    * [CVE-2024-26665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26665)

    * [CVE-2024-26673](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26673)

    * [CVE-2024-26684](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26684)

    * [CVE-2024-26688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26688)

    * [CVE-2024-26695](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26695)

    * [CVE-2024-26698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26698)

    * [CVE-2024-26702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26702)

    * [CVE-2024-26707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26707)

    * [CVE-2024-26712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26712)

    * [CVE-2024-26727](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26727)

    * [CVE-2024-26748](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26748)

    * [CVE-2024-26749](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26749)

    * [CVE-2024-26753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26753)

    * [CVE-2024-26781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26781)

    * [CVE-2024-26782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26782)

    * [CVE-2024-26787](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26787)

    * [CVE-2024-26788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26788)

    * [CVE-2024-26790](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26790)

    * [CVE-2024-26795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26795)

    * [CVE-2024-26808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26808)

    * [CVE-2024-26809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26809)

    * [CVE-2024-26814](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26814)

    * [CVE-2024-26833](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26833)

    * [CVE-2024-26835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26835)

    * [CVE-2024-26848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26848)

    * [CVE-2024-26855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26855)

    * [CVE-2024-26861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26861)

    * [CVE-2024-26862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26862)

    * [CVE-2024-26870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26870)

    * [CVE-2024-26877](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26877)

    * [CVE-2024-26885](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26885)

    * [CVE-2024-26891](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26891)

    * [CVE-2024-26895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26895)

    * [CVE-2024-26897](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26897)

    * [CVE-2024-26900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26900)

    * [CVE-2024-26924](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26924)

    * [CVE-2024-26925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26925)

    * [CVE-2024-26926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26926)

    * [CVE-2024-26935](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26935)

    * [CVE-2024-26937](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26937)

    * [CVE-2024-26950](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26950)

    * [CVE-2024-26951](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26951)

    * [CVE-2024-26970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26970)

    * [CVE-2024-26978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26978)

    * [CVE-2024-26988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26988)

    * [CVE-2024-27030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27030)

    * [CVE-2024-27038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27038)

    * [CVE-2024-27044](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27044)

    * [CVE-2024-27045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27045)

    * [CVE-2024-27047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27047)

    * [CVE-2024-27052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27052)

    * [CVE-2024-27053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27053)

    * [CVE-2024-27065](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27065)

    * [CVE-2024-27076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27076)

    * [CVE-2024-27414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27414)

    * [CVE-2024-27417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27417)

    * [CVE-2024-27431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27431)

    * [CVE-2024-35785](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35785)

    * [CVE-2024-35796](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35796)

    * [CVE-2024-35813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35813)

    * [CVE-2024-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35829)

    * [CVE-2024-35833](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35833)

    * [CVE-2024-35845](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35845)

    * [CVE-2024-35848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35848)

    * [CVE-2024-35852](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35852)

    * [CVE-2024-35853](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35853)

    * [CVE-2024-35854](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35854)

    * [CVE-2024-35855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35855)

    * [CVE-2024-35879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35879)

    * [CVE-2024-35884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35884)

    * [CVE-2024-35895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35895)

    * [CVE-2024-35897](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35897)

    * [CVE-2024-35899](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35899)

    * [CVE-2024-35900](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35900)

    * [CVE-2024-35905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35905)

    * [CVE-2024-35958](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35958)

    * [CVE-2024-35962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35962)

    * [CVE-2024-35983](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35983)

    * [CVE-2024-35988](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35988)

    * [CVE-2024-35990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35990)

    * [CVE-2024-35996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35996)

    * [CVE-2024-36005](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36005)

    * [CVE-2024-36006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36006)

    * [CVE-2024-36007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36007)

    * [CVE-2024-36008](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36008)

    * [CVE-2024-36031](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36031)

    * [CVE-2024-36889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36889)

    * [CVE-2024-36929](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36929)

    * [CVE-2024-36957](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36957)




Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

## May 28, 2024

Announcement

### Release 1.16.9

Google Distributed Cloud for bare metal 1.16.9 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade). Google Distributed Cloud for bare metal 1.16.9 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud software.

Security

### Security bulletin (all minor versions)

A new vulnerability ([CVE-2024-4323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4323)) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected.

Google Distributed Cloud software doesn't use a vulnerable version of Fluent Bit and is unaffected.

For more information, see the [GCP-2024-031](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-031) security bulletin.

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.9: 

  * High-severity container vulnerabilities:

    * [CVE-2023-39323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39323)

    * [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-39318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39318)

    * [CVE-2023-39319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39319)

    * [CVE-2024-2961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2961)

    * [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)

    * [CVE-2024-28085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28085)

  * Low-severity container vulnerabilities:

    * [CVE-2023-5363](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5363)

    * [CVE-2023-6246](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6246)

    * [CVE-2023-6779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6779)

    * [CVE-2023-6780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6780)




Issue

**Known issues:**

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/known-issues) in the Troubleshooting section.

## April 25, 2024

Announcement

### Release 1.16.8

GKE on Bare Metal 1.16.8 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.8 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.8: 

  * Critical container vulnerabilities:

    * [CVE-2021-38297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38297)

    * [CVE-2022-23806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23806)

    * [CVE-2023-24538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24538)

    * [CVE-2023-24540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24540)

    * [CVE-2023-29402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29402)

    * [CVE-2023-29404](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29404)

    * [CVE-2023-29405](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29405)

  * High-severity container vulnerabilities:

    * [CVE-2020-29652](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29652)

    * [CVE-2021-29923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29923)

    * [CVE-2021-33195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33195)

    * [CVE-2021-33196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33196)

    * [CVE-2021-33198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33198)

    * [CVE-2021-39293](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39293)

    * [CVE-2021-41771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41771)

    * [CVE-2021-41772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41772)

    * [CVE-2021-44716](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44716)

    * [CVE-2022-2879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2879)

    * [CVE-2022-2880](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2880)

    * [CVE-2022-21698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21698)

    * [CVE-2022-23772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23772)

    * [CVE-2022-23773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23773)

    * [CVE-2022-24675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24675)

    * [CVE-2022-24921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24921)

    * [CVE-2022-28131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28131)

    * [CVE-2022-28327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28327)

    * [CVE-2022-30580](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30580)

    * [CVE-2022-30630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30630)

    * [CVE-2022-30631](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30631)

    * [CVE-2022-30632](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30632)

    * [CVE-2022-30633](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30633)

    * [CVE-2022-30635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30635)

    * [CVE-2022-32189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32189)

    * [CVE-2022-41715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41715)

    * [CVE-2022-41724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41724)

    * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)

    * [CVE-2023-6040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6040)

    * [CVE-2023-6356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6356)

    * [CVE-2023-6536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6536)

    * [CVE-2023-6606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6606)

    * [CVE-2023-24534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24534)

    * [CVE-2023-24536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24536)

    * [CVE-2023-24537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24537)

    * [CVE-2023-24539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24539)

    * [CVE-2023-29400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29400)

    * [CVE-2023-29403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29403)

    * [CVE-2023-45287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45287)

    * [CVE-2023-46838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46838)

    * [CVE-2023-52436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52436)

    * [CVE-2023-52439](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52439)

    * [CVE-2023-52444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52444)

    * [CVE-2023-52445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52445)

    * [CVE-2023-52451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52451)

    * [CVE-2023-52464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52464)

    * [CVE-2023-52469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52469)

    * [CVE-2024-1086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1086)

    * [CVE-2024-26586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26586)

    * [CVE-2024-26597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26597)

    * [CVE-2024-26598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26598)

  * Medium-severity container vulnerabilities:

    * [CVE-2020-29509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29509)

    * [CVE-2020-29511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29511)

    * [CVE-2021-33197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33197)

    * [CVE-2021-34558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34558)

    * [CVE-2021-36221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36221)

    * [CVE-2022-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1705)

    * [CVE-2022-1962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1962)

    * [CVE-2022-32148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32148)

    * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)

    * [CVE-2023-6915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6915)

    * [CVE-2023-24532](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24532)

    * [CVE-2023-29406](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29406)

    * [CVE-2023-29409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29409)

    * [CVE-2023-39198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39198)

    * [CVE-2023-52443](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52443)

    * [CVE-2023-52449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52449)

    * [CVE-2023-52470](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52470)

  * Low-severity container vulnerabilities:

    * [CVE-2022-30629](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30629)

    * [CVE-2023-52438](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52438)

    * [CVE-2023-52448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52448)

    * [CVE-2023-52454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52454)

    * [CVE-2023-52456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52456)

    * [CVE-2023-52457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52457)

    * [CVE-2023-52462](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52462)

    * [CVE-2023-52463](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52463)

    * [CVE-2023-52467](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52467)

    * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)

    * [CVE-2024-24860](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24860)




Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## April 08, 2024

Announcement

### Release 1.16.7

GKE on Bare Metal 1.16.7 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.7 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Fixed

**Fixes:**

  * Fixed an issue with configuring a proxy for your cluster that required you to manually set `HTTPS_PROXY` and `NO_PROXY` environment variables on the admin workstation.



Fixed

The following container image security vulnerabilities have been fixed in 1.16.7: 

  * High-severity container vulnerabilities:

    * [CVE-2022-28948](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28948)

    * [CVE-2023-29499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29499)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-6004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6004)

    * [CVE-2023-6918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6918)

    * [CVE-2023-32611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32611)

    * [CVE-2023-32665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32665)

    * [CVE-2023-46218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46218)

    * [CVE-2023-49290](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49290)

    * [CVE-2024-21664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21664)

    * [GHSA-2c7c-3mj9-8fqh](https://github.com/advisories/GHSA-2c7c-3mj9-8fqh)

  * Low-severity container vulnerabilities:

    * [CVE-2021-25743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25743)



Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## April 03, 2024

Security

A Denial-of-Service (DoS) vulnerability ([CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. For more information, see the [GCP-2024-022 security bulletin](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-022).

## February 20, 2024

Feature

### Release 1.16.6

GKE on Bare Metal 1.16.6 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.6 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Fixed

**Fixes:**

  * Fixed an issue where upgrades are blocked because `cluster-operator` can't delete stale, failing preflight check resources.

  * Cleaned up stale `etcd-events` membership to enhance control plane initialization reliability in the event of a node join failure.




Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.6: 

  * High-severity container vulnerabilities:

    * [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626)
  * Medium-severity container vulnerabilities:

    * [CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)

    * [CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)

  * Low-severity container vulnerabilities:

    * [CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)

    * [CVE-2023-4527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4527)

    * [CVE-2023-4911](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4911)




Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## January 31, 2024

Security

### Security bulletin (all minor versions)

A security vulnerability, [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626), has been discovered in `runc` where a user with permission to create Pods might be able to gain full access to the node filesystem.

For instructions and more details, see the [GCP-2024-005](https://cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-005) security bulletin.

## January 30, 2024

Feature

### Release 1.16.5

GKE on Bare Metal 1.16.5 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.5 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.5: 

  * Critical container vulnerabilities:

    * [CVE-2023-25775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25775)
  * High-severity container vulnerabilities:

    * [CVE-2021-3121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3121)

    * [CVE-2021-41617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41617)

    * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)

    * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

    * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)

    * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)

    * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)

    * [CVE-2023-0464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464)

    * [CVE-2023-5717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5717)

    * [CVE-2023-5869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5869)

    * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)

    * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)

    * [CVE-2023-27533](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27533)

    * [CVE-2023-29491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491)

    * [CVE-2023-35827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35827)

    * [CVE-2023-39417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39417)

    * [CVE-2023-51780](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51780)

    * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)

    * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)

  * Medium-severity container vulnerabilities:

    * [CVE-2020-8565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8565)

    * [CVE-2021-44879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44879)

    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)

    * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)

    * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)

    * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

    * [CVE-2023-0465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465)

    * [CVE-2023-0466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466)

    * [CVE-2023-2650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650)

    * [CVE-2023-5868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5868)

    * [CVE-2023-5870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5870)

    * [CVE-2023-6121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6121)

    * [CVE-2023-25165](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25165)

    * [CVE-2023-27535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27535)

    * [CVE-2023-27536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536)

    * [CVE-2023-27538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27538)

    * [CVE-2023-28321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321)

    * [CVE-2023-34324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34324)

    * [CVE-2023-36054](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36054)

    * [CVE-2023-45863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45863)

    * [CVE-2023-46343](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46343)

    * [CVE-2023-51385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51385)

    * [CVE-2024-0584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0584)

  * Low-severity container vulnerabilities:

    * [CVE-2023-5178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5178)

    * [CVE-2023-5197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5197)

    * [CVE-2023-6531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6531)

    * [CVE-2023-6817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6817)

    * [CVE-2023-27534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27534)

    * [CVE-2023-28322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28322)

    * [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)

    * [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)

    * [CVE-2023-46813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46813)

    * [CVE-2023-46862](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46862)

    * [CVE-2024-0193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0193)

    * [CVE-2024-0641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0641)




Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## December 15, 2023

Feature

### Release 1.16.4

GKE on Bare Metal 1.16.4 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.4 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Change

**Functionality changes:**

  * Changed upgrade preflight checks behavior to skip kubeadm job creation check to improve upgrade reliability.



Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.4: 

  * Medium-severity container vulnerabilities:

    * [CVE-2021-3507](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3507)

    * [CVE-2021-3930](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3930)

    * [CVE-2021-20196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20196)

    * [CVE-2022-0216](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0216)

    * [CVE-2023-0330](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0330)

    * [CVE-2023-3180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3180)

    * [CVE-2023-34969](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34969)

    * [CVE-2023-41913](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41913)

    * [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq)

  * Low-severity container vulnerabilities:

    * [CVE-2017-16516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-16516)

    * [CVE-2020-14394](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14394)

    * [CVE-2021-20203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20203)

    * [CVE-2022-24795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24795)

    * [CVE-2023-1544](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1544)

    * [CVE-2023-3301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3301)

    * [CVE-2023-3354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3354)

    * [CVE-2023-33460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33460)




Fixed

**Fixes:**

  * Fixed an issue where the network check ConfigMap wasn't being updated when nodes were added or removed.

  * Fixed an issue where excessive `stackdriver-operator` reconciliations resulted in high CPU usage.




Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## November 28, 2023

Feature

### Release 1.16.3

GKE on Bare Metal 1.16.3 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). GKE on Bare Metal 1.16.3 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Change

**Functionality changes:**

  * Increased the certificate time to live (TTL) for `metrics-providers-ca` and `stackdriver-prometheus-scrape` for third-party monitoring.



Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

Fixed

**Fixes:**

  * Fixed an issue where `CoreDNS` Pods can get stuck in an unready state.

  * Fixed an issue that caused application metrics to be unavailable in Anthos clusters on bare metal versions 1.16.0 and 1.16.1.




Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.3: 

  * Critical container vulnerabilities:

    * [CVE-2023-38408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38408)

    * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)

  * High-severity container vulnerabilities:

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-4244](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4244)

    * [CVE-2023-4622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4622)

    * [CVE-2023-4623](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4623)

    * [CVE-2023-4921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4921)

    * [CVE-2023-42753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42753)

  * Medium-severity container vulnerabilities:

    * [CVE-2023-3772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3772)

    * [CVE-2023-37453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-37453)

    * [CVE-2023-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39189)

    * [CVE-2023-39192](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39192)

    * [CVE-2023-39193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39193)

    * [CVE-2023-39194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39194)

    * [CVE-2023-42754](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42754)

    * [CVE-2023-42755](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42755)

  * Low-severity container vulnerabilities:

    * [CVE-2023-3773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3773)

    * [CVE-2023-6176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6176)

    * [CVE-2023-42756](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42756)




Issue

**Known issues:**

For information about the latest known issues, see [GKE on Bare Metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## October 30, 2023

Feature

### Release 1.16.2

Anthos clusters on bare metal 1.16.2 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). Anthos clusters on bare metal 1.16.2 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Change

**Functionality changes:**

  * Increased the certificate time to live (TTL) for `metrics-providers-ca` and `stackdriver-prometheus-scrape` for third-party monitoring.

  * Removed hardcoded timeout value for the `bmctl backup` operation.




Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

Fixed

**Fixes:**

  * Fixed the `spec.featureGates.annotationBasedApplicationMetrics` feature gate in the stackdriver custom resource to enable collection of annotation-based workload metrics. This function is broken in Anthos clusters on bare metal versions 1.16.0 and 1.16.1.

  * Fixed a memory leak in Dataplane V2.

  * Fixed an issue where garbage collection deleted Source Network Address Translation (SNAT) entries for long-lived egress NAT connections, causing connection resets.

  * Fixed an issue that caused file and directory permissions to be set incorrectly after backing up and restoring a cluster.

  * Added direct dependencies on systemd, containerd, and kubelet over their mount point folders in `/var/lib/`.

  * Fixed an issue where etcd blocked upgrades due to an incorrect initial-cluster-state.

  * Fixed an issue that blocked upgrades to version 1.16 for clusters that have secure computing mode (`seccomp`) disabled.




Fixed

The following container image security vulnerabilities have been fixed in release 1.16.2: 

  * High-severity container vulnerabilities:

    * [CVE-2019-11253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253)

    * [CVE-2020-7919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7919)

    * [CVE-2020-8558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8558)

    * [CVE-2020-9283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9283)

    * [CVE-2021-25741](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25741)

    * [CVE-2021-27918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-27918)

    * [CVE-2022-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39189)

    * [CVE-2022-41721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41721)

    * [CVE-2023-1380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1380)

    * [CVE-2023-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2007)

    * [CVE-2023-2124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2124)

    * [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)

    * [CVE-2023-3111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3111)

    * [CVE-2023-3268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3268)

    * [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)

    * [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)

    * [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)

    * [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)

    * [CVE-2023-4128](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4128)

    * [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4206)

    * [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4207)

    * [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4208)

    * [CVE-2023-21255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21255)

    * [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840)

    * [CVE-2023-34319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34319)

    * [CVE-2023-35001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35001)

    * [CVE-2023-35788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35788)

    * [CVE-2023-40283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40283)

    * [GHSA-74fp-r6jw-h4mp](https://github.com/advisories/GHSA-74fp-r6jw-h4mp)

  * Medium-severity container vulnerabilities:

    * [CVE-2019-11250](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11250)

    * [CVE-2019-11251](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11251)

    * [CVE-2019-11254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254)

    * [CVE-2020-8554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8554)

    * [CVE-2020-8555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)

    * [CVE-2020-8561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8561)

    * [CVE-2020-8564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8564)

    * [CVE-2020-8911](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8911)

    * [CVE-2020-14040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14040)

    * [CVE-2020-21047](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-21047)

    * [CVE-2021-3114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3114)

    * [CVE-2021-25735](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25735)

    * [CVE-2022-2582](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2582)

    * [CVE-2022-4269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4269)

    * [CVE-2022-40982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40982)

    * [CVE-2022-46146](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-46146)

    * [CVE-2023-1206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1206)

    * [CVE-2023-2002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2002)

    * [CVE-2023-2269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2269)

    * [CVE-2023-3212](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3212)

    * [CVE-2023-3338](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3338)

    * [CVE-2023-3863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3863)

    * [CVE-2023-4132](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4132)

    * [CVE-2023-4194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4194)

    * [CVE-2023-4273](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4273)

    * [CVE-2023-20569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20569)

    * [CVE-2023-20593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20593)

    * [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841)

    * [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842)

    * [CVE-2023-31084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31084)

    * [CVE-2023-40577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40577)

    * [CVE-2023-41333](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41333)

    * [GHSA-2w8w-qhg4-f78j](https://github.com/advisories/GHSA-2w8w-qhg4-f78j)

    * [GHSA-76wf-9vgp-pj7w](https://github.com/advisories/GHSA-76wf-9vgp-pj7w)

    * [GHSA-rm8v-mxj3-5rmq](https://github.com/advisories/GHSA-rm8v-mxj3-5rmq)

  * Low-severity container vulnerabilities:

    * [CVE-2020-8562](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8562)

    * [CVE-2020-8912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8912)

    * [CVE-2021-25740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-25740)

    * [CVE-2021-32292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32292)

    * [CVE-2022-45886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45886)

    * [CVE-2022-45887](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45887)

    * [CVE-2022-45919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45919)

    * [CVE-2022-48554](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48554)

    * [CVE-2023-2156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2156)

    * [CVE-2023-2898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2898)

    * [CVE-2023-3141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3141)

    * [CVE-2023-3389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3389)

    * [CVE-2023-3610](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3610)

    * [CVE-2023-3777](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3777)

    * [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)

    * [CVE-2023-4147](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4147)

    * [CVE-2023-21400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21400)

    * [CVE-2023-31248](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31248)

    * [CVE-2023-34242](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34242)

    * [CVE-2023-34256](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34256)

    * [CVE-2023-35823](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35823)

    * [CVE-2023-35824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35824)

    * [CVE-2023-35828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35828)

    * [CVE-2023-35829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35829)

    * [CVE-2023-41332](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-41332)

    * [GHSA-qq97-vm5h-rrhg](https://github.com/advisories/GHSA-qq97-vm5h-rrhg)




Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## September 21, 2023

Feature

### Release 1.16.1

Anthos clusters on bare metal 1.16.1 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). Anthos clusters on bare metal 1.16 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

Fixed

**Fixes:**

  * Fixed an issue where etcd blocked upgrades due to an incorrect initial-cluster-state.

  * Fixed an issue that blocked upgrades to version 1.16 for clusters that have secure computing mode (`seccomp`) disabled.

  * Fixed an issue to prevent cluster upgrades from starting on a node before either all Pods have been drained or the Pod draining timeout has been reached.

  * Fixed an issue where the memory resource requests value wasn't set properly for `etcd-events`.




Change

**Functionality changes:**

  * Added the optional `userClaim` field to the ClientConfig custom resource definition bundled with Anthos clusters on bare metal. This change improves support for Azure AD integrations with Anthos Identity Service.

  * Updated constraint on NodePool `spec.upgradeStrategy.concurrentNodes` to be the smaller of either 15 nodes or 50% of the size of the node pool.




Fixed

**Fixes:**

The following container image security vulnerabilities have been fixed in 1.16.1: 

  * Critical container vulnerabilities:

    * [CVE-2022-1996](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1996)
  * High-severity container vulnerabilities:

    * [CVE-2017-11468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-11468)

    * [CVE-2019-13509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13509)

    * [CVE-2020-16845](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-16845)

    * [CVE-2020-28362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28362)

    * [CVE-2020-28366](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28366)

    * [CVE-2020-28367](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28367)

    * [CVE-2021-20206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20206)

    * [CVE-2023-27561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27561)

    * [CVE-2023-29002](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29002)

  * Medium-severity container vulnerabilities:

    * [CVE-2015-3627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3627)

    * [CVE-2019-19794](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19794)

    * [CVE-2020-8569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8569)

    * [CVE-2020-14039](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14039)

    * [CVE-2020-15586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15586)

    * [CVE-2020-24553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-24553)

    * [CVE-2020-29510](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29510)

    * [CVE-2021-20329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20329)

    * [CVE-2023-27593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27593)

    * [CVE-2023-27594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27594)

    * [CVE-2023-27595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27595)

    * [CVE-2023-30851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30851)




Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

## August 25, 2023

Feature

### Release 1.16.0

Anthos clusters on bare metal 1.16.0 is now available for [download](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). To upgrade, see [Upgrading Anthos on bare metal](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). Anthos clusters on bare metal 1.16.0 runs on Kubernetes 1.27.

If you use a third-party storage vendor, check the [GDCV Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of GKE on Bare Metal.

Announcement

**Version 1.13 end of life:** In accordance with the [Anthos Version Support Policy](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support), version 1.13 (all patch releases) of Anthos clusters on bare metal has reached its end of life and is no longer supported.

Red Hat Enterprise Linux (RHEL) 8 minor versions 8.2, 8.3, 8.4, and 8.5 have reached their [end of life](https://access.redhat.com/support/policy/updates/errata). Please ensure you're using a supported version of your operating system.

Feature

**Cluster lifecycle:**

  * Upgraded to Kubernetes version 1.27.4.

  * Added support for Red Hat Enterprise Linux (RHEL) version 8.8.

  * **GA:** Added support for [parallel upgrades of worker node pools](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#cw-strategy).

  * **GA:** Added support to [upgrade specific worker node pools separately from the rest of the cluster](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up).

  * **GA:** Added a [separate instance of etcd](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/limits#etcd_performance) for the `etcd-events` object. This new etcd instance is always on and requires [ports 2382 and 2383 to be open on control plane nodes](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/network-reqs#control_plane_nodes) for inbound TCP traffic. If these ports aren't opened, cluster creation and cluster upgrades are blocked.

  * **GA:** Updated preflight checks for cluster installation and upgrades to use changes from the latest Anthos clusters on bare metal patch version to address known issues and provide more useful checks.

  * **GA:** Support enrolling admin and user clusters in the Anthos On-Prem API automatically to enable cluster lifecycle management from the Google Cloud CLI, the Google Cloud console, and Terraform when the Anthos On-Prem API is enabled. If needed, you have the option to disable enrollment. For more information, see the description for the [`gkeOnPremAPI`](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#gkeonpremapi) field in the cluster configuration file.

  * **GA:** Added ability to configure kubelet image pull settings for node pools. For more information, see [Configure kubelet image pull settings](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-clusters#kubelet-config).

  * Added new health check to detect any unsupported drift in the custom resources managed by Anthos clusters on bare metal. Unsupported resource changes can lead to cluster problems.

  * Added a new flag, `--target-cluster-name`, that is supported by the `bmctl register bootstrap` command.




**Networking:**

  * **GA:** Added support for Services of type LoadBalancer to use `externalTrafficPolicy=Local` with [bundled load balancing with BGP](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/lb-bundled-bgp).

  * **Preview:** Added support for enabling Direct Server Return (DSR) load balancing for clusters configured with flat-mode networking. DSR load balancing is enabled with an annotation, `preview.baremetal.cluster.gke.io/dpv2-lbmode-dsr: enable`.

  * **Preview:** Upgraded wherabouts to v0.6.1-gke.1 to support dual-stack networking.

  * Added support for multiple BGP load balancer (`BGPLoadBalancer`) resources and BGP Community. Multiple BGP load balancer resources provide more flexibility to define which peers advertise specific load balancer nodes and Services. BGP Community support helps you to distinguish routes coming from BGP load balancers from other routes in your network.




**Observability:**

**Important:** As part of the following change, many metrics have shifted monitored resource types from Kubernetes Container ([`k8s_container`](https://cloud.google.com/monitoring/api/resources#tag_k8s_container)) to Prometheus Target ([`prometheus_target`](https://cloud.google.com/monitoring/api/resources#tag_prometheus_target)). In some cases, this resource change can cause existing dashboards to stop working properly until they are adjusted to use the metrics for the `prometheus_target` resource.

  * **GA:** Added [support for system metrics](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/log-monitoring#using-managed-service-for-prometheus) when you use Google Cloud Managed Service for Prometheus.



**Security and Identity:**

  * **GA:** Added support for Binary Authorization, a service on Google Cloud that provides software supply-chain security for container-based applications. For more information, see [Set up Binary Authorization policy enforcement](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/binary-authorization-policy).

  * **GA:** Added support for [VPC Service Controls](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/hardening-your-cluster#vpc-sc), which provides additional security for your clusters to help mitigate the risk of data exfiltration.

  * **Preview:** Added support for [using custom cluster certificate authorities (CAs)](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/custom-cluster-ca) to enable secure authentication and encryption between cluster components.

  * **Preview:** Added support for configuring the Subject Alternative Names (SANs) of the kubeadm generated certificate for the kube-apiserver.

  * Added support to run keepalived as a non-root user.




Change

**Supported node pool versions:**

If you use [selective worker node pool upgrades](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade#select_np_up) to upgrade a cluster to version 1.16.4, see [Node pool versioning rules](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#supported_nodepool_versions) for a list of the versions that are supported for the worker node pools.

Change

**Functionality changes:**

  * Updated constraint on NodePool `spec.upgradeStrategy.concurrentNodes` to be the smaller of 15 nodes or 50% of the size of the node pool.

  * Replaced legacy method of enabling application logging in the cluster configuration file with two fields, `enableCloudLoggingForApplications` and `enableGMPForApplications`, in the stackdriver custom resource.

The `spec.clusterOperations.enableApplication` field in the cluster configuration file has no effect on version 1.16.0 and higher clusters. This field populated the `enableStackdriverForApplications` field in the stackdriver custom resource, which enabled annotation based workload metric collection. If you need this capability, use the `annotationBasedApplicationMetrics` feature gate in the stackdriver custom resource as shown in the following sample to keep the same behavior:
        
        kind:stackdriver
        spec:
          enableCloudLoggingForApplications: true
          featureGates:
             annotationBasedApplicationMetrics: true
        

**Caution:** The annotation-based workload metrics collection enabled by the `annotationBasedApplicationMetrics` feature gate collects metrics for objects that have the `prometheus.io/scrape` annotation. Many software systems with open source origin may use this annotation. Be aware of this dependency so that you aren't surprised by metrics charges in Cloud Monitoring.
  * Added optional `ksmNodePodMetricsOnly` feature gate in the stackdriver custom resource to reduce the number of metrics from kube-state-metrics. Reducing the number of metrics makes monitoring pipeline more stable in large scale clusters.

  * Audit logs are compressed on the wire for Cloud Audit Logs consumption, reducing egress bandwidth by approximately 60%.

  * Upgraded local volume provisioner to v2.5.0.

  * Upgraded snapshot controller to v5.0.1.

  * Deprecated v1beta1 volume snapshot custom resources. Anthos clusters on bare metal will stop serving v1beta1 resources in a future release.

  * Removed resource request limits on edge profile workloads.

  * Added preflight check to make sure control plane and load balancer nodes aren't under maintenance before an upgrade.

  * Updated the cluster snapshot capability so that information can be captured for the target cluster even when the cluster custom resource is missing or unavailable.

  * Improved `bmctl` error reporting for failures during the creation of a bootstrap cluster.

  * Added support for using the `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds` cluster annotation to specify the maximum node draining duration, in seconds. By default, a 20-minute (1200 seconds) timeout is enforced. When the timeout elapses, all pods are stopped and the node is put into maintenance mode. For example to change the timeout to 10 minutes, add the annotation `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds: "600"` to your cluster.

  * Updated `bmctl check cluster` to create a HealthCheck custom resource in the admin cluster if it's healthy.




Fixed

The following container image security vulnerabilities have been fixed: 

  * Critical container vulnerabilities:

    * [CVE-2022-29155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29155)

    * [CVE-2022-29458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29458)

    * [CVE-2023-0464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0464)

    * [CVE-2023-0465](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0465)

    * [CVE-2023-0466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0466)

    * [CVE-2023-2283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2283)

    * [CVE-2023-2650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2650)

  * High-severity container vulnerabilities:

    * [CVE-2019-19906](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19906)

    * [CVE-2020-8032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8032)

    * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)

    * [CVE-2022-4904](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4904)

    * [CVE-2022-24407](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24407)

    * [CVE-2022-29154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29154)

    * [CVE-2022-32190](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32190)

    * [CVE-2023-0045](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0045)

    * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)

    * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)

    * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)

    * [CVE-2023-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0386)

    * [CVE-2023-0461](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0461)

    * [CVE-2023-1077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1077)

    * [CVE-2023-1078](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1078)

    * [CVE-2023-1118](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1118)

    * [CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281)

    * [CVE-2023-1670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1670)

    * [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)

    * [CVE-2023-1989](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1989)

    * [CVE-2023-2454](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2454)

    * [CVE-2023-3567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3567)

    * [CVE-2023-23559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23559)

    * [CVE-2023-28466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28466)

    * [CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)

    * [CVE-2023-32233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32233)

  * Medium-severity container vulnerabilities:

    * [CVE-2018-1099](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1099)

    * [CVE-2019-9511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9511)

    * [CVE-2019-9513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9513)

    * [CVE-2020-11080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11080)

    * [CVE-2020-13844](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13844)

    * [CVE-2021-3468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3468)

    * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)

    * [CVE-2022-3707](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3707)

    * [CVE-2022-3821](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3821)

    * [CVE-2022-4129](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4129)

    * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)

    * [CVE-2022-4382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4382)

    * [CVE-2022-4415](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4415)

    * [CVE-2022-23524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23524)

    * [CVE-2022-23525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23525)

    * [CVE-2022-23526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23526)

    * [CVE-2022-36055](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-36055)

    * [CVE-2023-0458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0458)

    * [CVE-2023-0459](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0459)

    * [CVE-2023-1073](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1073)

    * [CVE-2023-1074](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1074)

    * [CVE-2023-1076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1076)

    * [CVE-2023-1079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1079)

    * [CVE-2023-1667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1667)

    * [CVE-2023-1855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1855)

    * [CVE-2023-1859](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1859)

    * [CVE-2023-1990](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1990)

    * [CVE-2023-1998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1998)

    * [CVE-2023-2162](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2162)

    * [CVE-2023-2194](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2194)

    * [CVE-2023-2455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2455)

    * [CVE-2023-2985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2985)

    * [CVE-2023-3161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3161)

    * [CVE-2023-3220](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3220)

    * [CVE-2023-3358](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3358)

    * [CVE-2023-23916](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23916)

    * [CVE-2023-26545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26545)

    * [CVE-2023-28328](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28328)

    * [CVE-2023-28484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28484)

    * [CVE-2023-29469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29469)

    * [CVE-2023-30456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30456)

    * [CVE-2023-32269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32269)

    * [CVE-2023-33203](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33203)

    * [CVE-2023-33288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33288)

  * Low-severity container vulnerabilities:

    * [CVE-2009-5155](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-5155)

    * [CVE-2015-8985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-8985)

    * [CVE-2019-17594](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17594)

    * [CVE-2019-17595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17595)

    * [CVE-2021-3468](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3468)

    * [CVE-2022-2196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2196)

    * [CVE-2022-3424](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3424)

    * [CVE-2022-4379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4379)

    * [CVE-2023-1513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1513)

    * [CVE-2023-1611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1611)

    * [CVE-2023-1872](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1872)

    * [CVE-2023-2163](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2163)

    * [CVE-2023-21102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21102)

    * [CVE-2023-22998](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22998)

    * [CVE-2023-23004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23004)

    * [CVE-2023-25012](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25012)

    * [CVE-2023-30772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-30772)




Fixed

**Fixes:**

  * Fixed an issue where the apiserver could become unresponsive during a cluster upgrade for clusters with a single control plane node.

  * Fixed an issue where cluster installations or upgrades fail when the cluster name has more than 45 characters.

  * Fixed an issue where the control plane VIP wasn't reachable during cluster installation on Red Hat Enterprise Linux.

  * Fixed an issue where audit logs were duplicated into the offline buffer even when they are sent to Cloud Audit Logs successfully.

  * Fixed an issue where node-specific labels set on the node pool were sometimes overwritten.

  * Updated [`avoidBuggyIPs`](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#loadbalancer-addresspools-avoidbuggyips) and [`manualAssign`](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#loadbalancer-addresspools-manualassign) fields in load balancer address pools (`spec.loadBalancers.addressPools`) to allow changes at any time.

  * Fixed an issue where containerd didn't restart when there was a version mismatch. This issue caused an inconsistent containerd version within the cluster. 

  * Fixed an issue that caused the logging agent to use continuously increasing amounts of memory.

  * Fixed preflight check so that it no longer ignores the `no_proxy` setting. 

  * Fixed Anthos Identity Service annotation needed for exporting metrics. 

  * Fixed an issue that caused the `bmctl restore` command to stop responding for clusters with manually configured load balancers.

  * Fixed an issue that prevented Anthos clusters on bare metal from restoring a high-availability quorum for nodes that use `/var/lib/etcd` as a mountpoint. 

  * Fixed an issue that caused health checks to report failure when they find a Pod with a status of `TaintToleration` even when the replicaset for the Pod has sufficient Pods running.

  * Fixed an issue that caused conflicts with third-party Ansible automation. 

  * Fixed a cluster upgrade issue that prevented some control plane nodes from rejoining a cluster configured for high availability.




Issue

**Known issues:**

For information about the latest known issues, see [Anthos clusters on bare metal known issues](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) in the Troubleshooting section.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
