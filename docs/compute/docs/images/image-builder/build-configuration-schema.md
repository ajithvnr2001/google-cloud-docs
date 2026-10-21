---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema/
title: Cloud Build configuration file \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:21:58.123632+00:00
---

# Cloud Build configuration file  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Cloud Build configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

This document describes the structure and parameters of the Cloud Build configuration file (`cloudbuild.yaml`) that's used to orchestrate the steps of the Image Builder pipeline: parsing, building, validation, and release publishing.

## Schema overview

A standard Image Builder `cloudbuild.yaml` file follows the [standard Cloud Build configuration file structure](https://docs.cloud.google.com/build/docs/build-config-file-schema) and orchestrates three sequential container build steps: `/build`, `/validate`, and `/publish`.
    
    
    substitutions:
      _GCS_WORKDIR: 'gs://BUCKET_NAME/workdir/'
      _IMAGE_BUILDER_CONFIG_PATH: 'imagebuilder.yaml'
      _SERVICE_ACCOUNT: 'projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL'
      _IMAGE_OUTPUT_PATH: 'image-builder/binaryOut'
      _ARTIFACT_REGISTRY_RESOURCE_URI: 'projects/PROJECT_ID/locations/REGION/repositories/REPOSITORY_NAME/packages/PACKAGE_NAME/versions/v${BUILD_ID}'
    
    steps:
      # Step 1: Parse configs and run OS customization on the worker VM
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
    
      # Step 2: Validate by running system boot checks on the test VM
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/validator:stable'
        script: |
          #!/usr/bin/env bash
          /validate
        id: 'imagebuilder-validate'
        results:
          - name: image_builder_telemetry_metrics
    
      # Step 3: Register OS image and publish tar file to Artifact Registry
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/builder:stable'
        script: |
          #!/usr/bin/env bash
          /publish
        id: 'imagebuilder-publish'
        results:
          - name: image_builder_telemetry_metrics
    
    options:
      automapSubstitutions: true
      requestedVerifyOption: VERIFIED
      substitutionOption: ALLOW_LOOSE
      dynamicSubstitutions: true
      logging: CLOUD_LOGGING_ONLY
    
    artifacts:
      generic_artifacts:
        - folder: '${_IMAGE_OUTPUT_PATH}'
          registry_path: '${_ARTIFACT_REGISTRY_RESOURCE_URI}'
    
    timeout: '3600s'

## Substitution variables

The `cloudbuild.yaml` file uses the following substitution variables to map directly to environment variables for execution:
    
    
    substitutions:
      _GCS_WORKDIR: 'gs://BUCKET_NAME/workdir/'
      _IMAGE_BUILDER_CONFIG_PATH: 'imagebuilder.yaml'
      _SERVICE_ACCOUNT: 'projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL'
      _IMAGE_OUTPUT_PATH: 'image-builder/binaryOut'
      _ARTIFACT_REGISTRY_RESOURCE_URI: 'projects/PROJECT_ID/locations/REGION/repositories/REPOSITORY_NAME/packages/PACKAGE_NAME/versions/v${BUILD_ID}'

  * `_GCS_WORKDIR`: The regional Cloud Storage path used as a temporary staging location for artifacts like serial logs, temporary image archives, and guest execution histories. The bucket must already exist.
  * `_IMAGE_BUILDER_CONFIG_PATH`: The path to your `imagebuilder.yaml` customization recipe. This can be a remote Cloud Storage path (for example, `gs://BUCKET_NAME/imagebuilder.yaml`), or a relative path in your workspace or GitHub repository depending on the source.

**Note:** If fetching the configuration file from a remote Cloud Storage location, the object size must not exceed 1 MB.
  * `_SERVICE_ACCOUNT`: The full Identity and Access Management (IAM) resource name of the [service account configured to run the build](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#service-account) and authorize orchestrator steps.

  * `_IMAGE_OUTPUT_PATH`: The output path of the exported tar file inside the Cloud Build `/workspace/` directory.

  * `_ARTIFACT_REGISTRY_RESOURCE_URI` (Optional): The resource URI for the generic repository in Artifact Registry. If provided, the pipeline pushes the generated immutable image tar file and generates attestations at this location.




## Steps

Image Builder runs three distinct container steps in sequence to orchestrate your OS image build. Replace `REGION` in the container image path with the target Google Cloud region where you set up your pipelines, such as `us-central1`, `europe-west1`, or `asia-east1`:
    
    
    steps:
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/builder:stable'
        script: |
          #!/usr/bin/env bash
          /build
        id: 'imagebuilder-customize'
    
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/validator:stable'
        script: |
          #!/usr/bin/env bash
          /validate
        id: 'imagebuilder-validate'
    
      - name: 'REGION-docker.pkg.dev/image-builder-official/release/builder:stable'
        script: |
          #!/usr/bin/env bash
          /publish
        id: 'imagebuilder-publish'

### Telemetry and step ID requirements

The orchestrator container identifies and tracks the progression of each build phase—customization, validation, and publishing—by reading the `id` field of each step in your `cloudbuild.yaml` file.

Step IDs must begin with the `imagebuilder-` prefix, such as `imagebuilder-customize`, `imagebuilder-validate`, and `imagebuilder-publish`, to enable Image Builder to collect service-specific telemetry metrics.

When you include `image_builder_telemetry_metrics` in the `results` block of each step, Image Builder securely collects high-level pipeline execution metrics to monitor and track service reliability as follows:

  * Build execution and status: Success or failure status and completion duration for each build step and customization action.
  * Environment details: The Compute Engine machine type, zone, and container version tag used during execution.
  * Image metadata: Base OS distribution, version, and configured guest OS features.
  * Validation test results: Pass, fail, or skipped status of automated system validation tests, such as VM boot, Secure Boot, block storage health, guest agent status, and network driver binding.



### Customization step

The customization step validates the schema of `imagebuilder.yaml`, checks IAM permissions, launches the worker VM instance, mounts the customization binary disk, runs the customization provisioner, and securely exports the boot disk partition.

  * **Container image** : `us-central1-docker.pkg.dev/image-builder-official/release/builder:stable`
  * **Script command** : `/build`
  * **Results sub-block** : 
    * `image_builder_telemetry_metrics`: Collects customization build execution metrics.
    * `base_image` (Optional): Records base source image details in build attestation metadata when you specify an Artifact Registry generic repository destination. Set `attestationType: "https://cloudbuild.googleapis.com/attestations/build_content_restrictions"` to create a verifiable record of your image's origins.



### Validation step

The validation step boots a temporary test VM from the customized OS image and runs active automated validation test suites.

  * **Container image** : `us-central1-docker.pkg.dev/image-builder-official/release/validator:stable`
  * **Script command** : `/validate`
  * **Results sub-block** : `image_builder_telemetry_metrics` collects validation testing execution metrics.



### Publishing step

The publishing step registers the final OS image, deletes temporary intermediate disks, uploads the tar file payload to Artifact Registry if configured, and writes out Supply Chain Levels for Software Artifacts (SLSA) provenance records.

  * **Container image** : `us-central1-docker.pkg.dev/image-builder-official/release/builder:stable`
  * **Script command** : `/publish`
  * **Results sub-block** : `image_builder_telemetry_metrics` collects publishing release execution metrics.



## Options

The options flags define execution settings on the Cloud Build server. You must configure the following options:
    
    
    options:
      automapSubstitutions: true
      requestedVerifyOption: VERIFIED
      substitutionOption: ALLOW_LOOSE
      dynamicSubstitutions: true
      logging: CLOUD_LOGGING_ONLY
    

For more information about these settings, see [Options in the Cloud Build configuration file](https://docs.cloud.google.com/build/docs/build-config-file-schema#options).

  * `automapSubstitutions`: Set to `true` to ensure substitution variables are mapped into the container environment.
  * `requestedVerifyOption`: Set to `VERIFIED`. This setting instructs Cloud Build to automatically generate SLSA build provenance attestations. This provenance provides cryptographic verification that the image was built exactly as defined in your pipeline, helping prevent tampering and ensuring software supply chain integrity.
  * `substitutionOption`: Set to `ALLOW_LOOSE`. This setting is required to force Cloud Build to ignore dynamic parameters or unused script arguments.
  * `dynamicSubstitutions`: Set to `true` to allow system evaluation variables, like `${BUILD_ID}`, to resolve correctly.
  * `logging`: Set to `CLOUD_LOGGING_ONLY` to restrict build logs strictly to Cloud Logging.



## Artifacts

Configure the `artifacts` block when you export image archives and attestations to Artifact Registry:
    
    
    artifacts:
      generic_artifacts:
        - folder: '${_IMAGE_OUTPUT_PATH}'
          registry_path: '${_ARTIFACT_REGISTRY_RESOURCE_URI}'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
