---
url: https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/update/
title: gcloud looker instances update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:12:49.527881+00:00
---

# gcloud looker instances update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud looker instances update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud looker instances update - update a Looker instance 
SYNOPSIS
    

`gcloud looker instances update` (`INSTANCE` : `--region`=`REGION`) [`--accelerated-security-patch-enabled`] [`--allowed-email-domains`=[`ALLOWED_EMAIL_DOMAINS`,…]] [`--async`] [`--catalog-integration-opt-out`] [`--class-type`=`CLASS_TYPE`] [`--custom-domain`=`CUSTOM_DOMAIN`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--linked-lsp-project-number`=`LINKED_LSP_PROJECT_NUMBER`] [`--public-ip-enabled`] [`--release-channel`=`RELEASE_CHANNEL`] [`--add-developer-users`=`ADD_DEVELOPER_USERS` `--add-standard-users`=`ADD_STANDARD_USERS` `--add-viewer-users`=`ADD_VIEWER_USERS`] [`--clear-periodic-export-config` | `--periodic-export-gcs-uri`=`PERIODIC_EXPORT_GCS_URI` `--periodic-export-kms-key`=`PERIODIC_EXPORT_KMS_KEY` `--periodic-export-start-time`=`PERIODIC_EXPORT_START_TIME`] [`--clear-psc-allowed-vpcs` | `--psc-allowed-vpcs`=[`PSC_ALLOWED_VPCS`,…] `--clear-psc-service-attachments` | `--psc-service-attachment`=[`attachment`=`ATTACHMENT`],[`domain`=`DOMAIN`],[`multiple-domains`=`MULTIPLE-DOMAINS`]] [`--deny-maintenance-period-end-date`=`DENY_MAINTENANCE_PERIOD_END_DATE` `--deny-maintenance-period-start-date`=`DENY_MAINTENANCE_PERIOD_START_DATE` `--deny-maintenance-period-time`=`DENY_MAINTENANCE_PERIOD_TIME`] [`--egress-enabled` `--egress-fqdns`=[`EGRESS_FQDNS`,…] `--marketplace-enabled`] [`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY` `--maintenance-window-time`=`MAINTENANCE_WINDOW_TIME`] [`--oauth-client-id`=`OAUTH_CLIENT_ID` `--oauth-client-secret`=`OAUTH_CLIENT_SECRET`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the metadata and/or configuration parameters of a Looker instance. 

This command can fail for the following reasons: 

  * The instance specified does not exist. 
  * The active account does not have permission to update the given instance. 


EXAMPLES
     To update the maintenance window to Sunday at 11:00 PM for a Looker instance with the name `my-looker-instance`, run: 
    
    
    gcloud looker instances update my-looker-instance --maintenance-window-day=sunday --maintenance-window-time='23:00' --async

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Looker instance you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

Accelerated Security Patch - Looker (Google Cloud core) releases security patches to your instance. 
`--accelerated-security-patch-enabled`
     If specified, accelerated security patch will be enabled. Use `--no-accelerated-security-patch-enabled` to disable it. 
Email Domain Allowlist for Scheduled Content - Define the email domains to which your users can deliver Looker (Google Cloud core) content. 
`--allowed-email-domains`=[`ALLOWED_EMAIL_DOMAINS`,…]
     This specifies the entire allowed email domain list. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Catalog Integration - Catalog Integration is a feature that allows Looker to integrate with Universal Dataplex Catalog. 
`--catalog-integration-opt-out`
     If specified, catalog integration will be disabled. Use `--no-catalog-integration-opt-out` to re-enable it. 
`--class-type`=`CLASS_TYPE`
     The class type of the Looker instance. `CLASS_TYPE` must be one of: `p1`, `r1`. 
Custom Domains - Looker (Google Cloud core) lets you serve your application through a custom domain. If you use a custom domain, Google will provide a managed auto-renewing SSL certificate for security. 

DNS changes can take up to 24 hours to take effect. Your SSL certificate will take several minutes to activate. Note that you must get the Type A DNS Record from the Google Cloud Console and update with your domain registrar for your custom domain to work properly. 

`--custom-domain`=`CUSTOM_DOMAIN`
     Domain name wanted to serve the Looker instance. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--linked-lsp-project-number`=`LINKED_LSP_PROJECT_NUMBER`
     The Looker Studio Pro project number to be linked. 
`--public-ip-enabled`
     This specifies whether public IP is enabled on the Looker instance. 
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
User Allocations - There are ten Standard and two Developer users included in the cost of the product. You can allocate additional Standard, Viewer, and Developer users for this instance. It is an optional step and can be modified later. 

With the Standard edition of Looker (Google Cloud core), you can provision up to 50 total users, distributed across Viewer, Standard, and Developer. 

`--add-developer-users`=`ADD_DEVELOPER_USERS`
     Number of additional Developer Users to allocate to the Looker Instance. 
`--add-standard-users`=`ADD_STANDARD_USERS`
     Number of additional Standard Users to allocate to the Looker Instance. 
`--add-viewer-users`=`ADD_VIEWER_USERS`
     Number of additional Viewer Users to allocate to the Looker Instance. 
At most one of these can be specified: 

`--clear-periodic-export-config`
     Clears all periodic export configuration from the instance. 
Or at least one of these can be specified: 

Configuration for periodic export. All flags in this group must be provided to enable or update the configuration. 
`--periodic-export-gcs-uri`=`PERIODIC_EXPORT_GCS_URI`
     Cloud Storage bucket URI for periodic export. Format: gs://{bucket_name} 
`--periodic-export-kms-key`=`PERIODIC_EXPORT_KMS_KEY`
     Name of the CMEK key in KMS. Format: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key} 
