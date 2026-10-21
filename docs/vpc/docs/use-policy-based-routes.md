---
url: https://docs.cloud.google.com/vpc/docs/use-policy-based-routes/
title: Use policy-based routes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:15:55.379460+00:00
---

# Use policy-based routes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/use-policy-based-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use policy-based routes

Policy-based routes let you select a next hop based on more than a packet's destination IP address. This page describes how to create, list, describe, and delete policy-based routes.

## Before you begin

  * To use the command-line examples in this guide, install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).
  * You must [enable](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com) the [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest) in your project.
  * You need an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal). We recommend [enabling global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access) so that the internal passthrough Network Load Balancer does not drop packets from regions other than the one in which it is defined.



### Required roles

To get the permissions that you need to use policy-based routes, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create policy-based routes

When you create a policy-based route, you specify the following:

  * Route scope: the resources that the route can apply to.
  * Classification criteria: the source IP address ranges, destination IP address ranges, and protocols that determine which packets the route applies to. The policy-based route applies to packets that match _all_ of the specified classification criteria.
  * Next hop: a next hop internal passthrough Network Load Balancer or a next hop that [skips other policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option).




###  Console 

  1. In the Google Cloud console, go to **Routes**.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click **Route management**.

  3. Click **Create route**.

  4. Enter a name for the route.

  5. Optional: Enter a description.

  6. Click **Network** , and then select the network where you want to add the policy-based route.

  7. Click **Route type** , and then select **Policy-based route**.

  8. Select an IP version.

  9. In the **Route scope** section, do one of the following:

     * To make the route apply to all virtual machine (VM) instances, VLAN attachments for Cloud Interconnect, and Cloud VPN tunnels in the Virtual Private Cloud network, select **This route applies to all VM instances, VLAN attachments, and VPN tunnels**.

Google recommends caution when creating routes of this type. The route is applied to all egress packets that match the classification criteria, which can include egress traffic from the backend of the internal passthrough Network Load Balancer.

     * To make the route apply only to certain VM instances, select **This route only applies to VM instances** , and then enter the network tags of the VMs that this route should apply to. You can enter multiple network tags in a comma-separated list.

     * To make the route apply to all VLAN attachments for Cloud Interconnect in the route's VPC network, select **This route only applies to VLAN attachments**.

     * To make the route apply to VLAN attachments for Cloud Interconnect in a specific region, select **This route only applies to VLAN attachments** , and then select the region of the VLAN attachments. It is not possible to create a policy-based route that applies to a specific VLAN attachment.

  10. In the **Classification criteria** section, do the following:

     1. Enter a source IP range.
     2. Enter a destination IP range.
     3. Click **Protocol** , and then select the protocols that this route applies to.
  11. Enter a priority.

  12. In the **Next hop** section, click **Next hop** , and then do the following:

     * To specify a next hop internal passthrough Network Load Balancer, select **Specify a forwarding rule of the internal passthrough Network Load Balancer** , and then do the following:

       * To select a forwarding rule from a list of existing forwarding rules: 
         1. Select **In use by the forwarding rule of an internal load balancer in the current project**.
         2. Click **Forwarding rule IP address** , and then select an IP address that's associated with an internal load balancer in the selected project.
       * To enter an IP address:

         1. Select **Unused**.
         2. In the **Forwarding rule IP address** field, enter an IP address, without a prefix length. The IP address must come from one of the following sources:

            * The IP address ranges of the VPC network where you are creating this policy-based route.
            * The IP address ranges of a VPC network that is connected to the route's VPC network through VPC Network Peering.

You can specify an IP address that is already associated with an internal passthrough Network Load Balancer's forwarding rule, or you can specify an unused IP address and create the forwarding rule after you create this policy-based route.

     * To create a policy-based route that skips other policy-based routes, select **Skip other policy-based routes**.

  13. Click **Create**.




###  gcloud 

