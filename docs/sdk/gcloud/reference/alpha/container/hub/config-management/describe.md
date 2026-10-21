---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/config-management/describe/
title: gcloud alpha container hub config-management describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:34:26.598020+00:00
---

# gcloud alpha container hub config-management describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/config-management/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container hub config-management describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container hub config-management describe - describe the Config Management feature 
SYNOPSIS
    

`gcloud alpha container hub config-management describe` [`--view`=`VIEW` : `--filter`=`EXPRESSION` `--sort-by`=[`FIELD`,…]] [`--memberships`=[`MEMBERSHIPS`,…] : `--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe the Config Management feature. 
EXAMPLES
     To describe the entire Config Management feature, run: 
    
    
    gcloud alpha container hub config-management describe

To describe select membership configurations, run: 
    
    
    gcloud alpha container hub config-management describe --memberships=example-membership-1,example-membership-2

To list the membership configurations, run: 
    
    
    gcloud alpha container hub config-management describe --view=list

> MEMBERSHIP | LOCATION | STATUS | INSTALL_STATE | STOP_STATE | SYNC_STATE | VERSION | SYNCED_TO_FLEET_DEFAULT  
> ---|---|---|---|---|---|---|---  
> example-membership-1 | asia-east1 | OK | CONFIG_SYNC_NOT_INSTALLED |  | NOT_INSTALLED |  | FLEET_DEFAULT_NOT_CONFIGURED  
> example-membership-2 | us-central1 | OK | CONFIG_SYNC_INSTALLED | NOT_STOPPED | SYNCED | 1.22.0 | FLEET_DEFAULT_NOT_CONFIGURED  
> example-membership-3 | us-central1 | ERROR | CONFIG_SYNC_INSTALLED | NOT_STOPPED | ERROR | 1.21.3 | FLEET_DEFAULT_NOT_CONFIGURED  
  
FLAGS
    

`--view`=`VIEW`
     View of the feature. `VIEW` must be one of: 

`config`
     Membership configuration in a format that is passable to the `--config` flag on the `update` command. Note that the configuration includes any deprecated fields that are set. Errors if `--memberships` does not specify exactly one membership. 

To describe the configuration for a given membership, run: 
    
    
    gcloud alpha container hub config-management describe --view=config --memberships=example-membership-1

`fleet-default-member-config`
     [Fleet-default membership configuration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features) in a format that is passable to the `--fleet-default-member-config` flag on the `enable` and `update` commands. Note that the configuration includes any deprecated fields that are set. Errors if the fleet-default membership configuration is not set on the feature. Errors if specified with the `--memberships` flag. Tab to auto-complete this flag value. 
`full`
     Default view. Prints the entire feature. 
`list`
     List of membership configurations. Default format is a table summary. 

The `SYNCED_TO_FLEET_DEFAULT` column may display `UNKNOWN` for any membership whose configuration has not been updated since the [fleet-default membership configuration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features) enablement. 

To view the underlying configurations instead of the table summary for select memberships, run: 
    
    
    gcloud alpha container hub config-management describe --view=list --format=yaml --memberships=example-membership-1,example-membership-2

List command flags. Only specify when `--view=list`. Does not include support for `--limit`. 
`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 

To filter for memberships with an overall status of `ERROR`, use the ``COLUMN~VALUE`` pattern and run: 
    
    
    gcloud alpha container hub config-management describe --view=list --filter=STATUS~ERROR

To filter for memberships that are synced to the fleet-default membership configuration, run: 
    
    
    gcloud alpha container hub config-management describe --view=list --filter="spec.origin.type.synced_to_fleet_default()~YES"

`SYNCED_TO_FLEET_DEFAULT` is the only column that requires filtering on the underlying configuration field instead of the column name. An alternative is to `--sort-by=SYNCED_TO_FLEET_DEFAULT` and filter by eye. 

To filter on a configuration field not in the table summary, in this case the Config Sync repo, run: 
    
    
    gcloud alpha container hub config-management describe --view=list --format=yaml --filter="spec.configmanagement.configSync.git.syncRepo~<https://\>
    github.com/GoogleCloudPlatform/anthos-config-management-samples.git"

`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 

The default sort order is by the `LOCATION`, then `MEMBERSHIP` table columns. 

To sort the table by `VERSION` instead, run: 
    
    
    gcloud alpha container hub config-management describe --view=list --sort-by=VERSION

To sort by a configuration field not in the table summary, in this case the Config Sync repo, and print its values in a table, run: 
    
    
    gcloud alpha container hub config-management describe --view=list --sort-by="spec.configmanagement.configSync.git.syncRepo" --format="table(MEMBERSHIP,LOCATION,spec.configmanagement.configSync.git.syncRepo:label=REPO)"

MEMBERSHIP FLAGS
    

Memberships to print configurations for. Errors if a specified membership does not have a configuration for this feature. 
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


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container hub config-management describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/config-management/describe)
    
    
    [gcloud beta container hub config-management describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
