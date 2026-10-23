---
url: https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces/
title: Configure routing for Private Service Connect interfaces \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:31.924307+00:00
---

# Configure routing for Private Service Connect interfaces  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure routing for Private Service Connect interfaces 

This page describes how to configure routing for both virtual and dynamic Private Service Connect interfaces.

## Route traffic through a Private Service Connect interface

After you create a Private Service Connect interface, you need to route traffic through the interface by configuring the guest operating system (guest OS) on the interface's VM.

### Allow SSH connectivity

Make sure that firewall rules are configured to [allow ingress SSH connections](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh) to your Private Service Connect interface's VM.

### Find the Google Cloud name of your Private Service Connect interface

To configure routing, you need to know the Google Cloud name of your Private Service Connect interface.

To find the Google Cloud name of a dynamic Private Service Connect interface, use the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM that has your Private Service Connect interface.

  3. In the **Network interfaces** section, find and note the name of your virtual Private Service Connect interface—for example, `nic1`.




###  gcloud 

  1. Use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe).
         
         gcloud compute instances describe VM_NAME \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM that has your Private Service Connect interface
     * `ZONE`: the VM's zone
  2. In the command's output, find and note the Google Cloud name of your Private Service Connect interface.

     * For virtual Private Service Connect interfaces, the name has the form `nic[interface_number]`—for example, `nic0` or `nic1`.
     * For dynamic Private Service Connect interfaces, the name has the form `nic[parent_interface_number.VLAN_ID]`—for example, `nic0.10` or `nic1.42`.



### Configure automatic management of dynamic Private Service Connect interfaces

If you are configuring routing for a dynamic Private Service Connect interface, [Enable automatic management of Dynamic Network Interfaces](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics#configure-guest-os-automatic). You only need to do this once per VM.

### Find the guest OS name of your Private Service Connect interface

To configure routing, you need to know the guest OS name of your Private Service Connect interface, which is different than the interface's name in Google Cloud.

To find the interface's name on a Debian VM, do the following. For VMs with other operating systems, consult the public documentation of the operating system.

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) to your Private Service Connect interface's VM.
  2. Run the following command:
         
         ip address
         

In the list of network interfaces, find and note the interface name that is associated with your Private Service Connect interface's IP address. For example, if the [Linux guest agent](https://docs.cloud.google.com/compute/docs/images/guest-environment#linux) manages your VM's network interfaces, the names have the following forms:

     * Virtual Private Service Connect interfaces: `ens[number]`—for example, `ens5`.
     * Dynamic Private Service Connect interfaces: `gcp.ens[parent_interface_number].[VLAN_ID]`—for example, `gcp.ens5.10`.



### Find the gateway IP address of your Private Service Connect interface

To configure routing, you need to know the IP address of your Private Service Connect interface's default gateway.

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) to your Private Service Connect interface's VM.
  2. Send a `GET` request from your interface's VM to the associated [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview).

     * For virtual Private Service Connect interfaces, send the following request:
           
           curl http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/INTERFACE_NUMBER/gateway -H "Metadata-Flavor: Google" && echo
           

Replace `INTERFACE_NUMBER` with the index of your interface. For example, if the Google Cloud name for your Private Service Connect interface is `nic1`, use a value of `1`.

     * For dynamic Private Service Connect interfaces, send the following request:
           
           curl http://metadata.google.internal/computeMetadata/v1/instance/vlan-network-interfaces/PARENT_INTERFACE_NUMBER/VLAN_ID/gateway -H "Metadata-Flavor: Google" && echo
           

Replace the following:

       * `PARENT_INTERFACE_NUMBER`: the index of the dynamic Private Service Connect interface's parent vNIC

For example, if the Google Cloud name for your Private Service Connect interface is `nic1.5`, use a value of `1`.

       * `VLAN_ID`: the VLAN ID of your dynamic Private Service Connect interface

