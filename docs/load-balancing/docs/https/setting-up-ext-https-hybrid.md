---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-ext-https-hybrid/
title: Set up a classic Application Load Balancer with hybrid connectivity \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:43.319213+00:00
---

# Set up a classic Application Load Balancer with hybrid connectivity  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-ext-https-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a classic Application Load Balancer with hybrid connectivity Stay organized with collections  Save and categorize content based on your preferences. 

This page illustrates how to deploy the classic Application Load Balancer to load balance traffic to network endpoints that are on-premises or in other public clouds and are reachable by using [hybrid connectivity](https://cloud.google.com/hybrid-connectivity).

**Note:** For regional external Application Load Balancer instructions, see [Set up a regional external Application Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-hybrid). For global external Application Load Balancer instructions, see [Set up a global external Application Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-ext-global-https-hybrid).

After you complete these tasks, you can optionally explore enabling additional services (such as Cloud CDN and Google Cloud Armor) and advanced traffic management features.

If you haven't already done so, review the [Hybrid connectivity NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) to understand the network requirements to set up hybrid load balancing.

## Setup overview

The example on this page sets up the following sample deployment:

[ ![External Application Load Balancer example for hybrid connectivity.](https://docs.cloud.google.com/static/load-balancing/images/hybrid-ext-https-lb.svg)](https://docs.cloud.google.com/static/load-balancing/images/hybrid-ext-https-lb.svg) External Application Load Balancer example for hybrid connectivity (click to enlarge).

You must configure hybrid connectivity before you attempt to set up a hybrid load balancing deployment. This document does not include the hybrid connectivity setup.

Depending on your choice of hybrid connectivity product (either Cloud VPN or Cloud Interconnect (Dedicated or Partner)), use the relevant product documentation to configure this.

## Permissions

To set up hybrid load balancing, you must have the following permissions:

  * **On Google Cloud**

    * Permissions to establish hybrid connectivity between Google Cloud and your on-premises environment or other cloud environments. For the list of permissions needed, see the relevant [Network Connectivity product documentation](https://docs.cloud.google.com/network-connectivity/docs).
    * Permissions to create a hybrid connectivity NEG and the load balancer. The [Compute Load Balancer Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) contains the permissions required to perform the tasks described in this guide.
  * **On your on-premises environment or other non-Google Cloud cloud environment**

    * Permissions to configure network endpoints that allow services on your on-premises environment or other cloud environments to be reachable from Google Cloud by using an `IP:Port` combination. For more information, contact your environment's network administrator.
    * Permissions to create firewall rules on your on-premises environment or other cloud environments to allow Google's health check probes to reach the endpoints.



Additionally, to complete the instructions on this page, you need to create a hybrid connectivity NEG, a load balancer, and zonal NEGs (and their endpoints) to serve as Google Cloud-based backends for the load balancer.

You should be either a project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you should have the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)  
Add and remove firewall rules | [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`)  
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  
  
## Optional: Use BYOIP addresses

With bring your own IP (BYOIP), you can import your own public addresses to Google Cloud to use the addresses with Google Cloud resources. For example, if you import your own IPv4 addresses, you can assign one to the forwarding rule when you configure your load balancer. When you follow the instructions in this document to , provide the BYOIP address as the **IP address**.

For more information about using BYOIP, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip). 

## Establish hybrid connectivity

Your Google Cloud and on-premises environment or other cloud environments must be connected through [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) by using either Cloud Interconnect VLAN attachments or Cloud VPN tunnels with Cloud Router or Router appliance VMs. We recommend that you use a high availability connection.

A Cloud Router enabled with [global dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am-default) learns about the specific endpoint through Border Gateway Protocol (BGP) and programs it into your Google Cloud VPC network. Regional dynamic routing is not supported. Static routes are also not supported.

You can use either the same network or a different VPC network within the same project to configure both hybrid networking (Cloud Interconnect or Cloud VPN or a Router appliance VM) and the load balancer. Note the following:

  * If you use different VPC networks, the two networks must be connected using either VPC Network Peering or they must be [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) on the same [NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

  * If you use the same VPC network, ensure that your VPC network's subnet CIDR ranges don't conflict with your remote CIDR ranges. When IP addresses overlap, subnet routes are prioritized over remote connectivity.




For instructions, see the following documentation:

  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)

**Important:** Don't proceed with the instructions on this page until you set up hybrid connectivity between your environments.

## Set up your environment that is outside Google Cloud

Perform the following steps to set up your on-premises environment or other cloud environment for hybrid load balancing:

  * Configure network endpoints to expose on-premises services to Google Cloud (`IP:Port`).
  * Configure firewall rules on your on-premises environment or other cloud environment.
  * Configure Cloud Router to advertise certain required routes to your private environment.



### Set up network endpoints

After you set up hybrid connectivity, you configure one or more network endpoints within your on-premises environment or other cloud environments that are reachable through Cloud Interconnect or Cloud VPN or Router appliance by using an `IP:port` combination. This `IP:port` combination is configured as one or more endpoints for the hybrid connectivity NEG that is created in Google Cloud later on in this process.

If there are multiple paths to the IP endpoint, routing follows the behavior described in the [Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview).

### Set up firewall rules

The following firewall rules must be created on your on-premises environment or other cloud environment: 

  * Create an ingress allow firewall rule to allow traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).




### Advertise routes

Configure Cloud Router to [advertise the following custom IP ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) to your on-premises environment or other cloud environment:

  * The ranges used by [Google's health check probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).



## Set up the Google Cloud environment

For the following steps, make sure you use the same VPC network (called NETWORK in this procedure) that was used to configure hybrid connectivity between the environments.

### Create the subnet for the backends

This subnet is used to create the load balancer's zonal NEG backends, the frontend, and the internal IP address.

Create this subnet in the NETWORK network that was used to configure hybrid connectivity between the environments.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Go to the network that was used to configure hybrid connectivity between the environments.

  3. In the **Subnets** section:

     1. Set the **Subnet creation mode** to **Custom**.
     2. In the **New subnet** section, enter the following information: 
        * **Name** : LB_SUBNET_NAME
        * **Region** : REGION
        * **IP address range** : LB_SUBNET_RANGE
     3. Click **Done**.
  4. Click **Create**.




###  gcloud 

Create a subnet in the NETWORK network that was used to configure hybrid connectivity between the environments.
    
    
    gcloud compute networks subnets create LB_SUBNET_NAME \
        --network=NETWORK \
        --range=LB_SUBNET_RANGE \
        --region=REGION
    

### Create firewall rule

In this example, you create the following firewall rule:

  * `fw-allow-health-check`: An ingress rule, applicable to the Google Cloud instances being load balanced, that allows traffic from the load balancer and [Google Cloud health checking systems](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check` to identify the backend VMs to which it should apply.




###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** :

     1. Enter a **Name** of `fw-allow-health-check`.
     2. In the **Network** section, select `NETWORK`.
     3. Under **Targets** , select **Specified target tags**.
     4. Populate the **Target tags** field with `allow-health-check`.
     5. Set **Source filter** to **IPv4 ranges**.
     6. Set **Source IPv4 ranges** to `35.191.0.0/16`.
     7. Under **Protocols and ports** , select **Specified protocols and ports**.
     8. Select the checkbox next to **TCP** and type `80` for the port numbers.
  3. Click **Create**. 




###  gcloud 

  1. Create the `fw-allow-health-check-and-proxy` rule to allow the load balancer and Google Cloud health checks to communicate with backend instances on TCP port `80`.

Replace NETWORK with the name of the VPC network used to configure hybrid connectivity.
         
         gcloud compute firewall-rules create fw-allow-health-check \
             --network=NETWORK \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check \
             --source-ranges=35.191.0.0/16 \
             --rules=tcp:80
         




### Set up the zonal NEG

For Google Cloud-based backends, we recommend you configure multiple zonal NEGs in the same region where you configured hybrid connectivity.

For this example, we set up a zonal NEG (with `GCE_VM_IP_PORT` type endpoints) in the REGION region. First create the VMs in the GCP_NEG_ZONE zone. Then create a zonal NEG in the same GCP_NEG_ZONE and add the VMs' network endpoints to the NEG.

#### Create VMs

###  Console 

  1. Go to the VM instances page in the Google Cloud console.   
[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set the **Name** to `vm-a1`.

  4. For the **Region** , choose REGION.

  5. For the **Zone** , choose GCP_NEG_ZONE.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. Click **Choose** to change the image if necessary.

  7. Click **Advanced options** and make the following changes:

     * Click **Networking** and add the following **Network tags** : `allow-health-check`.
     * Click **Edit** edit under **Network interfaces** and make the following changes then click **Done** : 
       * **Network** : NETWORK
       * **Subnet** : LB_SUBNET_NAME
       * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
     * Click **Management**. In the **Startup script** field, copy and paste the following script contents. The script contents are identical for all four VMs:
           
           #! /bin/bash
           apt-get update
           apt-get install apache2 -y
           a2ensite default-ssl
           a2enmod ssl
           vm_hostname="$(curl -H "Metadata-Flavor:Google" \
           http://metadata.google.internal/computeMetadata/v1/instance/name)"
           echo "Page served from: $vm_hostname" | \
           tee /var/www/html/index.html
           systemctl restart apache2
           

  8. Click **Create**.

  9. Repeat the following steps to create a second VM, using the following name and zone combination:

     * Name: `vm-a2`, zone: GCP_NEG_ZONE



###  gcloud 

Create the VMs by running the following command two times, using these combinations for the name of the VM and its zone. The script contents are identical for both VMs.

  * VM_NAME of `vm-a1` and any GCP_NEG_ZONE zone of your choice
  * VM_NAME of `vm-a2` and the same GCP_NEG_ZONE zone

To support **IPv4 traffic** , run the following command:
        
        gcloud compute instances create VM_NAME \
            --zone=GCP_NEG_ZONE \
            --image-family=debian-12 \
            --image-project=debian-cloud \
            --tags=allow-health-check \
            --ipv6-network-tier=PREMIUM
            --stack-type=IPV4_ONLY \
            --subnet=LB_SUBNET_NAME \
            --metadata=startup-script='#! /bin/bash
              apt-get update
              apt-get install apache2 -y
              a2ensite default-ssl
              a2enmod ssl
              vm_hostname="$(curl -H "Metadata-Flavor:Google" \
              http://metadata.google.internal/computeMetadata/v1/instance/name)"
              echo "Page served from: $vm_hostname" | \
              tee /var/www/html/index.html
              systemctl restart apache2'
        




#### Create the zonal NEG

###  Console 

To create a zonal network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click **Create network endpoint group**.
  3. Enter a **Name** for the zonal NEG. Referred to as GCP_NEG_NAME in this procedure.
  4. Select the **Network endpoint group type** : **Network endpoint group (Zonal)**.
  5. Select the **Network** : NETWORK
  6. Select the **Subnet** : LB_SUBNET_NAME
  7. Select the **Zone** : GCP_NEG_ZONE
  8. Enter the **Default port** : `80`.
  9. Click **Create**.



Add endpoints to the zonal NEG:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click the **Name** of the network endpoint group created in the previous step (GCP_NEG_NAME). You see the **Network endpoint group details** page.
  3. In the **Network endpoints in this group** section, click **Add network endpoint**. You see the **Add network endpoint** page.
  4. Select a **VM instance** to add its internal IP addresses as network endpoints. In the **Network interface** section, the name, zone, and subnet of the VM is displayed.
  5. In the **IPv4 address** field, enter the IPv4 address of the new network endpoint. 
  6. Select the **Port type**. 
     1. If you select **Default** , the endpoint uses the default port `80` for all endpoints in the network endpoint group. This is sufficient for our example because the Apache server is serving requests at port `80`.
     2. If you select **Custom** , enter the **Port number** for the endpoint to use.
  7. To add more endpoints, click **Add network endpoint** and repeat the previous steps.
  8. After you add all the endpoints, click **Create**.



###  gcloud 

  1. Create a zonal NEG (with `GCE_VM_IP_PORT` endpoints) using the [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create) command:
         
         gcloud compute network-endpoint-groups create GCP_NEG_NAME \
             --network-endpoint-type=GCE_VM_IP_PORT \
             --zone=GCP_NEG_ZONE \
             --network=NETWORK \
             --subnet=LB_SUBNET_NAME
         

You can either specify a `--default-port` while creating the NEG, or [specify a port number for each endpoint](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#adding-endpoints) as shown in the next step. 

  2. Add single-stack endpoints to GCP_NEG_NAME.
         
         gcloud compute network-endpoint-groups update GCP_NEG_NAME \
             --zone=GCP_NEG_ZONE \
             --add-endpoint='instance=vm-a1,port=80' \
             --add-endpoint='instance=vm-a2,port=80'
         




### Set up the hybrid connectivity NEG

When creating the NEG, use a ZONE that minimizes the geographic distance between Google Cloud and your on-premises or other cloud environment. For example, if you are hosting a service in an on-premises environment in Frankfurt, Germany, you can specify the `europe-west3-a` Google Cloud zone when you create the NEG.

Moreover, if you're using Cloud Interconnect, the ZONE used to create the NEG should be in the same region where the hybrid connectivity Cloud Interconnect VLAN attachment was configured.

For the available regions and zones, see the [Compute Engine documentation: Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

###  Console 

To create a hybrid connectivity network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click **Create network endpoint group**.
  3. Enter a **Name** for the hybrid NEG. Referred to as ON_PREM_NEG_NAME in this procedure.
  4. Select the **Network endpoint group type** : **Hybrid connectivity network endpoint group (Zonal)**.
  5. Select the **Network** : **NETWORK**
  6. Select the **Subnet** : **LB_SUBNET_NAME**
  7. Select the **Zone** : **ON_PREM_NEG_ZONE**
  8. Enter the **Default port**.
  9. Click **Create**



Add endpoints to the hybrid connectivity NEG:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click the **Name** of the network endpoint group created in the previous step (**ON_PREM_NEG_NAME**). You see the **Network endpoint group detail** page.
  3. In the **Network endpoints in this group** section, click **Add network endpoint**. You see the **Add network endpoint** page.
  4. Enter the **IP address** of the new network endpoint.
  5. Select the **Port type**. 
     1. If you select **Default** , the endpoint uses the default port for all endpoints in the network endpoint group.
     2. If you select **Custom** , you can enter a different **Port number** for the endpoint to use.
  6. To add more endpoints, click **Add network endpoint** and repeat the previous steps.
  7. After you add all the non-Google Cloud endpoints, click **Create**.



###  gcloud 

  1. Create a hybrid connectivity NEG using the [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create) command.
         
         gcloud compute network-endpoint-groups create ON_PREM_NEG_NAME \
             --network-endpoint-type=NON_GCP_PRIVATE_IP_PORT \
             --zone=ON_PREM_NEG_ZONE \
             --network=NETWORK
         

  2. Add the endpoint to `on-prem-neg`:
         
         gcloud compute network-endpoint-groups update ON_PREM_NEG_NAME \
             --zone=ON_PREM_NEG_ZONE \
             --add-endpoint="ip=ON_PREM_IP_ADDRESS_1,port=PORT_1" \
             --add-endpoint="ip=ON_PREM_IP_ADDRESS_2,port=PORT_2"
         




You can use this command to add the network endpoints you previously configured on-premises or in your cloud environment. Repeat `--add-endpoint` as many times as needed.

You can repeat these steps to create multiple hybrid NEGs if needed.

## Configure the load balancer

###  Console 

**Note:** You cannot use the Google Cloud console to create a load balancer that has mixed zonal and hybrid connectivity NEGs backends in a single backend service. Use either `gcloud` or the REST API instead.

###  gcloud 

  1. Create a global static external IP address to which external clients send traffic. 
         
         gcloud compute addresses create LB_IP_ADDRESS_NAME \
               --global
           

  2. Create a [health check](https://docs.cloud.google.com/load-balancing/docs/health-checks) for the backends. 
         
         gcloud compute health-checks create http HTTP_HEALTH_CHECK_NAME \
               --use-serving-port
           

  3. Create a backend service. You add both the zonal NEG and the hybrid connectivity NEG as backends to this backend service.
    
    gcloud compute backend-services create BACKEND_SERVICE \
          --health-checks=HTTP_HEALTH_CHECK_NAME \
          --global
      

  4. Add the zonal NEG as a backend to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE \
               --global \
               --balancing-mode=RATE \
               --max-rate-per-endpoint=MAX_REQUEST_RATE_PER_ENDPOINT \
               --network-endpoint-group=GCP_NEG_NAME \
               --network-endpoint-group-zone=GCP_NEG_ZONE
            

For details about configuring the balancing mode, see the gcloud CLI documentation for the [`--max-rate-per-endpoint`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend#--max-rate-per-endpoint) parameter. 
  5. Add the hybrid NEG as a backend to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE \
               --global \
               --balancing-mode=RATE \
               --max-rate-per-endpoint=MAX_REQUEST_RATE_PER_ENDPOINT \
               --network-endpoint-group=ON_PREM_NEG_NAME \
               --network-endpoint-group-zone=ON_PREM_NEG_ZONE
           

  6. Create a URL map to route incoming requests to the backend service. 
         
         gcloud compute url-maps create URL_MAP_NAME \
               --default-service BACKEND_SERVICE
           

  7. _Perform this step only if you want to create an HTTPS load balancer. This is not required for HTTP load balancers._  
To create an HTTPS load balancer, you must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. You can create an SSL certificate resource using either a Google-managed SSL certificate or a self-managed SSL certificate. Using Google-managed certificates is recommended because Google Cloud obtains, manages, and renews these certificates automatically.  
  
To create a Google-managed certificate, [ you must have a domain](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#before_you_begin). If you don't have a domain, you can use a self-signed SSL certificate for testing.  
  
To create a Google-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
             --domains DOMAIN
         

To create a self-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create SSL_CERTIFICATE_NAME \
             --certificate CRT_FILE_PATH \
             --private-key KEY_FILE_PATH
         

  8. Create a target HTTP(S) proxy to route requests to your URL map.  
  
For an HTTP load balancer, create an HTTP target proxy: 
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
             --url-map=URL_MAP_NAME
         

For an HTTPS load balancer, create an HTTPS target proxy. The proxy is the portion of the load balancer that holds the SSL certificate for HTTPS Load Balancing, so you also load your certificate in this step. 
         
         gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
             --ssl-certificates=SSL_CERTIFICATE_NAME \
             --url-map=URL_MAP_NAME
         

  9. Create a forwarding rule to route incoming requests to the proxy.  
  
For an HTTP load balancer: 
         
         gcloud compute forwarding-rules create HTTP_FORWARDING_RULE_NAME \
             --address=LB_IP_ADDRESS_NAME \
             --target-http-proxy=TARGET_HTTP_PROXY_NAME \
             --global \
             --ports=80
         

For an HTTPS load balancer: 
         
         gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE_NAME \
             --address=LB_IP_ADDRESS_NAME \
             --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
             --global \
             --ports=443
         




## Connect your domain to your load balancer

After the load balancer is created, note the IP address that is associated with the load balancer—for example, `30.90.80.100`. To point your domain to your load balancer, create an `A` record by using your domain registration service. If you added multiple domains to your SSL certificate, you must add an `A` record for each one, all pointing to the load balancer's IP address. For example, to create `A` records for `www.example.com` and `example.com`, use the following:
    
    
    NAME                  TYPE     DATA
    www                   A        30.90.80.100
    @                     A        30.90.80.100
    

If you use Cloud DNS as your DNS provider, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Testing the load balancer

**Note:** It might take a few minutes for the load balancer configuration to propagate globally after you first deploy it.

Now that you have configured your load balancer, you can start sending traffic to the load balancer's IP address.

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click on the load balancer you just created.

  3. Note the **IP Address** of the load balancer.

  4. Send traffic to the load balancer.

     * If you created an **_HTTP load balancer_** , you can test your load balancer using a web browser by going to `http://IP_ADDRESS`. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the service you have exposed through the endpoint.

     * If you created an **_HTTPS load balancer_** , you can test your load balancer by using `curl` as follows. Replace `IP_ADDRESS` with the load balancer's IP address. You should be directed to the service you have exposed through the endpoint.
           
           curl -k https://IP_ADDRESS
           

If that does not work and you are using a Google-managed certificate, confirm that your certificate resource's status is ACTIVE. For more information, see [Google-managed SSL certificate resource status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#certificate-managed-status). Then test the domain pointing to the load balancer's IP address. For example:
           
           curl -s https://DOMAIN_NAME
           

Replace DOMAIN_NAME with your application domain name, for example, `test.example.com`.

  5. Testing the non-Google Cloud endpoints depends on the service you have exposed through the hybrid NEG endpoint.




## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
