---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval/
title: Provision an eval org without VPC peering \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:44.778962+00:00
---

# Provision an eval org without VPC peering  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision an eval org without VPC peering Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document explains how to install and configure an Apigee evaluation organization from the command line [without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options). Eval orgs expire after 60 days and may have other limitations. See also [ Comparing eval and paid organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro#comparing). **Important** : These steps are for the non-VPC peering setup. If you want to use the VPC peering setup, see [Provisioning an eval org from the command line with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval). If you are unsure which to use, see [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

## Limitations

The non-VPC peering installation option described in this document has some limitations: 

  * [ VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) are not supported.



For a complete list of features and networking approaches that are and are not supported for non-VPC peering, see [How to choose a networking option](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options#how-to-choose-a-networking-option). 

## Summary of steps

The provisioning steps are as follows:

  * Step 1: Define environment variables: Set up `gcloud` and define environment variables. The Google Cloud CLI manages authentication, local configuration, developer workflow, and interactions with the Google Cloud APIs. 
  * Step 2: Enable APIs: Apigee requires you to enable several Google Cloud APIs. 
  * Step 3: Create an organization: An Apigee organization (sometimes referred to as an org) is the top-level container in Apigee. It includes all of your environments and environment groups, users, API proxies, and related resources. 
  * Step 4: Configure routing: Allow external access or internal only access to your API. 
  * Step 5: Call the sample API proxy: Test the provisioning by deploying and calling an API proxy. 



## Step 1: Define environment variables

Set up `gcloud` and define environment variables for use in later steps:

  1. Be sure you have completed the requirements listed in [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites).
  2. You must have the gcloud CLI installed. If you need to install it, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  3. Initialize the gcloud CLI, as described in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize), or if the CLI is already initialized, ensure that the Google Cloud project you created in [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites) is the default project for gcloud. 
  4. Define the following environment variables: 
         
         AUTH="Authorization: Bearer $(gcloud auth print-access-token)"
         PROJECT_ID="YOUR_PROJECT_ID"
         RUNTIME_LOCATION="YOUR_RUNTIME_LOCATION"
         ANALYTICS_REGION="YOUR_ANALYTICS_REGION"

