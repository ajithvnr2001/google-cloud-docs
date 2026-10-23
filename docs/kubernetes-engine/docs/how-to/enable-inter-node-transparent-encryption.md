---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption/
title: Encrypt your data in-transit in GKE with user-managed encryption keys \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:31.136218+00:00
---

# Encrypt your data in-transit in GKE with user-managed encryption keys  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Encrypt your data in-transit in GKE with user-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to encrypt in-transit data for Pod communications across Google Kubernetes Engine (GKE) nodes by using user-managed encryption keys. This level of control over your encryption keys is useful if you're in a regulated industry and have a business need for compliance and security audits. On this page, you learn about configuring for single and multi-cluster environments, including best practices and limitations.

This page is for Security specialists who require fine-grained control over encryption keys to meet compliance and security requirements. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following concepts:

  * [In-transit data](https://docs.cloud.google.com/docs/security/encryption-in-transit#authentication_integrity_and_encryption).
  * [WireGuard, which GKE uses to perform encryption in GKE Dataplane V2](https://www.wireguard.com/), in addition to the default encryption provided by VM NICs.



By default, Google [encrypts all data in-transit between VMs](https://docs.cloud.google.com/security/encryption-in-transit) at the network interface controller (NIC) level to ensure the confidentiality of the data in-transit, regardless of what service or application is running on the VM (including GKE). This layer of encryption is applicable to all GKE nodes and Pod traffic. The encryption keys are provided and managed by Google.

You can enable inter-node transparent encryption in single and multi-cluster environments. For more information about how this feature works, see How inter-node transparent encryption works with GKE.

## Limitations

  * This feature on its own doesn't guarantee that Google can't access the encryption keys stored in the GKE node memory. In some regulated environments or jurisdictions, or to meet specific compliance requirements, you might want to further encrypt these keys and control access. To do this, we recommend that you use inter-node transparent encryption with [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).

  * Inter-node transparent encryption for GKE is only supported on GKE Dataplane V2 clusters.

  * GKE Autopilot is not supported.

  * Inter-node transparent encryption for GKE uses WireGuard. WireGuard is not [FIPS](https://csrc.nist.gov/publications/detail/fips/140/2/final) compliant.

  * Encryption keys are not dynamically rotated. Key rotation needs to be handled manually by restarting the nodes.

  * Inter-node transparent encryption along with Confidential GKE Nodes works only on Container-Optimized OS (COS) and Ubuntu, and not on Windows.

  * Inter-node transparent encryption does not encrypt network traffic initiated by the GKE node or a Pod using the `hostNetwork`.

  * Inter-node transparent encryption does not encrypt network traffic sent to a Pod exposed on a node port. Even when `ExternalTrafficPolicy: Cluster` is configured on the Service, the traffic forwarded from the first node receiving traffic from the client to the backend Pod is not encrypted.

  * The maximum number of nodes supported with inter-node transparent encryption enabled for single cluster or multi-cluster configurations is 500.

  * Inter-node transparent encryption might result in the nodes being oversubscribed. You might expect 15% CPU increase on average on n2-standard-8 nodes with the Ubuntu OS with 2 Gbps throughput.

The increase in CPU utilization is not attributed to any Pod because it is not aware by the kube-scheduler. The Pod with increased traffic might use all CPU resources on the node. This can prevent other Pods from getting the CPU resources they need, even if they are properly configured. This can cause problems for Pods that are trying to run sensitive workloads or that need to be able to respond quickly to requests. As a workaround, you can keep a significant amount of CPU unscheduled on nodes that have inter-node transparent encryption enabled. Alternatively, you can schedule a Pod with a low [PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) that has a large CPU request but never uses this CPU.

  * Inter-node transparent encryption incurs 150 microseconds of latency on two nodes in the same zone that don't use Confidential GKE Nodes.

  * When you enable inter-node transparent encryption, traffic observability features used for tracking traffic on the Pods might not work as expected because the data in-transit is encrypted with keys that are not accessible to the underlying Google infrastructure.

  * When you enable inter-node transparent encryption, Pod IP addresses are not visible on the VPC. Features that depend on packet inspection such as Packet Mirroring and Pod CIDR based VPC firewall rules are not compatible with inter-node transparent encryption.

  * When you enable inter-node transparent encryption across clusters attached to different VPC subnets, you need to manually create firewall rules to allow communications between the cluster nodes.

  * Inter-node transparent encryption turns off the some Layer 7 capabilities of GKE Dataplane V2. As a result, you can't enable [FQDN network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies) and inter-node transparent encryption at the same time.

  * You cannot enable this feature at the same time as [intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility).




## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * GKE inter-node transparent encryption is only supported on Google Cloud CLI version 458.0.0 and later and the following GKE versions:

    * 1.26.10-gke.1024000 or later
    * 1.27.7-gke.1506000 or later
    * 1.28.2-gke.1098000 or later



## Enable inter-node transparent encryption with GKE

You can enable inter-node transparent encryption with GKE on a single cluster or in a multi-cluster environment.

### Enable on a new cluster

  1. To enable inter-node transparent encryption on a new cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-datapane-v2 \
             --in-transit-encryption inter-node-transparent
         

Replace the following:

     * `CLUSTER_NAME` with the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
**Note:** We recommend that you create new clusters with inter-node encryption enabled, rather than creating them with inter-node encryption disabled and subsequently enabling it. Enabling inter-node encryption at a later time may result in node pool restarts.
  2. To verify your configuration, use the following command to check the encryption status:
         
         kubectl -n kube-system exec -ti anetd-XXXX -- cilium status | grep Encryption
         

The output is similar to the following:
         
         Encryption: Wireguard [cilium_wg0 (Pubkey: <key>, Port: 51871, Peers: 2)]
         

**Note:** Verify that the number of peers is one less than the number of nodes in your cluster. For example, in a cluster with 24 nodes, the number of peers should be 23. If the number of peers isn't one less than the number of nodes in the cluster, restart the `anetd` agent on your nodes again.



### Enable on an existing cluster

  1. To enable inter-node transparent encryption on an existing cluster:
         
         gcloud container clusters update CLUSTER_NAME \
           --in-transit-encryption inter-node-transparent \
           --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME` with the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
**Note:** We recommend that you perform this operation during a maintenance window as this operation might disrupt the traffic to your Pod. The cluster update and installation of the inter-node encryption network may require several hours to finish.
  2. To check that the Google Cloud CLI command completed successfully :
         
         gcloud container clusters describe CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --format json | jq .status
         

Replace the following:

     * `CLUSTER_NAME` with the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

Wait until the status displays "RUNNING". Enabling inter-node encryption in GKE will automatically restart the nodes. It might take several hours for the node restart to occur and for the new nodes to enforce policies.

  3. To confirm that nodes have restarted:
         
         kubectl get nodes
         

Check the `AGE` field of each node and proceed if the `AGE` field reflects new nodes.

  4. To verify your configuration, you can use the following command to check the encryption status:
         
         kubectl -n kube-system exec -ti anetd-XXXX -- cilium status | grep Encryption
         

The output is similar to the following:
         
         Encryption: Wireguard [cilium_wg0 (Pubkey: <key>, Port: 51871, Peers: 2)]
         

Verify that the number of peers is one less than the number of nodes in your cluster. For example, in a cluster with 24 nodes, the number of peers should be 23. If the number of peers isn't one less than the number of nodes in the cluster, restart the `anetd` agent on your nodes again.




### Enable across multiple clusters

Inter-node transparent encryption is not supported on Autopilot clusters. If your fleet includes Autopilot clusters, they won't be able to communicate with Standard clusters that have encryption enabled.

To enable inter-node transparent encryption in a multi-cluster environment:

  1. Enable inter-node transparent encryption on a new cluster or in an existing cluster.

  2. [Register your cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster) to a fleet.

  3. Enable inter-node transparent encryption for the fleet:
         
         gcloud container fleet dataplane-v2-encryption enable --project PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

  4. Verify status on all nodes:
         
         kubectl -n kube-system get pods -l k8s-app=cilium -o name | xargs -I {} kubectl -n kube-system exec -ti {} -- cilium status
         

The output is similar to the following:
         
         ...
         Encryption: Wireguard [cilium_wg0 (Pubkey: <key>, Port: 51871, Peers: 5)]
         ...
         

**Note:** Verify that the number of peers is one less than the number of nodes all registered clusters. For example, in a cluster with 24 nodes, the number of peers should be 23. If the number of peers isn't one less than the number of nodes in the cluster, restart the `anetd` agent on your nodes again.



## Disable inter-node transparent encryption

In some cases, you might want to disable inter-node transparent encryption in your GKE cluster for performance improvements, or to troubleshoot connectivity for your application. Before proceeding with this operation, consider the following:

  * Inter-node transparent encryption is enabled for the entire cluster and you can't partially disable it in individual Kubernetes resources such as namespaces or Pods.

  * Perform this operation during a maintenance window as this operation will disrupt the traffic of your Pod.




### Disable on a single cluster

To disable inter-node transparent encryption on a single cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --in-transit-encryption none
    

Replace the following:

  * `CLUSTER_NAME`: with your name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

**Note:** We recommend that you perform this operation during a maintenance window as this operation might disrupt the traffic to your Pod. The cluster update and disabling of the inter-node encryption network may require several hours to finish, as it recreates the node pool.

### Disable in a cluster that's part of a fleet

You can turn off encryption for a cluster in a fleet by using either of the following two options:

  * To completely remove the cluster from the fleet, [unregister your cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister#unregister).

  * Alternatively, keep the cluster in the fleet but disable encryption:
        
        gcloud container fleet dataplane-v2-encryption disable --project PROJECT_ID
        

Replace `PROJECT_ID` with your project ID.

Disabling encryption with this command initiates the removal of remote nodes from the Wireguard peers list on each cluster. This process can take up to several minutes to complete, depending on the number of clusters and nodes involved. To see the updated peer count, you'll need to manually refresh the WireGuard peers list on each cluster. You can use your cluster management tool or the following command:
        
        kubectl -n kube-system exec -ti anetd-XXXX -- cilium status | grep Encryption
        




### Disable for an entire fleet of clusters

  * To disable inter-node transparent encryption in a fleet:
        
        gcloud container fleet dataplane-v2-encryption disable --project PROJECT_ID
        

Replace `PROJECT_ID` with your project ID.

  * To disable inter-node transparent encryption and remove the now unused API, disable the GKE Dataplane V2 API at the fleet level. This will turn off the GKE Dataplane V2 controller running in your fleet.
        
        gcloud services disable gkedataplanev2.googleapis.com \
            --project=PROJECT_ID
        

Replace `PROJECT_ID` with your project ID.

**Note:** This API is responsible for the inter-node transparent encryption feature for your fleet. Make sure that you verify that this API is not used by anything else in your fleet before you disable it to avoid unexpected behavior.

To efficiently manage clusters with the same name and ensure multi-cluster encryption activation, follow these steps:

    1. [Unregister the old cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister) from the fleet before creating a new one with the same name.

    2. [Re-register](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke) the new cluster upon recreation.

    3. If you forget to [unregister](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister) a cluster, delete the old membership, and recreate the new cluster with a new membership.

Failure to follow these steps may result in multi-cluster encryption not activating on the new cluster until the fleet membership is recreated.




## How inter-node transparent encryption works with GKE

The following sections describe how inter-node transparent encryption works when you enable it in your cluster:

### Encryption of network traffic between two Pods on different nodes

With inter-node transparent encryption enabled, GKE Dataplane V2 encrypts Pod-to-Pod traffic if Pods are on different nodes, regardless of the cluster to which those nodes belong. When the clusters are part of the same [fleet](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview), they belong to the same encryption domain.

**Note:** Inter-node transparent encryption encrypts packets when they leave the originating node. Inter-node transparent encryption doesn't encrypt packets between Pods on the same node.

Clusters with different inter-node transparent encryption configurations can co-exist in the same fleet. If you have a multi-cluster environment in which only some clusters use inter-node transparent encryption, the following considerations apply:

  * Pod-to-Pod communication between nodes in the same cluster is encrypted using the public/private key pair.

  * Pod-to-Pod communication between a node in a cluster that has inter-node transparent encryption enabled and a node in a cluster that doesn't have inter-node transparent encryption enabled fails.




### Encryption key generation and usage

When the feature is enabled, every GKE node in the cluster automatically generates a public/private key pair known as the _encryption keys_.

  * The **private key** is stored in memory (not on disk) and never leaves the node. Using [GKE Confidential Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes) further decreases the risk of keys being compromised because the node memory is also encrypted (with different keys).

  * The public key is shared with other nodes using the GKE Dataplane V2 control plane and is accessible to all nodes in the same encryption domain.




After the keys are exchanged, each node can establish a WireGuard tunnel with other nodes in the same encryption domain. Each tunnel is unique for a given pair of nodes.

**Note:** WireGuard is not [FIPS](https://csrc.nist.gov/publications/detail/fips/140/2/final) compliant.

Consider the following when dealing with the private or public key pairs and session key:

  * **Private/public key pair:**

    * The public key is distributed in the cluster and all nodes in the cluster can access the public key.

    * The key pair is rotated when the node restarts. GKE doesn't rotate keys at regular intervals. To manually trigger a key rotation, drain and restart the node. This invalidates the original key pair and generates a new key pair.

  * **Session key:**

    * This key is not configurable.

    * This key gets periodically rotated every two minutes.

    * The session key is exclusive to the nodes involved in the tunnel.




## What's next

  * [Learn more about Google Cloud encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).
  * [Learn more about Google Cloud encryption in transit](https://docs.cloud.google.com/security/encryption-in-transit).
  * [Learn more about application-layer secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
