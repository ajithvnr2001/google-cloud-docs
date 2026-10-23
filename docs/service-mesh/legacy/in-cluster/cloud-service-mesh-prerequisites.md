---
url: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/cloud-service-mesh-prerequisites/
title: In-cluster Cloud Service Mesh prerequisites \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:29.405981+00:00
---

# In-cluster Cloud Service Mesh prerequisites  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/cloud-service-mesh-prerequisites/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# In-cluster Cloud Service Mesh prerequisites

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

This page describes the prerequisites and the requirements for installing in-cluster Cloud Service Mesh on GKE, such as GKE Enterprise licensing, cluster requirements, fleet requirements, and general requirements.

## Cloud project

Before you begin:

  * [Select or create a Google Cloud project](https://console.cloud.google.com/projectselector2).

  * [Verify that billing is enabled](https://cloud.google.com/billing/docs/how-to/modify-project) for your project.




## GKE Enterprise licensing

Cloud Service Mesh is available with GKE Enterprise or as a standalone service. Google APIs are used to determine how you are billed. To use Cloud Service Mesh as a standalone service, don't enable the GKE Enterprise API in your project. The `asmcli` enables all of the other required Google APIs for you. For information about Cloud Service Mesh pricing, see [Pricing](https://cloud.google.com/service-mesh/pricing).

  * GKE Enterprise subscribers, be sure to enable the GKE Enterprise API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=anthos.googleapis.com)

  * If you aren't a GKE Enterprise subscriber, you can still install Cloud Service Mesh, but certain UI elements and features in Google Cloud console are only available to GKE Enterprise subscribers. For information about what is available to subscribers and non-subscribers, see [GKE Enterprise and Cloud Service Mesh UI differences](https://docs.cloud.google.com/service-mesh/docs/ui-differences).

  * If you enabled the GKE Enterprise API, but you want to use Cloud Service Mesh as a standalone service, [disable the GKE Enterprise API](https://docs.cloud.google.com/service-usage/docs/enable-disable).




## General requirements

  * To be included in the service mesh, service ports must be named, and the name must include the port's protocol in the following syntax: `name: protocol[-suffix]` where the square brackets indicate an optional suffix that must start with a dash. For more information, see [Naming service ports](https://docs.cloud.google.com/service-mesh/docs/naming-service-ports).

  * If you have created a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) in your organization, you might need to add the Cloud Service Mesh certificate authority service to the perimeter. See [Adding Cloud Service Mesh certificate authority to a service perimeter](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/set-service-perimeter) for more information.

  * If you want to change the default [resource limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) for the `istio-proxy` sidecar container, the new values must be greater than the default values to [avoid out-of-memory (OOM) events](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-sidecar-proxies).

  * A Google Cloud project can only have one mesh associated with it. 




## Cluster requirements

  * Verify that your cluster version is listed in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms).

  * Your GKE cluster must meet the following requirements:

    * The GKE cluster must be Standard. Autopilot clusters are only supported with [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh).

    * A machine type that has at least 4 vCPUs, such as `e2-standard-4`. If the machine type for your cluster doesn't have at least 4 vCPUs, change the machine type as described in [Migrating workloads to different machine types](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool).

    * The minimum number of nodes depends on your machine type. Cloud Service Mesh requires at least 8 vCPUs. If the machine type has 4 vCPUs, your cluster must have at least 2 nodes. If the machine type has 8 vCPUs, the cluster only needs 1 node. If you need to add nodes, see [Resizing a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).

  * GKE Workload Identity is required. We recommend that you enable [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) before installing Cloud Service Mesh. Enabling Workload Identity changes the way calls from your workloads to Google APIs are secured, as described in [Workload Identity limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#limitations). Note that you do not need to enable the [GKE Metadata Server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#metadata_server) on [existing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to).

  * Optional but recommended, enroll the cluster in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). We recommend that you enroll in the Regular release channel because other channels might be based on a GKE version that isn't supported with Cloud Service Mesh 1.31.1. For more information, see [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms). Follow the instructions in [Enrolling an existing cluster in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#enrolling_an_existing_cluster_in_a_release_channel) if you have a static GKE version.

  * If you are installing Cloud Service Mesh on a private cluster, you must open port 15017 in the firewall to get the webhooks used for [automatic sidecar injection](https://docs.cloud.google.com/service-mesh/docs/anthos-service-mesh-proxy-injection) and configuration validation to work. For more information, see [Opening a port on a private cluster](https://docs.cloud.google.com/service-mesh/docs/private-cluster-open-port).

  * Ensure that the client machine that you install Cloud Service Mesh from has network connectivity to the API server.

  * For Windows Server workloads, Cloud Service Mesh is not supported. If your cluster has both Linux and Windows Server node pools, you can still install Cloud Service Mesh and use it on your Linux workloads.

    * After provisioning Cloud Service Mesh, you must [contact support](https://docs.cloud.google.com/service-mesh/docs/getting-support) before initiating [IP rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation) or [certificate credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation).



## Fleet requirements

All clusters must be registered to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets), and [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity) must be enabled. You can either [setup up the clusters](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity#cluster_setup) yourself, or you can let `asmcli` register the clusters as long as they meet the following requirements:

**Caution:** All Cloud Service Mesh clusters for one mesh must be registered to the same fleet at all times to use Cloud Service Mesh. Other clusters in the project of a Cloud Service Mesh cluster must not be registered to a different fleet. 

  * **GKE** : _(applies to in-cluster and managed Cloud Service Mesh)_ [Enable GKE Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on your Google Kubernetes Engine cluster, if it is not already enabled. Additionally, you must [register the cluster using fleet Workload Identity](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation).



When you run `asmcli install`, you specify the project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). `asmcli` registers the cluster if it isn't already registered.

**Note:** If you have not registered a cluster from a project to a fleet hosted in a different project before, there are extra steps required to configure fleet permissions. For detailed instructions, see [Grant permissions for registering a cluster into a different project](https://docs.cloud.google.com/anthos/fleet-management/docs/before-you-begin#gke-cross-project).

## What's next?

  * [Plan a new installation](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/plan-install)
  * [Plan an upgrade](https://docs.cloud.google.com/service-mesh/docs/upgrade/plan-upgrade)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
