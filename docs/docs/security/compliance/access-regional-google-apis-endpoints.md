---
url: https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints/
title: Access regional and multi-regional Google APIs through private endpoints \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:16.209520+00:00
---

# Access regional and multi-regional Google APIs through private endpoints  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Access regional and multi-regional Google APIs through private endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use Private Service Connect endpoints to connect to [regional endpoints and multi-regional endpoints of supported Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).

For information about other Private Service Connect configurations, see [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

## Required roles

If you're creating the endpoint in the same project as the subnet that you're connecting it to, see Required roles for your project.

If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) and are creating the endpoint in a service project, and connecting it to a subnet in the host project, you need the following roles:

  * Required roles for your project granted on the service project
  * Additional required roles for Shared VPC configurations granted on the host project



### Required roles for your project

To get the permissions that you need to manage Private Service Connect endpoints that access regional endpoints, ask your administrator to grant you the following IAM roles: 

  * Create, view, and delete endpoints: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on your project 
  * Configure DNS entries for an endpoint: [DNS Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.admin) (`roles/dns.admin`) on your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Additional required roles for Shared VPC configurations

If you're creating an endpoint in a service project that uses an IP address from a host project subnet, you need the following permissions in addition to the Roles for your project (the service project).

Both you and the Network Connectivity Service Account need permissions on the host project.

#### Roles to grant to your user account

To get the permissions that you need to manage Private Service Connect endpoints that access regional endpoints for Google APIs, ask your administrator to grant you the following IAM roles: 

  * Create, view, and delete endpoints that use a host project IP address: 
    * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on the service project
    * [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) on the host project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage Private Service Connect endpoints that access regional endpoints for Google APIs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage Private Service Connect endpoints that access regional endpoints for Google APIs:

  * To create, view, and delete endpoints that use a host project IP address: 
    * `compute.networks.use` on the host project
    * `compute.subnetworks.use` on the host project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Roles to grant to the Network Connectivity Service Account

To ensure that `service-PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com` has the necessary permissions to manage Private Service Connect endpoints that access regional endpoints for Google APIs, ask your administrator to grant the following IAM roles to `service-PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com`: 

**Important:** You must grant these roles to `service-PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com`, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Create, view, and delete endpoints that use a host project IP address: [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) on the host project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage Private Service Connect endpoints that access regional endpoints for Google APIs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage Private Service Connect endpoints that access regional endpoints for Google APIs:

  * To create, view, and delete endpoints that use a host project IP address: 
    * `compute.networks.get` on the host project
    * `compute.networks.use` on the host project
    * `compute.subnetworks.get` on the host project
    * `compute.subnetworks.use` on the host project



