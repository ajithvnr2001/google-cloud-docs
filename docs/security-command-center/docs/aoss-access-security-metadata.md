---
url: https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata/
title: Access security metadata and verify packages \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:12.439928+00:00
---

# Access security metadata and verify packages  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Access security metadata and verify packages Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document describes how to access security metadata from the `assuredoss-metadata` Cloud Storage bucket. For a description of the security metadata, see [Security metadata fields](https://docs.cloud.google.com/assured-open-source-software/docs/security-metadata-fields).

This document applies to the Assured OSS premium tier only. For the free tier, see [Verify signatures in the Assured OSS free tier](https://docs.cloud.google.com/assured-open-source-software/docs/verify-packages).

## Before you begin

  1. [Integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).

  2. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Assured OSS for the requested service accounts.


**Note:** To access the security metadata repository after setting up Assured OSS premium using gcloud, send an email to [customer-support-aoss@google.com](mailto:customer-support-aoss@google.com) with the service accounts that you enabled for Assured OSS.

## Extract the metadata

You can use either `gcloud` or `curl` commands to download the metadata. Construct the URL for both using the following information:

  * **Language:** `java`, `python`, `golang`, or `javascript`. The value must be lowercase.
  * **Package_ID:** one of the following:

    * Java: `groupId:artifactId`
    * Python: `packageName`
    * JavaScript (NPM): @scope/package-name or package-name
    * Go: `packageName`

The value must be lower case.

  * **Version:** the version of the package.




The URL must have the following format:

### gcloud

`gs://assuredoss-metadata/language/package_id/version/metadata.json`

The URL must be in lowercase.

Sample URLs include the following:

  * Sample Python URL: `gs://assuredoss-metadata/python/blessed/1.20.0/metadata.json`

  * Sample Java URL: `gs://assuredoss-metadata/java/org.apache.logging.log4j:log4j-core/2.17.1/metadata.json`

  * Sample JavaScript URL: `gs://assuredoss-metadata/javascript/@stoplight/spectral-core/0.0.0/metadata.json`

  * Sample Go URL: `gs://assuredoss-metadata/golang/github.com/rs/zerolog/1.9.1/metadata.json`




### curl

`https://storage.googleapis.com/assuredoss-metadata/language/package_id/version/metadata.json`

The URL must be lowercase.

Sample URLs include the following:

  * Sample Python URL: `https://storage.googleapis.com/assuredoss-metadata/python/blessed/1.20.0/metadata.json`

  * Sample Java URL: `https://storage.googleapis.com/assuredoss-metadata/java/org.apache.logging.log4j:log4j-core/2.17.1/metadata.json`

  * Sample JavaScript URL: `https://storage.googleapis.com/assuredoss-metadata/javascript/@stoplight/spectral-core/0.0.0/metadata.json`

  * Sample Go URL: `https://storage.googleapis.com/assuredoss-metadata/golang/github.com/rs/zerolog/1.9.1/metadata.json`




  1. Download the metadata:



### gcloud
    
    
    gcloud storage cp "gs://assuredoss-metadata/language/package_id/version/metadata.json" outputFolderLocation
    

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -L https://storage.googleapis.com/assuredoss-metadata/language/package_id/version/metadata.json -o metadata.json
    

You can verify the signatures. There are two options:

  * Verify the signatures using the aoss-verifier tool
  * Verify the signatures of downloaded packages manually



## Verify the signatures of downloaded packages using the aoss-verifier tool

Use the `aoss-verifier` tool to verify package metadata.

Before using this tool, [install Go](https://golang.org/doc/install).

  1. Install the [aoss-verifier](https://github.com/google/aoss-verifier) tool.

  2. Export `$(go env GOPATH)/bin`.

  3. Run the `aoss-verifier verify-metadata` command.
         
         aoss-verifier verify-metadata \
            --metadata_type TYPE \
            --language LANGUAGE \
            --package_id PACKAGE_ID \
            --version VERSION \
            [--disable_certificate_verification] \
            [--temp_downloads_path TEMP_DOWNLOADS_DIR_PATH] \
            [--disable_deletes]
         

Replace the following:

     * `TYPE`: The possible values are `premiuminfo`.
     * `LANGUAGE`: The package language. The value must be in lowercase.
     * `PACKAGE_ID`: For Java, the format is `groupId:artifactId`. For Python and Go, the format is `packageName`. For JavaScript (NPM), the format is `@scope/package-name` or `package-name`. The value must be in lower case.
     * `VERSION`: The version of the package.

`--disable_certificate_verification` is an optional flag which skips matching the leaf certificate to the root certificate through the certificate chain, if used.

`--temp_downloads_path` is an optional flag to set the path where you want to download the files (replace `TEMP_DOWNLOADS_DIR_PATH`). If the flag isn't set, the files are downloaded to the `tmp_downloads` folder in the current directory.

`--disable_deletes` is an optional flag which keeps the downloaded files. By default, the tool cleans all the downloaded files.




For more information, see the [README](https://github.com/google/aoss-verifier#readme).

## Verify the signatures of downloaded packages manually

You can verify the artifact signature only for the binaries that are securely built by Assured OSS, not the ones that are provided by Assured OSS through proxies.

To verify signatures manually, you can use various tools. The following steps use gcloud CLI, OpenSSL (version 3.0.1 or higher), and [jq](https://jqlang.github.io/jq/) (1.7.1 or higher) to verify the signatures on Linux.

  1. [Download the metadata file](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata). As described in [Security metadata fields](https://docs.cloud.google.com/security-command-center/docs/aoss-security-metadata-fields#build_information), the metadata file contains an `SBOM` field inside the `buildInfo` field. The SBOM contains the artifact (for example, a JAR or EGG file) that was built along with an annotation that represents the signature. This artifact lets you determine the SPDX ID.

For example, if the artifact name is `artifact_name`, the `spdx_id` is `SPDXRef-Package-artifact_name`. To validate a package that is named `gradio-3.30.0-py3-none-any.whl`, the `spdx_id` is `SPDXRef-Package-gradio-3.30.0-py3-none-any.whl`.

  2. Extract the SHA-256 digest from the metadata file:
         
         cat METADATA_FILENAME | jq -rj '.buildInfo' | jq -rj '.sbom' | jq -rj '.packages' | jq '.[] | select(.SPDXID=="SPDX_ID")' | jq -rj '.annotations[0].comment' | jq -rj '.digest[0].digest' | cut -d ' ' -f1 > expectedDigest.txt
         

Replace the following:

     * `METADATA_FILENAME`: The name of your security metadata file.

     * `SPDX_ID`: The SPDX identifier.

  3. Compute the artifact digest:
         
         sha256sum ARTIFACT_FILE | cut -d ' ' -f1 > actualDigest.txt
         

Replace `ARTIFACT_FILE` with the name of the artifact file.

**Note:** On macOS, you can use `shasum -a 256` to calculate the digest.
  4. Check for any differences between the two: 
         
         diff actualDigest.txt expectedDigest.txt
         

If there is no difference, there is no output.

  5. Extract the digest of the field to a `.bin` file:
         
         cat METADATA_FILENAME | jq -rj '.buildInfo' | jq -rj '.sbom' | jq -rj '.packages' | jq '.[] | select(.SPDXID=="SPDX_ID")' | jq -rj '.annotations[0].comment' | jq -rj '.digest[0].digest' | cut -d ':' -f2 | xxd -r -p > digest.bin
         

  6. Extract the signature of the digest to a `.sig` file:
         
         cat METADATA_FILENAME | jq -rj '.buildInfo' | jq -rj '.sbom' | jq -rj '.packages' | jq '.[] | select(.SPDXID=="SPDX_ID")' | jq -rj '.annotations[0].comment' | jq -rj '.signature[0].signature' | xxd -r -p > sig.sig
         

  7. Extract the public key from the public certificate to a `.pem` file:
         
         cat METADATA_FILENAME | jq -rj '.buildInfo' | jq -rj '.sbom' | jq -rj '.packages' | jq '.[] | select(.SPDXID=="SPDX_ID")' | jq -rj '.annotations[0].comment' | jq -rj '.certInfo.cert' | openssl x509 -pubkey -noout  > pubKey.pem
         

  8. Verify the signature of the digest using the extracted public key:
         
         openssl pkeyutl -in digest.bin -inkey pubKey.pem -pubin -verify -sigfile sig.sig
         

If successful, this command returns `Signature Verified Successfully`. You can verify the certificate.

  9. Extract the public certificate to a `.pem` file:
         
         cat METADATA_FILENAME | jq -rj '.buildInfo' | jq -rj '.sbom' | jq -rj '.packages' | jq '.[] | select(.SPDXID=="SPDX_ID")' | jq -rj '.annotations[0].comment' | jq -rj '.certInfo.cert' > cert.pem
         

  10. Download the root certificate (`ca.crt` in the following command):
         
         curl -o ca.crt https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
         

  11. Verify the certificate using the extracted certificate and the root certificate:
         
         openssl verify -verbose -CAfile ca.crt cert.pem
         

If successful, this command returns `cert.pem: OK`.




## Verify the signatures for security metadata fields

You can verify the signature of the following fields in the security metadata file independently:

  * `buildInfo`
  * `vexInfo`
  * `healthInfo` (if present)



The data inside the fields are hashed using SHA-256, and then the hash is signed using the ECDSAP256_DER algorithm. The certificate and certificate chain are provided inside the metadata so that you can verify the signature. Use the following root certificate to verify the certificate chain:
    
    
    https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
    

You can verify signatures manually or you can verify signatures using the [Assured OSS Verifier Tool](https://github.com/google/aoss-verifier/blob/main/README.md).

The following steps describe how to manually verify the signature of the `buildInfo` field in the `metadata.json` file. You can use similar steps to verify the signature of the `vexInfo` field or the `healthInfo` field.

You can verify signatures using various tools. The following example uses gcloud CLI, OpenSSL (version 3.0.1 or later) and [jq](https://jqlang.github.io/jq/) (1.7.1 or later) to verify the signatures on a Linux system.

  1. Generate the SHA-256 digest of the field:
         
         cat metadata.json | jq -rj '.buildInfo' | sha256sum | cut -d ' ' -f1 > actualDigest.txt
         

**Note:** On macOS, you can use `shasum -a 256` to calculate the digest.
  2. Extract the digest of the field that is provided in the `metadata.json` file:
         
         cat metadata.json | jq -rj '.buildInfoSignature.digest[0].digest' | cut -d ':' -f2 > expectedDigest.txt
         

  3. Check for any differences between the two digests:
         
         diff actualDigest.txt expectedDigest.txt
         

If there is no difference then there will be no output, which is the ideal case. You can verify the signature.

  4. Extract the digest of the field to a `.bin` file:
         
         cat metadata.json | jq -rj '.buildInfoSignature.digest[0].digest' | cut -d ':' -f2 | xxd -r -p > digest.bin
         

  5. Extract the signature of the digest to a `.sig` file:
         
         cat metadata.json | jq -rj '.buildInfoSignature.signature[0].signature' | xxd -r -p > sig.sig
         

  6. Extract the public key from the public certificate to a `.pem` file:
         
         cat metadata.json | jq -rj '.buildInfoSignature.certInfo.cert' | openssl x509 -pubkey -noout  > pubKey.pem
         

  7. Verify the signature of the digest using the extracted public key:
         
         openssl pkeyutl -in digest.bin -inkey pubKey.pem -pubin -verify -sigfile sig.sig
         

If the verification is successful, this command returns `Signature Verified Successfully`. You can verify the certificate.

  8. Extract the public certificate to a `.pem` file:
         
         cat metadata.json | jq -rj '.buildInfoSignature.certInfo.cert' > cert.pem
         

  9. Download the root certificate, named `ca.crt` in the following command:
         
         curl -o ca.crt https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
         

  10. Verify the certificate using the extracted certificate and the root certificate:
         
         openssl verify -verbose -CAfile ca.crt cert.pem
         

If successful, the command returns `cert.pem: OK`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
