---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general/
title: Updating a cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:25.507554+00:00
---

# Updating a cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Updating a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to perform a cluster update that does not include a change in version.

A cluster _update_ is a change to the cluster configuration.

A cluster _upgrade_ is a special case of a cluster update that includes a change to the control-plane version or a change to a node pool version. For information about upgrading, see [Upgrading Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

### Review your firewall rules

In version 1.29 and later, server-side preflight checks are enabled by default. Server-side preflight checks require additional firewall rules. In [Firewall rules for admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_admin_clusters), search for "Preflight checks" and make sure all required firewall rules are configured.

With server-side preflight checks, when you update a user cluster using `gkectl`, the preflight checks are run on the admin cluster instead of locally on the admin workstation. Server-side preflight checks are run on the admin cluster when you use the Google Cloud console, the Google Cloud CLI, or Terraform to update a cluster.

When you update an admin cluster, Google Distributed Cloud deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (kind) cluster to temporarily host the Kubernetes controllers needed to update the admin cluster. This transient cluster is called a _bootstrap cluster_. Server-side preflight checks are run on the bootstrap cluster when you update an admin cluster.

## What can be updated

Some cluster features and settings can be updated, but other features and settings can't be updated after the cluster is created. To see which features can be updated, look at the reference pages for the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest) and the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest). Fields that can be updated are marked as _Mutable_ , and fields that can't be updated are marked as _Immutable_.

You can also see which features and settings can be updated by running `gkectl` commands.

To see what can be updated in an admin cluster:
    
    
    gkectl update admin --help
    

Example output:
    
    
    Update the admin cluster. Only the following updates are supported and they can
    only be updated one at a time:
    - Enabling/Disabling Vsphere Resource Metrics
    - Adding static IPs
    - Updating vCenter CA certificate
    - Registering Admin Cluster
    - Enabling/Disabling Cloud Audit Logging
    - Enabling/Disabling Stackdriver
    - Enabling/Disabling Auto Repair
    - Enabling/Disabling Auto Resize for Addon Nodes
    - Enabling/Disabling GKE OnPrem API
    - Updating OS Image Type
    - Enabling/Disabling AntiAffinityGroups
    - Update Secrets Encryption Configuration
    - [Preview] Enabling/Disabling Cluster Backup
    - [Preview] Update Cluster Backup configs
    

To see what can be updated in a user cluster:
    
    
    gkectl update cluster --help
    

Example output:
    
    
    Update a GKE On-Prem cluster. Only the following updates are supported and they
    can only be updated one at a time:
    - Adding static IPs
    - Updating node pool
    - Updating user master cpu and memory
    - Enabling/Disabling Vsphere Resource Metrics
    - Enabling/Disabling vSphere CSI deployment
    - Enabling/Disabling Auto Repair
    - Enabling/Disabling Cloud Audit Logging
    - Enabling/Disabling Stackdriver
    - Enabling/Disabling GKE OnPrem API
    - Registering User Cluster
    - Updating vCenter CA certificate
    - Updating MetalLB Address Pools
    - Enabling/Disabling Auto Resizing on user master
    - Updating NodePoolUpdatePolicy
    - Enabling/Disabling AntiAffinityGroups
    - [Preview] Enabling/Disabling Node Network Policy
    - Updating Secrets Encryption
    - Enabling/Disabling DataplaneV2 forwardMode
    

## Update one thing at a time

Update only one feature or setting at a time. For example, suppose you want to update [master CPU and memory](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-cpus-field) and you also want to disable [auto repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#autorepair-enabled-field).

Then you would do two separate updates: one for master CPU and memory, and another auto repair. Verify that the first update is successful before you do the second update.

## Update procedure

You can use `gkectl`, the Google Cloud console, or the Google Cloud CLI to make updates to a user cluster. If you created the user cluster using Terraform, then you can use Terraform to update the cluster. In almost all cases, you must use `gkectl` to update admin clusters.

If you are using `gkectl` to update a cluster, make sure that your admin workstation has the needed version of `gkectl`. Typically, you use the same version of `gkectl` as the version of the cluster that you are updating. The following version rules are enforced during the update:

  * The `gkectl` minor version can't be lower than the cluster minor version. For example, updating a 1.30 cluster using `gkectl` version 1.29 isn't allowed. Patch versions don't matter. For example, you can use `gkectl` version 1.29.0-gke.1456 to update a cluster with a higher patch version, such as 1.29.1000-gke.94.

  * The `gkectl` minor version can't be more than two minor versions higher than the cluster version. For example, if you are updating a 1.28 cluster, the `gkectl` version can be 1.29 or 1.30. But you can't use `gkectl` version 1.31 because that is three minor versions higher than the cluster version.

  * If you are [updating the cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster), the `gkectl` version **must** be the same as your cluster version.




If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.

The following examples show how to update clusters.

### gkectl

The `gkectl update` command takes one of the following forms:

  * `gkectl update credentials` \- Use this to [update cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials).

  * `gkectl update admin` \- Run this command after you make a change in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest).

  * `gkectl update cluster` \- Run this command after you make a change in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest).




### Admin cluster example (`gkectl update admin`)

