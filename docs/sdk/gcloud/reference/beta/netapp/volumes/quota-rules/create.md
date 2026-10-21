---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/volumes/quota-rules/create/
title: gcloud beta netapp volumes quota-rules create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:54.572303+00:00
---

# gcloud beta netapp volumes quota-rules create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/volumes/quota-rules/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp volumes quota-rules create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp volumes quota-rules create - create a Cloud NetApp Volume Quota Rule 
SYNOPSIS
    

`gcloud beta netapp volumes quota-rules create` (`QUOTA_RULE` : `--location`=`LOCATION`) `--disk-limit-mib`=`DISK_LIMIT_MIB` `--type`=`TYPE` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--target`=`TARGET`] [`--volume`=`VOLUME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Cloud NetApp Volume Quota Rule. 
EXAMPLES
     The following command creates a default `user` Quota Rule named NAME using the required arguments: 
    
    
    gcloud beta netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=DEFAULT_USER_QUOTA --disk-limit-mib=200

The following command creates a default `group` Quota Rule named NAME using the required arguments: 
    
    
    gcloud beta netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=DEFAULT_GROUP_QUOTA --disk-limit-mib=200

The following command creates an individual user Quota Rule named NAME for user with UID '100' using the required arguments: 
    
    
    gcloud beta netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=INDIVIDUAL_USER_QUOTA --target=100 --disk-limit-mib=200

The following command creates an individual group Quota Rule named NAME for group with GID '1001' using the required arguments: 
    
    
    gcloud beta netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=INDIVIDUAL_GROUP_QUOTA --target=1001 --disk-limit-mib=200

POSITIONAL ARGUMENTS
    

Quota rule resource - The Quota rule to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `quota_rule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `volume` attribute: 

  * provide the argument `quota_rule` on the command line with a fully specified name; 
  * provide the argument `--volume` on the command line. 



This must be specified. 

`QUOTA_RULE`
     ID of the quota_rule or fully qualified identifier for the quota_rule. 

To set the `quota_rule` attribute: 

  * provide the argument `quota_rule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the quota_rule. 

To set the `location` attribute: 

  * provide the argument `quota_rule` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

`--disk-limit-mib`=`DISK_LIMIT_MIB`
     The disk limit in MiB for the quota rule. 
`--type`=`TYPE`
     String indicating the type of quota rule. The supported values are: 'DEFAULT_USER_QUOTA','DEFAULT_GROUP_QUOTA','INDIVIDUAL_USER_QUOTA','INDIVIDUAL_GROUP_QUOTA' 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Quota rule 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--target`=`TARGET`
     The target of the quota rule. Identified by a Unix UID/GID, Windows SID, or null for default. 
Volume resource - The volume for which quota rule applies. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--volume` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--volume` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--volume`=`VOLUME`
     ID of the volume or fully qualified identifier for the volume. 

To set the `volume` attribute: 

  * provide the argument `--volume` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud netapp volumes quota-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
