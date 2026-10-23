---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-admin-cluster-api/
title: Create an admin cluster using GKE On-Prem API clients \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:21.212812+00:00
---

# Create an admin cluster using GKE On-Prem API clients  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-admin-cluster-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create an admin cluster using GKE On-Prem API clients Stay organized with collections  Save and categorize content based on your preferences. 

Standard Google Cloud clients let you create an admin cluster to manage the lifecycle of your user clusters. Both the Google Cloud console and the Google Cloud CLI (gcloud CLI) call the GKE On-Prem API to provision the cluster.

## What is the GKE On-Prem API?

The GKE On-Prem API is a Google Cloud-hosted API that lets you manage the lifecycle of your on-premises clusters using Terraform and standard Google Cloud applications. The GKE On-Prem API runs in Google Cloud's infrastructure. Terraform, the console, and the gcloud CLI are clients of the API, and they use the API to create clusters in your data center.

To manage the lifecycle of your clusters, the GKE On-Prem API must store metadata about your cluster's state in Google Cloud, using the Google Cloud region that you specify when creating the cluster. This metadata lets the API manage the cluster lifecycle and doesn't include workload-specific data.

When you create a cluster using an GKE On-Prem API client, you specify a Google Cloud project. After the cluster is created, it is automatically registered to the specified project's [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs). This project is referred to as the [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project). The fleet host project can't be changed after the cluster is created.

If you prefer, you can create an admin cluster by creating an admin cluster configuration file and using `bmctl`, as described in [Creating an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/admin-cluster-creation).

If you want to use the console or gcloud CLI to manage the lifecycle of clusters that were created using `bmctl`, see [Configure clusters to be managed by the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster).

## IAM permissions

If you aren't a Google Cloud project owner, you must have a project owner grant you the following roles:

  * [roles/compute.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer)

  * [roles/gkeonprem.admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem)

  * [roles/gkehub.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub)

  * [roles/iam.securityAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin)

  * [roles/iam.serviceAccountAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin)

  * [roles/iam.serviceAccountKeyAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin)

  * [roles/serviceusage.serviceUsageAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)




If you want to access the Google Kubernetes Engine pages in the console, you must also have [roles/container.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/container).

For information on granting the roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Command line access

After the cluster is created, if you want to use the [connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway) to run `kubectl` commands against the cluster on computers other than the admin workstation, install the following command-line tools on the computer that you plan to use.

  * The latest version of the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  * `kubectl` for running commands against Kubernetes clusters. If you need to install `kubectl`, follow these [instructions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl).


**Note:** If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

## Choose the client to create the admin cluster

You can use either the console or the gcloud CLI to create an admin cluster that is managed by the GKE On-Prem API. If this is your first time installing Distributed Cloud software only for bare metal, you might find the console easier to use than the gcloud CLI.

