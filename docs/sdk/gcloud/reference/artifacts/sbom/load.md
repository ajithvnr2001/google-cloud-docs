---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load/
title: gcloud artifacts sbom load \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:16.781645+00:00
---

# gcloud artifacts sbom load  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts sbom load Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts sbom load - upload an SBOM file and create a reference occurrence 
SYNOPSIS
    

`gcloud artifacts sbom load` `--source`=`SOURCE` `--uri`=`ARTIFACT_URI` [`--destination`=`DESTINATION`] [`--kms-key-version`=`KMS_KEY_VERSION`] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Upload an SBOM file and create a reference occurrence. 
EXAMPLES
     To upload an SBOM file at /path/to/sbom.json for a Docker image in Artifact Registry: 
    
    
    gcloud artifacts sbom load --source=/path/to/sbom.json --uri=us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz

To upload an SBOM file at /path/to/sbom.json for a Docker image with a KMS key version to sign the created SBOM reference: 
    
    
    gcloud artifacts sbom load --source=/path/to/sbom.json --uri=us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz --kms-key-version=projects/my-project/locations/us-west1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/1

To upload an SBOM file at /path/to/sbom.json for a Docker image from a Docker registry: 
    
    
    gcloud artifacts sbom load --source=/path/to/sbom.json --uri=my-docker-registry/my-image@sha256:abcxyz --destination=gs://my-cloud-storage-bucket

REQUIRED FLAGS
    

`--source`=`SOURCE`
     The SBOM file for uploading. 
`--uri`=`ARTIFACT_URI`
     The URI of the artifact the SBOM is generated from. The URI can be a Docker image from any Docker registries. A URI provided with a tag (e.g. `[IMAGE]:[TAG]`) will be resolved into a URI with a digest (`[IMAGE]@sha256:[DIGEST]`). When passing an image which is not from Artifact Registry or Container Registry with a tag, only public images can be resolved. Also, when passing an image which is not from Artifact Registry or Container Registry, the `--destination` flag is required. 
OPTIONAL FLAGS
    

`--destination`=`DESTINATION`
     The storage path will be used to store the SBOM file. Currently only supports Cloud Storage paths start with 'gs://'. 
`--kms-key-version`=`KMS_KEY_VERSION`
     Cloud KMS key version to sign the SBOM reference. The key version provided should be the resource ID in the format of `projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]/cryptoKeyVersions/[KEY_VERSION]`. 
`--location`=`LOCATION`
     If specified, all requests to Artifact Analysis for occurrences will go to location specified 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
