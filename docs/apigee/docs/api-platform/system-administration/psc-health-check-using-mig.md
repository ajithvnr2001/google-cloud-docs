---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/psc-health-check-using-mig/
title: Configure active health check for regional failover with Private Service Connect \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:46.828037+00:00
---

# Configure active health check for regional failover with Private Service Connect  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/psc-health-check-using-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure active health check for regional failover with Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document explains how to use Apigee to configure [active health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) when you use Private Service Connect for northbound network routing (traffic from clients to Apigee). Active health check is useful for preventing loss of network traffic in case of a regional failure.

## Overview

**Note:** Apigee supports health checking with Private Service Connect. If you want regional failover for an Apigee organization that has multiple instances across regions and that routes traffic through Private Service Connect, opt in to **PSC health check** instead—no MIG is required. For details, see the [PSC health check](https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check#psc-health-check) tab on _Performing health checks_. The MIG-based pattern described below remains supported as an alternative.

This document describes a managed-instance-group (MIG) based pattern for performing active health check on Apigee instances reached through Private Service Connect. You can use this pattern if you prefer to manage the health check infrastructure yourself rather than opting in to the built-in PSC health check (see note above).

You could use [outlier detection](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global#traffic_policies) for health monitoring; however during regional failures, you may lose some amount of traffic periodically as outlier detection uses real-time traffic as indicators. Outlier detection re-routes part of the live traffic periodically to check the health of the failed region.

Figure 1 shows the proposed architecture. A service endpoint connects to the service attachment in the Apigee instance, and a MIG proxies traffic to the service endpoint. You enable health check monitoring on the MIG.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/health-check-mig-workaround.png)**Figure 1.** Apigee architecture for active health check without VPC peering.![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/health-check-mig-workaround.png)

## MIG-based health check approach

### Prerequisites

You can apply the technique described in this document to Apigee installations that use VPC peering or do not use VPC peering. But in the case of a VPC peered installation, the active health check technique described here only applies if you are using Private Service Connect for your routing configuration.

Before performing the steps in this section:

  * For **non-VPC peering** installations: 
    1. Complete Apigee provisioning Steps 1 through 6 for [subscription-based](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered) or [Pay-as-you-go installations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo). At this time, the only option is to perform these steps using the command-line interface.
    2. Skip Step 7: Configure routing, and do the following steps instead.
  * For **VPC peering** installations that use Private Service Connect for routing: 
    1. Complete Apigee provisioning Steps 1 through 7 for [subscription-based](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli) or [Pay-as-you-go installations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo). At this time, the only option is to perform these steps using the command-line interface.
    2. Skip Step 8: Configure routing, and do the following steps instead. 



### 1\. Configure a Private Service Connect service endpoint for the Apigee service attachment

In this step, you create a Private Service Connect Service Endpoint that points to the service attachment in the Apigee instance: 

  1. Get the service attachment from the Apigee instance you created previously: 
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
           "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
           "instances": [
             {
               "name": "us-west1",
               "location": "us-west1",
               "host": "10.82.192.2",
               "port": "443",
               "createdAt": "1645731488019",
               "lastModifiedAt": "1646504754219",
               "diskEncryptionKeyName": "projects/my-project/locations/us-west1/keyRings/us-west1/cryptoKeys/dek",
               "state": "ACTIVE",
               "peeringCidrRange": "SLASH_22",
               "runtimeVersion": "1-7-0-20220228-190814",
               "ipRange": "10.82.192.0/22,10.82.196.0/28",
               "consumerAcceptList": [
                 "875609189304"
               ],
               "serviceAttachment": "**projects/bfac74a67a320c43a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw1** "
             }
           ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  2. Create a Private Service Connect Service Endpoint that points to the service attachment that you obtained from the instance response body in the previous step, as explained in [Create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint). 



### 2\. Configure a MIG that points to the service endpoint

In this step, you create a MIG that proxies traffic to the service endpoint. You can then enable active health check on the MIG. 

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

**Note:** MIGs are not global, they are regional. Therefore, for multi-region, you must create one MIG for each region and add them to the global load balancer's backend service.

#### 2A. Enable Private Google Access for a subnet of your VPC network

To enable [Private Google Access](https://cloud.google.com/vpc/docs/private-google-access) for a subnet of your VPC network, follow the steps listed in [Enabling Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).

**Note:** If you are doing a multi-region setup, you must do this step once for each region.

#### 2B. Set environment variables

**Multi-region** : A multi-region setup requires a separate MIG for each region..

The instructions in this section use environment variables to refer to repeatedly used strings. We recommend that you set these before continuing:
    
    
    MIG_NAME=YOUR_MIG_NAME  # A name you provide for the MIG
    VPC_NAME=default       # If you are using a [shared VPC](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs), use the shared VPC name
    VPC_SUBNET=default     # Private Google Access must be enabled for this subnet
    REGION=RUNTIME_REGION        # The same region as your Apigee runtime instance
    **SERVICE_ENDPOINT_IP=** YOUR_SERVICE_ENDPOINT_IP.  ## The endpoint IP of the service endpoint you just created

You'll use these variables several times during the remaining processes. If you wish to configure multiple regions, then create variables with values specific for each region.

#### 2C. Create a managed instance group

**Multi-region** : A multi-region setup requires a separate MIG for each region. If you are configuring multiple regions, repeat Steps 2b and 2c for each region, substituting the appropriate variables for each region.

In this step, you create and configure a managed instance group (MIG). 

  1. Create an [instance template](https://cloud.google.com/compute/docs/instance-templates) by executing the following command. 
         
         gcloud compute instance-templates create $MIG_NAME \
         --project $PROJECT_ID \
         --region $REGION \
         --network $VPC_NAME \
         --subnet $VPC_SUBNET \
         --tags=https-server,apigee-mig-proxy,gke-apigee-proxy \
         --machine-type e2-medium --image-family debian-12 \
         --image-project debian-cloud --boot-disk-size 20GB \
         --no-address \
         --metadata ENDPOINT=**$SERVICE_ENDPOINT_IP** ,startup-script-url=gs://apigee-5g-saas/apigee-envoy-proxy-release/latest/conf/startup-script.sh

As you can see from this command, machines are of type `e2-medium`. They run Debian 12 and have 20GB of disk. The `startup-script.sh` script configures the MIG to route inbound traffic from the load balancer to the Apigee instance.

  2. Create a [managed instance group](https://cloud.google.com/compute/docs/instance-groups) by executing the following command: 
         
         gcloud compute instance-groups managed create $MIG_NAME \
         --project $PROJECT_ID --base-instance-name apigee-mig \
         --size 2 --template $MIG_NAME --region $REGION

  3. Configure [autoscaling](https://cloud.google.com/compute/docs/instance-groups#autoscaling) for the group by executing the following command: **Note:** A regional MIG with e2-medium instances can support a maximum of 6 Gbps. If that is not sufficient for your throughput needs, consider upsizing the VM and/or increasing the number of replicas.
         
         gcloud compute instance-groups managed set-autoscaling $MIG_NAME \
         --project $PROJECT_ID --region $REGION --max-num-replicas 3 \
         --target-cpu-utilization 0.75 --cool-down-period 90

  4. Define a named port by executing the following command: 
         
         gcloud compute instance-groups managed set-named-ports $MIG_NAME \
         --project $PROJECT_ID --region $REGION --named-ports https:443




### 3\. Configure the load balancer with health check monitoring

In the following steps you configure a load balancer with health check monitoring.

#### 3A. Create an SSL certificate and key for the load balancer

You only need to create the credentials once, whether you are installing in single or multi regions. In a later step, you will associate these credentials with the load balancer's target HTTPS proxy.

You can create the credentials with:

  * Your own certificate from a certificate authority
  * A [Google-managed SSL certificate](https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)
  * A [self-signed certificate](https://docs.cloud.google.com/apigee/docs/hybrid/latest/environment-self-signed-tls) (not recommended for production).



For more information on creating and using SSL certificates for Google Cloud load balancer, see [SSL certificates](https://cloud.google.com/load-balancing/docs/https#ssl_certificates#ssl-certificates) and [SSL certificate overview](https://cloud.google.com/load-balancing/docs/ssl-certificates).

In the following example, we create a Google-managed SSL certificate: 

  1. Create these environment variables: 
         
         **CERTIFICATE_NAME** =YOUR_CERT_NAME
         **DOMAIN_HOSTNAME** =YOUR_DOMAIN_HOSTNAME 

Set `DOMAIN_HOSTNAME` to a valid domain hostname that you have registered. In a later step, you will obtain the load balancer's IP address and update the domain A record to point to that address. For example, a domain hostname might look like this: `foo.example.com`. 

  2. Execute the [ gcloud compute ssl-certificates create](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command: 
         
         gcloud compute ssl-certificates create **$CERTIFICATE_NAME** \
         --domains=**$DOMAIN_HOSTNAME** \
         --project **$PROJECT_ID** \
         --global

The certificate can take up to an hour to be provisioned. To check the status of the provisioning, execute this command:
         
         gcloud compute ssl-certificates describe $CERTIFICATE_NAME \
         --global \
         --format="get(name,managed.status, managed.Status)"

**Note:** You can create multiple DNS A records for your environment group hostnames that all point to the same load balancer IP address. 



#### 3B. Create a health check

  1. Create a [health check](https://cloud.google.com/load-balancing/docs/health-checks): 
         
         gcloud compute health-checks create https HEALTH_CHECK_NAME \
         --project $PROJECT_ID --port 443 --global \
         --request-path /healthz/ingress

You'll use this health check to ensure that the backend service is running. For configuring more advanced health checks against a specific proxy, see [Performing health checks](https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check).

**Note:** If you get the following error while trying to create a health check: 
         
         ERROR: unrecognized arguments: --global,

Try updating `gcloud` using the `gcloud components update` command.

  2. Create a [backend service](https://cloud.google.com/load-balancing/docs/backend-service): 
         
         gcloud compute backend-services create PROXY_BACKEND_NAME \
         --project $PROJECT_ID \
         --protocol HTTPS \
         --health-checks HEALTH_CHECK_NAME \
         --port-name https \
         --timeout 302s \
         --connection-draining-timeout 300s \
         --global

**Note:** As documented in the Apigee [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#cloud-timeouts), Apigee's ingress (internal load balancer) has a default 300 seconds timeout. Setting the load balancer's backend-services timeout to 302 seconds will allow the backend-services command to fully complete within Apigee in the event there are long running transactions. Setting this value to something less, such as 60 seconds, may cause the load balancer to time out before the request has completed, resulting in 502 responses.
  3. Add the MIG to your backend service with the following command: **Multi-region:** For a multi-region setup, you must create a separate MIG for each region, then repeat this step to add each MIG to the backend service. Be sure to substitute the appropriate `REGION` and `MIG_NAME` variables for each region.
         
         gcloud compute backend-services add-backend PROXY_BACKEND_NAME \
         --project $PROJECT_ID --instance-group $MIG_NAME \
         --instance-group-region $REGION \
         --balancing-mode UTILIZATION --max-utilization 0.8 --global

  4. Create a [load balancing URL map](https://cloud.google.com/load-balancing/docs/url-map) with the following command: 
         
         gcloud compute url-maps create MIG_PROXY_MAP_NAME \
         --project $PROJECT_ID --default-service PROXY_BACKEND_NAME

  5. Create a [load balancing target HTTPS proxy](https://cloud.google.com/load-balancing/docs/target-proxies) with the following command: 
         
         gcloud compute target-https-proxies create MIG_HTTPS_PROXY_NAME \
         --project $PROJECT_ID --url-map MIG_PROXY_MAP_NAME \
         --ssl-certificates **$CERTIFICATE_NAME**




#### 3C. Get a reserved IP address and create firewall rules

You must assign an IP address to the load balancer and then create rules that allow the load balancer to access the MIG. You only need to do this step once, whether you are installing in single or multi regions.

  1. [Reserve an IP address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#reserve_new_static) for the load balancer: 
         
         gcloud compute addresses create ADDRESSES_NAME \
         --project $PROJECT_ID \
         --ip-version=IPV4 \
         --global

  2. Create a [global forwarding rule](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts) with the following command: 
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
         --project $PROJECT_ID --address ADDRESSES_NAME --global \
         --target-https-proxy MIG_HTTPS_PROXY_NAME --ports 443

  3. Get the reserved IP address by executing the following command: 
         
         gcloud compute addresses describe ADDRESSES_NAME \
         --project $PROJECT_ID --format="get(address)" --global

  4. **Important step:** Go to the site, DNS host, or ISP where your DNS records are managed, and make sure your domain's DNS record resolves to the IP address of the Google Cloud load balancer. This address is the IP value returned in the last step. For more detail, see [ Update the DNS A and AAAA records to point to the load balancer's IP address](https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns).
  5. Create a firewall rule that lets the load balancer access the MIG by using the following command: 
         
         gcloud compute firewall-rules create FIREWALL_RULE_NAME \
         --description "Allow incoming from GLB on TCP port 443 to Apigee Proxy" \
         --project $PROJECT_ID --network $VPC_NAME --allow=tcp:443 \
         --source-ranges=130.211.0.0/22,35.191.0.0/16 --target-tags=gke-apigee-proxy

Note that the IP address ranges `130.211.0.0/22` and `35.191.0.0/16` are the source IP address ranges for Google Load Balancing. This firewall rule allows Google Cloud Load Balancing to make health check requests to the MIG.




Apigee provisioning is complete. Go to [Deploy a sample proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#deploy-proxy). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
