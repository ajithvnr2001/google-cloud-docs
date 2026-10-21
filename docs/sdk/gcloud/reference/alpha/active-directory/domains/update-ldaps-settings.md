---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings/
title: gcloud alpha active-directory domains update-ldaps-settings \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:20.564266+00:00
---

# gcloud alpha active-directory domains update-ldaps-settings  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update-ldaps-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha active-directory domains update-ldaps-settings Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha active-directory domains update-ldaps-settings - update the LDAPS settings for a domain 
SYNOPSIS
    

`gcloud alpha active-directory domains update-ldaps-settings` `DOMAIN` (`--clear-certificates` | [`--certificate-pfx-file`=`PATH_TO_FILE` : `--certificate-password`=`CERTIFICATE_PASSWORD`]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Managed Microsoft AD domain's Lightweight Directory Access Protocol over TLS/SSL (LDAPS) settings. You must be safelisted for the Managed AD LDAPS Alpha in order to use this feature. Consult the API documentation for a list of certificate requirements. 

This command can fail for the following reasons: 

  * The certificate is invalid. 
  * The domain specified does not exist. 
  * The active account does not have permission to view LDAPS settings for the domain. 


EXAMPLES
     To enable LDAPS for the first time or update the certificates being used: 
    
    
    gcloud alpha active-directory domains update-ldaps-settings my-domain.com --certificate-pfx-file=certificate-chain-with-private-key.pfx --certificate-password="password"

To disable LDAPS: 
    
    
    gcloud alpha active-directory domains update-ldaps-settings my-domain.com --clear-certificates

POSITIONAL ARGUMENTS
    

Domain resource - Name of the managed Managed Microsoft AD domain you want to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `domain` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DOMAIN`
     ID of the domain or fully qualified identifier for the domain. 

To set the `domain` attribute: 

  * provide the argument `domain` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--clear-certificates`
     Disable LDAPS by deleting all existing certificates. Certificates will need to be re-uploaded if LDAPS is to be re-enabled. 
Or at least one of these can be specified: 

`--certificate-pfx-file`=`PATH_TO_FILE`
     PKCS#12-formatted pfx file that specifies the certificate chain used to configure LDAPS. If certificate-password is not specified, command will prompt user for secret. Use a full or relative path to a local file containing the value of certificate_pfx_file. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--certificate-password`=`CERTIFICATE_PASSWORD`
     Password used to encrypt the PKCS#12 certificate. If not specified, command will prompt user for secret. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud active-directory domains update-ldaps-settings](https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/update-ldaps-settings)
    
    
    [gcloud beta active-directory domains update-ldaps-settings](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/update-ldaps-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
