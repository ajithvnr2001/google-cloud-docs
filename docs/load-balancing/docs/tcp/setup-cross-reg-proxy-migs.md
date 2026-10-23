---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs/
title: Set up a cross-region internal proxy Network Load Balancer with VM instance group backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:40.218262+00:00
---

# Set up a cross-region internal proxy Network Load Balancer with VM instance group backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a cross-region internal proxy Network Load Balancer with VM instance group backends Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for configuring a cross-region internal proxy Network Load Balancer with Compute Engine VM instance group backends.

Before following this guide, familiarize yourself with the [Internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).

For this example, you configure the deployment shown in the following diagram.

[ ![Cross-region internal proxy Network Load Balancer high availability deployment.](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-proxy-vm.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-proxy-vm.svg) Cross-region internal proxy Network Load Balancer high availability deployment (click to enlarge).

This creates a cross-region internal proxy Network Load Balancer in a VPC network, with one backend service and two backend managed instance groups (MIGs) in region `REGION_A` and `REGION_B` regions.

**SNI-based routing** : This page also shows you an alternative deployment architecture that you can use to configure SNI-based routing. For SNI-based routing, you use TLS routes to define how traffic is distributed. For details, see Create a load balancer with TLS routes ([Preview](https://cloud.google.com/products/#product-launch-stages)).

Cross-region internal proxy Network Load Balancers require the following resources:

  1. A VPC network with the following subnets:

     * Subnet `SUBNET_A` and a proxy-only subnet in `REGION_A`.
     * Subnet `SUBNET_B` and a proxy-only subnet in `REGION_B`.

You must create [proxy-only subnets](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) in each region of a VPC network where you use cross-region internal proxy Network Load Balancers. The region's proxy-only subnet is shared among all cross-region internal proxy Network Load Balancers in the region. Source addresses of packets sent from the load balancer to your service's backends are allocated from the proxy-only subnet. In this example, the proxy-only subnet for the region `REGION_B` has a primary IP address range of `10.129.0.0/23`, and for `REGION_A`, has a primary IP address range of `10.130.0.0/23`, which is the recommended subnet size.

  2. High availability setup has managed instance group backends for Compute Engine VM deployments in `REGION_A` and `REGION_B` regions. If backends in one region happen to be down, traffic fails over to the other region.

  3. A global backend service that monitors the usage and health of backends.

  4. A global target TCP proxy, which receives a request from the user and forwards it to the backend service.

  5. Global forwarding rules, which have the regional internal IP address of your load balancer and can forward each incoming request to the target proxy.

The internal IP address associated with the forwarding rule can come from a subnet in the same network and region as the backends. Note the following conditions:

     * The IP address can (but does not need to) come from the same subnet as the backend instance groups.
     * The IP address must not come from a reserved proxy-only subnet that has its `--purpose` flag set to `GLOBAL_MANAGED_PROXY`. If you try to use the proxy-only subnet, forwarding rule creation fails.
     * If you want to use the same internal IP address with multiple forwarding rules, set the IP address `--purpose` flag to `SHARED_LOADBALANCER_VIP`.



## Permissions

To follow this guide, you must be able to create instances and modify a network in a project. You must be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/understanding-roles#basic), or you must have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Add and remove firewall rules | [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1)  
  
For more information, see the following guides:

  * [Roles and permissions](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Configure the network and subnets

Within the VPC network, configure a subnet in each region where your backends are configured. In addition, configure a `proxy-only-subnet` in each region that you want to configure the load balancer.

This example uses the following VPC network, region, and subnets:

  * **Network**. The network is a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `NETWORK`.

  * **Subnets for backends**.

    * A subnet named `SUBNET_A` in the `REGION_A` region uses `10.1.2.0/24` for its primary IP range.
    * A subnet named `SUBNET_B` in the `REGION_B` region uses `10.1.3.0/24` for its primary IP range.
  * **Subnets for proxies**.

    * A subnet named `PROXY_SN_A` in the `REGION_A` region uses `10.129.0.0/23` for its primary IP range.
    * A subnet named `PROXY_SN_B` in the `REGION_B` region uses `10.130.0.0/23` for its primary IP range.



Cross-region load balancers can be accessed from any region within the VPC. So clients from any region can globally access your load balancer backends.

**Note:** Subsequent steps in this guide use the network, region, and subnet parameters as outlined here.

### Configure the backend subnets

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Provide a **Name** for the network.

  4. In the **Subnets** section, set the **Subnet creation mode** to **Custom**.

  5. Create a subnet for the load balancer's backends. In the **New subnet** section, enter the following information:

     * Provide a **Name** for the subnet.
     * Select a **Region** : REGION_A
     * Enter an **IP address range** : `10.1.2.0/24`
  6. Click **Done**.

  7. Click **Add subnet**.

  8. Create a subnet for the load balancer's backends. In the **New subnet** section, enter the following information:

     * Provide a **Name** for the subnet.
     * Select a **Region** : REGION_B
     * Enter an **IP address range** : `10.1.3.0/24`
  9. Click **Done**.

  10. Click **Create**.




###  gcloud 

  1. Create the custom VPC network with the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create NETWORK \
             --subnet-mode=custom
         

  2. Create a subnet in the `NETWORK` network in the `REGION_A` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create SUBNET_A \
             --network=NETWORK \
             --range=10.1.2.0/24 \
             --region=REGION_A
         

  3. Create a subnet in the `NETWORK` network in the `REGION_B` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create SUBNET_B \
             --network=NETWORK \
             --range=10.1.3.0/24 \
             --region=REGION_B
         




###  Terraform 

To create the VPC network, use the [`google_compute_network` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).
    
    
    resource "google_compute_network" "default" {
      auto_create_subnetworks = false
      name                    = "lb-network-crs-reg"
      provider                = google-beta
    }

To create the VPC subnets in the `lb-network-crs-reg` network, use the [`google_compute_subnetwork` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork).
    
    
    resource "google_compute_subnetwork" "subnet_a" {
      provider      = google-beta
      ip_cidr_range = "10.1.2.0/24"
      name          = "lbsubnet-uswest1"
      network       = google_compute_network.default.id
      region        = "us-west1"
    }
    
    
    resource "google_compute_subnetwork" "subnet_b" {
      provider      = google-beta
      ip_cidr_range = "10.1.3.0/24"
      name          = "lbsubnet-useast1"
      network       = google_compute_network.default.id
      region        = "us-east1"
    }

###  API 

Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert). Replace `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
    
    {
     "routingConfig": {
       "routingMode": "regional"
     },
     "name": "NETWORK",
     "autoCreateSubnetworks": false
    }
    

Make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert). Replace `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_A/subnetworks
    
    {
     "name": "SUBNET_A",
     "network": "projects/PROJECT_ID/global/networks/lb-network-crs-reg",
     "ipCidrRange": "10.1.2.0/24",
     "region": "projects/PROJECT_ID/regions/REGION_A",
    }
    

Make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert). Replace `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_B/subnetworks
    
    {
     "name": "SUBNET_B",
     "network": "projects/PROJECT_ID/global/networks/NETWORK",
     "ipCidrRange": "10.1.3.0/24",
     "region": "projects/PROJECT_ID/regions/REGION_B",
    }
    

### Configure the proxy-only subnet

A [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides a set of IP addresses that Google Cloud uses to run Envoy proxies on your behalf. The proxies terminate connections from the client and create new connections to the backends.

This proxy-only subnet is used by all Envoy-based regional load balancers in the same region as the VPC network. There can only be one active proxy-only subnet for a given purpose, per region, per network.

**Important:** Don't try to assign addresses from the proxy-only subnet to your load balancer's forwarding rule or backends. You assign the forwarding rule's IP address and the backend instance IP addresses from a different subnet range (or ranges), not this one. Google Cloud reserves this subnet range for Google Cloud-managed proxies.

### Console

If you're using the Google Cloud console, you can wait and create the proxy-only subnet later on the **Load balancing** page.

If you want to create the proxy-only subnet now, use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network.
  3. On the **Subnet** tab, click **Add subnet**.
  4. Provide a **Name** for the proxy-only subnet.
  5. Select a **Region** : REGION_A
  6. In the **Purpose** list, select **Cross-region Managed Proxy**.
  7. In the **IP address range** field, enter `10.129.0.0/23`.
  8. Click **Add**.



Create the proxy-only subnet in `REGION_B`

  1. On the **Subnet** tab, click **Add subnet**.
  2. Provide a **Name** for the proxy-only subnet.
  3. Select a **Region** : REGION_B
  4. In the **Purpose** list, select **Cross-region Managed Proxy**.
  5. In the **IP address range** field, enter `10.130.0.0/23`.
  6. Click **Add**.



### gcloud

Create the proxy-only subnets with the [ `gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
        gcloud compute networks subnets create PROXY_SN_A \
            --purpose=GLOBAL_MANAGED_PROXY \
            --role=ACTIVE \
            --region=REGION_A \
            --network=NETWORK \
            --range=10.129.0.0/23
        
    
    
        gcloud compute networks subnets create PROXY_SN_B \
            --purpose=GLOBAL_MANAGED_PROXY \
            --role=ACTIVE \
            --region=REGION_B \
            --network=NETWORK \
            --range=10.130.0.0/23
        

### Terraform

To create the VPC proxy-only subnet in the `lb-network-crs-reg` network, use the [`google_compute_subnetwork` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork).
    
    
    resource "google_compute_subnetwork" "proxy_subnet_a" {
      provider      = google-beta
      ip_cidr_range = "10.129.0.0/23"
      name          = "proxy-only-subnet1"
      network       = google_compute_network.default.id
      purpose       = "GLOBAL_MANAGED_PROXY"
      region        = "us-west1"
      role          = "ACTIVE"
      lifecycle {
        ignore_changes = [ipv6_access_type]
      }
    }
    
    
    resource "google_compute_subnetwork" "proxy_subnet_b" {
      provider      = google-beta
      ip_cidr_range = "10.130.0.0/23"
      name          = "proxy-only-subnet2"
      network       = google_compute_network.default.id
      purpose       = "GLOBAL_MANAGED_PROXY"
      region        = "us-east1"
      role          = "ACTIVE"
      lifecycle {
        ignore_changes = [ipv6_access_type]
      }
    }

### API

Create the proxy-only subnets with the [ `subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert), replacing `PROJECT_ID` with your project ID.
    
    
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_A/subnetworks
    
        {
          "name": " PROXY_SN_A",
          "ipCidrRange": "10.129.0.0/23",
          "network": "projects/PROJECT_ID/global/networks/NETWORK",
          "region": "projects/PROJECT_ID/regions/REGION_A",
          "purpose": "GLOBAL_MANAGED_PROXY",
          "role": "ACTIVE"
        }
       
    
    
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_B/subnetworks
    
        {
          "name": "PROXY_SN_B",
          "ipCidrRange": "10.130.0.0/23",
          "network": "projects/PROJECT_ID/global/networks/NETWORK",
          "region": "projects/PROJECT_ID/regions/REGION_B",
          "purpose": "GLOBAL_MANAGED_PROXY",
          "role": "ACTIVE"
        }
       

## Configure firewall rules

This example uses the following firewall rules:

  * **`fw-ilb-to-backends`.** An ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port `22` from any address. You can choose a more restrictive source IP address range for this rule; for example, you can specify just the IP address ranges of the system from which you initiate SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs that the firewall rule applies to.

  * **`fw-healthcheck`.** An ingress rule, applicable to the instances being load balanced, that allows all TCP traffic from the Google Cloud health checking systems (in `130.211.0.0/22` and `35.191.0.0/16`). This example uses the target tag `load-balanced-backend` to identify the VMs that the firewall rule applies to.

  * **`fw-backends`.** An ingress rule, applicable to the instances being load balanced, that allows TCP traffic on ports `80`, `443`, and `8080` from the internal proxy Network Load Balancer's managed proxies. This example uses the target tag `load-balanced-backend` to identify the VMs that the firewall rule applies to.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

The [target tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#targets_for_firewall_rules) define the backend instances. Without the target tags, the firewall rules apply to all of your backend instances in the VPC network. When you create the backend VMs, make sure to include the specified target tags, as shown in Creating a managed instance group.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** to create the rule to allow incoming SSH connections:

     * **Name** : `fw-ilb-to-backends`
     * **Network** : NETWORK
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

     * **Name** : `fw-healthcheck`
     * **Network** : NETWORK
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `load-balanced-backend`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `130.211.0.0/22` and `35.191.0.0/16`
     * **Protocols and ports** :

       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80` for the port number.

As a best practice, limit this rule to just the protocols and ports that match those used by your health check. If you use `tcp:80` for the protocol and port, Google Cloud can use HTTP on port `80` to contact your VMs, but it cannot use HTTPS on port `443` to contact them.

  5. Click **Create**.

  6. Click **Create firewall rule** a third time to create the rule to allow the load balancer's proxy servers to connect the backends:

     * **Name** : `fw-backends`
     * **Network** : NETWORK
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `load-balanced-backend`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.129.0.0/23` and `10.130.0.0/23`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80, 443, 8080` for the port numbers.
  7. Click **Create**.




###  gcloud 

  1. Create the `fw-ilb-to-backends` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-ilb-to-backends \
             --network=NETWORK \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         

  2. Create the `fw-healthcheck` rule to allow Google Cloud health checks. This example allows all TCP traffic from health check probers; however, you can configure a narrower set of ports to meet your needs.
         
         gcloud compute firewall-rules create fw-healthcheck \
             --network=NETWORK \
             --action=allow \
             --direction=ingress \
             --source-ranges=130.211.0.0/22,35.191.0.0/16 \
             --target-tags=load-balanced-backend \
             --rules=tcp
         

  3. Create the `fw-backends` rule to allow the internal proxy Network Load Balancer's proxies to connect to your backends. Set `source-ranges` to the allocated ranges of your proxy-only subnet, for example, `10.129.0.0/23` and `10.130.0.0/23`.
         
         gcloud compute firewall-rules create fw-backends \
             --network=NETWORK \
             --action=allow \
             --direction=ingress \
             --source-ranges=SOURCE_RANGE \
             --target-tags=load-balanced-backend \
             --rules=tcp:80,tcp:443,tcp:8080
         




###  API 

Create the `fw-ilb-to-backends` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    {
     "name": "fw-ilb-to-backends",
     "network": "projects/PROJECT_ID/global/networks/NETWORK",
     "sourceRanges": [
       "0.0.0.0/0"
     ],
     "targetTags": [
       "allow-ssh"
     ],
     "allowed": [
      {
        "IPProtocol": "tcp",
        "ports": [
          "22"
        ]
      }
     ],
    "direction": "INGRESS"
    }
    

Create the `fw-healthcheck` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    {
     "name": "fw-healthcheck",
     "network": "projects/PROJECT_ID/global/networks/NETWORK",
     "sourceRanges": [
       "130.211.0.0/22",
       "35.191.0.0/16"
     ],
     "targetTags": [
       "load-balanced-backend"
     ],
     "allowed": [
       {
         "IPProtocol": "tcp"
       }
     ],
     "direction": "INGRESS"
    }
    

Create the `fw-backends` firewall rule to allow TCP traffic within the proxy subnet for the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    {
     "name": "fw-backends",
     "network": "projects/PROJECT_ID/global/networks/NETWORK",
     "sourceRanges": [
       "10.129.0.0/23",
       "10.130.0.0/23"
     ],
     "targetTags": [
       "load-balanced-backend"
     ],
     "allowed": [
       {
         "IPProtocol": "tcp",
         "ports": [
           "80"
         ]
       },
     {
         "IPProtocol": "tcp",
         "ports": [
           "443"
         ]
       },
       {
         "IPProtocol": "tcp",
         "ports": [
           "8080"
         ]
       }
     ],
     "direction": "INGRESS"
    }
    

## Create a managed instance group

This section shows how to create a template and a managed instance group. The managed instance group provides VM instances running the backend servers of an example cross-region internal proxy Network Load Balancer. For your instance group, you can define an HTTP service and map a port name to the relevant port. The backend service of the load balancer forwards traffic to the [named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named_ports). Traffic from clients is load balanced to backend servers. For demonstration purposes, backends serve their own hostnames.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

     1. Click **Create instance template**.
     2. For **Name** , enter `gil4-backendeast1-template`.
     3. Ensure that the **Boot disk** is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     4. Click **Advanced options**.
     5. Click **Networking** and configure the following fields: 
        1. For **Network tags** , enter `allow-ssh` and `load-balanced-backend`.
        2. For **Network interfaces** , select the following: 
           * **Network** : NETWORK
           * **Subnet** : SUBNET_B
     6. Click **Management**. Enter the following script into the **Startup script** field.
            
            #! /bin/bash
            apt-get update
            apt-get install apache2 -y
            a2ensite default-ssl
            a2enmod ssl
            vm_hostname="$(curl -H "Metadata-Flavor:Google" \
            http://169.254.169.254/computeMetadata/v1/instance/name)"
            echo "Page served from: $vm_hostname" | \
            tee /var/www/html/index.html
            systemctl restart apache2
            

     7. Click **Create**.

     8. Click **Create instance template**.

     9. For **Name** , enter `gil4-backendwest1-template`.

     10. Ensure that the **Boot disk** is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.

     11. Click **Advanced options**.

     12. Click **Networking** and configure the following fields:

        1. For **Network tags** , enter `allow-ssh` and `load-balanced-backend`.
        2. For **Network interfaces** , select the following: 
           * **Network** : NETWORK
           * **Subnet** : SUBNET_A
     13. Click **Management**. Enter the following script into the **Startup script** field.
            
            #! /bin/bash
            apt-get update
            apt-get install apache2 -y
            a2ensite default-ssl
            a2enmod ssl
            vm_hostname="$(curl -H "Metadata-Flavor:Google" \
            http://169.254.169.254/computeMetadata/v1/instance/name)"
            echo "Page served from: $vm_hostname" | \
            tee /var/www/html/index.html
            systemctl restart apache2
            

     14. Click **Create**.

  2. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     1. Click **Create instance group**.
     2. Select **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
     3. For **Name** , enter `gl4-ilb-miga`.
     4. For **Location** , select **Single zone**.
     5. For **Region** , select REGION_A.
     6. For **Zone** , select ZONE_A.
     7. For **Instance template** , select `gil4-backendwest1-template`.
     8. Specify the number of instances that you want to create in the group.

For this example, specify the following options under **Autoscaling** :

        * For **Autoscaling mode** , select `Off:do not autoscale`.
        * For **Maximum number of instances** , enter `2`.

Optionally, in the **Autoscaling** section of the UI, you can configure the instance group to [automatically add or remove instances](https://docs.cloud.google.com/compute/docs/autoscaler) based on instance CPU use.

     9. Click **Create**.

     10. Click **Create instance group**.

     11. Select **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).

     12. For **Name** , enter `gl4-ilb-migb`.

     13. For **Location** , select **Single zone**.

     14. For **Region** , select REGION_B.

     15. For **Zone** , select ZONE_B.

     16. For **Instance template** , select `gil4-backendeast1-template`.

     17. Specify the number of instances that you want to create in the group.

For this example, specify the following options under **Autoscaling** :

        * For **Autoscaling mode** , select `Off:do not autoscale`.
        * For **Maximum number of instances** , enter `2`.

Optionally, in the **Autoscaling** section of the UI, you can configure the instance group to [automatically add or remove instances](https://docs.cloud.google.com/compute/docs/autoscaler) based on instance CPU usage.

     18. Click **Create**.




###  gcloud 

The gcloud CLI instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.

  1. Create a VM instance template with HTTP server with the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).
         
         gcloud compute instance-templates create gil4-backendwest1-template \
            --region=REGION_A \
            --network=NETWORK \
            --subnet=SUBNET_A \
            --tags=allow-ssh,load-balanced-backend \
            --image-family=debian-12 \
            --image-project=debian-cloud \
            --metadata=startup-script='#! /bin/bash
              apt-get update
              apt-get install apache2 -y
              a2ensite default-ssl
              a2enmod ssl
              vm_hostname="$(curl -H "Metadata-Flavor:Google" \
              http://169.254.169.254/computeMetadata/v1/instance/name)"
              echo "Page served from: $vm_hostname" | \
              tee /var/www/html/index.html
              systemctl restart apache2'
         
         
         gcloud compute instance-templates create gil4-backendeast1-template \
             --region=REGION_B \
             --network=NETWORK \
             --subnet=SUBNET_B \
             --tags=allow-ssh,load-balanced-backend \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --metadata=startup-script='#! /bin/bash
               apt-get update
               apt-get install apache2 -y
               a2ensite default-ssl
               a2enmod ssl
               vm_hostname="$(curl -H "Metadata-Flavor:Google" \
               http://169.254.169.254/computeMetadata/v1/instance/name)"
               echo "Page served from: $vm_hostname" | \
               tee /var/www/html/index.html
               systemctl restart apache2'
         

  2. Create a managed instance group in the zone with the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).
         
         gcloud compute instance-groups managed create gl4-ilb-miga \
             --zone=ZONE_A \
             --size=2 \
             --template=gil4-backendwest1-template
         
         
         gcloud compute instance-groups managed create gl4-ilb-migb \
             --zone=ZONE_B \
             --size=2 \
             --template=gil4-backendeast1-template
         




###  API 

Create the instance template with the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name":"gil4-backendwest1-template",
      "properties":{
         "machineType":"e2-standard-2",
         "tags":{
           "items":[
             "allow-ssh",
             "load-balanced-backend"
           ]
         },
         "metadata":{
            "kind":"compute#metadata",
            "items":[
              {
                "key":"startup-script",
                "value":"#! /bin/bash\napt-get update\napt-get install
                apache2 -y\na2ensite default-ssl\na2enmod ssl\n
                vm_hostname=\"$(curl -H \"Metadata-Flavor:Google\"
                \\\nhttp://169.254.169.254/computeMetadata/v1/instance/name)\"\n
                echo \"Page served from: $vm_hostname\" | \\\ntee
                /var/www/html/index.html\nsystemctl restart apache2"
              }
            ]
         },
         "networkInterfaces":[
           {
             "network":"projects/PROJECT_ID/global/networks/NETWORK",
             "subnetwork":"regions/REGION_A/subnetworks/SUBNET_A",
             "accessConfigs":[
               {
                 "type":"ONE_TO_ONE_NAT"
               }
             ]
           }
         ],
         "disks":[
           {
             "index":0,
             "boot":true,
             "initializeParams":{
               "sourceImage":"projects/debian-cloud/global/images/family/debian-12"
             },
             "autoDelete":true
           }
         ]
      }
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name":"gil4-backendeast1-template",
      "properties":{
         "machineType":"e2-standard-2",
         "tags":{
           "items":[
             "allow-ssh",
             "load-balanced-backend"
           ]
         },
         "metadata":{
            "kind":"compute#metadata",
            "items":[
              {
                "key":"startup-script",
                "value":"#! /bin/bash\napt-get update\napt-get install
                apache2 -y\na2ensite default-ssl\na2enmod ssl\n
                vm_hostname=\"$(curl -H \"Metadata-Flavor:Google\"
                \\\nhttp://169.254.169.254/computeMetadata/v1/instance/name)\"\n
                echo \"Page served from: $vm_hostname\" | \\\ntee
                /var/www/html/index.html\nsystemctl restart apache2"
              }
            ]
         },
         "networkInterfaces":[
           {
             "network":"projects/PROJECT_ID/global/networks/NETWORK",
             "subnetwork":"regions/REGION_B/subnetworks/SUBNET_B",
             "accessConfigs":[
               {
                 "type":"ONE_TO_ONE_NAT"
               }
             ]
           }
         ],
         "disks":[
           {
             "index":0,
             "boot":true,
             "initializeParams":{
               "sourceImage":"projects/debian-cloud/global/images/family/debian-12"
             },
             "autoDelete":true
           }
         ]
      }
    }
    

Create a managed instance group in each zone with the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/{zone}/instanceGroupManagers
    
    {
      "name": "gl4-ilb-miga",
      "zone": "projects/PROJECT_ID/zones/ZONE_A",
      "instanceTemplate": "projects/PROJECT_ID/global/instanceTemplates/gil4-backendwest1-template",
      "baseInstanceName": "gl4-ilb-miga",
      "targetSize": 2
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/{zone}/instanceGroupManagers
    
    {
      "name": "gl4-ilb-migb",
      "zone": "projects/PROJECT_ID/zones/ZONE_A",
      "instanceTemplate": "projects/PROJECT_ID/global/instanceTemplates/gil4-backendwest1-template",
      "baseInstanceName": "gl4-ilb-migb",
      "targetSize": 2
    }
    

## Configure the load balancer

This section creates the following cross-region internal proxy Network Load Balancer resources:

  * A global TCP health check.
  * A global backend service with the same MIGs as the backend.
  * A global target proxy.
  * Two global forwarding rules with regional IP addresses. For the forwarding rule's IP address, use the `SUBNET_A` or `SUBNET_B` IP address range. If you try to use the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets), forwarding rule creation fails.



#### Proxy availability

Sometimes Google Cloud regions don't have enough proxy capacity for a new load balancer. If this happens, the Google Cloud console provides a proxy availability warning message when you are creating your load balancer. To resolve this issue, you can do one of the following:

  * Select a different region for your load balancer. This can be a practical option if you have backends in another region.
  * Select a VPC network that already has an allocated proxy-only subnet.
  * Wait for the capacity issue to be resolved.




###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Proxy load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. For **Cross-region or single region deployment** , select **Best for cross-region workloads** and click **Next**.
  7. Click **Configure**.



**Basic configuration**

  1. Provide a **Name** for the load balancer.
  2. For **Network** , select NETWORK.



**Configure the frontend with two forwarding rules**

  1. Click **Frontend configuration**.
     1. Provide a **Name** for the forwarding rule.
     2. In the **Subnetwork region** list, select REGION_A.   


**Reserve a proxy-only subnet**

If you already configured the proxy-only subnet, the **Reserve subnet** button isn't displayed. You can continue with the next steps. 
     3. In the **Subnetwork** list, select SUBNET_A.
     4. In the **IP address** list, click **Create IP address**. The **Reserve a static internal IP address** page opens.
        * Provide a **Name** for the static IP address.
        * In the **Static IP address** list, select **Let me choose**.
        * In the **Custom IP address** field, enter `10.1.2.99`.
        * Select **Reserve**.
  2. Click **Done**.
  3. To add the second forwarding rule, click **Add frontend IP and port**.
     1. Provide a **Name** for the forwarding rule.
     2. In the **Subnetwork region** list, select REGION_B.   


**Reserve a proxy-only subnet**

Because you have already configured the  proxy-only subnet, the **Reserve subnet** button isn't displayed. You can continue with the next steps. 
     3. In the **Subnetwork** list, select SUBNET_B.
     4. In the **IP address** list, click **Create IP address**. The **Reserve a static internal IP address** page opens.
        * Provide a **Name** for the static IP address.
        * In the **Static IP address** list, select **Let me choose**.
        * In the **Custom IP address** field, enter `10.1.3.99`.
        * Select **Reserve**.
  4. Click **Done**.

**Configure the backend service**

  1. Click **Backend configuration**.
  2. In the **Create or select backend services** list, click **Create a backend service**.
  3. Provide a **Name** for the backend service.
  4. For **Protocol** , select **TCP**.
  5. For **Named Port** , enter `http`.
  6. In the **Backend type** list, select **Instance group**.
  7. In the **Health check** list, click **Create a health check** , and then enter the following information:
     * In the **Name** field, enter `global-http-health-check`.
     * In the **Protocol** list, select `HTTP`.
     * In the **Port** field, enter `80`.
     * Click **Create**.
  8. In the **New backend** section:
     1. In the **Instance group** list, select `gl4-ilb-miga` in REGION_A.
     2. Set **Port numbers** to `80`.
     3. For the **Balancing mode** , select **Connection**.
     4. Click **Done**.
     5. To add another backend, click **Add backend**.
     6. In the **Instance group** list, select `gl4-ilb-migb` in REGION_B.
     7. Set **Port numbers** to `80`.
     8. Click **Done**.



**Review the configuration**

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Click **Create**.



###  gcloud 

  1. Define the TCP health check with the [`gcloud compute health-checks create tcp` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/tcp).
         
         gcloud compute health-checks create tcp global-health-check \
            --use-serving-port \
            --global
         

  2. Define the backend service with the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create).
         
         gcloud compute backend-services create gl4-gilb-backend-service \
           --load-balancing-scheme=INTERNAL_MANAGED \
           --protocol=TCP \
           --enable-logging \
           --logging-sample-rate=1.0 \
           --health-checks=global-health-check \
           --global-health-checks \
           --global
         

  3. Add backends to the backend service with the [`gcloud compute backend-services add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend).
         
         gcloud compute backend-services add-backend gl4-gilb-backend-service \
           --balancing-mode=CONNECTION \
           --max-connections=50 \
           --instance-group=gl4-ilb-miga \
           --instance-group-zone=ZONE_A \
           --global
         
         
         gcloud compute backend-services add-backend gl4-gilb-backend-service \
           --balancing-mode=CONNECTION \
           --max-connections=50 \
           --instance-group=gl4-ilb-migb \
           --instance-group-zone=ZONE_B \
           --global
         

  4. Create the target proxy.

Create the target proxy with the [`gcloud compute target-tcp-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create).
         
         gcloud compute target-tcp-proxies create gilb-tcp-proxy \
           --backend-service=gl4-gilb-backend-service \
           --global
         

  5. Create two forwarding rules, one with a VIP (10.1.2.99) in `REGION_B` and another one with a VIP (10.1.3.99) in `REGION_A`. For more information, see [Reserve a static internal IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip).

For custom networks, you must reference the subnet in the forwarding rule. Note that this is the VM subnet, not the proxy subnet.

Use the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) with the correct flags.
         
         gcloud compute forwarding-rules create gil4forwarding-rule-a \
           --load-balancing-scheme=INTERNAL_MANAGED \
           --network=NETWORK \
           --subnet=SUBNET_A \
           --subnet-region=REGION_A \
           --address=10.1.2.99 \
           --ports=80 \
           --target-tcp-proxy=gilb-tcp-proxy \
           --global
         
         
         gcloud compute forwarding-rules create gil4forwarding-rule-b \
           --load-balancing-scheme=INTERNAL_MANAGED \
           --network=NETWORK \
           --subnet=SUBNET_B \
           --subnet-region=REGION_B \
           --address=10.1.3.99 \
           --ports=80 \
           --target-tcp-proxy=gilb-tcp-proxy \
           --global
         




