---
url: https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network/
title: Enable a VPC network to produce multicast traffic \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.838806+00:00
---

# Enable a VPC network to produce multicast traffic  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable a VPC network to produce multicast traffic

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how you configure resources in Google Cloud to allow multicast producers in a VPC network to send multicast traffic for a given multicast domain and one or more group ranges.

## Before you begin

Before you begin the procedures on this page, you must complete the prerequisites in the following sections.

### Confirm that the multicast domain and group range configurations are complete

Confirm that the multicast domain and multicast group range configurations for which you want to produce multicast traffic are complete as described in the [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview). If necessary, contact the multicast administrator of the domain.

### Set your project

The procedures on this page require you to create multicast producer resources in the project of the multicast administrator. This project contains the multicast domain and group range resources.

Set the gcloud CLI to use project of the multicast administrator. Alternatively you can use the `--project=MULTICAST_ADMIN_PROJECT` flag for each command in the following procedures.
    
    
        gcloud config set project MULTICAST_ADMIN_PROJECT
    

Replace `MULTICAST_ADMIN_PROJECT` with the ID of the multicast administrator project.

### Enable APIs

If you haven't already, enable the following APIs.

To enable APIs, you need the `serviceusage.services.enable` permission. If you don't have this permission, ask your Identity and Access Management (IAM) administrator to grant you the Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) role.

  1. To create multicast resources, enable the `networkservices` API:
         
         gcloud services enable networkservices.googleapis.com
         

  2. To create a Network Connectivity Center (NCC) VPC spoke, enable the `networkconnectivity` API:
         
         gcloud services enable networkconnectivity.googleapis.com
         




### Required roles

To get the permissions that you need to configure multicast producer resources, ask your administrator to grant you the following IAM roles: 

  * To create and manage network resources: Compute Network Admin (`compute.networkAdmin`) on the multicast administrator project 
  * To create and manage firewall rules: Compute Security Admin (`compute.securityAdmin`) on the multicast administrator project 
  * To create NCC spokes: Spoke Admin (`networkconnectivity.spokeAdmin`) on the multicast administrator project 
  * To create multicast resources: Multicast Admin (`networkservices.multicastAdmin`) on the multicast administrator project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a VPC network and add it to a hub

If the multicast domain uses a NCC star topology in which there are one or more separate multicast producer VPC networks, then you must complete the steps in this section.

If the multicast domain uses a single VPC network topology, or if the multicast domain uses a NCC star topology in which the multicast administrator network also acts as the multicast producer network, then you can skip this step and proceed directly to the steps to enable the VPC network to produce multicast traffic.

### Create a VPC network

This section describes how to create a Virtual Private Cloud (VPC) network for producing multicast traffic.

For more information about creating VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

