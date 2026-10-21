---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade/
title: Upgrade Google Distributed Cloud \u00a0|\u00a0 Anthos on bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:44.759624+00:00
---

# Upgrade Google Distributed Cloud  |  Anthos on bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade/

**Version 1.9**. This version is no longer supported. For information about how to upgrade to version 1.10, see [ Upgrading Anthos on bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.10/how-to/upgrade) in the 1.10 documentation. For more information about supported and unsupported versions, see the [Version history](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on bare metal 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/concepts/about-bare-metal)



Send feedback 

#  Upgrade Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 (unsupported)keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/getting-support#version-support)



When you install a new version of `bmctl`, you can upgrade your existing clusters that were created with an earlier version. Upgrading a cluster to the latest Google Distributed Cloud version brings added features and fixes to your cluster. It also ensures that your cluster remains [supported](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/getting-support#version-support). You can upgrade admin, hybrid, standalone, or user clusters with the `bmctl upgrade cluster` command.

**Note:** When upgrading Google Distributed Cloud from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version available to ensure you have the latest security patches. Always review the release notes before upgrading so you are aware of what has changed, including security fixes and known issues. Upgrading to a lower patch version is not supported.

## Enable SELinux

If you want to enable SELinux to secure your containers, you must make sure that SELinux is enabled in `Enforced` mode on all your host machines. Starting with Google Distributed Cloud release 1.9.0 or later, you can enable or disable SELinux before or after cluster creation or cluster upgrades. SELinux is enabled by default on Red Hat Enterprise Linux (RHEL) and CentOS. If SELinux is disabled on your host machines or you aren't sure, see [Securing your containers using SELinux](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/installing/configure-selinux) for instructions on how to enable it.

Google Distributed Cloud supports SELinux in only RHEL and CentOS systems.

## Before you upgrade

Preflight checks are run before a cluster upgrade to validate cluster status and node health.

The following examples show the upgrade process from version 1.8.2 to Google Distributed Cloud 1.9.8.

You can upgrade any given version to the next available version (for example, 1.9.0 to 1.9.1) in the same fashion. Skip upgrades, such as 1.8.1 to 1.9.8, are also supported.

Google Distributed Cloud supports the configuration of up to 250 maximum pods per node. This configuration can only be done during cluster creation and cannot be updated for existing clusters.

## Upgrade admin, standalone, hybrid, or user clusters

When you download and install a new version of `bmctl`, you can upgrade your admin, hybrid, standalone, and user clusters created with an earlier version. For a given version of `bmctl`, clusters can be upgraded to the same version only.

First, you download the latest `bmctl`, then modify the appropriate cluster config files, and then you issue the `bmctl upgrade cluster` command to complete the upgrade.

**Note:** You should upgrade an admin cluster before upgrading any associated user clusters. However, before upgrading the admin cluster to 1.9.8, make sure its associated user clusters are at version 1.8.0 or above. `bmctl` will emit an error if it finds any user cluster is below 1.8.0.

  1. Download the latest `bmctl` from the [Cloud Storage](https://docs.cloud.google.com/storage) bucket and use `chmod` to give `bmctl` execute permissions to all users:
         
         gcloud storage cp gs://anthos-baremetal-release/bmctl/1.9.8/linux-amd64/bmctl bmctl
         chmod a+x bmctl
         

  2. Modify the cluster config file to change the Google Distributed Cloud cluster version from `1.8.2` to `1.9.8`. The following shows an example from an admin cluster config:
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: cluster1
           namespace: cluster-cluster1
         spec:
           # Cluster type. This can be:
           #   1) admin:  to create an admin cluster. This can later be used to create user clusters.
           #   2) user:   to create a user cluster. Requires an existing admin cluster.
           #   3) hybrid: to create a hybrid cluster that runs admin cluster components and user workloads.
           #   4) standalone: to create a cluster that manages itself, runs user workloads, but does not manage other clusters.
           type: admin
           # Anthos cluster version.
           # Change the following line from 1.8.2 to 1.9.8, shown below
           anthosBareMetalVersion: 1.9.8
         

  3. When upgrading clusters to 1.9.8, you must register the clusters with Connect to your project [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets), if they have not been already.

     1. Manually create service accounts and retrieve the JSON key files as described in [Configuring service accounts for use with Connect](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/installing/configure-sa#connect-sa) on the Enabling Google services and service accounts page.
     2. Reference the downloaded JSON keys in the associated `gkeConnectAgentServiceAccountKeyPath` and `gkeConnectRegisterServiceAccountKeyPath` fields of the cluster config file.
  4. Use the `bmctl upgrade cluster` command to complete the upgrade:
         
         bmctl upgrade cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * CLUSTER_NAME: the name of the cluster to upgrade.
     * ADMIN_KUBECONFIG: the path to the admin cluster kubeconfig file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
