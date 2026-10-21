---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-basic/
title: Create basic clusters \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:12.868518+00:00
---

# Create basic clusters  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-basic/

**Version 1.13**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.13 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/overview)



Send feedback 

#  Create basic clusters Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.13 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/minimal-create-clusters)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/minimal-create-clusters)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This is the second part of a guide that walks you through a small proof-of-concept installation of Google Distributed Cloud. The first part is [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure), which shows you how to plan your IP addresses and set up the necessary vSphere and Google Cloud infrastructure for your deployment. This document builds on the setup and planning you did in the previous section and shows you how to create an admin workstation, admin cluster, and user cluster in your vSphere environment. You can then go on to [deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/deploy-first-app).

As with the infrastructure setup of this simple installation, the clusters you set up using this document may not be suitable for your actual production needs and use cases. For much more information, best practices, and instructions for production installations, see the [Installation guides](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/install-overview).

## Before you begin

  * Ensure that you have set up your vSphere and Google Cloud environments as described in [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure).



## Procedure overview

These are the primary steps involved in this setup:

  1. **Make sure you have all the necessary information** that you need to configure Google Distributed Cloud, including your vCenter username and password, and the IP addresses that you prepared in the previous section.
  2. **Log in to the Google Cloud CLI** with an account that has the necessary permissions to create service accounts.
  3. **Create an admin workstation** with the resources and tools you need to create admin and user clusters, including the additional service accounts you need to finish the setup.
  4. **Create an admin cluster** to host the Kubernetes control plane for your admin and user clusters, and to manage and update user clusters.
  5. **Create a user cluster** that can run actual workloads.



## Gather information

Before you start filling in Google Distributed Cloud configuration files, ensure you have all the necessary information that you prepared in [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure). You will need all the following values to configure Google Distributed Cloud and complete this setup.

#### vCenter details

  * The username and password of your vCenter account

  * Your [vCenter Server address](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/vcenter-server-address)

  * The [root CA certificate](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/vcenter-ca-cert-path) for your vCenter Server

  * The name of your [vSphere data center](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html)

  * The name of your [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html)

  * The name of your [vSphere datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html)

  * The name of your [vSphere network](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-35B40B0B-0C13-43B2-BC85-18C9C91BE2D4.html)




#### IP addresses

