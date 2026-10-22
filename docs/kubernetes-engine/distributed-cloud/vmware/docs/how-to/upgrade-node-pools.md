---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools/
title: Upgrade node pools \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:53.787091+00:00
---

# Upgrade node pools  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Upgrade node pools Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to upgrade the control plane and node pools separately in a user cluster created with Google Distributed Cloud (software only) on VMware. This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks). Before reading this document, ensure that you're familiar with planning and executing Google Distributed Cloud upgrades as described in the following:

  * [Upgrade overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview)

  * [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices)

  * [Upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading)




## Limitations

Upgrading node pools separately from the control plane has the following limitations:

  * This feature is supported for Ubuntu and COS node pools, but not for Windows node pools.

  * This feature is not available when upgrading non-advanced clusters to advanced clusters. Non-advanced clusters will be upgraded to advanced clusters in 1.33 automatically.

  * Version 1.31: this feature isn't available on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).

  * Version 1.32 and higher: this feature is available on advanced clusters.

  * Load balancer node pool version must be the same as the cluster version. Upgrading a load balancer node pool (a node pool with `enableLoadBalancer: true`) separately from the control plane or having version skew is not supported.




## Why upgrade the control plane and node pools separately?

  * If your clusters are at version 1.16 or higher, you can skip a minor version when upgrading node pools. Performing a skip-version upgrade halves the time that it would take to sequentially upgrade node pools two versions. Additionally, skip-version upgrades lets you increase the time between upgrades needed to stay on a supported version. Reducing the number of upgrades reduces workload disruptions and verification time. For more information, see [Skip a version when upgrading node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade). 

  * In certain situations, you might want to upgrade some, but not all of the worker node pools in a user cluster, for example:

    * You could first upgrade the control plane and a node pool that has light traffic or that runs your least critical workloads. After you are convinced that your workloads run correctly on the new version, you could upgrade additional node pools, until eventually all the node pools are upgraded.

    * Instead of one large maintenance window for the cluster upgrade, you could upgrade the cluster in several maintenance windows. See [Estimate the time commitment and plan a maintenance window](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices#estimate_the_time_commitment_and_plan_a_maintenance_window) for information on estimating the time for a maintenance window.




## Before you begin

  1. In version 1.29 and later, server-side preflight checks are enabled by default. Make sure to [review your firewall rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#google_api_and_iam_requirements) to make any needed changes.

  2. To upgrade to version 1.28 and later, you must enable `kubernetesmetadata.googleapis.com` and grant the `kubernetesmetadata.publisher` IAM role to the [logging-monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account). For details, see [Google API and IAM requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#google_api_and_iam_requirements).

  3. Make sure the current version of the cluster is at version 1.14 or higher.




## Upgrade the control plane and selected node pools

Upgrading a user cluster's control plane separately from worker node pools is supported using `gkectl`, the Google Cloud CLI, and Terraform. You can only use Terraform for the upgrade if you created the user cluster using Terraform.

### `gkectl`

  1. Define the source version and the target version in the following placeholder variables. All versions must be the full version number in the form `x.y.z-gke.N` such as `1.16.11-gke.25`.

Version | Description  
---|---  
`SOURCE_VERSION` | The current cluster version.  
`TARGET_VERSION` | Pick the target version. Select the [ recommended patch](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed) from the target minor version.  
  2. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) to the target version. Wait for a message indicating the upgrade was successful.

  3. Import the corresponding OS images to vSphere:
         
         gkectl prepare \
           --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of your admin cluster `kubeconfig` file.

  4. Make the following changes in the user cluster configuration file:

     * Set the `gkeOnPremVersion` field to the target version, `TARGET_VERSION`.

     * For each node pool that you want to upgrade, set the `nodePools.nodePool[i].gkeOnPremVersion` field to the empty string.

       * In version 1.28 and later, you can accelerate the node pool upgrade by setting `nodePools.nodePool[i].updateStrategy.rollingUpdate.maxSurge` [field](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-updatestrategy-rollingupdate-maxsurge-field) to an integer value greater than 1. When you upgrade nodes with `maxSurge`, multiple nodes upgrade in the same time that it takes to upgrade a single node.
     * For each node pool that you **don't** want to upgrade, set `nodePools.nodePool[i].gkeOnPremVersion` to the source version, `SOURCE_VERSION`. Note that you cannot hold back load balancer node pools (node pools with `enableLoadBalancer: true`); their version must match the cluster version.

The following example shows a portion of the user cluster configuration file. It specifies that the control plane and `pool-1` will be upgraded to `TARGET_VERSION`, but `pool-2` will remain at `SOURCE_VERSION`.
    
    gkeOnPremVersion: TARGET_VERSION
    ...
    nodePools:
    - name: pool-1
      gkeOnPremVersion: ""
      ...
    - name: pool-2
      gkeOnPremVersion: SOURCE_VERSION
      ...
    

  5. Upgrade the control plane and selected node pools:
         
         gkectl upgrade cluster \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config USER_CLUSTER_CONFIG_FILE
         

Replace `USER_CLUSTER_CONFIG` with the path of your user cluster configuration file.




#### Upgrade additional node pools

Using the previous example, suppose everything is working well with `pool-1`, and now you want to upgrade `pool-2`.

  1. In your user cluster configuration file, under `pool-2`, set `gkeOnPremVersion` to the empty string:
         
         gkeOnPremVersion: TARGET_VERSION
         ...
         nodePools:
         - name: pool-1
           gkeOnPremVersion: ""
           ...
         - name: pool-2
           gkeOnPremVersion: ""
           ...
         

  2. Run `gkectl update cluster` to apply the change:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config USER_CLUSTER_CONFIG
         




###  gcloud CLI 

Upgrading a user cluster requires some changes to the admin cluster. The the `gcloud container vmware clusters upgrade` command automatically does the following:

  * [Enrolls the admin cluster in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) if it isn't already enrolled.

  * Downloads and deploys a bundle of components to the admin cluster. The version of the components matches the version you specify for the upgrade. These components let the admin cluster manage user clusters at that version.




#### Upgrade the control plane

Do the following step to upgrade the user cluster's control plane.

  1. Update the Google Cloud CLI components:
         
         gcloud components update
         

  2. Change the upgrade policy on the cluster:
         
         gcloud container vmware clusters update USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --upgrade-policy control-plane-only=True
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster to upgrade.

     * `PROJECT_ID`: The ID of the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project) in which the user cluster is a member. This is the project that you specified when the cluster was created. If you created the cluster using `gkectl`, this is the project ID in the `gkeConnect.projectID` field in the cluster configuration file.

     * `REGION`: The Google Cloud region in which the GKE On-Prem API runs and stores its metadata. If you created the cluster using an GKE On-Prem API client, this is the region that you selected when creating the cluster. If you created the cluster using `gkectl`, this is the region that you specified when you enrolled the cluster in the GKE On-Prem API.

  3. Upgrade the cluster's control plane:
         
         gcloud container vmware clusters upgrade USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --version=TARGET_VERSION
         

Replace `TARGET_VERSION` with the version to upgrade to. Select the [recommended patch](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed) from the target minor version.

The output from the command is similar to the following:
         
         Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
         

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the OPERATION_ID of the long-running operation. You can find out the status of the operation by running the following command in another terminal window:
         
         gcloud container vmware operations describe OPERATION_ID \
           --project=PROJECT_ID \
           --location=REGION
         




#### Upgrade node pools

Do the following steps to upgrade the node pools after the user cluster's control plane has been upgraded:

**Important:** When you upgrade a node pool to a new version, you can't modify other node pool attributes, such as display name, labels, or taints, in the same operation. The GKE On-Prem API rejects requests that combine a version upgrade with other attribute changes. If you need to modify other attributes, do so in a separate operation before or after the version upgrade.

  1. Get a list of node pools on the user cluster:
         
         gcloud container vmware node-pools list
           --cluster=USER_CLUSTER_NAME  \
           --project=PROJECT_ID \
           --location=REGION
         

  2. For each node pool that you want to upgrade, run the following command:
         
         gcloud container vmware node-pools update NODE_POOL_NAME \
           --cluster=USER_CLUSTER_NAME  \
           --project=PROJECT_ID \
           --location=REGION \
           --version=TARGET_VERSION
         




### Terraform

  1. Update the Google Cloud CLI components:
         
         gcloud components update
         

  2. If you haven't already, [enroll the admin cluster in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster). After the cluster is enrolled in the GKE On-Prem API, you don't need to do this step again.

  3. Download the new version of the components and deploy them in the admin cluster:
         
         gcloud vmware admin-clusters update ADMIN_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --required-platform-version=TARGET_VERSION
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster to upgrade.

     * `PROJECT_ID`: The ID of the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project) in which the user cluster is a member. This is the project that you specified when the cluster was created. If you created the cluster using `gkectl`, this is the project ID in the `gkeConnect.projectID` field in the cluster configuration file.

     * `REGION`: The Google Cloud region in which the GKE On-Prem API runs and stores its metadata. If you created the cluster using an GKE On-Prem API client, this is the region that you selected when creating the cluster. If you created the cluster using `gkectl`, this is the region that you specified when you enrolled the cluster in the GKE On-Prem API.

     * `TARGET_VERSION`: The version to upgrade to. Select the [recommended patch](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed) from the target minor version.

