---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-zonal/
title: Set up a regional external proxy Network Load Balancer with zonal NEG backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:29.275788+00:00
---

# Set up a regional external proxy Network Load Balancer with zonal NEG backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-zonal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external proxy Network Load Balancer with zonal NEG backends Stay organized with collections  Save and categorize content based on your preferences. 

A regional external proxy Network Load Balancer is a proxy-based regional Layer 4 load balancer that lets you run and scale your TCP service traffic in a single region behind an external regional IP address. These load balancers distribute external TCP traffic from the internet to backends in the same region.

This guide contains instructions to set up a regional external proxy Network Load Balancer with a zonal network endpoint group (NEG) backend.

Before you begin, review the following documents:

  * [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp)
  * [Zonal NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts)



In this example, we'll use the load balancer to distribute TCP traffic across backend VMs in two zonal NEGs in Region A. For purposes of the example, the service is a set of [Apache](https://httpd.apache.org/) servers configured to respond on port `80`.

In this example, you configure the deployment shown in the following diagram.

[ ![Regional external proxy Network Load Balancer example configuration with zonal NEG backends.](https://docs.cloud.google.com/static/load-balancing/images/ext-reg-tcp-proxy-zonal.svg)](https://docs.cloud.google.com/static/load-balancing/images/ext-reg-tcp-proxy-zonal.svg) Regional external proxy Network Load Balancer example configuration with zonal NEG backends.

This is a regional load balancer. All load balancer components (backend instance group, backend service, target proxy, and forwarding rule) must be in the same region.

## Permissions

To follow this guide, you must be able to create instances and modify a network in a project. You must be either a project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)  
Add and remove firewall rules | [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`)  
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  
  
For more information, see the following guides:

  * [Roles and permissions](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Optional: Use BYOIP addresses

With bring your own IP (BYOIP), you can import your own public addresses to Google Cloud to use the addresses with Google Cloud resources. For example, if you import your own IPv4 addresses, you can assign one to the forwarding rule when you configure your load balancer. When you follow the instructions in this document to [configure the load balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-zonal#configure-the-load-balancer), provide the BYOIP address as the **IP address**.

For more information about using BYOIP, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Configure the network and subnets

You need a VPC network with two subnets, one for the load balancer's backends and the other for the load balancer's proxies. This is a regional load balancer. Traffic within the VPC network is routed to the load balancer if the traffic's source is in a subnet in the same region as the load balancer.

This example uses the following VPC network, region, and subnets:

  * **Network:** a [custom-mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`

  * **Subnet for backends:** a subnet named `backend-subnet` in Region A that uses `10.1.2.0/24` for its primary IP address range

  * **Subnet for proxies:** a subnet named `proxy-only-subnet` in Region A that uses `10.129.0.0/23` for its primary IP address range


**Note:** You can change the name of the network, the region, and the parameters for the subnets; however, subsequent steps in this guide use the network, region, and subnet parameters as named here.

### Create the network and subnet for backends

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. In the **Subnets** section, do the following:

     1. Set the **Subnet creation mode** to **Custom**.
     2. In the **New subnet** section, enter the following information: 
        * **Name** : `backend-subnet`
        * **Region** : `REGION_A`
        * **IP address range** : `10.1.2.0/24`
     3. Click **Done**.
  5. Click **Create**.




###  gcloud 

  1. To create the custom VPC network, use the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. To create a subnet in the `lb-network` network in the `REGION_A` region, use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create backend-subnet \
            --network=lb-network \
            --range=10.1.2.0/24 \
            --region=REGION_A
         




### Create the proxy-only subnet

A [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides a set of IP addresses that Google uses to run Envoy proxies on your behalf. The proxies terminate connections from the client and create new connections to the backends.

This proxy-only subnet is used by all Envoy-based load balancers in Region A of the `lb-network` VPC network.

**Important:** Don't try to assign addresses from the proxy-only subnet to your load balancer's forwarding rule or backends. You assign the forwarding rule's IP address and the backend instance IP addresses from a different subnet range (or ranges), not this one. Google Cloud reserves this subnet range for Google Cloud-managed proxies.

###  Console 

If you're using the Google Cloud console, you can wait and create the proxy-only subnet later on the **Load balancing** page.

If you want to create the proxy-only subnet now, use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the Shared VPC network: `lb-network`.

  3. Click **Add subnet**.

  4. For **Name** , enter `proxy-only-subnet`.

  5. For **Region** , select `REGION_A`.

  6. Set **Purpose** to **Regional Managed Proxy**.

  7. For **IP address range** , enter `10.129.0.0/23`.

  8. Click **Add**.




###  gcloud 

To create the proxy-only subnet, use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
    
    
    gcloud compute networks subnets create proxy-only-subnet \
        --purpose=REGIONAL_MANAGED_PROXY \
        --role=ACTIVE \
        --region=REGION_A \
        --network=lb-network \
        --range=10.129.0.0/23
    

## Create firewall rules

In this example, you create the following firewall rules:

  * `fw-allow-health-check`. An ingress rule, applicable to the Google Cloud instances being load balanced, that allows traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check` to identify the backend VMs to which it should apply.
  * `fw-allow-ssh`. An ingress rule that allows incoming SSH connectivity on TCP port `22` from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify only the IP ranges of the systems from which you initiate SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it should apply.
  * `fw-allow-proxy-only-subnet`. An ingress `allow` firewall rule for the proxy-only subnet that allows the load balancer to communicate with backend instances on TCP port `80`. This example uses the target tag `allow-proxy-only-subnet` to identify the backend VMs to which it should apply.




###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** , and then complete the following fields:

     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-health-check`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80` for the port number.
  3. Click **Create**.

  4. Click **Create firewall rule** a second time to create the rule to allow incoming SSH connections:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `22` for the port number.
  5. Click **Create**.

  6. Click **Create firewall rule** a third time to create the rule to allow incoming connections from the proxy-only subnet to the Google Cloud backends:

     * **Name** : `fw-allow-proxy-only-subnet`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-proxy-only-subnet`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.129.0.0/23`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80` for the port number.
  7. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-health-check` rule to allow the Google Cloud health checks to reach the backend instances on TCP port `80`:
         
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

**Note:** Regional external proxy Network Load Balancers support both the Premium and Standard Network Service Tiers. This procedure demonstrates the setup with Standard Tier.

###  Console 

  1. In the Google Cloud console, go to the **Reserve a static address** page.

[Go to Reserve a static address](https://console.cloud.google.com/networking/addresses/add)

  2. Choose a name for the new address.

  3. For **Network Service Tier** , select **Standard**.

  4. For **IP version** , select **IPv4**. IPv6 addresses are not supported.

  5. For **Type** , select **Regional**.

  6. For **Region** , select `REGION_A`.

  7. Leave the **Attached to** option set to **None**. After you create the load balancer, this IP address is attached to the load balancer's forwarding rule.

  8. Click **Reserve** to reserve the IP address.




###  gcloud 

  1. To reserve a static external IP address, use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create):
         
         gcloud compute addresses create ADDRESS_NAME  \
            --region=REGION_A \
            --network-tier=STANDARD
         

Replace `ADDRESS_NAME` with the name that you want to call this address.

  2. To view the result, use the [`gcloud compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe):
         
         gcloud compute addresses describe ADDRESS_NAME
         




## Set up the zonal NEG

Set up a zonal NEG with `GCE_VM_IP_PORT` type endpoints in Region A. First create the VMs, and then create a zonal NEG and add the VMs' network endpoints to the NEG.

### Create VMs

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set **Name** to `vm-a1`.

  4. For **Region** , select `REGION_A`.

  5. For **Zone** , select `ZONE_A`.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. Click **Choose** to change the image if necessary.

  7. Click **Advanced options**.

  8. Click **Networking** , and then configure the following fields:

     1. For **Network tags** , enter `allow-ssh`, `allow-health-check`, and `allow-proxy-only-subnet`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network`
        * **Subnet** : `backend-subnet`
  9. Click **Management**. Enter the following script into the **Startup script** field:
         
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

  11. Repeat the previous steps to create three more VMs. Use the following name and zone combinations:

     * Name: `vm-a2` | Zone: `ZONE_A`
     * Name: `vm-b1` | Zone: `ZONE_B`
     * Name: `vm-b2` | Zone: `ZONE_B`



###  gcloud 

To create the VMs, use the `gcloud compute instances create` command two times. Use the following combinations for `VM_NAME` and `ZONE`. The script contents are identical for both VMs:

  * `VM_NAME`: `vm-a1` and `ZONE`: `ZONE_A`
  * `VM_NAME`: `vm-a2` and `ZONE`: `ZONE_A`
  * `VM_NAME`: `vm-b1` and `ZONE`: `ZONE_B`
  * `VM_NAME`: `vm-b2` and `ZONE`: `ZONE_B`


    
    
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

**Create a zonal network endpoint group**

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)  


  2. Click **Create network endpoint group**.

  3. For **Name** , enter `zonal-neg-a`.

  4. For **Network endpoint group type** , select **Network endpoint group (Zonal)**.

  5. For **Network** , select `lb-network`.

  6. For **Subnet** , select `backend-subnet`.

  7. For **Zone** , select `ZONE_A`.

  8. For **Default port** , enter `80`.

  9. Click **Create**.

  10. Repeat all the steps in this section to create a second zonal NEG with the following changes in settings:

     * **Name** : `zonal-neg-b`
     * **Zone** : `ZONE_B`



**Add endpoints to the zonal NEGs**

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)  


  2. Click the name of the network endpoint group that you created in the previous step (for example, `zonal-neg-a`).

  3. On the **Network endpoint group details** page, in the **Network endpoints in this group** section, click **Add network endpoint**.

  4. Select a VM instance (for example, `vm-a1`).

  5. In the **Network interface** section, the VM name, zone, and subnet are displayed.

     1. For **IP address** , enter the IP address of the new network endpoint. To get the IP address, click **Check primary IP addresses and alias IP range in nic0**.
     2. For **Port type** , select **Default**. The endpoint uses the default port `80` for all endpoints in the network endpoint group. This is sufficient for our example because the Apache server is serving requests at port `80`.
     3. Click **Create**.
  6. Click **Add network endpoint**. Select the second VM instance, `vm-a2`, and repeat the previous steps to add its endpoints to `zonal-neg-a`.

  7. Repeat all the steps in this section to add endpoints from `vm-b1` and `vm-b2` to `zonal-neg-b`.




###  gcloud 

  1. Create a zonal NEG in the `ZONE_A` zone with `GCE_VM_IP_PORT` endpoints:
         
         gcloud compute network-endpoint-groups create zonal-neg-a \
             --network-endpoint-type=GCE_VM_IP_PORT \
             --zone=ZONE_A \
             --network=lb-network \
             --subnet=backend-subnet
         

You can either specify the `--default-port` while creating the NEG, or [specify a port number for each endpoint](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#adding-endpoints) as shown in the next step.

  2. Add endpoints to the zonal NEG:
         
         gcloud compute network-endpoint-groups update zonal-neg-a \
             --zone=ZONE_A \
             --add-endpoint='instance=vm-a1,port=80' \
             --add-endpoint='instance=vm-a2,port=80'
         

  3. Create a zonal NEG in the `ZONE_B` zone with `GCE_VM_IP_PORT` endpoints:
         
         gcloud compute network-endpoint-groups create zonal-neg-b \
             --network-endpoint-type=GCE_VM_IP_PORT \
             --zone=ZONE_B \
             --network=lb-network \
             --subnet=backend-subnet
         

You can either specify the `--default-port` while creating the NEG, or [specify a port number for each endpoint](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#adding-endpoints) as shown in the next step.

  4. Add endpoints to the zonal NEG:
         
         gcloud compute network-endpoint-groups update zonal-neg-b \
             --zone=ZONE_B \
             --add-endpoint='instance=vm-b1,port=80' \
             --add-endpoint='instance=vm-b2,port=80'
         




## Configure the load balancer

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Proxy load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  6. For **Global or single region deployment** , select **Best for regional workloads** and click **Next**.
  7. Click **Configure**.



#### Basic configuration

  1. For **Name** , enter `my-ext-tcp-lb`.
  2. For **Region** , select `REGION_A`.
  3. For **Network** , select `lb-network`.



#### Reserve a proxy-only subnet

**Note:** If you already created the proxy-only subnet, the **Reserve subnet** button isn't displayed. You can skip this section and continue with the steps in the **Configure the backends** section.

  1. Click **Reserve subnet**.
  2. For **Name** , enter `proxy-only-subnet`.
  3. For **IP address range** , enter `10.129.0.0/23`.
  4. Click **Add**.



#### Configure the backends

  1. Click **Backend configuration**.
  2. In the **Backend type** list, select **Zonal network endpoint group**.
  3. In the **Protocol** list, select **TCP**.
  4. Configure the health check: 
     1. In the **Health check** list, select **Create a health check**.
     2. In the **Name** field, enter `tcp-health-check`.
     3. In the **Protocol** list, select **TCP**.
     4. In the **Port** field, enter `80`.
     5. CLick **Create**.
  5. Configure the first backend: 
     1. For **New backend** , select zonal NEG `zonal-neg-a`.
     2. Retain the remaining default values, and then click **Done**.
  6. Configure the second backend: 
     1. Click **Add backend**.
     2. For **New backend** , select instance group `zonal-neg-b`.
     3. Retain the remaining default values, and then click **Done**.
  7. Retain the remaining default values, and then click **Save**.
  8. In the Google Cloud console, verify that there is a check mark next to **Backend configuration**. If not, double-check that you have completed all of the steps.



#### Configure the frontend

  1. Click **Frontend configuration**.
  2. For **Name** , enter `ext-tcp-forwarding-rule`.
  3. For **Network Service Tier** , select **Standard**.
  4. For **IP address** , select `ext-tcp-ip-address`.
  5. For **Port number** , enter `9090`. The forwarding rule only forwards packets with a matching destination port.
  6. For **Proxy protocol** , select **Off** because the PROXY protocol doesn't work with the Apache HTTP Server software. For more information, see [PROXY protocol](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp#proxy-protocol).
  7. Click **Done**.
  8. In the Google Cloud console, verify that there is a check mark next to **Frontend configuration**. If not, double-check that you have completed all the previous steps.



#### Review and finalize

  1. Click **Review and finalize**.
  2. Double-check your settings.
  3. Click **Create**.



###  gcloud 

  1. Create a regional health check for the backends:
         
         gcloud compute health-checks create tcp tcp-health-check \
             --region=REGION_A \
             --use-serving-port
         

  2. Create a backend service:
         
         gcloud compute backend-services create external-tcp-proxy-bs \
            --load-balancing-scheme=EXTERNAL_MANAGED \
            --protocol=TCP \
            --region=REGION_A \
            --health-checks=tcp-health-check \
            --health-checks-region=REGION_A
         

  3. Add the zonal NEG in the `ZONE_A` zone to the backend service:
         
         gcloud compute backend-services add-backend external-tcp-proxy-bs \
            --network-endpoint-group=zonal-neg-a \
            --network-endpoint-group-zone=ZONE_A \
            --balancing-mode=CONNECTION \
            --max-connections-per-endpoint=50 \
            --region=REGION_A
         

  4. Add the zonal NEG in the `ZONE_B` zone to the backend service:
         
         gcloud compute backend-services add-backend external-tcp-proxy-bs \
            --network-endpoint-group=zonal-neg-b \
            --network-endpoint-group-zone=ZONE_B \
            --balancing-mode=CONNECTION \
            --max-connections-per-endpoint=50 \
            --region=REGION_A
         

  5. Create the target TCP proxy:
         
         gcloud compute target-tcp-proxies create ext-tcp-target-proxy \
            --backend-service=external-tcp-proxy-bs \
            --region=REGION_A
         

  6. Create the forwarding rule. For `--ports`, specify a single port number from 1-65535. This example uses port `9090`. The forwarding rule only forwards packets with a matching destination port.
         
         gcloud compute forwarding-rules create ext-tcp-forwarding-rule \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network=lb-network \
           --network-tier=STANDARD \
           --address=ext-tcp-ip-address \
           --ports=9090 \
           --region=REGION_A \
           --target-tcp-proxy=ext-tcp-target-proxy \
           --target-tcp-proxy-region=REGION_A
         




## Test your load balancer

**Note:** It might take a few minutes for the load balancer configuration to propagate after you first deploy it.

Now that you have configured your load balancer, you can test sending traffic to the load balancer's IP address.

  1. Get the load balancer's IP address.

To get the IPv4 address, run the following command:
         
         gcloud compute addresses describe ADDRESS_NAME
         

  2. Send traffic to your load balancer by running the following command. Replace `LB_IP_ADDRESS` with your load balancer's IPv4 address.
         
         curl -m1 LB_IP_ADDRESS:9090
         




## What's next

  * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)
  * [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp).
  * [Proxy Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring).
  * [Add a Private Service Connect](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#add-neg-ext-tcp-proxy-lb).
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
