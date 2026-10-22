---
url: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart/
title: Get started with the Apigee Extension Processor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:29.405659+00:00
---

# Get started with the Apigee Extension Processor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Get started with the Apigee Extension Processor Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to configure the Apigee Extension Processor to enable API policy enforcement for API traffic using a Service Extensions-enabled load balancer.

To learn more about the suggested use cases and benefits of using the Apigee Extension Processor for API management, see [Apigee Extension Processor overview](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview).

The Apigee Extension Processor is a traffic [ extension](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview) (a type of Service Extension) that lets you use Cloud Load Balancing to send callouts from the data processing path of the application load balancer to the Apigee Extension Processor. Once the load balancer and traffic extension are configured, API traffic is processed by the load balancer. The policies in the Apigee Extension Processor are applied to API traffic using the traffic extension callouts.

The following sections guide you through the steps to configure the key elements of the Apigee Extension Processor: 

  * Configure a load balancer for a backend service.
  * Configure the Apigee Extension Processor.
  * Configure the traffic extension.
  * Use policies with the Extension Processor.



## Before you begin

Before you begin setting up the Apigee Extension Processor, complete the following tasks: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Apigee, Compute Engine, and Network Services APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=apigee.googleapis.com,compute.googleapis.com,networkservices.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Apigee, Compute Engine, and Network Services APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=apigee.googleapis.com,compute.googleapis.com,networkservices.googleapis.com)

  8. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

After you install the Google Cloud CLI, run the `gcloud components update` command to get the latest gcloud components.

  9. Provision an [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) instance using version `1-15-0-apigee-2` or later, if you have not already done so. 

View instance versions in the **Instance details** page of the Apigee UI in Google Cloud console. Go to the **Instances** page in the Google Cloud console to select an instance and view its details: 

