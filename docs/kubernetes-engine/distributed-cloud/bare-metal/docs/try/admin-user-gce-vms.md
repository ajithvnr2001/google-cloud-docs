---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/admin-user-gce-vms/
title: Create demo Google Distributed Cloud admin and user clusters on Compute Engine VMs \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:24.914175+00:00
---

# Create demo Google Distributed Cloud admin and user clusters on Compute Engine VMs  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/admin-user-gce-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create demo Google Distributed Cloud admin and user clusters on Compute Engine VMs Stay organized with collections  Save and categorize content based on your preferences. 

Learn about Distributed Cloud software only for bare metal by creating demo clusters on Compute Engine Virtual Machines (VMs). In this tutorial, you run a script that does the following:

  * Provisions five Compute Engine VMs for installing your demo clusters
  * Sets up a VPC network to provide cluster connectivity



After the script provisions the necessary resources, you use one of the following clients to create an admin cluster and an accompanying user cluster that can host workloads: `bmctl`, Google Cloud console, Google Cloud CLI, or Terraform. Completing this tutorial can take 40 minutes to an hour.

The demo clusters you create in this guide help you evaluate the process for provisioning and operating Google Distributed Cloud clusters, but they aren't intended for use in production.

**Note:** Distributed Cloud software only for bare metal was formerly known as Google Distributed Cloud Virtual, which was previously known as Anthos clusters on bare metal.

## Procedure overview

In this tutorial, you'll complete the following steps:

  1. **Prepare your local environment** so that the script has the required environment variables and you've gathered the basic information needed to run commands.

  2. **Create the VMs and network** with the downloaded script.

  3. **Create the admin cluster** with one of the supported clients.

  4. **Create the user cluster** with one of the supported clients.

  5. **Clean up** to remove the clusters and VMs you created with this guide.




## 1\. Prepare your local environment

