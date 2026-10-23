---
url: https://docs.cloud.google.com/armor/docs/configure-rate-limiting/
title: Configure rate limiting \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:33.273378+00:00
---

# Configure rate limiting  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/configure-rate-limiting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Configure rate limiting Stay organized with collections  Save and categorize content based on your preferences. 

To help to protect your services against denial-of-service (DoS) and web attacks, you can configure Google Cloud Armor security policies to enforce per-client rate limits. This page describes how to configure throttle or rate-based actions, which lets you control the rate at which clients send requests to help prevent abuse and ensure fair resource allocation. Before you configure rate limiting, see [rate limiting overview](https://docs.cloud.google.com/armor/docs/rate-limiting-overview).

## Before you begin

The following sections explain all of the Identity and Access Management (IAM) roles and permissions required to configure Cloud Armor security policies. For the use cases in this document, you only need the `compute.securityPolicies.create` permission.

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
  
## Rules for rate-based throttling

Rules for rate-based throttling have the following format in the Google Cloud CLI:
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy=SECURITY_POLICY \
        {--expression=EXPRESSION | --src-ip-ranges=SRC_IP_RANGE} \
        --action "throttle" \
        --rate-limit-threshold-count=RATE_LIMIT_THRESHOLD_COUNT \
        --rate-limit-threshold-interval-sec=RATE_LIMIT_THRESHOLD_INTERVAL_SEC \
        --conform-action=[allow] \
        --exceed-action=[deny-403|deny-404|deny-429|deny-502|redirect] \
        --exceed-redirect-type=[google-recaptcha|external-302] \
        --exceed-redirect-target=REDIRECT_URL \
        --enforce-on-key=[IP | ALL | HTTP-HEADER | XFF-IP | HTTP-COOKIE | HTTP-PATH | SNI | REGION-CODE] \
        --enforce-on-key-name=[HTTP_HEADER_NAME|HTTP_COOKIE_NAME]
    

### Rate limiting on single keys

For example, the following gcloud CLI command creates a `throttle` rule at priority `105` with a rate limit of 100 requests each 60 seconds for each IP address in `1.2.3.0/24`. Requests that exceed the throttling limit return a `429 Too Many Requests` status code.
    
    
    gcloud compute security-policies rules create 105 \
        --security-policy SECURITY_POLICY \
        --src-ip-ranges="1.2.3.0/24" \
        --action=throttle \
        --rate-limit-threshold-count=100 \
        --rate-limit-threshold-interval-sec=60 \
        --conform-action=allow \
        --exceed-action=deny-429 \
        --enforce-on-key=IP
    

For example, the following gcloud CLI command creates a `throttle` rule at priority `110` with a rate limit of 10 requests each 60 seconds for each unique value of the HTTP header `User-Agent` across all requests coming from IP addresses in `1.2.3.0/24`. Requests that exceed the throttling limit return a `429 Too Many Requests` status code.
    
    
    gcloud compute security-policies rules create 110 \
        --security-policy SECURITY_POLICY \
        --src-ip-ranges="1.2.3.0/24" \
        --action=throttle \
        --rate-limit-threshold-count=10 \
        --rate-limit-threshold-interval-sec=60 \
        --conform-action=allow \
        --exceed-action=deny-429 \
        --enforce-on-key=HTTP-HEADER \
        --enforce-on-key-name='User-Agent'
    

Finally, you can issue rate-based bans for users who have a valid reCAPTCHA exemption cookie. For example, the following gcloud CLI command creates a `throttle` rule at priority `115` with a rate limit of 20 requests per 5 minutes for each unique reCAPTCHA exemption cookie across all requests that have a valid reCAPTCHA exemption cookie. Requests that exceed the throttling limit are redirected for reCAPTCHA assessment. For more information about exemption cookies and reCAPTCHA assessment, see the [Cloud Armor bot management overview](https://docs.cloud.google.com/armor/docs/bot-management).
    
    
    gcloud compute security-policies rules create 115 \
        --security-policy SECURITY_POLICY \
        --expression="token.recaptcha_exemption.valid" \
        --action=throttle \
        --rate-limit-threshold-count=20 \
        --rate-limit-threshold-interval-sec=300 \
        --conform-action=allow \
        --exceed-action=redirect \
        --exceed-redirect-type=google-recaptcha \
        --enforce-on-key=HTTP-COOKIE \
        --enforce-on-key-name="recaptcha-ca-e"
    

#### Rate limiting based on JA4 and JA3 fingerprints

You can use JA4 and JA3 fingerprints as rate limiting keys. The following example creates a `throttle` rule at priority `1000` with a rate limit of 20 requests per 5 minutes that matches on requests with the `/login` path, based on the client's JA4 fingerprint. Requests that exceed the throttling limit are denied.
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy SECURITY_POLICY \
        --expression "request.path.matches('/login')" \
        --action throttle \
        --rate-limit-threshold-count 20 \
        --rate-limit-threshold-interval-sec 300 \
        --conform-action allow \
        --exceed-action deny-429 \
        --enforce-on-key-configs tls-ja4-fingerprint
    

#### Rate limiting based on user IP address

When you receive requests that come through an upstream proxy, you can apply rate limiting based on the originating client's IP address. The following example creates a `throttle` rule at priority `1000` with a rate limit of 20 requests per 5 minutes that matches on requests with the `/login` path, based on the originating client's IP address. Requests that exceed the throttling limit are denied.
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy SECURITY_POLICY \
        --expression "request.path.matches('/login')" \
        --action throttle \
        --rate-limit-threshold-count 20 \
        --rate-limit-threshold-interval-sec 300 \
        --conform-action allow \
        --exceed-action deny-429 \
        --enforce-on-key-configs user-ip
    

For more information about user IP address support, see the [rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference#attributes).

### Rate limiting based on multiple keys

You can also throttle traffic based on multiple rate limiting keys by using the `enforce-on-key-configs` flag. This flag replaces both the `enforce-on-key` flag and the `enforce-on-key-name` flag. The `enforce-on-key-configs` flag requires a comma-separated list of `KEY=NAME` pairs; although, you don't need to provide a name for some keys.

The following example creates a `throttle` rule for the policy `POLICY_NAME` at priority `105` with a rate limit of 100 requests each 60 seconds for each combination of `HTTP-PATH` and `site_id` across all requests coming from IP addresses in `1.2.3.0/24`. Requests that exceed the throttling limit return a `429 Too Many Requests` status code.
    
    
    gcloud compute security-policies rules create 105 \
        --security-policy=POLICY_NAME \
        --src-ip-ranges="1.2.3.0/24" \
        --action=throttle \
        --rate-limit-threshold-count=100 \
        --rate-limit-threshold-interval-sec=60 \
        --conform-action=allow \
        --exceed-action=deny-429 \
        --enforce-on-key-configs="HTTP-PATH,HTTP-COOKIE=site_id"
    

## Rules for rate-based bans

Rules for rate-based bans have the following format in the gcloud CLI:
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy=SECURITY_POLICY \
        {--expression=EXPRESSION | --src-ip-ranges=SRC_IP_RANGE} \
        --action "rate-based-ban" \
        --rate-limit-threshold-count=RATE_LIMIT_THRESHOLD_COUNT \
        --rate-limit-threshold-interval-sec=RATE_LIMIT_THRESHOLD_INTERVAL_SEC \
        --ban-duration-sec=BAN_DURATION_SEC \
        --ban-threshold-count=BAN_THRESHOLD_COUNT \
        --ban-threshold-interval-sec=BAN_THRESHOLD_INTERVAL_SEC \
        --conform-action=[allow] \
        --exceed-action=[deny-403|deny-404|deny-429|deny-502|redirect] \
        --exceed-redirect-type=[google-recaptcha|external-302] \
        --exceed-redirect-target=REDIRECT_URL \
        --enforce-on-key=[IP | ALL | HTTP-HEADER | XFF-IP | HTTP-COOKIE | HTTP-PATH | SNI | REGION-CODE] \
        --enforce-on-key-name=[HTTP_HEADER_NAME|HTTP_COOKIE_NAME]
    

For example, the following gcloud CLI command creates a rate-based ban rule at priority `100` for each IP address whose requests match a header `fish` with value `tuna` and ban it for 300 seconds when its rate exceeds a limit of 50 requests for each 120 seconds. Banned requests return a status code of `404 Not Found`.
    
    
    gcloud compute security-policies rules create 100 \
        --security-policy=sec-policy \
        --expression="request.headers['fish'] == 'tuna'" \
        --action=rate-based-ban \
        --rate-limit-threshold-count=50 \
        --rate-limit-threshold-interval-sec=120 \
        --ban-duration-sec=300 \
        --conform-action=allow \
        --exceed-action=deny-404 \
        --enforce-on-key=IP
    

For example, the following gcloud CLI command creates a rate-based ban rule at priority `101` to limit all requests whose region code matches `US` to 10 requests per 60 seconds. The rule also bans requests from the `US` region for 300 seconds when their rate exceeds a limit of 1000 requests per 600 seconds. Banned requests return a status code of `403 Forbidden`.
    
    
    gcloud compute security-policies rules create 101 \
        --security-policy sec-policy \
        --expression "origin.region_code == 'US'" \
        --action rate-based-ban \
        --rate-limit-threshold-count 10 \
        --rate-limit-threshold-interval-sec 60 \
        --ban-duration-sec 300 \
        --ban-threshold-count 1000 \
        --ban-threshold-interval-sec 600 \
        --conform-action allow \
        --exceed-action deny-403 \
        --enforce-on-key ALL
    

For example, the following gcloud CLI command creates a rate-based ban rule at priority `102` to limit all requests from any source IP address range to 20 requests per 60 seconds. The rule also bans requests from any source IP address range for 600 seconds when the rate of requests exceeds a limit of 500 requests per 400 seconds. Banned requests return a status code of `429 Too Many Requests`.
    
    
    gcloud compute security-policies rules create 102 \
        --security-policy sec-policy \
        --src-ip-ranges="*" \
        --action rate-based-ban \
        --rate-limit-threshold-count 20 \
        --rate-limit-threshold-interval-sec 60 \
        --ban-duration-sec 600 \
        --ban-threshold-count 500 \
        --ban-threshold-interval-sec 400 \
        --conform-action allow \
        --exceed-action deny-429 \
        --enforce-on-key ALL
    

## Change a throttle rule to a rate-based ban rule

You can use the following command to change the action of an existing rule from a throttle action to a rate-based ban action.
    
    
    gcloud compute security-policies rules update 105 \
        --action=rate-based-ban \
        --security-policy=sec-policy \
        --ban-duration-sec=600
    

You can't change the action of an existing rule from a rate-based ban action to a throttle action.

## What's next

  * View the [rate limiting overview](https://docs.cloud.google.com/armor/docs/rate-limiting-overview).
  * Learn more about [bot management](https://docs.cloud.google.com/armor/docs/bot-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