`--periodic-export-start-time`=`PERIODIC_EXPORT_START_TIME`
     Time in UTC when the periodic export job starts. A valid time of day must be specified in 24hr format (ex: 13:00, 17:30, 23:45). 
Private Service Connect - Private Service Connect allows the Looker Instance to be reached via a private connection from inside a VPC network, and for the Looker Instance to connect to managed services via private connections. 
At most one of these can be specified: 

`--clear-psc-allowed-vpcs`
     Remove all service attachments from the PSC config of the instance. 
`--psc-allowed-vpcs`=[`PSC_ALLOWED_VPCS`,…]
     List of VPCs that are allowed ingress into the Looker instance. 
At most one of these can be specified: 

`--clear-psc-service-attachments`
     Remove all allowed VPCs from the PSC config of the instance. 
`--psc-service-attachment`=[`attachment`=`ATTACHMENT`],[`domain`=`DOMAIN`],[`multiple-domains`=`MULTIPLE-DOMAINS`]
     Service attachments representing egress connections for the Looker instance. This flag can be repeated. (Example: --psc-service-attachment domain="mydomain.com",attachment="projects/my-project/regions/us-east1/serviceAttachments/sa" \--psc-service-attachments domain="mydomain2.com",attachment="projects/my-project/regions/us-east1/serviceAttachments/sa2") 

You can also assign multiple domains to a single service attachment. (Example: \--psc-service-attachment multiple-domains="mydomain.com;mydomain2.com",attachment="projects/my-project/regions/us-east1/serviceAttachments/sa") 

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

Controlled Egress - Controlled egress allows you to egress data from a Looker (Google Cloud core) instance to a third party service provider. 
`--egress-enabled`
     This specifies whether controlled egress is enabled on the Looker instance. To disable controlled egress, use the `--no-egress-enabled` flag. 
`--egress-fqdns`=[`EGRESS_FQDNS`,…]
     List of FQDNs that are allowed to egress from the Looker instance. Example: `--egress-fqdns="github.com,my.salesforce.com"`. To clear all egress FQDNs, use `--egress-fqdns=""`. 
`--marketplace-enabled`
     This specifies whether marketplace is enabled for controlled egress on the Looker instance. To disable marketplace for controlled egress, use the `--no-marketplace-enabled` flag. 
Maintenance Window - Maintenance typically only takes place once every few months, and requires your instance to be restarted while updates are made, which disrupts service briefly. 
`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY`
     Day of the week for the maintenance window, in UTC time zone. `MAINTENANCE_WINDOW_DAY` must be one of: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--maintenance-window-time`=`MAINTENANCE_WINDOW_TIME`
     Hour of day for maintenance window, in UTC time zone. A valid time of day must be specified in 24hr format (ex: 13:00, 17:30, 23:45). Maintenance will be scheduled within 60 minutes. To set the maintenance-window-time` attribute: 

  * provide the argument 

`\--maintenance-window-time` on the command line. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`
OAuth Application Credentials - Looker Instance OAuth login settings. Setup an OAuth app that will allow users to authenticate and access the instance. For more information see: <https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred>
\--oauth-client-id`=`OAUTH_CLIENT_ID``
     The client ID from an external OAuth application. 

This flag argument must be specified if any of the other arguments in this group are specified. 

\--oauth-client-secret`=`OAUTH_CLIENT_SECRET``
     The client secret from an external OAuth application. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `looker/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/looker/docs/reference/rest/>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha looker instances update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/looker/instances/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