After you are more familiar with the information that you need to provide for creating clusters, you might find the gcloud CLI more convenient because you can save the command with its arguments to a text file. If you are using a CI/CD tool, such as [Cloud Build](https://docs.cloud.google.com/build/docs/overview), you can use the `gcloud` commands to create a cluster and specify the `--impersonate-service-account` flag to automate the creation.

## Prerequisites

### Console

  1. In the console, go to the **Create a bare metal cluster** page.

[Go to Create a bare metal cluster](https://console.cloud.google.com/kubernetes/baremetal/add)

  2. Select the Google Cloud project that you want to create the cluster in. The selected project is also used as the fleet host project.




The **Prerequisites** page displays the requirements for your admin workstation and cluster node machines. The IP address planner in the **Network requirements** section helps you plan the IP addresses needed for a minimal installation of one admin cluster and one user cluster.

**Admin workstation prerequisites**

Expand this section to display the hardware, operating system, and connectivity requirements for your admin workstation.

**Cluster node machine prerequisites**

Expand this section to display the hardware, operating system, and connectivity requirements for the cluster node machines.

**Network requirements**

This section helps you plan the IP addresses that you need for a minimal environment. Optionally, in the **Node IP and Virtual IP addresses** section, you can provide a starting node IP address and a virtual IP address (VIP), and the console displays a table of IP addresses that you need. These IP addresses aren't applied to the admin cluster configuration. They are meant as a guide to help you plan the IP addresses that you need for your installation. You can download the table to a CSV file and import it into a spreadsheet or IP address planning tool to use as a starting point to track the IP addresses needed for your clusters.

**Review Google Cloud resources** :

Make sure that all the [required Google APIs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#enable_apis) are enabled in the fleet host project. In addition, you need to enable the GKE On-Prem API:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
      gkeonprem.googleapis.com
    

Replace `FLEET_HOST_PROJECT_ID` with the project ID of the fleet host project.

Before creating the cluster, you run the `bmctl register bootstrap` command on your admin workstation as described in Prepare bootstrap environment. This command can create the required service accounts with the minimum required IAM permissions needed to create the admin cluster. If you prefer, you can [Configure service accounts manually](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#configuring-sa).

When you are ready to begin, click **Install bootstrap environment** in the left navigation bar.

###  gcloud CLI 

**Hardware, networking, and operating system prerequisites**

Creating an admin cluster using a GKE On-Prem API client requires the same hardware, networking, and operating system prerequisites as creating the cluster using `bmctl`. For details, see [Installation prerequisites](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prereq).

**Required Google APIs**

Make sure that all the [required Google APIs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#enable_apis) are enabled in the fleet host project. In addition, you need to enable the GKE On-Prem API:
    
    
    gcloud services enable --project FLEET_HOST_PROJECT_ID \
      gkeonprem.googleapis.com
    

Replace `FLEET_HOST_PROJECT_ID` with the project ID of the fleet host project.

**Required service accounts and permissions**

Before creating the cluster, you run the `bmctl register bootstrap` command on your admin workstation as described in Prepare bootstrap environment. This command can create the required service accounts with the minimum required IAM permissions needed to create the admin cluster. If you prefer, you can [Configure service accounts manually](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#configuring-sa).

**Plan IP addresses**

Before creating the admin cluster, you need to plan the IP addresses for your clusters. Review [Plan your IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/plan-ip-addresses) for an example of how to allocate IP addresses for a high-availability (HA) admin cluster and two HA user clusters. Even if you will be using the gcloud CLI to create the admin cluster, you might want to follow the console steps in this section to use the IP address planner.

## Prepare bootstrap environment

Before you create the admin cluster, you need to run the `bmctl register bootstrap` command on your admin workstation. This command deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (kind) cluster on the admin workstation. This _bootstrap_ cluster hosts the Kubernetes controllers needed to create the admin cluster. When you create the admin cluster, the controllers on the bootstrap cluster will provision nodes, run preflight checks, and register the admin cluster to the fleet. The bootstrap cluster is automatically deleted after the cluster is successfully created.

### Console

  1. Enter a **Name** for the admin cluster. Notice that the bootstrap cluster name is derived by prepending _bootstrap-_ to the admin cluster name.

  2. Select the version for your admin cluster.

  3. In the **Google Cloud API Location** field, select the Google Cloud region from the list. This setting specifies the region where the following APIs and services run:

     * GKE On-Prem API (`gkeonprem.googleapis.com`)
     * Fleet service (`gkehub.googleapis.com`)
     * Connect service (`gkeconnect.googleapis.com`)

This setting also controls the region in which the following are stored:

     * The cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

  4. The console displays the commands that you need to run on your admin workstation. The `bmctl` command-line tool must match the version of the cluster that you're creating. If you already have the applicable version of `bmctl` downloaded to your admin workstation, you don't need to download it again.




###  gcloud CLI 

  1. Make sure to update components:
         
         gcloud components update
         

  2. Run the following command to sign in with your Google Account:
         
         gcloud auth login
         

  3. List the available bare metal cluster versions that you can install:

The `bmctl` version that you download to create the bootstrap environment must match the version that you will install on the admin cluster.
         
         gcloud container bare-metal admin-clusters query-version-config \
           --location=REGION
         

Replace `REGION` with the Google Cloud region that you will use when you create the cluster. This is the region in which the GKE On-Prem API and the Fleet and Connect services run. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api).




## Create the bootstrap cluster

Do the following steps on your admin workstation. These commands are displayed in the console.

  1. Set your user credentials as Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

Follow the prompts to select your Google Account for ADC.

  2. If needed, download the `bmctl` command-line tool to the current working directory.
         
         gcloud storage cp gs://anthos-baremetal-release/bmctl/VERSION/linux-amd64/bmctl .
         chmod a+x ./bmctl
         

Replace `VERSION` with the bare metal cluster version you want to install. If you copied the command from the console, the version is already in the command.

  3. Create the bootstrap cluster. You can either let `bmctl` create the required service accounts (SAs), or you can [create the service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#configuring-sa) and key files yourself and pass them to the `bmctl register bootstrap` command.




### `bmctl` creates SAs

Use the following command if you want `bmctl` to create the required service accounts with the minimum required permissions needed to create the admin cluster. This command assumes that `bmctl` is in the current working directory.
    
    
    ./bmctl register bootstrap \
      --ssh-key=YOUR_PRIVATE_KEY \
      --target-cluster-name=ADMIN_CLUSTER_NAME \
      --project-id=FLEET_HOST_PROJECT_ID
    

Replace the following:

  * `YOUR_PRIVATE_KEY`: The path to your private SSH key. You created the SSH key when you [set up root SSH access to nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/workstation-prerequisites#set_up_root_ssh_access_to_nodes).



If you copied the command displayed in the console, the following fields are already filled in for you.

  * `ADMIN_CLUSTER_NAME`: The name of your admin cluster.

  * `FLEET_HOST_PROJECT_ID`: The project that the admin cluster will be automatically registered to after the cluster is created.




The `bmctl register bootstrap` command creates the following service accounts. The service account keys are stored in the directory `bmctl-workspace/.sa-keys`.

Service account | Purpose | IAM roles  
---|---|---  
anthos-baremetal-gcr | Google Distributed Cloud uses this service account to download container images from Artifact Registry. | None  
anthos-baremetal-connect |  Connect Agent uses this service account to maintain a connection between your cluster and Google Cloud.  | roles/gkehub.connect  
anthos-baremetal-register |  Connect Agent uses this service account to register your clusters to the Google Cloud fleet.  | roles/gkehub.admin  
anthos-baremetal-cloud-ops |  Stackdriver Agent uses this service account to export logs and metrics from clusters to Cloud Logging and Cloud Monitoring.  |  roles/logging.logWriter  
roles/monitoring.metricWriter  
roles/stackdriver.resourceMetadata.writer  
roles/opsconfigmonitoring.resourceMetadata.writer  
roles/monitoring.dashboardEditor  
roles/monitoring.viewer  
roles/serviceusage.serviceUsageViewer  
roles/kubernetesmetadata.publisher   
  
### Specify SA key files

If you prefer, you can pass `bmctl` the service account key files that you created. The following command uses the key file names in [Configure service accounts manually](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#configuring-sa) and assumes that `bmctl` and the key files are in the current working directory.

**Note:** The `--target-cluster-name` flag is supported for Google Distributed Cloud version 1.16.0 and higher. This flag replaces the `--name` flag, which required you to specify the bootstrap cluster name derived from the admin cluster name.
    
    
    ./bmctl register bootstrap \
      --ssh-key=YOUR_PRIVATE_KEY \
      --target-cluster-name=ADMIN_CLUSTER_NAME \
      --project-id=FLEET_HOST_PROJECT_ID \
      --gcr-service-account-key=anthos-baremetal-gcr.json \
      --gke-agent-service-account-key=connect-agent.json \
      --gke-register-service-account-key=connect-register.json \
      --cloud-operation-service-account-key=anthos-baremetal-cloud-ops.json
    

Replace the following:

  * `YOUR_PRIVATE_KEY`: The path to your private SSH key. You created the SSH key when you [set up root SSH access to nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/workstation-prerequisites#set_up_root_ssh_access_to_nodes).

  * `ADMIN_CLUSTER_NAME`: The name of your admin cluster.

  * `FLEET_HOST_PROJECT_ID`: The project that the admin cluster will be automatically registered to after the cluster is created.




The following flags specify the path to the key files:

  * `-gcr-service-account-key`: The path to the key file for the service account that pulls container images (`anthos-baremetal-gcr`).

  * `--gke-agent-service-account-key`: The path to the key file for the Connect Agent service account (`anthos-baremetal-connect`).

  * `--gke-register-service-account-key`: The path to the key file for the Connect Agent service account that registers the cluster to the fleet (`anthos-baremetal-register`).

  * `--cloud-operation-service-account-key`: The path to the key file for the service account to audit logs and monitor projects (`anthos-baremetal-cloud-ops`).




After `bmctl` successfully creates the bootstrap cluster, you see output similar to the following:
    
    
    [2023-03-22 17:35:24+0000] Waiting for the temporary cluster to be registered... OK
    [2023-03-22 17:35:37+0000] Please go to https://console.cloud.google.com/home/dashboard?project=example-project-12345 to create the cluster
    [2023-03-22 17:35:37+0000] Waiting for preflight checks and cluster to run..
    

**Caution:** Leave the command running while you create the admin cluster. If you exit out of the `bmctl register bootstrap` command before the admin cluster is created, the admin cluster creation fails. After the cluster is successfully created, the command automatically deletes the bootstrap cluster and exits.

## Create the admin cluster

### Console

  1. On the **Install bootstrap environment** page, click **Check Connection**.

On success, the console displays check_circle **Connection established**.

The connection to the bootstrap cluster must be established before you continue. If the connection isn't established, check the arguments that you specified to the `bmctl register bootstrap` command:

     * Make sure that the value for `--target-cluster-name` matches the **Admin cluster name** displayed in the **Bootstrap environment basics** section.

     * Make sure the value for `--project-id` matches the ID of the project that you selected in the console.

If you need to change the bootstrap cluster name or the project ID, enter `Ctrl-C` to exit out of `bmctl register bootstrap` and re-run the command.

  2. Click **Next** to begin configuring the admin cluster. Most of the settings in the console correspond to the fields in the [cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref).

  3. Under **Node configuration** , enter a value between 64 and 250 in **Maximum Pods per node** , or accept the default, 110. After the cluster is created, you can't update this value.

The maximum Pods per node (referred to as Pod density} is also limited by your cluster's available IP resources. For details, see [Pod networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#pod_networking).

  4. Click **Next**.

  5. On the **Networking** page, define how your nodes and components in the cluster communicate with each other and with the Kubernetes control plane.

For detailed information, hold the pointer over the question_mark next to each field.

  6. Click **Verify and Create**.

The console displays status messages as it verifies the settings and creates the cluster in your data center.

If there is a problem with the configuration, the console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.




###  gcloud CLI 

Before creating the admin cluster, confirm that the bootstrap cluster has been registered as a member of the fleet:
    
    
    gcloud container fleet memberships list \
      --project=FLEET_HOST_PROJECT_ID
    

If the bootstrap cluster isn't listed, check the bootstrap cluster name and project ID that you specified to `bmctl register bootstrap`. If you need to change the bootstrap cluster name or the project ID, enter `Ctrl-C` to exit out of `bmctl register bootstrap` and re-run the command.

Use the following command to create an admin cluster:
    
    
    gcloud container bare-metal admin-clusters create
    

Most of the flags that you specify to the command correspond to the fields in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref).

To create an admin cluster with the bundled load balancer:
    
    
    gcloud container bare-metal admin-clusters create ADMIN_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --location=REGION \
      --version=VERSION \
      --max-pods-per-node=MAX_PODS_PER_NODE \
      --control-plane-vip=CONTROL_PLANE_VIP \
      --control-plane-load-balancer-port=CONTROL_PLANE_LOAD_BALANCER_PORT \
      --control-plane-node-configs 'CONTROL_PLANE_NODE_CONFIG' \
      --island-mode-service-address-cidr-blocks=SERVICE_ADDR_CIDR \
      --island-mode-pod-address-cidr-blocks=POD_ADDR_CIDR \
      --lvp-share-path=/mnt/localpv-share \
      --lvp-share-storage-class=local-shared \
      --lvp-node-mounts-config-path=/mnt/localpv-disk \
      --lvp-node-mounts-config-storage-class=local-disks
    

If you want to use manual load balancing, add `--enable-manual-lb` to the command.

Replace the following:

  * `ADMIN_CLUSTER_NAME`: The name of your admin cluster. The name can't be changed after the cluster is created.

  * `FLEET_HOST_PROJECT_ID`: The project that the admin cluster will be automatically registered to after the cluster is created. The fleet host project can't be changed after the cluster is created.

  * `REGION`: The Google Cloud region in which the GKE On-Prem API runs. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/supported-regions-on-prem-api). The region can't be changed after the cluster is created. This setting specifies the region where the following are stored:

    * The cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
    * The Cloud Logging and Cloud Monitoring data of system components
    * The Admin Audit log created by Cloud Audit Logs

The cluster name, project, and location together uniquely identify the cluster in Google Cloud.

  * `VERSION`: The bare metal cluster version. The version must match the `bmctl` version that you used to run `bmctl register bootstrap`. You can check the `bmctl` version by running `bmctl version` on the admin workstation.

  * `MAX_PODS_PER_NODE `: For admin clusters, allowable values are 32-250 and 64-250 for non-HA clusters. The default value if `--max-pods-per-node` isn't included in the command is 110. After the cluster is created, this value cannot be updated.

The maximum Pods per node (referred to as Pod density) is also limited by your cluster's available IP resources. For details, see [Pod networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/network-reqs#pod_networking).

  * `CONTROL_PLANE_VIP`: The virtual IP (VIP) on the load balancer for the cluster's Kubernetes API server. Include the control plane VIP in the same subnet as the load balancer nodes. Don't include the control plane VIP in the load balancer address pools.

  * `CONTROL_PLANE_LOAD_BALANCER_PORT`: The port the load balancer serves the control plane on. Although you can configure another value, port `443` is the standard port used for HTTPS connections.

  * `CONTROL_PLANE_NODE_CONFIG`: The IPv4 address of a control plane node. Control plane nodes run the system workload. Specify this flag for each control plane node. Typically, you have a single machine if using a minimum deployment, or three machines if using a high availability (HA) deployment. Specify an odd number of nodes to have a majority quorum for HA. You can change these addresses whenever you update or upgrade the cluster.

The value for the flag has the following format:
        
        'node-ip=CP_IP_ADDRESS_1,labels=CP_KEY_1.1=CP_VALUE_1.1;CP_KEY_1.2=CP_VALUE_1.2;...' \
        

The value has segments that start with the keywords `node-ip` and `labels`. Separate each segment with a comma.

    * `node-ip`: The IP address of a control plane node. You can specify only one `node-ip` per flag. If you need to specify more than one node, include the flag again for each node.

    * `labels`: One or more key=value pairs attached to the node.

Note the following syntax rules:

    * Surround the entire value in single quotes.
    * Whitespace isn't allowed.
    * Separate each key=value pair in the `labels` segment with a semicolon.

For example:
    
    --control-plane-node-configs 'node-ip=192.0.2.1' \
    --control-plane-node-configs 'node-ip=192.0.2.2,labels=key2.1=value2.1' \
    --control-plane-node-configs 'node-ip=192.0.2.3,labels=key3.1=value3.1;key3.2=value3.2' \
    

  * `SERVICE_ADDR_CIDR`: A range of IPv4 addresses, in CIDR format, for Services in your cluster. The CIDR range must be between /24 and /12, where /12 provides the most IP addresses. We recommend that you use a range in the IP address space for private internets, defined in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918), for example, `10.96.0.0/20`.

  * `POD_ADDR_CIDR`: A range of IPv4 addresses, in CIDR format, to be used for Pods in the user cluster. The CIDR range must be between /18 and /8, where /8 provides the most IP addresses. We recommend that you use a range in the IP address space for private internets, defined in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918), for example, `192.168.0.0/16`.




You must specify the following storage flags. The example command includes typical values. For more information, see [Configure local storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-local-storage).

  * `--lvp-share-path`: This is the host machine path where subdirectories can be created. A local PersistentVolume (PV) is created for each subdirectory.

  * `--lvp-share-storage-class`: This is the StorageClass to use to create persistent volumes. The StorageClass is created during cluster creation.

  * `--lvp-node-mounts-config-path`: This is the host machine path where mounted disks can be discovered. A local PersistentVolume (PV) is created for each mount.

  * `--lvp-node-mounts-config-storage`: The storage class that PVs are created with during cluster creation.




For a complete list of the flags and their descriptions, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/create).

The output from the command is similar to the following:
    
    
    Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
    

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation. You can find out the status of the operation with the following command:
    
    
    gcloud container bare-metal operations describe OPERATION_ID \
      --project=FLEET_HOST_PROJECT_ID \
      --location=REGION
    

For more information, see [gcloud container bare-metal operations](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/operations).

**Fix preflight errors**

Before creating the cluster, `bmctl` runs a series of preflight checks to verify the configuration. If there is a problem with the configuration, the `gcloud ... create` command exits with an error similar to:
    
    
    ERROR: (gcloud.container.bare-metal.admin-clusters.create) Invalid resource state for "projects/694677185633/locations/us-west1/bareMetalAdminClusters/abm-cluster-1": cluster preflight checks failed
    

For example, assume that a preflight check failed because the control plane node couldn't be reached. On the admin workstation, you will see something similar to the following:
    
    
    [2023-03-27 20:34:38+0000] Waiting for preflight check job to finish... OK
    [2023-03-27 20:35:58+0000] - Validation Category: machines and network
    [2023-03-27 20:35:58+0000]    - [PASSED] pod-cidr
    [2023-03-27 20:35:58+0000]    - [FAILED] node-network (log: bmctl-workspace/log/register-bootstrap-20230327-201548/node-network)
    [2023-03-27 20:35:58+0000]        - Failed to connect to the host via ssh: ssh: connect to host 10.100.0.5 port 22: Connection timed out
    [2023-03-27 20:35:58+0000] Flushing logs... OK
    [2023-03-27 20:35:58+0000] Error polling the preflight check abm-cluster-mar-27 in the cluster-abm-cluster-mar-27: preflight check failed
    

  1. On the admin workstation, make sure that the `bmctl register bootstrap` process is still running. If it isn't, re-run the command with the same arguments and add the flag `--reuse-bootstrap-cluster=true`.

  2. Run `gcloud ... update` to fix the invalid IP address:
         
         gcloud container bare-metal admin-clusters update ADMIN_CLUSTER_NAME \
           --project=FLEET_HOST_PROJECT_ID \
           --location=REGION \
           --control-plane-node-configs 'node-ip=NEW_NODE_ID_ADDRESS'
         

For more information, see [gcloud container bare-metal admin-clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update).




Details about the cluster creation process are output on your admin workstation. If the preflight checks pass, you see something like the following:
    
    
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
    

## Connect to the admin cluster

The `bmctl register bootstrap` command creates a `kubeconfig` file for the admin cluster on your admin workstation. The directory where the `kubeconfig` is located and the filename are based on the admin cluster name as follows:
    
    
    bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig
    

You need to restrict access to this `kubeconfig` because it contains authentication credentials for the cluster.

If you want to use your Google identity to sign in to the cluster, you can set up the connect gateway as follows:

  1. On your admin workstation, set the `KUBECONFIG` environment variable:
         
         export KUBECONFIG=$HOME/bmctl-workspace/ADMIN_CLUSTER_NAME/ADMIN_CLUSTER_NAME-kubeconfig
         

  2. Set the current context in an environment variable:
         
         export CONTEXT="$(kubectl config current-context)"
         

  3. Run the following `gcloud` command. This command does the following:

     * Grants your user account the Kubernetes `clusterrole/view` role on the cluster.
     * Configures the cluster so that you can run read-only `kubectl` commands on your local computer without having to SSH to the admin workstation.

Replace `GOOGLE_ACCOUNT_EMAIL` with the email address that is associated with your Google Cloud account. For example: `--users=alex@example.com`.
    
    gcloud container fleet memberships generate-gateway-rbac  \
        --membership=ADMIN_CLUSTER_NAME \
        --role=clusterrole/view \
        --users=GOOGLE_ACCOUNT_EMAIL \
        --project=FLEET_HOST_PROJECT_ID \
        --kubeconfig=$KUBECONFIG \
        --context=$CONTEXT\
        --apply
    

The output of this command is similar to the following, which is truncated for readability:
    
    Validating input arguments.
    Specified Cluster Role is: clusterrole/view
    Generated RBAC policy is:
    --------------------------------------------
    ...
    
    Writing RBAC policy for user: GOOGLE_ACCOUNT_EMAIL to cluster.
    Successfully applied the RBAC policy to cluster.
    




With these RBAC policies in place, you can sign in to the cluster from the console using your Google identity. Additionally, you can run read-only `kubectl` commands on computers other than the admin workstation using a special `kubeconfig` that routes requests through the connect gateway.

  1. Run the following command on a computer other than the admin workstation to get the `kubeconfig` entry that can access the cluster through the connect gateway.
         
         gcloud container fleet memberships get-credentials ADMIN_CLUSTER_NAME \
             --project=FLEET_HOST_PROJECT_ID
         

The output is similar to the following:
         
         Starting to build Gateway kubeconfig...
         Current project_id: FLEET_HOST_PROJECT_ID
         A new kubeconfig entry "connectgateway_FLEET_HOST_PROJECT_ID_global_ADMIN_CLUSTER_NAME" has been generated and set as the current context.
         

  2. You can now run `kubectl` commands through the connect gateway:
         
         kubectl get pods -A
         




## What's next

  * [Delete an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/reset-nodes#delete_self-managed_clusters)
  * [Unregister an unavailable cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister#unregister_unavailable)
  * [Add a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-user-cluster-api)
  * [Manage clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/anthos-ui)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
