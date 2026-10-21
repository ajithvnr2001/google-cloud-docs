---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/custom-intercept/create/
title: gcloud alpha network-security security-profiles custom-intercept create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:57:05.161868+00:00
---

# gcloud alpha network-security security-profiles custom-intercept create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/custom-intercept/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-security security-profiles custom-intercept create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-security security-profiles custom-intercept create - create a new Custom Intercept Profile 
SYNOPSIS
    

`gcloud alpha network-security security-profiles custom-intercept create` (`SECURITY_PROFILE` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) (`--intercept-endpoint-group`=`INTERCEPT_ENDPOINT_GROUP` : `--intercept-endpoint-group-location`=`INTERCEPT_ENDPOINT_GROUP_LOCATION` `--intercept-endpoint-group-project`=`INTERCEPT_ENDPOINT_GROUP_PROJECT`) [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Custom Intercept Security Profile. 
EXAMPLES
     To create a Custom Intercept Security Profile named `intercept-profile` linked to a Intercept Endpoint Group (q.v.), run: 
    
    
    [gcloud alpha network-security security-profiles custom-intercept](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles/custom-intercept) create intercept-profile --description="An Intercept Profile" --intercept-endpoint-group=projects/my-project/locations/global/interceptEndpointGroups/my-mep

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
    

Intercept endpoint group resource - Intercept Endpoint Group. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--intercept-endpoint-group`=`INTERCEPT_ENDPOINT_GROUP`
     ID of the intercept endpoint group or fully qualified identifier for the intercept endpoint group. 

To set the `id` attribute: 

  * provide the argument `--intercept-endpoint-group` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--intercept-endpoint-group-location`=`INTERCEPT_ENDPOINT_GROUP_LOCATION`
     Location of the intercept endpoint group. 

To set the `location` attribute: 

  * provide the argument `--intercept-endpoint-group` on the command line with a fully specified name; 
  * provide the argument `--intercept-endpoint-group-location` on the command line; 
  * provide the argument `--location` on the command line; 
  * provide the argument `security_profile` on the command line with a fully specified name. 


`--intercept-endpoint-group-project`=`INTERCEPT_ENDPOINT_GROUP_PROJECT`
     Project ID of the intercept endpoint group. 

To set the `project` attribute: 

  * provide the argument `--intercept-endpoint-group` on the command line with a fully specified name; 
  * provide the argument `--intercept-endpoint-group-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`; 
  * provide the argument `security_profile` on the command line with a fully specified name. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `False`. 
`--description`=`DESCRIPTION`
     Brief description of the security profile 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud network-security security-profiles custom-intercept create](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/custom-intercept/create)
    
    
    [gcloud beta network-security security-profiles custom-intercept](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/custom-intercept) create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