Because this guide uses a script that sets up the network for you, you don't need to gather much information or do any planning. The following steps set up your local environment and gather the basic information you need in subsequent sections of the guide:

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

  6. Make a note of the project ID, because you need it to set an environment variable that is used in the script and commands on this page. If you selected an existing project, make sure that you are either a project owner or editor. 
  7. You can run the script on [Cloud Shell](https://docs.cloud.google.com/shell/docs) or your local machine running Linux or macOS. If you're using a local machine, make sure your environment has the required tools installed: 
     1. Make sure you have installed the latest [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), the command line tool for interacting with Google Cloud. Update the gcloud CLI components, if needed: 
            
            gcloud components update

Depending on how the gcloud CLI was installed, you might see the following message:
            
            You cannot perform this action because the Google Cloud CLI component manager is disabled for this installation. You can run the following command to achieve the same result for this installation:

Follow the instructions to copy and paste the command to update the components.

     2. Make sure you have `kubectl` installed: 
            
            kubectl

You should see usage information for `kubectl`. If the command is not available, install `kubectl`: 
            
            gcloud components install kubectl

  8. Make sure your project has a VPC network named "default". 

If you don't have a "default" VPC network, the script in the following section fails to provision the necessary resources. Unless you choose to delete or restrict it, each new project starts with an auto mode VPC network named "default" that should work with the script. For more information, see [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc).

  9. Ensure the following organization policy constraints aren't enforced: 
     * `constraints/iam.disableServiceAccountKeyCreation`
     * `constraints/compute.vmCanIpForward`
     * `constraints/compute.requireShieldedVm`
     * `constraints/compute.vmExternalIpAccess`

If these constraints are enforced, the script in the following section fails to provision the necessary resources. For a new project, these constraints are set to Inactive (unenforced) by default. For more information, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

  10. Setup environment variables: 
         
         export PROJECT_ID=PROJECT_ID
         export ADMIN_CLUSTER_NAME=ADMIN_CLUSTER_NAME
         export ON_PREM_API_REGION=ON_PREM_API_REGION
         export ZONE=ZONE

     * `ADMIN_CLUSTER_NAME`: the name you choose for the admin cluster.
     * `ON_PREM_API_REGION`: the Google Cloud region in which the GKE On-Prem API runs and stores its metadata. Specify `us-central1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api).
     * `ZONE`: the Google Cloud zone that the Compute Engine VMs are created in. You can use `us-central1-a` or any of the other [Compute Engine zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  11. Run the following commands to set the default project and zone. 
         
         gcloud config set project $PROJECT_ID
         gcloud config set compute/zone $ZONE

If you get a `PERMISSION_DENIED` error, double check the project ID that you entered. If the project ID is correct, run `gcloud auth login` to sign in to the gcloud CLI with the account that has access to the project.

  12. Get a list of supported versions that you can install: 
         
         gcloud container bare-metal admin-clusters query-version-config \
             --location=ON_PREM_API_REGION

  13. Select a version from the output of the previous command and set it in an environment variable: 
         
         export BMCTL_VERSION=BMCTL_VERSION

We recommend that you select the highest compatible version to get the latest Google Distributed Cloud features and fixes.




## 2\. Create the VMs and the network

In this section, you download and run the `install_admin_cluster.sh` script.

  1. Clone the `anthos-samples` repository and change to the directory where the script is located:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-samples
         cd anthos-samples/anthos-bm-gcp-bash
         

  2. Run the script:
         
         bash install_admin_cluster.sh
         

  3. At the prompt, enter `2` to set up the Compute Engine infrastructure only and confirm your selection when prompted.

The script creates Compute Engine VMs, creates a VXLAN network, and sets up the admin workstation and cluster nodes. This infrastructure takes about 5 minutes to set up.

To learn more about the script, click the following link:

#### About the script

You can view the script in the [`anthos-bm-gcp-bash`](https://github.com/GoogleCloudPlatform/anthos-samples/blob/main/anthos-bm-gcp-bash) folder in the [anthos-samples](https://github.com/GoogleCloudPlatform/anthos-samples) GitHub repository. The script does the following: 

     1. Enables the following Google Cloud APIs: 
            
            anthos.googleapis.com
            anthosaudit.googleapis.com
            anthosgke.googleapis.com
            cloudresourcemanager.googleapis.com
            connectgateway.googleapis.com
            container.googleapis.com
            compute.googleapis.com
            gkeconnect.googleapis.com
            gkehub.googleapis.com
            gkeonprem.googleapis.com
            serviceusage.googleapis.com
            stackdriver.googleapis.com
            monitoring.googleapis.com
            logging.googleapis.com
            kubernetesmetadata.googleapis.com
            iam.googleapis.com
            opsconfigmonitoring.googleapis.com

     2. Instead of creating multiple service accounts for different APIs and services, the script creates a single service account called `baremetal-gcr` and grants it the following IAM roles: 
        * `roles/gkehub.admin`
        * `roles/gkehub.connect`
        * `roles/logging.logWriter`
        * `roles/monitoring.dashboardEditor`
        * `roles/monitoring.metricWriter`
        * `roles/monitoring.viewer`
        * `roles/opsconfigmonitoring.resourceMetadata.writer`
        * `roles/serviceusage.serviceUsageViewer`
        * `roles/stackdriver.resourceMetadata.writer`
     3. Creates the following VMs: 
        * One VM for the admin workstation 
        * One VM for the control plane node of the admin cluster 
        * Two VMs for the worker nodes of the user cluster 
        * One VM for the control plane node of the user cluster 
     4. Verifies that SSH is enabled on all VMs and that the admin workstation has SSH access to all the other VMs that were created for cluster nodes. 
     5. Creates a Virtual Extensible LAN (VXLAN) overlay network for Layer 2 connectivity between the VMs. The VXLAN isn't persistent, so if you reboot a VM instance the network is destroyed. The network is set up to be on the `10.200.0.0/24` subnet. The Layer 2 connectivity is a requirement for the [bundled load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/bundled-lb). 
     6. Installs the following tools on the admin workstation: 
        * `bmctl`
        * `kubectl`
        * Docker

The script also downloads the service account key for the `baremetal-gcr` service account to the admin workstation. 

     7. Ensures that `root@10.200.0.x` from the admin workstation works by doing the following: 
        1. Generates a new SSH key on the admin workstation. 
        2. Adds the public key to all the other VMs in the deployment. 

The script outputs each command it runs and the status. When it finishes, the script outputs the following:
    
    ✅ Successfully set up SSH access from admin workstation to cluster node VMs.
    
    ✅ GCE Infrastructure setup complete. Please check the logs for any errors!!!
    
    ✅ If you do not see any errors in the output log, then you now have the following setup:
    
    |---------------------------------------------------------------------------------------------------------|
    | VM Name               | L2 Network IP (VxLAN) | INFO                                                    |
    |---------------------------------------------------------------------------------------------------------|
    | abm-admin-cluster-cp  | 10.200.0.3            | 🌟 Ready for use as control plane for the admin cluster |
    | abm-user-cluster-cp   | 10.200.0.4            | 🌟 Ready for use as control plane for the user cluster  |
    | abm-user-cluster-w1   | 10.200.0.5            | 🌟 Ready for use as worker for the user cluster         |
    | abm-user-cluster-w2   | 10.200.0.6            | 🌟 Ready for use as worker for the user cluster         |
    |---------------------------------------------------------------------------------------------------------|
    




## 3\. Create the admin cluster

###  `bmctl`

To create an admin cluster with `bmctl`, you access the admin workstation VM in a terminal window and run commands from there:

  1. Use SSH to access the admin workstation VM, `abm-ws`, as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

  2. Set your user credentials as Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

Follow the prompts to select your Google Account for ADC.

  3. Generate a cluster configuration file:
         
         bmctl create config -c ADMIN_CLUSTER_NAME --project-id=PROJECT_ID
         

  4. Verify the admin cluster configuration file:

The following cluster configuration file is filled in with the values that you provided earlier. In addition to the values you entered, note the following differences from the generated configuration file:

     * Comments have been removed from this sample to improve readability.
     * The script creates a single service account with all required permissions and downloads the `bm-gcr.json` key referenced in the configuration file.
    
    gcrKeyPath: /root/bm-gcr.json
    sshPrivateKeyPath: /root/.ssh/id_rsa
    gkeConnectAgentServiceAccountKeyPath: /root/bm-gcr.json
    gkeConnectRegisterServiceAccountKeyPath: /root/bm-gcr.json
    cloudOperationsServiceAccountKeyPath: /root/bm-gcr.json
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
      anthosBareMetalVersion: BMCTL_VERSION
      gkeConnect:
        projectID: PROJECT_ID
      controlPlane:
        nodePoolSpec:
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
        projectID: PROJECT_ID
        location: ON_PREM_API_REGION
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
          maxPodsPerNode: 110
    

  5. Replace the contents of the generated configuration file on your admin workstation with the contents from the preceding sample.

Open the generated file, `bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME.yaml` and replace its contents with the contents of the sample you verified in the preceding step.

  6. Create the admin cluster:
         
         bmctl create cluster -c ADMIN_CLUSTER_NAME

The `bmctl` command displays output to the screen as it runs preflight checks and creates the cluster. Verbose information is written to logs in the `baremetal/bmctl-workspace/abm-user-cluster-metallb/log` folder on the admin workstation.

Cluster creation can take several minutes to finish.

  7. In the console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

Make sure that the project in which you created the user cluster is selected. You should see the admin cluster listed.

  8. Sign in to the admin cluster:

     1. Click the link on the cluster name, and on the side panel, click **Login**.

     2. Select **Use your Google identity to log in**.

     3. Click **Login**.




### Verify the admin cluster

You can find your admin cluster kubeconfig file on the admin workstation in the `bmctl-workspace` directory of the root account. To verify your deployment, complete the following steps:

  1. Use SSH to access the admin workstation as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

  2. Verify that your admin cluster was created and is running:
         
         kubectl --kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig get nodes
         

The output is similar to the following:
         
         NAME                   STATUS   ROLES              AGE      VERSION
         abm-admin-cluster-cp   Ready    control-plane      94m      1.31.300-gke.81
         

  3. When you are finished exploring, enter `exit` to disconnect from the admin workstation.




###  Console 

To create an admin cluster in the console, you must run `bmctl register bootstrap` from the admin workstation VM to create a bootstrap cluster. While the `bmctl register bootstrap` command is running, you perform steps in the console to create the admin cluster.

### Enter bootstrap environment basics

  1. In the Google Cloud console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click **Create**.

  3. In the **Create a cluster** dialog, select **On-premises** and click **Configure** for bare metal.

  4. Make sure to select `PROJECT_ID` from the project list.

  5. In the left-navigation bar, click **Install bootstrap environment**.

  6. Enter `ADMIN_CLUSTER_NAME` as the admin cluster name.

  7. Select `BMCTL_VERSION` as the version for your admin cluster. The script downloaded this version of the `bmctl` command-line tool to the admin workstation. The Google Distributed Cloud version that you install must match the `bmctl` version.

  8. In the **Google Cloud API Location** field, select ON_PREM_API_REGION from the list. This setting specifies the region where the GKE On-Prem API runs, and the region in which the following are stored:

     * The cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.




Use the steps in the next section instead of the steps displayed in the console to create the bootstrap cluster. Leave the console page displayed because you continue there to create the admin cluster.

### Create the bootstrap cluster

When you use a GKE On-Prem API client, such as the console, to create an admin cluster, you need to create a _bootstrap cluster_ on the admin workstation. The bootstrap cluster hosts the Kubernetes controllers needed to create the admin cluster.

  1. From the command line, use SSH to access the admin workstation VM as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

You can ignore any messages about updating the VM and complete this tutorial. If you plan to keep the VMs as a test environment, you might want to update the OS or upgrade to the next release as described in the [Ubuntu documentation](https://ubuntu.com/server/docs/upgrade-introduction).

  2. Set your user credentials as Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

Follow the prompts to select your Google Account for ADC.

  3. Change to the `baremetal/` directory and run the following command to create the bootstrap cluster.

The bootstrap cluster name is derived by prepending `bootstrap-` to the admin cluster name.

**Note:** There's no need to download `bmctl`, because the script you ran earlier took care of that when it set up the admin workstation.
         
         bmctl register bootstrap \
           --ssh-key=/root/.ssh/id_rsa \
           --name=bootstrap-ADMIN_CLUSTER_NAME \
           --project-id=PROJECT_ID
         

After `bmctl` successfully creates the bootstrap cluster, you see output similar to the following:
         
         [2023-03-22 17:35:24+0000] Waiting for the temporary cluster to be registered... OK
         [2023-03-22 17:35:37+0000] Please go to https://console.cloud.google.com/home/dashboard?project=example-project-12345 to create the cluster
         [2023-03-22 17:35:37+0000] Waiting for preflight checks and cluster to run..
         

**Important:** Leave the command running while you complete the steps in a new terminal window. If you exit out of the `bmctl register bootstrap` command before the admin cluster is created, the admin cluster creation fails. After the admin cluster is successfully created, the command automatically deletes the bootstrap cluster and exits.



### Create the admin cluster

  1. On the **Install bootstrap environment** page in the **Bootstrap environment from admin workstation** section, click **Check Connection**.

On success, the console displays check_circle **Connection established**.

The connection to the bootstrap cluster must be established before you continue. If the connection isn't established, check the arguments that you specified to the `bmctl register bootstrap` command:

     * Make sure that the value for `--name` matches the **Derived bootstrap name** displayed in the **Bootstrap environment basics** section.

     * Make sure the value for `--project-id` matches the ID of the project that you selected in the console.

If you need to change the bootstrap cluster name or the project ID, enter `Ctrl-C` to exit out of `bmctl register bootstrap` and re-run the command.




#### Networking

  1. Click **Networking** in the left-navigation bar.

  2. In the **Control plane** section, enter the following in the **Control plane node IP 1** field:
         
         10.200.0.3
         

This is the IP address of the abm-admin-cluster-cp VM in the VXLAN created by the script.

  3. In the **Load balancer** section, make sure that **Bundled** is selected.

  4. In the **Virtual IPs (VIPs)** section, enter the following in the **Control plane VIP** field:
         
         10.200.0.48
         

The following step depends upon the availability of the bootstrap cluster. The `bmctl register bootstrap` command in the terminal window must run for a few minutes before the bootstrap cluster shows as a registered member. If, after a few minutes, it's still not available, check the bootstrap cluster name and project ID that you used. If you need to change the bootstrap cluster name or the project ID, enter `Ctrl-C` in the other terminal window to exit out of `bmctl register bootstrap` and re-run the command.

  5. Click **Verify and Create**.

The console displays status messages as it verifies the settings and creates the cluster.

When the admin cluster is created, the bootstrap cluster on the admin workstation is deleted. The output of the `bmctl register bootstrap` command in the other terminal window is similar to the following:
         
         ...
         [2024-04-15 23:10:48+0000] Waiting for cluster to become ready OK
         [2024-04-15 23:16:38+0000] Please run
         [2024-04-15 23:16:38+0000] kubectl --kubeconfig bmctl-workspace/gce-admin-gcloud-001/gce-admin-gcloud-001-kubeconfig get nodes
         [2024-04-15 23:16:38+0000] to get cluster nodes status.
         [2024-04-15 23:16:38+0000] Waiting for node pools to become ready OK
         [2024-04-15 23:16:58+0000] Waiting for metrics to become ready in GCP OK
         [2024-04-15 23:21:58+0000] Waiting for cluster API provider to install in the created admin cluster OK
         [2024-04-15 23:22:08+0000] Moving admin cluster resources to the created admin cluster
         [2024-04-15 23:22:10+0000] Waiting for node update jobs to finish OK
         [2024-04-15 23:24:30+0000] Flushing logs... OK
         [2024-04-15 23:24:30+0000] Unregistering bootstrap cluster.
         [2024-04-15 23:24:30+0000] Deleting membership... OK
         [2024-04-15 23:24:32+0000] Deleting bootstrap cluster.
         




### Verify the admin cluster

You can find your admin cluster kubeconfig file on the admin workstation in the `bmctl-workspace` directory of the root account. To verify your deployment, complete the following steps:

  1. Use SSH to access the admin workstation as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

  2. Verify that your admin cluster was created and is running:
         
         kubectl --kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig get nodes
         

The output is similar to the following:
         
         NAME                   STATUS   ROLES              AGE      VERSION
         abm-admin-cluster-cp   Ready    control-plane      94m      1.31.300-gke.81
         

  3. When you are finished exploring, enter `exit` to disconnect from the admin workstation.




###  gcloud CLI 

The following instructions require two terminal windows. In one terminal window, you run `bmctl register bootstrap` to create a bootstrap cluster. While the `bmctl register bootstrap` command is running, you run `gcloud container bare-metal admin-clusters create` in another terminal window to create the admin cluster.

### Create the bootstrap cluster

When you use a GKE On-Prem API client, such as the gcloud CLI, to create an admin cluster, you need to create a _bootstrap cluster_ on the admin workstation. The bootstrap cluster hosts the Kubernetes controllers needed to create the admin cluster.

  1. From the command line, use SSH to access the admin workstation VM as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

You can ignore any messages about updating the VM and complete this tutorial. If you plan to keep the VMs as a test environment, you might want to update the OS or upgrade to the next release as described in the [Ubuntu documentation](https://ubuntu.com/server/docs/upgrade-introduction).

  2. Set your user credentials as Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

Follow the prompts to select your Google Account for ADC.

  3. Change to the `baremetal/` directory and run the following command to create the bootstrap cluster.

The bootstrap cluster name is derived by prepending `bootstrap-` to the admin cluster name.

**Note:** There's no need to download `bmctl`, because the script you ran earlier took care of that when it set up the admin workstation.
         
         bmctl register bootstrap \
           --ssh-key=/root/.ssh/id_rsa \
           --name=bootstrap-ADMIN_CLUSTER_NAME \
           --project-id=PROJECT_ID
         

After `bmctl` successfully creates the bootstrap cluster, you see output similar to the following:
         
         [2023-03-22 17:35:24+0000] Waiting for the temporary cluster to be registered... OK
         [2023-03-22 17:35:37+0000] Please go to https://console.cloud.google.com/home/dashboard?project=example-project-12345 to create the cluster
         [2023-03-22 17:35:37+0000] Waiting for preflight checks and cluster to run..
         

**Important:** Leave the command running while you complete the steps in a new terminal window. If you exit out of the `bmctl register bootstrap` command before the admin cluster is created, the admin cluster creation fails. After the admin cluster is successfully created, the command automatically deletes the bootstrap cluster and exits.



### Create the admin cluster

  1. In a new terminal window, confirm that the bootstrap cluster has been registered as a member of the fleet:
         
         gcloud container fleet memberships list \
             --project=PROJECT_ID
         

The `gcloud container bare-metal admin-clusters create` command in the following step depends upon the availability of the bootstrap cluster. The `bmctl register bootstrap` command in the other terminal window must run for a few minutes before the bootstrap cluster shows as a registered member. If, after a few minutes, it's still not listed, check the bootstrap cluster name and project ID that you used. If you need to change the bootstrap cluster name or the project ID, enter `Ctrl-C` in the other terminal window to exit out of `bmctl register bootstrap` and re-run the command.

  2. Create the admin cluster with the bundled load balancer:

Ensure that the values you specify match the environment variables that you specified earlier for the script.
         
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
         

In this command:

     * `--control-plane-vip`: Is set to `10.200.0.48`. This is the virtual IP (VIP) on the load balancer for the cluster's Kubernetes API server.

     * `--control-plane-node-configs`: The `node-ip` is set to `10.200.0.3`. This is the IP address of the `abm-admin-cluster-cp` VM in the VXLAN created by the script.

For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/create).

The output from the command is similar to the following:
    
    Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation by running the following command in another terminal window:
    
    gcloud container bare-metal operations describe OPERATION_ID \
        --project=PROJECT_ID \
        --location=ON_PREM_API_REGION
    

When the `gcloud container bare-metal admin-clusters create` command completes successfully, the output is similar to the following:
    
    Created Anthos on bare metal Admin Cluster
    [https://gkeonprem.googleapis.com/v1/projects/anonuser-anonproject/locations/us-central1/bareMetalAdminClusters/gce-admin-gcloud-001].
    NAME           LOCATION     VERSION           MEMBERSHIP     STATE
    abm-cluster-1  us-central1      1.31.300-gke.81 abm-cluster-1  RUNNING
    

When the admin cluster is created, the bootstrap cluster on the admin workstation is deleted. The output of the `bmctl register bootstrap` command in the other terminal window is similar to the following:
    
    ...
    [2024-04-15 23:10:48+0000] Waiting for cluster to become ready OK
    [2024-04-15 23:16:38+0000] Please run
    [2024-04-15 23:16:38+0000] kubectl --kubeconfig bmctl-workspace/gce-admin-gcloud-001/gce-admin-gcloud-001-kubeconfig get nodes
    [2024-04-15 23:16:38+0000] to get cluster nodes status.
    [2024-04-15 23:16:38+0000] Waiting for node pools to become ready OK
    [2024-04-15 23:16:58+0000] Waiting for metrics to become ready in GCP OK
    [2024-04-15 23:21:58+0000] Waiting for cluster API provider to install in the created admin cluster OK
    [2024-04-15 23:22:08+0000] Moving admin cluster resources to the created admin cluster
    [2024-04-15 23:22:10+0000] Waiting for node update jobs to finish OK
    [2024-04-15 23:24:30+0000] Flushing logs... OK
    [2024-04-15 23:24:30+0000] Unregistering bootstrap cluster.
    [2024-04-15 23:24:30+0000] Deleting membership... OK
    [2024-04-15 23:24:32+0000] Deleting bootstrap cluster.
    




### Verify the admin cluster

You can find your admin cluster kubeconfig file on the admin workstation in the `bmctl-workspace` directory of the root account. To verify your deployment, complete the following steps:

  1. Use SSH to access the admin workstation as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

  2. Verify that your admin cluster was created and is running:
         
         kubectl --kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig get nodes
         

The output is similar to the following:
         
         NAME                   STATUS   ROLES              AGE      VERSION
         abm-admin-cluster-cp   Ready    control-plane      94m      1.31.300-gke.81
         

  3. When you are finished exploring, enter `exit` to disconnect from the admin workstation.




###  Terraform 

The following instructions require two terminal windows. In one terminal window, you run `bmctl register bootstrap` to create a bootstrap cluster. While the `bmctl register bootstrap` command is running, you run the Terraform commands in another terminal window to create the admin cluster.

### Modify user cluster sample files to work for an admin cluster

The `anthos-samples` repository doesn't include a sample that is specifically for creating a Google Distributed Cloud admin cluster. The following steps show you how to create an admin cluster by modifying an existing user cluster Terraform sample.

  1. In the directory where you cloned `anthos-samples`, run the following command to copy the sample files for the MetalLB user cluster sample into a new folder for your admin cluster:
         
         cp -r anthos-samples/anthos-onprem-terraform/abm_user_cluster_metallb \
             anthos-samples/anthos-onprem-terraform/abm_admin_cluster_basic
         

  2. Change to the `abm_admin_cluster_basic` directory:
         
         cd anthos-samples/anthos-onprem-terraform/abm_admin_cluster_basic
         

  3. Edit the Terraform files:

     * `variables.tf`:

       * Define a variable for the control plane node IP addresses (though we use just one for this demo). This variable should be similar to the `variable "control_plane_ips" { ... }` entry.

       * Define a variable for the control plane VIP address. This variable should be similar to the `variable "control_plane_vip" { ... }` entry.

     * `terraform.tfvars`:

       * Assign variable values for the following admin cluster settings:

         * Control plane node IP addresses: `10.200.0.3`

         * Control plane VIP address: `10.200.0.48`

     * `main.tf`:

       * Replace the `google_gkeonprem_bare_metal_cluster` resource with the `google_gkeonprem_bare_metal_admin_cluster` resource.

       * Delete the `google_gkeonprem_bare_metal_node_pool` resource and related `lifecycle` section.

       * Update the resource to use the newly defined variables.

Here's an example of how the `main.tf` file might look when it's edited to create an admin cluster:
    
    /**
    * Copyright 2023 Google LLC
    *
    * Licensed under the Apache License, Version 2.0 (the "License");
    * you may not use this file except in compliance with the License.
    * You may obtain a copy of the License at
    *
    *      http://www.apache.org/licenses/LICENSE-2.0
    *
    * Unless required by applicable law or agreed to in writing, software
    * distributed under the License is distributed on an "AS IS" BASIS,
    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    * See the License for the specific language governing permissions and
    * limitations under the License.
    */
    
    #[START anthos_onprem_terraform_bare_metal_admin_cluster_basic_main]
    
    module "enable_google_apis_primary" {
      source     = "terraform-google-modules/project-factory/google//modules/project_services"
      version    = "~> 14.0"
      project_id = var.project_id
      activate_apis = [
        "anthos.googleapis.com",
        "anthosaudit.googleapis.com",
        "anthosgke.googleapis.com",
        "cloudresourcemanager.googleapis.com",
        "compute.googleapis.com",
        "connectgateway.googleapis.com",
        "container.googleapis.com",
        "file.googleapis.com",
        "gkehub.googleapis.com",
        "iam.googleapis.com",
        "kubernetesmetadata.googleapis.com",
        "logging.googleapis.com",
        "monitoring.googleapis.com",
        "opsconfigmonitoring.googleapis.com",
        "serviceusage.googleapis.com",
        "stackdriver.googleapis.com"
      ]
      disable_services_on_destroy = false
    }
    
    # Enable GKE OnPrem API
    resource "google_project_service" "default" {
      project            = var.project_id
      service            = "gkeonprem.googleapis.com"
      disable_on_destroy = false
    }
    
    # Create a baremetal admin cluster and enroll it with the gkeonprem API
    resource "**google_gkeonprem_bare_metal_admin_cluster** " "admin-cluster-basic" {
      name                     = **var.admin_cluster_name**
      description              = "Bare metal admin cluster"
      provider                 = google
      depends_on               = [google_project_service.default]
      location                 = var.region
      bare_metal_version       = var.bare_metal_version
      network_config {
        island_mode_cidr {
          service_address_cidr_blocks = ["10.96.0.0/20"]
          pod_address_cidr_blocks     = ["192.168.0.0/16"]
        }
      }
      node_config {
        max_pods_per_node = 250
      }
      control_plane {
        control_plane_node_pool_config {
          node_pool_config {
            operating_system = "LINUX"
            dynamic "node_configs" {
              for_each = **var.admin_cp_ips**
              content {
                node_ip = node_configs.value
              }
            }
          }
        }
      }
      load_balancer {
        port_config {
          control_plane_load_balancer_port = 443
        }
        vip_config {
          control_plane_vip = **var.admin_cp_vip**
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
    
      dynamic "security_config" {
        for_each = length(var.admin_user_emails) == 0 ? [] : [1]
        content {
          authorization {
            dynamic "admin_users" {
              for_each = var.admin_user_emails
              content {
                username = admin_users.value
              }
            }
          }
        }
      }
    
      lifecycle {
        ignore_changes = [
          annotations["onprem.cluster.gke.io/user-cluster-resource-link"],
          annotations["alpha.baremetal.cluster.gke.io/cluster-metrics-webhook"],
          annotations["baremetal.cluster.gke.io/operation"],
          annotations["baremetal.cluster.gke.io/operation-id"],
          annotations["baremetal.cluster.gke.io/start-time"],
          annotations["baremetal.cluster.gke.io/upgrade-from-version"]
        ]
      }
    }
    
    #[END anthos_onprem_terraform_bare_metal_admin_cluster_basic_main]
    

For more information about the Terraform resource for admin clusters, see [google_gkeonprem_bare_metal_admin_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_admin_cluster) in the Terraform registry.




### Create the bootstrap cluster

When you use a GKE On-Prem API client, such as Terraform, to create an admin cluster, you need to create a _bootstrap cluster_ on the admin workstation. The bootstrap cluster hosts the Kubernetes controllers needed to create the admin cluster.

  1. From the command line, use SSH to access the admin workstation VM as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

You can ignore any messages about updating the VM and complete this tutorial. If you plan to keep the VMs as a test environment, you might want to update the OS or upgrade to the next release as described in the [Ubuntu documentation](https://ubuntu.com/server/docs/upgrade-introduction).

  2. Set your user credentials as Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

Follow the prompts to select your Google Account for ADC.

  3. Change to the `baremetal/` directory and run the following command to create the bootstrap cluster.

The bootstrap cluster name is derived by prepending `bootstrap-` to the admin cluster name.

**Note:** There's no need to download `bmctl`, because the script you ran earlier took care of that when it set up the admin workstation.
         
         bmctl register bootstrap \
           --ssh-key=/root/.ssh/id_rsa \
           --name=bootstrap-ADMIN_CLUSTER_NAME \
           --project-id=PROJECT_ID
         

After `bmctl` successfully creates the bootstrap cluster, you see output similar to the following:
         
         [2023-03-22 17:35:24+0000] Waiting for the temporary cluster to be registered... OK
         [2023-03-22 17:35:37+0000] Please go to https://console.cloud.google.com/home/dashboard?project=example-project-12345 to create the cluster
         [2023-03-22 17:35:37+0000] Waiting for preflight checks and cluster to run..
         

**Important:** Leave the command running while you complete the steps in a new terminal window. If you exit out of the `bmctl register bootstrap` command before the admin cluster is created, the admin cluster creation fails. After the admin cluster is successfully created, the command automatically deletes the bootstrap cluster and exits.



### Create the admin cluster

  1. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider. 

  2. Review the configuration and make changes if needed:
         
         terraform plan
         

  3. Apply the Terraform plan to create the admin cluster:
         
         terraform apply
         

It takes 15 minutes or more to create the admin cluster. When the cluster creation completes, you see a message like the following:
         
         ...
         google_gkeonprem_bare_metal_admin_cluster.admin-cluster-basic: Still creating... [20m10s elapsed]
         google_gkeonprem_bare_metal_admin_cluster.admin-cluster-basic: Creation complete after 20m11s
         [id=projects/anonuser-anonproject/locations/us-central1/bareMetalAdminClusters/gce-admin-terra002]
         
         Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
         

When the admin cluster is created, the bootstrap cluster on the admin workstation is deleted. The output of the `bmctl register bootstrap` command in the other terminal window is similar to the following:
         
         ...
         [2024-04-15 23:10:48+0000] Waiting for cluster to become ready OK
         [2024-04-15 23:16:38+0000] Please run
         [2024-04-15 23:16:38+0000] kubectl --kubeconfig bmctl-workspace/gce-admin-gcloud-001/gce-admin-gcloud-001-kubeconfig get nodes
         [2024-04-15 23:16:38+0000] to get cluster nodes status.
         [2024-04-15 23:16:38+0000] Waiting for node pools to become ready OK
         [2024-04-15 23:16:58+0000] Waiting for metrics to become ready in GCP OK
         [2024-04-15 23:21:58+0000] Waiting for cluster API provider to install in the created admin cluster OK
         [2024-04-15 23:22:08+0000] Moving admin cluster resources to the created admin cluster
         [2024-04-15 23:22:10+0000] Waiting for node update jobs to finish OK
         [2024-04-15 23:24:30+0000] Flushing logs... OK
         [2024-04-15 23:24:30+0000] Unregistering bootstrap cluster.
         [2024-04-15 23:24:30+0000] Deleting membership... OK
         [2024-04-15 23:24:32+0000] Deleting bootstrap cluster.
         

  4. In the console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

Make sure that the project in which you created the user cluster is selected. You should see the admin cluster listed.

  5. Sign in to the admin cluster:

     1. Click the link on the cluster name, and on the side panel, click **Login**.

     2. Select **Use your Google identity to log in**.

     3. Click **Login**.




### Verify the admin cluster

You can find your admin cluster kubeconfig file on the admin workstation in the `bmctl-workspace` directory of the root account. To verify your deployment, complete the following steps:

  1. Use SSH to access the admin workstation as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

  2. Verify that your admin cluster was created and is running:
         
         kubectl --kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig get nodes
         

The output is similar to the following:
         
         NAME                   STATUS   ROLES              AGE      VERSION
         abm-admin-cluster-cp   Ready    control-plane      94m      1.31.300-gke.81
         

  3. When you are finished exploring, enter `exit` to disconnect from the admin workstation.




## 4\. Create the user cluster

You can use the Google Cloud console, the Google Cloud CLI, or Terraform to create the user cluster. For simplicity, use `abm-user-cluster-metallb` for the user cluster name, to match the hard-coded name in the Terraform scripts.

###  `bmctl`

  1. Use SSH to access the admin workstation VM, `abm-ws`, as root:
         
         gcloud compute ssh root@abm-ws --zone ZONE
         

  2. Generate a cluster configuration file:
         
         bmctl create config -c abm-user-cluster-metallb \
             --project-id=PROJECT_ID

  3. In the following user cluster configuration file, set your email address in the `clusterSecurity` section and verify the rest of the settings:

The following cluster configuration file is filled in with the values that you entered in the planning table earlier. In addition to the values you entered, note the following differences from the generated configuration file:

     * Comments have been removed from this sample to improve readability.
     * The credentials section has been removed as is normal for user clusters.
     * The cluster type, `spec.type`, has been set to `user`.
     * The `spec.clusterSecurity.authorization.clusterAdmin.gcpAccounts` field was added to grant the `clusterrole/cluster-admin` role to your account. Among other things, this field lets you sign in to your cluster in the Google Cloud console to see more cluster details.
    
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-abm-user-cluster-metallb
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: abm-user-cluster-metallb
      namespace: cluster-abm-user-cluster-metallb
    spec:**  type: user**
      profile: default
      anthosBareMetalVersion: BMCTL_VERSION
      gkeConnect:
        projectID: PROJECT_ID
      controlPlane:
        nodePoolSpec:
          nodes:
          - address: 10.200.0.4
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
          controlPlaneVIP: 10.200.0.50
          ingressVIP: 10.200.0.51
        addressPools:
        - name: pool1
          addresses:
          - 10.200.0.51-10.200.0.70
      clusterOperations:
        projectID: PROJECT_ID
        location: ON_PREM_API_REGION**  clusterSecurity:
        authorization:
          clusterAdmin:
            gcpAccounts:
            - YOUR_EMAIL_ADDRESS**
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
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: node-pool-1
      namespace: cluster-abm-user-cluster-metallb
    spec:
      clusterName: abm-user-cluster-metallb
      nodes:
      - address: 10.200.0.5
    

  4. Replace the contents of the generated configuration file on your admin workstation with the contents from the preceding sample.

Open the generated file, `bmctl-workspace/abm-user-cluster-metallb/abm-user-cluster-metallb.yaml`, and replace its contents with the contents of the sample you verified in the preceding step.

  5. Create the user cluster:
         
         bmctl create cluster -c abm-user-cluster-metallb \
           --kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig

The `bmctl` command displays output to the screen as it runs preflight checks and creates the cluster. Verbose information is written to logs in the `baremetal/bmctl-workspace/abm-user-cluster-metallb/log` folder on the admin workstation.

Cluster creation can take several minutes to finish.

  6. In the Google Cloud console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

Make sure that the project in which you created the user cluster is selected. You should see both the admin and user cluster on the list.

  7. Sign in to the user cluster:

     1. Click the link on the cluster name, and on the side panel, click **Login**.

     2. Select **Use your Google identity to log in**.

     3. Click **Login**.

Repeat the same steps to sign in to the admin cluster.




###  Console 

Complete the following steps to create a user cluster in the console:

  1. In the console, go to the **Create a bare metal cluster** page.

[Go to Create a bare metal cluster](https://console.cloud.google.com/kubernetes/baremetal/add)

  2. Make sure that the Google Cloud project in which you created the admin cluster is selected.

  3. Click **Create Cluster**.

  4. In the dialog, click **On-premises**.

  5. Next to **Bare metal** , click **Configure**. The **Prerequisites** page displays.

  6. Under **Choose your cluster type** , select **Create a user cluster for an existing admin cluster**

  7. Click **Next**.




### Cluster basics

  1. Enter a name for the user cluster or use the default.

  2. Make sure that the newly created admin cluster is selected. You can use the defaults for the rest of the settings on this page.

  3. Click **Networking** in the left-navigation bar.




### Networking

The script that you ran to create VMs and the admin cluster also created a Layer 2 VXLAN with IP addresses in the `10.200.0.0/24` subnet.

  1. In the **Control plane** section, enter the following in the **Control plane node IP 1** field:
         
         10.200.0.4
         

This is the IP address of the `abm-user-cluster-cp1` VM in the VXLAN created by the script.

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

Your user cluster must have at least one node pool for worker nodes.

  1. Enter the following IP address in the **Nodes address 1** field:
         
         10.200.0.5
         

This is the IP address of the abm-user-cluster-w1 VM in the VXLAN created by the script.




### Create the cluster

  1. Click **Verify and Create** to create the user cluster.

It takes 15 minutes or more to create the user cluster. The console displays status messages as it verifies the settings and creates the cluster.

If there is a problem with the configuration, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.

To see additional information about the creation process, click **Show details** to display a side panel. Click close to close the details panel.

When the cluster is created, **Cluster status: running** is displayed.

  2. After the cluster is created, click arrow_back **Clusters** to go back to the **Clusters** page.

  3. Sign in to the user cluster:

     1. Click the link on the cluster name, and on the side panel, click **Login**.

     2. Select **Use your Google identity to log in**.

     3. Click **Login**.

Repeat the same steps to sign in to the admin cluster.




###  gcloud CLI 

To create the user cluster:

  1. Run the following command to create the user cluster:
         
         gcloud container bare-metal clusters create abm-user-cluster-metallb \
             --project=PROJECT_ID \
             --admin-cluster-membership=projects/PROJECT_ID/locations/ON_PREM_API_REGION/memberships/ADMIN_CLUSTER_NAME \
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
         

After running the command, you see output like the following:
         
         Waiting for operation [projects/PROJECT_ID/locations/ON_PREM_API_REGION/operations/operation-1678304606537-5f668bde5c57e-341effde-b612ff8a] to complete...
         

In the example output, the string `operation-1678304606537-5f668bde5c57e-341effde-b612ff8a` is the `OPERATION_ID` of the long-running operation.

  2. To find out the status of the operation, open another terminal window and run the command.
         
         gcloud container bare-metal operations describe OPERATION_ID \
             --project=PROJECT_ID \
             --location=ON_PREM_API_REGION
         

Replace `OPERATION_ID` with the corresponding string from the output of the preceding step.

It takes about 15 minutes or more to create the cluster. As the cluster is being created, you can run the previous command every so often to get the current status.

When the cluster is created, you see output like the following:
         
         Created Anthos cluster on bare metal [https://gkeonprem.googleapis.com/v1/projects/PROJECT_ID/locations/ON_PREM_API_REGION/bareMetalClusters/abm-user-cluster-metallb].

For more information about the `gcloud container bare-metal clusters create` command, including descriptions of each flag, see the [container bare-metal clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal/clusters/create) page for the clusters resource in the gcloud CLI reference.




### Create a node pool

After the cluster is successfully created, you can create a node pool for the cluster.

To create a node pool:

  1. Run the following command to create a node pool:
         
         gcloud container bare-metal node-pools create NODE_POOL_NAME \
             --cluster=abm-user-cluster-metallb \
             --project=PROJECT_ID \
             --location=ON_PREM_API_REGION \
             --node-configs='node-ip=10.200.0.5'
         

Replace `NODE_POOL_NAME` with a name for the node pool.

After running the command, you should see output like the following:
         
         Waiting for operation [projects/PROJECT_ID/locations/ON_PREM_API_REGION/operations/operation-1678308682052-5f669b0d132cb-6ebd1c2c-816287a7] to complete...
         

It takes about 5 minutes or less to create the node pool. When the node pool is created, you see output like the following:
         
         Created node pool in Anthos cluster on bare metal [https://gkeonprem.googleapis.com/v1/projects/PROJECT_ID/locations/ON_PREM_API_REGION/bareMetalClusters/abm-user-cluster-metallb/bareMetalNodePools/NODE_POOL_NAME].
         

  2. Go to the **Kubernetes clusters** page in the console:

[Go to the Create a bare metal cluster page](https://console.cloud.google.com/kubernetes/list/overview)

Make sure that the project in which you created the user cluster is selected. You should see both the admin and user cluster on the list.

  3. Sign in to the user cluster:

     1. Click the link on the cluster name, and on the side panel, click **Login**.

     2. Select **Use your Google identity to log in**.

     3. Click **Login**.

Repeat the same steps to sign in to the admin cluster.




### Terraform

You can use the following basic configuration sample to create a user cluster with a bundled MetalLB load balancer. For more information, see the [`google_gkeonprem_bare_metal_cluster` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster).

  1. In the directory where you cloned `anthos-samples`, change to the directory where the Terraform sample is located:
         
         cd anthos-samples/anthos-onprem-terraform/abm_user_cluster_metallb
         

The sample provides an example variables file to pass in to `main.tf`.

  2. Make a copy of the `terraform.tfvars.sample` file:
         
         cp terraform.tfvars.sample terraform.tfvars
         

  3. Verify the values in the following sample.

The following Terraform variables file, `terraform.tfvars.sample`, is prefilled with IP addresses and with values that you entered in preceding sections of this guide.
         
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
         

Replace `ADMIN_2_EMAIL_ADDRESS` with an email address that is associated with your Google Cloud account, or remove it when you edit the variables file.

For more information about the arguments in this sample for which you're setting variables, see [Argument Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster#argument-reference) in the Terraform documentation for bare metal user clusters.

  4. Replace the contents of your copy of the variables file with the contents from the preceding sample.

  5. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider. 

  6. Review the configuration and make changes if needed:
         
         terraform plan
         

  7. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         

It takes 15 minutes or more to create the user cluster. You can view the cluster in the Google Cloud console on the [**GKE clusters**](https://console.cloud.google.com/kubernetes/list/overview) page.

  8. In the Google Cloud console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

Make sure that the project in which you created the user cluster is selected. You should see both the admin and user cluster on the list.

  9. Sign in to the user cluster:

     1. Click the link on the cluster name, and on the side panel, click **Login**.

     2. Select **Use your Google identity to log in**.

     3. Click **Login**.

Repeat the same steps to sign in to the admin cluster.




## 5\. Clean up

Use the following instructions to remove the clusters and VMs you created with this guide.

### Delete the user cluster

### `bmctl`

  * To delete the user cluster with `bmctl`, run the following command from the admin workstation VM, `abm-ws`:
        
        bmctl reset \
            --cluster abm-user-cluster-metallb \
            --admin-kubeconfig bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig
        




### Console

  1. In the console, go to the **GKE clusters** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the list of clusters, click the user cluster.

  3. In the **Details** panel, click **View more details**.

  4. Near the top of the window, click delete  **Delete**.

  5. When prompted to confirm, enter the cluster name and click **Delete**.

  6. Click notifications in the top-right corner to view the status of the deletion. You might have to refresh the page to update the clusters list.




###  gcloud CLI 

  * Delete the cluster:
        
        gcloud container bare-metal clusters delete abm-user-cluster-metallb \
            --project=PROJECT_ID \
            --location=ON_PREM_API_REGION \
            --force
        

The `--force` flag lets you delete a cluster that has node pools. Without the `--force` flag, you have to [delete the node pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/delete) first, and then delete the cluster.




For information about other flags, see [gcloud container bare-metal clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/delete).

### Terraform

The `terraform destroy` command terminates resources that were create when you ran `terraform apply` to create the user cluster.

  * Run the following command from the directory where the Terraform user cluster sample files, such as `main.tf` are located:
        
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

  4. Exit the admin workstation:
         
         exit
         

  5. List all VMs that have `abm` in their name:
         
         gcloud compute instances list | grep 'abm'
         

  6. Verify that you're fine with deleting all VMs that contain `abm` in the name.

After you've verified, you can delete `abm` VMs by running the following command:
         
         gcloud compute instances list --format="value(name)" | \
             grep 'abm' | \
             xargs gcloud compute instances delete --quiet --zone ZONE
         

  7. Run the following command to delete the service account and, when prompted, enter `y`:
         
         gcloud iam service-accounts delete baremetal-gcr@PROJECT_ID.iam.gserviceaccount.com
         

## What's next



  * To get started creating clusters on your own hardware, see [Plan for a basic installation on your hardware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/minimal-infrastructure) and [Create basic clusters on your hardware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/quickstart).

  * For detailed installation requirements, see [Installation prerequisites overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prereq).

  * For more information about installation, see [Cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

  * For instructions on deploying to your cluster, see [Deploy an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/deploy-app).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
