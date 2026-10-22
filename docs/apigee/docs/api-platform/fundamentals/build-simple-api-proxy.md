---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy/
title: Building a simple API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:22.884705+00:00
---

# Building a simple API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Building a simple API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** In environments enabled for [archive deployments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#deployment-types), you cannot build API proxies using the Apigee UI, API, or gcloud. To build API proxies for archive deployments using Apigee in VS Code,see [Developing API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-apiproxies) using Apigee in VS Code.

Apigee enables you to quickly expose backend services as APIs. You do this by creating an API proxy that provides a facade for the backend service that you want to expose. You need to provide only the network address for the backend service, along with some information that Apigee uses to create the API proxy that is exposed to developers. 

The API proxy decouples your backend service implementation from the API that developers consume. This shields developers from future changes to your backend services. As you update backend services, developers, insulated from those changes, can continue to call the API uninterrupted.

This topic provides information about the various types of proxies and the settings for them. For step-by-step instructions on creating proxies, see the following topics:

  * Tutorial: [Build your first API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started)
  * [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy)
  * [Configuring a proxy with YAML](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/configure-proxy-with-yaml)



In addition to the UI, the API, and the XML bundle format, you can define an API proxy in YAML using an Apigee Feature Template, and then deploy it with the Google Cloud CLI. This is an alternative to authoring the XML proxy bundle. For more information, see [Configuring a proxy with YAML](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/configure-proxy-with-yaml).

## Creating an API proxy using the UI

The easiest way to create an API proxy is using the **Create Proxy** wizard.

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Click **\+ Create**.



The **Create Proxy** wizard displays and leads you through the steps to generate and add minimal features to an API proxy.

The wizard enables you to create an API proxy from the following sources:

