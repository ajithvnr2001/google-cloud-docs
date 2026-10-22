---
url: https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis/
title: Access metadata using the Artifact Analysis API \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:59.935090+00:00
---

# Access metadata using the Artifact Analysis API  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Access metadata using the Artifact Analysis API Stay organized with collections  Save and categorize content based on your preferences. 

Assured OSS provides security metadata for every package available. Each version of the package has its own metadata. This page explains what information is provided as part of the metadata and how you can access this metadata.

You can access the security metadata using one of the following options:

  * Artifact Analysis API
  * Cloud Storage



This page applies to the free tier only.

## Security metadata

[Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-analysis) provides metadata storage according to the open source [Grafeas](https://github.com/grafeas/grafeas/tree/master/proto/v1) model. The following information is provided for each version of the package:

  * A [PackageNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes#packagenote) for each version released of the package by Assured OSS. The package note contains the following:

    * [`distribution`](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes#distribution) where each `distribution` corresponds to one artifact being provided by Assured OSS. It includes the location and digest `url` (from where the signature and hash can be downloaded) for binary and reproducible sources.
    * [`relatedURL`](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/RelatedUrl) that contains links to metadata like build provenance, test attestation, and vulnerabilities.
  * A [BuildOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#buildoccurrence). The link to this build occurrence is given in the package note's `relatedURL` section against the label `BUILD_OCCURRENCE`. The `intotoStatement` in the build occurrence contains the [SLSA v0.2 provenance](https://slsa.dev/provenance/v0.2#schema).

  * A second [BuildOccurrenance](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#buildoccurrence). The link to this build occurrence is given in the package note's `relatedURL` section against the label `ORIGINAL_SOURCE_PROVENANCE`. This file contains the original source (GitHub) details in the form of [Source](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#Source).

  * An [AttestationOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#attestationoccurrence). The link to this attestation occurrence is given in the package note's `relatedURL` section against the label `TEST_OCCURRENCE`. The serialized payload in the attestation contains JSON representing all security testing done on the package version.

  * A second [AttestationOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#attestationoccurrence). The link to this attestation occurrence is given in the package note's `relatedURL` section against the label `PACKAGE_ATTESTATION_OCCURRENCE`. The JSON serialized payload in the attestation is the payload of the package note and the signature for it. This attestation is used to verify the integrity of the package note's content.

  * A [VulnerabilityNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes#vulnerabilitynote) and [VulnerabilityOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences#vulnerabilityoccurrence) for every vulnerability associated with the package. The note and occurrence combined provide information about vulnerabilities such as the vulnerability summary or description, severity, CVSSV3 score, affected and fixed version information, and remediation.




## Access security metadata from Artifact Analysis

You can access the security metadata from Artifact Analysis using the [Artifact Analysis API clients](https://docs.cloud.google.com/artifact-analysis/docs/store-retrieve-metadata) which are available in different languages. To get started with the Cloud Client Libraries for the Artifact Analysis API, see [Install the required Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries).

To access the security metadata, follow these steps:

**Note:** If you're using your own service account in your Google Cloud project, you must [enable the Artifact Analysis API](https://docs.cloud.google.com/artifact-analysis/docs/enable-metadata#enable-metadata).

### Step 1 - Set up authentication

[Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication) using Application Default Credentials (ADC).

### Step 2 - Fetch security metadata

To fetch security metadata, create a _note_name_ package using the following information:

  * Project_ID: The alpha-numeric identifier for your Google Cloud project.
  * Package Language: Java or Python. This must be in uppercase.
  * Package_ID: for Java, it's groupId_artifactId and for Python it's packageName. This value is case sensitive. The valid casing for the release name of the package can be found in [Listing all Packages in Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#query_the_list_of_packages).
  * Version: The version of the package.



The _note_name_ should have the following structure: `projects/<project_id>/notes/<language>-<package_id>-<version>`.

For example: `projects/cloud-aoss/notes/JAVA-org.apache.commons_commons-compress-1.21`

Option 1:

If you're using the [Container Analysis Client Libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries), use `getNotes` with the _note_name_ to query the `PackageNote`. The `PackageNote` has links to other notes and occurrences.

Option 2:

If you're using the `curl` command, use the following command:
    
    
    curl  -H "Content-Type: application/json" -H   "Authorization: Bearer $(gcloud auth print-access-token)" $URL
    

  * For Java, use URL: `https://containeranalysis.googleapis.com/v1/projects/cloud-aoss/notes/JAVA-org.jsoup_jsoup-1.15.2`
  * For Python, use URL: `https://containeranalysis.googleapis.com/v1/projects/cloud-aoss/notes/PYTHON-Flask-Cors-3.0.10`



#### Sample Metadata
    
    
    {
      "name": "projects/cloud-aoss/notes/JAVA-org.jsoup_jsoup-1.15.2",
      "kind": "PACKAGE",
      "relatedUrl": [
        {
          "url": "projects/cloud-aoss/occurrences/621d7e7b-8e6c-4313-b24b-eae3a1d1b884",
          "label": "ORIGINAL_SOURCE_PROVENANCE"
        },
        {
          "url": "https://containeranalysis.googleapis.com/v1/projects/cloud-aoss/occurrences/a0967d97-634c-4066-b6da-0a723273a165",
          "label": "BUILD_OCCURRENCE"
        },
        {
          "url": "projects/cloud-aoss/occurrences/6005db73-7310-44f9-9a36-6ca0174732a1",
          "label": "TEST_OCCURRENCE"
        },
        {
          "url": "projects/cloud-aoss/notes/GHSA-gp7f-rwcx-9369",
          "label": "VULNERABILITY_GHSA-gp7f-rwcx-9369"
        }
      ],
      "createTime": "2022-10-12T06:48:19.162016Z",
      "updateTime": "2022-10-18T05:31:15.081736Z",
      "package": {
        "distribution": [
          {
            "cpeUri": "cpe:2.3:a:JAVA::org.jsoup:jsoup:1.15.2:*:*:*:*:*:*:*",
            "url": "https://us-maven.pkg.dev/…/org/jsoup/jsoup/1.15.2/jsoup-1.15.2.jar",
            "description": "..."
          },
          {
            "cpeUri": "cpe:2.3:a:JAVA::org.jsoup:jsoup:1.15.2:*:*:*:*:*:*:*",
            "url": "https://us-maven.pkg.dev/…/org/jsoup/jsoup/1.15.2/jsoup-1.15.2-sources.jar",
            "description": "..."
          }
    ]}}
    

Use the note and occurrence names provided in the `relatedURL` map to fetch additional data related to source, build, test, and vulnerability. To do this, use the `GetNote` and `GetOccurrence` APIs or `curl` commands. For `BUILD_OCCURRENCE`, remove the initial prefix of `https://containeranalysis.googleapis.com/v1/` when you use the API. For other entities, use the URLs directly as `note_name` or `occurrence_name` in API parameter.

#### Sample Python script

A sample Python script that prints the entire downloaded metadata is available at the following Cloud Storage location along with its `README` file:

`gs://cloud-aoss/utils/python-download-metadata/v1.1`

Follow these steps to download the script using the Google Cloud CLI:

  1. [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication) using Application Default Credentials (ADC).

  2. [Install the container-analysis client library](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest). Specifically this command should install:
         
         pip install google-cloud-containeranalysis
         

  3. Install the cloud-kms and cryptography packages using the following commands:
         
         pip install --upgrade google-cloud-kms
         pip install --upgrade cryptography
         

  4. Download the `download_metadata.py` to your system using the following command:
         
         gcloud storage cp gs://cloud-aoss/utils/python-download-metadata/v1.1/download_metadata.py
         PATH_TO_LOCAL_STORE --recursive
         

Replace PATH_TO_LOCAL_STORE with the local path where you want to save the file.

  5. Download the `README.md` that contains the instructions to use the script using the following command:
         
         gcloud storage cp gs://cloud-aoss/utils/python-download-metadata/v1.1/README.md PATH_TO_LOCAL_STORE --recursive
         

Replace PATH_TO_LOCAL_STORE with the local path where you want to save the file.




#### Sample Command
    
    
    python ./download_metadata.py -l 'JAVA' -p 'org.apache.logging.log4j:log4j-core' -v '2.17.1'
    

To verify the signatures in the container analysis metadata, add the following command to the script:
    
    
    python ./download_metadata.py -l 'JAVA' -p 'org.apache.logging.log4j:log4j-core' -v '2.17.1' -s`
    

**Note:** Use the package name and version that is available in the Assured OSS repository.

## What's next

  * [Subscribe to notifications](https://docs.cloud.google.com/assured-open-source-software/docs/use-notifications)
  * [Artifact signature overview](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview)
  * [Verify signatures](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview)
  * [Verify the build provenance](https://docs.cloud.google.com/assured-open-source-software/docs/verify-build-provenance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