###  API 

Create the health check by making a `POST` request to the [`healthChecks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/healthChecks
    
    {
    "name": "global-health-check",
    "type": "TCP",
    "httpHealthCheck": {
      "portSpecification": "USE_SERVING_PORT"
    }
    }
    

Create the global backend service by making a `POST` request to the [`backendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    
    {
    "name": "gl4-gilb-backend-service",
    "backends": [
      {
        "group": "projects/PROJECT_ID/zones/ZONE_A/instanceGroups/gl4-ilb-miga",
        "balancingMode": "CONNECTION"
      },
      {
        "group": "projects/PROJECT_ID/zones/ZONE_B/instanceGroups/gl4-ilb-migb",
        "balancingMode": "CONNECTION"
      }
    ],
    "healthChecks": [
      "projects/PROJECT_ID/regions/global/healthChecks/global-health-check"
    ],
    "loadBalancingScheme": "INTERNAL_MANAGED"
    }
    

Create the target TCP proxy by making a `POST` request to the [`targetTcpProxies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetTcpProxies/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetTcpProxy
    
    {
    "name": "l4-ilb-proxy",
    }
    

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules
    
    {
    "name": "gil4forwarding-rule-a",
    "IPAddress": "10.1.2.99",
    "IPProtocol": "TCP",
    "portRange": "80-80",
    "target": "projects/PROJECT_ID/global/targetTcpProxies/l4-ilb-proxy",
    "loadBalancingScheme": "INTERNAL_MANAGED",
    "subnetwork": "projects/PROJECT_ID/regions/REGION_A/subnetworks/SUBNET_A",
    "network": "projects/PROJECT_ID/global/networks/NETWORK",
    "networkTier": "PREMIUM"
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules
    
    {
    "name": "gil4forwarding-rule-b",
    "IPAddress": "10.1.3.99",
    "IPProtocol": "TCP",
    "portRange": "80-80",
    "target": "projects/PROJECT_ID/global/targetTcpProxies/l4-ilb-proxy",
    "loadBalancingScheme": "INTERNAL_MANAGED",
    "subnetwork": "projects/PROJECT_ID/regions/REGION_B/subnetworks/SUBNET_B",
    "network": "projects/PROJECT_ID/global/networks/NETWORK",
    "networkTier": "PREMIUM"
    }
    

Create the forwarding rule by making a `POST` request to the [`globalForwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules/insert), replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules
    
    {
    "name": "gil4forwarding-rule-a",
    "IPAddress": "10.1.2.99",
    "IPProtocol": "TCP",
    "portRange": "80-80",
    "target": "projects/PROJECT_ID/global/targetTcpProxies/l4-ilb-proxy",
    "loadBalancingScheme": "INTERNAL_MANAGED",
    "subnetwork": "projects/PROJECT_ID/regions/REGION_A/subnetworks/SUBNET_A",
    "network": "projects/PROJECT_ID/global/networks/NETWORK",
    "networkTier": "PREMIUM"
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules
    
    {
    "name": "gil4forwarding-rule-b",
    "IPAddress": "10.1.3.99",
    "IPProtocol": "TCP",
    "portRange": "80-80",
    "target": "projects/PROJECT_ID/global/targetTcpProxies/l4-ilb-proxy",
    "loadBalancingScheme": "INTERNAL_MANAGED",
    "subnetwork": "projects/PROJECT_ID/regions/REGION_B/subnetworks/SUBNET_B",
    "network": "projects/PROJECT_ID/global/networks/NETWORK",
    "networkTier": "PREMIUM"
    }
    

### Test the load balancer

#### Create a VM instance to test connectivity

  1. Create a client VM in `REGION_B` and `REGION_A` regions:
         
         gcloud compute instances create l4-ilb-client-a \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --network=NETWORK \
             --subnet=SUBNET_A \
             --zone=ZONE_A \
             --tags=allow-ssh
         
         
         gcloud compute instances create l4-ilb-client-b \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --network=NETWORK \
             --subnet=SUBNET_B \
             --zone=ZONE_B \
             --tags=allow-ssh
         

  2. Use SSH to connect to each client instance.
         
         gcloud compute ssh l4-ilb-client-a --zone=ZONE_A
         
         
         gcloud compute ssh l4-ilb-client-b --zone=ZONE_B
         

  3. Verify that the IP address is serving its hostname

     * Verify that the client VM can reach both IP addresses. The command should succeed and return the name of the backend VM which served the request:
           
           curl 10.1.2.99
           
           
           curl 10.1.3.99
           




#### Test failover

  1. Verify failover to backends in the `REGION_A` region when backends in the `REGION_B` are unhealthy or unreachable. To simulate failover, remove all backends from `REGION_B`:
         
         gcloud compute backend-services remove-backend gl4-gilb-backend-service \
           --instance-group=gl4-ilb-migb \
           --instance-group-zone=ZONE_B \
           --global
         

  2. Connect using SSH to a client VM in `REGION_B`.
         
         gcloud compute ssh l4-ilb-client-b \
            --zone=ZONE_B
         

  3. Send requests to the load balanced IP address in the `REGION_B` region. The command output shows responses from backend VMs in `REGION_A`:
         
         {
         RESULTS=
         for i in {1..100}
         do
           RESULTS="$RESULTS:$(curl 10.1.3.99)"
         done
         echo "***"
         echo "*** Results of load-balancing to 10.1.3.99: "
         echo "***"
         echo "$RESULTS" | tr ':' '\n' | grep -Ev "^$" | sort | uniq -c
         echo
         }
         




## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Create a load balancer with TLS routes

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section shows you how to create a load balancer that can use SNI-based routing. SNI-based routing lets your proxy Network Load Balancers route traffic to specific backend services based on the Server Name Indication (SNI) hostname provided during the TLS handshake.

To create this load balancer we use the same networks, subnets, and firewall rules created previously on this page. You configure the deployment shown in the following diagram:

[ ![Cross-region internal proxy Network Load Balancer configuration with TLS routes.](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-int-tcp-proxy-tls-routes-single-backend.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-int-tcp-proxy-tls-routes-single-backend.svg) External proxy Network Load Balancer configuration with TLS routes.

### Create a managed instance group backend

This section shows you how to create a managed instance group (MIG) backends for the load balancer. The MIG provides VM instances running the backend servers for this example.

The Google Cloud CLI instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

  1. Create an instance template with an "echo" HTTPS service that is exposed on port 443.
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
         --region=REGION_A \
         --network=NETWORK \
         --subnet=SUBNET_A \
         --stack-type=IPv4_ONLY \
         --tags=allow-ssh,load-balanced-backend \
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
             --global \
             --port=HC_PORT
         

Replace the following:

     * `HTTP_HEALTH_CHECK_NAME`: a name for the health check.
     * `HC_PORT`: the port for the health check.
  2. Create a backend service:
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --protocol=TCP \
             --port-name=PORT_NAME \
             --health-checks=global-health-check \
             --global-health-checks \
             --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: a name for the backend service.
     * `PORT_NAME`: the port name for the backend service. Use the same named port configured on the instance group—for example, `tcp443`.
     * `HTTPS_HEALTH_CHECK_NAME`: the name of the HTTPS health check.
  3. Add the backend instance group to your backend service:
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.8 \
             --instance-group=INSTANCE_GROUP_NAME \
             --instance-group-zone=ZONE_A \
             --global
         

Replace the following:

     * `INSTANCE_GROUP_NAME`: the name of the backend instance group.
     * `ZONE_A`: the zone of the instance group.
  4. Create a target TCP proxy.
         
         gcloud beta compute target-tcp-proxies create TARGET_TCP_PROXY_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --proxy-header=NONE \
             --global
         

Replace `TARGET_TCP_PROXY_NAME` with the name of the target TCP proxy.

  5. Create a TLS route specification and save it to a YAML file.
         
         cat <<EOF | tee YAML_FILE_NAME
         name: TLS_ROUTE_NAME
         targetProxies:
         - projects/PROJECT_NUMBER/locations/global/targetTcpProxies/TARGET_TCP_PROXY
         rules:
         - matches:
           - sniHost:
             - example.com
           action:
           destinations:
           - serviceName: projects/PROJECT_NUMBER/locations/global/backendServices/BACKEND_SERVICE
         EOF
         

Replace the following:

     * `YAML_FILE_NAME`: a name for the YAML file—for example, `tls-route.yaml`.
     * `TLS_ROUTE_NAME`: a name for the TLS route.
     * `PROJECT_NUMBER`: the project number.
  6. Use the YAML specification file to create the TLS route resource.
         
         gcloud network-services tls-routes import TLS_ROUTE_NAME \
           --source=YAML_FILE_NAME \
           --global
         

  7. Create the forwarding rule.
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
           --load-balancing-scheme=INTERNAL_MANAGED \
           --network=NETWORK \
           --subnet=SUBNET_A \
           --subnet-region=REGION_A \
           --address=IP_ADDRESS \
           --ports=PORT \
           --target-tcp-proxy=TARGET_TCP_PROXY_NAME \
           --global
         

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




### PROXY protocol for retaining client connection information

The internal proxy Network Load Balancer terminates TCP connections from the client and creates new connections to the VM instances. By default, the original client IP and port information is not preserved.

To preserve and send the original connection information to your instances, enable [PROXY protocol](http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt) (version 1). This protocol sends an additional header that contains the source IP address, destination IP address, and port numbers to the instance as a part of the request.

Make sure that the internal proxy Network Load Balancer's backend instances are running HTTP or HTTPS servers that support PROXY protocol headers. If the HTTP or HTTPS servers are not configured to support PROXY protocol headers, the backend instances return empty responses. For example, the PROXY protocol doesn't work with the Apache HTTP Server software. You can use different web server software, such as Nginx.

If you set the PROXY protocol for user traffic, you must also set it for your health checks. If you are checking health and serving content on the same port, set the health check's `--proxy-header` to match your load balancer setting.

The PROXY protocol header is typically a single line of user-readable text in the following format:
    
    
    PROXY TCP4 <client IP> <load balancing IP> <source port> <dest port>\r\n
    

Following is an example of the PROXY protocol:
    
    
    PROXY TCP4 192.0.2.1 198.51.100.1 15221 110\r\n

In the preceding example, the client IP is `192.0.2.1`, the load balancing IP is `198.51.100.1`, the client port is `15221`, and the destination port is `110`.

In cases where the client IP is not known, the load balancer generates a PROXY protocol header in the following format:
    
    
    PROXY UNKNOWN\r\n
    

#### Update PROXY protocol header for target TCP proxy

The example load balancer setup on this page shows you how to enable the PROXY protocol header while creating the internal proxy Network Load Balancer. Use these steps to change the PROXY protocol header for an existing target TCP proxy.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click edit**Edit** for your load balancer.

  3. Click **Frontend configuration**.

  4. Change the value of the **Proxy protocol** field to **On**.

  5. Click **Update** to save your changes.




###  gcloud 

In the following command, edit the `--proxy-header` field and set it to either `NONE` or `PROXY_V1` depending on your requirement.
    
    
    gcloud compute target-ssl-proxies update int-tcp-target-proxy \
        --proxy-header=[NONE | PROXY_V1]
    

### Use the same IP address between multiple internal forwarding rules

For multiple internal forwarding rules to share the same internal IP address, you must reserve the IP address and set its `--purpose` flag to `SHARED_LOADBALANCER_VIP`.

###  gcloud 
    
    
    gcloud compute addresses create SHARED_IP_ADDRESS_NAME \
        --region=REGION \
        --subnet=SUBNET_NAME \
        --purpose=SHARED_LOADBALANCER_VIP
    

### Enable session affinity

The example configuration creates a backend service without session affinity.

These procedures show you how to update a backend service for an example load balancer so that the backend service uses client IP affinity or generated cookie affinity.

When client IP affinity is enabled, the load balancer directs a particular client's requests to the same backend VM based on a hash created from the client's IP address and the load balancer's IP address (the internal IP address of an internal forwarding rule).

###  Console

To enable client IP session affinity:

  1. In the Google Cloud console, go to the **Load balancing** page.   
[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)
  2. Click **Backends**.
  3. Click the name of the backend service you created for this example and click **Edit**.
  4. On the **Backend service details** page, click **Advanced configuration**.
  5. Under **Session affinity** , select **Client IP** from the menu.
  6. Click **Update**.



###  gcloud 

Use the following gcloud command to update the `BACKEND_SERVICE` backend service, specifying client IP session affinity:
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --global \
        --session-affinity=CLIENT_IP
    

### Enable connection draining

You can enable connection draining on backend services to ensure minimal interruption to your users when an instance that is serving traffic is terminated, removed manually, or removed by an autoscaler. To learn more about connection draining, read the [Enabling connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining) documentation.

## What's next

  * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)
  * [Internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).
  * [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
