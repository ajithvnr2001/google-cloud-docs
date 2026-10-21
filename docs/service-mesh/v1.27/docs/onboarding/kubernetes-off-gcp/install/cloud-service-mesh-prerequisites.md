---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/kubernetes-off-gcp/install/cloud-service-mesh-prerequisites/
title: In-cluster Cloud Service Mesh prerequisites \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:32.123607+00:00
---

# In-cluster Cloud Service Mesh prerequisites  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/kubernetes-off-gcp/install/cloud-service-mesh-prerequisites/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# In-cluster Cloud Service Mesh prerequisites

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).

This page describes the prerequisites and the requirements for installing in-cluster Cloud Service Mesh for Kubernetes workloads off Google Cloud, such as cluster requirements, fleet requirements, and general requirements.

## Cloud project

Before you begin:

  * [Select or create a Google Cloud project](https://console.cloud.google.com/projectselector2).

  * [Verify that billing is enabled](https://cloud.google.com/billing/docs/how-to/modify-project) for your project.




## General requirements

  * To be included in the service mesh, service ports must be named, and the name must include the port's protocol in the following syntax: `name: protocol[-suffix]` where the square brackets indicate an optional suffix that must start with a dash. For more information, see [Naming service ports](https://docs.cloud.google.com/service-mesh/v1.27/docs/naming-service-ports).

  * If you have created a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) in your organization, you might need to add the Cloud Service Mesh certificate authority service to the perimeter. See [Adding Cloud Service Mesh certificate authority to a service perimeter](https://docs.cloud.google.com/service-mesh/v1.27/docs/set-service-perimeter) for more information.

  * If you want to change the default [resource limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) for the `istio-proxy` sidecar container, the new values must be greater than the default values to [avoid out-of-memory (OOM) events](https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-sidecar-proxies).

  * A Google Cloud project can only have one mesh associated with it. 




## Cluster requirements

  * Ensure that the user cluster that you install Cloud Service Mesh on has at least 4 vCPUs, 15 GB memory, and 4 nodes.

  * Verify that your cluster version is listed in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.27/docs/supported-platforms).

  * Ensure that the client machine that you install Cloud Service Mesh from has network connectivity to the API server.

  * If you are deploying sidecars in application pods where direct connectivity to CA services (such as `meshca.googleapis.com` and `privateca.googleapis.com`) is not available, you must [configure an explicit `CONNECT`-based HTTPS proxy](https://docs.cloud.google.com/service-mesh/v1.27/docs/unified-install/options/configure-ca-through-proxy).

  * For public clusters with egress firewall rules set that are blocking [implied rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules), ensure you have configured HTTP/HTTPS and DNS rules to reach public Google APIs.




## Fleet requirements

All clusters must be registered to a [fleet](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview), and [fleet workload identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) must be enabled. You can either [setup up the clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity#cluster_setup) yourself, or you can let `asmcli` register the clusters as long as they meet the following requirements:

**Caution:** All Cloud Service Mesh clusters for one mesh must be registered to the same fleet at all times to use Cloud Service Mesh. Other clusters in the project of a Cloud Service Mesh cluster must not be registered to a different fleet. 

  * **GKE clusters outside Google Cloud** : _(applies to in-cluster Cloud Service Mesh)_ [Google Distributed Cloud (software only) for VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem), [Google Distributed Cloud (software only) for bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs), [GKE on AWS](https://docs.cloud.google.com/anthos/clusters/docs/aws) (deprecated), and [GKE on Azure](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/azure) (deprecated) are automatically registered to your project fleet at cluster creation time. As of GKE Enterprise 1.8, all these cluster types automatically enable fleet Workload Identity when registered. Existing registered clusters are updated to use fleet Workload Identity when they are upgraded to GKE Enterprise 1.8.
  * **Amazon EKS clusters** (deprecated): _(applies to in-cluster Cloud Service Mesh)_ The cluster must have a public IAM OIDC Identity Provider. Follow the instructions in [Create an IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html) to check if a provider exists, and create a provider if necessary.



When you run `asmcli install`, you specify the project ID of the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project). `asmcli` registers the cluster if it isn't already registered.

**Note:** If you have not registered a cluster from a project to a fleet hosted in a different project before, there are extra steps required to configure fleet permissions. For detailed instructions, see [Grant permissions for registering a cluster into a different project](https://docs.cloud.google.com/anthos/fleet-management/docs/before-you-begin#gke-cross-project).

Starting with `asmcli` version 1.25, all in-cluster Cloud Service Mesh installations and upgrades provision the Managed Canonical Service Controller. This requires the Cloud Service Mesh feature to be enabled on your fleet project. To allow `asmcli` to enable this feature automatically during installation or upgrade, you must run the `asmcli` command with the `--enable_gcp_components` flag.

## What's next?

  * [Plan a new installation](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/kubernetes-off-gcp/install/plan-install)
  * [Plan an upgrade](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/plan-upgrade)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
