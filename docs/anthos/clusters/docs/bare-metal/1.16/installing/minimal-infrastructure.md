---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/minimal-infrastructure/
title: Plan your installation \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:09.461521+00:00
---

# Plan your installation  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/minimal-infrastructure/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Plan your installation Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/minimal-infrastructure)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/minimal-infrastructure)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page is the first part of a guide that walks you through a small proof-of-concept installation of Distributed Cloud. This document shows you how to set up a minimal hardware environment and plan your IP addresses. The follow-up [Create basic clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/quickstart) shows you how to create an admin cluster and a user cluster. The infrastructure you set up using this guide might not be suitable for your actual production needs and use cases. For more information about production installations, see [Choose a deployment model](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep).

## Before you begin

  1. Read [About Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal). 
  2. Familiarize yourself with some basic Google Cloud concepts, including [projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), [IAM permissions](https://docs.cloud.google.com/iam/docs/overview), and [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts). 

  3. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Make a note of the Google Cloud project ID, because it's needed later. 



## Procedure overview

Minimal infrastructure setup consists of these primary steps:

  1. **Set up your admin workstation.** Set up a Linux admin workstation for on-premises management tasks. This could be an existing or a dedicated machine, which can manage multiple clusters.

  2. **Set up your cluster node machines.** Set up at least three machines for nodes: one admin cluster node, one user cluster control plane node, and one user cluster worker node.

  3. **Plan your networking.** Plan the IP addresses for your node machines, virtual IP addresses (VIPs), and Service and Pod CIDR ranges.

  4. **Review required Google Cloud resources.** To create clusters, your Google Cloud project requires specific Google APIs and service accounts.




## 1\. Set up your admin workstation

The admin workstation hosts tools and configuration files for creating and working with your clusters.

### Hardware requirements

The admin workstation requires significant computing power, memory, and storage to run tools and store the resources associated with cluster creation and management.

Ensure your admin workstation meets the following hardware requirements:

  * At least 2 CPU cores
  * At least 4 GiB of RAM
  * At least 128 GiB of storage



### Configure the operating system and software

On the admin workstation, you install and configure the following:

  * **Configure Ubuntu**

  * **Install the gcloud CLI**

  * **Install`kubectl`**

  * **Install`bmctl`**




#### Configure the operating system

In order to run `bmctl` and create a cluster, the admin workstation has the same operating system (OS) requirements as nodes. Each machine must run a supported version of Ubuntu, such as Ubuntu 20.04.

**Note:** While Google Distributed Cloud is supported on multiple Linux operating systems, this minimal example uses Ubuntu for simplicity. Any steps or behavior that are specific to Ubuntu are highlighted in the documents.

Run the following commands to update firewall settings, install and configure Docker, and ensure each machine uses time synchronization:

  1. Disable Uncomplicated Firewall (UFW) and verify its status:
         
         sudo ufw disable
         sudo ufw status
         

  2. Remove any previous Docker version, update your package manager, and install the latest version of Docker:
         
         sudo apt-get remove docker docker-engine docker.io containerd runc
         sudo apt-get update
         sudo apt-get install \
           apt-transport-https \
           ca-certificates \
           curl \
           gnupg-agent \
           software-properties-common \
           docker.io
         

  3. Verify you're now running version 19.03+ of Docker:
         
         sudo docker version
         

Both Client and Server versions should be 19.03 or higher as shown in the following sample response:
         
         Client:**Version:           20.10.21**
          API version:       1.41
          Go version:        go1.18.1
          ...
         
         Server:
          Engine:**Version:          20.10.21**
           API version:      1.41 (minimum version 1.12)
           Go version:       go1.18.1
           ...
         

  4. Create the `docker` group.
         
         sudo groupadd docker
         

  5. Add yourself to the Docker group:
         
         sudo usermod -aG docker $USER
         

  6. Run the following command to activate your group changes:
         
         newgrp docker
         

  7. Run the following command to verify the system clock is synchronized:
         
         timedatectl
         

The output of `timedatectl` should contain the following status:
         
         System clock synchronized: yes
         




#### Install the Google Cloud CLI

To install the Google Cloud CLI on Ubuntu, follow the instructions in this [installation guide](https://docs.cloud.google.com/sdk/docs/install#deb).

Perform the following steps on your admin workstation to configure gcloud CLI:

  1. Sign in to set your gcloud CLI `account` property:
         
         gcloud auth login
         

  2. Set your gcloud CLI `project` property:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  3. Verify that your `account` and `project` properties are set correctly:
         
         gcloud config list
         

The output shows the values of your `account` and `project` properties. For example:
         
         [core]
         account = my-name@google.com
         disable_usage_reporting = False
         project = my-project-1234
         Your active configuration is: [default]
         




#### Install `kubectl`

To install `kubectl`:

  1. Run the following command on your admin workstation:
         
         gcloud components install kubectl
         




#### Install `bmctl`

`bmctl` is the proprietary command-line tool for Google Distributed Cloud that you can use for cluster creation and management.

To install `bmctl` on your admin workstation:

  1. Create a `baremetal` directory and add it to your path. If you are in your home directory, the commands are:
         
         mkdir baremetal
         export PATH="$HOME/baremetal:$PATH"
         

  2. Run the following command to download the latest version of the `bmctl` binary file and make it executable:
         
         gcloud storage cp gs://anthos-baremetal-release/bmctl/1.16.8/linux-amd64/bmctl .
         chmod +x ./bmctl
         

  3. Verify that `bmctl` is installed and executable:
         
         bmctl version
         

The response should look something like the following:
         
         [2023-05-12 17:36:16+0000] bmctl version: 1.14.2-gke.11, git commit: 4ff1347446a93925a079000b50437d4ecebcdf3a, build date: Mon Feb 27 14:07:30 PST 2023




### Connectivity

The admin workstation needs access to Google Cloud and all your cluster nodes.

#### Access to Google Cloud

The admin workstation accesses Google Cloud to download and install tools and images, process authorization requests, create service accounts, manage logging and monitoring, and more. You can't create clusters without access to Google Cloud.

#### Access from the admin workstation

To create and manage clusters from your admin workstation, you need the following access to the node machines:

  * Layer 3 connectivity to all cluster node machines.
  * Access to the control plane VIP.
  * Passwordless `root` access to all cluster node machines through SSH. SSH access can be either direct or through `sudo`.



The following section contains instructions for setting up SSH on the admin workstation and the node machines.

## 2\. Set up your cluster node machines

For the minimal installation of a single, non-high availability admin cluster and a single, non-high availability user cluster, you need three machines:

  * A machine for an admin cluster with one control plane node.

  * Two machines for a user cluster with one control plane node and one worker node.




### Hardware requirements

Each node machine must meet the following hardware requirements:

  * At least 2 CPU cores
  * At least 4 GiB of RAM
  * At least 128 GiB of storage



### Configure Ubuntu

Configure Ubuntu on each node with the same instructions that were used for the admin workstation.

### Set up SSH access to nodes

The admin workstation needs passwordless `root` access to all cluster node machines through SSH. The `root` access can be either direct or through `sudo`.

These are the high-level steps for setting up SSH for Google Distributed Cloud:

  1. **Install and configure SSH on all machines**

  2. **Create SSH keys and copy the public key to each node machine**

  3. **Disable password authentication on node machines**

  4. **Verify SSH access between admin workstation and node machines**




##### Install and configure SSH on all machines

Google Distributed Cloud requires passwordless SSH communication between the admin workstation and the cluster nodes. The following steps must be performed on the admin workstation and each node machine.

To configure SSH on machines running Ubuntu:

  1. If you don't already have an SSH server running, install one now:
         
         sudo apt update
         sudo apt install openssh-server
         sudo systemctl status ssh
         

  2. Enable `root` SSH password authentication by uncommenting or adding the `PermitRootLogin` and `PasswordAuthentication` lines in the `/etc/ssh/sshd_config` file and setting the values to `yes`:

**Note:** `PasswordAuthentication` is enabled temporarily to help with SSH setup. `PasswordAuthentication` is disabled on the node machines in a subsequent section.
         
         # Authentication:
         
         #LoginGraceTime 2m**PermitRootLogin yes**
         #StrictModes yes
         #MaxAuthTries 6
         #MaxSessions 10
         ...**PasswordAuthentication yes**
         

  3. Set a root password:
         
         sudo passwd root
         

  4. To apply your SSH configuration changes, restart the SSH service:
         
         sudo systemctl restart ssh.service
         

  5. Restart the machine.

  6. Verify that SSH is working by establishing an SSH connection from another machine.




##### Create SSH keys and copy the public key to each node machine

For secure, passwordless connections between the admin workstation and nodes, create an SSH key on your admin workstation and share the public key with the nodes.

  1. On your admin workstation, generate a private and public key pair. Don't set a passphrase for the keys:
         
         ssh-keygen -t rsa
         

  2. On your admin workstation, copy the generated public key to each of your node machines:
         
         ssh-copy-id -i PUBLIC_KEY root@CLUSTER_NODE_IP
         

Replace the following:

     * `PUBLIC_KEY`: the path to the file containing the SSH public key. By default, the path is `/home/USERNAME/.ssh/id_rsa.pub`
     * `CLUSTER_NODE_IP`: the IP address of the node machine



##### Disable password authentication on node machines

At this point, you no longer need to have password authentication enabled.

For each node machine:

  1. Open `/etc/ssh/sshd_config` and set `PasswordAuthentication` to `no` and save the file.

  2. Restart the SSH service.
         
         sudo systemctl restart ssh.service
         




##### Verify SSH access between admin workstation and node machines

When SSH is configured properly, you can establish an SSH connection to the node machine from the admin workstation (as root) without a password.

To verify that public key authentication works between your admin workstation and your cluster nodes:

  1. On the admin workstation, run the following command for each node machine:
         
         ssh -o IdentitiesOnly=yes -i PRIVATE_KEY root@CLUSTER_NODE_IP
         

Replace the following:

     * `PRIVATE_KEY`: the path to the file containing the SSH private key. By default, the path is `/home/USERNAME/.ssh/id_rsa`
     * `CLUSTER_NODE_IP`: the IP address of the node machine



## 3\. Plan your networking

When installing clusters, it's important that you plan your IP addresses, including making sure that you don't create any addressing conflicts. You might need your network administrator to help you find suitable addresses, even for this simple installation. Not counting Pods and Services CIDRs, you need at least 15 unique IP addresses for a minimum admin cluster and user cluster installation.

Plan and specify IP addresses for the following cluster components:

  * Cluster nodes: you need an IP address for each node machine
  * Virtual IP addresses (VIPs): you need VIPs for access to the Kubernetes API servers, the ingress proxy, and Services of type LoadBalancer
  * Pods and Services: you need CIDR address ranges to accommodate every Pod and Service running on your clusters



The rest of this section has illustrative examples of values that work for this installation in a hypothetical network - your values will be different.

For this small installation, put your admin workstation, admin cluster node, and user cluster nodes in the same Layer 2 domain. For example, suppose that all IP addresses in the `172.16.20.0/24` range are routed to a particular Layer 2 domain. Also suppose that your network administrator says you can use `172.16.20.10` \- `172.16.20.12` for node machine addresses and `172.16.0.13` \- `172.16.20.24` for VIPs.

**Important:** The IP address examples used in this document meet the requirements for Google Distributed Cloud. However, you must use IP addresses that are available in your network. If you're installing Google Distributed Cloud on a home network, you likely need to adjust addresses for node machines and the cluster VIPs.

The following diagram illustrates a Layer 2 domain that has an admin workstation, an admin cluster, and a user cluster:

[ ![IP addresses for an admin cluster and a user cluster.](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/installing/images/abm-ip-planning-min.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/bare-metal/1.16/installing/images/abm-ip-planning-min.svg) IP addresses for an admin cluster and a user cluster (Click to enlarge)

### Example cluster node IP addresses

The following table gives an example of how IP addresses could be used for cluster nodes:

Machine | Description | IP address  
---|---|---  
Admin cluster control plane node | Physical machine that serves as the control plane node for the admin cluster | 172.16.20.10  
User cluster control plane node | Physical machine that serves as the control plane node for the user cluster | 172.16.20.11  
User cluster worker node | Physical machine that runs user workloads | 172.16.20.12  
  
### Example virtual IP addresses (VIPs)

The following table gives an example of how you could specify VIPs for your clusters:

VIP | Description | IP address  
---|---|---  
Admin cluster control plane VIP address | Admin cluster control plane VIP address (admin cluster Kubernetes API server) | 172.16.20.13  
User cluster control plane VIP address | User cluster control plane VIP address (user cluster Kubernetes API server) | 172.16.20.14  
Ingress VIP address | Ingress VIP (included in MetalLB address pool range) | 172.16.20.15  
Service VIP addresses | Ten addresses for use as external IP addresses for Services of type `LoadBalancer`. Addresses are allocated as needed on user cluster nodes. This range includes the ingress VIP. This overlap of IP addresses is a requirement for MetalLB, the default bundled load balancer. | 172.16.20.15 - 172.16.20.24  
  
### IP addresses for Pods and Services

In addition to the IP addresses you have specified for cluster nodes and VIPs, you need to specify addresses for Pods and Services. You specify a [CIDR](https://datatracker.ietf.org/doc/html/rfc1519) range to be used for Pod IP addresses and another CIDR range to be used for the `ClusterIP` addresses of Kubernetes Services. Use IP addresses in the private address space, as described in [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3). These addresses are specified as part of cluster configuration, as illustrated in the next part of this guide.

As part of your IP planning, decide what CIDR ranges you want to use for Pods and Services. Unless you have a reason to do otherwise, use the following suggested ranges:

Purpose | Prepopulated CIDR range  
---|---  
Admin cluster Pods | 192.168.0.0/16  
Admin cluster Services | 10.96.0.0/20  
User cluster Pods | 192.168.0.0/16  
User cluster Services | 10.96.0.0/20  
  
The suggested ranges illustrate these points:

  * The Pod CIDR range can be the same for multiple clusters in the default, _island mode_ network model.

  * The Service CIDR range can be the same for multiple clusters.

  * Typically you need more Pods than Services in a cluster, so you probably want a Pod CIDR range that is larger than the Service CIDR range. For example, the suggested Pod range for a user cluster has 2(32-16) = 216 addresses, but the suggested Service range for a user cluster has only 2(32-20) = 212 addresses.




#### Avoid overlap

To avoid overlapping with IP addresses that are reachable on your network, you might need to use CIDR ranges that are different from the preceding suggestions. The Service and Pod ranges must not overlap with any address outside the cluster that you want to reach from inside the cluster.

For example, suppose that your Service range is `10.96.232.0/24`, and your Pod range is `192.168.0.0/16`. Traffic sent from a Pod to an address in either of those ranges is treated as in-cluster and can't reach any destination outside the cluster.

In particular, the Service and Pod ranges must not overlap with:

  * IP addresses of nodes in any cluster

  * IP addresses used by load balancer machines

  * VIPs used by control-plane nodes and load balancers

  * IP address of DNS servers or NTP servers




## 4\. Review required Google Cloud resources

Before you can create clusters, Google Distributed Cloud requires a specific set of Google APIs to be enabled in your associated Google Cloud project. To use the Google APIs, Google Distributed Cloud requires [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) configured with specific IAM roles in your associated Google Cloud project.

The process for creating clusters in the next part of this guide, [Create basic clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/quickstart), enables APIs and creates service accounts for you automatically.

Here are the Google APIs that are automatically enabled:

  * `anthos.googleapis.com`
  * `anthosaudit.googleapis.com`
  * `anthosgke.googleapis.com`
  * `cloudresourcemanager.googleapis.com`
  * `connectgateway.googleapis.com`
  * `container.googleapis.com`
  * `gkeconnect.googleapis.com`
  * `gkehub.googleapis.com`
  * `gkeonprem.googleapis.com`
  * `iam.googleapis.com`
  * `logging.googleapis.com`
  * `monitoring.googleapis.com`
  * `opsconfigmonitoring.googleapis.com`
  * `serviceusage.googleapis.com`
  * `stackdriver.googleapis.com`
  * `storage.googleapis.com`



The following table describes the service accounts that are created automatically:

Service account | Purpose | Roles  
---|---|---  
anthos-baremetal-gcr |  Distributed Cloud uses this service account to download container images from Container Registry.  | None  
anthos-baremetal-connect |  [Connect Agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent) uses this service account to maintain a connection between your cluster and Google Cloud. This enables access to the cluster and to workload management features, including the Google Cloud console and the [connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway) to interact with your cluster.  | roles/gkehub.connect  
anthos-baremetal-register |  Connect Agent uses this service account to register your clusters with [ a fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts).  | roles/gkehub.admin  
anthos-baremetal-cloud-ops |  Stackdriver Agent uses this service account to export logs and metrics from clusters to [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).  |  roles/logging.logWriter  
roles/monitoring.metricWriter  
roles/stackdriver.resourceMetadata.writer  
roles/opsconfigmonitoring.resourceMetadata.writer  
roles/monitoring.dashboardEditor   
  
## What's next

[Create basic clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/quickstart)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
