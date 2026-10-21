---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/admin-user-gce-vms/
title: Create Google Distributed Cloud admin and user clusters on Compute Engine VMs \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:09.218920+00:00
---

# Create Google Distributed Cloud admin and user clusters on Compute Engine VMs  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/admin-user-gce-vms/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Create Google Distributed Cloud admin and user clusters on Compute Engine VMs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/try/admin-user-gce-vms)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/admin-user-gce-vms)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page shows you how to create a Google Distributed Cloud user cluster and an admin cluster on Compute Engine Virtual Machines (VMs). The [provided script](https://github.com/GoogleCloudPlatform/anthos-samples/tree/main/anthos-bm-gcp-bash) creates Compute Engine VMs for the admin and user cluster nodes and an admin workstation.

The _admin workstation_ hosts command-line interface (CLI) tools and configuration files to provision clusters during installation, and CLI tools for interacting with provisioned clusters post-installation. The script installs the CLI tools on the admin workstation VM.

A _user cluster_ is a Kubernetes cluster that runs your containerized workloads. It consists of _control plane nodes_ and _worker nodes_. User clusters must contain one or more worker nodes that run _user workloads_. An _admin cluster_ is a Kubernetes cluster that manages one or more user clusters, helping with creation, updates, and deletion of user clusters. An admin cluster consists of only control plane nodes. To learn more, see [Admin and user cluster deployment](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep#admin_user_model).

The script configures a Virtual Extensible LAN (VXLAN) overlay network between the VMs and prepares the VMs for cluster creation. Optionally, the script creates an admin cluster, or you can choose to create the admin cluster yourself to learn about the tools that Google Distributed Cloud provides for creating admin clusters.

With the provided script, you can try out Google Distributed Cloud quickly and without having to prepare any hardware. Completing the steps on this page provides you with a working Google Distributed Cloud test environment that runs on Compute Engine.

**Important:** This deployment is for evaluation purposes only. Don't run Google Distributed Cloud on Compute Engine VMs in production.

## What is the GKE On-Prem API?

The GKE On-Prem API is a Google Cloud-hosted API that lets you manage the lifecycle of your on-premises clusters using Terraform and standard Google Cloud applications. The GKE On-Prem API runs in Google Cloud's infrastructure. Terraform, the console, and the gcloud CLI are clients of the API, and they use the API to create clusters in your data center.

To manage the lifecycle of your clusters, the GKE On-Prem API must store metadata about your cluster's state in Google Cloud, using the Google Cloud region that you specify when creating the cluster. This metadata lets the API manage the cluster lifecycle and doesn't include workload-specific data.

When you create a cluster using an GKE On-Prem API client, you specify a Google Cloud project. After the cluster is created, it is automatically registered to the specified project's [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). This project is referred to as the [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project). The fleet host project can't be changed after the cluster is created.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make a note of the project ID because you need it to set an environment variable that is used in the script and commands on this page. If you selected an existing project, make sure that you are either a project owner or editor. 
  7. You can run the script on [Cloud Shell](https://docs.cloud.google.com/shell/docs) or your local machine running Linux or macOS. If you aren't using Cloud Shell: 
     1. Make sure you have installed the latest [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), the command line tool for interacting with Google Cloud. Update the gcloud CLI components, if needed: 
            
            gcloud components update

Depending on how the gcloud CLI was installed, you might see the following message: "You cannot perform this action because the gcloud CLI component manager is disabled for this installation. You can run the following command to achieve the same result for this installation:" Follow the instructions to copy and paste the command to update the components.

     2. Make sure you have `kubectl` installed. If you need to install `kubectl`, run the following command: 
            
            gcloud components install kubectl




## Create the VM infrastructure and optionally, the admin cluster

Do the following steps to get set up and run the script. The script that you download and run is from the [anthos-samples](https://github.com/GoogleCloudPlatform/anthos-samples/tree/main/anthos-bm-gcp-bash) repository. If you want to learn more about the script before you run it, see the next section, About the script.

  1. Set up environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export ADMIN_CLUSTER_NAME=ADMIN_CLUSTER_NAME
         export ON_PREM_API_REGION=ON_PREM_API_REGION
         export ZONE=ZONE
         

     * `ON_PREM_API_REGION`: The Google Cloud region in which the GKE On-Prem API runs and stores its metadata. Specify `us-central1` or another [supported region](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/supported-regions-on-prem-api).

     * `ZONE`: The Google Cloud zone that the Compute Engine VMs will be created in. You can use `us-central1-a` or any of the other [Compute Engine zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  2. Set the default project and zone:
         
         gcloud config set project $PROJECT_ID
         gcloud config set compute/zone $ZONE
         

If you get a `PERMISSION_DENIED` error, double check the project ID that you entered. If the project ID is correct, run `gcloud auth login` to sign in to the gcloud CLI with the account that has access to the project.

  3. Get a list of Google Distributed Cloud versions that you can install:
         
         gcloud container bare-metal admin-clusters query-version-config \
             --location=ON_PREM_API_REGION | grep 1.16
         

Some instructions in this document depend on the GKE On-Prem API, which supports a subset of available Google Distributed Cloud versions.

  4. Select a version from the output of the previous command and set it in an environment variable:
         
         export BMCTL_VERSION=BMCTL_VERSION
         

We recommend that you select the highest compatible version to get the latest Google Distributed Cloud features and fixes.

  5. Clone the `anthos-samples` repository and change to the directory where the script is located:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-samples
         cd anthos-samples/anthos-bm-gcp-bash
         

  6. Run the script:
         
         bash install_admin_cluster.sh
         

  7. When prompted, enter a number to choose the installation mode:

     * Enter **1** to have the script set up the VM infrastructure and install the admin cluster.
     * Enter **2** to have the script set up the VM infrastructure only.
  8. When prompted, confirm your selection.




The script outputs each command it runs and the status. When it finishes, the script outputs the following depending on whether you chose to install the admin cluster:

### Admin cluster created
    
    
    ✅ Installation complete. Please check the logs for any errors!!!
    ✅ If you do not see any errors in the output log, then you now have the following setup:
    
    |---------------------------------------------------------------------------------------------------------|
    | VM Name               | L2 Network IP (VxLAN) | INFO                                                    |
    |---------------------------------------------------------------------------------------------------------|
    | abm-admin-cluster-cp1 | 10.200.0.3            | Has control plane of admin cluster running inside       |
    | abm-user-cluster-cp1  | 10.200.0.4            | 🌟 Ready for use as control plane for the user cluster  |
    | abm-user-cluster-w1   | 10.200.0.5            | 🌟 Ready for use as worker for the user cluster         |
    | abm-user-cluster-w2   | 10.200.0.6            | 🌟 Ready for use as worker for the user cluster         |
    |---------------------------------------------------------------------------------------------------------|
    

### Set up VMs only
    
    
    |---------------------------------------------------------------------------------------------------------|
    | VM Name               | L2 Network IP (VxLAN) | INFO                                                    |
    |---------------------------------------------------------------------------------------------------------|
    | abm-admin-cluster-cp1 | 10.200.0.3            | 🌟 Ready for use as control plane for the admin cluster |
    | abm-user-cluster-cp1  | 10.200.0.4            | 🌟 Ready for use as control plane for the user cluster  |
    | abm-user-cluster-w1   | 10.200.0.5            | 🌟 Ready for use as worker for the user cluster         |
    | abm-user-cluster-w2   | 10.200.0.6            | 🌟 Ready for use as worker for the user cluster         |
    |---------------------------------------------------------------------------------------------------------|
    

### About the script

To learn more about [`install_admin_cluster.sh`](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-bm-gcp-bash/install_admin_cluster.sh), click add_circle **About the script** on the next line.

#### About the script

The script automates the following manual steps: 

  1. Creates a service account called `baremetal-gcr`, and grants the service account additional permissions to avoid needing multiple service accounts for different APIs and services. 
  2. Enables the following Google Cloud APIs: 
         
         anthos.googleapis.com
           anthosaudit.googleapis.com
           anthosgke.googleapis.com
           cloudresourcemanager.googleapis.com
           connectgateway.googleapis.com
           container.googleapis.com
           gkeconnect.googleapis.com
           gkehub.googleapis.com
           gkeonprem.googleapis.com
           iam.googleapis.com
           logging.googleapis.com
           monitoring.googleapis.com
           opsconfigmonitoring.googleapis.com
           serviceusage.googleapis.com
           stackdriver.googleapis.com
           storage.googleapis.com

  3. Creates the following VMs: 
     * One VM for the admin workstation. The admin workstation will have access to all the other cluster nodes using SSH. 
     * One VM for the control plane node of the admin cluster. 
     * Two VMs for the worker nodes of the user cluster. 
     * One VM for the control plane node of the user cluster. 
The script also verifies that SSH is enabled on all VMs. 
  4. Creates a Virtual Extensible LAN (VXLAN) overlay network for layer 2 connectivity between the VMs. The VXLAN isn't persistent, so if you reboot a VM instance the network is destroyed. The network is setup to be on the 10.200.0.0/24 subnet. The layer 2 connectivity is a requirement for the [bundled load balancer](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/bundled-lb). 
  5. Installs the following tools on the admin workstation: 
     * `bmctl`
     * `kubectl`
     * Docker

The script also downloads the service account key for the `baremetal-gcr` service account to the admin workstation. 

  6. Ensures that `root@10.200.0.x` from the admin workstation works by doing the following tasks: 
     1. Generate a new SSH key on the admin workstation. 
     2. Adds the public key to all the other VMs in the deployment. 
  7. Optionally, the script creates the admin cluster with the following configuration file: 
         
         gcloud compute ssh "$VM_WS" --zone "${ZONE}" --tunnel-through-iap <<EOF
         sudo su
         cd
         set -x
         export PROJECT_ID=\$(gcloud config get-value project)
         ADMIN_CLUSTER_NAME=\$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/cluster_id -H "Metadata-Flavor: Google")
         BMCTL_VERSION=\$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/bmctl_version -H "Metadata-Flavor: Google")
         export ADMIN_CLUSTER_NAME
         export BMCTL_VERSION
         bmctl create config -c \$ADMIN_CLUSTER_NAME
         cat > bmctl-workspace/\$ADMIN_CLUSTER_NAME/\$ADMIN_CLUSTER_NAME.yaml << EOB
         ---
         gcrKeyPath: /root/bm-gcr.json
         sshPrivateKeyPath: /root/.ssh/id_rsa
         gkeConnectAgentServiceAccountKeyPath: /root/bm-gcr.json
         gkeConnectRegisterServiceAccountKeyPath: /root/bm-gcr.json
         cloudOperationsServiceAccountKeyPath: /root/bm-gcr.json
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-\$ADMIN_CLUSTER_NAME
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: \$ADMIN_CLUSTER_NAME
           namespace: cluster-\$ADMIN_CLUSTER_NAME
         spec:
           type: admin
           anthosBareMetalVersion: \$BMCTL_VERSION
           gkeConnect:
             projectID: \$PROJECT_ID
           controlPlane:
             nodePoolSpec:
               clusterName: \$ADMIN_CLUSTER_NAME
               nodes:
               - address: 10.200.0.3
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
               controlPlaneVIP: 10.200.0.48
           clusterOperations:
             # might need to be this location
             location: us-central1
             projectID: \$PROJECT_ID
           storage:
             lvpNodeMounts:
               path: /mnt/localpv-disk
               storageClassName: node-disk
             lvpShare:
               numPVUnderSharedPath: 5
               path: /mnt/localpv-share
               storageClassName: local-shared
           nodeConfig:
             podDensity:
               maxPodsPerNode: 250
         EOB
         
         bmctl create cluster -c \$ADMIN_CLUSTER_NAME
         EOF

If you chose to have the script create the admin cluster, the script uses SSH to sign in to the admin workstation as the root user. Next, the script runs the `bmctl` command-line tool to create the admin cluster. This is one of the tools that you can use to create admin clusters. 

When Google Distributed Cloud creates clusters, it deploys a Kubernetes in Docker (kind) cluster on the admin workstation. This _bootstrap_ cluster hosts the Kubernetes controllers needed to create clusters and is used to create the admin cluster. Upon creation, relevant controllers are moved from the bootstrap cluster into the admin cluster. Finally, unless you specify otherwise, the bootstrap cluster is removed when cluster creation completes successfully. The bootstrap cluster requires Docker to pull container images. 




## Optionally create the admin cluster

If the script created the admin cluster, skip to the next section Verify the admin cluster. Otherwise, follow the steps in this section to create a bootstrap cluster and the admin cluster.

Before you create the admin cluster, you need to run the `bmctl register bootstrap` command on your admin workstation. This command deploys a temporary Kubernetes in Docker (kind) cluster on the admin workstation. This _bootstrap_ cluster hosts the Kubernetes controllers needed to create the admin cluster. When you create the admin cluster, the controllers on the bootstrap cluster will provision nodes, run preflight checks, and register the admin cluster to the fleet. The bootstrap cluster is automatically deleted after the cluster is successfully created.

### Console

  1. In the console, go to the **Create a Distributed Cloud cluster** page.

[Go to Create a Distributed Cloud cluster](https://console.cloud.google.com/kubernetes/baremetal/add)

  2. Make sure to select `PROJECT_ID` from the project list.

  3. In the left-navigation bar, click **Install bootstrap environment**.

  4. Enter `ADMIN_CLUSTER_NAME` as the admin cluster name. Notice that the bootstrap cluster name is derived by prepending _bootstrap-_ to the admin cluster name.

  5. Select `VERSION` as the version for your admin cluster. The script downloaded this version of the `bmctl` command-line tool to the admin workstation. The Google Distributed Cloud version that you install must match the `bmctl` version.

  6. In the **Google Cloud API Location** field, select ON_PREM_API_REGION from the list. This setting specifies the region where the GKE On-Prem API runs, and the region in which the following are stored:

     * The cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.




Use the steps in the next section instead of the steps displayed in the console to create the bootstrap cluster. Leave the console page displayed because you will come back there to create the admin cluster.

###  gcloud CLI 

Open a new terminal window. You will use the second terminal window to connect to the admin workstation to create the bootstrap cluster. You will use the first terminal window to run the gcloud CLI command to create the admin cluster.

### Create the bootstrap cluster

Do the following steps on your admin workstation.

  1. Use SSH to access the admin workstation as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

You can ignore any messages about updating the VM and complete this tutorial. If you plan to keep the VMs as a test environment, you might want to update the OS or upgrade to the next release as described in the [Ubuntu documentation](https://ubuntu.com/server/docs/upgrade-introduction).

  2. Set your user credentials as Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

Follow the prompts to select your Google Account for ADC.

  3. Create the bootstrap cluster.
         
         bmctl register bootstrap \
           --ssh-key=/root/.ssh/id_rsa \
           --name=bootstrap-ADMIN_CLUSTER_NAME \
           --project-id=PROJECT_ID
         




After `bmctl` successfully creates the bootstrap cluster, you see output similar to the following:
    
    
    [2023-03-22 17:35:24+0000] Waiting for the temporary cluster to be registered... OK
    [2023-03-22 17:35:37+0000] Please go to https://console.cloud.google.com/home/dashboard?project=example-project-12345 to create the cluster
    [2023-03-22 17:35:37+0000] Waiting for preflight checks and cluster to run..
    

**Caution:** Leave the command running while you create the admin cluster. If you exit out of the `bmctl register bootstrap` command before the admin cluster is created, the admin cluster creation fails. After the cluster is successfully created, the command automatically deletes the bootstrap cluster and exits.

### Create the admin cluster

### Console

  1. On the **Install bootstrap environment** page in the **Bootstrap environment from admin workstation** section, click **Check Connection**.

On success, the console displays check_circle **Connection established**.

The connection to the bootstrap cluster must be established before you continue. If the connection isn't established, check the arguments that you specified to the `bmctl register bootstrap` command:

     * Make sure that the value for `--name` matches the **Derived bootstrap name** displayed in the **Bootstrap environment basics** section.

     * Make sure the value for `--project-id` matches the ID of the project that you selected in the console.

If you need to change the bootstrap cluster name or the project ID, enter `Ctrl-C` to exit out of `bmctl register bootstrap` and re-run the command.

  2. Click **Networking** in the left-navigation bar.

  3. In the **Control plane** section, enter the following in the **Control plane node IP 1** field:
         
         10.200.0.3
         

This is the IP address of the abm-admin-cluster-cp VM in the VXLAN created by the script.

  4. In the **Load balancer** section, make sure that **Bundled** is selected.

  5. In the **Virtual IPs (VIPs)** section, enter the following in the **Control plane VIP** field:
         
         10.200.0.48
         

  6. Click **Verify and Create**.

The console displays status messages as it verifies the settings and creates the cluster.




###  gcloud CLI 

  1. Ensure the environment variables that you defined previously have the correct values. Although the example command uses placeholders, they need to match the environment variables that the script used.
         
         echo $PROJECT_ID
         echo $ADMIN_CLUSTER_NAME
         echo $ON_PREM_API_REGION
         echo $BMCTL_VERSION
         

  2. Confirm that the bootstrap cluster has been registered as a member of the fleet:
         
         gcloud container fleet memberships list \
           --project=PROJECT_ID
         

If the bootstrap cluster isn't listed, check the bootstrap cluster name and project ID that you specified to `bmctl register bootstrap`. If you need to change the bootstrap cluster name or the project ID, enter `Ctrl-C` to exit out of `bmctl register bootstrap` and re-run the command.

  3. Create the admin cluster with the bundled load balancer:
         
         gcloud container bare-metal admin-clusters create ADMIN_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=ON_PREM_API_REGION \
           --version=BMCTL_VERSION \
           --max-pods-per-node=110 \
           --control-plane-vip=10.200.0.48 \
           --control-plane-load-balancer-port=443 \
           --control-plane-node-configs node-ip=10.200.0.3 \
           --island-mode-service-address-cidr-blocks=10.96.0.0/20 \
           --island-mode-pod-address-cidr-blocks=192.168.0.0/16 \
           --lvp-share-path=/mnt/localpv-share \
           --lvp-share-storage-class=local-shared \
           --lvp-node-mounts-config-path=/mnt/localpv-disk \
           --lvp-node-mounts-config-storage-class=local-disks
         

In the previous command:

     * `--control-plane-vip`: Is set to `10.200.0.48`. This is the virtual IP (VIP) on the load balancer for the cluster's Kubernetes API server.

     * `--control-plane-node-configs`: The `node-ip` is set to `10.200.0.3`. This is the IP address of the abm-admin-cluster-cp VM in the VXLAN created by the script.

For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/create).

The output from the command is similar to the following:
    
    Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
    

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation by running the following command in another terminal window:
    
    gcloud container bare-metal operations describe OPERATION_ID \
      --project=PROJECT_ID \
      --location=ON_PREM_API_REGION
    




Details about the cluster creation process are output on your admin workstation. Before creating the cluster, `bmctl` runs a series of preflight checks to verify the configuration. If the preflight checks pass, you see something like the following:
    
    
    [2023-03-22 23:12:47+0000] Waiting for cluster kubeconfig to become ready OK
    [2023-03-22 23:15:47+0000] Writing kubeconfig file
    [2023-03-22 23:15:47+0000] kubeconfig of cluster being created is present at bmctl-workspace/abm-cluster-1/abm-cluster-1-kubeconfig
    [2023-03-22 23:15:47+0000] Please restrict access to this file as it contains authentication credentials of your cluster.
    [2023-03-22 23:15:47+0000] Waiting for cluster to become ready OK
    [2023-03-22 23:20:17+0000] Please run
    [2023-03-22 23:20:17+0000] kubectl --kubeconfig bmctl-workspace/abm-cluster-1/abm-cluster-1-kubeconfig get nodes
    [2023-03-22 23:20:17+0000] to get cluster nodes status.
    [2023-03-22 23:20:17+0000] Waiting for node pools to become ready OK
    [2023-03-22 23:20:37+0000] Waiting for metrics to become ready in GCP OK
    [2023-03-22 23:25:38+0000] Waiting for cluster API provider to install in the created admin cluster OK
    [2023-03-22 23:25:48+0000] Moving admin cluster resources to the created admin cluster
    [2023-03-22 23:25:51+0000] Waiting for node update jobs to finish OK
    [2023-03-22 23:27:41+0000] Flushing logs... OK
    [2023-03-22 23:27:41+0000] Deleting membership... OK
    [2023-03-22 23:27:42+0000] Deleting bootstrap cluster.
    

## Verify the admin cluster

You can find your admin cluster's `kubeconfig` file on the admin workstation in the `bmctl-workspace` directory of the root account. To verify your deployment, complete the following steps.

  1. If the script created the admin cluster, use SSH to access the admin workstation as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

You can ignore any messages about updating the VM and complete this tutorial. If you plan to keep the VMs as a test environment, you might want to update the OS or upgrade to the next release as described in the [Ubuntu documentation](https://ubuntu.com/server/docs/upgrade-introduction).

  2. Set the `KUBECONFIG` environment variable with the path to the cluster's configuration file to run `kubectl` commands on the cluster.
         
         export clusterid=ADMIN_CLUSTER_NAME
         export KUBECONFIG=$HOME/bmctl-workspace/$clusterid/$clusterid-kubeconfig
         kubectl get nodes
         

The output is similar to the following:
         
         NAME                   STATUS   ROLES                  AGE   VERSION
         abm-admin-cluster-cp   Ready    control-plane,master   91m   v1.24.2-gke.1900
         

  3. Set the current context in an environment variable:
         
         export CONTEXT="$(kubectl config current-context)"
         

  4. Run the following `gcloud` command. This command does the following:

     * Grants your user account the Kubernetes `clusterrole/cluster-admin` role on the cluster.
     * Configures the cluster so that you can run `kubectl` commands on your local computer without having to SSH to the admin workstation.
     * Lets you sign in to the cluster in the console using your Google identity.

Replace `YOUR_EMAIL_ADDRESS` with the email address that is associated with your Google Cloud account. For example: `--users=alex@example.com`.
    
    gcloud container fleet memberships generate-gateway-rbac  \
        --membership=ADMIN_CLUSTER_NAME \
        --role=clusterrole/cluster-admin \
        --users=YOUR_EMAIL_ADDRESS \
        --project=PROJECT_ID \
        --kubeconfig=$KUBECONFIG \
        --context=$CONTEXT\
        --apply
    

The output of this command is similar to the following, which is truncated for readability:
    
    Validating input arguments.
    Specified Cluster Role is: clusterrole/cluster-admin
    Generated RBAC policy is:
    --------------------------------------------
    ...
    
    Applying the generate RBAC policy to cluster with kubeconfig: /root/bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig, context: ADMIN_CLUSTER_NAME-admin@ADMIN_CLUSTER_NAME
    Writing RBAC policy for user: YOUR_EMAIL_ADDRESS to cluster.
    Successfully applied the RBAC policy to cluster.
    

  5. When you are finished exploring, enter **exit** to log out of the admin workstation.

  6. Run the following command on your local computer to get the kubeconfig entry that can access the cluster through the [connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway):
         
         gcloud container fleet memberships get-credentials ADMIN_CLUSTER_NAME
         

The output is similar to the following:
         
         Starting to build Gateway kubeconfig...
         Current project_id: PROJECT_ID
         A new kubeconfig entry "connectgateway_PROJECT_ID_global_ADMIN_CLUSTER_NAME" has been generated and set as the current context.
         

  7. You can now run `kubectl` commands through the connect gateway:
         
         kubectl get nodes
         

The output is similar to the following:
         
         NAME                   STATUS   ROLES                  AGE   VERSION
         abm-admin-cluster-cp   Ready    control-plane,master   94m   v1.24.2-gke.1900
         




In Google Distributed Cloud 1.16 and later, the cluster is automatically enrolled in the GKE On-Prem API. This lets you use the gcloud CLI and the console to upgrade and update the admin cluster.

## Create the user cluster

When the script created the L2 VXLAN for the VMs, it assigned the following IP addresses in the 10.200.0.0/24 network. You use these IP addresses when configuring network and node pool settings for the user cluster.

VM Name | Network IP | Node description  
---|---|---  
abm-admin-cluster-cp1 | 10.200.0.3 | Control plane node for the admin cluster  
abm-user-cluster-cp1 | 10.200.0.4 | Control plane node for the user cluster  
abm-user-cluster-w1 | 10.200.0.5 | Worker node for the user cluster  
abm-user-cluster-w2 | 10.200.0.6 | Another worker node for the user cluster  
  
You can use the Google Cloud console, the Google Cloud CLI, or Terraform to create the user cluster.

### Console

Do the following steps to create a user cluster in the console:

  1. In the console, go to the **Create a Distributed Cloud cluster** page.

[Go to Create a Distributed Cloud cluster](https://console.cloud.google.com/kubernetes/baremetal/add)

  2. Make sure that the Google Cloud project in which you created the admin cluster is selected.

  3. Under **Choose your cluster type** , select **Create a user cluster for an existing admin cluster**

  4. Click **Next**.




### Cluster basics

  1. Enter a name for the user cluster or use the default.

  2. Make sure that the newly created admin cluster is selected. You can use the defaults for the rest of the settings on this page.

  3. Click **Networking** in the left-navigation bar.




### Networking

  1. In the **Control plane** section, enter the following in the **Control plane node IP 1** field:
         
         10.200.0.4
         

This is the IP address of the abm-user-cluster-cp1 VM in the VXLAN created by the script.

  2. In the **Load balancer** section, use the default load balancer, **Bundled with MetalLB**.

  3. In the **New address pool** section, enter the following IP address range in the **IP address range 1** field:
         
         10.200.0.51-10.200.0.70
         

  4. Click **Done**.

  5. In the **Virtual IPs** section, enter the following IP address in the **Control Plane VIP** field:
         
         10.200.0.50
         

  6. Enter the following IP address for the **Ingress VIP** :
         
         10.200.0.51
         

  7. Use the default IP addresses in the **Service and Pod CIDRs** section.

  8. Click **default pool** in the left-navigation bar.




### Create a node pool

Your cluster must have at least one node pool for worker nodes. A node pool is a template for the groups of worker nodes created in this cluster.

Enter the following IP address in the **Nodes address 1** field:
    
    
    10.200.0.5
    

This is the IP address of the abm-user-cluster-w1 VM in the VXLAN created by the script.

### Create the cluster

  1. Click **Verify and Create** to create the user cluster.

It takes 15 minutes or more to create the user cluster. The console displays status messages as it verifies the settings and creates the cluster.

If there is a problem with the configuration, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.

To see additional information about the creation process, click **Show details** to display a side panel. Click close to close the details panel.

When the cluster is created, **Cluster status: running** is displayed.

![Screenshot cluster ready](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/cluster-status-running.png)

  2. After the cluster is created, click arrow_back **Clusters** to go back to the **Clusters** page.




###  gcloud CLI 

You use the following command to create a user cluster:
    
    
    gcloud container bare-metal clusters create
    

After creating the cluster, you need to create at least one node pool using the following command:
    
    
    gcloud container bare-metal node-pools create
    

To create the user cluster:

  1. Ensure the environment variables that you defined previously have the correct values. Although the example command uses placeholders, they need to match the environment variables that the script used.
         
         echo $PROJECT_ID
         echo $ADMIN_CLUSTER_NAME
         echo $ON_PREM_API_REGION
         echo $BMCTL_VERSION
         

  2. Run the following command to create the user cluster. Replace the the following:

     * `USER_CLUSTER_NAME`: The name for the cluster.

     * Be sure that `--admin-users` is set to the email address associated with your Google Account so that you can administer the cluster.

The rest of the flag values have been filled out for you. Scroll over if needed to verify that the `--admin-cluster-membership` flag has the correct value for the admin cluster name, which is the last segment in the fully-specified membership name.
    
    gcloud container bare-metal clusters create USER_CLUSTER_NAME \
      --project=PROJECT_ID \
      --admin-cluster-membership=projects/PROJECT_ID/locations/global/memberships/ADMIN_CLUSTER_NAME \
      --location=ON_PREM_API_REGION \
      --version=BMCTL_VERSION \
      --admin-users=YOUR_EMAIL_ADDRESS \
      --metal-lb-address-pools='pool=lb-pool-1,manual-assign=True,addresses=10.200.0.51-10.200.0.70' \
      --control-plane-node-configs='node-ip=10.200.0.4' \
      --control-plane-vip=10.200.0.50 \
      --control-plane-load-balancer-port=443 \
      --ingress-vip=10.200.0.51 \
      --island-mode-service-address-cidr-blocks=10.96.0.0/20 \
      --island-mode-pod-address-cidr-blocks=192.168.0.0/16 \
      --lvp-share-path=/mnt/localpv-share \
      --lvp-share-storage-class=local-shared \
      --lvp-node-mounts-config-path=/mnt/localpv-disk \
      --lvp-node-mounts-config-storage-class=local-disks
    




The following list describes the flags:

  * `--project`: The ID of the project in which the user cluster will be registered. This project is referred to as the fleet host project.

  * `--admin-cluster-membership`: The fully-specified admin cluster name that identifies the admin cluster in the fleet.

  * `--location`: The Google Cloud region in which the GKE On-Prem API runs and stores its metadata.

  * `--version`: The Google Distributed Cloud version.

  * `--admin-users`: Include your email address to be granted the Kubernetes role-based access control (RBAC) policies that gives you full administrative access to the cluster.

  * `--metal-lb-address-pools`: The address pool configuration for the bundled MetalLB load balancer. The IP address range must be in the `10.200.0.0/24` network that the script created. The address range must not contain the IP addresses assigned to the VMs nor the control plane VIP. Note, however, that the ingress VIP must be in this address range.

  * `--control-plane-node-configs`: The control plane node configuration for the user cluster. The value for `node-ip` is `10.200.0.4`, which is the IP address that the script assigned to the VM `abm-user-cluster-cp1`.

  * `--control-plane-vip`: The virtual IP for the control plane. The value `10.200.0.50`is in the `10.200.0.0/24` network that the script created, but doesn't overlap with the IP address range used for the MetalLB load balancer address pools.

  * `--control-plane-load-balancer-port`: The port the load balancer serves the control plane on. Although you can configure another value, port `443` is the standard port used for HTTPS connections.

  * `--ingress-vip`: The virtual IP for the ingress service. This IP address must be in the IP address range used for the MetalLB load balancer address pools.

  * `--island-mode-service-address-cidr-blocks`: A range of IP addresses, in CIDR format, to be used for Services in the user cluster. The example command used `10.96.0.0/20`, which is the default value provided by the console. The CIDR range must be between /24 and /12, where /12 provides the most IP addresses. We recommend that you use a range in the IP address space for private internets, as defined in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918).

  * `--island-mode-pod-address-cidr-blocks`: A range of IP addresses, in CIDR format, to be used for Pods in the user cluster. The example command used `192.168.0.0/16`, which is the default value provided by the console. The CIDR range must be between /18 and /8, where /8 provides the most IP addresses. We recommend that you use a range in the IP address space for private internets, as defined in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918).

  * `--lvp-share-path`: This is the host machine path where subdirectories can be created. A local PersistentVolume (PV) is created for each subdirectory.

  * `--lvp-share-storage-class`: This is the StorageClass to use to create persistent volumes. The StorageClass is created during cluster creation.

  * `--lvp-node-mounts-config-path`: This is the host machine path where mounted disks can be discovered. A local PersistentVolume (PV) is created for each mount.

  * `--lvp-node-mounts-config-storage`: The storage class that PVs are created with during cluster creation.




After running the command, you see output like the following:
    
    
    Waiting for operation [projects/PROJECT_ID/locations/ON_PREM_API_REGION/operations/operation-1678304606537-5f668bde5c57e-341effde-b612ff8a] to complete...
    

In the example output, the string `operation-1678304606537-5f668bde5c57e-341effde-b612ff8a` is the `OPERATION_ID` of the long-running operation.

To find out the status of the operation, copy the `OPERATION_ID` from your output into the following command. Open another terminal window and run the command.
    
    
    gcloud container bare-metal operations describe OPERATION_ID \
        --project=PROJECT_ID \
        --location=ON_PREM_API_REGION
    

It takes about 15 minutes or more to create the cluster. As the cluster is being created, you can run the previous command every so often to get the current status.

When the cluster is created, you see output like the following:
    
    
    Created Anthos cluster on bare metal [https://gkeonprem.googleapis.com/v1/projects/PROJECT_ID/locations/ON_PREM_API_REGION/bareMetalClusters/USER_CLUSTER_NAME].
    

### Create a node pool

After the cluster is successfully created, run the following command to create a node pool. Replace `NODE_POOL_NAME` with a name for the node pool, and ensure that the placeholder for the the `--cluster` flag is still set to the user cluster's name.
    
    
    gcloud container bare-metal node-pools create NODE_POOL_NAME \
      --cluster=USER_CLUSTER_NAME \
      --project=PROJECT_ID \
      --location=ON_PREM_API_REGION \
      --node-configs='node-ip=10.200.0.5'

  * `-node-configs`: The value assigned to `node-ip` is the IP address of the abm-user-cluster-w1 VM in the VXLAN created by the script.



After running the command, you see output like the following:
    
    
    Waiting for operation [projects/PROJECT_ID/locations/ON_PREM_API_REGION/operations/operation-1678308682052-5f669b0d132cb-6ebd1c2c-816287a7] to complete...
    

It takes about 5 minutes or less to create the node pool. When the node pool is created, you see output like the following:
    
    
    Created node pool in Anthos cluster on bare metal [https://gkeonprem.googleapis.com/v1/projects/PROJECT_ID/locations/ON_PREM_API_REGION/bareMetalClusters/USER_CLUSTER_NAME/bareMetalNodePools/NODE_POOL_NAME].
    

### Other user cluster commands

In addition to creating clusters, there are other gcloud CLI commands that you can run, for example:

  * To list your user clusters:


    
    
    gcloud container bare-metal clusters list \
        --project=PROJECT_ID \
        --location=ON_PREM_API_REGION
    

  * To describe a user cluster:


    
    
    gcloud container bare-metal clusters describe USER_CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=ON_PREM_API_REGION
    

For more information, see [gcloud container bare-metal clusters](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters).

### Other node pool commands

In addition to creating node pools, there are other gcloud CLI commands that you can run, for example:

  * To list node pools:


    
    
    gcloud container bare-metal node-pools list \
        --cluster=USER_CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=ON_PREM_API_REGION
    

  * To describe a node pool:


    
    
    gcloud container bare-metal node-pools describe NODE_POOL_NAME \
        --cluster=USER_CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=ON_PREM_API_REGION
    

For more information, see [gcloud container bare-metal node-pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools).

### Terraform

You can use the following basic configuration sample to create a user cluster with bundled MetalLB load balancer. For more information, see the [`google_gkeonprem_bare_metal_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster).

  1. In the directory where you cloned `anthos-samples`, change to the directory where the Terraform sample is located:
         
         cd anthos-samples/anthos-onprem-terraform/abm_user_cluster_metallb
         

The sample provides an example variables file to pass in to `main.tf`.

  2. Make a copy of the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         
         
         project_id          = "PROJECT_ID"
         region              = "ON_PREM_API_REGION"
         admin_cluster_name  = "ADMIN_CLUSTER_NAME"
         bare_metal_version  = "VERSION"
         admin_user_emails   = ["YOUR_EMAIL_ADDRESS", "ADMIN_2_EMAIL_ADDRESS"]
         cluster_name        = "abm-user-cluster-metallb"
         control_plane_ips   = ["10.200.0.4"]
         worker_node_ips     = ["10.200.0.5", "10.200.0.6"]
         control_plane_vip   = "10.200.0.50"
         ingress_vip         = "10.200.0.51"
         lb_address_pools    = [
             { name = "lbpool_1", addresses = ["10.200.0.51-10.200.0.70"] }
         ]
         

  3. Modify the parameters values in `terraform.tfvars`and save the file.

The following list describes the variables:

     * `project_id`: The ID of the project in which the user cluster will be registered. This project is referred to as the fleet host project.

     * `region`: The Google Cloud region that you set at the beginning of the tutorial. Run `echo $ON_PREM_API_REGION` to get the value.

     * `admin_cluster_name`: The name of the admin cluster that you set at the beginning of this tutorial. Run echo `$ADMIN_CLUSTER_NAME` to get the value.

     * `bare_metal_version`: The Google Distributed Cloud version for your user cluster. To use the same version that you used for the admin cluster, run `echo $BMCTL_VERSION` to get the value. If you prefer, you can specify a version that is no more than one minor version lower than the admin cluster version. The user cluster version can't be higher than the admin cluster version.

     * `cluster_name`: You can either use the name in the TVARS file for the user cluster or specify a name of your choice. The name can't be changed after the cluster is created.

     * `admin_user_emails`: A list of email addresses of the users to be granted administrative privileges on the cluster. Be sure to add your email address so that you can administer the cluster.

When the cluster is created, the GKE On-Prem API applies the Kubernetes role-based access control (RBAC) policies to the cluster to grant the admin users the Kubernetes `clusterrole/cluster-admin` role, which provides full access to every resource in the cluster in all namespaces. This also lets users log on to the console using their Google identity.

Use the default values defined in `terraform.tvars` for the remaining variables. The script used these values when it created the VMs and admin cluster.

     * `control_plane_ips`: A list of one or more IPv4 addresses for the control plane nodes. Use the default value, which is the IP address that the script assigned to the VM `abm-user-cluster-cp1`.

     * `worker_node_ips`: A list of one or more IPv4 addresses for the worker node machines. Use the default values, which are the IP addresses that the script assigned to the VMs `abm-user-cluster-w1` and `abm-user-cluster-w2`.

     * `control_plane_vip`: The virtual IP (VIP) for the control plane. Use the default value, `10.200.0.50`, which is in the `10.200.0.0/24` network that the script created. Note that this IP address doesn't overlap with the IP address range used for the MetalLB load balancer address pools.

     * `ingress_vip`: The virtual IP address to configure on the load balancer for the ingress proxy. Use the default value, `10.200.0.51`, which is in the `10.200.0.0/24` network that the script created. Note that this IP address is in the IP address range used for the MetalLB load balancer address pools.

     * `lb_address_pools`: A list of maps that define the address pools for the MetalLB load balancer. Use the default value.

  4. Save the changes in `terraform.tfvars`.

  5. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider. 

  6. Review the configuration and make changes if needed:
         
         terraform plan
         

  7. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         

It takes 15 minutes or more to create the user cluster. You can view the cluster in the Google Cloud console on the [**GKE clusters**](https://console.cloud.google.com/kubernetes/list/overview) page.




## Connect to the user cluster

When you create a user cluster using the console or the gcloud CLI, the cluster is configured with the same Kubernetes role-based access control (RBAC) policies that you configured for the admin cluster when you ran `gcloud container fleet memberships generate-gateway-rbac`. These RBAC policies let you connect to the cluster using your Google Cloud identity, which is the email address associated with your Google Cloud account. These RBAC policies let you sign in to the console without any additional configuration.

### Connect to the cluster in the console

If you used the gcloud CLI or Terraform to create the user cluster, go to the **GKE clusters** page in the console:

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

Make sure that the project in which you created the user cluster is selected. You should see both the admin and user cluster on the list.

Notice that the user cluster has **Bare metal: User** in the **Type** column. This indicates that the cluster is managed by the GKE On-Prem API.

If you used the script to create the admin cluster, it has **External** in the **Type** column. This indicates that the cluster isn't managed by the GKE On-Prem API. You can [configure the admin cluster to be managed by the GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/enroll-cluster) after the cluster is created.

![Screenshot cluster list](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/anthos_clusters_not_login.png)

To login to a cluster:

  1. Click the link on the cluster name, and on the side panel, click **Login**.

  2. Select **Use your Google identity to log in**.

  3. Click **Login**.




Repeat the same steps to log into the admin cluster as well.

![Screenshot cluster list](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/images/anthos_clusters_login.png)

### Connect to the cluster on the command line

The GKE On-Prem API configures the RBAC policies for you as the user cluster creator. These policies let you run `kubectl` commands on your local desktop using the connect gateway `kubeconfig`.

From your local computer:

  1. Get the `kubeconfig` entry that can access the cluster through the connect gateway.
         
         gcloud container fleet memberships get-credentials USER_CLUSTER_NAME
         

The output is similar to the following:
         
         Starting to build Gateway kubeconfig...
         Current project_id: PROJECT_ID
         A new kubeconfig entry "connectgateway_PROJECT_ID_global_USER_CLUSTER_NAME" has been generated and set as the current context.
         

  2. You can now run `kubectl` commands through the connect gateway:
         
         kubectl get nodes
         

The output is similar to the following:
         
         NAME                  STATUS   ROLES                  AGE     VERSION
         abm-user-cluster-cp   Ready    control-plane,master   14m     v1.24.2-gke.1900
         abm-user-cluster-w1   Ready    worker                 8m28s   v1.24.2-gke.1900
         




## Add another node pool to the user cluster

### Console

  1. In the console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the cluster list, click the name of the cluster, and then click **More details** in the **Details** panel.

  3. Click the **Nodes** tab.

  4. Click add **Add Node Pool**.

  5. Enter a name for the node pool.

  6. In the **Nodes address 1** field, enter the following IP address:
         
         10.200.0.6
         

This is the IP address of the abm-user-cluster-w2 VM that the script created.

  7. Click **Create**

  8. Click the **Nodes** tab again if needed.

  9. The new node pool shows a status of **Reconciling**.

  10. Click notifications in the top-right corner to view the status of the node pool creation. You might have to refresh the page to see the updated status in the node pools list.




###  gcloud CLI 

Run the following command to create another node pool. Replace `NODE_POOL_NAME_2` with a name for the node pool, and ensure that the placeholder for the `--cluster` flag is still set to the user cluster's name.
    
    
    gcloud container bare-metal node-pools create NODE_POOL_NAME_2 \
      --cluster=USER_CLUSTER_NAME \
      --project=PROJECT_ID \
      --location=ON_PREM_API_REGION \
      --node-configs='node-ip=10.200.0.6'

  * `-node-configs`: The value assigned to `node-ip` is the IP address of the abm-user-cluster-w2 VM in the VXLAN created by the script.



### Terraform

If you created the cluster using Terraform, the cluster was created with two nodes, so there aren't any additional VMs in the VXLAN available to add another node. For information on adding node pools, see see the [`google_gkeonprem_bare_metal_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster).

You can also verify the new node using `kubectl`. You first have to run the `gcloud container fleet memberships get-credentials` command as shown earlier to fetch the cluster config:
    
    
    kubectl get nodes
    

The output is similar to the following:
    
    
    NAME                  STATUS   ROLES                  AGE     VERSION
    abm-user-cluster-cp   Ready    control-plane,master   24m   v1.24.2-gke.1900
    abm-user-cluster-w1   Ready    worker                 18m   v1.24.2-gke.1900
    abm-user-cluster-w2   Ready    worker                 52s   v1.24.2-gke.1900
    

## Clean up

The following sections include instructions for removing the clusters and VMs that you created with this guide.

### Delete the user cluster

### Console

  1. In the console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the list of clusters, click the user cluster.

  3. In the **Details** panel, click **More details**.

  4. Near the top of the window, click delete  **Delete**.

  5. When prompted to confirm, enter the cluster name and click **Confirm**.

  6. Click notifications in the top-right corner to view the status of the deletion. You might have to refresh the page to update the clusters list.




###  gcloud CLI 

Run the following command to delete the cluster:
    
    
    gcloud container bare-metal clusters delete USER_CLUSTER_NAME \
      --project=PROJECT_ID \
      --location=ON_PREM_API_REGION \
      --force
    

The `--force` flag lets you delete a cluster that has node pools. Without the `--force` flag, you have to [delete the node pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/delete) first, and then delete the cluster.

For information about other flags, see [gcloud container bare-metal clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete).

### Terraform

Run the following command:
    
    
    terraform destroy
    

Wait for the user cluster to be deleted before deleting the admin cluster and VMs.

### Delete the admin cluster and VMs

  1. Unenroll the admin cluster from the GKE On-Prem API:
         
         gcloud container bare-metal admin-clusters unenroll ADMIN_CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=ON_PREM_API_REGION
         

  2. Connect to the admin workstation:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

  3. Delete the admin cluster:
         
         bmctl reset -c ADMIN_CLUSTER_NAME
         

`bmctl` unregisters the cluster from the fleet and then deletes the cluster. Wait for the cluster to be deleted before deleting the VMs.

  4. Exit the admin workstation.

  5. List all VMs that have `abm` in their name:
         
         gcloud compute instances list | grep 'abm'
         

  6. Verify that you're fine with deleting all VMs that contain `abm` in the name.

After you've verified, you can delete `abm` VMs by running the following command:
         
         gcloud compute instances list --format="value(name)" | \
           grep 'abm'  | \
           xargs gcloud --quiet compute instances delete --zone ZONE
         

  7. Delete the service account:
         
         gcloud iam service-accounts delete baremetal-gcr@PROJECT_ID.iam.gserviceaccount.com
         

At the confirmation prompt, enter **y**.

## What's next



  * [Create a Service and an Ingress](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/create-service-ingress)
  * [Plan your installation](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/minimal-infrastructure)
  * [Create basic clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
