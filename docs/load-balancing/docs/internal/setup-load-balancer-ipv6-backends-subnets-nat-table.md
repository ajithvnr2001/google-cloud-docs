---
url: https://docs.cloud.google.com/load-balancing/docs/internal/setup-load-balancer-ipv6-backends-subnets-nat-table/
title: Set up an internal passthrough Network Load Balancer with internal IPv6-only backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:13.374668+00:00
---

# Set up an internal passthrough Network Load Balancer with internal IPv6-only backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/setup-load-balancer-ipv6-backends-subnets-nat-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up an internal passthrough Network Load Balancer with internal IPv6-only backends Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to configure and test an internal passthrough Network Load Balancer that supports internal IPv6-only traffic. In this example configuration, you install an Apache web server on the internal IPv6-only backend virtual machine (VM) instances to serve content in response to traffic received through the load balancer's virtual IP (VIP).

As shown in the following architecture diagram, the backend VMs of the load balancer are configured with internal IPv6-only addresses. For the purpose of this example configuration, these backend VMs need to download Apache to install a web server, which requires access to the public internet. However, because these backend VMs lack external IP addresses, they cannot reach the internet directly.

To enable internet access, this example uses a separate VM instance, configured using an external IPv6 address, that serves as a NAT gateway. This VM performs address translation at the Linux kernel level. Specifically, the `POSTROUTING` chain in the NAT table is used to masquerade the source address of outgoing packets—replacing each backend VM's internal IPv6 address with the NAT gateway VM's external IPv6 address on the specified network interface.

