---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs/
title: Set up a regional internal proxy Network Load Balancer with VM instance group backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:04:42.327699+00:00
---

# Set up a regional internal proxy Network Load Balancer with VM instance group backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional internal proxy Network Load Balancer with VM instance group backends Stay organized with collections  Save and categorize content based on your preferences. 

The regional internal proxy Network Load Balancer is a proxy-based regional Layer 4 load balancer that lets you run and scale your TCP service traffic behind an internal IP address that is accessible only to clients in the same VPC network or clients connected to your VPC network.

Before you start, read the [Regional internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).

This guide contains instructions for setting up a regional internal proxy Network Load Balancer with a managed instance group (MIG) backend. For this example, you configure the following deployment:

[ ![Regional internal proxy Network Load Balancer example configuration with instance group backends.](https://docs.cloud.google.com/static/load-balancing/images/int-tcp-proxy-migs.svg)](https://docs.cloud.google.com/static/load-balancing/images/int-tcp-proxy-migs.svg) Regional internal proxy Network Load Balancer example configuration with instance group backends

In this example, we'll use the load balancer to distribute TCP traffic across backend VMs in two zonal managed instance groups in the `REGION_A` region. For purposes of the example, the service is a set of [Apache](https://httpd.apache.org/) servers configured to respond on port `110`. Many browsers don't allow port `110`, so the testing section uses `curl`.

The regional internal proxy Network Load Balancer is a regional load balancer. All load balancer components must be in the same region as the load balancer.

**SNI-based routing** : This page also shows you an alternative deployment architecture that you can use to configure SNI-based routing. For SNI-based routing, you use TLS routes to define how traffic is distributed. For details, see Create a load balancer with TLS routes ([Preview](https://cloud.google.com/products/#product-launch-stages)).

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




To demonstrate [global access](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#client-access), this example also creates a second test client VM in a different region (REGION_B) and a subnet with primary IP address range `10.3.4.0/24`.

**Note:** You can change the name of the network, the region, and the parameters for the subnets; however, subsequent steps in this guide use the network, region, and subnet parameters as outlined here.

### Create the network and subnets

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. In the **Subnets** section, set the **Subnet creation mode** to **Custom**.

  5. Create a subnet for the load balancer's backends. In the **New subnet** section, enter the following information:

     * **Name** : `backend-subnet`
     * **Region** : `REGION_A`
     * **IP address range** : `10.1.2.0/24`
  6. Click **Done**.

  7. Click **Add subnet**.

  8. Create a subnet to demonstrate [global access](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#client-access). In the **New subnet** section, enter the following information:

     * **Name** : `test-global-access-subnet`
     * **Region** : `REGION_B`
     * **IP address range** : `10.3.4.0/24`
  9. Click **Done**.

  10. Click **Create**.




###  gcloud 

  1. Create the custom VPC network with the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. Create a subnet in the `lb-network` network in the `REGION_A` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create backend-subnet \
            --network=lb-network \
            --range=10.1.2.0/24 \
            --region=REGION_A
         

Replace REGION_A with the name of the target Google Cloud region.

  3. Create a subnet in the `lb-network` network in the `REGION_B` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create test-global-access-subnet \
            --network=lb-network \
            --range=10.3.4.0/24 \
            --region=REGION_B
         

Replace REGION_B with the name of the Google Cloud region where you want to create the second subnet to test global access.




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
  4. For **Name** , enter `proxy-only-subnet`.
  5. For **Region** , select `REGION_A`.
  6. Set **Purpose** to **Regional Managed Proxy**.
  7. For **IP address range** , enter `10.129.0.0/23`.
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

This example requires the following firewall rules:

  * **`fw-allow-ssh`.** An ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port `22` from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify just the IP ranges of the system from which you initiate SSH sessions. This example uses the target tag `allow-ssh`.

  * **`fw-allow-health-check`.** An ingress rule, applicable to the instances being load balanced, that allows all TCP traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check`.

  * **`fw-allow-proxy-only-subnet`.** An ingress rule that allows connections from the proxy-only subnet to reach the backends.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

The [target tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#targets_for_firewall_rules) define the backend instances. Without the target tags, the firewall rules apply to all of your backend instances in the VPC network. When you create the backend VMs, make sure to include the specified target tags, as shown in [Creating a managed instance group](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#creating_a_managed_instance_group).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.   
[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)
  2. Click **Create firewall rule** to create the rule to allow incoming SSH connections: 
     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `22` for the port number.
  3. Click **Create**.
  4. Click **Create firewall rule** a second time to create the rule to allow Google Cloud health checks: 
     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-health-check`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80` for the port number.   
As a best practice, limit this rule to just the protocols and ports that match those used by your health check. If you use `tcp:80` for the protocol and port, Google Cloud can use HTTP on port `80` to contact your VMs, but it cannot use HTTPS on port `443` to contact them.
  5. Click **Create**.
  6. Click **Create firewall rule** a third time to create the rule to allow the load balancer's proxy servers to connect the backends: 
     * **Name** : `fw-allow-proxy-only-subnet`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-proxy-only-subnet`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.129.0.0/23`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80` for the port numbers.
  7. Click **Create**.



###  gcloud 

  1. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
            --network=lb-network \
            --action=allow \
            --direction=ingress \
            --target-tags=allow-ssh \
            --rules=tcp:22
         

  2. Create the `fw-allow-health-check` rule to allow Google Cloud health checks. This example allows all TCP traffic from health check probers; however, you can configure a narrower set of ports to meet your needs.
         
         gcloud compute firewall-rules create fw-allow-health-check \
            --network=lb-network \
            --action=allow \
            --direction=ingress \
            --source-ranges=35.191.0.0/16 \
            --target-tags=allow-health-check \
            --rules=tcp:80
         

  3. Create the `fw-allow-proxy-only-subnet` rule to allow the region's Envoy proxies to connect to your backends. Set `--source-ranges` to the allocated ranges of your proxy-only subnet, in this example, `10.129.0.0/23`.
         
         gcloud compute firewall-rules create fw-allow-proxy-only-subnet \
            --network=lb-network \
            --action=allow \
            --direction=ingress \
            --source-ranges=10.129.0.0/23 \
            --target-tags=allow-proxy-only-subnet \
            --rules=tcp:80
         




## Reserve the load balancer's IP address

To reserve a static internal IP address for your load balancer, see [Reserve a new static internal IPv4 or IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip).

**Note:** Ensure that you use the subnet name that you specified when you created the subnet.

## Create a managed instance group

This section shows you how to create two managed instance group (MIG) backends in the `REGION_A` region for the load balancer. The MIG provides VM instances running the backend Apache servers for this example regional internal proxy Network Load Balancer. Typically, a regional internal proxy Network Load Balancer isn't used for HTTP traffic, but Apache software is commonly used for testing.

###  Console 

  1. Create an instance template. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

     1. Click **Create instance template**.
     2. For **Name** , enter `int-tcp-proxy-backend-template`.
     3. Ensure that the **Boot disk** is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     4. Click **Advanced options**.
     5. Click **Networking** and configure the following fields: 
        1. For **Network tags** , enter `allow-ssh`, `allow-health-check` and `allow-proxy-only-subnet`.
        2. For **Network interfaces** , select the following: 
           * **Network** : `lb-network`
           * **Subnet** : `backend-subnet`
     6. Click **Management**. Enter the following script into the **Startup script** field.
            
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
            

     7. Click **Create**.

  2. Create a managed instance group. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     1. Click **Create instance group**.
     2. Select **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
     3. For **Name** , enter `mig-a`.
     4. Under **Location** , select **Single zone**.
     5. For **Region** , select `REGION_A`.
     6. For **Zone** , select `ZONE_A1`.
     7. Under **Instance template** , select `int-tcp-proxy-backend-template`.
     8. Specify the number of instances that you want to create in the group.

For this example, specify the following options under **Autoscaling** :

        * For **Autoscaling mode** , select `Off:do not autoscale`.
        * For **Maximum number of instances** , enter `2`.
     9. For **Port mapping** , click **Add port**.

        * For **Port name** , enter `tcp80`.
        * For **Port number** , enter `80`.
     10. Click **Create**.

  3. Repeat Step 2 to create a second managed instance group with the following settings:

     1. **Name** : `mig-c`
     2. **Zone** : `ZONE_A2` Keep all other settings the same.



###  gcloud 

The `gcloud` instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.

  1. Create a VM instance template with HTTP server with the [`gcloud compute instance-templates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) command.
         
         gcloud compute instance-templates create int-tcp-proxy-backend-template \
            --region=REGION_A \
            --network=lb-network \
            --subnet=backend-subnet \
            --tags=allow-ssh,allow-health-check,allow-proxy-only-subnet \
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
         

  2. Create a managed instance group in the `ZONE_A1` zone.
         
         gcloud compute instance-groups managed create mig-a \
            --zone=ZONE_A1 \
            --size=2 \
            --template=int-tcp-proxy-backend-template
         

Replace ZONE_A1 with the name of the zone in the target Google Cloud region.

  3. Create a managed instance group in the `ZONE_A2` zone.
         
         gcloud compute instance-groups managed create mig-c \
            --zone=ZONE_A2 \
            --size=2 \
            --template=int-tcp-proxy-backend-template
         

Replace ZONE_A2 with the name of another zone in the target Google Cloud region.




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
  2. For **Backend type** , select **Instance group**.
  3. For **Protocol** , select **TCP**.
  4. For **Named port** , enter `tcp80`.
  5. In the **Health check** list, click **Create a health check** , and then enter the following information: 
     * **Name** : `tcp-health-check`
     * **Protocol** : **TCP**
     * **Port** : `80`
  6. Click **Create**.
  7. Configure the first backend: 
     1. Under **New backend** , select instance group `mig-a`.
     2. For **Port numbers** , enter `80`.
     3. Retain the remaining default values and click **Done**.
  8. Configure the second backend: 
     1. Click **Add backend**.
     2. Under **New backend** , select instance group `mig-c`.
     3. For **Port numbers** , enter `80`.
     4. Retain the remaining default values and click **Done**.
  9. In the Google Cloud console, verify that there is a check mark next to **Backend configuration**. If not, double-check that you have completed all of the steps.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. For **Name** , enter `int-tcp-forwarding-rule`.
  3. For **Subnetwork** , select **backend-subnet**.
  4. For **IP address** , select the IP address reserved previously: LB_IP_ADDRESS
  5. For **Port number** , enter `110`. The forwarding rule only forwards packets with a matching destination port.
  6. In this example, don't enable the **Proxy Protocol** because it doesn't work with the Apache HTTP Server software. For more information, see Proxy protocol.
  7. Click **Done**.
  8. In the Google Cloud console, verify that there is a check mark next to **Frontend configuration**. If not, double-check that you have completed all the previous steps.



#### Review and finalize

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.



###  gcloud 

  1. Create a regional health check.
         
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
         

  3. Add instance groups to your backend service.
         
         gcloud compute backend-services add-backend internal-tcp-proxy-bs \
            --region=REGION_A \
            --instance-group=mig-a \
            --instance-group-zone=ZONE_A1 \
            --balancing-mode=UTILIZATION \
            --max-utilization=0.8
         
         
         gcloud compute backend-services add-backend internal-tcp-proxy-bs \
            --region=REGION_A \
            --instance-group=mig-c \
            --instance-group-zone=ZONE_A2 \
            --balancing-mode=UTILIZATION \
            --max-utilization=0.8
         

  4. Create an internal target TCP proxy.
         
         gcloud compute target-tcp-proxies create int-tcp-target-proxy \
            --backend-service=internal-tcp-proxy-bs \
            --proxy-header=NONE \
            --region=REGION_A
         

If you want to turn on the proxy header, set it to `PROXY_V1` instead of `NONE`. In this example, don't enable Proxy protocol because it doesn't work with the Apache HTTP Server software. For more information, see Proxy protocol.

  5. Create the forwarding rule. For `--ports`, specify a single port number from 1-65535. This example uses port `110`. The forwarding rule only forwards packets with a matching destination port.
         
         gcloud compute forwarding-rules create int-tcp-forwarding-rule \
            --load-balancing-scheme=INTERNAL_MANAGED \
            --network=lb-network \
            --subnet=backend-subnet \
            --region=REGION_A \
            --target-tcp-proxy=int-tcp-target-proxy \
            --target-tcp-proxy-region=REGION_A \
            --address=int-tcp-ip-address \
            --ports=110
         




### Test your load balancer

To test the load balancer, create a client VM in the same region as the load balancer. Then send traffic from the client to the load balancer.

#### Create a client VM

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
    

#### Send traffic to the load balancer

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
            
            curl IP_ADDRESS:110
            




## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Create a load balancer with TLS routes

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section shows you how to create a load balancer that can use SNI-based routing. SNI-based routing lets your proxy Network Load Balancers route traffic to specific backend services based on the Server Name Indication (SNI) hostname provided during the TLS handshake.

To create this load balancer we use the same networks, subnets, and firewall rules created previously on this page. You configure the deployment shown in the following diagram:

[ ![Regional internal proxy Network Load Balancer configuration with TLS routes.](https://docs.cloud.google.com/static/load-balancing/images/reg-int-tcp-proxy-tls-routes.svg)](https://docs.cloud.google.com/static/load-balancing/images/reg-int-tcp-proxy-tls-routes.svg) Regional internal proxy Network Load Balancer configuration with TLS routes.

### Create a managed instance group backend

This section shows you how to create a managed instance group (MIG) backends for the load balancer. The MIG provides VM instances running the backend servers for this example.

The Google Cloud CLI instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

  1. Create an instance template with an "echo" HTTPS service that is exposed on port 443.
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
         --region=REGION_A \
         --network=NETWORK \
         --subnet=SUBNET_A \
         --stack-type=IPv4_ONLY \
         --tags=allow-ssh,allow-health-check,allow-proxy-only-subnet \
         --image-family=debian-12 \
         --image-project=debian-cloud \
         --metadata=startup-script='#! /bin/bash
         sudo sed -i "s/^#DNS=.*/DNS=8.8.8.8 8.8.4.4/" /etc/systemd/resolved.conf
         sudo systemctl restart systemd-resolved
         sudo rm -rf /var/lib/apt/lists/*
         sudo apt-get -y clean
         sudo apt-get -y update
         sudo apt-get -y install ca-certificates curl gnupg software-properties-common
         sudo curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
         sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
         sudo apt-get -y update
         sudo apt-get -y install docker-ce
         sudo which docker
         echo "{ \"registry-mirrors\": [\"https://mirror.gcr.io\"] }" | sudo tee -a /etc/docker/daemon.json
         sudo service docker restart
         sudo docker run -e HTTPS_PORT=9999 -p 443:9999 --rm -dt mendhak/http-https-echo:22'
         

Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: a name for the instance template.
     * `REGION_A`: the region for the instance template.
     * `NETWORK`: the name of the network.
     * `SUBNET_A`: the name of the subnetwork.
  2. Create a managed instance group based on the instance template:
         
         gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
           --zone=ZONE_A \
           --size=2 \
           --template=INSTANCE_TEMPLATE_NAME
         

Replace `ZONE_A` with the zone for the instance group.

  3. Set the name of the serving port for the managed instance group:
         
         gcloud compute instance-groups managed set-named-ports INSTANCE_GROUP_NAME \
           --named-ports=PORT_NAME:PORT_NUMBER \
           --zone=ZONE_A
         

Replace the following:

     * `PORT_NAME`: a name for the serving port—for example, `tcp443`.
     * `PORT_NUMBER`: a port number for the serving port—for example, `443`.



### Configure the firewall

Configure a firewall rule to allow traffic from the load balancer and from the health check probes to the backend instances.
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME \
        --network=NETWORK \
        --action=allow \
        --direction=ingress \
        --source-ranges=35.191.0.0/16 \
        --target-tags=allow-health-check \
        --rules=tcp:443
    

Replace `FIREWALL_RULE_NAME` with a name for the firewall rule.

### Configure the load balancer

  1. Create an HTTPS health check:
         
         gcloud compute health-checks create http HTTPS_HEALTH_CHECK_NAME \
             --region=REGION_A \
             --port=HC_PORT
         

Replace the following:

     * `HTTPS_HEALTH_CHECK_NAME`: a name for the health check.
     * `HC_PORT`: the port for the health check—for example, `443`.
     * `REGION_A`: the region for the health check.
  2. Create a backend service:
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --protocol=TCP \
             --port-name=PORT_NAME \
             --region=REGION_A \
             --health-checks=tcp-health-check \
             --health-checks-region=REGION_A
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: a name for the backend service.
     * `PORT_NAME`: the port name for the backend service. Use the same named port configured on the instance group—for example, `tcp443`.
     * `HTTPS_HEALTH_CHECK_NAME`: the name of the HTTPS health check.
  3. Add the backend instance group to your backend service:
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.8
             --instance-group=INSTANCE_GROUP_NAME \
             --instance-group-zone=ZONE_A \
             --region=REGION_A
           

Replace the following:

     * `INSTANCE_GROUP_NAME`: the name of the backend instance group.
     * `ZONE_A`: the zone of the instance group.
  4. Create a target TCP proxy.
         
         gcloud beta compute target-tcp-proxies create TARGET_TCP_PROXY_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --proxy-header=NONE \
             --region=REGION_A
         

Replace `TARGET_TCP_PROXY_NAME` with the name of the target TCP proxy.

  5. Create a TLS route specification and save it to a YAML file.
         
         cat <<EOF | tee YAML_FILE_NAME
         name: TLS_ROUTE_NAME
         targetProxies:
         - projects/PROJECT_NUMBER/locations/REGION_A/targetTcpProxies/TARGET_TCP_PROXY
         rules:
         - matches:
           - sniHost:
             - example.com
           action:
           destinations:
           - serviceName: projects/PROJECT_NUMBER/locations/REGION_A/backendServices/BACKEND_SERVICE_NAME
         EOF
         

Replace the following:

     * `YAML_FILE_NAME`: a name for the YAML file—for example, `tls-route.yaml`.
     * `TLS_ROUTE_NAME`: a name for the TLS route.
     * `PROJECT_NUMBER`: the project number.
  6. Use the YAML specification file to create the TLS route resource.
         
         gcloud network-services tls-routes import TLS_ROUTE_NAME \
           --source=YAML_FILE_NAME \
           --location=REGION_A
         

  7. Create the forwarding rule.
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
           --load-balancing-scheme=INTERNAL_MANAGED \
           --network=NETWORK \
           --subnet=SUBNET_A \
           --region=REGION_A \
           --target-tcp-proxy=TARGET_TCP_PROXY_NAME \
           --target-tcp-proxy-region=REGION_A \
           --address=IP_ADDRESS \
           --ports=PORT_NUMBER
         

Replace the following:

     * `FORWARDING_RULE_NAME`: a name for the forwarding rule.
     * `NETWORK`: the name of the network.
     * `SUBNET_A`: the name of the subnetwork in the same region as the load balancer.
     * `IP_ADDRESS`: the IP address of the load balancer.
     * `PORT_NUMBER`: the port used by the forwarding rule—for example, `443`.



### Test the load balancer

**Note:** It might take a few minutes for the load balancer configuration to propagate after you first deploy it.

Now that you have configured your load balancer, you can test sending traffic to the load balancer's IP address.

  1. Verify that you can access the HTTPS service through the load balancer.
         
         curl https://example.com --resolve example.com:443:IP_ADDRESS -k
         

You will see the command returning a response from one of the VMs in the managed instance group with the following printed to the console.
         
         "path": "/",
         "headers": {
           "host": "example.com",
           "user-agent": "curl/7.81.0",
           "accept": "*/*"
         },
         "method": "GET",
         "body": "",
         "fresh": false,
         "hostname": "example.com",
         "ip": "::ffff:10.142.0.2",
         "ips": [],
         "protocol": "https",
         "query": {},
         "subdomains": [],
         "xhr": false,
         "os": {
           "hostname": "0cd3aec9b351"
         },
         "connection": {
           "servername": "example.com"
         }
         

You can further verify that if you provide a different SNI hostname that doesn't match a TLS route, or if you don't provide an SNI hostname at all, the request is dropped.

     * Run a test with an SNI hostname that doesn't match example.com, to ensure that the connection is rejected.
    
    curl https://unknown.com --resolve unknown.com:443:IP_ADDRESS -k
    

     * Run a test with a plain text connection without TLS, to ensure that the connection is rejected.
    
    curl example.com:443 --resolve example.com:443:IP_ADDRESS -k
    

These commands return the following error.
    
    curl: (35) OpenSSL SSL_connect: Connection reset by peer in connection
    

You'll see the `connection_refused` error code in the [`proxyStatus` logs](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#proxy-status) when the load balancer refuses such invalid connections.




### Enable global access

You can enable [global access](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#client-access) for your load balancer to make it accessible to clients in all regions. The backends of your example load balancer must still be located in one region (`REGION_A`).

[ ![Regional internal proxy Network Load Balancer with global access](https://docs.cloud.google.com/static/load-balancing/images/proxy-ilb-global-access-arch.svg)](https://docs.cloud.google.com/static/load-balancing/images/proxy-ilb-global-access-arch.svg) Regional internal proxy Network Load Balancer with global access (click to enlarge)

You can't modify an existing regional forwarding rule to enable global access. You must create a new forwarding rule for this purpose. Additionally, after a forwarding rule has been created with global access enabled, it cannot be modified. To disable global access, you must create a new regional access forwarding rule and delete the previous global access forwarding rule.

To configure global access, make the following configuration changes.

###  Console 

Create a new forwarding rule for the load balancer:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. In the **Name** column, click your load balancer.

  3. Click **Frontend configuration**.

  4. Click **Add frontend IP and port**.

  5. Enter the name and subnet details for the new forwarding rule.

  6. For **Subnetwork** , select **backend-subnet**.

  7. For **IP address** , you can either select the same IP address as an existing forwarding rule, reserve a new IP address, or use an ephemeral IP address. Sharing the same IP address across multiple forwarding rules is only possible if you set the IP address `--purpose` flag to `SHARED_LOADBALANCER_VIP` while creating the IP address.

  8. For **Port number** , enter `110`.

  9. For **Global access** , select **Enable**.

  10. Click **Done**.

  11. Click **Update**.




###  gcloud 

  1. Create a new forwarding rule for the load balancer with the `--allow-global-access` flag.
         
         gcloud compute forwarding-rules create int-tcp-forwarding-rule-global-access \
            --load-balancing-scheme=INTERNAL_MANAGED \
            --network=lb-network \
            --subnet=backend-subnet \
            --region=REGION_A \
            --target-tcp-proxy=int-tcp-target-proxy \
            --target-tcp-proxy-region=REGION_A \
            --address=int-tcp-ip-address \
            --ports=110 \
            --allow-global-access
         

  2. You can use the `gcloud compute forwarding-rules describe` command to determine whether a forwarding rule has global access enabled. For example:
         
         gcloud compute forwarding-rules describe int-tcp-forwarding-rule-global-access \
            --region=REGION_A \
            --format="get(name,region,allowGlobalAccess)"
         

When global access is enabled, the word `True` appears in the output after the name and region of the forwarding rule.




#### Create a client VM to test global access

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set **Name** to `test-global-access-vm`.

  4. Set **Zone** to `ZONE_B1`.

  5. Click **Advanced options**.

  6. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network`
        * **Subnet** : `test-global-access-subnet`
  7. Click **Create**.




###  gcloud 

Create a client VM in the `ZONE_B1` zone.
    
    
    gcloud compute instances create test-global-access-vm \
        --zone=ZONE_B1 \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=test-global-access-subnet
    

Replace ZONE_B1 with the name of the zone in the REGION_B region.

#### Connect to the client VM and test connectivity

  1. Use `ssh` to connect to the client instance:
         
         gcloud compute ssh test-global-access-vm \
             --zone=ZONE_B1
         

  2. Use the [`gcloud compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to get the load balancer's IP address:
         
         gcloud compute addresses describe int-tcp-ip-address \
             --region=REGION_A
         

Make a note of the IP address.

  3. Send traffic to the load balancer; replace IP_ADDRESS with the IP address of the load balancer:
         
         curl IP_ADDRESS:110
         




### PROXY protocol for retaining client connection information

The proxy Network Load Balancer ends TCP connections from the client and creates new connections to the instances. By default, the original client IP and port information is not preserved.

To preserve and send the original connection information to your instances, enable [PROXY protocol version 1](http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt). This protocol sends an additional header that contains the source IP address, destination IP address, and port numbers to the instance as a part of the request.

Make sure that the proxy Network Load Balancer's backend instances are running servers that support PROXY protocol headers. If the servers are not configured to support PROXY protocol headers, the backend instances return empty responses.

If you set the PROXY protocol for user traffic, you can also set it for your health checks. If you are checking health and serving content on the same port, set the health check's `--proxy-header` to match your load balancer setting.

The PROXY protocol header is typically a single line of user-readable text in the following format:
    
    
    PROXY TCP4 <client IP> <load balancing IP> <source port> <dest port>\r\n
    

The following example shows a PROXY protocol:
    
    
    PROXY TCP4 192.0.2.1 198.51.100.1 15221 110\r\n

In the preceding example, the client IP is `192.0.2.1`, the load balancing IP is `198.51.100.1`, the client port is `15221`, and the destination port is `110`.

When the client IP is not known, the load balancer generates a PROXY protocol header in the following format:
    
    
    PROXY UNKNOWN\r\n
    

#### Update PROXY protocol header for target proxy

You cannot update the PROXY protocol header in the existing target proxy. You have to create a new target proxy with the required setting for the PROXY protocol header. Use these steps to create a new frontend with the required settings:

### Console

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of the load balancer you want to edit.
  3. Click edit**Edit** for your load balancer.
  4. Click **Frontend configuration**.
  5. Delete the old frontend IP and port.
  6. Click **Add frontend IP and port**. 
     1. For **Name** , enter `int-tcp-forwarding-rule`.
     2. For **Subnetwork** , select **backend-subnet**.
     3. For **IP address** , select the IP address reserved previously: LB_IP_ADDRESS
     4. For **Port number** , enter `110`. The forwarding rule only forwards packets with a matching destination port.
     5. Change the value of the **Proxy protocol** field to **On**.
     6. Click **Done**.
  7. Click **Update** to save your changes.



### gcloud

  1. In the following command, edit the `--proxy-header` field and set it to either `NONE` or `PROXY_V1` depending on your requirement.
         
         gcloud compute target-tcp-proxies create TARGET_PROXY_NAME \
                --backend-service=BACKEND_SERVICE \
                --proxy-header=[NONE | PROXY_V1] \
                --region=REGION
            

  2. Delete the existing forwarding rule.
         
         gcloud compute forwarding-rules delete int-tcp-forwarding-rule \
                --region=REGION
            

  3. Create a new forwarding rule and associate it with the target proxy.
         
         gcloud compute forwarding-rules create int-tcp-forwarding-rule \
                --load-balancing-scheme=INTERNAL_MANAGED \
                --network=lb-network \
                --subnet=backend-subnet \
                --region=REGION \
                --target-tcp-proxy=TARGET_PROXY_NAME \
                --target-tcp-proxy-region=REGION \
                --address=LB_IP_ADDRESS \
                --ports=110
            




### Enable session affinity

The example configuration creates a backend service without session affinity.

These procedures show you how to update a backend service for the example regional internal proxy Network Load Balancer so that the backend service uses client IP affinity or generated cookie affinity.

When client IP affinity is enabled, the load balancer directs a particular client's requests to the same backend VM based on a hash created from the client's IP address and the load balancer's IP address (the internal IP address of an internal forwarding rule).

###  Console

To enable client IP session affinity:

  1. In the Google Cloud console, go to the **Load balancing** page.   
[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)
  2. Click **Backends**.
  3. Click **internal-tcp-proxy-bs** (the name of the backend service you created for this example) and click **Edit**.
  4. On the **Backend service details** page, click **Advanced configuration**.
  5. Under **Session affinity** , select **Client IP** from the menu.
  6. Click **Update**.



###  gcloud 

Use the following Google Cloud CLI command to update the `internal-tcp-proxy-bs` backend service, specifying client IP session affinity:
    
    
    gcloud compute backend-services update internal-tcp-proxy-bs \
        --region=REGION_A \
        --session-affinity=CLIENT_IP
    

### Enable connection draining

You can enable connection draining on backend services to ensure minimal interruption to your users when an instance that is serving traffic is terminated, removed manually, or removed by an autoscaler. To learn more about connection draining, read the [Enabling connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining) documentation.

## What's next

  * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)
  * [Regional internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
  * [Using monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring)
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
