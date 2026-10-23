---
url: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull/
title: Set up Packet Mirroring for ULL VPC networks \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:34.491529+00:00
---

# Set up Packet Mirroring for ULL VPC networks  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Packet Mirroring for ULL VPC networks

**Preview — ULL Packet Mirroring for exchange participants**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to set up Packet Mirroring for Ultra Low Latency (ULL) Virtual Private Cloud (VPC) networks and validate that traffic mirrors correctly to your collector appliances.

## Before you begin

Verify that the Google Cloud project that hosts your Packet Mirroring resources is on the allowlist for the ULL VPC network service in the specific location where you want to mirror traffic. To initiate the allowlist process, contact your Google Cloud account team.

If your projects are protected by VPC Service Controls, see [Configure VPC Service Controls](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/configure-vpc-service-controls) for instructions on setting up required service perimeters and egress rules.

### Roles

To create, view, or delete mirroring resources, ask your administrator to grant you the following Identity and Access Management (IAM) roles on your project:

Task | Required role  
---|---  
Manage network resources like forwarding rules and instance groups | Network Admin (`roles/compute.networkAdmin`)  
Create a collector for the in-scope `UllMirroringEngine` | Engine User (`roles/networksecurity. ullMirroringEngineUser`)  
Manage the lifecycle of `UllMirroringCollector` resources | Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)  
View details of `UllMirroringCollector` resources | Collector Viewer (`roles/networksecurity. ullMirroringCollectorViewer`)  
  
The service account or user creating the `UllMirroringCollector` also needs the `networksecurity.ullMirroringEngines.use` permission on the engine's project in order to bind to it. This permission is granted through the `roles/networksecurity.ullMirroringEngineUser` role.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create ULL Mirroring collector resources

To receive mirrored traffic, create ULL Mirroring collector instances and an internal passthrough Network Load Balancer. The ULL Mirroring collector references the exchange operator's ULL Mirroring engine and the forwarding rule for the internal passthrough Network Load Balancer. The load balancer sends the traffic to your collector instances. The collector receives mirrored traffic from VPC networks in the same project where you create the collector instance. The collector appliance (`compute.Instance`) does not need to be in the same project as the `UllMirroringCollector`.

To create the collector instances, the internal passthrough Network Load Balancer, and the forwarding rule, follow these steps:

  1. Ask the exchange operator to grant you the `networksecurity.ullMirroringEngines.use` permission in the project that contains the `UllMirroringEngine` resource. 
  2. Create one or more collector instances in the collector project. For more information, see Create a ULL Packet Mirroring collector. 
     * Verify that the VPC network used by the collector instances has an MTU of at least 1808 bytes.
     * Install software capable of receiving and analyzing GENEVE-encapsulated traffic.
  3. Add the collector instances to an instance group.
  4. Create a health check for your collector application.
  5. Create a regional backend service for the internal passthrough Network Load Balancer with the protocol set to `UDP`.
  6. Create the forwarding rule for the internal passthrough Network Load Balancer. For more information, see Create an internal load balancer for Packet Mirroring.

When you configure the forwarding rule, specify the `--is-mirroring-collector` flag, set `--ip-protocol` to `UDP`, and set `--ports` to `6081`.




### Create an internal load balancer for Packet Mirroring

