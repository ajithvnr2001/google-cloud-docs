---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-cluster/
title: Step 1: Create a cluster \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:21:07.415877+00:00
---

# Step 1: Create a cluster  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 1: Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-create-cluster.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-cluster.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-cluster.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-cluster.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-cluster.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-cluster.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-cluster.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-create-cluster.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-create-cluster.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-create-cluster.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-create-cluster.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-create-cluster.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-create-cluster.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-create-cluster.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-create-cluster.html)



**Upgrading:** If you are upgrading to Apigee hybrid version 1.10.5, see [Upgrading Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade) for instructions. If you are performing a new installation, continue with the configurations described below.

This step explains how to create the cluster in which you will run Apigee hybrid. The instructions vary depending on the platform in which you are running hybrid. Before you begin, make sure to review the following information: 

  * [Minimum cluster configurations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview)
  * [Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes)
  * [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-production)
  * [Configuring authentication for Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-tls)
  * [StorageClass configuration](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-config)
  * [Secure ports usage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/ports)

**Note:** You can create a new, dedicated cluster for Apigee hybrid or you can install it in a cluster that is running other workloads. Creating a dedicated cluster for Apigee hybrid adds isolation and simplifies the overall effort required to maintain the cluster and its Apigee hybrid workloads. 

If you install Apigee hybrid in a cluster running other workloads, you need to upgrade and maintain your cluster at the versions and features required in common for Apigee hybrid and for your other workloads. You may want to develop a plan to migrate one or more workloads if conflicts arise between supported versions and requirements. 

The remainder of the installation instructions assume you are installing on a dedicated cluster. 

## Create your cluster

Follow the steps for your selected platform:

### GKE

##  Create a cluster on GKE 

These steps explain how to configure and create a GKE cluster in your Google Cloud project. 

**Caution:** Apigee does not support [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) or [gVisor for hybrid installations on GKE](https://github.com/google/gvisor). 

Apigee recommends you create a **regional cluster** rather than a **zonal cluster**. If you are unfamiliar with the distinction between regions and zones, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). The available regions are listed in [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). Just be aware that, for example, `us-west1` is a valid region name, while `us-west1-a` is a zone in the region.

  1. Make sure you are using a version of GKE that is supported for hybrid version 1.10.5. See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms).
  2. Ensure the clocks on all nodes and application servers are synchronized with Network Time Protocol (NTP), as explained in the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites). The Cassandra database relies on Network Time Protocol (NTP) synchronization to maintain data consistency. If you plan to install hybrid into multiple regions, make sure they are synchronized with NTP across all regions.
  3. (GKE private clusters only), If you are creating a private cluster, add a firewall rule to allow port 9443 for communication between GKE master nodes and GKE worker nodes and to allow the GKE masters to access Apigee mutating webhooks. Follow the procedure in [Adding firewall rules for specific use cases](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules) in the Google Kubernetes Engine documentation. For more information see [Private clusters in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept). 

