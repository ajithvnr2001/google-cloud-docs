---
url: https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface/
title: Configure routing for an additional network interface \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:18.499685+00:00
---

# Configure routing for an additional network interface  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback 

#  Configure routing for an additional network interface Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to create a virtual machine (VM) instance with multiple network interfaces, each of which is attached to different Virtual Private Cloud (VPC) networks. Additionally, the tutorial provides an example of how to configure routing on a Linux VM so that you can successfully ping the `nic1` interface.

The routing configuration in this tutorial applies to both [network interface types](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts): vNICs and Dynamic Network Interfaces (NICs). While the example in this tutorial uses an instance with multiple vNICs, you can configure the same example for an instance that has Dynamic NICs.

Instances with multiple network interface are referred to as _multi-NIC instances_.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [ Virtual Private Cloud](https://docs.cloud.google.com/vpc/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




## Example configuration

The following diagram shows the VPC networks, subnets, and instances that you create in this tutorial, along with example values that you can use for resource names and subnet IP address ranges:

[ ![](https://docs.cloud.google.com/static/vpc/images/multinic/multi-nic-tutorial.svg)](https://docs.cloud.google.com/static/vpc/images/multinic/multi-nic-tutorial.svg)

**Figure 1.** In this tutorial, you create two VPC networks that each have two subnets. All subnets are in the same region. Additionally, you create three instances: one multi-NIC instance that attaches to the first two subnets, and one instance in each of the two remaining subnets (click to enlarge). 

## Create two VPC networks

To create a multi-NIC instance, the VPC networks that you are connecting it to must already exist. Create two VPC networks. In this tutorial, each VPC network has two subnets.

To create the configuration shown in the example configuration, create your networks and subnets with the following values:

  * A network called `network-1` that contains the following: 
    * A subnet called `subnet-1` that has a primary IPv4 address range of `10.10.1.0/24`.
    * A subnet called `subnet-3` that has a primary IPv4 address range of `10.10.3.0/24`.
  * A network called `network-2` that contains the following:

    * A subnet called `subnet-2` that has a primary IPv4 address range of `10.10.2.0/24`.
    * A subnet called `subnet-4` that has a primary IPv4 address range of `10.10.4.0/24`.



###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. In the **Name** field, enter a name for the VPC network.

  4. Choose **Custom** for the **Subnet creation mode**.

  5. In the **New subnet** section, specify the following:

     1. Provide a **Name** for the subnet.
     2. Select a **Region**. Make sure that both VPC networks that you create use the same region for at least one of their subnets. Use this same region when you create the multi-NIC instance in the following section. The example configuration uses the same region for all subnets.
     3. Enter an **IP address range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     4. Click **Done**.

  6. Click **Add subnet** to create a second subnet. Use this second subnet for testing `ping` from outside of the primary subnet range of the network interface of your instance.

  7. In the **Firewall rules** section, select the **allow-custom** rule, and then click **EDIT**. Configure the rule as follows to ensure that you can test connectivity from the test instances to `multi-nic-vm`:

     1. Under **IPv4 ranges** , keep the checkboxes selected for the subnets' IPv4 address ranges.
     2. Under **Other IPv4 ranges** , enter `35.235.240.0/20` so that you can connect to the test instances using SSH. Including this range allows SSH connections using Identity-Aware Proxy (IAP) TCP forwarding. For more information, see [Allow ingress ssh connections to VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh).
     3. Under **Protocols and ports** , select **specified protocols and ports**. 
        1. Select **TCP** , and then enter `22, 3389` to allow RDP and SSH.
        2. Select **Other** , and then enter `icmp` to allow ICMP.
  8. Click **Create**.

  9. Repeat these steps to create a second VPC network. Make sure that the subnet IP address ranges don't overlap with the subnets from your first network, such as the IP address ranges used in the example configuration.




###  gcloud 

  1. Use the [`networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) to create a VPC network.
         
         gcloud compute networks create NETWORK --subnet-mode=custom
         

Replace the following:

     * `NETWORK`: a name for the VPC network.
  2. Use the [`networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) to create a subnet for your VPC network.
         
         gcloud compute networks subnets create NAME \
           --network=NETWORK \
           --range=RANGE \
           --region=REGION
         

Replace the following:

     * `NAME`: a name for the subnet.
     * `NETWORK`: the name of the VPC network.
     * `RANGE`: an IP address range. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you enter a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     * `REGION`: a region. Make sure that both VPC networks that you create use the same region for at least one of their subnets. Use this same region when you create the multi-NIC instance in the following section. The example configuration uses the same region for all subnets.

  3. Repeat the previous step to create another subnet. Use this second subnet for testing `ping` from outside of the primary subnet range of the network interface of your instance.

  4. Create a firewall rule to allow SSH, RDP, and ICMP:
         
         gcloud compute firewall-rules create allow-ssh-rdp-icmp \
          --network NETWORK \
          --action=ALLOW \
          --direction=INGRESS \
          --rules=tcp:22,tcp:3389,icmp \
          --source-ranges=SOURCE_RANGE
         

Replace the following:

     * `NETWORK`: enter the value that corresponds to the network you're creating: 
       * For the first network, enter `network-1`.
       * When you repeat the steps in this section for the second network, enter `network-2`.
     * `SOURCE_RANGE`: enter the value that corresponds to the network you're creating: 
       * For the first network, enter `10.10.3.0/24, 35.235.240.0/20`. Including `10.10.3.0/24` ensures that you can test connectivity from `test-vm-1` to the `nic0` interface of the `multi-nic-vm`. Including `35.235.240.0/20` allows SSH connections using Identity-Aware Proxy (IAP) TCP forwarding. For more information, see [Allow ingress ssh connections to VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh).
       * When you repeat the steps in this section for the second network, enter `10.10.4.0/24, 35.235.240.0/20`. Including `10.10.4.0/24` ensures that you can test connectivity from `test-vm-2` to the `nic0` interface of the `multi-nic-vm`. Including `35.235.240.0/20` allows SSH connections using Identity-Aware Proxy (IAP) TCP forwarding. For more information, see [Allow ingress ssh connections to VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh).
  5. Repeat these steps to create a second VPC network. Make sure that the subnet IP address ranges don't overlap with the subnets from your first network, such as the IP address ranges used in the example configuration.




## Create a multi-NIC instance

Create an instance that has one interface for each VPC network that you created in the previous section.

To create a multi-NIC instance:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Name** field, enter a name for the instance. This corresponds to `multi-nic-vm` in the example configuration.

  3. In the **Region** field, select the same region in which you created one subnet in each of your VPC networks. The instance must be in the same region as the subnets to which its interfaces connect. The example configuration uses the same region for all subnets.

  4. In the **Zone** field, select a zone.

  5. In the **Advanced options** section, expand **Networking** , and then do the following:

     1. Review the **Network interfaces** section. Google Cloud automatically populates the first network interface with a network and subnetwork. This corresponds to `network-1` and `subnet-1` in the example configuration.
     2. For **Primary internal IPv4 address** , select one of the following: 
        * **Ephemeral** to assign a new ephemeral IPv4 address
        * A reserved static internal IPv4 address from the list
        * **Reserve static internal IPv4 address** to reserve and assign a new static internal IPv4 address. If you are using the example configuration, reserve `10.10.1.3`.
     3. For **External IPv4 address** , select one `None`.

     4. To add another interface, click **Add network interface**.

     5. For **Network** and **Subnetwork** , select the second network and subnetwork that you created. This corresponds to `network-2` and `subnet-2` in the example configuration.

     6. For **IP stack type** , select **IPv4 (single-stack)**.

     7. For **Primary internal IPv4 address** , select one of the following:

        * **Ephemeral** to assign a new ephemeral IPv4 address
        * A reserved static internal IPv4 address from the list
        * **Reserve static internal IPv4 address** to reserve and assign a new static internal IPv4 address. If you are using the example configuration, reserve `10.10.2.3`.
     8. For **External IPv4 address** , select one `None`.

     9. To finish adding the network interface, click **Done**.

  6. Click **Create**.




###  gcloud 

To create network interfaces on a new instance, use the [`instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

Include the `--network-interface` flag for each interface, followed by any appropriate networking keys, such as `network`, `subnet`, `private-network-ip`. For the external IP address, the following command specifies `no-address`.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone ZONE \
        --network-interface \
            network=NIC0_NETWORK,subnet=NIC0_SUBNET,private-network-ip=NIC0_INTERNAL_IPV4_ADDRESS,no-address \
        --network-interface \
            network=NIC1_NETWORK,subnet=NIC1_SUBNET,private-network-ip=NIC1_INTERNAL_IPV4_ADDRESS,no-address
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to create. This corresponds to `multi-nic-vm` in the example configuration.
  * `ZONE`: the zone where the instance is created. Enter a zone in the same region in which you created one subnet in each of your VPC networks. The instance must be in the same region as the subnets to which its interfaces connect. The example configuration uses the same region for all subnets.
  * Values for the first interface: 
    * `NIC0_NETWORK`: the network where the interface attaches. This corresponds to `network-1` in the example configuration.
    * `NIC0_SUBNET`: the subnet where the interface attaches. This corresponds to `subnet-1` in the example configuration.
    * `NIC0_INTERNAL_IPV4_ADDRESS`: the internal IPv4 address that you want the interface to have in the target subnet. If you are using the example configuration, enter `10.10.1.3`. Omit if you just want any valid address assigned.
  * Values for the second interface 
    * `NIC1_NETWORK`: the network where the interface attaches. This corresponds to `network-2` in the example configuration.
    * `NIC1_SUBNET`: the subnet where the interface attaches. This corresponds to `subnet-2` in the example configuration.
    * `NIC1_INTERNAL_IPV4_ADDRESS`: the internal IPv4 address that you want the interface to have in the target subnet. If you are using the example configuration, enter `10.10.2.3`. Omit if you just want any valid address assigned.



## Create two test instances

Create two additional instances:

  * One in the same network, but different subnet, as the `nic0` interface of the multi-NIC instance that you created. This corresponds to `test-vm-1` in `subnet-3` in the example configuration.
  * One in the same network, but different subnet, as the `nic1` interface of the multi-NIC instance that you created. This corresponds to `test-vm-2` in `subnet-4` in the example configuration.



You use these instances for testing `ping` from the subnets that are outside of the primary subnet range of your instance that has multiple network interfaces.

To create the instances:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Name** field, enter a name for the instance.

  3. In the **Region** field, select the region in which you placed the additional subnet in your first VPC network.

  4. In the **Zone** field, select a zone.

  5. In the **Advanced options** section, expand **Networking** , and then do the following:

     1. Review the **Network interfaces** section. Make sure that the subnet is different from the one used by the `nic0` interface of your multi-NIC instance.
  6. Click **Create**.

  7. Repeat these steps to create an instance in your second VPC network, and in a subnet that is different from that of the `nic1` interface of your multi-NIC instance.




###  gcloud 

  1. Run the [`instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and include the `--network-interface` flag for each interface, followed by any appropriate networking keys, such as `network`, `subnet`, `private-network-ip`, or `address`.
         
         gcloud compute instances create INSTANCE_NAME \
           --zone ZONE \
           --network-interface \
                network=NIC0_NETWORK,subnet=NIC0_SUBNET, private-network-ip=NIC0_INTERNAL_IPV4_ADDRESS
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance to create.
     * `ZONE`: the zone where the instance is created. Enter the region in which you placed the additional subnet in your first VPC network—the subnet that is not used by the multi-NIC instance.
     * `NIC0_NETWORK`: the network where the interface attaches.
     * `NIC0_SUBNET`: the subnet where the interface attaches.
     * `NIC0_INTERNAL_IPV4_ADDRESS`: the internal IPv4 address that you want the interface to have in the target subnet. Omit if you just want any valid address assigned.
  2. Repeat the previous step to create an instance in your second VPC network and in a subnet that is different from that of the `nic1` interface of your multi-NIC instance.




## Test connectivity to the multi-NIC instance

Follow the steps in this section to test `ping` from the additional instances that you created to each interface of your instance with multiple network interfaces.

The following table shows the scenarios in which you can successfully ping at this point in the tutorial using the IP address values from the example configuration.

From | To | `ping successful`  
---|---|---  
Instance (`test-vm-1`) in the same network, but different subnet, as the `nic0` interface of the `multi-nic-vm`. | Internal IP address (`10.10.1.3`) of the `nic0` interface of `multi-nic-vm` |   
Instance (`test-vm-2`) in the same network, but different subnet, as the `nic1` interface of `multi-nic-vm` | Internal IP address (`10.10.2.3`) of the `nic1` interface of `multi-nic-vm` |   
  
### Get the IP addresses of the multi-NIC instance

If necessary, get the interface IP addresses of your multi-NIC instance so that you can ping them in the following sections.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of instances, find the multi-NIC instance that you created, and record these values so that you can ping them in the following steps:

     * The **Internal IP** addresses of its `nic0` and `nic1` interfaces



###  gcloud 

  1. Run the [`instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list):
         
         gcloud compute instances list
         

  2. Locate your multi-NIC instance and record the following from the output:

     * `INTERNAL_IP`: the first and second addresses correspond to the `nic0` and `nic1` network interfaces.



### Ping the `nic0` interface of your instance

  1. In the list of instances, locate the instance that you created in the same network, but different subnet, as the `nic0` interface of the multi-NIC instance.

     1. In the row of the instance, click **SSH**.
  2. Run the following command to ping the _internal IP_ address of the `nic0` interface of your multi-NIC instance:
         
         ping INTERNAL_IP_NIC0
         

Replace `INTERNAL_IP_NIC0` with the corresponding address that you recorded previously. If you are using the example configuration, enter `10.10.1.3`.

Note that the ping is successful.

  3. Run `exit` to close the terminal window.




### Ping the `nic1` interface of your instance

  1. In the list of instances, locate the instance that you created in the same network, but different subnet, as the `nic1` interface of the multi-NIC instance.

     1. In the row of the instance, click **SSH**.
  2. Run the following command to ping the _internal IP_ address of the second interface of your multi-NIC instance:
         
         ping INTERNAL_IP_NIC1
         

Replace `INTERNAL_IP_NIC1` with the corresponding address that you recorded previously. If you are using the example configuration, enter `10.10.2.3`.

Note that the ping is unsuccessful.

  3. Run `exit` to close the terminal window.




## Configure policy routing

The ping test in the preceding section failed due to asymmetric routing— traffic is sent to the `nic1` interface of `multi-nic-vm`, but the default route for the instance results in the replies being sent from `nic0`. For more information, see [Specifications](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications) in the Multiple network interfaces overview.

Follow the steps in this section to configure policy routing to make sure that egress packets leave through the correct interface.

This tutorial uses Linux VMs. Source-based policy routing is not supported by Windows operating systems.

### Find the default gateway for the `nic1` interface of the instance

You can find the default gateway for an instance's interface by querying the metadata server. If you are using the example configuration, the value is `10.10.2.1`.

To find the default gateway for the `nic1` interface's IPv4 address, make the following request from the multi-NIC instance:
    
    
    curl http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/1/gateway -H "Metadata-Flavor: Google"
    

To find the default gateway for a different network interface, specify the appropriate interface number. To find the name that Google Cloud has assigned to the interface, see Get the IP addresses of the multi-NIC instance. This is different from the interface name that the operating system assigns. The interface has the format `nicNUMBER`. In your request to the metadata server, enter only the number. For example, for `nic2`, specify `2`.

### Configure a new routing table on the multi-NIC instance

This section describes how to configure a new routing table on the multi-NIC instance.

**Note:** While the following commands use the internal IP address of the `nic1` interface, completing this configuration lets you reach both the internal and external (if assigned) IP addresses of the interface. For example, when you ping the external IPv4 address of an instance, Google Cloud performs destination network address translation (DNAT) to the internal IPv4 address of the instance. The instance then responds using the local routing policy that you configured with the internal IP address. For the response, Google Cloud then performs source network address translation (SNAT) to translate the source back to the external IP address. However, you might need an addition firewall rule to allow ICMP from the external IP address.

  1. Enable the serial console by following the steps in [Enabling access for a VM instance](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enable_instance_access).

  2. To avoid losing connectivity to the instance while you change the default route, [connect to the serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console).

  3. Run `ip link list` to list your instance's network interfaces, and then record the name of the `nic1` interface, such as `ens5`.

  4. Run the following command to ensure that the `nic1` interface is configured with an IP address.
         
         ip addr show NIC
         

Replace `NIC` with the name of the `nic1` interface from the previous step.

If the `nic1` interface has not been assigned an IP address automatically, you can manually assign an IP address by running the following command:
         
         sudo ip addr add IP_ADDRESS dev NIC
         

Replace the following:

     * `IP_ADDRESS`: the internal IP address to configure on the interface. This corresponds to `10.10.2.3` in the example configuration.
     * `NIC`: the name of the `nic1` interface from the previous step.
  5. Create a custom route table for the `nic1` network interface.
         
         echo "1 ROUTE_TABLE_NAME" | sudo tee -a /etc/iproute2/rt_tables
         

Replace `ROUTE_TABLE_NAME` with a name for the route table, such as `route-nic1`.

  6. Create the default route in the custom route table intended for the `nic1` network interface and a route with a source hint for packets sent to the gateway.
         
         sudo ip route add default via GATEWAY dev NIC table ROUTE_TABLE_NAME
         sudo ip route add GATEWAY src IP_ADDRESS dev NIC table ROUTE_TABLE_NAME
         

Replace the following:

     * `GATEWAY`: the default gateway IP address of the interface. This corresponds to `10.10.2.1` in the example configuration.
     * `NIC`: the interface that you want to add a route for. For example, `ens5`.
     * `ROUTE_TABLE_NAME`: the name of your route table.
     * `IP_ADDRESS`: the internal IP address configured on the interface. This corresponds to `10.10.2.3` in the example configuration.
  7. Create routing rules that instruct the instance to use the custom route table for packets with sources or destinations that match the primary internal IPv4 address assigned to the `nic1` interface:
         
         sudo ip rule add from IP_ADDRESS/PREFIX_LENGTH table ROUTE_TABLE_NAME
         sudo ip rule add to IP_ADDRESS/PREFIX_LENGTH table ROUTE_TABLE_NAME
         

Replace the following:

     * `IP_ADDRESS`: the internal IP address configured on the interface. This corresponds to `10.10.2.3` in the example configuration.
     * `PREFIX_LENGTH`: the prefix length for the configured IP address.
     * `ROUTE_TABLE_NAME`: the name of your route table.
  8. Run the following command to remove all entries from the cache route table. This might be necessary if you are using an existing instance with previously configured route tables.
         
         sudo ip route flush cache
         




The preceding routing configurations don't persist after system reboots or network service restarts. To ensure your policy routing persists, you must define these rules in your operating system's persistent network configuration. For more information, consult the documentation for your guest OS.

## Retest connectivity to the multi-NIC instance

The following table shows the scenarios in which you can successfully ping now that you have configured policy routing. Repeat the steps to ping the nic1 interface of your instance to confirm that you can now ping both IP addresses successfully.

From | To | `ping successful`  
---|---|---  
Instance (`test-vm-1`) in the same network, but different subnet, as the `nic0` interface of `multi-nic-vm`. | Internal IP address (`10.10.1.3`) of the `nic0` interface of `multi-nic-vm` |   
Instance (`test-vm-2`) in the same network, but different subnet, as the `nic1` interface of `multi-nic-vm` | Internal IP addresses (`10.10.2.3`) of the `nic1` interface of the `multi-nic-vm` |   
  
## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

If you don't want to delete the entire project, delete the VPC networks and instances that you created for the tutorial.

Before you can delete a network, you must delete all resources in all of its subnets, and all resources that reference the network.

#### Delete instances

To delete instances:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Check the instances you want to delete.

  3. Click the **Delete** button.




###  gcloud 

Use the [`gcloud compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete). When you delete an instance in this way, the instance shuts down and is removed from the list of instances, and all resources attached to the instance are released, such as persistent disks and any static IP addresses.

To delete an instance, use the following command:
    
    
    gcloud compute instances delete example-instance [example-instance-2 example-instance-3..]
    

#### Delete VPC networks

To delete a VPC network:

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click **Delete VPC network**.

  4. In the message that appears, click **Delete** to confirm.




###  gcloud 

Use the [`networks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/delete).
    
    
    gcloud compute networks delete NETWORK
    

Replace `NETWORK` with the name of the network to delete.

## What's next

  * Read the [overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) for multiple network interfaces.
  * Read [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
