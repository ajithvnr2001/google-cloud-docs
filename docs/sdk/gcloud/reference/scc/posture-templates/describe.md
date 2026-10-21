---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe/
title: gcloud scc posture-templates describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:07.689708+00:00
---

# gcloud scc posture-templates describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc posture-templates describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc posture-templates describe - describe a Cloud Security Command Center posture template 
SYNOPSIS
    

`gcloud scc posture-templates describe` (`POSTURE_TEMPLATE` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--revision-id`=`REVISION_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a Cloud Security Command Center (SCC) posture template. 

By default, the latest created revision of the posture template is described. Users must provide revision ID to describe a specific revision. 

EXAMPLES
     Describe a posture template named `organizations/123/locations/global/postureTemplates/secure_by_default` (i.e. a posture in organization `123`, location `global`, with id `secure_by_default`): 
    
    
    gcloud scc posture-templates describe organizations/123/locations/global/postureTemplates/secure_by_default

Describe a specific revision `v1.0.0` of posture template named `organizations/123/locations/global/postureTemplates/secure_by_default`: 
    
    
    gcloud scc posture-templates describe organizations/123/locations/global/postureTemplates/secure_by_default --revision-id=v1.0.0

POSITIONAL ARGUMENTS
    

Posture template resource - Posture template to be described. For example organizations/<organizationID>/locations/<location>/postureTemplates/<postureTemplateID>. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`POSTURE_TEMPLATE`
     ID of the posture_template or fully qualified identifier for the posture_template. 

To set the `posture_template` attribute: 

  * provide the argument `posture_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     ID of the location where the resource exists (for example, global). To set the `location` attribute: 

  * provide the argument `posture_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     ID of the organization which is the parent of the resource. To set the `organization` attribute: 

  * provide the argument `posture_template` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


FLAGS
    

`--revision-id`=`REVISION_ID`
     ID of the specific posture template revision to be described. If not specified, latest revision is described. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securityposture/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc posture-templates describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/posture-templates/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
