---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation/
title: Create an admin workstation \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:23.229932+00:00
---

# Create an admin workstation  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Create an admin workstation Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to create an admin workstation, for Google Distributed Cloud. The admin workstation hosts command-line interface (CLI) tools and configuration files to provision clusters during installation, and CLI tools for interacting with provisioned clusters post-installation.

This page is for Admins, Architects, and Operators who set up, monitor, and manage the tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

The instructions here are complete. For a shorter introduction to creating an admin workstation, see [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-create-clusters#3_create_an_admin_workstation) in the Create basic clusters guide.

## Choose how to create the admin workstation

There are two ways you can create an admin workstation:

  * Use `gkeadm` to create an admin workstation VM in your vSphere environment.
  * Create a user-managed admin workstation on any computer of your choice.



Both approaches have advantages and disadvantages.

When you use `gkeadm` to create your admin workstation, `gkeadm` does the following, which simplifies the setup:

  * Creates the admin workstation VM.
  * The VM template that `gkeadm` uses to create the admin workstation has all the software that you need to create and manage clusters using the `gkectl` command-line tool.
  * Creates one user account that you or other administrators use to log on to the admin workstation.
  * Provides the SSH command to log on to the admin workstation with the provided user account.



A `gkeadm`-created admin workstation can only manage one admin cluster. If you plan to create several admin clusters, then you need to create an admin workstation for each admin cluster.

The `gkeadm`-created admin workstation is tied to cluster lifecycle. When you upgrade an admin cluster or any of the user clusters managed by the admin cluster, you first have to upgrade the admin workstation.

When you set up your own admin workstation, you have to install one of the required operating systems and all the required software. This makes the initial setup more time consuming because creating a VM from a template is faster than installing the required software on a computer. However, after the workstation is set up, it has the following advantages over a `gkeadm`-created admin workstation:

  * You can configure the user-managed workstation to create and manage more than one admin cluster.
  * You don't need to upgrade a user-managed admin workstation when you upgrade a cluster.
  * You can use standard CI/CD tools to automate cluster lifecycle management.
  * You can use standard authentication methods such as Active Directory to control access to the admin workstation.
  * You can use standard authorization systems to control what users can access on the admin workstation and to audit their actions.
  * You can choose the software that you want to use to create snapshots or backups of the admin workstation.



## Create the admin workstation

### `gkeadm`

## Before you begin

[Know your vCenter server address.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address)

[Know your CA cert path.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path)

[Install the Google Cloud CLI.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cloud-sdk)

Create one or more Google Cloud projects as described in [Using multiple Google Cloud projects](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects).

## Planning your service accounts

When you use `gkeadm` to create an admin workstation, you have the option of letting `gkeadm` create some of your service accounts and keys for you. In that case, `gkeadm` also grants the appropriate Identity and Access Management roles to the service accounts.

As an alternative, you can create your service accounts and keys manually. In that case, you must manually grant IAM roles to your service accounts.

Creating service accounts manually gives you more flexibility than having `gkeadm` create them for you:

  * Automatically created service accounts all have the same parent Google Cloud project as your component access service account. When you create a service account manually, you can choose the parent Google Cloud project.

  * Automatically created service accounts are all granted IAM roles on the parent Google Cloud project of your component access service account. This is fine if that is the only Google Cloud project associated with your clusters. But if you want to associate your clusters with [multiple Google Cloud projects](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects), then you need the flexibility to grant roles to a service account on a Google Cloud project of your choice.




If you decide to create your own service accounts, follow the instructions in [Service accounts and keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts).

Regardless of whether you have `gkeadm` create service accounts for you automatically, there is one service account that you must create manually: your component access service account. For instructions on how to create your component access service account and grant it the appropriate IAM roles, see [Component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account).

There is one other service account that you might need to create manually: your [audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account). If you want to use a [GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) client to manage your user clusters, then you must enable [audit logging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#cloudauditlogging-section) in your admin cluster.

## Generating templates for your configuration files

[Download `gkeadm`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads) to your current directory.

Generate templates:
    
    
    ./gkeadm create config
    

The preceding command created these files in your current directory:

  * `credential.yaml`
  * `admin-ws-config.yaml`



## Filling in `credential.yaml`

In `credential.yaml`, fill in your vCenter username and password. For example:
    
    
    kind: CredentialFile
    items:
    - name: vCenter
    username: "my-account-name"
    password: "AadmpqGPqq!a"
    

## Filling in `admin-ws-config.yaml`

**Note:** Admin workstations cannot contain special characters and cannot be renamed after creation.

Several fields in `admin-ws-config.yaml` are already filled in with default or generated values. You can keep the populated values or make changes as you prefer.

See the fields that are already filled in.
    
    
    vCenter:
    credentials:
      fileRef:
      path: credential.yaml
      entry: vCenter
    
    adminWorkstation:
    name: gke-admin-ws-...
    cpus: 4
    memoryMB: 8192
    
    diskGB: 100
    dataDiskName: gke-on-prem-admin-workstation-data-disk,,,.vmdk
    dataDiskMB: 512
    network:
      ntpServer: ntp.ubuntu.com
    

**Warning:** If you will be using static IPs for your admin and user clusters, make sure that admin workstation name specified in `admin-ws-config.yaml` isn't included as a hostname in the [IP block files](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) `admin-ip-block.yaml` and `user-ip-block.yaml`.

### Fields that you must fill in

Fill in the following required fields. For information on how to fill in the fields, [Admin workstation configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file).
    
    
    gcp:
     componentAccessServiceAccountKeyPath: "Fill in"
    vCenter:
    credentials:
      address: "Fill in"
    datacenter: "Fill in"
    datastore: "Fill in"
    cluster: "Fill in"
    network: "Fill in"
    resourcePool: "Fill in"
    caCertPath: "Fill in"
    

If you want to create your admin workstation inside a vSphere VM folder, fill in the `vCenter.folder` field:
    
    
    vCenter:
    folder: "Fill in"
    

If your admin workstation will be behind a proxy server, fill in the `proxyURL` field:
    
    
    adminWorkstation:
    proxyURL: "Fill in"
    

If you want your admin workstation to get its IP address from a DHCP server, set `ipAllocationMode` to `"dhcp"`, and remove the `hostconfig` section:
    
    
    adminWorkstation:
    network:
      ipAllocationMode: "dhcp"
    

If you want to specify a static IP address for your admin workstation, set `ipAllocationMode` to `"static"`, and fill in the [`hostconfig`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file#adminworkstationnetworkhostconfig) section:
    
    
    adminWorkstation:
    network:
      ipAllocationMode: "static"
      hostconfig:
        ip: "Fill in"
        gateway: "Fill in"
        netmask: "Fill in"
        dns:
        - "Fill in"
    

**Note:** Check the vCenter network to make sure the static IP address that you enter is not already in use.

## Logging in

  1. Log in with any Google Account. This sets your SDK `account` property:


    
    
    gcloud auth login
    

  1. Verify that your SDK `account` property is set correctly:


    
    
    gcloud config list
    

  1. The Google Account that is set as your [SDK `account` property](https://docs.cloud.google.com/sdk/docs/properties) is called your _SDK account_. The `gkeadm` command-line tool uses your SDK account to download the admin workstation OVA and enable services in your Google Cloud project.



If you choose to have `gkeadm` automatically create service accounts for you, then `gkeadm` also uses your SDK account to create service accounts and keys, and to grant roles to service accounts. So it is important that you set your SDK `account` property before you run `gkeadm` to create an admin workstation.

The output shows the values of your SDK `account` property. For example:
    
    
    [core]
    account = my-name@google.com
    disable_usage_reporting = False
    Your active configuration is: [default]
    

## Grant roles to your SDK account

Your SDK account must have the following [IAM role](https://docs.cloud.google.com/iam/docs/overview) on the parent Google Cloud project of your component access service account. This is so that `gkeadm` can enable services on the Google Cloud project.

  * `serviceUsage.serviceUsageAdmin`



If you choose to have `gkeadm` automatically create service accounts for you, then your SDK account must also have the following roles on the parent project of your component access service account. This is so that `gkeadm` can create service accounts and keys.

  * `resourcemanager.projectIamAdmin`
  * `iam.serviceAccountCreator`
  * `iam.serviceAccountKeyAdmin`



To grant roles on a Google Cloud project, you must have certain permissions on the Google Cloud project. For details, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If you have the required permissions, you can grant the roles yourself. Otherwise, someone else in your organization must grant the roles for you.

To grant the required role to your SDK account:

### Linux and macOS
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="user:ACCOUNT" \
      --role="roles/serviceusage.serviceUsageAdmin"
    

### Windows
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
      --member="user:ACCOUNT" ^
      --role="roles/serviceusage.serviceUsageAdmin"
    

Replace the following:

  * `PROJECT_ID`: the ID of the parent Google Cloud project of your component access service account

  * `ACCOUNT`: your SDK account




To grant additional roles in case you want `gkeadm` to automatically create service accounts:

### Linux and macOS
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="user:ACCOUNT" \
      --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="user:ACCOUNT" \
      --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="user:ACCOUNT" \
      --role="roles/iam.serviceAccountKeyAdmin"
    

### Windows
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
      --member="user:ACCOUNT" ^
      --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
      --member="user:ACCOUNT" ^
      --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
      --member="user:ACCOUNT" ^
      --role="roles/iam.serviceAccountKeyAdmin"
    

Replace the following:

  * `PROJECT_ID`: the ID of the parent project of your component access service account

  * `ACCOUNT`: your SDK account




## Creating your admin workstation

Enter this command to create your admin workstation. If you want `gkeadm` to create the [connect-register](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account) and [logging-monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account) service accounts for you, include the `--auto-create-service-accounts` flag. If you want to create those service service accounts manually, omit the flag.
    
    
    ./gkeadm create admin-workstation [--auto-create-service-accounts]
    

The output gives detailed information about the creation of your admin workstation:
    
    
    ...
    Getting ... service account...
    ...
    ********************************************************************
    Admin workstation is ready to use.
    
    Admin workstation information saved to /usr/local/google/home/me/my-admin-workstation
    This file is required for future upgrades
    SSH into the admin workstation with the following command:
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.5.1
    ********************************************************************
    

## Getting an SSH connection to your admin workstation

Near the end of the preceding output there is a command you can use to get an SSH connection to your admin workstation. Enter that command now. For example:
    
    
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.5.1
    

List the files on your admin workstation:
    
    
    ls -1
    

In the output, you can see two cluster configuration files, your CA certificate file, and the JSON key file for your component access service account. If `gkeadm` created service accounts for you, you can also see the JSON key files for those service accounts. For example:
    
    
    admin-cluster.yaml
    user-cluster.yaml
    vcenter-ca-cert.pem
    component-access-key.json
    

Verify that `gkeadm` activated your component access service account on your admin workstation:
    
    
    gcloud config get-value account
    

## Copying JSON key files to your admin workstation

Before you create a cluster, the JSON key files for your service accounts must be on your admin workstation in the home directory.

The key for your component access service account is already on your admin workstation.

If you included the `--auto-create-service-accounts` flag when you ran `gkeadm create admin-workstation`, then then the keys for the following service accounts are already on your admin workstation in the home directory. Otherwise you must manually copy the keys to the home directory of your admin workstation:

  * Connect-register service account
  * Logging-monitoring service account



If you created any of the following service accounts, you must manually copy the keys for those service accounts to the home directory of your admin workstation:

  * Audit logging service account
  * Binary Authorization service account



## Restoring the admin workstation from a backup file

When you upgrade an admin workstation, the `gkeadm upgrade` command saves a backup file. Later, if you no longer have an admin workstation, or if you have lost some of the files that were on your upgraded admin workstation, you can use this backup file to create an admin workstation that is restored to what was in place immediately after the upgrade.

To create an admin workstation from a backup file, run this command:
    
    
    gkeadm create admin-workstation --restore-from-backup ADMIN_WORKSTATION_NAME-backup.tar.gz
    

Replace ADMIN_WORKSTATION_NAME with the name of the admin workstation.

### User-managed

Choose a computer to serve as your admin workstation. You can use either Ubuntu or Red Hat Enterprise Linux (RHEL). These are the requirements:

  * Ubuntu 20.04 LTS or 22.04 LTS

    * 4 CPU cores
    * 8 GiB RAM
    * 100 GiB of storage
  * RHEL 8.6, 8.7, or 8.8

    * 4 CPU cores
    * 12 GB RAM
    * 256 GiB of storage



## Access to Google Cloud

Your admin workstation must have access to Google Cloud to download and install tools, process authorization requests, create service accounts, and more.

For information on different ways to connect to Google Cloud, see [Connect to Google](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/connect-on-prem-gcp).

Access to Google Cloud can be direct or via a proxy server. For information on firewall rules and configuring a proxy server, see [Proxy and firewall rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules).

## Access to vCenter Server

To create and manage clusters from your admin workstation, you need access to your instance of vCenter Server. For information, see:

  * [vSphere requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements)
  * [Determine your vCenter server address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address)
  * [Getting your vCenter CA root certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path)



## Set up an NTP server

When your cluster is configured to use an NTP server, you need to set up a time sync service on your admin workstation to ensure that `timedatectl` reports time that is in sync with the cluster. This is required to avoid large clock drift issues, which might cause certificate verification failures due to unmatched expiration dates.

### Ubuntu

We recommend that you use the `chrony` time server.

To install `chrony`:
    
    
    sudo apt-get update
    sudo apt install chrony
    

This provides two binaries:

  * `chronyd` \- the daemon to sync and serve via the Network Time Protocol
  * `chronyc` \- the command-line interface for the `chrony` daemon



To configure `chronyd`:

Edit `/etc/chrony/chrony.conf` to add or remove server lines. Then restart `chrony`:
    
    
    sudo systemctl restart chrony.service
    

### RHEL

We recommend that you use the `chrony` time server.

For installation instructions, see [How to configure chrony](https://www.redhat.com/sysadmin/chrony-time-services-linux).

## Passwordless sudo

If your security policy allows it, enable passwordless sudo for the current user. This allows `gkectl` to prepare a private registry if one is provided, setup proxy for docker if your network is behind a proxy server, and force delete the bootstrap cluster that is used for admin cluster lifecycle operations in case the deletion fails.

If you choose not to enable passwordless sudo, and you intend to use a [private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section) for your admin cluster, then do the following manual configuration before you create the admin cluster:

  * Place the [CA root certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-cacertpath-field) for the private registry in this directory:
        
        /etc/docker/certs.d/REGISTRY_ADDRESS/

Replace REGISTRY_ADDRESS with the [address](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-address-field) of the machine that runs the private registry.

For more information, see [Verify repository client with certificates](https://docs.docker.com/engine/security/certificates/).

  * If your network is behind a proxy server, specify the [proxy server](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#proxy-section) in the admin cluster configuration file, and [configure Docker to use the proxy server](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy).




If you choose not to enable passwordless sudo, you might need to manually delete the `kind` cluster after you create an admin cluster. For more information, see [Kind cluster does not get deleted](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade#kind_cluster_not_deleted) in the troubleshooting documentation.

## Install software

### Ubuntu

Install the following software:

  * **Docker version 19.03 or later** : See [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/). Ensure that the non-root user is a member of the docker group. See [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

  * **Google Cloud CLI latest version** : See [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  * **kubectl** : Run `gcloud components install kubectl`, or use `apt-get`:



    
    
    sudo apt-get update
    sudo apt-get -y install kubectl
    

### RHEL

Install the following software:

**Docker 19.03 or later**

  1. Remove any previous Docker version:
         
         sudo dnf remove docker \
           docker-client \
           docker-client-latest \
           docker-common \
           docker-latest \
           docker-latest-logrotate \
           docker-logrotate \
           docker-engine
         

  2. Remove podman-manpages:
         
         sudo dnf remove podman-manpages
         

  3. Install Docker 19.03+:
         
         sudo dnf install -y yum-utils
         
         sudo yum-config-manager \
           --add-repo \
           https://download.docker.com/linux/centos/docker-ce.repo
         
         sudo dnf install -y --allowerasing docker-ce docker-ce-cli containerd.io
         
         sudo systemctl start docker
         

  4. Verify that you are now running version 19.03+:
         
         sudo docker version
         

  5. Compare your output with the following example to ensure the Client and Server versions are 19.03+:
         
         Client: Docker Engine - Community
         Version:           19.03.13
         ...
         Server: Docker Engine - Community
         Engine:
         Version:          19.03.13
         

  6. Verify Docker runs:
         
         docker run hello-world
         

You should see something similar to this:
         
         Hello from Docker!
         

This message shows that your installation appears to be working correctly.




**Google Cloud CLI latest version** :

See [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

**kubectl**

Run `gcloud components install kubectl`.

## Log in

The Google Account that is set as your [SDK `account` property](https://docs.cloud.google.com/sdk/docs/properties) is called your _SDK account_. The `gkectl` command-line tool uses your SDK account to download cluster node OVAs, pull container images and more. So it is important that you set your SDK account property before you run `gkectl` commands.

Log in with any Google Account. This sets your SDK `account` property:
    
    
    gcloud auth login
    

Verify that your SDK `account` property is set correctly:
    
    
    gcloud config list
    

The output shows the values of your SDK `account` property. For example:
    
    
    [core]
    account = my-name@google.com
    disable_usage_reporting = False
    Your active configuration is: [default]
    

## Download gkectl and the bundle

Navigate to a directory where you want to install `gkectl`.

Download `gkectl`:
    
    
    gcloud storage cp gs://gke-on-prem-release/gkectl/VERSION/gkectl ./
    chmod +x gkectl
    

Replace VERSION with the version of Google Distributed Cloud. For example: `1.16.0-gke.1`.

Download the Google Distributed Cloud bundle. Make sure the version matches the one you used to download `gkectl`:
    
    
    gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/VERSION/gke-onprem-vsphere-VERSION.tgz ./
    

## Service accounts and keys

Make sure you have created the following required service accounts and JSON key files:

  * [component access](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account)
  * [connect-register](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account)
  * [logging-monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account)



Also Make sure you have created any optional service service accounts and JSON key files that you need:

  * [audit logging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account)
  * [Binary Authorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#binary_authorization_service_account)



Place all of your JSON key files in the home directory of your admin workstation.

## Troubleshooting

The following section re-enables SSH access to the admin workstation in the event the SSH key is lost or corrupted.

### SSH key recovery

Use a temporary VM to perform the following steps:

  1. To generate a new set of SSH keys, follow the instructions in [Create SSH keys](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys#create_an_ssh_key_pair) in the Compute Engine documentation.

  2. Verify that the temporary VM and the admin workstation are in a `Powered Off` state.

  3. Within vSphere, attach the boot disk of the admin workstation to the temporary VM.

The boot disk has the label `Hard disk 1`.

  4. Mount the boot disk inside the VM by running the following commands:
         
         sudo mkdir -p /mnt/boot-disk
         sudo mount DISK_ID /mnt/boot-disk
         

Replace `DISK_ID` with your boot disk identifier, which should have a format similar to `dev/sdc1`.

  5. Edit the `authorized_keys` file on the boot disk to append the contents of the **public key** file generated in the first step:
         
         vi /mnt/boot-disk/.ssh/authorized_keys
         

  6. Shut down the temporary VM.

  7. Power on the admin workstation.

  8. Use the newly generated **private key** to access the admin workstation.
         
         ssh -i ~/.ssh/new-admin-ws.key ubuntu@"${ADMIN_WS_IP}"
         




Use the newly generated private key to continue accessing your admin workstation.

## What's next

[Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
