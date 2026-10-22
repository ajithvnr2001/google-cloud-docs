---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/verify-image-provenance/
title: Verify image provenance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:58.593625+00:00
---

# Verify image provenance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/verify-image-provenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Verify image provenance Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

You can verify SLSA (Supply-chain Levels for Software Artifacts) build provenance attestations for your custom OS images to ensure software supply chain integrity.

When you configure your Image Builder pipeline to output to Artifact Registry and enable verification options, Cloud Build automatically generates a cryptographic attestation describing the exact pipeline source code, configurations, execution parameters, and base image used during compilation. Verifying this build provenance confirms that trusted pipelines built your images securely without unauthorized tampering.

## Before you begin

  * Complete the environment setup steps in [Prepare your environment](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required roles

To get the permissions that you need to view and verify build provenance attestations, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`)
  * [Cloud Build Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.viewer) (`roles/cloudbuild.builds.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure provenance generation

To generate build provenance, ensure that you configure the `substitutions`, `options`, `results`, and `artifacts` blocks in your [`cloudbuild.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema) file as shown in the following snippet:
    
    
    substitutions:
      # 1. Specify your output path and target Artifact Registry resource URI
      _IMAGE_OUTPUT_PATH: 'image-builder/binaryOut'
      _ARTIFACT_REGISTRY_RESOURCE_URI: 'projects/PROJECT_ID/locations/REGION/repositories/REPOSITORY_NAME/packages/PACKAGE_NAME/versions/v${BUILD_ID}'
    
    steps:
      # 2. Configure step results and base image attestations
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/builder:stable'
        script: |
          #!/usr/bin/env bash
          /build
        id: 'imagebuilder-customize'
        results:
          - name: image_builder_telemetry_metrics
          - name: base_image
            attestationType: "https://cloudbuild.googleapis.com/attestations/build_content_restrictions"
            attestationContent: base_image
    
    options:
      # 3. Enable Cloud Logging and cryptographic provenance generation
      logging: CLOUD_LOGGING_ONLY
      requestedVerifyOption: VERIFIED
    
    artifacts:
      # 4. Upload generic image artifacts and provenance to Artifact Registry
      generic_artifacts:
        - folder: '${_IMAGE_OUTPUT_PATH}'
          registry_path: '${_ARTIFACT_REGISTRY_RESOURCE_URI}'
    

## Verify provenance data

You can view and verify build provenance data and execution artifacts by using either the Google Cloud console or the Google Cloud CLI:

###  Console (Cloud Build) 

To view build provenance and output artifacts through Cloud Build build history:

  1. In the Google Cloud console, go to the **Cloud Build** page.

[Go to Cloud Build](https://console.cloud.google.com/cloud-build/builds)

  2. Click **History** and select the **Build ID** for your image pipeline run. The build details page displays logs for the three process steps (`imagebuilder-customize`, `imagebuilder-validate`, and `imagebuilder-publish`).

  3. Click the **Build Artifacts** tab to view the exact OS image created during execution.

**Note:** The **Build Artifacts** tab appears only if you configure an Artifact Registry repository. Click the artifact link to open your package in the generic repository in Artifact Registry.
  4. Click the **Attachments** tab to view the signed SLSA provenance attestation files and results files. The results file records the source base image used during execution.




###  Console (Artifact Registry) 

To view build provenance directly in Artifact Registry:

  1. In the Google Cloud console, go to the **Artifact Registry** page.

[Go to Artifact Registry](https://console.cloud.google.com/artifacts)

  2. In the repositories list, click the name of your generic repository.

  3. In the package list, click your OS image package name.

  4. In the version history list, click the version ID (`v${BUILD_ID}`) for your pipeline run.

  5. Click the **Attachments** tab to view the signed SLSA provenance attestation files and results files for that image version. The results file records the base source image used during execution.




###  gcloud 

Artifact Registry stores provenance records as attachment files alongside the generic image tarballs.

Because the attestation is formatted as a Dead Simple Signing Envelope (DSSE), the actual provenance statement payload inside the JSON is base64-encoded. To read the details, perform the following steps using the gcloud CLI and `jq` utility:

  1. List the versions of your package to locate the specific build ID version that you want to verify by running the [`gcloud artifacts versions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/versions/list):
         
         gcloud artifacts versions list \
             --package=PACKAGE_NAME \
             --repository=REPOSITORY_NAME \
             --location=REPOSITORY_LOCATION \
             --project=PROJECT_ID
         

Replace the following:

     * `PACKAGE_NAME`: the name of the package in your Artifact Registry repository, for example, `my-custom-image`.
     * `REPOSITORY_NAME`: the name of your generic Artifact Registry repository, for example, `custom-os-images`.
     * `REPOSITORY_LOCATION`: the region of your repository, for example, `us-central1`.
     * `PROJECT_ID`: your project ID.
  2. Query the attachments metadata matching the target package version by running the [`gcloud artifacts attachments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/attachments/list):
         
         gcloud artifacts attachments list \
             --target=projects/PROJECT_ID/locations/REPOSITORY_LOCATION/repositories/REPOSITORY_NAME/packages/PACKAGE_NAME/versions/vBUILD_ID \
             --repository=REPOSITORY_NAME \
             --location=REPOSITORY_LOCATION \
             --project=PROJECT_ID
         

Replace `BUILD_ID` with the version identifier returned in step 1, for example, `12345`.

From the command output, locate the attachment entry whose `name` field contains `build-result` (with `type: application/vnd.in-toto+json`), and copy the path listed under `files:`, for example:

`projects/PROJECT_ID/locations/REPOSITORY_LOCATION/repositories/REPOSITORY_NAME/files/sha256:SHA256_HASH`

  3. Download the JSON metadata attachment payload from your repository by running the [`gcloud artifacts files download` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/download):
         
         gcloud artifacts files download ATTACHMENT_FILE_ID \
             --repository=REPOSITORY_NAME \
             --location=REPOSITORY_LOCATION \
             --project=PROJECT_ID \
             --destination=./provenance.json
         

Replace `ATTACHMENT_FILE_ID` with the `files:` attachment path retrieved in the previous step.

  4. Run the following command to isolate, base64-decode, and format the JSON payload contents:
         
         cat ./provenance.json | jq -r '.payload' | base64 --decode | jq
         

The output contains standard SLSA format parameters highlighting the build trigger, recipe repository details, container images used, build hashes, and base image attributes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
