---
url: https://docs.cloud.google.com/armor/docs/configure-adaptive-protection/
title: Configure Adaptive Protection \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:32.658954+00:00
---

# Configure Adaptive Protection  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/configure-adaptive-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Configure Adaptive Protection Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure Google Cloud Armor Adaptive Protection, which helps protect your services from layer 7 (L7) distributed denial-of-service (DDoS) attacks and other web attacks by using Google's global infrastructure and security systems. By following the instructions on this page, you can fine-tune Adaptive Protection's mitigation strategies and customize how it safeguards your applications. Before you begin, familiarize yourself with the [Adaptive Protection overview](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview) and its [Adaptive Protection use cases](https://docs.cloud.google.com/armor/docs/adaptive-protection-use-cases) to understand its capabilities.

## Before you begin

The following sections explain all of the Identity and Access Management (IAM) roles and permissions required to configure Google Cloud Armor security policies. For the use cases in this document, you only need the `compute.securityPolicies.update` permission.

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
  
## Enable Adaptive Protection

Use the following steps to enable Adaptive Protection for your security policy. Adaptive Protection is applied to each security policy individually.

###  Console 

To activate Adaptive Protection for a security policy:

  1. In the Google Cloud console, go to the **Network Security** page.

[Go to Network Security](https://console.cloud.google.com/net-security/)

  2. On the **Policies** page, click the name of a security policy.

  3. Click **Edit**.

  4. Under **Adaptive Protection** , select **Enable**.

  5. Click **Update**.




To deactivate Adaptive Protection for a security policy:

  1. In the Google Cloud console, go to the **Network Security** page.

[Go to Network Security](https://console.cloud.google.com/net-security/)

  2. On the **Policies** page, click the name of a security policy.

  3. Click **Edit**.

  4. Under **Adaptive Protection** , clear **Enable**.

  5. Click **Update**.




###  gcloud 

To activate Adaptive Protection for a security policy:
    
    
    gcloud compute security-policies update MY-SECURITY-POLICY \
        --enable-layer7-ddos-defense
    

To deactivate Adaptive Protection for a security policy:
    
    
    gcloud compute security-policies update MY-SECURITY-POLICY \
        --no-enable-layer7-ddos-defense
    

## Configure granular models

The granular models feature lets you configure specific hosts or paths as the granular units that Adaptive Protection analyzes. In the following examples, you create granular traffic units for each host, customize a granular traffic unit, and configure Adaptive Protection to take action when traffic exceeds your baseline queries per second (QPS). For more information about granular models, see the [Adaptive Protection overview](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview#granular-models).

### Configure granular traffic units

The examples in this section use the [`add-layer7-ddos-defense-threshold-config`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config) command with some or all of the following flags:

Flag | Description  
---|---  
`--threshold-config-name` | The name of the threshold config.  
`--traffic-granularity-configs` | Configuration options for enabling Adaptive Protection to work on the specified service granularity.  
`--auto-deploy-impacted-baseline-threshold` | Threshold on Adaptive Protection's estimated impact to the baseline traffic of the suggested mitigating rule to a detected attack. Automatic defenses are applied only if the threshold is not exceeded.  
`--auto-deploy-expiration-sec` | The duration of actions, if any, taken by auto-deploy.  
`--detection-load-threshold` | Detection threshold based on the backend service's load.  
`--detection-absolute-qps` | Detection threshold based on absolute QPS.  
`--detection-relative-to-baseline-qps` | Detection threshold based on QPS relative to the average of baseline traffic.  
  
In the first example, you configure Adaptive Protection to detect attacks on and suggest independent mitigations for each host behind your backend service, without overriding any default thresholds.

###  gcloud 

  1. Create a security policy with the name `POLICY_NAME`, or use an existing security policy.
  2. If Adaptive Protection is not already enabled, use the following command to enable Adaptive Protection for your policy: 
         
         gcloud compute security-policies update POLICY_NAME   
         
         --enable-layer7-ddos-defense
         

  3. Apply the security policy to a backend service with multiple hosts.
  4. Use the following `add-layer7-ddos-defense-threshold-config` command with the `--traffic-granularity-configs` flag to configure a granular traffic unit: 
         
         gcloud compute security-policies add-layer7-ddos-defense-threshold-config POLICY_NAME   
         
         --threshold-config-name=per-host-config   
         
         --traffic-granularity-configs=type=HTTP_HEADER_HOST;enableEachUniqueValue=true
         




In the second example, you configure different auto-deploy and detection thresholds for some or all of the granular traffic units that you configured in the first example.

###  gcloud 

  1. If Adaptive Protection auto-deploy is not already enabled, [create a placeholder rule](https://docs.cloud.google.com/armor/docs/adaptive-protection-auto-deploy#example_placeholder_rules).
  2. The following command customizes the auto-deploy threshold for a granular traffic unit with an `HTTP_HEADER_HOST` of `HOST` and an `HTTP_PATH` of `PATH`. Use this command for each granular traffic unit that you want to customize, replacing the variables as needed for each host and URL path: 
         
         gcloud compute security-policies add-layer7-ddos-defense-threshold-config POLICY_NAME   
         
         --threshold-config-name=my-host-config   
         
         --auto-deploy-impacted-baseline-threshold=0.01   
         
         --auto-deploy-expiration-sec=3600   
         
         --traffic-granularity-configs=type=HTTP_HEADER_HOST;value=HOST,type=HTTP_PATH;value=PATH
         




### Detect when attack volume exceeds baseline average QPS

In the following example, you configure Adaptive Protection to detect an attack only when the attack volume exceeds your baseline average QPS by more than 50%, and only when the backend service's load is more than 90% of its capacity.

###  gcloud 

  1. Create a security policy with the name `POLICY_NAME`, or use an existing security policy.
  2. If Adaptive Protection is not already enabled, use the following command to enable Adaptive Protection for your policy:
         
         gcloud compute security-policies update POLICY_NAME \
           --enable-layer7-ddos-defense
         

  3. Apply the security policy to a backend service.

  4. Use the following command to configure Adaptive Protection with customized detection thresholds:
         
         gcloud compute security-policies add-layer7-ddos-defense-threshold-config POLICY_NAME \
            --threshold-config-name=my-customized-thresholds \
            --detection-load-threshold=0.9 \
            --detection-relative-to-baseline-qps=1.5
         




## What's next

  * [Adaptive Protection overview](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview)
  * [Adaptive Protection use cases](https://docs.cloud.google.com/armor/docs/adaptive-protection-use-cases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
