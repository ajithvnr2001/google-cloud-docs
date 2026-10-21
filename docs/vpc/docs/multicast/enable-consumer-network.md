---
url: https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network/
title: Enable a VPC network to consume multicast traffic \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:45.029772+00:00
---

# Enable a VPC network to consume multicast traffic  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable a VPC network to consume multicast traffic

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes the steps required to configure resources in Google Cloud so that multicast consumers in a VPC network can receive multicast traffic from a given multicast domain and one or more group ranges.

## Before you begin

Before you begin the procedures on this page, you must complete the prerequisites that are described in this section.

### Confirm that the multicast domain, group range, and producer configurations are complete

Confirm that the multicast domain, multicast group range, and multicast producer configurations for which you want to consume multicast traffic are complete as described in the [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview). If necessary, contact the multicast administrator of the domain.

### Set your project

Set the gcloud CLI to use project of the multicast consumer VPC network. Alternatively you can pass in the `--project=PROJECT` flag for each command in the following procedures.
    
    
        gcloud config set project PROJECT
    

Replace `PROJECT` with the ID of your project.

### Enable APIs

If you haven't already, enable the following APIs.

To enable APIs, you need the `serviceusage.services.enable` permission. If you don't have this permission, ask your Identity and Access Management (IAM) administrator to grant you the Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) role.

  1. To create multicast resources, enable the `networkservices` API:
         
         gcloud services enable networkservices.googleapis.com
         

  2. To create a Network Connectivity Center (NCC) VPC spoke, enable the `networkconnectivity` API:
         
         gcloud services enable networkconnectivity.googleapis.com
         




### Required roles

To get the permissions that you need to configure multicast consumer resources, ask your administrator to grant you the following IAM roles: 

  * To create and manage network resources: Compute Network Admin (`compute.networkAdmin`) on your project 
  * To create and manage firewall rules: Compute Security Admin (`compute.securityAdmin`) on your project 
  * To create NCC spokes: Spoke Admin (`networkconnectivity.spokeAdmin`) on your project 
  * To propose NCC spokes to the hub associated with a multicast domain: Group User (`networkconnectivity.groupUser`) on the multicast administrator project 
  * To create multicast resources: Multicast Admin (`networkservices.multicastAdmin`) on your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a VPC network and add it to a hub

If the multicast domain uses a NCC star topology in which there are separate multicast consumer VPC networks, then you must complete the steps in this section.

If the multicast domain uses a single VPC network topology, then you can skip this section and proceed directly to the steps to enable the VPC network to consume multicast traffic.

### Create a VPC network

This section describes how to create a Virtual Private Cloud (VPC) network for consuming multicast traffic.

For more information about creating VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

