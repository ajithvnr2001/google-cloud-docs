---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-basic/
title: Create basic clusters \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:31.341872+00:00
---

# Create basic clusters  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-basic/

**Version 1.11**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.11 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/overview)



Send feedback 

#  Create basic clusters Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.11 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/minimal-create-clusters)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/minimal-create-clusters)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create basic clusters for a small proof-of-concept installation of Google Distributed Cloud.

These are the primary steps:

  1. Create an admin workstation.

  2. From your admin workstation, create an admin cluster.

  3. From your admin workstation, create a user cluster.




## Before you begin

Set up your vSphere and Google Cloud environments as described in [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure).

## Gather information

To prepare for filling in an admin workstation configuration file, gather the following information:

  * The username and password of your vCenter account

  * Your [vCenter Server address](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/vcenter-server-address)

  * The [root CA certificate](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/vcenter-ca-cert-path) for your vCenter Server

  * The name of your [vSphere data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html)

  * The name of your [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html)

  * The name of your [vSphere datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html)

  * The name of your [vSphere network](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-35B40B0B-0C13-43B2-BC85-18C9C91BE2D4.html)

  * The IP addresses described in [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure#plan-ip-addresses)

  * The ID of your [Google Cloud project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure#cloud-resources)

  * The path of the JSON key file for your [component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure#cloud-resources)




## Log in

The `gkeadm` command-line tool uses your SDK `account` [property](https://docs.cloud.google.com/sdk/docs/properties) to create service accounts. So it is important that you set your SDK `account` property before you run `gkeadm` to create an admin workstation.

Log in with any Google Account. This sets your SDK `account` property:
    
    
    gcloud auth login
    

Verify that your SDK `account` property is set correctly:
    
    
    gcloud config list
    

The output shows the value of your SDK `account` property. For example:
    
    
    [core]
    account = my-name@google.com
    disable_usage_reporting = False
    Your active configuration is: [default]
    

## Grant roles to your SDK account

The Google Account that is set as your SDK `account` property must have these [IAM roles](https://docs.cloud.google.com/iam/docs/overview) so that `gkeadm` can create and manage service accounts for you:

  * `resourcemanager.projectIamAdmin`
  * `serviceusage.serviceUsageAdmin`
  * `iam.serviceAccountCreator`
  * `iam.serviceAccountKeyAdmin`



To grant roles, you must have certain permissions on your Google Cloud project. For details, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If you have the required permissions, you can grant the roles yourself. Otherwise, someone else in your organization must grant the roles for you.

To grant the roles:

### Linux and macOS
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/resourcemanager.projectIamAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:ACCOUNT" \
        --role="roles/serviceusage.serviceUsageAdmin"
    
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
        --role="roles/serviceusage.serviceUsageAdmin"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountCreator"
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="user:ACCOUNT" ^
        --role="roles/iam.serviceAccountKeyAdmin"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `ACCOUNT`: the value of your SDK `account` property



## Create an admin workstation.

The steps in this section use the `gkeadm` command-line tool, which is available for 64-bit Linux, Windows 10, Windows Server 2019, and macOS 10.15 and higher.

[Download `gkeadm`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/download-gkeadm) to your current directory.

### Generate templates
    
    
    ./gkeadm create config
    

The preceding command created these files in your current directory:

  * `credential.yaml`
  * `admin-ws-config.yaml`



### Fill in `credential.yaml`

In `credential.yaml`, fill in your vCenter username and password. For example:
    
    
    kind: CredentialFile
    items:
    - name: vCenter
      username: "my-account-name"
      password: "AadmpqGPqq!a"
    

### Familiarize yourself with the admin workstation configuration file

Scan the documentation for the [admin workstation configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file) to get a general sense of what's in the file. You might want to keep the page open in a separate tab or window so you can refer to it as you fill in values for the fields.

### Fill in `admin-ws-config.yaml`

Open `admin-ws-config.yaml` for editing.

The following fields are filled in for you with default or generated values:
    
    
    vCenter:
      credentials:
        fileRef:
          credentials:
          entry:
    
    adminWorkstation:
      name:
      cpus:
      memoryMB:
      diskGB:
      dataDiskName:
      dataDiskMB:
    
    ntpServer:
    

Fill in the [gcp.componentAccessServiceAccountKeyPath](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file#gcpcomponentaccessserviceaccountkeypath) field.

Fill in the following fields in the [vCenter](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file#vcenter-section) section.
    
    
    credentials:
      address:
    datacenter:
    datastore:
    cluster:
    network:
    caCertPath:
    

Set [vCenter.resourcePool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file#vcenterresourcepool) to CLUSTER_NAME/Resources. Replace CLUSTER_NAME with the name of your vSphere cluster.

If necessary, fill in the [proxyURL](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file#proxyurl-field) field.

If necessary, fill in the [adminWorkstation.proxyURL](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file#adminworkstationproxyurl) field.

Set [adminWorkstation.network.ipAllocationMode](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file#adminworkstationnetworkipallocationmode) to `"static"`.

Fill in the following fields in the [adminWorkstation.network.hostConfig](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-workstation-configuration-file#adminworkstationnetworkhostconfig) section:
    
    
    ip:
    gateway:
    netmask:
    dns:
    

### Example admin workstation configuration file

Here's an example of a filled-in admin workstation configuration file:
    
    
    gcp:
      componentAccessServiceAccountKeyPath: "/usr/local/google/home/me/keys/component-access-key.json"
    vCenter:
      credentials:
        address: "vc01.example"
        fileRef:
          path: "credential.yaml"
          entry: "vCenter"
      datacenter: "vc01"
      datastore: "vc01-datastore-1"
      cluster: "vc01-workloads-1"
      network: "vc01-net-1"
      resourcePool: "vc01-workloads-1/Resources"
      caCertPath: "/usr/local/google/home/stevepe/certs/vc01-cert.pem"
    proxyUrl: ""
    adminWorkstation:
      name: gke-admin-ws-220304-014925
      cpus: 4
      memoryMB: 8192
      diskGB: 50
      dataDiskName: gke-on-prem-admin-workstation-data-disk/gke-admin-ws-220304-014925-data-disk.vmdk
      dataDiskMB: 512
      network:
        ipAllocationMode: "static"
        hostConfig:
          ip: "172.16.20.49"
          gateway: "172.16.20.1"
          netmask: "255.255.255.0"
          dns:
          - "203.0.113.1"
      proxyUrl: ""
      ntpServer: ntp.ubuntu.com
    

### Create your admin workstation

Create your admin workstation, and automatically create service accounts:
    
    
    ./gkeadm create admin-workstation --auto-create-service-accounts
    

The output gives detailed information about the creation of your admin workstation and provides a command that you can use to get an SSH connection to your admin workstation:
    
    
    ...
    Admin workstation is ready to use.
    Admin workstation information saved to /usr/local/google/home/me/my-admin-workstation
    This file is required for future upgrades
    SSH into the admin workstation with the following command:
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.20.49
    ********************************************************************
    

For more detailed information about creating an admin workstation, see [Create an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/create-admin-workstation).

## View the files on your admin workstation

Use the command displayed in the preceding output to get an SSH connection to your admin workstation. For example:
    
    
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.20.49
    

List the files in the home directory:
    
    
    ls -1
    

The output includes the JSON key files for two service accounts that `gkeadm` created for you: a connect-register service account and a logging-monitoring service account. Make a note of the name of the JSON key files for your connect-register service account. You will need it later when you create your clusters. For example:
    
    
    admin-cluster.yaml
    admin-ws-config.yaml
    sa-key.json
    connect-register-sa-2203040617.json
    credential.yaml
    log-mon-sa-2203040617.json
    logs
    vc01-cert.pem
    user-cluster.yaml
    

## Create an admin cluster

Get an SSH connection to your admin workstation.

**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal nameserver in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).

### Specify static IP addresses for your admin cluster

To specify the static IP addresses that you want to use for your admin cluster nodes, create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/ip-block-file) named `admin-cluster-ipblock.yaml`.

You need five IP addresses for the following nodes in your admin cluster:

  * Three nodes to run the admin cluster control plane and add-ons

  * An additional node to be used temporarily during upgrades

  * One node to run the control plane for the user cluster that you will create later




Here is an example of an IP block file that has addresses for five nodes:
    
    
    blocks:
      - netmask: 255.255.255.0
        gateway: 172.16.20.1
        ips:
        - ip: 172.16.20.50
          hostname: admin-vm-1
        - ip: 172.16.20.51
          hostname: admin-vm-2
        - ip: 172.16.20.52
          hostname: admin-vm-3
        - ip: 172.16.20.53
          hostname: admin-vm-4
        - ip: 172.16.20.54
          hostname: admin-vm-5

The `ips` field is an array of IP addresses and hostnames. These are the IP addresses and hostnames that Google Distributed Cloud will assign to your admin cluster nodes.

In the IP block file, you also specify a subnet mask and a default gateway for the admin cluster nodes.

### Familiarize yourself with the admin cluster configuration file

Scan the documentation for the [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file) to get a general sense of what's in the file. You might want to keep the page open in a separate tab or window so you can refer to it as you fill in values for the fields.

### Fill in the admin cluster configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `admin-cluster.yaml`. This configuration file is for creating your admin cluster.

Open `admin-cluster.yaml` for editing. Several fields in your admin cluster configuration file are already filled in with default values, generated values, or values that you provided when you created your admin workstation. You can leave those fields unchanged.

Fill in the [vCenter.dataDisk](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#vcenter-datadisk-field) field.

Fill in the following fields in the [network.hostConfig](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#network-hostconfig-section) section:
    
    
    dnsServers:
    ntpServers:
    

Set [network.ipMode.type](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#network-ipmode-type-field) to `"static"`.

Set [network.ipMode.ipBlockFilePath](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#network-ipmode.ipblockfilepath-field) to `"admin-cluster-ipblock.yaml"`

Fill in or keep the [default values](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure#ip-addresses-pods-services) for [network.serviceCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#network-servicecidr-field) and [network.podCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#network-podcidr-field).

Fill in the following fields in the [loadBalancer.vips](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) section:
    
    
    controlPlaneVIP:
    addonsVIP:
    

Set [loadBalancer.kind](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#loadbalancerkind) to `"MetalLB"`.

Set [antiAffinityGroups.enabled](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#antiaffinitygroups-enabled-field) to `false`.

Set [gkeConnect.projectID](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#gkeconnect-projectid-field) to the ID of your Google Cloud project.

Set [gkeConnect.registerServiceAccountKeyPath](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/how-to/anthos/clusters/docs/on-prem/1.11/admin-cluster-configuration-file#gkeconnect-registerserviceaccount-field) to the path of the JSON key file for your connect-register service account.

### Example of an admin cluster configuration file

Here's an example of a filled-in admin cluster configuration file:
    
    
    apiVersion: v1
    kind: AdminCluster
    name: "gke-admin-01"
    bundlePath: "/var/lib/gke/bundles/gke-onprem-vsphere-1.11.0-gke.543-full.tgz"
    vCenter:
      address: "vc01.example"
      datacenter: "vc-01"
      cluster: "vc01-workloads-1"
      resourcePool: "my-cluster/Resources"
      datastore: "vc01-datastore-1"
      caCertPath: "/usr/local/google/home/me/certs/vc01-cert.pem""
      credentials:
        fileRef:
          path: "credential.yaml"
          entry: "vCenter"
      dataDisk: "vc01-admin-disk.vmdk"
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.1"
        - "198.51.100.1"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: "static"
      serviceCIDR: "10.96.232.0/24"
      podCIDR: "192.168.0.0/16"
      vCenter:
        networkName: "vc01-net-1"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.59"
        addonsVIP: "172.16.20.60"
      kind: "MetalLB"
    antiAffinityGroups:
      enabled: false
    componentAccessServiceAccountKeyPath: "sa-key.json"
    gkeConnect:
      projectID: "my-project-123"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
      disableVsphereResourceMetrics: false
    
    

### Validate the admin cluster configuration file

Verify that the your admin cluster configuration file is valid and can be used for cluster creation:
    
    
    gkectl check-config --config admin-cluster.yaml
    

### Prepare your vSphere environment

Run `gkectl prepare` to initialize your vSphere environment:
    
    
    gkectl prepare --config admin-cluster.yaml --skip-validation-all
    

### Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config admin-cluster.yaml
    

### Resume admin cluster creation after a failure

If the admin cluster creation fails or is canceled, you can run the `create` command again:
    
    
    gkectl create admin --config admin-cluster.yaml
    

### Locate the admin cluster kubeconfig file

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

### Verify that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig kubeconfig
    

The output shows the admin cluster nodes. For example:
    
    
    gke-admin-master-hdn4z            Ready    control-plane,master ...
    gke-admin-node-7f46cc8c47-g7w2c   Ready ...
    gke-admin-node-7f46cc8c47-kwlrs   Ready ...
    

## Create a user cluster

You can create a user cluster either in the Google Cloud console or from the command line on your admin workstation.

### Console

This section shows how to create a user cluster configured for the minimal infrastructure with MetalLB as the load balancer.

When you create a user cluster, the Google Cloud console automatically enables the GKE On-Prem API in the Google Cloud project that you select for the cluster creation. The GKE On-Prem API runs in Google Cloud's infrastructure, and the Google Cloud console uses this API to create the cluster in your vSphere data center. To manage your clusters, the GKE-On-Prem API must store metadata about your cluster's state in the Google Cloud region that you specify when creating the cluster. This metadata lets the GKE On-Prem API manage the user cluster lifecycle and doesn't include workload-specific data.

  1. In the Google Cloud console, go to the GKE Enterprise clusters page.

[Go to the GKE Enterprise clusters page](https://console.cloud.google.com/anthos/clusters)

  2. Select the Google Cloud project that you want to create the cluster in. The selected project is also used as the [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet.

  3. Click **Create Cluster**.

  4. In the dialog box, click **On-premises**.

  5. Next to **VMware vSphere** , click **Configure**.

  6. Review the prerequisites, and click **Continue**.




**Cluster basics**

  1. Enter a **Name** for the user cluster.
  2. Under **Admin cluster** , select the admin cluster from the list. If the admin cluster that you want to use isn't displayed, see the troubleshooting section [The admin cluster isn't displayed on the **Cluster basics** drop-down list](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/troubleshoot-user-cluster-create-api).

  3. In the **GCP API Location** field, select the Google Cloud region from the list. In addition to controlling the region where the GKE On-Prem API runs, this setting controls the region in which the following is stored:

     * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * The Cloud Logging and Cloud Monitoring data of system components
     * The Admin Audit log created by Cloud Audit Logs
  4. Select the Google Distributed Cloud version for your user cluster.

  5. Click **Continue** to go to the **Networking** section.




**Networking**

In this section, you specify the IP addresses for your cluster's nodes, Pods, and Services. A user cluster needs to have one IP address for each node and an additional IP address to be used for a temporary node during upgrade of the user cluster. For more information, see [How many IP addresses does a user cluster need?](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/manage-node-ip-addresses#how_many_ip_addresses_does_a_user_cluster_need).

  1. In the **Node IPs** section, select the **IP mode** for the user cluster. Select one of the following:

     * **DHCP** : Choose **DHCP** if you want your cluster nodes to get their IP address from a DHCP server.

     * **Static** : Choose **Static** if you want to provide static IP addresses for your cluster nodes.

  2. If you selected **DHCP** skip to the next step to specify **Service and Pod CIDRs**. For **Static IP mode** , provide the following information:

     1. Enter the IP address of the **Gateway** for the user cluster.
     2. Enter the **Subnet mask** for the user cluster nodes.

     3. In the **IP Addresses** section, enter the IP addresses and optionally, the hostnames for the nodes in the user cluster. You can enter either an individual IP v4 address (such as 192.0.2.1) or a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) block of IPv4 addresses (such as 192.0.2.0/24).

        * If you enter a CIDR block, don't enter a hostname.
        * If you enter an individual IP address, you can optionally enter a hostname. If you don't enter a hostname, Google Distributed Cloud uses the VM's name from vSphere as the hostname.
     4. Click **\+ Add IP Address** as needed to enter more IP addresses.

  3. In the **Service and Pod CIDRs** section, the Google Cloud console provides the following address ranges for your Kubernetes Service and Pod:

     * **Service CIDR** : 10.96.0.0/20
     * **Pod CIDR** : 192.168.0.0/16

If you prefer to enter your own address ranges, see [IP addresses for Pods and Services](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure#ip-addresses-pods-services) for best practices.

  4. If you selected **Static IP mode** , specify the following information in **Host config** section:

     1. Enter the IP addresses of the DNS servers.
     2. Enter the IP addresses of the NTP servers.
     3. Optionally, enter DNS search domains.
  5. Click **Continue** to go to the **Load balancer** section.




**Load balancer**

Configure [MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/bundled-load-balance-metallb) as the load balancer.

  1. In the **Load balancer type** , leave **MetalLB** selected.

  2. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) server of the user cluster. This IP address must be in the same L2 domain as the admin cluster nodes. Don't add this address in the **Address pools** section.

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy. You must add this to an address pool in the **Address pools** section.

  3. In the **Address pools** section, specify an address pool for the ingress VIP.

     1. Click **\+ Add IP Address Range**.
     2. Enter a name for the address pool.
     3. Enter an IP address range in either CIDR notation (ex. 192.0.2.0/26) or range notation (ex. 192.0.2.64-192.0.2.72). The IP addresses in each pool cannot overlap, and must be in the same subnet as the cluster nodes.
     4. Under **Assignment of IP addresses** , select one of the following:

        * **Automatic** : Choose this option if you want the MetalLB controller to automatically assign IP addresses from the address pool to Services of type `LoadBalancer`.
        * **Manual** : Choose this option if you intend to use addresses from the pool to manually specify addresses for Services of type `LoadBalancer`
     5. Click **Avoid buggy IP addresses** if you want the MetalLB controller to not use addresses from the pool that end in .0 or .255. This avoids the problem of buggy consumer devices mistakenly dropping traffic sent to those special IP addresses.

     6. Repeat as needed. When you're finished click **Done**.

  4. Click **Continue**.




**Control Plane**

  1. Review the default values configured for the nodes in the admin cluster that run the control-plane components for your user cluster. The default values are sufficient for the minimal infrastructure, but you can adjust the values as needed.

  2. Click **Continue**.




**Features**

  1. Clear **Enable anti-affinity groups**. When you set up the [minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure), you only created one ESXi host, so you shouldn't enable [anti-affinity groups](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field).

  2. Click **Continue**.




**Node pools**

Your cluster will be created with at least one node pool. A node pool is a template for the groups of nodes created in this cluster. For more information, see [Creating and managing node pools ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/managing-node-pools).

Review the default values configured for the node pool. The default values are sufficient for the minimal infrastructure, but you can adjust the values as needed.

**Verify and Complete**

Click **Verify and Complete** to create the user cluster. It takes 10 minutes or more to create the user cluster. The Google Cloud console displays status messages as it verifies the settings and creates the cluster in your data center.

The operator who creates the user cluster in the Google Cloud console is automatically logged in to the cluster after it is created. Other operators need to follow the steps in [Logging in to a cluster from the Cloud Console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in) to gain access to the cluster.

If an error is encountered verifying the settings, the Google Cloud console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.

For more information about possible errors and how to fix them, see [Troubleshoot user cluster creation in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/troubleshoot-user-cluster-create-api).

**Create the user cluster kubeconfig file**

To access the user cluster in your data center from the command line, you need to get a `kubeconfig` file from the admin cluster. After the Google Cloud console indicates that user cluster status is healthy, run the following command on the admin workstation to save a new `kubeconfig` file for the user cluster locally. Replace the following:

  * CLUSTER_NAME: the name of the newly-created user cluster
  * ADMIN_CLUSTER_KUBECONFIG: the path to the admin cluster `kubeconfig` file
  * USER_CLUSTER_KUBECONFIG: the name of the user cluster `kubeconfig` file that the command outputs


    
    
    kubectl get secret admin \
    --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
    -n CLUSTER_NAME \
    -o=jsonpath='{.data.admin\.conf}' | base64 -d > USER_CLUSTER_KUBECONFIG
    

After the file has been saved, you can begin accessing the user cluster using `kubectl`, for example:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get namespaces
    

### Command line

  1. Get an SSH connection to your admin workstation.

  2. Specify static IPs for your user cluster.

To specify the static IP addresses that you want to use for your user cluster, create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/ip-block-file) named `user-cluster-ipblock.yaml`. You need three IP addresses for your user cluster nodes and an additional address to be used temporarily during upgrades. Here is an example of an IP block file with four addresses:
         
         blocks:
           - netmask: 255.255.255.0
             gateway: 172.16.20.1
             ips:
             - ip: 172.16.20.55
               hostname: user-vm-1
             - ip: 172.16.20.56
               hostname: user-vm-2
             - ip: 172.16.20.57
               hostname: user-vm-3
             - ip: 172.16.20.58
               hostname: user-vm-4
         




**Fill in the user cluster configuration file**

When `gkeadm` created your admin workstation, it generated a configuration file named `user-cluster.yaml`. This configuration file is for creating your user cluster.

  1. Familiarize yourself with the user cluster configuration file.

Scan the documentation for the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file) to get a general sense of what's in the file. You might want to keep the page open in a separate tab or window so you can refer to it as you fill in values for the fields.

  2. Open `user-cluster.yaml` for editing.

Several fields in your user cluster configuration file are already filled in with default values, generated values, or values that you provided when you created your admin workstation. You can leave those fields unchanged.

  3. Set [name](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#name-field) to a name of your choice for the user cluster.




**Fill in fields in the network section**

  1. Enter IP addresses for the following fields in the [network.hostConfig](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#network-hostconfig-section) section:
         
         dnsServers:
         ntpServers:
         

  2. Set [network.ipMode.type](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#network-ipmode-type-field) to `"static"`.

  3. Set [network.ipMode.ipBlockFilePath](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#network-ipmode.ipblockfilepath-field) to `"user-cluster-ipblock.yaml"`

  4. Fill in or keep the [default values](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/minimal-infrastructure#ip-addresses-pods-services) for [network.serviceCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#network-servicecidr-field) and [network.podCIDR](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#network-podcidr-field).




**Fill in fields in the load balancer section**

  1. Fill in the following fields in the [loadBalancer.vips](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) section:
         
         controlPlaneVIP:
         ingressVIP:
         

  2. Set [loadBalancer.kind](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/admin-cluster-configuration-file#loadbalancerkind) to `"MetalLB"`.

  3. Fill in the [loadBalancer.metalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#loadbalancer-metallb-section) section. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11).

  4. For at least one of your node pools, set [enableLoadBalancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#loadbalancer-metallb-section) to `true`. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11).

  5. Set [antiAffinityGroups.enabled](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field) to `false`.




**Example of a user cluster configuration file**

Here's an example of a filled-in user cluster configuration file:
    
    
    apiVersion: v1
    kind: UserCluster
    name: "my-user-cluster"
    gkeOnPremVersion: "1.11.0-gke.543"
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.1"
        - "198.51.100.1"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: "static"
      serviceCIDR: "10.96.0.0/20"
      podCIDR: "192.168.0.0/16"
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.61"
        ingressVIP: "172.16.20.62"
      kind: "MetalLB"
      metalLB:
        addressPools:
        - name: "uc-address-pool"
          addresses:
          - "172.16.20.63-172.16.20.72"
    nodePools:
    - name: "uc-node-pool"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      enableLoadBalancer: true
    antiAffinityGroups:
      enabled: false
    gkeConnect:
      projectID: "my-project-123"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
      disableVsphereResourceMetrics: false
    autoRepair:
      enabled: true
    

**Validate the configuration and create the cluster**

  1. Verify that the your user cluster configuration file is valid and can be used for cluster creation:
         
         gkectl check-config --kubeconfig kubeconfig --config user-cluster.yaml
         

  2. Create the user cluster:
         
         gkectl create cluster --kubeconfig kubeconfig --config user-cluster.yaml
         

Cluster creation takes approximately 30 minutes.




**Locate the user cluster kubeconfig file**

The `gkectl create cluster` command creates a kubeconfig file named `USER_CLUSTER_NAME-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

**Verify that your user cluster is running**

Verify that your user cluster is running:
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG
    

Replace USER_CLUSTER_KUBECONFIG with the path of your kubeconfig file.

The output shows the user cluster nodes. For example:
    
    
    my-user-cluster-node-pool-69-d46d77885-7b7tx   Ready ...
    my-user-cluster-node-pool-69-d46d77885-lsvzk   Ready ...
    my-user-cluster-node-pool-69-d46d77885-sswjk   Ready ...
    

## What's next

[Deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/deploy-first-app)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
