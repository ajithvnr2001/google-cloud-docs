---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/workstation-prerequisites/
title: Admin workstation prerequisites \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:45.822260+00:00
---

# Admin workstation prerequisites  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/workstation-prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Admin workstation prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

The admin workstation hosts command-line interface (CLI) tools and configuration files to provision clusters during installation, and CLI tools for interacting with provisioned clusters post-installation.

This page is for Admins and architects and Operators who set up, monitor, and manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

You download and run tools, such as `bmctl` and the Google Cloud CLI, on the admin workstation to interact with clusters and Google Cloud resources. The admin workstation hosts configuration files to provision clusters during installation, upgrades, and updates. Post installation, the admin workstation hosts `kubeconfig` files so that you can use `kubectl` to interact with provisioned clusters. You also access logs for critical cluster operations on the admin workstation. A single admin workstation can be used to create and manage many clusters.

Make sure the admin workstation meets the prerequisites described in the following sections.

**Note:** A workstation that meets the requirements on this page can be used as the admin workstation for creating and managing your clusters. Also, you can use the workstation as an admin control plane node for one of your clusters.

## Operating system and software

In order to run `bmctl` and work as a control plane node, the admin workstation has the same operating system (OS) requirements as nodes. The admin workstation requires Docker, but not for use as a container runtime. When Google Distributed Cloud creates clusters, it deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (kind) cluster on the admin workstation. This _bootstrap_ cluster hosts the Kubernetes controllers needed to create clusters. Unless you specify otherwise, the bootstrap cluster is removed when cluster creation completes successfully. The bootstrap cluster requires Docker to pull container images.

**Note:** The bootstrap cluster uses a single in-memory node to perform installation and has limited resources. If you're installing a cluster with more than 20 nodes, create the cluster with control plane nodes only. After the cluster is up and running, [add the remaining worker nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#add_or_remove_nodes_in_a_cluster). In this scenario, the control plane nodes perform the worker node installation.

The admin workstation must meet the following requirements before you can install a cluster:

  * Operating system is a supported Linux distribution.

For a list of supported Linux OSes and versions, see [Select your operating system](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs). That page has links to configuration instructions, including Docker configuration, for each OS.

  * Docker version 19.03 or later is installed. However, if your system uses cgroup v2, the Docker installation on your admin workstation must be version 20.10.0 or higher. (You can tell if your system uses cgroup v2 by the presence of the file `/sys/fs/cgroup/cgroup.controllers`).

