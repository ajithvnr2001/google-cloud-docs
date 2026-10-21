---
url: https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/create/
title: gcloud looker instances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:12:48.726969+00:00
---

# gcloud looker instances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud looker instances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud looker instances create - create a Looker instance 
SYNOPSIS
    

`gcloud looker instances create` (`INSTANCE` : `--region`=`REGION`) `--edition`=`EDITION` `--oauth-client-id`=`OAUTH_CLIENT_ID` `--oauth-client-secret`=`OAUTH_CLIENT_SECRET` [`--accelerated-security-patch-enabled`] [`--async`] [`--catalog-integration-opt-out`] [`--class-type`=`CLASS_TYPE`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--fips-enabled`] [`--kms-key`=`KMS_KEY`] [`--no-public-ip-enabled`] [`--release-channel`=`RELEASE_CHANNEL`] [`--consumer-network`=`CONSUMER_NETWORK` `--private-ip-enabled` : `--reserved-range`=`RESERVED_RANGE`] [`--deny-maintenance-period-end-date`=`DENY_MAINTENANCE_PERIOD_END_DATE` `--deny-maintenance-period-start-date`=`DENY_MAINTENANCE_PERIOD_START_DATE` `--deny-maintenance-period-time`=`DENY_MAINTENANCE_PERIOD_TIME`] [`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY` `--maintenance-window-time`=`MAINTENANCE_WINDOW_TIME`] [`--psc-enabled` : `--psc-allowed-vpcs`=[`PSC_ALLOWED_VPCS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Looker instance. 

This command can fail for the following reasons: 

  * An instance with the same name already exists. 
  * The active account does not have permission to create instances. 
  * `--async` flag is not passed 


EXAMPLES
     To create a basic tier instance with the name `my-looker-instance` in region `us-central-1` with an edition of `LOOKER_CORE_STANDARD`, run: 
    
    
    gcloud looker instances create my-looker-instance --region=us-central1 --edition="core-standard" --oauth-client-id='looker' --oauth-client-secret='looker' --async

Note: It is `recommended` that the `--async` argument is provided when creating a Looker instance. 

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Looker instance you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Looker region of the instance. Overrides the default looker/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `looker/region`. 


REQUIRED FLAGS
    

`--edition`=`EDITION`
     The edition of the Looker instance. `EDITION` must be one of: 

`core-embed-annual`
     A Looker (Google Cloud core) product for deploying and maintaining external analytics and custom applications at scale. This can be purchased via an annual contract. 
`core-enterprise-annual`
     A Looker (Google Cloud core) product with enhanced security features for a wide variety of internal BI and analytics use cases. This can be purchased via an annual contract. 
`core-l-annual`
     A Subscription Enterprise Plus Annual edition of Looker (Google Cloud core) product. For enterprise-sized rollouts involving large-scale implementations. 
`core-m-annual`
     A Subscription Enterprise Annual edition of Looker (Google Cloud core) product. Designed for medium-sized ongoing business use cases. 
`core-s-annual`
     A Subscription Standard Annual edition of Looker (Google Cloud core) product. Intended for a single-team project or a standalone startup. 
`core-standard`
     A Looker (Google Cloud core) product for small organizations or teams with fewer than 50 users. This will be billed monthly while the instance is active. 
`core-standard-annual`
     A Looker (Google Cloud core) product for small organizations or teams with fewer than 50 users. This can be purchased via an annual contract. 
`core-trial`
     Trial edition of Looker. 
`core-trial-embed`
     An embed trial edition of Looker (Google Cloud core) product. 
`core-trial-enterprise`
     An enterprise trial edition of Looker (Google Cloud core) product. 
`core-trial-l-annual`
     A Subscription Trial Enterprise Plus Annual edition of Looker (Google Cloud core) product. For enterprise-sized rollouts involving large-scale implementations. 
`core-trial-m-annual`
     A Subscription Trial Enterprise Annual edition of Looker (Google Cloud core) product. Designed for medium-sized ongoing business use cases. 
`core-trial-s-annual`
     A Subscription Trial Standard Annual edition of Looker (Google Cloud core) product. Intended for a single-team project or a standalone startup. 
`core-trial-standard`
     A standard trial edition of Looker (Google Cloud core) product. 
`core-trial-xl-annual`
     A Subscription Trial Enterprise Ultra Annual edition of Looker (Google Cloud core) product. This is the largest tier for massive enterprise deployments. 
`core-xl-annual`
     A Subscription Enterprise Ultra Annual edition of Looker (Google Cloud core) product. This is the largest tier for massive enterprise deployments. 
`nonprod-core-embed-annual`
     A non-production edition of Looker (Google Cloud core) product for deploying and maintaining external analytics and custom applications at scale. This can be purchased via an annual contract. 
`nonprod-core-enterprise-annual`
     A non-production edition of Looker (Google Cloud core) product with enhanced security features for a wide variety of internal BI and analytics use cases. This can be purchased via an annual contract. 
`nonprod-core-l-annual`
     A Non-prod Subscription Enterprise Plus Annual edition of Looker (Google Cloud core) product. For enterprise-sized rollouts involving large-scale implementations. 
`nonprod-core-m-annual`
     A Non-prod Subscription Enterprise Annual edition of Looker (Google Cloud core) product. Designed for medium-sized ongoing business use cases. 
`nonprod-core-standard-annual`
     A non-production edition of Looker (Google Cloud core) product for small organizations or teams with fewer than 50 users. This can be purchased via an annual contract. 
`nonprod-core-xl-annual`
     A Non-prod Subscription Enterprise Ultra Annual edition of Looker (Google Cloud core) product. This is the largest tier for massive enterprise deployments. 
`--oauth-client-id`=`OAUTH_CLIENT_ID`
     The client ID from an external OAuth application. 

OAuth Application Credentials - Looker Instance OAuth login settings. Setup an OAuth app that will allow users to authenticate and access the instance. For more information see: <https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred>

`--oauth-client-secret`=`OAUTH_CLIENT_SECRET`
     The client secret from an external OAuth application. 

OAuth Application Credentials - Looker Instance OAuth login settings. Setup an OAuth app that will allow users to authenticate and access the instance. For more information see: <https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred>

OPTIONAL FLAGS
    

Accelerated Security Patch - Looker (Google Cloud core) releases security patches to your instance. 
`--accelerated-security-patch-enabled`
     If specified, accelerated security patch will be enabled, otherwise it will be disabled by default. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Catalog Integration - Catalog Integration is a feature that allows Looker to integrate with Universal Dataplex Catalog. 
`--catalog-integration-opt-out`
     If specified, catalog integration will be disabled, otherwise it will be enabled by default. 
`--class-type`=`CLASS_TYPE`
     The class type of the Looker instance. `CLASS_TYPE` must be one of: `p1`, `r1`. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--fips-enabled`
     This specifies whether FIPS is enabled on the Looker instance. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the Looker instance and backups. The 'Looker Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 


`--public-ip-enabled`
     This specifies whether public IP is enabled on the Looker instance. Enabled by default, use `--no-public-ip-enabled` to disable. 
Release Channel - Looker (Google Cloud core) releases updates to your instance through release channels. 
`--release-channel`=`RELEASE_CHANNEL`
     The selected release channel for the instance. For more details on release channels, review <https://cloud.google.com/looker/docs/looker-core-release-process#release_channels>. `RELEASE_CHANNEL` must be one of: 

`no-channel`
     Maintains existing monthly update cadence and features. This channel will remain available for a limited period to prevent immediate deployment disruptions. 
`rapid`
     Access new features as soon as they are released. Use the Rapid channel to thoroughly test upcoming versions in your development or non-production environments before they roll out to production. Note: This channel is excluded from the Looker SLA. 
`regular`
     Maintain a reliable balance between feature availability and platform stability. Versions in the Regular channel are qualified over a longer period and are recommended for critical production workloads. 
`stable`
     Versions in the Stable channel prioritize stability and are ideal for production workloads that require the most conservative update schedule. 
Private IP - Assigns an internal, Google-hosted VPC IP address. Private IP connectivity requires additional APIs and permissions. Private IP cannot be disabled once it has been enabled. If enabled, `consumer-network` must be assigned. 
`--consumer-network`=`CONSUMER_NETWORK`
     The network name within the consumer project. This MUST be delared if enabling private IP. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--private-ip-enabled`
     This specifies whether private IP (PSA) is enabled on the Looker instance. This flag is for creating a PSA (Private Service Access) instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--reserved-range`=`RESERVED_RANGE`
     The name of a reserved IP address range within the consumer network to be used for private service access connection. 
Deny Maintanence Period - You must allow at least 48 hours of maintenance availability in a 60-day rolling window. Only contiguous availability windows of at least two hours are considered. When setting a maintenance exclusion please be aware that excluding application upgrades cannot exceed 60-days and excluding infrastructure upgrades cannot exceed 90-days. 
`--deny-maintenance-period-end-date`=`DENY_MAINTENANCE_PERIOD_END_DATE`
     End date of the deny maintenance period in format: YYYY-MM-DD 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--deny-maintenance-period-start-date`=`DENY_MAINTENANCE_PERIOD_START_DATE`
     Start date of the deny maintenance period in format: YYYY-MM-DD 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--deny-maintenance-period-time`=`DENY_MAINTENANCE_PERIOD_TIME`
     Time in UTC when the period starts and ends. A valid time of day must be specified in 24hr format (ex: 13:00, 17:30, 23:45). 

This flag argument must be specified if any of the other arguments in this group are specified. 

Maintenance Window - Maintenance typically only takes place once every few months, and requires your instance to be restarted while updates are made, which disrupts service briefly. 
`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY`
     Day of week for maintenance window, in UTC time zone. `MAINTENANCE_WINDOW_DAY` must be one of: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--maintenance-window-time`=`MAINTENANCE_WINDOW_TIME`
     Hour of day for maintenance window, in UTC time zone. A valid time of day must be specified in 24hr format (ex: 13:00, 17:30, 23:45). Maintenance will be scheduled within 60 minutes. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Private Service Connect - Private Service Connect allows private consumption of services across VPC networks that belong to different groups, teams, projects, or organizations. 
`--psc-enabled`
     This specifies whether Private Service Connect (PSC) is enabled on the Looker instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--psc-allowed-vpcs`=[`PSC_ALLOWED_VPCS`,…]
     List of VPCs that are allowed ingress into the Looker instance. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `looker/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/looker/docs/reference/rest/>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha looker instances create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/looker/instances/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
