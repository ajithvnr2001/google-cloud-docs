---
url: https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions/
title: Configure an authorization extension \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:36.807232+00:00
---

# Configure an authorization extension  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Configure an authorization extension Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions enables Application Load Balancers to send callouts to backend services to insert custom processing in the processing path. [Authorization extensions](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#authorization-extensions) run in the request processing path when the load balancer receives request headers and after the [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) chooses the backend service. This page describes how to configure authorization extensions to use a custom authorization engine defined in an [authorization policy](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

For an overview about Application Load Balancer extensions, see [Cloud Load Balancing extensions overview](https://docs.cloud.google.com/service-extensions/docs/callouts-overview).

## Introduction

Cloud Load Balancing lets you configure authorization policies that enforce access control on traffic entering load balancers. Sometimes, complex authorization decisions cannot be readily expressed using an authorization policy.

You can configure authorization policies with authorization extensions to delegate authorization decisions to custom authorization engines. In the data path, authorization extensions are executed after route extensions but before traffic extensions. For more information about authorization policies, see [Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

For each authorization request, the proxy forwards the request headers to the extension. Depending on the response from the provider, the proxy either forwards or rejects the request.

In [Preview](https://cloud.google.com/products#product-launch-stages), for regional external Application Load Balancers and regional internal Application Load Balancers, you can configure authorization extensions separately for request authorization policies and content authorization policies. Extensions that are based on request authorization policies are configured to run before those based on content authorization policies.

For information about the limits related to Application Load Balancer extensions, see the [Quotas and limits](https://docs.cloud.google.com/service-extensions/docs/quotas#for_callouts) page.

**Important:** You can attach only one authorization extension to a forwarding rule.

## Configure a basic authorization extension

The following example shows how to configure an authorization extension, `my-authz-ext`, with an authorization policy to delegate authorization decisions for a global external Application Load Balancer.

###  gcloud 

  1. Create the required resources as described in [Configure a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service).

For this exercise, create a global external Application Load Balancer. Name the service `authz-service` and the forwarding rule `fr1`.

  2. Configure the authorization extension.

     1. Define the extension in a YAML file that associates it with the backend service, `authz-service`. Use the sample values provided.
            
            cat >authz-extension.yaml <<EOF
                name: my-authz-ext
                authority: ext11.com
                loadBalancingScheme: EXTERNAL_MANAGED
                service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/authz-service
                forwardHeaders:
                  - Authorization
                failOpen: false
                timeout: "0.1s"
                forwardAttributes:
                - request.mcp_param
                - connection.client_cert_leaf
            EOF
            

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

For more information about the fields in the YAML file, see [ExtensionChain](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/ExtensionChain) in the API documentation.

The `forwardAttributes` field lets you specify the request, connection, and location attributes to forward to your authorization service. You can configure a maximum of 16 attributes for each extension. For more information about supported attributes, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

     2. Import the authorization extension. Use the [`gcloud service-extensions authz-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/authz-extensions/import) with the following sample values.
            
            gcloud service-extensions authz-extensions import my-authz-ext \
                --source=authz-extension.yaml \
                --location=global
            

  3. Configure an authorization policy with the extension.

     1. Define an authorization policy that associates the extension `my-authz-ext` with the forwarding rule `fr1`. Use the sample values provided. The `CUSTOM` action indicates that an extension is being used.
            
            cat >authz-policy.yaml <<EOF
                name: my-authz-policy
                target:
                  loadBalancingScheme: EXTERNAL_MANAGED
                  resources:
                    - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules/fr1"
                action: CUSTOM
                customProvider:
                  authzExtension:
                    resources:
                      - "projects/PROJECT_ID/locations/global/authzExtensions/my-authz-ext"
            EOF
            

     2. Import the authorization policy to the project. Use the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import) with the following sample values.
            
            gcloud network-security authz-policies import my-authz-policy \
                --source=authz-policy.yaml \
                --location=global
            




## Configure authorization extensions based on profiles

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can configure authorization extensions separately for request and content authorization policies.

### For a request authorization policy

The following example shows how to configure an authorization extension that applies a request authorization policy to a forwarding rule in `us-west1`. The policy requires traffic to pass mutual TLS authentication from a specific principal before being allowed to reach the destination, `example.com/mcp`.

### gcloud

  1. [Configure a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service) named `lb-request-authz-service` in `us-west1` with a forwarding rule named `fr2`.

For the service, [set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb).

  2. Configure the authorization extension.

     1. Define the extension in a YAML file that associates the extension with the backend service, `lb-request-authz-service`. Use the sample values provided.
            
            cat >lb-request-authz-extension.yaml <<EOF
            name: my-lb-request-authz-ext
            authority: ext11.com
            loadBalancingScheme: INTERNAL_MANAGED
            service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/lb-authz-request-service
            forwardHeaders:
              - Authorization
            failOpen: false
            timeout: "0.1s"
            wireFormat: EXT_AUTHZ_GRPC
            EOF
            

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

The extension must be in the same region as your backend service.

By default, all Service Extensions callouts use the Envoy External Processing or [`ext_proc`](https://github.com/envoyproxy/envoy/blob/main/api/envoy/service/ext_proc/v3/external_processor.proto) protocol. In the case of authorization callouts, the External Authorization or [`ext_authz`](https://github.com/envoyproxy/envoy/blob/main/api/envoy/service/auth/v3/external_auth.proto) protocol is also supported in [Preview](https://cloud.google.com/products#product-launch-stages). When the `wireFormat` option is set to `EXT_AUTHZ_GRPC`, the callout uses the `ext_authz` protocol. If the option isn't specified, the callout uses the `ext_proc` protocol.

For request authorization policies, the `wireFormat` value can be `EXT_AUTHZ_GRPC` so that the callout uses the `ext_authz` protocol although the `ext_proc` protocol is also supported.

By default, `failOpen` is set to `false`. If the extension times out or fails, request processing stops. This default option is preferred when prioritizing security or integrity over availability.

     2. Import the authorization extension. Use the [`gcloud beta service-extensions authz-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-extensions/authz-extensions/import) with the following sample values.
            
            gcloud beta service-extensions authz-extensions import my-lb-request-authz-ext \
                --source=lb-request-authz-extension.yaml \
                --location=us-west1
            

  3. In the same project, configure an authorization policy with the extension.

For any request to `example.com/mcp`, the policy requires mutual TLS authentication from a specific principal and further delegates the authorization decision to the authorization extension, `my-lb-authz-request-ext`.

     1. Define an authorization policy that associates the `my-lb-request-authz-ext` extension with the with the forwarding rule `fr2`. Use the sample values provided.
            
            cat >lb-request-authz-policy.yaml <<EOF
            name: my-lb-request-authz-policy
            target:
              resources:
                - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/fr2"
            policyProfile: REQUEST_AUTHZ
            httpRules:
            - to:
                operations:
                - hosts:
                  - exact: "example.com"
                - paths:
                  - prefix: "/mcp"
              from:
                sources:
                - principals:
                  - principal_selector: CLIENT_CERT_DNS_NAME_SANS
                    principal:
                      exact: "spiffe://p.global.123.workload.id.goog/ns/ns1/sa/hellomcp"
            action: CUSTOM
            customProvider:
              authzExtension:
                resources:
                  - "projects/PROJECT_ID/locations/us-west1/authzExtensions/my-lb-request-authz-ext"
            EOF
            

For request authorization policies, the value of `policyProfile` must be `REQUEST_AUTHZ`. This value indicates that the custom policy provider acts on requests to allow or deny traffic.

The `CUSTOM` action indicates that an extension is associated with the proxy.

For more information about an authorization policy resource, see the [`authzPolicy` reference documentation](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1beta1/projects.locations.authzPolicies#AuthzAction).

     2. Import the authorization policy to the project. Use the [`gcloud beta network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/authorization-policies/import) with the following sample values.
            
            gcloud beta network-security authz-policies import my-lb-request-authz-policy \
                --source=lb-request-authz-policy.yaml \
                --location=us-west1
            




### For a content authorization policy

The following example shows how to configure an authorization extension that applies a content authorization policy to a forwarding rule in `us-west1`. The policy requires a content sanitization service to perform deep inspection of your application payloads to allow or deny requests or mutate the requests and responses, as required.

### gcloud

  1. [Configure a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service) named `lb-content-authz-service` in `us-west1` with a forwarding rule named `fr3`.

For the service, [set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb).

Configure the extension server with the [`ext_proc`](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#ext_proc) protocol in `FULL_DUPLEX_STREAMED` [body processing mode](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#body-processing-modes) and supporting all events.

  2. Configure the authorization extension.

     1. Define the extension in a YAML file that associates the extension with the backend service, `lb-content-authz-service`. Use the sample values provided.
            
            cat >lb-content-authz-extension.yaml <<EOF
            name: my-lb-content-authz-ext
            authority: ext11.com
            loadBalancingScheme: INTERNAL_MANAGED
            service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/lb-authz-sdp-service
            failOpen: false
            timeout: "0.1s"
            EOF
            

For content authorization policies, the value of `policyProfile` must be `CONTENT_AUTHZ`.

For `CONTENT_AUTHZ` policies, the `wireFormat` value need not be set explicitly as `EXT_PROC_GRPC`. By default, the callout uses the `ext_proc` protocol.

     2. Import the authorization extension. Use the [`gcloud beta service-extensions authz-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-extensions/authz-extensions/import) with the following sample values.
            
            gcloud beta service-extensions authz-extensions import my-lb-content-authz-ext \
                --source=lb-content-authz-extension.yaml \
                --location=us-west1
            

  3. Configure an authorization policy with the extension.

     1. Define an authorization policy that associates the extension `my-lb-content-authz-ext` with the forwarding rule, `fr3`. Use the sample values provided.
            
            cat >lb-content-authz-policy.yaml <<EOF
            name: lb-content-authz-policy
            target:
              resources:
                - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/fr3"
            policyProfile: CONTENT_AUTHZ
            httpRules:
            - to:
                operations:
                - hosts:
                  - exact: "example.com"
                - paths:
                  - prefix: "/sensitive-stuff"
            action: CUSTOM
            customProvider:
              authzExtension:
                resources:
                  - "projects/PROJECT_ID/locations/us-west1/authzExtensions/my-lb-authz-content-ext"
            EOF
            

The value of `policyProfile` must be `CONTENT_AUTHZ`.

     2. Import the authorization policy to the project. Use the [`gcloud beta network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/authorization-policies/import) with the following sample values.
            
            gcloud beta network-security authz-policies import my-lb-content-authz-policy \
                --source=lb-content-authz-policy.yaml \
                --location=us-west1
            




## Limitations for authorization extensions

The following are some limitations of authorization extensions:

  * An authorization policy can have only one authorization extension.
  * A forwarding rule can be used with several authorization policies of which only one can be a custom authorization policy.



For limitations that are applicable to all extensions, see [Limitations for extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#limitations).

## What's next

  * View Python and Go samples of `ext_authz` and `ext_proc` servers in the Service Extensions [GitHub repository](https://github.com/GoogleCloudPlatform/service-extensions-samples/tree/main/callouts).
  * [Configure a route extension](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions)
  * [Configure a traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions)
  * [Manage extensions](https://docs.cloud.google.com/service-extensions/docs/manage-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
