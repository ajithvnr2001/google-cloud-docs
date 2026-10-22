---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/hardening-your-cluster/
title: Harden your cluster security \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:30.727301+00:00
---

# Harden your cluster security  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/hardening-your-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Harden your cluster security Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to harden the security of your clusters created with Distributed Cloud software only for bare metal.

## Secure your containers using SELinux

You can secure your containers by enabling SELinux, which is supported for Red Hat Enterprise Linux (RHEL). If your host machines are running RHEL and you want to enable SELinux for your cluster, you must enable SELinux in all of your host machines. See [secure your containers using SELinux](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux) for details.

## Use `seccomp` to restrict containers

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Secure computing mode (`seccomp`) is available in version 1.11 and higher of Google Distributed Cloud. Running containers with a `seccomp` profile improves the security of your cluster because it restricts the system calls that containers are allowed to make to the kernel. This reduces the chance of kernel vulnerabilities being exploited.

The default `seccomp` profile contains a list of system calls that a container is allowed to make. Any system calls not on the list are disallowed. `seccomp` is enabled by default in version 1.11 and higher clusters. This means that all system containers and customer workloads are run with the container runtime's default `seccomp` profile. Even containers and workloads that don't specify a `seccomp` profile in their configuration files are subject to `seccomp` restrictions.

### How to disable `seccomp` cluster-wide or on particular workloads

You can disable `seccomp` during cluster creation or cluster upgrade only. `bmctl update` can't be used to disable this feature. If you want to disable `seccomp` within a cluster, add the following `clusterSecurity` section to the cluster's configuration file:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: example
      namespace: cluster-example
    spec:
    ...**  clusterSecurity:
        enableSeccomp: false**
    ...
    

In the unlikely event that some of your workloads need to execute system calls that `seccomp` blocks by default, you don't have to disable `seccomp` on the whole cluster. Instead, you can single out particular workloads to run in `unconfined mode`. Running a workload in `unconfined mode` frees that workload from the restrictions that the `seccomp` profile imposes on the rest of the cluster.

To run a container in `unconfined mode`, add the following `securityContext` section to the Pod manifest:
    
    
    apiVersion: v1
    kind: Pod
    ....
    spec:**  securityContext:
        seccompProfile:
          type: Unconfined**
    ....
    

## Don't run containers as `root` user

By default, processes in containers execute as `root`. This poses a potential security problem, because if a process breaks out of the container, that process runs as `root` on the host machine. It's therefore advisable to run all your workloads as a non-root user.

The following sections describe two ways of running containers as a non-root user.

### Method #1: add `USER` instruction in `Dockerfile`

This method uses a `Dockerfile` to ensure that containers don't run as a `root` user. In a `Dockerfile`, you can specify which user the process inside a container should be run as. The following snippet from a `Dockerfile` shows how to do this:
    
    
    ....
    
    #Add a user with userid 8877 and name nonroot
    RUN useradd −u 8877 nonroot
    
    #Run Container as nonroot
    USER nonroot
    ....
    

In this example, the Linux command `useradd -u` creates a user called `nonroot` inside the container. This user has a user ID (UID) of `8877`.

The next line in the `Dockerfile` runs the command `USER nonroot`. This command specifies that from this point on in the image, commands are run as the user `nonroot`.

Grant permissions to UID `8877` so that the container processes can execute properly for `nonroot`.

### Method #2: add securityContext fields in Kubernetes manifest file

This method uses a Kubernetes manifest file to ensure that containers don't run as a `root` user. Security settings are specified for a Pod, and those security settings are in turn applied to all containers within the Pod.

The following example shows an excerpt of a manifest file for a given Pod:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: name-of-pod
    spec:
      securityContext:
        runAsUser: 8877
        runAsGroup: 8877
    ....
    

The `runAsUser` field specifies that for any containers in the Pod, all processes run with user ID `8877`. The `runAsGroup` field specifies that these processes have a primary group ID (GID) of `8877`. Remember to grant the necessary and sufficient permissions to UID `8877` so that the container processes can execute properly.

