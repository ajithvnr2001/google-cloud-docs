---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb/
title: Set up a regional external Application Load Balancer with VM instance group backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:41.588172+00:00
---

# Set up a regional external Application Load Balancer with VM instance group backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external Application Load Balancer with VM instance group backends Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for configuring a regional external Application Load Balancer for your services that run on Compute Engine VMs.

Because regional external Application Load Balancers allow you to create load balancers in specific regions, they are often used for workloads that have jurisdictional compliance requirements. Workloads that require access to [Standard Network Tier egress](https://docs.cloud.google.com/network-tiers) are another common use case for regional external Application Load Balancers, because the regional external Application Load Balancers support both the Premium and Standard Network Service Tier.

Before following this guide, familiarize yourself with the following:

  * [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [VPC firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls)



**Note:** Regional external Application Load Balancers support both the Premium and Standard Network Service Tiers. This procedure demonstrates the setup with Standard Tier.

## Permissions

To follow this guide, you must be able to create instances and modify a network in a project. You must be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Add and remove firewall rules | [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Create instances | [Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Optional: Use BYOIP addresses

With bring your own IP (BYOIP), you can import your own public addresses to Google Cloud to use the addresses with Google Cloud resources. For example, if you import your own IPv4 addresses, you can assign one to the forwarding rule when you configure your load balancer. When you follow the instructions in this document to [configure the load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb#lb-config), provide the BYOIP address as the **IP address**.

For more information about using BYOIP, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Setup overview

You can configure a regional external Application Load Balancer as described in the following high-level configuration flow. The numbered steps refer to the numbers in the diagram.

[ ![Regional external Application Load Balancer numbered components](https://docs.cloud.google.com/static/load-balancing/images/regional-l7xlb-numbered-components.svg)](https://docs.cloud.google.com/static/load-balancing/images/regional-l7xlb-numbered-components.svg) Regional external Application Load Balancer numbered components (click to enlarge)

As shown in the diagram, this example creates a regional external Application Load Balancer in a VPC network in region `us-west1`, with one backend service and two backend instance groups.

The diagram shows the following:

  1. A VPC network with two subnets:

     1. One subnet is used for backends (instance groups). Its primary IP address range is `10.1.2.0/24`.

     2. One subnet is a proxy-only subnet in the `us-west1` region. You must create one proxy-only subnet in each region of a VPC network where you use regional external Application Load Balancers. The region's proxy-only subnet is shared among all regional load balancers in the region. Source addresses of packets sent from the load balancers to your service's backends are allocated from the proxy-only subnet. In this example, the proxy-only subnet for the region has a primary IP address range of `10.129.0.0/23`, which is the recommended subnet size. For more information, see [Proxy-only subnets](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).

  2. A firewall rule that permits proxy-only subnet traffic flows in your network. This means adding one rule that allows TCP port `80`, `443`, and `8080` traffic from `10.129.0.0/23` (the range of the proxy-only subnet in this example). Another firewall rule for the [health check probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

  3. Backend instances.

  4. Instance groups:

     1. Managed or unmanaged instance groups for Compute Engine VM deployments
     2. NEGs for GKE deployments

In each zone, you can have a combination of backend group types based on the requirements of your deployment.

  5. A regional health check that reports the readiness of your backends.

  6. A regional backend service that monitors the usage and health of backends.

  7. A regional URL map that parses the URL of a request and forwards requests to specific backend services based on the host and path of the request URL.

  8. A regional target HTTP or HTTPS proxy, which receives a request from the user and forwards it to the URL map. For HTTPS, configure a regional SSL certificate resource. The target proxy can use either the SSL certificate or the Certificate Manager certificate to decrypt SSL traffic if you configure HTTPS load balancing. The target proxy can forward traffic to your instances by using HTTP or HTTPS.

  9. A forwarding rule, which has the external IP address of your load balancer to forward each incoming request to the target proxy.

The external IP address that is associated with the forwarding rule is reserved by using the `gcloud compute addresses create` command, as described in [Reserving the load balancer's IP address](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb#reserve-ip).




## Configure the network and subnets

You need a VPC network with two subnets: one for the load balancer's backends and the other for the load balancer's proxies. A regional external Application Load Balancer is regional. Traffic within the VPC network is routed to the load balancer if the traffic's source is in a subnet in the same region as the load balancer.

This example uses the following VPC network, region, and subnets:

  * **Network.** The network is a [custom-mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.

  * **Subnet for backends.** A subnet named `backend-subnet` in the `us-west1` region uses `10.1.2.0/24` for its primary IP range.

  * **Subnet for proxies.** A subnet named `proxy-only-subnet` in the `us-west1` region uses `10.129.0.0/23` for its primary IP range.


**Note:** You can change the name of the network, the region, and the parameters for the subnets; however, subsequent steps in this guide use the network, region, and subnet parameters as outlined here.

### Configure the network and subnet for backends

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. In the **Subnets** section:

     * Set **Subnet creation mode** to **Custom**.
     * In the **New subnet** section, enter the following information: 
       * **Name** : `backend-subnet`
       * **Region** : `us-west1`
       * **IP address range** : `10.1.2.0/24`
     * Click **Done**.
  5. Click **Create**.




###  gcloud 

  1. Create the custom VPC network with the [`gcloud compute networks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) command:
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. Create a subnet in the `lb-network` network in the `us-west1` region with the [`gcloud compute networks subnets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command:
         
         gcloud compute networks subnets create backend-subnet \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=us-west1
         




###  Terraform 

To create the VPC network, use the [`google_compute_network`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network) resource.
    
    
    resource "google_compute_network" "default" {
      name                    = "lb-network"
      auto_create_subnetworks = false
      routing_mode            = "REGIONAL"
    }

To create the VPC subnet in the `lb-network` network, use the [`google_compute_subnetwork`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork) resource.
    
    
    resource "google_compute_subnetwork" "default" {
      name                       = "backend-subnet"
      ip_cidr_range              = "10.1.2.0/24"
      network                    = google_compute_network.default.id
      private_ipv6_google_access = "DISABLE_GOOGLE_ACCESS"
      purpose                    = "PRIVATE"
      region                     = "us-west1"
      stack_type                 = "IPV4_ONLY"
    }

###  API 

  1. Make a `POST` request to the [`networks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert) method, replacing PROJECT_ID with your project ID.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
         {
          "routingConfig": {
            "routingMode": "REGIONAL"
          },
          "name": "lb-network",
          "autoCreateSubnetworks": false
         }
         

  2. Make a `POST` request to the [`subnetworks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert) method, replacing PROJECT_ID with your project ID.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks
         {
          "name": "backend-subnet",
          "network": "projects/PROJECT_ID/global/networks/lb-network",
          "ipCidrRange": "10.1.2.0/24",
          "region": "projects/PROJECT_ID/regions/us-west1",
         }
         




### Configure the proxy-only subnet

A [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides a set of IP addresses that Google uses to run Envoy proxies on your behalf. The proxies terminate connections from the client and create new connections to the backends.

This proxy-only subnet is used by all [Envoy-based regional load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) in the same region of the `lb-network` VPC network. There can only be one active proxy-only subnet per region, per network.

**Important:** Don't try to assign addresses from the proxy-only subnet to your load balancer's backends. You assign the backend instance IP addresses from a different subnet range (or ranges), not this one. Google Cloud reserves this subnet range for Google Cloud-managed proxies.

###  Console 

If you're using the Google Cloud console, you can also wait and create the proxy-only subnet later on the **Load balancing** page.

If you want to create the proxy-only subnet now, use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network: `lb-network`.

  3. Click **Add subnet**.

  4. For **Name** , enter `proxy-only-subnet`.

  5. For **Region** , select `us-west1`.

  6. Set **Purpose** to **Regional Managed Proxy**.

  7. For **IP address range** , enter `10.129.0.0/23`.

  8. Click **Add**.




###  gcloud 

Create the proxy-only subnet with the [`gcloud compute networks subnets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) command.
    
    
    gcloud compute networks subnets create proxy-only-subnet \
      --purpose=REGIONAL_MANAGED_PROXY \
      --role=ACTIVE \
      --region=us-west1 \
      --network=lb-network \
      --range=10.129.0.0/23
    

###  Terraform 

To create the VPC proxy-only subnet in the `lb-network` network, use the [`google_compute_subnetwork`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork) resource.
    
    
    resource "google_compute_subnetwork" "proxy_only" {
      name          = "proxy-only-subnet"
      ip_cidr_range = "10.129.0.0/23"
      network       = google_compute_network.default.id
      purpose       = "REGIONAL_MANAGED_PROXY"
      region        = "us-west1"
      role          = "ACTIVE"
    }

###  API 

Create the proxy-only subnet with the [`subnetworks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert) method, replacing PROJECT_ID with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks
    {
      "name": "proxy-only-subnet",
      "ipCidrRange": "10.129.0.0/23",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "region": "projects/PROJECT_ID/regions/us-west1",
      "purpose": "REGIONAL_MANAGED_PROXY",
      "role": "ACTIVE"
    }
    

### Configure firewall rules

This example uses the following firewall rules:

  * **`fw-allow-health-check`.** An ingress rule, applicable to the instances being load balanced, that allows all TCP traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `load-balanced-backend` to identify the VMs that the firewall rule applies to.

  * **`fw-allow-proxies`.** An ingress rule, applicable to the instances being load balanced, that allows TCP traffic on ports `80`, `443`, and `8080` from the regional external Application Load Balancer's managed proxies. This example uses the target tag `load-balanced-backend` to identify the VMs that the firewall rule applies to.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

The [target tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#targets_for_firewall_rules) define the backend instances. Without the target tags, the firewall rules apply to all of your backend instances in the VPC network. When you create the backend VMs, make sure to include the specified target tags, as shown in [Creating a managed instance group](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https#creating_a_managed_instance_group).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall rules](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** to create the rule to allow Google Cloud health checks:

     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `load-balanced-backend`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80` for the port number. As a best practice, limit this rule to just the protocols and ports that match those used by your health check. If you use `tcp:80` for the protocol and port, Google Cloud can use HTTP on port `80` to contact your VMs, but it cannot use HTTPS on port `443` to contact them.
  3. Click **Create**.

  4. Click **Create firewall rule** to create the rule to allow the load balancer's proxy servers to connect the backends:

     * **Name** : `fw-allow-proxies`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `load-balanced-backend`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.129.0.0/23`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `80, 443, 8080` for the port numbers.
  5. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-health-check` rule to allow Google Cloud health checks. This example allows all TCP traffic from health check probers; however, you can configure a narrower set of ports to meet your needs.
         
         gcloud compute firewall-rules create fw-allow-health-check \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=35.191.0.0/16 \
             --target-tags=load-balanced-backend \
             --rules=tcp
         

  2. Create the `fw-allow-proxies` rule to allow the regional external Application Load Balancer's proxies to connect to your backends. Set `source-ranges` to the allocated ranges of your proxy-only subnet, for example, `10.129.0.0/23`.
         
         gcloud compute firewall-rules create fw-allow-proxies \
           --network=lb-network \
           --action=allow \
           --direction=ingress \
           --source-ranges=source-range \
           --target-tags=load-balanced-backend \
           --rules=tcp:80,tcp:443,tcp:8080
         




###  Terraform 

To create the firewall rules, use the [`google_compute_firewall`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall) resource.
    
    
    resource "google_compute_firewall" "default" {
      name = "fw-allow-health-check"
      allow {
        protocol = "tcp"
      }
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      priority      = 1000
      source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
      target_tags   = ["load-balanced-backend"]
    }
    
    
    resource "google_compute_firewall" "allow_proxy" {
      name = "fw-allow-proxies"
      allow {
        ports    = ["443"]
        protocol = "tcp"
      }
      allow {
        ports    = ["80"]
        protocol = "tcp"
      }
      allow {
        ports    = ["8080"]
        protocol = "tcp"
      }
      direction     = "INGRESS"
      network       = google_compute_network.default.id
      priority      = 1000
      source_ranges = ["10.129.0.0/23"]
      target_tags   = ["load-balanced-backend"]
    }

###  API 

Create the `fw-allow-health-check` firewall rule by making a `POST` request to the [`firewalls.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert) method, replacing PROJECT_ID with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    {
      "name": "fw-allow-health-check",
      "network": "projects/PROJECT-ID/global/networks/lb-network",
      "sourceRanges": [HEALTH_CHECK_RANGES],
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
    

Replace the following:

  * PROJECT_ID: the project ID

  * HEALTH_CHECK_RANGES: the comma-separated list of [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges), formatted as quoted strings (for example, "192.0.2.0/24", "198.51.100.0/24")




Create the `fw-allow-proxies` firewall rule to allow TCP traffic within the proxy subnet for the [`firewalls.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert) method, replacing PROJECT_ID with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    {
      "name": "fw-allow-proxies",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "sourceRanges": [
        "10.129.0.0/23"
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
    

## Configure a regional external Application Load Balancer with a VM-based service

This section shows the configuration required for services that run on Compute Engine VMs. Client VMs connect to the IP address and port that you configure in the forwarding rule. When your client applications send traffic to this IP address and port, their requests are forwarded to your backend virtual machines (VMs) according to your regional external Application Load Balancer's URL map.

The example on this page explicitly creates a reserved external IP address for the regional external Application Load Balancer's forwarding rule, rather than allowing an ephemeral external IP address to be allocated. As a best practice, we recommend reserving IP addresses for forwarding rules.

### Create a managed instance group backend

This section shows how to create a template and a managed instance group. The managed instance group provides VM instances running the backend servers of an example regional external Application Load Balancer. Traffic from clients is load balanced to these backend servers. For demonstration purposes, backends serve their own hostnames.

###  Console 

  1. Create an instance template. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

     1. Click **Create instance template**.
     2. For **Name** , enter `l7-xlb-backend-template`.
     3. Ensure that **Boot disk** is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     4. Click **Advanced options**.
     5. Click **Networking** and configure the following fields: 
        1. For **Network tags** , enter `load-balanced-backend`.
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
     3. For **Name** , enter `l7-xlb-backend-example`.
     4. For **Location** , select **Single zone**.
     5. For **Region** , select `us-west1`.
     6. For **Zone** , select `us-west1-a`.
     7. For **Instance template** , select `l7-xlb-backend-template`.
     8. For **Autoscaling mode** , select **On: add and remove instances to the group**.

Set **Minimum number of instances** to `2`, and set **Maximum number of instances** to `2` or more.

     9. Click **Create**.




###  gcloud 

The `gcloud` instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.

  1. Create a VM instance template with HTTP server with the [`gcloud compute instance-templates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) command.
         
         gcloud compute instance-templates create l7-xlb-backend-template \
         --region=us-west1 \
         --network=lb-network \
         --subnet=backend-subnet \
         --tags=load-balanced-backend \
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
         

  2. Create a managed instance group in the zone with the [`gcloud compute instance-groups managed create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) command.
         
         gcloud compute instance-groups managed create l7-xlb-backend-example \
             --zone=us-west1-a \
             --size=2 \
             --template=l7-xlb-backend-template
         




###  Terraform 

To create the instance template, use the [`google_compute_instance_template`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template) resource.
    
    
    resource "google_compute_instance_template" "default" {
      name = "l7-xlb-backend-template"
      disk {
        auto_delete  = true
        boot         = true
        device_name  = "persistent-disk-0"
        mode         = "READ_WRITE"
        source_image = "projects/debian-cloud/global/images/family/debian-12"
        type         = "PERSISTENT"
      }
      labels = {
        managed-by-cnrm = "true"
      }
      machine_type = "n1-standard-1"
      metadata = {
        startup-script = <<EOF
        #! /bin/bash
        sudo apt-get update
        sudo apt-get install apache2 -y
        sudo a2ensite default-ssl
        sudo a2enmod ssl
        vm_hostname="$(curl -H "Metadata-Flavor:Google" \
        http://169.254.169.254/computeMetadata/v1/instance/name)"
        sudo echo "Page served from: $vm_hostname" | \
        tee /var/www/html/index.html
        sudo systemctl restart apache2
        EOF
      }
      network_interface {
        access_config {
          network_tier = "PREMIUM"
        }
        network    = google_compute_network.default.id
        subnetwork = google_compute_subnetwork.default.id
      }
      region = "us-west1"
      scheduling {
        automatic_restart   = true
        on_host_maintenance = "MIGRATE"
        provisioning_model  = "STANDARD"
      }
      service_account {
        email  = "default"
        scopes = ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/pubsub", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/trace.append"]
      }
      tags = ["load-balanced-backend"]
    }

To create the managed instance group, use the [`google_compute_instance_group_manager`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager) resource.
    
    
    resource "google_compute_instance_group_manager" "default" {
      name = "l7-xlb-backend-example"
      zone = "us-west1-a"
      named_port {
        name = "http"
        port = 80
      }
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      base_instance_name = "vm"
      target_size        = 2
    }

###  API 

  1. Create the instance template with the [`instanceTemplates.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert) method, replacing `PROJECT_ID` with your project ID.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
         {
          "name":"l7-xlb-backend-template",
          "properties": {
            "machineType":"e2-standard-2",
            "tags": {
              "items":[
                "load-balanced-backend"
              ]
            },
            "metadata": {
              "kind":"compute#metadata",
              "items":[
                {
                  "key":"startup-script",
                  "value":"#! /bin/bash\napt-get update\napt-get install apache2 -y\na2ensite default-ssl\na2enmod ssl\nvm_hostname=\"$(curl -H \"Metadata-Flavor:Google\" \\\nhttp://metadata.google.internal/computeMetadata/v1/instance/name)\"\necho \"Page served from: $vm_hostname\" | \\\ntee /var/www/html/index.html\nsystemctl restart apache2"
                }
              ]
            },
            "networkInterfaces":[
              {
                "network":"projects/PROJECT_ID/global/networks/lb-network",
                "subnetwork":"regions/us-west1/subnetworks/backend-subnet",
                "accessConfigs":[
                  {
                    "type":"ONE_TO_ONE_NAT"
                  }
                ]
              }
            ],
            "disks": [
              {
                "index":0,
                "boot":true,
                "initializeParams": {
                  "sourceImage":"projects/debian-cloud/global/images/family/debian-12"
                },
                "autoDelete":true
              }
            ]
          }
         }
         

  2. Create a managed instance group in each zone with the [`instanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) method, replacing `PROJECT_ID` with your project ID.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/{zone}/instanceGroupManagers
         {
          "name": "l7-xlb-backend-example",
          "zone": "projects/PROJECT_ID/zones/us-west1-a",
          "instanceTemplate": "projects/PROJECT_ID/global/instanceTemplates/l7-xlb-backend-template",
          "baseInstanceName": "l7-xlb-backend-example",
          "targetSize": 2
         }
         




### Add a named port to the instance group

For your instance group, define an HTTP service and map a port name to the relevant port. The backend service of the load balancer forwards traffic to the named port.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of your instance group (in this example `l7-xlb-backend-example`).

  3. On the instance group's **Overview** page, click **Edit** edit.

  4. Click **Specify port name mapping**.

  5. Click **Add item**.

  6. For the port name, enter `http`. For the port number, enter `80`.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute instance-groups set-named-ports`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/set-named-ports) command.
    
    
    gcloud compute instance-groups set-named-ports l7-xlb-backend-example \
        --named-ports http:80 \
        --zone us-west1-a
    

###  Terraform 

The `named_port` attribute is included in the managed instance group sample.

### Reserve the load balancer's IP address

Reserve a static IP address for the load balancer.

###  Console 

  1. In the Google Cloud console, go to the **Reserve a static address** page.

[Go to Reserve a static address](https://console.cloud.google.com/networking/addresses/add)

  2. Choose a **Name** for the new address.

  3. For **Network Service Tier** , select **Standard**.

  4. For **IP version** , select **IPv4**. IPv6 addresses can only be global and can only be used with global load balancers.

  5. For **Type** , select **Regional**.

  6. For **Region** , select **us-west1**.

  7. Leave the **Attached to** option set to **None**. After you create the load balancer, this IP address will be attached to the load balancer's forwarding rule.

  8. Click **Reserve** to reserve the IP address.




###  gcloud 

  1. To reserve a static external IP address using `gcloud compute`, use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create ADDRESS_NAME  \
            --region=us-west1 \
            --network-tier=STANDARD
         

Replace the following:

     * `ADDRESS_NAME`: the name you want to call this address.
     * `REGION`: the region where you want to reserve this address. This region should be the same region as the load balancer. All regional IP addresses are `IPv4`.
  2. Use the [`compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to view the result:
         
         gcloud compute addresses describe ADDRESS_NAME
         




###  Terraform 

To reserve the IP address, use the [`google_compute_address`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_address) resource.
    
    
    resource "google_compute_address" "default" {
      name         = "address-name"
      address_type = "EXTERNAL"
      network_tier = "STANDARD"
      region       = "us-west1"
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

To create a regional IPv4 address, call the regional [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses

Your request body should contain the following:
    
    
    {
      "name": "ADDRESS_NAME"
      "networkTier": "STANDARD"
      "region": "us-west1"
    }

Replace the following:

  * `ADDRESS_NAME`: the name for the address
  * `REGION`: the name of the region for this request
  * `PROJECT_ID`: the project ID for this request



### Configure the load balancer

This example shows you how to create the following regional external Application Load Balancer resources:

  * HTTP health check
  * Backend service with a managed instance group as the backend
  * A [URL map](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management)
    * Make sure to refer to a regional URL map if a region is defined for the target HTTP(S) proxy. A regional URL map routes requests to a regional backend service based on rules that you define for the host and path of an incoming URL. A regional URL map can be referenced by a regional target proxy rule in the same region only.
  * SSL certificate (for HTTPS)
  * Target proxy
  * Forwarding rule



#### Proxy availability

Sometimes Google Cloud regions don't have enough proxy capacity for a new load balancer. If this happens, the Google Cloud console provides a proxy availability warning message when you are creating your load balancer. To resolve this issue, you can do one of the following:

  * Select a different region for your load balancer. This can be a practical option if you have backends in another region.
  * Select a VPC network that already has an allocated proxy-only subnet.
  * Wait for the capacity issue to be resolved.




###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for regional workloads** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. For the name of the load balancer, enter `regional-l7-xlb`.
  2. For **Region** , select `us-west1`.
  3. For **Network** , select `lb-network`.



**Reserve a proxy-only subnet**

**Note:** If you already configured the proxy-only subnet, the **Reserve subnet** button isn't displayed. You can skip this section and continue with the steps in Configure the frontend service.

For a regional external Application Load Balancer, reserve a proxy-only subnet:

  1. Click **Reserve subnet**.
  2. For **Name** , enter `proxy-only-subnet`.
  3. For **IP address range** , enter `10.129.0.0/23`.
  4. Click **Add**.



**Configure the frontend**

For HTTP:

  1. Click **Frontend configuration**.
  2. Set **Name** to `l7-xlb-forwarding-rule`.
  3. Set **Protocol** to `HTTP`.
  4. Set **Network service tier** to **Standard**.
  5. Set **Port** to `80`.
  6. Select the **IP address** that you created in [Reserving the load balancer's IP address](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb#reserve-ip).
  7. Click **Done**.



For HTTPS:

  1. Click **Frontend configuration**.
  2. In the **Name** field, enter `l7-xlb-forwarding-rule`.
  3. In the **Protocol** field, select `HTTPS (includes HTTP/2)`.
  4. Set **Network service tier** to **Standard**.
  5. Ensure that the **Port** is set to `443`.
  6. Select the **IP address** that you created in [Reserving the load balancer's IP address](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb#reserve-ip).
  7. To assign an SSL certificate to the target HTTPS proxy of the load balancer, you can either use a Compute Engine SSL certificate or a Certificate Manager certificate.

     1. To attach a Certificate Manager certificate to the target HTTPS proxy of the load balancer, in the **Choose certificate repository** section, select **Certificates**.

If you already have an existing Certificate Manager certificate to select, do the following:

        1. Click **Add Certificate**.
        2. Click **Select an existing certificate** and select the certificate from the list of certificates.
        3. Click **Select**.

After you select the new Certificate Manager certificate, it appears in the list of certificates.

To create a new Certificate Manager certificate, do the following:

        1. Click **Add Certificate**.
        2. Click **Create a new certificate**.
        3. To create a new certificate, follow the steps starting from _step 3_ as outlined in any one of the following configuration methods in the Certificate Manager documentation:

           * [Create a Google-managed certificate referencing the DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional#create-google-managed-certificate-dns-auth)

           * [Create a Google-managed certificate issued by your CA Service instance](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional#create-google-managed-certificate-issued-by-your-cas-instance)

           * [Upload a self-managed certificate to Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional#upload-self-managed-certificate-to-certificate-manager)

After you create the new Certificate Manager certificate, it appears in the list of certificates.

     2. To attach a Compute Engine SSL certificate to the target HTTPS proxy of the load balancer, in the **Choose certificate repository** section, select **Classic Certificates**.

        1. In the **Certificate** list, do the following: 
           1. If you already have a Compute Engine [self-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types) resource, select the primary SSL certificate.
           2. Click **Create a new certificate**. 
              1. In the **Name** field, enter `l7-xlb-cert`.
              2. In the appropriate fields, upload your PEM-formatted files: 
                 * **Certificate**
                 * **Private key**
              3. Click **Create**.
           3. Optional: To add certificates in addition to the primary SSL certificate: 
              1. Click **Add certificate**.
              2. If you already have a certificate, select it from the **Certificates** list.
              3. Optional: Click **Create a new certificate** and follow the instructions as specified in the previous step.
  8. Select an SSL policy from the **SSL policy** list. Optionally, to create an SSL policy, do the following:

     1. In the **SSL policy** list, select **Create a policy**.
     2. Enter a name for the SSL policy.
     3. Select a minimum TLS version. The default value is **TLS 1.0**.
     4. Select one of the pre-configured Google-managed profiles or select a **Custom** profile that lets you select SSL features individually. The **Enabled features** and **Disabled features** are displayed.
     5. Click **Save**.

If you have not created any SSL policies, a [default Google Cloud SSL policy](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#default-ssl-policy) is applied.

  9. Click **Done**.




**Configure the backend service**

  1. Click **Backend configuration**.
  2. From the **Create or select backend services** menu, select **Create a backend service**.
  3. Set the name of the backend service to `l7-xlb-backend-service`.
  4. For **Protocol** , select **HTTP**.
  5. For **Named Port** , enter `http`.
  6. Set **Backend type** to **Instance group**.
  7. In the **Health check** list, click **Create a health check** , and then enter the following information: 
     * In the **Name** field, enter `l7-xlb-basic-check`.
     * In the **Protocol** list, select **HTTP**.
     * In the **Port** field, enter `80`.
  8. Click **Create**.
  9. In the **New backend** section: 
     1. Set **Instance group** to `l7-xlb-backend-example`.
     2. Set **Port numbers** to `80`.
     3. Set **Balancing mode** to **Utilization**.
     4. Click **Done**.
  10. Click **Create**.



**Configure the routing rules**

  1. Click **Routing rules**.
  2. For **Mode** , select **Simple host and path rule**.
  3. Ensure that the `l7-xlb-backend-service` is the only backend service for any unmatched host and any unmatched path.



**Review the configuration**

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.



###  gcloud 

  1. Define the HTTP health check with the [`gcloud compute health-checks create http`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http) command.
         
         gcloud compute health-checks create http l7-xlb-basic-check \
            --region=us-west1 \
            --request-path='/' \
            --use-serving-port
         

  2. Define the backend service with the [`gcloud compute backend-services create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) command.
         
         gcloud compute backend-services create l7-xlb-backend-service \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --protocol=HTTP \
           --port-name=http \
           --health-checks=l7-xlb-basic-check \
           --health-checks-region=us-west1 \
           --region=us-west1
         

  3. Add backends to the backend service with the [`gcloud compute backend-services add-backend`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) command.
         
         gcloud compute backend-services add-backend l7-xlb-backend-service \
           --balancing-mode=UTILIZATION \
           --instance-group=l7-xlb-backend-example \
           --instance-group-zone=us-west1-a \
           --region=us-west1
         

  4. Create the URL map with the [`gcloud compute url-maps create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create) command.
         
         gcloud compute url-maps create regional-l7-xlb-map \
           --default-service=l7-xlb-backend-service \
           --region=us-west1
         

  5. Create the target proxy.

**For HTTP:**

For an HTTP load balancer, create the target proxy with the [`gcloud compute target-http-proxies create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create) command.
         
         gcloud compute target-http-proxies create l7-xlb-proxy \
           --url-map=regional-l7-xlb-map \
           --url-map-region=us-west1 \
           --region=us-west1
         

**For HTTPS:**

You can create either Compute Engine or Certificate Manager certificates. Use any of the following methods to create certificates using Certificate Manager:

     * Regional self-managed certificates. For information about creating and using regional self-managed certificates, see [Deploy a regional self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional). Certificate maps aren't supported.
     * Regional Google-managed certificates. Certificate maps aren't supported.

The following types of regional Google-managed certificates are supported by Certificate Manager:

       * Regional Google-managed certificates with per-project DNS authorization. For more information, see [Deploy a regional Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional).
       * Regional Google-managed (private) certificates with Certificate Authority Service. For more information, see [Deploy a regional Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional).

After you create certificates, attach the certificate directly to the target proxy.

     1. Assign your filepaths to variable names.
            
            export LB_CERT=path to PEM-formatted file
            
            
            export LB_PRIVATE_KEY=path to PEM-formatted file
            

     2. Create a regional SSL certificate using the [`gcloud compute ssl-certificates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command.
            
            gcloud compute ssl-certificates create l7-xlb-cert \
             --certificate=$LB_CERT \
             --private-key=$LB_PRIVATE_KEY \
             --region=us-west1
            

     3. Use the regional SSL certificate to create a target proxy with the [`gcloud compute target-https-proxies create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create) command.
            
            gcloud compute target-https-proxies create l7-xlb-proxy \
             --url-map=regional-l7-xlb-map \
             --region=us-west1 \
             --ssl-certificates=l7-xlb-cert
            

  6. Create the forwarding rule.

**For HTTP:**

Use the [`gcloud compute forwarding-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command with the correct flags.
         
         gcloud compute forwarding-rules create l7-xlb-forwarding-rule \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network-tier=STANDARD \
           --network=lb-network \
           --address=ADDRESS_NAME \
           --ports=80 \
           --region=us-west1 \
           --target-http-proxy=l7-xlb-proxy \
           --target-http-proxy-region=us-west1
         

**For HTTPS:**

Create the forwarding rule with the [`gcloud compute forwarding-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command with the correct flags.
         
         gcloud compute forwarding-rules create l7-xlb-forwarding-rule \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network-tier=STANDARD \
           --network=lb-network \
           --address=ADDRESS_NAME \
           --ports=443 \
           --region=us-west1 \
           --target-https-proxy=l7-xlb-proxy \
           --target-https-proxy-region=us-west1
         




###  Terraform 

To create the health check, use the [`google_compute_region_health_check`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_health_check) resource.
    
    
    resource "google_compute_region_health_check" "default" {
      name               = "l7-xlb-basic-check"
      check_interval_sec = 5
      healthy_threshold  = 2
      http_health_check {
        port_specification = "USE_SERVING_PORT"
        proxy_header       = "NONE"
        request_path       = "/"
      }
      region              = "us-west1"
      timeout_sec         = 5
      unhealthy_threshold = 2
    }

To create the backend service, use the [`google_compute_region_backend_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_backend_service) resource.
    
    
    resource "google_compute_region_backend_service" "default" {
      name                  = "l7-xlb-backend-service"
      region                = "us-west1"
      load_balancing_scheme = "EXTERNAL_MANAGED"
      health_checks         = [google_compute_region_health_check.default.id]
      protocol              = "HTTP"
      session_affinity      = "NONE"
      timeout_sec           = 30
      backend {
        group           = google_compute_instance_group_manager.default.instance_group
        balancing_mode  = "UTILIZATION"
        capacity_scaler = 1.0
      }
    }

To create the URL map, use the [`google_compute_region_url_map`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_url_map)resource.
    
    
    resource "google_compute_region_url_map" "default" {
      name            = "regional-l7-xlb-map"
      region          = "us-west1"
      default_service = google_compute_region_backend_service.default.id
    }

To create the target HTTP proxy, use the [`google_compute_region_target_http_proxy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_target_http_proxy) resource.
    
    
    resource "google_compute_region_target_http_proxy" "default" {
      name    = "l7-xlb-proxy"
      region  = "us-west1"
      url_map = google_compute_region_url_map.default.id
    }

To create the forwarding rule, use the [`google_compute_forwarding_rule`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_forwarding_rule) resource.
    
    
    resource "google_compute_forwarding_rule" "default" {
      name       = "l7-xlb-forwarding-rule"
      provider   = google-beta
      depends_on = [google_compute_subnetwork.proxy_only]
      region     = "us-west1"
    
      ip_protocol           = "TCP"
      load_balancing_scheme = "EXTERNAL_MANAGED"
      port_range            = "80"
      target                = google_compute_region_target_http_proxy.default.id
      network               = google_compute_network.default.id
      ip_address            = google_compute_address.default.id
      network_tier          = "STANDARD"
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Create the health check by making a `POST` request to the [`regionHealthChecks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/regions/{region}/healthChecks
    {
      "name": "l7-xlb-basic-check",
      "type": "HTTP",
      "httpHealthCheck": {
        "portSpecification": "USE_SERVING_PORT"
      }
    }
    

Create the regional backend service by making a `POST` request to the [`regionBackendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/regions/us-west1/backendServices
    {
      "name": "l7-xlb-backend-service",
      "backends": [
        {
          "group": "projects/<var>PROJECT_ID</var>/zones/us-west1-a/instanceGroups/l7-xlb-backend-example",
          "balancingMode": "UTILIZATION"
        }
      ],
      "healthChecks": [
        "projects/<var>PROJECT_ID</var>/regions/us-west1/healthChecks/l7-xlb-basic-check"
      ],
      "loadBalancingScheme": "EXTERNAL_MANAGED"
    }
    

Create the URL map by making a `POST` request to the [`regionUrlMaps.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/regions/us-west1/urlMaps
    {
      "name": "regional-l7-xlb-map",
      "defaultService": "projects/<var>PROJECT_ID</var>/regions/us-west1/backendServices/l7-xlb-backend-service"
    }
    

Create the target HTTP proxy by making a `POST` request to the [`regionTargetHttpProxies.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpProxies/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/targetHttpProxy
    {
      "name": "l7-xlb-proxy",
      "urlMap": "projects/PROJECT_ID/global/urlMaps/regional-l7-xlb-map",
      "region": "us-west1"
    }
    

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    {
      "name": "l7-xlb-forwarding-rule",
      "IPAddress": "10.1.2.99",
      "IPProtocol": "TCP",
      "portRange": "80-80",
      "target": "projects/PROJECT_ID/regions/us-west1/targetHttpProxies/l7-xlb-proxy",
      "loadBalancingScheme": "EXTERNAL_MANAGED",
      "network": "projects/PROJECT_ID/global/networks/lb-network",
      "networkTier": "STANDARD",
    }
    

## Connect your domain to your load balancer

After the load balancer is created, note the IP address that is associated with the load balancer—for example, `30.90.80.100`. To point your domain to your load balancer, create an `A` record by using your domain registration service. If you added multiple domains to your SSL certificate, you must add an `A` record for each one, all pointing to the load balancer's IP address. For example, to create `A` records for `www.example.com` and `example.com`, use the following:
    
    
    NAME                  TYPE     DATA
    www                   A        30.90.80.100
    @                     A        30.90.80.100
    

If you use Cloud DNS as your DNS provider, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Test the load balancer

Now that the load balancing service is running, you can send traffic to the forwarding rule and watch the traffic be dispersed to different instances.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/)

  2. Select the load balancer that you just created.
  3. In the **Backend** section, confirm that the VMs are healthy. The **Healthy** column should be populated, indicating that both VMs are healthy (`2/2`). If you see otherwise, first try reloading the page. It can take a few moments for the Google Cloud console to indicate that the VMs are healthy. If the backends do not appear healthy after a few minutes, review the firewall configuration and the network tag assigned to your backend VMs.
  4. After the Google Cloud console shows that the backend instances are healthy, you can test your load balancer using a web browser by going to `https://IP_ADDRESS` (or `http://IP_ADDRESS`). Replace `IP_ADDRESS` with the load balancer's IP address.
  5. If you used a self-signed certificate for testing HTTPS, your browser displays a warning. You must explicitly instruct your browser to accept a self-signed certificate.
  6. Your browser should render a page with content showing the name of the instance that served the page, along with its zone (for example, `Page served from: lb-backend-example-xxxx`). If your browser doesn't render this page, review the configuration settings in this guide.



###  gcloud 

Note the IPv4 address that was reserved:
    
    
    gcloud beta compute addresses describe ADDRESS_NAME \
        --format="get(address)" \
        --region="us-west1"
    

You can test your load balancer using a web browser by going to `https://IP_ADDRESS` (or `http://IP_ADDRESS`). Replace `IP_ADDRESS` with the load balancer's IP address.

If you used a self-signed certificate for testing HTTPS, your browser displays a warning. You must explicitly instruct your browser to accept a self-signed certificate.

Your browser should render a page with minimal information about the backend instance. If your browser doesn't render this page, review the configuration settings in this guide.

## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Enable session affinity

These procedures show you how to update a backend service for the example regional external Application Load Balancer so that the backend service uses generated cookie affinity, header field affinity, or HTTP cookie affinity.

When generated cookie affinity is enabled, the load balancer issues a cookie on the first request. For each subsequent request with the same cookie, the load balancer directs the request to the same backend VM or endpoint. For regional external Application Load Balancers, the cookie is named `GCILB`.

When header field affinity is enabled, the load balancer routes requests to backend VMs or endpoints in a NEG based on the value of the HTTP header named in the `--custom-request-header` flag. Header field affinity is only valid if the load balancing locality policy is either `RING_HASH` or `MAGLEV` and the backend service's consistent hash specifies the name of the HTTP header.

When HTTP cookie affinity is enabled, the load balancer routes requests to backend VMs or endpoints in a NEG, based on an HTTP cookie named in the `HTTP_COOKIE` flag with the optional `--affinity-cookie-ttl` flag. If the client does not provide the cookie in its HTTP request, the proxy generates the cookie and returns it to the client in a `Set-Cookie` header. HTTP cookie affinity is only valid if the load balancing locality policy is either `RING_HASH` or `MAGLEV` and the backend service's consistent hash specifies the HTTP cookie.

###  Console 

To enable or change session affinity for a backend service:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Select the load balancer that you just created.

  3. Click **Backends**.

  4. Click **l7-xlb-backend-service** (the name of the backend service you created for this example) and click **Edit**.

  5. On the **Backend service details** page, click **Advanced configuration**.

  6. For **Session affinity** , select the type of session affinity you want from the menu.

  7. Click **Update**.




###  gcloud 

Use the following commands to update the `l7-xlb-backend-service` backend service to different types of session affinity:
    
    
    gcloud compute backend-services update l7-xlb-backend-service \
        --session-affinity=GENERATED_COOKIE | HEADER_FIELD | HTTP_COOKIE | CLIENT_IP
        --region=us-west1
    

###  API 

To set session affinity, make a `PATCH` request to the [`regionBackendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/regions/us-west1/regionBackendServices/l7-xlb-backend-service
    {
      "sessionAffinity": <var>"GENERATED_COOKIE" | "HEADER_FIELD" | "HTTP_COOKIE" | "CLIENT_IP"</var>
    }
    

### Update client HTTP keepalive timeout

The load balancer created in the previous steps has been configured with a default value for the [client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#http-keepalive-timeout). 

To update the client HTTP keepalive timeout, use the following instructions.

### Console

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add).

  2. Click the name of the load balancer that you want to modify.
  3. Click edit**Edit**.
  4. Click **Frontend configuration**.
  5. Expand **Advanced features**. For **HTTP keepalive timeout** , enter a timeout value.
  6. Click **Update**.
  7. To review your changes, click **Review and finalize** , and then click **Update**.



### gcloud

For an HTTP load balancer, update the target HTTP proxy by using the [`gcloud compute target-http-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update).
    
    
          gcloud compute target-http-proxies update TARGET_HTTP_PROXY_NAME \
              --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
              --region=REGION
          

For an HTTPS load balancer, update the target HTTPS proxy by using the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update).
    
    
          gcloud compute target-https-proxies update TARGET_HTTP_PROXY_NAME \
              --http-keep-alive-timeout-sec=HTTP_KEEP_ALIVE_TIMEOUT_SEC \
              --region REGION
          

Replace the following:

  * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy.
  * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy.
  * `HTTP_KEEP_ALIVE_TIMEOUT_SEC`: the HTTP keepalive timeout value from 5 to 600 seconds.



### Enable IAP on the external Application Load Balancer

You can configure IAP to be enabled or disabled (default). If enabled, you must provide values for `oauth2-client-id` and `oauth2-client-secret`.

To enable IAP, update the backend service to include the `--iap=enabled` flag with the `oauth2-client-id` and `oauth2-client-secret`.

Optionally, you can [enable IAP](https://docs.cloud.google.com/iap/docs/enabling-compute-howto#enabling) for a Compute Engine resource by using the Google Cloud console, gcloud CLI, or API.

## What's next

  * [Convert Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-applb-dualstack)
  * [Traffic management overview for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional)
  * [Proxy-only subnets](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * [Using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#replacing-certificates)
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
