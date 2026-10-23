---
url: https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities/
title: Investigate vulnerabilities \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:27.790553+00:00
---

# Investigate vulnerabilities  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Investigate vulnerabilities Stay organized with collections  Save and categorize content based on your preferences. 

When you hear about a new vulnerability, acting quickly is important. This page provides a list of essential API calls and filters that are pre-constructed for you. Use these API calls to retrieve scan results from Artifact Analysis and gather information about the status of your artifacts.

This content is designed for use with automatic scanning metadata. If your images have exceeded the 30-day [continuous analysis](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types#continuous_analysis) window, you can run a new scan by pushing to Artifact Registry again.

All of the examples on this page access the API directly, but you can also use the [Container Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries), or [gcloud commands](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically#view-gcloud).

## Required permissions

All of these examples use the `ListOccurrences` API method. To call this method, you will need the **Container Analysis Occurrences Viewer** `(roles/containeranalysis.occurrences.viewer)` role for the project that you're analyzing.

  * If you are analyzing projects that you own, you already have the required permissions.

  * If you are analyzing projects that you don't own, use the [IAM access management instructions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to grant permissions.




For more information on types of access for providers and customers using Artifact Analysis, see [permissions](https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control#iam_roles_for_metadata_providers_and_customers).

## View all the vulnerability metadata for an image

Use the filter `kind=VULNERABILITY` with your project ID and the full resource URL for your image, including `https://`:
    
    
      curl -G -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data-urlencode "filter=(kind=\"VULNERABILITY\" AND resourceUrl=\"RESOURCE_URL\")" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * RESOURCE_URL is the complete URL of the image, in the format: `https://HOST_NAME/PROJECT_ID/IMAGE_ID@sha256:HASH`. The `https://` must be included at the beginning of the URL. If you need to find the URL for an image, you can use the call in [View all the metadata for a project](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities#all-metadata).



Output includes a vulnerability list with details such as the severity, mitigation options if available, and the name of the package that contains the vulnerability.

## Check for a specific vulnerability in a project

In most cases, Artifact Analysis uses the [CVE ID](https://cve.mitre.org/cve/identifiers/index.html) as the vulnerability identifier. However, there are some vulnerabilities listed in the [GitHub Advisory Database](https://github.com/advisories) that don't have an associated CVE ID. In this case, Artifact Analysis uses the [GHSA ID](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-ghsa-ids) instead.

The vulnerability ID is included as part of the `noteName` field. It starts with the prefix `CVE` for CVE IDs, and `GHSA` for GHSA IDs. Consider the following sample output from running the command to view all the vulnerabilities for an image:
    
    
    vulnerabilities:
      HIGH:
      - name: projects/my-project/occurrences/1234fh2c-699a-462f-b920-93a80f56f544
        resourceUri: https://my_region-docker.pkg.dev/my-project/my-repo/my-image@sha256:8a1a79b587797c5164ec95977cf7aaaa828694a615947bdaed6a327d5b6a17bb
        noteName: projects/goog-vulnz/notes/CVE-2021-32798
        kind: VULNERABILITY
        ...
      - name: projects/my-project/occurrences/OCCURRENCE_ID
        resourceUri: https://my_region-docker.pkg.dev/my-project/my-repo/my-image@sha256:8a1a79b587797c5164ec95977cf7aaaa828694a615947bdaed6a327d5b6a17bb
        noteName: projects/goog-vulnz/notes/GHSA-884p-74jh-xrg2
        kind: VULNERABILITY
        ...
    

In this example, the first vulnerability has the ID `CVE-2021-32798`, and the second vulnerability has the ID `GHSA-884p-74jh-xrg2`.

After you have your vulnerability ID, you can run the following command to retrieve a list of affected images in your project that have an occurrence ID of VULN_ID:
    
    
      curl -G -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data-urlencode "filter=(noteProjectId=\"goog-vulnz\" AND noteId=\"VULN_ID\")" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * VULN_ID is the ID of the vulnerability as a CVE ID or GHSA ID number, such as `CVE-2021-32798` or `GHSA-884p-74jh-xrg2`.



## Search for vulnerabilities across multiple projects

Use curl [globbing](https://curl.se/docs/manpage.html) to make queries across projects.

For example, the following snippet sets a variable to contain two project IDs, then sends an API call for each project to search for occurrences.
    
    
      PROJECT_IDS="PROJECT_ID_1,PROJECT_ID_2"
    
      curl -G -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://containeranalysis.googleapis.com/v1/projects/{$PROJECT_IDS}/occurrences"
    

Where:

  * PROJECT_ID_1 is the Google Cloud project ID for the first project you want to examine.
  * PROJECT_ID_2 is the Google Cloud project ID for the second project you want to examine.

**Note:** There isn't support for a single API call across multiple projects.

## View all the metadata for a project

Request all [occurrences](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#occurrence) associated with your project ID:
    
    
      curl -X GET -H "Content-Type: application/json" -H \
        "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences
    

Where:

  * PROJECT_ID is your Google Cloud project ID.



The output includes vulnerability information and other [supported metadata types](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#occurrence) associated with your project. For example, your project might have build details or attestations.

## Check for a specific package in a project

Artifact Analysis creates package dependencies for scanned artifacts. To find all the artifacts that have a specific package as a dependency, you can filter by the package name:
    
    
    curl -G -H "Content-Type: application/json" \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    --data-urlencode "filter=(dependencyPackageName=\"PACKAGE_NAME\")" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * PACKAGE_NAME is the name of the package.



## View all package metadata for an image

To view all the different types of package metadata for an image, use the filter `kind=PACKAGE_NAME` with your project ID and the full image resource URL:
    
    
     curl -G -H "Content-Type: application/json" \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       --data-urlencode "filter=(kind=\"PACKAGE\" AND resourceUrl=\"RESOURCE_URL\")" \
       https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * RESOURCE_URL is the complete URL of the image, in the format `https://HOST_NAME/PROJECT_ID/IMAGE_ID@sha256:HASH`. The `https://` must be included at the beginning of the URL. If you need to find the URL for an image, you can use the call from [View all the metadata for a project](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities#all-metadata).



The output includes a dependency list with the dependency name, version, and license information.

## Query a specific occurrence for all available details

You can run a query for more details about an [occurrence](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#occurrence). For example, if you're using [Pub/Sub](https://docs.cloud.google.com/artifact-analysis/docs/pub-sub-notifications) to get notifications about vulnerability occurrences, then Pub/Sub sends basic details to help you identify the occurrence that changed and when the change happened.

The payload includes an occurrence ID. You can use the occurrence ID to query for details to help you triage issues and take action.
    
    
      curl -X GET -H "Content-Type: application/json" -H \
        "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/occurrences/OCCURRENCE_ID
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * OCCURRENCE_ID can be either of the following, depending on the output of the command from [View all the metadata for a project](https://docs.cloud.google.com/artifact-analysis/docs/investigate-vulnerabilities#all-metadata):

    * A numerical value from an occurrences list.
    * The numerical value at the end of the URL from a Pub/Sub message.



The output includes information such as package type, vulnerability severity, CVSS score, and information on fixes, if available.

## What's next

  * [Learn more metadata filtering options](https://docs.cloud.google.com/artifact-analysis/docs/os-scanning-automatically#viewing_vulnerability_occurrences).
  * [Run a manual scan on-demand](https://docs.cloud.google.com/artifact-analysis/docs/quickstart-scanning-os-manually).
  * [Learn best practices to protect your software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
