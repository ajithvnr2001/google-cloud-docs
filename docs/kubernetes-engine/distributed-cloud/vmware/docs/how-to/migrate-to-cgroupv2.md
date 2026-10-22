---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-to-cgroupv2/
title: Migrate to cgroup v2 \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:38.993781+00:00
---

# Migrate to cgroup v2  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-to-cgroupv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate to cgroup v2 Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud software-only on VMware version 1.35 requires cgroup v2. As of [version 1.35](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/), Kubernetes no longer supports cgroup v1. This document explains how to migrate your clusters to cgroup v2.

## Before you begin

To install or upgrade Google Distributed Cloud software-only on VMware with Kubernetes 1.35, check the following:

  * **Verify software version:** You must use Google Distributed Cloud software-only on VMware version 1.35.00 or later.
  * **OS cgroup v2 compatibility:** You must use an operating system that supports cgroup v2.
  * **Configure cgroup v2 (if required):** If your OS doesn't default to cgroup v2 (for example, Ubuntu 18.04/20.04), you must configure it manually. For more information, see [Migrating to cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/#migrating-cgroupv2) in the Kubernetes documentation.
  * **Update Cluster Configuration:** Change the `osImageType` field from `ubuntu`, `ubuntu_containerd`, or `cos` to either `ubuntu_cgv2` or `cos_cgv2` before upgrading to version 1.35.
  * **Prepare vSphere Images:** Run `gkectl prepare` if images are missing from vSphere.
  * **Update Automation Scripts:** Review and update any automation scripts to use the new `ubuntu_cgv2` or `cos_cgv2` image types.



## Update OS image type

Before you run `gkectl upgrade`, change the `osImageType` to a cgroup v2 compatible image in your cluster YAML file.

### Admin cluster

  1. Open your admin cluster configuration file.
  2. Locate the `osImageType` field.
  3. Change the value to `ubuntu_cgv2` (if you use Ubuntu) or `cos_cgv2` (if you use COS).



For more information about this field, see [documentation for `osImageType`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field).

### User cluster

  1. Open your user cluster configuration file.
  2. Locate the `osImageType` field within the `nodePools` section.
  3. Change the value to `ubuntu_cgv2` (if you use Ubuntu) or `cos_cgv2` (if you use COS).



For more information about this field, see [documentation for `nodePools[i].osImageType`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field).

## Upgrade your cluster

After updating the `osImageType` in your configuration file, upgrade your cluster.

  1. Run the following command to upgrade your cluster:
         
         gkectl upgrade cluster --config USER_CLUSTER_CONFIG --admin-config ADMIN_CLUSTER_CONFIG
         

Replace `USER_CLUSTER_CONFIG` with the path to your user cluster configuration file. Replace `ADMIN_CLUSTER_CONFIG` with the path to your admin cluster configuration file.




## Preflight checks

GKE on VMware 1.35 does not support the `ubuntu`, `ubuntu_containerd`, and `cos` OS image types. If you attempt to create or upgrade a cluster or node pool with these image types, the system blocks the request during preflight checks.

## New default OS image type

The default `osImageType` for GKE on VMware 1.35 is `ubuntu_cgv2`. If you create a new cluster configuration and leave the `osImageType` field blank, the system deploys nodes with cgroup v2 enabled by default.

If you prefer Container-Optimized OS (COS) over Ubuntu, explicitly set the `osImageType` field to `cos_cgv2` in your configuration file.

## What's next

  * Update the [Admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) `osImageType` field.
  * Update the [User cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field) `osImageType` field in node pools.
  * Learn more about [upgrading GKE on VMware clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
