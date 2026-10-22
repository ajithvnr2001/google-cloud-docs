---
url: https://docs.cloud.google.com/armor/docs/configure-security-policies/
title: Create and view Cloud Armor security policies \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:57.079246+00:00
---

# Create and view Cloud Armor security policies  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/configure-security-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Create and view Cloud Armor security policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can create Google Cloud Armor security policies to filter incoming traffic to your application. For information about security policy concepts, see the [Cloud Armor security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

**Caution:** You can configure Cloud Armor by using Google Kubernetes Engine (GKE) ingress security policies. When you apply changes to GKE resources, Cloud Armor configuration is overwritten. For information about configuring Cloud Armor on GKE, see [Configure ingress features through BackendConfig parameters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#configuring_ingress_features_through_backendconfig_parameters) in [Cloud Armor ingress security policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#cloud_armor).

## Before you begin

Before you configure security policies, do the following:

  * Make sure that you're familiar with [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) concepts.

  * Examine your existing backend services to determine which ones don't have a security policy attached. These backend services and their associated backends are not protected. To add Cloud Armor protection, attach a new or existing security policy to the backend service.




### Set up IAM permissions for Cloud Armor security policies

The following operations require the Identity and Access Management (IAM) [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`):

  * Configuring, modifying, updating, and deleting a Cloud Armor security policy
  * Using the following API methods: 
    * `SecurityPolicies insert`
    * `SecurityPolicies delete`
    * `SecurityPolicies patch`
    * `SecurityPolicies addRule`
    * `SecurityPolicies patchRule`
    * `SecurityPolicies removeRule`



A user with the [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) can perform the following operations:

  * Setting a Cloud Armor security policy for a backend service
  * Using the following API methods: 
    * `BackendServices setSecurityPolicy`
    * `BackendServices list` (`gcloud` only)



Users with the [Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) and the Compute Network Admin role (`roles/compute.networkAdmin`) can view Cloud Armor security policies by using the `SecurityPolicies` API methods `get`, `list`, and `getRule`.

### Set up IAM permissions for custom roles

The following table lists the IAM roles' base permissions, their associated API methods, and the roles that grant that permission.

IAM permission | API methods | Roles  
---|---|---  
`compute.securityPolicies.create` | `SecurityPolicies insert` | [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.securityAdmin)  
`compute.securityPolicies.delete` | `SecurityPolicies delete` | [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.securityAdmin)  
`compute.securityPolicies.get` | `SecurityPolicies get`  
`SecurityPolicies getRule` | [Security Admin (`roles/iam.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#iam.securityAdmin)  
`compute.securityPolicies.list` | `SecurityPolicies list` | [Security Admin (`roles/iam.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#iam.securityAdmin)  
Both of the following: 

  * `compute.securityPolicies.use`
  * `compute.backendServices.  
setSecurityPolicy`

| `BackendServices  
setSecurityPolicy` | [Compute Network Admin (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.networkAdmin)  
`compute.securityPolicies.update` | `SecurityPolicies patch`  
`SecurityPolicies addRule`  
`SecurityPolicies patchRule`  
`SecurityPolicies removeRule` | [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.securityAdmin)  
  
## Create security policies

Use the Google Cloud console, the Google Cloud CLI, or the REST API to configure Cloud Armor security policies, rules, and expressions. When you use the gcloud CLI, use the `--type` flag to specify whether the security policy is a backend security policy or an edge security policy.

If you're unfamiliar with security policy configuration, review the [example security policies](https://docs.cloud.google.com/armor/docs/example-policies).

### Sample expressions

The following are sample expressions. For more information, see the [ Cloud Armor custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference).

If your rule or expression uses [ISO 3166-1 alpha-2](https://www.wikipedia.org/wiki/ISO_3166-1_alpha-2) country or region codes, Cloud Armor treats each code independently. Cloud Armor rules and expressions use those codes to permit or deny requests.

  * The following expression matches requests from the IP address `1.2.3.4` that contain the string `example` in the `User-Agent` header:
        
        inIpRange(origin.ip, '1.2.3.4/32') && has(request.headers['user-agent']) && request.headers['user-agent'].contains('example')
        

Alternatively, match on the IP address range of a custom client IP address header by using the [`origin.user_ip`](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes) attribute:
        
        inIpRange(origin.user_ip, '1.2.3.4/32') && has(request.headers['user-agent']) && request.headers['user-agent'].contains('example')
        

  * The following expression matches requests that have a cookie with a specific value:
        
        has(request.headers['cookie']) && request.headers['cookie'].contains('cookie_name=cookie_value')
        

  * The following expression matches requests from the region `AU`:
        
        origin.region_code == 'AU'
        

  * The following expression matches requests from the region `AU` that aren't in the specified IP range:
        
        origin.region_code == "AU" && !inIpRange(origin.ip, '1.2.3.0/24')
        

  * The following expression matches requests with a numbered variable path to a specific file if the URI matches a regular expression:
        
        request.path.matches('/path/[0-9]+/target_file.html')
        

  * The following expression matches requests if the Base64-decoded value of the `user-id` header contains a specific value:
        
        has(request.headers['user-id']) && request.headers['user-id'].base64Decode().contains('myValue')
        

  * The following expression uses a preconfigured expression set to match against SQLi attacks:
        
        evaluatePreconfiguredWaf('sqli-stable')
        




### Path traversal and normalization

Normalize content in your path-based rules to manage path traversal and encoding rules and to create generalized rules that avoid capitalization or content-specific encoding.

When you write rules that use `startsWith`, `endsWith`, or `contains` to match on `request.path`, use `lower` and `urlDecode` to normalize the path before matching. This helps prevent bypasses that use URL-encoding or case variations.

For example, to block access to the `/admin` directory, use the following expression:
    
    
    request.path.lower().urlDecode().startsWith('/admin')
    

This rule blocks requests for `/admin`, `/Admin`, `/a%64min`, and other variations.

When you write rules that use `matches` to match on `request.path`, account for the backslash character (\\) in your regular expression.

For example, to block access to the `/admin` directory, use the following expression to block bypasses that use the backslash character (\\):
    
    
    request.path.matches(r'^/\\*admin')
    

Combine this with `urlDecode` to handle both URL-encoding and the backslash character (\\) bypasses:
    
    
    request.path.urlDecode().matches(r'^/\\*admin')
    

## What's next

  * [Tune web application firewall (WAF) rules](https://docs.cloud.google.com/armor/docs/rule-tuning)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)
  * [Use the custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference)
  * [Manage security policies](https://docs.cloud.google.com/armor/docs/manage-security-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
