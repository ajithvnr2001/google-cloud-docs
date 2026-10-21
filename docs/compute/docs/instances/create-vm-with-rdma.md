---
url: https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma/
title: Create an instance that uses Cloud RDMA \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:58.095985+00:00
---

# Create an instance that uses Cloud RDMA  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance that uses Cloud RDMA Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create compute instances with [Cloud RDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma) (`IRDMA`) network interfaces for low-latency, high-throughput communication between instances.

Creating a Cloud RDMA-enabled instance involves the following steps:

  1. Create a compact placement policy.
  2. Create the Virtual Private Cloud networks, including a standard VPC network (`GVNIC` or `IDPF`) and a Falcon VPC network (`IRDMA`).
  3. Create the instance with the network interfaces and placement policy.



For instructions on creating accelerator-optimized instances (such as A4X Max, A4X, A4, or A3 Ultra) that use RDMA, see [Create an AI-optimized instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create an instance that supports Cloud RDMA, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create an instance that supports Cloud RDMA. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create an instance that supports Cloud RDMA:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Requirements

Review the following rules for configuring a network interface for an instance:

  * To configure an IRDMA network interface, you must first create a VPC network with the Falcon RDMA network profile in the same region and zone as the instance.
  * For the gVNIC or IDPF network interface, you must use a regular VPC. If you don't specify a network or subnet, Compute Engine uses the default VPC network and the auto subnet that's in the same region as the instance.
  * If you specify a subnet but don't specify a network, Compute Engine infers the network from the subnet specified.
  * If you specify a network, then you must specify a subnet and it must belong to the same network. Otherwise, instance creation fails.



## Limitations

  * You can't use live migration with virtual machines (VMs) that use Cloud RDMA. You must configure the instance to terminate during maintenance events.
  * You can't use Cloud RDMA with managed instance groups (MIGs) (managed or unmanaged).
  * You can use only `IPv4_ONLY` network stack types with a Cloud RDMA-enabled instance.
  * You can use only machine series that support Cloud RDMA, such as the [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) or the [Z4M machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series).
  * The instance must use an [OS image that supports IRDMA](https://docs.cloud.google.com/compute/docs/images/os-details#networking).



## Create a Cloud RDMA-enabled instance

Instances that use Cloud RDMA require at least two virtual network interfaces (vNICs) per physical NIC, configured from the following network interface types:

  * Network interface type `GVNIC`: VMs use the `gve` driver for TCP/IP and Internet traffic for normal VM to VM and VM to Internet communication
  * Network interface type `IDPF`: bare metal instances use an IDPF network interface type instead of `GVNIC` for normal instance to instance and instance to Internet communication.
  * Network interface type `IRDMA`: uses IDPF/iRDMA drivers for RDMA-based communication between compute instances. This interface must use a [Falcon RDMA network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).



The number of network interfaces of each type that you can configure for an instance depends on the machine series, as explained in the following table:

Machine series | Network interface types | Number to configure  
---|---|---  
H4D | GVNIC only | GVNIC: 1 to 10  
H4D | GVNIC and IRDMA | GVNIC: 1 to 9  
IRDMA: 1  
Z4M VMs | GVNIC only | GVNIC: 1 to 10  
Z4M VMs (< 192 vCPUs) | GVNIC and IRDMA | GVNIC: 1 to 9  
IRDMA: 1  
Z4M VMs (192 vCPUs) | GVNIC and IRDMA | GVNIC: 1 to 9  
IRDMA: 1 to 2  
Z4M (bare metal) | IDPF only | IDPF: 1 to 2  
Z4M (bare metal) | IDPF and IRDMA | 1 IDPF and 1 IRDMA or   
2 IDPF and 1 or 2 IRDMA  
  
The number of IRDMA network interfaces for bare metal instances can't exceed the number of IDPF network interfaces. Also, for multi-NIC instances, to correctly assign the network interface types to each physical NIC, you must define a GVNIC or IDPF interface before each IRDMA interface. The following examples describe possible configurations:

  * A multi-NIC VM with 1 IRDMA network interface and 4 GVNIC network interfaces: Configure the network interfaces in this order: GVNIC, IRDMA, GVNIC, GVNIC, GVNIC. This results in the following assignments: 
    * NIC 0: GVNIC, IRDMA, GVNIC
    * NIC 1: GVNIC, GVNIC
  * A multi-NIC VM with 2 IRDMA network interfaces and 5 GVNIC network interfaces: Configure the network interfaces in this order: GVNIC, IRDMA, GVNIC, IRDMA, GVNIC, GVNIC, GVNIC. This results in the following assignments: 
    * NIC 0: GVNIC, IRDMA, GVNIC, GVNIC
    * NIC 1: GVNIC, IRDMA, GVNIC



For an overview of multiple network interfaces in Google Cloud, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

To create an instance that uses IRDMA, complete the steps in the following sections:

  1. Create a placement policy, if a suitable one doesn't exist.

  2. Create a new VPC network, or use an existing Falcon VPC network.

  3. Create a Cloud RDMA-enabled instance that has at least one `GVNIC` or `IDPF` network interface, at least one `IRDMA` network interface, and uses a compact placement policy.




### Create a placement policy for Cloud RDMA instances

Instances that communicate using Cloud RDMA must be located in a single zone, and more stringently within a single cluster fabric. You can create a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) and specify a max distance value to set the minimum compactness within a zone. There is a limit to the number of instances you can assign the compact placement policy to when you specify a max distance value, and the limit changes depending on what value you choose.

  * To create a compact placement policy to use with your Cloud RDMA instances, follow the steps in [Create a compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy) and specify a maximum distance value of 3 or lower.



### Create Virtual Private Cloud networks

To set up the networks, you can either follow the documented instructions or use the provided script.

###  Instruction guides 

To create the networks, you can use the following instructions:

  * To create the host networks for the `GVNIC` or `IDPF` network interfaces, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

If you are configuring only one `GVNIC` or `IDPF` network interface, you can use the default VPC network and the auto subnet that's in the same region as the instance.

  * To create a network for the `IRDMA` network interface, see [Create a VPC network for RDMA NICs](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma) and use a [Falcon RDMA network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles). Set the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to `8896` for the Falcon VPC network.




###  Script 

To create the networks, you can use the following script.

  1. Optional: Before running the script, list the Falcon RDMA network profiles to verify they are available.
         
         gcloud compute network-profiles list --filter=falcon
         

  2. Copy the following code and run it in a Linux shell window.



    
    
    #!/bin/bash
    
    # Create standard VPC (network and subnet) for the GVNIC or IDPF interface
      gcloud compute networks create GVNIC_NAME_PREFIX-net-0 \
        --subnet-mode=custom
    
      gcloud compute networks subnets create GVNIC_NAME_PREFIX-sub-0 \
        --network=GVNIC_NAME_PREFIX-net-0 \
        --region=REGION \
        --range=10.0.0.0/16
    
      gcloud compute firewall-rules create GVNIC_NAME_PREFIX-internal-0 \
        --network=GVNIC_NAME_PREFIX-net-0 \
        --action=ALLOW \
        --rules=tcp:0-65535,udp:0-65535,icmp \
        --source-ranges=10.0.0.0/8
    
    # Create SSH firewall rules
    gcloud compute firewall-rules create GVNIC_NAME_PREFIX-ssh \
      --network=GVNIC_NAME_PREFIX-net-0 \
      --action=ALLOW \
      --rules=tcp:22 \
      --source-ranges=IP_RANGE
    
    # Optional: Create an external IP for only the GVNIC or IDPF interface
    gcloud compute firewall-rules create GVNIC_NAME_PREFIX-allow-ping-net-0 \
      --network=GVNIC_NAME_PREFIX-net-0 \
      --action=ALLOW \
      --rules=icmp \
      --source-ranges=IP_RANGE
    
    # Create network for Cloud RDMA over Falcon transport
    gcloud compute networks create RDMA_NAME_PREFIX-irdma \
      --network-profile=ZONE-vpc-falcon \
      --subnet-mode custom
    
    # Create subnet for Cloud RDMA
    gcloud compute networks subnets create RDMA_NAME_PREFIX-irdma-sub \
        --network=RDMA_NAME_PREFIX-irdma \
        --region=REGION \
        --range=10.1.0.0/16  # offset to avoid overlap with GVNIC or IDPF network
    

Replace the following:

  * `GVNIC_NAME_PREFIX`: the name prefix to use for the regular Virtual Private Cloud network and subnet that uses a GVNIC or IDPF NIC type.
  * `RDMA_NAME_PREFIX`: the name prefix to use for the Virtual Private Cloud network and subnet that uses the IRDMA NIC type.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where you want to create the networks and compute instances. Use either `us-central1-a` or `europe-west4-b`.
  * `REGION`: the region where you want to create the networks. This must correspond to the zone specified. For example, if your zone is `europe-west4-b`, then your region is `europe-west4`.
  * `IP_RANGE`: the range of IP addresses outside of the VPC network to use for the [SSH firewall rules](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access#use-firewall-policies). As a best practice, specify the specific IP address ranges that you need to allow access from, rather than all IPv4 or IPv6 sources. Don't use `0.0.0.0/0` or `::/0` as a source range because this allows traffic from all IPv4 or IPv6 sources, including sources outside of Google Cloud.



### Create a Cloud RDMA-enabled instance

The following steps show how to create an instance with the first network interface configured as a gVNIC or IDPF interface, and the second network interface configured as an IRDMA network interface:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**.

The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. Optional: In the **Zone** field, select a zone for this instance.

Choose the zone that you used to set up the Falcon VPC network.

     3. Choose a supported machine family and machine series.

     4. In the **Machine type** section, select the machine type for your instance.

  3. In the left-side navigation menu, click **OS and Storage**. In the **Operating system and storage** pane that appears, do the following:

     1. At the bottom of the **Operating system & Storage** section, click **Change**.
     2. In the **Operating system** and **Version** lists, select an OS type and version that offers Cloud RDMA support.
     3. Make sure the **Boot disk typ** e is set to Hyperdisk Balanced.
     4. Click **Select** at the bottom of the pane to save the changes.
  4. In the left-side navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. Go to the **Network interfaces** section. There should already be one network interface, labeled `default`.
     2. Click **Add a network interface**. In the **New network interface** section that appears, do the following: 
        1. In the **Network interface card** list, select `IRDMA`.
        2. In the **Network** field, select the Falcon VPC network.
        3. Optional: In the **Subnetwork** list, select the subnet for the instance to use.
        4. In the **IP stack type** field, make sure it is set to **IPV4-only**.
        5. In the **External IPv4 address** list, select **None**.
        6. To confirm the network interface details, click **Done**.
  5. Optional: Specify other configuration options for the instance. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new_instance_configuration_options).

  6. To create and start the instance, click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with at least two `--network-interface` flags, one for the GVNIC or IDPF interface and one for the IRDMA interface. You can customize the rest of the command options, as needed.

**Note:** The gVNIC or IDPF network interface can have only one IPv6 address, either internal or external, but not both. The IRDMA network interface can only use IPv4 addresses.
         
         gcloud compute instances create INSTANCE_NAME \
             --zone=ZONE \
             --machine-type=MACHINE_TYPE \
             --create-disk=boot=yes, \
                 image=projects/IMAGE_PROJECT/global/images/IMAGE, \
                 size=SIZE \
             --maintenance-policy=TERMINATE \
             --network-interface \
                 nic-type=GVNIC, \
                 network=NETWORK_NAME,subnet=SUBNET_NAME, \
                 stack-type=STACK_TYPE, \
                 private-network-ip=INTERNAL_IPV4_ADDRESS, \
                 address=EXTERNAL_IPV4_ADDRESS \
             --network-interface \
                 nic-type=IRDMA, \
                 network=RDMA_NETWORK_NAME,subnet=RDMA_SUBNET_NAME, \
                 stack-type=IPV4_ONLY, \
                 no-address \
         

Replace the following:

     * `INSTANCE_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the compute instance
     * `ZONE`: the zone where the instance is created, such as `europe-west1-b`. The instance's region is inferred from the zone.
     * `MACHINE_TYPE`: a supported machine type to use for the instance.
     * `IMAGE_PROJECT`: Optional: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image.
     * `IMAGE`: Optional: specify one of the following: 
       * A specific version of the OS image—for example, `hpc-rocky-linux-8-v20250721`.
       * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/hpc-rocky-linux-8`, then Compute Engine creates an instance using the latest version of the OS image in the HPC Rocky Linux 8 image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
     * `SIZE`: Optional: the size of the new disk. The value must be a whole number. The default unit of measurement is GiB.
     * `NETWORK_NAME`: Optional: name of the network
     * `SUBNET_NAME`: name of the subnet to use for the network interface. To view a list of subnets in the network, use the [`gcloud compute networks subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list).

For the GVNIC or IDPF network interface, you can omit the `network` and `subnet` flags and use the `default` network instead.

     * `STACK_TYPE`: Optional: the stack type for the GVNIC or IDPF network interface. `STACK_TYPE` must be one of: `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY`. The default value is `IPV4_ONLY`.

     * `INTERNAL_IPV4_ADDRESS`: Optional: the internal IPv4 address that you want the compute instance to use in the target subnet. Omit this flag if you don't need a specific IP address.

To specify an internal IPv6 address, use the flag `--internal-ipv6-address` instead.

     * `EXTERNAL_IPV4_ADDRESS`: Optional: the static external IPv4 address to use with the network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Do one of the following:

       * Specify a valid IPv4 address from the subnet.
       * Use the flag `no-address` instead if you don't want the network interface to have an external IP address.
       * Specify `address=''` if you want the interface to receive an ephemeral external IP address.

To specify an external IPv6 address, use the flag `--external-ipv6-address` instead.

     * `RDMA_NETWORK_NAME`: The name of the VPC network that you created with a Falcon RDMA network profile.

     * `RDMA_SUBNET_NAME`: The name of a subnet in the Falcon VPC network.




###  REST 

To create an instance configured to use Cloud RDMA, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). Include the `networkInterfaces` object with at least two network configurations, one for the gVNIC or IDPF interface and one for the IRDMA interface. You can customize the rest of the instance properties, as needed.

**Note:** The gVNIC or IDPF network interface can have only one IPv6 address, either internal or external, but not both. The IRDMA network interface can only use IPv4 addresses.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: ID of the project to create the instance in
  * `ZONE`: zone to create the instance in
  * `MACHINE_TYPE`: a supported machine type, for example, `h4d-highmem-192-lssd`
  * `INSTANCE_NAME`: a name for the new instance
  * `IMAGE_PROJECT`: Optional: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image
  * `IMAGE`: Optional: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20250415`
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates an instance using the latest version of the OS image in the Debian 12 image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices). 
  * `NETWORK_NAME`: Optional: name of the network to use with the gVNIC or IDPF network interface
  * `SUBNET_NAME`: name of the subnet to use with the gVNIC or IDPF network interface

For the GVNIC or IDPF network interface, you can omit the `network` and `subnet` properties and use the `default` network instead.

  * `INTERNAL_IPV4_ADDRESS`: Optional: the internal IPv4 address that you want the compute instance to use in the target subnet. Omit this flag if you don't need a specific IP address.
  * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). 
  * `RDMA_NETWORK_NAME`: the name of the network that you created with a RDMA network profile
  * `RDMA_SUBNET_NAME`: the name of a subnet in the RDMA network