This ensures that processes within a container are run as UID `8877`, which has fewer privileges than root.

System containers in Distributed Cloud software only help install and manage clusters. The UIDs and GIDs used by these containers can be controlled by the field [`startUIDRangeRootlessContainers`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clustersecurity-startuidrangerootlesscontainers) in the cluster specification. The `startUIDRangeRootlessContainers` is an optional field which, if not specified, has a value of `2000`. Allowed values for `startUIDRangeRootlessContainers` are `1000`-`57000`. The `startUIDRangeRootlessContainers` value can be changed during upgrades only. The system containers use the UIDs and GIDs in the range `startUIDRangeRootlessContainers` to `startUIDRangeRootlessContainers` \+ 2999.

The following example shows an excerpt of a manifest file for a Cluster resource:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: name-of-cluster
    spec:
     clusterSecurity:
        startUIDRangeRootlessContainers: 5000
    ...
    

Choose the value for `startUIDRangeRootlessContainers` so that the UID and GID spaces used by the system containers don't overlap with those assigned to user workloads.

### How to disable rootless mode

Starting with Google Distributed Cloud release 1.10, Kubernetes control plane containers and system containers run as non-root users by default. Google Distributed Cloud assigns these users UIDs and GIDs in the range `2000`-`4999`. However, this assignment can cause problems if those UIDs and GIDs have already been allocated to processes running inside your environment.

Starting with release 1.11, you can disable rootless mode when you upgrade your cluster. When rootless mode is disabled, Kubernetes control plane containers and system containers run as the root user.

To disable rootless mode, perform the following steps:

  1. Add the following `clusterSecurity` section to the cluster's configuration file:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: example
           namespace: cluster-example
         spec:
         ...**  clusterSecurity:
             enableRootlessContainers: false**
         ...
         

  2. Upgrade your cluster. For details, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).




## Restrict the ability for workloads to self-modify

Certain Kubernetes workloads, especially system workloads, have permission to self-modify. For example, some workloads vertically autoscale themselves. While convenient, this can allow an attacker who has already compromised a node to escalate further in the cluster. For example, an attacker could have a workload on the node change itself to run as a more privileged service account that exists in the same namespace.

Ideally, workloads shouldn't be granted the permission to modify themselves in the first place. When self-modification is necessary, you can limit permissions by applying Gatekeeper or Policy Controller constraints, such as [NoUpdateServiceAccount](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/noupdateserviceaccount) from the open source Gatekeeper library, which provides several useful security policies.

When you deploy policies, it's usually necessary to allow the controllers that manage the cluster lifecycle to bypass the policies. This is necessary so that the controllers can make changes to the cluster, such as applying cluster upgrades. For example, if you deploy the `NoUpdateServiceAccount` policy on your clusters, you must set the following parameters in the `Constraint`:
    
    
    parameters:
      allowedGroups:
      - system:masters
      allowedUsers: []
    

## Disable kubelet read-only port

Starting with release 1.15.0, Google Distributed Cloud disables by default port `10255`, the kubelet read-only port. Any customer workloads that are configured to read data from this insecure kubelet port `10255` should migrate to use the secure kubelet port 10250.

Only clusters created with version 1.15.0 or higher have this port disabled by default. The kubelet read-only port `10255` remains accessible for clusters created with a version lower than 1.15.0, even after a cluster upgrade to version 1.15.0 or higher.

This change was made because the kubelet leaks low sensitivity information over port `10255`, which is unauthenticated. The information includes the full configuration information for all Pods running on a Node, which can be valuable to an attacker. It also exposes metrics and status information, which can provide business-sensitive insights.

Disabling the kubelet read-only port is recommended by the CIS Kubernetes Benchmark.

## Maintenance

Monitoring security bulletins and upgrading your clusters are important security measures to take once your clusters are up and running.

### Monitor security bulletins

The GKE security team publishes [security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins) for high and critical severity vulnerabilities.

