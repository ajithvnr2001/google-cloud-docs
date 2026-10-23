---
url: https://docs.cloud.google.com/vpc/docs/multicast/create-domains/
title: Create multicast domains \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:00.125009+00:00
---

# Create multicast domains  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/create-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create multicast domains

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes the steps that you must follow to create multicast domains.

For an overview of the configuration process for Cloud Multicast, see [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview).

## Before you begin

Before you create multicast domains, see the following sections.

### Create or identify a VPC network

If you haven't already, create a Virtual Private Cloud (VPC) network to use as the multicast administrator network. For more information about creating VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

If your multicast administrator network will also host multicast producers or consumers, such as when using the single VPC network topology, then ensure that the network has the appropriate firewall rules to allow multicast traffic. See the following:

  * [Add firewall rules for multicast producers](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network#add-firewall-rules)
  * [Add firewall rules for multicast consumers](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#add-firewall-rules)



### Set your project

Set the gcloud CLI to use your project. Alternatively you can include the `--project=MULTICAST_ADMIN_PROJECT` flag for each command in the following procedures.
    
    
        gcloud config set project MULTICAST_ADMIN_PROJECT
    

Replace `MULTICAST_ADMIN_PROJECT` with the ID of your project.

### Enable APIs

If you haven't already, enable the following APIs.

To enable APIs, you need the `serviceusage.services.enable` permission. If you don't have this permission, ask your Identity and Access Management (IAM) administrator to grant you the Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) role.

  1. To create multicast resources, enable the `networkservices` API:
         
         gcloud services enable networkservices.googleapis.com
         

  2. To create a Network Connectivity Center (NCC) VPC spoke, enable the `networkconnectivity` API:
         
         gcloud services enable networkconnectivity.googleapis.com
         




### Required roles

To get the permissions that you need to create multicast domains, ask your administrator to grant you the following IAM roles: 

  * To create and manage network resources: Compute Network Admin (`compute.networkAdmin`) on your project 
  * To create and manage firewall rules: Compute Security Admin (`compute.securityAdmin`) on your project 
  * To create and manage NCC hubs and spokes: Hub and Spoke Admin (`networkconnectivity.hubAdmin`) on your project 
  * To create multicast resources: Multicast Admin (`networkservices.multicastAdmin`) on your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure NCC

If you are creating a multicast domain that uses the NCC star topology, then follow the steps in this section to configure the hub.

If you are creating a multicast domain that uses the single VPC network topology, then you can skip this section and proceed to Create a multicast domain.

This section describes how to configure NCC hub with the preset star topology to enable the following:

  * You can add your administrator VPC network to the hub as a center spoke.
  * If there is a separate multicast producer VPC network, the multicast producer VPC network can join the hub as a center spoke.
  * Multicast consumer VPC networks can join the hub as edge spokes.



For more information, see [Star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#star-topology) and [Configure a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub) in the NCC documentation.

###  gcloud 

To configure NCC, do the following:

  1. To create a hub, use the [`network-connectivity hubs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create).
         
         gcloud network-connectivity hubs create HUB_NAME \
             --policy-mode=PRESET \
             --preset-topology=STAR
         

Replace `HUB_NAME` with a name for the hub.

  2. To add your VPC network as a center spoke to the hub, use the [`network-connectivity spokes linked-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create).
         
         gcloud network-connectivity spokes linked-vpc-network create SPOKE_NAME \
             --hub=projects/MULTICAST_ADMIN_PROJECT/locations/global/hubs/HUB_NAME \
             --vpc-network=MULTICAST_ADMIN_NETWORK \
             --group="center" \
             --global
         

Replace the following:

     * `SPOKE_NAME`: a name for the spoke
     * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
     * `HUB_NAME`: the name of the NCC hub that you created previously
     * `MULTICAST_ADMIN_NETWORK`: the name of the multicast administrator network that you created previously

You can alternatively provide the URI of the multicast administrator network by using the following format: `projects/MULTICAST_ADMIN_PROJECT/global/networks/MULTICAST_ADMIN_NETWORK`.

  3. To allow multicast consumer VPC networks to join the hub, do the following. Alternatively, you can continue configuring multicast and complete these steps later as described in [Control access to multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/control-access-domains).

     1. Grant multicast consumer network administrators in other projects the ability to propose VPC spokes to the hub by following the steps in [Give access](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-give-access) in the NCC documentation.

     2. Ask multicast consumer network administrators to add their VPC networks as spokes to the hub that you created when they follow the procedure to [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network).

     3. [Review proposed VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes) as needed to check for spoke proposals.

     4. When you receive a spoke proposal, follow the steps to [Accept the VPC spoke](https://docs.cloud.google.com/vpc/docs/multicast/control-access-domains#accept-spoke).




## Create a multicast domain

This section describes how to create a multicast domain.

### Create a domain group

This section describes how to create a multicast domain group. Before proceeding, review the following:

  * If you plan to create redundant domains, we recommend that you create a domain group for higher availability between the domains.

  * A domain group explicitly groups two related domains together. Don't create a domain group for a single domain or for more than two domains.

  * Creating a domain group is an optional configuration. If you don't require a domain group, you can skip this step. However, you can't add existing domains to a domain group later.




###  gcloud 

To create a domain group, use the [`network-services multicast-domain-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-groups/create).
    
    
    gcloud network-services multicast-domain-groups create DOMAIN_GROUP_NAME \
       --location=global
    

Replace `DOMAIN_GROUP_NAME` with a name for the domain group.

###  API 

To create a domain group, use the [`multicastDomainGroups.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/create).
    
    
    POST https://networkservices.googleapis.com/v1/projects/MULTICAST_ADMIN_PROJECT/locations/global/multicastDomainGroups?multicastDomainGroupId=DOMAIN_GROUP_NAME
    

Replace the following:

  * `DOMAIN_GROUP_NAME`: a name for the domain group
  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project



### Create a domain

Create one or more multicast domains associated with your multicast administrator VPC network.

###  gcloud 

To create a domain, use the [`network-services multicast-domains create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domains/create).

If you want to use a domain group, then you must specify the domain group when you create the domain. You can't add the domain to a domain group later. To create domains that are part of a domain group, you must run the following command twice, for example to create `DOMAIN_1` and `DOMAIN_2`.
    
    
       gcloud network-services multicast-domains create DOMAIN_NAME \
          --location=global \
          --admin-network=projects/MULTICAST_ADMIN_PROJECT/locations/global/networks/MULTICAST_ADMIN_NETWORK \
          --connection-type=TOPOLOGY \
          [--ncc-hub=projects/MULTICAST_ADMIN_PROJECT/locations/global/hubs/HUB_NAME] \
          [--multicast-domain-group=projects/MULTICAST_ADMIN_PROJECT/locations/global/multicastDomainGroups/DOMAIN_GROUP_NAME]
    

Replace the following values:

  * `DOMAIN_NAME`: a name for the domain
  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
  * `MULTICAST_ADMIN_NETWORK`: the VPC network of the multicast administrator. If you are using the NCC topology, this network must also part of the hub as the center spoke, otherwise domain creation fails.
  * `TOPOLOGY`: the [topology](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#topologies) that you want to configure for Cloud Multicast. Specify one of the following: 
    * `SAME_VPC`: the single VPC network topology.
    * `NCC`: the NCC star topology.
  * `HUB_NAME`: if you are configuring the Network Connectivity Center star topology, then specify the name of the hub.
  * `DOMAIN_GROUP_NAME`: if you created a domain group, then enter the name of the domain group.



###  API 

To create a domain, use the [`multicastDomains.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/create).

If you want to use a domain group, then you must specify the domain group when you create the domain. You can't add the domain to a domain group later. To create domains that are part of a domain group, you must make the following API request twice. For example, make the following request once to create `DOMAIN_1`, and then make the request again to create `DOMAIN_2`:
    
    
    POST https://networkservices.googleapis.com/v1/projects/MULTICAST_ADMIN_PROJECT/locations/global/multicastDomains?multicastDomainId=DOMAIN_NAME
    
    {
      "adminNetwork": "projects/MULTICAST_ADMIN_PROJECT/locations/global/networks/MULTICAST_ADMIN_NETWORK",
      "connection": {
          "connectionType": "TOPOLOGY",
          "nccHub": "projects/MULTICAST_ADMIN_PROJECT/locations/global/hubs/HUB_NAME"
      },
      "multicastDomainGroup": "projects/MULTICAST_ADMIN_PROJECT/locations/global/multicastDomainGroups/DOMAIN_GROUP_NAME"
    }
    

Replace the following values:

  * `DOMAIN_NAME`: a name for the domain
  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
  * `MULTICAST_ADMIN_NETWORK`: the VPC network of the multicast administrator. If you are using the NCC topology, this network must also part of the hub as the center spoke, otherwise domain creation fails.
  * `TOPOLOGY`: the [topology](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#topologies) that you want to configure for Cloud Multicast. Specify one of the following: 
    * `SAME_VPC`: the single VPC network topology.
    * `NCC`: the NCC star topology.
  * `HUB_NAME`: if you are configuring the Network Connectivity Center star topology, then specify the name of the hub by using the `nccHub` field.
  * `DOMAIN_GROUP_NAME`: if you created a domain group, then enter the name of the domain group by using the `multicastDomainGroup` field.



### Activate the domain

Activate the domain in each zone where multicast producers or consumers need to send or receive multicast traffic. When you activate a domain in a zone, Google Cloud provisions multicast infrastructure for your domain in that zone.

If you don't activate a domain in a given zone, then multicast traffic can't be sent or received in that zone.

###  gcloud 

To activate a domain, use the [`network-services multicast-domain-activations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-activations/create).

The following command takes around 10 to 30 minutes to complete.
    
    
       gcloud network-services multicast-domain-activations create DOMAIN_ACTIVATION_NAME \
          --multicast-domain="projects/MULTICAST_ADMIN_PROJECT/locations/global/multicastDomains/DOMAIN_NAME" \
          --location=ZONE \
          [--disable-placement-policy] \
          [--aggr-egress-pps=AGGR_EGRESS_PPS] \
          [--aggr-ingress-pps=AGGR_INGRESS_PPS] \
          [--avg-packet-size=AVG_PACKET_SIZE] \
          [--max-per-group-ingress-pps=MAX_PER_GROUP_INGRESS_PPS] \
          [--max-per-group-subscribers=MAX_PER_GROUP_SUBSCRIBERS]
    

Replace the following values:

  * `DOMAIN_ACTIVATION_NAME`: a name for the domain activation
  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
  * `DOMAIN_NAME`: the name of the domain to activate
  * `ZONE`: the zone in which to activate the domain
  * `--disable-placement-policy`: If you are activating a domain that is part of a domain group, then you can optionally include this flag to disable the creation of a placement policy. Otherwise, Google Cloud automatically creates placement policy that can optionally be [applied to new or existing multicast consumers](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).
  * Specify the following parameters according to your needs for the multicast traffic in this zone. Google Cloud uses these parameters to determine the scale of your multicast infrastructure.

Before you specify these parameters, see the following:

    * Review the corresponding [limitations for multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/overview#limitations-domain-activation) described in the Cloud Multicast overview.
    * If you don't include these flags, Google Cloud generates a minimal configuration that you can use for testing.
    * You can update the configuration of these flags later as described in [Update multicast domain parameters](https://docs.cloud.google.com/vpc/docs/multicast/update-domain-parameters).
    * While the these flags are optional, if you include any of the flags, then `--aggr-egress-pps` becomes a required flag.

For more information about each flag, see the following:

    * `AGGR_EGRESS_PPS`: aggregate egress packets per second (pps) for all multicast groups in the domain in the specified zone. Egress refers to packets distributed from the multicast infrastructure to multicast consumers.

You can enter a value from 0 to 500000000 (500 million). The default is value is 1000000 (1 million). Default values for the other fields are set dynamically based on the value that you enter for this flag.

**Note:** If you don't know your aggregate egress pps, then you can estimate it by using the following formula: `AGGR_EGRESS_PPS = AGGR_INGRESS_PPS * MAX_PER_GROUP_SUBSCRIBERS / 2`.
    * `AGGR_INGRESS_PPS`: aggregate ingress pps for all multicast groups in the domain in the specified zone. Ingress refers to packets sent from multicast producers to the multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `--aggr-ingress-pps` can't be greater than the value of `--aggr-egress-pps`.

    * `AVG_PACKET_SIZE`: average packet size in bytes. You can enter a value from 64 to 1500.

    * `MAX_PER_GROUP_INGRESS_PPS`: maximum ingress pps for a single multicast group in the domain in the specified zone. Use this flag to specify the most active multicast group in the domain, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `--max-per-group-ingress-pps` can't be greater than the value of `--aggr-ingress-pps`.

    * `MAX_PER_GROUP_SUBSCRIBERS`: maximum number of multicast consumers for a single multicast group in the domain in the specified zone. Use this flag to specify the group with the most multicast consumers, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure. Including this flag does not enforce a limit on the number of multicast consumers for a group.

You can enter a value from 1 to 500.




###  API 

To activate a domain, use the [`multicastDomainActivations.create` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/create).

The following request takes around 10 to 30 minutes to complete.
    
    
    POST https://networkservices.googleapis.com/v1/projects/MULTICAST_ADMIN_PROJECT/locations/ZONE/multicastDomainActivations?multicastDomainActivationId=DOMAIN_ACTIVATION_NAME
    
    {
      "multicastDomain": "projects/MULTICAST_ADMIN_PROJECT/locations/global/multicastDomains/DOMAIN_NAME",
      "disablePlacementPolicy": "PLACEMENT_POLICY_DISABLED",
      "trafficSpec": {
        "aggrEgressPps": "AGGR_EGRESS_PPS",
        "aggrIngressPps": "AGGR_INGRESS_PPS",
        "avgPacketSize": "AVG_PACKET_SIZE",
        "maxPerGroupIngressPps": "MAX_PER_GROUP_INGRESS_PPS",
        "maxPerGroupSubscribers": "MAX_PER_GROUP_SUBSCRIBERS"
      }
    }
    

Replace the following values:

  * `DOMAIN_ACTIVATION_NAME`: a name for the domain activation
  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
  * `DOMAIN_NAME`: the name of the domain to activate
  * `ZONE`: the zone in which to activate the domain
  * `PLACEMENT_POLICY_DISABLED`: If you are activating a domain that is part of a domain group, then you can optionally include this field and set it to `true` to disable the creation of a placement policy. Otherwise, Google Cloud automatically creates placement policy that can optionally be [applied to new or existing multicast consumers](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).
  * Specify values for the `trafficSpec` object according to your needs for the multicast traffic in this zone. Google Cloud uses these parameters to determine the scale of your multicast infrastructure.

Before you specify these parameters, see the following:

    * Review the corresponding [limitations for multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/overview#limitations-domain-activation) described in the Cloud Multicast overview.
    * If you don't include the `trafficSpec` object in the request body, Google Cloud generates a minimal configuration that you can use for testing.
    * You can update the `trafficSpec` configuration later as described in [Update multicast domain parameters](https://docs.cloud.google.com/vpc/docs/multicast/update-domain-parameters).
    * While the fields in `trafficSpec` are optional, if you include any fields, then `aggrEgressPps` becomes a required field. If you include `trafficSpec` object with some fields, you must include `aggrEgressPps`.

For more information about each field, see the following:

    * `AGGR_EGRESS_PPS`: aggregate egress packets per second (pps) for all multicast groups in the domain in the specified zone. Egress refers to packets distributed from the multicast infrastructure to multicast consumers.

You can enter a value from 0 to 500000000 (500 million). The default is value is 1000000 (1 million). Default values for the other fields are set dynamically based on the value that you enter for this field.

**Note:** If you don't know your aggregate egress pps, then you can estimate it by using the following formula: `AGGR_EGRESS_PPS = AGGR_INGRESS_PPS * MAX_PER_GROUP_SUBSCRIBERS / 2`.
    * `AGGR_INGRESS_PPS`: aggregate ingress pps for all multicast groups in the domain in the specified zone. Ingress refers to packets sent from multicast producers to the multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `aggrIngressPps` can't be greater than the value of `aggrEgressPps`.

    * `AVG_PACKET_SIZE`: average packet size in bytes. You can enter a value from 64 to 1500.

    * `MAX_PER_GROUP_INGRESS_PPS`: maximum ingress pps for a single multicast group in the domain in the specified zone. Use this flag to specify the most active multicast group in the domain, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `maxPerGroupIngressPps` can't be greater than the value of `aggrIngressPps`.

    * `MAX_PER_GROUP_SUBSCRIBERS`: maximum number of multicast consumers for a single multicast group in the domain in the specified zone. Use this flag to specify the group with the most multicast consumers, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure. Providing this specification does not enforce a limit on the number of multicast consumers for a group.

You can enter a value from 1 to 500.




## What's next

  * To view the multicast domain configurations that you created, see [View multicast domain configurations](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-domain-configs).
  * [Update multicast domain configurations](https://docs.cloud.google.com/vpc/docs/multicast/update-configurations#domain)
  * [Create multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
