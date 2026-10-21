---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/update/
title: gcloud alpha apphub applications services update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:36.489436+00:00
---

# gcloud alpha apphub applications services update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apphub applications services update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apphub applications services update - update an Apphub application service 
SYNOPSIS
    

`gcloud alpha apphub applications services update` (`SERVICE` : `--application`=`APPLICATION` `--location`=`LOCATION`) [`--async`] [`--business-owners`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`--criticality-type`=`CRITICALITY_TYPE`] [`--description`=`DESCRIPTION`] [`--developer-owners`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`--display-name`=`DISPLAY_NAME`] [`--environment-type`=`ENVIRONMENT_TYPE`] [`--operator-owners`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update an Apphub application service. 
EXAMPLES
     To update the Service `my-service` with a new environment `prod` in the Application `my-app` in location `us-east1`, run: 
    
    
    gcloud alpha apphub applications services update my-service --environment-type=TEST --application=my-app --location=us-east1

POSITIONAL ARGUMENTS
    

Service resource - The Service ID. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--application`=`APPLICATION`
     Name for the application 

To set the `application` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--application` on the command line. 


`--location`=`LOCATION`
     The Cloud location for the service. 

To set the `location` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--business-owners`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]
     Business owners of the service 
`--criticality-type`=`CRITICALITY_TYPE`
     Criticality Type of the service. `CRITICALITY_TYPE` must be one of: 

`HIGH`
     High impact 
`LOW`
     Low impact 
`MEDIUM`
     Medium impact 
`MISSION_CRITICAL`
     Mission critical service, application or workload 
`TYPE_UNSPECIFIED`
     Unspecified criticality type 
`--description`=`DESCRIPTION`
     Description of the service 
`--developer-owners`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]
     Developer owners of the service 
`--display-name`=`DISPLAY_NAME`
     Human-friendly display name 
`--environment-type`=`ENVIRONMENT_TYPE`
     Environment Type of the service. `ENVIRONMENT_TYPE` must be one of: 

`DEVELOPMENT`
     Development environment 
`PRODUCTION`
     Production environment 
`STAGING`
     Staging environment 
`TEST`
     Test environment 
`TYPE_UNSPECIFIED`
     Unspecified environment type 
`--operator-owners`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]
     Operator owners of the service 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud apphub applications services update](https://docs.cloud.google.com/sdk/gcloud/reference/apphub/applications/services/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
