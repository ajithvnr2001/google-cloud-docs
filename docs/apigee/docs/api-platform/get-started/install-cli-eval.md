---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval/
title: Provision an eval org with VPC peering \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:43.725953+00:00
---

# Provision an eval org with VPC peering  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision an eval org with VPC peering Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Summary of steps

This document explains how to install and configure an Apigee evaluation [organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts) (or _eval org_) from the command line. Eval orgs expire after 60 days and may have other limitations. See also [ Comparing eval and paid organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro#comparing). 

The provisioning steps are as follows:

  * Step 1: Define environment variables: Set up `gcloud` and define environment variables. The Google Cloud CLI manages authentication, local configuration, developer workflow, and interactions with the Google Cloud APIs. 
  * Step 2: Enable APIs: Apigee requires you to enable several Google Cloud APIs. 
  * Step 3: Configure service networking: Service networking automates the private connectivity set up (using VPC Network Peering) between your network and Apigee. 
  * Step 4: Create an organization: An Apigee organization (sometimes referred to as an org) is the top-level container in Apigee. It includes all of your environments and environment groups, users, API proxies, and related resources. 
  * Step 5: Configure routing: Allow external access or internal only access to your API. 
  * Step 6: Call the sample API proxy: Test the provisioning by deploying and calling an API proxy. 



## Step 1: Define environment variables

Set up `gcloud` and define environment variables for use in later steps:

  1. Be sure you have completed the requirements listed in [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites).
  2. You must have the gcloud CLI installed. If you need to install it, see [Installing the gcloud CLI](https://cloud.google.com/sdk/docs/install).
  3. Initialize the gcloud CLI, as described in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize), or if the CLI is already initialized, ensure that the Google Cloud project you created in [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites) is the default project for gcloud. 
  4. Define the following environment variables: 
         
         AUTH="Authorization: Bearer $(gcloud auth print-access-token)"
         PROJECT_ID="YOUR_PROJECT_ID"
         RUNTIME_LOCATION="YOUR_RUNTIME_LOCATION"
         ANALYTICS_REGION="YOUR_ANALYTICS_REGION"

Where:

     * AUTH defines the `Authentication` header with a bearer token. You will use this header when calling Apigee APIs. Note that the token expires after a period of time and when it does, you can simply regenerate it using the same command. For more information, see the reference page for the [print-access-token command](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
     * PROJECT_ID is the Cloud [project ID](https://support.google.com/googleapi/answer/7014113) that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites).
     * RUNTIME_LOCATION is the physical location where the Apigee instance is located. For a list of available runtime locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

**Note:** For `**RUNTIME_LOCATION**`, be sure to use a _**region**_ name and not a zone name. For example, `us-west1` is a region name, while `us-west1-a` is a zone in the region. See also [Identifying a region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone).
     * ANALYTICS_REGION is the physical location at which Apigee analytics data will be stored. For a list of available Apigee API Analytics regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

Both RUNTIME_LOCATION and ANALYTICS_REGION can be the same region, but they do not have to be the same. However, there may be a performance benefit if they are the same.

  5. (Optional) Check your work by echoing the values you just set. Note that when you want to use a variable in your commands, precede the variable's name with a dollar sign (**$**). 
         
         echo $AUTH
         echo $PROJECT_ID
         echo $RUNTIME_LOCATION
         echo $ANALYTICS_REGION
         

The responses to your `echo` commands should look something like the following:
         
         Authorization: Bearer ya29.a123456678940B63hPSAMPLEsampleKKYVsample0f3pWDWZDuH2-hENkNa
         TvgZ1PD977TMvv6edBQPJezdHw040880Ol_LoD5ZDkt-i-knizia_KhA9L20sSvztL81-SAMPLE42ELPMASk2_
         1CxN
         my-cloud-project
         us-west1
         us-west1
         




## Step 2: Enable APIs

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [API enablement permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#api-enablement-permissions). 

  1. Apigee requires you to enable several Google Cloud APIs. Enable them by executing the [`services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command:
         
         gcloud services enable apigee.googleapis.com \
           servicenetworking.googleapis.com compute.googleapis.com \
           cloudkms.googleapis.com --project=$PROJECT_ID

  2. (Optional) To check your work, use the [`services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command to show all the enabled APIs:
         
         gcloud services list

The response shows all enabled services, including the APIs that you just enabled (Apigee, Service Networking, Cloud KMS, and Compute Engine). 




## Step 3: Configure service networking

**Important:** If you already have a peering range and private connection with `servicenetworking.googleapis.com`, and your range is big enough to handle another `/22` and `/28` CIDR range, you can skip this step. Apigee will create the needed CIDR blocks for you. This step is only required if you do not already have a space created that has room to create a `/22` and `/28` block, or if you want to use a specific `/22` and `/28` that is currently not present.

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Service networking permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#service-networking-permissions).

  1. Create these environment variables: 
         
         **RANGE_NAME** =YOUR_RANGE_NAME
         **NETWORK_NAME** =YOUR_NETWORK_NAME
         

Where:

     * **`RANGE_NAME`** is the name of the IP address range you are creating. You can name the range anything you want. For example: `google-svcs`
     * **`NETWORK_NAME`** is the name of the network resource in which the addresses should be reserved. Google creates a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) (named `default`) for each new project, so you can use that. However, Google does not recommend using the default network for anything other than testing. **Note:** If you have a different Cloud network and want to use it, then enter its name. (Note that the network must have a /22 CIDR block of IP addresses free.)
  2. Create an IP range with a CIDR length of /22: 
         
         gcloud compute addresses create **$RANGE_NAME** \
           --global \
           --prefix-length=22 \
           --description="Peering range for Apigee services" \
           --network=**$NETWORK_NAME** \
           --purpose=VPC_PEERING \
           --addresses=OPTIONAL_ADDRESSES \
           --project=**$PROJECT_ID**

Where `--addresses` lets you optionally specify one or more address IPs for the prefix length of `/22`. For example, to allocate the CIDR block `192.168.0.0/22`, specify `192.168.0.0` for the address and `22` for the prefix length. See also [Creating an IP allocation](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#procedure).

If you do not provide the `--addresses` parameter, then gcloud selects an available address range for you. 

On success, `gcloud` responds with the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/global/addresses/google-svcs].

After you create a range of IP addresses, the addresses are associated with the project until you release them.

  3. Create a second IP range with a CIDR length of /28. This range is used by Apigee for troubleshooting purposes and cannot be customized or changed. 
         
         gcloud compute addresses create google-managed-services-support-1 \
           --global \
           --prefix-length=28 \
           --description="Peering range for supporting Apigee services" \
           --network=**$NETWORK_NAME** \
           --purpose=VPC_PEERING \
           --addresses=OPTIONAL_ADDRESSES \
           --project=**$PROJECT_ID**

Where `--addresses` lets you optionally specify one or more address IPs for the prefix length of `/28`. For example, to allocate the CIDR block `192.168.0.0/28`, specify `192.168.0.0` for the address and `28` for the prefix length. See also [Creating an IP allocation](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#procedure).

If you do not provide the `--addresses` parameter, then gcloud selects an available address range for you. 

  4. Connect your services to the network using the following command: 
         
         gcloud services vpc-peerings connect \
           --service=servicenetworking.googleapis.com \
           --network=**$NETWORK_NAME** \
           --ranges=**$RANGE_NAME** ,**google-managed-services-support-1** \
           --project=$PROJECT_ID

This operation can take several minutes to complete. On success, `gcloud` responds with the following:
         
         Operation "operations/OPERATION_ID" finished successfully.

Where OPERATION_ID is the UUID of the _LRO_ (long-running operation).

Apigee creates a connection between your network and Google's services; specifically, Apigee connects your project to the Service Networking API through VPC peering. Apigee also associates IP addresses with your project.




## Step 4: Create an organization

An organization is the top-level container in Apigee. It contains all your API proxies and related resources. For details, see [Understanding organizations](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure).

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See:

  * [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles)
  * [Provisioning wizard permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#provisioning-wizard-permissions)
  * [Organization creation permissions (paid org)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#organizationcreationpermissionspaid).



  1. Create a new eval org using the [gcloud alpha apigee organizations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision) command: 
         
         gcloud alpha apigee organizations provision \
           --runtime-location=**$RUNTIME_LOCATION** \
           --analytics-region=$ANALYTICS_REGION \
           --authorized-network=**$NETWORK_NAME** \
           --project=$PROJECT_ID

Where `--authorized-network` is the name of your custom peering network. For example: `default`.

  2. When you execute the `provision` command, Google starts an LRO to create the eval org. This operation takes up to 40 minutes to complete. During that time, `gcloud` displays the following:
         
         Provisioning organization...

**Note:** The `provision` command can create only _eval organizations_. It cannot be used to create production organizations.

When the eval org and its associated runtime instance are created, `gcloud` responds with the following message:
         
         Provisioning organization...done.

  3. If you execute the following command:
         
         gcloud alpha apigee operations list --organization=**$PROJECT_ID**

you should see that all UUIDs are in the `FINISHED` state. For example:
         
         UUID                                  ORGANIZATION  STATE
         00bab06f-c60c-41a5-4242-7SAMPLE7f     my-org        FINISHED
         429790a7-3151-4642-4343-7SAMPLE7f     my-org        FINISHED
         d00a92a9-9b83-4642-4343-7SAMPLE7f     my-org        FINISHED
         f48a00ff-7daa-4c4a-4444-7SAMPLE7f     my-org        FINISHED




## Step 5: Configure routing

Decide whether to allow external access or internal only access:

Access type | Description of the configuration and deployment process  
---|---  
Internal |  Allow only internal access to your API proxies. You must create a new VM inside the network and connect to it. From the new VM, you can send a request to an Apigee API proxy.  
External |  Allow external access to your API proxies. Use [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) to enable private connection between a service producer (Apigee) and a service consumer (the peered VPC project and/or one or more other Cloud projects that you control). With this method, requests pass through a global external load balancer to a single point of attachment, called a [Service Attachment](https://cloud.google.com/vpc/docs/private-service-connect#service-attachments). This configuration lets you send Apigee API proxy requests from any network-enabled machine.  
  
Each of these routing approaches is presented on a tab in the instructions below.

### Internal routing

There are no tasks to perform for this step if you are using the command line to set up an API proxy for _internal_ access only. You can skip to Step 6: Call the sample API proxy, where you will send a request to your API proxy.

#### External routing

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section describes how to configure external routing using [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) to allow communication between Apigee and VPCs that you control. You must do this before you can send a request from an external client to your Apigee runtime instance. 

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

The external configuration steps are:

Step 5a: Create a network endpoint group (NEG)  
Step 5b: Configure the load balancer  


Each of these steps is described in the sections that follow.

#### Step 5a: Create a network endpoint group (NEG)

  1. Get the [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect?_gl=1*c4k3na*_ga*NDMwNTU0NDIyLjE2NjIwNzQzNzQ.*_ga_WH2QY8WWF5*MTY2MjE0NDAyMi42LjEuMTY2MjE0OTcxNC4wLjAuMA..#service-attachments) for your Apigee [instance](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts#instance): 
         
         curl -i -X GET -H "**$AUTH** " \
           "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
           "instances": [
             {
               "name": "eval-instance",
               "location": "us-west1",
               "host": "10.72.100.2",
               "port": "443",
               "createdAt": "1657832463500",
               "lastModifiedAt": "1657833920670",
               "state": "ACTIVE",
               "peeringCidrRange": "SLASH_22",
               "runtimeVersion": "1-8-0-apigee-18",
               "ipRange": "10.74.100.0/28,10.74.100.16/28",
               "consumerAcceptList": [
                 "apigee-eval-test"
               ],
               "serviceAttachment": "**projects/s8da1b0111eb33765-tp/regions/us-west1/serviceAttachments/apigee-us-west1-icza** "
             }
           ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  2. Create a Private Service Connect network endpoint group (NEG) that points to the service attachment that you obtained from the instance response body in the previous step. 
         
         gcloud compute network-endpoint-groups create NEG_NAME \
           --network-endpoint-type=private-service-connect \
           --psc-target-service=TARGET_SERVICE \
           --region=**$RUNTIME_LOCATION** \
           --network=**$NETWORK_NAME** \
           --subnet=SUBNET_NAME \
           --project=**$PROJECT_ID**
         

Replace the following:

     * NEG_NAME: a name for the network endpoint group.
     * TARGET_SERVICE: the service attachment that you want to connect to. For example: `projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7`
     * SUBNET_NAME: Name of the subnet used for private connectivity to the producer. The subnet size can be small: the Private Service Connect NEG only needs one IP from the subnet. For Apigee, only one Private Service Connect NEG is needed per region. The subnet can be shared and used by VMs or other entities. If a subnet is not specified, network endpoints may belong to any subnetwork in the region where the network endpoint group is created. **NOTE:** If you specify the `--network` parameter,you must also specify `--subnet`.



#### Step 5b: Configure the load balancer

Configure a [global external HTTP(S) load balancer](https://cloud.google.com/load-balancing/docs/https) (load balancing scheme set to `EXTERNAL_MANAGED`).

Although the Private Service Connect NEG is regional, all other load balancing components in this configuration are global.

  1. Reserve a global external IPv4 address for the load balancer. 
         
         gcloud compute addresses create ADDRESS_NAME \
           --ip-version=IPV4 --global --project=**$PROJECT_ID**

Replace ADDRESS_NAME with a name for the IP address resource. 

Run this command to view the reserved IP address: 
         
         gcloud compute addresses describe ADDRESS_NAME \
           --format="get(address)" --global --project=**$PROJECT_ID**

  2. Create a backend service for the NEG. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --protocol=HTTPS \
           --global --project=**$PROJECT_ID**

Replace BACKEND_SERVICE_NAME with the name of the backend service. 

  3. Add the NEG to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --network-endpoint-group=NEG_NAME \
           --network-endpoint-group-region=**$RUNTIME_LOCATION** \
           --global --project=**$PROJECT_ID**

Replace the following:

     * BACKEND_SERVICE_NAME: the name of the backend service.
     * NEG_NAME: the name of the network endpoint group.
  4. Create a URL map for the load balancer.

A URL map must reference a default backend service. Set the backend service you just created as the default.
         
         gcloud compute url-maps create URL_MAP_NAME \
           --default-service=DEFAULT_BACKEND_SERVICE_NAME \
           --global --project=**$PROJECT_ID**

Replace the following:

     * URL_MAP_NAME: a name for the URL map.
     * DEFAULT_BACKEND_SERVICE_NAME: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  5. Create an SSL certificate for the HTTPS target proxy.

To create an HTTPS load balancer, you must have an [SSL certificate resource](https://cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. You can create an SSL certificate resource using either a [Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) or a [self-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs). 

**Note:** To create a Google-managed certificate, you must have a registered domain.

Use this command to create a Google-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create CERTIFICATE \
           --domains DOMAIN --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * DOMAIN: the domain name you will use for the external load balancer.

To create a self-managed SSL certificate, you need a local private key file and a local certificate file. If you need to create these files, see [Using self-managed SSL certificates](https://cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).
    
    gcloud compute ssl-certificates create CERTIFICATE \
      --certificate LB_CERT \
      --private-key LB_PRIVATE_KEY --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * LB_CERT: the path to the PEM-formatted certificate file for your self-managed certificate.
     * LB_PRIVATE_KEY: the path to the PEM-formatted private key file for your self-managed certificate.
  6. The certificate can take up to an hour to be provisioned. To check the status of the provisioning, execute this command:
         
         gcloud compute ssl-certificates describe CERTIFICATE \
            --global \
            --format="get(name,managed.status, managed.Status)"

  7. Add the domain to the Apigee environment group that was created for you. The name of the environment group is `eval-group`: 
         
         curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/envgroups/eval-group" \
           -H "$AUTH" \
           -X PATCH \
           -H "Content-Type:application/json" \
           -d '{
             "hostnames":["'"DOMAIN"'"]
           }'

  8. Check the status of the environment group operation: 
         
         curl -H "$AUTH" \
           "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/envgroups/eval-group/attachments"
         

  9. Use the SSL certificate resource to create a target HTTPS proxy.
         
         gcloud compute target-https-proxies create PROXY_NAME \
           --url-map=URL_MAP_NAME \
           --ssl-certificates=CERTIFICATE --project=**$PROJECT_ID**

Replace the following:

     * PROXY_NAME: a name for the target HTTPS proxy.
     * URL_MAP_NAME: the name of the URL map.
     * CERTIFICATE: the name of the certificate resource.
  10. Create the forwarding rule. 
         
         gcloud compute forwarding-rules create FWD_RULE \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network-tier=PREMIUM \
           --address=ADDRESS_NAME \
           --target-https-proxy=PROXY_NAME \
           --ports=443 \
           --global --project=**$PROJECT_ID**

Replace the following:

     * FWD_RULE: a name for the forwarding rule.
     * ADDRESS_NAME: the IP address resource that you reserved to use for the forwarding rule.
     * PROXY_NAME: the name of the target HTTPS proxy.



Apigee provisioning is complete. 

## Step 6: Call the sample API proxy

An API proxy called `hello-world` was created and deployed for you during provisioning. In this step, you will test the new eval organization by calling the proxy.

#### Permissions required for this task

Creating and deploying proxies requires a minimum set of permissions. If you have Apigee Org Admin role, you can complete this task. To learn about other roles you can employ, see [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles). 

###  Call the proxy with internal routing 

If you chose the internal routing option in Step 5, follow the steps in [Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies).

###  Call the proxy with external routing 

If you chose the external routing option in Step 5, follow the steps in this section. 

  1. Set up a DNS entry for your domain. Here are two ways to accomplish this task: 
     * At your registrar, create an A record pointing to your domain. For example, if your domain is `sales.example.com` and the IP is 10.23.0.2, then point the record for `sales.example.com` to the address `10.23.0.2`. 

Run this command to view the reserved IP address:
           
           gcloud compute addresses describe ADDRESS_NAME \
             --format="get(address)" --global --project=**$PROJECT_ID**

     * Use Google [Cloud DNS](https://docs.cloud.google.com/dns/docs) to map a URL to an IP address.
  2. Confirm that the `hello-world` proxy is deployed: 
         
         curl -i -H "**$AUTH** " \
           "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/eval/apis/hello-world/revisions/1/deployments"

  3. Call the API proxy: 

Send a request to the API proxy from any network-enabled machine by executing the following command:
         
         curl -i -H "Host: DOMAIN" \
           https://DOMAIN/hello-world

Where DOMAIN is the domain you put into the certificate and added to the environment group, as discussed in [Step 5: Configure routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval#configure-routing). If needed, you can use this API to get the `DOMAIN` value from the environment group: 
         
         curl -i -H "**$AUTH** " \
           "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /envgroups"

Upon success, the sample API proxy returns the response: 
         
         Hello, Guest!

**Troubleshooting tips:**

If you get a handshake error, check the status of the SSL certificate. For information on troubleshooting self-managed and Google-managed certificates, see [Troubleshoot SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting). 

Be sure that your registered domain has an A record that points to the IP address of global external IPv4 address created in Step 5. Run this command to view the reserved IP address:
         
         gcloud compute addresses describe ADDRESS_NAME \
           --format="get(address)" --global --project=**$PROJECT_ID**

If you're unable to resolve the domain configuration, try calling the proxy with this command: 
         
         curl  -H Host:DOMAIN --resolve \
           DOMAIN:443:EXTERNAL_IP_ADDRESS  \
           https://DOMAIN:443/hello-world -k

**Note:** DNS changes are published immediately, but may take time to propagate. Because of this delay, you may have to wait up to an hour before you can call the sample proxy.



**Next:** To learn more about building and deploying API proxies, see [ Build your first API proxy overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[CIDR]: Classless Inter-Domain Routing
  *[VPC]: Virtual Private Cloud
  *[LRO]: Long-Running Operation
