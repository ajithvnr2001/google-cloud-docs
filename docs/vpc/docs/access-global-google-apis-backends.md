---
url: https://docs.cloud.google.com/vpc/docs/access-global-google-apis-backends/
title: Access global Google APIs through backends \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:12.232991+00:00
---

# Access global Google APIs through backends  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/access-global-google-apis-backends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access global Google APIs through backends

This page describes how to access global Google APIs by using [Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) that are based on [cross-region internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal).

This configuration lets you target one or more individual global Google APIs while applying the [visibility and control](https://docs.cloud.google.com/vpc/docs/private-service-connect#backends) that Private Service Connect backends provide.

  * You can configure custom hostnames, local to your Virtual Private Cloud (VPC) and connected on-premises networks, that route traffic to your chosen global Google APIs.
  * You can access the backends from any region, and the backend can load balance traffic to Private Service Connect network endpoint groups (NEGs) that are located in any region.
  * You can send traffic to the backends from peered VPC networks.



For a list of the available global Google APIs, see [Global Google API targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis).

## Before you begin

  * To get the permissions that you need to configure a backend to access global Google APIs, ask your administrator to grant you the following IAM roles on your Google Cloud project: 

    * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
    * [Certificate Manager Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.owner) (`roles/certificatemanager.owner`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.

  * [Enable](https://console.cloud.google.com/apis/api/certificatemanager.googleapis.com) the [Certificate Manager API](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest) in your project.

  * Create a private key and a signed certificate from a certificate authority (CA). Follow the instructions in [Step 1: Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert). The private key and certificate are needed to create a self-managed SSL certificate with Certificate Manager.

  * Create a certificate resource for a cross-region internal Application Load Balancer by using the private key and signed certificate that you created. When you upload the certificate you must set the scope to `all-regions`. For more information, see [Upload a self-managed certificate to Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed#upload-self-managed). The certificate resource is needed to configure the target HTTPS proxy for the load balancer.

  * Create a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) if you don't already have one. There must be a single proxy-only subnet in the VPC network and region where you intend to create the cross-region internal Application Load Balancer's forwarding rule. This subnet is used by all internal Application Load Balancers within that network and region.




## Create a Private Service Connect NEG

For each global Google API that you want to access, create a [Private Service Connect NEG](https://docs.cloud.google.com/load-balancing/docs/negs#psc-neg). Private Service Connect NEGs are regional, even when they are used to connect to global Google APIs.

A Private Service Connect NEG can't be updated after it is created.

###  Console 

  1. In the Google Cloud console, go to the **Create a network endpoint group** page.

[Go to Create a network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/add)

  2. On the **Create network endpoint group** page, enter a **Name** for the network endpoint group.

  3. For the **Network endpoint group type** , select **Private Service Connect NEG (Regional)**.

  4. For **Target** , select **Global Google APIs**.

  5. Select the **Region** for the network endpoint group.

  6. Select the **Target service** for the network endpoint group.

  7. Click **Create**.




###  gcloud 

Use the [`network-endpoint-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create).
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=private-service-connect \
        --psc-target-service=TARGET_SERVICE \
        --region=REGION
    

Replace the following:

  * `NEG_NAME`: a name for the network endpoint group.

  * `TARGET_SERVICE`: the global Google API target that you want to connect to—for example, `pubsub.googleapis.com`. See the [list of supported global Google API targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis).

  * `REGION`: the region to create the network endpoint group in.




###  API 

Make a `POST` request to the [`regionNetworkEndpointGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkEndpointGroups
    {
      "name": "NEG_NAME",
      "networkEndpointType": "PRIVATE_SERVICE_CONNECT",
      "pscTargetService": "TARGET_SERVICE"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the network endpoint group.
  * `REGION`: the region to create the network endpoint group in.
  * `NEG_NAME`: a name for the network endpoint group.
  * `TARGET_SERVICE`: the global Google API target that you want to connect to—for example, `pubsub.googleapis.com`. See the [list of supported global Google API targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis).



## Configure the load balancer

To access global Google APIs, configure a cross-region internal Application Load Balancer.

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Internal** and click **Next**.
  5. For **Cross-region or single region deployment** , select **Best for cross-region workloads** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. Enter a **Name** for the load balancer.
  2. Select a **Network** for the load balancer.

The network must contain a proxy-only subnet in the region where you are creating the load balancer.




#### Frontend configuration

  1. Click **Frontend configuration**.
  2. Enter a **Name** for the load balancer's forwarding rule.
  3. In the **Protocol** field, select **HTTPS (includes HTTP/2 and HTTP/3)**.
  4. Select a **Subnetwork region** for the load balancer's subnetwork.
  5. Select a **Subnetwork** for the load balancer.
  6. Click **IP address** , and then do one of the following: 
     * To automatically assign an ephemeral IP address, select **Ephemeral (Automatic)**.
     * To choose an ephemeral IP address, select **Ephemeral (Custom)** , and then enter a **Custom ephemeral IP address** from the IP address range of the load balancer's subnet.
     * To reserve and use a static internal IP address, click **Create IP address** , and then do the following: 
       1. Enter a **Name** for the IP address.
       2. Click **Static IP address** , and then do one of the following: 
          * To automatically assign a static IP address, select **Assign automatically**.
          * To configure a specific IP address, select **Let me choose** , and then enter a **Custom IP address** from the IP address range of the load balancer's subnet.
       3. Click **Reserve**.
  7. Ensure that the **Port** field is set to `443`, to allow HTTPS traffic.
  8. Click the **Certificate** list, and then select your self-managed certificate.
  9. Click **Done**.



#### Backend configuration

  1. Click **Backend configuration**.
  2. For each global Google API that you want to access, create a global backend service. To create a global backend service, do the following:

     1. From the **Create or select backend services** menu, select **Create a backend service**.
     2. Enter a **Name** for the backend service.
     3. Set the **Backend type** to **Private Service Connect network endpoint group**.
     4. Set the **Private Service Connect target type** to **Global Google API**.
     5. Select **HTTPS** for the protocol.
     6. In the **Backends** section, click the **New backend** menu, and select a Private Service Connect network endpoint group.

If you need to create a new Private Service Connect network endpoint group, click **Create PSC NEG**.

     7. Click **Done**.

     8. Click **Create**.

  3. Ensure that each backend service that you want to add is selected in the **Create or select backend services** menu, and then click **OK**.




#### Routing rules

The set of rules for routing incoming HTTPS requests to specific backend services is called a _URL map_. To learn more about URL maps, see [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

If you are configuring only one backend service for the load balancer, the default routing rule is sufficient, and you can skip to **Review and finalize**.

If you are configuring multiple backend services, you must create one path matcher for each backend service. Each host rule can reference only one path matcher, but two or more host rules can reference the same path matcher.

  1. If you have more than one backend service, click **Routing rules**.
  2. Select **Simple host and path rule**.
  3. For each backend, do the following: 
     1. Click **Add host and path rule**.
     2. For **Host** , enter the hostname that will be used to send requests to this service—for example, `pubsub.example.com`.
     3. For **Paths** , enter the path—for example, `/*`.
     4. For **Backends** , select the backend service.



#### Review and finalize

  1. Click **Review and finalize** to review the configuration.
  2. Click **Create**.



###  gcloud 

  1. For each global Google API that you want to access, do the following:

     1. To create a global backend service, use the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create).
            
            gcloud compute backend-services create BACKEND_SERVICE_NAME \
                --load-balancing-scheme=INTERNAL_MANAGED \
                --protocol=HTTPS \
                --global
            

Replace `BACKEND_SERVICE_NAME` with the name of the backend service.

     2. To add a NEG to the corresponding backend service, use the [`gcloud compute backend-services add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend).
            
            gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
                --network-endpoint-group=NEG_NAME \
                --network-endpoint-group-region=REGION \
                --global
            

Replace the following:

        * `NEG_NAME`: the name of the Private Service Connect NEG.
        * `REGION`: the region of the Private Service Connect NEG.
  2. To create a global [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) for the load balancer, use the [`gcloud compute url-maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create).

A URL map must reference a default backend service. If you're configuring your load balancer with one backend service, set that backend service as the default. If you're configuring your load balancer to use multiple backend services, pick one of the backend services to be the URL map default.
         
         gcloud compute url-maps create URL_MAP_NAME \
             --default-service=DEFAULT_BACKEND_SERVICE_NAME
         

Replace the following:

     * `URL_MAP_NAME`: a name for the URL map.
     * `DEFAULT_BACKEND_SERVICE_NAME`: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  3. Optional: If you're configuring your load balancer to use multiple backend services, complete this step. If your URL map only references one backend service, skip this step.

To add additional backend services to the URL map, use the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher).

For each backend service, add a path matcher and one or more host rules. You must create one path matcher for each backend service. Each host rule can reference only one path matcher, but two or more host rules can reference the same path matcher.
         
         gcloud compute url-maps add-path-matcher URL_MAP_NAME \
             --path-matcher-name=PATH_MATCHER \
             --default-service=BACKEND_SERVICE_NAME \
             --new-hosts=HOSTNAMES
         

Replace the following:

     * `PATH_MATCHER`: a name for the path matcher.
     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `HOSTNAMES`: one or more hostnames to send requests to for the backend service—for example, `pubsub.example.com`. You can enter multiple hostnames in a comma-separated list.
  4. To create a target HTTPS proxy, use the [`gcloud compute target-https-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create).
         
         gcloud compute target-https-proxies create PROXY_NAME \
             --url-map=URL_MAP_NAME \
             --certificate-manager-certificates=CERTIFICATE_NAME
         

Replace the following:

     * `PROXY_NAME`: a name for the target HTTPS proxy.
     * `URL_MAP_NAME`: the name of the URL map.
     * `CERTIFICATE_NAME`: the name of the certificate resource.
  5. To create a global forwarding rule for your load balancer, use the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).
         
         gcloud compute forwarding-rules create RULE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=NETWORK \
             --address=IP_ADDRESS \
             --ports=443 \
             --target-https-proxy=PROXY_NAME \
             --subnet=SUBNET \
             --subnet-region=SUBNET_REGION \
             --global
         

Replace the following:

     * `RULE_NAME`: the name of the forwarding rule.
     * `NETWORK`: the VPC network of the forwarding rule. This network must contain a proxy-only subnet in the region where you are creating the load balancer.
     * `IP_ADDRESS`: the internal IP address of the forwarding rule, which must be within the IP address range of the forwarding rule's subnet. To use a specific ephemeral IP address, enter the IP address—for example, `10.0.0.5`. To use a static internal IP address, enter the name of the IP address. To let Google Cloud select an ephemeral IP address, omit this flag.
     * `SUBNET`: the subnet of the forwarding rule.
     * `SUBNET_REGION`: the region of the forwarding rule's subnet.



###  API 

  1. For each global Google API that you want to access, do the following:

     1. To create a global backend service, make a `POST` request to the [`backendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert).
            
            POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
            {
              "loadBalancingScheme": "INTERNAL_MANAGED",
              "name": "BACKEND_SERVICE_NAME",
              "protocol": "HTTPS"
            }
            

Replace the following:

        * `PROJECT_ID`: the project ID of your project.
        * `BACKEND_SERVICE_NAME`: the name of the backend service.
     2. To add a NEG to the corresponding backend service, make a `PATCH` request to the [`backendServices.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch).
            
            PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME
            {
              "backends": [
                {
                  "group": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkEndpointGroups/NEG_NAME"
                }
              ]
            }
            

Replace the following:

        * `REGION`: the region of the NEG.
        * `NEG_NAME`: the name of the network endpoint group to add.
  2. To create a global [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) for the load balancer, make a `POST` request to the [`urlMaps.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps/insert).

A URL map must reference a default backend service. If you're configuring your load balancer with one backend service, set that backend service as the default. If you're configuring your load balancer to use multiple backend services, pick one of the backend services to be the URL map default.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps
          {
            "defaultService": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/DEFAULT_BACKEND_SERVICE_NAME",
            "name": "URL_MAP_NAME"
          }
          

Replace the following:

     * `DEFAULT_BACKEND_SERVICE_NAME`: the name of the load balancer's default. The default is used when no host rule matches the requested hostname.
     * `URL_MAP_NAME`: a name for the URL map.
  3. If you're configuring your load balancer to use multiple backend services, complete this step. If your URL map only references one backend service, skip this step.

To add additional backend services to the URL map, make a `PATCH` request to the [`urlMaps.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps/patch).

For each backend service, add a path matcher and one or more host rules. You must create one path matcher for each backend service. Each host rule can reference only one path matcher, but two or more host rules can reference the same path matcher.

You can add multiple path matchers and host rules by making a single API request.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/URL_MAP_NAME
          {
            "pathMatchers": [
              {
                "name": "PATH_MATCHER_NAME_1",
                "defaultService": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME_1"
              },
              {
                "name": "PATH_MATCHER_NAME_2",
                "defaultService": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME_2"
              }
            ],
            "hostRules": [
              {
                "hosts": ["HOSTNAME_1"],
                "pathMatcher": "PATH_MATCHER_NAME_1"
              },
              {
                "hosts": ["HOSTNAME_2"],
                "pathMatcher": "PATH_MATCHER_NAME_2"
              }
            ]
          }
          

Replace the following:

     * `PATH_MATCHER_NAME_1`: a name for the first path matcher.
     * `BACKEND_SERVICE_NAME_1`: the name of the first backend service.
     * `PATH_MATCHER_NAME_2`: a name for the second path matcher.
     * `BACKEND_SERVICE_NAME_2`: the name of the second backend service.
     * `HOSTNAME_1`: the hostname to send requests to for the first service—for example, `pubsub.example.com`.
     * `HOSTNAME_2`: the hostname to send requests to for the second service.
  4. To create a target HTTPS proxy, make a `POST` request to the [`targetHttpsProxies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetHttpsProxies
          {
            "name": "PROXY_NAME",
            "sslCertificates": [
              "https://certificatemanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/certificates/CERTIFICATE_NAME"
            ],
            "urlMap": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/URL_MAP_NAME"
          }
          

Replace the following:

     * `PROJECT_ID`: the ID of the project.
     * `PROXY_NAME`: a name for the target HTTPS proxy.
     * `CERTIFICATE_NAME`: the name of the certificate resource.
     * `URL_MAP_NAME`: the name of the URL map.
  5. To create a global forwarding rule for your load balancer, make a `POST` request to the [`globalForwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules/insert). The forwarding rule's network must contain a proxy-only subnet in the subnet of your forwarding rule's region.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules
          {
            "IPAddress": "IP_ADDRESS",
            "loadBalancingScheme": "INTERNAL_MANAGED",
            "name": "FORWARDING_RULE_NAME",
            "network": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME",
            "portRange": "443",
            "subnetwork": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/SUBNET_REGION/subnetworks/SUBNET_NAME",
            "target": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetHttpsProxies/PROXY_NAME"
          }
          

Replace the following:

     * `IP_ADDRESS`: the internal IP address of the forwarding rule, which must be within the IP address range of the forwarding rule's subnet. To use a specific ephemeral IP address, provide the IP address—for example, `10.0.0.5`. To use a static internal IP address, provide the name of the IP address. To let Google Cloud select an ephemeral IP address, omit this field.
     * `FORWARDING_RULE_NAME`: the name of the forwarding rule.
     * `NETWORK_NAME`: the name of the forwarding rule's VPC network. This network must contain a proxy-only subnet in the region where you are creating the load balancer.
     * `SUBNET_REGION`: the region of the forwarding rule's subnet.
     * `SUBNET_NAME`: the name of the forwarding rule's subnet.



## Verify the configuration

To test your backend's connection to global Google APIs, do the following:

  1. If you don't have one, create a virtual machine (VM) instance in the VPC network where you configured the backend.
  2. Ensure that you haven't created firewall rules or firewall policies that override the [implied IPv4 allow egress rule](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules).
  3. Connect to the VM.
  4. From the VM, use `curl` to verify that you can query each API. This command sets the `Host` header and bypasses DNS resolution by specifying a user-defined IP address.

You can skip certificate validation using the `-k` flag. You might need to skip validation if you used a self-signed certificate to configure the target HTTPS proxy or if the VM doesn't have the certificate of the certificate authority that signed your certificate.
         
         curl -iv --resolve HOSTNAME:443:IP_ADDRESS \
            'https://HOSTNAME/RESOURCE_URI'
         

Replace the following:

     * `HOSTNAME`: the hostname that you configured in your URL map—for example, `pubsub.example.com`.
     * `IP_ADDRESS`: the IP address of your load balancer's forwarding rule.
     * `RESOURCE_URI`: the rest of the URI of the resource that you want to use for verification. For example, if the load balancer is forwarding requests to a regional endpoint for Pub/Sub, you could use `$discovery/rest?version=v1`.



## Configure DNS records

Configure DNS records for each host that you added to the URL map, pointing to the IP address of the forwarding rule. If you're using Cloud DNS to manage DNS, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records#adding_a_record). Otherwise, configure DNS records on your DNS server.

For example, say you have created the following configurations:

  * A Private Service Connect NEG that uses target service `pubsub.googleapis.com`.

  * A cross-region internal Application Load Balancer that uses that Private Service Connect NEG as a backend.

  * A URL map that defines a host rule for `pubsub.example.com`.




For this configuration to work correctly, you must create a DNS record that points `pubsub.example.com` to the IP address of the forwarding rule.

With this configuration, any requests sent to `pubsub.example.com` are sent to the load balancer, which forwards the request to `pubsub.googleapis.com`.

## Configure clients to send requests to the backend

To send requests through the backend instead of the public service endpoints, you must configure clients to send requests to the hostname that you defined in the load balancer's URL map—for example, `pubsub.example.com`. See the documentation for your client or client library for information about configuring it to use custom endpoints. The following pages include configuration steps for some common clients:

  * **Python** : you can configure `api_endpoint` in [Client options](https://googleapis.dev/python/google-api-core/latest/client_options.html).

  * **Go** : you can configure `WithEndpoint` in [ClientOptions](https://godoc.org/google.golang.org/api/option).

  * **.NET** : you can configure [`Endpoint`](https://docs.cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint) in the client's builder class.

  * **Java** : you can configure [`setEndpoint`](https://docs.cloud.google.com/java/docs/endpoints) in the client's settings class.

  * **gcloud** : you can configure `api_endpoint_overrides` in the [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/topic/endpoint-override).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
