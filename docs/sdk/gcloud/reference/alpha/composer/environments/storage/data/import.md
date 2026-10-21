---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/storage/data/import/
title: gcloud alpha composer environments storage data import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:17:13.448131+00:00
---

# gcloud alpha composer environments storage data import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/storage/data/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha composer environments storage data import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha composer environments storage data import - import data from local storage or Cloud Storage into an environment 
SYNOPSIS
    

`gcloud alpha composer environments storage data import` `--source`=`SOURCE` (`--environment`=`ENVIRONMENT` : `--location`=`LOCATION`) [`--destination`=`DESTINATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` If the SOURCE is a directory, it and its contents are imported recursively. Colliding files in the environment's Cloud Storage bucket will be overwritten. If a file exists in the bucket but is not present in the SOURCE, it is not removed. 
EXAMPLES
     Suppose the '/foo' directory in the local filesystem has the following structure: 
    
    
    foo
    |
    +-- subdir1
    |   |
    |   +-- file1.txt
    |   +-- file2.txt
    |
    +-- subdir2
    |   |
    |   +-- file3.txt
    |   +-- file4.txt

And the environment `myenv`'s Cloud Storage bucket has the following structure: 
    
    
    gs://the-bucket
    |
    +-- data
    |   |
    |   +-- foo
    |   |   |
    |   |   +-- subdir1
    |   |   |   |
    |   |   |   +-- bar.txt

The following command: 
    
    
    gcloud alpha composer environments storage data import myenv --source=/foo

would result in the following structure in `myenv`'s Cloud Storage bucket: 
    
    
    gs://the-bucket
    |
    +-- data
    |   |
    |   +-- foo
    |   |   |
    |   |   +-- subdir1
    |   |   |   |
    |   |   |   +-- bar.txt
    |   |   |   +-- file1.txt
    |   |   |   +-- file2.txt
    |   |   |
    |   |   +-- subdir2
    |   |   |   |
    |   |   |   +-- file3.txt
    |   |   |   +-- file4.txt

If instead we had run 
    
    
    gcloud alpha composer environments storage data import myenv --source=/foo --destination=bar

the resulting bucket structure would be the following: 
    
    
    gs://the-bucket
    |
    +-- data
    |   |
    |   +-- foo
    |   |   |
    |   |   +-- subdir1
    |   |   |   |
    |   |   |   +-- bar.txt
    |   |
    |   +-- bar
    |   |   |
    |   |   +-- foo
    |   |   |   |
    |   |   |   +-- subdir1
    |   |   |   |   |
    |   |   |   |   +-- file1.txt
    |   |   |   |   +-- file2.txt
    |   |   |   |
    |   |   |   +-- subdir2
    |   |   |   |   |
    |   |   |   |   +-- file3.txt
    |   |   |   |   +-- file4.txt

REQUIRED FLAGS
    

`--source`=`SOURCE`
     Path to a local directory/file or Cloud Storage bucket/object to be imported into the data/ subdirectory in the environment's Cloud Storage bucket. Cloud Storage paths must begin with 'gs://'. 
Environment resource - The environment into whose Cloud Storage bucket to import data.. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--destination`=`DESTINATION`
     An optional subdirectory under the data/ directory in the environment's Cloud Storage bucket into which to import files. May contain forward slashes to delimit multiple levels of subdirectory nesting, but should not contain leading or trailing slashes. If the DESTINATION does not exist, it will be created. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud composer environments storage data import](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/storage/data/import)
    
    
    [gcloud beta composer environments storage data import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/storage/data/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
