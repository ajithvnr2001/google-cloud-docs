---
url: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service/
title: Set up a regional external passthrough Network Load Balancer with a backend service \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:45.357970+00:00
---

# Set up a regional external passthrough Network Load Balancer with a backend service  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external passthrough Network Load Balancer with a backend service Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides instructions for creating a [regional external passthrough Network Load Balancer deployment by using a regional backend service](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service). This example creates a regional external passthrough Network Load Balancer that supports either TCP or UDP traffic. If you want to create a regional external passthrough Network Load Balancer that load-balances TCP, UDP, ESP, GRE, ICMP, and ICMPv6 traffic (not just TCP or UDP), see [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols).

This example uses the load balancer to distribute TCP traffic across backend VMs in two zonal managed instance groups in the `us-central1` region. An equally valid approach is to use a single regional managed instance group for the `us-central1` region.

[ ![Regional external passthrough Network Load Balancer with zonal instance groups.](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-zonal.svg)](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-zonal.svg) Regional external passthrough Network Load Balancer with zonal managed instance groups (click to enlarge).

This scenario load balances TCP connections and uses a TCP health check. For information about other supported protocols, see [Regional backend service](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#backend-service) and [Health checks](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#health-checks).

The regional external passthrough Network Load Balancer is a regional load balancer. All load balancer components (backend VMs, backend service, and forwarding rule) must be in the same region.

## Before you begin

Install the Google Cloud CLI. For a complete overview of the tool, see the [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). You can find commands related to load balancing in the [API and gcloud references](https://docs.cloud.google.com/load-balancing/docs/apis).

If you haven't run the Google Cloud CLI previously, first run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.

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

The instance group references an instance template, which is used to create backend VMs. In this example, you create backend VMs with IPv4-only, dual-stack, and IPv6-only network interfaces. The VMs also inherit the `ipv6-access-type` setting (in this example, `EXTERNAL`) from the subnet. For more information about IPv6 requirements, see [Forwarding rule](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule) in the regional external passthrough Network Load Balancer overview.

To use existing VMs as backends, update the VMs to be dual-stack by using the [`gcloud compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update).

Instances that participate as backend VMs for regional external passthrough Network Load Balancers must be running the appropriate [Linux Guest Environment](https://docs.cloud.google.com/compute/docs/instances/linux-guest-environment), [Windows Guest Environment](https://github.com/GoogleCloudPlatform/compute-image-windows), or other processes that provide equivalent capability.

### Setting up the instances

###  Console 

**Create an instance template**

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.

  3. For **Name** , enter `ig-us-template`.

  4. In the **Boot disk** section, ensure that the **Image** is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.

  5. Click **Advanced options**.

  6. Click **Networking**.

     1. For **Network tags** , enter `lb-tag`.
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
     3. Click **Done**.

  7. Click **Management** and copy the following script into the **Startup script** field.
         
         #! /bin/bash
           apt-get update
           apt-get install apache2 -y
           a2ensite default-ssl
           a2enmod ssl
           vm_hostname="$(curl -H "Metadata-Flavor:Google"   
         
           http://metadata.google.internal/computeMetadata/v1/instance/name)"
           echo "Page served from: $vm_hostname" |   
         
           tee /var/www/html/index.html
           systemctl restart apache2
           

  8. Click **Create**.




**Create a managed instance group**

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**.

  3. Select **New managed instance group (stateless)**. For more information, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

  4. For **Name** , enter `ig-us-1`.

  5. For **Instance template** , select `ig-us-template`.

  6. For **Location** , select **Single zone**.

  7. For **Region** , select `us-central1`.

  8. For **Zone** , select `us-central1-a`.

  9. Specify the number of instances that you want to create in the group.

For this example, specify the following options in the **Autoscaling** section:

     * For **Autoscaling mode** , select `Off:do not autoscale`.
     * For **Maximum number of instances** , enter `2`.
  10. Click **Create**.




Repeat the previous steps to create a second managed instance group in the `us-central1-c` zone with the following specifications:

  * **Name** : `ig-us-2`
  * **Zone** : `us-central1-c`
  * **Instance template** : Use the same `ig-us-template` template created in the previous section.



###  gcloud 

The `gcloud` instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.

  1. Create a VM instance template with HTTP server with the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

To create backend VMs with _dual-stack_ network interfaces, use the following command.

Set `--ipv6-network-tier` to `PREMIUM` only if you are creating the VMs in subnets with `ipv6-access-type` set to `EXTERNAL`. Omit the flag if the subnet's `ipv6-access-type` is `INTERNAL`.
         
         gcloud compute instance-templates create ig-us-template \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --ipv6-network-tier=PREMIUM \
               --stack-type=IPV4_IPV6 \
               --tags=lb-tag \
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
         
         gcloud compute instance-templates create ig-us-template \
               --region=us-central1 \
               --network=lb-network \
               --subnet=lb-subnet \
               --stack-type=IPV4_ONLY \
               --tags=lb-tag \
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
         

To create backend VMs with _IPv6-only_ network interfaces, use the following command.

**Note:** Set `--ipv6-network-tier` to `PREMIUM` only if you are creating the VMs in subnets with `ipv6-access-type` set to `EXTERNAL`. Omit the flag if the subnet's `ipv6-access-type` is `INTERNAL`.
         
         gcloud compute instance-templates create ig-us-template \
             --region=us-central1 \
             --network=lb-network \
             --subnet=lb-subnet \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV6_ONLY \
             --tags=lb-tag \
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
         
         gcloud compute instance-groups managed create ig-us-1 \
               --zone us-central1-a \
               --size 2 \
               --template ig-us-template
         

  3. Create a second managed instance group in the `us-central1-c` zone:
         
         gcloud compute instance-groups managed create ig-us-2 \
              --zone us-central1-c \
              --size 2 \
              --template ig-us-template
         




## Configure firewall rules

Create firewall rules that allow external traffic—which includes health check probes—to reach the backend instances.

This example creates a firewall rule that allows TCP traffic from _all_ source ranges to reach your backend instances on port 80. If you want to create separate firewall rules specifically for the health check probes, use the source IP address ranges documented in the [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) section of the Health checks overview.

###  Console 

In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

To allow **IPv4 traffic** , perform the following steps:

  1. Click **Create firewall rule**.
  2. For **Name** , enter `allow-network-lb-ipv4`.
  3. In the **Network** list, select **`lb-network`**.
  4. For **Targets** , select **Specified target tags**.
  5. In the **Target tags** field, enter `lb-tag`.
  6. For **Source filter** , select **IPv4 ranges**.
  7. Set the **Source IPv4 ranges** to `0.0.0.0/0`. This allows IPv4 traffic from any source. This also allows Google's health check probes to reach the backend instances.
  8. For **Specified protocols and ports** , select the **TCP** checkbox and enter `80`.
  9. Click **Create**. It might take a moment for the Google Cloud console to display the new firewall rule, or you might have to click **Refresh** to see the rule.



To allow **IPv6 traffic** , perform the following steps:

  1. Click **Create firewall rule** again.
  2. For **Name** , enter `allow-network-lb-ipv6`.
  3. In the **Network** list, select **`lb-network`**.
  4. For **Targets** , select **Specified target tags**.
  5. In the **Target tags** field, enter `lb-tag`.
  6. For **Source filter** , select **IPv6 ranges**.
  7. Set the **Source IPv6 ranges** to `::/0`. This allows IPv6 traffic from any source. This also allows Google's health check probes to reach the backend instances.
  8. For **Specified protocols and ports** , select the **TCP** checkbox and enter `80`.
  9. Click **Create**. It might take a moment for the console to display the new firewall rule, or you might have to click **Refresh** to see the rule.



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

When you configure the load balancer, your virtual machine (VM) instances receive packets that are destined for the static external IP address you configure. If you are using an [image provided by Compute Engine](https://docs.cloud.google.com/compute/docs/images#os-compute-support), your instances are automatically configured to handle this IP address. If you are using any other image, you must configure this address as an alias on `eth0` or as a loopback on each instance.

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

  1. On the **Create external passthrough Network Load Balancer** page, enter the name `tcp-network-lb` for the new load balancer.
  2. For **Region** , select `us-central1`.
  3. Click **Backend configuration**.
  4. On the **Backend configuration** page, do the following: 
     1. In the **Health check** list, click **Create a health check** , and then enter the following information: 
        * **Name** : `tcp-health-check`
        * **Protocol** : **TCP**
        * **Port** : `80`
     2. Click **Create**.
     3. For **New Backend** , select the IP stack type.
     4. In the **Instance group** list, select `ig-us-1`, and then click **Done**.
     5. Click **Add a backend** and repeat this step to add `ig-us-2`.
     6. Click **Save**.
  5. Before continuing, verify that there is a blue checkmark next to **Backend configuration**.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. For **Name** , enter `network-lb-forwarding-rule`.
  3. To handle IPv4 traffic, use the following steps: 
     1. For **IP version** , select **IPv4**.
     2. Click the **IP address** list and select **Create IP address**. 
        1. On the **Reserve a new static IP address** page, for **Name** , enter `network-lb-ipv4`.
        2. Click **Reserve**.
     3. For **Ports** , choose **Single**. For **Port number** , enter `80`.
     4. Click **Done**.
  4. To handle IPv6 traffic, use the following steps:

     1. For **IP version** , select **IPv6**.
     2. For **Subnetwork** , select **lb-subnet**.
     3. In the **IPv6 range** list, select **Create IP address**. 
        1. On the **Reserve a new static IP address** page, for **Name** , enter `network-lb-ipv6`.
        2. Click **Reserve**.
     4. For **Ports** , select **Single**. For **Port number** , enter `80`.
     5. Click **Done**.

Before continuing, verify a successful setup by confirming that there's a blue circle with a checkmark to the left of **Frontend configuration**.




#### Review the configuration

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request to be used to create the load balancer.
  4. Click **Create**.

On the load balancing page, in the **Backend** column for your new load balancer, confirm that there's a green checkmark showing that the new load balancer is healthy.




###  gcloud 

  1. Reserve a static external IP address.

**For IPv4 traffic**

Create a [static external IPv4 address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) for your load balancer.
         
         gcloud compute addresses create network-lb-ipv4 \
              --region us-central1
         

**For IPv6 traffic**

Create a [static external IPv6 address range](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) for your load balancer. The subnet used must be a dual-stack subnet with an external IPv6 range.
         
         gcloud compute addresses create network-lb-ipv6 \
              --region us-central1 \
              --subnet lb-subnet \
              --ip-version IPV6 \
              --endpoint-type NETLB
         

  2. Create a TCP health check.
         
         gcloud compute health-checks create tcp tcp-health-check \
             --region us-central1 \
             --port 80
         

  3. Create a [backend service](https://docs.cloud.google.com/compute/docs/reference/latest/backendServices).
         
         gcloud compute backend-services create network-lb-backend-service \
             --protocol TCP \
             --health-checks tcp-health-check \
             --health-checks-region us-central1 \
             --region us-central1
         

  4. Add the instance groups to the backend service.
         
         gcloud compute backend-services add-backend network-lb-backend-service \
             --instance-group ig-us-1 \
             --instance-group-zone us-central1-a \
             --region us-central1
         
         
         gcloud compute backend-services add-backend network-lb-backend-service \
             --instance-group ig-us-2 \
             --instance-group-zone us-central1-c \
             --region us-central1
         

  5. Create the forwarding rules depending on whether you want to handle IPv4 traffic or IPv6 traffic. Create both forwarding rules to handle both types of traffic.

     1. **For IPv4 traffic**

Create a forwarding rule to route incoming TCP traffic to the backend service. Use the IPv4 address reserved in step 1 as the static external IP address of the load balancer.
            
            gcloud compute forwarding-rules create network-lb-forwarding-rule-ipv4 \
                 --load-balancing-scheme EXTERNAL \
                 --region us-central1 \
                 --ports 80 \
                 --address network-lb-ipv4 \
                 --backend-service network-lb-backend-service
            

     2. **For IPv6 traffic**

Create a forwarding rule to handle IPv6 traffic. Use the IPv6 address range reserved in step 1 as the static external IP address of the load balancer. The subnet used must be a dual-stack subnet or an IPv6-only subnet with an external IPv6 subnet range.
            
            gcloud compute forwarding-rules create network-lb-forwarding-rule-ipv6 \
                 --load-balancing-scheme EXTERNAL \
                 --region us-central1 \
                 --network-tier PREMIUM \
                 --ip-version IPV6 \
                 --subnet lb-subnet \
                 --address network-lb-ipv6 \
                 --ports 80 \
                 --backend-service network-lb-backend-service
            




## Test the load balancer

Now that the load balancing service is configured, you can start sending traffic to the load balancer's external IP address and watch traffic get distributed to the backend instances.

### Look up the load balancer's external IP address

###  Console 

  1. In the Google Cloud console, go to the **Load balancing components** load balancing page.

[Go to Load balancing components](https://console.cloud.google.com/loadbalancing/advanced/forwardingRules/list)

  2. On the **Forwarding Rules** tab, locate the forwarding rule used by the load balancer.

  3. In the **External IP address** column, note the external IP address listed.




###  gcloud: IPv4 

Enter the following command to view the external IPv4 address of the `network-lb-forwarding-rule` forwarding rule used by the load balancer.
    
    
    gcloud compute forwarding-rules describe network-lb-forwarding-rule-ipv4 \
        --region us-central1
    

###  gcloud: IPv6 

Enter the following command to view the external IPv6 address of the `network-lb-forwarding-rule` forwarding rule used by the load balancer.
    
    
    gcloud compute forwarding-rules describe network-lb-forwarding-rule-ipv6 \
        --region us-central1
    

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

This section expands on the configuration example to provide instructions about how to further customize your regional external passthrough Network Load Balancer. These tasks are optional. You can perform them in any order.

### Configure session affinity

The example configuration creates a backend service with session affinity disabled (value set to `NONE`). This section shows you how to update the backend service to change the load balancer's session affinity setting.

For supported session affinity types, see [Session affinity](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#session_affinity).

**Note:** For external _UDP_ load balancers, setting session affinity is supported in the gcloud CLI and the API. You cannot set session affinity for UDP load balancers using the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. On the **Load balancers** tab, click the name of the backend service, and then click **Edit**.

  3. On the **Edit external passthrough Network Load Balancer** page, click **Backend configuration**.

  4. Select an option from the **Session affinity** list.

  5. Click **Update**.




###  gcloud 

Use the following `gcloud` command to update session affinity for the backend service:
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --region=REGION \
        --session-affinity=SESSION_AFFINITY_OPTION
    

Replace the placeholders with valid values:

  * `BACKEND_SERVICE`: the backend service that you're updating
  * `SESSION_AFFINITY_OPTION`: the session affinity option that you want to set

For the list of supported values for a regional external passthrough Network Load Balancer, see [Session affinity options](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#session_affinity).




### Configure a connection tracking policy

The example configuration creates a backend service with the default settings for its connection tracking policy. This section shows you how to update the backend service to change the load balancer's default connection tracking policy.

A connection tracking policy includes the following settings:

  * [Connection tracking mode](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#tracking-mode)
  * [Connection persistence on unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#connection-persistence)
  * Idle timeout (60 seconds, not configurable)

**Note:** You cannot use the Google Cloud console to configure a connection tracking policy. Use the Google Cloud CLI or the REST API instead.

###  gcloud 

Use the following [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services) to update the connection tracking policy for the backend service:
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --region=REGION \
        --tracking-mode=TRACKING_MODE \
        --connection-persistence-on-unhealthy-backends=CONNECTION_PERSISTENCE_BEHAVIOR
    

Replace the placeholders with valid values:

  * `BACKEND_SERVICE`: the backend service that you're updating
  * `TRACKING_MODE`: the connection tracking mode to be used for incoming packets. For the list of supported values, see [Tracking mode](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#tracking-mode).
  * `CONNECTION_PERSISTENCE_BEHAVIOR`: the connection persistence behavior when backends are unhealthy. For the list of supported values, see [Connection persistence on unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#connection-persistence).



### Configure traffic steering

This section shows you how to update a load balancer's frontend configuration to set up source IP-based traffic steering. For details about how traffic steering works, see [Traffic steering](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#traffic-steering).

These instructions assume that you already have the parent base forwarding rule created. This example creates a second forwarding rule, which is the steering forwarding rule, with the same IP address, IP protocol, and ports as the parent. This steering forwarding rule is configured with source IP ranges so that you can customize how packets from those source IP ranges are forwarded.

**Note:** You cannot use the Google Cloud console to configure traffic steering. Use the Google Cloud CLI or the [REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) instead.

###  gcloud 

Use the following command to create a steering forwarding rule that points to a backend service:
    
    
    gcloud compute forwarding-rules create STEERING_FORWARDING_RULE_BS \
        --load-balancing-scheme=EXTERNAL \
        --backend-service=BACKEND_SERVICE \
        --address=LOAD_BALANCER_VIP \
        --ip-protocol=IP_PROTOCOL \
        --ports=PORTS \
        --region=REGION \
        --source-ip-ranges=SOURCE_IP_ADDRESS_RANGES
    

Use the following command to create a steering forwarding rule that points to a target instance:
    
    
    gcloud compute forwarding-rules create STEERING_FORWARDING_RULE_TI \
        --load-balancing-scheme=EXTERNAL \
        --target-instance=TARGET_INSTANCE \
        --address=LOAD_BALANCER_VIP \
        --ip-protocol=IP_PROTOCOL \
        --ports=PORTS \
        --region=REGION \
        --source-ip-ranges=SOURCE_IP_ADDRESS_RANGES
    

Replace the placeholders with valid values:

  * `STEERING_FORWARDING_RULE_BS` or `STEERING_FORWARDING_RULE_TI`: the name of the steering forwarding rule to create.
  * `BACKEND_SERVICE` or `TARGET_INSTANCE`: the name of the backend service or target instance to which this steering forwarding rule will send traffic. Even if the parent forwarding rule points to a backend service, you can create steering forwarding rules that point to target instances.
  * `LOAD_BALANCER_VIP`, `IP_PROTOCOL`, `PORTS`: the IP address, IP protocol, and ports, respectively, for the steering forwarding rule that you're creating. These settings must match a pre-existing base forwarding rule.
  * `REGION`: the region of the forwarding rule that you're creating.
  * `SOURCE_IP_ADDRESS_RANGES`: comma-separated list of IP addresses or IP address ranges. This forwarding rule only forwards traffic when the source IP address of the incoming packet falls into one of the IP ranges set here.



Use the following command to delete a steering forwarding rule. You must delete any steering forwarding rules that are being used by a load balancer before you can delete the load balancer itself.
    
    
    gcloud compute forwarding-rules delete STEERING_FORWARDING_RULE \
        --region=REGION
    

### Configure failover policy

To configure the failover policy, see [Configure failover for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-setting-up-failover).

### Configure weighted load balancing

To configure weighted load balancing, see [Configure weighted load balancing](https://docs.cloud.google.com/load-balancing/docs/network/configure-weighted-netlb).

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
  * `PROTOCOL`: the IP protocol for the forwarding rule. The default is `TCP`. For this example, the IP protocol can be one of `TCP` or `UDP`.
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
  * `PROTOCOL`: the IP protocol for the forwarding rule. The default is `TCP`. For this example, the IP protocol can be one of `TCP` or `UDP`.
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

  * To learn how to migrate a regional external passthrough Network Load Balancer from a target pool backend to a regional backend service, see [Migrate a regional external passthrough Network Load Balancer from target pool to backend service](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services).
  * To configure a regional external passthrough Network Load Balancer for multiple IP protocols (supporting IPv4 and IPv6 traffic), see [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols).
  * To configure a regional external passthrough Network Load Balancer with zonal network endpoint group (NEG) backends that let you forward packets to non-`nic0` network interfaces of VM instances, see [Set up a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg).
  * To configure advanced network DDoS protection for a regional external passthrough Network Load Balancer by using Cloud Armor, see [Configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).
  * To delete resources, see [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
