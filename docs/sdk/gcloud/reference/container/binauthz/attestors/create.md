---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create/
title: gcloud container binauthz attestors create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:40.707090+00:00
---

# gcloud container binauthz attestors create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container binauthz attestors create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container binauthz attestors create - create an Attestor 
SYNOPSIS
    

`gcloud container binauthz attestors create` `ATTESTOR` (`--attestation-authority-note`=`ATTESTATION_AUTHORITY_NOTE` : `--attestation-authority-note-project`=`ATTESTATION_AUTHORITY_NOTE_PROJECT`) [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create an Attestor. 
EXAMPLES
     To create an Attestor with an existing Note `projects/my_proj/notes/my_note`: 
    
    
    gcloud container binauthz attestors create my_new_attestor --attestation-authority-note=my_note --attestation-authority-note-project=my_proj

POSITIONAL ARGUMENTS
    

Attestor resource - The attestor to be created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `ATTESTOR` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ATTESTOR`
     ID of the attestor or fully qualified identifier for the attestor. 

To set the `name` attribute: 

  * provide the argument `ATTESTOR` on the command line. 


REQUIRED FLAGS
    

Note resource - The Container Analysis Note to which the created attestor will be bound. 

For the attestor to be able to access and use the Note, the Note must exist and the active gcloud account (core/account) must have the `containeranalysis.notes.listOccurrences` permission for the Note. This can be achieved by granting the `containeranalysis.notes.occurrences.viewer` role to the active account for the Note resource in question. 
    
    
    The arguments in this group can be used to specify the attributes of this resource.

This must be specified. 

`--attestation-authority-note`=`ATTESTATION_AUTHORITY_NOTE`
     ID of the note or fully qualified identifier for the note. 

To set the `note` attribute: 

  * provide the argument `--attestation-authority-note` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--attestation-authority-note-project`=`ATTESTATION_AUTHORITY_NOTE_PROJECT`
     The Container Analysis project for the note. 

To set the `project` attribute: 

  * provide the argument `--attestation-authority-note` on the command line with a fully specified name; 
  * provide the argument `--attestation-authority-note-project` on the command line. 


OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     A description for the attestor 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container binauthz attestors create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/attestors/create)
    
    
    [gcloud beta container binauthz attestors create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/attestors/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
