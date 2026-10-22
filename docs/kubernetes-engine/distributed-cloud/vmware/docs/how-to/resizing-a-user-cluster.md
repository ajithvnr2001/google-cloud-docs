---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-a-user-cluster/
title: Resizing a user cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:17.424933+00:00
---

# Resizing a user cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-a-user-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Resizing a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

Resizing a user cluster means adding or removing nodes. Adding nodes requires that IP addresses are available for the new nodes. You resize a user cluster by changing the number of replicas in the node pool.

For information on maximum and minimum limits for user clusters, see [Scalability limits](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/scalability#limits).

For information on managing node pools, see [creating and managing node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools).

## Verify that enough IP addresses are available

If you intend to have N nodes after the resizing, then you must have N + 1 IP addresses available.

Before resizing a cluster, verify that you have enough IP addresses. How you do the verification depends on whether the cluster uses a DHCP server or static IP addresses.

### DHCP

If the cluster uses DHCP, check that the DHCP server can provide enough IP addresses. It must be able to provide at least one more IP address than the number of nodes that will be in the cluster after the resizing.

### Static IPs

How you verify that you have enough static IP addresses depends on whether the cluster is enrolled in the GKE On-Prem API. A user cluster is enrolled in the GKE On-Prem API if one of the following is true:

  * The cluster was created by using the Google Cloud console, the Google Cloud CLI (gcloud CLI), or Terraform, which automatically enrolls the cluster in the GKE On-Prem API. Collectively, these standard applications are referred to as GKE On-Prem API clients.

  * The command `gkectl enroll cluster` was run on a user cluster, which [configures it to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster).




If the GKE On-Prem API is managing a user cluster, use the console to count the number of IPs and add more IPs if needed. If the user cluster isn't managed by the GKE On-Prem API, you can run `gkectl update cluster` first, which verifies whether you've allocated enough IP addresses in the cluster. If not, you can find the number of extra IP addresses needed in the error message.

## Add static IPs

If the cluster is managed by the GKE On-Prem API, use the console to add more IP addresses. Otherwise, use the command line on your admin workstation.

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **More details** in the **Details** panel.

  4. In the **Networking** section, click edit  **Edit**.

  5. In the **Add additional static IP addresses** dialog box, click **Add IP Address**. Enter the IP address and optionally, a hostname. Repeat as needed. When finished, click **Done**.




### Command line

  1. Open the user cluster's [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for editing.

  2. Verify that all of the IP addresses you intend to use for the user cluster are included in the IP block file. The IP block file should have at least one more IP address than the number of nodes that will be in the cluster after the resizing.

  3. To view the addresses reserved for a user cluster:
         
         kubectl get cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --namespace USER_CLUSTER_NAME USER_CLUSTER_NAME --output yaml

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file
     * `USER_CLUSTER_NAME`: the name of the user cluster
  4. Add as many additional static IP addresses to the corresponding block as required, and then run `gkectl update cluster`.




Here is an example of an IP block file that has four IP addresses and the corresponding hostnames:
    
    
    hostconfig:
    dns: 172.16.255.1
    tod: 216.239.35.0
    blocks:
    - netmask: 255.255.248.0
      gateway: 21.0.135.254
      ips:
      - ip: 21.0.133.41
        hostname: user-node-1
      - ip: 21.0.133.50
        hostname: user-node-2
      - ip: 21.0.133.56
        hostname: user-node-3
      - ip: 21.0.133.47
        hostname: user-node-4
    

## Resize the cluster

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **More details** in the **Details** panel.

  4. Click the **Nodes** tab.

  5. Click the name of the node pool that you want to resize.

  6. Click edit **Resize**.

  7. In the **Nodes** field, enter the number of nodes that you want in the node pool, and then click **Done**.

  8. Click arrow_back to go back to the previous page.

  9. The console displays **Cluster status: changes in progress**. Click **Show Details** to view the **Resource status condition** and **Status messages**.




### Command line

In the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-replicas-field), update the value of the `replicas` field in one or more of the `nodePools` elements.

Resize the cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file

  * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file




Verify that the resizing succeeded:

  * If [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) isn't enabled:
        
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get nodes
        
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe machinedeployments NODE_POOL_NAME | grep Replicas

  * If [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) is enabled
        
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get nodes
        
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG describe nodepoolclaim -n USER_CLUSTER_NAMESPACE NODE_POOL_NAME | grep "Node Count"




Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file

  * `USER_CLUSTER_KUBECONFIG`: the path of the user cluster kubeconfig file

  * `NODE_POOL_NAME`: the name of the node pool that you resized.

  * `USER_CLUSTER_NAMESPACE`: the namespace of the user cluster that you resized.




## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
