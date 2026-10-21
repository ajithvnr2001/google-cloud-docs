---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/update/
title: gcloud beta container hub policycontroller update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:52:44.458353+00:00
---

# gcloud beta container hub policycontroller update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub policycontroller update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub policycontroller update - updates the configuration of Policy Controller Feature 
SYNOPSIS
    

`gcloud beta container hub policycontroller update` [`--all-memberships` | [`--memberships`=[`MEMBERSHIPS`,…] : `--location`=`LOCATION`] `--origin`=`ORIGIN` | `--audit-interval`=`AUDIT_INTERVAL` `--constraint-violation-limit`=`CONSTRAINT_VIOLATION_LIMIT` `--version`=`VERSION` `--clear-exemptable-namespaces` | `--exemptable-namespaces`=`EXEMPTABLE_NAMESPACES` `--log-denies` | `--no-log-denies` `--monitoring`=`MONITORING` | `--no-monitoring` `--mutation` | `--no-mutation` `--referential-rules` | `--no-referential-rules`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Updates the configuration of the Policy Controller installation 
EXAMPLES
     To change the installed version, run: 
    
    
    gcloud beta container hub policycontroller update --version=VERSION

To modify the audit interval to 120 seconds, run: 
    
    
    gcloud beta container hub policycontroller update --audit-interval=120

FLAGS
    

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


At most one of these can be specified: 

`--origin`=`ORIGIN`
     If --origin=FLEET will set the configuration of the membership to the fleet default. 

`ORIGIN` must be (only one value is supported): `FLEET`. 

Or at least one of these can be specified: 

`--audit-interval`=`AUDIT_INTERVAL`
     How often Policy Controller will audit resources, in seconds. 
`--constraint-violation-limit`=`CONSTRAINT_VIOLATION_LIMIT`
     The number of violations stored on the constraint resource. Must be greater than 0\. 
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
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub policycontroller update](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/update)
    
    
    [gcloud alpha container hub policycontroller update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/policycontroller/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
