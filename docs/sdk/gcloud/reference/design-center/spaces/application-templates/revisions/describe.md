---
url: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/revisions/describe/
title: gcloud design-center spaces application-templates revisions describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:53.265502+00:00
---

# gcloud design-center spaces application-templates revisions describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/revisions/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud design-center spaces application-templates revisions describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud design-center spaces application-templates revisions describe - describe an application template revision 
SYNOPSIS
    

`gcloud design-center spaces application-templates revisions describe` (`REVISION` : `--application-template`=`APPLICATION_TEMPLATE` `--location`=`LOCATION` `--space`=`SPACE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe an application template revision. 
EXAMPLES
     To describe the application template revision `my-revision` in application template `my-app-template`, space `my-space`, project `my-project` and location `us-central1`, run: 
    
    
    [gcloud design-center spaces application-templates revisions](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/revisions) describe my-revision --application-template=my-app-template --space=my-space --project=my-project --location=us-central1

Or run: 
    
    
    [gcloud design-center spaces application-templates revisions](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/revisions) describe projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template/revisions/my-revision

POSITIONAL ARGUMENTS
    

Revision resource - The application template revision name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REVISION`
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `revision` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--application-template`=`APPLICATION_TEMPLATE`
     The applicationTemplate id of the revision resource. 

To set the `application-template` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--application-template` on the command line. 


`--location`=`LOCATION`
     The location id of the revision resource. 

To set the `location` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--space`=`SPACE`
     The space id of the revision resource. 

To set the `space` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--space` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `designcenter/v1` API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha design-center spaces application-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/application-templates) revisions describe

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