Use the [`policy-based-routes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create).

  * To apply the route to all VM instances, VLAN attachments for Cloud Interconnect, and Cloud VPN tunnels in the Virtual Private Cloud network, use the following command.

Google recommends caution when creating routes of this type. The route is applied to all egress packets that match the classification criteria, which can include egress traffic from the backend of the internal passthrough Network Load Balancer.
        
        gcloud network-connectivity policy-based-routes create ROUTE_NAME \
            --source-range=SOURCE_RANGE \
            --destination-range=DESTINATION_RANGE \
            --ip-protocol=PROTOCOL \
            --protocol-version=IP_VERSION \
            --network="projects/PROJECT_ID/global/networks/NETWORK" \
            --next-hop-ilb-ip=NEXT_HOP \
            --description=DESCRIPTION \
            --priority=PRIORITY
        

Replace the following:

    * `ROUTE_NAME`: the name of the policy-based route.
    * `SOURCE_RANGE`: the source IP CIDR range.
    * `DESTINATION_RANGE`: the destination IP CIDR range.
    * `PROTOCOL`: the protocol of traffic to forward. Options are `ALL`, `TCP`, or `UDP`. The default is `ALL`.
    * `IP_VERSION`: a single Internet Protocol version that this route applies to. Specify either `IPv4` or `IPv6`. The default is `IPv4`.
    * `PROJECT_ID`: the ID of the project.
    * `NETWORK`: the name of the network to apply the policy-based route to.
    * `NEXT_HOP`: a single IP address, without a prefix length, for the route's next hop internal passthrough Network Load Balancer. Specify an IPv4 address as a next hop for IPv4 traffic, or specify an IPv6 address for IPv6 traffic. The load balancer must be in either the same VPC network as the policy-based route or in a VPC network that is connected to the route's VPC network through VPC Network Peering.

If the route applies to IPv6 traffic, you must [set up the load balancer with subnets that have IPv6 address ranges](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-test-environment-ipv6).

    * `DESCRIPTION`: an optional description of the route.

    * `PRIORITY`: the priority of the policy-based route compared to other policy-based routes.

  * To apply the route only to certain VM instances, use the following command:
        
        gcloud network-connectivity policy-based-routes create ROUTE_NAME \
            --source-range=SOURCE_RANGE \
            --destination-range=DESTINATION_RANGE \
            --ip-protocol=PROTOCOL \
            --protocol-version=IP_VERSION \
            --network="projects/PROJECT_ID/global/networks/NETWORK" \
            --next-hop-ilb-ip=NEXT_HOP \
            --description=DESCRIPTION \
            --priority=PRIORITY \
            --tags=NETWORK_TAGS
        

Replace `NETWORK_TAGS` with one or more network tags of the VMs to apply the route to. You can include multiple network tags in a comma-separated list.

  * To apply the route only to VLAN attachments for Cloud Interconnect, use the following command. You can apply the route to either VLAN attachments for Cloud Interconnect in a specific region or to all VLAN attachments for Cloud Interconnect in a VPC network.
        
        gcloud network-connectivity policy-based-routes create ROUTE_NAME \
            --source-range=SOURCE_RANGE \
            --destination-range=DESTINATION_RANGE \
            --ip-protocol=PROTOCOL \
            --protocol-version=IP_VERSION \
            --network="projects/PROJECT_ID/global/networks/NETWORK" \
            --next-hop-ilb-ip=NEXT_HOP \
            --description=DESCRIPTION \
            --priority=PRIORITY \
            --interconnect-attachment-region=INTERCONNECT_REGION
        

Replace `INTERCONNECT_REGION` with the region of the VLAN attachments for Cloud Interconnect to apply the route to. To apply the policy-based route to all VLAN attachments for Cloud Interconnect in the route's VPC network, use `all`.

  * To specify a next hop that skips other policy-based routes for specific VMs that are identified by network tags, use the following command:
        
        gcloud network-connectivity policy-based-routes create ROUTE_NAME \
            --source-range=SOURCE_RANGE \
            --destination-range=DESTINATION_RANGE \
            --ip-protocol=PROTOCOL \
            --protocol-version=IP_VERSION \
            --network="projects/PROJECT_ID/global/networks/NETWORK" \
            --next-hop-other-routes=DEFAULT_ROUTING \
            --description=DESCRIPTION \
            --priority=PRIORITY \
            --tags=NETWORK_TAGS
        




###  API 

Send a `POST` request to the [`policyBasedRoutes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.policyBasedRoutes/create):
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/policyBasedRoutes?policyBasedRouteId=ROUTE_NAME
    

  * To apply the route to all VM instances, VLAN attachments for Cloud Interconnect, and Cloud VPN tunnels in the Virtual Private Cloud network, include the following request body.

