---
url: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls/
title: Access published services through backends \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:12.416286+00:00
---

# Access published services through backends  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access published services through backends 

This guide describes how to configure a global external Application Load Balancer with a Private Service Connect backend to access a service that is [published by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

[ ![](https://docs.cloud.google.com/static/vpc/images/private-service-connect-xlb-services.png)](https://docs.cloud.google.com/static/vpc/images/private-service-connect-xlb-services.png) Using a backend that's based on a global external Application Load Balancer lets service consumers with internet access send traffic to services in the service producer's VPC network (click to enlarge).

For more information, see [About Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).

## Roles

The [Compute Load Balancer Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) contains the permission required to perform the tasks described in this guide.

## Before you begin

  * If you want to publish your own service, see [Publish services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

  * If you're connecting a service that is published by a third party, ask the service producer for the following information:

    * The URI of the service attachment for the service that you want to connect to. The service attachment has this format: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`

    * Any requirements for what DNS names you use to send requests to. You might need to use specific DNS names in your URL map configuration or DNS configuration.




## Create a network endpoint group

Create a Private Service Connect NEG that points to the service attachment for the published service that you want to access. If the [published service is deployed across multiple different regions](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#multi-region-services), create one NEG per service attachment.

Each Private Service Connect NEG consumes a `/32` IP address so that the load balancer can communicate with it.

###  Console 

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/add)  


  2. Click **Create network endpoint group**.

  3. Enter a **Name** for the network endpoint group.

  4. For the **Network endpoint group type** , select **Network endpoint group (Private Service Connect)**.

  5. Select the target type **Published service**.

  6. For **Target service** , enter the URI of the service attachment.

  7. Select the **Network** and **Subnet** to create the network endpoint group in.

The subnet must be in the same region as the published service.

  8. Click **Create**.




###  gcloud 
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=private-service-connect \
        --psc-target-service=TARGET_SERVICE \
        --region=REGION \
        --network=NETWORK \
        --subnet=SUBNET
    

Replace the following:

  * `NEG_NAME`: a name for the network endpoint group.

  * `TARGET_SERVICE`: the service attachment that you want to connect to.

  * `REGION`: the region to create the network endpoint group in. The region must be the same region as the target service.

  * `NETWORK`: the network to create the network endpoint group in. If omitted, the default network is used.

  * `SUBNET`: the subnet to create the network endpoint group in. The subnet must be in the same region as the target service. A subnet must be provided if you provide the network. If both network and subnet are omitted, the default network is used, and the default subnet in the specified `REGION` is used.




## Reserve an external IP address for the load balancer

To reserve an external IP address for the load balancer, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/addresses/list)

  2. To reserve an IPv4 address, click **Reserve static address**.

  3. Assign a **Name** for the IP address resource.

  4. Set the Network tier to **Premium**.

  5. Set the **IP version** to **IPv4**.

  6. Set the **Type** to **Global**.

  7. Click **Reserve**.




###  gcloud 

  1. Reserve a global external IPv4 address for the load balancer.
         
         gcloud compute addresses create ADDRESS_NAME \
             --ip-version=IPV4 --global
         

Replace `ADDRESS_NAME` with a name for the IP address resource.

  2. Run this command to view the reserved IP address:
         
         gcloud compute addresses describe ADDRESS_NAME \
           --format="get(address)" --global
         




## Create an SSL certificate resource

To create an _HTTPS_ load balancer, you must add an SSL certificate resource to the load balancer's front end. Create an SSL certificate resource by using either a [Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) or a [self-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).

  * **Google-managed certificates.** We recommend that you use Google-managed certificates because Google Cloud obtains, manages, and renews these certificates automatically. To create a Google-managed certificate, you must have a domain and the DNS records for that domain to provision the certificate. Additionally, you need to update the domain's DNS A record to point to the load balancer's IP address created in the previous step; for detailed instructions, see [Use Google-managed certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs).

  * **Self-managed certificates.** Self-managed SSL certificates are certificates that you obtain, provision, and renew yourself. Self-managed certificates can be signed by a certificate authority or can be self-signed. If they are signed by a certificate authority, you must have a domain. Additionally, you need to update the domain's DNS A record to point to the load balancer's IP address created in the previous step; for detailed instructions, see [Use self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).

If you do not want to set up a domain at this time, you can use a self-signed SSL certificate for testing.

**Warning:** Don't use a self-signed certificate for production purposes.



These instructions assume that you have already created an SSL certificate resource.

## Configure the load balancer

Configure a [global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with advanced traffic management capabilities (load balancing scheme set to `EXTERNAL_MANAGED`) to connect to a managed service.

If you are connecting to a [published service that is deployed across multiple regions](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#multi-region-services), and you have created multiple Private Service Connect NEGs to connect to each service attachment, you can add all of the NEGs to the backend service.

Although the Private Service Connect NEG is regional, all other load balancing components in this configuration are global.

###  Console 

#### Select the load balancer type

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Application Load Balancer (HTTP/HTTPS)** and click **Next**.
  4. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  5. For **Global or single region deployment** , select **Best for global workloads** and click **Next**.
  6. For **Load balancer generation** , select **Global external Application Load Balancer** and click **Next**.
  7. Click **Configure**.



#### Basic configuration

  1. Enter a **Load balancer name**.
  2. Keep the window open to continue.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. Click **Add frontend IP and port**.
  3. Enter a **Name** for the load balancer.
  4. In the **Protocol** field, select **HTTPS (includes HTTP/2)**.
  5. Ensure that the **Port** is set to `443` to allow HTTPS traffic.
  6. For **IP address** , select the IP address that you reserved.

  7. Click the **Certificate** list and select the certificate that you have created.

  8. Click **OK**.

  9. Click **Done**.




#### Backend configuration

The Private Service Connect network endpoint group is a type of load balancer backend. Add all Private Service Connect NEGs for the same managed service to the backend service.

  1. Click **Backend configuration**.
  2. Click the **Backend services & backend buckets** list, and then click **Create a backend service**.
  3. Enter a **Name** for the backend service.
  4. Set the **Backend type** to **Private Service Connect network endpoint group**.
  5. In the **Backends** section, click the **Private Service Connect network endpoint group** list, and select the Private Service Connect NEG that you created. Click **Done**.
  6. If you created more than one Private Service Connect NEG, click **Add backend** to select another NEG.

Repeat this step until all NEGs for this managed service are added to the backend service.

  7. Click **Create**.




#### Routing rules

Because this configuration contains only one backend service, the default routing rule is sufficient and you do not need to make any changes in this section.

#### Review and finalize

  1. To review the configuration, click **Review and finalize**.
  2. Click **Create**.



###  gcloud 

  1. Create a backend service for the managed service that you want to connect to.
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --protocol=HTTPS \
             --global
         

Replace `BACKEND_SERVICE_NAME` with the name of the backend service.

  2. Add the Private Service Connect NEG that points to the target service.

If you have created multiple NEGs in different regions for the same service, repeat this step to add all of the NEGs to the backend service.
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --network-endpoint-group=NEG_NAME \
           --network-endpoint-group-region=REGION \
           --global
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `NEG_NAME`: the name of the network endpoint group.
     * `REGION`: the region of the network endpoint group.
  3. Create a URL map for the load balancer.

A URL map must reference a default backend service. Configure the backend service that you have created as the default backend service.
         
         gcloud compute url-maps create URL_MAP_NAME \
           --default-service=BACKEND_SERVICE_NAME \
           --global
         

Replace the following:

     * `URL_MAP_NAME`: a name for the URL map.

     * `BACKEND_SERVICE_NAME`: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.

  4. Create the target HTTPS proxy.

Use the SSL certificate resource that you created to create a target HTTPS proxy.
         
         gcloud compute target-https-proxies create PROXY_NAME \
           --url-map=URL_MAP_NAME \
           --ssl-certificates=CERTIFICATE
         

Replace the following:

     * `PROXY_NAME`: a name for the target HTTPS proxy.
     * `URL_MAP_NAME`: the name of the URL map.
     * `CERTIFICATE`: the name of the certificate resource.
  5. Create the forwarding rule.
         
         gcloud compute forwarding-rules create FWD_RULE \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --network-tier=PREMIUM \
             --address=ADDRESS_NAME \
             --target-https-proxy=PROXY_NAME \
             --ports=443 \
             --global
         

Replace the following:

     * `FWD_RULE`: a name for the forwarding rule.

     * `ADDRESS_NAME`: the IP address resource that you reserved to use for the forwarding rule.

     * `PROXY_NAME`: the name of the target HTTPS proxy.




## Configure DNS records

If you want to access your Private Service Connect backend by using a DNS name, create DNS names for each external forwarding rule. The DNS record must correspond to a name in the URL map. Unless your URL map [rewrites the names](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt), the DNS record must also correspond to the names that the producer service expects.

If you're using Cloud DNS to manage DNS, see [adding a DNS record](https://docs.cloud.google.com/dns/docs/records#adding_a_record).

## Verify the configuration

  1. Create the VM instance.
         
         gcloud compute instances create VM_NAME \
             --network=NETWORK \
             --image-project=debian-cloud --image-family=debian-11 \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: a name for the virtual machine.

     * `NETWORK`: the network for the VM.

     * `ZONE`: the zone for the VM.

  2. Connect to the VM.
         
         gcloud compute ssh VM_NAME --zone=ZONE
         

  3. Use `curl` to verify the configuration. This command sets the `Host` header and bypasses DNS resolution by specifying a user-defined IP address. You can omit the port if you are using the default port for the protocol, for example, using port 443 for HTTPS.

You can skip certificate validation using the `-k` flag. You might need to skip validation if you used a self-signed certificate to configure the target HTTPS proxy, or if the VM does not have the certificate of the certificate authority that signed your certificate.
         
         curl [-k] -s 'https://HOST:443/RESOURCE_URI' \
             -H 'Host: HOST' \
             --connect-to HOST:443:FWD_RULE_IP_ADDRESS:443
         

Replace the following:

     * `HOST`: the hostname that is configured in the URL map.

     * `RESOURCE_URI`: the rest of the URI of the resource that you want to use for verification.

     * `FWD_RULE_IP_ADDRESS`: the IP address assigned to the forwarding rule.




## Known issues

### Health check failures with global NEGs

There is a known issue with consumer Private Service Connect NEGs that are configured for global access. A Private Service Connect NEG is configured for global access if it's associated with a [global backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service).

If you connect a Private Service Connect NEG that is configured for global access to a producer load balancer, and the service producer disables global access for that load balancer, health checks don't work correctly. As a result, traffic might be sent to unhealthy backends and dropped.

If you access a published service by using a Private Service Connect NEG that is configured for global access, and your backend is affected by this issue, do one of the following:

  * If you want to use global access, ask the service producer to [enable global access](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#global-access-service-attachments-backends) for their load balancer.
  * If you don't want to use global access, reconfigure your Private Service Connect NEG for regional access. To do this, you must [remove your Private Service Connect NEG from the global backend service](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend) and then [attach the NEG to a regional backend service](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend).



Reconfiguring your Private Service Connect NEG for regional access temporarily interrupts network traffic through your backend.

## Troubleshooting

### Backend creation succeeds, but connectivity is not established

If you successfully create a backend for published services but connectivity is not established, check the backend's [connection status](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#connection-statuses). The connection status might indicate steps that you can take to resolve the issue.

### Backend connection status is accepted, but traffic doesn't flow

If a backend has an `ACCEPTED` connection status, but traffic can't reach the published service, the service producer might have recently updated the target service of the service attachment. During a target service update, traffic is briefly interrupted. For information about recent or ongoing target service updates, or to verify the state of the service, contact the service producer.

### Backend creation succeeds, but the producer is refusing the connection

If you receive a `connection refused` error, it typically means that the producer backend server isn't listening on the port that the client is trying to connect to.

Ask the service producer to check if their service is listening on the port that you specified.

If the producer's service is hosted on an Internal passthrough Network Load Balancer that uses multiple ports, specify the appropriate producer port in your Private Service Connect NEG configuration. See [Producer port configuration](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#producer-ports).

### Backend has performance issues or connection timeouts

If your backend has performance issues or intermittent connection timeouts, it might be due to dropped packets. You can investigate dropped packets by checking the metrics that are described in the following sections.

#### Dropped packets to published service

The [`private_service_connect/consumer/dropped_sent_packets_count` metric](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#compute/private_service_connect/consumer/dropped_sent_packets_count) tracks packets from a Private Service Connect consumer such as a backend to a published service that are dropped because the backend exceeded its maximum connections to the service.

If a backend reports values for this metric, consider the following solutions to address specific limits described in [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections):

  * Reduce the number of connections through this backend.
  * Ask the service producer to increase the capacity of the published service—for example, by adding more virtual machine (VM) instances or network endpoints.
  * For IPv4 connections, if the service attachment is configured with one NAT IP address per endpoint or backend (the default), ask the service producer to do both of the following: 
    * [Update the service attachment](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint) to assign two NAT IP addresses per endpoint or backend.
    * Make sure that the producer backend VMs have sufficient vCPUs. Increasing the number of vCPUs in a backend VM can increase the per-backend connection limit. For specific limits, see [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections). Increasing the number of vCPUs doesn't affect the maximum connections for [services that use Envoy proxies](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#envoy-lb).



#### Dropped packets from published services

The [`private_service_connect/consumer/dropped_received_packets_count` metric](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#compute/private_service_connect/consumer/dropped_received_packets_count) tracks packets sent from a published service to a Private Service Connect consumer such as a backend that are dropped because Private Service Connect can't find a matching connection for response packets.

Private Service Connect only allows connections that are initiated from the consumer VPC network. When a consumer initiates a connection, the connection is tracked in order to match response packets from the published service with an existing connection. If Private Service Connect can't find a match for a response packet, the packet is dropped.

Private Service Connect might not find a match for a response packet if a published service sends response packets after a connection has timed out. If you see values for this metric, contact the service producer. They might be able to [configure their service to avoid this issue](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#nat-subnets-other).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
