---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters/
title: Update clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:38.031819+00:00
---

# Update clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Update clusters Stay organized with collections  Save and categorize content based on your preferences. 

After you create a cluster, you can change some aspects of the cluster's configuration. For example you can:

  * Add, remove, or replace nodes.
  * Add or remove annotations to the cluster.
  * Modify the values of mutable fields in the cluster and node pool resources.
  * Modify other custom resources.



You can use `bmctl` or the Google Cloud CLI to make updates to a cluster. If you created an admin or user cluster using Terraform, then you can use Terraform to update the cluster. Note the following:

  * Many aspects of your cluster configuration are immutable and can't be updated after you create your cluster. For a comprehensive list of mutable and immutable fields, see the [Cluster configuration field reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#cluster_configuration_fields). The field reference is a sortable table. Click the column headings to change the sort order. Click a field name to view its description.

  * The gcloud CLI and Terraform only support updating admin and user clusters. You have to use `bmctl` to update other cluster types.

  * The gcloud CLI and Terraform only support changes to the cluster and node pool resources. You have to use `kubectl` or `bmctl` to update other custom resources that affect the cluster.

Modifying the namespace of an existing cluster in the cluster configuration file is `not a supported operation` and can lead to cluster instability and potential failures. To avoid these issues, don't attempt to modify the cluster namespace after its creation. 




This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## How to update clusters

Generally, you do the following sequence of actions to update a cluster:

### `bmctl`

  1. Change the values of the applicable fields in the cluster's configuration file, which by default is located here:   
`bmctl-workspace/CLUSTER-NAME/CLUSTER-NAME.yaml`

  2. Update the cluster by running the `bmctl update` command:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you want to update.
     * `KUBECONFIG`: for admin, hybrid, or standalone clusters, enter the path to the cluster's kubeconfig file. For a user cluster, enter the path to the **admin** cluster's kubeconfig file.

Don't use `bmctl update` and `kubectl apply -f` interchangeably when editing the cluster configuration file. When these commands are used interchangeably, contents populated by the header of the cluster spec might be unintentionally removed. For example, you might use `bmctl update` to update the cluster configuration file to [configure a registry mirror](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror#create_clusters_from_the_registry_mirror). The cluster then has `spec.nodeConfig.registryMirrors` populated after reconciliation. 

If you then attempt to make changes to the cluster using the cluster configuration with the `kubectl apply -f` command, the `spec.nodeConfig.registryMirrors` populated by the reconciler on the cluster is removed. This behavior happens because the configuration doesn't exist in the cluster configuration spec, but it does in the cluster. 

###  gcloud CLI 

  1. Specify only the flags for the configuration that you want to modify.

  2. Run the applicable update command:

     * Admin clusters: [`gcloud container bare-metal admin-clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update)

     * User clusters: [`gcloud container bare-metal clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update).

     * Node pools on a user cluster: [`gcloud container bare-metal node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update)




### Terraform

  1. Change the values of the applicable fields in the Terraform configuration file that you used to create the cluster or node pool. See the Terraform reference documentation for detailed field descriptions:

     * [`google_gkeonprem_bare_metal_admin_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_admin_cluster)

     * [`google_gkeonprem_bare_metal_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster)

     * [`google_gkeonprem_bare_metal_node_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_node_pool)

  2. Update the configuration by running the `terraform apply` command.




The following sections outline some common examples for updating an existing cluster.

## Add or remove nodes in a cluster

A [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) is a group of nodes within a cluster that have the same configuration. Keep in mind that a node always belongs to a node pool. To add a new node to a cluster, you need to add it to a particular node pool. Removing a node from a node pool amounts to removing the node from the cluster altogether.

There are three kinds of node pools in Google Distributed Cloud: control plane, load balancer, and worker node pools. The following sections describe how to add or remove nodes from each kind of node pool.

### `bmctl`

You add or remove a node from a node pool by adding or removing the IP address of the node in a specific section of the cluster configuration file. The following list shows which section to edit for a given node pool:

  * Worker node pool: add or remove the IP address of the node in the `spec.nodes` section of the `NodePool` spec.
  * Control plane node pool: add or remove the IP address of the node in the `spec.controlPlane.nodePoolSpec.nodes` section of the `Cluster` spec.
  * Load balancer node pool: add or remove the IP address of the node in the `spec.loadBalancer.nodePoolSpec.nodes` section of the `Cluster` spec.



#### Example: remove a worker node

Here's a sample cluster configuration file that shows the specifications of two worker nodes:
    
    
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: nodepool1
      namespace: cluster-cluster1
    spec:
      clusterName: cluster1
      nodes:
      - address: 192.0.2.1
      - address: 192.0.2.2
    

To remove a node:

  1. (Optional) If the node that you're removing is running critical Pods, first put the node into [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/maintenance-mode).

You can monitor the node draining process for worker nodes by viewing the `status.nodesDrained` and `status.nodesDraining` fields on the `NodePool` resource.

  2. Edit the cluster configuration file to _delete_ the IP address entry for the node.

  3. Update the cluster:
         
         bmctl update cluster1 \
             --kubeconfig=ADMIN_KUBECONFIG
         




###  gcloud CLI 