**Note:** Although this example uses an internal passthrough Network Load Balancer, the same NAT gateway setup can also apply to other load balancer types that support internal IPv6-only backends.[ ![Internal passthrough Network Load Balancer example configuration with internal IPv6-only backends.](https://docs.cloud.google.com/static/load-balancing/images/ilb-ipv6-nat-gateway.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-ipv6-nat-gateway.svg) Internal passthrough Network Load Balancer example configuration with internal IPv6-only backends (click to enlarge).

The information that follows walks you through the configuration of the different components that are used to set up an internal passthrough Network Load Balancer with internal IPv6-only backends.

## Permissions

To follow this guide, you need to create instances and modify a network in a project. You need to be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
(`roles/compute.networkAdmin`)   
Add and remove firewall rules | [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
(`roles/compute.securityAdmin`)   
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
(`roles/compute.instanceAdmin`)   
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Configure a network and an IPv6-only subnet with internal IPv6 addresses

The example internal passthrough Network Load Balancer described on this page is created in a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network-ipv6-only`.

To configure subnets with internal IPv6 ranges, enable a VPC network ULA internal IPv6 range. Internal IPv6 subnet ranges are allocated from this range.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network-ipv6-only`.

  4. If you want to configure internal IPv6 address ranges on subnets in this network, complete these steps:

     1. For **Private IPv6 address settings** , select **Configure a ULA internal IPv6 range for this VPC Network**.
     2. For **Allocate internal IPv6 range** , select **Automatically** or **Manually**. If you select **Manually** , enter a `/48` range from within the `fd20::/20` range. If the range is already in use, you are prompted to provide a different range.
  5. For **Subnet creation mode** , select **Custom**.

  6. In the **New subnet** section, specify the following configuration parameters for the subnet:

     * **Name** : `lb-subnet-ipv6-only`
     * **Region** : `us-west1`
     * **IP stack type** : **IPv6 (single-stack)**
     * **IPv6 access type** : **Internal**
  7. Click **Done**.

  8. Click **Create**.




###  gcloud 

  1. To create a new custom mode VPC network, run the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).

To configure [internal IPv6 ranges](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#enable-internal-ipv6-network) on any subnets in this network, use the `--enable-ula-internal-ipv6` flag.
         
         gcloud compute networks create lb-network-ipv6-only \
             --subnet-mode=custom \
             --enable-ula-internal-ipv6 \
             --bgp-routing-mode=regional
         

  2. Configure a subnet with the `ipv6-access-type` set to `INTERNAL`. This indicates that the VMs in this subnet can only have internal IPv6 addresses. In this example, the subnet is named `lb-subnet-ipv6-only-internal`.

To create the subnet, run the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create lb-subnet-ipv6-only-internal \
             --network=lb-network-ipv6-only \
             --region=us-west1 \
             --stack-type=IPV6_ONLY \
             --ipv6-access-type=INTERNAL
         




## Configure an IPv6-only subnet with external IPv6 addresses

An IPv6-only subnet with external IPv6 addresses is used to create a VM instance that serves as a NAT gateway.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To view the **VPC network details** page, click the name of the VPC network that you created.

  3. On the **Subnets** tab, click add_box**Add subnet**. In the panel that appears, specify the following configuration parameters for the subnet:

     * **Name** : `lb-subnet-ipv6-only-external`
     * **Region** : `us-west1`
     * **IP stack type** : **IPv6 (single-stack)**
     * **IPv6 access type** : **External**
  4. Click **Add**.




###  gcloud 

Configure a subnet with the `ipv6-access-type` set to `EXTERNAL`. This indicates that the VMs in this subnet can have external IPv6 addresses. In this example, the subnet is named `lb-subnet-ipv6-only-external`.

To create the subnet, run the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create  lb-subnet-ipv6-only-external \
        --network=lb-network-ipv6-only \
        --region=us-west1 \
        --stack-type=IPV6_ONLY \
        --ipv6-access-type=EXTERNAL
    

## Configure firewall rules in the VPC network

This example uses the following firewall rules:

  * `fw-allow-lb-access-ipv6-only`: an ingress rule, applicable to all targets in the VPC network, that allows traffic from all IPv6 sources.

  * `fw-allow-ssh`: an ingress rule that allows incoming SSH connectivity on TCP port `22` from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify just the IP ranges of the system from which you initiate SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it must apply.

  * `fw-allow-health-check-ipv6-only`: an ingress rule, applicable to the instances being load balanced, that allows traffic from the Google Cloud health checking systems (`2600:2d00:1:b029::/64`). This example uses the target tag `allow-health-check-ipv6` to identify the instances to which it must apply.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

**Note:** You must create a firewall rule to allow health checks from the IP ranges of Google Cloud probe systems. For more information, see [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To allow IPv6 subnet traffic, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-lb-access-ipv6-only`
     * **Network** : `lb-network-ipv6-only`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **All instances in the network**
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : `::/0`
     * **Protocols and ports** : **Allow all**
  3. Click **Create**.

  4. To allow incoming SSH connections, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network-ipv6-only`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : `::/0`
     * **Protocols and ports** : Select **Specified protocols and ports** , select the **TCP** checkbox, and then enter `22` in **Ports**.
  5. Click **Create**.

  6. To allow Google Cloud IPv6 health checks, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-health-check-ipv6-only`
     * **Network** : `lb-network-ipv6-only`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-health-check-ipv6`
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : `2600:2d00:1:b029::/64`
     * **Protocols and ports** : **Allow all**
  7. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-lb-access-ipv6-only` firewall rule to allow all inbound IPv6 traffic to all VM instances in the VPC network:
         
         gcloud compute firewall-rules create fw-allow-lb-access-ipv6-only \
             --network=lb-network-ipv6-only \
             --action=allow \
             --direction=ingress \
             --source-ranges=::/0 \
             --rules=all
         

  2. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network-ipv6-only \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --source-ranges=::/0 \
             --rules=tcp:22
         

  3. Create the `fw-allow-health-check-ipv6` rule to allow Google Cloud IPv6 health checks.
         
         gcloud compute firewall-rules create fw-allow-health-check-ipv6-only \
             --network=lb-network-ipv6-only \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check-ipv6 \
             --source-ranges=2600:2d00:1:b029::/64 \
             --rules=tcp,udp
         




## Create a VM instance that serves as a NAT gateway

In this example, a Bash script is used to create a NAT gateway that is used to modify IPv6 packets at the Linux kernel level.

The Bash script modifies the source address of all outgoing IPv6 packets in the `POSTROUTING` chain, replacing it with the external IPv6 address of the VM interface.

The Bash script modifies the `POSTROUTING` chain in `iptables` to masquerade the source IPv6 address of all outgoing packets, replacing it with the external IPv6 address of the VM's network interface.

You also need to [enable IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) for this instance.

To create a VM instance that serves as a NAT gateway, do the following:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `nat-gateway-instance`.

  4. For **Region** , select `us-west1`, and for **Zone** , select `us-west1-a`.

  5. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. If necessary, click **Change** to change the image.

  6. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **IP forwarding** , select the **Enable** checkbox.
     3. For **Network interfaces** , select the following: 
        * **Network** : `lb-network-ipv6-only`
        * **Subnet** : `lb-subnet-ipv6-only-external`
        * **IP stack type** : **IPv6 (single-stack)**
        * **External IPv6 address** : **Auto-Allocate**
  7. Click **Advanced** and in the **Startup script** field, enter the following script: 
         
         #!/bin/bash
         
         set -e
         
         echo "Starting GCE startup script..."
         
         # --- IPv6 NAT table configuration ---
         echo "Modifying the source IPv6 address using the NAT table"
         
         # Enable IPv6 forwarding
         sysctl -w net.ipv6.conf.all.forwarding=1
         
         # Determine the primary network interface (assuming it's the last one listed)
         IFACE=$(ip -brief link | tail -1 | awk '{print $1}')
         
         echo "Using interface: $IFACE for IPv6 NAT"
         
         # Flush existing IPv6 NAT rules
         ip6tables -F -t nat
         ip6tables -X -t nat
         
         # Masquerade all outgoing IPv6 traffic on the determined interface
         ip6tables -t nat -A POSTROUTING -o "$IFACE" -j MASQUERADE
         
         echo "IPv6 masquerading configured successfully."
         
         echo "GCE startup script finished."
         

  8. Click **Create**.




###  gcloud 

  1. Create a startup script.
         
         nano startup.sh
         

  2. Add the following script and save the file.
         
         #!/bin/bash
         
         set -e
         
         echo "Starting GCE startup script..."
         
         # --- IPv6 NAT table configuration ---
         echo "Modifying the source IPv6 address using the NAT table"
         
         # Enable IPv6 forwarding
         sysctl -w net.ipv6.conf.all.forwarding=1
         
         # Determine the primary network interface (assuming it's the last one listed)
         IFACE=$(ip -brief link | tail -1 | awk '{print $1}')
         
         echo "Using interface: $IFACE for IPv6 NAT"
         
         # Flush existing IPv6 NAT rules
         ip6tables -F -t nat
         ip6tables -X -t nat
         
         # Masquerade all outgoing IPv6 traffic on the determined interface
         ip6tables -t nat -A POSTROUTING -o "$IFACE" -j MASQUERADE
         
         echo "IPv6 masquerading configured successfully."
         
         echo "GCE startup script finished."
         

  3. Create a VM instance and add the metadata file to the VM instance. To use this VM as a next hop for a route, use the `--can-ip-forward` flag to [enable IP forwarding for this instance](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward).
         
         gcloud compute instances create nat-gateway-instance \
             --zone=us-west1-a \
             --tags=allow-ssh \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --subnet=lb-subnet-ipv6-only-external \
             --stack-type=IPV6_ONLY \
             --can-ip-forward \
             --metadata-from-file=startup-script=startup.sh
         




## Create a new static route in the VPC network

In this example, a custom route is created that directs all IPv6 internet-bound traffic (`::/0`) from VMs tagged `nat-gw-tag` to the `nat-gateway-instance` VM instance, which serves as the NAT gateway.

To create a route, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Routes page**.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click the **Route management** tab.

  3. Click **Create route**.

  4. Specify a name and a description for the route.

  5. In the **Network** list, select the VPC network `lb-network-ipv6-only`.

  6. In the **IP version** list, select **IPv6**.

  7. Specify a destination IPv6 range. The broadest possible destination is `::/0` for IPv6.

  8. To make the route applicable only to select instances with matching network tags, specify those in the **Instance tags** field. Leave the field blank to make the route applicable to all instances in the network. For this example, enter `nat-gw-tag`.

  9. For the [next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops), select **Specify an instance**.

  10. Select the name of the instance that you created to serve as the NAT gateway. For this example, select `nat-gateway-instance`.

  11. Click **Create**.




###  gcloud 

Use the [`gcloud compute routes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create) to create a new route. The packet is forwarded to the `nat-gateway-instance` VM instance as specified by `--next-hop-instance` of the route.
    
    
    gcloud compute routes create route-1 \
        --network=lb-network-ipv6-only \
        --priority=1000 \
        --tags=nat-gw-tag \
        --destination-range=::/0 \
        --next-hop-instance=nat-gateway-instance \
        --next-hop-instance-zone=us-west1-a
    

## Create backend VMs and instance groups

This example uses two _unmanaged_ instance groups, each having two backend VMs. To demonstrate the regional nature of internal passthrough Network Load Balancers, the two instance groups are placed in separate zones, `us-west1-a` and `us-west1-c`.

  * Instance group `ig-a` contains these two VMs: 
    * `vm-a1`
    * `vm-a2`
  * Instance group `ig-c` contains these two VMs: 
    * `vm-c1`
    * `vm-c2`



Traffic to all four of the backend VMs is load balanced.

In this example, the static route that was created in an earlier step is scoped to specific VM instances by using the network tag, `nat-gw-tag`.

###  Console 

#### Create backend VMs

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat these steps for each VM, using the following name and zone combinations.

     * Name: `vm-a1`, zone: `us-west1-a`
     * Name: `vm-a2`, zone: `us-west1-a`
     * Name: `vm-c1`, zone: `us-west1-c`
     * Name: `vm-c2`, zone: `us-west1-c`
  3. Click **Create instance**.

  4. Set the **Name** as indicated in step 2.

  5. For **Region** , select `us-west1`, and choose a **Zone** as indicated in step 2.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. If necessary, click **Change** to change the image.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`, `allow-health-check-ipv6`, and `nat-gw-tag`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network-ipv6-only`
        * **Subnet** : `lb-subnet-ipv6-only-internal`
        * **IP stack type** : **IPv6 (single-stack)**
        * **Primary internal IPv6 address** : **Ephemeral (Automatic)**
  9. Click **Advanced** , and then in the **Startup script** field, enter the following script. The script contents are identical for all four VMs.
         
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
         

  10. Click **Create**.




#### Create instance groups

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Repeat the following steps to create two unmanaged instance groups each with two VMs in them, using these combinations.

     * Instance group name: `ig-a`, zone: `us-west1-a`, VMs: `vm-a1` and `vm-a2`
     * Instance group name: `ig-c`, zone: `us-west1-c`, VMs: `vm-c1` and `vm-c2`
  3. Click **Create instance group**.

  4. Click **New unmanaged instance group**.

  5. Set **Name** as indicated in step 2.

  6. In the **Location** section, select `us-west1` for the **Region** , and then choose a **Zone** as indicated in step 2.

  7. For **Network** , select `lb-network-ipv6-only`.

  8. For **Subnetwork** , select `lb-subnet-ipv6-only-internal`.

  9. In the **VM instances** section, add the VMs as indicated in step 2.

  10. Click **Create**.




###  gcloud 

  1. To create the four VMs, run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) four times, using the following four combinations for `[VM-NAME]` and `[ZONE]`.

     * `VM-NAME`: `vm-a1`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-a2`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-c1`, `ZONE`: `us-west1-c`
     * `VM-NAME`: `vm-c2`, `ZONE`: `us-west1-c`
    
    gcloud compute instances create VM-NAME \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh,allow-health-check-ipv6,nat-gw-tag \
        --subnet=lb-subnet-ipv6-only-internal \
        --stack-type=IPV6_ONLY \
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
    

  2. Create the two unmanaged instance groups in each zone:
         
         gcloud compute instance-groups unmanaged create ig-a \
             --zone=us-west1-a
         gcloud compute instance-groups unmanaged create ig-c \
             --zone=us-west1-c
         

  3. Add the VMs to the appropriate instance groups:
         
         gcloud compute instance-groups unmanaged add-instances ig-a \
             --zone=us-west1-a \
             --instances=vm-a1,vm-a2
         gcloud compute instance-groups unmanaged add-instances ig-c \
             --zone=us-west1-c \
             --instances=vm-c1,vm-c2
         




## Configure load balancer components

The steps that follow configure the different components of an internal passthrough Network Load Balancer starting with the health check and backend service followed by the frontend.

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. Click **Configure**.



#### Basic configuration

On the **Create internal passthrough Network Load Balancer** page, enter the following information:

  * **Load balancer name** : `ilb-ipv6-only`
  * **Region** : **`us-west1`**
  * **Network** : **`lb-network-ipv6-only`**



#### Backend configuration

  1. Click **Backend configuration**.
  2. In the **Health check** list, select **Create a health check** , and then enter the following information: 
     * **Name** : `hc-http-80`
     * **Scope** : **Regional**
     * **Protocol** : **HTTP**
     * **Port** : `80`
     * **Proxy protocol** : **None**
     * **Request** : `/`
  3. Click **Create**.
  4. In the **New Backend** section, for **IP stack type** , select the **IPv6 (single-stack)** option.
  5. In **Instance group** , select the `ig-a` instance group and click **Done**.
  6. Click **Add a backend** and repeat the step to add `ig-c`.
  7. Verify that a blue check mark appears next to **Backend configuration**.



#### Frontend configuration

  1. Click **Frontend configuration**. In the **New Frontend IP and port** section, do the following: 
     1. For **Name** , enter `fr-ilb-ipv6-only`.
     2. To handle IPv6 traffic, do the following: 
        1. For **IP version** , select **IPv6**. The IPv6 TCP server that you are going to create in the following section binds to the VIP of the forwarding rule.
        2. For **Subnetwork** , select`lb-subnet-ipv6-only-internal`. The IPv6 address range in the forwarding rule is always ephemeral.
        3. For **Ports** , select **Multiple** , and then in the **Port number** field, enter `80`.
        4. Click **Done**.
     3. Verify that there is a blue check mark next to **Frontend configuration** before continuing.



#### Review the configuration

  1. Click **Review and finalize**. Check all your settings.
  2. If the settings are correct, click **Create**. It takes a few minutes for the internal passthrough Network Load Balancer to be created.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to the VMs on port 80.
         
         gcloud compute health-checks create http hc-http-80 \
             --region=us-west1 \
             --port=80
         

  2. Create the backend service:
         
         gcloud compute backend-services create ilb-ipv6-only \
             --load-balancing-scheme=INTERNAL \
             --protocol=tcp \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  3. Add the two instance groups to the backend service:
         
         gcloud compute backend-services add-backend ilb-ipv6-only \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         
         
         gcloud compute backend-services add-backend ilb-ipv6-only \
             --region=us-west1 \
             --instance-group=ig-c \
             --instance-group-zone=us-west1-c
         

  4. Create the IPv6 forwarding rule with an ephemeral IPv6 address.
         
         gcloud compute forwarding-rules create fr-ilb-ipv6-only \
             --region=us-west1 \
             --load-balancing-scheme=INTERNAL \
             --subnet=lb-subnet-ipv6-only-internal \
             --ip-protocol=TCP \
             --ports=80 \
             --backend-service=ilb-ipv6-only \
             --backend-service-region=us-west1 \
             --ip-version=IPV6
         




## Test your load balancer

To test the load balancer, create a client VM in the same region as the load balancer, and then send traffic from the client to the load balancer.

### Create a client VM

This example creates a client VM (`vm-client`) in the same region as the backend (server) VMs.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `vm-client`.

  4. For **Region** , select **`us-west1`**.

  5. For **Zone** , select **`us-west1-a`**.

  6. Click **Advanced options**.

  7. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : **`lb-network-ipv6-only`**
        * **Subnet** : **`lb-subnet-ipv6-only-internal`**
        * **IP stack type** : **IPv6 (single-stack)**
     3. Click **Done**.
  8. Click **Create**.




###  gcloud 

The client VM can be in any zone in the same region as the load balancer. In this example, the client is in the `us-west1-a` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create vm-client \
        --zone=us-west1-a \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --stack-type=IPV6_ONLY \
        --tags=allow-ssh \
        --subnet=lb-subnet-ipv6-only-internal
    

### Test the connection

This test contacts the load balancer from a separate client VM; that is, not from a backend VM of the load balancer. The expected behavior is for traffic to be distributed among the four backend VMs.

  1. Connect to the client VM instance [by using SSH](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms).
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Describe the IPv6 forwarding rule `fr-ilb-ipv6-only`. Note the `IPV6_ADDRESS` in the description.
         
         gcloud compute forwarding-rules describe fr-ilb-ipv6-only \
             --region=us-west1
         

  3. From clients with IPv6 connectivity, run the following command:
         
         curl http://IPV6_ADDRESS:80
         

For example, if the assigned IPv6 address is `[fd20:307:120c:2000:0:1:0:0/96]:80`, the command should look as follows:
         
         curl http://[fd20:307:120c:2000:0:1:0:0]:80
         

The response can be as follows:
         
         Page returned from: vm-a2
         




## What's next

  * Review the setup to [configure an internal passthrough Network Load Balancer with an internal IPv6-only subnet and backend using an IPv6 TCP server installed on the backend VMs](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-ipv6-only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
