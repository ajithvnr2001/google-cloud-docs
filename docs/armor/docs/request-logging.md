---
url: https://docs.cloud.google.com/armor/docs/request-logging/
title: Per-request logging \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:20.808606+00:00
---

# Per-request logging  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/request-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Per-request logging Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor per-request logs for security policy name, match rule priority, associated action, and related information are logged as part of logging for external Application Load Balancers and external proxy Network Load Balancers. Logging for new backend services is disabled by default, so you must enable logging to record complete logging information for Cloud Armor.

Cloud Armor logs are part of the Cloud Load Balancing logs. This means that Cloud Armor log generation is subject to the log sampling rate configured for your load balancer. If you reduce the sampling rate for your load balancer, your Cloud Armor requests logs are sampled at that reduced rate. In addition, if you use [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project), logs are generated under the host or service project that includes your load balancer's frontend and URL map. Therefore, we recommend that administrators in the frontend project grant permissions to read logs and metrics to administrators in the backend project.

Using logging, you can view every request evaluated by a Cloud Armor security policy and the outcome or action taken based on the highest priority matching rule. For example, to view denied requests, you can use filters such as `jsonPayload.enforcedSecurityPolicy.outcome="DENY"` or `jsonPayload.statusDetails="denied_by_security_policy"`.

To enable logging for an external Application Load Balancer, see [Logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#logging) on the Global external Application Load Balancer logging and monitoring page. For the external proxy Network Load Balancer, you can use the Google Cloud CLI commands as listed in the previous _External Application Load Balancer logging and monitoring_ page. You cannot enable logging for the external proxy Network Load Balancer using the Google Cloud console. 

In addition, you can set different logging levels to help you evaluate whether your security policies and their rules are working as intended. For complete information, see [Verbose logging](https://docs.cloud.google.com/armor/docs/verbose-logging).

## Security policy log entries

The following log entries in the **Logs Explorer** are for Cloud Armor security policy and rules logging. The entries include the following structure in `jsonPayload`. HTTP request details appear in the `httpRequest` message.

  * `statusDetails`: a textual description of the response code. 
    * `redirected_by_security_policy`: the request was redirected by a redirect rule, either `GOOGLE_RECAPTCHA` or `EXTERNAL_302`.
    * `denied_by_security_policy`: a request was denied by the load balancer because of a Cloud Armor security policy.
    * `body_denied_by_security_policy`: a request body was denied by the load balancer because of a Cloud Armor security policy.
  * `enforcedSecurityPolicy`: the security policy rule that was enforced. 
    * `name`: the name of the security policy.
    * `priority`: a numerical priority of the matching rule in the security policy.
    * `adaptiveProtection`: information about the automatically deployed Google Cloud Armor Adaptive Protection rule, if applicable. 
      * `autoDeployAlertId`: the alert ID of the events that Adaptive Protection detected.
    * `configuredAction`: the name of the configured action in the matching rule—for example, `ALLOW`, `DENY`, `GOOGLE_RECAPTCHA`, `EXTERNAL_302`, `THROTTLE` (for a throttle rule), `RATE_BASED_BAN` (for a rate-based ban rule).
    * `rateLimitAction`: information about the rate limit action when a throttle rule or rate-based ban rule is matched. 
      * `key`: rate limit key value (up to 36 bytes). This field is omitted if the key type is `ALL`, or if the key type is `HTTP-HEADER` or `HTTP-COOKIE` and the specified header or cookie is not present in the request.
      * `outcome`: possible values are as follows: 
        * `"RATE_LIMIT_THRESHOLD_CONFORM"` if under the configured rate limit threshold.
        * `"RATE_LIMIT_THRESHOLD_EXCEED"` if above the configured rate limit threshold.
        * `"BAN_THRESHOLD_EXCEED"` if above the configured ban threshold.
    * `outcome`: the outcome of executing the configured action—for example, `ACCEPT`, `DENY`, `REDIRECT`, `EXEMPT`.
    * `preconfiguredExprIds`: the IDs of all preconfigured WAF rule expressions that triggered the rule.
    * `ruleNumber`: a permanent, unique identifier for the security policy rule that persists after it is set.
    * `rulesetId`: the name or identifier for the triggered managed rules category (for example, `google:sqli:stable`).
    * `rulesetVersion`: the version configuration defined in the matched rule (for example, `stable` or `canary`).
    * `rulesetArtifact`: the opaque, unique identifier corresponding to the version artifact registry used for evaluation.
    * `threatIntelligence`: information about the matched IP address lists from Google Threat Intelligence, if applicable. 
      * `categories`: the matched IP address list names.
    * `addressGroup`: information about the matched address groups, if applicable. 
      * `names`: the matched address group names.
  * `previewSecurityPolicy`: populated if a request matches a rule configured for preview (present only when a preview rule would have taken priority over the enforced rule). 
    * `name`: the name of the security policy
    * `priority`: a numerical priority of the matching rule in the security policy.
    * `configuredAction`: the name of the configured action in the matching rule—for example, `ALLOW`, `DENY`, `GOOGLE_RECAPTCHA`, `EXTERNAL_302`, `THROTTLE` (for a throttle rule), `RATE_BASED_BAN` (for a rate-based ban rule).
    * `rateLimitAction`: information about the rate limit action when a throttle rule or rate-based ban rule is matched. 
      * `key`: rate limit key value (up to 36 bytes). This field is omitted if the key type is `ALL`, or if the key type is `HTTP-HEADER` or `HTTP-COOKIE` and the specified header or cookie is not present in the request.
      * `outcome`: possible values are as follows: 
        * `"RATE_LIMIT_THRESHOLD_CONFORM"` if under the configured rate limit threshold.
        * `"RATE_LIMIT_THRESHOLD_EXCEED"` if above the configured rate limit threshold.
        * `"BAN_THRESHOLD_EXCEED"` if above the configured ban threshold.
    * `outcome`: the outcome of executing the configured action—for example, `ACCEPT`, `DENY`, `REDIRECT`, `EXEMPT`.
    * `preconfiguredExprIds`: the IDs of all preconfigured WAF rule expressions that triggered the rule.
    * `ruleNumber`: a permanent, unique identifier for the security policy rule that persists after it is set.
    * `rulesetId`: the name or identifier for the triggered managed rules category (for example, `google:sqli:stable`).
    * `rulesetVersion`: the version configuration defined in the matched rule (for example, `stable` or `canary`).
    * `rulesetArtifact`: the opaque, unique identifier corresponding to the version artifact registry used for evaluation.
    * `threatIntelligence`: information about the matched IP address lists from Threat Intelligence, if applicable. 
      * `categories`: the matched IP address list names.
    * `addressGroup`: information about the matched address groups, if applicable. 
      * `names`: the matched address group names.
  * `enforcedEdgeSecurityPolicy`: the edge security policy rule that was enforced. 
    * `name`: the name of the security policy.
    * `priority`: the priority of the matching rule in the security policy.
    * `configuredAction`: the name of the configured action in the matching rule—for example, `ALLOW`, `DENY`.
    * `outcome`: the outcome of executing the configured action—for example, `ACCEPT`, `DENY`.
  * `previewEdgeSecurityPolicy`: populated if a request matches an edge security policy rule configured for preview. The `previewEdgeSecurityPolicy` log entry is only present when a preview rule takes priority over the enforced rule. 
    * `name`: the name of the security policy.
    * `priority`: a numerical priority of the matching rule in the security policy.
    * `configuredAction`: the name of the configured action in the matching rule—for example, `ALLOW`, `DENY`.
    * `outcome`: the outcome of executing the configured action—for example, `ACCEPT`, `DENY`.
  * `evaluatedSecurityPolicies`: a list of non-terminal matching rules evaluated for this policy (for example, info-only and candidate preview matches). 
    * `ruleNumber`: a permanent, unique identifier for the security policy rule that persists after it is set.
    * `rulesetId`: the name or identifier for the triggered managed rules category (for example, `google:sqli:stable`).
    * `rulesetVersion`: the version configuration defined in the matched rule (for example, `stable` or `canary`).
    * `rulesetArtifact`: the opaque, unique identifier corresponding to the version artifact registry used for evaluation.



## Viewing logs

You can view the logs for a Cloud Armor security policy only in the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to **Cloud Armor policies**.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click more_vert**Actions**.

  3. Select **View logs**.




## Request data logging

When used with Cloud Armor, `jsonPayload` has the following additional field:

  * `securityPolicyRequestData`: data pertaining to the request while being processed by a security policy, regardless of which rule is matched eventually. 
    * `recaptchaActionToken`: data related to a reCAPTCHA action-token. 
      * `score`: a user legitimacy score embedded in a reCAPTCHA action-token. Only present when a reCAPTCHA action-token is attached with the request and it is decoded successfully based on a security policy rule. For more information, see [Enforce reCAPTCHA assessment](https://docs.cloud.google.com/armor/docs/configure-bot-management#enforce-assessment).
    * `recaptchaSessionToken`: data related to a reCAPTCHA session-token. 
      * `score`: a user legitimacy score embedded in a reCAPTCHA session-token. Only present when a reCAPTCHA session-token is attached with the request and it is decoded successfully based on a security policy rule.
    * `userIpInfo`: the data related to user IP usage. 
      * `source`: a field that is typically the header from which the user IP was resolved.
      * `ipAddress`: the IP address resolved from the source field.
    * `remoteIpInfo`: the data related to the client IP address of the request. 
      * `ipAddress`: the client IP address of the request.
      * `region_code`: the two-letter country code or region code for the IP address.
      * `asn`: the five-digit Autonomous System Number (ASN) corresponding to the IP address.
    * `tlsJa4Fingerprint`: a JA4 TTL/SSL fingerprint if the client connects using `HTTPS`, `HTTP/2`, or `HTTP/3`. Only present if the fingerprint is available and there is a security policy that evaluates the request (regardless of whether an expression in the policy matches on the request).
    * `tlsJa3Fingerprint`: a JA3 TTL/SSL fingerprint if the client connects using `HTTPS`, `HTTP/2`, or `HTTP/3`. Only present if the fingerprint is available and there is a security policy that evaluates the request (regardless of whether an expression in the policy matches on the request).



## Log examples

The following is an example of log details for a throttle rule that blocks a request:
    
    
    jsonPayload: {
     enforcedSecurityPolicy: {
      priority: 100
      name: "sample-prod-policy"
      configuredAction: "THROTTLE"
      outcome: "DENY"
      rateLimitAction: {
        key:"sample-key"
        outcome:"RATE_LIMIT_THRESHOLD_EXCEED"
      }
     }
     @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
     statusDetails: "denied_by_security_policy"
    }
    httpRequest: {8}
    resource: {2}
    timestamp: "2021-03-17T19:16:48.185763Z"
    

The following is an example of log details for a rate-based ban rule that blocks a request:
    
    
    jsonPayload: {
     @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
     enforcedSecurityPolicy: {
      priority: 150
      name: "sample-prod-policy"
      outcome: "DENY"
      configuredAction: "RATE_BASED_BAN"
      rateLimitAction: {
        key:"sample-key"
        outcome:"BAN_THRESHOLD_EXCEED"
      }
     }
     statusDetails: "denied_by_security_policy"
    }
    httpRequest: {8}
    resource: {2}
    timestamp: "2021-03-17T19:27:17.393244Z"
    

## What's next

  * Learn about [Troubleshooting Cloud Armor issues](https://docs.cloud.google.com/armor/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
