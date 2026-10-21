---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/security-policies/update/
title: gcloud beta compute security-policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:32:35.985710+00:00
---

# gcloud beta compute security-policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/security-policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute security-policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute security-policies update - update a Compute Engine security policy 
SYNOPSIS
    

`gcloud beta compute security-policies update` `NAME` [`--description`=`DESCRIPTION`] [`--enable-layer7-ddos-defense`] [`--json-custom-content-types`=[`CONTENT_TYPE`,…]] [`--json-parsing`=`JSON_PARSING`] [`--layer7-ddos-defense-auto-deploy-confidence-threshold`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_CONFIDENCE_THRESHOLD`] [`--layer7-ddos-defense-auto-deploy-expiration-sec`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_EXPIRATION_SEC`] [`--layer7-ddos-defense-auto-deploy-impacted-baseline-threshold`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_IMPACTED_BASELINE_THRESHOLD`] [`--layer7-ddos-defense-auto-deploy-load-threshold`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_LOAD_THRESHOLD`] [`--layer7-ddos-defense-rule-visibility`=`VISIBILITY_TYPE`] [`--log-level`=`LOG_LEVEL`] [`--network-ddos-adaptive-protection`=`NETWORK_DDOS_ADAPTIVE_PROTECTION`] [`--network-ddos-protection`=`NETWORK_DDOS_PROTECTION`] [`--recaptcha-redirect-site-key`=`RECAPTCHA_REDIRECT_SITE_KEY`] [`--request-body-inspection-size`=`REQUEST_BODY_INSPECTION_SIZE`] [`--user-ip-request-headers`=[`USER_IP_REQUEST_HEADER`,…]] [`--clear-network-ddos-impacted-baseline-threshold` | `--network-ddos-impacted-baseline-threshold`=`NETWORK_DDOS_IMPACTED_BASELINE_THRESHOLD`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute security-policies update` is used to update security policies. 
EXAMPLES
     To update the description run this: 
    
    
    gcloud beta compute security-policies update SECURITY_POLICY --description='new description'

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the security policy to update. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the security policy. 
`--enable-layer7-ddos-defense`
     Whether to enable Cloud Armor Layer 7 DDoS Defense Adaptive Protection. 
`--json-custom-content-types`=[`CONTENT_TYPE`,…]
     A comma-separated list of custom Content-Type header values to apply JSON parsing for preconfigured WAF rules. Only applicable when JSON parsing is enabled, like ``\--json-parsing=STANDARD``. When configuring a Content-Type header value, only the type/subtype needs to be specified, and the parameters should be excluded. 
`--json-parsing`=`JSON_PARSING`
     The JSON parsing behavior for this rule. Must be one of the following values: [DISABLED, STANDARD, STANDARD_WITH_GRAPHQL]. `JSON_PARSING` must be one of: `DISABLED`, `STANDARD`, `STANDARD_WITH_GRAPHQL`. 
`--layer7-ddos-defense-auto-deploy-confidence-threshold`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_CONFIDENCE_THRESHOLD`
     Confidence threshold above which Adaptive Protection's auto-deploy takes actions 
`--layer7-ddos-defense-auto-deploy-expiration-sec`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_EXPIRATION_SEC`
     Duration over which Adaptive Protection's auto-deployed actions last 
`--layer7-ddos-defense-auto-deploy-impacted-baseline-threshold`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_IMPACTED_BASELINE_THRESHOLD`
     Impacted baseline threshold below which Adaptive Protection's auto-deploy takes actions 
`--layer7-ddos-defense-auto-deploy-load-threshold`=`LAYER7_DDOS_DEFENSE_AUTO_DEPLOY_LOAD_THRESHOLD`
     Load threshold above which Adaptive Protection's auto-deploy takes actions 
`--layer7-ddos-defense-rule-visibility`=`VISIBILITY_TYPE`
     The visibility type indicates whether the rules are opaque or transparent. `VISIBILITY_TYPE` must be one of: `STANDARD`, `PREMIUM`. 
`--log-level`=`LOG_LEVEL`
     The level of detail to display for WAF logging. `LOG_LEVEL` must be one of: `NORMAL`, `VERBOSE`. 
`--network-ddos-adaptive-protection`=`NETWORK_DDOS_ADAPTIVE_PROTECTION`
     The DDoS adaptive protection level for network load balancing and instances with external IPs. `NETWORK_DDOS_ADAPTIVE_PROTECTION` must be one of: `DISABLED`, `ENABLED`, `PREVIEW`. 
`--network-ddos-protection`=`NETWORK_DDOS_PROTECTION`
     The DDoS protection level for network load balancing and instances with external IPs. `NETWORK_DDOS_PROTECTION` must be one of: `STANDARD`, `ADVANCED`, `ADVANCED_PREVIEW`. 
`--recaptcha-redirect-site-key`=`RECAPTCHA_REDIRECT_SITE_KEY`
     The reCAPTCHA site key to be used for rules using the ``redirect`` action and the ``google-recaptcha`` redirect type under the security policy. 
`--request-body-inspection-size`=`REQUEST_BODY_INSPECTION_SIZE`
     Maximum request body inspection size. `REQUEST_BODY_INSPECTION_SIZE` must be one of: `8KB`, `16KB`, `32KB`, `48KB`, `64KB`. 
`--user-ip-request-headers`=[`USER_IP_REQUEST_HEADER`,…]
     A comma-separated list of request header names to use for resolving the caller's user IP address. 
At most one of these can be specified: 

`--clear-network-ddos-impacted-baseline-threshold`
     If provided, clears the Network DDoS impacted baseline threshold from the security policy. 
`--network-ddos-impacted-baseline-threshold`=`NETWORK_DDOS_IMPACTED_BASELINE_THRESHOLD`
     DDoS Protection for Network Load Balancers (and VMs with public IPs) builds DDoS mitigations that minimize collateral damage. It quantifies this as the fraction of a non-abuse baseline that's inadvertently blocked. Rules whose collateral damage exceeds ddosImpactedBaselineThreshold will not be deployed. Using a lower value will prioritize keeping collateral damage low, possibly at the cost of its effectiveness in rate limiting some or all of the attack. It should typically be unset, so Advanced DDoS (and Adaptive Protection) uses the best mitigation it can find. Setting the threshold is advised if there are logs for false positive detections with high collateral damage, and will cause Advanced DDoS to attempt to find a less aggressive rule that satisfies the constraint. If a suitable rule cannot be found, the system falls back to either no mitigation for smaller attacks or broader network throttles for larger ones. 
At most one of these can be specified: 

`--global`
     If set, the security policy is global. 
`--region`=`REGION`
     Region of the security policy to update. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute security-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/update)
    
    
    [gcloud alpha compute security-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies/update)
    
    
    [gcloud preview compute security-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