Category | Type | Description  
---|---|---  
General template | Reverse proxy (most common) |  An API proxy that routes inbound requests to existing HTTP backend services. Can be a JSON or XML API. See Creating a reverse proxy for an HTTP service later in this section.  
No target |  An API proxy with no API backend ("no target"). Similar to Creating a reverse proxy for an HTTP service described previously, except you will not specify an existing API when defining the API proxy details.   
Upload proxy bundle | An existing API proxy bundle (for example one of the [sample API proxies](https://github.com/apigee/api-platform-samples) available on GitHub). See [ Importing an API proxy from an API proxy bundle](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#importinganapiproxyfromanapiproxybundle).  
Proxy with Server-Sent Events (SSE) | An API proxy that includes an `EventFlow` for streaming server-sent events (SSE). For more information, see [Streaming server-sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).  
AI template | Prompt Token Limit | Similar to a spike arrest, this policy helps you control the rate of token usage from user prompts to prevent abuse. For more information, see [ Get started with Apigee AI Token Policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-ai-token-policies).   
LLM Token Quota | Manage and limit token consumption for LLM API calls. For more information, see [ Get started with Apigee AI Token Policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-ai-token-policies).   
Proxy with Model Armor | Enforces safe AI interactions by sanitizing user prompts and model responses. For more information, see [ Get started with Apigee Model Armor policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies).  
Proxy with Semantic Cache | Cache responses to similar requests, optimizing response time and LLM calls. For more information, see [ Get started with semantic caching policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies).  
OpenAPI spec template | Reverse proxy (most common) | Generate the proxy from a valid OpenAPI specification. For more information on this option, see Using OpenAPI Specifications to generate proxies later in this section.  
No target | An API proxy with no API backend ("no target"). Similar to Creating a reverse proxy for an HTTP service described previously, except you will not specify an existing API when defining the API proxy details.   
  
The following sections discuss the details of each proxy type.

## Creating a reverse proxy for an HTTP service

Apigee generates reverse proxies based on the following information:

  * URL of the backend service.
  * URI path that uniquely identifies the API that will be exposed by the API proxy to consumer apps.



The backend service URL typically represents a service-enabled application owned by your organization. It can also point to a publicly available API. The API or service can be under your control (for example, an internal HR application or a Rails application in the Cloud) or it can be a third-party API or service (for example, Twitter or Instagram). 

The following **Proxy details** are available after accessing the **Create Proxy wizard** and selecting a proxy type:

Field | Description  
---|---  
Name | Name displayed for your API. Specify alphanumeric characters, dash (-), or underscore (_).  
Base path |  URI fragment that appears after the `http://[host]` or `https://[host]` address of your API proxy. Apigee uses the base path URI to match and route incoming request messages to the proper API proxy. **Note** : The API proxy base path defaults to the value specified for the `Name` field converted to all lower case.Following the base path are any additional resource URLs. The full URL structure that clients use to call your API proxy is as follows: `https://[host]/BASE_PATH/CONDITIONAL_FLOW_PATH` **Note** : The base path must be unique; you cannot deploy two API proxies with the same base path. If you edit a deployed API proxy and set the base path to the same value as the base path of another API proxy, Apigee automatically undeploys the API proxy when you save it. Before you can redeploy the API proxy, you must edit the base path so that it is unique. **Use wildcards in base paths** Use one or more `/*/` wildcards in API proxy base paths to future-proof your API proxies. For example, a base path of `/team/*/members` allows clients to call `https://[host]/team/**blue** /members` and `https://[host]/team/**green** /members` without you needing to create new API proxies to support new teams. Note that `/**/` is not supported.  
Description | (Optional) Description of the API.  
Target (Existing API) | URL of the backend service that this API proxy invokes.  
  
## Importing an API proxy from an API proxy bundle

**Note:** When importing an API proxy from an API proxy bundle, you are responsible for configuring security in and adding policies to the bundle. The UI does not prompt you to add security or policies when importing the bundle, as described in Adding security later in this section.

Often you define API proxies as a collection of XML files, along with any other supporting files. By defining your API proxies as a set of files external to Apigee you can maintain them in a source-control system, and then import them into Apigee for testing and deployment.

To import API proxies from an API proxy bundle, perform the following steps: 

  1. Access the **Create Proxy** wizard as described in Creating an API proxy using the UI.
  2. Specify the API proxy bundle details.
     1. In the **Proxy template** menu, select **Upload proxy bundle**.
     2. In the **Proxy details** section, enter the **Proxy name** , upload the zip file and click **Next**.
     3. In the **Deploy** section, select the deployment environments, if desired, and click **Create**.



## Creating gRPC API proxies

In addition to REST API proxies, Apigee supports gRPC API proxies _with passthrough support only_ at this time. With _passthrough support_ , the gRPC payload is itself opaque to Apigee and the traffic is routed from the gRPC client to the preconfigured gRPC target server in the target configuration. 

At this time, Apigee gRPC API proxies: 

  * Support unary gRPC requests.
  * Can't use policies that affect the payload.
  * Can be used in API products that are not associated with GraphQL or REST proxies. API product-specific quotas and other operation settings apply across all proxies in the product.
  * Are not supported in Apigee hybrid.
  * Use two gRPC-specific [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#request): `request.grpc.rpc.name` and `request.grpc.service.name`. 
  * Can be monitored with these gRPC-specific [Apigee Analytics variables](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions): `x_apigee_grpc_rpc_name`, `x_apigee_grpc_service_name`, and `x_apigee_grpc_status`. 
  * Return [gRPC status codes](https://grpc.github.io/grpc/core/md_doc_statuscodes.html). 



You must also configure your load balancer to support gRPC. See [Using gRPC with your applications](https://cloud.google.com/load-balancing/docs/https#using_grpc_with_your_applications) and Using gcloud CLI commands to create routing for gRPC.

To create a gRPC API proxy, first define a gRPC target server (see [Creating TargetServers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#createtargetservers)) and then specify that target server when creating the new proxy.

### Using gcloud CLI commands to create routing for gRPC

This section shows example commands for creating routing for gRPC proxies, using the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). The instructions include setting up load balancers, a target server, and a MIG.

This section is not as a comprehensive guide to creating the routing. These examples might not be appropriate for all use cases. Also, these instructions assume familiarity with [External routing (MIG)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#external-routing-mig) and [Cloud load balancer gRPC configuration](https://cloud.google.com/load-balancing/docs/l7-internal#grpc_support). 

**Set environment variables**

These environment variables are used in the commands in the subsections. 
    
    
    PROJECT_ID=YOUR_PROJECT_ID
    MIG_NAME=YOUR_MIG_NAME
    VPC_NAME=default
    VPC_SUBNET=default
    REGION=REGION_NAME
    APIGEE_ENDPOINT=ENDPOINT
    CERTIFICATE_NAME=CERTIFICATE_NAME
    DOMAIN_HOSTNAME=DOMAIN_HOSTNAME

#### Example gcloud CLI commands for creating routing for gRPC proxies using new load balancers

This section shows example commands for creating gRPC proxies using the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) and a new load balancer. The instructions include setting up the load balancer, a target server, and a MIG.

**Create the instance template**
    
    
    gcloud compute instance-templates create $MIG_NAME \
    --project $PROJECT_ID \
    --region $REGION \
    --network $VPC_NAME \
    --subnet $VPC_SUBNET \
    --tags=https-server,apigee-mig-proxy,gke-apigee-proxy \
    --machine-type e2-medium --image-family debian-12 \
    --image-project debian-cloud --boot-disk-size 20GB \
    --no-address \
    --metadata ENDPOINT=$APIGEE_ENDPOINT,startup-script-url=gs://apigee-5g-saas/apigee-envoy-proxy-release/latest/conf/startup-script.sh

**Create the managed instance group**
    
    
    gcloud compute instance-groups managed create $MIG_NAME \
    --project $PROJECT_ID --base-instance-name apigee-mig \
    --size 2 --template $MIG_NAME --region $REGION

**Configure autoscaling**
    
    
    gcloud compute instance-groups managed set-autoscaling $MIG_NAME \
    --project $PROJECT_ID --region $REGION --max-num-replicas 50 \
    --target-cpu-utilization 0.75 --cool-down-period 90

**Define a named port**
    
    
    gcloud compute instance-groups managed set-named-ports $MIG_NAME \
    --project $PROJECT_ID --region $REGION --named-ports https:443

**Create a Google-managed SSL certificate and key for the load balancer**
    
    
    gcloud compute ssl-certificates create $CERTIFICATE_NAME \
    --domains=$DOMAIN_HOSTNAME \
    --project $PROJECT_ID \
    --global

**Validate that the certificate is provisioned**
    
    
    gcloud compute ssl-certificates describe $CERTIFICATE_NAME \
    --global \
    --format="get(name,managed.status, managed.Status)"

**Create the Global Cloud Load Balancer (GCLB)**

  1. Create a health check  

         
         gcloud compute health-checks create https hc-apigee-envoy-443 \
         --project $PROJECT_ID --port 443 --global \
         --request-path /healthz/ingress

  2. Create the backend service for http1  

         
         gcloud compute backend-services create YOUR_BACKEND_1 \
         --project $PROJECT_ID \
         --protocol HTTPS \
         --health-checks hc-apigee-envoy-443 \
         --port-name https \
         --timeout 302s \
         --connection-draining-timeout 300s \
         --global

  3. Create the backend service for http2  

         
         gcloud compute backend-services create YOUR_BACKEND_2 \
         --project $PROJECT_ID \
         --protocol HTTP2 \
         --health-checks hc-apigee-envoy-443 \
         --port-name https \
         --timeout 302s \
         --connection-draining-timeout 300s \
         --global

  4. Add MIGs to the backend service. In this example we are reusing the MIG, but you could also create a new pair of MIGs.  

         
         gcloud compute backend-services add-backend YOUR_BACKEND_1 \
         --project $PROJECT_ID --instance-group $MIG_NAME \
         --instance-group-region $REGION \
         --balancing-mode UTILIZATION --max-utilization 0.8 --global
         
         gcloud compute backend-services add-backend YOUR_BACKEND_2 \
         --project $PROJECT_ID --instance-group $MIG_NAME \
         --instance-group-region $REGION \
         --balancing-mode UTILIZATION --max-utilization 0.8 --global

  5. Create a load balancing URL map. Check first whether you already have a URL map. If you do, make sure to modify that map according to the requirements below rather than overwrite it.  


Create a YAML file or use your existing file, at `/tmp/apigee-map.yaml`, with this configuration. Note that the URL map http1 backend is default.
         
         defaultService: projects/$PROJECT_ID/global/backendServices/YOUR_BACKEND_1
         name: matcher1
         routeRules:
         - matchRules:
         - headerMatches:
         - headerName: Content-Type
         prefixMatch: application/grpc
         prefixMatch: /
         priority: 100
         routeAction:
         weightedBackendServices:
         - backendService: projects/$PROJECT_ID/global/backendServices/YOUR_BACKEND_2
         weight: 100

Validate the URL map:
         
         gcloud compute url-maps validate --source /tmp/apigee-map.yaml --project $PROJECT_ID

Create the url map with header-based routing:
         
         gcloud compute url-maps import apigee-http1-http2 \
         --source /tmp/apigee-map.yaml  \
         --global --project $PROJECT_ID




**Create a load balancing target HTTPS proxy**
    
    
    gcloud compute target-https-proxies create apigee-envoy-https-proxy \
    --project $PROJECT_ID --url-map apigee-envoy-proxy-map \
    --ssl-certificates $CERTIFICATE_NAME

**Reserve an IPV4 External IP and create firewall rules for the load balancer**
    
    
    gcloud compute addresses create lb-ipv4-vip-1 \
    --project $PROJECT_ID \
    --network-tier=PREMIUM \
    --ip-version=IPV4 \
    --global
    
      gcloud compute addresses describe lb-ipv4-vip-1 \
    --project $PROJECT_ID --format="get(address)" --global
    
      gcloud compute forwarding-rules create apigee-envoy-https-lb-rule \
    --project $PROJECT_ID --address lb-ipv4-vip-1 --global \
    --target-https-proxy apigee-envoy-https-proxy --ports 443

**Create a firewall rule**
    
    
    gcloud compute firewall-rules create k8s-allow-lb-to-apigee-envoy \
    --description "Allow incoming from GLB on TCP port 443 to Apigee Proxy" \
    --project $PROJECT_ID --network $VPC_NAME --allow=tcp:443 \
    --source-ranges=130.211.0.0/22,35.191.0.0/16 --target-tags=gke-apigee-proxy

#### Example gcloud CLI commands for creating routing for gRPC proxies for existing load balancers

This section shows example commands for creating gRPC proxies using the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) and an existing load balancer. The instructions include setting up the load balancer, a target server, and a MIG.

**Create another backend service for http2**
    
    
    # Create backend service for http2
        gcloud compute backend-services create YOUR_BACKEND_2 \
    --project $PROJECT_ID \
    --protocol HTTP2 \
    --health-checks hc-apigee-envoy-443 \
    --port-name https \
    --timeout 302s \
    --connection-draining-timeout 300s \
    --global

**Attach the second backend service to the MIG**
    
    
    gcloud compute backend-services add-backend YOUR_BACKEND_2 \
    --project $PROJECT_ID --instance-group $MIG_NAME \
    --instance-group-region $REGION \
    --balancing-mode UTILIZATION --max-utilization 0.8 --global

**List the URL map for the existing Apigee GCLB**
    
    
    gcloud compute url-maps list -project $PROJECT_ID

**Pick up the correct URL map name used for Apigee load balancing**
    
    
    gcloud compute url-maps export APIGEE_URL_MAP_NAME -project $PROJECT_ID

**Create a load balancing URL map YAML file**

If you already have an existing URL map, merge this configuration into that. Otherwise, create a YAML file at `/tmp/apigee-map.yaml` with this configuration.
    
    
    defaultService: projects/dg-runtime-test1/global/backendServices/YOUR_BACKEND_1
    name: matcher1
    routeRules:
    - matchRules:
    - headerMatches:
    - headerName: Content-Type
    prefixMatch: application/grpc
    prefixMatch: /
    priority: 100
    routeAction:
    weightedBackendServices:
    - backendService: projects/dg-runtime-test1/global/backendServices/YOUR_BACKEND_2
    weight: 100

**Apply the new YAML for gRPC routing**
    
    
    gcloud compute url-maps import APIGEE_URL_MAP_NAME\
    --source /tmp/apigee-map.yaml  \
    --global -project $PROJECT_ID

## Adding security

Proxy security is achieved by adding a policy to your proxy. For more information on policies, see [What's a policy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement). For more information on security, see [Securing a proxy](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-security).

To add a security policy to your proxy:

  1. Create a proxy as described in [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy).
  2. Add a security policy as described in one of the sections listed in [Securing a proxy](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-security). The most common security policies used are [API keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-keys) and [OAuth2](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home).



## Adding support for CORS

Cross-origin resource sharing (CORS) is a standard mechanism that allows a web browser to make direct requests to another domain. The CORS standard defines a set of HTTP headers that web browsers and servers use to implement cross-domain communication.

You can add support for CORS by adding the CORS policy to the **request PreFlow of the ProxyEndpoint**. 

For more detailed information about CORS support, including adding CORS preflight support to a proxy, see [Adding CORS support to an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-cors-support-api-proxy).

## Adding Quotas

Quotas protect your backend service from high traffic under **Quota**. See [Quotas](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product#quotas). (Not available if Pass-through authorization is selected.)

## Using OpenAPI Specifications to generate proxies

This section discusses the Use OpenAPI option that is available for generating from an OpenAPI Specification the following types of API proxies: reverse or no target.

### What is an OpenAPI Specification?

![Open API Initiative logo](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/OpenAPI_Pantone.png) "The Open API Initiative (OAI) is focused on creating, evolving and promoting a vendor neutral API description format based on the Swagger Specification." For more information, see [OpenAPI Initiative](https://openapis.org).

An _OpenAPI Specification_ uses a standard format to describe a RESTful API. Written in either JSON or YAML format, an OpenAPI Specification is machine readable, but is also easy for humans to read and understand. The specification describes API elements such as its base path, paths and verbs, headers, query parameters, operations, content types, response descriptions, and more. In addition, an OpenAPI Specification is commonly used to generate API documentation.

The following fragment from an OpenAPI Specification describes Apigee's mock target service, [http://mocktarget.apigee.net](https://mocktarget.apigee.net). For more information, see [OpenAPI spec for the helloworld sample](https://github.com/apigee/api-platform-samples/tree/master/default-proxies/helloworld/openapi).
    
    
    openapi: 3.0.0
    info:
      description: OpenAPI Specification for the Apigee mock target service endpoint.
      version: 1.0.0
      title: Mock Target API
    paths:
      /:
        get:
          summary: View personalized greeting
          operationId: View a personalized greeting
          description: View a personalized greeting for the specified or guest user.
          parameters:
            - name: user
              in: query
              description: Your user name.
              required: false
              schema:
                type: string
          responses:
            "200":
              description: Success
      /help:
        get:
          summary: Get help
          operationId: Get help
          description: View help information about available resources in HTML format.
          responses:
            "200":
              description: Success
    ...

Through the **Create Proxy** wizard, you can import an OpenAPI Specification and use it to generate an API proxy. Once the proxy is generated, you can use the Apigee UI to further develop it by adding policies, implementing custom code, and so on&emdash;just like any Apigee proxy.

###  Creating an API proxy from an OpenAPI Specification

Create your API proxies from an OpenAPI Specification. In just a few clicks, you'll have an API proxy with the paths, parameters, conditional flows, and target endpoints generated automatically. Then, you can add features such as OAuth security, rate limiting, and caching.

In the **Create Proxy** wizard, click **Use OpenAPI Spec** and follow the wizard to create a reverse or no target proxy from an OpenAPI Specification. For details, see [Creating an API proxy from an OpenAPI Specification](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/create-api-proxy-openapi-spec).

## Creating a new revision of an API proxy

To create a new revision of an API proxy, perform the following steps:

  1. Open the Apigee UI.

In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Click the API proxy in the list that you want to copy. 
  3. Click the **Develop** tab. 

  4. Select the **Save** button and select **Save as New Revision**. 



## Backing up an API proxy

You can back up an existing API proxy as a set of XML files in an API proxy bundle. Once exported to a bundle, you can import the API proxy to a new proxy, as described in Importing an API proxy from an API proxy bundle previously in this section. For more information, see [Download API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/download-api-proxies). 

## Creating an API proxy using the API

To create an API proxy using the API, see [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy#apigee-api). 

## About no target proxies

No target proxies in Apigee are useful when you want to process requests within Apigee itself without forwarding them to a backend service. It's important to understand when this approach is appropriate. 

### Common use cases

  * **Interacting with Apigee-managed data** : A no target proxy is useful in cases where you only need to interact with Apigee-managed data, such as data stored in a [key-value map (KVM)](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps) or the [Apigee cache](https://docs.cloud.google.com/apigee/docs/api-platform/cache/optimize-performance-using-cache). For example, you can use a no-target proxy to retrieve data, such as user session data or configuration data, from the KVM. In this case, there's no need to call a backend service. All that's needed is a [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) in the proxy flow. For another example, you might want the caller to request that a cache be flushed. You can do this by invoking the [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy), without any need to connect to a target.
  * **Using mock APIs** : You can create mock APIs to simulate API behavior before the backend implementation is complete to enable frontend development to progress independently. To learn more about creating mock APIs, see [OpenAPI Mock API Proxy](https://github.com/apigee/devrel/tree/main/references/openapi-mock).
  * **Token management** : Apigee can issue OAuthV2 tokens, and that is usually done via a no-target proxy. 
  * **Testing policy behavior** : A no-target proxy can be useful when you want to try out Apigee policies to test their behavior.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
