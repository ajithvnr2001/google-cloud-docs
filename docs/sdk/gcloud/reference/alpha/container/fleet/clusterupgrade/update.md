---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/clusterupgrade/update/
title: gcloud alpha container fleet clusterupgrade update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:53:03.105217+00:00
---

# gcloud alpha container fleet clusterupgrade update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/clusterupgrade/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container fleet clusterupgrade update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container fleet clusterupgrade update - update the clusterupgrade feature for a fleet within a given project 
SYNOPSIS
    

`gcloud alpha container fleet clusterupgrade update` [`--default-upgrade-soaking`=`DEFAULT_UPGRADE_SOAKING`] [`--remove-upgrade-soaking-overrides` | `--add-upgrade-soaking-override`=`ADD_UPGRADE_SOAKING_OVERRIDE` `--upgrade-selector`=[`name`=`NAME`],[`version`=`VERSION`]] [`--reset-upstream-fleet` | `--upstream-fleet`=`UPSTREAM_FLEET`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the clusterupgrade feature for a fleet within a given project. 
EXAMPLES
     To update the clusterupgrade feature for the current fleet, run: 
    
    
    gcloud alpha container fleet clusterupgrade update --default-upgrade-soaking=DEFAULT_UPGRADE_SOAKING

FLAGS
    

`--default-upgrade-soaking`=`DEFAULT_UPGRADE_SOAKING`
     Note: This flag only applies to Rollout Sequencing v1, not Rollout Sequencing v2 (which uses custom stages). If using Rollout Sequencing v1 and this flag is not provided, a default value of 7 days will be used. 

Configures the default soaking duration for each upgrade propagating through the current fleet to become "COMPLETE". Soaking begins after all clusters in the fleet are on the target version, or after 30 days if all cluster upgrades are not complete. Once an upgrade state becomes "COMPLETE", it will automatically be propagated to the downstream fleet. Max is 30 days. 

To configure Rollout Sequencing for a fleet, this attribute must be set. To do this while specifying a default soaking duration of 7 days, run: 
    
    
    gcloud alpha container fleet clusterupgrade update --default-upgrade-soaking=7d

At most one of these can be specified: 

`--remove-upgrade-soaking-overrides`
     Removes soaking time overrides for all upgrades propagating through the current fleet. Consequently, all upgrades will follow the soak time configured by `--default-upgrade-soaking` until new overrides are configured with `--add_upgrade_soaking_override` and `--upgrade_selector`. 

To remove all configured soaking time overrides, run: 
    
    
    gcloud alpha container fleet clusterupgrade update --remove-upgrade-soaking-overrides

Or at least one of these can be specified: 

Upgrade soaking override. 

Defines a specific soaking time override for a particular upgrade propagating through the current fleet that supercedes the default soaking duration configured by `--default-upgrade-soaking`. 

To set an upgrade soaking override of 12 hours for the upgrade with name, `k8s_control_plane`, and version, `1.23.1-gke.1000`, run: 
    
    
    gcloud alpha container fleet clusterupgrade update               --add-upgrade-soaking-override=12h               --upgrade-selector=name="k8s_control_plane",version="1.23.1-gke.1000"

`--add-upgrade-soaking-override`=`ADD_UPGRADE_SOAKING_OVERRIDE`
     Overrides the soaking time for a particular upgrade name and version propagating through the current fleet. Set soaking to 0 days to bypass soaking and fast-forward the upgrade to the downstream fleet. 

See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--upgrade-selector`=[`name`=`NAME`],[`version`=`VERSION`]
     Name and version of the upgrade to be overridden where version is a full GKE version. Currently, name can be either `k8s_control_plane` or `k8s_node`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

At most one of these can be specified: 

`--reset-upstream-fleet`
     Clears the relationship between the current fleet and its upstream fleet in the rollout sequence. 

To remove the link between the current fleet and its upstream fleet, run: 
    
    
    gcloud alpha container fleet clusterupgrade update --reset-upstream-fleet

`--upstream-fleet`=`UPSTREAM_FLEET`
     The upstream fleet. GKE will finish upgrades on the upstream fleet before applying the same upgrades to the current fleet. 

To configure the upstream fleet, run: 
    
    
    gcloud alpha container fleet clusterupgrade update             --upstream-fleet={upstream_fleet}

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container fleet clusterupgrade update](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/clusterupgrade/update)
    
    
    [gcloud beta container fleet clusterupgrade update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/clusterupgrade/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
