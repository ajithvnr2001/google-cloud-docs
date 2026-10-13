---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-inline-cloud-analysis-rule/
title: gcloud beta network-security security-profiles wildfire-analysis add-inline-cloud-analysis-rule \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:16.992010+00:00
---

# gcloud beta network-security security-profiles wildfire-analysis add-inline-cloud-analysis-rule  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis/add-inline-cloud-analysis-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security security-profiles wildfire-analysis add-inline-cloud-analysis-rule Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security security-profiles wildfire-analysis add-inline-cloud-analysis-rule - add a WildFire inline cloud analysis rule to a WildFire Analysis Profile 
SYNOPSIS
    

`gcloud beta network-security security-profiles wildfire-analysis add-inline-cloud-analysis-rule` (`SECURITY_PROFILE` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--action`=`ACTION` `--direction`=`DIRECTION` `--file-types`=[`FILE_TYPE`,…] [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Add a WildFire inline cloud analysis rule to a WildFire Analysis Security Profile. 
EXAMPLES
     To add an inline cloud analysis rule to a WildFire Analysis Security Profile named `my-wf-profile` in organization `1234` with file-types `ANY_FILE`, direction `BOTH`, and action `ALLOW`, run: 
    
    
    [gcloud beta network-security security-profiles wildfire-analysis](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/wildfire-analysis) add-inline-cloud-analysis-rule my-wf-profile --organization=1234 --location=global --file-types=ANY_FILE --direction=BOTH --action=ALLOW

POSITIONAL ARGUMENTS
    

Security profile resource - Security Profile Name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `security_profile` on the command line with a fully specified name; 
  * set the property `core/project`. This resource can be one of the following types: [networksecurity.organizations.locations.securityProfiles, networksecurity.projects.locations.securityProfiles]. 



This must be specified. 

`SECURITY_PROFILE`
     ID of the security_profile or fully qualified identifier for the security_profile. 

To set the `security_profile` attribute: 

  * provide the argument `security_profile` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the security profile. 

To set the `location` attribute: 

  * provide the argument `security_profile` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     Organization ID to which the changes should apply. 

To set the `organization` attribute: 

  * provide the argument `security_profile` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [networksecurity.organizations.locations.securityProfiles]. 


REQUIRED FLAGS
    

`--action`=`ACTION`
     Action to take when Inline Cloud Analysis detects a threat. `ACTION` must be one of: `ALLOW`, `DENY`, `ALERT`. 
`--direction`=`DIRECTION`
     Direction of traffic that will be checked for files to submit to WildFire. `DIRECTION` must be one of: `UPLOAD`, `DOWNLOAD`, `BOTH`. 
`--file-types`=[`FILE_TYPE`,…]
     Types of files that will be submitted to WildFire for analysis. FILE_TYPE must be one of: ANY_FILE, PE. If ANY_FILE is specified, no other types can be specified. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `False`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) wildfire-analysis add-inline-cloud-analysis-rule

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