Ensure that you have all the IP addresses that you chose in [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#plan-ip-addresses), including:

  * One IP address for your admin workstation.
  * Ten IP addresses for your admin and user cluster nodes, including addresses for two extra nodes that can be used during cluster upgrades.
  * A virtual IP address (VIP) for the admin cluster Kubernetes API server.
  * A VIP for the user cluster Kubernetes API server.
  * An Ingress VIP for the user cluster.
  * Ten Service VIPs for the user cluster.
  * A CIDR range for user cluster Pods and Services if you need to use non-default ranges as described in [Avoid overlap](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#avoid_overlap).



You also need:

  * The IP address of a DNS server.
  * The IP address of an NTP server.
  * The IP address of the default gateway for the subnet that has your admin workstation and cluster nodes.



#### Google Cloud details

  * The ID of your chosen [Cloud project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#cloud-resources)

  * The path of the JSON key file for the [component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#cloud-resources) that you set up in the previous section.




## Log in to the Google Cloud CLI

Setting up Google Distributed Cloud requires multiple [service accounts](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-basic/) with different permissions. While you must [create your component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#set_up_your_component_access_service_account) manually, the `gkeadm` command line tool can create and configure default versions of the remaining accounts for you as part of creating the admin workstation. To do this, however, you must be logged in to the Google Cloud CLI with an account that has the necessary permissions to create and configure service accounts, as `gkeadm` uses your current gcloud CLI `account` [property](https://docs.cloud.google.com/sdk/docs/properties) when doing this setup.

  1. Log in to the gcloud CLI. You can use any Google account but it must have the [required permissions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#required_permissions). If you have followed the previous part of this guide you have probably already logged in with an appropriate account to create your component access service account.
         
         gcloud auth login
         

  2. Verify that your gcloud CLI `account` property is set correctly:
         
         gcloud config list
         

The output shows the value of your SDK `account` property. For example:
         
         [core]
         account = my-name@google.com
         disable_usage_reporting = False
         Your active configuration is: [default]
         




## Create an admin workstation.

Before you can create any clusters, you need to set up and then SSH into an admin workstation. The admin workstation is a standalone VM with the tools and resources you need to create GKE Enterprise clusters in your vSphere environment. The steps in this section use the `gkeadm` command-line tool, which is available for 64-bit Linux, Windows 10, Windows Server 2019, and macOS 10.15 and higher.

  * [Download `gkeadm`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/download-gkeadm) to your current directory.



### Generate templates

Run the following command to generate template configuration files:
    
    
    ./gkeadm create config
    

Running this command generates the following template configuration files in your current directory:

  * `credential.yaml`, which you use to provide your vCenter login details
  * `admin-ws-config.yaml`, which you use to provide your admin workstation configuration settings 



### Fill in your credentials file

In `credential.yaml`, fill in your vCenter username and password. For example:
    
    
    kind: CredentialFile
    items:
    - name: vCenter
      username: "my-account-name"
      password: "AadmpqGPqq!a"
    

### Fill in the admin workstation configuration file

Open `admin-ws-config.yaml` for editing. When completed, this file contains all the information `gkeadm` needs to create an admin workstation for this basic installation. Some of the fields are already filled in for you with default or generated values: do not change these values for this simple installation.

Fill in the remaining fields as follows, using the information you gathered earlier. You can see a complete example configuration file below if you are unsure about how to format any fields, or see the [admin workstation configuration file reference](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-workstation-configuration-file). You might want to keep the page open in a separate tab or window so you can refer to it as you fill in values for the fields.

Field or section | Instructions  
---|---  
`gcp.componentAccessServiceAccountKeyPath` | The path of the [JSON key file you created](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#set_up_your_component_access_service_account) for your component access service account.  
`vCenter.credentials.address` | The IP address or hostname of your vCenter server.   
`vCenter.datacenter` | The name of your vCenter datacenter.  
`vCenter.datastore` | The name of your vCenter datastore.  
`vCenter.cluster` | The name of your vCenter cluster.  
`vCenter.network` | The name of the vCenter network where you want to create the admin workstation.  
`vCenter.resourcePool` | Set this field to `"CLUSTER_NAME/Resources"`, replacing CLUSTER_NAME with the name of your vSphere cluster.  
`vCenter.caCertPath` | The path to the root CA certificate for your vCenter server.  
`proxyURL` | If the machine you are using to run `gkeadm` needs to use a proxy server for access to the internet, set this field to the URL of the proxy server.  
`adminWorkstation.ipAllocationMode` | Set this field to `"static"`.  
`adminWorkstation.network.hostConfig.ip` | The IP address you [chose earlier](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#example_ip_address_admin_workstation) for your admin workstation.  
`adminWorkstation.network.hostConfig.gateway` | The IP address of the default gateway for the subnet you want to use for your admin workstation and cluster nodes.  
`adminWorkstation.network.hostConfig.netmask` | The netmask for the network that contains your admin workstation.  
`adminWorkstation.network.hostConfig.dns` | IP addresses for DNS servers that your admin workstation can use.  
`adminWorkstation.proxyURL` | If your network is behind a proxy server, and you want both your admin workstation and your clusters to use the same proxy server, set this field to the URL of the proxy server.  
  
#### Example admin workstation configuration file

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

Create your admin workstation using the following command:
    
    
    ./gkeadm create admin-workstation --auto-create-service-accounts
    

Running this command:

  * Creates your admin workstation
  * Automatically creates any additional service accounts you need for your installation
  * Creates template configuration files for your admin and user clusters



The output gives detailed information about the creation of your admin workstation and provides a command that you can use to get an SSH connection to your admin workstation:
    
    
    ...
    Admin workstation is ready to use.
    Admin workstation information saved to /usr/local/google/home/me/my-admin-workstation
    This file is required for future upgrades
    SSH into the admin workstation with the following command:
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.20.49
    ********************************************************************
    

For more detailed information about creating an admin workstation, see [Create an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-admin-workstation).

### Connect to your admin workstation

Use the command displayed in the preceding output to get an SSH connection to your admin workstation. For example:
    
    
    ssh -i /usr/local/google/home/me/.ssh/gke-admin-workstation ubuntu@172.16.20.49
    

### View generated files

On your admin workstation, list the files in the home directory:
    
    
    ls -1
    

The output should include:

  * `admin-cluster.yaml`, a template config file for creating your admin cluster.
  * `user-cluster.yaml`, a template config file for creating your user cluster.
  * JSON key files for two service accounts that `gkeadm` created for you: a connect-register service account and a logging-monitoring service account. Make a note of the name of the JSON key file for your connect-register service account. You will need it later when you create your clusters. 



For example:
    
    
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

Now that you have an admin workstation configured with your vCenter and other details, you can use it to create an admin cluster in your vSphere environment. Ensure you have an SSH connection to your admin workstation, as described above, before starting this step. All of the following commands are run on the admin workstation.

**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal nameserver in [`/etc/resolv.conf`](https://ubuntu.com/server/docs#name-resolution).

### Specify static IP addresses for your admin cluster

To specify the static IP addresses that you [planned earlier](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#ip-addresses-nodes) for your admin cluster nodes, create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/ip-block-file) named `admin-cluster-ipblock.yaml`.

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

### Fill in the admin cluster configuration file

Open `admin-cluster.yaml` for editing. When completed, this file contains all the information `gkectl` needs to create an admin cluster for this basic installation. Some of the fields are already filled in for you with default values, generated values, or values that you provided when configuring your admin workstation such as vCenter details: do not change these values for this simple installation.

Fill in the remaining fields as follows, using the information you gathered earlier. You can see a complete example configuration file below if you are unsure about how to format any fields, or see the [admin cluster configuration file reference](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/admin-cluster-configuration-file). You might want to keep the page open in a separate tab or window so you can refer to it as you fill in values for the fields.

Field or section | Instructions  
---|---  
`vCenter.dataDisk` | The name you want to use for the virtual machine disk (VMDK) that the installer creates to hold Kubernetes object data.  
`network.hostConfig.dnsServers` | IP addresses for DNS servers that your cluster VMs can use.  
`network.hostConfig.ntpServers` | IP addresses for time servers that your cluster VMs can use.  
`network.ipMode.type` | Set this field to `"static"`.   
`network.ipMode.ipBlockFilePath` | The path to the IP block file you created earlier.  
`network.serviceCIDR` and `network.podCIDR` | Only change these values if you need to use non-default ranges, as described in [Avoid overlap](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#avoid_overlap).  
`loadBalancer.vips.controlPlaneVIP` | The virtual IP address (VIP) that you have chosen for the admin cluster's Kubernetes API server.   
`loadbalancer.kind` | Set this field to `"MetalLB"`.  
`antiAffinityGroups` | Set this field to `"false"`  
`gkeConnect.projectID` | Set this field to your [Google project's](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#cloud-resources) project ID.   
`gkeConnect.registerServiceAccountKeyPath` | Set this field to the JSON key of your connect-register service account.   
  
#### Example of an admin cluster configuration file

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
    
    

#### Validate the admin cluster configuration file

Verify that the your admin cluster configuration file is valid and can be used for cluster creation:
    
    
    gkectl check-config --config admin-cluster.yaml
    

### Import OS images to vSphere

Run `gkectl prepare` with your completed config file to import node OS images to vSphere:
    
    
    gkectl prepare --config admin-cluster.yaml --skip-validation-all
    

Running this command imports the images to vSphere and marks them as VM templates, including the image for your admin cluster.

### Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config admin-cluster.yaml
    

#### Resume admin cluster creation after a failure

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

You can create a user cluster for this simple installation either in the Google Cloud console or from the command line on your admin workstation. Currently you can use the Google Cloud console to create user clusters only.

### Console

This approach uses a Google Cloud service called the GKE On-Prem API to create and manage clusters in your vSphere environment. When you create a user cluster from the Google Cloud console, this API is automatically enabled in your chosen fleet host project. You can find out more about how this works in [Create a user cluster in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/create-user-cluster-api). Using this approach also means that as cluster creator you can automatically [log in to your new cluster in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/connecting-to-a-cluster) with your Google identity, although you will need to set authentication up for any other users.

  1. In the Google Cloud console, go to the GKE Enterprise clusters page.

[Go to the GKE Enterprise clusters page](https://console.cloud.google.com/anthos/clusters)

  2. Select the Google Cloud project that you want to create the cluster in. The selected project will also be your [fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project). This must be the same project that the admin cluster is registered to. After the user cluster is created, it is automatically registered to the selected project's fleet.

  3. Click **Create Cluster**.

  4. In the dialog box, click **On-premises**.

  5. Next to **VMware vSphere** , click **Configure**.

  6. Review the prerequisites, and click **Continue**.




**Cluster basics**

  1. Enter a **Name** for the user cluster.
  2. Under **Admin cluster** , select the admin cluster you created earlier from the list. If the admin cluster that you want to use isn't displayed, see the troubleshooting section [The admin cluster isn't displayed on the **Cluster basics** drop-down list](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/troubleshoot-user-cluster-create-api).

  3. In the **GCP API Location** field, select the Google Cloud region from the list. In addition to controlling the region where the GKE On-Prem API runs, this setting controls the region in which the following is stored:

     * The user cluster metadata that the GKE On-Prem API needs to manage the cluster lifecycle
     * Logging, monitoring, and audit data for system components.
  4. Select the Google Distributed Cloud version for your user cluster.

  5. Click **Continue** to go to the **Networking** section.




**Networking**

In this section, you specify the IP addresses for your cluster's nodes, Pods, and Services. For this simple installation your cluster needs an address each for three nodes, and an additional IP address that can be to be used for a temporary node during upgrade of the user cluster.

  1. In the **Node IPs** section, specify **Static** as your cluster's **IP mode**.

  2. Using the addresses you [planned earlier](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#ip-addresses-nodes) for your user cluster nodes, fill in the following information:

     1. Enter the IP address of the **Gateway** for the user cluster.
     2. Enter the **Subnet mask** for the user cluster nodes.
     3. In the **IP Addresses** section, enter the IP addresses and optionally, the hostnames for the worker nodes in the user cluster. You can enter either an individual IP v4 address (such as 192.0.2.1) or a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) block of IPv4 addresses (such as 192.0.2.0/24).

        * If you enter a CIDR block, don't enter a hostname.
        * If you enter an individual IP address, you can optionally enter a hostname. If you don't enter a hostname, Google Distributed Cloud uses the VM's name from vSphere as the hostname.
     4. Click **\+ Add IP Address** as needed to enter more IP addresses.

  3. Leave the default provided values in the **Service and Pod CIDRs** section, unless you need to use non-default ranges as described in [Avoid overlap](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#avoid_overlap).

  4. Specify the following information in **Host config** section:

     1. Enter the IP addresses of DNS servers that your user cluster can use.
     2. Enter the IP addresses of the NTP servers.
  5. Click **Continue** to go to the **Load balancer** section.




**Load balancer**

Configure [MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/bundled-load-balance-metallb) as the load balancer.

  1. In the **Load balancer type** , leave **MetalLB** selected.

  2. In the **Virtual IPs** section, enter the following:

     * **Control plane VIP** : The destination IP address to be used for traffic sent to the [Kubernetes API server](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-configuration-file#loadbalancer-vips-controlplanevip-field) server of the user cluster. This IP address must be in the same L2 domain as the admin cluster nodes. Don't add this address in the **Address pools** section.

     * **Ingress VIP** : The IP address to be configured on the load balancer for the ingress proxy. This must be included in the address pool you specify in the **Address pools** section.

  3. In the **Address pools** section, specify an address pool for the load balancer, including the ingress VIP - these are the Service VIPs that you [planned earlier](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#ip-addresses-vips-user-cluster).

     1. Click **\+ Add IP Address Range**.
     2. Enter a name for the address pool.
     3. Enter the IP address range in either CIDR notation (such as 192.0.2.0/26) or range notation (such as 192.0.2.64-192.0.2.72). The IP addresses in each pool cannot overlap, and must be in the same subnet as the cluster nodes.
     4. Under **Assignment of IP addresses** , select **Automatic**.
     5. When you're finished click **Done**.
  4. Click **Continue**.




**Control Plane**

Use the provided default values in this section. Click **Continue**.

**Features**

  1. Clear **Enable anti-affinity groups**. When you set up the [minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure), you only created one ESXi host, so you shouldn't enable [anti-affinity groups](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-configuration-file#antiaffinitygroups-enabled-field).

  2. Click **Continue**.




**Node pools**

Your cluster must have at least one node pool. A node pool is a template for the groups of nodes created in this cluster. For more information, see [Creating and managing node pools ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/managing-node-pools).

Review the default values configured for the node pool. The default values are sufficient for the minimal infrastructure, but you can adjust the values as needed.

**Verify and Complete**

Click **Verify and Complete** to create the user cluster. It takes 10 minutes or more to create the user cluster. The Google Cloud console displays status messages as it verifies the settings and creates the cluster in your data center.

You are automatically logged in to the cluster after creating it. Other operators need to follow the steps in [Logging in to a cluster from the Cloud Console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in) to gain access to the cluster.

If you encounter an error verifying the settings, the Google Cloud console displays an error message that should be clear enough for you to fix the configuration issue and try again to create the cluster.

For more information about possible errors and how to fix them, see [Troubleshoot user cluster creation in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/troubleshoot-user-cluster-create-api).

**Create the user cluster kubeconfig file**

To access the user cluster in your data center from the command line, you need to get a `kubeconfig` file from the admin cluster. After the Google Cloud console indicates that user cluster status is healthy, run the following command on the admin workstation to save a new `kubeconfig` file for the user cluster locally. Replace the following:

  * CLUSTER_NAME: the name of the newly-created user cluster
  * ADMIN_CLUSTER_KUBECONFIG: the path to the admin cluster `kubeconfig` file
  * USER_CLUSTER_KUBECONFIG: the name of the user cluster `kubeconfig` file that the command outputs


    
    
    kubectl get secret admin \
    --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
    -n CLUSTER_NAME \
    -o=jsonpath='{.data.admin\.conf}' | base64 -d > USER_CLUSTER_KUBECONFIG
    

After the file has been saved, you can begin accessing the user cluster using `kubectl`, as in the following example:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get namespaces
    

### Command line

Ensure you have an SSH connection to your admin workstation, as described above, before starting this procedure. All of the following commands are run on the admin workstation.

**Specify static IPs for your user cluster**

To specify the static IP addresses that you [planned earlier](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#ip-addresses-nodes) for your user cluster nodes, create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/ip-block-file) named `user-cluster-ipblock.yaml`. You need three IP addresses for your user cluster nodes and an additional address to be used temporarily during upgrades. Here is an example of an IP block file with four addresses:
    
    
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

When `gkeadm` created your admin workstation, it generated a configuration file named `user-cluster.yaml`. This configuration file is for creating your user cluster. Some of the fields are already filled in for you with default values, generated values, or values that you provided when configuring your admin workstation such as vCenter details: do not change these values for this simple installation.

  1. Open `user-cluster.yaml` for editing.

  2. Fill in the remaining fields as follows, using the information you gathered earlier. You can see a complete example configuration file below if you are unsure about how to format any fields, or see the [user cluster configuration file reference](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/user-cluster-configuration-file). You might want to keep the page open in a separate tab or window so you can refer to it as you fill in values for the fields.


Field or section | Instructions  
---|---  
`name` | The name of your choice for the user cluster  
`network.hostConfig.dnsServers` | IP addresses for DNS servers that your cluster VMs can use.  
`network.hostConfig.ntpServers` | IP addresses for time servers that your cluster VMs can use.  
`network.ipMode.type` | Set this field to `"static"`.   
`network.ipMode.ipBlockFilePath` | The path to `user-cluster-ipblock.yaml`.  
`network.serviceCIDR` and `network.podCIDR` | Only change these values if you need to use non-default ranges, as described in [Avoid overlap](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#avoid_overlap).  
`loadBalancer.vips.controlPlaneVIP` | The virtual IP address (VIP) that you have chosen for the user cluster's Kubernetes API server.   
`loadBalancer.vips.ingressVIP` | The virtual IP address that you have chosen to be configured on the load balancer for the ingress proxy.   
`loadbalancer.kind` | Set this field to `"MetalLB"`.  
`loadbalancer.metalLB.addressPools` | Specify an address pool for the load balancer - these are the Service VIPs that you [planned earlier](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#ip-addresses-vips-user-cluster). Provide a `name` for the address pool and your chosen `addresses`. The address pool must include the ingress proxy VIP.   
`nodePools` | Use the prepopulated values provided for a single node pool, specifying your chosen `name`. Set `enableLoadBalancer` to `true` for your node pool. This is necessary to use MetalLB because it runs on your cluster nodes.   
`antiAffinityGroups` | Set this field to `"false"`  
`gkeConnect.projectID` | Set this field to your [Google project's](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/minimal-infrastructure#cloud-resources) project ID.   
`gkeConnect.registerServiceAccountKeyPath` | Set this field to the JSON key of your connect-register service account.   
  
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
          - "172.16.20.62-172.16.20.72"
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

You have now completed this minimal installation of Google Distributed Cloud. As an optional follow-up, you can see your installation in action by [deploying an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/deploy-first-app).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
