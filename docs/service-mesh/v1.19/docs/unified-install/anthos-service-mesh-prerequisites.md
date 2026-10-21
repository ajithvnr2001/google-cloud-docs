---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/anthos-service-mesh-prerequisites/
title: Cloud Service Mesh prerequisites \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:51.584830+00:00
---

# Cloud Service Mesh prerequisites  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/anthos-service-mesh-prerequisites/

You are viewing archived v1.19 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh prerequisites

This page describes the prerequisites and the requirements for installing Cloud Service Mesh, such as GKE Enterprise licensing, cluster requirements, fleet requirements, and general requirements.

## Cloud project

Before you begin:

  * [Select or create a Google Cloud project](https://console.cloud.google.com/projectselector2).

  * [Verify that billing is enabled](https://cloud.google.com/billing/docs/how-to/modify-project) for your project.




## GKE Enterprise licensing

### GKE

Cloud Service Mesh is available with GKE Enterprise or as a standalone service. Google APIs are used to determine how you are billed. To use Cloud Service Mesh as a standalone service, don't enable the GKE Enterprise API in your project. The `asmcli` enables all of the other required Google APIs for you. For information about Cloud Service Mesh pricing, see [Pricing](https://docs.cloud.google.com/service-mesh/v1.19/pricing).

  * GKE Enterprise subscribers, be sure to enable the GKE Enterprise API.



[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=anthos.googleapis.com)

  * If you aren't an GKE Enterprise subscriber, you can still install Cloud Service Mesh, but certain UI elements and features in Google Cloud console are only available to GKE Enterprise subscribers. For information about what is available to subscribers and non-subscribers, see [GKE Enterprise and Cloud Service Mesh UI differences](https://docs.cloud.google.com/service-mesh/v1.19/docs/ui-differences).

  * If you enabled the GKE Enterprise API, but you want to use Cloud Service Mesh as a standalone service, [disable the GKE Enterprise API](https://docs.cloud.google.com/service-usage/docs/enable-disable).




### Outside Google Cloud

To install Cloud Service Mesh on-premises, on GKE on AWS, on Amazon EKS, or on Microsoft AKS, you have to be an GKE Enterprise customer. GKE Enterprise customers are not billed separately for Cloud Service Mesh because it is already included in the GKE Enterprise pricing. For more information, see the [GKE Enterprise Pricing guide](https://cloud.google.com/anthos/pricing).

## General requirements

  * To be included in the service mesh, service ports must be named, and the name must include the port's protocol in the following syntax: `name: protocol[-suffix]` where the square brackets indicate an optional suffix that must start with a dash. For more information, see [Naming service ports](https://docs.cloud.google.com/service-mesh/v1.19/docs/naming-service-ports).

  * If you have created a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) in your organization, you might need to add the Cloud Service Mesh certificate authority service to the perimeter. See [Adding Cloud Service Mesh certificate authority to a service perimeter](https://docs.cloud.google.com/service-mesh/v1.19/docs/set-service-perimeter) for more information.

  * If you want to change the default [resource limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) for the `istio-proxy` sidecar container, the new values must be greater than the default values to [avoid out-of-memory (OOM) events](https://docs.cloud.google.com/service-mesh/v1.19/docs/troubleshooting/troubleshoot-sidecar-proxies).

  * A Google Cloud project can only have one mesh associated with it. 




## Cluster requirements

### GKE

  * Verify that your cluster version is listed in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-platforms).

  * Your GKE cluster must meet the following requirements:

    * The GKE cluster must be Standard. Autopilot clusters are only supported with [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh).

    * A machine type that has at least 4 vCPUs, such as `e2-standard-4`. If the machine type for your cluster doesn't have at least 4 vCPUs, change the machine type as described in [Migrating workloads to different machine types](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool).

    * The minimum number of nodes depends on your machine type. Cloud Service Mesh requires at least 8 vCPUs. If the machine type has 4 vCPUs, your cluster must have at least 2 nodes. If the machine type has 8 vCPUs, the cluster only needs 1 node. If you need to add nodes, see [Resizing a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster).

  * GKE Workload Identity is required. We recommend that you enable [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) before installing Cloud Service Mesh. Enabling Workload Identity changes the way calls from your workloads to Google APIs are secured, as described in [Workload Identity limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#limitations). Note that you do not need to enable the [GKE Metadata Server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#metadata_server) on [existing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to).

  * Optional but recommended, enroll the cluster in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). We recommend that you enroll in the Regular release channel because other channels might be based on a GKE version that isn't supported with Cloud Service Mesh 1.19.10. For more information, see [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-platforms). Follow the instructions in [Enrolling an existing cluster in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#enrolling_an_existing_cluster_in_a_release_channel) if you have a static GKE version.

  * If you are installing Cloud Service Mesh on a private cluster, you must open port 15017 in the firewall to get the webhooks used for [automatic sidecar injection](https://docs.cloud.google.com/service-mesh/v1.19/docs/anthos-service-mesh-proxy-injection) and configuration validation to work. For more information, see [Opening a port on a private cluster](https://docs.cloud.google.com/service-mesh/v1.19/docs/private-cluster-open-port).

  * Ensure that the client machine that you install Cloud Service Mesh from has network connectivity to the API server.

  * For Windows Server workloads, Cloud Service Mesh is not supported. If your cluster has both Linux and Windows Server node pools, you can still install Cloud Service Mesh and use it on your Linux workloads.



  * After provisioning Cloud Service Mesh, you must [contact support](https://docs.cloud.google.com/service-mesh/v1.19/docs/getting-support) before initiating [IP rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation) or [certificate credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation).



### Outside Google Cloud

  * Ensure that the user cluster that you install Cloud Service Mesh on has at least 4 vCPUs, 15 GB memory, and 4 nodes.

  * Verify that your cluster version is listed in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-platforms).

  * Ensure that the client machine that you install Cloud Service Mesh from has network connectivity to the API server.

  * If you are deploying sidecars in application pods where direct connectivity to CA services (such as `meshca.googleapis.com` and `privateca.googleapis.com`) is not available, you must [configure an explicit `CONNECT`-based HTTPS proxy](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/options/configure-ca-through-proxy).

  * For public clusters with egress firewall rules set that are blocking [implied rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules), ensure you have configured HTTP/HTTPS and DNS rules to reach public Google APIs.




## Fleet requirements

With Cloud Service Mesh 1.11 and later, all clusters must be registered to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets), and [fleet workload identity](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity) must be enabled. You can either [setup up the clusters](https://docs.cloud.google.com/anthos/multicluster-management/fleets/workload-identity#cluster_setup) yourself, or you can let `asmcli` register the clusters as long as they meet the following requirements:

**Caution:** All Cloud Service Mesh clusters for one mesh must be registered to the same fleet at all times to use Cloud Service Mesh. Other clusters in the project of a Cloud Service Mesh cluster must not be registered to a different fleet. 

  * **GKE** : _(applies to in-cluster and managed Cloud Service Mesh)_ [Enable GKE Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on your Google Kubernetes Engine cluster, if it is not already enabled. Additionally, you must [register the cluster using fleet Workload Identity](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation).

  * **GKE clusters outside Google Cloud** : _(applies to in-cluster Cloud Service Mesh)_ [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem), [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal), [GKE on AWS](https://docs.cloud.google.com/anthos/clusters/docs/aws), and [GKE on Azure](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/azure) are automatically registered to your project fleet at cluster creation time. As of GKE Enterprise 1.8, all these cluster types automatically enable fleet Workload Identity when registered. Existing registered clusters are updated to use fleet Workload Identity when they are upgraded to GKE Enterprise 1.8.

  * **Amazon EKS clusters** : _(applies to in-cluster Cloud Service Mesh)_ The cluster must have a public IAM OIDC Identity Provider. Follow the instructions in [Create an IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html) to check if a provider exists, and create a provider if necessary.




When you run `asmcli install`, you specify the project ID of the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). `asmcli` registers the cluster if it isn't already registered.

**Note:** If you have not registered a cluster from a project to a fleet hosted in a different project before, there are extra steps required to configure fleet permissions. For detailed instructions, see [Grant permissions for registering a cluster into a different project](https://docs.cloud.google.com/anthos/multicluster-management/connect/prerequisites#gke-cross-project).

## What's next?

  * [Plan a new installation](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/plan-install)
  * [Plan an upgrade](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/plan-upgrade)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
