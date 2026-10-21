---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/delete/
title: gcloud privateca roots delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:16.967998+00:00
---

# gcloud privateca roots delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca roots delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca roots delete - delete a Root Certificate Authority 
SYNOPSIS
    

`gcloud privateca roots delete` (`CERTIFICATE_AUTHORITY` : `--location`=`LOCATION` `--pool`=`POOL`) [`--ignore-active-certificates`] [`--ignore-dependent-resources`] [`--skip-grace-period`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a Root Certificate Authority. Deleted Root Certificate Authorities may be recovered with the `[gcloud privateca roots undelete](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/undelete)` command within a grace period of 30 days. 

Use the --skip-grace-period flag to delete as soon as possible without the 30-day grace period to undelete. 

Note that any user-managed KMS keys or Google Cloud Storage buckets will not be affected by this operation. You will need to delete the user- managed resources separately once the CA is deleted. Any Google-managed resources will be cleaned up. 

The CA specified in this command MUST: 
    
    
    1) be in the DISABLED or STAGED state.
    2) have no un-revoked or un-expired certificates. Use the revoke command
       to revoke any active certificates.

Use the `--ignore-active-certificates` flag to remove 2) as a requirement. 

EXAMPLES
     To delete a root CA: 
    
    
    gcloud privateca roots delete prod-root --pool=my-pool --location=us-west1

To delete a CA while skipping the confirmation input: 
    
    
    gcloud privateca roots delete prod-root --pool=my-pool --location=us-west1 --quiet

To undo the deletion for a root CA: 
    
    
    [gcloud privateca roots undelete](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/undelete) prod-root --pool=my-pool --location=us-west1

POSITIONAL ARGUMENTS
    

CERTIFICATE AUTHORITY resource - The certificate authority to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE_AUTHORITY`
     ID of the CERTIFICATE_AUTHORITY or fully qualified identifier for the CERTIFICATE_AUTHORITY. 

To set the `certificate_authority` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the CERTIFICATE_AUTHORITY. 

To set the `location` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `privateca/location`. 


`--pool`=`POOL`
     The parent CA Pool of the CERTIFICATE_AUTHORITY. 

To set the `pool` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--pool` on the command line. 


FLAGS
    

`--ignore-active-certificates`
     If this flag is set, the Certificate Authority will be deleted even if the Certificate Authority has un-revoked or un-expired certificates after the grace period. 
`--ignore-dependent-resources`
     This field skips the integrity check that would normally prevent breaking a CA Pool if it is used by another cloud resource and allows the CA Pool to be in a state where it is not able to issue certificates. Doing so may result in unintended and unrecoverable effects on any dependent resource(s) since the CA Pool would not be able to issue certificates. 
`--skip-grace-period`
     If this flag is set, the Certificate Authority will be deleted as soon as possible without a 30-day grace period where undeletion would have been allowed. If you proceed, there will be no way to recover this CA. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
