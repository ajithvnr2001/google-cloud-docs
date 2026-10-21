---
url: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add/
title: gcloud spanner databases splits add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:18.663386+00:00
---

# gcloud spanner databases splits add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud spanner databases splits add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud spanner databases splits add - add split points to a Spanner database 
SYNOPSIS
    

`gcloud spanner databases splits add` (`DATABASE` : `--instance`=`INSTANCE`) `--splits-file`=`SPLITS_FILE` [`--initiator`=`INITIATOR`] [`--split-expiration-date`=`SPLIT_EXPIRATION_DATE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Add split points to a Spanner database. 
EXAMPLES
     To add split points to the given Spanner database, run: 
    
    
    gcloud spanner databases splits add my-database-id --instance=my-instance-id --splits-file=path/to/splits.txt --initiator=my-initiator-string --split-expiration-date=2024-08-15T15:55:10Z

POSITIONAL ARGUMENTS
    

Database resource - The Cloud Spanner database on which to add split points. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `database` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The Cloud Spanner instance for the database. 

To set the `instance` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


REQUIRED FLAGS
    

`--splits-file`=`SPLITS_FILE`
     The path of a file containing split points to add to the database. Separate split points in the file with a new line. The file format is <ObjectType>[space]<ObjectName>[space]<Split Value>, where the ObjectType is one of TABLE or INDEX and the Split Value is the split point key. For index, the split point key is the index key with or without a full table key prefix. 
OPTIONAL FLAGS
    

`--initiator`=`INITIATOR`
     The tag to identify the initiator of the split points. 
`--split-expiration-date`=`SPLIT_EXPIRATION_DATE`
     The date when the split points become system managed and becomes eligible for merging. The default is 10 days from the date of creation. The maximum is 30 days from the date of creation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha spanner databases splits add](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/splits/add)
    
    
    [gcloud beta spanner databases splits add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/databases/splits/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
