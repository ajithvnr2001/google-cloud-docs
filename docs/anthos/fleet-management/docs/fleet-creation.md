---
url: https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation/
title: Fleet creation overview \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:26.286945+00:00
---

# Fleet creation overview  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Fleet creation overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of how fleet creation works, with details for different cluster types. For more information about how to manually register clusters to your fleet and the prerequisites for manual registration, see our detailed fleet creation guides.

You can create a fleet in one of the following ways:

  * **By registering a cluster** : When you register a cluster of any type in a project that doesn't already have a fleet, a new fleet is created and the project becomes a [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project). At most, a project can have a single fleet. Depending on the cluster type and where it lives, registration can happen automatically at cluster creation time with registration details specified in the cluster configuration, or you might need to manually add the cluster to your fleet.
  * **By creating a named fleet** : You can [create an empty fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#optional_create_an_empty_fleet) before you register clusters to it.



Each fleet has a name that is displayed in the Google Cloud console. By default, this is the project ID of the fleet host project with `fleet` appended. If you want a more descriptive name for your fleet, you can specify it when creating a fleet.

**Note:** Registering a cluster to a Fleet does not incur any additional charges.

## About fleet membership

Once you register a cluster to a fleet, it becomes a fleet member. Because fleets can include clusters from multiple projects and environments, you must ensure that each cluster you add to your fleet has a unique name. This is sometimes referred to in commands and documentation as the cluster's _fleet membership name_. Typically, a cluster's fleet membership name is its regular cluster name, but you may need to create a new name at registration time (for example by appending or prepending a qualifier to the original cluster name) if another cluster with that name already exists in the fleet. If you attempt to register a cluster with an existing name to your fleet, registration will fail.

### Fleet membership location

Each fleet cluster's membership is managed by the Fleet service. The location of this service can be _global_ or _regional_ , depending on how the cluster is registered to the fleet.

  * GKE clusters on Google Cloud [registered by using the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#gcloud) have their membership managed by a Fleet service instance that runs in the same region as the cluster itself. This provides optimal latency for building your own high availability services, including using regional instances of some services such as the Connect gateway. Regional membership management also supports situations where, for example, you have data that cannot leave a specific region for regulatory reasons. You cannot choose to have a cluster managed from a different region.

  * GKE clusters on Google Cloud [registered by using Config Connector](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#config-connector) can be managed by either a global or regional Fleet service.

  * All other fleet members are managed using a global Fleet service.


**Note:** All clusters registered before January 2023 have memberships managed by the global Fleet service.

You cannot change a cluster's membership location while it is still a fleet member. If you have a GKE cluster with global fleet membership and want to change it to be managed from its region, you must unregister the cluster and then register it again to the same fleet using `gcloud` or Config Connector.

To check a cluster's membership location (for example, to use as a command parameter or if you are considering switching a cluster to regional membership), do one of the following:

  * List all your fleet members. Each cluster's membership location is shown in the `LOCATION` column of the output.
        
        gcloud container fleet memberships list \
           --project=PROJECT_ID
        

  * Run the following command to `describe` your cluster's membership, including its membership location. Replace MEMBERSHIP_NAME with your cluster's membership name.
        
        gcloud container fleet memberships describe MEMBERSHIP_NAME \
           --project=PROJECT_ID
        




### Team scopes

A fleet member cluster can be associated with one or more team scopes within its fleet. [Team scopes](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management#fleet_team_management_overview) are an enterprise fleet-level construct for associating subsets of fleet clusters with specific application teams, and can be used to enable a range of team-based features, including access control, team-scoped observability, and [sequencing cluster upgrade rollouts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing).

## GKE clusters on Google Cloud

[GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) clusters on Google Cloud must be explicitly registered to add them to a fleet. To register existing clusters, you can choose between quick registration from the Clusters page in the Google Cloud console, registration from the command line with the gcloud CLI, or declarative registration using Terraform or Config Connector. You can also register new clusters during cluster creation using the Google Cloud console, gcloud CLI, or Terraform. Find out more about these options in [Register a cluster on Google Cloud to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster).

Clusters on Google Cloud can be registered to a fleet in their current project or ([with some extra permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#gke-cross-project)) to a fleet in a different project.

### Lightweight memberships

GKE clusters on Google Cloud support lightweight memberships, which let you register the cluster as a fleet member without enabling all of the fleet-level configurations and features. 

Clusters that use a lightweight membership can [use fleet-based rollout sequencing for cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing)

Lightweight memberships prevent clusters from using the following fleet-level configurations:

  * [Fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features)
  * [Fleet-level default logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#default-logs-enterprise)
  * [Fleet-level default metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#default-metrics-enterprise)
  * [Fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/about-fleet-workload-identity-federation)



## Clusters outside Google Cloud

You can add clusters outside Google Cloud to your fleet and view and manage your clusters across different environments together. GKE clusters outside Google Cloud are mostly registered to your fleet automatically at cluster creation time, as described in the rest of this section. If you want to add third-party Kubernetes clusters to your fleet, you must register them manually.

Registering clusters outside Google Cloud installs the Connect Agent on the cluster to handle communication between the cluster and your Google Cloud project. You can read more about how the Connect Agent works in the [Connect Agent overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent).

### Google Distributed Cloud (on-premises)

On-premises GKE clusters [on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem) and [on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal) are automatically registered to your chosen fleet at cluster creation time, with your fleet host project and other registration details specified in the relevant cluster configuration file. If you are using Google Distributed Cloud on VMware, note that from version 1.13 onwards, both [admin clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-admin-cluster) and [user clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-user-cluster) _must_ be registered. For versions prior to 1.13, you can optionally add registration details to [admin cluster configurations](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/admin-cluster-configuration-file#gkeconnect-section) if you want to manage them as part of your fleet. You can register unregistered admin clusters by updating their cluster configuration file and using `gkectl` to [update the cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/updating-general). On-premises GKE clusters cannot be unregistered or (with the exception of unregistered admin clusters) manually registered.

### GKE on other public clouds

GKE clusters on AWS and Azure created using the [GKE Multi-Cloud API](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud) are automatically registered to your chosen fleet at cluster creation time, with your fleet host project specified when you run the relevant `gcloud cluster create` command. Because clusters created using GKE Multi-Cloud already have a project associated with them (the project where the API is enabled), you need to [do some additional setup](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/how-to/create-cluster#cross-project_registration) at cluster creation if you want to register them to a fleet in a different project. Clusters created with the GKE Multi-Cloud API cannot be unregistered or manually registered.

### Third-party Kubernetes clusters (attached clusters)

If you have existing third-party Kubernetes clusters (such as EKS, AKS, or on-premises distributions) that you want to manage as fleet members, you can register these to your project fleet along with any GKE clusters. You can attach any [conformant Kubernetes cluster](https://www.cncf.io/certification/software-conformance/) that includes x86 nodes to your fleet using the GKE Multi-Cloud API. These include Amazon EKS, Azure AKS, and other CNCF-conformant clusters that meet our requirements. Any third-party clusters you register will incur a per-vCPU charge as part of your [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).

To register an attached cluster, see the following guides:

  * [Attach your EKS cluster](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/eks/how-to/attach-cluster).
  * [Attach your AKS cluster](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/aks/how-to/attach-cluster).
  * For all other cluster types, follow the instructions to [attach CNCF-conformant clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/generic/how-to/attach-cluster), paying attention to the [cluster prerequisites](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/generic/reference/cluster-prerequisites).



## Move a cluster to a different fleet

Moving registered clusters between fleets (unregistering then reregistering) is not currently recommended, as it can result in unexpected or unwanted behavior: for example, your workloads' fleet Workload Identity will change, potentially resulting in blocked requests and outages. The recommended approach is to create a new cluster in the fleet in which you want your workloads to reside, then move your workloads from your old cluster to the new cluster.

## (Optional) Create an empty fleet

By default, a new fleet is created in your fleet host project the first time you register a cluster in that project. If you want to create a new named fleet before you register any clusters (for example, to [set up scopes for team access](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management)), run the following command:
    
    
    gcloud container fleet create --display-name=NAME [--project=FLEET_HOST_PROJECT_ID]
    

If you don't specify a `display-name`, the new fleet has a default display name based on its fleet host project name.

## View your fleets

If your organization has multiple fleets, you can view and navigate between them in the Google Cloud console. To view fleets across projects within your organization you need the [`roles/gkehub.viewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.viewer) role at the minimum. To learn more, see the [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) and [how to grant them](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

###  All fleets 

To view all fleets:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/overview/fleet-overview)

  2. At the top of the GKE navigation menu, click **All fleets**. A list of all fleets in the organization displays.




You can click on a fleet name to see the [clusters registered to that fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#view_registered_clusters). Selecting a fleet in this list automatically switches you to its fleet host project in the Google Cloud console.

###  Fleet drop-down list 

To view selected fleets from a drop-down list:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/overview/fleet-overview)

  2. At the top of the navigation menu, click the **Fleet** drop-down list that shows the fleets across projects.

  3. Select a fleet name which opens the [fleet dashboard](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard). Selecting a fleet in this list automatically switches you to its fleet host project in the Google Cloud console.




You can click **View all clusters** on the dashboard to see the [clusters registered to that fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#view_registered_clusters).

## What's next?

  * [Plan fleet resources](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets): Before you create your first fleet, read this document for practical guidance on organizing clusters into fleets, including best practices and limitations.

  * [Before you begin](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin) for all cluster types.

  * Register a GKE cluster on Google Cloud:

    * [Prerequisites for clusters on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke)
    * [Register a cluster on Google Cloud to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