You do not need to add this rule if you are creating a standard or public cluster.

  4. Create a **standard** cluster by following the instructions at [Create a regional cluster with a multi-zone node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster#create-regional-multi-zone-nodepool). It's okay to create the cluster with just the default node pool. You will configure and create the required Apigee hybrid node pools in the next step. **Important** : Create a standard cluster instead of an Autopilot cluster. Apigee hybrid does not support Autopilot clusters, because Autopilot clusters do not support custom node pools. If you are using the Google Cloud console UI, make sure to select **SWITCH TO STANDARD CLUSTER**. ![Create cluster screen heading showing Switch to Standard Cluster choice.](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.10/images/create-cluster-switch-to-standard-cluster.png)**Tip:** If you are not creating your cluster in the default network, follow the instructions in [Creating a cluster in an existing subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#creating_cluster)

Go to the next step only after the cluster creation completes successfully.

  5. Create two node pools by following the instructions in [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools). Be sure to configure the node pools with the minimum requirements listed in the table below. 

#### What you need to know about node pools

**Note:** We recommend you use the names `apigee-data` and `apigee-runtime` for the node pools. Apigee hybrid recognizes these names by default. If you do not want to use the default names, additional configuration is required later when you configure the cluster for Apigee hybrid. For more information, including instructions for changing the default node pool names by editing your cluster configuration file, see [Using the default nodeSelectors](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#using-the-default-nodeselectors).

We recommend you review the following information about node pools and node pool configuration before continuing:

     * [About node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#about-node-pools)
     * [ Cassandra network requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#cassandra-network-requirements)

**Minimum node pool requirements**

Be sure to satisfy these minimum requirements when creating the node pools. If using the Cloud console, be sure to configure both the **Node pool details** and **Nodes** sections. 

**Note:** The node pool configuration values described in the following table represent _minimum_ values. This minimum configuration is suitable for testing; however, based on your needs, you can upsize the nodes now or in the future. For information on managing cluster nodes, see [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).Node pool name | Description | Minimum nodes | Minimum  
machine type  
---|---|---|---  
`apigee-data` | A stateful node pool used for the Cassandra database. | 1 per zone  
(3 per region) | e2-standard-4  
(4 vCPU, 16 GB memory)  
`apigee-runtime` | A stateless node pool used by the runtime message processor.  | 1 per zone  
(3 per region) | e2-standard-4  
(4 vCPU, 16 GB memory)  
  
For more details about node pool configuration see [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes). 

  6. (Optional) If you wish, you can delete the `default` node pool. See [Delete a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool).
  7. Create the following environment variables. These variables are used in the gcloud commands that follow. 

###  Linux / MacOS 
         
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export CLUSTER_LOCATION="YOUR_CLUSTER_LOCATION"

###  Windows 
         
         set CLUSTER_NAME="YOUR_CLUSTER_NAME"
         set CLUSTER_LOCATION=YOUR_CLUSTER_LOCATION
         set PROJECT_ID=YOUR_PROJECT_ID

Where: 

     * **`CLUSTER_NAME`** : The name of your cluster. 
     * **`CLUSTER_LOCATION`** : The region in which you created your cluster. 
  8. Verify the node pool configurations: 

### Regional clusters
         
         gcloud container node-pools list \
         --cluster=**${CLUSTER_NAME}** \
         --region=**${CLUSTER_LOCATION}** \
         --project=**${PROJECT_ID}**

### Zonal clusters
         
         gcloud container node-pools list \
         --cluster=**${CLUSTER_NAME}** \
         --zone=**${CLUSTER_LOCATION}** \
         --project=**${PROJECT_ID}**

  9. Make sure your cluster is set as the default cluster for `kubectl` by getting the `gcloud` credentials of the cluster you just created: 

### Regional clusters
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
             --region **${CLUSTER_LOCATION}** \
             --project **${PROJECT_ID}**

### Zonal clusters
         
         gcloud container clusters get-credentials **${CLUSTER_NAME}** \
             --zone **${CLUSTER_LOCATION}** \
             --project **${PROJECT_ID}**

See [ Set a default cluster for kubectl commands](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#default_cluster_kubectl). 

  10. Configure [persistent solid state disk (SSD)](https://docs.cloud.google.com/compute/docs/disks#pdspecs) storage for Cassandra. We do not support using [local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds). For more information, see [ Change the default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) in the Kubernetes documentation. 

     1. Get the name of the current default StorageClass: 
            
            kubectl get sc

For example: 
            
            kubectl get sc
              NAME                    PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
              premium-rwo             pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h
              standard                kubernetes.io/gce-pd    Delete          Immediate              true                   15h
              **standard-rwo (default)  pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h**

     2. Describe the StorageClass named `standard-rwo`. Note that its type is `pd-balanced`: 
            
            kubectl describe sc standard-rwo

For example: 
            
            kubectl describe sc standard-rwo
            
            Name:                  standard-rwo
              IsDefaultClass:        Yes
              Annotations:           components.gke.io/layer=addon,storageclass.kubernetes.io/is-default-class=false
              Provisioner:           pd.csi.storage.gke.io
              Parameters:            type=pd-balanced
              AllowVolumeExpansion:  True
              MountOptions:          <none>
              ReclaimPolicy:         Delete
              VolumeBindingMode:     WaitForFirstConsumer
              Events:                <none>

     3. Create a new file called `storageclass.yaml`.
     4. Add this code to the file. Note that the name of the new class is `apigee-sc`. You can use any name you like. Also, note that the storage type is `pd-ssd`: 
            
            ---
            kind: StorageClass
            apiVersion: storage.k8s.io/v1
            metadata:
              name: "apigee-sc"
            provisioner: kubernetes.io/gce-pd
            parameters:
              type: pd-ssd
              replication-type: none
            volumeBindingMode: WaitForFirstConsumer
            allowVolumeExpansion: true

     5. Apply the new StorageClass to your Kubernetes cluster: 
            
            kubectl apply -f storageclass.yaml

     6. Execute the following two commands to change the default StorageClass: 
            
            kubectl patch storageclass standard-rwo \
            -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
            
            kubectl patch storageclass apigee-sc \
            -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

     7. Execute this command to verify that the new default StorageClass is called `apigee-sc`: 
            
            kubectl get sc

For example: 
            
            kubectl get sc
              NAME                  PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
              **apigee-sc (default)   kubernetes.io/gce-pd    Delete          WaitForFirstConsumer   true                   14h**
              premium-rwo           pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h
              standard              kubernetes.io/gce-pd    Delete          Immediate              true                   15h
              standard-rwo          pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h

  11. Enable workload identity for the cluster. Workload Identity allows workloads in your GKE clusters to impersonate Identity and Access Management (IAM) service accounts to access Google Cloud services. This operation can take up to 30 minutes: 

### Regional clusters
         
         gcloud container clusters update **${CLUSTER_NAME}** \
           --workload-pool=**${PROJECT_ID}**.svc.id.goog \
           --project **${PROJECT_ID}** \
           --region **${CLUSTER_LOCATION}**

### Zonal clusters
         
         gcloud container clusters update **${CLUSTER_NAME}** \
           --workload-pool=**${PROJECT_ID}**.svc.id.goog \
           --zone **${CLUSTER_LOCATION}** \
           --project **${PROJECT_ID}**

For more information, see [Enable Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable). 

  12. Verify whether Workload identity is successfully enabled with the following command; 

### Regional clusters
         
         gcloud container clusters describe **${CLUSTER_NAME}** \
           --project **${PROJECT_ID}** \
           --region **${CLUSTER_LOCATION} | grep -i "workload"**

### Zonal clusters
         
         gcloud container clusters describe **${CLUSTER_NAME}** \
           --zone **${CLUSTER_LOCATION}** \
           --project **${PROJECT_ID} | grep -i "workload"**




When you have a cluster installed and running, go to the next step. 

### GKE on-prem

##  Create a cluster on GKE on-prem 

These steps explain how to configure and create a GKE on-prem cluster for Apigee hybrid.

  1. Make sure you are using a version of Anthos on-premises VMWare that is supported for hybrid version 1.10.5. See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms).
  2. Ensure the clocks on all nodes and application servers are synchronized with Network Time Protocol (NTP), as explained in the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites). The Cassandra database relies on Network Time Protocol (NTP) synchronization to maintain data consistency. If you plan to install hybrid into multiple regions, be sure they are synchronized with NTP across all regions.
  3. Create the cluster by following the instructions at [Create basic clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/minimal-create-clusters). It's okay to create the cluster with just the default node pool. You will configure and create the required Apigee hybrid node pools in the next step. 

Go to the next step only after the cluster creation completes successfully.

  4. Create two node pools by following the instructions in [Creating and managing node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/managing-node-pools). Configure the node pools with the minimum requirements listed in the table below. 

#### What you need to know about node pools

**Note:** We recommend you use the names `apigee-data` and `apigee-runtime` for the node pools. Apigee hybrid recognizes these names by default. If you do not want to use the default names, additional configuration is required later when you configure the cluster for Apigee hybrid. For more information, including instructions for changing the default node pool names by editing your cluster configuration file, see [Using the default nodeSelectors](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#using-the-default-nodeselectors).

We recommend you review the following information about node pools and node pool configuration before continuing:

     * [About node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#about-node-pools)
     * [ Cassandra network requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#cassandra-network-requirements)

**Minimum node pool requirements**

Be sure to satisfy these minimum requirements when creating the node pools. 

**Note:** The node pool configuration values described in the following table represent _minimum_ values. This minimum configuration is suitable for testing; however, based on your needs, you can upsize the nodes now or in the future. For information on managing cluster nodes, see [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).Node pool name | Description | Minimum nodes | Minimum  
machine type  
---|---|---|---  
`apigee-data` | A stateful node pool used for the Cassandra database. | 1 per zone  
(3 per region) | e2-standard-4  
(4 vCPU, 16 GB memory)  
`apigee-runtime` | A stateless node pool used by the runtime message processor.  | 1 per zone  
(3 per region) | e2-standard-4  
(4 vCPU, 16 GB memory)  
  
For more details about node pool configuration see [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes). 

  5. (Optional) If you wish, you can delete the `default` node pool. See [Delete a node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/managing-node-pools#delete_a_node_pool).
  6. Configure [persistent solid state disk (SSD)](https://docs.cloud.google.com/compute/docs/disks#pdspecs) storage for Cassandra. We do not support using [local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds). For more information, see [ Change the default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) in the Kubernetes documentation. 

     1. Get the name of the current default StorageClass: 
            
            kubectl get sc

For example: 
            
            kubectl get sc
              NAME                    PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
              premium-rwo             pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h
              standard                kubernetes.io/gce-pd    Delete          Immediate              true                   15h
              **standard-rwo (default)  pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h**

     2. Describe the StorageClass named `standard-rwo`. Note that its type is `pd-balanced`: 
            
            kubectl describe sc standard-rwo

For example: 
            
            kubectl describe sc standard-rwo
            
            Name:                  standard-rwo
            IsDefaultClass:        Yes
            Annotations:           components.gke.io/layer=addon,storageclass.kubernetes.io/is-default-class=false
            Provisioner:           pd.csi.storage.gke.io
            Parameters:            type=pd-balanced
            AllowVolumeExpansion:  True
            MountOptions:          <none>
            ReclaimPolicy:         Delete
            VolumeBindingMode:     WaitForFirstConsumer
            Events:                <none>

     3. Create a new file called `storageclass.yaml`.
     4. Add this code to the file. Note that the name of the new class is `apigee-sc`. You can use any name you like. Also, note that the storage type is `pd-ssd`: 
            
            ---
            kind: StorageClass
            apiVersion: storage.k8s.io/v1
            metadata:
              name: "apigee-sc"
            provisioner: kubernetes.io/gce-pd
            parameters:
              type: pd-ssd
              replication-type: none
            volumeBindingMode: WaitForFirstConsumer
            allowVolumeExpansion: true

     5. Apply the new StorageClass to your Kubernetes cluster: 
            
            kubectl apply -f storageclass.yaml

     6. Execute the following two commands to change the default StorageClass: 
            
            kubectl patch storageclass standard-rwo \
              -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
            
            kubectl patch storageclass apigee-sc \
              -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

     7. Execute this command to verify that the new default StorageClass is called `apigee-sc`: 
            
            kubectl get sc

For example: 
            
            kubectl get sc
              NAME                  PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
              **apigee-sc (default)   kubernetes.io/gce-pd    Delete          WaitForFirstConsumer   true                   14h**
              premium-rwo           pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h
              standard              kubernetes.io/gce-pd    Delete          Immediate              true                   15h
              standard-rwo          pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   15h




When you have a cluster installed and running, go to the next step. 

### Anthos on bare metal

##  Create a cluster on Anthos on bare metal 

These steps explain how to configure and create a cluster for Apigee hybrid on Anthos on bare metal. Anthos on bare metal lets you run Kubernetes clusters directly on your own machine resources.

  1. Make sure you are using a version of Anthos on Bare Metal that is supported for hybrid version 1.10.5. See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms).
  2. Ensure the clocks on all nodes and application servers are synchronized with Network Time Protocol (NTP), as explained in the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites). The Cassandra database relies on Network Time Protocol (NTP) synchronization to maintain data consistency. If you plan to install hybrid into multiple regions, be sure they are synchronized with NTP across all regions.
  3. Review the [ Installation prerequisites overview](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/install-prereq) and [Creating clusters: overview](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-clusters-overview).
  4. Create the cluster with two node pools configured as described below: 
     * Follow the cluster creation instructions [Anthos clusters on bare metal quickstart](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/quickstart).
     * Create a minimum of two node pools. Configure the node pools with the minimum requirements listed in the table below. 

#### What you need to know about node pools

**Note:** We recommend you use the names `apigee-data` and `apigee-runtime` for the node pools. Apigee hybrid recognizes these names by default. If you do not want to use the default names, additional configuration is required later when you configure the cluster for Apigee hybrid. For more information, including instructions for changing the default node pool names by editing your cluster configuration file, see [Using the default nodeSelectors](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#using-the-default-nodeselectors).

We recommend you review the following information about node pools and node pool configuration before continuing:

       * [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes)
       * [About node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#about-node-pools)
       * [ Cassandra network requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#cassandra-network-requirements)

The minimum configurations for your cluster are:

**Note:** The node pool configuration values described in the following table represent _minimum_ values. This minimum configuration is suitable for testing; however, based on your needs, you can upsize the nodes now or in the future.Configuration | Stateful node pool | Stateless node pool  
---|---|---  
Purpose | A stateful node pool used for the Cassandra database. | A stateless node pool used by the runtime message processor.  
Label name | apigee-data | apigee-runtime  
Number of nodes | 1 per zone (3 per region) | 1 per zone (3 per region)  
CPU | 4 | 4  
RAM | 15 | 15  
Storage | dynamic | Managed with the [ApigeeDeployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-deployment-services) CRD  
Minimum disk IOPS | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS. | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS.  
Network bandwidth for each machine instance type | 1 Gbps | 1 Gbps  
  
For more details on minimum cluster configuration see: [Minimum cluster configurations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview)




When you have a cluster installed and running, go to the next step. 

### AKS

##  Create a cluster on AKS 

These steps explain how to configure and create a cluster for Apigee hybrid on AKS.

  1. Make sure you are using a version of AKS that is supported for hybrid version 1.10.5. See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms).
  2. Ensure the clocks on all nodes and application servers are synchronized with Network Time Protocol (NTP), as explained in the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites). The Cassandra database relies on Network Time Protocol (NTP) synchronization to maintain data consistency. If you plan to install hybrid into multiple regions, be sure they are synchronized with NTP across all regions.
  3. Create the cluster using either the [Azure CLI](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough) or [Azure Portal](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal), and create two node pools as described below. 

#### What you need to know about node pools

**Note:** We recommend you use the names `apigee-data` and `apigee-runtime` for the node pools. Apigee hybrid recognizes these names by default. If you do not want to use the default names, additional configuration is required later when you configure the cluster for Apigee hybrid. For more information, including instructions for changing the default node pool names by editing your cluster configuration file, see [Using the default nodeSelectors](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#using-the-default-nodeselectors).

We recommend you review the following information about node pools and node pool configuration before continuing:

     * [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes)
     * [About node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#about-node-pools)
     * [ Cassandra network requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#cassandra-network-requirements)

The minimum configurations for your cluster are:

**Note:** The node pool configuration values described in the following table represent _minimum_ values. This minimum configuration is suitable for testing; however, based on your needs, you can upsize the nodes now or in the future. For information on managing cluster nodes, see [Add and manage AKS node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#anthos-node-pool-configuration).Configuration | Stateful node pool | Stateless node pool  
---|---|---  
Purpose | A stateful node pool used for the Cassandra database. | A stateless node pool used by the runtime message processor.  
Label name | apigee-data | apigee-runtime  
Number of nodes | 1 per zone (3 per region) | 1 per zone (3 per region)  
CPU | 4 | 4  
RAM | 15 | 15  
Storage | dynamic | Managed with the [ApigeeDeployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-deployment-services) CRD  
Minimum disk IOPS | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS. | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS.  
Network bandwidth for each machine instance type | 1 Gbps | 1 Gbps  
  
For more details on minimum cluster configuration see: [Minimum cluster configurations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview)

When you have a cluster installed and running, go to the next step. 




### EKS

##  Create a cluster on EKS 

These steps explain how to configure and create a cluster for Apigee hybrid on EKS.

  1. Make sure you are using a version of EKS that is supported for hybrid version 1.10.5. See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms).
  2. Ensure the clocks on all nodes and application servers are synchronized with Network Time Protocol (NTP), as explained in the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites). The Cassandra database relies on Network Time Protocol (NTP) synchronization to maintain data consistency. If you plan to install hybrid into multiple regions, be sure they are synchronized with NTP across all regions.
  3. If you are using Kubernetes version 1.24 or newer, make sure you have installed the [Kubernetes CSI driver for Amazon EBS](https://github.com/kubernetes-sigs/aws-ebs-csi-driver). 
  4. Use the following instructions to create a user cluster, and create two node pools as described below. 
     * [EKS overview documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html).
     * [Creating an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html).

#### What you need to know about node pools

**Note:** We recommend you use the names `apigee-data` and `apigee-runtime` for the node pools. Apigee hybrid recognizes these names by default. If you do not want to use the default names, additional configuration is required later when you configure the cluster for Apigee hybrid. For more information, including instructions for changing the default node pool names by editing your cluster configuration file, see [Using the default nodeSelectors](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#using-the-default-nodeselectors).

We recommend you review the following information about node pools and node pool configuration before continuing:

     * [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes)
     * [About node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#about-node-pools)
     * [ Cassandra network requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#cassandra-network-requirements)

The minimum configurations for your cluster are:

**Note:** The node pool configuration values described in the following table represent _minimum_ values. This minimum configuration is suitable for testing; however, based on your needs, you can upsize the nodes now or in the future. For information on managing cluster nodes, see [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).Configuration | Stateful node pool | Stateless node pool  
---|---|---  
Purpose | A stateful node pool used for the Cassandra database. | A stateless node pool used by the runtime message processor.  
Label name | apigee-data | apigee-runtime  
Number of nodes | 1 per zone (3 per region) | 1 per zone (3 per region)  
CPU | 4 | 4  
RAM | 15 | 15  
Storage | dynamic | Managed with the [ApigeeDeployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-deployment-services) CRD  
Minimum disk IOPS | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS. | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS.  
Network bandwidth for each machine instance type | 1 Gbps | 1 Gbps  
  
For more details on minimum cluster configuration see: [Minimum cluster configurations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview)




When you have a cluster installed and running, go to the next step. 

### GKE on AWS

##  Create a cluster on GKE on AWS 

These steps explain how to configure and create a cluster for Apigee hybrid on GKE on AWS.

  1. Make sure you are using a version of GKE that is supported for hybrid version 1.10.5. See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms).
  2. Ensure the clocks on all nodes and application servers are synchronized with Network Time Protocol (NTP), as explained in the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites). The Cassandra database relies on Network Time Protocol (NTP) synchronization to maintain data consistency. If you plan to install hybrid into multiple regions, be sure they are synchronized with NTP across all regions.
  3. Use the following instructions to create a user cluster, and create two node pools as described below. 
     * [GKE on AWS overview documentation](https://docs.cloud.google.com/anthos/gke/docs/aws).
     * [Deploy an application on GKE on AWS](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart).

#### What you need to know about node pools

**Note:** We recommend you use the names `apigee-data` and `apigee-runtime` for the node pools. Apigee hybrid recognizes these names by default. If you do not want to use the default names, additional configuration is required later when you configure the cluster for Apigee hybrid. For more information, including instructions for changing the default node pool names by editing your cluster configuration file, see [Using the default nodeSelectors](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#using-the-default-nodeselectors).

We recommend you review the following information about node pools and node pool configuration before continuing:

     * [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes)
     * [About node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#about-node-pools)
     * [ Cassandra network requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#cassandra-network-requirements)

The minimum configurations for your cluster are:

**Note:** The node pool configuration values described in the following table represent _minimum_ values. This minimum configuration is suitable for testing; however, based on your needs, you can upsize the nodes now or in the future. For information on managing cluster nodes, see [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).Configuration | Stateful node pool | Stateless node pool  
---|---|---  
Purpose | A stateful node pool used for the Cassandra database. | A stateless node pool used by the runtime message processor.  
Label name | apigee-data | apigee-runtime  
Number of nodes | 1 per zone (3 per region) | 1 per zone (3 per region)  
CPU | 4 | 4  
RAM | 15 | 15  
Storage | dynamic | Managed with the [ApigeeDeployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-deployment-services) CRD  
Minimum disk IOPS | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS. | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS.  
Network bandwidth for each machine instance type | 1 Gbps | 1 Gbps  
  
For more details on minimum cluster configuration see: [Minimum cluster configurations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview)




When you have a cluster installed and running, go to the next step. 

### OpenShift

##  Create a cluster on OpenShift 

These steps explain how to configure and create a cluster for Apigee hybrid on OpenShift.

  1. Make sure you are using a version of OpenShift that is supported for hybrid version 1.10.5. See [Apigee hybrid supported platforms and versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms).
  2. Ensure the clocks on all nodes and application servers are synchronized with Network Time Protocol (NTP), as explained in the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites). The Cassandra database relies on Network Time Protocol (NTP) synchronization to maintain data consistency. If you plan to install hybrid into multiple regions, be sure they are synchronized with NTP across all regions.
  3. Build the OpenShift cluster to deploy on the runtime plane, install Apigee on your OpenShift user cluster, and create two node pools. You can find additional information about OpenShift cluster creation and management on Google Cloud in the OpenShift documentation, for example: [Installing a cluster quickly on Google Cloud](https://docs.openshift.com/container-platform/4.10/installing/installing_gcp/installing-gcp-default.html#installing-gcp-default).For help setting up your OpenShift cluster on Google Cloud VMs, see [How to Set Up Apigee hybrid on Openshift on Google Cloud VMs](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/How-to-Set-Up-Apigee-hybrid-on-Openshift-on-GCP-VMs/ta-p/480473).

As part of the OpenShift install, install and configure the `oc` CLI tool. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.10/cli_reference/openshift_cli/getting-started-cli.html#installing-openshift-cli) in the OpenShift documentation.

#### What you need to know about node pools

**Note:** We recommend you use the names `apigee-data` and `apigee-runtime` for the node pools. Apigee hybrid recognizes these names by default. If you do not want to use the default names, additional configuration is required later when you configure the cluster for Apigee hybrid. For more information, including instructions for changing the default node pool names by editing your cluster configuration file, see [Using the default nodeSelectors](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes#using-the-default-nodeselectors).

We recommend you review the following information about node pools and node pool configuration before continuing:

     * [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-dedicated-nodes)
     * [About node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#about-node-pools)
     * [ Cassandra network requirements](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview#cassandra-network-requirements)

The minimum configurations for your cluster are:

**Note:** The node pool configuration values described in the following table represent _minimum_ values. This minimum configuration is suitable for testing; however, based on your needs, you can upsize the nodes now or in the future. For information on managing cluster nodes, see [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).Configuration | Stateful node pool | Stateless node pool  
---|---|---  
Purpose | A stateful node pool used for the Cassandra database. | A stateless node pool used by the runtime message processor.  
Label name | apigee-data | apigee-runtime  
Number of nodes | 1 per zone (3 per region) | 1 per zone (3 per region)  
CPU | 4 | 4  
RAM | 15 | 15  
Storage | dynamic | Managed with the [ApigeeDeployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-deployment-services) CRD  
Minimum disk IOPS | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS. | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS.  
Network bandwidth for each machine instance type | 1 Gbps | 1 Gbps  
  
For more details on minimum cluster configuration see: [Minimum cluster configurations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview)




When you have installed a cluster, go to the next step. 

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-cluster) [(NEXT) Step 2: Install cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-cert-manager) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-apigeectl) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-configure-cluster) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-check-cluster) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-hybrid-runtime) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-expose-apigee-ingress) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