To enable Packet Mirroring, use an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal). The internal passthrough Network Load Balancer must meet the following requirements:

  * The internal passthrough Network Load Balancer's forwarding rule must have Packet Mirroring enabled when you create the rule. You can't change this status after you create the rule. While the forwarding rule only accepts IPv4 traffic, GENEVE-encapsulated mirrored traffic can be IPv4 or IPv6.
  * The internal passthrough Network Load Balancer and the collector instances receiving mirrored traffic must be in the same region.
  * The internal passthrough Network Load Balancer's backend service uses a [session affinity](https://docs.cloud.google.com/load-balancing/docs/internal#session_affinity) of `NONE` (5-tuple hash).
  * Disable the [backend subsetting](https://docs.cloud.google.com/load-balancing/docs/internal#backend_subsetting) of the internal passthrough Network Load Balancer's backend service.



If your collector instances don't respond to the health check you configure for your backend service, the health check might fail. However, packet mirroring continues in this scenario.

To create an internal passthrough Network Load Balancer for Packet Mirroring, follow these steps.

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. Click **Configure**.



#### Basic configuration

  1. On the **Create internal passthrough Network Load Balancer** page, enter the following information:

     1. For **Load balancer name** , enter a name.
     2. For **Region** , select the region of the collector instances where you want to mirror packets.
     3. For **Network** , select the regular VPC network where you want to mirror packets.



#### Configure the backends

  1. Click **Backend configuration**.
  2. For **Backend type** , select **Instance group**.
  3. From the **Protocol** list, select **UDP**.
  4. In the **New Backend** section, from **Instance group** list, select the instance group to forward packets to.
  5. In the **New Backend** section, complete the following steps: 
     1. Select the **IP stack type**.
     2. From **Instance group** list, select the instance group to forward packets to.
     3. Click **Done**.



When you use the Google Cloud console to create your load balancer, the health check is global. To create a regional health check, use the Google Cloud CLI or the API.

#### Configure the frontend

  1. On the **Create internal passthrough Network Load Balancer** page, click **Frontend configuration**.
  2. In the **New Frontend IP and port** section, complete the following steps: 
     1. For **Name** , enter a name.
     2. For **Subnetwork** , select a subnetwork in the same region as the collector instances that receive the mirrored traffic.
     3. For **Ports** , select **Single** and then in **Port numbers** , enter `6081`.
     4. Click **Advanced configurations** and select **Enable this load balancer for packet mirroring**.
     5. Click **Done**.



#### Review the configuration

  1. On the **Create internal passthrough Network Load Balancer** page, click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Click **Create**.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to an instance group:
         
         gcloud compute health-checks create http HEALTH_CHECK_NAME \
             --region REGION \
             --port PORT
         

Replace the following:

     * `HEALTH_CHECK_NAME`: the name of the health check.
     * `REGION`: the region of the collector instances for which you want to mirror packets.
     * `PORT`: The port number that the health check monitors. If none is specified, the default port of `80` is used.
  2. Create a backend service for HTTP traffic:
         
         gcloud compute backend-services create COLLECTOR_BACKEND_SERVICE \
             --region=REGION \
             --health-checks-region=REGION \
             --health-checks=HEALTH_CHECK_NAME \
             --load-balancing-scheme=internal \
             --protocol=udp
         

Replace the following:

     * `COLLECTOR_BACKEND_SERVICE`: the name of the backend service.
     * `REGION`: the region of the collector instances where you want to mirror packets.
     * `HEALTH_CHECK_NAME`: the name of the health check.
  3. Add an instance group to the backend service:
         
         gcloud compute backend-services add-backend COLLECTOR_BACKEND_SERVICE \
             --region=REGION \
             --instance-group=INSTANCE_GROUP \
             --instance-group-zone=LOCATION
         

Replace the following:

     * `COLLECTOR_BACKEND_SERVICE`: the name of the backend service.
     * `REGION`: the region of the instance group.
     * `INSTANCE_GROUP`: the name of the instance group.
     * `LOCATION`: the location of the instance group.
  4. Create a forwarding rule for the backend service:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
             --region REGION \
             --load-balancing-scheme=internal \
             --network NETWORK \
             --subnet SUBNET \
             --address=ADDRESS \
             --ports=6081 \
             --ip-protocol=UDP \
             --backend-service COLLECTOR_BACKEND_SERVICE \
             --backend-service-region BACKEND_REGION \
             --is-mirroring-collector
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule.
     * `REGION`: the region for the forwarding rule.
     * `NETWORK`: the regular VPC network for the forwarding rule.
     * `SUBNET`: a subnetwork in the region of the collector instances where you want to mirror packets.
     * `ADDRESS`: the IP address that the forwarding rule serves. When the mirrored traffic reaches the collector instances, this value becomes the destination IP address.
     * `COLLECTOR_BACKEND_SERVICE`: the backend service for the load balancer.
     * `BACKEND_REGION`: the region of the backend service.



## Create and manage ULL Packet Mirroring collectors

The ULL Packet Mirroring collector is the zonal resource that represents the destination for mirrored traffic.

### Create a ULL Packet Mirroring collector instance

The ULL Mirroring collector instance must reside in the same location as the ULL Mirroring engine.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectors.create`
  * `networksecurity.ullMirroringEngines.use` (required on the engine's project)



**Roles**

  * Engine Admin (`roles/networksecurity.ullMirroringEngineAdmin`)
  * Engine User (`roles/networksecurity.ullMirroringEngineUser`)
  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)



###  gcloud 

To create the ULL Mirroring collector, use the `gcloud network-security ull-mirroring-collectors create` command in the collector project.
    
    
    gcloud network-security ull-mirroring-collectors create COLLECTOR_NAME \
        --location=ULL_LOCATION \
        --project=COLLECTOR_PROJECT \
        --engine="projects/ULL_PROJECT/locations/ULL_LOCATION/ullMirroringEngines/ENGINE_NAME" \
        --forwarding-rule="projects/COLLECTOR_PROJECT/regions/COLLECTOR_REGION/forwardingRules/FW_RULE_NAME"
    

Replace the following:

  * `COLLECTOR_NAME`: a name for the ULL Packet Mirroring collector.
  * `ULL_LOCATION`: the location of the collector resource.
  * `COLLECTOR_PROJECT`: the ID of the project that contains the collector instances and resources.
  * `ULL_PROJECT`: the ID of a project that supports ULL APIs.
  * `ENGINE_NAME`: the name of the ULL Mirroring Engine.
  * `COLLECTOR_REGION`: the region where the collector resources are located.
  * `FW_RULE_NAME`: a name for the forwarding rule.



###  Terraform 

To create the ULL Mirroring Collector, you can use a [`google_network_security_ull_mirroring_collector` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_ull_mirroring_collector).

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

By default, the ULL Mirroring collector instance is in the `ACTIVE` state, has no filter rules attached to it, and doesn't receive mirrored traffic. After you create the collector instance, create ULL Mirroring collector filter rules to mirror filtered traffic.

### Describe a ULL Packet Mirroring collector

To view the details of a ULL Packet Mirroring collector, use the `gcloud network-security ull-mirroring-collectors describe` command.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectors.get`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)
  * Collector Viewer (`roles/networksecurity.ullMirroringCollectorViewer`)



