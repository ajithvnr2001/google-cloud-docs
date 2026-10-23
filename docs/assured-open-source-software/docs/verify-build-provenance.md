---
url: https://docs.cloud.google.com/assured-open-source-software/docs/verify-build-provenance/
title: Verify the build provenance \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:30.512750+00:00
---

# Verify the build provenance  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/verify-build-provenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Verify the build provenance Stay organized with collections  Save and categorize content based on your preferences. 

Assured OSS packages are built with [SLSA Level 2](https://slsa.dev/spec/v0.1/levels) compliance. Build provenance is provided as part of the security metadata. This page explains how to verify the build provenance metadata.

This document applies to the free tier. For information about the build provenance in the premium tier, see [Access security metadata and verify packages](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata).

## Before you begin

  * Install [cosign](https://github.com/sigstore/cosign) to verify the signature in the build provenance.



## Set up authentication

For information about setting up authentication, see [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication).

## Verify build provenance

Build provenance is signed using an in-toto attestation which in turn uses [dsse envelope format](https://github.com/secure-systems-lab/dsse/blob/master/protocol.md). This means that the generated signature contains the wrapped signature and the raw data.

### Using the aoss-verifier tool

  1. To verify build provenance, install the [aoss-verifier](https://github.com/google/aoss-verifier) tool.

  2. Export `$(go env GOPATH)/bin`, and run the `aoss-verifier verify-package` command with the `--verify_build_provenance` flag.
         
         aoss-verifier verify-package \
            --language LANGUAGE \
            --package_id PACKAGE_ID \
            --version VERSION \
            --artifact_path ARTIFACT_PATH \
            --verify_build_provenance \
            [--disable_certificate_verification] \
            [--temp_downloads_path TEMP_DOWNLOADS_DIR_PATH] \
            [--disable_deletes]
         

Replace the following:

     * LANGUAGE: The package language. The value must be in lowercase.
     * PACKAGE_ID: For Java, the format is groupId:artifactId. For Python, the format is packageName. The value must be in lowercase.
     * VERSION: The version of the package.
     * ARTIFACT_PATH: The path to the data file in your local directory that you want to verify. Use the following filename extensions: 
       * `jar` file extension for a Java package
       * `whl` file extension for a Python package

`--disable_certificate_verification` is an optional flag which skips matching leaf certificate to the root certificate through the certificate chain, if used.

`--temp_downloads_path` is an optional flag to set the path where you want to download the files. Replace TEMP_DOWNLOADS_DIR_PATH. If this flag isn't set, the files are downloaded to the `tmp_downloads` folder in the current directory.

`--disable_deletes` is an optional flag which keeps the downloaded files. By default, the tool cleans all the downloaded files.




For more information, see the [README file of the tool](https://github.com/google/aoss-verifier#readme).

### Manual verification

To verify the build provenance, do the following:

  1. Retrieve build provenance.

Depending on how you [access security metadata](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis), the build provenance is accessed differently.

     * If you [access security metadata using Cloud Storage](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-cloud-storage), build provenance is available as part of the `Build Information` metadata under the `buildDetails` field.

For more information, see the following sample metadata snippet:
    
    {
      "creationTime": "2023-03-25T05:32:23Z",
      "buildDetails": [
       {
         "packageFileName": "jackson-databind-2.13.3.jar",
         "envelope": {
         "payload": "eyJfdHlwZSI6Imh0d……………",
         "payloadType": "application/vnd.in-toto+json",
         "signatures": [
            "sig": "eyJwYXlsb2FkVHlwZSI6Im……",
            "keyid": "gcpkms://projects/cloud-aoss/locations/global/keyRings/cloud-aoss-ring/cryptoKeys/tekton-chains"
           }
         ]
       },
      "buildProvenance": "{\"_type\":\"https://in-toto.io/Statement/v0.1…"
    .....
    
    

     * If you [access security metadata using Artifact Analysis API](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis), build provenance is stored in the `BuildOccurrence` section of the security metadata.

Sample metadata snippet:
    
    {'BuildOccurrence': name: "projects/cloud-aoss/occurrences/06c514bb-1069-4cde-8d68-b1306f19535a"
    resource_uri: "jackson-databind-2.13.3.jar@sha256:4c01a14673bc1cd4a2df337a3b4e695af0a6ed8ac6be19c9e4077377fb8adf92"
    note_name: "projects/cloud-aoss/notes/tekton-cloudbuild-intoto"
    kind: BUILD
    create_time {
      seconds: 1665556616
      nanos: 891004000
    }
    ……
    ……
    }
    envelope {
      payload: "{\"_type\":\"https://in-toto.io/Statement/v0.1\", ….."
      payload_type: "application/vnd.in-toto+json"
      signatures {
        sig: "{\"payloadType\":\"application/vnd.in-toto+json\",....."
        keyid: "gcpkms://projects/cloud-aoss/locations/global/keyRings/cloud-aoss-ring/cryptoKeys/tekton-chains"
      }
    }
    ,
    …
    
    

  2. Retrieve the build provenance signature.

Build provenance contains a section named [Envelope](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#envelope) which contains signatures as [EnvelopeSignature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#envelope). To retrieve the signature, follow these steps:

     1. Store the `sig` data in a file named `signature.txt`.
     2. Check if the metadata is downloaded using the metadata script.

If the metadata is downloaded using the metadata script, modify the signature and store it in another file called `signature.sig`.

To modify the signature, run the following command:
            
            cat signature.txt | sed -e 's/\\"/"/g' > signature.sig
            

If the metadata is **not** downloaded using the metadata script, decode the signature and store it in another file called `signature.sig`.

To decode the signature, use the following command:
            
            cat signature.txt | tr '\-_' '+/' | base64 -d > signature.sig
            

  3. Retrieve the build provenance public key.

The [EnvelopeSignature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#EnvelopeSignature) section in build provenance contains the reference to the key that is used to sign the build provenance. The key is stored in one of the following formats:

     1. `gcpkms://projects/cloud-aoss/locations/global/keyRings/cloud-aoss-ring/cryptoKeys/KEY_NAME`
     2. `gcpkms://projects/cloud-aoss/locations/global/keyRings/cloud-aoss-ring/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION`

Where KEY_NAME and KEY_VERSION are the name and version of the Cloud Key Management Service key.

The public key is stored in a Cloud Storage bucket that is owned by Assured OSS.

Retrieve the public key using the Google Cloud CLI. Use one of the following commands:

     * If only KEY_NAME is present:
           
           gcloud storage cp gs://cloud-aoss/keys/KEY_NAME-public.pem PATH_TO_LOCAL_STORE
           

     * If both KEY_NAME and KEY_VERSION are present:
           
           gcloud storage cp gs://cloud-aoss/keys/KEY_NAME-KEY_VERSION-public.pem PATH_TO_LOCAL_STORE
           

Replace the following :

     * KEY_NAME with the name of the Cloud Key Management Service key.
     * KEY_VERSION with the version of the Cloud Key Management Service key.
     * PATH_TO_LOCAL_STORE with the name of the local path for storing the public key.
  4. Verify the provenance signature.

     1. To verify the signature, run the following command:
            
            cosign verify-blob-attestation --insecure-ignore-tlog --key KEY_REF --signature signature.sig --type slsaprovenance --check-claims=false /dev/null
            

Replace the following:

        * KEY_REF: The path to the public key you downloaded in the previous step.
        * signature.sig: The file containing the signature retrieved in the previous step.

The following output is returned after the command runs successfully:

`Verified OK`

     2. To also verify the artifact hash associated with the provenance, use the following command:
            
            cosign verify-blob-attestation --insecure-ignore-tlog --key KEY_REF --signature signature.sig --type slsaprovenance --check-claims=true ARTIFACT_PATH 
            

Replace the following:

        * KEY_REF: The path to the public key you downloaded in the previous step.
        * signature.sig: The file containing the signature retrieved in the previous step.
        * ARTIFACT_PATH: The path to the artifact.

The following output is returned after the command runs successfully:

`Verified OK`




## What's next

  * [Subscribe to notifications](https://docs.cloud.google.com/assured-open-source-software/docs/use-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
