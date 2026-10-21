---
url: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/test-iam-permissions/
title: gcloud design-center spaces test-iam-permissions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:16:04.024212+00:00
---

# gcloud design-center spaces test-iam-permissions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/test-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud design-center spaces test-iam-permissions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud design-center spaces test-iam-permissions - test IAM permissions for a Design Center space 
SYNOPSIS
    

`gcloud design-center spaces test-iam-permissions` (`SPACE` : `--location`=`LOCATION`) `--permissions`=[`PERMISSION`,…] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Tests the IAM permissions that a caller has on a Design Center space. 

Returns an empty set of permissions if the space does not exist. 

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. 

EXAMPLES
     To test if the caller has the `designcenter.spaces.get` and `designcenter.spaces.update` permissions on the Space `my-space` in project `my-project` and location `us-central1`, run: 
    
    
    gcloud design-center spaces test-iam-permissions my-space --location=us-central1 --project=my-project --permissions=designcenter.spaces.get,designcenter.spaces.update

POSITIONAL ARGUMENTS
    

Space resource - The Space ID. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `space` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SPACE`
     ID of the space or fully qualified identifier for the space. 

To set the `space` attribute: 

  * provide the argument `space` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the space. 

To set the `location` attribute: 

  * provide the argument `space` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--permissions`=[`PERMISSION`,…]
     The set of permissions to check for the resource. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the designcenter/v1alpha API. The full documentation for this API can be found at: <http://cloud.google.com/application-design-center/docs>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha design-center spaces test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center/spaces/test-iam-permissions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
