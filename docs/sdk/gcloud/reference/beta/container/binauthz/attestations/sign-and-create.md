---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/attestations/sign-and-create/
title: gcloud beta container binauthz attestations sign-and-create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:41.241198+00:00
---

# gcloud beta container binauthz attestations sign-and-create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/attestations/sign-and-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container binauthz attestations sign-and-create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container binauthz attestations sign-and-create - sign and create a Binary Authorization Attestation using a Cloud KMS key 
SYNOPSIS
    

`gcloud beta container binauthz attestations sign-and-create` `--artifact-url`=`ARTIFACT_URL` (`--keyversion`=`KEYVERSION` : `--keyversion-key`=`KEYVERSION_KEY` `--keyversion-keyring`=`KEYVERSION_KEYRING` `--keyversion-location`=`KEYVERSION_LOCATION` `--keyversion-project`=`KEYVERSION_PROJECT`) [`--dsse-type`=`DSSE_TYPE`; default="application/vnd.dev.cosign.simplesigning.v1+json"] [`--pae-encode-payload`] [`--public-key-id-override`=`PUBLIC_KEY_ID_OVERRIDE`] [[`--note`=`NOTE` : `--note-project`=`NOTE_PROJECT`] | `--validate` [`--attestor`=`ATTESTOR` : `--attestor-project`=`ATTESTOR_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command signs and creates a Binary Authorization attestation for your project. The attestation is created for the specified artifact (e.g. a gcr.io container URL), associate with the specified attestor, and stored under the specified project. 
EXAMPLES
     To sign and create an attestation in the project "my_proj" as the attestor with resource path "projects/foo/attestors/bar" with the key "projects/foo/locations/us-west1/keyRings/aring/cryptoKeys/akey/cryptoKeyVersions/1", run: 
    
    
    gcloud beta container binauthz attestations sign-and-create --project=my_proj --artifact-url='gcr.io/example-project/example-image@sha256:abcd' --attestor=projects/foo/attestors/bar --keyversion-project=foo --keyversion-location=us-west1 --keyversion-keyring=aring --keyversion-key=akey --keyversion=1

To sign and create an attestation in the project "my_proj" in note "bar" with the key "projects/foo/locations/us-west1/keyRings/aring/cryptoKeys/akey/cryptoKeyVersions/1", run: 
    
    
    gcloud beta container binauthz attestations sign-and-create --project=my_proj --artifact-url='gcr.io/example-project/example-image@sha256:abcd' --note=projects/my_proj/notes/bar --keyversion-project=foo --keyversion-location=us-west1 --keyversion-keyring=aring --keyversion-key=akey --keyversion=1

REQUIRED FLAGS
    

`--artifact-url`=`ARTIFACT_URL`
     Container URL. May be in the `gcr.io/repository/image` format, or may optionally contain the `http` or `https` scheme 
CryptoKeyVersion resource - The Cloud KMS (Key Management Service) CryptoKeyVersion to use to sign the attestation payload. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--keyversion`=`KEYVERSION`
     ID of the CryptoKeyVersion or fully qualified identifier for the CryptoKeyVersion. 

To set the `version` attribute: 

  * provide the argument `--keyversion` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--keyversion-key`=`KEYVERSION_KEY`
     The key of the CryptoKeyVersion. 

To set the `key` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-key` on the command line. 


`--keyversion-keyring`=`KEYVERSION_KEYRING`
     The keyring of the CryptoKeyVersion. 

To set the `keyring` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-keyring` on the command line. 


`--keyversion-location`=`KEYVERSION_LOCATION`
     The location of the CryptoKeyVersion. 

To set the `location` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-location` on the command line. 


`--keyversion-project`=`KEYVERSION_PROJECT`
     Project ID of the Google Cloud project for the CryptoKeyVersion. 

To set the `project` attribute: 

  * provide the argument `--keyversion` on the command line with a fully specified name; 
  * provide the argument `--keyversion-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


OPTIONAL FLAGS
    

`--dsse-type`=`DSSE_TYPE`; default="application/vnd.dev.cosign.simplesigning.v1+json"
     DSSE type used for pae encoding. 
`--pae-encode-payload`
     Whether to pae-encode the payload before signing. 
`--public-key-id-override`=`PUBLIC_KEY_ID_OVERRIDE`
     If provided, the ID of the public key that will be used to verify the Attestation instead of the default generated one. This ID should match the one found on the Attestor resource(s) which will use this Attestation. 

This parameter is only necessary if the `--public-key-id-override` flag was provided when this KMS key was added to the Attestor. 

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
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha container binauthz attestations sign-and-create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/attestations/sign-and-create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
