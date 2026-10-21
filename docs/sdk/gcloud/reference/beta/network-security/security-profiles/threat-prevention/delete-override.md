---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/delete-override/
title: gcloud beta network-security security-profiles threat-prevention delete-override \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:57:58.403933+00:00
---

# gcloud beta network-security security-profiles threat-prevention delete-override  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention/delete-override/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security security-profiles threat-prevention delete-override Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security security-profiles threat-prevention delete-override - delete overrides of Threat Prevention Profile 
SYNOPSIS
    

`gcloud beta network-security security-profiles threat-prevention delete-override` (`SECURITY_PROFILE` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) (`--antivirus`=[`PROTOCOL`,…] | `--severities`=[`SEVERITY_LEVEL`,…] | `--threat-ids`=[`THREAT-ID`,…]) [`--async`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` To delete existing antivirus, severities, or threat-ids of threat prevention profile. Check the updates of update-override command by using `gcloud network-security security-profiles threat-prevention list-override my-security-profile`. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To delete an override, run: 
    
    
    [gcloud beta network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention) delete-override my-security-profile --severities=MEDIUM

`my-security-profile` is the name of the Security Profile in the format organizations/{organizationID}/locations/{location}/securityProfiles/ {security_profile_id} where organizationID is the organization ID to which the changes should apply, location - `global` specified and security_profile_id the Security Profile Identifier 

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
    

Exactly one of these must be specified: 

`--antivirus`=[`PROTOCOL`,…]
     List of comma-separated protocols where each value in the list indicates the protocol of the antivirus threat. 
`--severities`=[`SEVERITY_LEVEL`,…]
     List of comma-separated severities where each value in the list indicates the severity of the threat. 
`--threat-ids`=[`THREAT-ID`,…]
     List of comma-separated threat identifiers where each identifier in the list is a vendor-specified Signature ID representing a threat type. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `False`. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    [gcloud beta network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention) delete-override --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    [gcloud beta network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profiles/threat-prevention) delete-override --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-security security-profiles threat-prevention](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention) delete-override
    
    
    [gcloud alpha network-security security-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profiles) threat-prevention delete-override

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
