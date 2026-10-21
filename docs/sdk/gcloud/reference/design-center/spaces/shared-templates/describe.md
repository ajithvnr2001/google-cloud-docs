---
url: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/shared-templates/describe/
title: gcloud design-center spaces shared-templates describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:57.992888+00:00
---

# gcloud design-center spaces shared-templates describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/shared-templates/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud design-center spaces shared-templates describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud design-center spaces shared-templates describe - describe a shared template 
SYNOPSIS
    

`gcloud design-center spaces shared-templates describe` `SHARED_TEMPLATE` [`--location`=`LOCATION`] [`--google-catalog` | `--project`=`PROJECT` `--space`=`SPACE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a shared template. 
EXAMPLES
     To describe the shared template `my-shared-template` in space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces shared-templates describe my-shared-template --space=my-space --project=my-project --location=us-central1

Or run: 
    
    
    gcloud design-center spaces shared-templates describe projects/my-project/locations/us-central1/spaces/my-space/sharedTemplates/my-shared-template

To describe a shared template `google-template` from the Google Catalog and location `us-central1`, run: 
    
    
    gcloud design-center spaces shared-templates describe google-template --google-catalog --location=us-central1

POSITIONAL ARGUMENTS
    

`SHARED_TEMPLATE`
     ID of the sharedTemplate or fully qualified identifier for the sharedTemplate. Format: projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate To set the shared_template attribute: 

  * provide the fully qualified identifier `shared_template` on the command line; 
  * provide the argument `shared_template` which represents the shared template id and the other arguments `--location`, `--project`, `--space` or `--google-catalog` on the command line. 


FLAGS
    

`--location`=`LOCATION`
     The location id of the sharedTemplate resource. 

To set the location attribute: 

  * provide the argument `shared_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


At most one of these can be specified: 

`--google-catalog`
     If provided, describes a shared template from the Google Catalog. This sets the project to "gcpdesigncenter" and space to "googlespace". 
Or at least one of these can be specified: 

Specify --project and --space for custom shared templates. 
`--project`=`PROJECT`
     The project id of the sharedTemplate resource. 

To set the project attribute: 

  * provide the argument `shared_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--space`=`SPACE`
     The space id of the sharedTemplate resource. 

To set the space attribute: 

  * provide the argument `shared_template` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the designcenter/v1 API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha design-center spaces shared-templates describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/shared-templates/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
