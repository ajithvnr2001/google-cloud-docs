---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks/
title: Setting up multi-cluster Services with Shared VPC \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:09.935777+00:00
---

# Setting up multi-cluster Services with Shared VPC  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/msc-setup-with-shared-vpc-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Setting up multi-cluster Services with Shared VPC Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes common [Multi-cluster Services (MCS)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services) scenarios. The scenarios presented on this page share the following characteristics:

  * **Two GKE clusters** : The first GKE cluster is registered to its own project's [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). This is the _fleet host project_. The second GKE cluster is registered to the same fleet, though depending on the scenario may not be in the same project. Both GKE clusters are [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).
  * **Same VPC network** : Both GKE clusters use subnets in the same Shared VPC network.
  * **Workload Identity Federation for GKE** is enabled in both clusters.



## Terminology

The terms _Shared VPC host project_ and _GKE fleet host project_ have different meanings.

  * The Shared VPC host project is the project which contains the Shared VPC network.
  * The GKE fleet host project is the project that contains the [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) to which you register the clusters.



## Scenarios

The following table describes common MCS scenarios:

Scenario | Fleet host project (project containing the first cluster) | The location of the second cluster  
---|---|---  
Clusters in the same Shared VPC service project | A Shared VPC service project | The same Shared VPC service project as the first cluster  
Shared VPC host project as fleet host project (One cluster in the Shared VPC host project, a second cluster in a Shared VPC service project) | The Shared VPC host project | A Shared VPC service project  
Clusters in different Shared VPC service projects | A Shared VPC service project | A different Shared VPC service project  
  
## Prerequisites

