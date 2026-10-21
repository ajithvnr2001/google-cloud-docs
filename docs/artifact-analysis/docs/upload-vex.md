---
url: https://docs.cloud.google.com/artifact-analysis/docs/upload-vex/
title: Upload VEX statements \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:43.915836+00:00
---

# Upload VEX statements  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/upload-vex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Upload VEX statements Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to upload existing [Vulnerability Exploitability eXchange (VEX)](https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf) statements to Artifact Analysis. You can also upload statements provided by other publishers.

VEX statements must be formatted according to the [Common Security Advisory Format (CSAF)](https://oasis-open.github.io/csaf-documentation/) 2.0 standard in JSON.

## Required roles

To get the permissions that you need to upload VEX assessments and check the VEX status of vulnerabilities, ask your administrator to grant you the following IAM roles on the project: 

  * To create and update notes: [Container Analysis Notes Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Upload VEX statements

Run the [`artifacts vulnerabilities load-vex`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/vulnerabilities/load-vex) command to upload VEX data and store it in Artifact Analysis:
    
    
    gcloud artifacts vulnerabilities load-vex /
        --source CSAF_SOURCE /
        --uri RESOURCE_URI /
    

Where

  * CSAF_SOURCE is the path to your VEX statement file stored locally. The file must be a JSON file following the [CSAF schema](https://github.com/oasis-tcs/csaf/blob/master/csaf_2.0/json_schema/csaf_json_schema.json).
  * RESOURCE_URI can be one of: 
    * the complete URL of the image, similar to `https://LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_ID@sha256:HASH`.
    * the image URL, similar to `https://LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_ID`.



Artifact Analysis converts your VEX statements to [Grafeas `VulnerabilityAssessment`](https://github.com/grafeas/grafeas/blob/master/proto/v1/vex.proto#L28) notes.

Artifact Analysis stores vulnerability assessment notes as one note per CVE. Notes are stored in the Container Analysis API, within the same project as the specified image.

When you upload VEX statements, Artifact Analysis also carries VEX status information into associated [vulnerability occurrences](https://docs.cloud.google.com/artifact-analysis/docs/metadata-storage#occurrence) so that you can filter vulnerabilities by VEX status. If a VEX statement is applied to an image, Artifact Analysis will carry over the VEX status to all versions of that image, including newly pushed versions.

If a single version has two VEX statements, one written for the resource URL and one written for the associated image URL, the VEX statement written for the resource URL will take precedence and will be carried over to the vulnerability occurrence.

## What's next

  * Prioritize vulnerability issues using VEX. Learn how to [view VEX statements](https://docs.cloud.google.com/artifact-analysis/docs/view-vex) and filter vulnerabilities by their VEX status.
  * Learn how to [generate a software bill of materials](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview) (SBOM) to support compliance requirements.
  * [Scan for vulnerabilities](https://docs.cloud.google.com/artifact-analysis/docs/scanning-types) in OS packages and language packages with Artifact Analysis.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