Suppose you want to change the value of [`gkeOnPremAPI.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeonpremapienabled) from `false` to `true` in an admin cluster. First, edit the admin cluster configuration file, and set the value to `true`:
    
    
    gkeOnPremAPI:
      enabled: true
    

Then update the admin cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * ADMIN_CLUSTER_CONFIG: the path of the admin cluster configuration file




### User cluster example (`gkectl update cluster`)

Suppose you want to change the value of [`stackdriver.vSphereDisableResourceMetrics`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-disablevsphereresourcemetrics-field) from `false` to `true` in a user cluster. First, edit the user cluster configuration file, and set the value to `true`:
    
    
    stackdriver:
      disableVsphereResourceMetrics: true
    

Then update the user cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of the user cluster configuration file




### User cluster example (`gkectl update credentials`)

Suppose you want to change the credentials that a user cluster uses to call vCenter Server.

The user cluster configuration file has a [vCenter.credentials.fileRef.path](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-credentials-fileref-path-field) field that points to a [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file). In the credentials configuration file, update the values of `username` and `password`. For example:
    
    
    items:
    - name: "vcenter-creds"
      username: "new-vcenter-account"
      password: "U$icUKEW#INE"
    

Then update the credentials:
    
    
    gkectl update credentials vsphere \
        --config USER_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace the following:

  * USER_CLUSTER_CONFIG: the path of the user cluster configuration file

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file




### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project, and then select the cluster that you want to update.

  3. In the **Details** panel, click **More details**.

  4. Fields that can be updated in the Google Cloud console have a pencil icon. Click one of the pencil icons. In the box that opens, change field values as desired, and click **DONE**.

  5. At the top of the page, in the progress bar, click **Show details**. Wait for the update to complete.




###  gcloud CLI 

Run the applicable update command. Specify only the flags for the configuration that you want to modify:

  * Admin clusters: [`gcloud container vmware admin-clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update)

  * User clusters: [`gcloud container vmware clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update)

  * Node pools on a user cluster: [`gcloud container vmware node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools/update)




### Update admin users on a user cluster

Each cluster's Kubernetes API server needs to be able to authorize requests that it receives. To configure authorization, you need to configure Kubernetes role-based access control (RBAC) policies on each cluster. An _admin user_ is a user who has been granted the `cluster-admin` role in the user cluster. This role grants the user full administrative access to the cluster.

Suppose Alice and Bob are the only admin users on the user cluster called cluster-1 in the us-west1 region. And suppose Alice wants to add Trent as an additional admin user. Alice could run the following command:
    
    
    gcloud container vmware clusters update cluster-1 \
        --project example-project-id-12345 \
        --location us-west1 \
        --admin-users alice@example.com \
        --admin-users bob@example.com \
        --admin-users trent@example.com
    

The preceding command keeps Alice and Bob in the list of admin users and adds Trent to the list of admin users. Notice that Alice and Bob must be listed in the command, because the command overwrites the current list of admin users with the list specified in the command. Also notice that each `--admin-users` flag specifies only one user. You can't specify multiple users in a single flag.

### Terraform

  1. Change the values of the applicable fields in the Terraform configuration file that you used to create the cluster or node pool. For detailed field descriptions, see the Terraform reference documentation:

     * [`google_gkeonprem_vmware_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_cluster)

     * [`google_gkeonprem_vmware_node_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_node_pool)

  2. Update the configuration by running [`terraform apply`](https://developer.hashicorp.com/terraform/cli/commands/apply).




### Update admin users on a user cluster

Each cluster's Kubernetes API server needs to be able to authorize requests that it receives. To configure authorization, you need to configure Kubernetes role-based access control (RBAC) policies on each cluster. An _admin user_ is a user who has been granted the `cluster-admin` role in the user cluster. This role grants the user full administrative access to the cluster.

Suppose Alice and Bob are the only admin users in a particular user cluster. And suppose Alice wants to add Trent as an additional admin user. Alice could adjust the Terraform configuration as follows and then run `terraform apply`:
    
    
    authorization {
      admin_users {
        username = "alice@example.com"
        username = "bob@example.com"
        username = "trent@example.com"
      }
    }
    

The preceding adjustment keeps Alice and Bob in the list of admin users and adds Trent to the list of admin users. Notice that Alice and Bob must be listed in the new configuration, because the `terraform apply` command overwrites the current list of admin users with the list specified in the configuration.

## More information

The documents listed in this section give additional details about updating clusters.

### Update cluster/admin

The following documents provide details about using `gkectl update admin` and `gkectl update cluster` to update features and settings:

  * [Automatic node repair and health checking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair)

  * [Resizing a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-a-user-cluster)

  * [Creating and managing node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools)

  * [Migrate a user cluster to Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2)




### Update credentials

The following documents provide details about using `gkectl update credentials` to update keys and certificates:

  * [Rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys)

  * [Updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials)

  * [Rotating admin cluster CA certificates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-ca-rotation)

  * [Rotating user cluster certificate authorities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation)

  * [Rotate KSA signing keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotate-ksa-signing-key)

  * [Update vCenter CA certificate references](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate)




## What's next

[Upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
