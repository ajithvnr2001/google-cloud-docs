---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/service-directory-integration-setup/
title: Set up integration with Service Directory \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:04.430928+00:00
---

# Set up integration with Service Directory  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/service-directory-integration-setup/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up integration with Service Directory

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Deprecated:** Cloud Service Mesh's integration with Service Directory is going to be deprecated. Creating new service binding resources will be disabled.

This guide assumes that you have a running Cloud Service Mesh deployment and that you registered at least one service with Service Directory. The setup instructions apply whether you are using Envoy or proxyless gRPC.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

To use Service Directory and Cloud Service Mesh, the first step is to publish your service to Service Directory. See information about [publishing a service to Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory) or the [Service Directory documentation](https://docs.cloud.google.com/service-directory/docs) for general overview information.

After the service is registered with Service Directory, you create a service binding by using Cloud Service Mesh's API resources. You create a backend service that is dedicated to the integration with Service Directory, because a backend service that references service bindings cannot have backends or an associated health check.

## Cloud Service Mesh forwarding rule and host rule requirements with the load balancing APIs

When you configure Cloud Service Mesh for use with Service Directory and you use the older load balancing APIs, follow these guidelines:

  1. Ensure that the Cloud Service Mesh forwarding rule uses the `0.0.0.0` virtual IP address (VIP).
  2. If you have a [private zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone), make sure that the host rule in the URL map matches the DNS name that Service Directory configures in your Cloud DNS private zone.



If you don't follow these guidelines, outbound requests from your applications are likely to fail.

## Set the `network-services` API endpoint

Before you create and use a backend service, make sure that the `network-services` API endpoint is set so that service bindings resources under `network-services` resources are referenced correctly. Set the `network-services` API endpoint using the following command.
    
    
    export CLOUDSDK_API_ENDPOINT_OVERRIDES_NETWORKSERVICES="https://networkservices.googleapis.com/"
    

## Role and permission requirements

Make sure that you have following permissions and roles before you create your Cloud Service Mesh deployment.

### Service binding permissions and roles

This section does not discuss project-level Owner, Editor, and Viewer permissions. It describes the permissions and roles required to create, read, update, and delete resources.

Action | Permission | Roles  
---|---|---  
Create a service binding. | `networkservices.serviceBindings.create` | Network Admin  
Get a service binding. | `networkservices.serviceBindings.get` | Network Admin, Network Viewer  
List service bindings in a Google Cloud project. | `networkservices.serviceBindings.list` | Network Admin, Network Viewer  
Update service bindings. | `networkservices.serviceBindings.update` | Network Admin  
Delete service bindings. | `networkservices.serviceBindings.delete` | Network Admin  
  
### Service Directory service permissions

The Service Directory administrator must grant the permission `servicedirectory.services.bind` to the service account that is attempting to attach the service binding to the Service Directory service. This lets the service account use a Service Directory service, meaning that the account can reference a Service Directory service in a service binding.

### Permissions enforcement

IAM permission checks are performed when you configure Cloud Service Mesh. You must have the requisite permissions to create service bindings, and to associate service bindings with particular Service Directory services. If the correct permissions are in place, you can configure your mesh clients to learn about and send traffic to a Service Directory service.

Because these checks happen at configuration time, removing the bind permission on an existing Service Directory service does not disrupt traffic flows. After a service binding is established, removing a permission does not affect whether a mesh client can learn about and send traffic to a Service Directory service.

To stop a mesh client from communicating with a Service Directory service, you can use other mechanisms:

  1. Restrict access to the Service Directory service. For example, you can use firewall rules.
  2. Delete the Service Directory service.
  3. Update your Cloud Service Mesh configuration, for example, by removing the service binding from the backend service.



## Best practices

  * Although Service Directory allows registration of endpoints using the Service Directory API, we recommend using integrations that automatically register to Service Directory when they are available. For more information on these integrations, see [Service Directory for GKE overview](https://docs.cloud.google.com/service-directory/docs/sd-gke-overview) and [Service Directory and Cloud Load Balancing overview](https://docs.cloud.google.com/service-directory/docs/sd-lb-overview).
  * We recommend that you use the same namespace and service for a particular logical service, even when that service is deployed across different regions.



## Use Service Directory for service discovery

The following diagram provides an overview of the end state of this setup procedure, including configuration, how different systems interact, and how a request is resolved to a service's endpoints. This example assumes that you already have a service registered with Service Directory.

[ ![Configuration details for using Service Directory for service discovery.](https://docs.cloud.google.com/static/service-mesh/v1.24/docs/images/service-discovery-endpoints.svg)](https://docs.cloud.google.com/static/service-mesh/v1.24/docs/images/service-discovery-endpoints.svg) Configuration details for using Service Directory for service discovery (click to enlarge)

Making a Service Directory service available to Cloud Service Mesh consists of the following steps.

  1. Create a new backend service in Cloud Service Mesh and don't create backends for the backend service.
  2. Create a global service binding for the Service Directory service.
  3. Bind the Service Directory service to this backend service. Optionally, set additional fields and policies on the backend service.

  4. Create a new routing configuration, or update an existing configuration, so that client requests can be routed to the new backend service.




You cannot set a health check on a backend service that references a service binding. The backend service also cannot have backends.

## Create the integration

Use the following instructions to integrate Cloud Service Mesh with Service Directory.

### Create a backend service

Use the following instructions to create a backend service in your Cloud Service Mesh deployment.

  1. Create a backend service to use with Service Directory services.
         
         gcloud compute backend-services create td-sd-demo-service \
          --global \
          --load-balancing-scheme=INTERNAL_SELF_MANAGED
         

  2. Create a service binding that references a Service Directory service.
         
         gcloud beta network-services service-bindings create my-sd-binding \
          --location global \
          --service-directory-region us-east1 \
          --service-directory-namespace my-namespace \
          --service-directory-service my-service
         

  3. Bind the service to the backend service.
         
         gcloud beta compute backend-services update td-sd-demo-service \
          --global \
          --service-bindings my-sd-binding
         




After you create the backend service and bind one or more Service Directory services, Cloud Service Mesh begins to track the endpoints that are associated with the Service Directory service. The endpoints are distinct IP:port pairs. To make this service routable, you need to configure routing.

### Configure routing

Use the following instructions to update your routing configuration.

###  Service routing APIs 

The following example assumes that you have a `Mesh` resource called `sidecar- mesh`. You create an `HTTPRoute` resource with hostnames set to `myservice.example.com` and destination set to the backend service `td-sd-demo-service` that you created in the previous section.

  1. Create the `HTTPRoute` specification and save it a file called `httproute.yaml`.
         
         name: td-sd-demo-route
         hostnames:
         ‐ myservice.example.com
         meshes:
         ‐ projects/PROJECT_NUMBER/locations/global/meshes/sidecar-mesh
         rules:
         ‐ action:
           destinations:
           ‐ serviceName: "projects/PROJECT_NUMBER/locations/global/backendServices/td-sd-demo-service"
         

  2. Import the `HTTPRoute` specification.
         
         gcloud network-services httproutes import td-sd-demo-route \
           --source=httproute.yaml \
           --location=global
         




###  Load balacing APIs 

The following example assumes that you already have a basic routing configuration, including a URL map that is called `my-url-map`.

  * First, you create a path matcher for this URL map. The path matcher is uncomplicated. When it's used, it resolves to `td-sd-demo-service`, which you created in the previous step.
  * Next, you add a host rule to the URL map. This host rule causes the path matcher to be used if a request specifies the hostname `myservice.example.com`.


  1. Create a simple path matcher that points to your backend service.
         
         gcloud compute url-maps add-path-matcher my-url-map \
          --global \
          --default-service td-sd-demo-service \
          --path-matcher-name my-path-matcher
         

  2. Map the backend service to a new host rule in the existing URL map.
         
         gcloud compute url-maps add-host-rule my-url-map \
          --global \
          --path-matcher-name=my-path-matcher \
          --hosts=myservice.example.com
         




### Attach the same service from multiple regions

Cloud Service Mesh lets you bind multiple Service Directory services to the same backend service. For example, you might have two Service Directory services, each identical, but with endpoints in different Google Cloud regions or zones. In other words, a single global backend service could have two global service bindings, with one pointing to a service in `us-east1` and the other pointing to a service in `us-west1`.

  1. Create a backend service for your imported Service Directory service.
         
         gcloud compute backend-services create td-sd-demo-service \
          --global \
          --load-balancing-scheme=INTERNAL_SELF_MANAGED
         

  2. Create a service binding to Service Directory service in `us-east1`.
         
         gcloud beta network-services service-bindings create us-east1-binding \
          --location global \
          --service-directory-region us-east1 \
          --service-directory-namespace my-namespace \
          --service-directory-service my-service \
         

  3. Create a service binding to Service Directory service in `us-west1`.
         
         gcloud beta network-services service-bindings create us-west1-binding \
          --location global
          --service-directory-region us-west1 \
          --service-directory-namespace my-namespace \
          --service-directory-service my-service \
         

  4. Bind the `us-east1` and the `us-west1` services to the backend service.
         
         gcloud compute backend-services update td-sd-demo-service \
           --global \
           --service-bindings us-east1-binding,us-west1-binding
         




### Apply advanced traffic management policies

In the preceding section, you used Cloud Service Mesh to set up routing policies against an existing Service Directory service. You can apply this pattern to more advanced traffic management scenarios.

Consider this scenario. You have an existing test service that is outside of the Cloud Service Mesh mesh. The test service is a backend for an internal Application Load Balancer. You want to replay some production traffic originating in the Cloud Service Mesh mesh to this external service. Cloud Service Mesh can do this using `RequestMirrorPolicy`, which can send traffic to another backend service when the request is processed. This process is also called _shadowing a request_ , and it lets you examine traffic without affecting your production services.

You can enable Envoy clients to shadow traffic to a test service by manually adding or removing the test service endpoint to the Cloud Service Mesh mesh. However, the process is simpler when you use the Service Directory integration.

[ ![Using Service Directory for service discovery with mirroring.](https://docs.cloud.google.com/static/service-mesh/v1.24/docs/images/service-discovery-mirroring.svg)](https://docs.cloud.google.com/static/service-mesh/v1.24/docs/images/service-discovery-mirroring.svg) Using Service Directory for service discovery with mirroring(click to enlarge)

In this example, you start by pointing a backend service to the Service Directory registration for the payments test service. Then you add a request mirror policy to the service in Cloud Service Mesh.

  1. Create a backend service for the request mirror policy.
         
         gcloud compute backend-services create payments-test-bes \
          --global \
          --load-balancing-scheme=INTERNAL_SELF_MANAGED
         

  2. Create a service binding that references a Service Directory service.
         
         gcloud beta network-services service-bindings create my-sd-binding \
          --location global \
          --service-directory-region us-east1 \
          --service-directory-namespace my-namespace \
          --service-directory-service my-service \
         

  3. Bind the Service Directory service to the test backend service.
         
         gcloud beta compute backend-services update payments-test-bes \
          --global \
          --service-bindings my-sd-binding
         

  4. Edit the URL map to mirror requests to the test service.
         
         gcloud compute url-maps edit my-url-map \
           --region=global
         

  5. After the URL map configuration is loaded into an editor, add the request mirror policy to mirror requests to the existing Service Directory service.
         
         defaultService: my-project/global/default-service
            hostRules:
             - hosts:
               - '*'
               pathMatcher: path-matcher-one
            pathMatchers:
             - defaultService: my-project/global/default-service
              name: path-matcher-one
              pathRules:
               - paths:
                 - /payments/
                 service: my-project/global/default-service
                 requestMirrorPolicy:
                   backendService: myproject/global/payments-test-bes
         




## Remove a service binding from a backend service

To remove a service binding from the backend service, pass a new list of service bindings to the `gcloud compute backend-services update` command. The new list must not include the service binding that you want to delete:

  * To remove all service bindings, set the `--no-service-bindings` flag.
  * To remove one or more service bindings: pass a new list of service bindings that omits the service bindings that you want to remove to the `--service-bindings` flag.

**Note:** The `update` command only updates the values of flags that are specified in the command.

### Add or remove service bindings

The `bind-service` command adds a service binding to the set of existing service bindings on the backend service.
    
    
    gcloud compute backend-services bind-service BACKEND_SERVICE_NAME \
      --service-binding-name SERVICE_BINDING_URL \
      --global
    

The `unbind-service` command removes a service binding from the set of existing service bindings on the backend service.
    
    
    gcloud compute backend-services unbind-service BACKEND_SERVICE_NAME \
      --service-binding-name SERVICE_BINDING_URL \
      --global
    

The commands `bind-service` and `unbind-service` are Google Cloud CLI constructs. They are not API-level constructs.

## What's next

  * For information about observability with this integration, see [Observability and debugging with Service Directory](https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/service-directory-observability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
