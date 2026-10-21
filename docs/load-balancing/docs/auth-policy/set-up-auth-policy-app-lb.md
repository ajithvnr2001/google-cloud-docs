---
url: https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb/
title: Set up authorization policies for Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:37.454324+00:00
---

# Set up authorization policies for Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/auth-policy/set-up-auth-policy-app-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up authorization policies for Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up authorization policies for Application Load Balancers.

## Before you begin

  * Familiarize yourself with the [Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).
  * [Enable the following APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api#enabling_an_api):

    * Network Security API
    * Network Services API



### Set up the load balancer

If you haven't created a load balancer, see the following pages to set up your preferred Application Load Balancer:

  * To create a global external Application Load Balancer, see [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).


  * To create a regional external Application Load Balancer, see [Set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb).

  * To create a regional internal Application Load Balancer, see [Set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal).



  * To create a cross-region internal Application Load Balancer, see [Set up a cross-region internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal).



## Create an authorization policy

To create an [authorization policy](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies), you create a YAML file defining the target and the rules, and then import the file using the `gcloud network-security authz-policies` command.

This section provides instructions for creating authorization policies attached to the forwarding rule of Application Load Balancers.

To learn more about how to create an authorization policy for an Agent Gateway that delegates authorization using Service Extensions, see [Delegate authorization with Service Extensions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/delegate-authorization).

To learn more about how to create an authorization policy for a Secure Web Proxy, see [Set up authorization policies for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies).

### Authorization policy to deny requests

This section provides authorization policy examples that denies requests based on certain request attributes.

#### Deny requests based on IP address ranges

This section provides an authorization policy example that denies requests based on requests originating from [specific IP address ranges](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies#ipblock).

###  Global and cross-region 

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-deny.yaml` file for the forwarding rule `LB_FORWARDING_RULE` in the `global` location. The policy denies clients with IP addresses in the `10.0.0.0/24` range to access the `/api/payments` URL path.
         
         cat >authz-policy-deny.yaml <<EOF
         name: my-authz-policy-deny
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules/LB_FORWARDING_RULE"
         httpRules:
         - from:
             sources:
             - ipBlocks:
               - prefix: "10.0.0.0"
                 length: "24"
         - to:
             operations:
             - paths:
               - prefix: "/api/payments"
         action: DENY
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For global external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud network-security authz-policies import my-authz-policy-deny \
             --source=authz-policy-deny.yaml \
             --location=global
         




###  Regional 

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-deny.yaml` file for the forwarding rule `LB_FORWARDING_RULE` in a Google Cloud region. The policy denies clients with IP addresses in the `10.0.0.0/24` range to access the `/api/payments` URL path.
         
         cat >authz-policy-deny.yaml <<EOF
         name: my-authz-policy-deny
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         httpRules:
         - from:
             sources:
             - ipBlocks:
               - prefix: "10.0.0.0"
                 length: "24"
         - to:
             operations:
             - paths:
               - prefix: "/api/payments"
         action: DENY
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For regional internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud network-security authz-policies import my-authz-policy-deny \
             --source=authz-policy-deny.yaml \
             --location=global
         




#### Deny requests based on client certificate principals

This section provides an authorization policy example that denies requests based on [client certificate principals](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview#authz-policy-principals).

###  Global and cross-region 

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-deny.yaml` file for the forwarding rule `LB_FORWARDING_RULE` in the `global` location.The policy denies access to the `/api/payments` URL path to clients that have `www.example.com` in their client certificate DNS name SANs.
         
         cat >authz-policy-deny.yaml <<EOF
         name: my-authz-policy-deny
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules/LB_FORWARDING_RULE"
         httpRules:
         - from:
             sources:
             - principals:
               - principalSelector: CLIENT_CERT_DNS_NAME_SAN
                 principal:
                   exact: "www.example.com"
           to:
             operations:
             - paths:
               - prefix: "/api/payments"
         action: DENY
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For global external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud network-security authz-policies import my-authz-policy-deny \
             --source=authz-policy-deny.yaml \
             --location=global
         




###  Regional 

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-deny.yaml` file for the forwarding rule `LB_FORWARDING_RULE` in a Google Cloud region. The policy denies access to the `/api/payments` URL path to clients that have `www.example.com` in their client certificate DNS name SANs.
         
         cat >authz-policy-deny.yaml <<EOF
         name: my-authz-policy-deny
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - from:
             sources:
             - principals:
               - principalSelector: CLIENT_CERT_DNS_NAME_SAN
                 principal:
                   exact: "www.example.com"
           to:
             operations:
             - paths:
               - prefix: "/api/payments"
         action: DENY
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For regional internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: your Google Cloud region.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-deny \
             --source=authz-policy-deny.yaml \
             --location=LOCATION
         




### Authorization policy to allow requests

This section provides an authorization policy example that allows requests originating from [specific IP address ranges](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies#ipblock).

###  Global and cross-region 

If you're using a global external Application Load Balancer or a cross-region internal Application Load Balancer, follow these steps to create an authorization policy:

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-allow.yaml` file for the forwarding rule `LB_FORWARDING_RULE` in the `global` location. The policy allows clients with IP addresses in the `10.0.0.0/24` range to access the `/api/payments` URL path.
         
         cat >authz-policy-allow.yaml <<EOF
         name: my-authz-policy-allow
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules/LB_FORWARDING_RULE"
         httpRules:
         - from:
             sources:
             - ipBlocks:
               - prefix: "10.0.0.0"
                 length: "24"
           to:
             operations:
             - paths:
               - exact: "/api/payments"
         action: ALLOW
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For global external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud network-security authz-policies import my-authz-policy-allow \
             --source=authz-policy-allow.yaml \
             --location=global
         




###  Regional 

If you're using a regional external Application Load Balancer or a regional internal Application Load Balancer, follow these steps to create and import an authorization policy:

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-allow.yaml` file for the forwarding rule `LB_FORWARDING_RULE` in a specific Google Cloud region. The policy allows clients with IP addresses in the `10.0.0.0/24` range to access the `/api/payments` URL path.
         
         cat >authz-policy-allow.yaml <<EOF
         name: my-authz-policy-allow
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - from:
             sources:
             - ipBlocks:
               - prefix: "10.0.0.0"
                 length: "24"
           to:
             operations:
             - paths:
               - exact: "/api/payments"
         action: ALLOW
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For regional internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: your Google Cloud region.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-allow \
             --source=authz-policy-allow.yaml \
             --location=LOCATION
         




### Authorization policy based on service accounts or tags

You can apply an [authorization policy based on service accounts or secure tags](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview#authz-policy-tags-and-sa) attached to various Google Cloud resources.

This example assumes that you have done the following:

  * [created a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and [attached it to a Google Cloud resource](https://docs.cloud.google.com/iam/docs/attach-service-accounts).

  * [created a secure tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) and attached it to a Google Cloud resource as a key-value pair. When you create a tag, set its `--purpose` flag to `GCE_FIREWALL`. Authorization policies require the `GCE_FIREWALL` purpose to apply the tag.




###  Service account 

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-deny.yaml` file for the forwarding rule `LB_FORWARDING_RULE` of a regional internal Application Load Balancer. The policy is configured to deny requests from a Google Cloud resource, such as a Compute Engine VM, with the service account `my-sa-123@PROJECT_ID.iam.gserviceaccount.com` to reach the `/api/payments` path.
         
         cat >authz-policy-deny.yaml <<EOF
         name: my-authz-policy-deny
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - from:
             sources:
             - resources:
                - iamServiceAccount:
                    exact: "my-sa-123@PROJECT_ID.iam.gserviceaccount.com"
           to:
             operations:
             - paths:
               - prefix: "/api/payments"
         action: DENY
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional internal Application Load Balancers and cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: your Google Cloud region.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-deny \
             --source=authz-policy-deny.yaml \
             --location=LOCATION
         

Replace `LOCATION` with your Google Cloud region.




###  Tag 

  1. Define the authorization policy in a YAML file.

The following example creates an `authz-policy-allow.yaml` file for the forwarding rule `LB_FORWARDING_RULE` of a regional internal Application Load Balancer. The policy only allows requests that originate from a Google Cloud resource, such as a Compute Engine VM, with a secure tag value `TAG_VALUE_PERMANENT_ID` to access the `/api/payments` URL path.
         
         cat >authz-policy-allow.yaml <<EOF
         name: my-authz-policy-allow
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - from:
           sources:
             resources:
             - tagValueIdSet:
               - ids: "TAG_VALUE_PERMANENT_ID"
           to:
             operations:
             - paths:
               - exact: "/api/payments"
         action: ALLOW
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional internal Application Load Balancers and cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: your Google Cloud region.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
     * `TAG_VALUE_PERMANENT_ID`: the [permanent ID](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value) of a tag value.
  2. Create the authorization policy by importing the authorization policy YAML file using the [gcloud network-security authz-policies import command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-allow \
             --source=authz-policy-allow.yaml \
             --location=LOCATION
         

Replace the following:

     * `LOCATION`: your Google Cloud region.



### Authorization policy to delegate authorization decisions

The examples in this section create an authorization policy that delegate authorization decisions to the following services through Service Extensions:

  * User-managed service 
    * a Google Cloud backend service or an FQDN-based service
  * Google-managed service 
    * Model Armor
    * Identity-Aware Proxy



#### Delegate authorization decision to a user-managed service

You can configure an authorization policy to delegate the authorization decision to a user-managed service through Service Extensions, specifically an authorization extension.

  * For global and cross-region load balancers, the authorization extension can run on a user-managed Google Cloud backend service.

  * For regional load balancers, the authorization extension can run on both a user-managed Google Cloud backend service and an FQDN-based service.




This example setup assumes that you have created a user-managed Google Cloud backend service, also referred to as a callout backend service, named `authz-service`. To learn more about how to create one, see [Configure a user-managed callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service).

For an FQDN-based service, this example setup assumes that the custom service is deployed in your own VPC, supports the `ext_authz` protocol, and is accessible by the fully qualified domain name `mycustomauthz.internal.net`.

**Note:** When you point an authorization extension to a domain (FQDN), the load balancer uses the HTTP/2 protocol with TLS encryption to communicate with endpoints on port 443. However, even though the traffic is encrypted, the load balancer does not validate the server certificate, which means that it accepts any certificate that the server provides, even if it's expired, self-signed, or meant for a different domain. To ensure that the load balancer only communicates with trusted services, make sure that the FQDN resolves to an IP address within your VPC environment.

###  Global and cross-region 

If you're using a global external Application Load Balancer or a cross-region internal Application Load Balancer, follow these steps to delegate the authorization decision to user-managed service.

  1. Define the authorization extension in a YAML file. The authorization extension runs on a backend service (`authz-service`) and supports the `ext_authz` protocol.
         
         cat >authz-extension.yaml <<EOF
         name: my-authz-ext
         authority: ext11.com
         loadBalancingScheme: LB_SCHEME
         service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/authz-service
         forwardHeaders:
           - Authorization
         failOpen: false
         timeout: "0.1s"
         wireFormat: EXT_AUTHZ_GRPC
         EOF
         

  2. Create the authorization extension by importing the authorization extension YAML file using the [`gcloud service-extensions authz-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/authz-extensions/import).
         
         gcloud service-extensions authz-extensions import my-authz-ext \
             --source=authz-extension.yaml \
             --location=global
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For global external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
  3. Define the authorization policy in a YAML file. The authorization policy delegates authorization to the authorization extension in the `customProvider` field.

The policy calls the `my-authz-ext` authorization extension for all traffic to the `example.com/api/payments` URL path when the request contains a non-empty `Authorization` header.
         
         cat >authz-policy-custom.yaml <<EOF
         name: my-authz-policy-custom
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules/LB_FORWARDING_RULE"
         httpRules:
         - to:
             operations:
             - hosts:
               - exact: "example.com"
             - paths:
               - exact: "/api/payments"
           when: 'request.headers["Authorization"] != ""'
         action: CUSTOM
         customProvider:
           authzExtension:
             resources:
             - "projects/PROJECT_ID/locations/global/authzExtensions/my-authz-ext"
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For global external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  4. Create the authorization policy by importing the authorization policy YAML file using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud network-security authz-policies import my-authz-policy-custom \
             --source=authz-policy-custom.yaml \
             --location=global
         




###  Regional 

If you're using a regional external Application Load Balancer or a regional internal Application Load Balancer, follow these steps to delegate the authorization decision to a user-managed service.

  1. Define the authorization extension in a YAML file. The authorization extension can run on a backend service or an FQDN-based service.
         
         cat >authz-extension.yaml <<EOF
         name: my-authz-ext
         authority: ext11.com
         loadBalancingScheme: LB_SCHEME
         service: BACKEND_SERVICE_URI_OR_FQDN
         forwardHeaders:
           - Authorization
         failOpen: false
         timeout: "0.1s"
         wireFormat: EXT_AUTHZ_GRPC
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For regional internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `BACKEND_SERVICE_URI_OR_FQDN`: the service can be either of the following: 
       * a regional backend service resource URI of the form `https://www.googleapis.com/compute/v1/projects/`PROJECT_ID`/regions/LOCATION/backendServices/authz-service`.
       * a fully-qualified domain name (for example, `mycustomauthz.extension.net`) that can be resolved by Cloud DNS.
  2. Create the authorization extension by importing the authorization extension YAML file using the [`gcloud service-extensions authz-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/authz-extensions/import).
         
         gcloud service-extensions authz-extensions import my-authz-ext \
             --source=authz-extension.yaml \
             --location=LOCATION
         

Replace LOCATION with the Google Cloud region where the callout backend service is configured.

  3. Define the authorization policy in a YAML file. The authorization policy delegates authorization to the authorization extension in the `customProvider` field.

The policy calls the `my-authz-ext` authorization extension for all traffic to the `example.com/api/payments` URL path when the request contains a non-empty `Authorization` header.
         
         cat >authz-policy-custom.yaml <<EOF
         name: my-authz-policy-custom
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - to:
             operations:
             - paths:
               - exact: "/api/payments"
           when: 'request.headers["Authorization"] != ""'
         action: CUSTOM
         customProvider:
           authzExtension:
             resources:
             - "projects/PROJECT_ID/locations/LOCATION/authzExtensions/my-authz-ext"
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For regional internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the Google Cloud region.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  4. Create the authorization policy by importing the authorization policy YAML file using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-custom \
             --source=authz-policy-custom.yaml \
             --location=LOCATION
         

Replace LOCATION with the Google Cloud region where the load balancer is configured.




For more information about authorization extensions, see [Configure an authorization extension](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions).

#### Delegate authorization decision to Model Armor

You can configure an authorization policy to delegate the authorization decision to Model Armor.

Before you begin, [create a Model Armor template](https://docs.cloud.google.com/model-armor/manage-templates#create-ma-template). In this example setup, the authorization policy points to an authorization extension, which in turn points to Model Armor.

If you're using a regional external Application Load Balancer or a regional internal Application Load Balancer, follow these steps to delegate the authorization decision to Model Armor.

###  Regional 

  1. Define the authorization extension in a YAML file. The authorization extension points to Model Armor request and response templates.
         
         cat >authz-extension.yaml <<EOF
         name: my-authz-extension
         loadBalancingScheme: INTERNAL_MANAGED
         service: modelarmor.LOCATION.rep.googleapis.com
         metadata:
           model_armor_settings: '[
             {
             "response_template_id": "projects/PROJECT_ID/locations/LOCATION/templates/RESPONSE_TEMPLATE_ID",
             "request_template_id": "projects/PROJECT_ID/locations/LOCATION/templates/REQUEST_TEMPLATE_ID"
             }
           ]'
         failOpen: true
         EOF
         

Replace the following:

     * LOCATION: the [location](https://docs.cloud.google.com/model-armor/locations) of the template
     * PROJECT_ID: the ID of the project that the template belongs to
     * RESPONSE_TEMPLATE_ID: ID of the response template
     * REQUEST_TEMPLATE_ID: the ID of the request template
  2. Create the authorization extension by importing the authorization extension YAML file using the [`gcloud beta service-extensions authz-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-extensions/authz-extensions/import).
         
         gcloud beta service-extensions authz-extensions import my-authz-ext \
           --source=authz-extension.yaml \
           --location=LOCATION
         

Replace LOCATION with the Google Cloud region where the load balancer is located.

  3. Define the authorization policy in a YAML file. The authorization policy delegates authorization to the authorization extension in the `customProvider` field.

The value of the `policyProfile` is `CONTENT_AUTHZ`.
         
         cat >authz-policy-custom.yaml <<EOF
         name: my-authz-policy-custom
         target:
           loadBalancingScheme: INTERNAL_MANAGED
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         policyProfile: CONTENT_AUTHZ
         action: CUSTOM
         customProvider:
           authzExtension:
             resources:
             - "projects/PROJECT_ID/locations/LOCATION/authzExtensions/my-authz-ext"
         EOF
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the Google Cloud region.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  4. Create the authorization policy by importing the authorization policy YAML file using the [`gcloud beta network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/authorization-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-custom \
           --source=authz-policy-custom.yaml \
           --location=LOCATION
         

Replace LOCATION with the Google Cloud region where the load balancer is configured.




#### Delegate authorization decision to Identity-Aware Proxy

For global external Application Load Balancers and cross-region internal Application Load Balancers, you cannot delegate the authorization decision to IAP through an authorization extension. For these load balancers, you can delegate authorization decision to IAP through the `customProvider` field on the authorization policy resource.

For regional external Application Load Balancers and regional internal Application Load Balancers, you can configure an authorization policy to delegate the authorization decision to IAP through an authorization extension.

###  Global and cross-region 

In the following example, all authorization decisions are delegated to IAP for all requests originating from the `10.0.0.0/24` IP address block. If requests originate from any IP address outside of `10.0.0.0/24`, they don't match this policy and aren't evaluated by IAP under this specific rule.

  1. Define the authorization policy in a YAML file. The authorization policy delegates authorization to IAP through the `customProvider` field.
         
         cat >authz-policy-iap.yaml <<EOF
         name: my-authz-policy-custom
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules/LB_FORWARDING_RULE"
         httpRules:
           - from:
               sources:
               - ipBlock:
                 - prefix: "10.0.0.0"
                   length: 24
         action: CUSTOM
         customProvider:
           cloudIap: {}
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For global external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For cross-region internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  2. Create the authorization policy by importing the authorization policy YAML file using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud network-security authz-policies import my-authz-policy-custom \
             --source=authz-policy-iap.yaml \
             --location=global
         




###  Regional 

If you're using a regional external Application Load Balancer or a regional internal Application Load Balancer, follow these steps to delegate the authorization decision to IAP using an authorization extension.

  1. Define the authorization extension in a YAML file. The authorization extension points to IAP.
         
         cat >authz-extension.yaml <<EOF
         name: my-authz-ext
         loadBalancingScheme: LB_SCHEME
         service: iap.googleapis.com
         failOpen: false
         EOF
         

Replace the following:

     * LB_SCHEME: the load balancing scheme. For regional external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For regional internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
  2. Create the authorization extension by importing the authorization extension YAML file using the [`gcloud service-extensions authz-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/authz-extensions/import).
         
         gcloud service-extensions authz-extensions import my-authz-ext \
             --source=authz-extension.yaml \
             --location=LOCATION
         

Replace LOCATION with the Google Cloud region where the authorization extension is configured.

  3. Define the authorization policy in a YAML file. The authorization policy delegates authorization to the authorization extension in the `customProvider` field.
         
         cat >authz-policy-custom.yaml <<EOF
         name: my-authz-policy-custom
         target:
           loadBalancingScheme: LB_SCHEME
           resources:
           - "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/LB_FORWARDING_RULE"
         policyProfile: REQUEST_AUTHZ
         action: CUSTOM
         customProvider:
           authzExtension:
             resources:
             - "projects/PROJECT_ID/locations/LOCATION/authzExtensions/my-authz-ext"
         EOF
         

Replace the following:

     * `LB_SCHEME`: the load balancing scheme. For regional external Application Load Balancers, set the scheme to `EXTERNAL_MANAGED`. For regional internal Application Load Balancers, set the scheme to `INTERNAL_MANAGED`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the Google Cloud region.
     * `LB_FORWARDING_RULE`: the name of the load balancer's forwarding rule.
  4. Create the authorization policy by importing the authorization policy YAML file using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authorization-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-custom \
             --source=authz-policy-custom.yaml \
             --location=LOCATION
         

Replace LOCATION with the Google Cloud region where the load balancer is configured.




## Understand authorization policy logs in Cloud Logging

To understand how authorization policies are logged when a request is allowed or denied, review the following sections.

### Request matches neither the `ALLOW` nor `DENY` policies

When a request matches neither the `ALLOW` nor `DENY` policies, the `DENY` policy permits the request and logs it as `allowed_as_no_deny_policies_matched_request`. Conversely, the `ALLOW` policy rejects the request and logs it as `denied_as_no_allow_policies_matched_request`. Because one of the policies denies the request, the request is denied.

  * If you're using a global external Application Load Balancer, `statusDetails` is set to `denied_by_authz_policy` in the log. See the following example:
        
        {
            httpRequest: {8}
            insertId: "example-id"
            jsonPayload: {
              @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
              authzPolicyInfo: {
                policies: [
                  0: {
                    details: "allowed_as_no_deny_policies_matched_request"
                    result: "ALLOWED"
                  }
                  1: {
                    details: "denied_as_no_allow_policies_matched_request"
                    result: "DENIED"
                  }
                ]
                result: "DENIED"
              }
              backendTargetProjectNumber: "projects/12345567"
              remoteIp: "00.100.11.104"
              statusDetails: "denied_by_authz_policy"
            }
            logName: "projects/example-project/logs/requests"
            receiveTimestamp: "2024-08-28T15:33:56.046651035Z"
            resource: {2}
            severity: "WARNING"
            spanId: "3e1a09a8e5e3e14d"
            timestamp: "2024-08-28T15:33:55.355042Z"
            trace: "projects/example-project/traces/8c8b3dbf9a19c85954d0fa2d958ca509"
          }
        

  * If you're using a regional internal Application Load Balancer, regional external Application Load Balancer, or cross-region internal Application Load Balancer, `proxyStatus` is set to `error=\"http_request_error\"; details=\"denied_by_authz_policy\"` in the log. See the following example:
        
        {
            httpRequest: {8}
            insertId: "example-id"
            jsonPayload: {
              @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
              authzPolicyInfo: {
                policies: [
                  0: {
                    details: "allowed_as_no_deny_policies_matched_request"
                    result: "ALLOWED"
                  }
                  1: {
                    details: "denied_as_no_allow_policies_matched_request"
                    result: "DENIED"
                  }
                ]
                result: "DENIED"
              }
              backendTargetProjectNumber: "projects/12345567"
              remoteIp: "00.100.11.104"
              proxyStatus: "error=\"http_request_error\"; details=\"denied_by_authz_policy\""
            }
            logName: "projects/example-project/logs/requests"
            receiveTimestamp: "2024-08-28T15:33:56.046651035Z"
            resource: {2}
            severity: "WARNING"
            spanId: "3e1a09a8e5e3e14d"
            timestamp: "2024-08-28T15:33:55.355042Z"
            trace: "projects/example-project/traces/8c8b3dbf9a19c85954d0fa2d958ca509"
          }
        




### Request matches the `DENY` policy

When a request matches the `DENY` policy, it is denied and the policy that denied the request is logged.

  * If you're using a global external Application Load Balancer, `statusDetails` is set to `denied_by_authz_policy` in the log and the name of the policy that denied the request is logged in `policies`. See the following example:
        
        {
            httpRequest: {8}
            insertId: "example-id"
            jsonPayload: {
              @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
              authzPolicyInfo: {
                policies: [
                  0: {
                    details: "name: "projects/12345567/locations/global/authzPolicies/deny-authz-policy-test""
                    result: "DENIED"
                  }
                ]
                result: "DENIED"
              }
              backendTargetProjectNumber: "projects/12345567"
              cacheDecision: [2]
              remoteIp: "00.100.11.104"
              statusDetails: "denied_by_authz_policy"
            }
            logName: "projects/example-project/logs/requests"
            receiveTimestamp: "2024-08-28T15:33:56.046651035Z"
            resource: {2}
            severity: "WARNING"
            spanId: "3e1a09a8e5e3e14d"
            timestamp: "2024-08-28T15:33:55.355042Z"
            trace: "projects/example-project/traces/8c8b3dbf9a19c85954d0fa2d958ca509"
          }
        

  * If you're using a regional internal Application Load Balancer, regional external Application Load Balancer, or cross-region internal Application Load Balancer, `proxyStatus` is set to `error=\"http_request_error\"; details=\"denied_by_authz_policy\"` and the name of the policy is logged in `policies`. See the following example:
        
        {
            httpRequest: {8}
            insertId: "example-id"
            jsonPayload: {
              @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
              authzPolicyInfo: {
                policies: [
                  0: {
                    details: "name: "projects/12345567/locations/$REGION/authzPolicies/deny-authz-policy-test""
                    result: "DENIED"
                  }
                ]
                result: "DENIED"
              }
              backendTargetProjectNumber: "projects/12345567"
              remoteIp: "00.100.11.104"
              proxyStatus: "error=\"http_request_error\"; details=\"denied_by_authz_policy\""
            }
            logName: "projects/example-project/logs/requests"
            receiveTimestamp: "2024-08-28T15:33:56.046651035Z"
            resource: {2}
            severity: "WARNING"
            spanId: "3e1a09a8e5e3e14d"
            timestamp: "2024-08-28T15:33:55.355042Z"
            trace: "projects/example-project/traces/8c8b3dbf9a19c85954d0fa2d958ca509"
          }
        




### Request does not match the `DENY` policy, but matches the `ALLOW` policy

When a request doesn't match the `DENY` policy, but matches with the `ALLOW` policy, the request is allowed. In the log, this action is logged as `allowed_as_no_deny_policies_matched_request` for the `DENY` policy. The policy that allowed the request is also logged.

  * If you're using a global external Application Load Balancer, there is no `statusDetails` in the log. The policy that allowed the request is also logged in `policies`. See the following example:
        
        {
            httpRequest: {8}
            insertId: "example-id"
            jsonPayload: {
              @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
              authzPolicyInfo: {
                policies: [
                  0: {
                    details: "allowed_as_no_deny_policies_matched_request"
                    result: "ALLOWED"
                  }
                  1: {
                    details: "name: "projects/12345567/locations/global/authzPolicies/allow-authz-policy-test""
                    result: "ALLOWED"
                  }
                ]
                result: "ALLOWED"
              }
              backendTargetProjectNumber: "projects/12345567"
              cacheDecision: [2]
              remoteIp: "00.100.11.104"
            }
            logName: "projects/example-project/logs/requests"
            receiveTimestamp: "2024-08-28T15:33:56.046651035Z"
            resource: {2}
            severity: "WARNING"
            spanId: "3e1a09a8e5e3e14d"
            timestamp: "2024-08-28T15:33:55.355042Z"
            trace: "projects/example-project/traces/8c8b3dbf9a19c85954d0fa2d958ca509"
          }
        

  * If you're using a regional internal Application Load Balancer, regional external Application Load Balancer, or cross-region internal Application Load Balancer, there is no `proxyStatus` field in the log. The policy that allowed the request is also logged in `policies`. See the following example:
        
        {
            httpRequest: {8}
            insertId: "example-id"
            jsonPayload: {
              @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
              authzPolicyInfo: {
                policies: [
                  0: {
                    details: "allowed_as_no_deny_policies_matched_request"
                    result: "ALLOWED"
                  }
                  1: {
                    details: "name: "projects/12345567/locations/$REGION/authzPolicies/allow-authz-policy-test""
                    result: "ALLOWED"
                  }
                ]
                result: "ALLOWED"
              }
              backendTargetProjectNumber: "projects/12345567"
              cacheDecision: [2]
              remoteIp: "00.100.11.104"
            }
            logName: "projects/example-project/logs/requests"
            receiveTimestamp: "2024-08-28T15:33:56.046651035Z"
            resource: {2}
            severity: "WARNING"
            spanId: "3e1a09a8e5e3e14d"
            timestamp: "2024-08-28T15:33:55.355042Z"
            trace: "projects/example-project/traces/8c8b3dbf9a19c85954d0fa2d958ca509"
          }
        




## What's next

  * [Configure an authorization extension](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions)

  * [Delegate authorization to IAP and IAM](https://docs.cloud.google.com/iap/docs/auth-policies)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