Where:

     * AUTH defines the `Authentication` header with a bearer token. You will use this header when calling Apigee APIs. Note that the token expires after a period of time and when it does, you can simply regenerate it using the same command. For more information, see the reference page for the [print-access-token command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
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
           cloudkms.googleapis.com --project=$PROJECT_ID

  2. (Optional) To check your work, use the [`services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command to show all the enabled APIs:
         
         gcloud services list

The response shows all enabled services, including the APIs that you just enabled (Apigee, Cloud KMS, and Compute Engine). 




## Step 3: Create an organization

An organization is the top-level container in Apigee. It contains all your API proxies and related resources. For details, see [Understanding organizations](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure).

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See:

  * [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles)
  * [Provisioning wizard permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#provisioning-wizard-permissions)
  * [Organization creation permissions (paid org)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#organizationcreationpermissionspaid).



  1. Create a new eval org with the [provisionOrganization API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/projects/provisionOrganization): **Note:** The `provisionOrganization` API can create only _eval organizations_. It cannot be used to create production organizations.
         
         curl "https://apigee.googleapis.com/v1/projects/**$PROJECT_ID** :provisionOrganization"  \
           -H "**$AUTH** " \
           -X POST \
           -H "Content-Type:application/json" \
           -d '{
             "analyticsRegion":"'"**$ANALYTICS_REGION** "'",
             "runtimeLocation":"'"**$RUNTIME_LOCATION** "'",
             **"disableVpcPeering":"true"** ,
           }'

Where:

     * `-d` defines the data payload for the request. This payload must include the following: 
       * `ANALYTICS_REGION`: Specifies the physical location where your analytics data will be stored.

       * `RUNTIME_LOCATION`: is the physical location where the Apigee instance is located. 

       * `disableVpcPeering`: In this provisioning flow, we are not using VPC peering, so this flag must be set to `true`. Default: `false`
  2. Apigee starts an LRO to create the eval org. This operation takes up to 40 minutes to complete.

  3. To check the status of your creation request, you can send a `GET` request to the Apigee [List organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/list), as the following example shows: 
         
         curl -H "**$AUTH** " "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** "

If you see this response, then the organization creation has not completed yet: 
         
         {
           "error": {
             "code": 403,
             "message": "Permission denied on resource \"organizations/apigee-docs-m\" (or it may not exist)",
             "status": "PERMISSION_DENIED"
           }
         }

On success, the response object will indicate `"state": "ACTIVE"`, and you can go on to the next step.




## Step 4: Configure routing

In this step, you configure how client applications communicate with Apigee. Client to Apigee traffic is also called "northbound" traffic. Northbound configuration options include the following:

Access type | Description of the configuration and deployment process  
---|---  
Internal with Private Service Connect |  Allow only internal access to your API proxies from any of your Google Cloud projects using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Private Service Connect enables private connection between a service producer (Apigee) and a service consumer (the peered VPC project and/or one or more other Cloud projects that you control). With this method, requests pass through either a service endpoint or a regional internal load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments). This configuration lets your internal clients send Apigee API proxy requests from any network-enabled machine.  
External with Private Service Connect |  Allow external access to your API proxies using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to enable private connection between a service producer (Apigee) and a service consumer (the peered VPC project and/or one or more other Cloud projects that you control). With this method, requests pass through either a global external load balancer or a regional external load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments). This configuration lets you send Apigee API proxy requests from any network-enabled machine.  
  
Each of these routing approaches is presented on a tab in the instructions below.

### Internal routing (Private Service Connect)

This section explains how to allow only internal access to your API proxies from any of your Google Cloud projects using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

You have to options for configuring internal access with Private Service Connect:

  * **Service endpoint** : Requests pass through a service endpoint to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments).
  * **Internal regional load balancer** : Requests pass through a regional internal HTTP(S) load balancer. See also [Global vs regional load balancing](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#global-regional). 



Select the tab below for your configuration choice and follow the steps:

### Service endpoint

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

#### Create a Private Service Connect service endpoint for the service attachment

  1. Get the service attachment from the Apigee instance: 
         
         curl -i -X GET -H "**$AUTH** " \
           "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
           "instances": [
             {
               "name": "us-west1",
               "location": "us-west1",
               "createdAt": "1645731488019",
               "lastModifiedAt": "1646504754219",
               "diskEncryptionKeyName": "projects/my-project/locations/us-west1/keyRings/us-west1/cryptoKeys/dek",
               "state": "ACTIVE",
               "runtimeVersion": "1-7-0-20220228-190814",
               "consumerAcceptList": [
                 "my-project"
               ],
               "serviceAttachment": "**projects/bfac74a67a320c43a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw1** "
             }
           ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  2. Create a Private Service Connect Service Endpoint that points to the service attachment that you obtained from the instance response body in the previous step, as explained in [Create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint). 
  3. Note and remember the service endpoint IP address. You will need the IP address later when you test the setup by calling an API proxy. (For example: `10.138.0.2`) 



Apigee provisioning is complete. Go to Deploy a sample proxy. 

#### Internal regional LB

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

**Restrictions:** Note the following restrictions for Private Service Connect configuration: 

  * [Global external HTTP(S) load balancer (classic)](https://docs.cloud.google.com/load-balancing/docs/https) is not supported for this configuration.
  * Limits apply to the number of Google Cloud projects that can connect to an Apigee instance through Private Service Connect, and to the number of Private Service Connect NEG connections that you can have per project. For details, see [ Private Service Connect Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#private-service-connect-psc).
  * If a Google cloud project is removed from `consumerAcceptList`, the existing Private Service Connect NEGs in that removed project will continue to work. However, any new NEGs will be rejected. You must delete existing NEGs if you remove their associated projects from the `consumerAcceptList`. Alternatively, you can recreate the Apigee instance, which recreates the service attachment in the Apigee project.



#### Step 8a: Set up environment variables

The instructions in this section use environment variables to refer to repeatedly used strings. Be sure you have set the variables in [Define environment variables](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#define-variables).

In addition, set the following environment variables:

* Define the following environment variables in your command terminal: **Tip:** Save your environment variables in a text file so that you can easily restore them if needed.
    
    
    NEG_NAME=YOUR_NEG_NAME"
    TARGET_SERVICE=YOUR_TARGET_SERVICE"
    NETWORK_NAME=YOUR_NETWORK_NAME"
    SUBNET_NAME=YOUR_SUBNET_NAME"

Where:

  * NEG_NAME: a name for the network endpoint group.
  * TARGET_SERVICE: the service attachment that you want to connect to. For example: `projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7`
  * NETWORK_NAME: (Optional) Name of the network in which the NEG is created. If you omit this parameter, the `default` project network is used.
  * SUBNET_NAME: Name of the subnet used for private connectivity to the producer. The subnet size can be small: the Private Service Connect NEG only needs one IP from the subnet. For Apigee, only one Private Service Connect NEG is needed per region. The subnet can be shared and used by VMs or other entities. If a subnet is not specified, network endpoints may belong to any subnetwork in the region where the network endpoint group is created. **NOTE:** If you specify the `--network` parameter,you must also specify `--subnet`.



#### Step 8b: Create a proxy-only subnet

**Note:** This is a one-time only operation. This proxy-only subnet is required only once for any Envoy-based regional load balancer. See also [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
    
    
    gcloud compute networks subnets create testproxyonlysubnet \
      --purpose=REGIONAL_MANAGED_PROXY --role=ACTIVE --region=**$RUNTIME_REGION** --network=**$NETWORK_NAME** \
      --range=100.0.0.0/24 --project=**$PROJECT_ID**

#### Step 8c: Create a network endpoint group (NEG)

  1. Get the service attachment from the instance you created previously: 
         
         curl -i -X GET -H "**$AUTH** " \
         "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
         "instances": [
           {
             "name": "us-west1",
             "location": "us-west1",
             "createdAt": "1645731488019",
             "lastModifiedAt": "1646504754219",
             "diskEncryptionKeyName": "projects/my-project/locations/us-west1/keyRings/us-west1/cryptoKeys/dek",
             "state": "ACTIVE",
             "runtimeVersion": "1-7-0-20220228-190814",
             "consumerAcceptList": [
               "my-project"
             ],
             "serviceAttachment": "**projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7** "
           }
         ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  2. Create a Private Service Connect NEG that points to the service attachment that you obtained from the instance response body in the previous step. 
         
         gcloud compute network-endpoint-groups create **$ NEG_NAME** \
         --network-endpoint-type=private-service-connect \
         --psc-target-service=**$ TARGET_SERVICE** \
         --region=**$ RUNTIME_LOCATION** \
         --project=**$ PROJECT_ID**




#### Step 8d: Configure the regional internal load balancer

  1. Reserve an internal IPv4 address for the load balancer. 
         
         gcloud compute addresses create ADDRESS_NAME \
         --ip-version=IPV4 --subnet=**$ SUBNET_NAME** \
           --region=**$ RUNTIME_LOCATION** --project=**$ PROJECT_ID**

Replace ADDRESS_NAME with a name for the IP address resource. 

Run this command to view the reserved IP address: 
         
         gcloud compute addresses describe ADDRESS_NAME \
         --format="get(address)" --region=**RUNTIME_LOCATION** --project=**$ PROJECT_ID**

  2. Create a backend service for the NEG. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
         --load-balancing-scheme=INTERNAL_MANAGED \
         --protocol=HTTPS \
         --region=**$** RUNTIME_REGION \
         --project=**$** PROJECT_ID

Replace BACKEND_SERVICE_NAME with the name of the backend service. 

  3. Add the NEG to the backend service. 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
         --network-endpoint-group=NEG_NAME \
         --region=**$RUNTIME_LOCATION** \
         --project=**$PROJECT_ID**

Replace the following:

     * BACKEND_SERVICE_NAME: the name of the backend service.
     * NEG_NAME: the name of the network endpoint group.
  4. You must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. 

Use this command to create a self-managed SSL certificate resource. To create a self-managed SSL certificate, you need a local private key file and a local certificate file. If you need to create these files, see [step 1 of using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).

**Note:** Google-managed certificates are not supported by the internal regional load balancer.
         
         gcloud compute ssl-certificates create CERTIFICATE \
         --certificate LB_CERT \
         --private-key LB_PRIVATE_KEY
         --region=**RUNTIME_LOCATION** --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * LB_CERT: the path to the PEM-formatted certificate file for your self-managed certificate.
     * LB_PRIVATE_KEY: the path to the PEM-formatted private key file for your self-managed certificate.
  5. Create a URL map for the load balancer.

A URL map must reference a default backend service. Set the backend service you just created as the default.
         
         gcloud compute url-maps create URL_MAP_NAME \
             --default-service=DEFAULT_BACKEND_SERVICE_NAME \
             --global --project=**$** PROJECT_ID

Replace the following:

     * URL_MAP_NAME: a name for the URL map.
     * DEFAULT_BACKEND_SERVICE_NAME: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  6. Use the SSL certificate resource to create a target HTTPS proxy.
         
         gcloud compute target-https-proxies create PROXY_NAME \
         --url-map=URL_MAP_NAME \
         --ssl-certificates=CERTIFICATE \
         --region=**$RUNTIME_LOCATION** --project=**$PROJECT_ID**

Replace the following:

     * PROXY_NAME: a name for the target HTTPS proxy.
     * URL_MAP_NAME: the name of the URL map.
     * CERTIFICATE: the name of the certificate resource.
  7. Create the forwarding rule. 
         
         gcloud compute forwarding-rules create FWD_RULE \
         --load-balancing-scheme=INTERNAL_MANAGED \
         --address=ADDRESS_NAME \
         --target-https-proxy=PROXY_NAME \
         --ports=443 \
         --target-https-proxy-region=$RUNTIME_REGION \
         --region=$RUNTIME_REGION
         --project=**$** PROJECT_ID

Replace the following:

     * FWD_RULE: a name for the forwarding rule.
     * ADDRESS_NAME: the IP address resource that you reserved to use for the forwarding rule.
     * PROXY_NAME: the name of the target HTTPS proxy.



Apigee provisioning is complete. Go to Deploy a sample proxy. 

### External routing (Private Service Connect)

This section describes how to configure external routing using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to allow communication between Apigee and VPCs that you control. You must do this before you can send a request from an external client to your Apigee runtime instance. 

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

**Restrictions:** Note the following restrictions for Private Service Connect configuration: 

  * [Global external HTTP(S) load balancer (classic)](https://docs.cloud.google.com/load-balancing/docs/https) is not supported for this configuration.
  * Limits apply to the number of Google Cloud projects that can connect to an Apigee instance through Private Service Connect, and to the number of Private Service Connect NEG connections that you can have per project. For details, see [ Private Service Connect Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#private-service-connect-psc).
  * If a Google cloud project is removed from `consumerAcceptList`, the existing Private Service Connect NEGs in that removed project will continue to work. However, any new NEGs will be rejected. You must delete existing NEGs if you remove their associated projects from the `consumerAcceptList`. Alternatively, you can recreate the Apigee instance, which recreates the service attachment in the Apigee project.



#### Step 8b: Create a NEG and configure the load balancer

You can create a global or regional load balancer.

### Global external LB

Configure a [global external HTTP(S) load balancer](https://docs.cloud.google.com/load-balancing/docs/https) (load balancing scheme set to `EXTERNAL_MANAGED`).

Although the Private Service Connect NEG is regional, all other load balancing components in this configuration are global.

  1. Make sure you have set the environment variables in Define environment variables. 
  2. Get the service attachment from the instance you created previously: 
         
         curl -i -X GET -H "**$AUTH** " \
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
                   "serviceAttachment": "**projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7** "
                 }
               ]
             }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  3. Create a Private Service Connect NEG that points to the service attachment that you obtained from the instance response body in the previous step. 
         
         gcloud compute network-endpoint-groups create **$ NEG_NAME** \
               --network-endpoint-type=private-service-connect \
               --psc-target-service=**$ TARGET_SERVICE** \
               --region=**$ RUNTIME_LOCATION** \
               --network=NETWORK_NAME \
               --subnet=SUBNET_NAME \
               --project=**$ PROJECT_ID**
             

Replace the following:

     * NETWORK_NAME: (Optional) Name of the network in which the NEG is created. If you omit this parameter, the `default` project network is used.
     * SUBNET_NAME: Name of the subnet used for private connectivity to the producer. The subnet size can be small: the Private Service Connect NEG only needs one IP from the subnet. For Apigee, only one Private Service Connect NEG is needed per region. The subnet can be shared and used by VMs or other entities. If a subnet is not specified, network endpoints may belong to any subnetwork in the region where the network endpoint group is created. **NOTE:** If you specify the `--network` parameter,you must also specify `--subnet`.
     * PROJECT_ID The Cloud project that is already associated with your Apigee organization, or a Cloud project included in the `consumerAcceptlist` when the Apigee runtime instance was created. 
  4. Reserve a global external IPv4 address for the load balancer. 
         
         gcloud compute addresses create ADDRESS_NAME \
           --ip-version=IPV4 --global --project=**$ PROJECT_ID**

Replace ADDRESS_NAME with a name for the IP address resource. 

Run this command to view the reserved IP address: 
         
         gcloud compute addresses describe ADDRESS_NAME \
           --format="get(address)" --global --project=**$ PROJECT_ID**

  5. Create a backend service for the NEG. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --protocol=HTTPS \
           --global --project=**$** PROJECT_ID

Replace BACKEND_SERVICE_NAME with the name of the backend service. 

  6. Add the backend service to the NEG. 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --network-endpoint-group=NEG_NAME \
           --network-endpoint-group-region=**$REGION** \
           --global --project=**$PROJECT_ID**

Replace the following:

     * BACKEND_SERVICE_NAME: the name of the backend service.
     * NEG_NAME: the name of the network endpoint group.
     * REGION: the region of the network endpoint group.
  7. Create a URL map for the load balancer.

A URL map must reference a default backend service. Set the backend service you just created as the default.
         
         gcloud compute url-maps create URL_MAP_NAME \
           --default-service=DEFAULT_BACKEND_SERVICE_NAME \
           --global --project=**$** PROJECT_ID

Replace the following:

     * URL_MAP_NAME: a name for the URL map.
     * DEFAULT_BACKEND_SERVICE_NAME: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  8. Create the target HTTPS proxy.

You must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. You can create an SSL certificate resource using either a Google-managed SSL certificate or a self-managed SSL certificate. Using Google-managed certificates is recommended because Google Cloud obtains, manages, and renews these certificates automatically. 

To create a Google-managed certificate, [you must have a domain](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#before_you_begin). 

Use this command to create a Google-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create CERTIFICATE \
           --domains DOMAIN --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * DOMAIN: the domain name of your load balancer.

Use this command to create a self-managed SSL certificate resource. To create a self-managed SSL certificate, you need a local private key file and a local certificate file. If you need to create these files, see [step 1 of using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).
    
    gcloud compute ssl-certificates create CERTIFICATE \
      --certificate LB_CERT \
      --private-key LB_PRIVATE_KEY --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * LB_CERT: the path to the PEM-formatted certificate file for your self-managed certificate.
     * LB_PRIVATE_KEY: the path to the PEM-formatted private key file for your self-managed certificate.

Use the SSL certificate resource to create a target HTTPS proxy.
    
    gcloud compute target-https-proxies create PROXY_NAME \
      --url-map=URL_MAP_NAME \
      --ssl-certificates=CERTIFICATE --project=**$PROJECT_ID**

Replace the following:

     * PROXY_NAME: a name for the target HTTPS proxy.
     * URL_MAP_NAME: the name of the URL map.
     * CERTIFICATE: the name of the certificate resource.
  9. Create the forwarding rule. 
         
         gcloud compute forwarding-rules create FWD_RULE \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network-tier=PREMIUM \
           --address=ADDRESS_NAME \
           --target-https-proxy=PROXY_NAME \
           --ports=443 \
           --global --project=**$** PROJECT_ID

Replace the following:

     * FWD_RULE: a name for the forwarding rule.
     * ADDRESS_NAME: the IP address resource that you reserved to use for the forwarding rule.
     * PROXY_NAME: the name of the target HTTPS proxy.



Apigee provisioning is complete. Go to Deploy a sample proxy. 

### Regional external LB

Configure a regional external HTTP(S) load balancer. See also [External HTTP(S) load balancer overview](https://docs.cloud.google.com/load-balancing/docs/https).

  1. Be sure you have set the variables in [Define environment variables](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#define-variables).
  2. Create a proxy-only subnet: **Note:** This is a one-time only operation. This proxy-only subnet is required only once per Google Cloud project for any Envoy-based regional load balancer. See also [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets). 
         
         gcloud compute networks subnets create SUBNET_NAME \
           --purpose=REGIONAL_MANAGED_PROXY --role=ACTIVE \
           --region=**$RUNTIME_LOCATION** --network=NETWORK_NAME \
           --range=100.0.0.0/24 --project=**$PROJECT_ID**

     * Replace SUBNET_NAME with the name of the subnet. 
     * (Optional) Replace NETWORK_NAME Name of the network in which the subnet is created. If you omit this parameter, the default project network is used. 
  3. Get the service attachment from the instance you created previously: 
         
         curl -i -X GET -H "**$AUTH** " \
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
                     "serviceAttachment": "**projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7** "
                   }
                 ]
               }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  4. Create a network endpoint group. 
         
         gcloud compute network-endpoint-groups create NEG_NAME \
                 --network-endpoint-type=private-service-connect \
                 --psc-target-service=TARGET_SERVICE \
                 --region=**$ RUNTIME_LOCATION** --project=**$ PROJECT_ID**

Replace the following:

     * NEG_NAME: the name of the network endpoint group.
     * TARGET_SERVICE: the name of the service attachment that you want to connect to. For example: `projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7`
  5. Create a backend service for the NEG. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --protocol=HTTPS \
           --region=**$** RUNTIME_LOCATION  \
           --project=**$** PROJECT_ID

Replace BACKEND_SERVICE_NAME with the name of the backend service. 

  6. Add the backend service to the NEG. 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --network-endpoint-group=NEG_NAME \
           --region=**$RUNTIME_LOCATION**  \
           --project=**$PROJECT_ID**

Replace the following:

     * BACKEND_SERVICE_NAME: the name of the backend service.
     * NEG_NAME: the name of the network endpoint group.
  7. Create a URL map for the load balancer.

A URL map must reference a default backend service. Set the backend service you just created as the default.
         
         gcloud compute url-maps create URL_MAP_NAME \
           --default-service=DEFAULT_BACKEND_SERVICE_NAME \
           --region=**$RUNTIME_LOCATION**  \
           --project=**$PROJECT_ID**

Replace the following:

     * URL_MAP_NAME: a name for the URL map.
     * DEFAULT_BACKEND_SERVICE_NAME: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  8. Create the target HTTPS proxy.

You must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. 

Use this command to create a self-managed SSL certificate resource. To create a self-managed SSL certificate, you need a local private key file and a local certificate file. If you need to create these files, see [step 1 of using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).

**Note:** Google-managed certificates are not supported by the external regional load balancer.
         
         gcloud compute ssl-certificates create CERTIFICATE \
           --certificate LB_CERT \
           --private-key LB_PRIVATE_KEY --region=**$RUNTIME_LOCATION** \
           --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * LB_CERT: the path to the PEM-formatted certificate file for your self-managed certificate.
     * LB_PRIVATE_KEY: the path to the PEM-formatted private key file for your self-managed certificate.
  9. Add the domain to the Apigee environment group that was created for you. The name of the environment group is `eval-group`: 
         
         curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/envgroups/eval-group" \
               -H "**$AUTH** " \
               -X PATCH \
               -H "Content-Type:application/json" \
               -d '{
                 "hostnames":["'"DOMAIN"'"]
               }'

  10. Check the status of the environment group operation: 
         
         curl -H "**$AUTH** " \
               "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /envgroups/eval-group/attachments"
             

  11. Use the SSL certificate resource to create a target HTTPS proxy.
         
         gcloud compute target-https-proxies create PROXY_NAME \
           --url-map=URL_MAP_NAME --region=**$RUNTIME_LOCATION** \
           --ssl-certificates=CERTIFICATE --project=**$PROJECT_ID**

Replace the following:

     * PROXY_NAME: a name for the target HTTPS proxy.
     * URL_MAP_NAME: the name of the URL map.
     * CERTIFICATE: the name of the certificate resource.
  12. Reserve a regional external address for the load balancer. Note that the network tier must be set to `STANDARD`. 
         
         gcloud compute addresses create ADDRESS_NAME \
               --region=**$ RUNTIME_LOCATION** --network-tier=STANDARD \
               --project=**$ PROJECT_ID**

Replace ADDRESS_NAME with a name for the IP address resource. 

Run this command to view the reserved IP address: 
         
         gcloud compute addresses describe ADDRESS_NAME \
               --format="get(address)" --region=**$ RUNTIME_LOCATION** \
               --project=**$ PROJECT_ID**

  13. Create the forwarding rule. 
         
         gcloud compute forwarding-rules create FWD_RULE \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network-tier=STANDARD \
           --address=ADDRESS_NAME \
           --target-https-proxy=PROXY_NAME \
           --ports=443  --region=**$** RUNTIME_LOCATION \
           --target-https-proxy-region=**$** RUNTIME_LOCATION --project=**$** PROJECT_ID

Replace the following:

     * FWD_RULE: a name for the forwarding rule.
     * ADDRESS_NAME: the IP address resource that you reserved to use for the forwarding rule.
     * PROXY_NAME: the name of the target HTTPS proxy.



Apigee provisioning is complete. Go to Call the sample API proxy. 

## Step 5: Call the sample API proxy

An API proxy called `hello-world` was created and deployed for you during provisioning. In this step, you will test the new eval organization by calling the proxy.

#### Permissions required for this task

Creating and deploying proxies requires a minimum set of permissions. If you have Apigee Org Admin role, you can complete this task. To learn about other roles you can employ, see [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles). 

###  Call the API proxy with internal routing 

If you chose an **internal routing** with a **service endpoint** option in Step 5, follow the steps in [Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies).

###  Call the API proxy with external routing 

If you chose an **external routing** option in Step 5, follow the steps in this section. 

  1. Set up a DNS entry for your domain. Here are two ways to accomplish this task: 
     * At your registrar, create an A record pointing to your domain. For example, if your domain is `sales.example.com` and the IP is 10.23.0.2, then point the record for `sales.example.com` to the address `10.23.0.2`. 

Run this command to view the reserved IP address:
           
           gcloud compute addresses describe ADDRESS_NAME \
               --format="get(address)" --region=**$ RUNTIME_LOCATION** \
               --project=**$ PROJECT_ID**

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
                       --format="get(address)" --region=**$ RUNTIME_LOCATION** \
                       --project=**$ PROJECT_ID**

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
  *[LRO]: Long-Running Operation
