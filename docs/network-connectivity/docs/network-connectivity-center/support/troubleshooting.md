---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting/
title: Troubleshoot Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:31.456842+00:00
---

# Troubleshoot Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Troubleshoot Network Connectivity Center Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that you might find helpful if you run into problems using Network Connectivity Center, hybrid spokes, VPC spokes, NCC Gateway spokes, or Private Service Connect connection propagation.

For known limitations, see [NCC considerations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#considerations) on the overview page.

## Common issues with command syntax

When updating a spoke, you must specify the location that the spoke is in.

## Attach resources to spokes

For detailed requirements, recommendations, and considerations for creating spokes and attaching resources to them, see [Work with spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#working-with-spokes).

## Routes aren't distributed between regions

If routes aren't being distributed properly between regions, verify that the VPC network's [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-dynamic-routing) is set to `global`.

## Data transfer traffic doesn't flow between two non-Google Cloud networks

In this context, a non-Google Cloud network refers to your on-premises data center, a branch office, or another cloud provider's network.

If data transfer traffic isn't flowing between two locations, confirm that the following resources are correctly configured and working:

  * Verify the functionality of [HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status#checking-ha-tunnels) or [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/viewing-vlans) that are added as spokes.
  * Verify the [routes programmed between the two locations](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).
  * Verify that ASN assignments are set up as described in [ASN requirements for site-to-site data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/asn-requirements).
  * Verify that each spoke has the site-to-site data transfer field set to `true`.



## Duplicate route advertisements from BGP sessions

If there are duplicate route advertisements—some from BGP sessions participating in data transfer and some from sessions not participating in data transfer—then data transfer traffic might use ECMP to distribute traffic to all available next hops, even if those next hops aren't explicitly participating in data transfer.

## Cloud Interconnect connection to an unsupported location (non-Google Cloud network)

For an example of how to configure route advertisements when one of your redundant Cloud Interconnect connections is to an unsupported location, see [Configure external router to avoid unsupported locations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/optimal-route-advertisement).

## Troubleshoot network connectivity using Connectivity Tests

Connectivity Tests is a diagnostics tool that lets you check connectivity between endpoints in your network. It analyzes your configuration and in some cases performs run-time verification.

To analyze network configurations, Connectivity Tests simulates the expected forwarding path of a packet through your Virtual Private Cloud (VPC) network, Cloud VPN tunnels, VLAN attachments, or

You can use the Connectivity Tests configuration analysis to evaluate reachability for the following networks:

  * [From a non-Google Cloud network to a VPC network](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/test-between-networks#non-gcp2vpc) that are connected through NCC. In this context, a non-Google Cloud network is typically your on-premises data center or a branch office or another cloud provider's network.
  * [Test between VM instances through an NCC hub](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/test-through-ncc-hub)



Because Connectivity Tests doesn't have access to your on-premises network configuration, it can't verify the configuration of routes and firewall rules on your on-premises router. Thus, traffic from your on-premises network to your VPC network is always considered valid by the Connectivity Tests configuration analysis, and only configurations within Google Cloud are verified.

**Note:** Connectivity Tests doesn't support Private Service Connect connection propagation with NCC.

To run Connectivity Tests between two on-premises networks connected through NCC, see [Test from a non-Google Cloud network to a non-Google Cloud network](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#non-cloud-to-non-cloud).

For more information, see the [Connectivity Tests overview](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview).

## Troubleshoot hybrid spokes

The following issue can occur in Router appliance, VLAN attachment and VPN spokes.

### Configured hub subnets aren't advertised to an on-premises network

If the configured hub subnets aren't advertised to the on-premises network, check the hub route table of the hybrid spoke's group for the following issues:

  * If the subnets are displayed in the hub route table, do the following:

    * Make sure that the [BGP route policy](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview) hasn't dropped the subnet to be advertised.

    * Contact [Google Cloud Support](https://docs.cloud.google.com/support) to diagnose the underlying issue.

  * If the subnets aren't in the hub route table, do the following:

    * Check the include-export and exclude-export IP address ranges on the VPC spoke of the subnets. If the subnet is filtered by include-export ranges or exclude-export ranges, you can update the VPC spoke.



## Troubleshoot Router appliance

The following issues and solutions are unique to Router appliance.

The documentation for troubleshooting Cloud Router also applies to Router appliance, along with the issues described in the following sections.

For more information, see the following:

  * [Troubleshoot BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-sessions)
  * [Troubleshoot BGP peering](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering)
  * [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes)
  * [Troubleshoot Cloud Router log messages](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages)



### BGP sessions fail to establish

If BGP sessions between Cloud Router and Router appliance fail to establish, check for the following issues:

  * Make sure that a VM acting as a router appliance instance is configured as part of a spoke in Network Connectivity Center. To configure a router appliance instance as part of a spoke, see [Work with spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#working-with-spokes).
  * Check your firewall settings to ensure that TCP port `179` is allowed. To configure firewall settings for Router appliance, see [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances#create-ra-fw-rules).
  * Make sure that neither Cloud Router nor your router appliance instance are using link-local addresses (that is, `169.254.x.x`) to peer with each other. For guidance, see [IP addresses and router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances#ip-recommendations).
  * Make sure that Cloud Router has established two separate BGP sessions to your router appliance instance, one from each Cloud Router interface. The router appliance instance must advertise the same routes on both BGP sessions. If one of your BGP sessions goes down and your router appliance VM loses communication to Cloud Router, check the configuration of your Cloud Router interfaces. For more information, see [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances).



### Issues with internal IP addresses for BGP sessions on router appliance instances

If you discover issues related to your IP address configuration for router appliance instances, make sure that you have configured RFC 1918 internal IP addresses for BGP sessions between Cloud Router and the VMs acting as router appliance instances.

Router appliance instances don't use `169.254.x.x` addresses for BGP sessions. Instead, they must use IP addresses in the same VPC subnet as Cloud Router. For more information, see [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances).

## Troubleshoot VPC spokes

### Permissions

If permission is denied when creating a spoke in a different project from the hub, check with the hub administrator to confirm that you have been granted the required `networkconnectivity.groups.use` permission on the hub.

### VPC spoke creation failures

If your VPC spoke creation has failed, it could be due to one of the following reasons:

  * The VPC network is already peered with one or more of the existing spokes using VPC peering.
  * Subnets overlap with existing VPC spokes.
  * Subnets overlap with peers of existing VPC spokes.
  * You have exceeded the VPC spokes quota.
  * You have exceeded the routes per hub route table quota.
  * More than 16 export filters are specified.
  * Subnets in the VPC network are larger than one or more filters specified.



For quota-related errors, see [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas).

### VPC spoke creation failures after deleting a spoke

After you delete a spoke, you must wait for the cool-down period of at least 10 minutes before you can create a new spoke for the same VPC network attached to a different hub. This cool-down period isn't needed if the VPC network is added as a spoke to the same hub.

### Subnet creation failures in a VPC spoke

If you encounter subnet creation failure in a VPC spoke, it could be due to one of the following reasons:

  * There are overlapping subnets in other VPC spokes or peers of VPC spokes.
  * You have exceeded the routes per hub route table quota.
  * Subnets in the VPC network are larger than one or more filters specified.



### The VPC spoke is created but dataplane connectivity is missing

If your VPC spoke is showing as created, but dataplane connectivity is missing, it could be due to one of the following reasons:

  * The spoke is in a different project from the hub and the hub administrator hasn't accepted the spoke proposal.
  * All subnets in the VPC network are filtered and excluded from connectivity.
  * Destination subnets are filtered by their corresponding VPC spoke filters.



### The hub route table doesn't show some subnets in VPC spokes

If your hub route table doesn't show some of the subnets in the VPC spokes, it could be due to one of the following reasons:

  * The subnets are filtered using export filters.
  * The subnets were created within the last 5-10 minutes and the hub route table isn't refreshed yet.



### The VPC spoke update has failed

Make sure that your spoke updates comply with all the NCC [quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas); otherwise, the spoke update fails.

If a VPC spoke or producer VPC spoke is in a project different from the project that contains the hub, and a hub administrator hasn't enabled auto acceptance of proposals from the spoke project, a hub administrator must accept or reject a proposed update. For detailed information about how to check the status of the spoke update proposal, see [Check the status of a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status).

## Troubleshoot Private Service Connect connection propagation errors

Before investigating issues, familiarize yourself with the following pages:

  * [Private Service Connect connection propagation through NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview)
  * [Configure a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub)



### VM in one spoke can't access the Private Service Connect connection in another spoke

If a VM in one VPC spoke can't access the Private Service Connect endpoint in another spoke, make sure that the following conditions are met:

  * The `--export_psc` field is enabled in the hub.

To check if the `--export_psc` field is enabled in the hub, use the [`gcloud network-connectivity hubs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/describe).

###  gcloud 
        
        gcloud network-connectivity hubs describe HUB_NAME \
            --project=PROJECT_ID \
            --format='get(export_psc)'
        

Replace the following values:

    * `HUB_NAME`: the name of the hub
    * `PROJECT_ID`: the project ID where the hub resides

  * The IP address of the Private Service Connect endpoint isn't in any export exclude range of the hosting spoke. Private Service Connect endpoints that reside within the export exclude range aren't propagated.

To check the specified exclude export ranges of a spoke, use the [`gcloud network-connectivity spokes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/describe).

###  gcloud 
        
        gcloud network-connectivity spokes describe SPOKE_NAME \
            --global \
            --project=PROJECT_ID \
            --format='get(linked_vpc_network.exclude_export_ranges)'
        

Replace the following values:

    * `SPOKE_NAME`: the name of the spoke
    * `PROJECT_ID`: the project ID where the spoke resides

  * You haven't exceeded the NCC usage [quota](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas).

  * The `psc_connection_status` of the endpoint is in the `ACCEPTED` state. For information about connection statuses, see [Connection statuses](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#connection-statuses).

  * The propagated connection status of the endpoint in the spoke containing the VM is `READY`. If no status is showing up, check for the reasons in the You can't see the status of some target spokes section on this page. You can check the propagated connection status by using the [`gcloud network-connectivity hubs query-status` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status):

###  gcloud 
        
        gcloud network-connectivity hubs query-status HUB_NAME\
            --filter='psc_propagation_status.source_spoke="SOURCE_SPOKE_NAME" AND psc_propagation_status.target_spoke="TARGET_SPOKE_NAME" AND psc_propagation_status.source_forwarding_rule="ENDPOINT_NAME"
        

Replace the following values:

    * `HUB_NAME`: the name of the hub for which you want to check the connection propagation status
    * `SOURCE_SPOKE_NAME`: the name of the source spoke
    * `TARGET_SPOKE_NAME`: the name of the target spoke
    * `ENDPOINT_NAME`: the name of the endpoint

For detailed information about how to use these flags, see the `gcloud network-connectivity hubs query-status` command page.

  * The host VPC network of the Private Service Connect endpoint (source) is a VPC spoke in the hub.

  * The IP address of the Private Service Connect endpoint is an [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) address.




### You've exhausted the producer quota

If you see the `PRODUCER_QUOTA_EXHAUSTED` error message, you can ask the service producer to request a `PSC_ILB_CONSUMER_FORWARDING_RULES_PER_PRODUCER_NETWORK` quota increase. For details, see the [Per network](https://docs.cloud.google.com/vpc/docs/quota#per_network) section of the VPC documentation.

### You've exceeded the producer's propagated connection limit

If you see an error about exceeding the [propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit) of a service attachment, you can ask the service producer to [increase the limit](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#update-propagated-connection-limit). When a service producer updates the propagated connection limit, Google Cloud automatically checks if any pending propagated connections can be created.

### The producer NAT IP address space is exhausted

If you see the `PRODUCER_NAT_IP_SPACE_EXHAUSTED` error message, it means that you might need to ask the service producer to add NAT subnets. For information about adding subnets, see [Add or remove subnets from a published service](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#subnets).

### You've exhausted the consumer quota

If you see a `CONSUMER_QUOTA_EXHAUSTED` error message, contact the owner of the consumer VPC network and request a `PSC_PROPAGATED_CONNECTIONS_PER_VPC_NETWORK` quota increase.

### You've exceeded the Private Service Connect forwarding rules quota

If you see a `Quota limit PerProjectPerHubPscIlbConsumerForwardingRules has been exceeded` error message, you might not be able to do the following:

  * Create VPC spokes or enable the `--export_psc` flag in the hub.
  * Create a Private Service Connect forwarding rule in a VPC network that's a VPC spoke.



To avoid exceeding this quota, consider the following strategy for each VPC spoke that needs to export some Private Service Connect endpoints to the hub. In each region of the VPC spoke network, do the following:

  * Create one subnet for Private Service Connect endpoints that are shared with the hub.
  * Create another subnet for Private Service Connect endpoints that aren't shared with the hub.



When you add the VPC network to a hub as a spoke, you can add the IP address range of the subnet that hosts the subnet range within the VPC network to the exclude export filter so that any Private Service Connect endpoints hosted in this subnet range aren't shared with the hub.

### You can't see the status of some target spokes

If you don't see the status of some target spokes, it might be due to one of the following reasons:

  * The target spoke isn't a VPC spoke. Only VPC spokes, including VPC networks that are VPC spokes and also contain hybrid spokes, can receive propagated connections. A hybrid spoke in a routing VPC network that isn't also a VPC spoke can't receive propagated connections.

  * NCC only shows propagation status for each VPC spoke. If a VPC network is both a VPC spoke and contains hybrid spokes, check the propagation status of its VPC spoke to determine whether contained hybrid spokes have connectivity to propagated Private Service Connect endpoints.

  * If a VPC network is both the Private Service Connect producer VPC network and a VPC spoke on a hub that propagates its endpoints, NCC doesn't propagate its endpoints back to the producer VPC network itself.

  * The propagation is disallowed by the topology of the hub. For example, if the hub is configured to use star topology, the following conditions are also true:

    * Private Service Connect endpoints in the center group are propagated to all other VPC spokes.
    * Private Service Connect endpoints in the edge group are only propagated to VPC spokes in the center group.



## Troubleshoot VPC spokes route exchange

### VPC spokes and hybrid spokes are attached to the same hub but dataplane connectivity is missing

If the VPC spokes and hybrid spokes are attached to the same hub but dataplane connectivity is missing, it might be due to one of the following reasons:

  * The spoke is a cross-project spoke and the hub administrator hasn't accepted the spoke proposal.
  * All subnets in the VPC network are filtered and excluded from connectivity.
  * Auto propagation of VPC subnets isn't enabled or custom routes advertisement isn't set up.
  * The dynamic routes [quota](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-quotas) is exhausted.



### The hub route table doesn't show some dynamic routes or shows spurious dynamic routes

The hub route table might not show dynamic routes correctly due to one of the following reasons:

  * BGP routes have been advertised or withdrawn within the last five to ten minutes and the hub route table isn't updated yet.
  * The dynamic routes [quota](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-quotas) is exhausted.



### Hybrid spoke creation fails

If a hybrid spoke creation fails, it could be due to one of the following reasons:

  * The routing VPC network might be an existing VPC spoke to either the same hub or a different hub.
  * The routing VPC network might be implicitly associated with a different hub because of an existing hybrid spoke connected to that hub. Hybrid attachments from a VPC network can become spokes to only one hub.



### VPC spoke creation fails

VPC spoke creation might fail if the VPC spoke is implicitly associated with a hub as a routing VPC network.

### Error message

If you try to create a spoke and receive an error message that says `An internal error occurred`, to help troubleshoot the issue, contact [Google Cloud Support](https://docs.cloud.google.com/support).

## Troubleshoot NCC Gateway spokes

You can view the services and routers that are connected to your NCC Gateway by using the [`gcloud network-connectivity spokes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/describe) on the NCC Gateway spoke resource.

###  gcloud 
    
    
      gcloud network-connectivity spokes describe SPOKE_NAME \
          --region REGION
    

Replace the following:

  * `SPOKE_NAME`: the name of the NCC Gateway spoke
  * `REGION`: the region in which the spoke resides



The output is similar to the following:
    
    
    createTime: '2022-11-25T06:06:11.572019860Z'
    hub: projects/PROJECT/locations/REGION/hubs/HUB
    gateway:
      ipRangeReservation: 10.1.2.0/24
      asn: 65123
      routers:
        projects/PROJECT/locations/REGION/routers/ROUTER
      sacAttachment:
        projects/PROJECT/locations/REGION/sacAttachment/SAC-ATTACHMENT
    name: projects/PROJECT/locations/REGION/spoke/SPOKE
    state: ACTIVE
    uniqueId: 8ca10af0-ee69-43c2-b0b4-61e8f53d410b
    updateTime: '2023-12-27T21:26:47.786506888Z'
    

You can view the application VPC routing table and the created hub route table route that is propagated to your VPC route table with next hop as hub by using the [`gcloud compute routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/list):

###  gcloud 
    
    
      gcloud compute routes list \
          --filter="network=NETWORK"
    

Replace `NETWORK` with the name of the VPC network.

The output is similar to the following:
    
    
    NAME                                                  NETWORK  DEST_RANGE    NEXT_HOP  PRIORITY
    ncc-static-route-7296f3a4-cdc2-4560-a905-95cdb1d6833e  vpc-1    17.0.0.0/8   hub       0
    

You can view the hub route table for the spoke group and see the same created route pointing to the NCC Gateway spoke by using the [`gcloud network-connectivity hubs route-tables routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list):

###  gcloud 
    
    
      gcloud network-connectivity hubs route-tables routes list --hub=HUB_NAME \
          --route_table=ROUTE_TABLE
    

Replace the following values:

  * `HUB_NAME`: the name of the hub
  * `ROUTE_TABLE`: the ID of the route table that you want to list the routes for



### The hub route table doesn't show gateway advertised routes

If your hub route table doesn't show some of the gateway advertised routes with the gateway spoke as next hop, it could be due to routes not being installed in the data plane. This can cause connectivity issues between VPC spokes and on-premises applications connected through the NCC Gateway spoke. Try deleting and creating gateway advertised routes by following these steps:

  1. [Delete the advertised route](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes#delete_a_gateway_advertised_route).
  2. [Create an NCC Gateway advertised route](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes#create-gateway-advertised-routes).
  3. View the gateway advertised route associated with the NCC Gateway by using the [`gcloud beta network-connectivity spokes gateways advertised-routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/gateways/advertised-routes/list):

###  gcloud 
         
         gcloud beta network-connectivity spokes gateways advertised-routes list
             --region=REGION
         

Replace `REGION` with the region in which the spoke resides.

  4. Verify the gateway advertised route in the hub route table by using the [`gcloud network-connectivity hubs route-tables list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/list):

###  gcloud 
         
         gcloud network-connectivity hubs route-tables list \
             --hub=HUB_NAME \
             --route-table=ROUTE_TABLE
         

Replace the following values:

     * `HUB_NAME` with the name of the hub that you want to list the route table for
     * `ROUTE_TABLE`: the ID of the route table that you want to list the routes for

The output is similar to the following. An entry for your gateway advertised route must be present in the output.
    
    gcloud  network-connectivity hubs route-tables routes list --hub=HUB_NAME --route_table PROD
    IP_CIDR_RANGE  STATE    TYPE      NEXT_HOP   HUB       ROUTE_TABLE     PRIORITY
    10.0.0.0/8     ACTIVE   NCC_GW    NCC-GW-1   HUB_NAME  PROD            100
    




### Missing gateway advertised routes

If the traffic reaches endpoints in VPC spokes, but the traffic that should go to the gateway doesn't reach the partner or mobile applications, do the following:

  1. Confirm which gateway advertised routes are configured on the gateway.
  2. Check the hub route table of the source spoke group to confirm that there is a route that would send traffic to the gateway.
  3. If you don't see a route sending traffic to the gateway, [create gateway advertised routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes#create-gateway-advertised-routes).



### Missing custom route advertisements on the gateway Cloud Router

If the traffic from the edge or on-premises applications doesn't go to the gateway or the VLAN attachments, do the following:

  1. Check the received routes on the on-premises router and verify that the partner or mobile ranges are being received.
  2. Verify that application-side VPC ranges are being received.
  3. If you don't see the partner, mobile or the application-side ranges being received, add custom route advertisement on the gateway router. For details on how to set custom route advertisements, see [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments#create-cloud-router).



### Missing custom route advertisements on hybrid spokes

If traffic is reaching the endpoints on a hybrid spoke, but the traffic that should go to the gateway doesn't get sent to Google Cloud, do the following:

  1. Check the received routes on the router.
  2. Add custom route advertisement on the Cloud Router on the Google Cloud side for the hybrid spoke. For details on how to set custom route advertisements, see [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments#create-cloud-router).

Make sure that the IP address ranges configured for custom route advertisement match the gateway advertised routes.




For issues with Cloud Router, see [Troubleshoot Cloud Router log messages](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages).

For issues with Cloud Interconnect, see [Cloud Interconnect troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