You use an `update` command to add or remove nodes. The `update` command that you use and the flag in which you specify the IP address depends on the type of node pool that you want to update:

  * Worker node pool: Run `gcloud container bare-metal node-pools update` and specify the IP address in the flag `--node-configs 'node-ip=IP_ADDRESS'`.

  * Control plane node pool on an admin cluster: Run `gcloud container bare-metal admin-clusters update` and specify the IP address in the flag `--control-plane-node-configs 'node-ip=IP_ADDRESS'`.

  * Control plane node pool on a user cluster: Run `gcloud container bare-metal clusters update` and specify the IP address in the flag `--control-plane-node-configs 'node-ip=IP_ADDRESS'`.

  * Load balancer node pool: Run `gcloud container bare-metal clusters update` and specify the IP address in the flag `--metal-lb-load-balancer-node-configs 'node-ip=IP_ADDRESS'` or  
`--bgp-load-balancer-node-configs 'node-ip=IP_ADDRESS'`




The flag in which you specify the IP address only accepts one `node-ip`. You include the flag for each IP address in the node pool.

The `update` commands replace all IP addresses with the IP addresses that you specify. To add a node, include the IP addresses of the existing nodes and the IP address of the new node in the `update` command. Similarly, you remove nodes by only including the IP addresses of the nodes that you want to keep.

#### Example: remove a worker node

This section shows how to remove a worker node from a node pool using example data. Additional gcloud CLI commands that you might find useful are also included in the following steps.

  1. (Optional) If the node that you're removing is running critical Pods, first put the node into [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/maintenance-mode).

You can monitor the node draining process for worker nodes by viewing the `status.nodesDrained` and `status.nodesDraining` fields on the `NodePool` resource.

  2. Run the `list` command to list all the node pools in the cluster:
         
         gcloud container bare-metal node-pools list \
             --cluster=abm-user-cluster1 \
             --project=example-project-12345 \
             --location=us-central1
         

The output is similar to the following:
         
         NAME         LOCATION     STATE
         node-pool-1  us-central1  RUNNING
         node-pool-2  asia-east1   RUNNING
         

  3. Run the `describe` command to list all the IP addresses in the node pool:
         
         gcloud container bare-metal node-pools describe node-pool-1 \
             --cluster=abm-user-cluster1 \
             --project=example-project-12345 \
             --location=us-central1
         

The following example output is truncated for readability:
         
         annotations:
           ...
           baremetal.cluster.gke.io/version: 1.36
         ...
         name: projects/example-project-12345/locations/us-central1/bareMetalClusters/abm-user-cluster1/bareMetalNodePools/node-pool-1
         nodePoolConfig:
           nodeConfigs:
           - nodeIp: 192.0.2.1
           - nodeIp: 192.0.2.2
           operatingSystem: LINUX
         state: RUNNING
         ...
         

Note the following in the example output:

     * The `name` field contains the fully-qualified name of the node pool. When specifying the node pool name in a command, you can either specify the fully-qualified name, or the node pool name, for example, `node-pool-1`, along with the `--cluster`, `--project`, and the `--location` flags.

     * The `nodeConfigs` section contains two `nodeIp` fields with the IP addresses of the nodes.

  4. Run the following command to remove the node with the IP address 192.0.2.1:
         
         gcloud container bare-metal node-pools update node-pool-1 \
             --cluster=abm-user-cluster1 \
             --project=example-project-12345 \
             --location=us-central1 \
             --node-configs='node-ip=192.0.2.2'
         

The `update` command replaces all IP addresses with the IP addresses that you specify. Because 192.0.2.1 isn't included, the node is removed.

The output of the command is similar to the following:
         
         Waiting for operation [projects/example-project-12345/locations/us-central1/operations/operation-1697154681749-6078d9def4030-76686d6e-9fcb1de9] to complete
         

In the example output, the string `operation-1697154681749-6078d9def4030-76686d6e-9fcb1de9` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation by running the following command in another terminal window:
         
         gcloud container bare-metal operations describe operation-1697154681749-6078d9def4030-76686d6e-9fcb1de9 \
             --project= example-project-12345 \
             --location=us-central1
         

You can rerun the command every so often to check the status.




If the node removal fails, you can force its removal from the cluster. For details, see [Reset a failed node in Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).

## Replace HA control plane nodes

### `bmctl`

You can use `bmctl` to replace high availability (HA) control plane nodes in all cluster types.

You replace a node in a cluster by performing the following steps:

  1. Remove the node's IP address from the cluster configuration file.
  2. Update the cluster.
  3. Check the status of nodes in the cluster.
  4. Add a new node's IP address to the same cluster configuration file.
  5. Update the cluster.



#### Example: replace a HA control plane node

Here's a sample cluster configuration file that shows three control plane nodes in a user cluster:
    
    
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
    name: user-cluster
    namespace: cluster-user-cluster
    spec:
      controlPlane:
      nodePoolSpec:
        nodes:
        - address: 192.0.2.11
        - address: 192.0.2.12
        - address: 192.0.2.13
    

To replace the last node listed in the `spec.controlPlane.nodePoolSpec.nodes` section, perform the following steps:

  1. Remove the node by deleting its IP address entry in the cluster configuration file. After making this change, the cluster configuration file should look something like this:
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
         name: user-cluster
         namespace: cluster-user-cluster
         spec:
           controlPlane:
           nodePoolSpec:
             nodes:
             - address: 192.0.2.11
             - address: 192.0.2.12
         

  2. Update the cluster by running the following command:
         
         bmctl update cluster -c CLUSTER_NAME \
           --kubeconfig=KUBECONFIG
         

