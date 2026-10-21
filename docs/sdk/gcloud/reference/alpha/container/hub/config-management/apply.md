---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/config-management/apply/
title: gcloud alpha container hub config-management apply \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:03:41.937458+00:00
---

# gcloud alpha container hub config-management apply  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/config-management/apply/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container hub config-management apply Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container hub config-management apply - update a Config Management feature spec 
SYNOPSIS
    

`gcloud alpha container hub config-management apply` (`--origin`=`ORIGIN` | [`--config`=`CONFIG` : `--version`=`VERSION`]) [`--membership`=`MEMBERSHIP` : `--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a membership configuration for the Config Management feature in a fleet. This command errors if the Config Management feature is not enabled on the fleet. 
EXAMPLES
     To apply the [fleet-default membership configuration](https://cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features) to `MEMBERSHIP_NAME`, run: 
    
    
    gcloud alpha container hub config-management apply --membership=MEMBERSHIP_NAME --origin=FLEET

To apply a membership configuration as a YAML file, prepare [apply-spec.yaml](https://cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields#example_gcloud_apply_spec) then run: 
    
    
    gcloud alpha container hub config-management apply --membership=MEMBERSHIP_NAME --config=APPLY-SPEC.YAML --version=VERSION

REQUIRED FLAGS
    

Update the membership configuration either to the [fleet-default membership configuration](https://cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features) with `--origin` or to a user-provided configuration with `--config` and `--version`. 

Exactly one of these must be specified: 

`--origin`=`ORIGIN`
     Updates the configuration of the target membership to the current [fleet-default membership configuration](https://cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features). Errors if fleet-default membership configuration is not enabled; see the `enable` command for more details. `ORIGIN` must be (only one value is supported): `FLEET`. 
Or at least one of these can be specified: 

Provide the entire membership configuration to update with `--config` and `--version`. 
`--config`=`CONFIG`
     Path to YAML file that contains the configuration to update the target membership to. The file accepts the [following fields](https://cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--version`=`VERSION`
     Version of Config Management. Equivalent to the [`spec.version`](https://cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields#common) field in the `--config` file. Provides `--config` with a version in the absence of `spec.version`. Cannot specify this flag without `--config`; cannot set both this flag and `spec.version`. See [`spec.version`](https://cloud.google.com/anthos-config-management/docs/reference/gcloud-apply-fields#common) for more details. 
OPTIONAL FLAGS
    

Membership resource - The group of arguments defining a membership. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--membership` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--membership`=`MEMBERSHIP`
     ID of the membership or fully qualified identifier for the membership. 

To set the `membership` attribute: 

  * provide the argument `--membership` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location for the membership. 

To set the `location` attribute: 

  * provide the argument `--membership` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta container hub config-management apply](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/apply)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
