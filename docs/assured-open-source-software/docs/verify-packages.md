---
url: https://docs.cloud.google.com/assured-open-source-software/docs/verify-packages/
title: Verify signatures in the Assured OSS free tier \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:16.244613+00:00
---

# Verify signatures in the Assured OSS free tier  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/verify-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Verify signatures in the Assured OSS free tier Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to verify the signature on the Assured OSS artifacts.

This page applies to the free tier only. For the premium tier, see [Access security metadata and verify packages](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata).

## Package verification

Package signatures are stored separately from the package in a Cloud Storage bucket in a zip format. You can verify signatures using the [Assured OSS verifier tool (`aoss-verifier`)](https://github.com/google/aoss-verifier/blob/main/README.md) or using a verification script.

### Using the aoss-verifier tool

Before using this tool, make sure Go is installed on your system. If Go is not installed, install Go from the [Go website](https://golang.org/doc/install).

  1. To verify the authenticity and integrity of open source software packages, install the [aoss-verifier](https://github.com/google/aoss-verifier) tool.

  2. Export `$(go env GOPATH)/bin`, and run the `aoss-verifier verify-package` command.
         
         aoss-verifier verify-package \
            --language LANGUAGE \
            --package_id PACKAGE_ID \
            --version VERSION \
            --artifact_path ARTIFACT_PATH \
            [--disable_certificate_verification] \
            [--temp_downloads_path TEMP_DOWNLOADS_DIR_PATH] \
            [--disable_deletes]
         

Replace the following:

     * LANGUAGE: The programming package language, either `java` or `python`. The value must be in lower case.
     * PACKAGE_ID: for Java, it's groupId:artifactId and for Python it's packageName. The value must be in lower case.
     * VERSION: The version of the package.
     * ARTIFACT_PATH: The path to the data file in your local directory that you want to verify. Use the following filename extensions: 
       * `jar` file extension for a Java package
       * `whl` file extension for a Python package

`--disable_certificate_verification` is an optional flag which skips matching leaf certificate to the root certificate through the certificate chain, if used.

`--temp_downloads_path` is an optional flag to set the path where you want to download the files. (replace TEMP_DOWNLOADS_DIR_PATH). If this flag isn't set, the files are downloaded to the `tmp_downloads` folder in the current directory.

`--disable_deletes` is an optional flag which keeps the downloaded files. By default, the tool cleans all the downloaded files.




Refer the [README](https://github.com/google/aoss-verifier#readme) for further information.

### Using verification script

This section describes how to use a verification script to verify the signatures of downloaded packages.

#### Step 1: Get the signature URL

The URL of the zip file is available in the security metadata of each package. The following example is a sample from [Container Analysis metadata](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis).

As shown in the following example, you can find the signature zip URL in the `description: digestUrl` field.
    
    
    package {
      distribution {
        cpe_uri: "cpe:2.3:a:JAVA::com.fasterxml.jackson.core:jackson-databind:2.13.3:*:*:*:*:*:*:*"
        maintainer: "<nil>"
        url: "https://us-maven.pkg.dev/cloud-aoss/cloud-aoss-java/com/fasterxml/jackson/core/jackson-databind/2.13.3/jackson-databind-2.13.3.jar"
        description: "{\n \"artifactMetadataList\": [\n {\n \"digestUrl\": \**"gs://cloud-aoss/java/com.fasterxml.jackson.core:jackson-databind/2.13.3/jackson-databind-2.13.3_binary_2022-10-12T06:54:05Z.zip** \"\n }\n ]\n}"
      }
      distribution {
        cpe_uri: "cpe:2.3:a:JAVA::com.fasterxml.jackson.core:jackson-databind:2.13.3:*:*:*:*:*:*:*"
        url: "https://us-maven.pkg.dev/cloud-aoss/cloud-aoss-java/com/fasterxml/jackson/core/jackson-databind/2.13.3/jackson-databind-2.13.3-sources.jar"
        description: "{\n  \"digestUrl\": \"gs://cloud-aoss/java/com.fasterxml.jackson.core:jackson-databind/2.13.3/jackson-databind-2.13.3-sources_source_2022-10-12T06:54:05Z.zip\"\n}"
      }
    }
    

Sample example from Cloud Storage metadata (`buildInfo.json file`). As shown in the following example, you can get the signature zip URL from the `externalRefs` : `referenceLocator` field.
    
    
    "packages": [
            {
                "SPDXID": "SPDXRef-Package-logback-core-1.2.11.jar",
                "checksums": [
                    {
                        "algorithm": "SHA256",
                        "checksumValue": "c847e0e310acda8bc1347c9d9cc051e91210b9f943e131fceb5034c2f0c9a5d8"
                    }
                ],
                "downloadLocation": "https://us-maven.pkg.dev/cloud-aoss/cloud-aoss-java/ch/qos/logback/logback-core/1.2.11/logback-core-1.2.11.jar",
                "externalRefs": [
                    {
                        "referenceCategory": "SECURITY",
                        "referenceLocator": "cpe:2.3:a:*:JAVA\\:\\:ch\\.qos\\.logback\\:logback\\-core:1\\.2\\.11:*:*:*:*:*:*:*",
                        "referenceType": "cpe23Type"
                    },
                    {
                        "referenceCategory": "OTHER",
                        "referenceLocator": "**gs://cloud-aoss/java/ch.qos.logback:logback-core/1.2.11/logback-core-1.2.11_binary_2022-10-12T14:19:11Z.zip"** ,
                        "referenceType": "digestURL"
                    }
                ],
    
    

You can use the local signature zip for manual verification or the Cloud Storage URL directly for using the verification script. You can download the `signature.zip` file using the following steps:

  1. [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication) using Application Default Credentials (ADC).

  2. Download the `signature.zip` using the following command:
         
         gcloud storage cp SIGNATURE_ZIP_URL PATH_TO_LOCAL_STORE --recursive
         

Replace the following:

     * SIGNATURE_ZIP_URL: the signature zip URL.
     * PATH_TO_LOCAL_STORE: the local path where you want to download the file.



#### Step 2: Get the root certificate

To access the root certificate, use the following URL:
    
    
    https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
    

You can download the certificate locally or use the certificate link directly. To download the certificate, run the following command:
    
    
    curl -o PATH_TO_LOCAL_STORE/ca.crt https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
    

Replace PATH_TO_LOCAL_STORE with the local path where you want to download the certificate.

#### Step 3: Get the package file location

The file we would be verifying is the jar for Java packages and wheel file for Python packages. That file would be the PATH_TO_DATA_FILE for verification.

#### Step 4: Verification

You can manually verify the signature zip using the steps at [manual signature verification](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_manually) or can use the [verification script](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_using_a_script).

To verify using verification script, run the following commands:

  1. Download the verification script and give permissions.
         
         gcloud storage cp "gs://cloud-aoss/utils/signature-verification/v1.0/signatureverification.sh" . --recursive
           chmod +x signatureverification.sh
         

  2. Run the verification script and verify. You can use the remote URLs or local paths for signature zip and root certificate.
         
         ./signatureverification.sh --data_file_path PATH_TO_DATA_FILE --signature_url SIGNATURE_ZIP_URL --root_cert_url ROOT_CERT_URL
         

Replace the following:

     * PATH_TO_DATA_FILE with the path to the package file identified in step 3
     * SIGNATURE_ZIP_URL with the signature zip URL obtained in step 1.
     * ROOT_CERT_URL with the root certificate URL obtained in step 2. 



## Metadata verification

This section explains how you can verify the signature on the Assured OSS metadata accessed using Cloud Storage.

### Use the aoss-verifier tool

Use the `aoss-verifier` tool to verify metadata.

Before using this tool, [install Go](https://golang.org/doc/install).

  1. Install the [aoss-verifier](https://github.com/google/aoss-verifier) tool.

  2. Export `$(go env GOPATH)/bin`, and run the `aoss-verifier verify-metadata` command.
         
         aoss-verifier verify-metadata \
            --metadata_type TYPE \
            --language LANGUAGE \
            --package_id PACKAGE_ID \
            --version VERSION \
            [--disable_certificate_verification] \
            [--temp_downloads_path TEMP_DOWNLOADS_DIR_PATH] \
            [--disable_deletes]
         

Replace the following:

     * TYPE: The possible values are `buildinfo`, `vexinfo`, and `healthinfo`.
     * LANGUAGE: The programming package language, either `java` or `python`. The value must be in lower case.
     * PACKAGE_ID: For Java, the format is groupId:artifactId. For Python, the format is packageName. The value must be in lower case.
     * VERSION: The version of the package.

`--disable_certificate_verification` is an optional flag which skips matching the leaf certificate to the root certificate through the certificate chain, if used.

`--temp_downloads_path` is an optional flag to set the path where you want to download the files (replace TEMP_DOWNLOADS_DIR_PATH). If this flag isn't set, the files are downloaded to the `tmp_downloads` folder in the current directory.

`--disable_deletes` is an optional flag which keeps the downloaded files. By default, the tool cleans all the downloaded files.




For more information, see the [README](https://github.com/google/aoss-verifier#readme).

### Using verification script

This section describes how to use a verification script to verify the security metadata file.

#### Step 1: Get the signature zip and metadata file

We can access the metadata as in [Access Metadata](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-cloud-storage). The metadata file would be present with the signature.zip file.

Example - contents of `buildInfo.zip`
    
    
    buildInfo.json
    signature.zip
    

The `buildInfo.json` is the metadata file required to be verified and the `signature.zip` is the signature zip.

#### Step 2: Get the root certificate

Use the following URL link to get the root certificate:
    
    
    https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
    

You can download the certificate locally or use the certificate link directly. To download the certificate, run the following command:
    
    
    curl -o PATH_TO_LOCAL_STORE/ca.crt https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
    

Replace PATH_TO_LOCAL_STORE with the local path where you want to download the certificate.

#### Step 3: Verification

You can verify the `signature.zip` [using manual verification](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_manually) or by [using the verification script](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_using_a_script).

To verify using verification script, run the following commands:

  1. Download the verification script and give permissions.
         
         gcloud storage cp "gs://cloud-aoss/utils/signature-verification/v1.0/signatureverification.sh" . --recursive
           chmod +x signatureverification.sh
         

  2. Run the verification script and verify. You should use the local path for the signature zip. For the root certificate, you can use either the URL or local path. The data file would be the metadata file we are verifying - `buildInfo.json`, `vexInfo.json` or `healthInfo.json`.
         
         ./signatureverification.sh --data_file_path PATH_TO_DATA_FILE --signature_local_path SIGNATURE_LOCAL_PATH --root_cert_url ROOT_CERT_URL
         

Replace the following:

     * PATH_TO_DATA_FILE with the metadata file we are verifying as obtained in Step 1.

     * SIGNATURE_LOCAL_PATH with the signature zip URL obtained in step 1.

     * ROOT_CERT_URL with the root certificate URL obtained in step 2.

In case you want to use a local certificate already downloaded, use this option instead:
           
           --root_cert_local ROOT_CERT_LOCAL
           

Replace ROOT_CERT_LOCAL with the local certificate path.




## Utility script verification

Assured OSS provides three utility scripts. This section describes how to verify the signature on these scripts.

### Python `Requirements.txt` generator

Access the signature for this file at `gs://cloud-aoss/utils/python-requirements-txt/v1.0/generator-sig.zip`. You can verify the `signature.zip` either [using manual verification](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_manually) or [using the verification script](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_using_a_script). To quick verify the signature using the verification script, follow these steps:

  1. [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication).

  2. If you have not already downloaded the `requirements.txt` generator script file, download the file.
         
         gcloud storage cp "gs://cloud-aoss/utils/python-requirements-txt/v1.0/generator.sh" . --recursive
         

  3. Fetch the root certificate. The URL link is `https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt` You can download the certificate locally or use the certificate link directly. To download the certificate, run the following command:
         
         curl -o PATH_TO_LOCAL_STORE/ca.crt "https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt"
         

Replace PATH_TO_LOCAL_STORE with the local path where you want to download the certificate

  4. Download the verification script if you have not already done so.
         
         gcloud storage cp "gs://cloud-aoss/utils/signature-verification/v1.0/signatureverification.sh" . --recursive
         chmod +x signatureverification.sh
         

  5. Run the verification script and verify.
         
         ./signatureverification.sh --data_file_path PATH_TO_DATA_FILE --signature_url "gs://cloud-aoss/utils/python-requirements-txt/v1.0/generator-sig.zip" --root_cert_url ROOT_CERT_URL
         

Replace the following:

     * PATH_TO_DATA_FILE with the local path of the `generator.sh` script we want to verify as obtained in Step 2.
     * ROOT_CERT_URL with the root certificate URL. In case you want to use a local certificate already downloaded, run the following command: 
    
    –root_cert_local ROOT_CERT_LOCAL
    

Replace ROOT_CERT_LOCAL with the local path of the root certificate.




### Signature verification script

Access the signature for this file at `gs://cloud-aoss/utils/signature-verification/v1.0/signatureverification-sig.zip`. You can verify the `signature.zip` either [using manual verification](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_manually) or [using the verification script](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_using_a_script). To quick verify the signature using the verification script, follow these steps:

  1. [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication).

  2. If you have not already downloaded the signature verification script file, download the file.
         
         gcloud storage cp "gs://cloud-aoss/utils/signature-verification/v1.0/signatureverification.sh" . --recursive
         chmod +x signatureverification.sh
         

  3. Fetch the root certificate. The URL link is `https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt` You can download the certificate locally or use the certificate link directly. Command to download the certificate:
         
         curl -o PATH_TO_LOCAL_STORE/ca.crt https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
         

Replace PATH_TO_LOCAL_STORE with the local path where you want to download the certificate

  4. Run the verification script and verify.
         
         ./signatureverification.sh --data_file_path PATH_TO_DATA_FILE --signature_url "gs://cloud-aoss/utils/signature-verification/v1.0/signatureverification-sig.zip" --root_cert_url ROOT_CERT_URL
         

Replace the following:

PATH_TO_DATA_FILE with the local path of the verification script we want to verify as obtained in Step 2. ROOT_CERT_URL with the root certificate URL. In case you want to use a local certificate already downloaded, use this option instead:
         
         –root_cert_local ROOT_CERT_LOCAL
         

Replace ROOT_CERT_LOCAL with the local path of the root certificate.




### Download metadata script

Access the signature for this file at `gs://cloud-aoss/utils/python-download-metadata/v1.1/download_metadata-sig.zip`. You can verify the `signature.zip` either [using manual verification](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_manually) or [using the verification script](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview#verify_signatures_using_a_script). To quick verify the signature using the verification script, follow these steps:

  1. [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication).

  2. If you have not already downloaded the `download_metadata.py` script file, download the file.
         
         gcloud storage cp "gs://cloud-aoss/utils/python-download-metadata/v1.1/download_metadata.py" . --recursive
         

  3. Fetch the root certificate. The URL link is `https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt` You can download the certificate locally or use the certificate link directly.

To download the certificate, run the following command:
         
         curl -o PATH_TO_LOCAL_STORE/ca.crt https://privateca-content-6333d504-0000-2df7-afd6-30fd38154590.storage.googleapis.com/a2c725a592f1d586f1f8/ca.crt
         

Replace PATH_TO_LOCAL_STORE with the local path where you want to download the certificate

  4. Download the verification script.
         
         gcloud storage cp "gs://cloud-aoss/utils/signature-verification/v1.0/signatureverification.sh" . --recursive
         chmod +x signatureverification.sh
         

  5. Run the verification script and verify.
         
         ./signatureverification.sh --data_file_path PATH_TO_DATA_FILE --signature_url gs://cloud-aoss/utils/python-download-metadata/v1.1/download_metadata-sig.zip --root_cert_url ROOT_CERT_URL
         

Replace the following:

     * PATH_TO_DATA_FILE with the local path of the `download_metadata.py` script we want to verify as obtained in Step 2.
     * ROOT_CERT_URL with the root certificate URL. In case you want to use a local certificate already downloaded, run the following command: 
    
    –root_cert_local ROOT_CERT_LOCAL
    

Replace ROOT_CERT_LOCAL with the local path of the root certificate.




## What's next

  * [Verify the build provenance](https://docs.cloud.google.com/assured-open-source-software/docs/verify-build-provenance)
  * [Learn about protecting your software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
