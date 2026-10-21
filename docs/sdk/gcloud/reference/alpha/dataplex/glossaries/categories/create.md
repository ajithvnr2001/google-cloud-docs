---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/glossaries/categories/create/
title: gcloud alpha dataplex glossaries categories create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:44.344436+00:00
---

# gcloud alpha dataplex glossaries categories create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/glossaries/categories/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex glossaries categories create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex glossaries categories create - creates a glossary category 
SYNOPSIS
    

`gcloud alpha dataplex glossaries categories create` (`GLOSSARY_CATEGORY` : `--glossary`=`GLOSSARY` `--location`=`LOCATION`) `--parent`=`PARENT` [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` A glossary category represents a collection of glossary categories and glossary terms within a glossary that are related to each other. 
EXAMPLES
     To create a glossary category `test-category` in glossary `test-glossary` in project `test-project` in location `us-central1`, with description `test description`, displayName `displayName` and parent `projects/test-project/locations/us-central1/glossaries/test-glossary` , run: 
    
    
    gcloud alpha dataplex glossaries categories create test-category --glossary=test-glossary --location=us-central1 --project=test-project --parent='projects/test-project/locations/us-central1/glossaries/test-glossary' --description='test description' --display-name='displayName'

POSITIONAL ARGUMENTS
    

Glossary category resource - Arguments and flags that define the Dataplex Glossary Category you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `glossary_category` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GLOSSARY_CATEGORY`
     ID of the glossary category or fully qualified identifier for the glossary category. 

To set the `glossary_category` attribute: 

  * provide the argument `glossary_category` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--glossary`=`GLOSSARY`
     The name of glossary category to use. 

To set the `glossary` attribute: 

  * provide the argument `glossary_category` on the command line with a fully specified name; 
  * provide the argument `--glossary` on the command line. 


`--location`=`LOCATION`
     The location of the Dataplex resource. 

To set the `location` attribute: 

  * provide the argument `glossary_category` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

`--parent`=`PARENT`
     Immediate parent of the created glossary category. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of the glossary category. 
`--display-name`=`DISPLAY_NAME`
     Display name of the glossary category. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex glossaries categories create](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/glossaries/categories/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
