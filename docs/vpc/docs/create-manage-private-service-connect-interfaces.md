---
url: https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces/
title: Create and manage Private Service Connect interfaces \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:30.781816+00:00
---

# Create and manage Private Service Connect interfaces  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage Private Service Connect interfaces

This page describes how producer network administrators can create and manage Private Service Connect interfaces. Private Service Connect interfaces let service producer Virtual Private Cloud (VPC) networks initiate connections to consumer VPC networks.

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.
  * Find the URL of the [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments) that you want to connect to.
  * If the network attachment is configured to [manually accept connections](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies), ensure that a network administrator has added your project to the network attachment's accept list.



### Roles

To get the permissions that you need to create Private Service Connect interfaces, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The Compute Instance Admin (v1) role contains the `compute.instances.pscInterfaceCreate` permission, which is required to create Private Service Connect interfaces.

## Create VMs with Private Service Connect interfaces

To create a Private Service Connect interface connection, you need a virtual machine (VM) instance that has at least two network interfaces. The first interface connects to a producer subnet. The other interfaces can be Private Service Connect interfaces that request connections to [network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments) in different consumer VPC networks.

If a connection is accepted, Google Cloud assigns to the Private Service Connect interface an internal IP address from the subnet that is specified by the network attachment.

When you create a VM with multiple Private Service Connect interfaces, each interface must connect to:

  * A different network attachment that is associated with a different subnet.
  * A network attachment that is in a different VPC network, unless both of the following are true: 
    * The consumer network uses an [RDMA network profile for Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#falcon-supported-features).
    * The producer connects with [virtual Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#virtual-specifications).

**Caution:** Make sure that the VM connects only to network attachments from a single consumer. [Multi-tenant architectures](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#limitations) can let one consumer take actions that cause a loss of connectivity for other consumers that are connected to the same VM.

If you create a Private Service Connect interface that refers to a network attachment that's configured to [manually accept connections](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies), the following applies:

  * If the network attachment is configured to accept connections based on project ID, your project ID must be included in the consumer accept list.
  * If the network attachment is configured to accept connections based on service class ID, only authorized Google services can connect to it.



If these requirements aren't met, creation of the Private Service Connect interface's VM fails. Work with the consumer organization to add your project ID to the network attachment's accept list or to provide a network attachment that uses project-based authorization. After the authorization is corrected, create a new Private Service Connect interface.

When you create a Private Service Connect interface, you can optionally assign to it one or more internal [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip). If you plan to assign alias IP ranges, contact the consumer organization to determine the appropriate IP address ranges.

To assign an alias IP range, specify the prefix length of the range in CIDR notation. When you assign one or more alias IP ranges to a Private Service Connect interface, Google Cloud allocates the alias IP ranges from the primary IP address range of the subnet that's associated with the network attachment. The Private Service Connect interface's primary IP address is allocated from outside of any alias IP ranges. If there aren't enough IP addresses in the network attachment's subnet to allocate the primary IP address and alias IP ranges, creation of the Private Service Connect interface's VM fails. You can find the specific IP addresses that are assigned by [describing the interface's VM](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#describe).

**Important:** After creating a Private Service Connect interface, you must [configure routing](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces) before traffic can flow through the interface.

###  Console 

**Create a VM instance**

  1. In the Google Cloud console, go to the **VM instances** page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. In the **Name** box, enter a name.

  4. Click **Region** , and then select the region of the network attachment that you want to connect to.

  5. Select a zone.

  6. To configure the VM's default network interface, do the following:

     1. Click **Networking**.
     2. In the **Network interfaces** section, click the first network interface, which is the default network interface.
     3. Select a network.
     4. Select a subnet that is in the same region as the Private Service Connect interface's network attachment.
     5. Select an IP stack type.
  7. Click **Done**.




**Add Private Service Connect interfaces**

You can repeat these steps for each interface that you want to add.

**Add a virtual Private Service Connect interface**

  1. Click **Add a network interface**.
  2. For **Interface type** , select **Private Service Connect**.
  3. In the **Network attachment URL** box, enter the URL of this interface's network attachment.
  4. Select an [IP stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types) for the interface. The network attachment's subnet determines the possible stack types.
  5. Optional: To add an alias IP range, do the following: 
     1. In the **Alias IP ranges** section, click **Add IP range**.
     2. In the **Prefix length** box, enter the prefix length—for example, `/30`. You can add multiple alias IP ranges by clicking **Add IP range** , and then entering the prefix length for each additional alias IP range that you want to add.
  6. Click **Done**.



**Add a dynamic Private Service Connect interface**

  1. Click **Add a dynamic network interface**.
  2. For **Interface type** , select **Private Service Connect**.
  3. Select a parent network interface.
  4. In the **VLAN ID** box, enter a VLAN ID.
  5. In the **Network attachment URL** box, enter the URL of this interface's network attachment.
  6. Select an [IP stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types) for the interface. The network attachment's subnet determines the possible stack types.
  7. Optional: To add an alias IP range, do the following: 
     1. In the **Alias IP ranges** section, click **Add IP range**.
     2. In the **Prefix length** box, enter the prefix length—for example, `/30`. You can add multiple alias IP ranges by clicking **Add IP range** , and then entering the prefix length for each additional alias IP range that you want to add.
  8. Click **Done**.



To create the VM, click **Create**.

###  gcloud 

  * To create a VM with a virtual Private Service Connect interface, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
        
        gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --machine-type=MACHINE_TYPE \
            --image-project=IMAGE_PROJECT \
            --image-family=IMAGE_FAMILY \
            --network-interface='subnet=PRODUCER_SUBNET,no-address' \
            --network-interface='network-attachment=ATTACHMENT_URI,stack-type=STACK_TYPE'
        

Replace the following:

    * `INSTANCE_NAME`: the name of the new instance
    * `ZONE`: the zone of the new instance
    * `MACHINE_TYPE`: the instance's machine type, which can be [predefined](https://docs.cloud.google.com/compute/docs/machine-types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)—for example, `n1-standard-1`
    * `IMAGE_PROJECT`: the project of the image family

For example, if you specify `debian-12` as the image family, specify `debian-cloud` as the image project. You can view a list of available images, image projects, and image families by using the [`gcloud compute images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list).

    * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the instance

This creates the VM with the most recent, non-deprecated OS image in the image family. For example, if you specify `debian-12`, Compute Engine uses the latest version of the OS image in the [Debian 12](https://docs.cloud.google.com/compute/docs/images/os-details#debian) image family.

    * `PRODUCER_SUBNET`: the subnet of the VM's primary network interface

This subnet must be in the same region as the Private Service Connect interface's network attachment.

    * `ATTACHMENT_URI`: the URI of the network attachment—for example: `projects/CONSUMER_PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME`

    * `STACK_TYPE`: the [stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types) of the Private Service Connect interface

To create an interface with an IPv4 address, specify `IPV4_ONLY` (the default). To create an interface that uses both an IPv4 and an IPv6 address (dual-stack), specify `IPV4_IPV6`. For IPv6 only, specify `IPV6_ONLY`.

The interface's stack type must be compatible with the stack type of the network attachment's subnet.

  * To create a VM with a dynamic Private Service Connect interface, use the following command:
        
        gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --machine-type=MACHINE_TYPE \
            --image-project=IMAGE_PROJECT \
            --image-family=IMAGE_FAMILY \
            --network-interface='subnet=PRODUCER_SUBNET,no-address' \
            --network-interface='network-attachment=ATTACHMENT_URI,vlan=VLAN_ID,stack-type=STACK_TYPE'
        

Replace `VLAN_ID` with the VLAN ID of the dynamic Private Service Connect interface, which must be an integer from 2 to 255.

VLAN IDs must be unique for each dynamic interface that shares a parent vNIC. You can reuse the same ID for other dynamic interfaces that are associated with different vNICs.

  * To assign alias IP ranges to a Private Service Connect interface, use the following command:
        
        gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --machine-type=MACHINE_TYPE \
            --image-project=IMAGE_PROJECT \
            --image-family=IMAGE_FAMILY \
            --network-interface='subnet=PRODUCER_SUBNET,no-address' \
            --network-interface='network-attachment=ATTACHMENT_URI,vlan=VLAN_ID,stack-type=STACK_TYPE,aliases=ALIAS_IP_RANGES'
        

Replace `ALIAS_IP_RANGES` with one or more alias IP ranges to assign to the interface. You can enter specific ranges (`192.168.100.0/24`), specific IP addresses (`192.168.100.1`), or prefix lengths in CIDR format (`/24`). You can enter multiple values in a semicolon-separated list. You can't enter multiple values of different types. For example, `192.168.100.0/24;/28` isn't supported.

  * To create a VM with multiple Private Service Connect interfaces, include separate `--network-interface` flags for each interface, where each flag refers to a different network attachment.

For dynamic Private Service Connect interfaces, the parent vNIC is determined by the order of flags in the command. The parent vNIC is the first vNIC that you specify before the dynamic interface.

You can create dynamic and virtual Private Service Connect interfaces that coexist on the same VM. For example, the following command creates a VM with both virtual and dynamic Private Service Connect interfaces.

The parent of the dynamic Private Service Connect interfaces that have VLAN IDs `2` and `3` is the first vNIC, connecting to `producer-subnet`. The parent of the dynamic interface that has VLAN ID `4` is the vNIC that connects to `producer-subnet-2`. The last interface is a virtual Private Service Connect interface.
        
        gcloud compute instances create producer-vm \
            --zone=us-west-1a \
            --network-interface='subnet=producer-subnet,no-address' \
            --network-interface='network-attachment=projects/consumer-project/regions/us-west-1/networkAttachments/consumer-1-network-attachment,vlan=2' \
            --network-interface='network-attachment=projects/consumer-project/regions/us-west-1/networkAttachments/consumer-2-network-attachment,vlan=3' \
            --network-interface='network=producer-vpc-2,subnet=producer-subnet-2' \
            --network-interface='network-attachment=projects/consumer-project/regions/us-west-1/networkAttachments/consumer-3-network-attachment,vlan=4' \
            --network-interface='network-attachment=projects/consumer-project/regions/us-west-1/networkAttachments/consumer-4-network-attachment'
        




###  API 

  * To create a VM with a virtual Private Service Connect interface, send a request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

HTTP method and URL:
        
        POST https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/zones/INSTANCE_ZONE/instances
        

Request JSON body:
        
        {
          "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
          "name": "VM_NAME",
          "disks": [
            {
              "initializeParams": {
                "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
              },
              "boot": true
            }
          ],
          "networkInterfaces": [
            {
              "network": "https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/global/networks/PRODUCER_NETWORK",
              "subnetwork": "https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/regions/SUBNET_REGION/subnetworks/PRODUCER_SUBNET"
            },
            {
              "networkAttachment": "ATTACHMENT_URI",
              "stackType": "STACK_TYPE"
            }
          ]
        }
        

Replace the following:

    * `PRODUCER_PROJECT_ID`: the ID of the VM's project
    * `INSTANCE_ZONE`: the zone of the new instance
    * `MACHINE_TYPE_ZONE`: the zone of the machine type
    * `MACHINE_TYPE`: the instance's machine type, which can be [predefined](https://docs.cloud.google.com/compute/docs/machine-types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)—for example, `n1-standard-1`
    * `VM_NAME`: the name of the VM instance
    * `IMAGE_PROJECT`: the project of the image family

For example, if you specify `debian-12` as the image family, specify `debian-cloud` as the image project. You can view a list of available images, image projects, and image families by using the [`gcloud compute images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list).

    * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the instance

This creates the VM with the most recent, non-deprecated OS image in the image family. For example, if you specify `debian-12`, Compute Engine uses the latest version of the OS image in the [Debian 12](https://docs.cloud.google.com/compute/docs/images/os-details#debian) image family.

    * `PRODUCER_NETWORK`: the network of the VM's primary network interface

    * `SUBNET_REGION`: the region of the subnet of the VM's primary network interface

    * `PRODUCER_SUBNET`: the subnet of the VM's primary network interface

This subnet must be in the same region as the Private Service Connect interface's network attachment.

    * `ATTACHMENT_URI`: the URI of the network attachment—for example: `projects/CONSUMER_PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME`

    * `STACK_TYPE`: the [stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types) of the Private Service Connect interface.

To create an interface with an IPv4 address, specify `IPV4_ONLY` (the default). To create an interface that uses both an IPv4 and an IPv6 address (dual-stack), specify `IPV4_IPV6`. For IPv6 only, specify `IPV6_ONLY`.

The interface's stack type must be compatible with the stack type of the network attachment's subnet.

  * To create a VM with a dynamic Private Service Connect interface, send the following request. Include a VLAN ID in the network interface object to specify the creation of a dynamic Private Service Connect interface.

HTTP method and URL:
        
        POST https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/zones/INSTANCE_ZONE/instances
        

Request JSON body:
        
        {
          "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
          "name": "VM_NAME",
          "disks": [
            {
              "initializeParams": {
                "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
              },
              "boot": true
            }
          ],
          "networkInterfaces": [
            {
              "network": "https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/global/networks/PRODUCER_NETWORK",
              "subnetwork": "https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/regions/SUBNET_REGION/subnetworks/PRODUCER_SUBNET"
            },
            {
              "networkAttachment": "ATTACHMENT_URI",
              "vlan": VLAN_ID,
              "stackType": "IPV4_IPV6"
            }
          ]
        }
        

Replace `VLAN_ID` with the VLAN ID of the dynamic Private Service Connect interface, which must be an integer from 2 to 255.

VLAN IDs must be unique for each dynamic interface that shares a parent vNIC. You can reuse the same ID for other dynamic interfaces that are associated with different vNICs.

  * To assign alias IP ranges to a Private Service Connect interface, send the following request. Include the `aliasesIpRanges` field.

HTTP method and URL:
        
        POST https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/zones/INSTANCE_ZONE/instances
        

Request JSON body:
        
        {
          "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
          "name": "VM_NAME",
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
              "network": "https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/global/networks/PRODUCER_NETWORK",
              "subnetwork": "https://compute.googleapis.com/compute/v1/projects/PRODUCER_PROJECT_ID/regions/SUBNET_REGION/subnetworks/PRODUCER_SUBNET"
            },
            {
              "aliasIpRanges": [
                {
                  "ipCidrRange": "ALIAS_IP_RANGE"
                }
              ],
              "networkAttachment": "ATTACHMENT_URI"
            }
          ]
        }
        

Replace `ALIAS_IP_RANGE` with an alias IP ranges to assign to the interface. You can enter a specific range (`192.168.100.0/24`), specific IP address (`192.168.100.1`), or prefix length in CIDR format (`/24`).

You can specify multiple alias IP ranges in the `aliasIpRanges` array. Each range must be specified in the same form:
        
        "aliasIpRanges": [
          {
            "ipCidrRange": "/28"
          },
          {
            "ipCidrRange": "/30"
          }
        ]
        

  * To create a VM with multiple Private Service Connect interfaces, include separate objects in the `networkInterfaces` array for each interface, where each interface object refers to a different network attachment.

For dynamic Private Service Connect interfaces, the parent vNIC is determined by the order of objects in the array. The parent vNIC is the first vNIC that you specify before the dynamic interface.

You can create dynamic and virtual Private Service Connect interfaces that coexist on the same VM. For example, the following request creates a VM with both virtual and dynamic Private Service Connect interfaces.

The parent of the dynamic Private Service Connect interfaces that have VLAN IDs `2` and `3` is the first vNIC, connecting to `producer-subnet`. The parent of the dynamic interface that has VLAN ID `4` is the vNIC that connects to `producer-subnet-2`. The last interface is a virtual Private Service Connect interface.
        
        {
          "machineType": "zones/us-west-1a/machineTypes/e2-medium",
          "name": "producer-vm",
          "disks": [
            {
              "initializeParams": {
                "sourceImage": "projects/debian-cloud/global/images/family/debian-11"
            },
            "boot": true
          }
          ],
          "networkInterfaces": [
            {
              "network": "https://www.googleapis.com/compute/v1/projects/producer-project-id/global/networks/producer-vpc-1",
              "subnetwork": "https://www.googleapis.com/compute/v1/projects/producer-project-id/regions/us-west-1/subnetworks/producer-subnet"
            },
            {
              "networkAttachment": "projects/consumer-project1/regions/us-west-1/networkAttachments/consumer-1-network-attachment",
              "vlan": 2
            },
            {
              "networkAttachment": "projects/consumer-project2/regions/us-west-1/networkAttachments/consumer-2-network-attachment",
              "vlan": 3
            },
            {
              "network": "https://www.googleapis.com/compute/v1/projects/producer-project-id/global/networks/producer-vpc-2",
              "subnetwork": "https://www.googleapis.com/compute/v1/projects/producer-project-id/regions/us-west-1/subnetworks/producer-subnet-2"
            },
            {
              "networkAttachment": "projects/consumer-project3/regions/us-west-1/networkAttachments/consumer-3-network-attachment",
              "vlan": 4
            },
            {
              "networkAttachment": "projects/consumer-project4/regions/us-west-1/networkAttachments/consumer-4-network-attachment"
            }
          ]
        }
        ```
        




For more information about creating VM instances, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

## Add dynamic Private Service Connect interfaces to existing VMs

You can add dynamic Private Service Connect interfaces to an existing VM without restarting the VM:

  * Each interface must connect to a different network attachment.
  * Each network attachment must be associated with a different subnet.
  * Each network attachment must exist in a different VPC network.



You must [configure routing](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#route-traffic) before traffic can flow through a new Private Service Connect interface.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM that you want to update.

  3. Click **Edit**.

  4. In the **Networking** section, click **Add a dynamic network interface**.

  5. For **Interface type** , select **Private Service Connect**.

  6. Select a parent network interface.

  7. In the **VLAN ID** box, enter a VLAN ID.

  8. In the **Network attachment URL** box, enter the URL of this interface's network attachment.

  9. Select an IP stack type for the interface. The network attachment's subnet [determines the possible stack types](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types).

  10. Optional: To add an alias IP range, do the following:

     1. In the **Alias IP ranges** section, click **Add IP range**.
     2. In the **Prefix length** box, enter the prefix length—for example, `/30`. You can add multiple alias IP ranges by clicking **Add IP range** , and then entering the prefix length for each additional alias IP range that you want to add.
  11. Click **Done**.

  12. Click **Save**.




###  gcloud 

To add a single dynamic Private Service Connect interface to an existing VM, use the [`gcloud compute instances network-interfaces add` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/add).

To add multiple dynamic Private Service Connect interfaces, repeat the command for each interface that you want to add.
    
    
    gcloud compute instances network-interfaces add INSTANCE_NAME \
        --zone=ZONE \
        --vlan=VLAN_ID \
        --parent-nic-name=PARENT_NIC_NAME \
        --network-attachment=ATTACHMENT_URI
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to update
  * `ZONE`: the zone of the instance to update
  * `VLAN_ID`: an ID (integer from 2 to 255) for the dynamic Private Service Connect interface

VLAN IDs must be unique for each dynamic interface that shares a parent vNIC. You can reuse the same ID for other dynamic interfaces that are associated with different vNICs.

  * `PARENT_NIC_NAME`: the name of the new VLAN NIC's parent network interface—for example, `nic0`.

  * `ATTACHMENT_URI`: the URI of the network attachment—for example: `projects/CONSUMER_PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME`




###  API 

To add a single dynamic Private Service Connect interface to an existing VM, send a request to the [`instances.addNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/addNetworkInterface).

To add multiple dynamic Private Service Connect interfaces, repeat the request for each interface that you want to add.

HTTP method and URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/addNetworkInterface
    

Request JSON body:
    
    
    {
      "networkAttachment": "ATTACHMENT_URI",
      "parentNicName": "PARENT_NIC_NAME",
      "vlan": VLAN_ID
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the VM's project
  * `ZONE`: the zone of the VM
  * `INSTANCE_NAME`: the name of the VM to update

  * `ATTACHMENT_URI`: the URI of the network attachment—for example: `projects/CONSUMER_PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME`

  * `PARENT_NIC_NAME`: the name of the new VLAN NIC's parent network interface—for example, `nic0`

  * `VLAN_ID`: an ID (integer from 2 to 255) for the VLAN NIC Private Service Connect interface

VLAN NIC interface IDs must be unique for each VLAN NIC under a parent network interface, but you can reuse the same ID for other VLAN NICs that are associated with different parent network interfaces.




## Migrate from virtual to dynamic Private Service Connect interfaces

To configure your service to use dynamic Private Service Connect interfaces instead of virtual Private Service Connect interfaces, do the following.

  1. Create a VM that uses dynamic Private Service Connect interfaces.
  2. [Configure routing](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces) for the new VM.
  3. Update your service to use the new VM.
  4. Delete the VM that uses virtual Private Service Connect interfaces.



## Create and manage Private Service Connect interfaces by using instance templates

You can create and manage Private Service Connect interfaces by using [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates).

After you create an instance template, you can use it to:

  * [Create a regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#creating_a_regional_managed_instance_group) that uses Private Service Connect interfaces
  * [Apply new configurations to an existing MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs), including adding or removing Private Service Connect interfaces



To create instance templates that use alias IP ranges or multiple Private Service Connect interfaces, use the same approach as creating VMs with Private Service Connect interfaces. Instance templates only support specifying alias IP ranges by prefix length.

###  Console 

**Create an instance template**

  1. In the Google Cloud console, go to the **Instance templates** page:

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. In the **Name** box, enter a name.

  4. Click **Region** , and then select the region of the network attachment that you want to connect to.

  5. Click **Advanced options**.

  6. Click **Networking**.

  7. In the **Network interfaces** section, click the expand_moreexpander arrow.

  8. Select a network and subnetwork for the instance template's primary network interface.

  9. Click **Done**.




**Add Private Service Connect interfaces**

To add a Private Service Connect interface, do the following. You can repeat these steps for each interface that you want to add.

**Add a virtual Private Service Connect interface**

  1. Click **Add a network interface**.
  2. For **Interface type** , select **Private Service Connect**.
  3. Enter the URL of this interface's network attachment.
  4. Select an **IP stack type** for the interface. The network attachment's subnet [determines the possible stack types](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types).
  5. Optional: To add an alias IP range, do the following: 
     1. In the **Alias IP ranges** section, click **Add IP range**.
     2. In the **Prefix length** box, enter the prefix length—for example, `/30`. You can add multiple alias IP ranges by clicking **Add IP range** , and then entering the prefix length for each additional alias IP range that you want to add.
  6. Click **Done**.



**Add a dynamic Private Service Connect interface**

  1. Click **Add a dynamic network interface**.
  2. For **Interface type** , select **Private Service Connect**.
  3. Select a parent network interface.
  4. In the **VLAN ID** box, enter a VLAN ID.
  5. In the **Network attachment URL** box, enter the URL of this interface's network attachment.
  6. Select an **IP stack type** for the interface. The network attachment's subnet [determines the possible stack types](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types).
  7. Optional: To add an alias IP range, do the following: 
     1. In the **Alias IP ranges** section, click **Add IP range**.
     2. In the **Prefix length** box, enter the prefix length—for example, `/30`. You can add multiple alias IP ranges by clicking **Add IP range** , and then entering the prefix length for each additional alias IP range that you want to add.
  8. Click **Done**.



To create the instance template, click **Create**.

###  gcloud 

  * To create an instance template with a virtual Private Service Connect interface, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).
        
        gcloud compute instance-templates create NAME \
            --machine-type=MACHINE_TYPE \
            --image-project=IMAGE_PROJECT \
            --image-family=IMAGE_FAMILY \
            --region=REGION \
            --network-interface='subnet=PRODUCER_SUBNET,no-address' \
            --network-interface='network-attachment=ATTACHMENT_URI,stack-type=STACK_TYPE'
        

Replace the following:

    * `NAME`: the name of the new instance template
    * `MACHINE_TYPE`: the instance's machine type, which can be [predefined](https://docs.cloud.google.com/compute/docs/machine-types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)—for example, `n1-standard-1`
    * `IMAGE_PROJECT`: the project of the image family

For example, if you specify `debian-12` as the image family, specify `debian-cloud` as the image project. You can view a list of available images, image projects, and image families by using the [`gcloud compute images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list).

    * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the instance

This creates the VM with the most recent, non-deprecated OS image in the image family. For example, if you specify `debian-12`, Compute Engine uses the latest version of the OS image in the [Debian 12](https://docs.cloud.google.com/compute/docs/images/os-details#debian) image family.

    * `REGION`: the region of the instance template's producer subnet.

    * `PRODUCER_SUBNET`: the subnet of the instance template

When you create a VM by using this instance template, the VM's primary network interface is assigned an internal IP address from this subnet. This subnet must be in the same region as the Private Service Connect interface's network attachment.

    * `ATTACHMENT_URI`: the URI of the network attachment—for example: `projects/CONSUMER_PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME`

    * `STACK_TYPE`: the [stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types) of the instance template's Private Service Connect interface.

To create an interface with an IPv4 address, specify `IPV4_ONLY` (the default). To create an interface that uses both an IPv4 and an IPv6 address (dual-stack), specify `IPV4_IPV6`. For IPv6 only, specify `IPV6_ONLY`.

The interface's stack type must be compatible with the stack type of the network attachment's subnet.

  * To create an instance template with a dynamic Private Service Connect interface, use the following command:
        
        gcloud compute instance-templates create NAME \
            --machine-type=MACHINE_TYPE \
            --image-project=IMAGE_PROJECT \
            --image-family=IMAGE_FAMILY \
            --region=REGION \
            --network-interface='subnet=PRODUCER_SUBNET,no-address' \
            --network-interface='network-attachment=ATTACHMENT_URI,vlan=VLAN_ID,stack-type=STACK_TYPE'
        

Replace `VLAN_ID` with the VLAN ID of the dynamic Private Service Connect interface, which must be an integer from 2 to 255.

VLAN IDs must be unique for each dynamic interface that shares a parent vNIC. You can reuse the same ID for other dynamic interfaces that are associated with different vNICs.




###  API 

  * To create an instance template with a virtual Private Service Connect interface, make a request to the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

HTTP method and URL:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
        

Request JSON body:
        
        {
          "name": "NAME",
          "properties": {
            "disks": [
              {
                "boot": true,
                "initializeParams": {
                  "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
                }
              }
            ],
            "machineType": "MACHINE_TYPE",
            "networkInterfaces": [
              {
                "subnetwork": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/SUBNET_REGION/subnetworks/PRODUCER_SUBNET"
              },
              {
                "networkAttachment": "ATTACHMENT_URI",
                "stackType": "STACK_TYPE"
              }
            ]
          }
        }
        

Replace the following:

    * `PROJECT_ID`: the project ID of the instance template
    * `NAME`: the name of the new instance template
    * `IMAGE_PROJECT`: the project of the image family

For example, if you specify `debian-12` as the image family, specify `debian-cloud` as the image project. You can view a list of available images, image projects, and image families by using the [`gcloud compute images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list).

    * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the instance

This creates the VM with the most recent, non-deprecated OS image in the image family. For example, if you specify `debian-12`, Compute Engine uses the latest version of the OS image in the [Debian 12](https://docs.cloud.google.com/compute/docs/images/os-details#debian) image family.

    * `MACHINE_TYPE`: the instance's machine type, which can be [predefined](https://docs.cloud.google.com/compute/docs/machine-types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)—for example, `n1-standard-1`

    * `SUBNET_REGION`: the region of the instance template's producer subnet.

    * `PRODUCER_SUBNET`: the subnet of the instance template

When you create a VM by using this instance template, the VM's primary network interface is assigned an internal IP address from this subnet. This subnet must be in the same region as the Private Service Connect interface's network attachment.

    * `ATTACHMENT_URI`: the URI of the network attachment—for example: `projects/CONSUMER_PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME`

    * `STACK_TYPE`: the [stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types) of the instance template's Private Service Connect interface

To create an interface with an IPv4 address, specify `IPV4_ONLY` (the default). To create an interface that uses both an IPv4 and an IPv6 address (dual-stack), specify `IPV4_IPV6`. For IPv6 only, specify `IPV6_ONLY`.

The interface's stack type must be compatible with the stack type of the network attachment's subnet.

  * To create an instance template with a dynamic Private Service Connect interface, make the following request.

HTTP method and URL:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
        

Request JSON body:
        
        {
          "name": "NAME",
          "properties": {
            "disks": [
              {
                "boot": true,
                "initializeParams": {
                  "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
                }
              }
            ],
            "machineType": "MACHINE_TYPE",
            "networkInterfaces": [
              {
                "subnetwork": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/SUBNET_REGION/subnetworks/PRODUCER_SUBNET"
              },
              {
                "networkAttachment": "ATTACHMENT_URI",
                "vlan": VLAN_ID,
                "stackType": "STACK_TYPE"
              }
            ]
          }
        }
        

Replace `VLAN_ID` with the VLAN ID of the dynamic Private Service Connect interface, which must be an integer from 2 to 255.

VLAN IDs must be unique for each dynamic interface that shares a parent vNIC. You can reuse the same ID for other dynamic interfaces that are associated with different vNICs.




For more information about creating instance templates, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## Describe a Private Service Connect interface

You can describe a VM to view the details of its Private Service Connect interfaces. Each interface's name, IP address, alias IP ranges, network attachment, and consumer subnet are listed in the network interfaces section of the VM's description.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the VM that has your Private Service Connect interface.

  3. In the **Network interfaces** section, view the details of your Private Service Connect interface.




###  gcloud 
    
    
    gcloud compute instances describe VM_NAME
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of your interface's VM.
  * `ZONE`: your VM's zone.



###  API 
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
    

Replace the following:

  * `PROJECT_ID`: the VM's project ID.
  * `ZONE`: the zone of the VM.
  * `VM_NAME`: the name of the VM.



## Terminate Private Service Connect interface connections

To terminate a connection between a virtual Private Service Connect interface and a network attachment, delete the interface's VM.

To terminate a connection between a dynamic Private Service Connect interface and a network attachment, do one of the following:

  * Remove the dynamic Private Service Connect interface.
  * Delete the dynamic Private Service Connect interface's VM.



### Remove a dynamic Private Service Connect interface

You can remove a dynamic Private Service Connect interface without restarting the associated VM.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM that you want to update.

  3. Click **Edit**.

  4. In the **Dynamic network interfaces** section, click delete **Delete** next to the interface that you want to delete.




###  gcloud 

Use the [`gcloud compute instances network-interfaces delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/delete).
    
    
    gcloud compute instances network-interfaces delete INSTANCE_NAME \
        --zone=ZONE \
        --network-interface=INTERFACE_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name of the interface's VM instance
  * `ZONE`: the zone of the interface's VM instance
  * `INTERFACE_NAME`: the Google Cloud name of the dynamic Private Service Connect interface to delete

For example, `nic0.10` is the name of a dynamic Private Service Connect interface, where `nic0` is the parent and `10` is the VLAN ID.




###  API 

Send a request to the [`instances.deleteNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/deleteNetworkInterface).

HTTP method and URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/deleteNetworkInterface?networkInterfaceName=INTERFACE_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID of the interface's VM
  * `ZONE`: the zone of the interface's VM
  * `INSTANCE_NAME`: the name of the interface's VM
  * `INTERFACE_NAME`: the Google Cloud name of the dynamic Private Service Connect interface to delete

For example, `nic0.10` is the name of a dynamic Private Service Connect interface, where `nic0` is the parent vNIC name and `10` is the VLAN ID.




### Delete a VM with a Private Service Connect interface

Deleting a VM terminates any Private Service Connect interface connections.

For information about deleting a VM, see [Delete an instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

## What's next?

  * [Configure routing](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces) for Private Service Connect interfaces.
  * [Configure security](https://docs.cloud.google.com/vpc/docs/configure-security-private-service-connect-interfaces) for a network that has a Private Service Connect interface connection.
  * [Manage destination overlap](https://docs.cloud.google.com/vpc/docs/manage-destination-overlap) in a network that has a Private Service Connect interface connection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
