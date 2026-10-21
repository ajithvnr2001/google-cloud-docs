---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/tables/restore/
title: gcloud beta bigtable tables restore \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:16.459589+00:00
---

# gcloud beta bigtable tables restore  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/tables/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta bigtable tables restore Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta bigtable tables restore - restore a Cloud Bigtable backup to a new table 
SYNOPSIS
    

`gcloud beta bigtable tables restore` (`--destination`=`DESTINATION` : `--destination-instance`=`DESTINATION_INSTANCE`) (`--source`=`SOURCE` : `--source-cluster`=`SOURCE_CLUSTER` `--source-instance`=`SOURCE_INSTANCE`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command restores a Cloud Bigtable backup to a new table. 
EXAMPLES
     To restore table 'table2' from backup 'backup1', run: 
    
    
    gcloud beta bigtable tables restore --source-instance=instance1 --source-cluster=cluster1 --source=backup1 --destination-instance=instance1 --destination=table2

To restore table 'table2' from backup 'backup1' in a different project, run: 
    
    
    gcloud beta bigtable tables restore --source=projects/project1/instances/instance1/clusters/cluster1/backups/backup1 --destination=projects/project2/instances/instance2/tables/table2

REQUIRED FLAGS
    

Table resource - The destination to restore to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--destination`=`DESTINATION`
     ID of the table or fully qualified identifier for the table. 

To set the `destination` attribute: 

  * provide the argument `--destination` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--destination-instance`=`DESTINATION_INSTANCE`
     Name of the Bigtable instance. 

To set the `instance` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--destination-instance` on the command line; 
  * provide the argument `--source-instance` on the command line. 


Backup resource - The source to restore from. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--source`=`SOURCE`
     ID of the backup or fully qualified identifier for the backup. 

To set the `source` attribute: 

  * provide the argument `--source` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--source-cluster`=`SOURCE_CLUSTER`
     Name of the Bigtable cluster. 

To set the `cluster` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--source-cluster` on the command line. 


`--source-instance`=`SOURCE_INSTANCE`
     Name of the Bigtable instance. 

To set the `instance` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--source-instance` on the command line; 
  * provide the argument `--destination-instance` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud bigtable tables restore](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/tables/restore)
    
    
    [gcloud alpha bigtable tables restore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable/tables/restore)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