Google recommends caution when creating routes of this type. The route is applied to all egress packets that match the classification criteria, which can include egress traffic from the backend of the internal passthrough Network Load Balancer.
        
        {
          "filter": {
            "srcRange": "SOURCE_RANGE",
            "destRange": "DESTINATION_RANGE",
            "ipProtocol": "PROTOCOL",
            "protocolVersion": "IP_VERSION"
          },
          "network": "projects/PROJECT_ID/global/networks/NETWORK",
          "nextHopIlbIp": "NEXT_HOP",
          "description": "DESCRIPTION",
          "priority": "PRIORITY"
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project.
    * `ROUTE_NAME`: the name of the policy-based route.
    * `SOURCE_RANGE`: the source IP CIDR range.
    * `DESTINATION_RANGE`: the destination IP CIDR range.
    * `PROTOCOL`: the protocol of traffic to forward. Options are `ALL`, `TCP`, or `UDP`. The default is `ALL`.
    * `IP_VERSION`: a single Internet Protocol version that the route applies to. Specify either `IPv4` or `IPv6`. The default is `IPv4`.
    * `NETWORK`: the name of the network to apply the policy-based route to. The route applies to egress traffic from instances in this network that meet the other classification criteria.
    * `NEXT_HOP`: a single IP address, without a prefix length, for the route's next hop internal passthrough Network Load Balancer. Specify an IPv4 address as a next hop for IPv4 traffic, or specify an IPv6 address for IPv6 traffic. The load balancer must be in either the same VPC network as the policy-based route or in a VPC network that is connected to the route's VPC network through VPC Network Peering.

If the route applies to IPv6 traffic, you must [set up the load balancer with subnets that have IPv6 address ranges](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-test-environment-ipv6).

    * `DESCRIPTION`: an optional description of the route.

    * `PRIORITY`: the priority of the policy-based route compared to other policy-based routes.

  * To apply the route only to certain VM instances, include the following request body:
        
        {
          "filter": {
            "srcRange": "SOURCE_RANGE",
            "destRange": "DESTINATION_RANGE",
            "ipProtocol": "PROTOCOL",
            "protocolVersion": "IP_VERSION"
          },
          "network": "projects/PROJECT_ID/global/networks/NETWORK",
          "nextHopIlbIp": "NEXT_HOP",
          "description": "DESCRIPTION",
          "priority": "PRIORITY",
          "virtualMachine": {
            "tags": [
              "NETWORK_TAGS"
            ]
          }
        }
        

Replace `NETWORK_TAGS` with one or more network tags. The policy-based route applies to egress traffic from instances that have at least one of these tags. You can include multiple tags in the following form: `"tag1","tag2","tag3"`.

  * To apply the route only to VLAN attachments for Cloud Interconnect, include the following request body. It is not possible to create a policy-based route that applies to a specific VLAN attachment.
        
        {
          "filter": {
            "srcRange": "SOURCE_RANGE",
            "destRange": "DESTINATION_RANGE",
            "ipProtocol": "PROTOCOL",
            "protocolVersion": "IP_VERSION"
          },
          "interconnectAttachment": {
            "region": "INTERCONNECT_REGION"
          },
          "network": "projects/PROJECT_ID/global/networks/NETWORK",
          "nextHopIlbIp": "NEXT_HOP",
          "description": "DESCRIPTION",
          "priority": "PRIORITY"
        }
        

Replace `INTERCONNECT_REGION` with the region of the VLAN attachments for Cloud Interconnect to apply this route to. To apply the policy-based route to all VLAN attachments for Cloud Interconnect in the route's VPC network, use `all`.

  * To specify a next hop that skips other policy-based routes for specific VMs that are identified by network tags, use the following command:
        
        {
          "filter": {
            "srcRange": "SOURCE_RANGE",
            "destRange": "DESTINATION_RANGE",
            "ipProtocol": "PROTOCOL",
            "protocolVersion": "IP_VERSION"
          },
          "network": "projects/PROJECT_ID/global/networks/NETWORK",
          "nextHopOtherRoutes": "DEFAULT_ROUTING",
          "description": "DESCRIPTION",
          "priority": "PRIORITY",
          "virtualMachine": {
            "tags": [
              "NETWORK_TAGS"
            ]
          }
        }
        




## Verify connectivity for a policy-based route

[Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) is a diagnostics tool that lets you check connectivity between endpoints in your network. It analyzes your configuration and, in some cases, performs run-time verification. Connectivity Tests supports policy-based routes. To run Connectivity Tests with your policy-based routes, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

## List policy-based routes

You can list policy-based routes to view all policy-based routes in a project or network and region.

###  Console 

  1. In the Google Cloud console, go to **Routes**.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

     * To view all policy-based routes in a VPC network and region, do the following:

       1. Click **Effective routes**.
       2. Click **Network** , and then select a network.
       3. Click **Region** , and then select a region.
       4. Click **View**.
     * To view all policy-based routes in a project, do the following:

       1. Click **Route management**.



###  gcloud 

Use the [`policy-based-routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/list).
    
    
    gcloud network-connectivity policy-based-routes list
    

###  API 

Send a `GET` request to the [`policyBasedRoutes.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.policyBasedRoutes/list).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/policyBasedRoutes
    

Replace `PROJECT_ID` with the ID of the project to list policy-based routes in.

## Describe policy-based routes

You can describe a policy-based route to view details about the route.

###  Console 

  1. In the Google Cloud console, go to **Routes**.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click **Effective routes**.

  3. Click **Network** , and then select a network.

  4. Click **Region** , and then select a region.

  5. Click **View**.

  6. Click the name of a policy-based route to view its details.




###  gcloud 

To describe a policy-based route, use the [`policy-based-routes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/describe).
    
    
    gcloud network-connectivity policy-based-routes describe NAME
    

Replace `NAME` with the name of the route to describe.

###  API 

Send a `GET` request to the [`policyBasedRoutes.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.policyBasedRoutes/get).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/policyBasedRoutes/ROUTE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `ROUTE_NAME`: the name of the policy-based route to describe.



## Delete policy-based routes

You can delete a policy-based route to remove it from a VPC network.

###  Console 

  1. In the Google Cloud console, go to **Routes**.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. Click **Effective routes**.

  3. Click **Network** , and then select a network.

  4. Click **Region** , and then select a region.

  5. Click **View**.

  6. Click the name of a policy-based route.

  7. Click **Delete** , and then click **Delete** again to confirm.




###  gcloud 

To delete a policy-based route, use the [`policy-based-routes delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/delete).
    
    
    gcloud network-connectivity policy-based-routes delete NAME
    

Replace `NAME` with the name of the route to delete.

###  API 

Send a `DELETE` request to the [`policyBasedRoutes.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.policyBasedRoutes/delete).
    
    
    DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/policyBasedRoutes/ROUTE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `ROUTE_NAME`: the name of the policy-based route to delete.



## Compatibility

Special configuration is necessary to use policy-based routes in the following ways.

### Use policy-based routes with GKE

If you create policy-based routes in VPC networks that have Google Kubernetes Engine (GKE) clusters, keep the following in mind:

  * Don't create policy-based routes whose destinations include cluster node or Pod IP addresses.
  * Don't create policy-based routes whose destinations include cluster control plane private endpoints. 
    * Some [public Google Kubernetes Engine (GKE) clusters have Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#public-cluster-psc) control plane private endpoints. For these clusters, by default, GKE creates the Private Service Connect control plane private endpoint in the primary IPv4 address range of the cluster's subnet. To choose a custom subnet range (of a subnet in the same region) for the Private Service Connect control plane private endpoint, see [Create a cluster and select the control plane IP range](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#create_a_cluster_and_select_the_control_plane_ip_range).
    * When you create a [private GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept), you specify an IP address range for the control plane private endpoint (`--master-ipv4-cidr`). Ensure that you don't create a policy-based route whose destination includes this range. For more information, see [Endpoints in private clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#endpoints_in_private_clusters).



### Policy-based routes and Private Service Connect for published services

Policy-based routes can't route traffic to [Private Service Connect endpoints for published services](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) or [Private Service Connect backends for published services](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends). When using policy-based routes and Private Service Connect for published services:

  * Use network tags so that policy-based routes apply to specific VMs.
  * Avoid creating policy-based routes with source or destination IP address ranges of `0.0.0.0/0`.
  * If you need to create a policy-based route with a destination range that includes the IP address of a Private Service Connect endpoint or backend, create a higher priority policy-based route that [skips other policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option). Configure the destination of the higher priority policy-based route with a more specific IP address range that includes the IP address of the Private Service Connect endpoint or backend.



### Policy-based routes and accessing Google APIs and services

Google Cloud does not support routing traffic to Google APIs and services through other VM instances or custom next hops—including to VM backends of next hop internal passthrough Network Load Balancers in policy-based routes.

If you use any of the following ways to access Google APIs and services, see the best practices that are listed in the following section:

  * Using [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) to access Google APIs and services
  * Accessing Google APIs and services [from VMs with external IP addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip)
  * Using [Private Service Connect endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints)
  * Using [Private Service Connect backends for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls)



#### Best practices

We recommend the following best practices for the preceding ways of accessing Google APIs and services:

  * Use network tags so that the policy-based routes apply to specific VMs.
  * Avoid creating policy-based routes with source or destination ranges of `0.0.0.0/0`.
  * If you create policy-based routes that include destination ranges that are used by Google APIs and services, Private Service Connect endpoints for Google APIs, or Private Service Connect backends for APIs, create higher priority policy-based routes that [skip other policy-based routes](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option). Set the destinations of these higher priority policy-based routes to match the IP addresses for Google APIs and services, Private Service Connect endpoints, or Private Service Connect backends that you use. IP address ranges used by Google APIs and services include the following: 
    * The [IP addresses for the default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults) used by Google APIs and services
    * The Private Google Access virtual IP addresses (VIPs): 
      * `private.googleapis.com` (199.36.153.8/30)
      * `restricted.googleapis.com` (199.36.153.4/30)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
