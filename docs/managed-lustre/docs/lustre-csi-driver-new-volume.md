---
url: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume/
title: Access Managed Lustre instances on GKE with the Managed Lustre CSI driver \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:06:08.732318+00:00
---

# Access Managed Lustre instances on GKE with the Managed Lustre CSI driver  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Access Managed Lustre instances on GKE with the Managed Lustre CSI driver Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how you can create a new Kubernetes [volume](https://kubernetes.io/docs/concepts/storage/volumes/) backed by the Managed Lustre CSI driver in GKE with [dynamic provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/). The Managed Lustre CSI driver lets you create storage backed by [Managed Lustre instances](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-overview) on-demand, and access them as volumes for your stateful workloads.

### Multi-NIC support for high-performance networking

For GKE clusters running version `1.35.2-gke.1842000` or later, the Managed Lustre CSI driver is enabled by default to use all available Network Interface Cards (NICs) for increased throughput. This support aggregates bandwidth by spreading TCP storage traffic across your network interfaces.

To use multi-NIC support, your nodes must meet the following requirements:

  * **Standard NICs for TCP:** your nodes must use standard NICs, such as [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) or VirtIO-Net, to handle TCP storage traffic.
  * **Same VPC:** all standard NICs must reside in the same [VPC network](https://docs.cloud.google.com/vpc/docs/vpc).
  * **RDMA considerations:** your nodes can also have RDMA NICs attached; however, the Managed Lustre CSI driver only uses the standard NICs for TCP storage traffic.



If you want to disable the multi-NIC support, see Disable multi-NIC for Lustre.

### Lustre communication ports

The GKE Managed Lustre CSI driver uses different ports for communication with Managed Lustre instances, depending on your GKE cluster version and existing Managed Lustre configurations.

  * **Default port (Recommended):** for new GKE clusters that run version `1.33.2-gke.4780000` or later, the driver uses port `988` for Lustre communication by default.

  * **Legacy Port (Deprecated):** use port `6988` by appending the `--enable-legacy-lustre-port` flag to your `gcloud` commands in the following scenarios:

    * **Earlier GKE versions:** if your GKE cluster runs a version earlier than `1.33.2-gke.4780000`, the `--enable-legacy-lustre-port` flag works around a port conflict with the `gke-metadata-server` on GKE nodes.
    * **Existing Lustre instances:** if you are connecting to an existing Managed Lustre instance that was created with the `gke-support-enabled` flag, you _must_ still include `--enable-legacy-lustre-port` in your `gcloud` commands, irrespective of your cluster version. Without this flag, your GKE cluster will fail to mount the existing Lustre instance.



You can configure the new and existing clusters to use either the default port `988`, or the legacy port `6988`.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Cloud Managed Lustre API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,lustre.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * For limitations and requirements, see the [CSI driver overview](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-overview#csi-driver-overview).
  * Make sure to enable the Managed Lustre CSI driver. It is disabled by default in Standard and Autopilot clusters.



### Set up environment variables

Set up the following environment variables:
    
    
    export CLUSTER_NAME=CLUSTER_NAME
    export PROJECT_ID=PROJECT_ID
    export NETWORK_NAME=LUSTRE_NETWORK
    export IP_RANGE_NAME=LUSTRE_IP_RANGE
    export FIREWALL_RULE_NAME=LUSTRE_FIREWALL_RULE
    export LOCATION=ZONE
    export CLUSTER_VERSION=CLUSTER_VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `LUSTRE_NETWORK`: the shared Virtual Private Cloud (VPC) network where both the GKE cluster and Managed Lustre instance reside.
  * `LUSTRE_IP_RANGE`: the name for the IP address range created for VPC Network Peering with Managed Lustre.
  * `LUSTRE_FIREWALL_RULE`: the name for the firewall rule to allow TCP traffic from the IP address range.
  * `ZONE`: the geographical [zone](https://docs.cloud.google.com/compute/docs/regions-zones) of your GKE cluster; for example, `us-central1-a`.
  * `CLUSTER_VERSION`: the GKE cluster version.



### Set up a VPC network

You must specify the same VPC network when creating the Managed Lustre instance and your GKE clusters, or connected through [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes) if using a peered VPC network.

  1. To enable service networking, run the following command:
         
         gcloud services enable servicenetworking.googleapis.com \
             --project=${PROJECT_ID}
         

  2. Create a VPC network. Setting the `--mtu` flag to `8896` results in a 10% performance gain.
         
         gcloud compute networks create ${NETWORK_NAME} \
             --subnet-mode=auto --project=${PROJECT_ID} \
             --mtu=8896
         

  3. Create an IP address range.
         
         gcloud compute addresses create ${IP_RANGE_NAME} \
             --global \
             --purpose=VPC_PEERING \
             --prefix-length=20 \
             --description="Managed Lustre VPC Peering" \
             --network=${NETWORK_NAME} \
             --project=${PROJECT_ID}
         

  4. Get the CIDR range associated with the range you created in the preceding step.
         
         CIDR_RANGE=$(
           gcloud compute addresses describe ${IP_RANGE_NAME} \
               --global  \
               --format="value[separator=/](address, prefixLength)" \
               --project=${PROJECT_ID}
         )
         

  5. Create a firewall rule to allow TCP traffic from the IP address range you created.
         
         gcloud compute firewall-rules create ${FIREWALL_RULE_NAME} \
             --allow=tcp:988,tcp:6988 \
             --network=${NETWORK_NAME} \
             --source-ranges=${CIDR_RANGE} \
             --project=${PROJECT_ID}
         

  6. To set up network peering for your project, verify that you have necessary IAM permissions, specifically the `compute.networkAdmin` or `servicenetworking.networksAdmin` role.

     1. Go to Google Cloud console > **IAM & Admin**, then search for your project owner principal.
     2. Click the pencil icon, then click **\+ ADD ANOTHER ROLE**.
     3. Select **Compute Network Admin** or **Service Networking Admin**.
     4. Click **Save**.
  7. Connect the peering.
         
         gcloud services vpc-peerings connect \
             --network=${NETWORK_NAME} \
             --project=${PROJECT_ID} \
             --ranges=${IP_RANGE_NAME} \
             --service=servicenetworking.googleapis.com
         


**Note:** Your GKE cluster must be in the same VPC network that you set up in this section, or connected through [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes) if using a peered VPC network. For improved network throughput, consider [enabling Tier 1 bandwidth](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-tier-1#enable_tier_1_bandwidth_on_a_cluster) when you create the cluster.

## Configure the Managed Lustre CSI driver

This section covers how you can enable and disable the Managed Lustre CSI driver.

### Enable the Managed Lustre CSI driver on a new GKE cluster

The following sections describe how to enable the Managed Lustre CSI driver on a new GKE cluster.

#### Use the default port `988`

To enable the Managed Lustre CSI driver when creating a new GKE cluster that runs version `1.33.2-gke.4780000` or later, run the following command:

### Autopilot
    
    
    gcloud container clusters create-auto "${CLUSTER_NAME}" \
        --location=${LOCATION} \
        --network="${NETWORK_NAME}" \
        --cluster-version=${CLUSTER_VERSION} \
        --enable-lustre-csi-driver
    

### Standard
    
    
    gcloud container clusters create "${CLUSTER_NAME}" \
        --location=${LOCATION} \
        --network="${NETWORK_NAME}" \
        --cluster-version=${CLUSTER_VERSION} \
        --addons=LustreCsiDriver
    

#### Use the legacy port `6988`

To enable the Managed Lustre CSI driver when creating a new GKE cluster that runs a version earlier than `1.33.2-gke.4780000`, run the following command:

### Autopilot
    
    
    gcloud container clusters create-auto "${CLUSTER_NAME}" \
        --location=${LOCATION} \
        --network="${NETWORK_NAME}" \
        --cluster-version=${CLUSTER_VERSION} \
        --enable-lustre-csi-driver \
        --enable-legacy-lustre-port
    

### Standard
    
    
    gcloud container clusters create "${CLUSTER_NAME}" \
        --location=${LOCATION} \
        --network="${NETWORK_NAME}" \
        --cluster-version=${CLUSTER_VERSION} \
        --addons=LustreCsiDriver \
        --enable-legacy-lustre-port
    

### Enable the Managed Lustre CSI driver on existing GKE clusters

The following sections describe how to enable the Managed Lustre CSI driver on existing GKE clusters.

#### Use the default port `988`

To enable the Managed Lustre CSI driver on an existing GKE cluster that runs version `1.33.2-gke.4780000` or later, run the following command:
    
    
      gcloud container clusters update ${CLUSTER_NAME} \
          --location=${LOCATION} \
          --update-addons=LustreCsiDriver=ENABLED
    

#### Use the legacy port `6988`

To enable the Managed Lustre CSI driver on an existing GKE cluster, you might need to use the legacy port `6988` by adding the `--enable-legacy-lustre-port` flag. This flag is required in the following scenarios:

  * If your GKE cluster runs on a version _earlier than`1.33.2-gke.4780000`_.
  * If you intend to connect this cluster to an existing Managed Lustre instance that was created with the [`gke-support-enabled`](https://docs.cloud.google.com/managed-lustre/docs/create-instance#optional-flags) flag.
        
        gcloud container clusters update ${CLUSTER_NAME} \
            --location=${LOCATION} \
            --enable-legacy-lustre-port
        


**Note:** If you enable the CSI driver on an existing cluster and later upgrade your cluster to `1.33.2-gke.4780000` or newer, you might still need this flag if you continue to connect to `gke-support-enabled` Lustre instances.

### Node upgrade required on existing clusters

Enabling the Managed Lustre CSI driver on existing clusters can trigger node re-creation in order to update the necessary kernel modules for the Managed Lustre client. For immediate availability, we recommend manually upgrading your node pools.

GKE clusters on a release channel upgrade according to their scheduled rollout, which can take several weeks depending on your [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows). If you're on a static GKE version, you need to [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading-nodes) your node pools.

Until the node upgrade fully completes, the CSI driver Pod might crashloop on nodes pending update. If you see an `Operation not permitted` error in the CSI driver Pod logs, this indicates that node upgrade or recreation is required.

After the node pool upgrade, CPU nodes might appear to be using a GPU image in the Google Cloud console or CLI output. This behavior is expected. The GPU image is being reused on CPU nodes to securely install the Managed Lustre kernel modules. You won't be charged for GPU usage.

### (Optional) Create a multi-NIC node pool

To use high-performance networking, you must create a node pool with an instance type that supports [multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts). The multi-NIC support is enabled by default on GKE clusters that run version `1.35.2-gke.1842000` or later. Ensure that your secondary network interfaces reside within the same VPC network as your primary interface.

Run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --machine-type=MACHINE_TYPE \
        --enable-gvnic \
        --additional-node-network network=NETWORK_NAME,subnetwork=SECONDARY_SUBNET
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `LOCATION`: the region or zone of your cluster.
  * `MACHINE_TYPE`: the machine type for the node pool, such as `a3-megagpu-8g` which is often used with multi-NIC for high-performance. Multi-NIC is supported on any machine type.
  * `NETWORK_NAME`: the VPC network name.
  * `SECONDARY_SUBNET`: the name of the secondary subnet.



### Disable multi-NIC on Lustre

While multi-NIC support is recommended for high-performance workloads, you might want to disable it in specific scenarios. For example, you might not want to spread Lustre traffic across all available hardware interfaces, or you might need to isolate connectivity issues to a single network path for troubleshooting.

**Note:** If you disable multi-NIC support on running nodes, you might need to recreate or [manually upgrade your node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading-nodes) for this change to take effect.

### For a cluster

To disable high-performance networking for the entire cluster, use the `--disable-multi-nic-lustre` flag when creating or updating the cluster. For example:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --disable-multi-nic-lustre
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `LOCATION`: the region or zone of your cluster.



### For a node pool

To disable high-performance networking for a specific node pool, update the node pool to set the `lustre.csi.storage.gke.io/multi-nic` label to `false`:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
    --cluster=CLUSTER_NAME \
    --zone=LOCATION \
    --node-labels=lustre.csi.storage.gke.io/multi-nic=false
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `LOCATION`: the zone of your cluster.



### Disable the Managed Lustre CSI driver

You can disable the Managed Lustre CSI driver on an existing GKEcluster by using the Google Cloud CLI.

**Warning:** Disabling the Managed Lustre CSI driver can disrupt workloads that have Managed Lustre file systems mounted.
    
    
    gcloud container clusters update ${CLUSTER_NAME} \
        --location=${LOCATION} \
        --update-addons=LustreCsiDriver=DISABLED
    

After the CSI driver is disabled, GKE automatically recreates your nodes and uninstalls the Managed Lustre kernel modules.

## Create a new volume using the Managed Lustre CSI driver

The following sections describe the typical process for creating a Kubernetes volume backed by a Managed Lustre instance in GKE:

  1. Create a StorageClass.
  2. Use a PersistentVolumeClaim to access the volume.
  3. Create a workload that consumes the volume.



### Create a StorageClass

When the Managed Lustre CSI driver is enabled, GKE automatically creates a StorageClass for provisioning Managed Lustre instances. The StorageClass depends on the Managed Lustre [performance tier](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/create#--per-unit-storage-throughput), and is one of the following:

  * `lustre-rwx-125mbps-per-tib`
  * `lustre-rwx-250mbps-per-tib`
  * `lustre-rwx-500mbps-per-tib`
  * `lustre-rwx-1000mbps-per-tib`



GKE provides a default StorageClass for each supported Managed Lustre performance tier. This simplifies the dynamic provisioning of Managed Lustre instances, as you can use the built-in StorageClasses without having to define your own.

For zonal clusters, the CSI driver provisions Managed Lustre instances in the same zone as the cluster. For regional clusters, it provisions the instance in one of the zones within the region.

The following example shows you how to create a custom StorageClass with specific topology requirements:

  1. Save the following manifest in a file named `lustre-class.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: lustre-class
         provisioner: lustre.csi.storage.gke.io
         volumeBindingMode: Immediate
         reclaimPolicy: Delete
         parameters:
           perUnitStorageThroughput: "1000"
           network: LUSTRE_NETWORK
         allowedTopologies:
         - matchLabelExpressions:
           - key: topology.gke.io/zone
             values:
             - us-central1-a
         

For the full list of fields that are supported in the StorageClass, see the [Managed Lustre CSI driver reference documentation](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-reference).

  2. Create the StorageClass by running this command:
         
         kubectl apply -f lustre-class.yaml
         




### Use a PersistentVolumeClaim to access the Volume

This section shows you how to create a [PersistentVolumeClaim](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumeclaims) resource that references the Managed Lustre CSI driver's StorageClass.

  1. Save the following manifest in a file named `lustre-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: lustre-pvc
         spec:
           accessModes:
           - ReadWriteMany
           resources:
             requests:
               storage: 9000Gi
           storageClassName: lustre-class
         

**Warning:** For GKE clusters running versions earlier than `1.35.0-gke.2331000`, changing the storage size of the PVC isn't supported and requires you to re-create the PVC with the new size. For more information, see [Limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre#limitations). To increase storage capacity for clusters running version `1.35.0-gke.2331000` or later, see [Scale your Managed Lustre storage on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/expand-lustre-volumes).

For the full list of fields that are supported in the PersistentVolumeClaim, see the [Managed Lustre CSI driver reference documentation](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-reference).

  2. Create the PersistentVolumeClaim by running this command:
         
         kubectl apply -f lustre-pvc.yaml
         




### Create a workload to consume the volume

This section shows an example of how to create a Pod that consumes the PersistentVolumeClaim resource you created earlier.

Multiple Pods can share the same PersistentVolumeClaim resource.

  1. Save the following manifest in a file named `my-pod.yaml`.
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-pod
         spec:
           containers:
           - name: nginx
             image: nginx
             volumeMounts:
               - name: lustre-volume
                 mountPath: /data
           volumes:
           - name: lustre-volume
             persistentVolumeClaim:
               claimName: lustre-pvc
         

  2. Apply the manifest to the cluster.
         
         kubectl apply -f my-pod.yaml
         

  3. Verify that the Pod is running. The Pod runs after the PersistentVolumeClaim is provisioned. This operation might take a few minutes to complete.
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME           READY   STATUS    RESTARTS   AGE
         my-pod         1/1     Running   0          11s
         




## Use fsGroup with Managed Lustre volumes

You can change the group ownership of the _root level directory_ of the mounted file system to match a user-requested fsGroup specified in the Pod's [SecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod). fsGroup won't recursively change the ownership of the entire mounted Managed Lustre file system; only the root directory of the mount point is affected.

## Troubleshooting

For troubleshooting guidance, refer to the [Troubleshooting page](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-troubleshooting) in the Managed Lustre documentation.

## Clean up

To avoid incurring charges to your Google Cloud account, delete the storage resources you created in this guide.

  1. Delete the Pod and PersistentVolumeClaim.

**Note:** If you create the PersistentVolume with a "Delete" persistentVolumeReclaimPolicy, deleting the PersistentVolumeClaim also deletes the PersistentVolume and the underlying Managed Lustre instance.
         
         kubectl delete pod my-pod
         kubectl delete pvc lustre-pvc
         

  2. Check the PersistentVolume status.
         
         kubectl get pv
         

The output is similar to the following:
         
         No resources found
         

It might take a few minutes for the underlying Managed Lustre instance to be fully deleted.




## What's next

  * [Explore the Managed Lustre documentation](https://docs.cloud.google.com/managed-lustre/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
