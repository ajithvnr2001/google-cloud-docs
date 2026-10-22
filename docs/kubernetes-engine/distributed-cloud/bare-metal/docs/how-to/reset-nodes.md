---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/reset-nodes/
title: Reset nodes and delete clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:08.204189+00:00
---

# Reset nodes and delete clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/reset-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Reset nodes and delete clusters Stay organized with collections  Save and categorize content based on your preferences. 

When a Google Distributed Cloud cluster is in the process of being installed, binaries and [systemd](https://www.freedesktop.org/wiki/Software/systemd/) services are installed on the nodes hosting that cluster, and services begin to listen to ports on the nodes.

However, if a cluster installation fails, all these binaries and services need to be deleted. In other words, the nodes need to be **reset** or wiped clean to prepare them for a reattempt at installing the cluster. If nodes aren't reset in this way, the next attempt to install a cluster on them fails.

This page describes how do this clean up operation of specific nodes and how to delete a cluster.

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Choose a deletion method

The method that you use to delete a cluster depends on:

  * The cluster type.
  * If you want to clean up only specific nodes and not delete the entire cluster.
  * How the cluster was created.



Google Distributed Cloud provides the following deletion methods:

  * The Google Cloud console or Google Cloud CLI:

    * Use the console or gcloud CLI to delete user clusters that are managed by the GKE On-Prem API. A user cluster is managed by the GKE On-Prem API if one of the following is true:

      * The cluster was created in the Google Cloud console or using the gcloud CLI, which automatically configures the GKE On-Prem API to manage the cluster.

      * The cluster was created using `bmctl`, but it was [configured it to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster).

  * `bmctl`:

    * Use `bmctl reset nodes` to reset specific nodes.
    * Use `bmctl reset` to delete the following cluster types:

      * Admin, hybrid, and standalone clusters (referred to as self-managed clusters). This includes admin clusters that are managed by the GKE On-Prem API.
      * User clusters that aren't managed by the GKE On-Prem API.

If you use `bmctl` to reset nodes or to delete a cluster, the command expects the cluster configuration file to be in the current working directory. By default, the path is like the following:

`bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME.yaml`

If you used the `--workspace-dir` flag to specify a different directory during cluster creation, you must use the flag to specify the working directory during cluster reset.

  * `kubectl`:

    * Use `kubectl delete cluster` to delete only user clusters that aren't managed by the GKE On-Prem API clusters. Don't run the command on other cluster types.
    * Note that if you use `kubectl delete cluster`, you must also delete the namespace that the cluster is in after you delete the cluster.



After you delete a cluster, you can reinstall it after making any needed configuration changes.

## Delete self-managed clusters

To delete an admin, hybrid, or standalone cluster, run the following command:

**Note:** The `bmctl reset` command doesn't delete any `containerd` configuration files or binaries. The `containerd systemd` service is left up and running. The command deletes the containers running pods scheduled to the node.
    
    
    bmctl reset --cluster CLUSTER_NAME
    

In the command, replace `CLUSTER_NAME` with the name of the cluster you want to reset.

Output from the `bmctl cluster reset` command looks similar to this sample:
    
    
    Please check the logs at bmctl-workspace/example-cluster-1/log/reset-20221025-184705/reset.log
    [2022-10-25 18:47:11+0000] Creating bootstrap cluster... OK
    [2022-10-25 18:48:18+0000] Loading images... OK
    [2022-10-25 18:48:18+0000] Waiting for reset jobs to finish...
    [2022-10-25 18:48:28+0000] Operation reset in progress: 1       Completed: 0    Failed: 0
    ...
    [2022-10-25 18:50:08+0000] Operation reset in progress: 0       Completed: 1    Failed: 0
    [2022-10-25 18:50:08+0000] Flushing logs... OK
    [2022-10-25 18:50:08+0000] Deleting GKE Hub member example-cluster-1 in project example-project-12345...
    [2022-10-25 18:50:11+0000] Successfully deleted GKE Hub member example-cluster-1 in project example-project-12345
    [2022-10-25 18:50:11+0000] Deleting bootstrap cluster... OK
    

In addition to deleting the cluster, the command deletes the cluster's membership from the [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts).

For admin clusters managed by the GKE On-Prem API, you also need to delete the API resources in Google Cloud. Otherwise, the cluster will be displayed on the [GKE clusters](https://console.cloud.google.com/kubernetes/list/overview) page in the Google Cloud console. Use the following command to delete the GKE On-Prem API resources for an admin cluster:
    
    
    gcloud container bare-metal admin-clusters unenroll CLUSTER_NAME \
        --project=FLEET_HOST_PROJECT_ID \
        --location=REGION \
        --ignore-errors
    

Replace the following:

  * `FLEET_HOST_PROJECT_ID`: The project ID of the fleet in which the admin cluster was a member.

  * `REGION`: The Google Cloud region in which the GKE On-Prem API stores cluster metadata.




The `--ignore-errors` flag ensures that the unenrollment of a bare metal admin cluster resource succeeds even if errors occur during unenrollment.

After the cluster deletion finishes, you can create a new cluster. For details, see [Cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

## Delete user clusters

If the user cluster is managed by the GKE On-Prem API, delete the cluster using the console or the gcloud CLI. Otherwise, use `bmctl` or `kubectl` to delete the cluster.

**Note:** Deleting a namespace prevents new resources from being created in that namespace, including jobs to reset machines. When deleting a user cluster, you must delete the cluster object first before deleting its namespace. Otherwise, the jobs to reset machines can't get created, and the deletion process skips the machine clean-up step.

### `bmctl`

You can use `bmctl` to delete user clusters that were created with `bmctl` or `kubectl`, and that aren't enrolled in the GKE On-Prem API.

**Note:** The `bmctl reset` command doesn't delete any `containerd` configuration files or binaries. The `containerd systemd` service is left up and running. The command deletes the containers running pods scheduled to the node.

Run the following command to delete a user cluster with `bmctl`:
    
    
    bmctl reset --cluster USER_CLUSTER_NAME --admin-kubeconfig ADMIN_KUBECONFIG_PATH
    

In the command, replace the following entries with information specific to your environment:

  * `USER_CLUSTER_NAME`: the name of the user cluster you're deleting.

  * `ADMIN_KUBECONFIG_PATH`: the path to the associated admin cluster's `kubeconfig` file. `bmctl` supports the use of `--kubeconfig` as an alias for the`--admin-kubeconfig` flag.




Output from the `bmctl cluster reset` command looks similar to this sample:
    
    
    Please check the logs at bmctl-workspace/example-cluster-1/log/reset-20221025-184705/reset.log
    [2022-10-25 18:47:11+0000] Creating bootstrap cluster... OK
    [2022-10-25 18:48:18+0000] Loading images... OK
    [2022-10-25 18:48:18+0000] Waiting for reset jobs to finish...
    [2022-10-25 18:48:28+0000] Operation reset in progress: 1       Completed: 0    Failed: 0
    ...
    [2022-10-25 18:50:08+0000] Operation reset in progress: 0       Completed: 1    Failed: 0
    [2022-10-25 18:50:08+0000] Flushing logs... OK
    [2022-10-25 18:50:08+0000] Deleting GKE Hub member example-cluster-1 in project example-project-12345...
    [2022-10-25 18:50:11+0000] Successfully deleted GKE Hub member example-cluster-1 in project example-project-12345
    [2022-10-25 18:50:11+0000] Deleting bootstrap cluster... OK
    

### `kubectl`

You can use `kubectl` to delete user clusters that were created with `bmctl` or `kubectl`, and that aren't enrolled in the GKE On-Prem API. To use `kubectl` to delete a user cluster, you must first delete the cluster object, then its namespace. Otherwise, the jobs to reset machines can't be created, and the deletion process might be stuck indefinitely.

To delete a user cluster with `kubectl`:

  1. Run the following command to delete the cluster object:
         
         kubectl delete cluster USER_CLUSTER_NAME -n USER_CLUSTER_NAMESPACE \
             --kubeconfig ADMIN_KUBECONFIG_PATH

In the command, replace the following entries with information specific to your environment:

     * `USER_CLUSTER_NAME`: the name of the user cluster you're deleting.

     * `USER_CLUSTER_NAMESPACE`: the namespace for the cluster. By default, the cluster namespaces for Google Distributed Cloud are the name of the cluster prefaced with `cluster-`. For example, if you name your cluster `test`, the namespace has a name like `cluster-test`.

     * `ADMIN_KUBECONFIG_PATH`: the path to the associated admin cluster's `kubeconfig` file.

  2. After the cluster is deleted successfully, run the following command to delete the namespace:
         
         kubectl delete namespace USER_CLUSTER_NAMESPACE --kubeconfig ADMIN_KUBECONFIG_PATH




### Console

If the user cluster is managed by the GKE On-Prem API do the following steps to delete the cluster:

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the list of clusters, click the cluster that you want to delete.

  4. In the list of clusters, locate the cluster that you want to delete. If the **Type** is **external** , this indicates that the cluster was created using `bmctl` and wasn't enrolled in the GKE On-Prem API. In this case, follow the steps in the `bmctl` or `kubectl` tab to delete the cluster.

If the icon in the **Status** column indicates a problem, follow the steps in the gcloud CLI tab to delete the cluster. You will need to add the `--ignore-errors` flag to the delete command.

  5. Click the name of the cluster that you want to delete.

  6. In the **Details** panel, near the top of the window, click delete **Delete**.

  7. When prompted to confirm, enter the name of the cluster and click **Remove**.




###  gcloud CLI 

If the user cluster is managed by the GKE On-Prem API, do the following steps to delete the cluster on a computer that has the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) installed:

  1. Log in with your Google account:
         
         gcloud auth login
         

  2. Update components:
         
         gcloud components update
         

  3. Get a list of clusters to help ensure that you specify the correct cluster name in the delete command:
         
         gcloud container bare-metal clusters list \
           --project=FLEET_HOST_PROJECT_ID \
           --location=LOCATION
         

Replace the following:

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the cluster was created in. 

     * `LOCATION`: The Google Cloud location associated with the user cluster.

The output is similar to the following:
    
    NAME                      LOCATION    VERSION         ADMIN_CLUSTER            STATE
    example-user-cluster-1a   us-west1    1.36.100-gke.144          example-admin-cluster-1  RUNNING
    

  4. Run the following command to delete the cluster:
         
         gcloud container bare-metal clusters delete USER_CLUSTER_NAME \
           --project=FLEET_HOST_PROJECT_ID \
           --location=LOCATION \
           --force \
           --allow-missing
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster to delete.

     * `FLEET_HOST_PROJECT_ID`: The ID of the project that the cluster was created in.

     * `LOCATION`: The Google Cloud location associated with the user cluster.

The `--force` flag lets you delete a cluster that has node pools. Without the `--force` flag, you have to [delete the node pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/delete) first, and then delete the cluster.

The `--allow-missing` flag is a [standard Google API flag](https://google.aip.dev/135#delete-if-existing). When you include this flag, the command returns success if the cluster isn't found.

If the command returns an error that contains the text `failed connecting to the cluster's control plane`, this indicates connectivity issues with either the admin cluster, the [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent), or the on-premises environment. To troubleshoot issues with the Connect Agent, see [Collecting Connect Agent logs](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting).

     * If you think the connectivity issue is transient, for example, because of network problems, wait and retry the command.

     * If you know that the admin cluster has been deleted, of if the node machines for the admin or the user cluster have been shut down or taken offline, include the `--ignore-errors` flag and retry the command.

You also need to include `--ignore-errors` if the cluster was deleted using `bmctl` or `kubectl`, which leaves GKE On-Prem API resources in Google Cloud. One symptom of this is that the cluster is still displayed on the [GKE clusters](https://console.cloud.google.com/kubernetes/list/overview) page in the console in a unhealthy state.

**Caution:** When the admin and user clusters are unreachable, and you include `--ignore-errors`, the delete command removes Google Cloud resources only. In this case, you still need to delete the cluster using `bmctl`.



For information about other flags, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete).

## Reset specific cluster nodes

You might want to reset specific nodes of a cluster if, for example, an admin cluster has been deleted but the user clusters managed by that admin cluster remain. In this case, the user clusters as a whole can't be deleted because the admin cluster has been deleted. Consequently, the nodes of the user clusters have to be individually reset.

To reset nodes, you need a service account with read access to Artifact Registry. The `bmctl` command expects the JSON key file for this service account as an argument. To reset individual nodes of a cluster, run the following command:
    
    
    bmctl reset nodes --addresses NODE_1_IP_ADDRESS,NODE_2_IP_ADDRESS \
        --ssh-private-key-path SSH_KEY_PATH \
        --gcr-service-account-key SERVICE_ACCOUNT_KEY_PATH \
        --login-user root
    

In the command, replace the following entries with information specific to your environment:

  * `NODE_1_IP_ADDRESS , NODE_2_IP_ADDRESS`: comma-separated list of IP addresses of nodes you want to delete.

  * `SSH_KEY_PATH`: path to SSH private key. This is the key that will be used to establish SSH connections with nodes during reset.

  * `SERVICE_ACCOUNT_KEY_PATH`: path to the JSON file that contains the service account key. This key gives `bmctl` permission to pull images from Artifact Registry. You can create a service account key using the console or the gcloud CLI. For details, see [Creating and managing service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys). Another way the service account key file can be created is if you run the `create config` command with the `--create-service-accounts` flag. For details about that command, see [Create and admin cluster config with bmctl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/admin-cluster-creation#create_an_admin_cluster_config_with_bmctl).

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 




## Cluster deletion details

During the deletion, the cluster's fleet membership registration, storage mounts, and data from the `anthos-system StorageClass` are deleted.

For all nodes, the tunnel interfaces used for cluster networking are removed, and the following directories are deleted:

  * `/etc/kubernetes`
  * `/etc/cni/net.d`
  * `/root/.kube`
  * `/var/lib/kubelet`



For load balancer nodes:

  * The `keepalived` and `haproxy` services are deleted.
  * The configuration files for `keepalived` and `haproxy` are deleted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
