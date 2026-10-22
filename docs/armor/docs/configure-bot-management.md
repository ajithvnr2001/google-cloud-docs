---
url: https://docs.cloud.google.com/armor/docs/configure-bot-management/
title: Configure bot management \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:57.491161+00:00
---

# Configure bot management  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/configure-bot-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Configure bot management Stay organized with collections  Save and categorize content based on your preferences. 

To help protect your services against denial-of-service (DoS) and web attacks, you can configure Google Cloud Armor security policy rules for bot management. This page describes how to configure bot management, which lets you detect and mitigate automated threats, differentiate between human and bot traffic, and safeguard your applications from malicious activity. Before you configure bot management, see [Bot management overview](https://docs.cloud.google.com/armor/docs/bot-management).

## Before you begin

The following sections explain all of the Identity and Access Management (IAM) roles and permissions required to configure Cloud Armor security policies. For the use cases in this document, you only need the `compute.securityPolicies.create` and `compute.securityPolicies.update` permissions.

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
  
## Use a reCAPTCHA manual challenge to distinguish between human or automated clients

To use reCAPTCHA with Cloud Armor, you must associate your reCAPTCHA WAF site key (reCAPTCHA key) of type `CHALLENGEPAGE` with a security policy. For more information about reCAPTCHA keys, see [reCAPTCHA keys overview](https://docs.cloud.google.com/recaptcha/docs/keys).

To associate or disassociate your own reCAPTCHA key with a security policy, use the following command:
    
    
    gcloud compute security-policies update SECURITY_POLICY \
        --recaptcha-redirect-site-key SITE_KEY
    

Replace the following:

  * `SECURITY_POLICY`: the name of the security policy
  * `SITE_KEY`: your reCAPTCHA `CHALLENGEPAGE` key



### Associate a reCAPTCHA key

The following example associates a reCAPTCHA key with a security policy. The associated reCAPTCHA key applies to all the rules that use the manual challenge feature under the given security policy.
    
    
    gcloud compute security-policies update SECURITY_POLICY \
        --recaptcha-redirect-site-key "SITE_KEY"
    

### Disassociate a reCAPTCHA key

To disassociate a reCAPTCHA key with a security policy, use this command:
    
    
    gcloud compute security-policies update SECURITY_POLICY \
        --recaptcha-redirect-site-key ""
    

### Redirect traffic for reCAPTCHA assessment

When you have associated your reCAPTCHA key with your security policy, you can create a rule within that policy to internally redirect traffic for reCAPTCHA assessment. Use the following format in the gcloud CLI to redirect traffic:
    
    
    gcloud compute security-policies rules create PRIORITY \
      --security-policy SECURITY_POLICY \
      {--expression EXPRESSION | --src-ip-ranges SRC_IP_RANGE} \
      --action redirect \
      --redirect-type google-recaptcha
    

Replace the following:

  * `PRIORITY`: the priority at which you want to create the rule
  * `SECURITY_POLICY`: the name of the security policy
  * `EXPRESSION`: the custom rules language expression that matches the traffic on which you want to enforce reCAPTCHA assessment
  * `SRC_IP_RANGE`: an IP address range. Use this to enforce reCAPTCHA assessment on all requests from this range.



The following example creates a rule that redirects traffic attempting to reach `/login.html` for a reCAPTCHA manual challenge:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy SECURITY_POLICY \
        --expression "request.path.matches(\"/login.html\")" \
        --action redirect \
        --redirect-type google-recaptcha
    

## Enforce reCAPTCHA frictionless assessment

Before you proceed, see the [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management#recaptcha-tokens) for prerequisites on using reCAPTCHA action-tokens or session-tokens.

To extract attributes from a reCAPTCHA action-token, you can use `token.recaptcha_action.ATTRIBUTE`. Replace `ATTRIBUTE` with a valid token attribute in the Cloud Armor [rules language](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes). Similarly, use `token.recaptcha_session.ATTRIBUTE` to extract attributes from a reCAPTCHA session-token. For more information about the syntax of available reCAPTCHA token attributes, see the [rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).

An action-token can originate from a web application, an iOS application, or an Android application, while a session-token can only originate from a web application. Each platform requires a separate reCAPTCHA key. The expressions `token.recaptcha_action.ATTRIBUTE` and `token.recaptcha_session.ATTRIBUTE` apply to tokens from any of these platforms. To distinguish tokens from different platforms and to prevent token theft, we recommend that you associate reCAPTCHA keys when you configure rules that use these expressions.

### Examples

The first example creates a rule that allows traffic targeting `/login.html` with a reCAPTCHA action-token whose score is no less than `0.8`.
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy SECURITY_POLICY \
        --expression "request.path.matches(\"/login.html\") && token.recaptcha_action.score >= 0.8" \
        --action allow
    

The second example is the same as the first example, but it also requires that the action-token be issued with a reCAPTCHA key of `example-site-key-1` or `example-site-key-2`:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy SECURITY_POLICY \
        --expression "request.path.matches(\"/login.html\") && token.recaptcha_action.score >= 0.8" \
        --recaptcha-action-site-keys "example-site-key-1,example-site-key-2" \
        --action allow
    

The third example creates a rule that allows traffic targeting `/login.html`, with a reCAPTCHA session-token issued with a reCAPTCHA key of `example-site-key-3`, and with a score no less than `0.8`.
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy SECURITY_POLICY \
        --expression "request.path.matches(\"/login.html\") && token.recaptcha_session.score >= 0.8" \
        --recaptcha-session-site-keys "example-site-key-3" \
        --action allow
    

## Redirect (302 response)

To create a rule to redirect traffic to a user-configured URL, use the following format in the Google Cloud CLI:
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy SECURITY_POLICY \
        {--expression EXPRESSION | --src-ip-ranges SRC_IP_RANGE} \
        --action redirect \
        --redirect-type external-302 \
        --redirect-target REDIRECT_URL
    

Replace the following:

  * `PRIORITY`: the priority at which you want to create the rule
  * `SECURITY_POLICY`: the name of the security policy
  * `EXPRESSION`: the custom rules language expression that matches the traffic up which you want to enforce reCAPTCHA assessment
  * `SRC_IP_RANGE`: an IP address range. Use this to enforce reCAPTCHA assessment on all requests from this range.
  * `REDIRECT_URL`: the URL to which you want to redirect traffic



The following example creates a rule that redirects traffic coming from 10.10.10.0/24 to https://www.example.com.
    
    
    gcloud compute security-policies rules create 1000 \
       --security-policy SECURITY_POLICY \
       --src-ip-ranges "10.10.10.0/24" \
       --action redirect \
       --redirect-type external-302 \
       --redirect-target "https://www.example.com"
    

## Decorate request

To create a rule that allows traffic but adds custom headers and user-defined static values before sending them to protected backends, use the following format in the gcloud CLI:
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy SECURITY_POLICY \
        {--expression EXPRESSION | --src-ip-ranges SRC_IP_RANGE} \
        --action allow \
        --request-headers-to-add HEADER_1=VALUE_1,HEADER_2=VALUE_2,...
    

Replace the following:

  * `PRIORITY`: the priority at which you want to create the rule
  * `SECURITY_POLICY`: the name of the security policy
  * `EXPRESSION`: the custom rules language expression that matches the traffic on which you want to enforce reCAPTCHA assessment
  * `SRC_IP_RANGE`: an IP address range. Use this to enforce reCAPTCHA assessment on all requests from this range.
  * `HEADER_#`: the name of the request header with which you want to decorate the request
  * `VALUE_#`: the value of the request header with which you want to decorate the request



The following example creates a rule that allows traffic targeting `/login.html`, as long as the request also has a reCAPTCHA action-token score lower than `0.2`.
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy SECURITY_POLICY \
        --expression "request.path.matches("/login.html") && token.recaptcha_action.score < 0.2" \
        --action allow \
        --request-headers-to-add "reCAPTCHA-Warning=high"
    

## What's next

  * View the [rate limiting overview](https://docs.cloud.google.com/armor/docs/rate-limiting-overview).
  * Learn about [bot management](https://docs.cloud.google.com/armor/docs/bot-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