**Warning:** Docker installed by [snap](https://snapcraft.io/) is in [strict confinement mode](https://snapcraft.io/docs/snap-confinement) by default, which means Docker can't access files outside the `$HOME` directory. Verify that Docker is in strict confinement mode by running `snap info --verbose docker | grep confinement` on your admin workstation. If this applies to you, make sure that the `bmctl-workspace` folder is in the `$HOME` directory.
  * Non-root user is a member of the `docker` group (for instructions, go to [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)).

  * Google Cloud CLI is installed.

You use `kubectl` and `bmctl` tools to create and manage clusters. To install these tools, you need the `gcloud` tool. The `gcloud` and `kubectl` command-line tools are components of gcloud CLI. For installation instructions, including instructions for installing components, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  * `kubectl` is installed. Use gcloud CLI to install `kubectl` with the following command:
        
        gcloud components install kubectl
        

  * `bmctl` is installed for the version of the cluster that you're creating or operating.

Installation consists of using `gcloud` to download `bmctl` binary or images package. For instructions, see [Google Distributed Cloud for bare metal downloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).




## Hardware resource requirements

The admin workstation requires significant computing power, memory, and storage to run tools and store the resources associated with cluster creation and management.

By default, the cluster upgrade and cluster create operations use a bootstrap cluster. When a bootstrap cluster is used, there is a significant increase in CPU and memory usage. If you intend to use the admin workstation as a control plane node, use no less than the higher, recommended amount of CPUs and RAM to prevent admin workstation activities from disrupting cluster control plane fuctions.

Depending on the size of etcd database and number of control plane nodes, cluster backup and restore operations consume significant RAM. The rough estimate for RAM required for backups is 3-5 GiB per control plane node. The backup process fails there isn't enough memory. Plan your RAM requirements accordingly.

The following table provides the minimum and recommended hardware requirements for the admin workstation:

Resource | Minimum | Recommended  
---|---|---  
**CPUs / vCPUs *** | 2 core | 4 core  
**RAM** | Ubuntu: 4 GiBRHEL: 6 GiB | Ubuntu: 8 GiBRHEL: 12 GiB  
**Storage** | 128 GiB | 256 GiB  
  
* Google Distributed Cloud supports only x86-64 CPUs and vCPUs at the CPU microarchitecture level v3 (x86-64-v3) and higher.

## Networking requirements

The admin workstation needs access to Google Cloud and all your cluster nodes.

### Access to Google Cloud

The admin workstation accesses Google Cloud to download and install tools and images, process authorization requests, create service accounts, manage logging and monitoring, and more. You can't create clusters without access to Google Cloud.

Access to Google Cloud can be either direct or through a proxy server. For information on different ways to connect to Google Cloud, see [Connect to Google](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/connect-on-prem-gcp). For information on configuring a proxy server, see [Install behind a proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/proxy).

For information about the consequences of interrupted access to Google Cloud, see [Impact of temporary disconnection from Google Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/connectivity).

### Access to nodes

To create and manage clusters from your admin workstation, you need the following access to the node machines:

  * Layer 3 connectivity to all cluster node machines.
  * Passwordless SSH access to all cluster node machines as either `root` or as a [non-root user with passwordless `sudo` privileges](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#set_a_login_user). This high level of permissions is required by automation tooling to perform node-level tasks that provision the nodes during cluster installation.

  * Access to the control plane VIP.




### IP forwarding

IP forwarding must be enabled on the admin workstation. Without IP forwarding, the bootstrap cluster can't be created, which blocks cluster creation. If IP forwarding is disabled, you see an error like the following when you attempt to create a cluster:
    
    
    Error message: E0202 14:53:25.979322 225917 console.go:110] Error creating cluster: create kind cluster failed: error creating bootstrap cluster: failed to init node with kubeadm: command "docker exec --privileged bmctl-control-plane kubeadm init --skip-phases=preflight --config=/kind/kubeadm.conf --skip-token-print --v=6" failed with error: exit status 1

You can check the IP forwarding setting with the following command:
    
    
    cat /proc/sys/net/ipv4/ip_forward
    

A value of `1` indicates that IP forwarding is enabled. If IP forwarding is disabled (`0`), use the following command to enable it:
    
    
    echo '1' | sudo tee /proc/sys/net/ipv4/ip_forward
    

### Set up `root` SSH access to nodes

To enable secure, passwordless connections between the admin workstation and the cluster node machines, create an SSH key on your admin workstation and share the public key with cluster nodes.

**Note:** The following instructions set up passwordless SSH access to nodes for the `root` user. Alternatively, you can use a non-root user who has passwordless `sudo` privileges. This non-root user must be specified in the cluster configuration file (`nodeAccess.loginUser`). For more information, see [Set a login user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#set_a_login_user).

  1. Enable `root` SSH password authentication on each cluster node machine by uncommenting or adding the `PermitRootLogin` and `PasswordAuthentication` lines in the `/etc/ssh/sshd_config` file and setting the values to `yes`.
         
         # $OpenBSD: sshd_config,v 1.103 2018/04/09 20:41:22 tj Exp $
         
         # This is the sshd server system-wide configuration file.  See
         # sshd_config(5) for more information.
         
         ...
         
         # Authentication:
         
         #LoginGraceTime 2m**PermitRootLogin yes**
         #StrictModes yes
         #MaxAuthTries 6
         #MaxSessions 10
         
         ...
         **PasswordAuthentication yes**
         

Initially, you need SSH password authentication enabled on the remote cluster node machines to share keys from the admin workstation.

  2. To apply your SSH configuration changes, restart the SSH service:
         
         sudo systemctl restart ssh.service
         

  3. Generate a private and public key pair on the admin workstation. Don't set a passphrase for the keys. Generate the keys with the following command:
         
         ssh-keygen -t rsa
         

You can also use `sudo` user access to the cluster node machines to set up SSH. However, for passwordless, _non-root_ user connections you must update the cluster configuration file with the `spec.nodeAccess.loginUser` field. This field is commented out by default. You can specify your non-root username with `loginUser` during cluster creation or anytime after that. For more information, see [`loginUser`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#nodeaccess-loginuser).

  4. Add the generated public key to the cluster node machines:
         
         ssh-copy-id -i PATH_TO_IDENTITY_FILE root@CLUSTER_NODE_IP
         

Replace the following:

     * `PATH_TO_IDENTITY_FILE`: the path to the file containing the SSH public key. By default, the path to the identity file containing the public key is `/home/USERNAME/.ssh/id_rsa.pub`.
     * `CLUSTER_NODE_IP`: the IP address of the node machine to which you're adding the SSH public key.
  5. Disable SSH password authentication on the cluster node machines by setting `PasswordAuthentication` to `no` in the `sshd_config` file and restarting the SSH service.

  6. Use the following command on the admin workstation to verify the public key authentication works between the workstation and the node machines.
         
         ssh -o IdentitiesOnly=yes -i PATH_TO_IDENTITY_FILE root@CLUSTER_NODE_IP
         

When SSH is configured properly, you can log into the node machine from the admin workstation (as `root`) without having to enter a password.




## What's next

  * [Node machine prerequisites](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/node-machine-prerequisites)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
