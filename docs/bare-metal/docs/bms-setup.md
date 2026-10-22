---
url: https://docs.cloud.google.com/bare-metal/docs/bms-setup/
title: Quickstart: Set up Google Cloud to work with your Bare Metal Solution environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:15.987636+00:00
---

# Quickstart: Set up Google Cloud to work with your Bare Metal Solution environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-setup/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Google Cloud to work with your Bare Metal Solution environment

When your Bare Metal Solution environment is ready, you are notified by Google Cloud. The notification includes the internal IP addresses of your new servers.

These instructions show you how to do the following tasks that are required to connect to your Bare Metal Solution environment:

  * Create redundant VLAN attachments to the Bare Metal Solution environment.
  * Create a jump host VM instance in your VPC network.
  * Use SSH or RDP to log in to your Bare Metal Solution servers from the jump host VM instance.



After you are connected to your servers, validate the configuration of your Bare Metal Solution order.

## Before you begin

To connect to and configure your Bare Metal Solution environment, you need:

  * A Google Cloud project with billing enabled. You can create a project on [the project selector page](https://console.cloud.google.com/projectselector2/home/dashboard) in the Google Cloud console.
  * A Virtual Private Cloud (VPC) network. This is the VPC network that you named when you placed your order for Bare Metal Solution. If you need to create the VPC network, see [Using VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * The following information that is provided to you by Google Cloud when your Bare Metal Solution is ready: 
    * The IP addresses of your bare-metal servers.
    * The temporary passwords for each of your bare-metal servers.



## Create the VLAN attachments for the Cloud Interconnect connection

To access your Bare Metal Solution server, you need to create and set up VLAN attachments (also known as `InterconnectAttachments`) in the same region as your server. A VLAN attachment is a logical object in Cloud Interconnect that is used to connect your Bare Metal Solution environment to Google Cloud.

**Note:** VLAN attachment is not the same as a client network or private network used inside the Bare Metal Solution environment.

We recommend creating VLAN attachments in redundant pairs for high availability. The primary VLAN attachment and the secondary VLAN attachment of a pair are each provisioned in a separate [EAD (Edge Availability Domain)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) in separate hardware and physical racks. This ensures high availability during events, such as maintenance.

![Edge availability domain for Bare Metal Solution.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-ead.svg)

A single VLAN attachment supports a maximum speed of 10 Gbps. A pair of VLAN attachments (that is, the primary and the secondary VLAN attachments) can support a maximum speed of 20 Gbps. To achieve higher throughput between your Bare Metal Solution environment and VPC network, you can configure multiple VLAN attachment pairs.

To make one VLAN attachment preferable over others, you can [update the base route priority](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority) on the Cloud Router.

After creating the VLAN attachments, you need to pre-activate them and add them to your Bare Metal Solution [VRF](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_vrfs). To create and set up your VLAN attachments, follow these steps:

###  Console 

  1. If you don't already have a [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) in your Bare Metal Solution network and region, create a Cloud Router to connect your Bare Metal Solution environment with your VPC network.

You can use a single Cloud Router for the both VLAN attachments or separate Cloud Routers for each VLAN attachment.

For peering with Bare Metal Solution, use Google Public ASN (`16550`) when creating the router.

**Note:** A Cloud Router can have only one ASN. If you want to use an existing router, ensure that its ASN is `16550`. Otherwise, create a new one.

For instructions, see [Create Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-on-premises-network).

  2. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** page.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  3. Click **Create VLAN attachments**.

  4. Select **Partner Interconnect** , and then click **Continue**.

  5. Select **I already have a service provider**.

  6. Select **Create a redundant pair of VLAN attachments**.

Both VLAN attachments can serve traffic, and you can route the traffic to load-balance between them. If one attachment goes down (for example, during scheduled maintenance), then the other attachment continues to serve traffic. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy).

  7. In the **Network** field, select your VPC network.

  8. In the **Region** field, select the Google Cloud region.

  9. Specify the following details for the both VLAN attachments.

     * **Cloud Router** — A Cloud Router to associate with this VLAN attachment. You can only choose a Cloud Router that has an ASN of `16550` and is in your VPC network and region.
     * **VLAN attachment name** — A name for each attachment. For example, `my-attachment-1` and `my-attachment-2`.
     * **Description** — Information about each VLAN attachment.
     * **Maximum transmission unit (MTU)** — The maximum packet size for network transmission. The default size is 1440. You can choose between following MTUs when creating your VLAN attachments. 
       * 1440
       * 1460
       * 1500
       * 8896
**Note:** VLAN attachment for Bare Metal Solution does not supports jumbo frame (8896). We recommend you to configure standard MTU (1500) consistent between BMS network segments (BMS Client Network, VLAN attachment, VPC Network, On-premises network)
  10. Click **OK**.

On the **VLAN attachments** page, the VLAN attachment status shows `waiting for service provider`. Proceed to the next step.

  11. After Google Cloud notifies you that your Bare Metal Solution servers are ready, add your new VLAN attachments to a VRF by following these steps:

     1. To add VLAN attachments to an existing VRF, follow the instructions in [Add a VLAN attachment](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#add-vlan-attachment).
     2. To add VLAN attachments to a new VRF, follow the instructions in [Create a VRF](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#create-vrf).



###  gcloud 

  1. If you don't already have Cloud Router instances in the network and region that you are using with Bare Metal Solution, create one for each VLAN attachment. Use `16550` as the ASN number:
         
         [gcloud compute routers create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) router-name \
         --network vpc-network-name \
         --asn 16550 \
         --region region

For more information, see [Creating Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-on-premises-network).

  2. Create an `InterconnectAttachment` of type `PARTNER`, specifying the name of your Cloud Router and the [edge availability domain (EAD)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edgeavailabilitydomain) of the VLAN attachment. Also, add the `--admin-enabled` flag to [pre-activate](https://docs.cloud.google.com/interconnect/concepts/partner-overview#pre-activate) the attachments and send traffic immediately after Google Cloud completes the Bare Metal Solution configuration.
         
         [gcloud compute interconnects attachments partner create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create) first-attachment-name \
           --region region \
           --router first-router-name \
           --edge-availability-domain availability-domain-1 \
           --admin-enabled
         
         [gcloud compute interconnects attachments partner create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create) second-attachment-name \
           --region region \
           --router second-router-name \
           --edge-availability-domain availability-domain-2 \
           --admin-enabled

Google Cloud automatically adds an interface and a BGP peer on the Cloud Router.

The following example creates redundant attachments, one in EAD `availability-domain-1` and another in EAD `availability-domain-2`. Each is associated with a separate Cloud Router, `my-router-1` and `my-router-2`, respectively. They are both in the `us-central1` region.
         
         gcloud compute interconnects attachments partner create my-attachment \
          --region us-central1 \
          --router my-router-1 \
          --edge-availability-domain availability-domain-1 \
          --admin-enabled
         
         gcloud compute interconnects attachments partner create my-attachment \
          --region us-central1 \
          --router my-router-2 \
          --edge-availability-domain availability-domain-2 \
           --admin-enabled

  3. Run the `gcloud compute interconnects attachments describe` command to view the details of the VLAN attachment.
         
         gcloud compute interconnects attachments describe my-attachment \
           --region us-central1
         
         adminEnabled: false
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
         creationTimestamp: '2017-12-01T08:29:09.886-08:00'
         id: '7976913826166357434'
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: my-attachment
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/routers/my-router
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/interconnectAttachments/my-attachment
         state: PENDING_PARTNER
         type: PARTNER

     * The state of the VLAN attachment is `PENDING_PARTNER` until Google Cloud completes your VLAN attachment configuration. Afterwards, the state of the attachment is `INACTIVE` or `ACTIVE`, depending on whether you chose to pre-activate your attachments.

When you request connections from Google Cloud, you must select the same metro (city) for both attachments for them to be redundant. For more information, see the Redundancy section in the [Partner Interconnect Overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy) page.

  4. If the VLAN attachments do not come up after Google Cloud completes your Bare Metal Solution order, activate each VLAN attachment:
         
         [gcloud compute interconnects attachments partner update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update) attachment-name \
         --region region \
         --admin-enabled




You can check the status of the Cloud Routers and your advertised routes in the Cloud console. For more information, see [Viewing Router Status and Advertised Routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

## Set up routing between Bare Metal Solution and Google Cloud

As soon as your VLAN attachments are active, your BGP sessions come up and the routes from the Bare Metal Solution environment are received over the BGP sessions.

### Add a custom advertised route for a default IP range to your BGP sessions

To set up routing for traffic from the Bare Metal Solution environment, the recommendation is to add a custom advertised route of a default route, such as `0.0.0.0/0`, on your BGP sessions to the Bare Metal Solution environment.

To specify advertisements on an existing BGP session:

###  Console 

  1. Go to the Cloud Router page in the Google Cloud console.  
[Cloud Router list](https://console.cloud.google.com/hybrid/routers/list)
  2. Select the Cloud Router that contains the BGP session to update.
  3. In the Cloud Router's detail page, select the BGP session to update.
  4. In the BGP session details page, select **Edit**.
  5. For the **Routes** , select **Create custom routes**.
  6. Select **Add custom route** to add an advertised route.
  7. Configure the route advertisement. 
     * **Source** — Select **Custom IP range** to specify a custom IP address range.
     * **IP address range** — Specify the custom IP address range by using CIDR notation.
     * **Description** — Add a description to help you identify the purpose of this custom advertised route.
  8. After you're done adding routes, select **Save**.



###  gcloud 

You can add to existing custom advertised routes or you can set a new custom advertised route, which replaces any existing custom advertised routes with the new one.

To set a new custom advertised route for a default IP range, use the `--set-advertisement-ranges` flag:
    
    
    [gcloud compute routers update-bgp-peer](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer) router-name \
       --peer-name bgp-session-name \
       --advertisement-mode custom \
       --set-advertisement-ranges 0.0.0.0/0

To append the default IP range to existing ones, use the `--add-advertisement-ranges` flag. Note that this flag requires the Cloud Router's advertisement mode to already be set to `custom`. The following example, adds the `0.0.0.0/0` custom IP to the Cloud Router's advertisements:
    
    
    [gcloud compute routers update-bgp-peer](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer) router-name \
       --peer-name bgp-session-name \
       --add-advertisement-ranges 0.0.0.0/0

### Optionally, set the VPC Network Dynamic Routing Mode to `global`

If you have Bare Metal Solution servers in two different regions, consider enabling global routing mode on the VPC network to have your Bare Metal Solution regions talk to each other directly over the VPC network.

The global routing mode is also needed to enable communications between an on-premises environment that is connected to one Google Cloud region and a Bare Metal Solution environment in another Google Cloud region.

To set the global routing mode, see [Set routing and best path selection modes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes).

## VPC firewall setup

New VPC networks come with active default firewall rules that restrict most traffic in the VPC network.

By default, new VPC networks allow all outbound (egress) traffic and block all inbound (ingress) traffic. Because VPC firewalls are stateful, return traffic from your Bare Metal Solution environment in response to connections initiated from the VPC (such as from a jump host) is automatically allowed.

You only need to create firewall rules in your VPC network if:

  * Servers in your Bare Metal Solution environment need to **initiate** connections to services running in your VPC or other Google Cloud resources. In this case, you must create an **ingress** rule to allow this traffic.
  * You have modified the default firewall rules to restrict outbound traffic from your VPC to the Bare Metal Solution IP range. In this case, you must create an **egress** rule.



Within your Bare Metal Solution environment, if you need to control network traffic between the bare-metal servers or between the servers and destinations not on Google Cloud, you need to implement a control mechanism yourself.

To create a firewall rule in your VPC network on Google Cloud:

###  Console 

  1. Go to the **Firewall rules** page:

[Go to Firewall rules](https://console.cloud.google.com/networking/firewalls/list)

  2. Click **Create firewall rule**.

  3. Define the firewall rule.

     1. Name the firewall rule.
     2. In the **Network** field, select the network where your VM is located.
     3. In the **Targets** field, specify either **Specified target tags** or **Specified service account**.
     4. Specify the target network tag or service account in the appropriate fields.
     5. In the **Source filter** field, select **IPv4 ranges** from the drop-down
     6. In the **Source IP ranges** field, specify the IP addresses of the servers or devices in your Bare Metal Solution environment.
     7. In the **Protocols and ports** section, specify the protocols and ports that are required in your environment.
     8. Click **Create**.



###  gcloud 

The following command creates a firewall rule that defines the source by using an IP range and the target by using the network tag of an instance. Modify the command for your environment as necessary.
    
    
    [gcloud compute firewall-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) rule-name \
        --project=your-project-id \
        --direction=INGRESS \
        --priority=1000 \
        --network=your-network-name \
        --action=ALLOW \
        --rules=protocol:port \
        --source-ranges=ip-range \
        --target-tags=instance-network-tag
    

For more information about creating firewall rules, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

## Connecting to your bare-metal server

The servers in your Bare Metal Solution environment are not provisioned with external IP addresses.

After you have created a firewall rule to allow traffic into your VPC network from the Bare Metal Solution environment, you can connect to your server by using a jump host VM instance.

### Create a jump host VM instance on Google Cloud

To quickly connect to your bare-metal servers, create a Compute Engine virtual machine (VM) to use as a jump host. Create the VM in the same Google Cloud region as your Bare Metal Solution environment.

If you need a more secure connection method, see [Connect using a bastion host](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host).

To create a jump host VM instance, choose the instructions below based on the operating system you are using in your Bare Metal Solution environment.

For more information about creating Compute Engine VM instances, see [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

###  Linux 

#### Create a virtual machine instance

  1. In the Google Cloud console, go to the **VM Instances** page:

[Go to the VM Instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. In the **Name** field, specify a name for the VM instance.

  4. Under **Region** , select the region of your Bare Metal Solution environment.

  5. In the **Boot disk** section, click **Change**.

     1. In the **Operating systems** field, select an OS of your choice.
     2. In the **Version** field, select the OS version.
  6. Click **Management, security, disks, networking, sole tenancy** to expand the section.

  7. Click **Networking** to display the networking options.

     * Optionally, under **Network tags** , define one or more network tags for the instance.
     * Under **Network interfaces** , confirm that the proper VPC network is displayed.
  8. Click **Create**.




Allow a short time for the instance to start. After the instance is ready, it is listed on the **VM instances** page with a green status icon.

#### Connect to your jump host VM instance

  1. If you need to create a firewall rule to allow access to your jump host VM instance, see Firewall setup.

  2. In the Google Cloud console, go to the **VM instances** page:

[Go to the VM Instances page](https://console.cloud.google.com/compute/instances)

  3. In the list of VM instances, click SSH in the row that contains your jump host.

![The SSH button is highlighted for the jump host row in the VM
instances page](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-jump-server-ssh.png)




You now have a terminal window with your jump host VM instance, from which you can connect to your bare-metal server by using SSH.

### Logging in to a Bare Metal Solution server for the first time

###  Linux 

  1. Connect to your jump host VM instance.

  2. On the jump host VM instance, open a command-line terminal and confirm that you can reach your Bare Metal Solution server:
         
         ping bare-metal-ip

If your ping is unsuccessful, check and correct the following:

     * Your VLAN attachments are active with a `Status` of `Up`. See Create the VLAN attachments for the Cloud Interconnect connection.

     * Your VLAN attachments include a custom advertised route of `0.0.0.0/0`. See Add a custom advertised route for a default IP range to your BGP sessions.

     * If you have configured custom restrictive egress rules in your VPC, ensure they allow traffic to the Bare Metal Solution IP range. See VPC firewall setup.

  3. From the jump host VM instance, SSH into the Bare Metal Solution server by using the `customeradmin` user ID and the IP address of the server:
         
         ssh customeradmin@bare-metal-ip

  4. When prompted, enter the password provided to you by Google Cloud.

  5. On first login, you are required to change the password for your Bare Metal Solution server.

  6. Set a new password and store it in a safe location. After resetting the password, the server logs you out automatically.

  7. Log back into the Bare Metal Solution server using the `customeradmin` user ID and your new password:
         
         ssh customeradmin@bare-metal-ip

  8. We recommend that you also change the root user password. Start by logging in as the root user:
         
         sudo su -

  9. To change the root password, issue the `passwd` command and follow the prompts:
         
         passwd

  10. To return to the `customeradmin` user prompt, exit the root user prompt:
         
         exit

  11. Remember to store your passwords in a safe place for recovery purposes.

  12. Confirm that your server configuration matches your order. The things to check include:

     * The server configuration, including the number and type of CPUs, the sockets, and the memory.
     * The operating system or hypervisor software, including vendor and version.
     * The storage, including type and amount.



## Set up access to the public internet

Bare Metal Solution doesn't come with access to the internet. You can choose from the following methods to set up access depending on various factors, including your business requirements and existing infrastructure:

**Note:** [Cloud NAT](https://cloud.google.com/nat/docs/overview) feature doesn't support transitive endpoints thus it can not be used standalone to provide the internet access to the BMS server. Compute Engine VM must be used along with Cloud NAT.

  * [Access internet using a Compute Engine VM as a Proxy VM server](https://docs.cloud.google.com/data-fusion/docs/how-to/egress-control#create-proxy-vm).
  * Routing traffic through a Compute Engine VM that serves as a proxy server.

You can use a Compute Engine VM in the following ways to route the traffic:

    * Method 1: Access internet using a Compute Engine VM and Cloud NAT.
    * Method 2: Access internet using redundant Compute Engine VMs, Cloud NAT, internal passthrough Network Load Balancer, and policy-based routing.
    * Method 3: Access internet using redundant Compute Engine VMs, Cloud NAT, internal passthrough Network Load Balancer, and policy-based routing in a separate VPC.
  * Routing traffic through [Cloud VPN or Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product) to on-premises gateways to the internet.

**Note:** Make sure the cloud router is advertising the custom default route (0.0.0.0/0) towards your Bare Metal Solution for successful internet routing.



### Access internet using a Compute Engine VM and Cloud NAT

**Warning:** This method (Method 1) uses a global untagged route to direct traffic to the NAT VM. To prevent other VMs in your VPC from routing their internet traffic through this NAT VM, you must explicitly tag them (as described in step 4). This can be difficult to manage in large networks. For production environments, we strongly recommend using Method 2 (Policy-Based Routing), which isolates Bare Metal Solution traffic automatically without requiring tags on VPC VMs.

The following instructions set up a NAT gateway on a Compute Engine VM to connect the servers in a Bare Metal Solution environment to the internet for purposes such as receiving software updates.

The instructions use the default internet gateway of your VPC network to access the internet.

The Linux commands that are shown in the following instructions are for the Debian operating system. If you use a different operating system, the commands you need to use might also be different.

**Important:** For security reasons, such as to avoid exposing the VM to the internet, we recommend using the VM with [Cloud NAT] instead of an external IP address directly assigned to the VM.

In the VPC network that you are using with your Bare Metal Solution environment, perform the following steps:

  1. Open the Cloud Shell:

[Go to the Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Create and configure a Compute Engine VM to serve as a NAT gateway.

     1. Create a VM:
            
            [gcloud compute instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) instance-name \
              --machine-type=machine-type-name \
              --network vpc-network-name \
              --subnet=subnet-name \
              --can-ip-forward \
              --zone=your-zone \
              --image-family=os-image-family-name \
              --image-project=os-image-project \
              --tags=natgw-network-tag \
              --service-account=optional-service-account-email
            

In later steps, you use the network tag that you define in this step to route traffic to this VM.

If you don't specify a service account, remove the `--service-account=` flag. Compute Engine uses the default service account of the project.

     2. Create a Cloud NAT for VM internet access

Instructions to create a Cloud NAT for the VM - [HERE](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#configure-nat)

     3. SSH into the NAT gateway VM and configure the iptables:
            
            $ sudo sysctl -w net.ipv4.ip_forward=1
            
            $ sudo iptables -t nat -A POSTROUTING \
               -o $(/bin/ip -o -4 route show to default | awk '{print $5}') -j MASQUERADE
            

The first sudo command tells the kernel that you want to allow IP forwarding. The second sudo command masquerades packets received from internal instances as if they were sent from the NAT gateway instance.

     4. Check the iptables:
            
            $ sudo iptables -v -L -t nat

     5. To retain your NAT gateway settings across a reboot, execute the following commands on the NAT gateway VM:
            
            $ sudo -i
            
            
            $ echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/70-natgw.conf
            
            
            $ apt-get install iptables-persistent
            
            
            $ exit
            

  3. In Cloud Shell, create a route to `0.0.0.0/0` with the default internet gateway as the next hop. Specify the network tag that you defined in the previous step on the `--tags` argument. Assign the route a higher priority than any other default route.
         
         [gcloud compute routes create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create) default-internet-gateway-route-name \
             --destination-range=0.0.0.0/0 \
             --network=network-name \
             --priority=default-igw-route-priority \
             --tags=natgw-network-tag,default-igw-tags \
             --next-hop-gateway=default-internet-gateway
         

natgw-network-tag should be the same tag as natgw-vm is tagged in step 2. Your natvm created in step 2 will be using the default internet gateway to access the internet..

  4. Add the network tag (default-igw-tags) that you just created to any existing VMs in your VPC network that need internet access. This ensures they continue to use the default internet gateway directly and bypass the NAT VM.

  5. Optional: Remove routes to the internet that existed before the route you created in the previous step, including those created by default.

  6. Confirm that any existing VMs in your network and the NAT gateway VM can access the internet by pinging an external IP address, such as 8.8.8.8, the Google DNS, from each VM.

  7. Create a default route to `0.0.0.0/0` with the NAT gateway VM as the next hop. Give the route a lower priority than priority that you specified for the first route that you created.

**Note:** If you deploy a NAT gateway in a shared VPC service project, use the `--next-hop-address` option in place of the `--next-hop-instance` and `--next-hop-instance-zone` options, then issue the command against the host project. For more details, see [ Considerations for next hop instances](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-vm-only).**Warning:** Before creating a following natgw-route make sure that all your existing VMs tagged with default-igw-tags and uses the default-internet-gateway to access the internet.
         
         [gcloud compute routes create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create) natgw-route-name \
             --destination-range=0.0.0.0/0 \
             --network=network-name \
             --priority=natgw-route-priority \
             --next-hop-instance=natgw-vm-name \
             --next-hop-instance-zone=natgw-vm-zone
         

**Note:** Packets should be routed to the default-internet-gateway first so the natgw-route-priority must be higher than default-igw-route-priority in value (lower priority). 
  8. Log in to your Bare Metal Solution servers and ping an external IP address to confirm that they can access the internet.

If the ping is not successful, make sure that you have created a firewall rule that allows access from your Bare Metal Solution environment to your VPC network.




### Access internet using redundant Compute Engine VMs, Cloud NAT, internal passthrough Network Load Balancer, and policy-based routing

This section shows how to set up internal passthrough Network Load Balancer with Compute Engine VMs and Cloud NAT configured as the backend. Policy-based routing forwards the internet traffic to the frontend of the internal passthrough Network Load Balancer.

The following diagram shows this setup.

![Setup for using redundant Compute Engine VMs, Cloud NAT, internal passthrough Network Load Balancer, and policy-based routing to access internet.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-single-vpc-pbr.svg)

In the VPC network of your Bare Metal Solution environment, perform the following steps:

  1. Create and configure a Compute Engine VM and the Cloud NAT to serve as a NAT gateway. Complete the steps described in [Method 1: Using a single Compute Engine VM and Cloud NAT](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-access-internet-vm-nat).

**Note:** In this solution, two or more Compute Engine VMs can be created and put in the instance group for the redundancy.

A lightweight http server can be used to perform a health check for internal passthrough Network Load Balancer.
         
         # Installing http server
         
         sudo yum install httpd
         sudo systemctl restart httpd
         
         # Testing
         
         curl http://127.0.0.1:80
         
         
         

  2. Create an instance group.
         
         gcloud compute instance-groups unmanaged create INSTANCE_GROUP_NAME --project=PROJECT_ID --zone=ZONE
         

Replace the following:

     * INSTANCE_GROUP_NAME: the name of the instance group
     * PROJECT_ID: the ID of the project
     * ZONE: the zone in which to create the instance group
  3. Add the VM to the instance group.
         
         gcloud compute instance-groups unmanaged add-instances INSTANCE_GROUP_NAME --project=PROJECT_ID --zone=ZONE --instances=VM_NAME
         

Replace the following:

     * INSTANCE_GROUP_NAME: the name of the instance group
     * PROJECT_ID: the ID of the project
     * ZONE: the zone in which to create the instance group
     * VM_NAME: the name of the VM
  4. Create an internal passthrough Network Load Balancer:

#### Start your configuration

     1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

     2. Click **Create load balancer**.
     3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
     4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
     5. For **Public facing or internal** , select **Internal** and click **Next**.
     6. Click **Configure**.

#### Basic configuration

     1. Set **Load balancer name**.
     2. Select a **Region**.
     3. Select a **Network**.

#### Configure the backend and frontend

     1. Click **Backend configuration** and make the following changes:

        1. To add backends, do the following: 
           1. Under **New Backend** , to handle IPv4 traffic only, select the **IP stack type** as **IPv4 (single-stack)**.
           2. Select your instance group and click **Done**.
        2. Select a health check. You can also **create a health check** , enter the following information, and click **Save** :

           * **Name** : Enter a name for the health check.
           * **Protocol** : `HTTP`
           * **Port** : `80`
           * **Proxy protocol** : `NONE`
           * **Request path** : `/`
**Note:** If you use the Google Cloud console to create your load balancer, the health check is global. If you want to create a regional health check, use `gcloud` or the API.
     2. Click **Frontend configuration**. In the **New Frontend IP and port** section, make the following changes:

        1. **Ports** : Choose **All** , and enter `80,8008,8080,8088` for the **Port number**.
        2. Click **Done**.
     3. Click **Review and finalize**.

     4. Review your load balancer configuration settings.

     5. Click **Create**.

  5. Create a policy-based route for the internet.
         
         gcloud network-connectivity policy-based-routes create ROUTE_NAME \
          --source-range=SOURCE_RANGE \
          --destination-range=0.0.0.0/0 \
          --ip-protocol=ALL \
          --network="projects/PROJECT_ID/global/networks/NETWORK" \
          --next-hop-ilb-ip=NEXT_HOP \
          --description="DESCRIPTION" \
          --priority=PRIORITY \
          --interconnect-attachment-region=REGION
         

Replace the following:

     * ROUTE_NAME: the name of the policy-based route
     * SOURCE_RANGE: the source IP CIDR range. In this case, this is the Bare Metal Solution IP address.
     * PROJECT_ID: the ID of the project
     * NETWORK: the network to which the policy-based route is applied
     * NEXT_HOP: the IPv4 address of the route's next hop. In this case, this is the IP address of the frontend of the internal passthrough Network Load Balancer.
     * DESCRIPTION: a description of the route
     * PRIORITY: the priority of the policy-based route compared to other policy-based routes
     * REGION: the region of the VLAN attachment
  6. Create a policy-based route to skip the internet policy-based route for on-premises subnets and local subnets.
         
         gcloud network-connectivity policy-based-routes create ROUTE_NAME \
          --source-range=SOURCE_RANGE/32 \
          --destination-range=DESTINATION_RANGE \
          --ip-protocol=ALL \
          --network="projects/PROJECT_ID/global/networks/VPC_NAME" \
          --next-hop-other-routes="DEFAULT_ROUTING" \
          --description="DESCRIPTION" \
          --priority=PRIORITY \
          --interconnect-attachment-region=REGION
         

Replace the following:

     * ROUTE_NAME: the name of the policy-based route
     * SOURCE_RANGE: the source IP CIDR range. In this case, this is the Bare Metal Solution IP address.
     * DESTINATION_RANGE: the destination IP CIDR range. In this case, this is the on-premise subnet or a local subnet.
     * PROJECT_ID: the ID of the project
     * VPC_NAME: the name of the VPC network
     * DESCRIPTION: a description of the route
     * PRIORITY: the priority of the policy-based route compared to other policy-based routes. The priority of this policy-based route must be less than or equal to the policy-based route for the internet.
     * REGION: the region of the VLAN attachment
  7. Update the firewall to allow HTTP port 80 on the VM.

The health check might fail if you don't update the firewall.




### Access internet using redundant Compute Engine VMs, Cloud NAT, internal passthrough Network Load Balancer, and policy-based routing in a separate VPC

If you don't want to add policy-based routes for local subnets, you can use this method to access the internet. However, to use this method, you need to create a VLAN attachment and a VPC to connect the Bare Metal Solution.

The following diagram shows this setup.

![Set up for using redundant Compute Engine VMs, Cloud NAT, internal passthrough Network Load Balancer, and policy-based routing in a separate VPC.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-internet-vpc.svg)

Follow these steps:

  1. Create a VPC network for the internet.
         
         gcloud compute networks create NETWORK --project=PROJECT_ID --subnet-mode=custom --mtu=MTU --bgp-routing-mode=regional
         

Replace the following:

     * NETWORK: the name for the VPC network.
     * PROJECT_ID: the ID of the project
     * MTU: the maximum transmission unit (MTU), which is the largest packet size of the network
  2. Create a subnet.
         
         gcloud compute networks subnets create SUBNET_NAME --project=PROJECT_ID --range=RANGE --stack-type=IPV4_ONLY --network=NETWORK --region=REGION
         

Replace the following:

     * SUBNET_NAME: the name for the subnet
     * PROJECT_ID: the ID of the project
     * RANGE: the IP space allocated to this subnet in CIDR format
     * NETWORK: the VPC network to which the subnet belongs
     * REGION: the region of the subnet
  3. Create two Cloud Routers for the redundancy and advertisements.
         
         gcloud compute routers create ROUTER_NAME --project=PROJECT_ID --region=REGION --network=NETWORK --advertisement-mode=custom --set-advertisement-ranges=0.0.0.0/0
         

Replace the following:

     * ROUTER_NAME: the name of the router
     * PROJECT_ID: the ID of the project
     * REGION: the region of the router
     * NETWORK: the VPC network for this router
  4. Create four VLAN attachments, two for each Cloud Router.

For instructions, see [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).

  5. After the VLAN attachments are active, follow the steps in Method 2: Using redundant Compute Engine VMs, Cloud NAT, internal passthrough Network Load Balancer, and policy-based routing to configure the internet infrastructure. However, for this setup, don't configure the policy-based route for local traffic. Only create a policy-based route for the internet in a routing table of the VPC network.


**Note:** If the BGP session in an existing local VPC network advertises a default route (0.0.0.0/0) towards the Bare Metal Solution, it should be changed in order for this method to work. Only an internet VPC network should advertise the default route (0.0.0.0/0) towards the Bare Metal Solution through a newly created BGP session. The BGP session for local VPC network should advertise only a local subnet including on-premises and VPC subnets.

## Set up access to Google Cloud APIs and services

Bare Metal Solution doesn't come with access to Google Cloud services. You can choose how to implement access depending on various factors, including your business requirements and existing infrastructure.

**Note:** Most of the Google Cloud services that support on-prem environments can be configured for access from Bare Metal Solution. Follow the on-prem configuration guide for the Google Cloud service that you want to configure for Bare Metal Solution.

You can access Google Cloud APIs and services privately from your Bare Metal Solution environment.

You set up private access to the Google Cloud APIs and services from a Bare Metal Solution environment as you would for an on-premises environment.

Follow the instructions for on-premises environments in [Configuring Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

The instructions guide you through the following high-level steps:

  1. Configuring routes for the Google API traffic.
  2. Configuring your Bare Metal Solution DNS to resolve `*.googleapis.com` as a `CNAME` to `restricted.googleapis.com`.



## What's next

After you have set up your Bare Metal Solution environment, you can install your workloads.

If you plan to run Oracle databases on the servers in your Bare Metal Solution environment, you can use the open source [Toolkit for Bare Metal Solution](https://github.com/google/bms-toolkit) to install your Oracle software.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