Make the following changes:

     * Replace CLUSTER_NAME with the name of the cluster you want to update.
     * If the cluster is a self-managing cluster (such as admin or standalone cluster), replace KUBECONFIG with the path to the cluster's kubeconfig file. If the cluster is a user cluster, as it is in this example, replace KUBECONFIG with the path to the **admin** cluster's kubeconfig file.
  3. After the `bmctl update` command has executed successfully, it takes some time to complete the `machine-preflight` and `machine-init` jobs. You can view the status of nodes and their respective node pools by running the commands described in the Verify your updates section of this document. After the node pool and nodes are in a ready state, you can proceed to the next step.

  4. Add a new control plane node to the node pool by adding the IP address of the new control plane node to the `spec.controlPlane.nodePoolSpec.nodes` section of the cluster configuration file. After making this change, the cluster configuration file should look something like this:
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
         name: user-cluster
         namespace: cluster-user-cluster
         spec:
           controlPlane:
           nodePoolSpec:
             nodes:
             - address: 192.0.2.11
             - address: 192.0.2.12
             - address: 192.0.2.14
         

  5. Update the cluster by running the following command:
         
         bmctl update cluster -c CLUSTER_NAME \
           --kubeconfig=KUBECONFIG
         




###  gcloud CLI 

You can use the gcloud CLI to replace high availability (HA) control plane nodes in admin and user clusters.

You replace a node in a cluster by performing the following steps:

  1. Remove the node's IP address by running the applicable `update` command:

     * User cluster: `gcloud container bare-metal clusters update`
     * Admin cluster: `gcloud container bare-metal admin-clusters update`
  2. Check the status of the node removal in the cluster by running `gcloud container bare-metal operations describe OPERATION_ID`.

  3. Add the new node's IP address by running the applicable `update` command.




#### Example: replace a HA control plane node

This section shows how to replace a control plane from a cluster using example data. Additional gcloud CLI commands that you might find useful are also included in the following steps.

  1. Run the `list` command to list all the user clusters in a Google Cloud project:
         
         gcloud container bare-metal clusters list \
             --project=example-project-12345 \
             --location=-
         

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to a [specific region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api).

The output is similar to the following:
         
         NAME                 LOCATION      VERSION   ADMIN_CLUSTER        STATE
         abm-user-cluster1a   us-central1   1.36      abm-admin-cluster1   RUNNING
         abm-user-cluster1b   europe-west1  1.36      abm-admin-cluster1   RUNNING
         

  2. Run the `describe` command on the cluster:
         
         gcloud container bare-metal clusters describe abm-user-cluster1  \
             --project=example-project-12345 \
             --location=us-central1
         

The example output is truncated for readability:
         
         ...
         controlPlane:
           controlPlaneNodePoolConfig:
             nodePoolConfig:
               nodeConfigs:
               - nodeIp: 192.0.2.11
               - nodeIp: 192.0.2.12
               - nodeIp: 192.0.2.13
               operatingSystem: LINUX
         ...
         name: projects/example-project-1234567/locations/us-central1/bareMetalClusters/abm-user-cluster1a
         ...
         

Note the following in the example output:

     * The `name` field contains the fully-qualified name of the cluster. When specifying the cluster name in a command, you can either specify the fully-qualified name, or the cluster name, for example, `abm-user-cluster1a`, along with the `--project` and the `--location flags`.

     * The `nodeConfigs` section contains three `nodeIp` fields with the IP addresses of the control plane nodes.

  3. Remove the node with the IP address `192.0.2.13`:
         
         gcloud container bare-metal cluster update abm-user-cluster1a \
             --project=example-project-12345 \
             --location=us-central1 \
             --control-plane-node-configs 'node-ip=192.0.2.11'
             --control-plane-node-configs 'node-ip=192.0.2.12'
         

The output of the command is similar to the following:
         
         Waiting for operation [projects/example-project-12345/locations/us-central1/operations/operation-1956154681749-6078d9def4030-76686d6e-9fcb1d7] to complete
         

In the example output, the string `operation-1956154681749-6078d9def4030-76686d6e-9fcb1de7` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation by running the following command in another terminal window:
         
         gcloud container bare-metal operations describe operation-1956154681749-6078d9def4030-76686d6e-9fcb1de7 \
             --project= example-project-12345 \
             --location=us-central1
         

You can rerun the command every so often to check the status.

  4. Add the new node with the IP address `192.0.2.14`:
         
         gcloud container bare-metal cluster update abm-user-cluster1a \
             --project=example-project-12345 \
             --location=us-central1 \
             --control-plane-node-configs 'node-ip=192.0.2.11'
             --control-plane-node-configs 'node-ip=192.0.2.12'
             --control-plane-node-configs 'node-ip=192.0.2.14'
         




## Verify your updates

### `kubectl`

You can view the status of nodes and their respective node pools with the `kubectl get` command.

For example, the following command shows the status of the node pools in the cluster namespace `cluster-my-cluster`:
    
    
    kubectl -n cluster-my-cluster get nodepools.baremetal.cluster.gke.io
    

The system returns results similar to the following:
    
    
    NAME                    READY   RECONCILING   STALLED   UNDERMAINTENANCE   UNKNOWN
    cluster-my-cluster      3       0             0         0                  0
    cluster-my-cluster-lb   2       0             0         0                  0
    np1                     3       0             0         0                  0
    

`Reconciling=1` means that the reconciliation step is still in progress. You should wait until the status changes to `Reconciling=0`.

You can also check status of nodes in the a cluster by running following command:
    
    
    kubectl get nodes --kubeconfig=KUBECONFIG
    

###  gcloud CLI 

As described previously, after running an `update` command, you can check the status of the operation using `gcloud container bare-metal operations describe OPERATIONS_ID`. The output of the command gives the status of the nodes, for example:
    
    
      ...
      metrics:
      - intValue: '1'
        metric: NODES_RECONCILING
      - intValue: '2'
        metric: NODES_HEALTHY
      - intValue: '0'
        metric: NODES_FAILED
      - intValue: '0'
        metric: NODES_IN_MAINTENANCE
      - intValue: '3'
        metric: NODES_TOTAL
      stage: HEALTH_CHECK
    ...
    

