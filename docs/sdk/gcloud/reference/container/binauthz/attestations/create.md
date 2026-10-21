---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/attestations/create/
title: gcloud container binauthz attestations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:39.933273+00:00
---

# gcloud container binauthz attestations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/attestations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container binauthz attestations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container binauthz attestations create - create a Binary Authorization attestation 
SYNOPSIS
    

`gcloud container binauthz attestations create` `--artifact-url`=`ARTIFACT_URL` `--public-key-id`=`PUBLIC_KEY_ID` `--signature-file`=`SIGNATURE_FILE` [`--payload-file`=`PAYLOAD_FILE`] [[`--note`=`NOTE` : `--note-project`=`NOTE_PROJECT`] | `--validate` [`--attestor`=`ATTESTOR` : `--attestor-project`=`ATTESTOR_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command creates a Binary Authorization attestation for your project. The attestation is created for the specified artifact (e.g. a gcr.io container URL), associate with the specified attestor, and stored under the specified project. 
EXAMPLES
     To create an attestation in the project "my_proj" as the attestor with resource path "projects/foo/attestors/bar", run: 
    
    
    gcloud container binauthz attestations create --project=my_proj --artifact-url='gcr.io/example-project/example-image@sha256:abcd' --attestor=projects/foo/attestors/bar --signature-file=signed_artifact_attestation.pgp.sig --public-key-id=AAAA0000000000000000FFFFFFFFFFFFFFFFFFFF

To create an attestation in the project "my_proj" in note "projects/foo/notes/bar", run: 
    
    
    gcloud container binauthz attestations create --project=my_proj --artifact-url='gcr.io/example-project/example-image@sha256:abcd' --note=projects/foo/notes/bar --signature-file=signed_artifact_attestation.pgp.sig --public-key-id=AAAA0000000000000000FFFFFFFFFFFFFFFFFFFF

REQUIRED FLAGS
    

`--artifact-url`=`ARTIFACT_URL`
     Container URL. May be in the `gcr.io/repository/image` format, or may optionally contain the `http` or `https` scheme 
`--public-key-id`=`PUBLIC_KEY_ID`
     The ID of the public key that will be used to verify the signature of the created Attestation. This ID must match the one found on the Attestor resource(s) which will verify this Attestation. 

For PGP keys, this must be the version 4, full 160-bit fingerprint, expressed as a 40 character hexadecimal string. See <https://tools.ietf.org/html/rfc4880#section-12.2> for details. 

`--signature-file`=`SIGNATURE_FILE`
     Path to file containing the signature to store, or `-` to read signature from stdin. 
OPTIONAL FLAGS
    

`--payload-file`=`PAYLOAD_FILE`
     Path to file containing the payload over which the signature was calculated. 

This defaults to the output of the standard payload command: 
    
    
    [gcloud container binauthz create-signature-payload](https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/create-signature-payload)

NOTE: If you sign a payload with e.g. different whitespace or formatting, you must explicitly provide the payload content via this flag. 

At most one of these can be specified: 

Note resource - The Container Analysis Note which will be used to host the created attestation. In order to successfully attach the attestation, the active gcloud account (core/account) must have the `containeranalysis.notes.attachOccurrence` permission for the Note (usually via the `containeranalysis.notes.attacher` role). The arguments in this group can be used to specify the attributes of this resource. 
`--note`=`NOTE`
     ID of the note or fully qualified identifier for the note. 

To set the `note` attribute: 

  * provide the argument `--note` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--note-project`=`NOTE_PROJECT`
     The Container Analysis project for the note. 

To set the `project` attribute: 

  * provide the argument `--note` on the command line with a fully specified name; 
  * provide the argument `--note-project` on the command line. 


`--validate`
     Whether to validate that the Attestation can be verified by the provided Attestor. 
Attestor resource - The Attestor whose Container Analysis Note will be used to host the created attestation. In order to successfully attach the attestation, the active gcloud account (core/account) must be able to read this attestor and must have the `containeranalysis.notes.attachOccurrence` permission for the Attestor's underlying Note resource (usually via the `containeranalysis.notes.attacher` role). The arguments in this group can be used to specify the attributes of this resource. 
`--attestor`=`ATTESTOR`
     ID of the attestor or fully qualified identifier for the attestor. 

To set the `name` attribute: 

  * provide the argument `--attestor` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--attestor-project`=`ATTESTOR_PROJECT`
     Project ID of the Google Cloud project for the attestor. 

To set the `project` attribute: 

  * provide the argument `--attestor` on the command line with a fully specified name; 
  * provide the argument `--attestor-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container binauthz attestations create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/attestations/create)
    
    
    [gcloud beta container binauthz attestations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/attestations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