###  gcloud 
    
    
    gcloud network-security ull-mirroring-collectors describe COLLECTOR_NAME \
        --location=ULL_LOCATION \
        --project=COLLECTOR_PROJECT
    

Replace the following:

  * `COLLECTOR_NAME`: a name for the ULL Packet Mirroring collector.
  * `ULL_LOCATION`: the location of the collector resource.
  * `COLLECTOR_PROJECT`: the ID of the project that contains the collector instances and resources.



### Change the state of a ULL Packet Mirroring collector

You can change the state of a ULL Packet Mirroring collector to `ACTIVE` or `INACTIVE`. A collector in the `INACTIVE` state doesn't receive packets.

###  gcloud 

To change the ULL Packet Mirroring collector state to `ACTIVE`, use the `gcloud network-security ull-mirroring-collectors enable` command:
    
    
    gcloud network-security ull-mirroring-collectors enable COLLECTOR_NAME \
        --location=ULL_LOCATION \
        --project=COLLECTOR_PROJECT
    

To change the ULL Packet Mirroring collector state to `INACTIVE`, use the `gcloud network-security ull-mirroring-collectors disable` command:
    
    
    gcloud network-security ull-mirroring-collectors disable COLLECTOR_NAME \
        --location=ULL_LOCATION \
        --project=COLLECTOR_PROJECT
    

Replace the following:

  * `COLLECTOR_NAME`: the name of the ULL Packet Mirroring collector.
  * `ULL_LOCATION`: the location of the collector resource.
  * `COLLECTOR_PROJECT`: the ID of the project that contains your collector instances and resources.



### List ULL Packet Mirroring collectors

To list all ULL Packet Mirroring collectors in a specific location, use the `gcloud network-security ull-mirroring-collectors list` command.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectors.list`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)
  * Collector Viewer (`roles/networksecurity.ullMirroringCollectorViewer`)



###  gcloud 
    
    
    gcloud network-security ull-mirroring-collectors list \
        --location=ULL_LOCATION \
        --project=COLLECTOR_PROJECT
    

Replace the following:

  * `ULL_LOCATION`: the location of the collector resource.
  * `COLLECTOR_PROJECT`: the ID of the project that contains your collector instances and resources.



### Update a ULL Packet Mirroring collector

You can update only the labels of a ULL Packet Mirroring collector. To update a ULL Packet Mirroring collector, use the `gcloud network-security ull-mirroring-collectors update` command.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectors.update`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)



###  gcloud 
    
    
    gcloud network-security ull-mirroring-collectors update COLLECTOR_NAME \
        --location=ULL_LOCATION \
        --project=COLLECTOR_PROJECT \
        --update-labels=LABELS
    

Replace the following:

  * `COLLECTOR_NAME`: the name of the ULL Packet Mirroring collector.
  * `ULL_LOCATION`: the location of the collector resource.
  * `COLLECTOR_PROJECT`: the ID of the project that contains your collector instances and resources.
  * `LABELS`: the labels of the collector.



### Delete a ULL Packet Mirroring collector