These bulletins follow a common Google Cloud vulnerability numbering scheme and are linked to from the main [Google Cloud bulletins page](https://docs.cloud.google.com/support/bulletins) and the [release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes).

[ Use this XML feed to subscribe to security bulletins for Google Kubernetes Engine (GKE) and related products. ![Subscribe](https://docs.cloud.google.com/static/docs/images/feed-icon.png)](https://cloud.google.com/feeds/gke-security-bulletins.xml)

When customer action is required to address these high and critical vulnerabilities, Google contacts customers by email. In addition, Google might also contact customers with support contracts through support channels.

For more information about how Google manages security vulnerabilities and patches for GKE, see [Security patching](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching).

### Upgrade clusters

Kubernetes regularly introduces new security features and provides security patches. Google Distributed Cloud releases incorporate Kubernetes security enhancements that address security vulnerabilities that may affect your clusters.

You are responsible for keeping your clusters up to date. For each release, review the [release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes). To minimize security risks to your clusters, plan to update to new patch releases every month and minor versions every four months.

One of the many advantages of upgrading a cluster is that it automatically refreshes the cluster kubeconfig file. The kubeconfig file authenticates a user to a cluster. The kubeconfig file is added to your cluster directory when you create a cluster with `bmctl`. The default name and path is `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`. When you upgrade a cluster, that cluster's kubeconfig file is automatically renewed. Otherwise, the kubeconfig file expires one year after it was created.

**Note:** Only the kubeconfig file for the cluster you are upgrading gets renewed. If, for example, you upgrade an admin cluster that manages three user clusters, only the admin cluster's kubeconfig file is refreshed. You must upgrade each of the user clusters separately to refresh their respective kubeconfig files.

For information about how to upgrade your clusters, see [upgrade your clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).

## Use VPC Service Controls with Cloud Interconnect or Cloud VPN

Cloud Interconnect provides low latency, high availability connections that let you transfer data reliably between your on-premises bare metal machines and Google Cloud [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/vpc). To learn more about Cloud Interconnect, see [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

Cloud VPN securely connects your _peer network_ to your Virtual Private Cloud (VPC) network through an [IPsec](https://wikipedia.org/wiki/IPsec) [VPN](https://wikipedia.org/wiki/Virtual_private_network) connection. To learn more about Cloud VPN, see [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

VPC Service Controls works with either Cloud Interconnect or Cloud VPN to provide additional security for your clusters. VPC Service Controls helps to mitigate the risk of data exfiltration. Using VPC Service Controls, you can add projects to service perimeters that protect resources and services from requests that originate outside the perimeter. To learn more about service perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

**Caution:** VPC Service Controls isn't compatible with the [cluster proxy configuration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/proxy#configure_proxy_details_in_the_cluster_configuration_file). If you choose to use VPC Service Controls, don't specify [`proxy`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#proxy) settings in the cluster spec.

To fully protect your clusters created with Google Distributed Cloud, you need to use Restricted VIP and add the following APIs to the service perimeter:

  * Artifact Registry API (`artifactregistry.googleapis.com`)
  * Resource Manager API (`cloudresourcemanager.googleapis.com`)
  * Compute Engine API (`compute.googleapis.com`)
  * Connect gateway API (`connectgateway.googleapis.com`)
  * Google Container Registry API (`containerregistry.googleapis.com`)
  * GKE Connect API (`gkeconnect.googleapis.com`)
  * GKE Hub API (`gkehub.googleapis.com`)
  * GKE On-Prem API (`gkeonprem.googleapis.com`)
  * Identity and Access Management (IAM) API (`iam.googleapis.com`)
  * Cloud Logging API (`logging.googleapis.com`)
  * Cloud Monitoring API (`monitoring.googleapis.com`)
  * Config Monitoring for Ops API (`opsconfigmonitoring.googleapis.com`)
  * Service Control API (`servicecontrol.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)

**Note:** You can't create or upgrade a cluster in the Google Cloud console when VPC Service Controls is enabled. The operation fails, because the `bmctl register bootstrap` command doesn't have the `--skip-api-check` flag. If you use VPC Service Controls, use `bmctl create cluster` to create clusters, or use `bmctl upgrade cluster` to upgrade clusters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
