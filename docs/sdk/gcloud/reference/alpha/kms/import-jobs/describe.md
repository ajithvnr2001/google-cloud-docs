---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/import-jobs/describe/
title: gcloud alpha kms import-jobs describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:39.275979+00:00
---

# gcloud alpha kms import-jobs describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/import-jobs/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms import-jobs describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms import-jobs describe - get metadata for a given import job 
SYNOPSIS
    

`gcloud alpha kms import-jobs describe` `IMPORT_JOB` [`--attestation-file`=`ATTESTATION_FILE`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Returns metadata for the given import job. 

The optional flag `--attestation-file` specifies file to write the attestation into. The attestation enables the user to verify the integrity and provenance of the key. See <https://cloud.google.com/kms/docs/attest-key> for more information about attestations. 

EXAMPLES
     The following command returns metadata for import job 'strider' within the keyring 'fellowship' in the location 'us-central1': 
    
    
    gcloud alpha kms import-jobs describe strider --keyring=fellowship --location=us-central1

For import jobs with protection level `HSM`, use the `--attestation-file` flag to save the attestation to a local file. 
    
    
    gcloud alpha kms import-jobs describe strider --keyring=fellowship --location=us-central1 --attestation-file=path/to/attestation.dat

POSITIONAL ARGUMENTS
    

`IMPORT_JOB`
     Name of the import job to describe. 
FLAGS
    

`--attestation-file`=`ATTESTATION_FILE`
     Path to the output attestation file. 
`--keyring`=`KEYRING`
     Key ring of the import job. 
`--location`=`LOCATION`
     Location of the import job. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms import-jobs describe](https://docs.cloud.google.com/sdk/gcloud/reference/kms/import-jobs/describe)
    
    
    [gcloud beta kms import-jobs describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/import-jobs/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