For example, if the Google Cloud name for your Private Service Connect interface is `nic1.5`, use a value of `5`.

The request's output displays the gateway IP address.




### Add routes for consumer subnets

You must add a route to your Private Service Connect interface's default gateway for each consumer subnet that connects to your Private Service Connect interface. This lets traffic that is bound for the consumer network flow through the Private Service Connect interface.

The following steps describe how to temporarily update the routing table for a VM that uses the Debian operating system. To update the table permanently, or to update the route on a different operating system, consult the operating system's public documentation.

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) to your Private Service Connect interface's VM.

  2. Run the following command for each consumer subnet that connects to your Private Service Connect interface:
         
         sudo ip route add CONSUMER_SUBNET_RANGE via GATEWAY_IP dev OS_INTERFACE_NAME
         

Replace the following:

     * `CONSUMER_SUBNET_RANGE`: the IP address range of your consumer subnet
     * `GATEWAY_IP`: the IP address of the default gateway for your interface's subnet
     * `OS_INTERFACE_NAME`: the guest OS name for your Private Service Connect interface—for example, `ens5` or `gcp.ens5.10`
  3. Run the following command to remove all entries from the cache route table. This might be necessary if you are using an existing instance with previously configured route tables.
         
         sudo ip route flush cache
         




## Use a Private Service Connect interface with VPC Service Controls

You can use Private Service Connect interfaces with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). This lets a producer VPC network access Google APIs and services through a consumer VPC network, while the consumer organization can apply the security benefits of VPC Service Controls.

You can implement this configuration by using one of the following approaches, which are described in the following sections:

  * Configure guest OS routing
  * Isolate the Private Service Connect interface with network namespaces or VRF and then configure routing



### Configure guest OS routing

To use a Private Service Connect interface with VPC Service Controls, configure routing in the guest OS of the interface's VM. Direct traffic that is destined for Google APIs and services through your Private Service Connect interface.

The following steps describe how to temporarily update the routing table for a VM that uses the Debian operating system. To update the table permanently, or to update the route on a different operating system, consult the operating system's public documentation.

To configure routing, do the following:

  1. [Allow SSH connectivity](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#allow_ssh_connectivity) to your Private Service Connect interface's VM.
  2. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) to the VM.
  3. To create a custom route table for your Private Service Connect interface, run the following command:
         
         echo "1 ROUTE_TABLE_NAME" | sudo tee -a /etc/iproute2/rt_tables
         

Replace `ROUTE_TABLE_NAME` with a name for the route table.

  4. Add a route to your route table for traffic to Google APIs and services. For example, to add a route for traffic to the `restricted.googleapis.com` virtual IP (VIP), use the following command, which specifies the [IPv4 address range for restricted.googleapis.com](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity#ip-ranges):
         
         sudo ip route add 199.36.153.4/30 dev OS_INTERFACE_NAME table ROUTE_TABLE_NAME
         

Replace `OS_INTERFACE_NAME` with the guest OS name for your Private Service Connect interface—for example, `ens5` or `gcp.ens5.10`

  5. To add a routing rule that uses the custom route table for packets that originate from your Private Service Connect interface, use the following command:
         
         sudo ip rule add from INTERFACE_IP table ROUTE_TABLE_NAME
         

Replace `INTERFACE_IP` with the IP address of your Private Service Connect interface. You can find the interface's IP address by [describing the interface's VM](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#describe).

  6. Run the following command to remove all entries from the cache route table. This might be necessary if you are using an existing instance with previously configured route tables.
         
         sudo ip route flush cache
         




### Isolate Private Service Connect interfaces with namespaces or VRF

Alternatively, you can configure your VM to use network namespaces or virtual routing and forwarding (VRF) to isolate the Private Service Connect interface. This approach is helpful for containerized workloads, such as those running in Google Kubernetes Engine pods.

Configure routing using the same context that you used for isolating the interface, and make sure that workloads that use your Private Service Connect interface exist within this same context.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