Deleting a ULL Packet Mirroring collector stops the flow of mirrored packets to its associated forwarding rule. To delete a collector, use the `gcloud network-security ull-mirroring-collectors delete` command.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectors.delete`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)



###  gcloud 
    
    
    gcloud network-security ull-mirroring-collectors delete COLLECTOR_NAME \
        --location=ULL_LOCATION \
        --project=COLLECTOR_PROJECT
    

Replace the following:

  * `COLLECTOR_NAME`: a name for the ULL Packet Mirroring collector.
  * `ULL_LOCATION`: the location of the collector resource.
  * `COLLECTOR_PROJECT`: the ID of the project that contains your collector instances and resources.



## Create and manage ULL Packet Mirroring collector filter rules

A `UllMirroringCollectorRule` resource is a child resource of a `UllMirroringCollector`. Each rule contains conditions that a packet must meet to be mirrored. You can't change the conditions after you create the `UllMirroringCollectorRule` resource.

### Create a ULL Packet Mirroring collector filter rule

When you create a ULL Packet Mirroring collector filter rule, you define the source IP ranges, destination IP ranges, capture point primary IP ranges, protocols, and traffic direction to match against a replica packet.

**Note:** After you create a filter rule, it can take up to one minute for a filter rule to start filtering traffic.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectorRules.create`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)



###  gcloud 

To create a ULL Mirroring collector filter rule, use the `gcloud network-security ull-mirroring-collectors rules create` command in the collector project.
    
    
    gcloud network-security ull-mirroring-collectors rules create RULE_NAME \
        --ull-mirroring-collector=COLLECTOR_NAME \
        --project=COLLECTOR_PROJECT \
        --location=ULL_LOCATION \
        [--match-src-ip-ranges="SRC_IP_RANGES"] \
        [--match-dst-ip-ranges="DEST_IP_RANGES"] \
        [--match-primary-ip-ranges="PRIMARY_IP_RANGES"] \
        [--match-ip-protocols="PROTOCOL"] \
        [--match-direction=INGRESS | EGRESS]
    

Replace the following:

  * `RULE_NAME`: the ID or name of the filter rule.

You can define the name in the following fully qualified identifier format:
        
        projects/COLLECTOR_PROJECT/locations/ULL_LOCATION/ullMirroringCollectors/COLLECTOR_NAME/rules/RULE_NAME
        

If you don't specify the name in the previous format, you must specify the collector project ID, ULL location, and the collector name manually.

  * `COLLECTOR_NAME`: a name for the ULL Packet Mirroring collector.

  * `COLLECTOR_PROJECT`: the project ID that contains the collector compute instances and resources.

  * `ULL_LOCATION`: the location of the collector resource.

  * `SRC_IP_RANGES`: a comma-separated list of IPv4 address ranges in the CIDR format, such as `10.1.20.0/24`. The packet's source IP must match one of the ranges in this list. If you don't specify a range, the rule matches any range.

  * `DEST_IP_RANGES`: a comma-separated list of IPv4 address ranges in the CIDR format, such as `10.1.20.0/24`. The packet's destination IP must match one of the ranges in this list. If you don't specify a range, the rule matches any range.

  * `PRIMARY_IP_RANGES`: a comma-separated list of up to 10 IPv4 address ranges in the CIDR format, such as `10.1.20.0/24`. The primary IP address of the capture point must match a range in this list. The capture point is the U4 bare metal Compute Engine instance NIC that captures unicast and multicast traffic. If you don't specify a range, the rule matches traffic captured on any U4 instance NIC (any primary IP address).

  * `PROTOCOL`: the IP protocol names or numbers of the packet. If you don't specify a protocol, the rule matches packets of any protocol.

Valid protocol names and numbers are: `tcp` (`6`), `udp` (`17`), `icmp` (`1`), `igmp` (`2`)




**Note:** If you don't specify the `--match-direction` flag, the rule matches traffic in both directions.

###  Terraform 

To create the ULL Mirroring collector filter rule, you can use the [`google_network_security_ull_mirroring_collector_rule` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_ull_mirroring_collector_rule).

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

You can configure a collector to receive all traffic or no traffic by managing its filter rules.

  * To stop all traffic to a collector, ensure it has no `UllMirroringCollectorRule` resources, or set the state of the `UllMirroringCollector` to `INACTIVE`.

  * To mirror all traffic to a collector, create a single `UllMirroringCollectorRule` with the source and destination IP address ranges set to `0.0.0.0/0`, and omit the `--match-primary-ip-ranges`, `--match-ip-protocols`, and `--match-direction` flags.

