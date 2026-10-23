---
url: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services/
title: Access published services through endpoints \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:51.880402+00:00
---

# Access published services through endpoints  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access published services through endpoints 

This document explains how to [access services](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) in another VPC network by using Private Service Connect endpoints. You can connect to your own services, or those provided by other service producers, including by Google.

For more information about services, see [publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

## Before you begin

  * Read [About connecting to services by using endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints), including limitations.
  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.
  * You must [enable](https://console.cloud.google.com/apis/library/servicedirectory.googleapis.com) the [Service Directory API](https://docs.cloud.google.com/service-directory/docs/reference/rest) in your project.
  * You must [enable](https://console.cloud.google.com/apis/library/dns.googleapis.com) the [Cloud DNS API](https://docs.cloud.google.com/dns/docs/reference/v1) in your project.
  * Identify or create a [regular subnet](https://docs.cloud.google.com/vpc/docs/subnets#purpose) to use to assign an IP address for the endpoint. 
    * The subnet must be in the same region as the service that you want to connect to. 
    * You can use an IPv4 address from an IPv4-only subnet or a dual-stack subnet.
    * You can use a `/96` IPv6 address from an IPv6-only or dual-stack subnet if the subnet has an [internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).
    * The IP version of the IP address affects which published services the endpoint can connect to. For more information, see [IP version translation](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#ip-version-translation).
  * Egress firewall rules must permit traffic to the internal IP address of the endpoint. The [implied allow egress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) firewall rule permits egress to any destination IP address. If you've created any egress deny firewall rules in your VPC network, or if you've created hierarchical firewall policies which modify the implied allowed egress behavior, access to the endpoint might be affected. Create a specific egress allow firewall rule or policy to permit traffic to the service endpoint's internal IP address destination.
  * You must have the URI of the service attachment for the service. For example, `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`



### Required roles

If you're creating the endpoint in the same project as the subnet that you're connecting it to, see Required roles for your project.

If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) and are creating the endpoint in a service project, and connecting it to a subnet in the host project, you need the following roles:

  * Required roles for your project granted on the service project
  * Additional required roles for Shared VPC configurations granted on the host project.



### Required roles for your project

To get the permissions that you need to manage endpoints that access published services, ask your administrator to grant you the following IAM roles: 

  * Create, view, and delete endpoints: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on your project 
  * Automatically or manually configure DNS entries for an endpoint: 
    * [DNS Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`) on your project
    * [Service Directory Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.editor) (`roles/servicedirectory.editor`) on your project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage endpoints that access published services. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage endpoints that access published services:

  * To create, view, and delete endpoints: 
    * `compute.networks.use` on your project
    * `compute.subnetworks.use` on your project
    * `compute.addresses.createInternal` on your project
    * `compute.addresses.deleteInternal` on your project
    * `compute.addresses.get` on your project
    * `compute.addresses.list` on your project
    * `compute.addresses.use` on your project
    * `compute.forwardingRules.create` on your project
    * `compute.forwardingRules.delete` on your project
    * `compute.forwardingRules.get` on your project
    * `compute.forwardingRules.list` on your project
    * `compute.forwardingRules.pscCreate` on your project
    * `compute.forwardingRules.pscDelete` on your project
    * `compute.regionOperations.get` on your project
    * `servicedirectory.namespaces.create` on your project
    * `servicedirectory.namespaces.delete` on your project
    * `servicedirectory.services.create` on your project
    * `servicedirectory.services.delete` on your project
  * To automatically or manually configure DNS entries for an endpoint: 
    * `dns.managedZones.create` on your project
    * `dns.managedZones.delete` on your project
    * `dns.networks.bindPrivateDNSZone` on your project
    * `servicedirectory.namespaces.associatePrivateZone` on your project
  * To access the Private Service Connect page in the Google Cloud console: 
    * `compute.forwardingRules.list` on your project
    * `compute.globalForwardingRules.list` on your project
    * `compute.networkEndpointGroups.list` on your project
    * `compute.regionNetworkEndpointGroups.list` on your project
    * `compute.urlMaps.list` on your project
    * `compute.backendService.list` on your project
    * `compute.regionBackendService.list` on your project
    * `compute.backendBucket.list` on your project
    * `compute.targetHttpProxy.list` on your project
    * `compute.targetHttpsProxy.list` on your project
    * `compute.regionTargetTcpProxy.list` on your project
    * `compute.targetTcpProxy.list` on your project
    * `compute.targetSslProxy.list` on your project
    * `compute.sslCertificate.list` on your project
    * `compute.sslPolicy.list` on your project
    * `compute.regionHealthCheck.list` on your project
    * `compute.healthCheck.list` on your project
    * `compute.httpHealthCheck.list` on your project
    * `compute.httpsHealthCheck.list` on your project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Additional required roles for Shared VPC configurations

If you're creating an endpoint in a service project that uses an IP address from a host project subnet, you need the following permissions in addition to the Roles for your project (the service project).

To get the permissions that you need to manage endpoints that access published services, ask your administrator to grant you the following IAM roles: 

  * Create, view, and delete endpoints that use a host project IP address: [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) on the host project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage endpoints that access published services. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage endpoints that access published services:

  * To create, view, and delete endpoints that use a host project IP address: 
    * `compute.networks.use` on the host project
    * `compute.subnetworks.use` on the host project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an endpoint

An endpoint connects to services in another VPC network using a Private Service Connect forwarding rule. Each forwarding rule counts toward the [per project quota](https://docs.cloud.google.com/vpc/docs/quota#per_project) for Private Service Connect forwarding rules to access services in another VPC network.

When you create an endpoint, it is automatically registered with [Service Directory](https://docs.cloud.google.com/service-directory/docs/overview), using a namespace that you choose, or the default namespace, `goog-psc-default`.

If you want to make the endpoint available from more than one region, turn on [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access).

You can only update the global access field of endpoints for published services. If you want to update other fields, delete the endpoint, and then create a new one.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click **Connect endpoint**.

  4. For **Target** , select **Published service**.

  5. For **Target service** , enter the service attachment URI that you want to connect to.

The service attachment URI is in this format: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`

  6. For **Endpoint name** , enter a name to use for the endpoint.

  7. Select a **Network** for the endpoint.

  8. Select a **Subnetwork** for the endpoint.

  9. Select an **IP address** for the endpoint. If you need a new IP address, you can create one:

     1. Click the **IP address** drop-down menu and select **Create IP address**.
     2. Enter a **Name** and optional **Description** for the IP address.
     3. Select an **IP version**.
     4. If you're creating an IPv4 address, select **Assign automatically** or **Let me choose**.

If you selected **Let me choose** , enter the **Custom IP address** you want to use.

     5. Click **Reserve**.

  10. To make the endpoint available from any region, select **Enable global access**.

  11. Select a **Namespace** from the drop-down list or create a new namespace.

The **Region** is populated based on the selected subnetwork.

  12. Click **Add endpoint**.




###  gcloud 

  1. Reserve an internal IP address to assign to the endpoint.
         
         gcloud compute addresses create ADDRESS_NAME \
             --region=REGION \
             --subnet=SUBNET \
             --ip-version=IP_VERSION
         

Replace the following:

     * `ADDRESS_NAME`: the name to assign to the reserved IP address.

     * `REGION`: the region for the endpoint IP address. This must be the same region that contains the service producer's service attachment.

     * `SUBNET`: the name of the subnet for the endpoint IP address.

     * `IP_VERSION`: the IP version of the IP address, which can be either `IPV4` or `IPV6`. `IPV4` is the default. To specify `IPV6`, the IP address must be connected to a [subnet with an internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  2. Create a forwarding rule to connect the endpoint to the service producer's service attachment. By default, endpoints are available only from their own region. To make an endpoint available from any region, use the `--allow-psc-global-access` flag.

     * Create an endpoint that can be accessed only from its own region.
           
           gcloud compute forwarding-rules create ENDPOINT_NAME \
               --region=REGION \
               --network=NETWORK_NAME \
               --address=ADDRESS_NAME \
               --target-service-attachment=SERVICE_ATTACHMENT \
               [ --service-directory-registration=projects/PROJECT_ID/locations/REGION/namespaces/NAMESPACE ]
           

     * Create an endpoint that can be accessed from any region.
           
           gcloud compute forwarding-rules create ENDPOINT_NAME \
               --region=REGION \
               --network=NETWORK_NAME \
               --address=ADDRESS_NAME \
               --target-service-attachment=SERVICE_ATTACHMENT \
               --allow-psc-global-access \
               [ --service-directory-registration=projects/PROJECT_ID/locations/REGION/namespaces/NAMESPACE ]
           

Replace the following:

     * `ENDPOINT_NAME`: the name to assign to the endpoint.

     * `REGION`: the region for the endpoint. This must be the same region that contains the service producer's service attachment.

     * `NETWORK_NAME`: the name of the VPC network for the endpoint.

     * `ADDRESS_NAME`: the name of the reserved IPv4 or `/96` IPv6 address.

     * `SERVICE_ATTACHMENT`: the URI of the service producer's service attachment. For example: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`

     * `PROJECT_ID`: your project ID.

     * `NAMESPACE`: the Service Directory namespace that you want to use. If you specify a namespace that doesn't exist, the namespace is created.

If you omit the `--service-directory-registration` flag, the default namespace of `goog-psc-default` is used.




###  API 

  1. Reserve an internal IP address to assign to the endpoint.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses
         
         
         {
           "name": "ADDRESS_NAME",
           "addressType": "INTERNAL",
           "subnetwork": "SUBNET_URI",
           "ipVersion": "IP_VERSION"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID.

     * `REGION`: the region for the endpoint. This must be the same region that contains the service producer's service attachment.

     * `ADDRESS_NAME`: the name to assign to the reserved IP address.

     * `SUBNET_URI`: the subnet for the IP address. Use the [subnetworks.list method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/list) or `gcloud compute networks subnets list --uri` to find the URLs of your networks.

     * `IP_VERSION`: the IP version of the IP address, which can be either `IPV4` or `IPV6`. `IPV4` is the default. To specify `IPV6`, the IP address must be connected to a [subnet with an internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  2. Create a forwarding rule to connect the endpoint to the service producer's service attachment. By default, endpoints are available only from their own region. To make an endpoint available from any region, set `allowPscGlobalAccess` to `true`.

     * Create an endpoint that can be accessed only from its own region.
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules
           
           
           {
             "name": "ENDPOINT_NAME",
             "IPAddress": "ADDRESS_URI",
             "target": "SERVICE_ATTACHMENT",
             "network": "NETWORK_URI",
             "serviceDirectoryRegistrations": [
                 {
                     "namespace": "NAMESPACE"
                 }
             ]
           }
           

     * Create an endpoint that can be accessed from any region.
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules
           
           
           {
             "name": "ENDPOINT_NAME",
             "IPAddress": "ADDRESS_URI",
             "target": "SERVICE_ATTACHMENT",
             "network": "NETWORK_URI",
             "allowPscGlobalAccess": true,
             "serviceDirectoryRegistrations": [
                 {
                     "namespace": "NAMESPACE"
                 }
             ]
           }
           

Replace the following:

     * `PROJECT_ID`: your project ID.

     * `REGION`: the region for the endpoint.

     * `ENDPOINT_NAME`: the name to assign to the endpoint.

     * `ADDRESS_URI`: the URI of the reserved IPv4 or `/96` IPv6 address.

     * `SERVICE_ATTACHMENT`: the URI of the service producer's service attachment. For example: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`

     * `NETWORK_URI`: the VPC network for the endpoint. Use the [network.list method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/list) or `gcloud compute networks list --uri` to find the URI of your network.

     * `NAMESPACE`: the namespace for the endpoint. If you specify a namespace that doesn't exist, the namespace is created. If you omit the `namespace` field, the default namespace of `goog-psc-default` is assigned.




## Create an endpoint in a Shared VPC service project

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can create endpoints in Shared VPC service projects that use IP addresses from connected [Shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks). Creating endpoints of this type is not available in the Google Cloud console. You must use the Google Cloud CLI or send an API request. For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#shared-vpc).

This example shows how to create an endpoint with an IP address from a Shared VPC network that can be accessed from a single region. To enable global access, or to choose a namespace for Service Directory, see Create an endpoint.

###  gcloud 

  1. Reserve an internal IP address to assign to the endpoint. Create the address resource in the service project, specifying a subnet in the host project.

The IP address must be in the same region as the service producer's service attachment.
         
         gcloud compute addresses create ADDRESS_NAME \
             --region=REGION \
             --subnet=projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET \
             --ip-version=IP_VERSION
         

Replace the following:

     * `ADDRESS_NAME`: the name to assign to the reserved IP address.
     * `REGION`: the region for the endpoint IP address. This must be the same region that contains the service producer's service attachment.
     * `HOST_PROJECT`: the project ID of the host project.
     * `HOST_SUBNET`: the name of the host project subnet that provides the endpoint IP address.
     * `IP_VERSION`: the IP version of the IP address, which can be either `IPV4` or `IPV6`. `IPV4` is the default. To specify `IPV6`, the IP address must be connected to a [subnet with an internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).
  2. To create the endpoint in the service project, do one of the following:

     * If you have permission to use all subnets in the host project, use the following command:
           
           gcloud compute forwarding-rules create ENDPOINT_NAME \
               --region=REGION \
               --network=projects/HOST_PROJECT/global/networks/HOST_NETWORK \
               --address=projects/SERVICE_PROJECT/regions/REGION/addresses/ADDRESS_NAME \
               --target-service-attachment=SERVICE_ATTACHMENT
           

Replace the following:

       * `ENDPOINT_NAME`: the name to assign to the endpoint.
       * `REGION`: the region for the endpoint. This must be the same region that contains the service producer's service attachment.
       * `HOST_PROJECT`: the project ID of the Shared VPC network's project.
       * `HOST_NETWORK`: the name of the Shared VPC network that contains the endpoint's IP address.
       * `SERVICE_PROJECT`: the ID of the service project.
       * `ADDRESS_NAME`: the name of the reserved IPv4 or `/96` IPv6 address.
       * `SERVICE_ATTACHMENT`: the URI of the service producer's service attachment. For example: `projects/PRODUCER_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`
     * If you have permission to use only some subnets in the host project, specify a shared subnet by using the following command:
           
           gcloud compute forwarding-rules create ENDPOINT_NAME \
               --region=REGION \
               --subnet=projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET \
               --address=projects/SERVICE_PROJECT/regions/REGION/addresses/ADDRESS_NAME \
               --target-service-attachment=SERVICE_ATTACHMENT
           

Replace `HOST_SUBNET` with the name of the subnet that contains the endpoint's IP address.




###  API 

  1. Reserve an internal IP address to assign to the endpoint. Create the address resource in the service project, specifying a subnet in the host project.
         
         POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT/regions/REGION/addresses
         
         
         {
             "name": "ADDRESS_NAME",
             "addressType": "INTERNAL",
             "subnetwork": "projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET",
             "ipVersion": "IP_VERSION"
         }
         

Replace the following:

     * `SERVICE_PROJECT`: the ID of the service project.

     * `REGION`: the region for the endpoint. This must be the same region that contains the service producer's service attachment.

     * `ADDRESS_NAME`: the name to assign to the reserved IP address.

     * `HOST_PROJECT`: the ID of the host project.

     * `HOST_SUBNET`: the subnet in the host project.

     * `IP_VERSION`: the IP version of the IP address, which can be either `IPV4` or `IPV6`. `IPV4` is the default. To specify `IPV6`, the IP address must be connected to a [subnet with an internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  2. To create the endpoint in the service project, do one of the following:

     * If you have permission to use all subnets in the host project, make the following request:
           
           POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT/regions/REGION/forwardingRules
           
           
           {
             "name": "ENDPOINT_NAME",
             "IPAddress": "projects/SERVICE_PROJECT/regions/REGION/addresses/ADDRESS_NAME",
             "target": "SERVICE_ATTACHMENT",
             "network": "projects/HOST_PROJECT/global/networks/HOST_NETWORK"
           }
           

Replace the following:

       * `SERVICE_PROJECT`: the service project ID.
       * `REGION`: the region for the endpoint. This must be the same region that contains the service producer's service attachment.
       * `ENDPOINT_NAME`: the name to assign to the endpoint.
       * `SERVICE_PROJECT`: the ID of the service project.
       * `ADDRESS_NAME`: the name of the reserved IPv4 or `/96` IPv6 address.
       * `SERVICE_ATTACHMENT`: the URI of the service producer's service attachment. For example: `projects/PRODUCER_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`
       * `HOST_PROJECT`: the ID of the host project.
       * `HOST_NETWORK`: the name of the Shared VPC network that contains the endpoint's IP address.
     * If you have permission to use only some subnets in the host project, specify a shared subnet by making the following request:
           
           POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT/regions/REGION/forwardingRules
           
           
           {
             "name": "ENDPOINT_NAME",
             "IPAddress": "projects/SERVICE_PROJECT/regions/REGION/addresses/ADDRESS_NAME",
             "target": "SERVICE_ATTACHMENT",
             "subnetwork": "projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET"
           }
           

Replace `HOST_SUBNET` with the name of the subnet that contains the endpoint's IP address.




## List endpoints

You can list all configured endpoints.

###  Console

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

The endpoints are displayed.




###  gcloud 
    
    
    gcloud compute forwarding-rules list \
        --filter 'target~serviceAttachments'
    

The output is similar to the following:
    
    
    NAME  REGION  IP_ADDRESS  IP_PROTOCOL  TARGET
    RULE          IP          TCP          REGION/serviceAttachments/SERVICE_NAME
    

###  API 

This API call returns all forwarding rules, not only endpoints used to access services.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules
    

Replace the following:

  * `PROJECT_ID`: the project that contains the endpoint.
  * `REGION`: the region for the endpoint.



## View endpoint details

You can view all the configuration details of an endpoint, including the endpoint's [connection status](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#connection-statuses) and URI.

To find a Private Service Connect endpoint's ID-based URI, use the Google Cloud CLI or send an API request. The ID-based URI is displayed in the `selfLinkWithId` field. The service producer might need this URI if the service attachment's consumer accept list is configured to accept consumers based on individual Private Service Connect endpoints.

###  Console

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click the endpoint that you want to view.




###  gcloud 
    
    
    gcloud compute forwarding-rules describe \
        ENDPOINT_NAME --region=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: the name of the endpoint.
  * `REGION`: the region for the endpoint.



###  API 
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules/ENDPOINT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project that contains the endpoint.
  * `REGION`: the region for the endpoint.
  * `ENDPOINT_NAME`: the name of the endpoint.



## Label an endpoint

You can manage labels for endpoints. For detailed instructions, see [labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources).

## Delete an endpoint

You can delete an endpoint.

However, the following Service Directory configurations are _not_ deleted when you delete the endpoint:

  * Service Directory namespace
  * Service Directory DNS zone



The Service Directory namespace and Service Directory DNS zone can be used by other services. Check that the namespace is empty before you [delete the Service Directory namespace](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#delete_a_namespace) or [delete the Service Directory DNS zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone#delete_the_zone).

**Note:** When you delete a project, all resources in the project, including endpoints, are marked for deletion. However, the resources are not immediately deleted. For more information about project deletion, see [Shutting down projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

###  Console

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Select the endpoint that you want to delete, and then click **Delete**.




###  gcloud 
    
    
    gcloud compute forwarding-rules delete ENDPOINT_NAME \
        --region=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: the name of the endpoint.
  * `REGION`: the region for the endpoint.



###  API 
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules/ENDPOINT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project that contains the endpoint.
  * `REGION`: the region for the endpoint.
  * `ENDPOINT_NAME`: the name of the endpoint.



## Access endpoints from hybrid networks

Clients in networks that are connected to Google Cloud with VLAN attachments for Cloud Interconnect or Cloud VPN tunnels can reach Private Service Connect endpoints. 

  * The VLAN attachment or Cloud VPN tunnel must terminate in the same VPC network (or Shared VPC network) as the endpoint. Clients in peered VPC networks cannot reach endpoints.

  * Client traffic from VLAN attachments or Cloud VPN tunnels can reach endpoints in another region if [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) is configured.

  * Both Dataplane v1 and Dataplane v2 are supported for the VLAN attachments. For more information about Dataplane versions, see [Dataplane v2](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#dataplaneVersion).




If you want to access the endpoint by using its DNS name, you must configure systems in the other network so that they can make queries to your private DNS zones.

If you implemented the private DNS zones by using Cloud DNS, complete the following steps:

  * Create an [inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in) in the VPC network to which your other network connects.

  * Identify the [inbound forwarder entry points](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints) in the region where your VLAN attachment or Cloud VPN tunnel is located, in the VPC network to which your other network connects.

  * Configure systems and DNS name servers in the other network to forward the [DNS names for the endpoint](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer) to an inbound forwarder entry point in the same region as the VLAN attachment or Cloud VPN tunnel that connects to the VPC network.




## View Service Directory DNS zones

If the prerequisites for [automatic DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer) are met, a DNS zone is created with a name in the format `NAMESPACE--REGION`.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/networking/dns/zones/)

  2. Look for a private zone with the name `NAMESPACE--REGION`.




###  gcloud 

  * Run the following command to list all private DNS zones:
        
        gcloud dns managed-zones list \
            --filter="visibility=private"
        

  * Run the following command to get details for a zone with the name `NAMESPACE--REGION`.
        
        gcloud dns managed-zones describe NAMESPACE--REGION
        




If the zone is not present, view the details for the endpoint and check if the endpoint configuration includes a value for the namespace.

  * If the endpoint has a namespace configuration, see Configure a Service Directory DNS zone.

  * If the endpoint does not have a namespace configuration, see Register an endpoint with Service Directory.




## Other ways to configure DNS

If the prerequisites for [automatic DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer) are not met, you can create DNS entries in other ways:

  * If the endpoint has a namespace configured, see Configure a Service Directory DNS zone.

  * If the endpoint does not have a namespace configured, see Register an endpoint with Service Directory.

  * If you prefer to manually configure DNS, see Configure DNS manually.




### Configure a Service Directory DNS zone

If an endpoint is registered with Service Directory, but the published service that it connects to does not have a domain name configured, no DNS changes are made.

If you want to replicate the [automatic DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer), you can manually configure a Service Directory DNS zone that is backed by the Service Directory namespace. After the zone is created, DNS entries for the endpoint are automatically created.

Create a [Service Directory DNS zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone) with the following configuration:

  * Zone name: Specify `NAMESPACE--REGION`, where `NAMESPACE` is the namespace that the endpoint is registered to, and `REGION` is the region where the endpoint is created.

  * DNS name: The DNS domain that the service producer is using for their published services. Check with the service producer for this information.

The DNS name might have the format `REGION.p.DOMAIN`. For example, if the service producer's public domain is `example.com`, and their published service is in `us-west1`, then we recommend that they make their service available using `us-west1.p.example.com` domain names. Include a trailing dot—for example, `us-west1.p.example.com.`

  * Service Directory namespace: The namespace that you configured for this endpoint.




View the endpoint details to find the Service Directory namespace and region.

With this configuration, if you have configured a Service Directory DNS zone with the `us-west1.p.example.com` DNS name, and you create an endpoint with the name `analytics`, a DNS record for `analytics.us-west1.p.example.com` is automatically created.

### Register an endpoint with Service Directory

New endpoints are automatically registered with Service Directory. However, if a endpoint was created before automatic registration with Service Directory was enabled, this configuration might be missing.

You can delete the endpoint and create a new one, which is registered with Service Directory automatically.

Or you can follow these steps to register an existing endpoint with a Service Directory namespace.

  1. Create a [Service Directory namespace](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configuring_a_namespace) for the endpoint, `NAMESPACE`.

  2. Create a [Service Directory service](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configuring_a_service) for the endpoint, `SERVICE_NAME`.

For the service, use the same name as the name of the forwarding rule used for the endpoint, `ENDPOINT_NAME`.

  3. Create a [Service Directory endpoint](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configuring_an_endpoint), using the name `default` and use the IP address and port (`443`) of the endpoint.




After you have registered the endpoint with Service Directory, follow the instructions to Configure a Service Directory DNS zone.

### Configure DNS manually

If you've prevented automatic DNS configuration, or if it is not enabled in your configuration, you can use [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) to manually create DNS records

For more information, see the following pages:

  * [Access Control](https://docs.cloud.google.com/dns/docs/access-control#roles): the [DNS Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`) provides the permissions needed to create DNS zones and records.

  * [Create a private zone](https://docs.cloud.google.com/dns/zones#create-private-zone).

    * When you configure a private zone, you provide a DNS name. Use the DNS domain that the service producer is using for their published services. Check with the service producer for this information.

It might have this format: `REGION.p.DOMAIN`. For example, if the service producer's public domain is `example.com`, and their published service is in `us-west1`, then we recommend that they make their service available using `us-west1.p.example.com` domain names.

  * [Add a record](https://docs.cloud.google.com/dns/docs/records#adding_a_record).




## Known issues

### Unhealthy backends receive traffic with global access endpoints

It's possible to connect a [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) endpoint to a published service that's not configured for global access. However, health checks don't work correctly in this configuration. As a result, traffic might be sent to unhealthy backends and dropped.

Only enable global access for an endpoint if you know that the service attachment's load balancer is configured for global access.

If your endpoint is affected by this issue, do one of the following:

  * If you don't want to use global access, [disable global access for your endpoint](https://docs.cloud.google.com/vpc/docs/manage-endpoints-published-services#disable-global-access).
  * If you want to use global access, ask the service producer to [enable global access for the load balancer's forwarding rule](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#global-access-service-attachments).



Turning off global access for an endpoint doesn't interrupt network traffic for workloads in the same region as the endpoint. However, after global access is disabled, clients from other regions can't access the endpoint.

## Troubleshooting

### Private DNS zone creation fails

When you create an endpoint, a Service Directory DNS zone is created. Zone creation can fail for these reasons:

  * You haven't enabled the Cloud DNS API in your project.

  * You don't have the required permissions to create a Service Directory DNS zone.

  * A DNS zone with the same zone name exists in this VPC network.

  * A DNS zone for the same domain name already exists in this VPC network.




To manually create the Service Directory DNS zone, do the following:

  1. Verify that the Cloud DNS API is [enabled](https://console.cloud.google.com/apis/library/dns.googleapis.com) in your project.

  2. Verify that you have the required permissions to create the Service Directory DNS zone:

     * `dns.managedZones.create`
     * `dns.networks.bindPrivateDNSZone`
     * `servicedirectory.namespaces.associatePrivateZone`
  3. If there is a conflicting zone, but it is no longer needed, [delete the DNS zone](https://docs.cloud.google.com/dns/docs/zones#deleting_a_managed_zone).

  4. Create a Service Directory DNS zone that is backed by the Service Directory namespace associated with your endpoint.




### Endpoint connection status is pending

A `PENDING` connection status typically means that the producer's service attachment has received your connection request, but the connection is not yet accepted. An endpoint with the `PENDING` connection status must transition to `ACCEPTED` before traffic can flow between your VPC network and the published service.

If your connection status doesn't transition from `PENDING`, the troubleshooting steps depend on the type of service that you connect to:

  * **For Google published services** : Check the documentation of the [service that you are connected to](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#google-services). The documentation might contain service-specific steps to resolve the issue. For example, you might need to do the following: 
    * **Update the consumer accept list** : Some services require the consumer to update the service attachment's consumer accept list through an API that is specific to the service. For an example, see [Updating the consumer accept list for an Apigee instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc#updating-the-consumer-accept-list-for-an-apigee-instance).
    * **Recreate the service instance** : Some services don't support dynamic updates. For example, when you create a Dataproc Metastore service, you specify the subnetworks from which you can access the service with endpoints. If you want to access the service from another subnet, [you must recreate the service](https://docs.cloud.google.com/dataproc-metastore/docs/psc-ilb#limitations).
    * **Verify feature support** : In some environments, access is restricted by the service's architecture. For example, when you access the GKE control plane with endpoints, access [is only supported from the same VPC network as the GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#ip-based_endpoints).
  * **For third-party and self-managed services** : Check the documentation of the [service that you are connected to](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#third-party-services). If the documentation doesn't provide a solution, contact the service producer and ask them to verify their service attachment configuration. If the service is configured to require explicit authorization, the producer might need to do the following: 
    * **Authorize the consumer project** : The service might require your project, VPC network, or endpoint to be explicitly [added to the service attachment's consumer accept list](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#access).
    * **Increase your connection limit** : You might have exceeded the [consumer accept list limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-limits) that the producer configured for your endpoint's project or VPC network.



### Endpoint creation fails when global access is configured

Not all Private Service Connect published services support endpoints with global access. If you create an endpoint with global access and the published service doesn't support it, you see this error message:

`Private Service Connect global access is not supported for the given forwarding rule, since its producer service does not support consumer global access.`

Create the endpoint without the global access option.

### Endpoint creation succeeds, but connectivity is not established

If you successfully create an endpoint for published services but connectivity is not established, check the endpoint's [connection status](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#connection-statuses). The connection status might indicate steps that you can take to resolve the issue.

### Endpoint connection status is accepted, but traffic doesn't flow

If an endpoint has an `ACCEPTED` connection status, but traffic can't reach the published service, the service producer might have recently updated the target service of the service attachment. During a target service update, traffic is briefly interrupted. For information about recent or ongoing target service updates, or to verify the state of the service, contact the service producer.

### Propagated connection errors

For information about troubleshooting propagated connections, see [Troubleshoot Private Service Connect connection propagation errors](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshoot-psc-propagation-errors).

### Endpoint has performance issues or connection timeouts

If your endpoint has performance issues or intermittent connection timeouts, it might be due to dropped packets. You can investigate dropped packets by checking the metrics that are described in the following sections.

#### Dropped packets to published service

The [`private_service_connect/consumer/dropped_sent_packets_count` metric](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#compute/private_service_connect/consumer/dropped_sent_packets_count) tracks packets from a Private Service Connect consumer such as an endpoint to a published service that are dropped because the endpoint exceeded its maximum connections to the service.

If an endpoint reports values for this metric, consider the following solutions to address specific limits described in [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections):

  * Reduce the number of connections through this endpoint.
  * Ask the service producer to increase the capacity of the published service—for example, by adding more virtual machine (VM) instances or network endpoints.
  * For IPv4 connections, if the service attachment is configured with one NAT IP address per endpoint or backend (the default), ask the service producer to do both of the following: 
    * [Update the service attachment](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint) to assign two NAT IP addresses per endpoint or backend.
    * Make sure that the producer backend VMs have sufficient vCPUs. Increasing the number of vCPUs in a backend VM can increase the per-backend connection limit. For specific limits, see [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections). Increasing the number of vCPUs doesn't affect the maximum connections for [services that use Envoy proxies](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#envoy-lb).



#### Dropped packets from published services

The [`private_service_connect/consumer/dropped_received_packets_count` metric](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#compute/private_service_connect/consumer/dropped_received_packets_count) tracks packets sent from a published service to a Private Service Connect consumer such as an endpoint that are dropped because Private Service Connect can't find a matching connection for response packets.

Private Service Connect only allows connections that are initiated from the consumer VPC network. When a consumer initiates a connection, the connection is tracked in order to match response packets from the published service with an existing connection. If Private Service Connect can't find a match for a response packet, the packet is dropped.

Private Service Connect might not find a match for a response packet if a published service sends response packets after a connection has timed out. If you see values for this metric, contact the service producer. They might be able to [configure their service to avoid this issue](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#nat-subnets-other).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
