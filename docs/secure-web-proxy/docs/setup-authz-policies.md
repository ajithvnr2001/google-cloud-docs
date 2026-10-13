---
url: https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies/
title: Set up authorization policies for Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:34.138956+00:00
---

# Set up authorization policies for Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Set up authorization policies for Secure Web Proxy Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to set up authorization policies for Secure Web Proxy.

## Before you begin

  * Review the [Secure Web Proxy overview](https://docs.cloud.google.com/secure-web-proxy/docs/overview) and [Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview) pages.

  * [Enable the following APIs](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#enable-apis):

    * Network Security API
    * Network Services API
    * Certificate Manager API
  * Make sure that you have the appropriate [roles and permissions](https://docs.cloud.google.com/secure-web-proxy/docs/roles-permissions).

  * You must have an active Secure Web Proxy instance deployed and associated with a `GatewaySecurityPolicy`. For more information, see [Deploy a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart).

  * To configure Secure Web Proxy authorization policies, you must [enable a TLS inspection policy](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).




## Create an authorization policy

This section explains how to create different types of authorization policies that are attached to a Secure Web Proxy instance.

To create an [authorization policy](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) for Secure Web Proxy, do the following:

  * Configure a YAML file that defines the target and rules. 
  * Import the file by using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authz-policies/import).



### Authorization policy based on mTLS identity

Secure Web Proxy supports enforcing security rules based on identities derived from mutual TLS (mTLS) certificates. Enforcing rules based on these identities is particularly useful in zero-trust environments, where the traffic between clients and the proxy is secured by mTLS. For more information, see [Authorization policy based on principals](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview#authz-policy-principals).

The following example shows an authorization policy for a Secure Web Proxy instance named `swp1`. This example assumes that the traffic to the proxy uses HTTPS protocol.

The policy with the `REQUEST_AUTHZ` profile enforces that all traffic to [example.com/mcp](https://example.com/mcp) requires mTLS authentication from a specific principal before the traffic is allowed to pass through. The policy also denies all outbound traffic that isn't intended to go to [example.com/mcp](https://example.com/mcp).

  1. Create the authorization policy YAML file.

The following example creates an `authz-policy.yaml` file. The policy allows traffic to the specified host and path only if the client presents a certificate that matches the defined `SPIFFE ID` principal.
         
         $ cat >authz-policy.yaml <<EOF
         name: test-authz-policy-mtls
         target:
           resources:
           - "projects/ PROJECT_ID /locations/ LOCATION /gateways/swp1"
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - to:
           operations:
           - hosts:
               - exact: "example.com"
             paths:
               - exact: "/mcp"
           from:
             sources:
             - principals:
               - principalSelector: CLIENT_CERT_URI_SAN
                 principal:
                   exact: "spiffe:// PROJECT_ID .global.123.workload.id.goog/ns/ns1/sa/hellomcp"
         action: ALLOW
         EOF
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `LOCATION`: region of your Secure Web Proxy instance
  2. Create an authorization policy and import the YAML file by using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authz-policies/import).
         
         gcloud beta network-security authz-policies import my-authz-policy-allow
             --source=authz-policy.yaml
             --location= LOCATION 
         

Replace `LOCATION` with the region of your Secure Web Proxy instance.




### Authorization policy based on service accounts or tags

You can apply an [authorization policy based on service accounts or tags](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview#authz-policy-tags-and-sa) attached to various Google Cloud resources.

This example assumes that you have completed the following:

  * [Created a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and [attached it to a Google Cloud resource](https://docs.cloud.google.com/iam/docs/attach-service-accounts).

  * [Created a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) and attached it to a Google Cloud resource as a key-value pair. When you create a tag, set its `--purpose` flag to `GCE_FIREWALL`. Authorization policies require the `GCE_FIREWALL` purpose to apply the tag.




###  Service account 

  1. Create an authorization policy YAML file to allow certain requests.

The following example creates an `authz-policy.yaml` file for the Secure Web Proxy instance named `swp1`. The policy is configured to allow requests from a Compute Engine virtual machine (VM) instance with the service account `my-sa-123@56788.iam.gserviceaccount.com` to reach the [example1.com/url1](https://example1.com/url1) path.
         
         $ cat >authz-policy.yaml <<EOF
         name: my-authz-policy-allow
         target:
             resources:
             - "projects/PROJECT_ID/locations/ LOCATION /gateways/swp1"
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - from:
             sources:
                 - resources:
                     - iamServiceAccount:
                         exact: "my-sa-123@56788.iam.gserviceaccount.com"
           to:
             operations:
             - hosts:
                 - exact: "example1.com"
             paths:
             - prefix: "/url1"
         action: ALLOW
         EOF
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `LOCATION`: region of your Secure Web Proxy instance
  2. Create an authorization policy and import the YAML file by using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authz-policies/import).

The following example command shows how to import the previously created policy file and create an authorization policy:
         
         gcloud network-security authz-policies import my-authz-policy-allow
         
             --source=authz-policy.yaml
             --location= LOCATION 
         

Replace `LOCATION` with the region of your Secure Web Proxy instance.




###  Tag 

  1. Create an authorization policy YAML file to allow certain requests.

The following example creates an `authz-policy-tag.yaml` file for the Secure Web Proxy instance named `swp1`. The policy allows only the requests that originate from a Google Cloud resource with a tag value of `TAG_VALUE_PERMANENT_ID` to access the [example1.com/url1](https://example1.com/url1) URL path.
         
         $ cat >authz-policy-tag.yaml <<EOF
         name: my-authz-policy-tag-allow
         target:
             resources:
             - "projects/PROJECT_ID/locations/ LOCATION /gateways/ GATEWAY_NAME "
         policyProfile: REQUEST_AUTHZ
         httpRules:
         - from:
             sources:
             - resources:
                 - tagValueIdSet:
                     ids: ["TAG_VALUE_PERMANENT_ID"]
           to:
             operations:
             - hosts:
                 - exact: "example1.com"
                 paths:
                 - exact: "/url1"
         action: ALLOW
         EOF
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `LOCATION`: region of your Secure Web Proxy instance
     * `GATEWAY_NAME`: name of your Secure Web Proxy gateway
     * `TAG_VALUE_PERMANENT_ID`: [permanent ID](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value) of a tag value, such as `tagValues/123456789012`
  2. Create an authorization policy and import the YAML file by using the [`gcloud network-security authz-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/authz-policies/import).

The following example command imports the previously created policy file and creates an authorization policy in the specified Google Cloud region:
         
         gcloud network-security authz-policies import my-authz-policy-tag-allow
             --source=authz-policy-tag.yaml
             --location= LOCATION 
         

Replace `LOCATION` with the region of your Secure Web Proxy instance.




### Authorization policy to delegate authorization decisions

For complex authorization decisions that can't be expressed by using standard `ALLOW` or `DENY` rules, you can create an authorization policy with a `CUSTOM` action. You can then delegate your authorization decisions to [authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) (Service Extensions).

**Important:** Secure Web Proxy supports only authorization extensions that use a fully qualified domain name (FQDN).

When you configure a policy with a `CUSTOM` action, Secure Web Proxy offloads the request metadata or payload to Service Extensions. Depending on the response from Service Extensions, the proxy either allows or rejects the traffic.

Secure Web Proxy supports the following types of delegations:

  * [Delegate request authorization decisions to Service Extensions](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-for-swp#configure-swp-request): you can use an authorization policy that's configured with a `CUSTOM` action and a `REQUEST_AUTHZ` profile to delegate decisions based on request metadata and headers. In this mode, the access decision is delegated to an authorization extension. You can use this mode to verify identities and permissions.

  * [Delegate content authorization decisions to Service Extensions](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-for-swp#configure-swp-content): you can use an authorization policy with a `CUSTOM` action and a `CONTENT_AUTHZ` profile to delegate decisions to an authorization extension based on the actual data payload of the request. This mode lets you enable deep content inspection and security enforcement, letting you scan for sensitive information or malicious patterns by integrating with services like Model Armor.




## Limitations

When you implement authorization policies for Secure Web Proxy, the following limitations apply:

  * **Target and connectivity constraints** : authorization extensions for Secure Web Proxy don't support Identity-Aware Proxy (IAP) as a direct target.

  * **Policy conflict and compatibility** : if you have a [gateway security policy](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#policies-overview) with existing security rules, then you don't need to remove them. Secure Web Proxy ignores these rules when you apply an authorization policy to your instance.

  * **Protocol and inspection requirements** : to configure Secure Web Proxy authorization policies, you must [enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection).




## What's next

  * [Use frontend mTLS with Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