[Go to Instances](https://console.cloud.google.com/apigee/instances)

You can use Extension Processor with a [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) or [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-entitlements) Apigee organization. If you are unsure whether you are using a Subscription or Pay-as-you-go Apigee organization, contact your Apigee organization administrator. For more details about provisioning paid Apigee instances, see [Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview).

  10. Confirm that you have a [ VPC and subnet](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs#configuring-shared-vpc-with-apigee) enabled in the Apigee instance you plan to use. Go to the **VPC Networks** page in the Google Cloud console: 

[Go to VPC Networks](https://console.cloud.google.com/networking/networks/list)




### Required roles

To get the permissions that you need to install the Apigee Extension Processor, ask your administrator to grant you the following IAM roles: 

  * Create and manage service accounts: [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) on organization 
  * Create and manage service extensions: [Service Extensions Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkservices#networkservices.serviceExtensionsAdmin) (`roles/networkservices.serviceExtensionsAdmin`) on organization 
  * Create and manage network endpoint groups (NEGs): [Compute Instance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`) on organization 
  * Create and manage networking resources: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on organization 
  * Create and manage backend services: [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) on organization 
  * Create and manage Apigee resources: [Apigee Org Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`) on organization 
  * Create and manage traffic extensions: [Apigee APIM Service Extension Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apimServiceExtensionAdmin) (`roles/apigee.apimServiceExtensionAdmin`) on organization 
  * View traffic extensions: [Apigee APIM Service Extension Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apimServiceExtensionViewer) (`roles/apigee.apimServiceExtensionViewer`) on organization 
  * Manage long-running operations: [Apigee APIM Service Extension Service Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apimServiceExtensionServiceAgent) (`roles/apigee.apimServiceExtensionServiceAgent`) on the service agent in the Google Cloud project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set environment variables

In the Google Cloud project that contains your Apigee instance, use the following command to set environment variables: 
    
    
    export PROJECT_ID=PROJECT_ID
    export ORG_NAME=$PROJECT_ID
    export REGION=REGION
    export INSTANCE=INSTANCE
    export VPC_NETWORK_NAME=VPC_NETWORK_NAME
    export SUBNET=SUBNET

Where: 

  * `PROJECT_ID` is the ID of the project with your Apigee instance.
  * `REGION` is the Google Cloud region of your Apigee instance.
  * `INSTANCE` is the name of your Apigee instance.
  * `VPC_NETWORK_NAME` is the name of the VPC network in your Google Cloud project that you want to use for the Apigee Extension Processor.
  * `SUBNET` is the name of the subnet in your Google Cloud project that you want to use for the Apigee Extension Processor.



To confirm that the environment variables are set correctly, run the following command and review the output: 
    
    
    echo $PROJECT_ID $ORG_NAME $REGION $INSTANCE $VPC_NETWORK_NAME $SUBNET

### Configure an authentication token

To configure an authentication token, run the following command: 
    
    
    export TOKEN=$(gcloud auth print-access-token)
    echo $TOKEN

## Configure a load balancer for a backend service

The following sections describe the steps to set up a global external Application Load Balancer for a backend service, using **httpbin.org** as an example: 

  1. Create a global external Application Load Balancer.
  2. Create a network endpoint group (NEG).
  3. Create a backend service.
  4. Create a URL map.
  5. Create a target proxy.
  6. Create a global forwarding rule.



### Create a global external Application Load Balancer

To create the load balancer: 

  1. Set your `gcloud` configuration to use your current project: 
         
         gcloud config set project PROJECT_ID

Where PROJECT_ID is the ID of the project with your Apigee instance.

  2. Create a global static IP address: 
         
         gcloud compute addresses create IP_ADDRESS --ip-version=IPV4 --global

Where IP_ADDRESS is the name of the IP address you want to create. The name must match the regular expression `(?:a-z?)`.

  3. Get the IP address and save it as an environment variable: 
         
         IP=$(gcloud compute addresses describe IP_ADDRESS --format="get(address)" --global)

Where IP_ADDRESS is the name of the IP address you created in the previous step.

  4. Create a TLS certificate for [`nip.io`](https://nip.io/), a third-party service that provides wildcard DNS records for IP addresses: 
         
         gcloud compute ssl-certificates create SSL_CERT_NAME \
           --domains="nip.io"

Where SSL_CERT_NAME is the name of the certificate you want to create. 




### Create a network endpoint group (NEG)

To create the network endpoint group (NEG) for your load balancer: 

  1. Create a NEG: 
         
         gcloud compute network-endpoint-groups create NEG_NAME \
           --network-endpoint-type=INTERNET_FQDN_PORT \
           --default-port=443 \
           --global

Where NEG_NAME is the name of the NEG you want to create.

  2. Add the endpoint for **httpbin.org** to the NEG: 
         
         gcloud compute network-endpoint-groups update NEG_NAME \
           --add-endpoint=fqdn=**httpbin.org** ,port=443 \
           --global

Where NEG_NAME is the name of the NEG you created in the previous step.




### Create a backend service

To create the backend service exposed by the load balancer: 

  1. Create the backend service: 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --protocol=HTTPS \
           --global

Replace BACKEND_SERVICE_NAME is the name of the backend service you want to create.

  2. Add the NEG to the backend: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --network-endpoint-group=NEG_NAME \
           --global-network-endpoint-group \
           --global

Where: 

     * BACKEND_SERVICE_NAME is the name of the backend service you created in the previous step.
     * NEG_NAME is the name of the NEG you created in a previous step.



### Create a URL map

To create a URL map between the load balancer and the backend service, use the following command: 
    
    
    gcloud compute url-maps create URL_MAP_NAME \
      --default-service BACKEND_SERVICE_NAME \
      --global

Where: 

  * URL_MAP_NAME is the name of the URL map you want to create.
  * BACKEND_SERVICE_NAME is the name of the backend service you created in a previous step.



### Create a target proxy

To create a target proxy for the load balancer to process service extension traffic, use the following command: 
    
    
    gcloud compute target-https-proxies create TARGET_PROXY_NAME \
      --global \
      --ssl-certificates SSL_CERT_NAME \
      --global-ssl-certificates \
      --url-map URL_MAP_NAME \
      --global-url-map

Where: 

  * TARGET_PROXY_NAME is the name of the target proxy you want to create.
  * URL_MAP_NAME is the name of the URL map you created in a previous step.
  * SSL_CERT_NAME is the name of the SSL certificate you created for `nip.io` in a previous step.



### Create a global forwarding rule

To create a global forwarding rule for the load balancer, use the following command: 
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
      --load-balancing-scheme=EXTERNAL_MANAGED \
      --network-tier=PREMIUM \
      --address=IP_ADDRESS \
      --target-https-proxy=TARGET_PROXY_NAME \
      --ports=443 \
      --global

Where: 

  * FORWARDING_RULE_NAME is the name of the forwarding rule you want to create.
  * IP_ADDRESS is the name of the IP address of the NEG endpoint you created in a previous step.
  * TARGET_PROXY_NAME is the name of the target proxy that processes extension traffic.



## Configure the Apigee Extension Processor

The following sections describe the steps to set up the Apigee Extension Processor: 

  1. Create an Apigee environment.
  2. Create the Extension Processor proxy.



### Create an Apigee environment

**Note:** Before creating a new environment and environment group, or using existing resources for the step, review the limitations on environments, environment groups, and API proxies in the Extension Processor configuration. For more information, see [Limitations](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview#limitations).

  1. Create an Apigee environment using the following command: 
         
         curl -i -X POST -H  "Authorization: Bearer $TOKEN" \
             "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/environments" -H "Content-Type:application/json" -d \
             '{
                 "name": "ENV_NAME",
                 "displayName": "ENV_NAME",
                 "state": "ACTIVE",
                 "deploymentType": "PROXY",
                 "apiProxyType": "PROGRAMMABLE",
                 "type": "COMPREHENSIVE",
                 "properties":
                 {"property": [
                     {
                     "name": "apigee-service-extension-enabled",
                     "value": "true"
                     }
                   ]
                 }
             }'

Where ENV_NAME is the name of the environment you are creating. The name must contain between 2 and 32 characters which can be lowercase letters, numbers, or hyphens. The name must begin with a letter and cannot end with a hyphen. The name must be different from any other environment name in your organization.

Confirm that the environment is created: 
         
         curl -i -H "Authorization: Bearer $TOKEN" \
             "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/environments"

The list of environments should include the environment you just created.

  2. Attach the newly created environment to your Apigee instance: 
         
         curl -i -X POST -H "Authorization: Bearer $TOKEN" \
             "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/instances/$INSTANCE/attachments" -H "Content-Type:application/json" -d \
             '{
                 "environment": "ENV_NAME"
                 }'

Where ENV_NAME is the name of the environment you created in the previous step.

This operation may take up to 10 minutes.

  3. Create the Apigee environment group: 
         
         curl -H "Authorization: Bearer $TOKEN" -X POST \
             "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/envgroups" -H "Content-Type:application/json" -d \
             '{
                 "name": "ENV_GROUP_NAME",
                 "hostnames": ["ENV_GROUP_HOSTNAME"]
                 }'

Where: 

     * ENV_GROUP_NAME is the name of the environment group you are creating.
     * ENV_GROUP_HOSTNAME is the hostname of the environment group you are creating. The hostname must be a fully qualified domain name (FQDN). **Note:** The hostname does not need to be resolvable.
  4. Attach the new environment to the new environment group: 
         
         curl -H "Authorization: Bearer $TOKEN" -X POST\
             "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/envgroups/ENV_GROUP_NAME/attachments" -H "content-type:application/json" -d \
                 '{
                     "name": "ENV_GROUP_NAME",
                     "environment": "ENV_NAME"
                 }' 

Where: 

     * ENV_GROUP_NAME is the name of the environment group you are creating.
     * ENV_NAME is the name of the environment you created in an earlier step.



### Create the Extension Processor proxy

The Extension Processor proxy is an Apigee API proxy that is used to apply API management policies to the load balancer traffic. You can create a **no-target** proxy or an **Server-Sent event (SSE)-enabled** proxy. To learn more about using SSE with Apigee, see [Server-sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

To create an Apigee API proxy for use with the Extension Processor load balancer: 

### No target proxy

  1. Follow the steps in [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy#steps-to-create-an-api-proxy) to create a **No target** proxy with the following specifications: 
     * Proxy template: Select **No target**.
     * Proxy name: Enter a proxy name. This name will serve as the identifier for the Extension Processor.
     * Base path: Set any base path you would like. The path will not be used.

The XML specification for the proxy should appear similar to the following: 
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <APIProxy revision="1" name="extproc-sample">
        <DisplayName/>
        <Description/>
        <CreatedAt>1739581781912</CreatedAt>
        <LastModifiedAt>1739582447868</LastModifiedAt>
        <BasePaths>/</BasePaths>
        <Policies></Policies>
        <ProxyEndpoints>
            <ProxyEndpoint>default</ProxyEndpoint>
        </ProxyEndpoints>
    </APIProxy>

  2. Follow the steps in [Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new#deploy-an-api-proxy) to deploy the proxy to the environment you created earlier.



### SSE-enabled proxy

  1. Follow the steps in [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy#steps-to-create-an-api-proxy) to create a **Server-sent event** proxy with the following specifications: 
     * Proxy template: Select **No target**.
     * Proxy name: Enter a proxy name.
     * Base path: Set any base path you would like. The path will not be used.

The XML specification for the proxy should appear similar to the following: 
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <APIProxy revision="1" name="extproc-sample">
        <DisplayName/>
        <Description/>
        <CreatedAt>1739581781912</CreatedAt>
        <LastModifiedAt>1739582447868</LastModifiedAt>
        <BasePaths>/</BasePaths>
        <ProxyEndpoints>
            <ProxyEndpoint>default</ProxyEndpoint>
        </ProxyEndpoints>
    </APIProxy>

  2. Configure the `EventFlow` in the proxy: 
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <APIProxy revision="1" name="extproc-sample">
             <DisplayName/>
             <Description/>
             <CreatedAt>1739581781912</CreatedAt>
             <LastModifiedAt>1739582447868</LastModifiedAt>
             <BasePaths>/</BasePaths>
             **< ProxyEndpoints>
                 <ProxyEndpoint>default</ProxyEndpoint>
                 <EventFlow name="EventFlow" content-type="text/event-stream">
                   <Response/>
                 </EventFlow>
                 <HTTPProxyConnection>
                   <Properties/>
                   <URL>https://httpbin.org/sse</URL>
                 </HTTPProxyConnection>
             </ProxyEndpoints>**
         </APIProxy>

  3. Follow the steps in [Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new#deploy-an-api-proxy) to deploy the proxy to the environment you created earlier.



## Configure the traffic extension

This section describes how to configure the traffic service extension for your Extension Processor, using the following steps: 

  1. Create the traffic extension with the Extension Processor provisioning API.
  2. Send a request to the load balancer.



### Create the traffic extension with the Extension Processor provisioning API

In this step, create a traffic service extension for your Extension Processor using the Extension Processor provisioning API.

Create the traffic extension using the following command to call the Extension Processor provisioning API: 
    
    
    curl -X POST -H  "Authorization: Bearer $TOKEN" \
        https://apigee.googleapis.com/v1/organizations/$ORG_NAME/apimServiceExtensions?apimServiceExtensionId=TRAFFIC_EXT_NAME \
        -H "Content-Type:application/json" -d \
        '{
          "extensionProcessor": "TARGET_PROXY_NAME"
          "lbForwardingRule": "LB_FORWARDING_RULE",
          "network" : "NETWORK",
          "networkConfigs": [
            {
              "region": "$REGION",
              "subnet": "project/my-project/regions/$REGION/subnetworks/$SUBNET"
            }
          ],
          "extensions": [
            {
              "name": "TARGET_PROXY_NAME",
              "matchCondition": "CEL_EXPRESSION",
              "failOpen": FAIL_OPEN,
              "hostname": "ENV_GROUP_HOSTNAME",
              "supportedEvents": [
                "REQUEST_HEADERS",
                "RESPONSE_HEADERS"
              ]
            }
          ]
        }'

Where: 

  * TRAFFIC_EXT_NAME is is the name of the traffic extension you are creating.
  * LB_FORWARDING_RULE is the name of the forwarding rule you created in an earlier step.
  * NETWORK is the name of the network you created in an earlier step.
  * TARGET_PROXY_NAME is the name of the proxy that processes extension traffic.
  * CEL_EXPRESSION is the Common Expression Language (CEL) expression you want to use for the traffic extension. For more information on CEL syntax, see [CEL matcher language reference](https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference).
  * FAIL_OPEN is a boolean value that determines whether the traffic extension fails open or closed. Valid values are `true` or `false`.
  * ENV_GROUP_HOSTNAME is the hostname of the environment group you created in an earlier step.

**Note:** Once the traffic extension is created, the `name`, `lbForwardingRule`, and `network` fields can't be changed. 

This operation may take a few minutes to complete.

### Get traffic extension details

To verify that the traffic service extension was created successfully, use the following command: 
    
    
    curl -H "Authorization: Bearer $TOKEN" \
        "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/apimServiceExtensions/TRAFFIC_EXT_NAME"

Replace TRAFFIC_EXT_NAME with the name of the traffic extension you just created.

The response appears similar to the following: 
    
    
    {
      "name": "my-traffic-extension",
      "extensionProcessor": "my-extension-processor",
      "lbForwardingRule": "https://www.googleapis.com/compute/v1/projects/my-project/global/forwardingRules/my-forwarding-rule",
      "network": "projects/my-project/global/networks/my-network",
      "networkConfigs": [
        {
          "region": "us-west1",
          "subnet": "projects/my-project/regions/us-west1/subnetworks/my-subnet"
        }
      ],
      "extensions": [
        {
          "name": "organizations/my-org/apis/my-api-proxy",
          "matchCondition": "request.url.contains('1234567890')",
          "failOpen": true,
          "hostname": "my-hostname.apigee.net",
          "supportedEvents": [
            "REQUEST_HEADERS",
            "RESPONSE_HEADERS"
          ]
        }
      ]
    }

### Update a traffic extension

You can update the traffic extension using the `updateMask` parameter. When using the `updateMask` parameter, you specify the attributes of the resource that you want to update by providing a comma-separated list. The supported attributes for `updateMask` are: 

  * `networkConfigs`: updates to `region` and `subnet` fields. **Note:** This field is only updatable for **Global** Application Load Balancers. For **Regional** Application Load Balancers, the `networkConfigs` can't be updated; you must delete and recreate the extension to modify network configurations.
  * `extensions`: updates the `name`, `matchCondition`, `failOpen`, `hostname`, and `supportedEvents` fields.
  * `extensionProcessor`: updates the `extensionProcessor` field.



To update a traffic extension, use the `curl` command with the `PATCH` method. You can update multiple attributes by including them in the `updateMask` query parameter as a comma-separated string (e.g., `?updateMask=extensions,extensionProcessor`).

Here are some examples:

### Update `networkConfigs` (Global LB)

To update the `networkConfigs` attributes, use the following command:
    
    
    curl -X PATCH -H  "Authorization: Bearer $TOKEN" \
      https://apigee.googleapis.com/v1/organizations/$ORG_NAME/apimServiceExtensions/TRAFFIC_EXT_NAME?updateMask=networkConfigs \
      -H "Content-Type:application/json" -d \
      '{
        "networkConfigs": [
          {
            "region": "REGION",
            "subnet": "projects/$PROJECT/regions/REGION/subnetworks/SUBNET"
          }
        ]
      }'

Where: 

  * TRAFFIC_EXT_NAME is the name of the Extension Processor traffic extension to update.
  * REGION is the region of the updated region.
  * SUBNET is the new subnet of the network.



### Update `extensions`

To update the `extensions` attributes, use the following command:
    
    
    curl -X PATCH -H  "Authorization: Bearer $TOKEN" \
      https://apigee.googleapis.com/v1/organizations/$ORG_NAME/apimServiceExtensions/TRAFFIC_EXT_NAME?updateMask=extensions \
      -H "Content-Type:application/json" -d \
      '{
        "extensions": [
          {
            "name": "TARGET_PROXY_NAME",
            "matchCondition": "NEW_CEL_EXPRESSION",
            "failOpen": NEW_FAIL_OPEN
            "hostname": "NEW_ENV_GROUP_HOSTNAME",
            "supportedEvents": [
              "REQUEST_HEADERS",
              "RESPONSE_HEADERS"
            ]
          }
        ]
      }'

Where: 

  * TRAFFIC_EXT_NAME is the name of the Extension Processor traffic extension to update.
  * TARGET_PROXY_NAME is the name of the proxy that processes extension traffic.
  * NEW_CEL_EXPRESSION is the updated CEL expression.
  * NEW_FAIL_OPEN is the updated boolean value for fail open.
  * NEW_ENV_GROUP_HOSTNAME is the hostname of the environment group.



### Update `extensionProcessor`

To update the `extensionProcessor` attributes, use the following command:
    
    
    curl -X PATCH -H  "Authorization: Bearer $TOKEN" \
      https://apigee.googleapis.com/v1/organizations/$ORG_NAME/apimServiceExtensions/TRAFFIC_EXT_NAME?updateMask=extensionProcessor \
      -H "Content-Type:application/json" -d \
      '{
        "extensionProcessor": "NEW_TARGET_PROXY_NAME"
      }'

Where: 

  * TRAFFIC_EXT_NAME is the name of the Extension Processor traffic extension to update.
  * NEW_TARGET_PROXY_NAME is the new name of the proxy that processes extension traffic.



### Update Multiple Attributes (Global LB)

To update the `extensions` and `extensionProcessor` attributes simultaneously, use the following command:
    
    
    curl -X PATCH -H  "Authorization: Bearer $TOKEN" \
      https://apigee.googleapis.com/v1/organizations/$ORG_NAME/apimServiceExtensions/TRAFFIC_EXT_NAME?updateMask=extensions,extensionProcessor \
      -H "Content-Type:application/json" -d \
      '{
        "extensions": [
          {
            "name": "TARGET_PROXY_NAME",
            "matchCondition": "NEW_CEL_EXPRESSION",
            "failOpen": NEW_FAIL_OPEN,
            "hostname": "NEW_ENV_GROUP_HOSTNAME",
            "supportedEvents": [
              "REQUEST_HEADERS",
              "RESPONSE_HEADERS"
            ]
          }
        ],
        "extensionProcessor": "NEW_TARGET_PROXY_NAME"
      }'

Where: 

  * TRAFFIC_EXT_NAME is the name of the Extension Processor traffic extension to update.
  * TARGET_PROXY_NAME is the name of the proxy that processes extension traffic.
  * NEW_CEL_EXPRESSION is the updated CEL expression.
  * NEW_FAIL_OPEN is the updated boolean value for fail open.
  * NEW_ENV_GROUP_HOSTNAME is the hostname of the environment group.
  * NEW_TARGET_PROXY_NAME is the new name of the proxy that processes extension traffic.



## Send a request to the load balancer

To test the load balancer and Extension Processor setup, send a request to the load balancer: 
    
    
    curl "https://LB_DOMAIN_NAME/get"

Where LB_DOMAIN_NAME is the domain name you used for the load balancer and SSL certificate. If you used `nip.io`, the domain name will look similar to `IP_ADDRESS.nip.io`.

The response appears similar to the following: 
    
    
    {"status": 200,
      {
        "args": {},
        "headers": {
          ...
        },
        "origin": "173.93.50.108",
        "url": "https://httpbin.org/get"
      }
    }

## Use policies with the Extension Processor

This section describes how to use policies with the Extension Processor.

In this example, configure a [VerifyAPIKey](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) and [AssignMessage](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) policy for the Extension Processor. These policies validate API keys included in requests to Apigee and inject a Google token into request headers for calls to a backend service. This scenario would be useful for API providers using the Apigee Extension Processor to authorize and authenticate requests to their Apigee services and seamlessly inject the [Google auth tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview) required for a backend service like Vertex AI.

### Add the VerifyAPIKey policy for API key validation

The following sections describe how to use the VerifyAPIKey policy to validate API keys for calls to your backend service using the Extension Processor: 

  1. Attach the VerifyAPIKey policy to the Extension Processor.
  2. Create an API product.
  3. Create a developer App and App credentials.
  4. Send a request to the load balancer using the API key.



#### Attach the VerifyAPIKey policy to the proxy

To attach a VerifyAPIKey policy to the Extension Processor proxy: 

  1. In the Google Cloud console, go to the **Apigee > Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the Extension Processor proxy you created in Create an extension processor section.
  3. Click the **Develop** tab. 
  4. In the navigation pane, click  add_circle in the **Policies** section.
  5. In the **Create policy** dialog, select **VerifyAPIKey** from the list of policies. 
  6. In the **VerifyAPIKey** pane, complete the required fields in the **Name** and **Display name** sections using the following values: 
     * **Name** : Enter a policy name. For example, `VA-verify-api-key`.
     * **Display name** : Enter policy name for use in the UI. For example, `VA-verify-api-key`.
  7. Click **Create**. 

The XML specification for the VerifyAPIKey policy included in the Extension Processor proxy should appear similar to the following: 
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
           <VerifyAPIKey continueOnError="false" enabled="true" name="VA-verify-api-key">
             <DisplayName>VA-verify-api-key</DisplayName>
             <Properties/>
             <APIKey ref="request.queryparam.x-api-key"/>
           </VerifyAPIKey>

  8. Deploy the new proxy revision.



#### Create an API product

To create an API product and configure the API operation set for your service: 

  1. Follow the steps in [Creating an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#add) to create an API product for your service. You can configure the **Product details** for the API product however you wish.
  2. Follow the steps in [Operations](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#operations) to add an API operation set to the API product, according to the following specifications: 
     * Source: 

In the Google Cloud console, go to the **Apigee > Distribution > API Products** page.

[Go to API Products](https://console.cloud.google.com/apigee/apiproducts)

Select the API product you created in an earlier step.
     * Operation: Click **Edit** and configure the following paths and methods: 
       * Path: `/get` with Method: `GET`
       * Path: `/TARGET_PROXY_NAME` with Method: `GET`

TARGET_PROXY_NAME is the name of the proxy that processes extension traffic.




#### Create a developer App and App credentials

To create a developer App and App credentials for the newly created API product: 

  1. Go to the **Apigee API management** page in the Google Cloud console: 

[Apigee API management](https://console.cloud.google.com/apigee)

  2. Create a developer: 
     1. Select **Distribution > Developers**.
     2. On the **Developers** page, click **\+ Create**.
     3. In the **Add developer** page, complete the required fields using any values you wish.
     4. Click **Add**.
  3. Create an App: 
     1. Select **Distribution > Apps**.
     2. On the **Apps** page, click **\+ Create**
     3. On the **Create App** page, complete the required fields in the **App Details** section using the following values: 
        * **App name** : Enter a name for the App. For example, `ext-proc-app`
        * **Developer** : Select the developer you created in the previous step, or another developer from the list.
     4. In the **App Credentials** section, click **\+ Add Credential**.
     5. In the **Credential** section, select **Never** from the **Expiry** list box. 
     6. In the **Products** section, click **\+ Add products** to display the **Add Products** pane.
     7. Select the API product you created in the previous step.
     8. Click **OK**.
     9. Click **Add** to close the **Add Products** pane.
     10. Click **Create**.
  4. In the **App Details** page, in the **Credential** section, click _visibility_off_ to display the value of the **Key**. 

Copy the `Key` value. You will use this key to make API calls to your service in a later step.

  5. In the **App Details** page, in the **Credential** section, click _visibility_off_ to display the value of the **App Secret**.



#### Send a request to the load balancer using the API key

To test the API key validation, send a request to the load balancer using the API key: 
    
    
    curl "https://LB_DOMAIN_NAME/get"

Where LB_DOMAIN_NAME is the domain name you used for the load balancer and SSL certificate. 

The response fails without an API key.

Send another request to the load balancer, using the API key in the request: 
    
    
    curl "https://LB_DOMAIN_NAME/get?key=API_KEY"

Where: 

  * LB_DOMAIN_NAME is the domain name you used for the load balancer and SSL certificate.
  * API_KEY is the API key from the Developer App credentials revealed in an earlier step.



The response indicates successful authorization for the endpoint. This indicates that the Extension Processor validated the API key and the Apigee proxy can now process the request.

### Add the AssignMessage policy for Google authentication

If you want to use your Extension Processor to provide API management for a Google-authenticated service, you can inject a Google access token or Google ID token into requests sent to the backend service using the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

The following sections describe how to use the AssignMessage policy to inject a Google authentication token into requests sent to the backend service using the Extension Processor: 

  1. Attach the AssignMessage policy to the proxy.
  2. Send a request to the load balancer to test token injection.



#### Attach the AssignMessage policy to the proxy

To add the AssignMessage policy to your proxy: 

  1. In the Google Cloud console, go to the **Proxy Development > API Proxies** page.

[Go to API Proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the Extension Processor proxy you created in Create an extension processor section.
  3. Click the **Develop** tab. 
  4. In the navigation pane, click  add_circle in the **Policies** section.
  5. In the **Create policy** dialog, select **AssignMessage** from the list of policies.
  6. In the **Assign Message** pane, complete the required fields in the **Name** and **Display name** sections using the following values: 
     * **Name** : Enter a policy name. For example, `AM-auth`.
     * **Display name** : Enter a policy name to display in the UI. For example, `AM-auth`.
  7. Click **Create**.
  8. Under the `<Set>` element, add the following child elements: 
         
         <Set>
             <Authentication>
             <HeaderName>Authorization</HeaderName>
             <GoogleAccessToken>
                 <Scopes>
                 <Scope>https://www.googleapis.com/auth/cloud-platform</Scope>
                 </Scopes>
             </GoogleAccessToken>
             </Authentication>
         </Set>

  9. Click **Save**.
  10. Deploy the new revision using a Google service account.



The service account generates Google access tokens and injects them into the request header for API calls to Google backend services.

#### Send a request to the load balancer to test token injection

To confirm that token injection is working, send a request to the load balancer: 
    
    
    curl "https://LB_DOMAIN_NAME/get"

Where LB_DOMAIN_NAME is the domain name you used for the load balancer and SSL certificate.

The response appears similar to the following: 
    
    
    {
      ...
      "headers": {
        "Accept": "*/*",
        "**Authorization"** : "Bearer ya29.c.c0ASRK0Gbw03y9cfvxL11DxaRYBQUU18SmUP4Vu63OckHI5cX7wJ4DmGMG2vbDDS69HXJHqMj-lak4tcqOsJGmE65crn2gNuJLanXidwM8",
        "First": "1.0",
        "Host": "apigee-ext-proc-test.apigee.net",
        "Second": "1.0",
        "Sum": "2",
        "User-Agent": "curl/8.7.1",
        **"X-Api-Key" : "McYcHGR3PTSGLXExvKADwQ1JJeCjgPDUvAakCl0rJKCFaX0Y"**,
        "X-Cloud-Trace-Context": "0fd3dadc2a3c328fa968d5f5f1434c29/18300783092696918345"
      },
      ...
    }

The response shows the successful injection of the Google authentication token into the request header.

With the successful application of the AssignMessage policy, the client's successful request (containing the API key) to Apigee in the example scenario is modified further to include a Google authentication token in the request header, as required by the Google-authenticated backend service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