No matter which tool you use to update a node pool, you can get the current status of a node pool by running the applicable `describe` command as shown previously.

If you need more information about how to diagnose your clusters, see [Create snapshots for diagnosing clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/bmctl-snapshot).

## Load balancer address pools

### bmctl

The [`addressPools`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#loadbalancer-addresspools) section contains fields for specifying load-balancing pools for the MetalLB and Border Gateway Protocol (BGP) bundled load balancers. You can add more load-balancing address pools at any time, but you can't remove any existing address pools. Starting with Google Distributed Cloud version 1.16.0, you can modify the values for `addressPools.avoidBuggyIPs` and `addressPools.manualAssign` at any time.
    
    
    addressPools:
    - name: pool1
      addresses:
      - 198.51.100.0-198.51.100.4
      - 198.51.100.240/28
    **- name: pool2
      addresses:
      - 198.51.100.224/28**
    

###  gcloud CLI 

You can add more load-balancing address pools at any time for the bundled load balancers, but you can't remove any existing address pools. The flag that you specify in `gcloud container bare-metal clusters update` to add an address pool depends on the type of bundled load balancer:

  * MetalLB (layer 2): Use the `--metal-lb-address-pools` flag.
  * Border Gateway Protocol (BGP): Use the `--bgp-address-pools` flag.



The value for the flags have the following format:
    
    
    'pool=NAME,avoid-buggy-ips=True|False,manual-assign=True|False,addresses=IP_ADDRESS_RANGE_1;IP_ADDRESS_RANGE_2;...' \
    

The value has segments that start with the keywords `pool`, `avoid-buggy-ip`, `manual-assign`, and `addresses`. Separate each segment with a comma.

  * `pool`: A name of your choice for the pool.

  * `avoid-buggy-ips`: If you set this to `True`, the IP address management (IPAM) controller won't assign IP addresses ending in `.0` or `.255` to Services. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses. If not specified, defaults to `False`. Starting with Google Distributed Cloud version 1.16.0, you can modify this value in an existing address pool.

  * `manual-assign`: If you don't want the IPAM controller to automatically assign IP addresses from this pool to Services, set this to `True`. Then a developer can create a Service of type `LoadBalancer` and manually specify one of the addresses from the pool. If not specified, `manual-assign` is set to `False`. Starting with Google Distributed Cloud version 1.16.0, you can modify this value in an existing address pool.

  * In the list of `addresses`: Each address must be a range either in [CIDR](https://tools.ietf.org/html/rfc4632) or hyphenated-range format. To specify a single IP address in a pool (such as for the ingress VIP), use `/32` in CIDR notation (for example, 192.0.2.1/32).




Note the following syntax rules:

  * Surround the entire value in single quotes.
  * Whitespace isn't allowed.
  * Separate each IP address range with a semicolon.



You can specify more than one instance of the flag, as shown in the following example:
    
    
    --metal-lb-address-pools='pool=pool2,avoid-buggy-ips=False,manual-assign=True,addresses=198.51.100.0/30;198.51.100.64-198.51.100.72'
    --metal-lb-address-pools='pool=pool3,avoid-buggy-ips=True,manual-assign=True,addresses=203.0.113.0/28'
    

For more information about load balancer address pools, see [loadBalancer.addressPools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/bundled-lb#address-pools) in Configure bundled load balancing.

## Prevent inadvertent cluster deletion

### `bmctl`

If you add the `baremetal.cluster.gke.io/prevent-deletion: "true"` annotation to your cluster configuration file, you are prevented from deleting the cluster. For example, running `kubectl delete cluster` or `bmctl reset cluster` produces an error.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: ci-10c3c6f4d9c698e
      namespace: cluster-ci-10c3c6f4d9c698e
      annotations:
        **baremetal.cluster.gke.io/prevent-deletion : "true"**
    spec:
      clusterNetwork:
    

###  gcloud CLI 

If you specify the `--add-annotations` flag with the value `baremetal.cluster.gke.io/prevent-deletion="true"`, you are prevented from deleting the cluster. For example:

  1. Add the annotation to prevent accidental cluster deletion:
         
         gcloud container bare-metal clusters update abm-user-cluster1a \
             --project=example-project-12345 \
             --location=us-central1 \
             --add-annotations=baremetal.cluster.gke.io/prevent-deletion="true"
         

  2. Attempt to delete the user cluster:
         
         gcloud container bare-metal clusters delete abm-user-cluster1a \
             --project=example-project-12345 \
             --location=us-central1 \
             --force \
             --allow-missing
         

The response from the command is similar to the following:
         
         ERROR: (gcloud.container.bare-metal.clusters.delete) INVALID_ARGUMENT:
         invalid request: admission webhook "vcluster.kb.io" denied the request:
         annotations[baremetal.cluster.gke.io/prevent-deletion]: Invalid value:
         "true": Annotation "baremetal.cluster.gke.io/prevent-deletion" should be
         removed in order to delete this cluster
         

To remove the annotation, specify `--remove-annotations=baremetal.cluster.gke.io/prevent-deletion="true"` in the `update` command.




## Bypass preflight checks

This feature is available only with `bmctl update`.

The default value of the [`bypassPreflightCheck`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#bypasspreflightcheck) field is `false`. If you set this field to `true` in the cluster configuration file, the internal preflight checks are ignored when you apply resources to existing clusters.
    
    
      apiVersion: baremetal.cluster.gke.io/v1
      kind: Cluster
      metadata:
        name: cluster1
        namespace: cluster-cluster1
        annotations:
          baremetal.cluster.gke.io/private-mode: "true"
      spec:
        bypassPreflightCheck: true
    

## Add or remove cluster administrators

### `bmctl`

You can add or remove a user or service account as a cluster administrator for a user cluster by specifying email addresses in the [`clusterSecurity.authorization.clusterAdmin.gcpAccounts`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clustersecurity-authorization-clusteradmin-gcpaccounts) section of the cluster configuration file. The accounts are granted the cluster-admin role on the cluster, providing full access to the cluster.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
    spec:
      clusterSecurity:
        authorization:
          clusterAdmin:
            gcpAccounts:
            - alex@example.com
            - hao@example.com
            - my-sa@example-project-12345.iam.gserviceaccount.com
    

When updating a user cluster to add an account, be sure to include all accounts in the list (both existing and new accounts) because `bmctl update` overwrites the list with what you specify in the configuration file. To remove an account, remove it from the cluster configuration file and run `bmctl update`.

###  gcloud CLI 

You can add or remove a user or service account as a cluster administrator by specifying an email addresses in the `--admin-users` flag. The flag accepts only one email address. To add multiple users, specify one account in each flag, for example:
    
    
    gcloud container bare-metal clusters update abm-user-cluster1a \
        --project=example-project-12345 \
        --location=us-central1 \
        --admin-users=alex@example.com \
        --admin-users=hao@example.com
        --admin-users=my-sa@example-project-12345.iam.gserviceaccount.com
    

The `update` command overwrites the whole grant list. Specify all existing and new users who you want to be cluster administrators.

## Set a login user

You can specify a non-root username that you want to use for passwordless `sudo` capability access to the node machines in your cluster. Your SSH key, [`sshPrivateKeyPath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#sshprivatekeypath), must work for the specified user. The cluster create and update operations check that node machines can be accessed with the specified user and SSH key.

### `bmctl`
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
      annotations:
        baremetal.cluster.gke.io/private-mode: "true"
    spec:
      nodeAccess:
        loginUser: abm
    

###  gcloud CLI 

You specify the user that you want to use to access node machines in the `--login-user` flag, for example:
    
    
    gcloud container bare-metal clusters update abm-user-cluster1a \
        --project=example-project-12345 \
        --location=us-central1 \
        --login-user=abm
    

To enable passwordless `sudo` access for a user, follow these steps on each cluster node machine:

  1. Use `sudo visudo` to open the sudoers file for editing:
         
         sudo visudo -f /etc/sudoers
         

The `visudo` command locks the sudoers file to prevent simultaneous edits and validates the syntax of the file upon saving.

  2. For your login user, add an entry to the sudoers file like the following:
         
         USERNAME ALL=(ALL) NOPASSWD: ALL
         

  3. Close and save the file.

  4. To run commands with the privileges of your login user, run the following command:
         
         su - USERNAME
         

  5. To verify that a password isn't required for your login user to run `sudo` commands, run the following `sudo` command:
         
         sudo ip a
         




## Advanced networking

You configure advanced networking features in various custom resources after the cluster is created. To use the custom resources and related networking features, you must enable advanced networking when you **create** your cluster.

### `bmctl`

Set [`clusterNetwork.advancedNetworking`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusternetwork-advancednetworking) to `true`in the cluster configuration when you create your cluster:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
    spec:
      clusterNetwork:
        ...
        advancedNetworking: true
        ...
    

###  gcloud CLI 

Include the `--enable-advanced-networking` flag in the [`gcloud container bare-metal clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create) command when you create your cluster.

After the cluster is created with advanced networking enabled, you can configure the custom resources described in this section using `kubectl apply`.

**Note:** The `gcloud container bare-metal clusters update` command doesn't support configuring these custom resources.

### `NetworkGatewayGroup`

The `NetworkGatewayGroup` custom resource is used to provide floating IP addresses for advanced networking features, such as the [egress NAT gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/egress-nat) or the [bundled load-balancing feature with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp).
    
    
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
      name: default
      namespace: cluster-bm
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.2.100
    

### BGP load balancing

You configure Border Gateway Protocol (BGP) load balancing in the cluster resource and other custom resources. The `gcloud container bare-metal clusters create` and the `update` commands support configuring BGP in the cluster resource, but not the custom resources.

When you configure bundled load balancers with BGP, the data plane load balancing uses, by default, the same external peers that were specified for control plane peering. Alternatively, you can configure the data plane load balancing separately, using the `BGPLoadBalancer` custom resource and the `BGPPeer` custom resource. For more information, see [Configure bundled load balancers with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp).

#### `BGPLoadBalancer`
    
    
    apiVersion: networking.gke.io/v1
    kind: BGPLoadBalancer
    metadata:
      name: default
      namespace: cluster-bm
    spec:
      peerSelector:
        cluster.baremetal.gke.io/default-peer: "true"
    

#### `BGPPeer`
    
    
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer1
      namespace: cluster-bm
      labels:
        cluster.baremetal.gke.io/default-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.3.254
      sessions: 2
    

## Increase service network range

To create more services than the initial limit, you can reduce the IPv4 service CIDR mask to increase the service network of your cluster. Reducing the mask (the value after "/") results in a bigger network range. You can only _increase_ the range of the IPv4 service CIDR. The network range can't be reduced, which means the mask (the value after "/") can't be increased.

### `bmctl`
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
    spec:
      ...
      clusterNetwork:
        services:
          cidrBlocks:
            - 192.0.2.0/**14**
      ...
    

###  gcloud CLI 

To increase the range of the IPv4 service CIDR on a user cluster, specify the new range in the `--island-mode-service-address-cidr-blocks` flag.
    
    
    gcloud container bare-metal clusters update cluster1 \
        --project=example-project-12345 \
        --location=us-central1 \
        --island-mode-service-address-cidr-blocks=192.0.2.0/**14**
    

Starting with version 1.34, you will see new `ServiceCIDR` resources in your cluster. These resources are used by the Kubernetes control plane to manage the IP address ranges for your services.

Don't attempt to create or modify `ServiceCIDR` resources manually. They are managed automatically by the cluster operator based on the values in your `Cluster` custom resource. To prevent networking issues, any direct manual edits are blocked, and you will receive an error message similar to the following:
    
    
    The servicecidrs "my-cidr" is invalid: : This resource is managed by cluster
    operator and cannot be modified directly by users.
    

## Configure kubelet image pull settings

The kubelet runs on each node of your cluster. The kubelet is responsible for monitoring containers on a node and making sure they are healthy. When needed, the kubelet queries and pulls images from the Artifact Registry.

Updating your kubelet configurations manually and keeping them synchronized across all of your cluster nodes can be challenging. To make matters worse, manual kubelet configuration changes on your nodes are lost when you upgrade your cluster.

To help make synchronized updates easier and persistent, Google Distributed Cloud lets you specify some kubelet settings for each of your cluster node pools: control plane nodes, load balancer nodes, and worker nodes. The settings apply for all nodes in a given pool and persist through cluster upgrades. The fields for these settings are mutable, so you can update them at any time, not just during cluster creation.

### `bmctl`

The following supported fields control Artifact Registry pull operations for kubelet:

**Warning:** Setting `registryBurst` or `registryPullQPS` to a negative value results in update job failures for the kubelet configuration. To fix the issue, either update these fields to positive values or remove them from the spec. If the update job is left to fail for a long time, it can fill up the machine disk space with kubelet configuration backup files. You can find these backup files in `/var/lib/kubelet/config.yaml.bkup.*`. If these backup files are taking up too much disk space, you can remove them.

  * `registryBurst` (default: 10)
  * `registryPullQPS` (default: 5)
  * `serializeImagePulls` (default: true)



For more information about each of the kubelet configuration fields, see the [Cluster configuration field reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref).

You can specify these fields in `kubeletConfig` sections of the Cluster spec and the NodePool spec for the following pools of nodes:

  * Cluster spec:
  * Control plane nodes [`spec.controlPlane.nodePoolSpec.kubeletConfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#controlplane-nodepoolspec-kubeletconfig)
  * Load balancer nodes [`spec.loadBalancer.nodePoolSpec.kubeletConfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#loadbalancer-nodepoolspec-kubeletconfig)
  * NodePool spec:
  * Worker nodes [`spec.kubeletConfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#kubeletconfig)



The following example shows the added fields with their **default values** in the cluster configuration file. Note that the annotation `preview.baremetal.cluster.gke.io/custom-kubelet: "enable"` is required.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
      annotations:
        **preview.baremetal.cluster.gke.io/custom-kubelet : "enable"**
    spec:
      ...
      controlPlane:
        nodePoolSpec:**      kubeletConfig:
            registryBurst: 10
            registryPullQPS: 5
            serializeImagePulls: true**
      ...
      loadBalancer:
        nodePoolSpec:**      kubeletConfig:
            registryBurst: 10
            registryPullQPS: 5
            serializeImagePulls: true**
      ...
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: node-pool-new
      namespace: cluster-cluster1
    spec:
      clusterName: cluster1
      ...**  kubeletConfig:
        registryBurst: 10
        registryPullQPS: 5
        serializeImagePulls: true**
    

In each case, the setting applies to all nodes in the pool.

###  gcloud CLI 

The following flags control Artifact Registry pull operations for kubelet:

  * Control plane nodes

    * [\--control-plane-registry-burst](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--control-plane-registry-burst)
    * [\--control-plane-registry-pull-qps](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--control-plane-registry-pull-qps)
    * [\--disable-control-plane-serialize-image-pulls](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--disable-control-plane-serialize-image-pulls)
    * [\--enable-control-plane-serialize-image-pulls](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-control-plane-serialize-image-pulls)
  * Load balancer nodes

    * [\--bgp-load-balancer-registry-burst](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-load-balancer-registry-burst)
    * [\--bgp-load-balancer-registry-pull-qps](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-load-balancer-registry-pull-qps)
    * [\--disable-bgp-load-balancer-serialize-image-pulls](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--disable-bgp-load-balancer-serialize-image-pulls)
    * [\--enable-bgp-load-balancer-serialize-image-pulls](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-bgp-load-balancer-serialize-image-pulls)
    * [\--metal-lb-load-balancer-registry-burst](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-load-balancer-registry-burst)
    * [\--metal-lb-load-balancer-registry-pull-qps](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-load-balancer-registry-pull-qps)
    * [\--disable-metal-lb-load-balancer-serialize-image-pull](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--disable-metal-lb-load-balancer-serialize-image-pull)
    * [\--enable-metal-lb-load-balancer-serialize-image-pulls](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-metal-lb-load-balancer-serialize-image-pulls)
  * Worker nodes

    * [\--registry-burst](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--registry-burst)
    * [\--registry-pull-qps](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--registry-pull-qps)
    * [\--disable-serialize-image-pulls](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--disable-serialize-image-pulls)
    * [\--enable-serialize-image-pulls](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--enable-serialize-image-pulls)

**Warning:** Setting the `*-registryburst` or `*-registry-pull-qps` flags to a negative value results in update job failures for the kubelet configuration. To fix the issue, update these fields to positive values. If the update job is left to fail for a long time, it can fill up the machine disk space with kubelet configuration backup files. You can find these backup files in `/var/lib/kubelet/config.yaml.bkup.*`. If these backup files are taking up too much disk space, you can remove them.

### How to use

Here are some considerations for tuning image pulls:

  * Since images are pulled in series by default, an image pull that takes a long time can delay all other image pulls scheduled on a node. Delayed image pulls can block the upgrade process (especially when new Google Distributed Cloud images need to be deployed on a node). If you're affected by image pull delays, you can disable serialize image pulls to allow parallel image pulls.

  * If you're encountering image pull throttling errors, such as `pull QPS exceeded`, you may want to increase `*-registry-pull-qps` and `*-registry-burst` to increase image pull throughput. These two fields adjust the pull rate and queue size and may help to address other throttling related issues. **Negative values aren't allowed.**




## Keepalived customization

Starting in version 1.32, Google Distributed Cloud provides some customization of the Keepalived configuration. With bundled load balancing, the control plane load balancer serves the control plane virtual IP (VIP) address. Google Distributed Cloud runs Keepalived and HAProxy as Kubernetes static Pods on the load balancer nodes to announce the control plane VIP. Keepalived uses the Virtual Router Redundancy Protocol (VRRP) on the load balancer nodes for high availability.

Version 1.32 and later clusters have the following Keepalived customizations:

  * For high availability control planes, Google Distributed Cloud automatically configures the Keepalived VRRP configuration to make failover behaviour deterministic and prevent interleaving of ARP replies with different MAC addresses. This is accomplished by configuring each Keepalived instance with a different `priority` value.

  * Google Distributed Cloud lets you specify the number of gratuitous ARP (GARP) messages to send at a time after a control plane node transitions to the role of the master server. To change the number of GARP messages to send, add the [`controlPlane.loadBalancer.keepalivedVRRPGARPMasterRepeat`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#controlplane-loadbalancer-keepalivedvrrpgarpmasterrepeat) field to the cluster configuration file, set it to the new value, and update your cluster. This value maps to the `vrrp_garp_master_repeat` setting for Keepalived. The default value is 5.

The following example shows how to specify `keepalivedVRRPGARPMasterRepeat` in the cluster configuration file:
        
        apiVersion: baremetal.cluster.gke.io/v1
        kind: Cluster
        metadata:
          name: hybrid-ha-lb
          namespace: cluster-hybrid-ha-lb
        spec:
          type: hybrid
          profile: default
          anthosBareMetalVersion: 1.36
          gkeConnect:
            projectID: project-fleet**  controlPlane:
            loadBalancer:
              keepalivedVRRPGARPMasterRepeat: 1**
            nodePoolSpec:
              nodes:
              - address: 10.200.0.2
              - address: 10.200.0.3
              - address: 10.200.0.4
          ...
        




## Install or uninstall the bundled NVIDIA GPU Operator

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) lets you run GPU-related workloads in your clusters. Starting with Google Distributed Cloud version 1.33.0, clusters are bundled with a complete NVIDIA GPU Operator stack to provide a managed solution for handling the NVIDIA software components needed to provision GPUs on your cluster worker nodes. **Important:** Don't install the bundled NVIDIA GPU Operator if you intend to manually install and maintain the NVIDIA GPU Operator yourself. If you prefer to install and manage the NVIDIA GPU Operator manually, see [Set up and use NVIDIA GPUs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use) for instructions.

### Prerequisites

Before installing the the bundled NVIDIA GPU Operator, make sure your environment meets the following requirements:

  * **Operational cluster** : You have a functional bare metal cluster created with Google Distributed Cloud.

  * **NVIDIA GPUs** : The NVIDIA GPUs are installed on your cluster worker nodes. The following section for installing the NVIDIA GPU Operator includes steps to verify that the GPUs are installed properly and recognized by your operating system.

  * **Compatible NVIDIA driver version** : The NVIDIA driver version you use must be compatible with your GPU, your operating system, and the CUDA version your applications use. For more information, see Version information.

You have the following NVIDIA driver installation options:

    * Use the NVIDIA driver preinstalled in your operating system image.

    * Use the instructions in the [NVIDIA Driver Installation Quickstart Guide](https://docs.nvidia.com/datacenter/tesla/pdf/NVIDIA_Driver_Installation_Quickstart.pdf) to manually install the NVIDIA driver.

The NVIDIA GPU driver must be installed and ready before you enable the bundled NVIDIA GPU Operator.




### Version information

This section contains software version information for the bundled NVIDIA GPU Operator.

#### Software component versions

Google Distributed Cloud release version 1.33 bundles version 25.3.1 of the NVIDIA GPU Operator. In Google Distributed Cloud, the bundle contains the following images (with CDI enabled by default):

  * NVIDIA Container Toolkit version v1.17.9
  * NVIDIA DCGM Exporter v3.3.9-3.6.1
  * NVIDIA Kubernetes Device Plugin v0.17.1
  * Node Feature Discovery v0.17.2



The image versions bundled with Google Distributed Cloud release 1.33 might not match exactly with the software component versions listed in the [25.3.1 release notes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/25.3.1/release-notes.html).

#### Driver compatibility

See [Platform Support for version 25.3.1](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/25.3.1/platform-support.html) on the NVIDIA Docs Hub for drivers compatibility information.

#### Updating the bundled NVIDIA GPU Operator

If you have installed NVIDIA GPU Operator on your cluster, when you upgrade to a new minor version, the latest bundled version of the NVIDIA GPU Operator is installed.

### Install the bundled operator

While the bundled NVIDIA GPU Operator is in Preview, you install it by using `bmctl update` to add the following annotation to the cluster that has GPU nodes:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
      annotations:**    preview.baremetal.cluster.gke.io/nvidia-gpu-operator: "enable"**
    spec:
      ...
    

The NVIDIA GPU Operator stack is installed to the cluster when the annotation applied.

### Uninstall the bundled operator

While the bundled NVIDIA GPU Operator is in Preview, you uninstall it by using `bmctl update` to remove the following annotation from the cluster that has GPU nodes:
    
    
    preview.baremetal.cluster.gke.io/nvidia-gpu-operator: "enable"
    

All components of the NVIDIA GPU Operator stack are removed from the cluster when the annotation is removed.

## Enable dynamic resource allocation

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Dynamic resource allocation is a Kubernetes API that lets you request and share generic resources, such as GPUs, among Pods and containers. Third-party drivers manage these resources. This capability helps you run AI workloads by dynamically and precisely allocating the GPU resources within your bare metal clusters, improving resource utilization and performance for demanding workloads. 

Dynamic resource allocation is available for preview for version 1.33 and later clusters. The following instructions describe how to configure your cluster to use dynamic resource allocation. After it's enabled, you can configure your GPU workloads to use dynamic resource allocation.

Configure your cluster to enable dynamic resource allocation:

  1. Edit your cluster configuration file to include the `preview.baremetal.cluster.gke.io/dynamic-resource-allocation: "enable"` preview annotation and add `DynamicResourceAllocation: true` under `featureGates` in the `kubeletConfig` section:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: dra
           namespace: cluster-dra
           annotations:**    preview.baremetal.cluster.gke.io/dynamic-resource-allocation: "enable"**
         spec:
           controlPlane:
             nodePoolSpec:
               kubeletConfig:
                 featureGates:**          DynamicResourceAllocation: true**
         # ... other cluster configuration
         

  2. Update the cluster by running the `bmctl update` command:
         
         bmctl update cluster -c CLUSTER_NAME \
             --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the ame of the user cluster you are updating.

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

After you apply this configuration, the `READY` field for your bare metal machines might switch between `True` and `False` multiple times. Wait for the `READY` field to stabilize on `True` before proceeding.

  3. To enable the `DynamicResourceAllocation` feature gate in node pools that have nodes with GPUs, set `DynamicResourceAllocation` to `true` in the `featureGates` section of the `kubeletConfig` section of the NodePool spec:

For instructions to add and update a node pool, see [Manage node pools in a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/add-remove-node-pools).
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: np
           namespace: cluster-dra
         spec:
           clusterName: dra
           kubeletConfig:
             featureGates:**      DynamicResourceAllocation: true**
           nodes:
         # ... other node pool configuration
         

After you have added or updated the node pool, wait for all bare metal machines in the node pool to reach a `Ready` status.

  4. To check the status of your cluster bare metal machines, use the following command:
         
         kubectl get baremetalmachines --kubeconfig ADMIN_KUBECONFIG -A
         

When the bare metal machines are ready, the response should look similar to the following sample response:
         
         NAMESPACE          NAME         CLUSTER    READY   INSTANCEID               MACHINE      ABM VERSION        DESIRED ABM VERSION
         cluster-admin      10.200.0.2   dra        true    baremetal://10.200.0.2   10.200.0.2    1.33.0-gke.793   1.33.0-gke.793
         cluster-user-dra   10.200.0.6   user-dra   true    baremetal://10.200.0.6   10.200.0.6    1.33.0-gke.793   1.33.0-gke.793
         cluster-user-dra   10.200.0.7   user-dra   true    baremetal://10.200.0.7   10.200.0.7    1.33.0-gke.793   1.33.0-gke.793
         cluster-user-dra   10.200.0.8   user-dra   true    baremetal://10.200.0.8   10.200.0.8    1.33.0-gke.793   1.33.0-gke.793
         




### Limitations

The bundled NVIDIA GPU Operator has the following limitations:

  * The bundled NVIDIA GPU Operator supports the following NVIDIA software components only:

    * NVIDIA Container Toolkit
    * NVIDIA DCGM Exporter
    * NVIDIA Kubernetes Device Plugin
    * NVIDIA MIG Manager for Kubernetes.
  * During [Preview](https://cloud.google.com/products/#product-launch-stages), the NVIDIA GPU Operator configuration is fixed. If you attempt to customize any settings, they are reconciled back to the original installation settings.

  * The bundled NVIDIA GPU Operator can't be used to install NVIDIA GPU drivers.

  * During Preview, this feature uses the `resource.k8s.io/v1beta1` API group, which differs from the open source Kubernetes API group for this feature, `resource.k8s.io/v1`. The `v1` open source API group provides more features and better stability than the `v1beta1` API group.




### What's next

  * To use dynamic resource allocation with your GPU workloads, see [Manage GPU devices with dynamic resource allocation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/use-dra-for-gpus).

  * To learn more about dynamic resource allocation, see [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) in the Kubernetes documentation.




## Reference documentation

### `bmctl`

  * [bmctl command reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl)

  * [Cluster configuration field reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#cluster_configuration_fields)




###  gcloud CLI 

  * [`gcloud container bare-metal clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters)

  * [`gcloud container bare-metal node-pools`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools)

  * [`gcloud container bare-metal admin-clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters)




### Terraform

  * [`google_gkeonprem_bare_metal_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster)

  * [`google_gkeonprem_bare_metal_node_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_node_pool)

  * [`google_gkeonprem_bare_metal_admin_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_admin_cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
