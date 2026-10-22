---
url: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg/
title: Set up a regional external passthrough Network Load Balancer with zonal NEGs \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:26.604334+00:00
---

# Set up a regional external passthrough Network Load Balancer with zonal NEGs  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external passthrough Network Load Balancer with zonal NEGs Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to deploy a regional external passthrough Network Load Balancer with zonal network endpoint group (NEG) backends. Zonal NEGs with `GCE_VM_IP` endpoints let you do the following:

  * Forward packets to the non-`nic0` network interfaces of virtual machine (VM) instances by representing a network interface of a VM instance as the backend endpoint.
  * Create a flexible set of backend endpoints where an endpoint can be attached to multiple NEGs, and each NEG can have a different but possibly overlapping set of endpoints.



Before following this document, familiarize yourself with the following:

  * [Zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#zonal-negs) in the Backend service-based regional external passthrough Network Load Balancer overview
  * [Zonal network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts)



## Permissions

To follow these steps, you need to create instances and modify a network in a project. You must either be a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Compute Network Admin (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Add and remove firewall rules | [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Create instances | [Compute Instance Admin (`roles/compute.instanceAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
  
For more information, see the following pages:

  * [Roles and permissions](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Setup overview

This document shows you how to configure and test a regional external passthrough Network Load Balancer that uses `GCE_VM_IP` zonal NEG backends. The steps in this section describe how to configure the following:

  1. A VPC network called `lb-network` with a custom subnet.
  2. Firewall rules that allow incoming connections to backend VMs.
  3. Four VMs: 
     * VMs `vm-a1` and `vm-a2` in zone `us-central1-a`
     * VMs `vm-c1` and `vm-c2` in zone `us-central1-c`
  4. Two backend zonal NEGs, `neg-a` in zone `us-central1-a`, and `neg-c` in zone `us-central1-c`. Each NEG has the following endpoints: 
     * `neg-a` contains these two endpoints: 
       * `nic1` of VM `vm-a1` identified by its primary internal IP address
       * `nic1` of VM `vm-a2` identified by its primary internal IP address
     * `neg-c` contains these two endpoints: 
       * `nic1` of VM `vm-c1` identified by its primary internal IP address
       * `nic1` of VM `vm-c2` identified by its primary internal IP address
  5. The following load balancer components: 
     * An external backend service in the `us-central1` region to manage connection distribution to the two zonal NEGs
     * An external forwarding rule and IP address for the frontend of the load balancer
  6. Source-based policy routing in the guest OS of the backend VMs if the non-`nic0` interface (in this example, `nic1`) receives the load balancer traffic.



The regional external passthrough Network Load Balancer is a regional load balancer. All load balancer components (backend VMs, backend service, and forwarding rule) must be in the same region.

The architecture for this example looks like this:

[ ![Regional external passthrough Network Load Balancer with zonal NEGs.](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-zonal-negs.svg)](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-zonal-negs.svg) Regional external passthrough Network Load Balancer with zonal NEGs (click to enlarge).

## Before you begin

Install the Google Cloud CLI. For a complete overview of the tool, see the [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). You can find commands related to load balancing in the [API and gcloud references](https://docs.cloud.google.com/load-balancing/docs/apis).

If you haven't run the gcloud CLI previously, first run the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.

This page assumes that you are familiar with [bash](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)).

## Set up the network and subnets

The example on this page uses a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`. If you only want to handle IPv4 traffic, you can use an auto mode VPC network. However, subnets with IPv6 address ranges aren't supported on auto mode VPC networks. Subnets with IPv6 address ranges are supported on custom mode VPC networks only.

In this example, subnets of the following [stack types](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types) are created:

Subnet ranges | Stack type  
---|---  
Only IPv4 subnet ranges | `IPV4_ONLY` (single-stack)  
Both IPv4 and IPv6 subnet ranges | `IPV4_IPV6` (dual-stack)  
Only IPv6 subnet ranges | `IPV6_ONLY` (single-stack)  
  
For dual-stack and IPv6-only subnets that use an IPv6 address range, you need to choose an IPv6 access type for the subnet. The IPv6 access type determines whether the subnet is configured with [internal IPv6 addresses](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6) or [external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6). For this example, the subnet's `ipv6-access-type` parameter is set to `EXTERNAL`.

A subnet with an external IPv6 address range, that is, whose `ipv6-access-type` parameter is set to `EXTERNAL`, can also be used to source a forwarding rule's external IPv6 address. For more information, see [IP address specifications for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications).

**Note:** An IPv6 forwarding rule with a BYOIP address doesn't require a network or subnet. For more information, see [Create an IPv6 forwarding rule with BYOIP](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols#byoip-ipv6).

The backends and the load balancer components used for this example are located in this region and subnet:

  * Region: `us-central1`
  * Subnet: `lb-subnet`, with primary IPv4 address range 10.1.2.0/24. Although you choose which IPv4 address range is configured on the subnet, the IPv6 address range is assigned automatically. Google provides a fixed size (`/64`) IPv6 CIDR block.



To create the example network and subnet, follow these steps.

###  Console 

To create a dual-stack subnet, use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. Set **Subnet creation mode** to **Custom**.

  5. In the **Subnets** section, click **Add subnet** and configure the following fields:

     * **Name** : `lb-subnet`
     * **Region** : `us-central1`
     * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
     * **IPv4 range** : `10.1.2.0/24`   
Although you can configure an IPv4 range of addresses for the subnet, you cannot choose the range of the IPv6 addresses for the subnet. Google provides a fixed size (`/64`) IPv6 CIDR block.
     * **IPv6 access type** : **External**
     * Click **Done**
  6. Click **Create**.




To create an IPv4-only subnet, use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. Set **Subnet creation mode** to **Custom**.

  5. In the **Subnets** section, click **Add subnet** and configure the following fields:

     * **Name** : `lb-subnet`
     * **Region** : `us-central1`
     * **IP stack type** : **IPv4 (single-stack)**
     * **IPv4 range** : `10.1.2.0/24`
  6. Click **Create**.




To create an IPv6-only subnet, use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. Set **Subnet creation mode** to **Custom**.

  5. In the **Subnets** section, click **Add subnet** and configure the following fields:

     * **Name** : `lb-subnet`
     * **Region** : `us-central1`
     * **IP stack type** : **IPv6 (single-stack)**
     * **IPv6 access type** : **External**
  6. Click **Create**.




###  gcloud 

  1. Create the custom mode VPC network:
         
         gcloud compute networks create lb-network \
             --subnet-mode=custom
         

  2. Within the `lb-network` network, create a subnet for backends in the `us-central1` region.

To create a dual-stack subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet \
               --stack-type=IPV4_IPV6 \
               --ipv6-access-type=EXTERNAL \
               --network=lb-network \
               --range=10.1.2.0/24 \
               --region=us-central1
         

To create an IPv4-only subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet \
               --network=lb-network \
               --range=10.1.2.0/24 \
               --region=us-central1
         

To create an IPv6-only subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet \
             --stack-type=IPV6_ONLY \
             --ipv6-access-type=EXTERNAL \
             --network=lb-network \
             --region=us-central1
         




## Create VMs and network endpoint groups

To demonstrate the regional nature of regional external passthrough Network Load Balancers, this example uses two zonal NEG backends in two different zones. Traffic is load-balanced across both NEGs, and across endpoints within each NEG.

### Create VMs

For this load balancing scenario, you create four VMs and install an Apache web server on each instance. The web server listens on TCP port 80. By default, Apache is configured to bind to any IP address. Regional external passthrough Network Load Balancers deliver packets by preserving the destination IP address.

For instructional simplicity, these backend VMs run Debian GNU Linux 10.

To handle both IPv4 and IPv6 traffic, configure the `stack-type` of the backend VM's load balancer network interface (in this example, `nic1`) to `IPV4_IPV6`. The load balancer network interface also inherits the `ipv6-access-type` setting (in this example, `EXTERNAL`) from the subnet. For more details about IPv6 requirements, see the [Regional external passthrough Network Load Balancer overview: Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule).

To use existing VMs as backends, update the VMs to be dual-stack by using the [`gcloud compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update).

Instances that participate as backend VMs for regional external passthrough Network Load Balancers must run the appropriate [Linux guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#linux), [Windows guest environment](https://github.com/GoogleCloudPlatform/compute-image-windows), or other processes that provide equivalent capability.

Each VM is created with two network interfaces, `nic0` and `nic1`. This tutorial uses `nic1`, which is associated with the `lb-network` VPC network and `lb-subnet` subnet. Use this `lb-network` network and `lb-subnet` subnet to create the zonal NEGs later in this procedure.

###  Console 

**Create VMs**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat the following steps to create four VMs, using the following name and zone combinations:

     * Name: `vm-a1`, zone: `us-central1-a`
     * Name: `vm-a2`, zone: `us-central1-a`
     * Name: `vm-c1`, zone: `us-central1-c`
     * Name: `vm-c2`, zone: `us-central1-c`
  3. Click **Create instance**.

  4. Set the **Name** as indicated previously.

  5. For the **Region** , choose `us-central1`, and choose a **Zone** as indicated previously.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. If necessary, click **Choose** to change the image.

  7. Click **Advanced options** and make the following changes:

     * Click **Networking** and add the following **Network tags** : `lb-tag`
     * For **Network interfaces** , click **Add network interface** and make the following changes:

For **IPv4 and IPv6 backends** :

       * **Network** : `lb-network`
       * **Subnet** : `lb-subnet`
       * **IP stack type** : `IPv4 and IPv6 (dual-stack)`
       * **Primary internal IP** : Ephemeral (automatic)
       * **External IPv4 address** : Ephemeral (automatic)
       * **External IPv6 address** : Ephemeral (automatic)

For **IPv4-only backends** :

       * **Network** : `lb-network`
       * **Subnet** : `lb-subnet`
       * **IP stack type** : `IPv4 (single-stack)`
       * **Primary internal IP** : Ephemeral (automatic)
       * **External IP** : Ephemeral

For **IPv6-only backends** :

       * **Network** : `lb-network`
       * **Subnet** : `lb-subnet`
       * **IP stack type** : `IPv6 (single-stack)`
       * **External IPv6 address** : Ephemeral (automatic)

Then click **Done**.

     * Click **Management**. In the **Startup script** field, copy and paste the following script contents. The script contents are identical for all four VMs:
           
           #! /bin/bash
           apt-get update
           apt-get install apache2 -y
           a2ensite default-ssl
           a2enmod ssl
           vm_hostname="$(curl -H "Metadata-Flavor:Google" \
           http://metadata.google.internal/computeMetadata/v1/instance/name)"
           echo "Page served from: $vm_hostname" | \
           tee /var/www/html/index.html
           systemctl restart apache2
           

  8. Click **Create**.




###  gcloud 

Create the four VMs by running the following command four times, using these four combinations for `VM_NAME` and `ZONE`. The script contents are identical for all four VMs.

  * `VM_NAME`: `vm-a1` and `ZONE`: `us-central1-a`
  * `VM_NAME`: `vm-a2` and `ZONE`: `us-central1-a`
  * `VM_NAME`: `vm-c1` and `ZONE`: `us-central1-c`
  * `VM_NAME`: `vm-c2` and `ZONE`: `us-central1-c`



To create backend VMs with _dual-stack_ network interfaces, use the following command.

**Note:** Set `--ipv6-network-tier` to `PREMIUM` only if you are creating the VMs in subnets with `ipv6-access-type` set to `EXTERNAL`. Omit the flag if the subnet's `ipv6-access-type` is `INTERNAL`.

The dual-stack configuration applies to the load balancer network interface (`nic1`) and not the default network interface (`nic0`) in the default subnet of the VPC network.
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=lb-tag \
        --network-interface=network=default,subnet=default,stack-type=IPV4_ONLY \
        --network-interface=network=lb-network,subnet=lb-subnet,stack-type=IPV4_IPV6,ipv6-network-tier=PREMIUM \
        --metadata=startup-script='#! /bin/bash
        apt-get update
        apt-get install apache2 -y
        a2ensite default-ssl
        a2enmod ssl
        vm_hostname="$(curl -H "Metadata-Flavor:Google" \
        http://metadata.google.internal/computeMetadata/v1/instance/name)"
        echo "Page served from: $vm_hostname" | \
        tee /var/www/html/index.html
        systemctl restart apache2'
    

To create backend VMs with _IPv4-only_ network interfaces, use the following command.
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=lb-tag \
        --network-interface=network=default,subnet=default,stack-type=IPV4_ONLY \
        --network-interface=network=lb-network,subnet=lb-subnet,stack-type=IPV4_ONLY \
        --metadata=startup-script='#! /bin/bash
        apt-get update
        apt-get install apache2 -y
        a2ensite default-ssl
        a2enmod ssl
        vm_hostname="$(curl -H "Metadata-Flavor:Google" \
        http://metadata.google.internal/computeMetadata/v1/instance/name)"
        echo "Page served from: $vm_hostname" | \
        tee /var/www/html/index.html
        systemctl restart apache2'
    

To create backend VMs with _IPv6-only_ network interfaces, use the following command.

**Note:** Set `--ipv6-network-tier` to `PREMIUM` only if you are creating the VMs in subnets with `ipv6-access-type` set to `EXTERNAL`. Omit the flag if the subnet's `ipv6-access-type` is `INTERNAL`.

The `IPV6_ONLY` stack type configuration applies to the load balancer network interface (`nic1`) and not the default network interface (`nic0`) in the default subnet of the VPC network.
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=lb-tag \
        --network-interface=network=default,subnet=default,stack-type=IPV4_ONLY \
        --network-interface=network=lb-network,subnet=lb-subnet,stack-type=IPV6_ONLY,ipv6-network-tier=PREMIUM \
        --metadata=startup-script='#! /bin/bash
        apt-get update
        apt-get install apache2 -y
        a2ensite default-ssl
        a2enmod ssl
        vm_hostname="$(curl -H "Metadata-Flavor:Google" \
        http://metadata.google.internal/computeMetadata/v1/instance/name)"
        echo "Page served from: $vm_hostname" | \
        tee /var/www/html/index.html
        systemctl restart apache2'
    

### Create zonal NEGs with `GCE_VM_IP` endpoints

The NEGs must be created in the same zones as the VMs created in the previous step. This example also creates the NEG in the `lb-network` VPC network and `lb-subnet` subnet that are associated with `nic1` of the VMs created in the previous step. Therefore, the endpoints of the NEG are going to be on `nic1` of the VMs.

###  Console 

To create a zonal network endpoint group, use the following steps:

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click **Create network endpoint group**.

  3. For **Name** , enter `neg-a`.

  4. For **Network endpoint group type** , select **Zonal NEG**.

  5. For **Endpoints type** , select **GCE_VM_IP**.

  6. For **Network** , select **lb-network**.

  7. For **Subnetwork** , select **lb-subnet**.

  8. For **Zone** , select **us-central1-a**.

  9. Click **Create**.

  10. Repeat these steps to create a second zonal NEG called `neg-c`, in the **us-central1-c** zone.




To add endpoints to the zonal NEG, use the following steps:

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Click the name of the first network endpoint group created in the previous step (**neg-a**). You see the **Network endpoint group details** page.

  3. In the **Network endpoints in this group** section, click **Add network endpoint**.

     1. In the **Add network endpoint** page, click **VM instance** and select **vm-a1** to add its internal IP addresses as network endpoints.
     2. Click **Create**.
     3. Click **Add network endpoint** and under **VM instance** select **vm-a2**.
     4. Click **Create**.
  4. Click the name of the second network endpoint group created in the previous step (**neg-c**). You see the **Network endpoint group details** page.

  5. In the **Network endpoints in this group** section, click **Add network endpoint**. You see the **Add network endpoint** page.

     1. Click **VM instance** and select **vm-c1** to add its internal IP addresses as network endpoints.
     2. Click **Create**.
     3. Click **Add network endpoint** and under **VM instance** select **vm-c2**.
     4. Click **Create**.



###  gcloud 

  1. Create a `GCE_VM_IP` zonal NEG called `neg-a` in `us-central1-a` using the [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create) command:
         
         gcloud compute network-endpoint-groups create neg-a \
             --network-endpoint-type=gce-vm-ip \
             --zone=us-central1-a \
             --network=lb-network \
             --subnet=lb-subnet
         

  2. Add endpoints to `neg-a`:
         
         gcloud compute network-endpoint-groups update neg-a \
             --zone=us-central1-a \
             --add-endpoint='instance=vm-a1' \
             --add-endpoint='instance=vm-a2'
         

  3. Create a `GCE_VM_IP` zonal NEG called `neg-c` in `us-central1-c` using the [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create) command:
         
         gcloud compute network-endpoint-groups create neg-c \
             --network-endpoint-type=gce-vm-ip \
             --zone=us-central1-c \
             --network=lb-network \
             --subnet=lb-subnet
         

  4. Add endpoints to `neg-c`:
         
         gcloud compute network-endpoint-groups update neg-c \
             --zone=us-central1-c \
             --add-endpoint='instance=vm-c1' \
             --add-endpoint='instance=vm-c2'
         




## Configuring firewall rules

Create firewall rules that allow external traffic (which includes health check probes) to reach the backend instances.

This example creates a firewall rule that allows TCP traffic from _all_ source ranges to reach your backend instances on port 80. If you want to create separate firewall rules specifically for the health check probes, use the source IP address ranges documented in the [Health checks overview: Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

###  Console 

In the Google Cloud console, go to the **Firewall** page.

[Go to Firewall](https://console.cloud.google.com/networking/firewalls/list)

To allow **IPv4 traffic** , perform the following steps:

  1. Click **Create firewall rule**.
  2. Enter a **Name** : `allow-network-lb-ipv4`.
  3. For **Network** , select **lb-network**.
  4. For **Targets** , select **Specified target tags**.
  5. For the **Target tags** field, enter `lb-tag`.
  6. For **Source filter** , select **IPv4 ranges**.
  7. Set **Source IPv4 ranges** to `0.0.0.0/0`. This allows IPv4 traffic from any source. This also allows Google's health check probes to reach the backend instances.
  8. For **Specified protocols and ports** , select **TCP** and enter `80`.
  9. Click **Create**.



To allow **IPv6 traffic** , perform the following steps:

  1. Click **Create firewall rule** again.
  2. Enter a **Name** : `allow-network-lb-ipv6`.
  3. For **Network** , select **lb-network**.
  4. For **Targets** , select **Specified target tags**.
  5. For the **Target tags** field, enter `lb-tag`.
  6. For **Source filter** , select **IPv6 ranges**.
  7. Set **Source IPv6 ranges** to `::/0`. This allows IPv6 traffic from any source. This also allows Google's health check probes to reach the backend instances.
  8. For **Specified protocols and ports** , select **TCP** and enter `80`.
  9. Click **Create**.



###  gcloud 

To allow **IPv4 traffic** , run the following command:
    
    
    gcloud compute firewall-rules create allow-network-lb-ipv4 \
        --network=lb-network \
        --target-tags=lb-tag \
        --allow=tcp:80 \
        --source-ranges=0.0.0.0/0
    

To allow **IPv6 traffic** , run the following command:
    
    
    gcloud compute firewall-rules create allow-network-lb-ipv6 \
        --network=lb-network \
        --target-tags=lb-tag \
        --allow=tcp:80 \
        --source-ranges=::/0
     

## Configure the load balancer

Next, set up the load balancer.

When you configure the load balancer, your VMs receive packets that are destined for the static external IP address you configure. If you are using an [image provided by Compute Engine](https://docs.cloud.google.com/compute/docs/images#os-compute-support), your instances are automatically configured to handle this IP address. If you are using any other image, you must configure this address as an alias on `eth1` or as a loopback on each instance.

To set up the load balancer, use the following the instructions.

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  6. Click **Configure**.



#### Backend configuration

  1. On the **Create external passthrough Network Load Balancer** page, enter the name `network-lb-zonal-neg` for the new load balancer.
  2. In the **Region** list, select `us-central1`.
  3. Click **Backend configuration**. The load balancer name that you entered previously appears, but is not modifiable.
  4. In the **Backend type** list, select **Zonal network endpoint group**.
  5. On the **Backend configuration** page, do the following: 
     1. In the **Health check** list, click **Create a health check** , and then enter the following information: 
        * **Name** : `tcp-health-check`
        * **Protocol** : **TCP**
        * **Port** : `80`
     2. Click **Create**.
     3. In the **Network endpoint group** list, select `neg-a`, and then click **Done**.
     4. Click **Add backend** and repeat the previous step to add `neg-c`.
     5. Click **Save**.
  6. Verify that there is a blue checkmark next to **Backend configuration** before continuing.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. For **Name** , enter `netlb-forwarding-rule`.
  3. To handle IPv4 traffic, use the following steps: 
     1. For **IP version** , select **IPv4**.
     2. For **IP address** , click the drop-down menu and select **Create IP address**. 
        1. On the **Reserve a new static IP address** page, for **Name** , enter `netlb-ipv4-address`.
        2. Click **Reserve**.
     3. For **Ports** , choose **Single**. For **Port number** , enter `80`.
     4. Click **Done**.
  4. To handle IPv6 traffic, use the following steps:

     1. For **IP version** , select **IPv6**.
     2. For **Subnetwork** , select **lb-subnet**.
     3. For **IPv6 range** , click the drop-down menu and select **Create IP address**. 
        1. On the **Reserve a new static IP address** page, for **Name** , enter `netlb-ipv6-address`.
        2. Click **Reserve**.
     4. For **Ports** , choose **Single**. For **Port number** , enter `80`.
     5. Click **Done**.

A blue circle with a checkmark to the left of **Frontend configuration** indicates a successful setup.




#### Review the configuration

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.

On the load balancing page, under the Backend column for your new load balancer, you should see a green checkmark showing that the new load balancer is healthy.




###  gcloud 

  1. Reserve a static external IP address.

**For IPv4 traffic**

Create a [static external IPv4 address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) for your load balancer.
         
         gcloud compute addresses create netlb-ipv4-address \
             --region=us-central1
         

**For IPv6 traffic**

Create a [static external IPv6 address range](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) for your load balancer. The subnet used must be a dual-stack subnet with an external IPv6 range.
         
         gcloud compute addresses create netlb-ipv6-address \
             --region=us-central1 \
             --subnet=lb-subnet \
             --ip-version=IPV6 \
             --endpoint-type=NETLB
         

  2. Create a TCP health check.
         
         gcloud compute health-checks create tcp tcp-health-check \
             --region=us-central1 \
             --port=80
         

  3. Create a backend service.
         
         gcloud compute backend-services create networklb-backend-service \
             --protocol=TCP \
             --health-checks=tcp-health-check \
             --health-checks-region=us-central1 \
             --region=us-central1
         

  4. Add the two zonal NEGs, `neg-a` and `neg-c`, to the backend service:
         
         gcloud compute backend-services add-backend networklb-backend-service \
             --region=us-central1 \
             --network-endpoint-group=neg-a \
             --network-endpoint-group-zone=us-central1-a
         
         
         gcloud compute backend-services add-backend networklb-backend-service \
             --region=us-central1 \
             --network-endpoint-group=neg-c \
             --network-endpoint-group-zone=us-central1-c
         

  5. Create the forwarding rules depending on whether you want to handle IPv4 traffic or IPv6 traffic. Create both forwarding rules to handle both types of traffic.

**For IPv4 traffic**

Create a forwarding rule to route incoming TCP traffic to the backend service. Use the IPv4 address reserved in step 1 as the static external IP address of the load balancer.
         
         gcloud compute forwarding-rules create forwarding-rule-ipv4 \
               --load-balancing-scheme=EXTERNAL \
               --region=us-central1 \
               --ports=80 \
               --address=netlb-ipv4-address \
               --backend-service=networklb-backend-service
         

**For IPv6 traffic**

Create a forwarding rule to handle IPv6 traffic. Use the IPv6 address range reserved in step 1 as the static external IP address of the load balancer. The subnet used must be a dual-stack subnet with an external IPv6 subnet range.
         
         gcloud compute forwarding-rules create forwarding-rule-ipv6 \
               --load-balancing-scheme=EXTERNAL \
               --region=us-central1 \
               --network-tier=PREMIUM \
               --ip-version=IPV6 \
               --subnet=lb-subnet \
               --address=netlb-ipv6-address \
               --ports=80 \
               --backend-service=networklb-backend-service
         




## Configure policy routing in the guest OS

**Note:** Policy routing in the guest OS is only required when the zonal NEG endpoints are associated with a secondary (non-`nic0`) network interface (such as `nic1` in this tutorial). If your zonal NEG endpoints point to the VM's primary network interface (`nic0`), the VM's default routing table automatically routes egress traffic through `nic0`, in which case you can skip this section.

For backend service-based regional external passthrough Network Load Balancers with `GCE_VM_IP` zonal NEG backends, the load balancer delivers packets (both client traffic and [health check probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest)) with the destination IP address set to the load balancer's forwarding rule IP address. The packets arrive through the network interface in the VPC subnet associated with the NEG (in this example, `nic1` in `lb-subnet`).

By default, a Linux-based Google Cloud VM has a single main routing table where the default route points to the primary interface, `nic0` (`ens4`). When the backend VM replies to requests addressed to the load balancer's IP address received on `nic1` (`ens5`), the VM tries to send the replies back through the default gateway on `nic0`, resulting in asymmetric routing and causing connections to fail.

To resolve this, you must set up source-based policy routing in the guest OS of each backend VM that serves as an endpoint for the NEG. This ensures that outgoing responses to both client traffic and health check probes (with source IP set to the load balancer's IP address) exit through the same network interface (`nic1`) on which they were received.

For each backend VM (`vm-a1`, `vm-a2`, `vm-c1`, and `vm-c2`), perform the following steps:

  1. Connect to the backend VM by using [SSH](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms).

  2. Create the following variables.

**For IPv4 traffic** :

     * `NIC1_GATEWAY_IPV4`: IPv4 address of the gateway for `nic1`
     * `LB_IPV4`: IPv4 address of the load balancer's forwarding rule.
    
    NIC1_GATEWAY_IPV4=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/1/gateway)
    LB_IPV4=LOAD_BALANCER_EXTERNAL_IPV4
    

Replace LOAD_BALANCER_EXTERNAL_IPV4 with the IPv4 address configured for the forwarding rule of the load balancer.

**For IPv6 traffic** :

     * `NIC1_GATEWAY_IPV6`: IPv6 address of the gateway for `nic1`
     * `LB_IPV6`: IPv6 address of the load balancer's forwarding rule.
    
    NIC1_GATEWAY_IPV6=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/1/gateway-ipv6)
    LB_IPV6=LOAD_BALANCER_EXTERNAL_IPV6
    

Replace LOAD_BALANCER_EXTERNAL_IPV6 with the IPv6 address configured for the forwarding rule of the load balancer.

  3. Add the policy routing rules.

Run the following commands to create a custom routing table and add the necessary routing rules.

     1. Create a custom routing table named `route-nic1`. This table will hold routes specific to the `nic1` interface.
            
            echo "1 route-nic1" | sudo tee -a /etc/iproute2/rt_tables
            

     2. Add a default route to the `route-nic1` table. This route directs traffic to the gateway of `nic1` through the interface corresponding to `nic1` (typically `ens5` or `eth1`).

**For IPv4 traffic** :
            
            sudo ip route add default via $NIC1_GATEWAY_IPV4 dev ens5 table route-nic1
            

**For IPv6 traffic** :
            
            sudo ip -6 route add default via $NIC1_GATEWAY_IPV6 dev ens5 table route-nic1
            

**Note:** Replace `ens5` with the actual interface name for `nic1` on your VM, if it differs.
     3. Add a policy routing rule to decide when to use the `route-nic1` table.

Because passthrough load balancers preserve the destination IP address (the load balancer's VIP) when forwarding packets to the VM, the VM must respond with the source IP address set to the load balancer's IP address for both client traffic and health check probes.

Add a rule instructing the VM to use the `route-nic1` routing table for any outgoing packets with a source IP address matching the load balancer's IP address. This ensures that all responses to both client traffic and health check probes exit through `nic1`.

**For IPv4 traffic** :
            
            sudo ip rule add from $LB_IPV4/32 table route-nic1
            

**For IPv6 traffic** :
            
            sudo ip rule -6 add from $LB_IPV6/96 table route-nic1
            




After you complete these steps on all backend VMs, the health checks succeed, and the load balancer routes traffic to the backends.

To learn more about policy routes, see [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).

## Test the load balancer

Now that the load balancing service is configured, you can start sending traffic to the load balancer's external IP address and watch traffic get distributed to the backend instances.

### Look up the load balancer's external IP address

###  Console 

  1. On the **Advanced** load balancing page, go to the **Forwarding rules** tab.

[Go to Forwarding rules](https://console.cloud.google.com/loadbalancing/advanced/forwardingRules/list)

  2. Locate the forwarding rule used by the load balancer.

  3. In the **Address** column, note the external IP address listed.




###  gcloud: IPv4 

Enter the following command to view the external IPv4 address of the `network-lb-forwarding-rule` forwarding rule used by the load balancer.
    
    
    gcloud compute forwarding-rules describe forwarding-rule-ipv4 \
        --region=us-central1
    

###  gcloud: IPv6 

Enter the following command to view the external IPv6 address of the `network-lb-forwarding-rule` forwarding rule used by the load balancer.
    
    
    gcloud compute forwarding-rules describe forwarding-rule-ipv6 \
        --region=us-central1
    

### Send traffic to the load balancer

Make web requests to the load balancer using `curl` to contact its IP address.

  * From clients with IPv4 connectivity, run the following command:
        
        while true; do curl -m1 IPV4_ADDRESS; done
        

  * From clients with IPv6 connectivity, run the following command:
        
        while true; do curl -m1 http://IPV6_ADDRESS; done
        

For example, if the assigned IPv6 address is `[2001:db8:1:1:1:1:1:1/96]:80`, the command is similar to the following:
        
        while true; do curl -m1 http://[2001:db8:1:1:1:1:1:1]:80; done
        




Note the text returned by the `curl` command. The name of the backend VM generating the response is displayed in that text; for example: `Page served from: VM_NAME`

The response from the `curl` command alternates randomly among the backend instances. If your response is initially unsuccessful, you might need to wait approximately 30 seconds for the configuration to be fully loaded and for your instances to be marked healthy before trying again.

## Additional configuration options

To further customize your regional external passthrough Network Load Balancer, you can configure session affinity, traffic steering, and set up a failover policy or a connection tracking policy. These tasks are optional and you can perform them in any order. For instructions, see [Additional configuration options](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#additional-configuration-options).

### Create an IPv6 forwarding rule with BYOIP

The load balancer created in the previous steps is configured with forwarding rules with `IP version` as `IPv4` or `IPv6`. This section provides instructions to create an IPv6 forwarding rule with bring your own IP (BYOIP) addresses.

Bring your own IP addresses lets you provision and use your own public IPv6 addresses for Google Cloud resources. For more information, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

Before you start configuring an IPv6 forwarding rule with BYOIP addresses, you must complete the following steps:

  1. [Create a public advertised IPv6 prefix](https://docs.cloud.google.com/vpc/docs/create-pap#create-pap)
  2. [Create public delegated prefixes](https://docs.cloud.google.com/vpc/docs/create-pdp#create-pdp)
  3. [Create IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes)
  4. [Announce the prefix](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement)



You can configure a regional external passthrough Network Load Balancer to use IPv6 addresses from a Public Delegated Prefix (PDP). You can deploy this using one of three workflows: 

  * _Direct allocation from a PDP_. If you prefer the IP address to be tied directly to the lifecycle of the load balancer, you can reference the PDP directly during forwarding rule creation. The ephemeral IP is released back to the PDP pool if the load balancer is deleted.
  * _Reserve a BYOIP IPv6 address_. You can reserve a specific or automatically allocated regional BYOIP IPv6 address from a PDP prior to load balancer creation. This address persists independently of the load balancer lifecycle. This is the required path for Google Kubernetes Engine (GKE) users because the GKE API does not support creating a passthrough Network Load Balancer directly from a PDP.
  * _Promote an ephemeral IP_. If a load balancer is already running with an ephemeral BYOIP IPv6 address, you can promote it to a reserved address so that it persists even if the load balancer is deleted.



#### Limitations

  * To configure an IPv6 forwarding rule with a BYOIP address, the prefix length of the forwarding rule's IPv6 address must match the [ allocatable prefix length](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#allocatable-prefix-length) of the [IPv6 sub-prefix](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes) (in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode) that the forwarding rule's IPv6 address is allocated from. The prefix length can be one of `/48`, `/56`, `/64`, `/72`, `/80`, `/88`, or `/96`.
  * The IPv6 address must be in the same region as the PDP.



Depending on your requirements, choose one of the following deployments:

#### Direct allocation from a PDP

Create the forwarding rule by referencing the PDP directly. The IP address is tied to the lifecycle of the load balancer. 

### Console

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing)

  2. Click the name of the load balancer that you want to modify.
  3. Click edit**Edit**.
  4. Click **Frontend configuration**.
  5. Click **Add frontend IP and port**.
  6. In the **New Frontend IP and port** section, specify the following: 
     1. Select the **Protocol** that you need.
     2. In the **IP version** field, select **IPv6**.
     3. In the **Source of IPv6 range** field, select **BYOIP**.
     4. In the **BYOIP type** field, select **BYOIP IP collection**.
     5. In the **IP collection** list, select a sub-prefix (PDP) created in the previous steps with the forwarding rule option enabled.
     6. In the **IPv6 range** field, enter the IPv6 address range. The IPv6 address range's prefix length must match the [ allocatable prefix length of the associated sub-prefix](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#allocatable-prefix-length).
     7. In the **Ports** field, enter a port number.
     8. Click **Done**.
  7. Click **Update**.



### gcloud

Use the [ `gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create):
    
    
      gcloud compute forwarding-rules create FWD_RULE_NAME \
          --load-balancing-scheme=EXTERNAL \
          --ip-protocol=PROTOCOL \
          --ports=ALL \
          --ip-version=IPV6 \
          --region=REGION_A \
          --address=IPV6_CIDR_RANGE  \
          --backend-service=BACKEND_SERVICE \
          --ip-collection=PDP_NAME
    

Replace the following:

  * `FWD_RULE_NAME`: the name of the forwarding rule
  * `PROTOCOL`: the IP protocol for the forwarding rule. The default is `TCP`. The IP protocol can be one of `TCP`, `UDP`, or `L3_DEFAULT`.
  * `REGION_A`: region for the forwarding rule
  * `IPV6_CIDR_RANGE`: the IPv6 address range that the forwarding rule serves. The IPv6 address range's prefix must match the [ allocatable prefix length specified by the associated sub-prefix](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#allocatable-prefix-length).
  * `BACKEND_SERVICE`: the name of the backend service
  * `PDP_NAME`: the name of the public delegated prefix. The PDP must be a sub-prefix in the `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.



#### Reserve a BYOIP IPv6 address

Reserve the BYOIP IPv6 address for the load balancer and then create the forwarding rule by referencing either the IP address or the reserved address resource name. 

### Console

**Reserve the BYOIP IPv6 address for the load balancer**

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve external**.
  3. In the **Name** field, enter a name for the IP address resource.
  4. In the **Network Service Tier** field, select **Premium**.
  5. In the **IP version** field, select **IPv6**.
  6. Select the **Region**. The region must match the region of your PDP.
  7. In the **Source** section, select **IP collection**.
  8. In the **BYOIP IP collection** list, select the IPv6 sub-prefix (PDP) from which you want to reserve the address.
  9. Optional: In the **IP address** field, enter a specific IPv6 address range to reserve (custom allocation). If you don't specify an address range, Google Cloud automatically allocates an address range from the selected IP collection (automatic allocation).
  10. Click **Reserve**.



**Assign the reserved address to the load balancer**

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing)

  2. Click the name of the load balancer that you want to modify.
  3. Click edit**Edit** , and click **Frontend configuration**.
  4. Click **Add frontend IP and port**.
  5. In the **New Frontend IP and port** section, specify the following: 
     1. Select the **Protocol** that you need.
     2. In the **IP version** field, select **IPv6**.
     3. In the **Source of IPv6 range** field, select **BYOIP**.
     4. In the **BYOIP type** field, select **BYOIP reserved IP address**.
     5. In the **Reserved IP address** list, select the reserved BYOIPv6 address resource you created in Step 1.
     6. In the **Ports** field, enter a port number.
     7. Click **Done**.
  6. Complete the load balancer configuration and click **Update**.



### gcloud

**Reserve the BYOIP IPv6 address for the load balancer**

To reserve a regional BYOIP IPv6 address from a PDP prior to load balancer creation, run the [ `gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) with `--endpoint-type=NETLB`. Choose one of the following options:

  * To reserve a specific IPv6 address range, run:
        
        gcloud compute addresses create ADDRESS_NAME \
              --ip-collection=PDP_NAME \
              --addresses=IPV6_ADDRESS \
              --region=REGION_A \
              --endpoint-type=NETLB \
              --prefix-length=PREFIX_LENGTH
        

  * To have Google Cloud automatically allocate a range from the PDP, run:
        
        gcloud compute addresses create ADDRESS_NAME \
              --ip-collection=PDP_NAME \
              --region=REGION_A \
              --endpoint-type=NETLB \
              --prefix-length=PREFIX_LENGTH
        




Replace the following:

  * `ADDRESS_NAME`: the name of the reserved IP address resource.
  * `PDP_NAME`: the name of the public delegated prefix. The PDP must be a sub-prefix in the `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.
  * `IPV6_ADDRESS`: the starting IPv6 address of the range (for example, `2001:db8::`).
  * `REGION_A`: region in which the address is to be created. This region must match the region of the PDP.
  * `PREFIX_LENGTH`: the prefix length of the address range, which must be equal to the allocatable prefix length of the associated PDP (for example, `56`).



**Create the forwarding rule using the reserved address**

To create the forwarding rule using the reserved address, run the [ `gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create). Choose one of the following options:

  * To reference the IP address range, run the following command:
        
        gcloud compute forwarding-rules create FWD_RULE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --ip-protocol=PROTOCOL \
             --ports=ALL \
             --ip-version=IPV6 \
             --region=REGION_A \
             --address=IPV6_CIDR_RANGE \
             --backend-service=BACKEND_SERVICE
        

  * To reference the reserved address name, run the following command:
        
        gcloud compute forwarding-rules create FWD_RULE_NAME \
              --load-balancing-scheme=EXTERNAL \
              --ip-protocol=PROTOCOL \
              --ports=ALL \
              --ip-version=IPV6 \
              --region=REGION_A \
              --address=ADDRESS_NAME \
              --backend-service=BACKEND_SERVICE
        




Replace the following:

  * `FWD_RULE_NAME`: the name of the forwarding rule
  * `PROTOCOL`: the IP protocol for the forwarding rule. The default is `TCP`. The IP protocol can be one of `TCP`, `UDP`, or `L3_DEFAULT`.
  * `REGION_A`: region for the forwarding rule
  * `IPV6_CIDR_RANGE`: the IPv6 address range that the forwarding rule serves. The IPv6 address range's prefix must match the [ allocatable prefix length specified by the associated sub-prefix](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#allocatable-prefix-length).
  * `BACKEND_SERVICE`: the name of the backend service
  * `ADDRESS_NAME`: the name of the reserved IP address resource.



#### Promote an ephemeral IP to a reserved IP address

Create the forwarding rule using direct allocation and promote the in-use ephemeral IP address. 

### Console

  1. Follow the steps to create the forwarding rule using direct allocation from a PDP.
  2. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  3. Click the **External IP addresses** tab.
  4. Find the ephemeral BYOIP IPv6 address that is associated with your external passthrough Network Load Balancer.
  5. In the **Actions** column, click the three-dot menu (more_vert) and select **Promote to static IP address**.
  6. Enter a **Name** for the reserved address and click **Reserve**.



### gcloud

  1. Follow the steps to update the forwarding rule using direct allocation from a PDP.
  2. To promote the ephemeral IP range in use by the load balancer to a reserved static IP address, run the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create): 
         
         gcloud compute addresses create ADDRESS_NAME \
                --addresses=IPV6_ADDRESS \
                --region=REGION_A \
                --endpoint-type=NETLB \
                --prefix-length=PREFIX_LENGTH
         

Replace the following:

     * `ADDRESS_NAME`: the name of the reserved IP address resource.
     * `IPV6_ADDRESS`: the starting IPv6 address of the range (for example, `2001:db8::`).
     * `REGION_A`: region for the forwarding rule
     * `PREFIX_LENGTH`: the prefix length of the address range, which must be equal to the allocatable prefix length of the associated PDP (for example, `56`).



## What's next

  * To learn how to migrate a regional external passthrough Network Load Balancer from a target pool backend to a regional backend service, see [Migrate regional external passthrough Network Load Balancers from target pools to backend services](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services).
  * To configure a regional external passthrough Network Load Balancer for multiple IP protocols (supporting IPv4 and IPv6 traffic), see [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols).
  * To configure advanced network DDoS protection for a regional external passthrough Network Load Balancer by using Cloud Armor, see [Configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).
  * To delete resources, see [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
