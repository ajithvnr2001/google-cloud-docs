---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke/
title: Register a cluster on Google Cloud to your fleet \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:49.812702+00:00
---

# Register a cluster on Google Cloud to your fleet  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Register a cluster on Google Cloud to your fleet Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to add a GKE cluster on Google Cloud to your fleet. Depending on your project and use case, you can use the Google Cloud console, Terraform, Config Connector, or the Google Cloud CLI for registration. You can also create and register a new cluster in a single step using the Google Cloud CLI, the Google Cloud console, or Terraform.

## Before you begin

Ensure that you have followed the [general prerequisites](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin) for registering a cluster. We also recommend reviewing the general restrictions on cluster registration in [Plan fleet resources](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets#fleet_and_resource_limitations).

Depending on your use case, GKE cluster on Google Cloud registrations may also require the following:

  * If you want your registered cluster to have fleet Workload Identity Federation enabled (recommended), [ensure Workload Identity Federation for GKE is enabled on the cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#enable_wi). Autopilot clusters have Workload Identity Federation for GKE enabled by default.
  * If you are registering a cluster to a fleet in a different project (also known as cross-project registration), [ensure you have set up the necessary permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project).
  * If you are registering a cluster by using Terraform or Config Connector, ensure that you have set up a Google Cloud service account for the tool and configured it so that the tool can authenticate to Google Cloud: 
    * [Set up a service account for Terraform](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#tf-identity)
    * [Set up a service account for Config Connector](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#kcc-identity)
  * If you want to use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running `gcloud components update`.

**Note:** For existing gcloud CLI installations, make sure to set the `compute/region` and `compute/zone` [properties](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). By setting default locations, you can avoid errors in gcloud CLI like the following: `One of [--zone, --region] must be supplied:`



## Register your GKE cluster on Google Cloud

As you saw in the prerequisites, we recommend registering your GKE clusters with fleet Workload Identity Federation for GKE enabled, which provides a consistent way for applications to authenticate to Google Cloud APIs and services. You can find out more about the advantages of enabling fleet Workload Identity Federation for GKE in [Use fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity). Registering clusters using any of the following options lets you enable fleet Workload Identity Federation for GKE if required.

You can choose between registering a new cluster during cluster creation, or registering an existing cluster.

### Register a new cluster

You can register clusters during cluster creation using the following instructions.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click add_box **Create** , and then in the Standard or Autopilot section, click **Configure**.

  3. Follow the instructions in the GKE documentation to complete the sections for creating an [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#console), [Standard regional](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster), or [Standard zonal](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster#console) cluster from the Google Cloud console.

  4. Complete fleet registration based on your cluster mode:

     * **Autopilot** : In the navigation pane, click **Fleet registration** , and select the checkbox to register the cluster to a fleet. By default, the fleet name is based on your project ID.
     * **Standard** : In the navigation pane, click **Advanced settings** , and then do the following: 
       1. In the **Fleet registration** row, click _edit_ **Edit configuration** , select **Register cluster to the fleet** , and then click **Save**. By default, the fleet name is based on your project ID.
       2. If you want the registered cluster to use fleet Workload Identity Federation (recommended), in the **Workload identity** row, click _edit_ **Edit configuration** , select **Enable Workload Identity** , and then click **Save**. Autopilot clusters have this feature enabled by default.
  5. Fill out the remaining sections.

  6. When you have finished reviewing cluster details, click **Create** to create and register the cluster to a fleet.




### gcloud

These commands require the [gcloud CLI version 450.0.0 or higher](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-cloud-sdk).

Registering a cluster by using the Google Cloud CLI gives your cluster a regional [membership location](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#fleet_membership_location) by default.

  * To create and register a new GKE Autopilot cluster, run the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME --enable-fleet
        

Replace `CLUSTER_NAME` with a unique name for the cluster you are creating. This will also become the cluster's [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership). If there is already a cluster with this name in your chosen fleet, the command will return an error.

  * To create and register a new GKE Autopilot cluster as [lightweight](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#lightweight_memberships), run the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME --enable-fleet --membership-type=LIGHTWEIGHT
        

  * To create and register a new GKE Standard cluster with Workload Identity Federation for GKE enabled, run the following command:
        
        gcloud container clusters create CLUSTER_NAME --enable-fleet \
        --workload-pool=PROJECT_ID.svc.id.goog
        

Replace the following:

    * `CLUSTER_NAME`: a unique name for the cluster you are creating. This will also become the cluster's [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership). If there is already a cluster with this name in your chosen fleet, the command will return an error.
    * `PROJECT_ID`: the Google Cloud project ID for the project that will own your new cluster.

If you are creating a Standard cluster, we recommend creating the cluster with Workload Identity Federation for GKE enabled, as this enables fleet Workload Identity Federation for your registered cluster. However, you can omit the `--workload-pool` flag if you don't want to use this feature. Autopilot clusters have Workload Identity Federation for GKE enabled by default.

  * To create and register a new GKE Standard cluster as [lightweight](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#lightweight-memberships), run the following command:
        
        gcloud container clusters create CLUSTER_NAME --enable-fleet --membership-type=LIGHTWEIGHT
        




Depending on the cluster you want to create, you can also specify any of the other options for creating a [Standard zonal](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster), [Standard regional](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster), or [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#create_an_autopilot_cluster) cluster. You may also need to specify a Compute Engine zone if you haven't configured a default zone for the Google Cloud CLI, and a Google Cloud project to own the cluster if you have not configured a default project.

Learn more about creating different types of GKE cluster in the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).

### Terraform

You can create and register GKE clusters with Terraform using the [`google` provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_versions). You can find a complete reference for the `google_container_cluster` resource used to manage a GKE cluster in the [Terraform registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#fleet).

Ensure that you have created a service account for Terraform to use as described in the [prerequisites](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#tf-identity) before following these instructions.

To create and register a new cluster, add the following blocks in your Terraform configuration.

  1. Specify the `google` provider as a required provider:
         
         terraform {
           required_providers {
             google = {
               source = "hashicorp/google"
               version = "VERSION"
             }
           }
         }
         

Replace `VERSION` with 5.6.0 or later.

  2. Create and register a new cluster:
         
         resource "google_container_cluster" "TF_CLUSTER_RESOURCE_NAME" {
           provider = google
           name               = "CLUSTER_NAME"
           location           = "ZONE"
           initial_node_count = 1
           fleet {
             project = "FLEET_HOST_PROJECT"
           }
         }
         

Replace the following:

     * `TF_CLUSTER_RESOURCE_NAME`: a unique name for the new `google_container_cluster` resource that you are creating.
     * `CLUSTER_NAME`: a unique name for the new GKE cluster that you want to create and register.
     * `ZONE`: the zone for your GKE cluster resource. For example: `us-central1-a`.
     * `FLEET_HOST_PROJECT`: the Google Cloud project ID in which you are creating and registering the cluster. If this is not set, the cluster won't be registered to a fleet. Specify a different project ID if you want to [register the cluster to a fleet in a different project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project).



### Register an existing cluster

Use any of the following options to register existing clusters, either to their own project's fleet or to a fleet in a different project.

To register an existing GKE cluster:

### Console

If you want your cluster to use [fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) (recommended), ensure that [Workload Identity Federation for GKE is enabled](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#enable_wi) on the cluster before following these instructions. Autopilot clusters have Workload Identity Federation for GKE enabled by default. Clusters with Workload Identity Federation for GKE automatically have fleet Workload Identity Federation enabled when you register them from the Google Cloud console.

  1. In the Google Cloud console, go to the **GKE Clusters** page.

[Go to the GKE Clusters page](https://console.cloud.google.com/kubernetes/list)

  2. Beside the cluster you want to register, click more_vert **Actions** , and select **Register**.

  3. Click **Register** again on the confirmation dialog that appears.




### gcloud

These commands require the [gcloud CLI version 450.0.0 or higher](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-cloud-sdk).

Registering a cluster by using the Google Cloud CLI gives your cluster a regional [membership location](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#fleet_membership_location) by default.

Both of these commands enable fleet Workload Identity Federation for the cluster if the cluster already has Workload Identity Federation for GKE enabled.

  * To register an existing GKE cluster on Google Cloud to its project's fleet, run the following command:
        
        gcloud container clusters update CLUSTER_NAME --enable-fleet
        

Replace `CLUSTER_NAME` with the name of the cluster you are registering. This will also become the cluster's [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership).

  * To register an existing GKE cluster on Google Cloud to its project's fleet as [lightweight](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#lightweight-memberships), run the following command:
        
        gcloud container clusters update CLUSTER_NAME --enable-fleet --membership-type=LIGHTWEIGHT
        

  * To register the cluster to a fleet in a _different_ project, use the `--fleet-project` flag, as shown in the following command. Ensure you have set up the [necessary permissions for cross-project registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project) before running this command.
        
        gcloud container clusters update CLUSTER_NAME --fleet-project=PROJECT_ID_OR_NUMBER
        

    * Replace `CLUSTER_NAME` with the name of the cluster you are registering. This will also become the cluster's [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership).
    * Replace `PROJECT_ID_OR_NUMBER` with the project ID or number of your chosen fleet host project.
  * To register the cluster to a fleet in a _different_ project as lightweight, use the `--fleet-project` flag, as shown in the following command. Ensure you have set up the [necessary permissions for cross-project registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project) before running this command.
        
        gcloud container clusters update CLUSTER_NAME --fleet-project=PROJECT_ID_OR_NUMBER /
        --membership-type=LIGHTWEIGHT
        

  * To convert an existing GKE cluster on Google Cloud from lightweight to regular membership, use the following command:
        
        gcloud container clusters update CLUSTER_NAME --unset-membership-type
        




### Terraform

You can register GKE clusters with Terraform using the [`google` provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_versions). You can find a complete reference for the `google_container_cluster` resource used to manage a GKE cluster in the [Terraform registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#fleet).

Ensure that you have created a service account for Terraform to use as described in the [prerequisites](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#tf-identity) before following these instructions.

### Register an existing cluster

To register an existing cluster, add the following block to the `google_container_cluster` resource configuration of your cluster:
    
    
    fleet {
            project = "FLEET_HOST_PROJECT"
          }
    

Replace `FLEET_HOST_PROJECT` with the Google Cloud project ID to which your cluster belongs, or a different project ID if you want to [register the cluster to a fleet in a different project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project).

### Enable Workload Identity Federation for GKE on a registered cluster

You can use Terraform to enable Workload Identity Federation for GKE for a cluster.

To enable Workload Identity Federation for GKE for your new or existing cluster, add the following block in the relevant cluster's `google_container_cluster` resource configuration:
    
    
      workload_identity_config {
        workload_pool = "PROJECT_ID.svc.id.goog"
      }
      ```
    
     Replace <code><var>PROJECT_ID</var></code> with the Google Cloud project ID for your Terraform resources.
    

### Config Connector

If you have the [Config Connector add-on installed](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall), you can use [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) to register GKE clusters. Ensure that you have a version of Config Connector above 1.47.0 and that you've created a service account as described in the [prerequisites](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#kcc-identity).

You can find a complete reference for the `GKEHubMembership` resource in the [Config Connector reference documentation](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubmembership).

### Register a GKE cluster

To register the cluster, first specify where you want to create your resources, following [the instructions in the Config Connector guide](https://cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#specify). Then create a YAML file to register and (optionally) create a cluster, as follows:

#### Create and register a GKE cluster

  1. Create a GKE cluster, as in the following simple example:
         
         apiVersion: container.cnrm.cloud.google.com/v1beta1
         kind: ContainerCluster
         metadata:
           name: CLUSTER_NAME
         spec:
           location: LOCATION
           initialNodeCount: 1
         

Replace the following:

     * CLUSTER_NAME: the name that you chose to uniquely represent the cluster you created with Config Connector.
     * LOCATION: the zone or region that you chose to provision your GKE cluster resource. For example: `us-central1-a`.

For a complete list of options when creating a GKE cluster with Config Connector, see the [Config Connector documentation](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster).

  2. Register a membership for the GKE cluster.
         
         apiVersion: gkehub.cnrm.cloud.google.com/v1beta1
         kind: GKEHubMembership
         metadata:
           name: MEMBERSHIP_NAME
         spec:
           location: MEMBERSHIP_LOCATION
           endpoint:
             gkeCluster:
               resourceRef:
                 name: CLUSTER_NAME
         

Replace the following:

     * MEMBERSHIP_NAME: the membership name that you chose to uniquely represent the cluster being registered to the fleet.
     * MEMBERSHIP_LOCATION: the location of the Fleet service you want to manage your cluster's membership. This can be the cluster's own location (recommended) or `global`. Learn more in [Fleet membership location](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#fleet_membership_location). You cannot specify a location that's different from the cluster's location: if you do this, registration fails.
     * CLUSTER_NAME: the name that you chose to uniquely represent the cluster you created with Config Connector.



#### Register the cluster in a different project

Add the following to the `metadata` field of the `GKEHubMembership` resource to [register a cluster to a fleet in another project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin/gke#gke-cross-project).
    
    
       metadata:
         annotations:
           cnrm.cloud.google.com/project-id: FLEET_PROJECT_ID
    

Replace the following:

  * FLEET_PROJECT_ID: the fleet host project you chose to register the GKE cluster.



#### Register an existing cluster

Use the following configuration if you want to register any existing cluster, regardless of how it was created. In this case you need to specify the full resource name of the cluster so that Config Connector can find it. Replace the `resourceRef` field of the `GKEHubMembership` resource with:
    
    
       resourceRef:
         external: //container.googleapis.com/CLUSTER_RESOURCE_NAME
    

Replace the following:

  * CLUSTER_RESOURCE_NAME: the Google Cloud resource name for the GKE cluster. For example: `projects/my-project/zones/us-west1-a/clusters/my-cluster`.



If the cluster was created with Config Connector you don't need to specify the fully qualified cluster name.

### Enable Workload Identity Federation for GKE on a registered cluster

Enabling Workload Identity Federation for GKE uses the same configuration as registering a cluster, with the following additional steps.

  1. Enable Workload Identity Federation for GKE by adding the following in the `spec` field of `ContainerCluster` resource. You need to do this for both new and existing clusters.
         
         spec:
           workloadIdentityConfig:
             workloadPool: PROJECT_ID.svc.id.goog
         

Replace the following:

     * PROJECT_ID: the default project you chose [through namespace annotation](https://cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#specify) to create your GKE cluster resource.
  2. Enable fleet Workload Identity Federation by adding the following in the `spec` field of `GKEHubMembership` resource block.
         
         spec:
           authority:
             issuer: https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME
         }
         

Replace the following:

     * PROJECT_ID: the default project you chose [through namespace annotation](https://cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#specify) to create your GKE cluster resource.
     * LOCATION: the zone or region that you chose to provision your GKE cluster resource. For example: `us-central1-a`.
     * CLUSTER_NAME: the name that you chose to uniquely represent the cluster you created.



## Troubleshooting

If you run into any problems during this setup, see our [troubleshooting guide](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting).

## What's next?

  * Validate successful cluster registration and get other fleet membership details, as described in [Get fleet membership status](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status)
  * Set up authentication to registered clusters: 
    * [With Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway)
    * [With third-party identity](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity)
  * [Log in to a cluster from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
