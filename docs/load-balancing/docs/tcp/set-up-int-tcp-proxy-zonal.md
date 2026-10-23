---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-zonal/
title: Set up a regional internal proxy Network Load Balancer with zonal NEG backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:15.105872+00:00
---

# Set up a regional internal proxy Network Load Balancer with zonal NEG backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-zonal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional internal proxy Network Load Balancer with zonal NEG backends Stay organized with collections  Save and categorize content based on your preferences. 

The regional internal proxy Network Load Balancer is a proxy-based regional Layer 4 load balancer that lets you run and scale your TCP service traffic behind an internal IP address that is accessible only to clients in the same VPC network or clients connected to your VPC network.

This guide contains instructions for setting up a regional internal proxy Network Load Balancer with a zonal network endpoint group (NEG) backend. Before you start:

  * Read the [Regional internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
  * Read the [zonal NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts)



## Overview

In this example, we'll use the load balancer to distribute TCP traffic across backend VMs in two zonal NEGs in the `REGION_A` region. For purposes of the example, the service is a set of [Apache](https://httpd.apache.org/) servers configured to respond on port `80`.

In this example, you configure the following deployment:

[ ![Regional internal proxy Network Load Balancer example configuration with zonal NEG backends.](https://docs.cloud.google.com/static/load-balancing/images/int-tcp-proxy-zonal.svg)](https://docs.cloud.google.com/static/load-balancing/images/int-tcp-proxy-zonal.svg) Regional internal proxy Network Load Balancer example configuration with zonal NEG backends.

The regional internal proxy Network Load Balancer is a regional load balancer. All load balancer components (backend instance groups, backend service, target proxy, and forwarding rule) must be in the same region.

## Permissions

To follow this guide, you must be able to create instances and modify a network in a project. You must be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required Role  
---|---  
Create networks, subnets, and load balancer components | [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Add and remove firewall rules | [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Configure the network and subnets

You need a VPC network with two subnets: one for the load balancer's backends and the other for the load balancer's proxies. Regional internal proxy Network Load Balancers are regional. Traffic within the VPC network is routed to the load balancer if the traffic's source is in a subnet in the same region as the load balancer.

This example uses the following VPC network, region, and subnets:

  * **Network.** The network is a [custom-mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.

  * **Subnet for backends.** A subnet named `backend-subnet` in the `REGION_A` region uses `10.1.2.0/24` for its primary IP range.

  * **Subnet for proxies.** A subnet named `proxy-only-subnet` in the `REGION_A` region uses `10.129.0.0/23` for its primary IP range.


**Note:** You can change the name of the network, the region, and the parameters for the subnets; however, subsequent steps in this guide use the network, region, and subnet parameters as outlined here.

### Create the network and subnet for backends

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For the **Name** , enter `lb-network`.

  4. In the **Subnets** section:

     * Set the **Subnet creation mode** to **Custom**.
     * In the **New subnet** section, enter the following information: 
       * **Name** : `backend-subnet`
       * **Region** : `REGION_A`
       * **IP address range** : `10.1.2.0/24`
     * Click **Done**.
  5. Click **Create**.




###  gcloud 

  1. Create the custom VPC network with the [`gcloud compute networks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) command:
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. Create a subnet in the `lb-network` network in the `REGION_A` region with the [`gcloud compute networks subnets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command:
         
         gcloud compute networks subnets create backend-subnet \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=REGION_A
         




### Create the proxy-only subnet

A [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides a set of IP addresses that Google uses to run Envoy proxies on your behalf. The proxies terminate connections from the client and create new connections to the backends.

This proxy-only subnet is used by all [Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) in the `REGION_A` region of the `lb-network` VPC network.

**Important:** Don't try to assign addresses from the proxy-only subnet to your load balancer's forwarding rule or backends. You assign the forwarding rule's IP address and the backend instance IP addresses from a different subnet range (or ranges), not this one. Google Cloud reserves this subnet range for Google Cloud-managed proxies.

###  Console 

If you're using the Google Cloud console, you can wait and create the proxy-only subnet later on the **Load balancing** page.

If you want to create the proxy-only subnet now, use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the Shared VPC network: `lb-network`.

  3. Click **Add subnet**.

  4. For the **Name** , enter `proxy-only-subnet`.

  5. For the **Region** , select `REGION_A`.

  6. Set **Purpose** to **Regional Managed Proxy**.

  7. For the **IP address range** , enter `10.129.0.0/23`.

  8. Click **Add**.




###  gcloud 

Create the proxy-only subnet with the [`gcloud compute networks subnets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command.
    
    
    gcloud compute networks subnets create proxy-only-subnet \
        --purpose=REGIONAL_MANAGED_PROXY \
        --role=ACTIVE \
        --region=REGION_A \
        --network=lb-network \
        --range=10.129.0.0/23
    

## Create firewall rules

In this example, you create the following firewall rules:

  * `fw-allow-health-check`: An ingress rule, applicable to the Google Cloud instances being load balanced, that allows traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check` to identify the backend VMs to which it should apply.
  * `fw-allow-ssh`: An ingress rule that allows incoming SSH connectivity on TCP port 22 from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify just the IP ranges of the systems from which you will initiate SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it should apply.
  * `fw-allow-proxy-only-subnet`: Create an ingress allow firewall rule for the proxy-only subnet to allow the load balancer to communicate with backend instances on TCP port `80`. This example uses the target tag `allow-proxy-only-subnet` to identify the backend VMs to which it should apply.




###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** :

     1. Enter a **Name** of `fw-allow-health-check`.
     2. Under **Network** , select `lb-network`.
     3. Under **Targets** , select **Specified target tags**.
     4. Populate the **Target tags** field with `allow-health-check`.
     5. Set **Source filter** to **IPv4 ranges**.
     6. Set **Source IPv4 ranges** to `35.191.0.0/16`.
     7. Under **Protocols and ports** , select **Specified protocols and ports**.
     8. Select the **TCP** checkbox and enter `80` for the port numbers.
     9. Click **Create**.
  3. Click **Create firewall rule** again to create the rule to allow incoming SSH connections:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : Choose _Specified protocols and ports_ then type: `tcp:22`
  4. Click **Create**.

  5. Click **Create firewall rule** again to create the rule to allow incoming connections from the proxy-only subnet to the Google Cloud backends:

     * **Name** : `fw-allow-proxy-only-subnet`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-proxy-only-subnet`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.129.0.0/23`
     * **Protocols and ports** : Choose _Specified protocols and ports_ then type: `tcp:80`
  6. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-health-check` rule to allow the Google Cloud health checks to reach the backend instances on a TCP port `80`:
         
         gcloud compute firewall-rules create fw-allow-health-check \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check \
             --source-ranges=35.191.0.0/16 \
             --rules=tcp:80
         

  2. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         

  3. Create an ingress allow firewall rule for the proxy-only subnet to allow the load balancer to communicate with backend instances on TCP port `80`:
         
         gcloud compute firewall-rules create fw-allow-proxy-only-subnet \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-proxy-only-subnet \
             --source-ranges=10.129.0.0/23 \
             --rules=tcp:80
         




## Reserve the load balancer's IP address

To reserve a static internal IP address for your load balancer, see [Reserve a new static internal IPv4 or IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip).

**Note:** Ensure that you use the subnet name that you specified when you created the subnet.

## Set up the zonal NEG

Set up a zonal NEG (with `GCE_VM_IP_PORT` type endpoints) in the `REGION_A` region. First create the VMs. Then create a zonal NEG and add the VMs' network endpoints to the NEG.

### Create VMs

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set the **Name** to `vm-a1`.

  4. For the **Region** , select `REGION_A`.

  5. For the **Zone** , see `ZONE_A1`.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. Click **Choose** to change the image if necessary.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`, `allow-health-check` and `allow-proxy-only-subnet`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network`
        * **Subnet** : `backend-subnet`
  9. Click **Management**. Enter the following script into the **Startup script** field.
         
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

  11. Repeat the following steps to create 3 more VMs, using the following name and zone combinations:

     * Name: `vm-a2`, zone: `ZONE_A1`
     * Name: `vm-c1`, zone: `ZONE_A2`
     * Name: `vm-c2`, zone: `ZONE_A2`



###  gcloud 

Create the VMs by running the following command two times, using these combinations for VM_NAME and ZONE. The script contents are identical for both VMs.

  * VM_NAME: `vm-a1` and ZONE: `ZONE_A1`
  * VM_NAME: `vm-a2` and ZONE: `ZONE_A1`
  * VM_NAME: `vm-c1` and ZONE: `ZONE_A2`
  * VM_NAME: `vm-c2` and ZONE: `ZONE_A2`
        
        gcloud compute instances create VM_NAME \
            --zone=ZONE \
            --image-family=debian-12 \
            --image-project=debian-cloud \
            --tags=allow-ssh,allow-health-check,allow-proxy-only-subnet \
            --subnet=backend-subnet \
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
        




### Create the zonal NEGs

###  Console 

To create a zonal network endpoint group:

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)  


  2. Click **Create network endpoint group**.

  3. For **Name** , enter `zonal-neg-a`.

  4. For **Network endpoint group type** , select **Network endpoint group (Zonal)**.

  5. For **Network** , select `lb-network`.

  6. For **Subnet** , select `backend-subnet`.

  7. For **Zone** , select `ZONE_A1`.

  8. Enter the **Default port** : `80`.

  9. Click **Create**.

  10. Repeat all the steps in this section to create a second zonal NEG with the following changes in settings:

     * **Name** : `zonal-neg-c`
     * **Zone** : `ZONE_A2`



Add endpoints to the zonal NEGs:

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)  


  2. Click the **Name** of the network endpoint group created in the previous step (for example, `zonal-neg-a`). You see the **Network endpoint group details** page.

  3. In the **Network endpoints in this group** section, click **Add network endpoint**. You see the **Add network endpoint** page.

  4. Select a **VM instance** (for example, `vm-a1`). In the **Network interface** section, the VM name, zone, and subnet is displayed.

     1. Enter the **IP address** of the new network endpoint. You can click **Check primary IP addresses and alias IP range in nic0** for the IP address.
     2. For **Port type** , select **Default** , the endpoint uses the default port `80` for all endpoints in the network endpoint group. This is sufficient for our example because the Apache server is serving requests at port `80`.
     3. Click **Create**.
  5. Again click **Add network endpoint**. Select the second VM instance, `vm-a2`, and repeat these steps to add its endpoints to `zonal-neg-a`.

  6. Repeat all the steps in this section to add endpoints from `vm-c1` and `vm-c2` to `zonal-neg-c`.




###  gcloud 

  1. Create a zonal NEG in the `ZONE_A1` zone with `GCE_VM_IP_PORT` endpoints.
         
         gcloud compute network-endpoint-groups create zonal-neg-a \
            --network-endpoint-type=GCE_VM_IP_PORT \
            --zone=ZONE_A1 \
            --network=lb-network \
            --subnet=backend-subnet
         

You can either specify the `--default-port` while creating the NEG, or [specify a port number for each endpoint](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#adding-endpoints) as shown in the next step.

  2. Add endpoints to the zonal NEG.
         
         gcloud compute network-endpoint-groups update zonal-neg-a \
             --zone=ZONE_A1 \
             --add-endpoint='instance=vm-a1,port=80' \
             --add-endpoint='instance=vm-a2,port=80'
         

  3. Create a zonal NEG in the `ZONE_A2` zone with `GCE_VM_IP_PORT` endpoints.
         
         gcloud compute network-endpoint-groups create zonal-neg-c \
             --network-endpoint-type=GCE_VM_IP_PORT \
             --zone=ZONE_A2 \
             --network=lb-network \
             --subnet=backend-subnet
         

You can either specify the `--default-port` while creating the NEG, or [specify a port number for each endpoint](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#adding-endpoints) as shown in the next step.

  4. Add endpoints to the zonal NEG.
         
         gcloud compute network-endpoint-groups update zonal-neg-c \
             --zone=ZONE_A2 \
             --add-endpoint='instance=vm-c1,port=80' \
             --add-endpoint='instance=vm-c2,port=80'
         




## Configure the load balancer

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Proxy load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. For **Cross-region or single region deployment** , select **Best for regional workloads** and click **Next**.
  7. Click **Configure**.



#### Basic configuration

  1. For **Name** , enter `my-int-tcp-lb`.
  2. For **Region** , select `REGION_A`.
  3. For **Network** , select `lb-network`.



#### Reserve a proxy-only subnet

**Note:** If you already created the proxy-only subnet, the **Reserve subnet** button isn't displayed. You can skip this section and continue with the steps in the **Backend configuration** section.

To reserve a proxy-only subnet:

  1. Click **Reserve subnet**.
  2. For **Name** , enter `proxy-only-subnet`.
  3. For **IP address range** , enter `10.129.0.0/23`.
  4. Click **Add**.



#### Backend configuration

  1. Click **Backend configuration**.
  2. For **Backend type** , select **Zonal network endpoint group**.
  3. For **Protocol** , select **TCP**.
  4. In the **Health check** list, click **Create a health check** , and then enter the following information: 
     1. **Name** : `tcp-health-check`
     2. **Protocol** : **TCP**
     3. **Port** : `80`
  5. Click **Create**.
  6. Configure the first backend: 
     1. Under **New backend** , select zonal NEG `zonal-neg-a`.
     2. Retain the remaining default values and click **Done**.
  7. Configure the second backend:

     1. Click **Add backend**.
     2. Under **New backend** , select instance group `zonal-neg-c`.
     3. Retain the remaining default values and click **Done**.
  8. In the Google Cloud console, verify that there is a check mark next to **Backend configuration**. If not, double-check that you have completed all of the steps.




#### Frontend configuration

  1. Click **Frontend configuration**.
  2. For **Name** , enter `int-tcp-forwarding-rule`.
  3. For **Subnetwork** , select **backend-subnet**.
  4. For **IP address** , select **int-tcp-ip-address**.
  5. For **Port number** , enter `9090`. The forwarding rule only forwards packets with a matching destination port.
  6. In this example, don't enable the **Proxy Protocol** because it doesn't work with the Apache HTTP Server software. For more information, see Proxy protocol.
  7. Click **Done**.
  8. In the Google Cloud console, verify that there is a check mark next to **Frontend configuration**. If not, double-check that you have completed all the previous steps.



#### Review and finalize

  1. Click **Review and finalize**.
  2. Double-check your settings.
  3. Click **Create**.



###  gcloud 

  1. Create a regional health check for the backends.
         
         gcloud compute health-checks create tcp tcp-health-check \
             --region=REGION_A \
             --use-serving-port
         

  2. Create a backend service.
         
         gcloud compute backend-services create internal-tcp-proxy-bs \
            --load-balancing-scheme=INTERNAL_MANAGED \
            --protocol=TCP \
            --region=REGION_A \
            --health-checks=tcp-health-check \
            --health-checks-region=REGION_A
         

  3. Add the zonal NEG in the `ZONE_A1` zone to the backend service.
         
         gcloud compute backend-services add-backend internal-tcp-proxy-bs \
            --network-endpoint-group=zonal-neg-a \
            --network-endpoint-group-zone=ZONE_A1 \
            --balancing-mode=CONNECTION \
            --max-connections-per-endpoint=50 \
            --region=REGION_A
         

  4. Add the zonal NEG in the `ZONE_A2` zone to the backend service.
         
         gcloud compute backend-services add-backend internal-tcp-proxy-bs \
            --network-endpoint-group=zonal-neg-c \
            --network-endpoint-group-zone=ZONE_A2 \
            --balancing-mode=CONNECTION \
            --max-connections-per-endpoint=50 \
            --region=REGION_A
         

  5. Create the target TCP proxy.
         
         gcloud compute target-tcp-proxies create int-tcp-target-proxy \
            --backend-service=internal-tcp-proxy-bs \
            --region=REGION_A
         

  6. Create the forwarding rule. For `--ports`, specify a single port number from 1-65535. This example uses port `9090`. The forwarding rule only forwards packets with a matching destination port.
         
         gcloud compute forwarding-rules create int-tcp-forwarding-rule \
           --load-balancing-scheme=INTERNAL_MANAGED \
           --network=lb-network \
           --subnet=backend-subnet \
           --address=int-tcp-ip-address \
           --ports=9090 \
           --region=REGION_A \
           --target-tcp-proxy=int-tcp-target-proxy \
           --target-tcp-proxy-region=REGION_A
         




## Test the load balancer

To test the load balancer, create a client VM in the same region as the load balancer. Then send traffic from the client to the load balancer.

### Create a client VM

Create a client VM (`client-vm`) in the same region as the load balancer.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set **Name** to `client-vm`.

  4. Set **Zone** to `ZONE_A1`.

  5. Click **Advanced options**.

  6. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network`
        * **Subnet** : `backend-subnet`
  7. Click **Create**.




###  gcloud 

The client VM must be in the same VPC network and region as the load balancer. It doesn't need to be in the same subnet or zone. The client uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create client-vm \
        --zone=ZONE_A1 \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=backend-subnet
    

### Send traffic to the load balancer

**Note:** It might take a few minutes for the load balancer configuration to propagate globally after you first deploy it.

Now that you have configured your load balancer, you can test sending traffic to the load balancer's IP address.

  1. Use SSH to connect to the client instance.
         
         gcloud compute ssh client-vm \
           --zone=ZONE_A1
         

  2. Verify that the load balancer is serving backend hostnames as expected.

     1. Use the [`compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to view the load balancer's IP address:
            
            gcloud compute addresses describe int-tcp-ip-address \
              --region=REGION_A
            

Make a note of the IP address.

     2. Send traffic to the load balancer. Replace IP_ADDRESS with the IP address of the load balancer.
            
            curl IP_ADDRESS:9090
            




## What's next

  * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)
  * [Regional internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).
  * To set up monitoring for your regional internal proxy Network Load Balancer, see [Using monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring).
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
