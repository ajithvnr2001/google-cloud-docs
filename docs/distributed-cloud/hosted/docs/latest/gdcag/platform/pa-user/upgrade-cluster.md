---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/upgrade-cluster/
title: Upgrade a cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:51:14.421114+00:00
---

# Upgrade a cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/upgrade-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Upgrade a cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains how to upgrade the Kubernetes version of a Google Distributed Cloud (GDC) air-gapped Kubernetes cluster. You must plan routine upgrades for your clusters to ensure they incorporate the latest Kubernetes features and fixes.

This document is for audiences such as IT administrators, security engineers, and network administrators within the platform administrator group, who are responsible for managing Kubernetes resources within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to upgrade your Kubernetes cluster. You must request roles scoped to your project and organization.

#### Organization roles

To list available upgrade versions for a Kubernetes cluster, ask your Organization IAM Admin to grant you the **User Cluster Admin** (`user-cluster-admin`) role. This role isn't bound to a namespace.

If you manage a standard cluster and are unable to obtain the User Cluster Admin role from your platform administrator group, you must request they provide you with the list of available Kubernetes upgrade versions.

#### Project roles

To create, delete, edit, or view cluster upgrades, ask your Project IAM Admin to grant you the **Standard Cluster Admin** (`standard-cluster-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against a [Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#cluster-architecture) using the API, make sure you have the following resources:

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * Locate the Kubernetes cluster name, or ask a member of the platform administrator group what the cluster name is.

  * Use the Kubernetes cluster name to replace `CLUSTER_NAME` in these instructions.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-resources-kubeconfig) the kubeconfig file for the management API server.

  * Use the kubeconfig path of the management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




## Upgrade a Kubernetes cluster

Use the [`UserClusterUpgradeRequest`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/cluster/v1/cluster-v1#userclusterupgraderequest) API to upgrade an existing Kubernetes cluster.

To upgrade a Kubernetes cluster using the API, follow these steps:

  1. List the available Kubernetes upgrade versions by printing the `kubernetesVersion` value of the `UserClusterMetadata` objects:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get userclustermetadata -o=custom-columns='TARGET_VERSION:.spec.kubernetesVersion'
         

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file of the management API server.

The command returns a list of available Kubernetes versions:
         
         TARGET_VERSION
         1.30.1000-gke.85
         

  2. Note the Kubernetes version from the previous output that you want to upgrade your cluster to. The `targetVersion` you specify in the upgrade request in the next step must be one of these available versions.

  3. Request the cluster upgrade by creating a `UserClusterUpgradeRequest` resource:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
           apiVersion: cluster.gdc.goog/v1
           kind: UserClusterUpgradeRequest
           metadata:
             name: CLUSTER_NAME
             namespace: CLUSTER_NAMESPACE
           spec:
             clusterRef:
               name: CLUSTER_NAME
             targetVersion: TARGET_VERSION
           EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the path to the kubeconfig file of the management API server.
     * `CLUSTER_NAME`: the name of the Kubernetes cluster to upgrade, such as `user-vm-2`.
     * `CLUSTER_NAMESPACE`: the namespace of the Kubernetes cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.
     * `TARGET_VERSION`: the target version for the upgrade identified in the previous step, such as `1.30.1000-gke.85`.

The average upgrade time for a Kubernetes cluster takes approximately 20 minutes.

  4. Verify the cluster upgrade by monitoring the `UserClusterUpgradeRequest` resource:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             describe userclusterupgraderequest CLUSTER_NAME \
             -n CLUSTER_NAMESPACE
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the path to the kubeconfig file of the management API server.
     * `CLUSTER_NAME`: the name of the Kubernetes cluster to upgrade, such as `user-vm-2`.
     * `CLUSTER_NAMESPACE`: the namespace of the Kubernetes cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.

Inspect the `Spec` section of the output. It contains `Current Version` and `Target Version`. The upgrade is still in progress if the `Current Version` and the `Target Version` differ.
    
    Spec:
      ...
      Current Version: 1.29.500-gke.60
      Target Version: 1.30.1000-gke.85
    Status:
      Conditions:
      - Message: Upgrade is in progress
        Reason: UpgradeInProgress
        Status: "False"
        Type: Succeeded
    

The upgrade is complete and successful when the `Succeeded` condition has a status of `True`, and the `Current Version` matches the `Target Version`.

If the `Succeeded` condition has a status of `False`, the upgrade failed. If you encounter errors related to your Kubernetes cluster upgrade, contact the infrastructure operator group for further assistance.




## Verify cluster subcomponents after upgrade

After your Kubernetes cluster is successfully upgraded, we recommend confirming that all subcomponents of the cluster are healthy.

Check for subcomponent failures in your cluster:

  1. Verify that there are no subcomponents that show a `ReconciliationError` message:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get subcomponent -n CLUSTER_NAME -o json | jq -r \
             '.items[] |  select(.status.conditions[]?.reason == "ReconciliationError") |
             select(.status.featureDisabled != true) |  "Sub-Component: \(.metadata.name)
             - \(.status.conditions[]?.message)"'
         

If the output returns any subcomponents, reach out to your infrastructure operator group for further assistance.

  2. Verify that there are no subcomponents that show a `Reconciling` message:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get subcomponent -n CLUSTER_NAME -o json | jq -r \
             '.items[] |  select(.status.conditions[]?.reason == "Reconciling") |
             select(.status.featureDisabled != true) | select( "\(.status)" |
             contains("PreinstallPending") | not) | "Sub-Component: \(.metadata.name)
             - \(.status.conditions[]?.message)"'
         

For Kubernetes clusters with three control plane nodes and three worker nodes, the upgrade time takes approximately 20 minutes. If you still see subcomponents in a state of `Reconciling` after 20 minutes, contact your infrastructure operator group for further assistance.




## What's next

  * [Design workload separation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/workload-separation)
  * [Maintain Kubernetes clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