HTTP method and URL: 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances

Request JSON body: 
    
    
    {
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        "name": "INSTANCE_NAME",
        "disks": [
          {
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            },
            "boot": true
          }
        ],
        "networkInterfaces": [
          {
            "network": "NETWORK_NAME",
            "subnetwork": "SUBNET_NAME",
            "networkIP": "INTERNAL_IPV4_ADDRESS",
            "accessConfigs": [
              {
                "type": "ONE_TO_ONE_NAT",
                "name": "External IP",
                "natIP": "EXTERNAL_IPV4_ADDRESS"
              }
            ],
            "stackType": "IPV4_ONLY",
            "nicType": "GVNIC",
          },
          {
            "network": "RDMA_NETWORK_NAME",
            "subnetwork": "RDMA_SUBNET_NAME",
            "stackType": "IPV4_ONLY",
            "nicType": "IRDMA",
          }
        ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "compute#operation",
      "id": "9216044482154695709",
      "name": "operation-1739207409646-62dccc7d7bc58-d1350b42-64fdb7f7",
      "zone": "https://www.googleapis.com/compute/v1/projects/`PROJECT_ID`/zones/`ZONE`",
      "operationType": "insert",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/`PROJECT_ID`/zones/`ZONE`/instances/`INSTANCE_NAME`",
      "targetId": "2679381553616227357",
      "status": "RUNNING",
      "user": "USER_ID",
      "progress": 0,
      "insertTime": "2025-02-10T09:10:10.551-08:00",
      "startTime": "2025-02-10T09:10:10.551-08:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/`PROJECT_ID`/zones/`ZONE`/operations/operation-1565289606387-58f9f62f5989c-e582f586-6d22f38"
     "kind": "compute#operation"
    }
    

## What's next?

  * Learn how to [check the status of an instance](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle) to see when it is ready to use.
  * Learn how to [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  * Learn about the [IP addresses](https://docs.cloud.google.com/compute/docs/networking/network-overview#ip-addresses) that are assigned when you create an instance.
  * Learn how to [create a dual-stack or IPv6-only instance](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
