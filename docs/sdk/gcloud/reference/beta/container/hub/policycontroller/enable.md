---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/enable/
title: gcloud beta container hub policycontroller enable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:05:16.062611+00:00
---

# gcloud beta container hub policycontroller enable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub policycontroller enable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub policycontroller enable - enable Policy Controller Feature 
SYNOPSIS
    

`gcloud beta container hub policycontroller enable` [`--all-memberships` | [`--memberships`=[`MEMBERSHIPS`,…] : `--location`=`LOCATION`] `--audit-interval`=`AUDIT_INTERVAL` `--constraint-violation-limit`=`CONSTRAINT_VIOLATION_LIMIT` `--no-content` `--no-default-bundles` `--version`=`VERSION` `--clear-exemptable-namespaces` | `--exemptable-namespaces`=`EXEMPTABLE_NAMESPACES` `--log-denies` | `--no-log-denies` `--monitoring`=`MONITORING` | `--no-monitoring` `--mutation` | `--no-mutation` `--referential-rules` | `--no-referential-rules` | `--fleet-default-member-config`=`FLEET_DEFAULT_MEMBER_CONFIG` | `--no-fleet-default-member-config`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Enables the Policy Controller Feature in a fleet. 
EXAMPLES
     To enable the Policy Controller Feature, run: 
    
    
    gcloud beta container hub policycontroller enable

FLAGS
    

At most one of these can be specified: 

Membership flags. 

At most one of these can be specified: 

`--all-memberships`
     If supplied, apply to all Policy Controllers memberships in the fleet. 
Or at least one of these can be specified: 

Membership resource - The group of arguments defining one or more memberships. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--memberships` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--memberships`=[`MEMBERSHIPS`,…]
     IDs of the memberships or fully qualified identifiers for the memberships. 

To set the `memberships` attribute: 

  * provide the argument `--memberships` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location for the memberships. 

To set the `location` attribute: 

  * provide the argument `--memberships` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


`--audit-interval`=`AUDIT_INTERVAL`
     How often Policy Controller will audit resources, in seconds. 
`--constraint-violation-limit`=`CONSTRAINT_VIOLATION_LIMIT`
     The number of violations stored on the constraint resource. Must be greater than 0\. 
`--no-content`
     If set, Policy content, including the template library and policy bundles, will not be installed. 
`--no-default-bundles`
     If set, skip installing the default bundle of policy-essentials. 
`--version`=`VERSION`
     The version of Policy Controller to install; defaults to latest version. 
Exemptable Namespace flags. 

At most one of these can be specified: 

`--clear-exemptable-namespaces`
     Removes any namespace exemptions, enabling Policy Controller on all namespaces. Setting this flag will overwrite currently exempted namespaces, not append. 
`--exemptable-namespaces`=`EXEMPTABLE_NAMESPACES`
     Namespaces that Policy Controller should ignore, separated by commas if multiple are supplied. 
Log Denies flags. 

At most one of these can be specified: 

`--log-denies`
     If set, log all denies and dry run failures. (To disable, use --no-log-denies) 
`--no-log-denies`
     If set, disable all log denies. 
Monitoring flags. 

At most one of these can be specified: 

`--monitoring`=`MONITORING`
     Monitoring backend options Policy Controller should export metrics to, separated by commas if multiple are supplied. Setting this flag will overwrite currently enabled backends, not append. Options: prometheus, cloudmonitoring 
`--no-monitoring`
     Include this flag to disable the monitoring configuration of Policy Controller. 
Mutation flags. 

At most one of these can be specified: 

`--mutation`
     If set, enable support for mutation. (To disable, use --no-mutation) 
`--no-mutation`
     Disables mutation support. 
Referential Rules flags. 

At most one of these can be specified: 

`--referential-rules`
     If set, enable support for referential constraints. (To disable, use \--no-referential-rules) 
`--no-referential-rules`
     Disables referential rules support. 
Flags for setting Fleet Default Configuration files. 

At most one of these can be specified: 

`--fleet-default-member-config`=`FLEET_DEFAULT_MEMBER_CONFIG`
     The path to a policy-controller.yaml configuration file. If specified, this configuration will become the default Policy Controller configuration for all memberships in your fleet. It can be overridden with a membership-specific configuration by using the the `Update` command. 
    
    
    To enable the Policy Controller Feature with a fleet-level default
    membership configuration, run:
    
    
    gcloud beta container hub policycontroller enable --fleet-default-member-config=/path/to/policy-controller.yaml

`--no-fleet-default-member-config`
     Removes the fleet default configuration for policy controller. Memberships configured with the fleet default will maintain their current configuration. 
    
    
    gcloud beta container hub policycontroller enable --no-fleet-default-member-config

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub policycontroller enable](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/enable)
    
    
    [gcloud alpha container hub policycontroller enable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/policycontroller/enable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
