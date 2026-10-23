---
url: https://docs.cloud.google.com/load-balancing/docs/network/set-up-global-ext-passthrough-network-lb-multiple-protocols/
title: Set up a global external passthrough Network Load Balancer for multiple IP protocols \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:45.543169+00:00
---

# Set up a global external passthrough Network Load Balancer for multiple IP protocols  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/set-up-global-ext-passthrough-network-lb-multiple-protocols/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a global external passthrough Network Load Balancer for multiple IP protocols Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to create a global external passthrough Network Load Balancer to balance TCP, UDP, ESP, GRE, ICMP, and ICMPv6 traffic.

You can use such a configuration to:

  * Load-balance traffic that uses IP protocols other than TCP or UDP.

  * Serve multiple protocols with a single load balancer. For example, IPsec services typically handle some combination of ESP and UDP-based IKE and NAT-T traffic.




## Before you begin

Make sure that your setup meets the following prerequisites.

### Install the Google Cloud CLI

The instructions in this guide use the Google Cloud CLI to configure a global external passthrough Network Load Balancer. To install it, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

### Required roles

If you are the project creator, you are granted the [Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, the Owner role (`roles/owner`) or the Editor role (`roles/editor`) includes the permissions necessary to follow this document.

If you aren't the project creator, required permissions must be granted on the project to the appropriate [_principal_](https://docs.cloud.google.com/iam/docs/overview#principals). For example, a principal can be a Google Account (for end users) or a service account. 

To get the permissions that you need to to configure a global external passthrough Network Load Balancer with VM instance group backends, ask your administrator to grant you the following IAM roles on your project: 

  * Create a VPC network, subnet, and load balancing components: [Compute Network Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
  * Create firewall rules: [Compute Security Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`) 
  * Create VM instances: [Compute Instance Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles and permissions for Cloud Load Balancing, see [Roles and permissions](https://docs.cloud.google.com/load-balancing/docs/access-control). For more information about defining IAM policies with conditional grants for forwarding rules, see [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions).

## Setup overview

The following diagram shows two global external passthrough Network Load Balancers for the same IP address pair, each serving a different set of IP protocols and ports. To understand how a global external passthrough Network Load Balancer works, see the [Architecture](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#architecture) section in the overview guide.

**Note:** You must configure the components of a global external passthrough Network Load Balancer using gcloud or the REST API, and not the Google Cloud console.

  1. **`TCP` load balancer on port 80**

The forwarding rule of this load balancer is configured to capture only `TCP` traffic arriving specifically on port `80`.

     * When a packet arrives at a forwarding rule IP address, Google Cloud first checks if it is a `TCP` packet and if its destination port is exactly `80`.
     * If those conditions are met, this packet is captured by this specific `TCP` forwarding rule and routed to a backend based on the referenced backend service.
  2. **`L3_DEFAULT` load balancer for `TCP:8080` and `UDP` traffic**

The forwarding rule of this load balancer uses the `L3_DEFAULT` protocol and is configured to accept traffic on _all_ ports. In this setup, it acts as the _catch-all_ rule handling traffic that the first forwarding rule doesn't (like UDP, ICMP, and all TCP traffic other than port 80).

     * If a packet arrives at a forwarding rule IP address that doesn't match the specific TCP traffic arriving on port 80 rule (for example, if it is UDP traffic, an ICMP ping, or TCP traffic on port 8080 or 443), this packet is captured by the `L3_DEFAULT` forwarding rule.
     * Add a firewall rule to allow only `TCP:8080` and `UDP` traffic to reach the backend VM instances. So even though the `L3_DEFAULT` forwarding rule captures all IP protocol traffic on all ports, the firewall rule limits load balanced traffic to `TCP:8080` and `UDP` traffic.
     * The packet is then routed to a backend based on the referenced backend service.

Google Cloud prioritizes the more specific `TCP` rule on port `80` before letting the remaining traffic flow through to an `L3_DEFAULT` rule on the same IP address.

**Note:** Because `L3_DEFAULT` is a _catch-all_ rule, as a security best practice, you should configure ingress allow firewall rules that permit only the IP protocols and ports that you need.

[ ![Two global external passthrough Network Load Balancers sends traffic to VM instance group backends
    deployed in `us-west1` and `europe-west2` regions.](https://docs.cloud.google.com/static/load-balancing/images/global-netlb-set-up-multiple-protocols.svg)](https://docs.cloud.google.com/static/load-balancing/images/global-netlb-set-up-multiple-protocols.svg) Two global external passthrough Network Load Balancers for the same IP address pair, each serving a different set of IP protocols and ports (click to enlarge).

## Set up the network and subnets

The example uses a custom mode VPC network named `lb-network` with subnets in two different regions.

The following table summarizes the compatibility between load balancer traffic types, backend VM network interfaces, and VPC subnet stack types. Make sure that you are familiar with the [backend VM's network interface compatibility requirements with VPC subnets](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#setup-note) outlined in the global external passthrough Network Load Balancer architecture guide.

Load balancer traffic type | Stack type of backend VM network interface | Stack type of VPC subnet  
---|---|---  
IPv4 traffic only | `IPV4_ONLY` | `IPV4_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv6 traffic only | `IPV6_ONLY` | `IPV6_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv4 and IPv6 traffic | `IPV4_IPV6` | `IPV4_IPV6`  
  
The backends used in this example are located in the following regions and subnets. Although you can choose which IPv4 address range is configured on the subnet, Google Cloud automatically assigns a `/64` IPv6 address range to the entire subnet.

  * Region: `us-west1`

    * Subnet: `lb-subnet-us`, with primary IPv4 address range 10.1.2.0/24.
  * Region: `europe-west2`

    * Subnet: `lb-subnet-eu`, with primary IPv4 address range 10.1.3.0/24.



###  gcloud 

  1. Create a VPC network. In this example, the VPC network is named `lb-network`.
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. Within the VPC network (`lb-network`), create subnets in two regions.

**Create a subnet named`lb-subnet-us` for the backends in the `us-west1` region**.

To create an IPv4-only subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet-us \
             --stack-type=IPV4_ONLY \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=us-west1
         

To create a dual-stack subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet-us \
             --stack-type=IPV4_IPV6 \
             --ipv6-access-type=EXTERNAL \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=us-west1
         

To create an IPv6-only subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet-us \
             --stack-type=IPV6_ONLY \
             --ipv6-access-type=EXTERNAL \
             --network=lb-network \
             --region=us-west1
         

**Create a subnet named`lb-subnet-eu` for the backends in the `europe-west2` region**.

To create an IPv4-only subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet-eu \
             --stack-type=IPV4_ONLY \
             --network=lb-network \
             --range=10.1.3.0/24 \
             --region=europe-west2
         

To create dual-stack subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet-eu \
             --stack-type=IPV4_IPV6 \
             --ipv6-access-type=EXTERNAL \
             --network=lb-network \
             --range=10.1.3.0/24 \
             --region=europe-west2
         

To create an IPv6-only subnet, use the following command:
         
         gcloud compute networks subnets create lb-subnet-eu \
             --stack-type=IPV6_ONLY \
             --ipv6-access-type=EXTERNAL \
             --network=lb-network \
             --range=10.1.3.0/24 \
             --region=europe-west2
         




## Reserve global external IP addresses

Reserve two global external IP addresses, one from each availability group. As shown in the Setup overview, the two global external passthrough Network Load Balancers share the same IP address pair.

For a global external passthrough Network Load Balancer, the forwarding rule IP addresses are completely decoupled from VPC subnets. The IP addresses belong to Google-owned global external IP address pools or BYOIP [global external IPv4 public delegated prefixes](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#global-pdp) from distinct availability groups and are not associated with any VPC subnet.

When you configure an IPv6 forwarding rule, the forwarding rule IP addresses are allocated as `/96` prefixes.

###  gcloud 

**For IPv4 traffic** :

  1. Reserve the first global external IP address named `lb-ipv4-ag0` in availability group 0.
         
         gcloud beta compute addresses create lb-ipv4-ag0 \
             --global \
             --purpose=PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0 \
             --ip-version=IPV4
         

  2. Reserve the second global external IP address `lb-ipv4-ag1` in availability group 1.
         
         gcloud beta compute addresses create lb-ipv4-ag1 \
             --global \
             --purpose=PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1 \
             --ip-version=IPV4
         




**For IPv6 traffic** :

  1. Reserve the first global external IP address named `lb-ipv6-ag0` in availability group 0.
         
         gcloud beta compute addresses create lb-ipv6-ag0 \
             --global \
             --purpose=PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0 \
             --ip-version=IPV6
         

  2. Reserve the second global external IP address `lb-ipv6-ag1` in availability group 1.
         
         gcloud beta compute addresses create lb-ipv6-ag1 \
             --global \
             --purpose=PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1 \
             --ip-version=IPV6
         




## Configure a load balancer for TCP traffic on port 80

Follow the steps in this section to configure a global external passthrough Network Load Balancer that captures `TCP` traffic on port 80.

### Create firewall rules to only allow `TCP:80` traffic

To securely configure your production environment, you should create two separate firewall rules:

  * Health check firewall rule, which is configured to allow ingress traffic from:

    * Google's [health check IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges-passthrough), and
    * the IP protocol and ports that are configured in your health check
  * User traffic firewall rule, which is configured to allow ingress traffic from:

    * the specific client source IP ranges that need to access your load balancer, and
    * the IP protocol and ports that are configured in your forwarding rules



Note the following:

  * If your application is serving all internet users without any limitation, configure source IP ranges `0.0.0.0/0` for IPv4 traffic and `::/0` for IPv6 traffic.

  * If you configured your health check to probe your load balancing IP protocol and ports, you can configure a single firewall rule by merging the health check and user traffic firewall rules.




###  gcloud 

Create a firewall rule that allows TCP traffic from all source ranges to reach your backend VM instances on port 80. This port and protocol are used for both load balancing and health checking.

  * To allow all IPv4 traffic, run the following command:
        
        gcloud compute firewall-rules create allow-traffic-tcp-80-ipv4 \
              --network=lb-network \
              --target-tags=allow-traffic-tcp-80 \
              --allow=tcp:80 \
              --source-ranges=0.0.0.0/0
        

  * To allow all IPv6 traffic, run the following command:
        
        gcloud compute firewall-rules create allow-traffic-tcp-80-ipv6 \
              --network=lb-network \
              --target-tags=allow-traffic-tcp-80 \
              --allow=tcp:80 \
              --source-ranges=::/0
        




### Create backend VM instances

For this load balancing example, create managed instance groups in the `us-west1-a` and `europe-west2-a` zones. The managed instance group consists of VM instances that host the backend servers of the load balancer. For demonstration purposes, the backends are running the Apache server on port 80. In response to client requests, they serve their own hostnames.

The instance group references an instance template, which is used to create backend VMs.

The following table summarizes the compatibility between load balancer traffic types, backend VM network interfaces, and VPC subnet stack types. Make sure that you are familiar with the [backend VM's network interface compatibility requirements with VPC subnets](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#setup-note) outlined in the global external passthrough Network Load Balancer architecture guide.

Load balancer traffic type | Stack type of backend VM network interface | Stack type of VPC subnet  
---|---|---  
IPv4 traffic only | `IPV4_ONLY` | `IPV4_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv6 traffic only | `IPV6_ONLY` | `IPV6_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv4 and IPv6 traffic | `IPV4_IPV6` | `IPV4_IPV6`  
  
#### Create an instance template

In this example, you create [regional instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#regional_and_global_instance_templates) in the `us-west1` and `europe-west2` regions.

###  gcloud 

  1. **Create an instance template in the`us-west1` region**.

To create backend VMs with _IPv4-only_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-us-tcp-80 \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --stack-type=IPV4_ONLY \
             --tags=allow-traffic-tcp-80 \
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
         

To create backend VMs with _dual-stack_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-us-tcp-80 \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV4_IPV6 \
             --tags=allow-traffic-tcp-80 \
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
         
         gcloud compute instance-templates create ig-template-us-tcp-80 \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV6_ONLY \
             --tags=allow-traffic-tcp-80 \
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
         

  2. **Create an instance template in the`europe-west2` region**.

To create backend VMs with _IPv4-only_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-eu-tcp-80 \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --stack-type=IPV4_ONLY \
             --tags=allow-traffic-tcp-80 \
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
         

To create backend VMs with _dual-stack_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-eu-tcp-80 \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV4_IPV6 \
             --tags=allow-traffic-tcp-80 \
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
         
         gcloud compute instance-templates create ig-template-eu-tcp-80 \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV6_ONLY \
             --tags=allow-traffic-tcp-80 \
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
         




#### Create zonal managed instance groups

In this example, you create two zonal managed instance groups—one in the `us-west1-a` zone and the other in the `europe-west2-a` zone.

###  gcloud 

  1. Create a managed instance group in the `us-west1-a` zone.
         
         gcloud compute instance-groups managed create ig-us-tcp-80 \
           --template=ig-template-us-tcp-80 \
           --size=2 \
           --zone=us-west1-a
         

  2. Create a managed instance group in the `europe-west2-a` zone.
         
         gcloud compute instance-groups managed create ig-eu-tcp-80 \
           --template=ig-template-eu-tcp-80 \
           --size=2 \
           --zone=europe-west2-a
         




### Create the Cloud Load Balancing components

To create the Cloud Load Balancing components of a global external passthrough Network Load Balancer, do the following.

###  gcloud 

  1. Create a TCP health check configured to generate `TCP:80` probes.
         
         gcloud compute health-checks create tcp hc-tcp-80 \
           --global \
           --port=80
         

  2. Create a global backend service with the `EXTERNAL_PASSTHROUGH` load balancing scheme.
         
         gcloud beta compute backend-services create lb-backend-service-tcp-80 \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --health-checks=hc-tcp-80 \
           --global
         

  3. Add the instance groups as backends to the backend service.

Add the instance group in the `us-west1-a` zone to the backend service.
         
         gcloud beta compute backend-services add-backend lb-backend-service-tcp-80 \
             --instance-group=ig-us-tcp-80 \
             --instance-group-zone=us-west1-a \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.7 \
             --global
         

Add the instance group in the `europe-west2-a` zone to the backend service.
         
         gcloud beta compute backend-services add-backend lb-backend-service-tcp-80 \
             --instance-group=ig-eu-tcp-80 \
             --instance-group-zone=europe-west2-a \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.7 \
             --global
         

  4. Create a global forwarding rule to serve `TCP:80` traffic.

Make sure that the [IP version of your forwarding rule matches the stack type of your backend VM network interfaces](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#vm-compatibility-forwarding-rules).

The forwarding rule references IP addresses from each availability group.

**For IPv4 traffic** :
         
         gcloud beta compute forwarding-rules create lb-forwarding-rule-tcp-80-ipv4 \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --ip-protocol=TCP \
           --ports=80 \
           --backend-service=lb-backend-service-tcp-80 \
           --global \
           --ip-addresses=lb-ipv4-ag0,lb-ipv4-ag1
         

**For IPv6 traffic** :
         
         gcloud beta compute forwarding-rules create lb-forwarding-rule-tcp-80-ipv6 \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --ip-protocol=TCP \
           --ports=80 \
           --backend-service=lb-backend-service-tcp-80 \
           --global \
           --ip-addresses=lb-ipv6-ag0,lb-ipv6-ag1
         




## Configure a load balancer for `TCP:8080` and `UDP` traffic

Follow the steps in this section to configure a global external passthrough Network Load Balancer to serve `TCP:8080` and `UDP` traffic.

### Create firewall rules to only allow `TCP:8080` and UDP traffic

To securely configure your production environment, you should create two separate firewall rules:

  * Health check firewall rule, which is configured to allow ingress traffic from:

    * Google's [health check IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges-passthrough), and
    * the IP protocol and ports that are configured in your health check
  * User traffic firewall rule, which is configured to allow ingress traffic from:

    * the specific client source IP ranges that need to access your load balancer, and
    * the IP protocol and ports that are configured in your forwarding rules



Note the following:

  * If your application is serving all internet users without any limitation, configure source IP ranges `0.0.0.0/0` for IPv4 traffic and `::/0` for IPv6 traffic.

  * If you configured your health check to probe your load balancing IP protocol and ports, you can configure a single firewall rule by merging the health check and user traffic firewall rules.




###  gcloud 

Create a firewall rule that allows `TCP:8080` and `UDP` traffic from all source ranges to reach your backend VM instances. These protocols are used for load balancing, while TCP port 8080 is also used for health checking.

  1. To allow IPv4 traffic to reach backends in the `ig-us-l3-default` and `ig-eu-l3-default` instance groups, create the following firewall rule.
         
         gcloud compute firewall-rules create allow-traffic-l3-default-ipv4 \
             --network=lb-network \
             --target-tags=allow-traffic-l3-default \
             --allow=tcp:8080,udp \
             --source-ranges=0.0.0.0/0
         

  2. To allow IPv6 traffic to reach backends in the `ig-us-l3-default` and `ig-eu-l3-default` instance groups, create the following firewall rule.
         
         gcloud compute firewall-rules create allow-traffic-l3-default-ipv6 \
             --network=lb-network \
             --target-tags=allow-traffic-l3-default \
             --allow=tcp:8080,udp \
             --source-ranges=::/0
         




### Create backend VM instances

For this load balancing example, create managed instance groups in the `us-west1-a` and `europe-west2-a` zones. The managed instance group consists of VM instances that host the backend servers of the load balancer. For demonstration purposes, the backends serve their own hostnames. The startup script also configures the Apache server to listen on port 8080 instead of port 80.

The instance group references an instance template, which is used to create backend VMs.

The following table summarizes the compatibility between load balancer traffic types, backend VM network interfaces, and VPC subnet stack types. Make sure that you are familiar with the [backend VM's network interface compatibility requirements with VPC subnets](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#setup-note) outlined in the global external passthrough Network Load Balancer architecture guide.

Load balancer traffic type | Stack type of backend VM network interface | Stack type of VPC subnet  
---|---|---  
IPv4 traffic only | `IPV4_ONLY` | `IPV4_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv6 traffic only | `IPV6_ONLY` | `IPV6_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv4 and IPv6 traffic | `IPV4_IPV6` | `IPV4_IPV6`  
  
#### Create an instance template

In this example, you create [regional instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#regional_and_global_instance_templates) in the `us-west1` and `europe-west2` regions.

###  gcloud 

  1. **Create an instance template in the`us-west1` region**.

To create backend VMs with _IPv4-only_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-us-l3-default \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --stack-type=IPV4_ONLY \
             --tags=allow-traffic-l3-default \
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
         

To create backend VMs with _dual-stack_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-us-l3-default \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV4_IPV6 \
             --tags=allow-traffic-l3-default \
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
         
         gcloud compute instance-templates create ig-template-us-l3-default \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV6_ONLY \
             --tags=allow-traffic-l3-default \
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
         

  2. **Create an instance template in the`europe-west2` region**.

To create backend VMs with _IPv4-only_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-eu-l3-default \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --stack-type=IPV4_ONLY \
             --tags=allow-traffic-l3-default \
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
         

To create backend VMs with _dual-stack_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-eu-l3-default \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV4_IPV6 \
             --tags=allow-traffic-l3-default \
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
         
         gcloud compute instance-templates create ig-template-eu-l3-default \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV6_ONLY \
             --tags=allow-traffic-l3-default \
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
         




#### Create zonal managed instance groups

In this example, you create two zonal managed instance groups—one in the `us-west1-a` zone and the other in the `europe-west2-a` zone.

###  gcloud 

  1. Create a managed instance group in the `us-west1-a` zone.
         
         gcloud compute instance-groups managed create ig-us-l3-default \
           --template=ig-template-us-l3-default \
           --size=2 \
           --zone=us-west1-a
         

  2. Create a managed instance group in the `europe-west2-a` zone.
         
         gcloud compute instance-groups managed create ig-eu-l3-default \
           --template=ig-template-eu-l3-default \
           --size=2 \
           --zone=europe-west2-a
         




### Create the Cloud Load Balancing components

To create the Cloud Load Balancing components of a global external passthrough Network Load Balancer, do the following.

###  gcloud 

  1. Create a TCP health check configured to generate `TCP:8080` probes.
         
         gcloud compute health-checks create tcp hc-tcp-8080 \
           --global \
           --port=8080
         

  2. Create a global backend service with the `EXTERNAL_PASSTHROUGH` load balancing scheme.
         
         gcloud beta compute backend-services create lb-backend-service-l3-default \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --health-checks=hc-tcp-8080 \
           --global
         

  3. Add the instance groups as backends to the backend service.

Add the instance group in the `us-west1-a` zone to the backend service.
         
         gcloud beta compute backend-services add-backend lb-backend-service-l3-default \
             --instance-group=ig-us-l3-default \
             --instance-group-zone=us-west1-a \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.7 \
             --global
         

Add the instance group in the `europe-west2-a` zone to the backend service.
         
         gcloud beta compute backend-services add-backend lb-backend-service-l3-default \
             --instance-group=ig-eu-l3-default \
             --instance-group-zone=europe-west2-a \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.7 \
             --global
         

  4. Create a global forwarding rule with its `ip-protocol` field set to `L3_DEFAULT` to handle all IP protocol traffic (TCP traffic other than port 80, UDP, ESP, and ICMP). You must create two forwarding rules to handle both IPv4 and IPv6 traffic.

Make sure that the [IP version of your forwarding rule matches the stack type of your backend VM network interfaces](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#vm-compatibility-forwarding-rules).

The forwarding rule references IP addresses from each availability group.

**Note:** Even though the `L3_DEFAULT` forwarding rule captures all IP protocol traffic on all ports, the firewall rule allows only `TCP:8080` and `UDP` traffic to reach the backend VM instances.

**For IPv4 traffic** :
         
         gcloud beta compute forwarding-rules create lb-forwarding-rule-l3-default-ipv4 \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --ip-protocol=L3_DEFAULT \
           --ports=all \
           --backend-service=lb-backend-service-l3-default \
           --global \
           --ip-addresses=lb-ipv4-ag0,lb-ipv4-ag1
         

**For IPv6 traffic** :
         
         gcloud beta compute forwarding-rules create lb-forwarding-rule-l3-default-ipv6 \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --ip-protocol=L3_DEFAULT \
           --ports=all \
           --backend-service=lb-backend-service-l3-default \
           --global \
           --ip-addresses=lb-ipv6-ag0,lb-ipv6-ag1
         




## Test the load balancer

Now that the load balancing service is configured, you can start sending traffic to the load balancer's external IP addresses and watch traffic get distributed to the backend instances.

### Get the external IP addresses of the load balancer

  1. Get the reserved IP addresses attached to the forwarding rule. The forwarding rule for both load balancers use the same pair of IP addresses, so you can use either `lb-forwarding-rule-tcp-80-ipv4` or `lb-forwarding-rule-l3-default-ipv4` to view the external IP addresses.
         
         gcloud compute forwarding-rules describe lb-forwarding-rule-tcp-80-ipv4 \
               --global
         

This returns two IP addresses, one for each availability group. These IP addresses are referred to as `IP_ADDRESS_AVAILABILITY_GROUP_0` and `IP_ADDRESS_AVAILABILITY_GROUP_1` in the following steps.




### Send traffic to the load balancer

This procedure sends external traffic to the load balancer. Run the following tests to check that TCP traffic on port 80 is being load-balanced by the `ig-us-tcp-80` or `ig-eu-tcp-80` instance groups while all other traffic (`TCP:8080` and `UDP`) is being load-balanced by the `ig-us-l3-default` or `ig-eu-l3-default` instance groups.

#### Verifying behavior with TCP requests on port 80

  1. Make web requests (over TCP on port 80) to the load balancer using `curl` to contact its IP address.

     * From clients with IPv4 connectivity, run the following command:
           
           while true; do curl -m1 IP_ADDRESS_AVAILABILITY_GROUP_0; done
           

Note the text returned by the `curl` command. The text displays the name of the backend VM generating the response—for example, `Page served from: VM_NAME`. Responses come only from instances in the `ig-us-tcp-80` or `ig-eu-tcp-80` instance groups.

This shows that TCP traffic sent to the load balancer's IP address on port 80 is handled by the `TCP` forwarding rule.




#### Verifying behavior with TCP requests on port 8080

Make web requests (over TCP on port 8080) to the load balancer using `curl` to contact its IP address.

  * From clients with IPv4 connectivity, run the following command:
        
        while true; do curl -m1 IP_ADDRESS_AVAILABILITY_GROUP_0:8080; done
        

Note the text returned by the `curl` command. Responses come only from instances in the `ig-us-l3-default` or `ig-eu-l3-default` instance groups.

This shows that TCP traffic sent to the load balancer's IP address on port 8080 is handled by the `L3_DEFAULT` forwarding rule.




### Check local routing table for the load balancer's IP addresses

The [local routing tables of the backend VMs](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#local-routing) contain the IP addresses of the global external passthrough Network Load Balancer.

To check the local routes on the backend VM, connect to your backend VM using [SSH](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) and run the following command:
    
    
      ip route list table local
    

The output is as follows:
    
    
    local 10.1.2.5 dev ens4 proto kernel scope host src 10.1.2.5
    local 127.0.0.0/8 dev lo proto kernel scope host src 127.0.0.1
    local 127.0.0.1 dev lo proto kernel scope host src 127.0.0.1
    broadcast 127.255.255.255 dev lo proto kernel scope link src 127.0.0.1
    local 136.124.69.214 dev ens4 proto 66 scope host
    local 136.124.83.205 dev ens4 proto 66 scope host
    

In the preceding example, `136.124.69.214` and `136.124.83.205` are the IP addresses assigned to the load balancer's forwarding rule. The line entries `local 136.124.69.214 dev ens4 proto 66 scope host` and `local 136.124.83.205 dev ens4 proto 66 scope host` in the local routing table of the VM allow packets addressed to the IP addresses of the load balancer to be accepted by the backend. The Google Cloud [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) is responsible for adding this entry.

The local routing table entry on the backend VM accepts the packet for local host delivery, where the network stack delivers it to the listening application. The response packets from the application are then sent directly to the client.

Note that the load balancer's IP address is not actually configured on the VM's network interface. To verify this, run the following command:
    
    
      ip addr list
    

The output is as follows. The IP addresses (`136.124.69.214` and `136.124.83.205`) appear in the local routing table but are not configured on the network interface.
    
    
    1: lo:  mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host noprefixroute
           valid_lft forever preferred_lft forever
    2: ens4:  mtu 1460 qdisc fq_codel state UP group default qlen 1000
        link/ether 42:01:0a:01:02:0d brd ff:ff:ff:ff:ff:ff
        altname enp0s4
        inet 10.1.2.13/32 metric 100 scope global dynamic ens4
           valid_lft 84283sec preferred_lft 84283sec
        inet6 fe80::4001:aff:fe01:20d/64 scope link
           valid_lft forever preferred_lft forever
    

## What's next

  * [Cloud Load Balancing API and gcloud CLI references](https://docs.cloud.google.com/load-balancing/docs/apis)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