This command downloads the version of the components that you specify in `--required-platform-version` to the admin cluster, and then deploys the the components. These components let the admin cluster manage user clusters at that version.

  4. In the `main.tf` file that you used to create the user cluster, change `on_prem_version` in the cluster resource to the new version.

  5. Add the following to the cluster resource so that only the control plane is upgrade:
         
         upgrade_policy {
           control_plane_only = true
         }
         

  6. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider.

  7. Review the configuration and make changes if needed:
         
         terraform plan
         

  8. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         




#### Upgrade node pools

Do the following steps to upgrade node pools after the user cluster's control plane has been upgraded:

**Important:** When you upgrade a node pool to a new version, you can't modify other node pool attributes, such as display name, labels, or taints, in the same operation. The GKE On-Prem API rejects requests that combine a version upgrade with other attribute changes. If you need to modify other attributes, do so in a separate operation before or after the version upgrade.

  1. In `main.tf` in the resource for each node pool that you want to upgrade, add the following:
         
         on_prem_version = "TARGET_VERSION"
         

For example:
         
         resource "google_gkeonprem_vmware_node_pool" "nodepool-basic" {
         name = "my-nodepool"
         location = "us-west1"
         vmware_cluster = google_gkeonprem_vmware_cluster.default-basic.name
         config {
           replicas = 3
           image_type = "ubuntu_containerd"
           enable_load_balancer = true
         }
         on_prem_version = "1.16.0-gke.0"
         }
         

  2. Initialize and create the Terraform plan:
         
         terraform init
         

  3. Review the configuration and make changes if needed:
         
         terraform plan
         

  4. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         




## Troubleshooting

If you encounter an issue after upgrading a node pool, you can roll back to the previous version. For more information, see [Roll back a node pool after an upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade#roll-back-node-pool).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