###  gcloud 

  1. Create a VPC network by using the [`compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
         
         gcloud compute networks create MULTICAST_CONSUMER_NETWORK --subnet-mode=custom
         

Replace `MULTICAST_CONSUMER_NETWORK` with a name for the multicast consumer network.

  2. Add one or more subnets to host multicast consumers by using the [`compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create SUBNET
            --network=MULTICAST_CONSUMER_NETWORK \
            --range=PRIMARY_RANGE \
            --region=REGION
         

Replace the following values:

     * `SUBNET`: the name for the subnet
     * `MULTICAST_CONSUMER_NETWORK`: the name of the multicast consumer network that you created previously
     * `PRIMARY_RANGE`: the primary IPv4 range for the subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * `REGION`: the Google Cloud region in which the new subnet is created. Must be a region that supports multicast, such as `us-east5`.



### Add firewall rules

This section describes how to create firewall rules in the multicast consumer VPC network for multicast traffic.

To create additional firewall rules, such as for SSH, see [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules).

The commands are pre-populated with example firewall rule names. Keep in mind that the name of a firewall rule must be unique in a project.

#### Allow ingress multicast traffic

###  gcloud 

To create a firewall rule that allows ingress multicast traffic to your VPC network from the multicast producer network, use the [`compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).
    
    
    gcloud compute firewall-rules create allow-multicast-traffic-ingress \
       --direction=INGRESS \
       --priority=1000 \
       --network=MULTICAST_CONSUMER_NETWORK \
       --action=ALLOW \
       --rules=udp[:PORT[-PORT]] \
       --source-ranges=MULTICAST_PRODUCER_RANGE \
       --destination-ranges=MULTICAST_GROUP_IP_RANGES
    

Replace the following values:

  * `MULTICAST_CONSUMER_NETWORK`: the name of the multicast consumer network that you created previously
  * `PORT`: a list of ports to which the firewall rule applies. Google Cloud uses `udp` for multicast traffic. A port or port range can be specified after the protocol to which the firewall rule applies on traffic through specific ports. If no port or port range is specified, connections through all ranges are applied.

For example, specify `--rules=udp:1234` to allow multicast traffic through port 1234.

  * `MULTICAST_PRODUCER_RANGE`: The CIDR range of the multicast producer VPC network, used to allocate IP addresses for multicast producers. You can alternatively omit the `--source-ranges` flag, which sets the ingress source to any IPv4 address (`0.0.0.0/0`).

  * `MULTICAST_GROUP_IP_RANGES`: The CIDR ranges of the multicast groups that multicast producers send traffic to. This must be a Class D address range, for example you can use `224.0.0.0/4` to allow all multicast traffic.




#### Allow ingress IGMP query

###  gcloud 

To create a firewall rule that allows ingress IGMP query traffic to the multicast consumer VPC network from the multicast consumer network range, use the [`compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).

The following command includes:

  * `--destination-ranges=224.0.0.1/32` to specify the multicast group IP address that represents all hosts on this subnet.
  * `--rules=2` to specify IGMP.


    
    
    gcloud compute firewall-rules create allow-multicast-igmp-ingress \
        --direction=INGRESS \
        --priority=1000 \
        --network=MULTICAST_CONSUMER_NETWORK \
        --action=ALLOW \
        --rules=2 \
        --source-ranges=MULTICAST_CONSUMER_RANGE \
        --destination-ranges=224.0.0.1/32
    

Replace the following values:

  * `MULTICAST_CONSUMER_NETWORK`: the name of the multicast consumer network that you created previously
  * `MULTICAST_CONSUMER_RANGE`: The CIDR range of the multicast consumer network, used to allocate IP addresses for multicast consumers.



#### Allow egress IGMP

This section describes how to create a firewall rule that allows egress IGMP traffic so that you can send IGMP `JOIN` and `LEAVE` messages from multicast consumers.

All VPC networks have a default IPv4 allow egress rule with the lowest priority (65535). If there is no higher priority rule that explicitly blocks egress traffic, then you don't need to complete this step. For more information, see [Implied rules](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules).

###  gcloud 

To create a firewall rule that allows egress multicast IGMP traffic from the multicast consumer VPC network, use the [`compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).
    
    
    gcloud compute firewall-rules create allow-multicast-igmp-egress \
        --direction=EGRESS \
        --priority=1000 \
        --network=MULTICAST_CONSUMER_NETWORK \
        --action=ALLOW \
        --rules=2 \
        --destination-ranges=RANGES_FOR_JOIN_AND_LEAVE
    

Replace the following values:

  * `MULTICAST_CONSUMER_NETWORK`: the name of the multicast consumer network that you created previously
  * `RANGES_FOR_JOIN_AND_LEAVE`: a comma-separated list of the following:

    * The CIDR ranges of the multicast groups that multicast consumers need to join. You must use Class D address ranges.
    * The _All routers_ IP address: `224.0.0.2/32`. This range is required for sending IGMP leave messages.

Alternatively, you can specify `224.0.0.0/4` to allow all multicast traffic.




### Add the VPC network to a NCC hub

This section describes how to add your VPC network to the NCC hub that was created by the multicast administrator. To add your network, you create a VPC spoke in the _edge_ group.

For more information, see [Star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#star-topology) and [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke) in the NCC documentation.

###  gcloud 

  1. To add your VPC network as an edge spoke to a hub, use the [`network-connectivity spokes linked-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create).
         
         gcloud network-connectivity spokes linked-vpc-network create SPOKE_NAME \
             --hub=projects/MULTICAST_ADMIN_PROJECT/locations/global/hubs/HUB \
             --vpc-network=MULTICAST_CONSUMER_NETWORK \
             --group="edge" \
             --global \
             --include-export-ranges=INCLUDE_RANGES
         

Replace the following values:

     * `SPOKE_NAME`: a name for the edge spoke
     * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
     * `HUB`: the name of the NCC hub that was created by the multicast administrator. Your multicast consumer VPC network must attach to the same hub as the multicast administrator and multicast producer VPC networks. If necessary, contact the multicast administrator for the name of the hub.

     * `MULTICAST_CONSUMER_NETWORK`: the name of the multicast consumer network that you created previously

You can alternatively provide the URI of the multicast consumer network by using the following format: `projects/MULTICAST_CONSUMER_PROJECT/global/networks/MULTICAST_CONSUMER_NETWORK`.

     * `INCLUDE_RANGES`: a comma-separated list of IP address ranges to export to the hub.

By default, the spoke exports all subnet ranges. To avoid overlap with other spokes on the hub, you can specify which subnet ranges to export. If you specify subnet ranges, ensure that you include the ranges that host multicast consumers and any other ranges needed for communication with the spokes in the center group, such as for unicast traffic.

Google Cloud prohibits subnet overlaps across VPC spokes as described in [Subnet route uniqueness](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#subnet-uniqueness). For more information about using export filters to avoid overlap, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).

  2. Contact the multicast administrator to notify them that you proposed a VPC spoke to the hub.

If the hub is in a different project, then the multicast administrator must explicitly approve your spoke before it becomes active, unless the multicast administrator added your project as an auto-accept project.

To check the status of a spoke after you create it, see [Check the status of a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status).




## Enable a VPC network to consume multicast traffic

This section describes the steps required to enable multicast consumers in a VPC network to receive multicast traffic from a given domain and and one or more group ranges.

### Add the multicast consumer VPC network to a domain

This section describes how to add a multicast consumer VPC network to a domain by creating a multicast consumer association between the network and the domain.

Complete the following steps for each zone in which you want to host multicast consumers.

###  gcloud 

To add a multicast consumer VPC network to a domain, use the [`network-services multicast-consumer-associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-consumer-associations/create).
    
    
       gcloud network-services multicast-consumer-associations create CONSUMER_ASSOCIATION_NAME \
          --multicast-domain-activation="projects/ADMIN_PROJECT/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME" \
          --network="projects/MULTICAST_CONSUMER_PROJECT/locations/global/networks/MULTICAST_CONSUMER_NETWORK" \
          --location=ZONE
    

Replace the following values:

  * `CONSUMER_ASSOCIATION_NAME`: a name for the multicast consumer association
  * `ADMIN_PROJECT`: the ID of the multicast administrator project
  * `ZONE`: a zone in which the administrator activated the multicast domain and in which you need to host multicast consumers
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation that was created by the multicast administrator
  * `MULTICAST_CONSUMER_PROJECT` and `MULTICAST_CONSUMER_NETWORK`: the project and network that consumes multicast traffic. Either the multicast administrator project and network or a separate multicast consumer project and network, depending on the multicast topology of the domain.



###  API 

To add a multicast consumer VPC network to a domain, use the [`multicastConsumerAssociations.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/create).
    
    
    POST https://networkservices.googleapis.com/v1/projects/MULTICAST_CONSUMER_PROJECT/locations/ZONE/multicastConsumerAssociations?multicastConsumerAssociationId=CONSUMER_ASSOCIATION_NAME
    {
      "multicastDomainActivation": "projects/ADMIN_PROJECT/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME",
      "network": "projects/MULTICAST_CONSUMER_PROJECT/locations/global/networks/MULTICAST_CONSUMER_NETWORK"
    }
    

Replace the following values:

  * `CONSUMER_ASSOCIATION_NAME`: a name for the multicast consumer association
  * `ADMIN_PROJECT`: the ID of the multicast administrator project
  * `ZONE`: a zone in which the administrator activated the multicast domain and in which you need to host multicast consumers.
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation that was created by the multicast administrator
  * `MULTICAST_CONSUMER_PROJECT` and `MULTICAST_CONSUMER_NETWORK`: the project and network that consumes multicast traffic. Either the multicast administrator project and network or a separate multicast consumer project and network, depending on the multicast topology of the domain.



### Activate the multicast consumer VPC network for a group range

This section describes how to activate a multicast consumer VPC network for a group range.

Complete the following steps for each multicast group range and zone for which you want to consume multicast traffic.

After you complete this step, multicast consumers in the network can join the multicast group IP addresses in the specified group range given that they have [IGMP configured](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).

###  gcloud 

To activate a multicast consumer VPC network for a multicast group range, use the [`network-services multicast-group-consumer-activations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-consumer-activations/create).

**Note:** If you can't run the following command successfully, your project might not be part of the [consumer accept list](https://docs.cloud.google.com/vpc/docs/multicast/control-access-group-ranges) for the group range. If necessary, contact the multicast administrator.
    
    
       gcloud network-services multicast-group-consumer-activations create GROUP_CONSUMER_ACTIVATION_NAME \
          --multicast-consumer-association="projects/CONSUMER_PROJECT/locations/ZONE/multicastConsumerAssociations/CONSUMER_ASSOCIATION_NAME" \
          --multicast-group-range-activation="projects/ADMIN_PROJECT/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME" \
          --location=ZONE \
          [--enable-logging | --no-enable-logging]
    

Replace the following values:

  * `GROUP_CONSUMER_ACTIVATION_NAME`: a name for the multicast group consumer activation
  * `CONSUMER_PROJECT`: the ID of your project. This can be either the multicast administrator project or a separate multicast consumer project, depending on the topology of the multicast domain.

  * `ZONE`: the zone in which to activate the multicast consumer network. Must also be a zone in which the administrator activated the multicast group range.

  * `CONSUMER_ASSOCIATION_NAME`: the name of the multicast consumer association that you created previously

  * `ADMIN_PROJECT`: the ID of the multicast administrator project

  * `GROUP_RANGE_ACTIVATION_NAME`: the name of the group range activation that was created by the multicast administrator.

  * `--[no-]enable-logging`: optional, determines whether [group membership event logging](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs) is enabled.

    * To enable logging, use `--enable-logging`.
    * (Default) To disable logging, use `--no-enable-logging`.



###  API 

To activate a multicast consumer VPC network for a multicast group range, use the [`multicastGroupConsumerActivations.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/create).

**Note:** If you can't make the following request successfully, your project might not be part of the [consumer accept list](https://docs.cloud.google.com/vpc/docs/multicast/control-access-group-ranges) for the group range. If necessary, contact the multicast administrator.
    
    
    POST https://networkservices.googleapis.com/v1/projects/CONSUMER_PROJECT/locations/ZONE/multicastGroupConsumerActivations?multicastGroupConsumerActivationId=GROUP_CONSUMER_ACTIVATION_NAME
    {
      "multicastConsumerAssociation": "projects/CONSUMER_PROJECT/locations/ZONE/multicastConsumerAssociations/CONSUMER_ASSOCIATION_NAME",
      "multicastGroupRangeActivation": "projects/ADMIN_PROJECT/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME",
      "logConfig": {
              "enabled": "LOGGING_ENABLED"
        }
    }
    

Replace the following values:

  * `GROUP_CONSUMER_ACTIVATION_NAME`: a name for the multicast group consumer activation
  * `CONSUMER_PROJECT`: the ID of your project. This can be either the multicast administrator project or a separate multicast consumer project, depending on the topology of the multicast domain.
  * `ZONE`: the zone in which to activate the multicast consumer network. Must also be a zone in which the administrator activated the multicast group range.
  * `CONSUMER_ASSOCIATION_NAME`: the name of the multicast consumer association that you created previously
  * `ADMIN_PROJECT`: the ID of the multicast administrator project
  * `GROUP_RANGE_ACTIVATION_NAME`: the name of the group range activation that was created by the multicast administrator
  * `LOGGING_ENABLED`: determines whether [group membership event logging](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs) is enabled. 
    * To enable logging, set to `true`.
    * (Default) To disable logging, set to `false`.



## Create multicast consumer instances

If you haven't already, create one or more Compute Engine instances to run your application that consumes multicast traffic. To create a multicast consumer instance or configure an existing instance to be a multicast consumer, see [Configure multicast consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).

## What's next

  * To view the multicast consumer configurations that you created, see [View multicast consumer configurations](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-consumer-configs).
  * [Update multicast consumer configurations](https://docs.cloud.google.com/vpc/docs/multicast/update-configurations#consumer)
  * [Configure IGMP for multicast consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
