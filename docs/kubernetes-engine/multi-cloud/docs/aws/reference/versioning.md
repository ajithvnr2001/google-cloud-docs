---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/versioning/
title: Versioning \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:23.057249+00:00
---

# Versioning  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/versioning/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/apis)



Send feedback 

#  Versioning Stay organized with collections  Save and categorize content based on your preferences. 

This page explains GKE on AWS versioning.

## GKE on AWS versions

Each release of GKE on AWS supports several Kubernetes minor versions, each of which can have several GKE patch versions. The following GKE on AWS versions are fully supported, offering the latest patches and updates for security vulnerabilities, exposures, and issues affecting GKE on AWS:

Minor version | Patch releases  
---|---  
[1.35](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-versions#kubernetes_1.35) | 

  * 1.35.3-gke.300

  
[1.34](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-versions#kubernetes_1.34) | 

  * 1.34.6-gke.200
  * 1.34.1-gke.4700

  
[1.33](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-versions#kubernetes_1.33) | 

  * 1.33.10-gke.200
  * 1.33.5-gke.1900
  * 1.33.4-gke.900

  
  
### Properties of unsupported versions

Versions not listed in the preceding table are unsupported. After a minor version reaches its end of life, the following rules apply:

  * End-of-life patch versions can't be used to [create clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster).
  * End-of-life events don't disrupt your control planes and workloads. Regular operations on existing clusters can continue with end-of-life versions. To ensure support from Google and avoid potential bug-related failures or security vulnerabilities, you must manually upgrade your [clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/upgrade-cluster) and [node pools](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool) to a supported version as soon as possible.
  * Upgrades of existing clusters and node pools to newer versions can occur even if the upgraded version is at end of life. However, you must eventually upgrade to one of the supported versions.
  * New node pools can still be created with an end-of-life version, but this isn't recommended. Upgrades to a supported version should be prioritized.



### Check available Kubernetes versions

To see all available versions, including those which have reached their end of life and are unsupported, run this command:
    
    
    gcloud container aws get-server-config \
        --location=GOOGLE_CLOUD_LOCATION
    

Replace `GOOGLE_CLOUD_LOCATION` with the Google Cloud location from which you manage your clusters.

The supported versions are returned with their `enabled` flag set to `true`. Any end of life patch versions are returned in the output with their `end_of_life` flag set to `true`.

## Versioning scheme

GKE on AWS uses Kubernetes [semantic versioning](https://semver.org/) to refer to supported Kubernetes versions, but appends a GKE patch version. This results in a version number of the form: `x.y.z-gke.a`

For example, the most recently-supported Kubernetes version is 1.35.3-gke.300.

Kubernetes major version (x)
    Major versions are typically incremented if any backwards incompatible changes are introduced to the public API. A major version increments the Kubernetes version from `x.y` to `x+1.y`.
Kubernetes minor version (y)
    Kubernetes releases a new minor version [three times a year](https://github.com/kubernetes/kubernetes/releases). Each release cycle is approximately 15 weeks long. [Deprecated APIs](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) might be removed with a new minor version. A minor version increments the Kubernetes version from `1.y` to `1.y+1`; for example, Kubernetes 1. **29** is the minor release that follows Kubernetes 1.**28**.
Kubernetes patch release (z)
    New Kubernetes patch releases (such as 1.21.1) for use with GKE on AWS are normally released once a month. Patch releases only include security and bug fixes.
GKE patch release (-gke.a)
    A patch release with a higher -gke.a suffix (such as 1.24.1-gke.a) includes security updates and bug fixes for GKE on AWS alongside the open source upstream Kubernetes software. These updates or fixes are required for compatibility and interoperability with Google Cloud and AWS.

## Version notes

Each GKE on AWS release comes with Kubernetes version notes. These are similar to release notes but are specific to a Kubernetes version and might offer more technical detail. These version notes are listed on the [GKE on AWS version notes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-versions) page.

## Version skew

Nodes and node pool versions can be up to two minor versions older than the control plane, but, in accordance with [Kubernetes OSS version skew policy](https://kubernetes.io/docs/setup/release/version-skew-policy/), cannot be newer than the control plane version. We strongly recommend that your nodes always use a supported version regardless of version skew guidelines.

## Support for versions

To learn more about the support period, see the [GKE Version Support Policy](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/getting-support#version_support_policy), which GKE on AWS follows.

## What's next

  * [Update and upgrade a user cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