Before setting up a cross-project configuration of MCS, ensure that you're familiar with:

  * [Shared VPC concepts](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * [Setting up clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc)
  * [MCS limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#limitations)
  * [MCS known issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#known_issues)



## Clusters in the same Shared VPC service project

This section provides an example MCS configuration involving two existing GKE clusters both in the same Shared VPC service project:

  * Both clusters use the same Shared VPC network in the `SHARED_VPC_HOST_PROJ`.
  * The first VPC-native GKE cluster `FIRST_CLUSTER_NAME`, with Workload Identity Federation for GKE enabled, is created in the `FLEET_HOST_PROJ`. The fleet host project is a service project connected to the `SHARED_VPC_HOST_PROJ` in this scenario.
  * The second VPC-native GKE cluster `SECOND_CLUSTER_NAME`, with Workload Identity Federation for GKE enabled, is also created in the `FLEET_HOST_PROJ`.



### Enable required APIs

Enable the required APIs. The output of the Google Cloud CLI shows you if an API has already been enabled.

  1. Enable the Cloud DNS API:
         
         gcloud services enable dns.googleapis.com \
             --project SHARED_VPC_HOST_PROJ
         

In this scenario, the fleet host project is a service project connected to the Shared VPC host project. The Cloud DNS API must be enabled in the Shared VPC host project because that's where the Shared VPC network is located. GKE creates Cloud DNS managed private zones in the host project and authorizes them for the Shared VPC network.

  2. Enable GKE Hub (fleet) API. The GKE Hub API must be enabled in only the fleet host project.
         
         gcloud services enable gkehub.googleapis.com \
             --project FLEET_HOST_PROJ
         

Enabling this API in the fleet host project creates or ensures that the following service account exists: `service-FLEET_HOST_PROJ_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com`.

  3. Enable Cloud Service Mesh, Resource Manager, and Multi-cluster Service Discovery APIs in the fleet host project:
         
         gcloud services enable trafficdirector.googleapis.com \
             cloudresourcemanager.googleapis.com \
             multiclusterservicediscovery.googleapis.com \
             --project FLEET_HOST_PROJ
         




### Enable Multi-cluster services in the fleet host project

  1. Enable multi-cluster services in the fleet host project:
         
         gcloud container fleet multi-cluster-services enable \
             --project FLEET_HOST_PROJ
         

Enabling multi-cluster services in the fleet host project creates or ensures that the following service account exists: `service-FLEET_HOST_PROJ_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com`.




### Create IAM bindings

  1. Create IAM binding granting the fleet host project MCS service account the MCS Service Agent role on the Shared VPC host project:
         
         gcloud projects add-iam-policy-binding SHARED_VPC_HOST_PROJ \
             --member "serviceAccount:service-FLEET_HOST_PROJ_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com" \
             --role roles/multiclusterservicediscovery.serviceAgent
         

  2. Create IAM binding granting the fleet host project MCS service account the Network User role for its own project:
         
         gcloud projects add-iam-policy-binding FLEET_HOST_PROJ \
             --member "serviceAccount:FLEET_HOST_PROJ.svc.id.goog[gke-mcs/gke-mcs-importer]" \
             --role roles/compute.networkViewer
         

Because this scenario uses Workload Identity Federation for GKE, the fleet host project's MCS Importer GKE service account needs the Network User role for its own project.

Replace the following:

     * `SHARED_VPC_HOST_PROJ`: the project ID of the Shared VPC host project
     * `FLEET_HOST_PROJ_NUMBER`: the project number of the fleet host project, which is the Shared VPC service project for this scenario
     * `FLEET_HOST_PROJ`: the project ID of the first cluster's project.



### Register the clusters to the fleet

  1. Register the first cluster to the fleet. The `--gke-cluster` flag can be used for this command because the first cluster is located in the same project as the fleet to which it is being registered.
         
         gcloud container fleet memberships register MEMBERSHIP_NAME_1 \
             --project FLEET_HOST_PROJ \
             --enable-workload-identity \
             --gke-cluster=LOCATION/FIRST_CLUSTER_NAME
         

Replace the following:

     * `MEMBERSHIP_NAME_1`: a unique identifier for this cluster in this fleet. For example, you can use the name of the first GKE cluster.
     * `FLEET_HOST_PROJ`: the project ID for the fleet host project, identical to the Shared VPC host project in this scenario.
     * `LOCATION`: for zonal clusters, the Compute Engine zone containing the cluster; for regional clusters, the Compute Engine region containing the cluster.
     * `FIRST_CLUSTER_NAME`: the name of the first cluster.
  2. Register the second cluster to the fleet host project. The `--gke-cluster` flag can be used for this command because the second cluster is also located in the fleet host project.
         
         gcloud container fleet memberships register MEMBERSHIP_NAME_2 \
             --project FLEET_HOST_PROJ \
             --enable-workload-identity \
             --gke-cluster=LOCATION/SECOND_CLUSTER_NAME
         

Replace the following:

     * `MEMBERSHIP_NAME_2`: a unique identifier for this cluster in this fleet. For example, you can use the name of the second GKE cluster.
     * `FLEET_HOST_PROJ`: the project ID for the fleet host project, identical to the Shared VPC host project in this scenario.
     * `LOCATION`: for zonal clusters, the Compute Engine zone containing the cluster; for regional clusters, the Compute Engine region containing the cluster.
     * `SECOND_CLUSTER_NAME`: the name of the second cluster.



### Create a common namespace for the clusters

  1. Ensure that each cluster has a namespace to share Services in. If needed, create a namespace by using the following command in each cluster:
         
         kubectl create ns NAMESPACE
         

Replace `NAMESPACE` with a name for the namespace.




## Shared VPC host project as fleet host project

This section provides an example MCS configuration involving two existing GKE clusters:

  * The first VPC-native GKE cluster `FIRST_CLUSTER_NAME`, with Workload Identity Federation for GKE enabled, has been created in the `FLEET_HOST_PROJ`. The fleet host project is also the Shared VPC host project in this scenario.
  * The second VPC-native GKE cluster `SECOND_CLUSTER_NAME`, with Workload Identity Federation for GKE enabled, has been created in the `SECOND_CLUSTER_PROJ`.



### Enable required APIs

Enable the required APIs. The output of the Google Cloud CLI shows you if an API has already been enabled.

  1. Enable the Cloud DNS API:
         
         gcloud services enable dns.googleapis.com \
             --project FLEET_HOST_PROJ
         

In this scenario, the fleet host project is also the Shared VPC host project. The Cloud DNS API must be enabled in the Shared VPC host project because that's where the Shared VPC network is located. GKE creates Cloud DNS managed private zones in the host project and authorizes them for the Shared VPC network.

  2. Enable GKE Hub (fleet) API. The GKE Hub API must be enabled in only the fleet host project.
         
         gcloud services enable gkehub.googleapis.com \
             --project FLEET_HOST_PROJ
         

Enabling the GKE Hub API in the fleet host project creates or ensures that the following service account exists: `service-FLEET_HOST_PROJ_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com`.

  3. Enable Cloud Service Mesh, Resource Manager, and Multi-cluster Service Discovery APIs, in both the fleet host project and in the second cluster's project:
         
         gcloud services enable trafficdirector.googleapis.com \
             cloudresourcemanager.googleapis.com \
             multiclusterservicediscovery.googleapis.com \
             --project FLEET_HOST_PROJ
         
         
         gcloud services enable trafficdirector.googleapis.com \
             cloudresourcemanager.googleapis.com \
             multiclusterservicediscovery.googleapis.com \
             --project SECOND_CLUSTER_PROJ
         




### Enable Multi-cluster services in the fleet host project

  1. Enable multi-cluster services in the fleet host project:
         
         gcloud container fleet multi-cluster-services enable \
             --project FLEET_HOST_PROJ
         

Enabling multi-cluster services in the fleet host project creates or ensures that the following service account exists: `service-FLEET_HOST_PROJ_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com`.




### Create IAM bindings

  1. Create IAM binding granting the fleet host project's GKE fleet service account the GKE Service Agent role on the second cluster's project:
         
         gcloud projects add-iam-policy-binding SECOND_CLUSTER_PROJ \
             --member "serviceAccount:service-FLEET_HOST_PROJ_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com" \
             --role roles/gkehub.serviceAgent
         

  2. Create IAM binding granting the fleet host project's MCS service account the MCS Service Agent role on the second cluster's project:
         
         gcloud projects add-iam-policy-binding SECOND_CLUSTER_PROJ \
             --member "serviceAccount:service-FLEET_HOST_PROJ_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com" \
             --role roles/multiclusterservicediscovery.serviceAgent
         

  3. Create IAM binding granting each project's MCS service account the Network User role for its own project:
         
         gcloud projects add-iam-policy-binding FLEET_HOST_PROJ \
             --member "serviceAccount:FLEET_HOST_PROJ.svc.id.goog[gke-mcs/gke-mcs-importer]" \
             --role roles/compute.networkViewer
         
         
         gcloud projects add-iam-policy-binding SECOND_CLUSTER_PROJ \
             --member "serviceAccount:SECOND_CLUSTER_PROJ.svc.id.goog[gke-mcs/gke-mcs-importer]" \
             --role roles/compute.networkViewer
         

Because this scenario uses Workload Identity Federation for GKE, each project's MCS Importer GKE service account needs the Network User role for its own project.

Replace the following:

     * `SECOND_CLUSTER_PROJ`: the project ID of the second cluster's project
     * `FLEET_HOST_PROJ`: the project ID of the first cluster's project.
     * `FLEET_HOST_PROJ_NUMBER`: the project number of the fleet host project, which is the same as the Shared VPC host project for this scenario



### Register the clusters to the fleet

  1. Register the first cluster to the fleet. The `--gke-cluster` flag can be used for this command because the first cluster is located in the same project as the fleet to which it is being registered.
         
         gcloud container fleet memberships register MEMBERSHIP_NAME_1 \
             --project FLEET_HOST_PROJ \
             --enable-workload-identity \
             --gke-cluster=LOCATION/FIRST_CLUSTER_NAME
         

Replace the following:

     * `MEMBERSHIP_NAME_1`: a unique identifier for this cluster in this fleet. For example, you can use the name of the first GKE cluster.
     * `FLEET_HOST_PROJ`: the project ID for the fleet host project, identical to the Shared VPC host project in this scenario.
     * `LOCATION`: for zonal clusters, the Compute Engine zone containing the cluster; for regional clusters, the Compute Engine region containing the cluster.
     * `FIRST_CLUSTER_NAME`: the name of the first cluster.
  2. Register the second cluster to the fleet. The `--gke-uri` flag must be used for this command because the second cluster is not located in the same project as the fleet. You can obtain the full cluster URI by running `gcloud container clusters list --uri`.
         
         gcloud container fleet memberships register MEMBERSHIP_NAME_2 \
             --project FLEET_HOST_PROJ \
             --enable-workload-identity \
             --gke-uri https://container.googleapis.com/v1/projects/SECOND_CLUSTER_PROJ/locations/LOCATION/clusters/SECOND_CLUSTER_NAME
         

Replace the following:

     * `MEMBERSHIP_NAME_2`: a unique identifier for this cluster in this fleet. For example, you can use the name of the second GKE cluster.
     * `FLEET_HOST_PROJ`: the project ID for the fleet host project, identical to the Shared VPC host project in this scenario.
     * `LOCATION`: replace `LOCATION` with: 
       * the cluster's Compute Engine zone if the cluster is a zonal cluster
       * the cluster's Compute Engine region if the cluster is a regional cluster
     * `SECOND_CLUSTER_PROJECT`: the project containing the second cluster.
     * `SECOND_CLUSTER_NAME`: the name of the second cluster.



### Create a common namespace for the clusters

  1. Ensure that each cluster has a namespace to share Services in. If needed, create a namespace by using the following command in each cluster:
         
         kubectl create ns NAMESPACE
         

Replace `NAMESPACE` with a name for the namespace.




## Clusters in different Shared VPC service projects

This section provides an example MCS configuration involving two existing GKE clusters each in a different Shared VPC service project.

  * Both clusters use the same Shared VPC network in the `SHARED_VPC_HOST_PROJ`.
  * The first VPC-native GKE cluster `FIRST_CLUSTER_NAME`, with Workload Identity Federation for GKE enabled, has been created in the `FLEET_HOST_PROJ`. The fleet host project is a service project connected to the `SHARED_VPC_HOST_PROJ` in this scenario.
  * The second VPC-native GKE cluster `SECOND_CLUSTER_NAME`, with Workload Identity Federation for GKE enabled, has been created in the `SECOND_CLUSTER_PROJ`. The `SECOND_CLUSTER_PROJ` is also a service project connected to the `SHARED_VPC_HOST_PROJ` in this scenario.



### Enable required APIs

Enable the required APIs. The output of the Google Cloud CLI shows you if an API has already been enabled.

  1. Enable the Cloud DNS API:
         
         gcloud services enable dns.googleapis.com \
             --project SHARED_VPC_HOST_PROJ
         

In this scenario, the fleet host project is a service project connected to the Shared VPC host project. The Cloud DNS API must be enabled in the Shared VPC host project because that's where the Shared VPC network is located. GKE creates Cloud DNS managed private zones in the host project and authorizes them for the Shared VPC network.

  2. GKE Hub (fleet) API. The GKE Hub API must be enabled in only the fleet host project `FLEET_HOST_PROJ`.
         
         gcloud services enable gkehub.googleapis.com \
             --project FLEET_HOST_PROJ
         

Enabling this API in the fleet host project creates or ensures that the following service account exists: `service-FLEET_HOST_PROJ_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com`.

  3. Enable Cloud Service Mesh, Resource Manager, and Multi-cluster Service Discovery APIs, in both the fleet host project and in the second cluster's project:
         
         gcloud services enable trafficdirector.googleapis.com \
             cloudresourcemanager.googleapis.com \
             multiclusterservicediscovery.googleapis.com \
             --project=FLEET_HOST_PROJ
         
         
         gcloud services enable trafficdirector.googleapis.com \
             cloudresourcemanager.googleapis.com \
             multiclusterservicediscovery.googleapis.com \
             --project SECOND_CLUSTER_PROJ
         




### Enable Multi-cluster services in the fleet host project

  1. Enable multi-cluster services in the fleet host project:
         
         gcloud container fleet multi-cluster-services enable \
             --project FLEET_HOST_PROJ
         

Enabling multi-cluster services in the fleet host project creates or ensures that the following service account exists: `service-FLEET_HOST_PROJ_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com`.




### Create IAM bindings

  1. Create IAM binding granting the fleet host project's GKE Hub service account the GKE Service Agent role on the second cluster's project:
         
         gcloud projects add-iam-policy-binding SECOND_CLUSTER_PROJ \
             --member "serviceAccount:service-FLEET_HOST_PROJ_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com" \
             --role roles/gkehub.serviceAgent
         

  2. Create IAM binding granting the fleet host project's MCS service account the MCS Service Agent role on the second cluster's project:
         
         gcloud projects add-iam-policy-binding SECOND_CLUSTER_PROJ \
             --member "serviceAccount:service-FLEET_HOST_PROJ_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com" \
             --role roles/multiclusterservicediscovery.serviceAgent
         

  3. Create IAM binding granting the fleet host project MCS service account the MCS Service Agent role on the Shared VPC host project:
         
         gcloud projects add-iam-policy-binding SHARED_VPC_HOST_PROJ \
             --member "serviceAccount:service-FLEET_HOST_PROJ_NUMBER@gcp-sa-mcsd.iam.gserviceaccount.com" \
             --role roles/multiclusterservicediscovery.serviceAgent
         

  4. Create IAM binding granting each project's MCS service account the Network User role for its own project:
         
         gcloud projects add-iam-policy-binding FLEET_HOST_PROJ \
             --member "serviceAccount:FLEET_HOST_PROJ.svc.id.goog[gke-mcs/gke-mcs-importer]" \
             --role roles/compute.networkViewer
         
         
         gcloud projects add-iam-policy-binding SECOND_CLUSTER_PROJ \
             --member "serviceAccount:SECOND_CLUSTER_PROJ.svc.id.goog[gke-mcs/gke-mcs-importer]" \
             --role roles/compute.networkViewer
         

Because this scenario uses Workload Identity Federation for GKE, each project's MCS Importer GKE service account needs the Network User role for its own project.

Replace the following as needed in the previous commands:

     * `SECOND_CLUSTER_PROJ`: the project ID of the second cluster's project.
     * `SHARED_VPC_HOST_PROJ`: the project ID of the Shared VPC host project. In this example, both clusters use the same Shared VPC network, but neither cluster is located in the Shared VPC host project.
     * `FLEET_HOST_PROJ`: the project ID of the first cluster's project.
     * `FLEET_HOST_PROJ_NUMBER`: the project number of the fleet host project.



### Register the clusters to the fleet

  1. Register the first cluster to the fleet. The `--gke-cluster` flag can be used for this command because the first cluster is located in the same project as the fleet to which it is being registered.
         
         gcloud container fleet memberships register MEMBERSHIP_NAME_1 \
             --project FLEET_HOST_PROJ \
             --enable-workload-identity \
             --gke-cluster=LOCATION/FIRST_CLUSTER_NAME
         

Replace the following:

     * `MEMBERSHIP_NAME_1`: a unique identifier for this cluster in this fleet. For example, you can use the name of the first GKE cluster.
     * `FLEET_HOST_PROJ`: the project ID for the fleet host project, identical to the Shared VPC host project in this scenario.
     * `LOCATION`: for zonal clusters, the Compute Engine zone containing the cluster; for regional clusters, the Compute Engine region containing the cluster.
     * `FIRST_CLUSTER_NAME`: the name of the first cluster.
  2. Register the second cluster to the fleet. The `--gke-uri` flag must be used for this command because the second cluster is not located in the same project as the fleet. You can obtain the full cluster URI by running `gcloud container clusters list --uri`.
         
         gcloud container fleet memberships register MEMBERSHIP_NAME_2 \
             --project FLEET_HOST_PROJ \
             --enable-workload-identity \
             --gke-uri https://container.googleapis.com/v1/projects/SECOND_CLUSTER_PROJ/locations/LOCATION/clusters/SECOND_CLUSTER_NAME
         

Replace the following:

     * `MEMBERSHIP_NAME_2`: a unique identifier for this cluster in this fleet. For example, you can use the name of the second GKE cluster.
     * `FLEET_HOST_PROJ`: the project ID for the fleet host project, identical to the Shared VPC host project in this scenario.
     * `LOCATION`: replace `LOCATION` with: 
       * the cluster's Compute Engine zone if the cluster is a zonal cluster
       * the cluster's Compute Engine region if the cluster is a regional cluster
     * `SECOND_CLUSTER_PROJECT`: the project containing the second cluster.
     * `SECOND_CLUSTER_NAME`: the name of the second cluster.



### Create a common namespace for the clusters

  1. Ensure that each cluster has a namespace to share Services in. If needed, create a namespace by using the following command in each cluster:
         
         kubectl create ns NAMESPACE
         

Replace `NAMESPACE` with a name for the namespace.




## What's next

  * Learn how to [use MCS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