Your administrator might also be able to give `service-PROJECT_NUMBER@gcp-sa-networkconnectivity.iam.gserviceaccount.com` these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         $ gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. Enable the Compute Engine, Network Connectivity Center, and Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,networkconnectivity.googleapis.com,dns.googleapis.com)

  3. Additionally, [enable the API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for the target service that you want to access through the Private Service Connect endpoint. For example, if you want to access `spanner.me-central2.rep.googleapis.com`, enable the Cloud Spanner API. Private Service Connect doesn't automatically enable any APIs.

  4. Ensure that egress firewall rules permit traffic to the endpoint. The default firewall configuration for a VPC network permits this traffic because it contains an implied allow egress rule. Verify that you haven't created a higher priority egress rule that blocks the traffic.




## Create a regional Private Service Connect endpoint

You can create a regional Private Service Connect endpoint to send requests to a regional endpoint or a multi-regional endpoint for a target Google API.

For a list of supported regional endpoints and multi-regional endpoints, see [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click **Connect endpoint**.

  3. In **Target** , select **Google API**.

  4. In the **Scope** list, select **Regional**.

  5. In the **Region** list, select the region that you want to use.

  6. In the **Target service** list, select the service that you want to access.

  7. In **Endpoint name** , enter a name for the endpoint.

  8. In **Network** , select a network.

  9. In **Subnetwork** , select a subnetwork.

  10. In **IP address** , do one of the following to configure an IP address:

     * Select **Auto-allocate** to automatically allocate and reserve a new static IP address.
     * Select a static IP address from the list.
     * Click **Create IP address** to reserve a new static IP address.
  11. Optional: To make the endpoint available from all regions in the VPC network, select **Enable global access**.

  12. Click **Add endpoint**.




###  gcloud 

Use the [`gcloud network-connectivity regional-endpoints create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create) to create the endpoint.
    
    
    gcloud network-connectivity regional-endpoints create ENDPOINT_NAME \
        --region=REGION \
        --address=ADDRESS \
        --network=projects/PROJECT_ID/global/networks/NETWORK_NAME \
        --subnetwork=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
        --target-google-api=REP_DNS_NAME
    

If you want to make the endpoint available to resources in other regions, add the `--enable-global-access` flag.

Replace the following:

  * `ENDPOINT_NAME`: a name for the endpoint.

  * `REGION`: the region that you want to create the endpoint in.

  * `ADDRESS`: the IPv4 or `/96` IPv6 address that you want to use for the endpoint. If omitted, an IPv4 address from the subnetwork is allocated. Use one of the following formats:

    * IPv4 address—for example, `10.0.0.2`.
    * IPv4 or IPv6 address resource URI—for example, `projects/PROJECT_ID/regions/REGION/addresses/ADDRESS_NAME`.
  * `PROJECT_ID`: the project that you're creating the endpoint in.

  * `NETWORK_NAME`: the name of the VPC network for the endpoint.

  * `SUBNET_NAME`: the subnet that you're connecting the endpoint to.

  * `REP_DNS_NAME`: the hostname of the regional service endpoint or multi-regional endpoint that you're connecting to. For example, `spanner.me-central2.rep.googleapis.com` (regional) or `storage.us.rep.googleapis.com` (multi-regional).




###  API 

Use the [`projects.locations.regionalEndpoints.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints/create) to create the endpoint.

HTTP method and URL:
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/regionalEndpoints?regionalEndpointId=ENDPOINT_NAME
      
    
    
      {
        "accessType": "REGIONAL",
        "address": "ADDRESS",
        "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
        "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME",
        "targetGoogleApi": "REP_DNS_NAME"
      }
      

Replace the following:

  * `PROJECT_ID`: the project ID of the endpoint.
  * `REGION`: the region that you want to create the endpoint in.
  * `ENDPOINT_NAME`: a name for the endpoint.
  * `ADDRESS`: the IPv4 or `/96` IPv6 address that you want to use for the endpoint. If omitted, an IPv4 address from the subnetwork is allocated. Use one of the following formats: 
    * IPv4 address—for example, `10.0.0.2`.
    * IPv4 or IPv6 address resource URI—for example, `projects/PROJECT_ID/regions/REGION/addresses/ADDRESS_NAME`.
  * `NETWORK_NAME`: the name of the VPC network for the endpoint.
  * `SUBNET_NAME`: the name of the subnet that you want to connect the endpoint to.
  * `REP_DNS_NAME`: the hostname of the regional service endpoint or multi-regional endpoint that you want to connect to. For example, `spanner.me-central2.rep.googleapis.com` (regional) or `storage.us.rep.googleapis.com` (multi-regional).



## Create a regional Private Service Connect endpoint in a Shared VPC service project

If you're using Shared VPC, you can create an endpoint in a service project that uses an IP address from a subnet in a host project. You can't use the Google Cloud console to create this configuration—you must use the gcloud CLI or the API.

###  gcloud 

  1. Reserve a static IP address to use for the regional endpoint by using the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create). Using a static IP address is optional for IPv4, and required for IPv6.

Create the address resource in the service project, specifying a subnet in the host project.
         
         gcloud compute addresses create ADDRESS_NAME \
             --region=REGION \
             --subnet=projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET \
             --ip-version=IP_VERSION \
             --project=SERVICE_PROJECT
         

Replace the following:

     * `ADDRESS_NAME`: the name to assign to the reserved IP address.
     * `REGION`: the region for the endpoint IP address. This must be the same region that contains the service producer's service attachment.
     * `HOST_PROJECT`: the project ID of the host project.
     * `HOST_SUBNET`: the name of the subnet for the endpoint IP address.
     * `IP_VERSION`: the IP version of the IP address, which can be either `IPV4` or `IPV6`. `IPV4` is the default. To specify `IPV6`, the IP address must be connected to a [subnet with an internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).
     * `SERVICE_PROJECT`: the project ID of the service project
  2. Use the [`gcloud network-connectivity regional-endpoints create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create) to create the regional endpoint in the service project.
         
         gcloud network-connectivity regional-endpoints create ENDPOINT_NAME \
             --region=REGION \
             --address=ADDRESS \
             --network=projects/HOST_PROJECT/global/networks/HOST_NETWORK \
             --subnetwork=projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET \
             --target-google-api=REP_DNS_NAME \
             --project=SERVICE_PROJECT
             

If you want to make the endpoint available to resources in other regions, add the `--enable-global-access` flag.

Replace the following:

     * `ENDPOINT_NAME`: a name for the endpoint.

     * `REGION`: the region that you want to create the endpoint in.

     * `ADDRESS`: the IPv4 or `/96` IPv6 address that you want to use for the endpoint. If omitted, an IPv4 address from the subnetwork is allocated. Use one of the following formats:

       * IPv4 address—for example, `10.0.0.2`.
       * IPv4 or IPv6 address resource URI. The address resource must be created in the service project, not the host project. For example, `projects/SERVICE_PROJECT/regions/REGION/addresses/ADDRESS_NAME`.
       * `HOST_PROJECT`: the ID of the host project.
     * `HOST_NETWORK`: the name of the VPC network in the host project.

     * `HOST_SUBNET`: the subnet in the host project that you're connecting the endpoint to.

     * `REP_DNS_NAME`: the hostname of the regional service endpoint or multi-regional endpoint that you want to connect to. For example, `spanner.me-central2.rep.googleapis.com` (regional) or `storage.us.rep.googleapis.com` (multi-regional).

     * `SERVICE_PROJECT`: the project ID of the service project




###  API 

  1. Reserve a static IP address to use for the regional endpoint. Using a static IP address is optional for IPv4, and required for IPv6.

Create the address resource in the service project, specifying a subnet in the host project.
         
         POST https://compute.googleapis.com/compute/v1/projects/SERVICE_PROJECT/regions/REGION/addresses
         
         
         {
             "name": "ADDRESS_NAME",
             "addressType": "INTERNAL",
             "subnetwork": "projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET",
             "ipVersion": "IP_VERSION"
         }
         

Replace the following:

     * `SERVICE_PROJECT`: the ID of the service project.

     * `REGION`: the region for the endpoint. This must be the same region as the regional endpoint that you want to connect to.

     * `ADDRESS_NAME`: the name to assign to the static IP address.

     * `HOST_PROJECT`: the ID of the host project.

     * `HOST_SUBNET`: the subnet in the Shared VPC network to reserve the IP address from.

     * `IP_VERSION`: the IP version of the IP address, which can be either `IPV4` or `IPV6`. `IPV4` is the default. To specify `IPV6`, the IP address must be connected to a [subnet with an internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  2. Create the Private Service Connect endpoint by using the [`projects.locations.regionalEndpoints.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints/create).

HTTP method and URL:
         
         POST https://networkconnectivity.googleapis.com/v1/projects/SERVICE_PROJECT/locations/REGION/regionalEndpoints?regionalEndpointId=ENDPOINT_NAME
         
         
         {
           "accessType": "REGIONAL",
           "address": "ADDRESS",
           "network": "projects/HOST_PROJECT/global/networks/HOST_NETWORK",
           "subnetwork": "projects/HOST_PROJECT/regions/REGION/subnetworks/HOST_SUBNET",
           "targetGoogleApi": "REP_DNS_NAME"
         }
         

Replace the following:

     * `SERVICE_PROJECT`: the ID of the service project.
     * `REGION`: the region that you want to create the endpoint in.
     * `ENDPOINT_NAME`: a name for the endpoint.
     * `ADDRESS`: the IPv4 or `/96` IPv6 address that you want to use for the endpoint. If omitted, an IPv4 address from the subnetwork is allocated. Use one of the following formats: 
       * IPv4 address—for example, `10.0.0.2`.
       * IPv4 or IPv6 address resource URI—for example, `projects/SERVICE_PROJECT/regions/REGION/addresses/ADDRESS_NAME`.
     * `HOST_PROJECT`: the ID of the host project.
     * `HOST_NETWORK`: the name of the network in the host project.
     * `HOST_SUBNET`: the name of the subnet in the host project that you want to connect the endpoint to.
     * `REP_DNS_NAME`: the hostname of the regional service endpoint or multi-regional endpoint that you want to connect to. For example, `spanner.me-central2.rep.googleapis.com` (regional) or `storage.us.rep.googleapis.com` (multi-regional).



## List endpoints

You can list all configured endpoints.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

All endpoints are displayed, including endpoints with regional endpoint targets.




###  gcloud 

Use the [`gcloud network-connectivity regional-endpoints list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/list).
    
    
    gcloud network-connectivity regional-endpoints list \
        --region=REGION
    

Replace `REGION` with the region of the endpoints that you want to list.

###  API 

Use the [`projects.locations.regionalEndpoints.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints/list).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/regionalEndpoints
    

Replace the following:

  * `PROJECT_ID`: the project ID of the endpoint.
  * `REGION`: the region of the endpoints that you want to list.



## Verify that the endpoint is working

Create a virtual machine (VM) instance in the VPC network and region where the endpoint is configured. Run the following command on the VM to verify that the Private Service Connect endpoint is working. Endpoints don't respond to ping (ICMP) requests.

  * To verify an IPv4 endpoint, do the following:
        
        curl --connect-to REP_DNS_NAME:443:ADDRESS:443 \
        'https://REP_DNS_NAME/PATH'
        

  * To verify an IPv6 endpoint, do the following:
        
        curl -6 --connect-to REP_DNS_NAME:443:[ADDRESS]:443 \
        'https://REP_DNS_NAME/PATH'
        




Replace the following:

  * `REP_DNS_NAME`: the public DNS name of the target regional endpoint or multi-regional endpoint—for example, `spanner.me-central2.rep.googleapis.com` or `storage.us.rep.googleapis.com`.
  * `ADDRESS`: the IP address of the endpoint.
  * `PATH`: the path to a resource that is served by this service. For example, many services offer a discovery document with the path `$discovery/rest?version=v1`.



The following example request tests that an endpoint with IP address `192.168.1.100` can request the [Cloud Spanner API](https://docs.cloud.google.com/spanner/docs/reference/rest) discovery document from the regional endpoint in `me-central2`.
    
    
    curl --connect-to spanner.me-central2.rep.googleapis.com:443:192.168.1.100:443 \
    'https://spanner.me-central2.rep.googleapis.com/$discovery/rest?version=v1'
    

## Create a private DNS entry for the endpoint

You must create private DNS entries so that clients can direct requests to your Private Service Connect endpoint.

We recommend creating a private zone that uses the same hostname as the target regional or multi-regional endpoint, and create an apex record in that zone:

  * If your Private Service Connect endpoint has a target of `spanner.me-central2.rep.googleapis.com`, create a private zone for `spanner.me-central2.rep.googleapis.com` that contains an apex record for `spanner.me-central2.rep.googleapis.com`.
  * If your Private Service Connect endpoint has a target of `storage.us.rep.googleapis.com`, create a private zone for `storage.us.rep.googleapis.com` that contains an apex record for `storage.us.rep.googleapis.com`.



Creating records in the domain apex means that you can access the public hostname of other endpoints—for example, `logging.me-central2.rep.googleapis.com`.

The following sections describe how to use Cloud DNS to create a private zone and an apex DNS record.

### Create a private zone

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Private**.

  3. For **Zone name** , enter a name. For example, if your Private Service Connect endpoint points to `spanner.me-central2.rep.googleapis.com`, enter `spanner-me-central2-rep-googleapis-com`.

  4. For **DNS name** , specify the hostname of the target regional endpoint followed by a trailing dot. For example, `spanner.me-central2.rep.googleapis.com.`.

  5. Optional: Add a description.

  6. Under **Options** , select **Default (private)**.

  7. Select the VPC networks where you want the private zone to be visible. Only the VPC networks that you select are authorized to query records in the zone.

  8. Click **Create**.




###  gcloud 

Run the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create ZONE_NAME \
        --dns-name=REP_DNS_NAME. \
        --networks=VPC_NETWORK_LIST \
        --visibility=private \
        --description="Private zone for REP_DNS_NAME"
    

Replace the following:

  * `ZONE_NAME`: a name for your zone—for example, `spanner-me-central2-rep-googleapis.com`.
  * `DESCRIPTION`: a description for your zone
  * `REP_DNS_NAME`: the DNS suffix for your zone; use the target regional endpoint hostname—for example, `spanner.me-central2.rep.googleapis.com`
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that are authorized to query the zone



###  API 

Send a `POST` request using the [`managedZones.create`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/create) method:

HTTP method and URL:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones
    

Request JSON body:
    
    
    {
      "name": "ZONE_NAME",
      "dnsName": "REP_DNS_NAME.",
      "description": "DESCRIPTION",
      "visibility": "private",
      "privateVisibilityConfig": {
        "kind": "dns#managedZonePrivateVisibilityConfig",
        "networks": [
          {
            "kind": "dns#managedZonePrivateVisibilityConfigNetwork",
            "networkUrl": "NETWORK_1_URL"
          },
          {
            "kind": "dns#managedZonePrivateVisibilityConfigNetwork",
            "networkUrl": "NETWORK_2_URL"
          }
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the DNS zone.
  * `ZONE_NAME`: the name of the private zone that you created for this regional endpoint.
  * `REP_DNS_NAME`: the FQDN of the record you're creating; use the target regional endpoint hostname—for example, `spanner.me-central2.rep.googleapis.com`.
  * `DESCRIPTION`: a description for the DNS zone.
  * `NETWORK_1_URL` and `NETWORK_2_URL`: the full URLs of the VPC networks that are authorized to query the zone—for example, `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME`.



### Add a DNS record to the zone

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/)

  2. Click the name of the managed zone that you want to add the record to.

  3. On the **Zone details** page, click **Add standard**.

  4. On the **Create record set** page, leave the **DNS name** field blank. Leaving the field blank creates a resource record at the domain apex.

  5. For **Resource record type** , select `A`.

  6. In the **IPv4 address** field, enter or select the IP address of the Private Service Connect endpoint.

  7. Click **Create**.




###  gcloud 

To add a resource record set, use the [`gcloud dns record-sets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/create):
    
    
    gcloud dns record-sets create REP_DNS_NAME \
        --rrdatas=ADDRESS \
        --type=RECORD_TYPE \
        --ttl=TTL \
        --zone=ZONE_NAME
    

Replace the following:

  * `REP_DNS_NAME`: the FQDN of the record you're creating; use the target regional endpoint hostname—for example, `spanner.me-central2.rep.googleapis.com`.
  * `ADDRESS`: the IP address of the Private Service Connect endpoint.
  * `RECORD_TYPE`: the type of DNS record, such as `A` for IPv4 records or `AAAA` for IPv6 records.
  * `TTL`: the TTL in seconds that the resolver caches this resource record set—for example, `300`.
  * `ZONE_NAME`: the name of the private zone that you created for this regional endpoint.



###  API 

To add a resource record set, use the [`resourceRecordSets.create` method](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets/create):

HTTP method and URL:
    
    
    POST https://www.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/ZONE_NAME/rrsets
    

Request JSON body:
    
    
    {
      "name": "REP_DNS_NAME.",
      "type": "RECORD_TYPE",
      "ttl": TTL,
      "rrdatas": [ "ADDRESS" ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the DNS zone.
  * `ZONE_NAME`: the name of the private zone that you created for this regional endpoint.
  * `REP_DNS_NAME`: the FQDN of the record you're creating; use the target regional endpoint hostname—for example, `spanner.me-central2.rep.googleapis.com`.
  * `RECORD_TYPE`: the type of DNS record, such as `A` for IPv4 records or `AAAA` for IPv6 records.
  * `TTL`: the TTL in seconds that the resolver caches this resource record set—for example, `300`.
  * `ADDRESS`: the IP address of the Private Service Connect endpoint.



## Configure clients to use the private endpoint name

You must configure clients to use the private DNS names instead of the public DNS names. See the documentation for your client or client library for information about configuring it to use custom endpoints. The following pages include configuration steps for some common clients:

  * **Python** : you can configure `api_endpoint` in [Client options](https://googleapis.dev/python/google-api-core/latest/client_options.html).

  * **Go** : you can configure `WithEndpoint` in [ClientOptions](https://godoc.org/google.golang.org/api/option).

  * **.NET** : you can configure [`Endpoint`](https://docs.cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint) in the client's builder class.

  * **Java** : you can configure [`setEndpoint`](https://docs.cloud.google.com/java/docs/endpoints) in the client's settings class.

  * **gcloud** : you can configure `api_endpoint_overrides` in the [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/topic/endpoint-override).




## Get detailed information about an endpoint

You can view the configuration details of an endpoint.

###  gcloud 

Use the [`gcloud network-connectivity regional-endpoints describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/describe).
    
    
    gcloud network-connectivity regional-endpoints describe \
        ENDPOINT_NAME --region=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: the name of the endpoint.
  * `REGION`: the region of the endpoint.



###  API 

Use the [`projects.locations.regionalEndpoints.get` command](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints/get).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/regionalEndpoints/ENDPOINT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID of the endpoint.
  * `REGION`: the region of the endpoints that you want to list.
  * `ENDPOINT_NAME`: the name of the endpoint.



## Update the global access configuration

You can't update a Private Service Connect endpoint that has a regional endpoint target. If you need to change the global access setting for the endpoint, delete the endpoint and create a new endpoint that has the required global access setting.

## Delete an endpoint

You can delete an endpoint.

###  gcloud 

Use the [`gcloud network-connectivity regional-endpoints delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/delete).
    
    
    gcloud network-connectivity regional-endpoints delete \
        ENDPOINT_NAME --region=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: the name of the endpoint.
  * `REGION`: the region of the endpoint.



###  API 

Use the [`projects.location.regionalEndpoints.delete` command](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints/delete).
    
    
    DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/regionalEndpoints/ENDPOINT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID of the endpoint.
  * `REGION`: the region of the endpoint.
  * `ENDPOINT_NAME`: the name of the endpoint.



## Access endpoints from hybrid networks

Clients in networks that are connected to Google Cloud with VLAN attachments for Cloud Interconnect or Cloud VPN tunnels can reach Private Service Connect endpoints. 

  * The VLAN attachment or Cloud VPN tunnel must terminate in the same VPC network (or Shared VPC network) as the endpoint. Clients in peered VPC networks cannot reach endpoints.

  * Client traffic from VLAN attachments or Cloud VPN tunnels can reach endpoints in another region if [global access](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#create-regional-endpoint) is configured.

  * Both Dataplane v1 and Dataplane v2 are supported for the VLAN attachments. For more information about Dataplane versions, see [Dataplane v2](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#dataplaneVersion).




You must configure systems in the other network so that they can make queries to your private DNS zones.

If you implemented the private DNS zones by using Cloud DNS, complete the following steps:

  * Create an [inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in) in the VPC network to which your other network connects.

  * Identify the [inbound forwarder entry points](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints) in the region where your VLAN attachment or Cloud VPN tunnel is located, in the VPC network to which your other network connects.

  * Configure systems and DNS name servers in the other network to forward the [DNS names for the endpoint](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#configure-dns) to an inbound forwarder entry point in the same region as the VLAN attachment or Cloud VPN tunnel that connects to the VPC network.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
