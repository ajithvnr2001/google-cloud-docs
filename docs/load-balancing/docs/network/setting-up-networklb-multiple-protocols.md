---
url: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols/
title: Set up a regional external passthrough Network Load Balancer for multiple IP protocols \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:32.657782+00:00
---

# Set up a regional external passthrough Network Load Balancer for multiple IP protocols  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external passthrough Network Load Balancer for multiple IP protocols Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides instructions for creating [backend service-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service) that load balance TCP, UDP, ESP, GRE, ICMP, and ICMPv6 traffic. You can use such a configuration to load-balance traffic that is using IP protocols other than TCP or UDP. Target pool-based regional external passthrough Network Load Balancers don't support this capability.

To configure a regional external passthrough Network Load Balancer for IP protocols other than TCP or UDP, you create a [forwarding rule with protocol set to `L3_DEFAULT`](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule-protocols). This forwarding rule points to a [backend service with protocol set to `UNSPECIFIED`](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#backend-service).

In this example, we use two regional external passthrough Network Load Balancers to distribute traffic across backend VMs in two zonal managed instance groups in the `us-central1` region. Both load balancers receive traffic at the same external IP address.

One load balancer has a forwarding rule with protocol `TCP` and port 80, and the other load balancer has a forwarding rule with protocol `L3_DEFAULT`. TCP traffic arriving at the IP address on port 80 is handled by the `TCP` forwarding rule. All other traffic that doesn't match the TCP-specific forwarding rule is handled by the `L3_DEFAULT` forwarding rule.

[ ![Regional external passthrough Network Load Balancer with zonal managed instance groups.](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-multiple-protocols.svg)](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-multiple-protocols.svg) Regional external passthrough Network Load Balancer with zonal managed instance groups (click to enlarge).

This scenario load balances connections using multiple protocols with a TCP health check. For information about other supported protocols, see [Regional backend service](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#backend-service) and [Health checks](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#health-checks).

The regional external passthrough Network Load Balancer is a regional load balancer. All load balancer components must be in the same region.

## Before you begin

Install the Google Cloud CLI. For a complete overview of the tool, see the [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). You can find commands related to load balancing in the [API and gcloud reference](https://docs.cloud.google.com/load-balancing/docs/apis).

If you haven't run the gcloud CLI previously, first run the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.

This guide assumes that you are familiar with [bash](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)).

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
         




## Create the zonal managed instance groups

For this load balancing scenario, you create two Compute Engine zonal managed instance groups and install an Apache web server on each instance.

The instance group references an instance template, which is used to create backend VMs. In this example, you create backend VMs with IPv4-only, dual-stack, and IPv6-only network interfaces. The VMs also inherit the `ipv6-access-type` setting (in this example, `EXTERNAL`) from the subnet. For more information about IPv6 requirements, see [Forwarding rule](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule) in the regional external passthrough Network Load Balancer overview document.

To use existing VMs as backends, update the VMs to be dual-stack by using the [`gcloud compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update).

Instances that participate as backend VMs for regional external passthrough Network Load Balancers must run the appropriate [Linux guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#linux), [Windows guest environment](https://github.com/GoogleCloudPlatform/compute-image-windows), or other processes that provide equivalent capability.

### Create the instance group for TCP traffic on port 80

###  Console 

  1. Create an instance template. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

     1. Click **Create instance template**.
     2. For **Name** , enter `ig-us-template-tcp-80`.
     3. Ensure that the Boot disk is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     4. Expand the **Advanced options** section.
     5. Expand the **Management** section, and then copy the following script into the **Startup script** field.
            
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
            

     6. Expand the **Networking** section, and then specify the following:

        1. For **Network tags** , add `network-lb-tcp-80`.
        2. For **Network interfaces** , select the default network interface.

To create backend VMs with _dual-stack_ network interfaces, configure the following fields:

           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
           * **External IPv4 address** : **Ephemeral**
           * **External IPv6 address** : **Auto-allocate**

To create backend VMs with _IPv4-only_ network interfaces, configure the following fields:

           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv4 (single-stack)**
           * **External IPv4 address** : **Ephemeral**

To create backend VMs with _IPv6-only_ network interfaces, configure the following fields:

           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv6 (single-stack)**
           * **External IPv6 address** : **Auto-allocate**
     7. Click **Create**.

  2. Create a managed instance group. Go to the **Instance groups** page in the Google Cloud console.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     1. Click **Create instance group**.
     2. Select **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
     3. For the **Name** , enter `ig-us-tcp-80`.
     4. Under **Location** , select **Single zone**.
     5. For the **Region** , select `us-central1`.
     6. For the **Zone** , select `us-central1-a`.
     7. Under **Instance template** , select `ig-us-template-tcp-80`.
     8. Specify the number of instances that you want to create in the group.

For this example, specify the following options under **Autoscaling** :

        * For **Autoscaling mode** , select `Off:do not autoscale`.
        * For **Maximum number of instances** , enter `2`.
     9. Click **Create**.




###  gcloud 

The `gcloud` instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.

  1. Create a VM instance template with HTTP server with the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

To create backend VMs with _dual-stack_ network interfaces, use the following command.

**Note:** Set `--ipv6-network-tier` to `PREMIUM` only if you are creating the VMs in subnets with `ipv6-access-type` set to `EXTERNAL`. Omit the flag if the subnet's `ipv6-access-type` is `INTERNAL`.
         
         gcloud compute instance-templates create ig-us-template-tcp-80 \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --ipv6-network-tier=PREMIUM \
               --stack-type=IPV4_IPV6 \
               --tags=network-lb-tcp-80 \
               --image-family=debian-12 \
               --image-project=debian-cloud \
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
         
         gcloud compute instance-templates create ig-us-template-tcp-80 \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --stack-type=IPV4_ONLY \
               --tags=network-lb-tcp-80 \
               --image-family=debian-12 \
               --image-project=debian-cloud \
               --metadata=startup-script='#! /bin/bash
               apt-get update
               apt-get install apache2 -y
               a2ensite default-ssl
               a2enmod ssl
               vm_hostname="$(curl -H "Metadata-Flavor:Google" \
                       ://metadata.google.internal/computeMetadata/v1/instance/name)"
               echo "Page served from: $vm_hostname" | \
               tee /var/www/html/index.html
               systemctl restart apache2'
         

To create backend VMs with _IPv6-only_ network interfaces, use the following command.

**Note:** Set `--ipv6-network-tier` to `PREMIUM` only if you are creating the VMs in subnets with `ipv6-access-type` set to `EXTERNAL`. Omit the flag if the subnet's `ipv6-access-type` is `INTERNAL`.
         
         gcloud compute instance-templates create ig-us-template-tcp-80 \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --ipv6-network-tier=PREMIUM \
               --stack-type=IPV6_ONLY \
               --tags=network-lb-tcp-80 \
               --image-family=debian-12 \
               --image-project=debian-cloud \
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
         

  2. Create a managed instance group in the zone with the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).
         
         gcloud compute instance-groups managed create ig-us-tcp-80 \
               --zone us-central1-a \
               --size 2 \
               --template ig-us-template-tcp-80
         




### Create the instance group for TCP on port 8080, UDP, ESP, and ICMP traffic

###  Console 

  1. Create an instance template. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

     1. Click **Create instance template**.
     2. For the **Name** , enter `ig-us-template-l3-default`.
     3. Ensure that the Boot disk is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     4. Expand the **Advanced options** section.
     5. Expand the **Management** section, and then copy the following script into the **Startup script** field. The startup script also configures the Apache server to listen on port 8080 instead of port 80.
            
            #! /bin/bash
            apt-get update
            apt-get install apache2 -y
            a2ensite default-ssl
            a2enmod ssl
            vm_hostname="$(curl -H "Metadata-Flavor:Google" \
            http://metadata.google.internal/computeMetadata/v1/instance/name)"
            echo "Page served from: $vm_hostname" | \
            tee /var/www/html/index.html
            sed -ire 's/^Listen 80$/Listen 8080/g' /etc/apache2/ports.conf
            systemctl restart apache2
            

     6. Expand the **Networking** section, and then specify the following:

        1. For **Network tags** , add `network-lb-l3-default`.
        2. For **Network interfaces** , select the default network interface.

To create backend VMs with _dual-stack_ network interfaces, configure the following fields:

           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
           * **External IPv4 address** : **Ephemeral**
           * **External IPv6 address** : **Auto-allocate**

To create backend VMs with _IPv4-only_ network interfaces, configure the following fields:

           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv4 (single-stack)**
           * **External IPv4 address** : **Ephemeral**

To create backend VMs with _IPv6-only_ network interfaces, configure the following fields:

           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv6 (single-stack)**
           * **External IPv6 address** : **Auto-allocate**
     7. Click **Create**.

  2. Create a managed instance group. Go to the **Instance groups** page in the Google Cloud console.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     1. Click **Create instance group**.
     2. Choose **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
     3. For the **Name** , enter `ig-us-l3-default`.
     4. Under **Location** , select **Single zone**.
     5. For the **Region** , select `us-central1`.
     6. For the **Zone** , select `us-central1-c`.
     7. Under **Instance template** , select `ig-us-template-l3-default`.
     8. Specify the number of instances that you want to create in the group.

For this example, specify the following options under **Autoscaling** :

        * For **Autoscaling mode** , select `Off:do not autoscale`.
        * For **Maximum number of instances** , enter `2`.
     9. Click **Create**.




###  gcloud 

The `gcloud` instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.

  1. Create a VM instance template with HTTP server with the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

The startup script also configures the Apache server to listen on port 8080 instead of port 80.

To create backend VMs with _dual-stack_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-us-template-l3-default \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --ipv6-network-tier=PREMIUM \
               --stack-type=IPV4_IPV6 \
               --tags=network-lb-l3-default \
               --image-family=debian-12 \
               --image-project=debian-cloud \
               --metadata=startup-script='#! /bin/bash
               apt-get update
               apt-get install apache2 -y
               a2ensite default-ssl
               a2enmod ssl
               vm_hostname="$(curl -H "Metadata-Flavor:Google" \
               http://metadata.google.internal/computeMetadata/v1/instance/name)"
               echo "Page served from: $vm_hostname" | \
               tee /var/www/html/index.html
               sed -ire "s/^Listen 80$/Listen 8080/g" /etc/apache2/ports.conf
               systemctl restart apache2'
         

To create backend VMs with _IPv4-only_ interfaces, use the following command.
         
         gcloud compute instance-templates create ig-us-template-l3-default \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --stack-type=IPV4_ONLY \
               --tags=network-lb-l3-default \
               --image-family=debian-12 \
               --image-project=debian-cloud \
               --metadata=startup-script='#! /bin/bash
               apt-get update
               apt-get install apache2 -y
               a2ensite default-ssl
               a2enmod ssl
               vm_hostname="$(curl -H "Metadata-Flavor:Google" \
               http://metadata.google.internal/computeMetadata/v1/instance/name)"
               echo "Page served from: $vm_hostname" | \
               tee /var/www/html/index.html
               sed -ire "s/^Listen 80$/Listen 8080/g" /etc/apache2/ports.conf
               systemctl restart apache2'
         

To create backend VMs with _IPv6-only_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-us-template-l3-default \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --ipv6-network-tier=PREMIUM \
               --stack-type=IPV6_ONLY \
               --tags=network-lb-l3-default \
               --image-family=debian-12 \
               --image-project=debian-cloud \
               --metadata=startup-script='#! /bin/bash
               apt-get update
               apt-get install apache2 -y
               a2ensite default-ssl
               a2enmod ssl
               vm_hostname="$(curl -H "Metadata-Flavor:Google" \
               http://metadata.google.internal/computeMetadata/v1/instance/name)"
               echo "Page served from: $vm_hostname" | \
               tee /var/www/html/index.html
               sed -ire "s/^Listen 80$/Listen 8080/g" /etc/apache2/ports.conf
               systemctl restart apache2'
         

  2. Create a managed instance group in the zone with the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).
         
         gcloud compute instance-groups managed create ig-us-l3-default \
               --zone us-central1-c \
               --size 2 \
               --template ig-us-template-l3-default
         




## Configure firewall rules

Create the following firewall rules:

  * Firewall rules that allow external TCP traffic to reach backend instances in the `ig-us-tcp-80` instance group on port 80 (using target tag `network-lb-tcp-80`). Create separate firewall rules to allow IPv4 and IPv6 traffic.
  * Firewall rules that allow other external traffic (TCP on port 8080, UDP, ESP, and ICMP) to reach backend instances in the `ig-us-l3-default` instance group (using target tag `network-lb-l3-default`). Create separate firewall rules to allow IPv4 and IPv6 traffic.



This example creates firewall rules that allow traffic from _all_ source ranges to reach your backend instances on the configured ports. If you want to create separate firewall rules specifically for the health check probes, use the source IP address ranges documented in the [Health checks overview: Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To allow **IPv4 TCP traffic** to reach backends in the `ig-us-tcp-80` instance group, create the following firewall rule.

     1. Click **Create firewall rule**.
     2. Enter a **Name** of `allow-network-lb-tcp-80-ipv4`.
     3. Select the **Network** that the firewall rule applies to (**Default**).
     4. Under **Targets** , select **Specified target tags**.
     5. In the **Target tags** field, enter `network-lb-tcp-80`.
     6. Set **Source filter** to **IPv4 ranges**.
     7. Set the **Source IPv4 ranges** to 0.0.0.0/0, which allows traffic from any source. This allows both external traffic and health check probes to reach the backend instances.
     8. Under **Protocols and ports** , select **Specified protocols and ports**. Then select the **TCP** checkbox and enter `80`.
     9. Click **Create**. It might take a moment for the Console to display the new firewall rule, or you might have to click **Refresh** to see the rule.
  3. To allow **IPv4 UDP, ESP, and ICMP traffic** to reach backends in the `ig-us-l3-default` instance group, create the following firewall rule.

     1. Click **Create firewall rule**.
     2. Enter a **Name** of `allow-network-lb-l3-default-ipv4`.
     3. Select the **Network** that the firewall rule applies to (**Default**).
     4. Under **Targets** , select **Specified target tags**.
     5. In the **Target tags** field, enter `network-lb-l3-default`.
     6. Set **Source filter** to **IPv4 ranges**.
     7. Set the **Source IPv4 ranges** to `0.0.0.0/0`, which allows traffic from any source. This allows both external traffic and health check probes to reach the backend instances.
     8. Under **Protocols and ports** , select **Specified protocols and ports**. 
        1. Select the **TCP** checkbox and enter `8080`.
        2. Select the **UDP** checkbox.
        3. Select the **Other** checkbox and enter `esp, icmp`.
     9. Click **Create**. It might take a moment for the Console to display the new firewall rule, or you might have to click **Refresh** to see the rule.
  4. To allow **IPv6 TCP traffic** to reach backends in the `ig-us-tcp-80` instance group, create the following firewall rule.

     1. Click **Create firewall rule**.
     2. Enter a **Name** of `allow-network-lb-tcp-80-ipv6`.
     3. Select the **Network** that the firewall rule applies to (**Default**).
     4. Under **Targets** , select **Specified target tags**.
     5. In the **Target tags** field, enter `network-lb-tcp-80`.
     6. Set **Source filter** to **IPv6 ranges**.
     7. Set the **Source IPv6 ranges** to `::/0`, which allows traffic from any source. This allows both external traffic and health check probes to reach the backend instances.
     8. Under **Protocols and ports** , select **Specified protocols and ports**. Click the checkbox next to **TCP** and enter `80`.
     9. Click **Create**. It might take a moment for the Console to display the new firewall rule, or you might have to click **Refresh** to see the rule.
  5. To allow **IPv6 UDP, ESP, and ICMPv6 traffic** to reach backends in the `ig-us-l3-default` instance group, create the following firewall rule. This firewall rule also allows TCP health check probes to reach the instances on port 8080.

     1. Click **Create firewall rule**.
     2. Enter a **Name** of `allow-network-lb-l3-default-ipv6`.
     3. Select the **Network** that the firewall rule applies to (**Default**).
     4. Under **Targets** , select **Specified target tags**.
     5. In the **Target tags** field, enter `network-lb-l3-default`.
     6. Set **Source filter** to **IPv6 ranges**.
     7. Set the **Source IPv6 ranges** to `::/0`, which allows traffic from any source. This allows both external traffic and health check probes to reach the backend instances.
     8. Under **Protocols and ports** , select **Specified protocols and ports**. 
        1. Click the checkbox next to **TCP** and enter `8080`.
        2. Click the checkbox next to **UDP**.
        3. Click the checkbox next to **Other** and enter `esp, 58`.
     9. Click **Create**. It might take a moment for the Console to display the new firewall rule, or you might have to click **Refresh** to see the rule.



###  gcloud 

  1. To allow **IPv4 TCP traffic** to reach backends in the `ig-us-tcp-80` instance group, create the following firewall rule.
         
         gcloud compute firewall-rules create allow-network-lb-tcp-80-ipv4 \
             --network=lb-network \
             --target-tags network-lb-tcp-80 \
             --allow tcp:80 \
             --source-ranges=0.0.0.0/0
         

  2. To allow **IPv4 UDP, ESP, and ICMP traffic** to reach backends in the `ig-us-l3-default` instance group, create the following firewall rule. This firewall rule also allows TCP health check probes to reach the instances on port 8080.
         
         gcloud compute firewall-rules create allow-network-lb-l3-default-ipv4 \
             --network=lb-network \
             --target-tags network-lb-l3-default \
             --allow tcp:8080,udp,esp,icmp \
             --source-ranges=0.0.0.0/0
         

  3. To allow **IPv6 TCP traffic** to reach backends in the `ig-us-tcp-80` instance group, create the following firewall rule.
         
         gcloud compute firewall-rules create allow-network-lb-tcp-80-ipv6 \
             --network=lb-network \
             --target-tags network-lb-tcp-80 \
             --allow tcp:80 \
             --source-ranges=::/0
         

  4. To allow **IPv6 UDP, ESP, and ICMPv6 traffic** to reach backends in the `ig-us-l3-default` instance group, create the following firewall rule. This firewall rule also allows TCP health check probes to reach the instances on port 8080.
         
         gcloud compute firewall-rules create allow-network-lb-l3-default-ipv6 \
             --network=lb-network \
             --target-tags network-lb-l3-default \
             --allow tcp:8080,udp,esp,58 \
             --source-ranges=::/0
         




## Configure the load balancers

Next, set up two load balancers. Configure both load balancers to use the same external IP address for the forwarding rules where one load balancer handles TCP traffic on port 80, and the other load balancer handles TCP, UDP, ESP, and ICMP traffic on port 8080.

When you configure a load balancer, your backend VM instances receive packets that are destined for the static external IP address you configure. If you are using an [image provided by Compute Engine](https://docs.cloud.google.com/compute/docs/images#os-compute-support), your instances are automatically configured to handle this IP address. If you are using any other image, you must configure this address as an alias on `eth0` or as a loopback on each instance.

To setup two load balancers, use the following the instructions.

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. In the **Name** field, enter the name `backend-service-tcp-80` for the new load balancer.
  2. In the **Region** list, select `us-central1`.



#### Backend configuration

  1. Click **Backend configuration**.
  2. On the **Backend configuration** page, do the following: 
     1. In the **Health check** list, click **Create a health check** , and then enter the following information: 
        * **Name** : `tcp-health-check-80`
        * **Protocol** : **TCP**
        * **Port** : `80`
     2. Click **Create**.
     3. In the **New Backend** section, select the **IP stack type**.
     4. In the **Instance group** list, select `ig-us-tcp-80`, and then click **Done**.
  3. Verify that there is a blue checkmark next to **Backend configuration** before continuing.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. In the **Name** field, enter `forwarding-rule-tcp-80`.
  3. To handle IPv4 traffic, use the following steps: 
     1. For **IP version** , select **IPv4**.
     2. In the **Internal IP purpose** section, in the **IP address** list, select **Create IP address**. 
        1. In the **Name** field, enter `network-lb-ipv4`.
        2. Click **Reserve**.
     3. For **Ports** , choose **Single**. In the **Port number** field, enter `80`.
     4. Click **Done**.
  4. To handle IPv6 traffic, use the following steps:

     1. For **IP version** , select **IPv6**.
     2. For **Subnetwork** , select **lb-subnet**.
     3. In the **IPv6 range** list, select **Create IP address**. 
        1. In the **Name** field, enter `network-lb-ipv6`.
        2. Click **Reserve**.
     4. For **Ports** , choose **Single**. In the **Port number** field, enter `80`.
     5. Click **Done**.

A blue circle with a checkmark to the left of **Frontend configuration** indicates a successful setup.




#### Review the configuration

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.

On the load balancing page, under the Backend column for your new load balancer, you see a green checkmark showing that the new load balancer is healthy.




### Create the second load balancer

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. In the **Name** field, enter the name `backend-service-l3-default` for the new load balancer.
  2. In the **Region** list, select `us-central1`.



#### Backend configuration

  1. Click **Backend configuration**.
  2. On the **Backend configuration** page, do the following: 
     1. In the **Health check** list, click **Create a health check** , and then enter the following information: 
        * **Name** : `tcp-health-check-8080`
        * **Protocol** :**TCP**
        * **Port** : `8080`
     2. Click **Create**.
     3. In the **New Backend** section, select the **IP stack type**. If you created dual-stack backends to handle both IPv4 and IPv6 traffic, select **IPv4 and IPv6 (dual-stack)**. To handle IPv4 traffic only, select **IPv4 (single-stack)**.
     4. In the **Instance group** list, select `ig-us-l3-default`, and then click **Done**.
     5. In the **Protocols** list, select **L3 (Multiple protocols)**.
  3. Verify that there is a blue checkmark next to **Backend configuration** before continuing.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. In the **Name** field, enter `forwarding-rule-l3-default`.
  3. To handle IPv4 traffic, use the following steps: 
     1. For **IP version** , select **IPv4**.
     2. In the **Internal IP purpose** section, in the **IP address** list, select **Create IP address**. 
        1. In the **Name** field, enter `network-lb-ipv4`.
        2. Click **Reserve**.
     3. In the **Protocol** list, select **L3 (Multiple protocols)**.
     4. For **Ports** , choose **All**.
     5. Click **Done**.
  4. To handle IPv6 traffic, use the following steps:

     1. For **IP version** , select **IPv6**.
     2. For **Subnetwork** , select **lb-subnet**.
     3. In the **IPv6 range** list, select **Create IP address**. 
        1. In the **Name** field, enter `network-lb-ipv6`.
        2. Click **Reserve**.
     4. In the **Protocol** field, select **L3 (Multiple protocols)**.
     5. For **Ports** , select **All**.
     6. Click **Done**.

A blue circle with a checkmark to the left of **Frontend configuration** indicates a successful setup.




#### Review the configuration

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.

On the load balancing page, under the Backend column for your new load balancer, you see a green checkmark showing that the new load balancer is healthy.




###  gcloud 

  1. Reserve a static external IP address.

**For IPv4 traffic:** Create a [static external IP address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) for your load balancers.
         
         gcloud compute addresses create network-lb-ipv4 \
             --region us-central1
         

**For IPv6 traffic:** Create a [static external IPv6 address range](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) for your load balancers. The subnet used must be a dual-stack subnet with an external IPv6 subnet range.
         
         gcloud compute addresses create network-lb-ipv6 \
             --region us-central1 \
             --subnet lb-subnet \
             --ip-version IPV6 \
             --endpoint-type NETLB
         

  2. Create a TCP health check for port 80. This health check is used to verify the health of backends in the `ig-us-tcp-80` instance group.
         
         gcloud compute health-checks create tcp tcp-health-check-80 \
             --region us-central1 \
             --port 80
         

  3. Create a TCP health check for port 8080. This health check is used to verify the health of backends in the `ig-us-l3-default` instance group.
         
         gcloud compute health-checks create tcp tcp-health-check-8080 \
             --region us-central1 \
             --port 8080
         

  4. Create the first load balancer for TCP traffic on port 80.

     1. Create a [backend service](https://docs.cloud.google.com/compute/docs/reference/latest/backendServices) with the protocol set to `TCP`.
            
            gcloud compute backend-services create backend-service-tcp-80 \
                --protocol TCP \
                --health-checks tcp-health-check-80 \
                --health-checks-region us-central1 \
                --region us-central1
            

     2. Add the backend instance group to the backend service.
            
            gcloud compute backend-services add-backend backend-service-tcp-80 \
                --instance-group ig-us-tcp-80 \
                --instance-group-zone us-central1-a \
                --region us-central1
            

     3. **For IPv4 traffic:** Create a forwarding rule to route incoming TCP traffic on port 80 to the backend service. `TCP` is the default forwarding rule protocol and does not need to be set explicitly.

Use the IP address reserved in step 1 as the static external IP address of the load balancer.
            
            gcloud compute forwarding-rules create forwarding-rule-tcp-80 \
                --load-balancing-scheme external \
                --region us-central1 \
                --ports 80 \
                --address network-lb-ipv4 \
                --backend-service backend-service-tcp-80
            

     4. **For IPv6 traffic:** Create a forwarding rule to route incoming TCP traffic on port 80 to the backend service. `TCP` is the default forwarding rule protocol and does not need to be set explicitly.

Use the IPv6 address range reserved in step 1 as the static external IP address of the load balancer. The subnet used must be a dual-stack subnet with an external IPv6 subnet range.
            
            gcloud compute forwarding-rules create forwarding-rule-tcp-80 \
                --load-balancing-scheme external \
                --region us-central1 \
                --network-tier PREMIUM \
                --ip-version IPV6 \
                --subnet lb-subnet \
                --address network-lb-ipv6 \
                --ports 80 \
                --backend-service backend-service-tcp-80
            

  5. Create the second load balancer for TCP on port 8080, UDP, ESP, and ICMP traffic.

     1. Create a [backend service](https://docs.cloud.google.com/compute/docs/reference/latest/backendServices) with the protocol set to `UNSPECIFIED`.
            
            gcloud compute backend-services create backend-service-l3-default \
                --protocol UNSPECIFIED \
                --health-checks tcp-health-check-8080 \
                --health-checks-region us-central1 \
                --region us-central1
            

     2. Add the backend instance group to the backend service.
            
            gcloud compute backend-services add-backend backend-service-l3-default \
                --instance-group ig-us-l3-default \
                --instance-group-zone us-central1-c \
                --region us-central1
            

     3. **For IPv4 traffic:** Create a forwarding rule with the protocol set to `L3_DEFAULT` to handle all remaining supported IP protocol traffic (TCP on port 8080, UDP, ESP, and ICMP). All ports must be configured with `L3_DEFAULT` forwarding rules.

Use the same external IPv4 address that you used for the previous load balancer.
            
            gcloud compute forwarding-rules create forwarding-rule-l3-default \
                --load-balancing-scheme external \
                --region us-central1 \
                --ports all \
                --ip-protocol L3_DEFAULT \
                --address network-lb-ipv4 \
                --backend-service backend-service-l3-default
            

     4. **For IPv6 traffic:** Create a forwarding rule with the protocol set to `L3_DEFAULT` to handle all remaining supported IP protocol traffic (TCP on port 8080, UDP, ESP, and ICMP). All ports must be configured with `L3_DEFAULT` forwarding rules.

Use the IPv6 address range reserved in step 1 as the static external IP address of the load balancer. The subnet used must be a dual-stack subnet with an external IPv6 subnet range.
            
            gcloud compute forwarding-rules create forwarding-rule-l3-default \
                --load-balancing-scheme external \
                --region us-central1 \
                --network-tier PREMIUM \
                --ip-version IPV6 \
                --subnet lb-subnet \
                --address network-lb-ipv6 \
                --ports all \
                --ip-protocol L3_DEFAULT \
                --backend-service backend-service-l3-default
            




## Test the load balancer

Now that the load balancing service is configured, you can start sending traffic to the load balancer's external IP address and watch traffic get distributed to the backend instances.

### Look up the load balancer's external IP address

###  Console 

  1. In the Google Cloud console, go to the **Load balancing components** load balancing page.

[Go to Load balancing components](https://console.cloud.google.com/loadbalancing/advanced/forwardingRules/list)

  2. On the **Forwarding Rules** tab, locate the forwarding rules used by the load balancer.

  3. In the **IP Address** column, note the external IP address listed for each IPv4 and IPv6 forwarding rule.




###  gcloud: IPv4 

Enter the following command to view the external IP address of the forwarding rule used by the load balancer.
    
    
    gcloud compute forwarding-rules describe forwarding-rule-tcp-80 \
        --region us-central1
    

This example uses the same IP address for both IPv4 forwarding rules, so using `forwarding-rule-l3-default` also works.

###  gcloud: IPv6 

Enter the following command to view the external IPv6 address of the `forwarding-rule-tcp-80` forwarding rule used by the load balancer.
    
    
    gcloud compute forwarding-rules describe forwarding-rule-tcp-80 \
        --region us-central1
    

This example uses the same IP address for both IPv6 forwarding rules, so using `forwarding-rule-l3-default` also works.

### Send traffic to the load balancer

This procedure sends external traffic to the load balancer. Run the following tests to help ensure that TCP traffic on port 80 is being load-balanced by the `ig-us-tcp-80` instance group while all other traffic (TCP on port 8080, UDP, ESP, and ICMP) is being handled by the `ig-us-l3-default` instance group.

#### Verifying behavior with TCP requests on port 80

  1. Make web requests (over TCP on port 80) to the load balancer using `curl` to contact its IP address.

     * From clients with IPv4 connectivity, run the following command:
           
           while true; do curl -m1 IP_ADDRESS; done
           

     * From clients with IPv6 connectivity, run the following command:
           
           while true; do curl -m1 http://IPV6_ADDRESS; done
           

For example, if the assigned IPv6 address is [2001:db8:1:1:1:1:1:1/96], the command is similar to the following:
           
           while true; do curl -m1 http://[2001:db8:1:1:1:1:1:1]; done
           

  2. Note the text returned by the `curl` command. The name of the backend VM generating the response is displayed in that text—for example, `Page served from: VM_NAME`. Responses come only from instances in the `ig-us-tcp-80` instance group.

If your response is initially unsuccessful, you might need to wait approximately 30 seconds for the configuration to be fully loaded and for your instances to be marked healthy before trying again.




#### Verifying behavior with TCP requests on port 8080

Make web requests (over TCP on port 8080) to the load balancer using `curl` to contact its IP address.

  * From clients with IPv4 connectivity, run the following command:
        
        while true; do curl -m1 IPV4_ADDRESS:8080; done
        

  * From clients with IPv6 connectivity, run the following command:
        
        while true; do curl -m1 http://IPV6_ADDRESS; done
        

For example, if the assigned IPv6 address is [2001:db8:1:1:1:1:1:1/96], the command is similar to the following:
        
        while true; do curl -m1 http://[2001:db8:1:1:1:1:1:1]:8080; done
        




Note the text returned by the `curl` command. Responses come only from instances in the `ig-us-l3-default` instance group.

This shows that any traffic sent to the load balancer's IP address at port 8080 is handled only by backends in the `ig-us-l3-default` instance group.

#### Verifying behavior with ICMP requests

To verify behavior with ICMP traffic, you capture output from the `tcpdump` command to confirm that only backend VMs in the `ig-us-l3-default` instance group are handling ICMP requests send to the load balancer.

  1. Use SSH to connect to the backend VMs.

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

     2. In the list of virtual machine (VM) instances, click **SSH** in the row of the instance that you want to connect to.

  2. Run the following command to use `tcpdump` to start listening for ICMP traffic.
         
         sudo tcpdump icmp -w ~/icmpcapture.pcap -s0 -c 10000
         tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
         

Leave the SSH window open.

  3. Repeat steps 1 and 2 for all four backend VMs.

  4. Make ICMP requests to the load balancer.

To test the IPv4 responses, use `ping` to contact the load balancer's IPv4 address.
         
         ping IPV4_ADDRESS
         

To test the IPv6 responses, use `ping6` to contact the load balancer's IPv6 address.
         
         ping6 IPV6_ADDRESS
         

For example, if the assigned IPv6 address is [2001:db8:1:1:1:1:1:1/96], the command is similar to the following:
         
         ping6 2001:db8:1:1:1:1:1:1
         

  5. Go back to each VM's open SSH window and stop the `tcpdump` capture command. You can use Ctrl+C to do this.

  6. For each VM, check the output of the `tcpdump` command in the `icmpcapture.pcap` file.
         
         sudo tcpdump -r ~/icmpcapture.pcap -n
         

For backend VMs in the `ig-us-l3-default` instance group, you see file entries that are similar to the following:
         
         reading from file /home/[user-directory]/icmpcapture.pcap, link-type EN10MB (Ethernet)
         22:13:07.814486 IP 35.230.115.24 > 35.193.84.93: ICMP echo request, id 1995, seq 1, length 64
         22:13:07.814513 IP 35.193.84.93 > 35.230.115.24: ICMP echo reply, id 1995, seq 1, length 64
         22:13:08.816150 IP 35.230.115.24 > 35.193.84.93: ICMP echo request, id 1995, seq 2, length 64
         22:13:08.816175 IP 35.193.84.93 > 35.230.115.24: ICMP echo reply, id 1995, seq 2, length 64
         22:13:09.817536 IP 35.230.115.24 > 35.193.84.93: ICMP echo request, id 1995, seq 3, length 64
         22:13:09.817560 IP 35.193.84.93 > 35.230.115.24: ICMP echo reply, id 1995, seq 3, length 64
         ...
         

For backend VMs in the `ig-us-tcp-80` instance group, you see that no packets have been received and the file is blank:
         
         reading from file /home/[user-directory]/icmpcapture.pcap, link-type EN10MB (Ethernet)
         




## Additional configuration options

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
  * `PROTOCOL`: the IP protocol for the forwarding rule. The default is `TCP`. For this example, the IP protocol can be one of `TCP` or `L3_DEFAULT`.
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
  * `PROTOCOL`: the IP protocol for the forwarding rule. The default is `TCP`. For this example, the IP protocol can be one of `TCP` or `L3_DEFAULT`.
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

  * To configure a regional external passthrough Network Load Balancer with zonal NEG backends that let you forward packets to non-`nic0` network interfaces of VM instances, see [Set up a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg).
  * For information about how regional external passthrough Network Load Balancers work with backend services, see [Backend service-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).
  * To learn how to transition a regional external passthrough Network Load Balancer from a target pool backend to a regional backend service, see [Migrate regional external passthrough Network Load Balancers from target pools to backend services](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services).
  * To configure advanced network DDoS protection for a regional external passthrough Network Load Balancer by using Cloud Armor, see [Configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).
  * To delete resources, see [Cleaning up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
