---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/quickstart/
title: Create basic clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:49:49.100962+00:00
---

# Create basic clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create basic clusters Stay organized with collections  Save and categorize content based on your preferences. 

Distributed Cloud software only lets you evaluate GKE clusters on bare metal hardware by creating a proof-of-concept admin cluster and user cluster. As the second part of a two-part tutorial, this document builds on the configuration in [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/minimal-infrastructure). After deployment, you can proceed to [Create a Service and an Ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress).

This document is intended for Admins and architects and Operators who set up, monitor, and manage the infrastructure lifecycle. Don't use a minimal proof-of-concept cluster on a production environment. To evaluate production architectures, see [Choose a deployment model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep).

**Note:** Distributed Cloud software only for bare metal was formerly known as Google Distributed Cloud Virtual, which was previously known as Anthos clusters on bare metal.

## Before you begin

  1. Ensure that you have set up hardware and planned your IP addresses as described in the preceding part of this guide, [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/minimal-infrastructure). Alternatively, use the network requirements planner in the **Prerequisites** section of the [**Create a bare metal admin cluster**](https://console.cloud.google.com/kubernetes/baremetal/add) flow in the Google Cloud console.

  2. If you want to use Terraform to create the user cluster, you need [Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli) either on your admin workstation or another computer.

     1. Make sure you have the latest Google Cloud CLI components installed:
            
            gcloud components update
            

  3. Do the following steps to activate and use the GKE On-Prem API:

     1. Enable the API in your project:
            
            gcloud services enable \
                --project PROJECT_ID \
                gkeonprem.googleapis.com
            

Replace `PROJECT_ID` with the project ID of your fleet host project.

If you get a `PERMISSION_DENIED` error, double check the project ID that you entered. If the project ID is correct, run `gcloud auth login` to sign in to the Google Cloud CLI with the account that has access to the project.

     2. If this is the first time that you have enabled the GKE On-Prem API in your project, you need to [initialize the API](https://docs.cloud.google.com/iam/docs/service-agents). You can do this by calling a gcloud CLI command that displays available versions that you can use to create a cluster:
            
            gcloud container bare-metal clusters query-version-config \
                --project=PROJECT_ID \
                --location="us-central1"
            




## Procedure overview

Creating basic clusters consists of these primary steps:

  1. **Gather information** used to specify the configuration of your clusters.

  2. **Create an admin cluster** for managing your user cluster.

  3. **Create a user cluster** that can run your workloads.




## 1\. Gather information

Use the information that you prepared in [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/minimal-infrastructure) or from the network planner to fill in each placeholder in the following table. The placeholders correspond to field values in the cluster configuration files for the minimal installation of one admin cluster and one user cluster. Some placeholders are set to the prefilled values from the generated cluster configuration file, but all placeholders are editable.

**Caution:** To make the placeholders in the table editable, you may need to refresh this page in your browser. However, the placeholders aren't persistent. Any values you've entered in the table are reset if you close or refresh this browser tab, or if you navigate away from this page.Basic cluster information  
---  
The name of the admin cluster you're creating. The location and naming of cluster artifacts on the admin workstation are based on the cluster name. The cluster namespace is derived from the cluster name. | `ADMIN_CLUSTER_NAME`  
The name of the user cluster you're creating. The location and naming of cluster artifacts on the admin workstation are based on the cluster name. The cluster namespace is derived from the cluster name. | `USER_CLUSTER_NAME`  
The version of `bmctl` that you downloaded in the first part of this guide. | `CLUSTER_VERSION`  
Account information  
The path to the SSH private key file on your admin workstation. By default, the path is  
`/home/USERNAME/.ssh/id_rsa`. | `SSH_PRIVATE_KEY_PATH`  
The ID of the Google Cloud project that you want to use for connecting your cluster to Google Cloud and viewing logs and metrics. This project is also referred to as the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project). | `PROJECT_ID`  
The email address that is associated with your Google Cloud account. For example: `alex@example.com`. | `GOOGLE_ACCOUNT_EMAIL`  
Node machine IP addresses  
One IP address for the admin cluster control plane node. | `ADMIN_CP_NODE_IP`  
One IP address for the user cluster control plane node. | `USER_CP_NODE_IP`  
One IP address for the user cluster worker node. | `USER_WORKER_NODE_IP`  
VIP addresses  
VIP for the Kubernetes API server of the admin cluster. | `ADMIN_CP_VIP`  
VIP for the Kubernetes API server of the user cluster. | `USER_CP_VIP`  
One VIP to use as the external address for the [ingress proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress). | `USER_INGRESS_VIP`  
Range of ten IP addresses for use as external IP addresses for Services of type LoadBalancer. Notice that this range includes the ingress VIP, which is required by MetalLB. No other IP addresses can overlap this range. | `START_IP-END_IP`  
Pod and Service CIDRs  
Range of IP addresses in CIDR block notation for use by Pods on the admin cluster. The recommended starting value, which is pre-filled in the generated cluster configuration file is `192.168.0.0/16`. | `192.168.0.0/16`  
Range of IP addresses in CIDR block notation for use by Services on the admin cluster. The recommended starting value, which is pre-filled in the generated cluster configuration file is `10.96.0.0/20`. | `10.96.0.0/20`  
Range of IP addresses in CIDR block notation for use by Pods on the user cluster. The recommended starting value, which is pre-filled in the generated cluster configuration file and is the default value in the console is `192.168.0.0/16`. | `192.168.0.0/16`  
Range of IP addresses in CIDR block notation for use by Services on the user cluster. The recommended starting value, which is pre-filled in the generated cluster configuration file and is the default value in the console is `10.96.0.0/20`. | `10.96.0.0/20`  
  
## 2\. Create an admin cluster

The following steps create an admin cluster for a minimal admin cluster and user cluster installation. Ensure that you have provided values for each placeholder in the table in the preceding Gather information section before proceeding.

When the GKE On-Prem API (`gkeonprem.googleapis.com`) is enabled for your project, newly created clusters are enrolled with the API automatically. Enrollment occurs even when [`spec.gkeOnPremAPI`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#gkeonpremapi) is unspecified in the cluster configuration file. Enrolling with this Google Cloud-hosted API lets you manage the lifecycle of your cluster using the Google Cloud console or the gcloud CLI.

To disable automatic enrollment, uncomment the `spec.gkeOnPremAPI` section in the cluster configuration file and set `spec.gkeOnPremAPI.enabled` to `false` before you create the cluster. The `spec.gkeOnPremAPI.enabled` field is mutable, so you can unenroll your cluster at any time after it's been created.

To create an admin cluster for the minimal installation:

  1. Set the default credentials that Google Distributed Cloud can use to create the cluster with the following command:
         
         gcloud auth application-default login

  2. To generate a cluster configuration file, run the following command from the `/baremetal` directory on your admin workstation:
         
         bmctl create config -c ADMIN_CLUSTER_NAME \
             --enable-apis --create-service-accounts --project-id=PROJECT_ID

  3. Verify the admin cluster configuration file:

The following cluster configuration file is filled in with the values that you entered in the planning table in the preceding section. In addition to the values you entered, note the following differences from the generated configuration file:

     * Comments have been removed from this sample to improve readability.
     * The `NodePool` spec has been removed. Worker nodes aren't allowed for an admin cluster.
    
    gcrKeyPath: bmctl-workspace/.sa-keys/PROJECT_ID-anthos-baremetal-gcr.json
    sshPrivateKeyPath: SSH_PRIVATE_KEY_PATH
    gkeConnectAgentServiceAccountKeyPath: bmctl-workspace/.sa-keys/PROJECT_ID-anthos-baremetal-connect.json
    gkeConnectRegisterServiceAccountKeyPath: bmctl-workspace/.sa-keys/PROJECT_ID-anthos-baremetal-register.json
    cloudOperationsServiceAccountKeyPath: bmctl-workspace/.sa-keys/PROJECT_ID-anthos-baremetal-cloud-ops.json
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-ADMIN_CLUSTER_NAME
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: ADMIN_CLUSTER_NAME
      namespace: cluster-ADMIN_CLUSTER_NAME
    spec:**  type: admin**
      profile: default
      anthosBareMetalVersion: CLUSTER_VERSION
      gkeConnect:
        projectID: PROJECT_ID
      controlPlane:
        nodePoolSpec:
          nodes:
          - address: ADMIN_CP_NODE_IP
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20
      loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: ADMIN_CP_VIP
      clusterOperations:
        projectID: PROJECT_ID
        location: us-central1
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
      # GKEOnPremAPI (Optional) Specify if you wish to explicitly enable/disable the cloud hosted gkeonprem
      # API to enable/disable cluster lifecycle management from gcloud UI and Terraform.
      # gkeOnPremAPI:
        # enabled: false
        # location is the Cloud location for the cluster resource metadata where the cluster will be enrolled.
        # location: us-central1

  4. Replace the contents of the generated configuration file on your admin workstation with the contents from the preceding sample.

Open the generated file, `bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME.yaml` and replace its contents with the contents of the sample you verified in the preceding step.

  5. To create the admin cluster, run the following command from the `/baremetal` directory on your admin workstation:
         
         bmctl create cluster -c ADMIN_CLUSTER_NAME

The `bmctl` command displays output to the screen as it runs preflight checks and creates the cluster. Verbose information is written to logs in the `baremetal/bmctl-workspace/ADMIN_CLUSTER_NAME/log` folder on the admin workstation.

Cluster creation can take several minutes to finish.

  6. Verify that your cluster was created and is running:
         
         kubectl --kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig \
             get nodes

If your cluster is running, the response looks something like this:
         
         NAME     STATUS  ROLES          AGE  VERSION
         node-01  Ready   control-plane  16h  v1.25.7-gke.1000

  7. To grant your user account the Kubernetes `clusterrole/cluster-admin` role on the cluster, run the following `gcloud` command:
         
         gcloud container fleet memberships generate-gateway-rbac \
             --membership=ADMIN_CLUSTER_NAME \
             --role=clusterrole/cluster-admin \
             --users=GOOGLE_ACCOUNT_EMAIL \
             --project=PROJECT_ID \
             --kubeconfig=bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig \
             --context=ADMIN_CLUSTER_NAME-admin@ADMIN_CLUSTER_NAME \
             --apply

The output of this command is similar to the following, which is truncated for readability:
         
         Validating input arguments.
         Specified Cluster Role is: clusterrole/cluster-admin
         Generated RBAC policy is:
         --------------------------------------------
         ...
         
         Applying the generate RBAC policy to cluster with kubeconfig: /root/bmctl-workspace/<var class="edit"scope="ADMIN_CLUSTER_NAME">ADMIN_CLUSTER_NAME</var>/<var class="edit"scope="ADMIN_CLUSTER_NAME">ADMIN_CLUSTER_NAME</var>-kubeconfig, context: <var class="edit"scope="ADMIN_CLUSTER_NAME">ADMIN_CLUSTER_NAME</var>-admin@<var class="edit"scope="ADMIN_CLUSTER_NAME">ADMIN_CLUSTER_NAME</var>
         Writing RBAC policy for user: GOOGLE_ACCOUNT_EMAIL to cluster.
         Successfully applied the RBAC policy to cluster.
         

Among other things, the RBAC policy lets you sign in to your cluster in the Google Cloud console to see more cluster details.




## 3\. Create a user cluster

The following steps create a user cluster for a minimal admin cluster and user cluster installation. Ensure that you have provided values for each placeholder in the table in the earlier Gather information section before proceeding.

To create a user cluster for the minimal installation:

### `bmctl`

When the GKE On-Prem API (`gkeonprem.googleapis.com`) is enabled for your project, newly created clusters are enrolled with the API automatically. Enrollment occurs even when [`spec.gkeOnPremAPI`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#gkeonpremapi) is unspecified in the cluster configuration file. When your cluster is enrolled with this Google Cloud-hosted API, you can use the Google Cloud console or the gcloud CLI to manage the cluster lifecycle.

To disable automatic enrollment, uncomment the `spec.gkeOnPremAPI` section in the cluster configuration file and set `spec.gkeOnPremAPI.enabled` to `false` before you create the cluster. The `spec.gkeOnPremAPI.enabled` field is mutable, so you can unenroll your cluster at any time after it's been created.

  1. Generate a cluster configuration file:
         
         bmctl create config -c USER_CLUSTER_NAME \
           --project-id=PROJECT_ID

  2. Verify the user cluster configuration file:

The following cluster configuration file is filled in with the values that you entered in the planning table earlier. In addition to the values you entered, note the following differences from the generated configuration file:

     * Comments have been removed from this sample to improve readability.
     * The cluster type, `spec.type`, has been set to `user`.
     * The `spec.clusterSecurity.authorization.clusterAdmin.gcpAccounts` field was added to grant the `clusterrole/cluster-admin` to your account. Among other things, this field lets you sign in to your cluster in the Google Cloud console to see more cluster details.
    
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-USER_CLUSTER_NAME
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: USER_CLUSTER_NAME
      namespace: cluster-USER_CLUSTER_NAME
    spec:**  type: user**
      profile: default
      anthosBareMetalVersion: CLUSTER_VERSION
      gkeConnect:
        projectID: PROJECT_ID
      controlPlane:
        nodePoolSpec:
          nodes:
          - address: USER_CP_NODE_IP
      clusterNetwork:
        pods:
          cidrBlocks:
          - 192.168.0.0/16
        services:
          cidrBlocks:
          - 10.96.0.0/20
      loadBalancer:
        mode: bundled
        ports:
          controlPlaneLBPort: 443
        vips:
          controlPlaneVIP: USER_CP_VIP
          ingressVIP: USER_INGRESS_VIP
        addressPools:
        - name: pool1
          addresses:
          - START_IP-END_IP
      clusterOperations:
        projectID: PROJECT_ID
        location: us-central1**  clusterSecurity:
        authorization:
          clusterAdmin:
            gcpAccounts:
            - GOOGLE_ACCOUNT_EMAIL**
      storage:
        lvpNodeMounts:
          path: /mnt/localpv-disk
          storageClassName: local-disks
        lvpShare:
          path: /mnt/localpv-share
          storageClassName: local-shared
          numPVUnderSharedPath: 5
      nodeConfig:
        podDensity:
          maxPodsPerNode: 250
      # GKEOnPremAPI (Optional) Specify if you wish to explicitly enable/disable the cloud hosted gkeonprem
      # API to enable/disable cluster lifecycle management from gcloud UI and Terraform.
      # gkeOnPremAPI:
        # enabled: false
        # location is the Cloud location for the cluster resource metadata where the cluster will be enrolled.
        # location: us-central1
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: node-pool-1
      namespace: cluster-USER_CLUSTER_NAME
    spec:
      clusterName: USER_CLUSTER_NAME
      nodes:
      - address: USER_WORKER_NODE_IP
    

  3. Replace the contents of the generated configuration file on your admin workstation with the contents from the preceding sample.

Open the generated file, `bmctl-workspace/USER_CLUSTER_NAME/USER_CLUSTER_NAME.yaml` and replace its contents with the contents of the sample you verified in the preceding step.

  4. Create the user cluster:
         
         bmctl create cluster -c USER_CLUSTER_NAME \
         --kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig

The `bmctl` command displays output to the screen as it runs preflight checks and creates the cluster. Verbose information is written to logs in the `baremetal/bmctl-workspace/USER_CLUSTER_NAME/log` folder on the admin workstation.

Cluster creation can take several minutes to finish.

  5. Verify that your cluster was created and is running:
         
         kubectl --kubeconfig bmctl-workspace/USER_CLUSTER_NAME/USER_CLUSTER_NAME-kubeconfig \
           get nodes

If your cluster is running, the response looks something like this:
         
         NAME    STATUS   ROLES           AGE     VERSION
         nuc-3   Ready    control-plane   4m32s   v1.26.2-gke.1001
         nuc-4   Ready    worker          2m2s    v1.26.2-gke.1001




### Console

Do the following steps to create a user cluster in the console:

  1. In the console, go to the **Create a bare metal cluster** page.

[Go to Create a bare metal cluster](https://console.cloud.google.com/kubernetes/baremetal/add)

  2. Make sure that the Google Cloud project list has `PROJECT_ID` selected.

  3. Click **Create Cluster**.

  4. In the dialog, click **On-premises**.

  5. Next to **Bare metal** , click **Configure**. The **Prerequisites** page displays.

  6. Under **Choose your cluster type** , select **Create a user cluster for an existing admin cluster**

  7. Click **Next**.




### Cluster basics

  1. Enter `USER_CLUSTER_NAME` as the name of the user cluster or use the default.

  2. Make sure that the newly created admin cluster is selected.

  3. In **GCP API Location** , select **us-central1**.

  4. In **Google Distributed Cloud version** , select `CLUSTER_VERSION` or use the default. You can use the defaults for the rest of the settings on this page.

  5. Click **Networking** in the left-navigation bar.




### Networking

  1. In the **Control plane** section, enter the following in the **Control plane node IP 1** field:
         
         USER_CP_NODE_IP
         

  2. In the **Load balancer** section, use the default load balancer, **Bundled with MetalLB**.

  3. Go to the **New address pool** section. Enter the IP address range in the **IP address range 1** field:
         
         10.200.0.51-10.200.0.70
         

  4. Click **Done**.

  5. In the **Virtual IPs** section, enter the IP address for the **Control Plane VIP** :
         
         USER_CP_VIP
         

  6. Enter the IP address for the **Ingress VIP** :
         
         USER_INGRESS_VIP
         

  7. In the **Service and Pod CIDRs** section, if you didn't change the Service and Pod CIDRs in the planner, you can use the defaults.

If you changed the CIDRs, then enter the CIDRs you want to use:

     * **Service CIDR** :
    
    10.96.0.0/20
    

     * **Pod CIDR** :
    
    192.168.0.0/16
    

  8. Click **default pool** in the left-navigation bar.




### Create a node pool

Your cluster must have at least one node pool for worker nodes. A node pool is a template for the groups of worker nodes created in this cluster.

Enter the IP address of the user cluster worker node in the **Nodes address 1** field:
    
    
    USER_WORKER_NODE_IP
    

### Create the cluster

  1. Click **Verify and Create** to create the user cluster.

It takes 15 minutes or more to create the user cluster. The console displays status messages as it verifies the settings and creates the cluster.

If there is a problem with the configuration, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.

To see additional information about the creation process, click **Show details** to display a side panel. Click close to close the details panel.

When the cluster is created, **Cluster status: running** is displayed.

  2. After the cluster is created, click arrow_back **Clusters** to go back to the **Clusters** page.




###  gcloud CLI 

This section shows you how to create a user cluster and a node pool using the gcloud CLI.

  1. Run the following command to create a user cluster:
         
         gcloud container bare-metal clusters create USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=us-central1 \
           --admin-cluster-membership=ADMIN_CLUSTER_NAME \
           --admin-cluster-membership-project=PROJECT_ID \
           --admin-cluster-membership-location=global \
           --version=CLUSTER_VERSION \
           --admin-users=GOOGLE_ACCOUNT_EMAIL \
           --island-mode-service-address-cidr-blocks=10.96.0.0/20 \
           --island-mode-pod-address-cidr-blocks=192.168.0.0/16 \
           --metal-lb-address-pools='pool=lb-pool-1,manual-assign=True,addresses=START_IP-END_IP' \
           --control-plane-node-configs='node-ip=USER_CP_NODE_IP' \
           --control-plane-vip=USER_CP_VIP \
           --control-plane-load-balancer-port=443 \
           --ingress-vip=USER_INGRESS_VIP \
           --lvp-share-path=/mnt/localpv-share \
           --lvp-share-storage-class=local-shared \
           --lvp-node-mounts-config-path=/mnt/localpv-disk \
           --lvp-node-mounts-config-storage-class=local-disks
         

The output from the command is similar to the following:
         
         Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
         

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation with the following command:
         
         gcloud container bare-metal operations describe OPERATION_ID \
           --project=PROJECT_ID \
           --location=us-central1
         

It takes about 15 minutes or more to create the cluster. As the cluster is being created, you can run the previous command every so often to get the current status.

When the cluster is created, you see output like the following:
         
         Created Anthos cluster on bare metal [https://gkeonprem.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/bareMetalClusters/USER_CLUSTER_NAME].
         

  2. After the cluster is created, run the following command to create a node pool on the newly created cluster.
         
         gcloud container bare-metal node-pools create node-pool-1 \
           --cluster=USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=us-central1 \
           --node-configs node-ip=USER_WORKER_NODE_IP




For more information and other examples, see the following:

  * [`gcloud container bare-metal clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters)

  * [`gcloud container bare-metal node-pools`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools)

  * [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-user-cluster-api#create_a_user_cluster)




### Terraform

This section shows you how to create a user cluster and a node pool using Terraform.

  1. Create a directory and a new file within that directory. The filename must have the `.tf` extension. In this guide, the file is called `main.tf`.
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf
         

  2. Verify the user cluster Terraform resource:

The following Terraform resource example is filled in with the values that you entered in the planning table in the preceding section.
         
         resource "google_gkeonprem_bare_metal_cluster"  "cluster-basic" {
           provider = google-beta
           name = "USER_CLUSTER_NAME"
           project = "PROJECT_ID"
           location = "us-central1"
           admin_cluster_membership = "projects/PROJECT_ID/locations/global/memberships/ADMIN_CLUSTER_NAME"
           bare_metal_version = "CLUSTER_VERSION"
           network_config {
             island_mode_cidr {
               service_address_cidr_blocks = ["10.96.0.0/20"]
               pod_address_cidr_blocks = ["192.168.0.0/16"]
             }
           }
           control_plane {
             control_plane_node_pool_config {
               node_pool_config {
                 labels = {}
                 operating_system = "LINUX"
                 node_configs {
                   labels = {}
                   node_ip = "USER_CP_NODE_IP"
                 }
               }
             }
           }
           load_balancer {
             port_config {
               control_plane_load_balancer_port = 443
             }
             vip_config {
               control_plane_vip = "USER_CP_VIP"
               ingress_vip = "USER_INGRESS_VIP"
             }
             metal_lb_config {
               address_pools {
                 pool = "pool1"
                 addresses = [
                   "START_IP-END_IP"
                 ]
                 avoid_buggy_ips = true
                 manual_assign = true
               }
             }
           }
           storage {
             lvp_share_config {
               lvp_config {
                 path = "/mnt/localpv-share"
                 storage_class = "local-shared"
               }
               shared_path_pv_count = 5
             }
             lvp_node_mounts_config {
               path = "/mnt/localpv-disk"
               storage_class = "local-disks"
             }
           }
           security_config {
             authorization {
               admin_users {
                 username = "GOOGLE_ACCOUNT_EMAIL"
               }
             }
           }
         }
         
         resource "google_gkeonprem_bare_metal_node_pool" "node-pool-default" {
           provider = google-beta
           name =  "node-pool-1"
           bare_metal_cluster = google_gkeonprem_bare_metal_cluster.cluster-basic.name
           project = "PROJECT_ID"
           location = "us-central1"
           node_pool_config {
             operating_system = "LINUX"
             node_configs {
               node_ip = "USER_WORKER_NODE_IP"
             }
           }
         }
         

  3. Copy the Terraform resource to `main.tf` and save the file.

  4. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider.

  5. Review the configuration and make changes if needed:
         
         terraform plan
         

  6. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         

When prompted, enter `yes`.

It takes about 15 minutes (or more depending on your network) to create the basic user cluster and node pool.

  7. To create a kubeconfig file for the user cluster, run the following command on the admin workstation:
         
         bmctl get credentials --cluster USER_CLUSTER_NAME \
         --admin-kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig

The output from the command displays the name of the kubeconfig file for the user cluster, for example:
         
         bmctl-workspace/USER_CLUSTER_NAME/USER_CLUSTER_NAME-TIMESTAMP-kubeconfig

The `TIMESTAMP` in the filename indicates the date and time the file was created.

Because this file contains authentication credentials for your cluster, you should store it in a secure location with restricted access.

  8. Verify that your cluster was created and is running:
         
         kubectl --kubeconfig bmctl-workspace/USER_CLUSTER_NAME/USER_CLUSTER_NAME-TIMESTAMP-kubeconfig \
             get nodes

If your cluster is running, the response looks something like this:
         
         NAME    STATUS   ROLES           AGE     VERSION
         nuc-3   Ready    control-plane   4m32s   v1.26.2-gke.1001
         nuc-4   Ready    worker          2m2s    v1.26.2-gke.1001




For more information and other examples, see the following:

  * [`google_gkeonprem_bare_metal_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster)

  * [`google_gkeonprem_bare_metal_node_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_node_pool)

  * [terraform.tfvars.sample](https://github.com/GoogleCloudPlatform/anthos-samples/blob/HEAD/anthos-onprem-terraform/abm_user_cluster_metallb/terraform.tfvars.sample)

  * [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-user-cluster-api#create_a_user_cluster)




## Connect to the user cluster

No matter which tool you used to create the user cluster, your email address is granted the role-based access control (RBAC) policies that let you connect to the cluster with full administrative privileges. Where your email address is specified depends on the tool:

  * **`bmctl`** : Your email address is included in the `clusterSecurity` section of the example user configuration file.

  * **Terraform** : Your email address is included in the `security_config` section of the example `google_gkeonprem_bare_metal_cluster` resource.

  * **The console** : As the cluster creator, your email address is automatically included on the **Cluster basics** page in the **Authorization** section.




Although only your email address is specified, you could include other email addresses to grant administrative access to the cluster to other users.

The RBAC policies granted to your email address do the following:

  * Grant you the Kubernetes `clusterrole/cluster-admin` role on the cluster.

  * Let you sign in to the cluster in the Google Cloud console using your Google identity. You can view the cluster on the [**GKE clusters**](https://console.cloud.google.com/kubernetes/list/overview) page in the console.

  * Let you run `kubectl` commands on your local computer using the connect gateway's kubeconfig.




To get the connect gateway's kubeconfig, run the following commands from your local computer:

  1. Get the kubeconfig entry that can access the cluster through the connect gateway.
         
         gcloud container fleet memberships get-credentials USER_CLUSTER_NAME  \
         --project=PROJECT_ID

The output is similar to the following:
         
         Starting to build Gateway kubeconfig...
         Current project_id: PROJECT_ID
         A new kubeconfig entry "connectgateway_PROJECT_ID_global_USER_CLUSTER_NAME" has been generated and set as the current context.
         

  2. You can now run `kubectl` commands through the connect gateway:
         
         kubectl get nodes
         

The output is similar to the following:
         
         NAME    STATUS   ROLES           AGE     VERSION
         nuc-3   Ready    control-plane   4m32s   v1.26.2-gke.1001
         nuc-4   Ready    worker          2m2s    v1.26.2-gke.1001
         

Many `kubectl` commands require the kubeconfig for the admin cluster. You will need to run those commands on the admin workstation.




## What's next

  * [Create a Service and an Ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress)

  * Learn more about:

    * The [`google_gkeonprem_bare_metal_cluster` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster)
    * The [connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
