---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/update/
title: gcloud beta network-security security-profile-groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:55:54.656672+00:00
---

# gcloud beta network-security security-profile-groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/security-profile-groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security security-profile-groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security security-profile-groups update - update a Security Profile Group 
SYNOPSIS
    

`gcloud beta network-security security-profile-groups update` (`SECURITY_PROFILE_GROUP` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--clear-threat-prevention-profile` | [`--threat-prevention-profile`=`THREAT_PREVENTION_PROFILE` : `--threat-prevention-profile-location`=`THREAT_PREVENTION_PROFILE_LOCATION` `--threat-prevention-profile-organization`=`THREAT_PREVENTION_PROFILE_ORGANIZATION` `--threat-prevention-profile-project`=`THREAT_PREVENTION_PROFILE_PROJECT`]] [`--clear-url-filtering-profile` | [`--url-filtering-profile`=`URL_FILTERING_PROFILE` : `--url-filtering-profile-location`=`URL_FILTERING_PROFILE_LOCATION` `--url-filtering-profile-organization`=`URL_FILTERING_PROFILE_ORGANIZATION` `--url-filtering-profile-project`=`URL_FILTERING_PROFILE_PROJECT`]] [`--clear-wildfire-analysis-profile` | [`--wildfire-analysis-profile`=`WILDFIRE_ANALYSIS_PROFILE` : `--wildfire-analysis-profile-location`=`WILDFIRE_ANALYSIS_PROFILE_LOCATION` `--wildfire-analysis-profile-organization`=`WILDFIRE_ANALYSIS_PROFILE_ORGANIZATION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update details of a Security Profile Group. 
EXAMPLES
     To update a Security Profile Group with new threat prevention profile `my-new-security-profile`, run: 
    
    
    gcloud beta network-security security-profile-groups update my-security-profile-group --organization=1234 --location=global --threat-prevention-profile=`organizations/1234/locations/global/securityProfiles/my-new-security-profile` --description='New Security Profile of type threat prevention'

POSITIONAL ARGUMENTS
    

Security profile group resource - Security Profile Group Name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `security_profile_group` on the command line with a fully specified name; 
  * set the property `core/project`. This resource can be one of the following types: [networksecurity.organizations.locations.securityProfileGroups, networksecurity.projects.locations.securityProfileGroups]. 



This must be specified. 

`SECURITY_PROFILE_GROUP`
     ID of the security_profile_group or fully qualified identifier for the security_profile_group. 

To set the `security_profile_group` attribute: 

  * provide the argument `security_profile_group` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     location of the security_profile_group - Global. 

To set the `location` attribute: 

  * provide the argument `security_profile_group` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     Organization ID of Security Profile Group 

To set the `organization` attribute: 

  * provide the argument `security_profile_group` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [networksecurity.organizations.locations.securityProfileGroups]. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `False`. 
`--description`=`DESCRIPTION`
     Brief description of the security profile group 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta network-security security-profile-groups update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta network-security security-profile-groups update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--clear-threat-prevention-profile`
     Clear the threat-prevention-profile field. 
Or at least one of these can be specified: 

Threat prevention profile resource - Path to Threat Prevention Profile resource. The arguments in this group can be used to specify the attributes of this resource. This resource can be one of the following types: [networksecurity.organizations.locations.securityProfiles, networksecurity.projects.locations.securityProfiles]. 
`--threat-prevention-profile`=`THREAT_PREVENTION_PROFILE`
     ID of the threat_prevention_profile or fully qualified identifier for the threat_prevention_profile. 

To set the `name` attribute: 

  * provide the argument `--threat-prevention-profile` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--threat-prevention-profile-location`=`THREAT_PREVENTION_PROFILE_LOCATION`
     Location of the threat_prevention_profile. NOTE: Only `global` security profiles are supported. To set the `location` attribute: 

  * provide the argument `--threat-prevention-profile` on the command line with a fully specified name; 
  * provide the argument `--threat-prevention-profile-location` on the command line; 
  * provide the argument `--security-profile-location` on the command line; 
  * provide the argument `--location` on the command line; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. 


`--threat-prevention-profile-organization`=`THREAT_PREVENTION_PROFILE_ORGANIZATION`
     Organization ID of the Security Profile. 

To set the `organization` attribute: 

  * provide the argument `--threat-prevention-profile` on the command line with a fully specified name; 
  * provide the argument `--threat-prevention-profile-organization` on the command line; 
  * provide the argument `--security-profile-organization` on the command line; 
  * provide the argument `--organization` on the command line; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. Must be specified for resource of type [networksecurity.organizations.locations.securityProfiles]. 


`--threat-prevention-profile-project`=`THREAT_PREVENTION_PROFILE_PROJECT`
     Project ID of the threat_prevention_profile. 

To set the `project` attribute: 

  * provide the argument `--threat-prevention-profile` on the command line with a fully specified name; 
  * provide the argument `--threat-prevention-profile-project` on the command line; 
  * set the property `core/project`; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. Must be specified for resource of type [networksecurity.projects.locations.securityProfiles]. 


At most one of these can be specified: 

`--clear-url-filtering-profile`
     Clear the url-filtering-profile field. 
Or at least one of these can be specified: 

Url filtering profile resource - Path to URL Filtering Profile resource. The arguments in this group can be used to specify the attributes of this resource. This resource can be one of the following types: [networksecurity.organizations.locations.securityProfiles, networksecurity.projects.locations.securityProfiles]. 
`--url-filtering-profile`=`URL_FILTERING_PROFILE`
     ID of the url_filtering_profile or fully qualified identifier for the url_filtering_profile. 

To set the `name` attribute: 

  * provide the argument `--url-filtering-profile` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--url-filtering-profile-location`=`URL_FILTERING_PROFILE_LOCATION`
     Location of the url_filtering_profile. NOTE: Only `global` security profiles are supported. To set the `location` attribute: 

  * provide the argument `--url-filtering-profile` on the command line with a fully specified name; 
  * provide the argument `--url-filtering-profile-location` on the command line; 
  * provide the argument `--location` on the command line; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. 


`--url-filtering-profile-organization`=`URL_FILTERING_PROFILE_ORGANIZATION`
     Organization ID of the Security Profile. 

To set the `organization` attribute: 

  * provide the argument `--url-filtering-profile` on the command line with a fully specified name; 
  * provide the argument `--url-filtering-profile-organization` on the command line; 
  * provide the argument `--organization` on the command line; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. Must be specified for resource of type [networksecurity.organizations.locations.securityProfiles]. 


`--url-filtering-profile-project`=`URL_FILTERING_PROFILE_PROJECT`
     Project ID of the url_filtering_profile. 

To set the `project` attribute: 

  * provide the argument `--url-filtering-profile` on the command line with a fully specified name; 
  * provide the argument `--url-filtering-profile-project` on the command line; 
  * set the property `core/project`; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. Must be specified for resource of type [networksecurity.projects.locations.securityProfiles]. 


At most one of these can be specified: 

`--clear-wildfire-analysis-profile`
     Clear the wildfire-analysis-profile field. 
Or at least one of these can be specified: 

Wildfire analysis profile resource - Path to WildFire Analysis Profile resource. The arguments in this group can be used to specify the attributes of this resource. This resource can be one of the following types: [wildfire_analysis_profile]. 
`--wildfire-analysis-profile`=`WILDFIRE_ANALYSIS_PROFILE`
     ID of the wildfire_analysis_profile or fully qualified identifier for the wildfire_analysis_profile. 

To set the `name` attribute: 

  * provide the argument `--wildfire-analysis-profile` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--wildfire-analysis-profile-location`=`WILDFIRE_ANALYSIS_PROFILE_LOCATION`
     Location of the wildfire_analysis_profile. NOTE: Only `global` security profiles are supported. To set the `location` attribute: 

  * provide the argument `--wildfire-analysis-profile` on the command line with a fully specified name; 
  * provide the argument `--wildfire-analysis-profile-location` on the command line; 
  * provide the argument `--location` on the command line; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. 


`--wildfire-analysis-profile-organization`=`WILDFIRE_ANALYSIS_PROFILE_ORGANIZATION`
     Organization ID of the Security Profile. 

To set the `organization` attribute: 

  * provide the argument `--wildfire-analysis-profile` on the command line with a fully specified name; 
  * provide the argument `--wildfire-analysis-profile-organization` on the command line; 
  * provide the argument `--organization` on the command line; 
  * provide the argument `security_profile_group` on the command line with a fully specified name. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-security security-profile-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/update)
    
    
    [gcloud alpha network-security security-profile-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/security-profile-groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