###  gcloud 

  1. Create a VPC network by using the [`compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
         
         gcloud compute networks create MULTICAST_PRODUCER_NETWORK --subnet-mode=custom
         

Replace `MULTICAST_PRODUCER_NETWORK` with a name for the multicast producer VPC network.

  2. Add one or more subnets to host multicast producers by using the [`compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create SUBNET \
            --network=MULTICAST_PRODUCER_NETWORK \
            --range=PRIMARY_RANGE \
            --region=REGION
         

Replace the following values:

     * `SUBNET`: a name for the subnet
     * `MULTICAST_PRODUCER_NETWORK`: the name of the multicast producer network that you created previously
     * `PRIMARY_RANGE`: the primary IPv4 range for the subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * `REGION`: the Google Cloud region in which the new subnet is created. Must be a region that supports multicast, such as `us-east5`.



### Add firewall rules

This section describes how to create a firewall rule in the multicast producer VPC network for multicast traffic.

To create additional firewall rules, such as for SSH, see [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules).

#### Allow egress multicast traffic

This section describes how to create a firewall rule that allows egress multicast traffic from the VPC network.

All VPC networks have a default IPv4 allow egress rule with the lowest priority (65535). If there is no higher priority rule that explicitly blocks egress traffic, then you don't need to complete this step. For more information, see [Implied rules](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules).

This command is pre-populated with an example firewall rule name. Keep in mind that the name of a firewall rule must be unique in a project.

###  gcloud 

To create a firewall rule that allows egress multicast traffic from the VPC network, use the [`compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).
    
    
    gcloud compute firewall-rules create allow-multicast-egress --direction=EGRESS \
       --priority=1000 \
       --network=MULTICAST_PRODUCER_NETWORK \
       --action=ALLOW \
       --rules=udp[:PORT[-PORT]] \
       --destination-ranges=MULTICAST_GROUP_IP_RANGES
    

Replace the following values:

  * `MULTICAST_PRODUCER_NETWORK`: the name of the multicast producer network that you created previously
  * `PORT`: a list of ports to which the firewall rule applies. Google Cloud uses `udp` for multicast traffic. A port or port range can be specified after the protocol to which the firewall rule applies on traffic through specific ports. If no port or port range is specified, connections through all ranges are applied.

For example, specify `--rules=udp:1234` to allow multicast traffic through port `1234`.

Optionally, you can use `--rules=all` to allow all protocols and ports.

  * `MULTICAST_GROUP_IP_RANGES`: The IP address ranges of the multicast groups that multicast producers send traffic to. Multicast IP address ranges must be Class D address ranges, for example you can use `224.0.0.0/4` to allow all multicast traffic.




### Add the VPC network to a NCC hub

This section describes how to add your VPC network to the NCC hub that was created by the multicast administrator. To add your network, you create a VPC spoke in the _center_ group.

For more information, see [Star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#star-topology) and [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke) in the NCC documentation.

###  gcloud 

To add your VPCnetwork as a center spoke to a hub, use the [`network-connectivity spokes linked-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create).
    
    
      gcloud network-connectivity spokes linked-vpc-network create SPOKE_NAME \
         --hub=projects/MULTICAST_ADMIN_PROJECT/locations/global/hubs/HUB_NAME \
         --vpc-network=MULTICAST_PRODUCER_NETWORK \
         --group="center" \
         --global \
         --include-export-ranges=INCLUDE_RANGES
    

Replace the following values:

  * `SPOKE_NAME`: a name for the spoke
  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
  * `HUB_NAME`: the name of the NCC hub that was created by the multicast administrator
  * `MULTICAST_PRODUCER_NETWORK`: the name of the multicast producer network that you created previously

You can alternatively provide the URI of the multicast producer network by using the following format: `projects/MULTICAST_ADMIN_PROJECT/global/networks/MULTICAST_PRODUCER_NETWORK`.

  * `INCLUDE_RANGES`: a comma-separated list of IP address ranges to export to the hub.

By default, the spoke exports all subnet ranges. To avoid overlap with other spokes on the hub, you can specify which subnet ranges to export. If you specify subnet ranges, ensure that you include the ranges that host multicast producers and any other ranges needed for communication with other spokes, such as for unicast traffic.

Google Cloud prohibits subnet overlaps across VPC spokes as described in [Subnet route uniqueness](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#subnet-uniqueness). For more information about using export filters to avoid overlap, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).




## Enable a VPC network to produce multicast traffic

This section describes the steps required to enable multicast producers in a VPC network to send multicast traffic for a given domain and one or more group ranges.

### Add the multicast producer VPC network to a domain

This section describes how to add a multicast producer VPC network to a domain by creating a multicast producer association between the network and the domain.

Complete the following steps for each zone in which you want to host multicast producers.

###  gcloud 

To add a multicast producer VPC network to a domain, use the [`network-services multicast-producer-associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-producer-associations/create).
    
    
       gcloud network-services multicast-producer-associations create PRODUCER_ASSOCIATION_NAME \
          --multicast-domain-activation="projects/ADMIN_PROJECT/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME" \
          --network=projects/ADMIN_PROJECT/locations/global/networks/MULTICAST_PRODUCER_NETWORK \
          --location=ZONE
    

Replace the following values:

  * `PRODUCER_ASSOCIATION_NAME`: a name for the multicast producer association
  * `ADMIN_PROJECT`: the ID of the multicast administrator project
  * `ZONE`: a zone in which the administrator activated the multicast domain and in which you host multicast producers
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation that was created by the multicast administrator
  * `MULTICAST_PRODUCER_NETWORK`: the VPC network that produces multicast traffic. Either the multicast administrator network or a separate multicast producer network, depending on the multicast topology of the domain.



###  API 

To add a multicast producer VPC network to a domain, use the [`multicastProducerAssociations.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/create).
    
    
    POST https://networkservices.googleapis.com/v1/projects/ADMIN_PROJECT/locations/ZONE/multicastProducerAssociations?multicastProducerAssociationId=PRODUCER_ASSOCIATION_NAME
    {
      "multicastDomainActivation": "projects/ADMIN_PROJECT/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME",
      "network": "projects/ADMIN_PROJECT/locations/global/networks/MULTICAST_PRODUCER_NETWORK"
    }
    

Replace the following values:

  * `PRODUCER_ASSOCIATION_NAME`: a name for the multicast producer association
  * `ADMIN_PROJECT`: the ID of the multicast administrator project
  * `ZONE`: a zone in which the administrator activated the multicast domain and in which you host multicast producers.
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation that was created by the multicast administrator
  * `MULTICAST_PRODUCER_NETWORK`: the VPC network that produces multicast traffic. Either the multicast administrator network or a separate multicast producer network, depending on the multicast topology of the domain.



### Activate the multicast producer VPC network for a group range

This section describes how to activate a multicast producer VPC network for a group range.

Complete the following steps for each multicast group range and zone in which you want to produce multicast traffic.

###  gcloud 

To activate a multicast producer VPC network for a group range, use the [`network-services multicast-group-producer-activations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-producer-activations/create).
    
    
       gcloud network-services multicast-group-producer-activations create GROUP_PRODUCER_ACTIVATION_NAME \
          --multicast-producer-association="projects/ADMIN_PROJECT/locations/ZONE/multicastProducerAssociations/PRODUCER_ASSOCIATION_NAME" \
          --multicast-group-range-activation="projects/ADMIN_PROJECT/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME" \
          --location=ZONE
    

Replace the following values:

  * `GROUP_PRODUCER_ACTIVATION_NAME`: a name for the multicast group producer activation
  * `ADMIN_PROJECT`: the project ID of the multicast administrator
  * `ZONE`: a zone in which to activate the multicast producer network. The corresponding multicast producer association and multicast group range activation must also exist in the zone.
  * `PRODUCER_ASSOCIATION_NAME`: the name of the multicast producer association that you created previously
  * `GROUP_RANGE_ACTIVATION_NAME`: the name of the multicast group range activation that was created by the multicast administrator



###  API 

To activate a multicast producer VPC network for a group range, use the [`multicastGroupProducerActivations.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/create).
    
    
    POST https://networkservices.googleapis.com/v1/projects/ADMIN_PROJECT/locations/ZONE/multicastGroupProducerActivations?multicastGroupProducerActivationId=GROUP_PRODUCER_ACTIVATION_NAME
    {
      "multicastProducerAssociation": "projects/ADMIN_PROJECT/locations/ZONE/multicastProducerAssociations/PRODUCER_ASSOCIATION_NAME",
      "multicastGroupRangeActivation": "projects/ADMIN_PROJECT/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME"
    }
    

Replace the following values:

  * `GROUP_PRODUCER_ACTIVATION_NAME`: a name for the multicast group producer activation
  * `ADMIN_PROJECT`: the project ID of the multicast administrator
  * `ZONE`: a zone in which to activate the multicast producer network. The corresponding multicast producer association and multicast group range activation must also exist in the zone.
  * `PRODUCER_ASSOCIATION_NAME`: the name of the multicast producer association that you created previously
  * `GROUP_RANGE_ACTIVATION_NAME`: the name of the multicast group range activation that was created by the multicast administrator



## Create multicast producer instances

If you haven't already, create one or more Compute Engine instances to run your application that produces multicast traffic. See the following:

  * For information about choosing a machine type, see [Machine considerations for multicast producer and consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements).
  * For information about creating instances, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).



Unlike multicast consumer instances, multicast producer instances don't need to be configured for IGMP and can send traffic to a multicast group _without_ joining the group.

## What's next

  * To view the multicast producer configurations that you created, see [View multicast producer configurations](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-producer-configs).
  * [Update multicast producer configurations](https://docs.cloud.google.com/vpc/docs/multicast/update-configurations#producer)
  * [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
