---
url: https://docs.cloud.google.com/artifact-analysis/docs/view-vex/
title: View VEX status \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:04.982830+00:00
---

# View VEX status  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/view-vex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  View VEX status Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to view the [Vulnerability Exploitability eXchange (VEX)](https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf) statements stored in Artifact Analysis and filter vulnerabilities using VEX status.

Security and policy enforcers can use these features to prioritize among security issue mitigation tasks. You can also use VEX data to attest to the composition of your artifacts to help your organization meet regulatory requirements.

## Required roles

To get the permissions that you need to upload VEX assessments and check the VEX status of vulnerabilities, ask your administrator to grant you the following IAM roles on the project: 

  * To view vulnerability occurrences: [Container Analysis Occurrences Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.occurrences.viewer) (`roles/containeranalysis.occurrences.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View VEX status in the Google Cloud console

To view VEX information for container images stored in Artifact Registry:

  1. Open the Artifact Registry **Repositories** page.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

The page displays a list of your repositories.

  2. In the repositories list, click a repository name.

  3. In the images list, click an image name.

A list of the image digests opens.

  4. In the digests list, click a digest name.

A digest details page opens with a row of tabs. By default, the **Overview** tab is open.

  5. In the row of tabs, select the **Vulnerabilities** tab.

The page displays a **Scan results** overview with a **VEX Status** section.

The **VEX Status** summary section displays the number of packages that are categorized by each VEX status type. To see all packages with a specific VEX status, click the number beside the status type.

The **Vulnerabilities** tab also displays the VEX status for each package is in the vulnerabilities list.

To filter the vulnerabilities list:

     1. Above the vulnerabilities list, click **Filter vulnerabilities**.
     2. Choose a filter from the filter list.
     3. Specify the value that you want to use for filtering the list.



### View VEX status in Cloud Build

If you're using Cloud Build, you can also view VEX information in the **Security insights** side panel within the Google Cloud console.

If you're using Cloud Build, you can view image metadata in the **Security insights** side panel within the Google Cloud console.

The **Security insights** side panel provides a high-level overview of build security information for artifacts stored in Artifact Registry. To learn more about the side panel and how you can use Cloud Build to help protect your software supply chain, see [View build security insights](https://docs.cloud.google.com/build/docs/view-build-security-insights).

## View using the gcloud CLI

The following section explains how to retrieve VEX information and apply filters to limit results based on your needs.

### View VEX info for a single artifact

To view uploaded VEX info, you can query the API and list notes with the note type `VULNERABILITY_ASSESSMENT`.

Use the following API call to request all of the vulnerability assessment notes for the specified artifact:
    
    
    curl -G -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data-urlencode "filter=(kind=\"VULNERABILITY_ASSESSMENT\" AND vulnerability_assessment.product.generic_uri=\"https://LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_NAME@DIGEST\"" https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/notes
    

Where

  * LOCATION is the region or multi-regional location of your repository.
  * PROJECT_ID is the ID for the Google Cloud project where your image is stored in an Artifact Registry repository.
  * REPO_NAME is the name of the Artifact Registry repository that contains the image.
  * IMAGE_NAME is the name of the image.
  * DIGEST is the image digest, a string starting with `sha256:`.



### Filter vulnerabilities by VEX status

Using gcloud, you can filter vulnerability metadata by VEX status. Artifact Analysis filters based on the status stored in each [Grafeas vulnerability occurrence](https://github.com/grafeas/grafeas/blob/master/proto/v1/vulnerability.proto#L257).

Run the following command to filter vulnerability occurrences based on a specified VEX status:
    
    
    gcloud artifacts vulnerabilities list RESOURCE_URI \
        --occurrence-filter="vulnDetails.vex_assessment.state=\"STATUS\""
    

Where

  * RESOURCE_URI is the complete URL of the image, similar to https://LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_ID@sha256:HASH.
  * STATUS is the VEX status to filter for, which can be one of the following values: `known_affected`, `known_not_affected`, `under_investigation`, or `fixed`.



For example, run the following command to filter for vulnerability occurrences with the VEX status `AFFECTED`:
    
    
    gcloud artifacts vulnerabilities list RESOURCE_URI \
        --occurrence-filter="vulnDetails.vex_assessment.state=\"AFFECTED\""
    

### List vulnerabilities without VEX

To identify which vulnerabilities don't yet have any VEX information associated with them, use the following gcloud command:
    
    
    gcloud artifacts vulnerabilities list /
        LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_NAME@DIGEST /--occurrence-filter="isNull(vulnDetails.vex_assessment.state)"
    

Where

  * LOCATION is the region or multi-regional location of your repository.
  * PROJECT_ID is the ID for the Google Cloud project where your image is stored in an Artifact Registry repository.
  * REPO_NAME is the name of the Artifact Registry repository that contains the image.
  * IMAGE_NAME is the name of the image.
  * DIGEST is the image digest, a string starting with `sha256:`.



## Limitations

  * Uploading VEX statements is only supported for container images.
  * Uploaded VEX statements can't be exported into CSAF, OpenVex, or SPDX standards.



## What's next

  * [Learn about SBOMs](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview).
  * [Scan for vulnerabilities](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) with Artifact Analysis.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
