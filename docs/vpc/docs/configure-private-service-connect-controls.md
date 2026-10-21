---
url: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls/
title: Access regional Google APIs through backends \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:54.668315+00:00
---

# Access regional Google APIs through backends  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access regional Google APIs through backends

This guide describes how to configure an internal Application Load Balancer with a Private Service Connect backend to access a [regional Google API](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

For more information about backends, see [About backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).

An internal Application Load Balancer used for Private Service Connect can be reached from [Shared VPC networks](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc) and from [connected networks](https://docs.cloud.google.com/load-balancing/docs/l7-internal/internal-https-lb-and-other-networks).

## Roles

The [Compute Load Balancer Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) contains the permission required to perform the tasks described in this guide.

## Supported services

See the list of supported [regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.

  * If you want to register the load balancing forwarding rule with Service Directory, [enable](https://console.cloud.google.com/apis/library/servicedirectory.googleapis.com) the [Service Directory API](https://docs.cloud.google.com/service-directory/docs/reference/rest) in your project. To configure Service Directory, you must create the forwarding rule by using the Google Cloud CLI or the API.

  * Create a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) if you don't already have one. There must be a single proxy-only subnet in the VPC network and region where you intend to create the internal Application Load Balancer. This subnet is used by all internal Application Load Balancers within that network and region.

  * If you don't already have them, create a private key and a self-managed certificate for your domain. See [step 1 of using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs). You need a private key and certificate to create the target HTTPS proxy when you [configure the load balancer](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls#configure-the-load-balancer).




## Create a network endpoint group

For each service that you want to make available using the load balancer, create a Private Service Connect network endpoint group (NEG).

###  Console 

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/add)

  2. Click **Create network endpoint group**.

  3. Enter a **Name** for the network endpoint group.

  4. For the **Network endpoint group type** , select **Network endpoint group (Private Service Connect)**.

  5. Select the **Region** for the network endpoint group.

  6. Select the **Target service** for the network endpoint group.

  7. Click **Create**.




###  gcloud 
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=private-service-connect \
        --psc-target-service=TARGET_SERVICE \
        --region=REGION
    

Replace the following:

  * `NEG_NAME`: a name for the network endpoint group.

  * `TARGET_SERVICE`: the target service that you want to connect to. See [the list of supported regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

  * `REGION`: the region to create the network endpoint group in. The region must be the same region as the service you want to connect to.




## Configure the load balancer

All load balancer components must be created in the same region as the Private Service Connect network endpoint group.

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Internal** and click **Next**.
  5. For **Cross-region or single region deployment** , select **Best for regional workloads** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. Enter a **Name** for the load balancer.
  2. Select a **Region** for the load balancer.
  3. Select a **Network** for the load balancer.

The network must contain a proxy-only subnet in the region that you are creating the NEG and load balancer in. If you don't have one, you can click **Reserve subnet** to create one.

  4. Keep the window open to continue.




#### Backend configuration

The Private Service Connect network endpoint group is a type of load balancer backend. You create a backend service for each backend you want to configure.

  1. Click **Backend configuration**.
  2. For each Private Service Connect network endpoint group that you want to configure, create a backend service.

     1. From the **Create or select backend services** menu, select **Create a backend service**.
     2. Enter a **Name** for the backend service.
     3. Set the **Backend type** to **Private Service Connect network endpoint group**.
     4. Set the **Private Service Connect target type** to **Regional Google API**.
     5. Select **HTTPS** for the protocol.

     6. In the **Backends** section, click the **New backend** menu, and select the Private Service Connect network endpoint group.

If you need to create a new Private Service Connect network endpoint group, click **Create Private Service Connect network endpoint group**.




#### Routing rules

The set of rules for routing incoming HTTPS requests to specific backend services or backend buckets is called a _URL map_. To learn more about URL maps, see [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

If you are configuring only one backend service for the load balancer, the default routing rule is sufficient, and you can skip to **Frontend configuration**.

  1. If you have more than one backend service, click **Routing rules**.
  2. Select **Simple host and path rule**.
  3. For each backend, do the following: 
     1. **Add host and path rule**.
     2. For **Host** , enter the hostname that will be used to send requests to this service—for example, `pubsub.example.com`.
     3. For **Paths** , enter the path—for example, `/*`.
     4. For **Backends** , select the backend service.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. Click **Add frontend IP and port**.
  3. Enter a **Name** for the load balancer.
  4. In the **Protocol** field, select **HTTPS (includes HTTP/2)**.
  5. Select a **Subnetwork** for the load balancer.
  6. Ensure that the **Port** is set to `443`, to allow HTTPS traffic.
  7. For **IP address** , select an IP address from the menu.

If you want to reserve a new IP address, click **Create IP address**.

  8. Click the **Certificate** drop-down list.

     1. If you already have a [self-managed SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types) that you want to use, select it from the menu.
     2. Otherwise, select **Create a new certificate**.
     3. Enter a **Name** for the certificate resource.
     4. In the appropriate fields, upload your PEM-formatted files: 
        * **Certificate**
        * **Private key**
     5. Click **Create**.
  9. Click **Done**.




#### Review and finalize

  1. Click **Review and finalize** to review the configuration.
  2. Click **Create**.



###  gcloud 

  1. For each network endpoint group that you have created, create a backend service.
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --protocol=HTTPS \
             --region=REGION
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `REGION`: the region to create the backend service in.
  2. For each backend service that you have created, add the corresponding NEG to the backend service.
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --network-endpoint-group=NEG_NAME \
             --region=REGION
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `NEG_NAME`: the name of the network endpoint group.
     * `REGION`: the region for the backend.
  3. Create a URL map for the load balancer.

A URL map must reference a default backend service. If you're configuring your load balancer with one backend service, set that backend service as the default. If you're configuring your load balancer to use multiple backend services, referenced by host rules and path matchers that you create in the next step, pick one of the backend services to be the URL map default.
         
         gcloud compute url-maps create URL_MAP_NAME \
             --default-service=DEFAULT_BACKEND_SERVICE_NAME \
             --region=REGION
         

Replace the following:

     * `URL_MAP_NAME`: a name for the URL map.

     * `DEFAULT_BACKEND_SERVICE_NAME`: the name of the load balancer's default. The default is used when no host rule matches the requested hostname.

     * `REGION`: the region to create the URL map in.

  4. Add additional backend services to the URL map.

If your URL map needs to reference two or more backend services, complete the following steps. If your URL map only references one backend service, skip this step.

     1. For each backend service, add a path matcher. You must create one path matcher for each backend service.
            
            gcloud compute url-maps add-path-matcher URL_MAP_NAME \
                --path-matcher-name=PATH_MATCHER \
                --default-service=BACKEND_SERVICE_NAME \
                --region=REGION
            

Replace the following:

        * `URL_MAP_NAME`: the name of the URL map.
        * `PATH_MATCHER`: a name for the path matcher.
        * `BACKEND_SERVICE_NAME`: the name of the backend service.
        * `REGION`: the region of the URL map.
     2. For each hostname, add a host rule.

Each host rule can reference only one path matcher, but two or more host rules can reference the same path matcher.
            
            gcloud compute url-maps add-host-rule URL_MAP_NAME \
                --hosts=HOST \
                --path-matcher-name=PATH_MATCHER \
                --region=REGION
            

Replace the following:

        * `URL_MAP_NAME`: the name of the URL map.
        * `HOST`: the hostname to send requests to for this service. For example, `pubsub.example.com`.
        * `PATH_MATCHER`: the name of the path matcher.
        * `REGION`: the region of the URL map.
  5. Create the target HTTPS proxy.

     1. Create a regional [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) using the [`gcloud compute ssl-certificates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command. Google-managed certificates aren't supported with internal Application Load Balancers.
            
            gcloud compute ssl-certificates create CERTIFICATE \
                --certificate=LB_CERT \
                --private-key=LB_PRIVATE_KEY \
                --region=REGION
            

Replace the following:

        * `CERTIFICATE`: a name for the certificate.

        * `LB_CERT`: the path to the PEM-formatted certificate file for your self-managed certificate.

        * `LB_PRIVATE_KEY`: the path to the PEM-formatted private key file for your self-managed certificate.

        * `REGION`: the region for the certificate.

     2. Use the regional SSL certificate resource to create a target HTTPS proxy with the [`gcloud compute target-https-proxies create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create) command.
            
            gcloud compute target-https-proxies create PROXY_NAME \
                --url-map=URL_MAP_NAME \
                --region=REGION \
                --ssl-certificates=CERTIFICATE
            

Replace the following:

        * `PROXY_NAME`: a name for the target HTTPS proxy.
        * `URL_MAP_NAME`: the name of the URL map.
        * `REGION`: the region for the certificate resource.
        * `CERTIFICATE`: the name of the certificate resource.
  6. Reserve a regional internal IPv4 address for the forwarding rule.
         
         gcloud compute addresses create ADDRESS_NAME \
             --ip-version=IPV4 \
             --region=REGION \
             --subnet=SUBNETWORK
         

Replace the following:

     * `ADDRESS_NAME`: a name for the IP address resource.
     * `REGION`: the region to create the IP address in.
     * `SUBNET`: the subnet to create the IP address in.

Run this command to view the reserved IP address. After you've created the load balancer, you can use the IP address to verify the configuration.
    
    gcloud compute addresses describe ADDRESS_NAME \
        --format="get(address)" --region=REGION
    

  7. Create the forwarding rule.

Create the forwarding rule using the [`gcloud compute forwarding-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command.
         
         gcloud compute forwarding-rules create FWD_RULE \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=NETWORK \
             --address=ADDRESS_NAME \
             --ports=443 \
             --region=REGION \
             --target-https-proxy=PROXY_NAME \
             --target-https-proxy-region=PROXY_REGION \
            [--service-directory-registration=SD_SERVICE_NAME]
         

Replace the following:

     * `FWD_RULE`: a name for the forwarding rule.

     * `NETWORK`: the network to create the forwarding rule in.

     * `ADDRESS_NAME`: the reserved IP address.

     * `REGION`: the region for the forwarding rule.

     * `PROXY_NAME`: the name of the target HTTPS proxy.

     * `PROXY_REGION`: the region of the target HTTPS proxy.

     * `SD_SERVICE_NAME`: the URI of the [Service Directory service that you want to register the load balancer with](https://docs.cloud.google.com/service-directory/docs/configuring-ilb-in-sd), in this format: `projects/PROJECT/locations/REGION/namespaces/NAMESPACE_NAME/services/SERVICE_NAME`. Specifying `--service-directory-registration` is optional.




## Verify the configuration

  1. Create the VM instance.
         
         gcloud compute instances create VM_NAME \
             --network=NETWORK \
             --image-project=debian-cloud --image-family=debian-12 \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: a name for the virtual machine.

     * `NETWORK`: the network for the VM.

     * `ZONE`: the zone for the VM.

  2. Connect to the VM.
         
         gcloud compute ssh VM_NAME --zone=ZONE
         

  3. Use `curl` to verify the configuration. This command sets the `Host` header and bypasses DNS resolution by specifying a user-defined IP address. You can omit the port if you are using the default port for the protocol, for example using port 443 for HTTPS.

If needed, you can skip certificate validation using the `-k` flag. You might need to skip validation if you used a self-signed certificate to configure the target HTTPS proxy, or if the VM does not have the certificate of the certificate authority that signed your certificate.
         
         curl -iv --resolve HOSTNAME:443:IP_ADDRESS \
            'https://HOSTNAME/RESOURCE_URI'
         

Replace the following:

     * `HOSTNAME`: the hostname that you configured in your URL map—for example, `pubsub.example.com`.
     * `IP_ADDRESS`: the IP address of your load balancer's forwarding rule.
     * `RESOURCE_URI`: the rest of the URI of the resource that you want to use for verification. For example, if the load balancer is forwarding requests to a regional endpoint for Pub/Sub, you could use `rest?version=v1`.



## Configure DNS records

Configure DNS records for each host that you added to the URL map, pointing to the IP address of the forwarding rule. If you're using Cloud DNS to manage DNS, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records#adding_a_record). Otherwise, configure DNS records on your DNS server.

For example, say you have created the following configurations:

  * A Private Service Connect NEG that uses target service `pubsub.europe-west3.rep.googleapis.com`.

  * An internal Application Load Balancer that uses that Private Service Connect NEG as a backend.

  * A URL map that defines a host rule for `pubsub.example.com`.




For this configuration to work correctly, you must create a DNS record that points `pubsub.example.com` to the IP address of the forwarding rule.

With this configuration, any requests sent to `pubsub.example.com` are sent to the load balancer, which forwards the request to `pubsub.europe-west3.rep.googleapis.com`.

## Configure clients to send requests to the backend

To send requests through the backend instead of the public service endpoints, you must configure clients to send requests to the hostname that you defined in the load balancer's URL map—for example, `pubsub.example.com`. See the documentation for your client or client library for information about configuring it to use custom endpoints. The following pages include configuration steps for some common clients:

  * **Python** : you can configure `api_endpoint` in [Client options](https://googleapis.dev/python/google-api-core/latest/client_options.html).

  * **Go** : you can configure `WithEndpoint` in [ClientOptions](https://godoc.org/google.golang.org/api/option).

  * **.NET** : you can configure [`Endpoint`](https://docs.cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint) in the client's builder class.

  * **Java** : you can configure [`setEndpoint`](https://docs.cloud.google.com/java/docs/endpoints) in the client's settings class.

  * **gcloud** : you can configure `api_endpoint_overrides` in the [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/topic/endpoint-override).




## Access the backend from on-premises hosts

If your on-premises network is connected to a VPC network, you can send traffic to the Private Service Connect backend.

  * Your on-premises network must be connected to the VPC network containing your internal Application Load Balancer using Cloud VPN tunnels or VLAN attachments in the same region as the internal Application Load Balancer.

  * The on-premises network must have appropriate routes to your internal Application Load Balancer. Ensure that each Cloud Router managing the BGP session for the Cloud VPN tunnel or VLAN attachment has been configured to advertise the primary IP address range of the subnet used by your internal Application Load Balancer forwarding rule. Cloud Routers advertise subnet routes by default.

  * You must configure on-premises systems so that the hostnames in the URL map of your internal Application Load Balancer resolve to the internal Application Load Balancer forwarding rule IP address. You can create the DNS records in on-premises name servers or you can use Cloud DNS.

If you've created the DNS records using Cloud DNS managed private zones, complete the following steps:

    * Create an [inbound server policy](https://docs.cloud.google.com/dns/docs/policies#create-in) in the VPC network to which your on-premises network connects.

    * Identify the [inbound forwarder entry points](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints), in the regions where your Cloud VPN tunnels and VLAN attachments are located, in the VPC network to which your on-premises network connects.

    * Configure on-premises DNS name servers to forward DNS requests for the hostnames in the URL map to a Cloud DNS inbound forwarder entry point.


[ ![](https://docs.cloud.google.com/static/vpc/images/psc-internal-lb-regional-apis-onprem.svg)](https://docs.cloud.google.com/static/vpc/images/psc-internal-lb-regional-apis-onprem.svg) **Figure 1.** By configuring Private Service Connect, Cloud Router, and on-premises hosts, you can connect to Google APIs and services using regional backends (click to enlarge). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