Example:
        
        gcloud network-security ull-mirroring-collectors rules create mirror-all-traffic-rule \
            --ull-mirroring-collector=my-collector \
            --location=us-central1-a \
            --project=my-project \
            --match-src-ip-ranges="0.0.0.0/0" \
            --match-dst-ip-ranges="0.0.0.0/0"
        




### List all rules for a collector

Lists all filter rules for a specific collector.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectorRules.list`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)
  * Collector Viewer (`roles/networksecurity.ullMirroringCollectorViewer`)



###  gcloud 

To list all rules for a collector, use the `gcloud network-security ull-mirroring-collectors rules list` command.
    
    
    gcloud network-security ull-mirroring-collectors rules list \
        --ull-mirroring-collector=COLLECTOR_NAME \
        --location=ULL_LOCATION
    

Replace the following:

  * `COLLECTOR_NAME`: the ID or name of the ULL Packet Mirroring collector.

If you specify the name in the fully qualified identifier format, you don't have to specify the ULL location manually.

  * `ULL_LOCATION`: the location of the collector resource.




### Describe a rule

Displays the detailed configuration and matching criteria for a single rule.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectorRules.get`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)
  * Collector Viewer (`roles/networksecurity.ullMirroringCollectorViewer`)



###  gcloud 

To describe a specific rule, use the `gcloud network-security ull-mirroring-collectors rules describe` command.
    
    
    gcloud network-security ull-mirroring-collectors rules describe RULE_NAME \
        --ull-mirroring-collector=COLLECTOR_NAME \
        --location=ULL_LOCATION
    

Replace the following:

  * `RULE_NAME`: the ID or name of the rule.

If you specify the name in the fully qualified identifier format, you don't need to specify the collector name or the ULL location manually.

  * `COLLECTOR_NAME`: the name of the ULL Packet Mirroring collector.

  * `ULL_LOCATION`: the location of the collector resource.




### Update a rule

The filter criteria are immutable after you create the rule, but you can update metadata such as labels.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectorRules.update`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)



###  gcloud 

To update a rule, use the `gcloud network-security ull-mirroring-collectors rules update` command.
    
    
    gcloud network-security ull-mirroring-collectors rules update RULE_NAME \
        --ull-mirroring-collector=COLLECTOR_NAME \
        --location=ULL_LOCATION \
        --update-labels=LABELS \
        [--remove-labels=REMOVE_LABELS]
    

Replace the following:

  * `RULE_NAME`: the ID or name of the rule.

If you specify the name in the fully qualified identifier format, you don't need to specify the collector name or the ULL location manually.

  * `COLLECTOR_NAME`: the name of the ULL Packet Mirroring collector.

  * `ULL_LOCATION`: the location of the collector resource.

  * `LABELS`: the label to update.

  * `REMOVE_LABELS`: the label to remove.


**Note:** To remove all labels, use the `--clear-labels` flag.

### Delete a rule

Remove a specific filter rule. If you delete all rules, the collector doesn't mirror traffic by default.

**Note:** After you delete a filter rule, it can take up to one minute for the rule to stop filtering traffic.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.ullMirroringCollectorRules.delete`



**Roles**

  * Collector Admin (`roles/networksecurity.ullMirroringCollectorAdmin`)



###  gcloud 

To delete a rule, use the `gcloud network-security ull-mirroring-collectors rules delete` command.
    
    
    gcloud network-security ull-mirroring-collectors rules delete RULE_NAME \
        --ull-mirroring-collector=COLLECTOR_NAME \
        --location=ULL_LOCATION
    

Replace the following:

  * `RULE_NAME`: the ID or name of the rule.

If you specify the name in the fully qualified identifier format, you don't need to specify the collector name or the ULL location manually.

  * `COLLECTOR_NAME`: the name of the ULL Packet Mirroring collector.

  * `ULL_LOCATION`: the location of the collector resource.




## Troubleshoot

This section lists common issues and solutions.

### No traffic at ULL Packet Mirroring collectors

  * Ask the exchange operator to verify that the ULL VPC network status is `ACTIVE` on the engine.


  * Check firewall rules on the collector instances and verify that they allow ingress on UDP 6081.
  * Verify the collector VPC network MTU is at least 1808.
  * Verify that the collector instances have one or more `UllMirroringCollectorRule` resources attached.
  * Verify that `UllMirroringCollectorRule` resources have the correct filter criteria.



### Packet drops

  * Check collector instance performance for CPU and network utilization.
  * Consider scaling the instance group.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
