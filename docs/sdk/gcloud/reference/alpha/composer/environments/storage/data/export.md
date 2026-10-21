---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/storage/data/export/
title: gcloud alpha composer environments storage data export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:17:13.118430+00:00
---

# gcloud alpha composer environments storage data export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/storage/data/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha composer environments storage data export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha composer environments storage data export - export data from an environment into local storage or Cloud Storage 
SYNOPSIS
    

`gcloud alpha composer environments storage data export` `--destination`=`DESTINATION` (`--environment`=`ENVIRONMENT` : `--location`=`LOCATION`) [`--source`=`SOURCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` If the SOURCE is a directory, it and its contents are are exported recursively. If no SOURCE is provided, the entire contents of the environment's data directory will be exported. Colliding files in the DESTINATION will be overwritten. If a file exists in the DESTINATION but there is no corresponding file to overwrite it, it is untouched. 
EXAMPLES
     Suppose the environment `myenv`'s Cloud Storage bucket has the following structure: 
    
    
    gs://the-bucket
    |
    +-- data
    |   |
    |   +-- file1.txt
    |   +-- file2.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- file4.txt

And the local directory '/foo' has the following structure: 
    
    
    /foo
    |
    +-- file1.txt
    +-- fileX.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- fileY.txt

The following command: 
    
    
    gcloud alpha composer environments storage data export myenv --destination=/foo

would result in the following structure in the local '/foo' directory: 
    
    
    /foo
    |
    +-- file1.txt
    +-- file2.txt
    +-- fileX.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- file4.txt
    |   |   +-- fileY.txt

The local files '/foo/file1.txt' and '/foo/subdir1/file3.txt' will be overwritten with the contents of the corresponding files in the Cloud Storage bucket. 

If instead we had run 
    
    
    gcloud alpha composer environments storage data export myenv --source=subdir1/file3.txt --destination=/foo

the resulting local directory structure would be the following: 
    
    
    /foo
    |
    +-- file1.txt
    +-- file3.txt
    +-- fileX.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- fileY.txt

No local files would be overwritten since 'gs://the-bucket/dags/subdir1/file3.txt' was written to '/foo/file3.txt' instead of 'foo/subdir1/file3.txt'. 

REQUIRED FLAGS
    

`--destination`=`DESTINATION`
     The path to an existing local directory or a Cloud Storage bucket/directory into which to export files. 
Environment resource - The environment from whose Cloud Storage bucket to export data.. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--environment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--environment`=`ENVIRONMENT`
     ID of the environment or fully qualified identifier for the environment. 

To set the `environment` attribute: 

  * provide the argument `--environment` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Region where Composer environment runs or in which to create the environment. 

To set the `location` attribute: 

  * provide the argument `--environment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `composer/location`. 


OPTIONAL FLAGS
    

`--source`=`SOURCE`
     An optional relative path to a file or directory to be exported from the data/ subdirectory in the environment's Cloud Storage bucket. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud composer environments storage data export](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/storage/data/export)
    
    
    [gcloud beta composer environments storage data export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/storage/data/export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
