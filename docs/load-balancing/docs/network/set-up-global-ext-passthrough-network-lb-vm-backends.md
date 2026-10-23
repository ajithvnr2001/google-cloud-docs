---
url: https://docs.cloud.google.com/load-balancing/docs/network/set-up-global-ext-passthrough-network-lb-vm-backends/
title: Set up a global external passthrough Network Load Balancer with VM instance group backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:36.514457+00:00
---

# Set up a global external passthrough Network Load Balancer with VM instance group backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/set-up-global-ext-passthrough-network-lb-vm-backends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a global external passthrough Network Load Balancer with VM instance group backends Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to create a global external passthrough Network Load Balancer to balance traffic among VM instance group backends deployed in multiple regions.

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

The following diagram shows a global external passthrough Network Load Balancer with VM instance group backends deployed in `us-west1` and `europe-west2` regions.

In this example, you configure a single forwarding rule with two global external IP addresses, one from each availability group. To understand how a global external passthrough Network Load Balancer works, see the [Architecture](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#architecture) section in the overview guide.

**Note:** You must configure the components of a global external passthrough Network Load Balancer using gcloud or the REST API, and not the Google Cloud console.[ ![A global external passthrough Network Load Balancer sends traffic to VM instance group backends
    deployed in `us-west1` and `europe-west2` regions.](https://docs.cloud.google.com/static/load-balancing/images/global-netlb-set-up-vm-ig-backends.svg)](https://docs.cloud.google.com/static/load-balancing/images/global-netlb-set-up-vm-ig-backends.svg) Distributing traffic to VM instance group backends using a global external passthrough Network Load Balancer (click to enlarge).

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

    * Subnet: `lb-subnet-us`, with primary IPv4 address range `10.1.2.0/24`.
  * Region: `europe-west2`

    * Subnet: `lb-subnet-eu`, with primary IPv4 address range `10.1.3.0/24`.



###  gcloud 

  1. Create a VPC network. In this example, the VPC network is named `lb-network`.
         
         gcloud compute networks create lb-network \
             --subnet-mode=custom
         

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
         

To create a dual-stack subnet, use the following command:
         
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
         




## Configure firewall rules

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

  * Create a firewall rule that allows TCP traffic from all source ranges to reach your backend VM instances on port 80. This port and protocol are used for both load balancing and health checking.

    * To allow all IPv4 traffic, run the following command:
    
    gcloud compute firewall-rules create firewall-allow-traffic-ipv4 \
          --network=lb-network \
          --target-tags=allow-traffic \
          --allow=tcp:80 \
          --source-ranges=0.0.0.0/0
    

    * To allow all IPv6 traffic, run the following command:
    
    gcloud compute firewall-rules create firewall-allow-traffic-ipv6 \
          --network=lb-network \
          --target-tags=allow-traffic \
          --allow=tcp:80 \
          --source-ranges=::/0
    




## Create the backend VM instances

For this load balancing scenario, you create two Compute Engine zonal managed instance groups in the `us-west1-a` and `europe-west2-a` zones. The managed instance group consists of VM instances that host the backend servers of the load balancer. For demonstration purposes, the backends serve their own hostnames.

The instance group references an instance template, which is used to create backend VMs.

The following table summarizes the compatibility between load balancer traffic types, backend VM network interfaces, and VPC subnet stack types. Make sure that you are familiar with the [backend VM's network interface compatibility requirements with VPC subnets](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#setup-note) outlined in the global external passthrough Network Load Balancer architecture guide.

Load balancer traffic type | Stack type of backend VM network interface | Stack type of VPC subnet  
---|---|---  
IPv4 traffic only | `IPV4_ONLY` | `IPV4_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv6 traffic only | `IPV6_ONLY` | `IPV6_ONLY` or `IPV4_IPV6`  
`IPV4_IPV6` | `IPV4_IPV6`  
IPv4 and IPv6 traffic | `IPV4_IPV6` | `IPV4_IPV6`  
  
### Create an instance template

In this example, you create [regional instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#regional_and_global_instance_templates) in the `us-west1` and `europe-west2` regions.

###  gcloud 

  1. **Create an instance template in the`us-west1` region**.

To create backend VMs with _IPv4-only_ network interfaces, use the following command.
         
         gcloud compute instance-templates create ig-template-us \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --stack-type=IPV4_ONLY \
             --tags=allow-traffic \
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
         
         gcloud compute instance-templates create ig-template-us \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV4_IPV6 \
             --tags=allow-traffic \
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
         
         gcloud compute instance-templates create ig-template-us \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet-us \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV6_ONLY \
             --tags=allow-traffic \
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
         
         gcloud compute instance-templates create ig-template-eu \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --stack-type=IPV4_ONLY \
             --tags=allow-traffic \
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
         
         gcloud compute instance-templates create ig-template-eu \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV4_IPV6 \
             --tags=allow-traffic \
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
         
         gcloud compute instance-templates create ig-template-eu \
             --region=europe-west2 \
             --network=lb-network \
             --subnet=lb-subnet-eu \
             --ipv6-network-tier=PREMIUM \
             --stack-type=IPV6_ONLY \
             --tags=allow-traffic \
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
         




### Create zonal managed instance groups

In this example, you create two zonal managed instance groups—one in the `us-west1-a` zone and the other `europe-west2-a` zones.

###  gcloud 

  1. Create a managed instance group in the `us-west1-a` zone.
         
         gcloud compute instance-groups managed create mig-us \
           --template=ig-template-us \
           --size=2 \
           --zone=us-west1-a
         

  2. Create a managed instance group in the `europe-west2-a` zone.
         
         gcloud compute instance-groups managed create mig-eu \
           --template=ig-template-eu \
           --size=2 \
           --zone=europe-west2-a
         




## Reserve global external IP addresses

A global external passthrough Network Load Balancer requires two global external IP addresses, one from each availability group. These two IP addresses are then attached to the forwarding rule of the load balancer.

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
         




## Configure the load balancer

Setting up a global external passthrough Network Load Balancer involves creating a health check, a backend service, and a forwarding rule.

###  gcloud 

  1. Create a TCP health check configured to generate `TCP:80` probes.
         
         gcloud compute health-checks create tcp hc-tcp-80 \
           --global \
           --port=80
         

  2. Create a global backend service with the `EXTERNAL_PASSTHROUGH` load balancing scheme.
         
         gcloud beta compute backend-services create lb-backend-service \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --health-checks=hc-tcp-80 \
           --global
         

  3. Add the instance groups as backends to the backend service.

Add the instance group in the `us-west1-a` region to the backend service.
         
         gcloud beta compute backend-services add-backend lb-backend-service \
             --instance-group=mig-us \
             --instance-group-zone=us-west1-a \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.7 \
             --global
         

Add the instance group in the `europe-west2-a` region to the backend service.
         
         gcloud beta compute backend-services add-backend lb-backend-service \
             --instance-group=mig-eu \
             --instance-group-zone=europe-west2-a \
             --balancing-mode=UTILIZATION \
             --max-utilization=0.7 \
             --global
         

  4. Create a global forwarding rule to serve `TCP:80` traffic. You must create two forwarding rules to handle both IPv4 and IPv6 traffic.

Make sure that the [IP version of your forwarding rule matches the stack type of your backend VM network interfaces](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#vm-compatibility-forwarding-rules).

The forwarding rule references IP addresses from each availability group.

**For IPv4 traffic** :
         
         gcloud beta compute forwarding-rules create lb-forwarding-rule-ipv4 \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --ip-protocol=TCP \
           --ports=80 \
           --backend-service=lb-backend-service \
           --global \
           --ip-addresses=lb-ipv4-ag0,lb-ipv4-ag1
         

**For IPv6 traffic** :
         
         gcloud beta compute forwarding-rules create lb-forwarding-rule-ipv6 \
           --load-balancing-scheme=EXTERNAL_PASSTHROUGH \
           --ip-protocol=TCP \
           --ports=80 \
           --backend-service=lb-backend-service \
           --global \
           --ip-addresses=lb-ipv6-ag0,lb-ipv6-ag1
         




## Test the load balancer

  1. Get the reserved IP addresses attached to the forwarding rule.
         
         gcloud beta compute forwarding-rules describe lb-forwarding-rule-ipv4 \
               --global
         

This returns two IP addresses, one for each availability group. These IP addresses are referred to as `IP_ADDRESS_AVAILABILITY_GROUP_0` and `IP_ADDRESS_AVAILABILITY_GROUP_1`.

  2. Send traffic to either of the IP addresses.
         
         curl http://IP_ADDRESS_AVAILABILITY_GROUP_0
         
         
         curl http://IP_ADDRESS_AVAILABILITY_GROUP_1
         




You should see responses from the backend VMs in different regions depending on your location and backend health.

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
    

### View child forwarding rules

When a forwarding rule is created for a global external passthrough Network Load Balancer, Google Cloud generates two read-only child forwarding rules, one for each availability group, to ensure high availability.

To view the child forwarding rules of your forwarding rule, run the following command:
    
    
      gcloud beta compute forwarding-rules list
    

This command lists all the forwarding rules in your project. The read-only child forwarding rules have `-ag0` and `-ag1` appended to the parent forwarding rule name.

[Monitoring metrics](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#metrics-resources) can't be queried or filtered by using the parent global forwarding rule that you create, but instead queried and filtered using the _child_ forwarding rules. This is because each child forwarding rule in its availability group implements the load-balanced traffic and health checks.

## Additional configuration options

This section expands on the configuration example to provide instructions about how to further customize your global external passthrough Network Load Balancer. These tasks are optional. You can perform them in any order.

### Configure session affinity

By default, the backend service of the load balancer is created with a session affinity value set to `NONE`. This section shows you how to update the backend service to change the load balancer's session affinity setting.

###  gcloud 

Use the following [`gcloud beta compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/backend-services/update) to update session affinity for the backend service:
    
    
    gcloud beta compute backend-services update BACKEND_SERVICE \
        --global \
        --session-affinity=SESSION_AFFINITY_OPTION
    

Replace the following:

  * `BACKEND_SERVICE`: the backend service that you're updating
  * `SESSION_AFFINITY_OPTION`: the session affinity option that you want to set



### Change the connection persistence behavior

By default, the connection persistence behavior of a load balancer is set to `DEFAULT_FOR_PROTOCOL`. This section shows you how to change the connection persistence behavior of the load balancer.

###  gcloud 

Use the following [`gcloud beta compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/backend-services/update) to update the connection persistence behavior:
    
    
    gcloud beta compute backend-services update BACKEND_SERVICE \
        --global \
        --connection-persistence-on-unhealthy-backends=CONNECTION_PERSISTENCE_BEHAVIOR
    

Replace the following:

  * `BACKEND_SERVICE`: the backend service that you're updating
  * `CONNECTION_PERSISTENCE_BEHAVIOR`: the connection persistence behavior when backends are unhealthy. 



## What's next

  * [Cloud Load Balancing API and gcloud CLI references](https://docs.cloud.google.com/load-balancing/docs/apis)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
